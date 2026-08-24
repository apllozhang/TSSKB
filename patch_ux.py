# -*- coding: utf-8 -*-
"""站点体验优化补丁：内容预处理（去流水线署名/段落拆行/来源条目）、面包屑+上下篇导航、CSS"""
s = open("build_site.py", encoding="utf-8").read()

# ---------- 1. 内容预处理 ----------
old = """def to_html(text):
    md.reset()
    return md.convert(text)"""
new = '''import re as _re
_CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮"

def preprocess(text):
    # 内部使用：去掉流水线署名描述
    out = []
    for ln in text.splitlines():
        low = ln.lower()
        if "cangjie" in low:
            ln = _re.sub(r"[*_`\\s]*由\\s*cangjie-skill\\s*流水线[^*\\n]*?蒸馏生成\\.?", "", ln, flags=_re.I)
            ln = _re.sub(r"cangjie-skill\\s*流水线", "内部整理流程", ln, flags=_re.I)
            ln = _re.sub(r"cangjie-skill", "内部整理流程", ln, flags=_re.I)
            if not ln.strip().strip("*_ `"):
                continue
        out.append(ln)
    text = "\\n".join(out)
    text = text.replace("由 cangjie-skill 流水线蒸馏为", "整理为").replace("蒸馏流水线", "整理流程")

    # 段落拆行：同段挤了多个 **②**/② 小标题时切开
    def split_para(m):
        seg = m.group(0)
        marks = [c for c in _CIRC if ("**" + c) in seg or seg.count(c) >= 2]
        if seg.count("**") >= 4 and marks:
            parts = _re.split(r"(?=\\**\\s*[②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮])", seg)
            parts = [p.strip() for p in parts if p.strip()]
            if len(parts) > 1:
                return "\\n\\n".join(parts)
        return seg
    text = _re.sub(r"^[^\\n|>#*-]{60,}$", split_para, text, flags=_re.M)

    # 长段落内"；"枚举换行（表格行/短行不动）
    def br_semi(m):
        seg = m.group(0)
        if "|" in seg or len(seg) < 120:
            return seg
        return seg.replace("；", "；\\n")
    text = _re.sub(r"^[^\\n|>#*]{100,}$", br_semi, text, flags=_re.M)

    # 来源条目行：改成 · 分隔的 chip 流（配合 CSS 换行更整齐）
    def src_line(m):
        toks = _re.split(r"[,，]\\s*", m.group(2).strip())
        toks = [t.strip() for t in toks if t.strip()]
        return m.group(1) + " · ".join(toks)
    text = _re.sub(r"^(来源条目[:：]\\s*)(.+)$", src_line, text, flags=_re.M)
    return text

def to_html(text):
    md.reset()
    return md.convert(preprocess(text))'''
assert old in s, "to_html anchor missing"
s = s.replace(old, new)

# ---------- 2. 模板文案 ----------
s = s.replace("。由 cangjie-skill 流水线蒸馏为 {n} 个可执行知识单元：", "。整理为 {n} 个可执行知识单元：")
s = s.replace("每一门课程由官方培训教材经 cangjie-skill 流水线蒸馏为可执行的知识单元（框架 · 清单 · 参数表 · 陷阱），",
              "每一门课程由官方培训教材整理为可执行的知识单元（框架 · 清单 · 参数表 · 陷阱），")
s = s.replace("内容由 AI 蒸馏流水线（cangjie-skill）从 ALE 官方培训教材生成，仅供内部学习使用；\n教材版权归 ALE Training Services 所有。新课程上线流程：上传教材 PDF → 蒸馏流水线 → 自动生成课程子站。",
              "内容整理自 ALE 官方培训教材与配置手册，仅供内部学习使用；教材版权归 ALE Training Services 所有，请勿外传。")

# ---------- 3. 面包屑 + 上下篇 + 页脚 ----------
# course page() 增加 crumbs 和 footer；skill 页加 prev/next
old_page = '''    def page(title, body, active=''):
        return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html_mod.escape(title)} — {c['title']}</title>
<style>{CSS}</style></head>
<body><div class="layout"><aside><h1>{c['title']}</h1>
<div class="sub">{c['subtitle']}</div>
{nav(active)}</aside><main>{body}</main></div></body></html>"""'''
new_page = '''    def crumbs(cur=''):
        cat = c['id'].split('/')[0]
        cat_label = {'postsales': '售后', 'presales': '售前', 'manuals': '配置手册'}[cat]
        bar = f'<nav class="crumbs"><a href="../../index.html">🏠 培训门户</a> › <a href="../../{cat}/index.html">{cat_label}</a> › <a href="index.html">{html_mod.escape(c["title"].split(" · ")[0])}</a>'
        if cur:
            bar += f' › <span>{html_mod.escape(cur)}</span>'
        return bar + '</nav>'

    def page(title, body, active='', cur=''):
        foot = '<div class="foot">仅供内部学习使用 · 教材版权归 ALE Training Services 所有</div>'
        return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html_mod.escape(title)} — {c['title']}</title>
<style>{CSS}</style></head>
<body><div class="layout"><aside><h1>{c['title']}</h1>
<div class="sub">{c['subtitle']}</div>
{nav(active)}</aside><main>{crumbs(cur)}{body}{foot}</main></div></body></html>"""'''
assert old_page in s, "page() anchor missing"
s = s.replace(old_page, new_page)

# skill 页：标题+面包屑+上下篇
old_skill = """        h = rel_links(to_html(body))
        body_html = f'<h1>{slug}</h1><p class="meta"><span class="badge">SKILL</span> 来源页码: {html_mod.escape(chap)}</p>' + h
        with open(os.path.join(sub, 'skills', slug + '.html'), 'w', encoding='utf-8') as f:
            f.write(page(slug, body_html, slug))"""
new_skill = """        h = rel_links(to_html(body))
        # 中文标题取 H1；prev/next
        m1 = _re.search(r'^#\\s+(.+)$', body, _re.M)
        zh = m1.group(1).strip() if m1 else slug
        idx = skills.index(slug)
        pn = '<div class="pn">'
        pn += (f'<a href="{skills[idx-1]}.html">⬅ 上一单元：{skills[idx-1]}</a>' if idx > 0
               else f'<a href="index.html">⬅ 返回课程首页</a>')
        pn += (f'<a class="nxt" href="{skills[idx+1]}.html">下一单元：{skills[idx+1]} ➡</a>' if idx < len(skills)-1
               else f'<a class="nxt" href="../digest.html">查看课程精华 DIGEST ➡</a>')
        pn += '</div>'
        body_html = f'<h1>{html_mod.escape(zh)}</h1><p class="meta"><span class="badge">SKILL</span> {slug} · 来源页码: {html_mod.escape(chap)}</p>' + h + pn
        with open(os.path.join(sub, 'skills', slug + '.html'), 'w', encoding='utf-8') as f:
            f.write(page(slug, body_html, slug, cur=zh))"""
assert old_skill in s, "skill anchor missing"
s = s.replace(old_skill, new_skill)

# 其余页面带 cur
s = s.replace("f.write(page('首页', home))", "f.write(page('首页', home, cur='首页'))")
s = s.replace("f.write(page(title, f'<h1>{title}</h1>' + h))", "f.write(page(title, f'<h1>{title}</h1>' + h, cur=title))")

# ---------- 4. CSS ----------
s = s.replace("""@media(max-width:800px){.layout{grid-template-columns:1fr}aside{position:static;height:auto}main{padding:20px}}""",
"""main p,main li,main td{overflow-wrap:break-word;word-break:break-word}
main{padding:28px 48px 40px;max-width:1040px}
h1{font-size:26px}h2{margin-top:30px;padding-top:10px;border-top:1px solid var(--line)}h3{margin-top:22px}
blockquote p{margin:6px 0}
.crumbs{font-size:13px;color:var(--mut);margin:0 0 14px}
.crumbs a{color:var(--acc)}
.pn{display:flex;justify-content:space-between;gap:12px;margin-top:36px;padding-top:14px;border-top:1px solid var(--line)}
.pn a{flex:1;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 14px;font-size:14px}
.pn a:hover{border-color:var(--acc)}
.pn .nxt{text-align:right}
.foot{margin-top:34px;font-size:12px;color:var(--mut);border-top:1px solid var(--line);padding-top:10px}
@media(max-width:800px){.layout{grid-template-columns:1fr}aside{position:static;height:auto}main{padding:20px}}""")

open("build_site.py", "w", encoding="utf-8").write(s)
print("UX patch applied")
