/**
 * TSSKB 认证核心：登录、会话读写、退出。
 * 会话保存在 localStorage，并同步一个 tsskb_auth cookie，
 * 便于将来在反向代理层（nginx auth）做服务端强校验。
 */
(function () {
  "use strict";

  var SALT = "tsskb-auth-v1";
  var SESSION_KEY = "tsskb_session";
  var COOKIE_NAME = "tsskb_auth";

  /* 纯 JS SHA-256 后备：http 内网地址不是安全上下文，crypto.subtle 不可用 */
  var SHA256_K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
  ];

  function sha256BytesJs(bytes) {
    function rotr(x, n) {
      return (x >>> n) | (x << (32 - n));
    }
    var H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19];
    var bitLen = bytes.length * 8;
    var totalLen = bytes.length + 9 + ((((55 - bytes.length) % 64) + 64) % 64);
    var m = new Uint8Array(totalLen);
    m.set(bytes);
    m[bytes.length] = 0x80;
    var dv = new DataView(m.buffer);
    dv.setUint32(totalLen - 8, Math.floor(bitLen / 4294967296), false);
    dv.setUint32(totalLen - 4, bitLen >>> 0, false);
    var w = new Uint32Array(64);
    for (var i = 0; i < totalLen; i += 64) {
      for (var t = 0; t < 16; t++) w[t] = dv.getUint32(i + t * 4, false);
      for (t = 16; t < 64; t++) {
        var s0 = rotr(w[t - 15], 7) ^ rotr(w[t - 15], 18) ^ (w[t - 15] >>> 3);
        var s1 = rotr(w[t - 2], 17) ^ rotr(w[t - 2], 19) ^ (w[t - 2] >>> 10);
        w[t] = (w[t - 16] + s0 + w[t - 7] + s1) >>> 0;
      }
      var a = H[0], b = H[1], c = H[2], d = H[3], e = H[4], f = H[5], g = H[6], h = H[7];
      for (t = 0; t < 64; t++) {
        var S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25);
        var ch = (e & f) ^ (~e & g);
        var temp1 = (h + S1 + ch + SHA256_K[t] + w[t]) >>> 0;
        var S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22);
        var maj = (a & b) ^ (a & c) ^ (b & c);
        var temp2 = (S0 + maj) >>> 0;
        h = g; g = f; f = e; e = (d + temp1) >>> 0;
        d = c; c = b; b = a; a = (temp1 + temp2) >>> 0;
      }
      H[0] = (H[0] + a) >>> 0; H[1] = (H[1] + b) >>> 0; H[2] = (H[2] + c) >>> 0; H[3] = (H[3] + d) >>> 0;
      H[4] = (H[4] + e) >>> 0; H[5] = (H[5] + f) >>> 0; H[6] = (H[6] + g) >>> 0; H[7] = (H[7] + h) >>> 0;
    }
    return H.map(function (x) {
      return ("00000000" + x.toString(16)).slice(-8);
    }).join("");
  }

  function sha256Hex(text) {
    if (window.isSecureContext && window.crypto && window.crypto.subtle) {
      return crypto.subtle
        .digest("SHA-256", new TextEncoder().encode(text))
        .then(function (buf) {
          return Array.prototype.map
            .call(new Uint8Array(buf), function (b) {
              return b.toString(16).padStart(2, "0");
            })
            .join("");
        });
    }
    return Promise.resolve(sha256BytesJs(new TextEncoder().encode(text)));
  }

  function setCookie(name, value, maxAgeSeconds) {
    document.cookie =
      name + "=" + value + "; Path=/; Max-Age=" + maxAgeSeconds + "; SameSite=Lax";
  }

  function login(username, password) {
    var cfg = window.TSSKB_AUTH || {};
    var ttlMs = (cfg.sessionTtlHours || 12) * 3600 * 1000;

    var userPromise;
    if (cfg.mode === "remote") {
      userPromise = fetch(cfg.remoteAuthUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username, password: password }),
      }).then(function (res) {
        if (!res.ok) {
          var err = new Error("AUTH_FAILED");
          err.code = "AUTH_FAILED";
          throw err;
        }
        return res.json();
      });
    } else {
      userPromise = (function () {
        var users = cfg.users || [];
        var found = null;
        for (var i = 0; i < users.length; i++) {
          if (users[i].username === username) {
            found = users[i];
            break;
          }
        }
        if (!found) {
          return Promise.reject({ code: "AUTH_FAILED" });
        }
        return sha256Hex(SALT + ":" + password).then(function (hex) {
          var expected = (found.passwordHash || "").replace(/^sha256:/, "");
          if (hex !== expected) {
            throw { code: "AUTH_FAILED" };
          }
          return {
            username: found.username,
            displayName: found.displayName || found.username,
            role: found.role || "user",
          };
        });
      })();
    }

    return userPromise.then(function (user) {
      var session = { user: user, exp: Date.now() + ttlMs };
      localStorage.setItem(SESSION_KEY, JSON.stringify(session));
      setCookie(COOKIE_NAME, "1", Math.floor(ttlMs / 1000));
      return user;
    });
  }

  function logout() {
    localStorage.removeItem(SESSION_KEY);
    setCookie(COOKIE_NAME, "", 0);
  }

  function getSession() {
    var raw = null;
    try {
      raw = localStorage.getItem(SESSION_KEY);
    } catch (err) {
      return null;
    }
    if (!raw) return null;
    try {
      var session = JSON.parse(raw);
      if (!session || !session.user || typeof session.exp !== "number") {
        logout();
        return null;
      }
      if (Date.now() > session.exp) {
        logout();
        return null;
      }
      return session;
    } catch (err) {
      logout();
      return null;
    }
  }

  function isAuthed() {
    return getSession() !== null;
  }

  window.TSSKB = window.TSSKB || {};
  window.TSSKB.auth = {
    login: login,
    logout: logout,
    getSession: getSession,
    isAuthed: isAuthed,
  };
})();
