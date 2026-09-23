const normalized = (value) => String(value || "").toLocaleLowerCase();

self.addEventListener("message", (event) => {
  const { query, entries, requestId } = event.data;
  const q = normalized(query);
  const results = [];
  for (const entry of entries) {
    let score = 0;
    if (normalized(entry.t).includes(q)) score += 12;
    if (normalized(entry.s).includes(q)) score += 9;
    if (normalized(entry.x).includes(q)) score += 3;
    if (score) results.push({ score, ...entry });
  }
  results.sort((left, right) => right.score - left.score || left.t.localeCompare(right.t));
  self.postMessage({ requestId, results: results.slice(0, 20) });
});
