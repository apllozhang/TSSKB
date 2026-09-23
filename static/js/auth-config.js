/**
 * TSSKB 登录门配置。
 *
 * mode = "local"  : 使用下方 users 列表做本地校验（密码仅存加盐 SHA-256 摘要，
 *                   哈希可用 tools/gen_auth_hash.py 生成）。
 * mode = "remote" : 改为调用 remoteAuthUrl（POST {username,password}，
 *                   2xx 即视为登录成功，响应体作为用户信息）。
 */
window.TSSKB_AUTH = {
  mode: "local",
  sessionTtlHours: 12,
  users: [
    {
      username: "aletss",
      displayName: "ALE TSS",
      role: "admin",
      passwordHash: "sha256:008bf9fd63e1d5dd21f094c5634b64f2b4099b07e8ebaaf2f2c3f35d6e14f522",
    },
  ],
  remoteAuthUrl: "",
};
