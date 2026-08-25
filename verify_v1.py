# -*- coding: utf-8 -*-
"""V1 原文真实性核对 v2：特征词命中率匹配（摘录为转写压缩，不能逐字匹配）"""
import re, json, sys
from pathlib import Path

STOP = set("the a an of to in and or for with on by is are be as at from this that it its can will not use used using when which all any each per via only page type mode".split())

def load_pages(fulltext):
    pages, cur, buf = {}, None, []
    for line in fulltext.split("\n"):
        m = re.match(r"^<<<PAGE (\d+)>>>", line)
        if m:
            if cur: pages[cur] = " ".join(buf)
            cur, buf = int(m.group(1)), []
        else:
            buf.append(line)
    if cur: pages[cur] = " ".join(buf)
    return pages

def words(s):
    return [w for w in re.findall(r"[a-zA-Z0-9][a-zA-Z0-9./_-]{3,}", s.lower()) if w not in STOP]

def check_book(base):
    bdir = Path(base)
    pages = load_pages((bdir / "fulltext.md").read_text(encoding="utf-8"))
    report = {}
    for f in sorted((bdir / "candidates").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        cat = f.stem
        # 条目分隔：glossary 为编号行；其他为 ## 标题或顶格数字编号
        if cat == "glossary":
            entries = re.split(r"\n(?=\d+\.\s+\*\*|- \*\*)", text)
        else:
            entries = re.split(r"\n(?=## |### |\d+\.\s+\S|- \*\*)", text)
        results = []
        for e in entries:
            if not e.strip() or e.startswith("# "): continue
            raw = re.findall(r"<<<PAGE (\d+)(?:-(\d+))?", e)
            pnums = []
            for a, b in raw:
                a = int(a)
                if b:
                    pnums.extend(range(a, min(int(b), a + 24) + 1))
                else:
                    pnums.append(a)
            if not pnums: continue
            quotes = re.findall(r"原文摘录：\"(.*?)\"", e, re.S) or re.findall(r"\"([^\"\\]{25,})\"", e)
            qs = " ".join(quotes) if quotes else e
            ws = words(qs)
            if not ws:
                results.append({"h": "n/a", "ok": True}); continue
            # 页面文本：声称页 ±1 容忍
            ptext = " ".join(pages.get(p, "") for p in set(pnums + [p+1 for p in pnums] + [p-1 for p in pnums]))
            pw = set(words(ptext))
            hit = sum(1 for w in ws if w in pw)
            ratio = hit / len(ws)
            results.append({"h": round(ratio, 2), "ok": ratio >= 0.35, "head": e.split("\n")[0][:70]})
        report[cat] = results
    (bdir / "v1_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"== {base.split('/')[-1]} ==")
    for cat, rs in report.items():
        ok = sum(1 for r in rs if r["ok"])
        print(f"  {cat}: {len(rs)} 条, V1通过 {ok}, 淘汰 {len(rs)-ok}")

for slug in sys.argv[1:]:
    check_book(f"D:/Claude code/TSSKB/books/{slug}")
