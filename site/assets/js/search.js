(() => {
  const roots = Array.from(document.querySelectorAll("[data-search]"));
  if (!roots.length) return;

  const worker = new Worker("/assets/js/search-worker.js");
  let manifestPromise;
  let titlePromise;
  const shards = new Map();
  const pending = new Map();
  let requestId = 0;

  const escapeHtml = (value) => {
    const node = document.createElement("span");
    node.textContent = value;
    return node.innerHTML;
  };

  const manifest = () => manifestPromise ||= fetch("/search/manifest.json").then((response) => {
    if (!response.ok) throw new Error(`search manifest ${response.status}`);
    return response.json();
  });
  const titles = () => titlePromise ||= fetch("/search/titles.json").then((response) => {
    if (!response.ok) throw new Error(`title index ${response.status}`);
    return response.json();
  });

  async function entriesFor(query) {
    const [meta, titleRows] = await Promise.all([manifest(), titles()]);
    const q = query.toLocaleLowerCase();
    const candidates = new Set(
      titleRows.filter((row) => `${row.t} ${row.s}`.toLocaleLowerCase().includes(q)).map((row) => row.c),
    );
    const selected = candidates.size ? meta.shards.filter((shard) => candidates.has(shard.category)) : meta.shards;
    await Promise.all(selected.map(async (shard) => {
      if (!shards.has(shard.id)) {
        shards.set(shard.id, fetch(`/${shard.url}`).then((response) => response.json()));
      }
      await shards.get(shard.id);
    }));
    const rows = await Promise.all(selected.map((shard) => shards.get(shard.id)));
    return rows.flat();
  }

  worker.addEventListener("message", (event) => {
    const target = pending.get(event.data.requestId);
    if (!target) return;
    pending.delete(event.data.requestId);
    const html = event.data.results.map((entry) => {
      const anchor = entry.a ? `#${encodeURIComponent(entry.a)}` : "";
      return `<a class="search-result" role="option" href="/${entry.u}${anchor}"><b>${escapeHtml(entry.s)}</b><small>${escapeHtml(entry.t)}</small></a>`;
    }).join("");
    target.innerHTML = html || '<span class="search-state">没有匹配结果</span>';
  });

  roots.forEach((root) => {
    const input = root.querySelector("[data-search-input]");
    const results = root.querySelector("[data-search-results]");
    let timer;
    input.addEventListener("input", () => {
      window.clearTimeout(timer);
      const query = input.value.trim();
      if (query.length < 2) {
        results.innerHTML = "";
        return;
      }
      results.innerHTML = '<span class="search-state">正在检索…</span>';
      timer = window.setTimeout(async () => {
        try {
          const id = ++requestId;
          pending.set(id, results);
          worker.postMessage({ requestId: id, query, entries: await entriesFor(query) });
        } catch (error) {
          results.innerHTML = '<span class="search-state">搜索暂时不可用</span>';
          console.error("TSSKB search failed", error);
        }
      }, 120);
    });
  });
})();
