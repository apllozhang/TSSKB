# -*- coding: utf-8 -*-
"""从 candidates + v1_report 生成 verified.md 和 rejected/<cat>.md
override_keep：V1 特征词误判但内容核心、人工判保留的条目头部关键字
override_drop：V1 通过但人工判 V2/V3 弱、需淘汰的条目头部关键字
"""
import re, json, sys
from pathlib import Path

KEEP = {
    "smb-express-lan-wlan": ["16. **Wi-Fi Express"],
}
DROP = {
    # V1 通过但空洞/通用，人工淘汰（暂无）
}

def split_entries(text, cat):
    if cat == "glossary":
        return re.split(r"\n(?=\d+\.\s+\*\*)", text)
    return re.split(r"\n(?=## |### |\d+\.\s+\S)", text)

def gen(slug):
    bdir = Path(f"D:/Claude code/TSSKB/books/{slug}")
    rep = json.load(open(bdir / "v1_report.json", encoding="utf-8"))
    (bdir / "rejected").mkdir(exist_ok=True)
    ver_parts, rej_parts = [], []
    stats = {}
    for f in sorted((bdir / "candidates").glob("*.md")):
        cat = f.stem
        if cat not in rep or not rep[cat]:
            # 无报告的类别（如 T311 无 glossary）——整体收录
            text = f.read_text(encoding="utf-8")
            body = re.sub(r"^# .*\n+", "", text).strip()
            ver_parts.append(f"## {cat}\n\n{body}\n")
            stats[cat] = [len(split_entries(text, cat)) - (1 if text.startswith('# ') else 0), 0]
            continue
        text = f.read_text(encoding="utf-8")
        if cat in rep and rep[cat]:
            rs = [r for r in rep[cat]]
        else:
            rs = []
        entries = split_entries(text, cat)
        # 对齐：entries[0] 可能是标题头
        eidx = 0
        if entries and not re.search(r"<<<PAGE \d+>>>", entries[0]):
            eidx = 1
        keep, drop = [], []
        for r in rs:
            if eidx >= len(entries): break
            e = entries[eidx]; eidx += 1
            head = e.split("\n")[0][:40]
            keep_flag = r.get("ok", True)
            if slug in KEEP and any(head.startswith(k) for k in KEEP[slug]):
                keep_flag = True
            if slug in DROP and any(head.startswith(k) for k in DROP[slug]):
                keep_flag = False
            (keep if keep_flag else drop).append(e)
        # 未对齐的剩余条目全部保留
        keep.extend(entries[eidx:])
        if keep:
            ver_parts.append(f"## {cat}\n\n" + "\n".join(x.strip() for x in keep if x.strip()) + "\n")
        if drop:
            rej_parts.append(f"## {cat}\n\n" + "\n---\n".join(x.strip() for x in drop) + "\n")
        stats[cat] = [len(keep), len(drop)]
    (bdir / "verified.md").write_text(
        "# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）\n\n" + "\n".join(ver_parts),
        encoding="utf-8")
    if rej_parts:
        (bdir / "rejected" / "v1-v3.md").write_text("# 淘汰条目及原因\n\n" + "\n".join(rej_parts), encoding="utf-8")
    print(f"== {slug} ==")
    for cat, (k, d) in stats.items():
        print(f"  {cat}: 保留 {k} / 淘汰 {d}")

for slug in sys.argv[1:]:
    gen(slug)
