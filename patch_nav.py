# -*- coding: utf-8 -*-
"""修复 skill 子页的 nav/crumbs 相对路径"""
s = open("build_site.py", encoding="utf-8").read()

# 1) nav 增加 sub 参数
old_nav = """    def nav(active):
        items = ['<a href="index.html">🏠 课程首页</a>',
                 '<a href="digest.html">📖 精华长文 DIGEST</a>',
                 '<a href="overview.html">📘 教书理解 BOOK_OVERVIEW</a>',
                 '<a href="glossary.html">🔤 术语词典</a>',
                 '<a href="../../index.html">⬅️ 返回培训门户</a>',
                 '<a href="index.html">──── Skills ────</a>']
        for gname, slugs in c['groups']:
            items.append(f'<div class="grp">{html_mod.escape(gname)}</div>')
            for s in slugs:
                cls = ' class="on"' if s == active else ''
                items.append(f'<a href="skills/{s}.html"{cls}>{s}</a>')
        return '\\n'.join(items)"""
new_nav = """    def nav(active, sub=False):
        p = '../' if sub else ''
        items = [f'<a href="{p}index.html">🏠 课程首页</a>',
                 f'<a href="{p}digest.html">📖 精华长文 DIGEST</a>',
                 f'<a href="{p}overview.html">📘 教书理解 BOOK_OVERVIEW</a>',
                 f'<a href="{p}glossary.html">🔤 术语词典</a>',
                 f'<a href="{p}../../index.html">⬅️ 返回培训门户</a>',
                 f'<a href="{p}index.html">──── Skills ────</a>']
        for gname, slugs in c['groups']:
            items.append(f'<div class="grp">{html_mod.escape(gname)}</div>')
            for s in slugs:
                cls = ' class="on"' if s == active else ''
                items.append(f'<a href="{p}skills/{s}.html"{cls}>{s}</a>')
        return '\\n'.join(items)"""
assert old_nav in s, "nav not found"
s = s.replace(old_nav, new_nav)

# 2) crumbs 增加 sub 参数
old_cr = "    def crumbs(cur=''):\n        cat = c['id'].split('/')[0]"
new_cr = "    def crumbs(cur='', sub=False):\n        cat = c['id'].split('/')[0]"
assert old_cr in s, "crumbs sig not found"
s = s.replace(old_cr, new_cr)

old_cr2 = "        bar = f'<nav class=\"crumbs\"><a href=\"../../index.html\">🏠 培训门户</a> › <a href=\"../../{cat}/index.html\">{cat_label}</a> › <a href=\"index.html\">{html_mod.escape(c[\"title\"].split(\" · \")[0])}</a>'"
new_cr2 = "        p = '../../../' if sub else '../../'\n        q = '../' if sub else ''\n        bar = f'<nav class=\"crumbs\"><a href=\"{p}index.html\">🏠 培训门户</a> › <a href=\"{p}{cat}/index.html\">{cat_label}</a> › <a href=\"{q}index.html\">{html_mod.escape(c[\"title\"].split(\" · \")[0])}</a>'"
assert old_cr2 in s, "crumbs bar not found"
s = s.replace(old_cr2, new_cr2)

# 3) page 增加 sub 参数并传递
old_pg = "    def page(title, body, active='', cur=''):"
new_pg = "    def page(title, body, active='', cur='', sub=False):"
assert old_pg in s, "page sig not found"
s = s.replace(old_pg, new_pg)
s = s.replace("{nav(active)}</aside><main>{crumbs(cur)}{body}{foot}</main>",
              "{nav(active, sub)}</aside><main>{crumbs(cur, sub)}{body}{foot}</main>")

# 4) skill 页 sub=True
old_sk = "            f.write(page(slug, body_html, slug, cur=zh))"
new_sk = "            f.write(page(slug, body_html, slug, cur=zh, sub=True))"
assert old_sk in s, "skill page call not found"
s = s.replace(old_sk, new_sk)

open("build_site.py", "w", encoding="utf-8").write(s)
print("nav path fix applied")
