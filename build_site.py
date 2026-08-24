# -*- coding: utf-8 -*-
"""构建 ALE Networking 技术培训门户 + 各课程学习子站"""
import os, re, markdown, html as html_mod

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'site')
os.makedirs(OUT, exist_ok=True)

md = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc'])

# ============ 课程定义 ============
NEW_COURSES = [
  dict(id='presales/spb-presales', book='spb-presales', title='DT00XPS279 · OmniSwitch LAN SPB 售前',
       subtitle='Issue 05 · 147 页 · SPB 技术推销课（卖点弹药/架构/L3 服务/案例/三技术对比）',
       route=['售前攻防弹药库：为什么弃 STP 选 SPB', '架构与控制面/数据面：BEB/BCB/BVLAN/IS-IS/ECT',
              'L3 集成三形态：Outline/Front-panel/Service-based', 'OV2500 编排与三大成功案例', 'SPB vs EVPN vs MPLS 七维选型'],
       groups=[
        ('售前攻防', ['spb-presales-battlecard', 'spb-micro-segmentation']),
        ('架构与设计', ['spb-topology-isis-design']),
        ('边缘与服务', ['spb-edge-services']),
        ('L3 集成', ['spb-l3-integration']),
        ('交付与选型', ['spb-ov2500-delivery', 'spb-vs-evpn-mpls-selection', 'spb-stp-migration-cases', 'spb-license-spec-sizing']),
       ]),
  dict(id='presales/campus-lan', book='campus-lan-presales', title='DT00XPS281 · Campus LAN 售前',
       subtitle='Edition 29 · 480 页 · 园区网售前全科（特性→网管→选型→License→产品组合）',
       route=['分层设计与高可用六方案', '机型定位表→功能矩阵→VC vs 机箱', '参考架构模板库（SMB/紧凑核心/环网/密集核心）',
              '网管三平台与 Network Advisor', 'WWPL 报价规则与安全统一接入'],
       groups=[
        ('设计与高可用', ['campus-design-tiering-and-ha', 'virtual-chassis-design', 'dhl-erp-ring-protection']),
        ('机型与架构', ['omniswitch-model-selection', 'campus-reference-architectures']),
        ('织物与自动化', ['spb-vxlan-core-fabric', 'ifab-zero-touch-automation']),
        ('网管与商务', ['nms-platform-and-network-advisor', 'license-wwpl-pricing']),
        ('安全与垂直', ['security-unified-access', 'video-surveillance-design']),
       ]),
  dict(id='presales/stellar-wlan', book='stellar-wlan-presales', title='DT00XPS288 · OmniAccess Stellar WLAN 售前',
       subtitle='Edition 28 · 273 页 · 无线售前全科（AP 矩阵/三管理模式/License 三体系/用例/VoWLAN）',
       route=['AP 三维选型矩阵', '管理模式三岔口（Express/本地/云）', 'License 三体系报价法（OVCX 63 编码）',
              '七大行业用例弹药库', 'VoWLAN 与场景化容量基线'],
       groups=[
        ('选型与模式', ['ap-selection-matrix', 'management-mode-selection']),
        ('商务与报价', ['license-quotation']),
        ('用例与语音', ['industry-use-cases', 'vowlan-deployment']),
        ('场景与增值', ['rf-scenario-baseline', 'network-advisor-aiops', 'special-topologies']),
       ]),
  dict(id='postsales/acfe-wlan-basic', book='acfe-wlan', title='DT00XTE360 · ACFE WLAN Basic Deployment with OmniVista',
       subtitle='Edition 04 · 585 页 · Stellar+Cirrus 云管交付实操（AP 生命周期全流程，5 天带 Lab）',
       route=['部署模式判定与开局前置', 'Cirrus 组织与 License 生命周期', '设备 Onboarding 与激活排障',
              'SSID 全家桶与 PSK 四级体系', 'UPAM 策略/RF 基线/漫游 RAP/WIPS/勘测'],
       groups=[
        ('开局与云管', ['express-mode-bootstrap', 'cirrus-license-org-lifecycle', 'device-cloud-onboarding']),
        ('SSID 与策略', ['ssid-authentication-suite', 'upam-policy-bandwidth']),
        ('RF 与漫游', ['rf-optimization-baseline', 'roaming-rap-design']),
        ('安全与收尾', ['wips-security-deployment', 'site-survey-troubleshooting', 'rlab-lab-manual']),
       ]),
  dict(id='postsales/stellar-adv-trouble', book='stellar-wlan-adv-trouble', title='DT00XTE478 · Stellar WLAN 高级排障',
       subtitle='187 页 · 无线排障专题（方法论/工具箱/四层排障/勘测/TKC）',
       route=['排障总方法论：七步流程+三域根因地图', '排障工具箱与基础体检', '客户端连接决策链与 802.1X 排查',
              '网络侧与漫游 RF 排障', '勘测三步法与五发现五动作'],
       groups=[
        ('方法论', ['wlan-trouble-methodology']),
        ('工具与体检', ['stellar-ap-toolbox', 'stellar-ap-system-health']),
        ('故障域', ['client-connection-trouble', 'dot1x-radius-trouble', 'network-side-trouble', 'wireless-rf-roaming-trouble']),
        ('勘测纠正', ['site-survey-remediation']),
       ]),
  dict(id='postsales/stellar-express', book='stellar-wlan-express', title='DT00XTE455 · Stellar WLAN Express',
       subtitle='Edition 07 · 183 页 · 免云管小微交付专题（集群/SSID/Bridge-Mesh/15 排障案例）',
       route=['开箱六步与集群上线', 'SSID/Portal/内置服务', '射频勘测与调优',
              'Bridge/Mesh 特殊组网', '15 案例三域排障地图'],
       groups=[
        ('开局', ['express-cluster-onboarding']),
        ('业务与射频', ['ssid-portal-auth', 'rf-survey-tuning']),
        ('组网与排障', ['bridge-mesh-deployment', 'ap-side-troubleshooting']),
       ]),
  dict(id='postsales/os-lan-spb-impl', book='os-lan-spb-impl', title='DT00XTE323 · OmniSwitch LAN SPB 实施',
       subtitle='Edition 12 · 367 页 · SPB 交付配置手册（骨干→L2→L3→自动化，10 Lab CLI 全录）',
       route=['骨干部署四步（BCB/BEB/BVLAN/IS-IS）', 'L2 服务五步开通（SAP/ISID/vlan-xlation）',
              'IP over SPB 三方案配置模板', 'BUM 组播与接入保护', 'UNP 动态服务/OV2500 编排/E-Tree'],
       groups=[
        ('骨干与 L2', ['spb-backbone-deploy', 'spb-l2-service']),
        ('L3 集成', ['ip-over-spb']),
        ('保护与冗余', ['spb-bum-protection', 'spb-access-ring-redundancy', 'spb-hybrid-etree']),
        ('自动化与运维', ['unp-dynamic-ov2500', 'spb-oam-troubleshoot']),
       ]),
  dict(id='postsales/os-lan-mpls-impl', book='os-lan-mpls-impl', title='DT00XTE324 · OmniSwitch LAN MPLS 实施',
       subtitle='Edition 02 · 153 页 · MPLS/VPLS 实施精要（三 Lab CLI + 参考设计 + 能力边界）',
       route=['MPLS 部署十步与许可', 'VPLS 双信令（LDP vs BGP）选型与配置', '园区/城域参考设计模板',
              '运行规则与 show 判读', 'AOS 六项能力边界（售前禁引核对）'],
       groups=[
        ('部署与信令', ['aos-mpls-deploy-license', 'vpls-signaling-ldp-vs-bgp']),
        ('设计与运维', ['mpls-reference-design', 'aos-mpls-operating-rules', 'aos-mpls-capability-limits']),
       ]),
  dict(id='postsales/os-lan-vxlan-evpn', book='os-lan-vxlan-evpn', title='DT00XTE325 · OmniSwitch LAN VxLAN/EVPN',
       subtitle='Edition 01 · 213 页 · 五步配置法 + 三 Lab + EVPN 架构指南',
       route=['五步配置法总纲与版本边界', 'Underlay/Overlay BGP 设计', 'L2/L3 业务开通（VNI/IRB/RT 总表）',
              '多归属与 DF', 'BUM 与验证排障'],
       groups=[
        ('总纲与底座', ['vxlan-evpn-five-step-architecture', 'vxlan-evpn-underlay-bgp-design']),
        ('业务与多归属', ['vxlan-evpn-service-provisioning', 'vxlan-evpn-multihoming-df']),
        ('排障', ['vxlan-evpn-bum-troubleshooting']),
       ]),
  dict(id='postsales/os-lan-access', book='os-lan-access-switching', title='DT00XTE215 · OmniSwitch LAN Access Switching',
       subtitle='Edition 19 · 500 页 · 接入层基础全科（三目录模型/VC/VLAN/LACP/STP/DHL/QoS/AG）',
       route=['AOS 三目录配置管理模型', 'Virtual Chassis 部署运维', 'VLAN 与链路冗余（LACP/STP/DHL）',
              'IP 服务与 QoS/ACL', '接入安全（AG/UNP/LLDP）与 PoE 运维'],
       groups=[
        ('管理面', ['aos-config-management', 'switch-management-access']),
        ('转发面', ['virtual-chassis-deployment', 'vlan-link-redundancy']),
        ('策略面', ['ip-services-basic', 'qos-acl-policy', 'access-guardian-unp']),
        ('运维', ['poe-ops-diagnostics']),
       ]),
  dict(id='postsales/os-lan-troubleshooting', book='os-lan-troubleshooting', title='DT00XTE221 · OmniSwitch LAN Troubleshooting',
       subtitle='587 页 · 有线排障全科（方法论/启动/系统/L2/VC/STP/L3/组播/OVNA）',
       route=['排障总方法论与 TKC', '启动与系统排障', 'L2/STP 环路/VC 四层递进',
              'L3 路由 VRRP 与组播', '日志工具层与 OVNA AI 运维'],
       groups=[
        ('方法论与系统', ['lan-troubleshooting-methodology', 'boot-system-troubleshooting']),
        ('故障域', ['l2-connectivity-troubleshooting', 'stp-loop-troubleshooting', 'virtual-chassis-troubleshooting',
                'l3-routing-vrrp-troubleshooting', 'multicast-troubleshooting']),
        ('工具与 AI 运维', ['app-logging-qos-troubleshooting', 'ovna-deployment-teams-bot']),
       ]),
  dict(id='manuals/awos-ap-guide', book='awos-ap-guide', title='AWOS 5.0.3 · Stellar AP 用户手册',
       subtitle='128 页 · AP 本地管理配置手册（Express 模式 GUI 全参考）',
       route=['集群开局与 PVM 选举', 'SSID 射频调优与内置服务', 'WLAN 安全与高级认证', '运维升级与 Mesh'],
       groups=[
        ('开局', ['cluster-bootstrap-pvm']),
        ('业务', ['ssid-radio-tuning']),
        ('安全', ['wlan-security-enterprise']),
        ('运维', ['ap-ops-upgrade-mesh']),
       ]),
  dict(id='manuals/ov2500-install', book='ov2500-install', title='OV2500 4.9R2 · 安装与升级指南',
       subtitle='326 页 · 网管平台部署手册（三平台/HA/升级链）',
       route=['部署规划与四档规模', '三平台安装流程', 'HA 集群设计与转换', '升级路径与备份恢复'],
       groups=[
        ('规划', ['ov2500-sizing-and-platform-planning']),
        ('安装', ['ov2500-install-on-esxi-hyperv-kvm']),
        ('HA 与升级', ['ov2500-ha-cluster-design-and-conversion', 'ov2500-upgrade-backup-restore']),
       ]),
  dict(id='manuals/ov2500-rap-vpn', book='ov2500-rap-vpn', title='OV2500 4.9R2 · RAP 与 VPN VA 安装',
       subtitle='84 页 · 远程 AP 安全回连方案部署',
       route=['VPN 模式选型与 RAP 注册', 'VPN VA 三平台部署与容量', '数据隧道与 Local Breakout', '四层排障决策树'],
       groups=[
        ('规划', ['rap-vpn-mode-registration']),
        ('部署与配置', ['vpn-va-deploy-capacity', 'rap-data-tunnel-config']),
        ('排障', ['rap-vpn-troubleshooting']),
       ]),

  dict(id='postsales/stellar-adv-deploy', book='stellar-wlan-adv-deploy', title='DT00XTE361 · Stellar WLAN Advanced Deployment with OmniVista',
       subtitle='Edition 02 · 330 页 · Cirrus 云管进阶（QoE 分析/监控运维/IoT/全流程演练）',
       route=['QoE 与分析三件套（六指标+四阈值）', '监控告警与设备运维', '有线客户端与 IoT 接入',
              '全流程部署演练当交付 checklist', 'CLI 排障速查'],
       groups=[
        ('可观测性', ['stellar-qoe-analytics', 'stellar-monitoring-ops']),
        ('接入进阶', ['stellar-wired-iot-access', 'stellar-bridge-mesh', 'stellar-ssid-advanced']),
        ('交付与排障', ['stellar-deployment-checklist', 'stellar-troubleshooting-cli', 'stellar-vowlan']),
       ]),
  dict(id='postsales/stellar-enterprise-basic', book='stellar-wlan-enterprise-basic', title='DT00XTE368 · Stellar WLAN Enterprise Basic',
       subtitle='Edition 14 · 515 页 · 无线理论 + OV2500 企业模式实操二合一',
       route=['无线理论速成（802.11/天线/安全/勘测）', 'Ekahau 勘测七步法', 'Enterprise 开局与设备发现',
              'Employee SSID 与 AD 认证', 'UPAM Guest/L2 漫游/RAP'],
       groups=[
        ('理论与勘测', ['wlan-theory-fundamentals', 'site-survey-ekahau']),
        ('开局与业务', ['enterprise-mode-onboarding', 'employee-ssid-8021x', 'upam-guest-access']),
        ('漫游与远程', ['roaming-l2-l3', 'rap-remote-deployment']),
       ]),
  dict(id='postsales/stellar-adv-trouble-update', book='stellar-wlan-adv-trouble-update', title='DT00XTE378 · Stellar WLAN 高级排障与更新',
       subtitle='488 页 · 排障篇同 T478 + Features Update 增量（新硬件/云运维/升级迁移）',
       route=['Enterprise 上线与 SSID 策略进阶', 'RAP 双模式与云运维三件套', '新硬件速览（Wi-Fi 7 双雄）', '升级迁移陷阱清单'],
       groups=[
        ('上线与业务', ['stellar-enterprise-onboarding', 'stellar-ssid-policy-advanced']),
        ('云运维', ['stellar-rap-backup-upgrade-ops']),
        ('硬件速览', ['stellar-wifi7-hardware-rf-quickref']),
       ]),
  dict(id='manuals/ov2500-release-notes', book='ov2500-release-notes', title='OV2500 4.9R2 · Release Notes',
       subtitle='93 页 · 新特性/兼容矩阵/升级路径 + 63 条已知问题排障库',
       route=['新特性与兼容矩阵（升级评估入口）', '升级路径与部署规则', '已知问题 13 模块排障库', '危险陷阱 TOP12'],
       groups=[
        ('升级评估', ['ov2500-49r2-features-compat', 'ov2500-upgrade-deploy']),
        ('排障库', ['ov2500-known-issues', 'ov2500-danger-traps']),
       ]),
]
COURSES = NEW_COURSES  # 旧课程(ov-terra/bootcamp/core)保留 site/ 预构建页面，源 books 未随库分发
_LEGACY = [
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

import re as _re
_CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮"

def preprocess(text):
    # 内部使用：去掉流水线署名描述
    out = []
    for ln in text.splitlines():
        low = ln.lower()
        if "cangjie" in low:
            ln = _re.sub(r"[*_`\s]*由\s*cangjie-skill\s*流水线[^*\n]*?蒸馏生成\.?", "", ln, flags=_re.I)
            ln = _re.sub(r"cangjie-skill\s*流水线", "内部整理流程", ln, flags=_re.I)
            ln = _re.sub(r"cangjie-skill", "内部整理流程", ln, flags=_re.I)
            if not ln.strip().strip("*_ `"):
                continue
        out.append(ln)
    text = "\n".join(out)
    text = text.replace("由 cangjie-skill 流水线蒸馏为", "整理为").replace("蒸馏流水线", "整理流程")

    # 段落拆行：同段挤了多个 **②**/② 小标题时切开
    def split_para(m):
        seg = m.group(0)
        marks = [c for c in _CIRC if ("**" + c) in seg or seg.count(c) >= 2]
        if seg.count("**") >= 4 and marks:
            parts = _re.split(r"(?=\**\s*[②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮])", seg)
            parts = [p.strip() for p in parts if p.strip()]
            if len(parts) > 1:
                return "\n\n".join(parts)
        return seg
    text = _re.sub(r"^[^\n|>#*-]{60,}$", split_para, text, flags=_re.M)

    # 长段落内"；"枚举换行（表格行/短行不动）
    def br_semi(m):
        seg = m.group(0)
        if "|" in seg or len(seg) < 120:
            return seg
        return seg.replace("；", "；\n")
    text = _re.sub(r"^[^\n|>#*]{100,}$", br_semi, text, flags=_re.M)

    # 来源条目行：改成 · 分隔的 chip 流（配合 CSS 换行更整齐）
    def src_line(m):
        toks = _re.split(r"[,，]\s*", m.group(2).strip())
        toks = [t.strip() for t in toks if t.strip()]
        return m.group(1) + " · ".join(toks)
    text = _re.sub(r"^(来源条目[:：]\s*)(.+)$", src_line, text, flags=_re.M)
    return text

def to_html(text):
    md.reset()
    return md.convert(preprocess(text))

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
main p,main li,main td{overflow-wrap:break-word;word-break:break-word}
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

    def crumbs(cur=''):
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
{nav(active)}</aside><main>{crumbs(cur)}{body}{foot}</main></div></body></html>"""

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
        # 中文标题取 H1；prev/next
        m1 = _re.search(r'^#\s+(.+)$', body, _re.M)
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
            f.write(page(slug, body_html, slug, cur=zh))

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
<p class="meta">教材: <b>{c['subtitle']}</b>。整理为 {n} 个可执行知识单元：
每个单元含 原文引用(R) / 方法论骨架(I) / 书中案例(A1) / 触发场景(A2) / 可执行步骤(E) / 边界与陷阱(B)。</p>
<h2>建议学习路线</h2><ol>{route}</ol>
<h2>知识单元</h2>{cards}
<h2>全文阅读</h2>
<p><a href="digest.html">📖 精华长文 DIGEST</a> · <a href="overview.html">📘 教书理解</a> · <a href="glossary.html">🔤 术语词典</a></p>"""
    with open(os.path.join(sub, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page('首页', home, cur='首页'))

    for src, title, out in [('DIGEST.md', '精华长文 DIGEST', 'digest.html'),
                            ('BOOK_OVERVIEW.md', '教书理解 BOOK_OVERVIEW', 'overview.html'),
                            ('GLOSSARY.md', '术语词典', 'glossary.html')]:
        h = to_html(read(os.path.join(book, src)))
        with open(os.path.join(sub, out), 'w', encoding='utf-8') as f:
            f.write(page(title, f'<h1>{title}</h1>' + h, cur=title))
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

for dirname, label in [('postsales', '售后 · Postsales'), ('presales', '售前 · Presales'), ('manuals', '配置手册 · Manuals')]:
    build_category(dirname, label)

# ============ 门户封面 ============
course_map = {c['id']: c for c in COURSES}
CATALOG = [
    ('售前 · Presales', '#38bdf8', [
        ('DT00XPS279 · OmniSwitch LAN SPB 售前', 'Issue 05 · 147 页 · 9 个知识单元 · 卖点弹药 / L3 集成 / 三技术对比', 'presales/spb-presales/index.html'),
        ('DT00XPS281 · Campus LAN 售前', 'Edition 29 · 480 页 · 11 个知识单元 · 分层设计 / 机型选型 / WWPL 报价 / 参考架构库', 'presales/campus-lan/index.html'),
        ('DT00XPS288 · OmniAccess Stellar WLAN 售前', 'Edition 28 · 273 页 · 8 个知识单元 · AP 矩阵 / 三管理模式 / License 三体系 / 七大用例', 'presales/stellar-wlan/index.html'),
        ('SD-WAN / SASE 方案', 'Alestra 与云网融合场景', None),
    ]),
    ('售后 · Postsales', '#f59e0b', [
        ('DT00XTE360 · ACFE WLAN Basic Deployment with OmniVista', 'Edition 04 · 585 页 · 10 个知识单元 · AP 生命周期交付 / SSID 全家桶 / WIPS', 'postsales/acfe-wlan-basic/index.html'),
        ('DT00XTE361 · Stellar WLAN Advanced Deployment', 'Edition 02 · 330 页 · 7 个知识单元 · QoE 分析 / 监控运维 / 全流程演练', 'postsales/stellar-adv-deploy/index.html'),
        ('DT00XTE368 · Stellar WLAN Enterprise Basic', 'Edition 14 · 515 页 · 7 个知识单元 · 无线理论 + OV2500 企业模式实操', 'postsales/stellar-enterprise-basic/index.html'),
        ('DT00XTE378 · Stellar WLAN 高级排障与更新', '488 页 · 4 个知识单元 · Features Update 增量 / RAP 云运维 / 升级陷阱', 'postsales/stellar-adv-trouble-update/index.html'),
        ('DT00XTE478 · Stellar WLAN 高级排障', '187 页 · 8 个知识单元 · 七步方法论 / 四层排障 / 勘测纠正', 'postsales/stellar-adv-trouble/index.html'),
        ('DT00XTE455 · Stellar WLAN Express', 'Edition 07 · 183 页 · 5 个知识单元 · 免云管小微交付 / Bridge-Mesh / 15 案例', 'postsales/stellar-express/index.html'),
        ('DT00XTE323 · OmniSwitch LAN SPB 实施', 'Edition 12 · 367 页 · 8 个知识单元 · 骨干/L2/L3/自动化 + 10 Lab CLI', 'postsales/os-lan-spb-impl/index.html'),
        ('DT00XTE324 · OmniSwitch LAN MPLS 实施', 'Edition 02 · 153 页 · 5 个知识单元 · VPLS 双信令 / 参考设计 / 能力边界', 'postsales/os-lan-mpls-impl/index.html'),
        ('DT00XTE325 · OmniSwitch LAN VxLAN/EVPN', 'Edition 01 · 213 页 · 5 个知识单元 · 五步配置法 / 多归属 DF / BUM 排障', 'postsales/os-lan-vxlan-evpn/index.html'),
        ('DT00XTE215 · OmniSwitch LAN Access Switching', 'Edition 19 · 500 页 · 8 个知识单元 · 三目录模型 / VC / DHL / 接入安全', 'postsales/os-lan-access/index.html'),
        ('DT00XTE221 · OmniSwitch LAN Troubleshooting', '587 页 · 9 个知识单元 · 有线排障全科 / 五大 LAB 根因 / OVNA', 'postsales/os-lan-troubleshooting/index.html'),
        ('DT00XTE317 · OmniVista Cirrus / Terra 部署与配置', 'Edition 10 · 478 页 · 10 个知识单元 · 激活排障 / SSID 选型 / RF 调优 / 漫游排障', 'postsales/ov-terra/index.html'),
        ('DT00XTE220 · OmniSwitch LAN R8 Bootcamp', 'Edition 23 · 1162 页 · 五天全科训练营 · 12 个知识单元 · 开局加固 / L2 冗余 / 路由 / SPB Fabric', 'postsales/dt00xte220-bootcamp/index.html'),
        ('DT00XTE216 · OmniSwitch LAN R8 Core Switching', 'Edition 15 · 724 页 · 核心交换专题 · 11 个知识单元 · SPB 织构重点（含 Tech Brief 与实验附录）', 'postsales/dt00xte216-core-switching/index.html'),
        ('Stellar WLAN 实施与优化', 'AP 部署、RF 规划、无线排障', None),
    ]),
    ('配置手册 · Manuals', '#22d3ee', [
        ('AWOS 5.0.3 · Stellar AP 用户手册', '128 页 · 4 个知识单元 · 集群开局 / 射频调优 / 安全 / 运维升级', 'manuals/awos-ap-guide/index.html'),
        ('OV2500 4.9R2 · 安装与升级指南', '326 页 · 4 个知识单元 · 四档规模 / 三平台 / HA / 升级链', 'manuals/ov2500-install/index.html'),
        ('OV2500 4.9R2 · RAP 与 VPN VA 安装', '84 页 · 4 个知识单元 · VPN 模式 / VA 容量 / 隧道排障', 'manuals/ov2500-rap-vpn/index.html'),
        ('OV2500 4.9R2 · Release Notes', '93 页 · 4 个知识单元 · 升级评估 / 63 条已知问题排障库 / 危险陷阱', 'manuals/ov2500-release-notes/index.html'),
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
每一门课程由官方培训教材整理为可执行的知识单元（框架 · 清单 · 参数表 · 陷阱），
覆盖 部署实施 · 运维排障 · 方案设计 · 安全准入 全生命周期。</p>
</div>
{cats_html}
<h2>关于本站</h2>
<p class="meta">内容整理自 ALE 官方培训教材与配置手册，仅供内部学习使用；教材版权归 ALE Training Services 所有，请勿外传。</p>
</main></body></html>"""
with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(cover)
print('portal built')
