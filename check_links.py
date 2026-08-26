# -*- coding: utf-8 -*-
"""全站链接检查：内部链接/锚点/资源引用"""
import os, re, html
from collections import defaultdict

ROOT = "site"
pages = []  # (relpath, hrefs)
for root, _, files in os.walk(ROOT):
    for fn in files:
        if fn.endswith(".html"):
            rel = os.path.normpath(os.path.join(root, fn)).replace("\\", "/")
            pages.append(rel)

page_set = set(pages)
link_re = re.compile(r'(?:href|src)="([^"#]+?)(#[^"]*)?"')

broken = defaultdict(list)   # target -> [from pages]
anchors_missing = []
stats = {"pages": len(pages), "links": 0, "internal": 0}

for rel in pages:
    s = open(rel, encoding="utf-8").read()
    # 收集本页定义的 id（供锚点检查）
    ids = set(re.findall(r'id="([^"]+)"', s))
    for m in link_re.finditer(s):
        href = html.unescape(m.group(1))
        stats["links"] += 1
        if href.startswith(("http://", "https://", "mailto:", "data:")):
            continue  # 外链单独抽样
        stats["internal"] += 1
        if href.startswith("#"):
            if href[1:] and href[1:] not in ids:
                anchors_missing.append((rel, href))
            continue
        # 相对路径解析（以 / 开头的按站点根）
        base = ROOT if href.startswith('/') else os.path.dirname(rel)
        href_rel = href.lstrip('/')
        target = os.path.normpath(os.path.join(base, href_rel)).replace("\\", "/")
        if target not in page_set and not (os.path.exists(target) and not target.endswith('.html')):
            broken[target].append(rel)

print(f"pages={stats['pages']} links={stats['links']} internal={stats['internal']}")
print(f"\n=== 断链 {sum(len(v) for v in broken.values())} 处（{len(broken)} 个目标） ===")
for t, frm in sorted(broken.items()):
    print(f"  {t}  <- {len(frm)} 页, 如 {frm[0]}")
print(f"\n=== 失效锚点 {len(anchors_missing)} 处 ===")
for p, a in anchors_missing[:20]:
    print(f"  {a}  in {p}")

# 图片资源检查
img_broken = 0
for rel in pages:
    s = open(rel, encoding="utf-8").read()
    for m in re.finditer(r'src="([^"]+)"', s):
        src = m.group(1)
        if src.startswith(("http", "data:")): continue
        if src.startswith('/'):
            t = os.path.normpath(os.path.join(ROOT, src.lstrip('/')))
        else:
            t = os.path.normpath(os.path.join(os.path.dirname(rel), src))
        if not os.path.exists(t):
            img_broken += 1
            print(f"  missing asset: {src} in {rel}")
print(f"\n缺失资源: {img_broken}")
