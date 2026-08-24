# -*- coding: utf-8 -*-
"""文本+图片提取：python extract2.py <slug> <pdf> [imgs]"""
import fitz, hashlib, json, sys
from pathlib import Path

slug, pdf = sys.argv[1], sys.argv[2]
do_imgs = len(sys.argv) > 3 and sys.argv[3] == "imgs"

out = Path(r"D:\Claude code\TSSKB\books") / slug
out.mkdir(parents=True, exist_ok=True)
doc = fitz.open(pdf)
print(f"{slug}: {doc.page_count} pages", flush=True)

parts = []
for i, pg in enumerate(doc):
    t = pg.get_text().strip()
    if t: parts.append(f"<<<PAGE {i+1}>>>\n{t}")
(out / "fulltext.md").write_text("\n\n".join(parts), encoding="utf-8")
print(f"  text: {len(parts)} pages", flush=True)

if do_imgs:
    img_dir = Path(r"D:\Claude code\TSSKB\extract") / slug
    img_dir.mkdir(parents=True, exist_ok=True)
    seen, figures = set(), []
    for i in range(doc.page_count):
        for j, img in enumerate(doc[i].get_images(full=True)):
            try: b = doc.extract_image(img[0])
            except: continue
            w, h, data = b["width"], b["height"], b["image"]
            if w < 260 or h < 160 or len(data) < 12288: continue
            md5 = hashlib.md5(data).hexdigest()
            if md5 in seen: continue
            seen.add(md5)
            fn = f"p{i+1:03d}_{j:02d}.{b['ext']}"
            (img_dir / fn).write_bytes(data)
            figures.append({"page": i+1, "file": fn, "w": w, "h": h, "md5": md5})
        if (i+1) % 100 == 0: print(f"  ...page {i+1}, imgs={len(figures)}", flush=True)
    (img_dir / "figures.json").write_text(json.dumps(figures, ensure_ascii=False, indent=2), encoding="utf-8")
    json.dump(figures, open(img_dir.parent / f"{slug}_manifest.json", "w", encoding="utf-8"), ensure_ascii=False)
    print(f"  images: {len(figures)}", flush=True)
doc.close()
print("DONE", flush=True)
