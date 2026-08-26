# -*- coding: utf-8 -*-
"""按 fulltext.md 中各机型 'Front Panel' 小节标题定位 PDF 页，整页渲染面板图并生成 GALLERY.md"""
import os, re
import fitz

SRC = r"D:/AOS 8.10 R04 Complete User Guides"
BOOKS = {
    "hw-6465":  ("Omniswitch 6465 Hardware Guide-rev V.pdf",  "6465"),
    "hw-6560":  ("Omniswitch 6560 Hardware Guide rev P.pdf",  "6560"),
    "hw-6570":  ("Omniswitch 6570 Hardware Guide rev G.pdf",  "6570"),
    "hw-6575":  ("Omniswitch 6575 Hardware Guide rev A.pdf",  "6575"),
    "hw-6860":  ("Omniswitch 6860 Hardware Guide rev W.pdf",  "6860"),
    "hw-6865":  ("Omniswitch 6865 Hardware Guide rev Y.pdf",  "6865"),
    "hw-6870":  ("Omniswitch 6870 Hardware Guide rev D.pdf",  "6870"),
    "hw-6900v2":("Omniswitch 6900v2 Hardware Users Guide rev C.pdf","6900"),
    "hw-9900":  ("Omniswitch 9900 Hardware Guide rev S.pdf", "9900"),
}
ROOT = os.path.dirname(os.path.abspath(__file__))

for book, (pdf, num) in BOOKS.items():
    bdir = os.path.join(ROOT, "books", book)
    pdir = os.path.join(bdir, "images", "panels")
    os.makedirs(pdir, exist_ok=True)
    for f in os.listdir(pdir):
        os.remove(os.path.join(pdir, f))
    ft = open(os.path.join(bdir, "fulltext.md"), encoding="utf-8").read().splitlines()
    prefix = "OS99" if book == "hw-9900" else f"OS{num}"
    head = re.compile(rf"^({prefix}\d{{0,2}}[A-Z0-9]*(?:-[A-Z0-9]+)*(?:\s*\([A-Z0-9-]+\))?)\s+Front Panel( Components)?\s*$")
    chassis = re.compile(rf"^(OmniSwitch {num}[- ][A-Z0-9]+)\s*$")
    page = 0
    last_model = None
    found = {}  # model -> pdf page
    for ln in ft:
        m = re.match(r"<<<PAGE (\d+)>>>", ln.strip())
        if m:
            page = int(m.group(1)); continue
        s = ln.strip()
        if "." in s:
            continue  # 排除目录虚线行
        h = head.match(s)
        if h:
            found.setdefault(h.group(1).replace(" ", ""), page)
            continue
        c = chassis.match(s)
        if c:
            last_model = c.group(1).replace("OmniSwitch ", "").replace(" ", "")
        elif s == "Chassis Front Panel" and last_model:
            found.setdefault(last_model, page)
    if not found:
        print(f"{book}: NO PANELS FOUND"); continue
    doc = fitz.open(os.path.join(SRC, pdf))
    lines, pgs = [], []
    for model, pg in sorted(found.items(), key=lambda kv: kv[1]):
        if pg - 1 >= len(doc):
            continue
        pix = doc[pg - 1].get_pixmap(dpi=120)
        pix.save(os.path.join(pdir, model + ".png"))
        lines.append(f"![{model} 前/后面板](images/panels/{model}.png)")
        pgs.append(pg)
        print(f"{book} p{pg} -> {model}.png")
    doc.close()
    with open(os.path.join(bdir, "GALLERY.md"), "w", encoding="utf-8") as f:
        f.write(f"# 产品外观 · OmniSwitch {num} 系列\n\n> {len(lines)} 款机型面板示意，来自 Hardware Guide 各机型页（原文p{min(pgs)}-{max(pgs)}）。点击图片可放大查看原尺寸。\n\n" + "\n".join(lines) + "\n")
    print(f"{book}: GALLERY.md x{len(lines)}")
