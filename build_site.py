# -*- coding: utf-8 -*-
"""构建 ALE Networking 技术培训门户 + 各课程学习子站"""
import os, re, shutil, markdown, html as html_mod

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
  dict(id='presales/dan', book='dan', title='DAN · 数字化时代网络',
       subtitle='10 份官方文档 · 74 页 · DAN 愿景三支柱与七大行业方案（售前叙事弹药库）',
       route=['DAN 愿景：Autonomous Network / IoT / Business Innovation 三支柱',
              '企业白皮书：全球版与 APAC 版差异', '七大行业方案：教育/企业/政府/医疗/酒店/交通'],
       groups=[
        ('总纲', ['dan-vision', 'dan-vertical-enterprises']),
        ('白皮书', ['dan-wp-enterprises', 'dan-wp-apac']),
        ('行业方案', ['dan-vertical-education', 'dan-vertical-government',
                   'dan-vertical-healthcare', 'dan-vertical-hospitality', 'dan-vertical-transportation']),
       ]),
  dict(id='presales/dan-cases', book='dan-cases', title='全球客户案例 · Customer Reference 2024',
       subtitle='98 页 · 约 95 例 · 按行业分类的全球客户参考案例（医疗/交通/教育/酒店/政府/综合）',
       route=['六行业案例速查表：客户/挑战/方案组合/成效数字', '每行业精选案例详解',
              '售前引用方法与注意'],
       groups=[
        ('案例库', ['cases-healthcare', 'cases-transportation', 'cases-education',
                 'cases-hospitality', 'cases-government', 'cases-general']),
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
  dict(id='wlan/awos-ap-guide', book='awos-ap-guide', title='AWOS 5.0.3 · Stellar AP 用户手册',
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
  dict(id='postsales/smb-lan-wlan-install', book='smb-lan-wlan-install', title='DT00XTE301 · SMB LAN & WLAN 安装配置',
       subtitle='Edition 04 · 512 页 · SMB 交付两日课（交换机+Stellar AP+Cirrus 云管全链路）',
       route=['设备开局与管理界面访问', 'PoE/VLAN/STP/LACP 有线基础', 'Stellar 三模式选型与 Wi-Fi 创建',
              'Cirrus 云管设备申报与员工/访客 SSID', '运维巡检'],
       groups=[
        ('开局', ['switch-first-setup', 'aos-config-management']),
        ('有线基础', ['vlan-port-assignment', 'poe-power-design', 'stp-lacp-basics']),
        ('无线与云管', ['stellar-mode-selection', 'ssid-security-design', 'guest-access-design', 'cirrus-onboarding']),
        ('运维', ['smb-troubleshooting']),
       ]),
  dict(id='postsales/smb-express-lan-wlan', book='smb-express-lan-wlan', title='DT00XTE310 · OmniSwitch 接入与 Stellar WLAN Express',
       subtitle='Edition 05 · 1083 页 · 五日交付全科（三部署模式+语音 WLAN+故障排查）',
       route=['AOS 文件/配置/固件管理', 'PoE/VLAN/VLAN 间路由', 'Stellar 三模式（Express/Enterprise/Cloud）',
              'Wi-Fi 业务全家桶（员工/访客/VLAN 分配/内置服务）', 'Voice over WLAN 五阶段'],
       groups=[
        ('交换机管理', ['aos-dual-partition-config-management', 'poe-management', 'vlan-inter-vlan-routing', 'switch-high-availability', 'qos-acl-access-guardian']),
        ('部署模式', ['stellar-deployment-mode-selection', 'wifi-express-operations', 'cirrus-cloud-management']),
        ('无线与排障', ['wireless-tech-fundamentals', 'voice-over-wlan-deployment', 'lan-wlan-troubleshooting']),
       ]),
  dict(id='postsales/ov2500-nms-admin', book='ov2500-nms-admin', title='DT00XTE311 · OmniVista 2500 NMS 管理',
       subtitle='Edition 09 · 581 页 · 网管平台管理全科（安装/发现/资源/统一接入/PolicyView/隔离）',
       route=['虚机安装与容量规划', 'Discovery 与拓扑/Locator', 'Resource Manager 与 CLI 脚本',
              'Unified Access 三层策略模型', 'PolicyView QoS 与 Quarantine'],
       groups=[
        ('平台与安装', ['ov-va-install-license', 'ov-ha-services-alerting', 'ov-switch-snmp-bootstrap']),
        ('发现与资源', ['ov-discovery-topology-locator', 'ov-resource-manager-provisioning', 'ov-cli-scripting-batch']),
        ('策略与监控', ['ov-unified-access', 'ov-policyview-qos', 'ov-quarantine-manager', 'ov-analytics-appvis-iot']),
       ]),
  dict(id='manuals/ov2500-userguide', book='ov2500-userguide', title='OmniVista 2500 4.9R2 User Guide',
       subtitle='935 页 · GUI 参考手册全科（控制台/Analytics/发现拓扑/资源管理/统一接入/UPAM/SSID 高级/隔离/VM 织构）',
       route=['控制台与仪表盘', 'Analytics 报表与 sFlow', 'Discovery 与三层拓扑',
              'Resource Manager 备份升级', 'Unified Access 与 UPAM 策略', 'SSID 高级与 VM/VXLAN 织构'],
       groups=[
        ('控制台与分析', ['ov-console-basics-dashboard', 'ov-analytics-reports']),
        ('发现与资源', ['ov-discovery-topology-views', 'ov-resource-manager-ops', 'ov-cli-scripting-mib']),
        ('接入与策略', ['ov-unified-access-profiles', 'ov-upam-guest-byod', 'ov-quarantine-policyview']),
        ('无线高级与织构', ['ov-wlan-ssid-advanced', 'ov-vm-vxlan-fabric']),
       ]),
  dict(id='postsales/ov-terra', book='ov-terra-deploy', title='DT00XTE317 · OmniVista Cirrus / Terra 部署与配置',
       subtitle='Edition 10 · 478 页 · 云管与本地部署平台（新流水线重制版，全文可溯源）',
       route=['平台选型与网络前置条件', 'Partner/MSP/Customer 三级账号与组织体系', 'Terra 3-VM K8s 部署链',
              'License 与 Trial 转正', 'AP/交换机 Onboarding 与激活排障', '无线下发/有线配置/RF 优化/监控运维'],
       groups=[
        ('平台与账号', ['platform-selection-prereqs', 'account-org-system']),
        ('部署与许可', ['terra-3vm-deployment', 'license-and-trial']),
        ('设备纳管', ['ap-onboarding', 'switch-onboarding']),
        ('业务与运维', ['wired-switch-config', 'wireless-service-delivery', 'rf-roaming-optimization', 'monitoring-operations']),
       ]),
  dict(id='postsales/dt00xte216-core-switching', book='os-lan-core-switching-v2', title='DT00XTE216 · OmniSwitch LAN R8 Core Switching',
       subtitle='Edition 15 · 724 页 · 核心交换专题（新流水线重制版：ERP/MACsec/PVLAN/MSTP/安全/OSPF/组播/BGP/SPB）',
       route=['ERP 环网保护与 MACsec 链路加密', 'Private VLAN/MSTP/MVRP 二层专题', 'ARP/DoS 防御与端口安全',
              'OSPF 区域设计与路由重分发', '组播/BGP/VRF/SPB Fabric', '平台运维'],
       groups=[
        ('二层专题', ['erp-ring-protection', 'macsec-link-encryption', 'private-vlan-isolation', 'mstp-load-sharing', 'mvrp-dynamic-vlan']),
        ('安全', ['arp-dos-defense', 'learned-port-security']),
        ('三层路由', ['ip-routing-fundamentals', 'ospf-area-redistribution', 'bgp-vrf-leak']),
        ('Fabric 与组播', ['spb-fabric', 'multicast-pim']),
        ('运维', ['switch-platform-ops']),
       ]),
  dict(id='postsales/dt00xte220-bootcamp', book='os-lan-bootcamp', title='DT00XTE220 · OmniSwitch R6/R8 Bootcamp',
       subtitle='Issue 25 · 1207 页 · 五天全科训练营（新流水线重制版，全文可溯源）',
       route=['产品矩阵与 Flash 双目录回滚', 'Stacking/VC 与 VLAN/LACP/STP 冗余', 'VRRP/QoS 策略引擎/AG-UNP/IoT/PoE',
              'RIP/OSPF 与安全/VRF/MACsec', '组播/ERP/SPB 智能织构'],
       groups=[
        ('开局与系统管理', ['aos-bootcamp-switch-fundamentals', 'aos-flash-config-management', 'aos-stacking-virtual-chassis']),
        ('二层基础与冗余', ['aos-vlan-l2-foundations', 'aos-lacp-stp-redundancy', 'aos-vrrp-first-hop-redundancy']),
        ('策略与准入', ['aos-qos-policy-engine', 'aos-access-guardian-unp-bootcamp', 'aos-poe-power']),
        ('路由与安全', ['aos-ip-routing-rip-ospf', 'aos-security-vrf-macsec']),
        ('组播与织构', ['aos-multicast-erp-spb']),
       ]),

  dict(id='aos/net-config', book='aos810-net-config', title='AOS 8.10R04 · Network Configuration',
       subtitle='1745 页 · 网络配置全科（二层/织构/IP 服务/路由/组播/QoS/准入/OAM，48 章）',
       route=['VLAN/QinQ 与冗余保护', 'SPB/MPLS/VXLAN 骨干', 'IP/IPv6/DHCP 服务',
              '组播与 QoS 策略', '准入安全与 OAM 监测'],
       groups=[
        ('二层与冗余', ['aos-nc-vlan-l2', 'aos-nc-redundancy-protection']),
        ('骨干织构', ['aos-nc-fabric-backbone']),
        ('三层与服务', ['aos-nc-ip-ipv6-services', 'aos-nc-routing', 'aos-nc-multicast']),
        ('策略与安全', ['aos-nc-qos-policy', 'aos-nc-access-security']),
        ('监测与基础', ['aos-nc-oam-monitoring', 'aos-nc-switch-foundation']),
       ]),
  dict(id='aos/switch-management', book='aos810-switch-mgmt', title='AOS 8.10R04 · Switch Management',
       subtitle='511 页 · 交换机管理（Flash/升级/CLI 用户/SNMP Web 纳管/日志健康/机箱 CMM）',
       route=['Flash 双目录与配置管理', '代码升级与 ISSU', 'CLI 会话与用户权限',
              'SNMP/Web/Cirrus 纳管', '日志健康与机箱管理'],
       groups=[
        ('配置与升级', ['aos-sm-flash-config', 'aos-sm-software-upgrade']),
        ('用户与纳管', ['aos-sm-cli-session-usermgmt', 'aos-sm-mgmt-services']),
        ('运维与硬件', ['aos-sm-logging-health', 'aos-sm-chassis-cmm']),
       ]),
  dict(id='aos/advanced-routing', book='aos810-adv-routing', title='AOS 8.10R04 · Advanced Routing',
       subtitle='313 页 · 高级路由（OSPF/OSPFv3/IS-IS/BGP/组播边界/DVMRP/PIM/MBR）',
       route=['OSPF 与 OSPFv3 区域设计', 'IS-IS', 'BGP 与策略（本书重点）',
              '组播高级（PIM/DVMRP/MBR）', 'Route Map 策略工具箱'],
       groups=[
        ('IGP', ['aos-ar-ospf-ospfv3', 'aos-ar-isis']),
        ('BGP 与策略', ['aos-ar-bgp', 'aos-ar-policy-toolbox']),
        ('组播高级', ['aos-ar-multicast-advanced']),
       ]),
  dict(id='aos/cli-reference', book='aos810-cli-reference', title='AOS 8.10R04 · CLI Reference 命令地图',
       subtitle='6240 页 · 70 章命令字典导航（约 2480 条命令，按 5 域组织）',
       route=['L2 接入域命令', 'Fabric 骨干域命令', '路由域命令',
              '组播/QoS/准入域命令', '管理与 OAM 域命令'],
       groups=[
        ('二层与接入', ['aos-cli-map-l2-access']),
        ('骨干与路由', ['aos-cli-map-fabric', 'aos-cli-map-routing']),
        ('策略与运维', ['aos-cli-map-multicast-qos', 'aos-cli-map-mgmt-oam']),
       ]),
  dict(id='aos/release-notes', book='aos810-release-notes', title='AOS 8.10R04 · Release Notes',
       subtitle='105 页 · 版本说明（升级方法论/Secure Boot/已知问题库/新特性与废弃）',
       route=['升级路径与固件三件套', 'Secure Boot 与包管理', 'Open CR 已知问题排障库', '新特性与废弃变更'],
       groups=[
        ('升级与安全', ['aos-rn-upgrade-path', 'aos-rn-secure-boot']),
        ('问题与特性', ['aos-rn-known-issues', 'aos-rn-new-features-deprecations']),
       ]),
  dict(id='aos/specifications', book='aos810-specifications', title='AOS 8.10R04 · Specifications Guide',
       subtitle='98 页 · 规格指南（平台三梯队/容量红线/TCAM 分配/特性矩阵）',
       route=['平台梯队与规格解读', 'VC/织构/路由容量红线', 'TCAM 零和分配与特性缺口'],
       groups=[
        ('平台与容量', ['aos-spec-platform-tiers', 'aos-spec-capacity-limits']),
        ('TCAM 与特性', ['aos-spec-tcam-features']),
       ]),
  dict(id='aos/transceivers', book='aos810-transceivers', title='AOS 8.10R04 · Transceivers Guide',
       subtitle='107 页 · 光模块指南（1G-400G 型号矩阵/平台兼容/DDM 安装纪律）',
       route=['模块型号与速率距离矩阵', '平台兼容与硬件修订陷阱', 'DDM 监控与安装纪律'],
       groups=[
        ('选型', ['aos-tx-module-matrix', 'aos-tx-platform-compat']),
        ('运维', ['aos-tx-ddm-install']),
       ]),
  dict(id='hardware/os6360', book='hw-6360', title='OmniSwitch 6360 Hardware Guide',
       subtitle='Rev J · 83 页 · 入门千兆接入（10 机型/内置电源/PoE 三环）',
       route=['P/PX/H 命名解码', 'combo 与 10G 许可口', 'PoE 三环与 Fast/Perpetual'],
       groups=[
        ('机型与端口', ['os6360-model-ports']),
        ('安装与电源', ['os6360-install-power']),
        ('运维排障', ['os6360-ops-troubleshoot']),
       ]),
  dict(id='hardware/os6465', book='hw-6465', title='OmniSwitch 6465 Hardware Guide',
       subtitle='Rev V · 99 页 · 工业加固（宽温三档/DIN-DNV 安装/告警继电器）',
       route=['工业线/运输线双线', '宽温与 PoE 温度降额', 'DIN/DUO/DNV 三套件与 ROJ 接线'],
       groups=[
        ('机型与端口', ['os6465-model-ports']),
        ('安装与电源', ['os6465-install-power']),
        ('运维排障', ['os6465-ops-troubleshoot']),
       ]),
  dict(id='hardware/os6560', book='hw-6560', title='OmniSwitch 6560 Hardware Guide',
       subtitle='Rev P · 111 页 · 多千兆 bt 接入（2.5G/5G/双 PX 1565W/DNV）',
       route=['Z/E 命名与 5G 口位', '三档热换电源与混插规则', 'lanpower 全家桶与 Dying Gasp'],
       groups=[
        ('机型与端口', ['os6560-model-ports']),
        ('安装与电源', ['os6560-install-power']),
        ('运维排障', ['os6560-ops-troubleshoot']),
       ]),
  dict(id='hardware/os6570', book='hw-6570', title='OmniSwitch 6570M Hardware Guide',
       subtitle='Rev G · 59 页 · 千兆接入（12/12D/U28/半宽并装）',
       route=['三机型选型', '双层电源架构', 'DG 三通道与温度阈值分化'],
       groups=[
        ('机型与端口', ['os6570-model-ports']),
        ('安装与电源', ['os6570-install-power']),
        ('运维排障', ['os6570-ops-troubleshoot']),
       ]),
  dict(id='hardware/os6575', book='hw-6575', title='OmniSwitch 6575 Hardware Guide',
       subtitle='Rev A · 86 页 · 工业无风扇（M12 连接器/温度阶梯预算/Alarm Relay）',
       route=['P12/U28/MP16 形态选型', '四款电源与 ROJ 接线', '告警继电器与 Port Bypass'],
       groups=[
        ('机型与端口', ['os6575-model-ports']),
        ('安装与电源', ['os6575-install-power']),
        ('运维排障', ['os6575-ops-troubleshoot']),
       ]),
  dict(id='hardware/os6860', book='hw-6860', title='OmniSwitch 6860/6860E/6860N Hardware Guide',
       subtitle='Rev W · 115 页 · 三代 15 机型（20G VC→QSFP28 VFL/七款电源）',
       route=['三代命名与 VFL 演进', 'N 型预算矩阵与 2000W 降额', 'DG PDU 挤占公式与反向优先级'],
       groups=[
        ('机型与端口', ['os6860-model-ports']),
        ('安装与电源', ['os6860-install-power']),
        ('运维排障', ['os6860-ops-troubleshoot']),
       ]),
  dict(id='hardware/os6865', book='hw-6865', title='OmniSwitch 6865 Hardware Guide',
       subtitle='Rev Y · 76 页 · 加固型（无风扇宽温/五形态安装/军规 DC 极性）',
       route=['P16X/U12X/U28X 选型', '高温预算腰斩', 'DC 极性军规与 LED 判读'],
       groups=[
        ('机型与端口', ['os6865-model-ports']),
        ('安装与电源', ['os6865-install-power']),
        ('运维排障', ['os6865-ops-troubleshoot']),
       ]),
  dict(id='hardware/os6870', book='hw-6870', title='OmniSwitch 6870 Hardware Guide',
       subtitle='Rev D · 85 页 · 九机型（QSFP56 200G/混插扩容/四色 LED）',
       route=['M/Z/V/CNI/LNI 分类', '200G 阶梯与允许混插', 'Class 5-8 与上电七步'],
       groups=[
        ('机型与端口', ['os6870-model-ports']),
        ('安装与电源', ['os6870-install-power']),
        ('运维排障', ['os6870-ops-troubleshoot']),
       ]),
  dict(id='hardware/os6900', book='hw-6900v2', title='OmniSwitch 6900 Hardware Guide',
       subtitle='Rev C · 90 页 · 模块化机箱（端口组锁速/QSFP-DD 十二态/两代电源）',
       route=['十机型矩阵与 NI 板卡', '深机箱三方案与气流', '热插拔与十二态 LED'],
       groups=[
        ('机箱与板卡', ['os6900-chassis-modules']),
        ('安装与电源', ['os6900-install-power']),
        ('运维排障', ['os6900-ops-troubleshoot']),
       ]),
  dict(id='hardware/os9900', book='hw-9900', title='OmniSwitch 9900 Hardware Guide',
       subtitle='Rev S · 74 页 · 核心机箱（9907/9912/CMM-CFM 矩阵/VC-of-2）',
       route=['9907/9912 与 NI 禁用清单', 'N+1 冗余与三不混', '热插拔节律与五灯诊断'],
       groups=[
        ('机箱与板卡', ['os9900-chassis-modules']),
        ('安装与电源', ['os9900-install-power']),
        ('运维排障', ['os9900-ops-troubleshoot']),
       ]),
  dict(id='brochures/nms', book='bp-nms-brochures', title='ALE 网管与安全 · 官方彩页',
       subtitle='2026-08 快照 · 5 份 23 页 · OmniVista 双形态/订阅/Fleet/Milestone/Advisor',
       route=['Cirrus/Terra 双形态选型', '订阅与维保边界', 'Fleet Supervision 免费切入点', 'Advisor 与 Smart Tool'],
       groups=[
        ('平台与工具', ['bp-ov2500-nms-datasheet', 'bp-network-advisor-datasheet', 'bp-fleet-supervision-sheet']),
        ('方案页', ['bp-milestone-plugin-sheet', 'bp-smart-tool-sheet']),
       ]),
  dict(id='brochures/stellar-ap', book='bp-stellar-ap-datasheets', title='OmniAccess Stellar WLAN · 官方数据表',
       subtitle='2026-08 快照 · 14 份 128 页 · AP1261-AP1570 全系选型速查',
       route=['Wi-Fi 7 旗舰（1540/1561/1570）', 'Wi-Fi 7 中端（1501/1511/1521）', 'Wi-Fi 6E（1431/1451）',
              'Wi-Fi 6 系列（1301-1360）', 'Wi-Fi 5 系列（1261） · 一表一技能'],
       groups=[
        ('Wi-Fi 7 旗舰（1540/1561/1570）', ['bp-ap1540-datasheet', 'bp-ap1561-datasheet', 'bp-ap1570-datasheet']),
        ('Wi-Fi 7 中端（1501/1511/1521）', ['bp-ap1501-datasheet', 'bp-ap1511-datasheet', 'bp-ap1521-datasheet']),
        ('Wi-Fi 6E（1431/1451）', ['bp-ap1431-datasheet', 'bp-ap1451-datasheet']),
        ('Wi-Fi 6 系列（1301-1360）', ['bp-ap1301-datasheet', 'bp-ap1301h-datasheet', 'bp-ap1331-datasheet', 'bp-ap1351-datasheet', 'bp-ap1360-datasheet']),
        ('Wi-Fi 5 系列（1261）', ['bp-ap1261-datasheet']),
       ]),
  dict(id='brochures/omniswitch', book='bp-omniswitch-datasheets', title='OmniSwitch · 官方数据表',
       subtitle='2026-08 快照 · 15 份 158 页 · OS2260-OS9900 全系选型速查',
       route=['接入层 SMB（2260/2360）', '接入千兆（6360/6370/6570M）', '多千兆与工业（6560/6465/6465T/6575）', '汇聚（6860/6865）', '核心（6870/6900/6920/9900）'],
       groups=[
        ('接入层 SMB', ['bp-os2260-datasheet', 'bp-os2360-datasheet']),
        ('接入层千兆', ['bp-os6360-datasheet', 'bp-os6370-datasheet', 'bp-os6570m-datasheet']),
        ('接入层多千兆与工业', ['bp-os6560e-datasheet', 'bp-os6465-datasheet', 'bp-os6465t-datasheet', 'bp-os6575-datasheet']),
        ('汇聚', ['bp-os6860-datasheet', 'bp-os6865-datasheet']),
        ('核心', ['bp-os6870-datasheet', 'bp-os6900-datasheet', 'bp-os6920-datasheet', 'bp-os9900-datasheet']),
       ]),
  dict(id='solutions/spb', book='sol-spb', title='SPB 智能织构 · 架构与部署',
       subtitle='3 份 86 页 · Tech Brief + 部署指南 + 方案简报（IS-IS SPB/I-SID/VRRP tracking/客户案例）',
       route=['IS-IS SPB 控制面机制', 'I-SID 二层与 VRF 三层服务', '部署 11 步流程', '卖点与客户案例'],
       groups=[
        ('架构与服务', ['sol-spb-architecture', 'sol-spb-l2-l3-services']),
        ('部署与案例', ['sol-spb-deployment-flow', 'sol-spb-positioning-cases']),
       ]),
  dict(id='solutions/campus-architecture', book='sol-campus-architecture', title='园区网络架构 · 设计指南',
       subtitle='2 份 47 页 · 园区架构指南 + Hybrid POL 彩页（分层设计/AP 发现/漫游/NMS/POL）',
       route=['园区分层 LAN/WLAN 设计', 'AP 发现与漫游判定', 'NMS 与安全', 'POL 光园区'],
       groups=[
        ('设计与运维', ['sol-campus-lan-wlan-design', 'sol-campus-nms-security']),
        ('POL 方案', ['sol-campus-hybrid-pol']),
       ]),
  dict(id='solutions/evpn-architecture', book='sol-evpn-architecture', title='EVPN 架构指南',
       subtitle='1 份 73 页 · BGP EVPN（Route Types/多归属五机制/IRB/OISM 组播）',
       route=['BGP EVPN 控制面', '多归属五机制', 'IRB 与组播/外部连通'],
       groups=[
        ('控制面', ['sol-evpn-control-plane']),
        ('数据面', ['sol-evpn-multi-homing', 'sol-evpn-irb-multicast']),
       ]),
  dict(id='solutions/mpls-reference', book='sol-mpls-reference', title='MPLS 参考设计指南',
       subtitle='1 份 45 页 · MPLS/VPLS/VPWS（双标签/LDP/VPLS 信令/QoS/OAM）',
       route=['双标签与 LDP', 'VPLS/VPWS 业务', 'QoS/OAM 与 AOS 边界'],
       groups=[
        ('基础与业务', ['sol-mpls-foundation', 'sol-mpls-vpls-vpws']),
        ('运维', ['sol-mpls-qos-oam']),
       ]),
  dict(id='solutions/erp-switching', book='sol-erp-switching', title='ERP 环网保护 · 应用笔记',
       subtitle='1 份 17 页 · G.8032（RPL/R-APS/定时器/多环设计）',
       route=['环网机制与定时器', '多环设计与选型对比'],
       groups=[
        ('机制', ['sol-erp-ring-mechanism']),
        ('设计', ['sol-erp-multi-ring-design']),
       ]),
  dict(id='solutions/guest-tunneling', book='sol-guest-tunneling', title='访客流量隧道 GTTS · 应用笔记',
       subtitle='1 份 19 页 · Guest Traffic Tunnelling（L2 GRE/DMZ/多租户/四种冗余）',
       route=['GTTS 机制与配置', '部署场景', '四种冗余设计'],
       groups=[
        ('机制与配置', ['sol-gtts-architecture-config']),
        ('场景与冗余', ['sol-gtts-deployment-scenarios', 'sol-gtts-redundancy-designs']),
       ]),
  dict(id='solutions/network-security', book='sol-network-security', title='网络基础设施安全 · Tech Brief',
       subtitle='2 份 100 页 · 安全 Tech Brief + 白皮书（五层框架/三平面加固/NLM 生命周期）',
       route=['五层框架与三平面', '协议加固与替换', '管理面准入', 'NLM 生命周期'],
       groups=[
        ('框架与加固', ['sol-sec-five-layer-framework', 'sol-sec-protocol-hardening']),
        ('准入与运维', ['sol-sec-device-access', 'sol-sec-nlm-lifecycle']),
       ]),
  dict(id='solutions/wlan-design', book='sol-wlan-design', title='Stellar WLAN 设计与调优',
       subtitle='3 份 75 页 · 高密设计指南 + 微调最佳实践 + 部署服务表',
       route=['高密设计五步法', 'RF 微调七要点', '三级配置层次'],
       groups=[
        ('设计', ['sol-wlan-high-density', 'sol-wlan-fine-tuning']),
        ('配置', ['sol-wlan-profile-hierarchy']),
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
    # 密集段落要点化（渲染层，全站生效）：标题/小节下的整段长文按句号拆成 bullet，便于扫读
    def bulletize(m):
        head, para = m.group(1), m.group(2).strip()
        if para.startswith(('- ', '* ', '1.', '|', '!', '>')):
            return m.group(0)
        # 单句叙事短段（<100 字）保持段落原样，避免过度碎片化
        sents = [s.strip() for s in para.split('。') if s.strip()]
        if len(sents) < 2 or len(para) < 100:
            return m.group(0)
        return head + '\n' + '\n'.join(f'- {s}。' for s in sents) + '\n'
    text = _re.sub(r'(^#{1,3}\s*[^\n]+\n+)([^\n#\-*|!>][^\n]*)', bulletize, text, flags=_re.M)
    # 密集长列表项拆分：'1. **标题**——句。解释a。解释b。' → 标题句保留，其余降为嵌套子要点
    def split_item(m):
        prefix, content = m.group(1), m.group(2).strip()
        if len(content) < 160 or content.startswith('!['):
            return m.group(0)
        def rtail(s):
            return s.strip().rstrip('。；;、，,')
        parts = [p.strip() for p in content.split('。') if p.strip()]
        sep = '。'
        if len(parts) < 3:
            # 单句但含多个分号：按分号拆
            parts = [p.strip() for p in content.split('；') if p.strip()]
            sep = '；'
        if len(parts) < 3 and len(content) >= 240:
            # 超长枚举句：按顿号拆（不带尾标点）
            parts = [p.strip() for p in content.split('、') if p.strip()]
            sep = ''
        if len(parts) < 3:
            return m.group(0)
        parts = [p.replace('**', '') for p in parts]
        indent = '    ' if prefix[0].isdigit() else '   '
        return (prefix + rtail(parts[0]) + sep + '\n'
                + '\n'.join(f'{indent}- {rtail(p)}{sep}' for p in parts[1:]) + '\n')
    # 粗体编号归位为真列表：'**1. 标题** 内容' → '1. **标题** 内容'
    text = _re.sub(r'^\*\*(\d+)\.\s*([^*\n]+)\*\*', r'\1. **\2**', text, flags=_re.M)
    text = _re.sub(r'^(?:^)(\*\*\d+\.\s*|\d+\.\s+|\-\s+)([^\n]+)$', split_item, text, flags=_re.M)
    # 块级要点化：按空行分块；密集普通段落块转列表，多行长列表项合并后拆子要点
    def block_bulletize(text):
        out_blocks = []
        for block in _re.split(r'\n\s*\n', text):
            s = block.strip()
            mli = _re.match(r'^(\d+\.|\-)\s+(.+)$', s, _re.S)
            if mli and len(s) > 200 and not _re.search(r'\n\s*[-*]\s', s):
                joined = _re.sub(r'\n\s*', ' ', s)
                m2 = _re.match(r'^(\d+\.|\-)\s+(.+)$', joined)
                prefix, content = m2.group(1), m2.group(2)
                parts = [p.strip().replace('**', '') for p in content.split('。') if p.strip()]
                if len(parts) >= 3:
                    indent = '    ' if prefix[0].isdigit() else '   '
                    def rt(x): return x.rstrip('。；;、，,')
                    out_blocks.append(prefix + ' ' + rt(parts[0]) + '。\n'
                                      + '\n'.join(f'{indent}- {rt(p)}。' for p in parts[1:]))
                    continue
            if (len(s) > 200 and s.count('。') >= 3
                    and not s.startswith(('#', '|', '-', '*', '!', '>', '`', '1.', '2.', '3.', '4.'))
                    and not _re.match(r'^\d+\.\s', s)):
                sents = [x.strip() for x in s.replace('\n', '').split('。') if x.strip()]
                if len(sents) >= 3:
                    out_blocks.append('\n'.join(f'- {x}。' for x in sents))
                    continue
            out_blocks.append(block)
        return '\n\n'.join(out_blocks)
    text = block_bulletize(text)
    # 要点行"观点：解释"分层：观点短语加粗独占一行，解释换行跟随（≤40 字观点才判定为 lead）
    def lead_split(m):
        lead, rest = m.group(1).strip(), m.group(2).strip()
        if not rest or lead.startswith('**'):
            return m.group(0)
        visible = _re.sub(r'<[^>]+>', '', lead)
        if len(visible) > 52:
            return m.group(0)
        return f'- **{lead}**：<br>{rest}'
    text = _re.sub(r'^- ([^：*\n]{2,240})：(.+)$', lead_split, text, flags=_re.M)
    # 无结构的超长普通行（技能清单/枚举）：≥4 个 ' / ' 分隔时按斜杠拆行
    def slash_split(m):
        parts = [p.strip() for p in m.group(0).split(' / ')]
        if len(parts) < 4:
            return m.group(0)
        return parts[0] + '：\n' + '\n'.join(f'- {p}' for p in parts[1:])
    text = _re.sub(r'^[^\n#\-*|!>`][^\n]{160,}$', lambda m: slash_split(m) if ' / ' in m.group(0) else m.group(0), text, flags=_re.M)
    # 页码标记渲染为紧凑徽章：<<<PAGE 13>>> / <<<PAGE 13-15>>> / <<<PAGE 1, 4>>>
    text = _re.sub(r'<<<PAGE\s+([\d,\s\-]+)>>>', lambda m: f'<span class="pg">原文p{m.group(1).strip()}</span> ', text)
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
    h = md.convert(preprocess(text))
    # 表格包横向滚动层：窄屏滚动查看，宽屏自动占满，避免挤压变形
    return h.replace('<table>', '<div class="twrap"><table>').replace('</table>', '</table></div>')

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
:root{--bg:#f7f7f5;--panel:#ffffff;--card:#ffffff;--tx:#1a1a1a;--mut:#75787B;--acc:#6B489D;--acc2:#4F3478;--line:#D9D9D6;
--ale-blue:#0085CA;--ale-teal:#00B2A9;--ale-orange:#FF4500;--ale-red:#A50034;--purple-light:#F1ECF7}
*{box-sizing:border-box}
body{margin:0;font-family:"Trebuchet MS","Noto Sans SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--tx);line-height:1.75}
a{color:var(--acc);text-decoration:none} a:hover{text-decoration:underline}
.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(480px,1fr));gap:18px;margin:16px 0}
.gallery figure{margin:0;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px}
.gallery img{display:block;width:100%;height:auto;max-height:480px;object-fit:contain;background:#fff;border-radius:6px}
.gallery figcaption{font-size:12.5px;color:var(--mut);text-align:center;margin-top:6px}
/* 顶部品牌导航 */
.topbar{background:#fff;border-bottom:3px solid var(--acc);padding:0 28px;display:flex;align-items:center;gap:22px;height:62px;position:sticky;top:0;z-index:50}
.topbar img.logo{height:34px;width:auto}
.topbar .site-name{font-size:15px;font-weight:700;color:var(--acc2);white-space:nowrap}
.topbar nav{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}
.topbar nav a{color:var(--tx);font-size:14px;padding:6px 12px;border-radius:6px}
.topbar nav a:hover{background:var(--purple-light);color:var(--acc);text-decoration:none}
.topbar nav a.on{background:var(--purple-light);color:var(--acc);font-weight:700}
@media(max-width:860px){.topbar{flex-wrap:wrap;height:auto;padding:8px 14px}.topbar .site-name{display:none}}
/* 侧栏折叠 + 图片灯箱 */
.tgl{position:fixed;left:0;top:45%;z-index:60;background:#fff;border:1px solid var(--line);border-right:none;border-radius:0 8px 8px 0;color:var(--tx);padding:10px 6px;cursor:pointer;font-size:13px;line-height:1.1;writing-mode:vertical-lr}
.tgl:hover{background:var(--acc);color:#fff}
.layout.full{grid-template-columns:minmax(0,1fr)}
.layout.full aside{display:none}
.layout.full main{grid-column:1}
.lb{position:fixed;inset:0;background:rgba(18,12,30,.93);backdrop-filter:blur(3px);z-index:100;display:flex;align-items:center;justify-content:center;flex-direction:column;cursor:zoom-out}
.lb img{max-width:92vw;max-height:80vh;background:#fff;border-radius:8px;box-shadow:0 18px 60px rgba(0,0,0,.55);transition:transform .1s ease-out;cursor:grab;user-select:none;-webkit-user-drag:none}
.lb img.grabbing{cursor:grabbing;transition:none}
.lb .lbb{margin-top:14px;display:flex;gap:8px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);border-radius:30px;padding:5px 8px}
.lb button{background:transparent;border:none;color:#EDE7F6;border-radius:20px;padding:6px 14px;cursor:pointer;font-size:14px}
.lb button:hover{background:var(--acc);color:#fff}
.lb .zoom{color:#CBB8E8;font-size:12.5px;line-height:32px;padding:0 8px;min-width:52px;text-align:center;font-variant-numeric:tabular-nums}
.search{margin:0 0 14px}
.search input{width:100%;padding:7px 10px;border-radius:8px;border:1px solid var(--line);background:#fff;color:var(--tx);font-size:13px;outline:none}
.search input:focus{border-color:var(--acc)}
#qres{max-height:340px;overflow-y:auto;margin-top:6px}
#qres .qi{display:block;padding:6px 8px;border-radius:6px;font-size:12.5px;color:var(--tx);border-left:2px solid transparent}
#qres .qi:hover{background:var(--purple-light);text-decoration:none;border-left-color:var(--acc)}
#qres .qi .qp{color:var(--mut);font-size:11px;display:block}
#qres .qi b{color:var(--acc)}
.pg{display:inline-block;font-size:11px;line-height:1;padding:2px 6px;border-radius:8px;background:var(--purple-light);color:var(--acc);border:1px solid #E0D3EE;vertical-align:1px;white-space:nowrap}
main img{max-width:100%;border-radius:8px;border:1px solid var(--line);margin:8px 0;background:#fff}
.layout{display:grid;grid-template-columns:260px minmax(0,1fr);min-height:calc(100vh - 62px);max-width:1600px;margin:0 auto;width:100%}
aside{background:var(--panel);padding:20px 14px;border-right:1px solid var(--line);position:sticky;top:62px;height:calc(100vh - 62px);overflow-y:auto}
aside h1{font-size:17px;margin:0 0 4px} aside .sub{font-size:12px;color:var(--mut);margin-bottom:18px}
aside .grp{font-size:11px;letter-spacing:.1em;color:var(--mut);margin:16px 0 6px;text-transform:uppercase}
aside a{display:block;padding:6px 10px;border-radius:6px;color:var(--tx);font-size:14px}
aside a:hover{background:var(--purple-light);text-decoration:none}
aside a.on{background:var(--purple-light);color:var(--acc)}
main{padding:32px 48px 48px;max-width:1120px;width:100%;justify-self:center}
h1{font-size:28px;border-bottom:2px solid var(--line);padding-bottom:10px}
h2{margin-top:34px;color:var(--acc)} h3{color:var(--acc2)}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:14px}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left}
.twrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
.twrap table{margin:14px 0;min-width:640px}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left}
th{background:#EFEFEA} tr:nth-child(even) td{background:#F4F3EF}
code{background:var(--purple-light);padding:1px 6px;border-radius:4px;font-size:.92em;color:var(--acc2)}
pre{background:#231a35;border:1px solid var(--line);padding:14px;border-radius:8px;overflow-x:auto}
pre code{background:none;padding:0;color:#E8E1F2}
blockquote{border-left:4px solid var(--acc);background:var(--purple-light);margin:12px 0;padding:8px 16px;border-radius:0 8px 8px 0}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin:20px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:18px;transition:border-color .15s,box-shadow .15s;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.card:hover{border-color:var(--acc);box-shadow:0 3px 10px rgba(107,72,157,.14)} .card a{font-weight:600;font-size:16px;color:var(--acc2)}
.card p{font-size:13px;color:var(--mut);margin:8px 0 0}
.meta{font-size:13px;color:var(--mut)}
hr{border:none;border-top:1px solid var(--line);margin:26px 0}
.badge{display:inline-block;background:var(--ale-teal);color:#fff;font-size:12px;border-radius:20px;padding:1px 10px;font-weight:700}
.badge.soon{background:#FFF1EB;color:var(--ale-orange);border:1px solid #FFD6C2}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px!important}
.chip{display:inline-block;font-size:11.5px;line-height:1;padding:3px 8px;border-radius:6px;background:#F4F3EF;color:#5B5E61;border:1px solid #E4E3DE;white-space:nowrap}
.gcards{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px;margin:20px 0;align-items:start}
.gcard{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;box-shadow:0 1px 3px rgba(0,0,0,.05);grid-column:1/-1}
.gcard h3{margin:0 0 10px;font-size:15px;color:var(--acc);border-left:3px solid var(--acc);padding-left:8px;line-height:1.3}
.gcard .gwrap{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
@media(max-width:900px){.gcard .gwrap{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){.gcard .gwrap{grid-template-columns:1fr}}
.gskill{display:block;padding:9px 10px;border-radius:8px;font-size:14px;color:var(--tx);border:1px solid var(--line);background:#FBFAFD;height:100%}
.gskill:hover{background:var(--purple-light);border-color:#E0D3EE;text-decoration:none}
.gskill b{color:var(--acc2);font-weight:600}
.gskill .gslug{display:block;font-size:11px;color:var(--mut);font-family:Consolas,monospace;margin-top:1px}
.gskill .gdesc{display:block;font-size:12px;color:var(--mut);margin-top:3px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}
main p,main li,main td{overflow-wrap:break-word;word-break:break-word}
main{padding:28px 44px 40px}
h1{font-size:26px}h2{margin-top:30px;padding-top:10px;border-top:1px solid var(--line)}h3{margin-top:22px}
blockquote p{margin:6px 0}
.crumbs{font-size:13px;color:var(--mut);margin:0 0 14px}
.crumbs a{color:var(--acc)}
.pn{display:flex;justify-content:space-between;gap:12px;margin-top:36px;padding-top:14px;border-top:1px solid var(--line)}
.pn a{flex:1;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 14px;font-size:14px}
.pn a:hover{border-color:var(--acc)}
.pn .nxt{text-align:right}
.foot{margin-top:34px;font-size:12px;color:var(--mut);border-top:1px solid var(--line);padding-top:10px}
@media(max-width:1180px){.layout{grid-template-columns:220px minmax(0,1fr)}main{padding:24px 28px}}
@media(max-width:800px){.layout{grid-template-columns:1fr}aside{position:static;height:auto}main{padding:16px 18px}.twrap table{min-width:520px}}
"""

# ============ 顶部品牌导航 / 分类 Banner ============
NAV_ITEMS = [('首页', 'index.html'), ('学习路径', 'paths.html'), ('售前', 'presales/index.html'), ('售后', 'postsales/index.html'),
             ('无线', 'wlan/index.html'), ('AOS 手册', 'aos/index.html'), ('硬件', 'hardware/index.html'),
             ('彩页', 'brochures/index.html'), ('解决方案', 'solutions/index.html')]

def topbar(pfx='', active=''):
    def on(h):
        return ' class="on"' if (active and h != 'index.html' and h.startswith(active + '/')) or (not active and h == 'index.html') else ''
    links = ''.join(f'<a href="{pfx}{h}"{on(h)}>{n}</a>' for n, h in NAV_ITEMS)
    return (f'<header class="topbar"><a href="{pfx}index.html"><img class="logo" src="{pfx}assets/ale-logo-color.png" alt="Alcatel-Lucent Enterprise"></a>'
            f'<span class="site-name">技术培训门户</span><nav>{links}</nav></header>')

# 分类 → Banner 图（PBG-2026 模板素材，ALE 品牌紫色调）
CAT_BANNER = {'presales': 'banner-presales.jpg', 'postsales': 'banner-postsales.jpg', 'wlan': 'banner-wlan.jpg',
              'aos': 'banner-aos.jpg', 'hardware': 'banner-hardware.jpg', 'brochures': 'banner-brochures.jpg',
              'manuals': 'banner-manuals.jpg', 'solutions': 'banner-solutions.jpg'}

HERO_CSS = """
.hero{position:relative;background:linear-gradient(118deg,#4F3478 0%,#6B489D 55%,#7E5CB4 100%);color:#fff;
padding:56px 32px 88px;overflow:hidden}
.hero .inner{position:relative;z-index:2;max-width:1080px;margin:0 auto;display:flex;gap:36px;align-items:center;flex-wrap:wrap}
.hero img.hlogo{height:44px;margin-bottom:14px}
.hero h1{font-size:36px;border:none;color:#fff;margin:0 0 6px;padding:0}
.hero p{color:#E9E1F4;margin:6px 0 0;max-width:560px}
.hero .cta{margin-top:22px;display:flex;gap:12px;flex-wrap:wrap}
.hero .cta a{background:#fff;color:#4F3478;border-radius:8px;padding:10px 22px;font-weight:700;font-size:15px}
.hero .cta a:hover{text-decoration:none;background:#F1ECF7}
.hero .cta a.ghost{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.6)}
.hero .cta a.ghost:hover{background:rgba(255,255,255,.12)}
.hero .side{flex:0 0 380px;max-width:100%}
.hero .side img{width:100%;border-radius:12px;box-shadow:0 10px 30px rgba(0,0,0,.28);border:none;margin:0}
.hero svg.wave{position:absolute;left:0;right:0;bottom:-2px;width:100%;z-index:1}
.hsearch{margin-top:18px;max-width:560px}
.hsearch input{width:100%;padding:11px 14px;border-radius:10px;border:none;font-size:14px;outline:none;background:#fff}
.hsearch #qres{max-height:340px;overflow-y:auto;margin-top:6px;background:#fff;border-radius:10px}
.hsearch #qres .qi{display:block;padding:8px 12px;font-size:13px;color:var(--tx);border-left:3px solid transparent}
.hsearch #qres .qi:hover{background:var(--purple-light);text-decoration:none;border-left-color:var(--acc)}
.hsearch #qres .qi .qp{color:var(--mut);font-size:11px;display:block}
.hsearch #qres .qi b{color:var(--acc)}
.tasks{max-width:1080px;margin:-38px auto 0;padding:0 32px;position:relative;z-index:3;display:grid;
grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px}
.tasks a{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 16px;font-size:14px;
color:var(--tx);box-shadow:0 3px 10px rgba(79,52,120,.08)}
.tasks a:hover{border-color:var(--acc);text-decoration:none;color:var(--acc)}
.tasks a b{display:block;font-size:15px;color:var(--acc2)}
.tasks a span{font-size:12px;color:var(--mut)}
.catbanner{position:relative;border-radius:12px;overflow:hidden;margin:0 0 22px;max-height:220px}
.catbanner img{width:100%;height:220px;object-fit:cover;display:block;margin:0;border:none;border-radius:0}
.catbanner .ov{position:absolute;inset:0;background:linear-gradient(90deg,rgba(52,32,84,.88) 0%,rgba(79,52,120,.62) 55%,rgba(79,52,120,.15) 100%)}
.catbanner .tt{position:absolute;left:28px;bottom:20px;color:#fff}
.catbanner .tt h1{color:#fff;border:none;margin:0;padding:0;font-size:26px}
.catbanner .tt p{color:#E9E1F4;margin:4px 0 0;font-size:13px}
@media(max-width:700px){.hero{padding:36px 18px 76px}.hero .side{display:none}.tasks{padding:0 14px;margin-top:-30px}}
"""

def hero_section():
    wave = ('<svg class="wave" viewBox="0 0 1440 90" preserveAspectRatio="none">'
            '<path d="M0,50 C240,95 480,0 720,35 C960,70 1200,15 1440,55 L1440,90 L0,90 Z" fill="#f7f7f5"/></svg>')
    return f"""<div class="hero"><div class="inner">
<div><img class="hlogo" src="assets/ale-logo-white.png" alt="Alcatel-Lucent Enterprise">
<h1>ALE Networking 技术培训门户</h1>
<p>面向售前、售后和网络工程师的产品、部署与排障知识中心</p>
<div class="hsearch"><input id="qk" type="search" placeholder="🔍 搜索课程编号 / 产品型号 / 技术关键词，如 DT00XTE221、SPB、OmniSwitch 6860…" autocomplete="off"><div id="qres"></div></div>
<div class="cta"><a href="#catalog">开始学习</a><a class="ghost" href="#catalog">查找资料</a></div></div>
<div class="side"><img src="assets/banner-wlan.jpg" alt="ALE 网络技术"></div>
</div>{wave}</div>
<div class="tasks">
<a href="presales/index.html"><b>我是售前工程师</b><span>选型 · 彩页 · 方案与报价</span></a>
<a href="postsales/index.html"><b>我是售后工程师</b><span>部署 · 配置 · 排障手册</span></a>
<a href="hardware/os6860/index.html"><b>我要做产品选型</b><span>机型矩阵 · 硬件指南 · 数据表</span></a>
<a href="postsales/os-lan-troubleshooting/index.html"><b>我要排查故障</b><span>有线/无线排障 · 已知问题库</span></a>
<a href="solutions/index.html"><b>我要设计方案</b><span>SPB/EVPN/MPLS · 园区架构</span></a>
<a href="paths.html"><b>不知道从哪学起</b><span>售前 / 售后 / WLAN 学习路径</span></a>
</div>"""

# ============ 学习路径（第二阶段） ============
LEARNING_PATHS = [
    ('售前工程师路径', '从产品体系到方案报价，建立卖点弹药库', 'banner-presales.jpg', [
        ('ALE 产品体系与全系选型速查', 'OmniSwitch / Stellar AP 全系数据表，先建立产品地图', 'brochures/omniswitch/index.html'),
        ('OmniSwitch 机型定位与选型', '机型定位表 → 功能矩阵 → VC vs 机箱', 'presales/campus-lan/index.html'),
        ('Stellar WLAN 产品与场景', 'AP 三维选型矩阵、三管理模式、License 三体系报价法', 'presales/stellar-wlan/index.html'),
        ('园区网络参考架构', 'SMB / 紧凑核心 / 环网 / 密集核心模板库', 'solutions/campus-architecture/index.html'),
        ('SPB 售前与三技术对比', '为什么弃 STP 选 SPB；SPB vs EVPN vs MPLS 七维选型', 'presales/spb-presales/index.html'),
        ('License 与 WWPL 报价规则', '报价规则与安全统一接入', 'presales/campus-lan/index.html'),
        ('DAN 数字化时代网络叙事', '愿景三支柱 + 七大行业方案话术', 'presales/dan/index.html'),
        ('全球客户案例弹药库', '六行业约 95 例：客户/挑战/方案组合/成效数字速查', 'presales/dan-cases/index.html'),
    ]),
    ('售后工程师路径', '从开局配置到故障排查的交付主线', 'banner-postsales.jpg', [
        ('OmniSwitch 基础操作', '三目录配置管理模型、VLAN/LACP/STP 接入基础', 'postsales/os-lan-access/index.html'),
        ('AOS 软件体系与升级', 'Flash 双目录、代码升级与 ISSU、日志健康', 'aos/switch-management/index.html'),
        ('交换机开局与接入配置', 'SMB 交付两日课：开局 / PoE / VLAN / STP', 'postsales/smb-lan-wlan-install/index.html'),
        ('WLAN 部署与云管', 'Stellar+Cirrus 云管交付，AP 生命周期全流程', 'postsales/acfe-wlan-basic/index.html'),
        ('OmniVista 网管平台', 'OV2500 安装 / 发现 / 资源 / 统一接入 / 隔离', 'postsales/ov2500-nms-admin/index.html'),
        ('有线排障全科', '七步方法论、五大故障域、OVNA AI 运维', 'postsales/os-lan-troubleshooting/index.html'),
    ]),
    ('WLAN 专项路径', '无线理论到高级排障的完整进阶线', 'banner-wlan.jpg', [
        ('无线技术基础', '802.11 / 天线 / 安全 / 勘测理论速成', 'postsales/stellar-enterprise-basic/index.html'),
        ('AP 部署与 Express 模式', '开箱六步、集群上线、免云管小微交付', 'postsales/stellar-express/index.html'),
        ('SSID 全家桶与认证', 'PSK 四级体系、802.1X、Guest、UPAM 策略', 'postsales/acfe-wlan-basic/index.html'),
        ('RF 调优与勘测三步法', 'RF 基线、勘测纠正、微调七要点', 'solutions/wlan-design/index.html'),
        ('漫游与 RAP 远程接入', 'L2/L3 漫游、RAP 双模式、云运维三件套', 'postsales/stellar-adv-trouble-update/index.html'),
        ('无线高级排障', '七步流程 + 三域根因地图、802.1X 排查', 'postsales/stellar-adv-trouble/index.html'),
    ]),
]

PATH_CSS = """
.paths{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:20px;margin:24px 0}
.path{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.path .ph{position:relative;height:120px}
.path .ph img{width:100%;height:120px;object-fit:cover;display:block;margin:0;border:none;border-radius:0}
.path .ph .ov{position:absolute;inset:0;background:linear-gradient(90deg,rgba(52,32,84,.85),rgba(79,52,120,.35))}
.path .ph h2{color:#fff;margin:0;position:absolute;left:20px;bottom:18px;font-size:20px;border:none;padding:0}
.path .ph p{color:#E9E1F4;margin:0;position:absolute;left:20px;bottom:0;font-size:12px}
.path ol{list-style:none;margin:0;padding:14px 18px;counter-reset:st}
.path ol li{counter-increment:st;padding:9px 0 9px 38px;position:relative;border-bottom:1px dashed #E8E6E0;font-size:14px}
.path ol li:last-child{border-bottom:none}
.path ol li::before{content:counter(st);position:absolute;left:0;top:9px;width:24px;height:24px;border-radius:50%;
background:var(--purple-light);color:var(--acc);font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center}
.path ol a{color:var(--acc2);font-weight:600}
.path ol span{display:block;font-size:12px;color:var(--mut);font-weight:400}
.recent{background:#fff;border:1px solid var(--line);border-radius:12px;padding:18px 22px;margin:30px 0}
.recent h2{margin:0 0 6px;font-size:18px;border:none;padding:0}
.recent .ri{display:flex;gap:12px;align-items:baseline;padding:7px 0;border-bottom:1px dashed #E8E6E0;font-size:14px}
.recent .ri:last-child{border-bottom:none}
.recent .rd{color:var(--mut);font-size:12px;white-space:nowrap}
.recent a{color:var(--acc2);font-weight:600}
.recent span{color:var(--mut);font-size:13px}
.catfilter{margin:0 0 16px}
.catfilter input{width:100%;max-width:420px;padding:9px 14px;border-radius:8px;border:1px solid var(--line);font-size:14px;outline:none;background:#fff}
.catfilter input:focus{border-color:var(--acc)}
"""

def build_paths_page():
    blocks = ''
    for name, desc, img, steps in LEARNING_PATHS:
        items = ''.join(f'<li><a href="{h}">{t}</a><span>{d}</span></li>' for t, d, h in steps)
        blocks += f'''<div class="path"><div class="ph"><img src="assets/{img}" alt="" loading="lazy"><div class="ov"></div>
<h2>{name}</h2><p>{desc} · {len(steps)} 步</p></div><ol>{items}</ol></div>'''
    page = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>学习路径 — ALE Networking 技术培训</title><style>{CSS}{HERO_CSS}{PATH_CSS}</style></head>
<body>{topbar('', '')}<div class="layout"><aside><h1>ALE 培训门户</h1>
<div class="search"><input id="qk" type="search" placeholder="🔍 搜索全站…" autocomplete="off"><div id="qres"></div></div>
<div class="sub">学习路径</div>
<a href="index.html">⬅️ 返回培训门户</a></aside>
<main><h1>学习路径</h1>
<p class="meta">不知道从哪开始？按角色或专项跟着走，每条路径从入门到进阶：</p>
<div class="paths">{blocks}</div></main></div></body></html>"""
    with open(os.path.join(OUT, 'paths.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print('paths page built')

# ============ 课程元数据（第二阶段：版本/页数/更新时间） ============
import datetime as _dt

def course_chips(cid):
    """从副标题解析版本与页数 + 源文件更新时间，返回 chips 行（负责人无数据不编造）"""
    c = course_map.get(cid)
    if not c:
        return ''
    sub = c['subtitle']
    chips = []
    mv = _re.match(r'^(Edition\s+\S+|Issue\s+\S+|Rev\s+\S+|AWOS\s+[\d.]+|\d+\.\d+R\d+)', sub)
    if mv:
        chips.append(mv.group(1))
    mp = _re.search(r'(\d[\d,]*)\s*页', sub)
    if mp:
        chips.append(mp.group(1) + ' 页')
    book = os.path.join(ROOT, 'books', c['book'])
    if os.path.isdir(book):
        t = max(os.path.getmtime(os.path.join(r, f)) for r, _, fs in os.walk(book) for f in fs)
        chips.append('更新 ' + _dt.date.fromtimestamp(t).isoformat())
    if not chips:
        return ''
    return '<p class="chips">' + ''.join(f'<span class="chip">{x}</span>' for x in chips) + '</p>'

# 最近更新（首页区块）
RECENT = [
    ('2026-08-26', '门户品牌化改版上线', None, 'ALE 品牌紫视觉 / 顶部导航 / 学习路径 / 全局搜索'),
    ('2026-08-25', '产品彩页 2026-08 快照', 'brochures/omniswitch/index.html', 'OmniSwitch 15 份 · Stellar AP 14 份 · 网管安全 5 份'),
    ('2026-08-20', 'AOS 8.10R04 软件手册全集', 'aos/net-config/index.html', 'Network Configuration 1745 页 · CLI 命令地图 70 章'),
    ('2026-08-15', 'OV2500 4.9R2 配置手册', 'manuals/ov2500-userguide/index.html', 'User Guide 935 页 · 安装升级 · Release Notes'),
    ('2026-08-10', '硬件手册 10 机型全覆盖', 'hardware/os6860/index.html', 'OS6360–OS9900 全系 Hardware Guide'),
]

def recent_html():
    rows = ''
    for d, t, h, note in RECENT:
        link = f'<a href="{h}">{t}</a>' if h else f'<b>{t}</b>'
        rows += f'<div class="ri"><span class="rd">{d}</span>{link}<span>{note}</span></div>'
    return f'<div class="recent"><h2>最近更新</h2>{rows}</div>'

def build_course(c):
    sub = os.path.join(OUT, c['id'].replace('/', os.sep))
    os.makedirs(os.path.join(sub, 'skills'), exist_ok=True)
    book = os.path.join(ROOT, 'books', c['book'])
    skills = [s for _, slugs in c['groups'] for s in slugs]
    # 原文插图：books/<book>/images -> site/<course>/skills/images（SKILL.md 以 images/x.png 相对引用）
    bimg = os.path.join(book, 'images')
    if os.path.isdir(bimg):
        simg = os.path.join(sub, 'skills', 'images')
        os.makedirs(simg, exist_ok=True)
        for root_d, _, fns in os.walk(bimg):
            rel_d = os.path.relpath(root_d, bimg)
            dst_d = simg if rel_d == '.' else os.path.join(simg, rel_d)
            os.makedirs(dst_d, exist_ok=True)
            for fn in fns:
                shutil.copy2(os.path.join(root_d, fn), os.path.join(dst_d, fn))

    def nav(active, sub=False):
        p = '../' if sub else ''
        gal = f'<a href="{p}gallery.html">🖼 产品外观</a>' if os.path.exists(os.path.join(book, 'GALLERY.md')) else ''
        items = [f'<a href="{p}index.html">🏠 课程首页</a>',
                 f'<a href="{p}digest.html">📖 精华长文 DIGEST</a>',
                 gal,
                 f'<a href="{p}overview.html">📘 教书理解 BOOK_OVERVIEW</a>',
                 f'<a href="{p}glossary.html">🔤 术语词典</a>',
                 f'<a href="{p}../../index.html">⬅️ 返回培训门户</a>',
                 f'<a href="{p}index.html">──── Skills ────</a>']
        for gname, slugs in c['groups']:
            items.append(f'<div class="grp">{html_mod.escape(gname)}</div>')
            for s in slugs:
                cls = ' class="on"' if s == active else ''
                items.append(f'<a href="{p}skills/{s}.html"{cls}>{s}</a>')
        return '\n'.join(items)

    def crumbs(cur='', sub=False):
        cat = c['id'].split('/')[0]
        cat_label = {'postsales': '售后', 'presales': '售前', 'manuals': 'OV2500 配置手册', 'aos': 'AOS 软件手册', 'hardware': '硬件手册', 'brochures': '产品彩页', 'wlan': '无线网络', 'solutions': '解决方案'}[cat]
        p = '../../../' if sub else '../../'
        q = '../' if sub else ''
        bar = f'<nav class="crumbs"><a href="{p}index.html">🏠 培训门户</a> › <a href="{p}{cat}/index.html">{cat_label}</a> › <a href="{q}index.html">{html_mod.escape(c["title"].split(" · ")[0])}</a>'
        if cur:
            bar += f' › <span>{html_mod.escape(cur)}</span>'
        return bar + '</nav>'

    def page(title, body, active='', cur='', sub=False):
        foot = '<div class="foot">仅供内部学习使用 · 教材版权归 ALE Training Services 所有</div>'
        tp = '../../../' if sub else '../../'
        return f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html_mod.escape(title)} — {c['title']}</title>
<style>{CSS}</style></head>
<body>{topbar(tp, c['id'].split('/')[0])}<div class="layout"><aside><h1>{c['title']}</h1>
<div class="search"><input id="qk" type="search" placeholder="🔍 搜索全站…" autocomplete="off"><div id="qres"></div></div>

<div class="sub">{c['subtitle']}</div>
{nav(active, sub)}<script src="/search.js"></script></aside><main>{crumbs(cur, sub)}{body}{foot}</main></div></body></html>"""

    def rel_links(h):
        for s in skills:
            h = h.replace(f'>{s}<', f'><a href="{s}.html">{s}</a><')
        return h

    desc_map, zh_map = {}, {}
    for slug in skills:
        fm, body = parse_fm(read(os.path.join(book, slug, 'SKILL.md')))
        desc_map[slug] = fm.get('description', '')
        chap = fm.get('source_chapter', '')
        h = rel_links(to_html(body))
        # 中文标题取 H1；prev/next
        m1 = _re.search(r'^#\s+(.+)$', body, _re.M)
        zh = m1.group(1).strip() if m1 else slug
        zh_map[slug] = zh
        idx = skills.index(slug)
        pn = '<div class="pn">'
        pn += (f'<a href="{skills[idx-1]}.html">⬅ 上一单元：{skills[idx-1]}</a>' if idx > 0
               else f'<a href="../index.html">⬅ 返回课程首页</a>')
        pn += (f'<a class="nxt" href="{skills[idx+1]}.html">下一单元：{skills[idx+1]} ➡</a>' if idx < len(skills)-1
               else f'<a class="nxt" href="../digest.html">查看课程精华 DIGEST ➡</a>')
        pn += '</div>'
        body_html = f'<h1>{html_mod.escape(zh)}</h1><p class="meta"><span class="badge">SKILL</span> {slug} · 来源页码: {html_mod.escape(chap)}</p>' + h + pn
        with open(os.path.join(sub, 'skills', slug + '.html'), 'w', encoding='utf-8') as f:
            f.write(page(slug, body_html, slug, cur=zh, sub=True))

    # 分组卡：PC 端各分组一个横排（auto-fit 自适应列数），手机端竖排
    gcards = '<div class="gcards">'
    for gname, slugs in c['groups']:
        inner = ''.join(
            f'<a class="gskill" href="skills/{s}.html"><b>{html_mod.escape(zh_map.get(s, s))}</b>'
            f'<span class="gslug">{s}</span><span class="gdesc">{html_mod.escape(desc_map.get(s, "")[:110])}</span></a>'
            for s in slugs)
        gcards += f'<div class="gcard"><h3>{html_mod.escape(gname)}</h3><div class="gwrap">{inner}</div></div>'
    gcards += '</div>'
    route = ''.join(f'<li>{html_mod.escape(r)}</li>' for r in c['route'])
    n = len(skills)
    gal_link = ' · <a href="gallery.html">🖼 产品外观</a>' if os.path.exists(os.path.join(book, 'GALLERY.md')) else ''
    home = f"""<p><a href="../../index.html">⬅️ 返回培训门户</a></p>
<h1>{c['title']} · 学习站</h1>
<p class="meta">教材: <b>{c['subtitle']}</b>。整理为 {n} 个可执行知识单元：
每个单元含 原文引用(R) / 方法论骨架(I) / 书中案例(A1) / 触发场景(A2) / 可执行步骤(E) / 边界与陷阱(B)。</p>
<h2>建议学习路线</h2><ol>{route}</ol>
<h2>知识单元</h2>{gcards}
<h2>全文阅读</h2>
<p><a href="digest.html">📖 精华长文 DIGEST</a> · <a href="overview.html">📘 教书理解</a> · <a href="glossary.html">🔤 术语词典</a>{gal_link}</p>"""
    with open(os.path.join(sub, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page('首页', home, cur='首页'))

    gsrc = os.path.join(book, 'GALLERY.md')
    if os.path.exists(gsrc):
        gh = to_html(read(gsrc))
        gh = gh.replace('src="images/', 'src="skills/images/').replace('](images/', '](skills/images/')
        # 网格卡片化：每个 <p><img></p> 转成 figure
        def _fig(m):
            alt = _re.search(r'alt="([^"]*)"', m.group(1))
            cap = alt.group(1) if alt else ''
            return f'<figure><img {m.group(1)} loading="lazy"><figcaption>{cap}</figcaption></figure>'
        gh = _re.sub(r'<img ([^>]*?)/?>', _fig, gh)
        gh = gh.replace('<p><figure', '<figure').replace('</figure></p>', '</figure>')
        gh = _re.sub(r'<p>\s*</p>', '', gh)
        with open(os.path.join(sub, 'gallery.html'), 'w', encoding='utf-8') as f:
            f.write(page('产品外观', f'<h1>🖼 产品外观</h1><div class="gallery">' + gh + '</div>', cur='产品外观'))
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
course_map = {c['id']: c for c in COURSES}

def build_category(dirname, label):
    d = os.path.join(OUT, dirname)
    os.makedirs(d, exist_ok=True)
    items = ''
    for c in COURSES:
        if c['id'].startswith(dirname + '/'):
            n = len([s for _, sl in c['groups'] for s in sl])
            items += f'''<div class="card"><a href="../{c['id']}/index.html">{c['title']}</a>
<p>{c['subtitle']}</p>{course_chips(c['id'])}
<p style="margin-top:6px"><span class="badge">{n} 个知识单元 · 已上线</span></p></div>'''
    banner = CAT_BANNER.get(dirname)
    bh = (f'<div class="catbanner"><img src="../assets/{banner}" alt="" loading="lazy"><div class="ov"></div>'
          f'<div class="tt"><h1>{label}</h1><p>该分类下的课程与资料</p></div></div>') if banner else f'<h1>{label}</h1>'
    page = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{label} — ALE Networking 技术培训</title><style>{CSS}{HERO_CSS}{PATH_CSS}</style></head>
<body>{topbar('../', dirname)}<div class="layout"><aside><h1>ALE 培训门户</h1>
<div class="search"><input id="qk" type="search" placeholder="🔍 搜索全站…" autocomplete="off"><div id="qres"></div></div>

<div class="sub">{label}</div>
<a href="index.html">⬅️ 返回培训门户</a></aside>
<main>{bh}
<div class="catfilter"><input id="cf" type="search" placeholder="⏩ 在本分类中筛选：输入课程号 / 产品 / 关键词…" autocomplete="off"></div>
<div class="cards">{items}</div></main></div>
<script>
(function(){{
  var cf=document.getElementById('cf'); if(!cf)return;
  cf.addEventListener('input',function(){{
    var q=cf.value.trim().toLowerCase();
    document.querySelectorAll('.cards .card').forEach(function(c){{
      c.style.display = !q || c.textContent.toLowerCase().indexOf(q)>=0 ? '' : 'none';
    }});
  }});
}})();
</script></body></html>"""
    with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print('category built:', dirname)

for dirname, label in [('postsales', '售后 · Postsales'), ('presales', '售前 · Presales'), ('manuals', 'OV2500 配置手册 · Manuals'), ('aos', 'AOS 软件手册 · Software Guides'), ('hardware', '硬件手册 · Hardware Guides'), ('brochures', '产品彩页 · Product Datasheets'), ('wlan', '无线网络 · WLAN'), ('solutions', '解决方案 · Solutions')]:
    build_category(dirname, label)

build_paths_page()

# ============ 门户封面 ============
CATALOG = [
    ('售前 · Presales', '#38bdf8', [
        ('DT00XPS279 · OmniSwitch LAN SPB 售前', 'Issue 05 · 147 页 · 9 个知识单元 · 卖点弹药 / L3 集成 / 三技术对比', 'presales/spb-presales/index.html'),
        ('DT00XPS281 · Campus LAN 售前', 'Edition 29 · 480 页 · 11 个知识单元 · 分层设计 / 机型选型 / WWPL 报价 / 参考架构库', 'presales/campus-lan/index.html'),
        ('DT00XPS288 · OmniAccess Stellar WLAN 售前', 'Edition 28 · 273 页 · 8 个知识单元 · AP 矩阵 / 三管理模式 / License 三体系 / 七大用例', 'presales/stellar-wlan/index.html'),
        ('DAN · 数字化时代网络', '10 份官方文档 · 9 个知识单元 · 愿景三支柱 / 全球与 APAC 白皮书 / 七大行业方案', 'presales/dan/index.html'),
        ('全球客户案例 · Customer Reference 2024', '98 页 · 约 95 例 · 6 个知识单元 · 医疗 / 交通 / 教育 / 酒店 / 政府 / 综合行业速查', 'presales/dan-cases/index.html'),
        ('SD-WAN / SASE 方案', '零信任与云网融合', None),
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
        ('DT00XTE220 · OmniSwitch R6/R8 Bootcamp', 'Issue 25 · 1207 页 · 五天全科训练营 · 12 个知识单元 · Flash 回滚 / VC / QoS 策略引擎 / AG-UNP / SPB 织构', 'postsales/dt00xte220-bootcamp/index.html'),
        ('DT00XTE216 · OmniSwitch LAN R8 Core Switching', 'Edition 15 · 724 页 · 核心交换专题 · 13 个知识单元 · SPB 织构重点（含 Tech Brief 与实验附录）', 'postsales/dt00xte216-core-switching/index.html'),
        ('DT00XTE301 · OmniSwitch 接入与 Stellar WLAN 安装', 'Edition 04 · 512 页 · 10 个知识单元 · 交换机开局 / PoE / SSID 安全 / Cirrus 云管', 'postsales/smb-lan-wlan-install/index.html'),
        ('DT00XTE310 · OmniSwitch 接入与 Stellar WLAN Express', 'Edition 05 · 1083 页 · 11 个知识单元 · 三部署模式 / 语音 WLAN / 故障排查', 'postsales/smb-express-lan-wlan/index.html'),
        ('DT00XTE311 · OmniVista 2500 NMS 管理', 'Edition 09 · 581 页 · 10 个知识单元 · 安装 / 发现 / 资源 / 统一接入 / 隔离', 'postsales/ov2500-nms-admin/index.html'),
        ('Stellar WLAN 实施与优化', 'AP 部署、RF 规划、无线排障', None),
    ]),
    ('OV2500 配置手册 · Manuals', '#22d3ee', [
        ('OV2500 4.9R2 · 安装与升级指南', '326 页 · 4 个知识单元 · 四档规模 / 三平台 / HA / 升级链', 'manuals/ov2500-install/index.html'),
        ('OV2500 4.9R2 · RAP 与 VPN VA 安装', '84 页 · 4 个知识单元 · VPN 模式 / VA 容量 / 隧道排障', 'manuals/ov2500-rap-vpn/index.html'),
        ('OV2500 4.9R2 · Release Notes', '93 页 · 4 个知识单元 · 升级评估 / 63 条已知问题排障库 / 危险陷阱', 'manuals/ov2500-release-notes/index.html'),
        ('OV2500 4.9R2 · User Guide', '935 页 · 10 个知识单元 · Analytics 报表 / 发现拓扑 / 资源管理 / UPAM / VM 织构', 'manuals/ov2500-userguide/index.html'),
    ]),
    ('AOS 软件手册 · Software Guides', '#60a5fa', [
        ('AOS 8.10R04 · Network Configuration', '1745 页 · 10 个知识单元 · 二层/织构/IP 服务/路由/组播/QoS/准入/OAM', 'aos/net-config/index.html'),
        ('AOS 8.10R04 · Switch Management', '511 页 · 6 个知识单元 · Flash / 升级 / 用户 / 纳管 / 日志 / 机箱', 'aos/switch-management/index.html'),
        ('AOS 8.10R04 · Advanced Routing', '313 页 · 5 个知识单元 · OSPF / IS-IS / BGP / 组播高级 / Route Map', 'aos/advanced-routing/index.html'),
        ('AOS 8.10R04 · CLI Reference 命令地图', '6240 页 · 5 个命令域 · 70 章 2480 条命令导航', 'aos/cli-reference/index.html'),
        ('AOS 8.10R04 · Release Notes', '105 页 · 4 个知识单元 · 升级方法论 / 已知问题库 / 新特性', 'aos/release-notes/index.html'),
        ('AOS 8.10R04 · Specifications Guide', '98 页 · 3 个知识单元 · 平台梯队 / 容量红线 / TCAM', 'aos/specifications/index.html'),
        ('AOS 8.10R04 · Transceivers Guide', '107 页 · 3 个知识单元 · 模块矩阵 / 平台兼容 / DDM', 'aos/transceivers/index.html'),
    ]),
    ('硬件手册 · Hardware Guides', '#f97316', [
        ('OmniSwitch 6360', 'Rev J · 83 页 · 入门千兆接入 · 10 机型 / 内置电源 / PoE 三环', 'hardware/os6360/index.html'),
        ('OmniSwitch 6465', 'Rev V · 99 页 · 工业加固 · 宽温三档 / DIN-DNV / 告警继电器', 'hardware/os6465/index.html'),
        ('OmniSwitch 6560', 'Rev P · 111 页 · 多千兆 bt 接入 · 2.5G/5G / 双 PX 1565W', 'hardware/os6560/index.html'),
        ('OmniSwitch 6570M', 'Rev G · 59 页 · 千兆接入 · 12/12D/U28 / 半宽并装', 'hardware/os6570/index.html'),
        ('OmniSwitch 6575', 'Rev A · 86 页 · 工业无风扇 · M12 / 温度阶梯预算 / Alarm Relay', 'hardware/os6575/index.html'),
        ('OmniSwitch 6860', 'Rev W · 115 页 · 三代 15 机型 · 20G VC→QSFP28 VFL / 七款电源', 'hardware/os6860/index.html'),
        ('OmniSwitch 6865', 'Rev Y · 76 页 · 加固型 · 无风扇宽温 / 五形态安装 / 军规 DC', 'hardware/os6865/index.html'),
        ('OmniSwitch 6870', 'Rev D · 85 页 · 九机型 · QSFP56 200G / 允许混插扩容', 'hardware/os6870/index.html'),
        ('OmniSwitch 6900', 'Rev C · 90 页 · 模块化机箱 · 端口组锁速 / QSFP-DD 十二态', 'hardware/os6900/index.html'),
        ('OmniSwitch 9900', 'Rev S · 74 页 · 核心机箱 · 9907/9912 / CMM-CFM / N+1', 'hardware/os9900/index.html'),
    ]),
    ('产品彩页 · Product Datasheets', '#fb923c', [
        ('ALE 网管与安全 · 官方彩页', '5 份 23 页 · OmniVista 双形态 / 订阅 / Fleet / Milestone / Advisor', 'brochures/nms/index.html'),
        ('OmniAccess Stellar WLAN · 官方数据表', '14 份 128 页 · AP1261-AP1570 全系选型速查', 'brochures/stellar-ap/index.html'),
        ('OmniSwitch · 官方数据表', '15 份 158 页 · OS2260-OS9900 全系选型速查', 'brochures/omniswitch/index.html'),
    ]),
    ('解决方案 · Solutions', '#4ade80', [
        ('SPB 智能织构 · 架构与部署', '3 份 86 页 · IS-IS SPB / I-SID / 部署流程 / 客户案例', 'solutions/spb/index.html'),
        ('园区网络架构 · 设计指南', '2 份 47 页 · 分层设计 / AP 发现 / 漫游 / POL', 'solutions/campus-architecture/index.html'),
        ('EVPN 架构指南', '1 份 73 页 · Route Types / 多归属五机制 / IRB / OISM', 'solutions/evpn-architecture/index.html'),
        ('MPLS 参考设计指南', '1 份 45 页 · 双标签 / LDP / VPLS-VPWS / OAM', 'solutions/mpls-reference/index.html'),
        ('ERP 环网保护 · 应用笔记', '1 份 17 页 · G.8032 / RPL / 多环设计', 'solutions/erp-switching/index.html'),
        ('访客流量隧道 GTTS · 应用笔记', '1 份 19 页 · L2 GRE / DMZ / 四种冗余', 'solutions/guest-tunneling/index.html'),
        ('网络基础设施安全 · Tech Brief', '2 份 100 页 · 五层框架 / 三平面加固 / NLM', 'solutions/network-security/index.html'),
        ('Stellar WLAN 设计与调优', '3 份 75 页 · 高密五步法 / 微调七要点', 'solutions/wlan-design/index.html'),
    ]),
    ('无线网络 · WLAN', '#a78bfa', [
        ('AWOS 5.0.3 · Stellar AP 用户手册', '128 页 · 4 个知识单元 · 集群开局 / 射频调优 / 安全 / 运维升级', 'wlan/awos-ap-guide/index.html'),
        ('WiFi 6 / 6E / 7 技术基础', '标准演进、OFDMA、多链路操作', None),
        ('Stellar AP 产品与组网', 'Mesh / Bridge / RAP 特殊组网', None),
    ]),
    ('有线网络 · LAN Switching', '#34d399', [
        ('OmniSwitch R8 体系结构', 'VC 虚拟机箱、SPB / MPLS、UNP', None),
        ('AOS CLI 进阶', '脚本化配置与自动化运维', None),
    ]),
    ('云网管 · Cloud base Management', '#f472b6', [
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
            cid = href.replace('/index.html', '')
            n = len([s for _, sl in course_map[cid]['groups'] for s in sl]) if cid in course_map else 0
            cards += f'''<div class="card">
<a href="{href}">{title}</a><p>{desc}</p>{course_chips(cid)}
<p style="margin-top:6px"><span class="badge">● 已上线</span>{f' <span class="meta">{n} 个知识单元</span>' if n else ''}</p></div>'''
        else:
            cards += f'''<div class="card" style="background:#FCFCFB">
<a style="color:var(--mut);cursor:default" onclick="return false">{title}</a><p>{desc}</p>
<p style="margin-top:6px"><span class="badge soon">◷ 待建设 · 教材翻译后上线</span></p></div>'''
    cats_html += f'<h2 id="catalog">{gname}</h2><div class="cards">{cards}</div>'

cover = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ALE Networking 技术培训</title>
<style>{CSS}{HERO_CSS}{PATH_CSS}
main.cover{{max-width:1160px;margin:0 auto;padding:26px 32px 60px}}
main.cover h2{{margin-top:44px}}
footer.brand{{background:#fff;border-top:1px solid var(--line);padding:22px 32px;display:flex;gap:14px;align-items:center;justify-content:center;flex-wrap:wrap}}
footer.brand img{{height:26px}}
footer.brand span{{font-size:12px;color:var(--mut)}}
</style></head><body>{topbar('', '')}
{hero_section()}
<main class="cover">
{recent_html()}
{cats_html}
<h2>关于本站</h2>
<p class="meta">内容整理自 ALE 官方培训教材与配置手册，仅供内部学习使用；教材版权归 ALE Training Services 所有，请勿外传。</p>
</main>
<footer class="brand"><img src="assets/ale-logo-color.png" alt="Alcatel-Lucent Enterprise"><span>仅供内部学习使用 · 教材版权归 ALE Training Services 所有</span></footer>
<script src="/search.js"></script></body></html>"""
with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(cover)
print('portal built')

# ============ 全站搜索索引 ============
import html as _H
def build_search_index():
    import glob as _glob, json as _json
    entries = []
    pat = _re.compile(r'<h([23]) id="([^"]+)">(.*?)</h' + chr(92) + '1>(.*?)(?=<h[123] |</main>|<footer|$)', _re.S)
    for f in _glob.glob(os.path.join(OUT, '**', '*.html'), recursive=True):
        rel = os.path.relpath(f, OUT).replace(os.sep, '/')
        if rel == 'index.html':
            continue
        t = open(f, encoding='utf-8').read()
        mt = _re.search(r'<title>(.*?)</title>', t)
        title = _H.unescape(mt.group(1)).strip() if mt else rel
        for m in pat.finditer(t):
            sec = _H.unescape(_re.sub(r'<[^>]+>', '', m.group(3))).strip()
            body = _H.unescape(_re.sub(r'<[^>]+>', ' ', m.group(4)))
            body = ' '.join(body.split())[:400]
            entries.append({'u': rel, 'a': m.group(2), 's': sec, 't': title, 'x': body})
        if not _re.search(r'<h[23] id=', t):
            body = _H.unescape(_re.sub(r'<[^>]+>', ' ', t))
            body = ' '.join(body.split())[:400]
            entries.append({'u': rel, 'a': '', 's': title, 't': title, 'x': body})
    with open(os.path.join(OUT, 'search_index.json'), 'w', encoding='utf-8') as fo:
        _json.dump(entries, fo, ensure_ascii=False)
    print(f'search index built: {len(entries)} sections')

SEARCH_JS = """// 全站静态搜索：输入关键字 -> 章节/页面匹配 -> 直达锚点
(function(){
  var IDX = null, box = document.getElementById('qk'), res = document.getElementById('qres');
  if (!box) return;
  function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML}
  function load(cb){ if(IDX) return cb();
    fetch('/search_index.json').then(function(r){return r.json()}).then(function(j){IDX=j;cb()}).catch(function(){res.innerHTML=''}) }
  function score(e, q){
    var s=0
    if(e.t.indexOf(q)>=0) s+=10
    if(e.s.indexOf(q)>=0) s+=8
    if(e.x.indexOf(q)>=0) s+=3
    return s
  }
  function run(){
    var q=box.value.trim().toLowerCase()
    if(q.length<2){res.innerHTML='';return}
    load(function(){
      var out=[]
      for(var i=0;i<IDX.length;i++){var e=IDX[i];var sc=score(e,q);if(sc>0)out.push([sc,e])}
      out.sort(function(a,b){return b[0]-a[0]})
      var top=out.slice(0,20), h=top.map(function(p){
        var e=p[1]
        var url='/'+e.u+(e.a?('#'+e.a):'')
        return '<a class="qi" href="'+url+'"><b>'+esc(e.s)+'</b><span class="qp">'+esc(e.t)+'</span></a>'
      }).join('')
      res.innerHTML = h || '<span class="qi">无匹配</span>'
    })
  }
  box.addEventListener('input', run)
  box.addEventListener('focus', run)
})();

// ===== 侧栏折叠（内容全屏） =====
(function(){
  var lay = document.querySelector('.layout');
  if(!lay) return;
  var KEY = 'sidebar-collapsed';
  var b = document.createElement('button');
  b.className = 'tgl'; b.title = '折叠/展开侧栏';
  function sync(){
    var off = localStorage.getItem(KEY) === '1';
    lay.classList.toggle('full', off);
    b.textContent = off ? '\\u25B6 \\u5c55\\u5f00' : '\\u25C0 \\u6536\\u8d77';
  }
  b.onclick = function(){
    localStorage.setItem(KEY, localStorage.getItem(KEY) === '1' ? '0' : '1');
    sync();
  };
  document.body.appendChild(b);
  sync();
})();

// ===== 图片灯箱（滚轮缩放 + 拖拽平移 + 双击快捷缩放） =====
(function(){
  var box=null, img=null, scale=1, tx=0, ty=0, badge=null, moved=false;
  var MIN=0.2, MAX=8;
  function apply(){
    img.style.transform='translate('+tx+'px,'+ty+'px) scale('+scale+')';
    if(badge) badge.textContent=Math.round(scale*100)+'%';
  }
  function clampScale(s){ return Math.min(MAX, Math.max(MIN, s)) }
  function ensure(){
    if(box) return;
    box=document.createElement('div'); box.className='lb';
    img=document.createElement('img');
    var bar=document.createElement('div'); bar.className='lbb';
    function mkBtn(t,fn){var x=document.createElement('button');x.textContent=t;x.onclick=function(e){e.stopPropagation();fn()};return x}
    badge=document.createElement('span'); badge.className='zoom'; badge.textContent='100%';
    bar.appendChild(mkBtn('\\uff0d',function(){zoomAt(0.8,0,0)}));
    bar.appendChild(badge);
    bar.appendChild(mkBtn('\\uff0b',function(){zoomAt(1.25,0,0)}));
    bar.appendChild(mkBtn('\\u21fa \\u590d\\u4f4d',reset));
    bar.appendChild(mkBtn('\\u2715 \\u5173\\u95ed',close));
    box.appendChild(img); box.appendChild(bar);
    // 滚轮缩放：以鼠标位置为中心
    box.addEventListener('wheel',function(e){
      e.preventDefault();
      var r=img.getBoundingClientRect();
      var cx=e.clientX-(r.left+r.width/2), cy=e.clientY-(r.top+r.height/2);
      zoomAt(e.deltaY<0?1.15:1/1.15, cx, cy);
    },{passive:false});
    // 双击：1x <-> 2x
    img.addEventListener('dblclick',function(e){e.stopPropagation(); if(scale===1){zoomAt(2/scale,e.clientX,e.clientY)}else{reset()}});
    // 拖拽平移
    var drag=false,lx=0,ly=0;
    img.addEventListener('mousedown',function(e){drag=true;moved=false;lx=e.clientX;ly=e.clientY;img.classList.add('grabbing');e.preventDefault()});
    window.addEventListener('mousemove',function(e){
      if(!drag)return; moved=true; tx+=e.clientX-lx; ty+=e.clientY-ly; lx=e.clientX; ly=e.clientY; apply();
    });
    window.addEventListener('mouseup',function(){drag=false;img.classList.remove('grabbing')});
    box.onclick=function(e){ if(e.target===box||e.target===bar) close(); };
    document.addEventListener('keydown',function(e){
      if(!box||box.style.display!=='flex')return;
      if(e.key==='Escape')close();
      if(e.key==='+'||e.key==='=')zoomAt(1.25,0,0);
      if(e.key==='-')zoomAt(0.8,0,0);
      if(e.key==='0')reset();
    });
    document.body.appendChild(box);
    function zoomAt(f,cx,cy){
      var ns=clampScale(scale*f); if(ns===scale)return;
      var k=ns/scale;
      tx=cx-(cx-tx)*k; ty=cy-(cy-ty)*k; scale=ns; apply();
    }
    function reset(){ scale=1; tx=0; ty=0; apply(); }
    function close(){ box.style.display='none'; }
  }
  document.addEventListener('click',function(e){
    var t=e.target;
    if(t.tagName==='IMG' && t.closest('main') && !t.closest('.lb')){
      ensure();
      img.src=t.src; scale=1; tx=0; ty=0; apply();
      box.style.display='flex';
      e.preventDefault();
    }
  });
})();
"""
with open(os.path.join(OUT, 'search.js'), 'w', encoding='utf-8') as fo:
    fo.write(SEARCH_JS)
build_search_index()
print('search.js written')
