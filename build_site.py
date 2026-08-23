# -*- coding: utf-8 -*-
"""构建 ALE Networking 技术培训门户 + 各课程学习子站"""
import os, re, markdown, html as html_mod

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'site')
os.makedirs(OUT, exist_ok=True)

md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])

# ============ 课程定义 ============
COURSES = [
  dict(id='postsales/ov-terra', book='ov-terra-deploy', title='DT00XTE317 · OmniVista Cirrus / Terra 部署与配置',
       subtitle='Edition 10 · 478 页 · 云管与本地部署平台',
       route=['许可证与组织开通→Terra 3-VM 部署', '设备纳管与激活排障', 'SSID 选型→策略带宽→有线认证',
              'RF 调优→漫游排障', 'WIPS 安全→Mesh/Bridge/RAP'],
       groups=[
        ('平台部署与开通', ['ov-terra-deploy', 'ov-license-org-onboarding']),
        ('设备纳管与激活', ['ov-device-activation-troubleshoot']),
        ('SSID / 策略 / 认证设计', ['ov-ssid-psk-selection', 'ov-policy-bandwidth-design', 'ov-wired-auth-config']),
        ('RF / 漫游 / 安全 / 特殊组网', ['ov-rf-tuning', 'ov-roaming-troubleshoot', 'ov-wips-rogue-policy', 'ov-mesh-bridge-rap']),
       ]),
  dict(id='postsales/dt00xte220-bootcamp', book='acfe-lan', title='DT00XTE220 · OmniSwitch LAN R8 Bootcamp',
       subtitle='Edition 23 · 1162 页 · 五天全科训练营（开局→L2→路由→织构→安全→组播→运维）',
       route=['开局与管理面加固', 'VLAN/MVRP→LAG/STP 冗余→虚拟机箱', '准入认证 UNP→L2 安全→QoS 策略',
              'OSPF/IS-IS→BGP/VRF', 'SPB Fabric→组播→诊断运维'],
       groups=[
        ('开局与管理面', ['aos-switch-access-mgmt', 'aos-virtual-chassis']),
        ('L2 基础与冗余', ['aos-vlan-mvrp', 'aos-lag-stp']),
        ('安全与策略', ['aos-access-guardian-unp', 'aos-l2-security', 'aos-qos-acl-pbr']),
        ('L3 路由', ['aos-igp-routing', 'aos-bgp-vrf']),
        ('SPB Fabric 与组播', ['aos-spb-fabric', 'aos-multicast', 'aos-diagnostics-ops']),
       ]),
  dict(id='postsales/dt00xte216-core-switching', book='acfe-lan', title='DT00XTE216 · OmniSwitch LAN R8 Core Switching',
       subtitle='Edition 15 · 724 页 · 核心交换专题（L2/路由/织构/安全/组播；无 Lightning 开局与 AG 深入章节）',
       route=['VLAN/MVRP→LAG/STP 冗余→虚拟机箱', 'UNP 分类→L2 安全→QoS 策略',
              'OSPF/IS-IS→BGP/VRF', 'SPB Fabric（本课重点，含 Tech Brief 与实验附录）→组播→诊断运维'],
       groups=[
        ('开局与管理面', ['aos-virtual-chassis']),
        ('L2 基础与冗余', ['aos-vlan-mvrp', 'aos-lag-stp']),
        ('安全与策略', ['aos-access-guardian-unp', 'aos-l2-security', 'aos-qos-acl-pbr']),
        ('L3 路由', ['aos-igp-routing', 'aos-bgp-vrf']),
        ('SPB Fabric 与组播', ['aos-spb-fabric', 'aos-multicast', 'aos-diagnostics-ops']),
       ]),
]

def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()

def to_html(text):
    md.reset()
    return md.convert(text)

def parse_fm(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
        text = text[m.end():]
    return fm, text

CSS = """
:root{--bg:#0f172a;--panel:#1e293b;--card:#243447;--tx:#e2e8f0;--mut:#94a3b8;--acc:#38bdf8;--acc2:#f59e0b;--line:#334155}
*{box-sizing:border-box}
body{margin:0;font-family:"Segoe UI","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--tx);line-height:1.75}
a{color:var(--acc);text-decoration:none} a:hover{text-decoration:underline}
.layout{display:grid;grid-template-columns:250px 1fr;min-height:100vh}
aside{background:var(--panel);padding:20px 14px;border-right:1px solid var(--line);position:sticky;top:0;height:100vh;overflow-y:auto}
aside h1{font-size:17px;margin:0 0 4px} aside .sub{font-size:12px;color:var(--mut);margin-bottom:18px}
aside .grp{font-size:11px;letter-spacing:.1em;color:var(--mut);margin:16px 0 6px;text-transform:uppercase}
aside a{display:block;padding:6px 10px;border-radius:6px;color:var(--tx);font-size:14px}
aside a:hover{background:var(--card);text-decoration:none}
aside a.on{background:var(--card);color:var(--acc)}
main{padding:36px 48px;max-width:1000px}
h1{font-size:28px;border-bottom:2px solid var(--line);padding-bottom:10px}
h2{margin-top:34px;color:var(--acc)} h3{color:var(--acc2)}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:14px}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left}
th{background:var(--card)} tr:nth-child(even) td{background:#1b2740}
code{background:#2b3b52;padding:1px 6px;border-radius:4px;font-size:.92em;color:#7dd3fc}
pre{background:#0b1222;border:1px solid var(--line);padding:14px;border-radius:8px;overflow-x:auto}
pre code{background:none;padding:0}
blockquote{border-left:4px solid var(--acc2);background:var(--card);margin:12px 0;padding:8px 16px;border-radius:0 8px 8px 0}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin:20px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px;transition:border-color .15s}
.card:hover{border-color:var(--acc)} .card a{font-weight:600;font-size:16px}
.card p{font-size:13px;color:var(--mut);margin:8px 0 0}
.meta{font-size:13px;color:var(--mut)}
hr{border:none;border-top:1px solid var(--line);margin:26px 0}
.badge{display:inline-block;background:var(--acc);color:#062033;font-size:12px;border-radius:20px;padding:1px 10px;font-weight:700}
.badge.soon{background:#475569;color:#cbd5e1}
@media(max-width:800px){.layout{grid-template-columns:1fr}aside{position:static;height:auto}main{padding:20px}}
"""

def build_course(c):
    sub = os.path.join(OUT, c['id'].replace('/', os.sep))
    os.makedirs(os.path.join(sub, 'skills'), exist_ok=True)
    book = os.path.join(ROOT, 'books', c['book'])
    skills = [s for _, slugs in c['groups'] for s in slugs]

    def nav(active):
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
        return '\n'.join(items)

    def page(title, body, active=''):
        return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html_mod.escape(title)} — {c['title']}</title>
<style>{CSS}</style></head>
<body><div class="layout"><aside><h1>{c['title']}</h1>
<div class="sub">{c['subtitle']}</div>
{nav(active)}</aside><main>{body}</main></div></body></html>"""

    def rel_links(h):
        for s in skills:
            h = h.replace(f'>{s}<', f'><a href="{s}.html">{s}</a><')
        return h

    desc_map = {}
    for slug in skills:
        fm, body = parse_fm(read(os.path.join(book, slug, 'SKILL.md')))
        desc_map[slug] = fm.get('description', '')
        chap = fm.get('source_chapter', '')
        h = rel_links(to_html(body))
        body_html = f'<h1>{slug}</h1><p class="meta"><span class="badge">SKILL</span> 来源页码: {html_mod.escape(chap)}</p>' + h
        with open(os.path.join(sub, 'skills', slug + '.html'), 'w', encoding='utf-8') as f:
            f.write(page(slug, body_html, slug))

    cards = ''
    for gname, slugs in c['groups']:
        cards += f'<h2>{html_mod.escape(gname)}</h2><div class="cards">'
        for s in slugs:
            d = html_mod.escape(desc_map.get(s, '')[:150])
            cards += f'<div class="card"><a href="skills/{s}.html">{s}</a><p>{d}…</p></div>'
        cards += '</div>'
    route = ''.join(f'<li>{html_mod.escape(r)}</li>' for r in c['route'])
    n = len(skills)
    home = f"""<p><a href="../../index.html">⬅️ 返回培训门户</a></p>
<h1>{c['title']} · 学习站</h1>
<p class="meta">教材: <b>{c['subtitle']}</b>。由 cangjie-skill 流水线蒸馏为 {n} 个可执行知识单元：
每个单元含 原文引用(R) / 方法论骨架(I) / 书中案例(A1) / 触发场景(A2) / 可执行步骤(E) / 边界与陷阱(B)。</p>
<h2>建议学习路线</h2><ol>{route}</ol>
<h2>知识单元</h2>{cards}
<h2>全文阅读</h2>
<p><a href="digest.html">📖 精华长文 DIGEST</a> · <a href="overview.html">📘 教书理解</a> · <a href="glossary.html">🔤 术语词典</a></p>"""
    with open(os.path.join(sub, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page('首页', home))

    for src, title, out in [('DIGEST.md', '精华长文 DIGEST', 'digest.html'),
                            ('BOOK_OVERVIEW.md', '教书理解 BOOK_OVERVIEW', 'overview.html'),
                            ('GLOSSARY.md', '术语词典', 'glossary.html')]:
        h = to_html(read(os.path.join(book, src)))
        with open(os.path.join(sub, out), 'w', encoding='utf-8') as f:
            f.write(page(title, f'<h1>{title}</h1>' + h))
    print('course built:', c['id'], f'({n} skills)')

for c in COURSES:
    build_course(c)

# ============ 分类列表页 (如 /postsales/) ============
def build_category(dirname, label):
    d = os.path.join(OUT, dirname)
    os.makedirs(d, exist_ok=True)
    items = ''
    for c in COURSES:
        if c['id'].startswith(dirname + '/'):
            n = len([s for _, sl in c['groups'] for s in sl])
            items += f'''<div class="card"><a href="../{c['id']}/index.html">{c['title']}</a>
<p>{c['subtitle']}</p><p style="margin-top:6px"><span class="badge">{n} 个知识单元</span></p></div>'''
    page = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{label} — ALE Networking 技术培训</title><style>{CSS}</style></head>
<body><div class="layout"><aside><h1>ALE 培训门户</h1>
<div class="sub">{label}</div>
<a href="../index.html">⬅️ 返回培训门户</a></aside>
<main><h1>{label}</h1>
<p class="meta">该分类下的课程：</p>
<div class="cards">{items}</div></main></div></body></html>"""
    with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print('category built:', dirname)

for dirname, label in [('postsales', '售后 · Postsales')]:
    build_category(dirname, label)

# ============ 门户封面 ============
course_map = {c['id']: c for c in COURSES}
CATALOG = [
    ('售前 · Presales', '#38bdf8', [
        ('网络方案设计与产品选型', 'OmniSwitch / Stellar AP 产品矩阵、方案架构与配置报价', None),
        ('OmniVista Cirrus 云管方案', 'SaaS 价值主张、License 模式与容量规划', None),
        ('SD-WAN / SASE 方案', 'Alestra 与云网融合场景', None),
    ]),
    ('售后 · Postsales', '#f59e0b', [
        ('DT00XTE317 · OmniVista Cirrus / Terra 部署与配置', 'Edition 10 · 478 页 · 10 个知识单元 · 激活排障 / SSID 选型 / RF 调优 / 漫游排障', 'postsales/ov-terra/index.html'),
        ('DT00XTE220 · OmniSwitch LAN R8 Bootcamp', 'Edition 23 · 1162 页 · 五天全科训练营 · 12 个知识单元 · 开局加固 / L2 冗余 / 路由 / SPB Fabric', 'postsales/dt00xte220-bootcamp/index.html'),
        ('DT00XTE216 · OmniSwitch LAN R8 Core Switching', 'Edition 15 · 724 页 · 核心交换专题 · 11 个知识单元 · SPB 织构重点（含 Tech Brief 与实验附录）', 'postsales/dt00xte216-core-switching/index.html'),
        ('Stellar WLAN 实施与优化', 'AP 部署、RF 规划、无线排障', None),
    ]),
    ('无线网络 · WLAN', '#a78bfa', [
        ('WiFi 6 / 6E / 7 技术基础', '标准演进、OFDMA、多链路操作', None),
        ('Stellar AP 产品与组网', 'Mesh / Bridge / RAP 特殊组网', None),
    ]),
    ('有线网络 · LAN Switching', '#34d399', [
        ('OmniSwitch R8 体系结构', 'VC 虚拟机箱、SPB / MPLS、UNP', None),
        ('AOS CLI 进阶', '脚本化配置与自动化运维', None),
    ]),
    ('网络管理 · Management', '#f472b6', [
        ('OmniVista 2500 / Cirrus / Terra', '三大管理平台定位与选型', None),
        ('QoE 与网络分析', '体验质量度量与根因分析', None),
    ]),
    ('安全 · Security', '#fb7185', [
        ('网络准入与认证', '802.1X / MAC / Captive Portal / UPAM', None),
        ('WIPS 无线入侵防护', 'Rogue 检测与抑制', None),
    ]),
    ('认证与学习路径 · Certification', '#fbbf24', [
        ('ALE 认证体系', 'ACE / ACFE 认证路径与考前串讲', None),
    ]),
]

cats_html = ''
for gname, color, items in CATALOG:
    cards = ''
    for title, desc, href in items:
        if href:
            n = len([s for _, sl in course_map[href.replace('/index.html','')]['groups'] for s in sl]) if href.replace('/index.html','') in course_map else 0
            cards += f'''<div class="card" style="border-color:{color}">
<a href="{href}">{title}</a><p>{desc}</p>
<p style="margin-top:6px"><span class="badge">已上线</span></p></div>'''
        else:
            cards += f'''<div class="card">
<a style="color:var(--mut);cursor:default" onclick="return false">{title}</a><p>{desc}</p>
<p style="margin-top:6px"><span class="badge soon">待建设 · 教材上传后蒸馏上线</span></p></div>'''
    cats_html += f'<h2 style="color:{color}">{gname}</h2><div class="cards">{cards}</div>'

cover = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ALE Networking 技术培训</title>
<style>{CSS}
.hero{{text-align:center;padding:60px 20px 30px}}
.hero h1{{font-size:40px;border:none;margin-bottom:8px}}
.hero .en{{color:var(--acc);letter-spacing:.35em;font-size:14px;text-transform:uppercase}}
.hero p{{color:var(--mut);max-width:640px;margin:14px auto 0}}
main.cover{{max-width:1100px;margin:0 auto;padding:0 32px 60px}}
</style></head><body><main class="cover">
<div class="hero">
<div class="en">Alcatel-Lucent Enterprise</div>
<h1>ALE Networking 技术培训</h1>
<p>面向售前、售后与网络工程师的 ALE 网络技术学习门户。
每一门课程由官方培训教材经 cangjie-skill 流水线蒸馏为可执行的知识单元（框架 · 清单 · 参数表 · 陷阱），
覆盖 部署实施 · 运维排障 · 方案设计 · 安全准入 全生命周期。</p>
</div>
{cats_html}
<h2>关于本站</h2>
<p class="meta">内容由 AI 蒸馏流水线（cangjie-skill）从 ALE 官方培训教材生成，仅供内部学习使用；
教材版权归 ALE Training Services 所有。新课程上线流程：上传教材 PDF → 蒸馏流水线 → 自动生成课程子站。</p>
</main></body></html>"""
with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(cover)
print('portal built')
