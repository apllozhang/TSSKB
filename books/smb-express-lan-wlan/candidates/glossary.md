# glossary 候选 — DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express

> 术语 + 中文解释，均含页码。共 58 条。

## 产品/平台
1. **OmniSwitch** — ALE 以太网交换机家族；AOS R8 覆盖 6360/6465/6560/6570M/6860E/N/6865/6870/6900/9900（<<<PAGE 84>>>）
2. **OmniAccess Stellar** — ALE WLAN 接入点家族（Wi-Fi 6/6E/7：AP1301~AP1571），无控制器分布式架构（<<<PAGE 20>>>-<<<PAGE 23>>>）
3. **OmniVista Cirrus (OVC10)** — 云管平台（SaaS），管理 10000 AP + 2000 交换机（<<<PAGE 276>>>-<<<PAGE 277>>>）
4. **OmniVista 2500** — 本地 NMS，Enterprise 模式管理服务器兼许可证服务器（<<<PAGE 190>>>、<<<PAGE 845>>>）
5. **AWOS** — Stellar AP 的操作系统（软件名，如 AWOS 4.0.7）（<<<PAGE 370>>>）
6. **AOS** — Alcatel-Lucent Operating System，OmniSwitch 操作系统 R6/R8 双目录结构（<<<PAGE 125>>>）
7. **OXO Connect / OXE** — ALE 中小/大企业 IP 话音通信服务器（OmniPCX），VoWLAN 的 PBX 侧（<<<PAGE 824>>>）
8. **Rainbow UCaaS** — ALE 云统一通信客户端（iOS/Android/桌面），WebRTC 音视频（<<<PAGE 858>>>）
9. **OTC (OpenTouch Conversation)** — ALE 移动协作客户端（<<<PAGE 824>>>）
10. **8158s / 8168s** — ALE WLAN 话机（Ascom OEM）；8168s 彩屏/免提/PTT/Ekahau RTLS，8158s 黑白屏（<<<PAGE 847>>>）
11. **IMS3** — Integrated Messaging and Wireless Services，81x8s 话机集中网管/告警服务器（ELISE3 硬件 Linux）（<<<PAGE 853>>>）
12. **WinPDM** — Windows Portable Device Manager，话机配置工具（配 Cradle）（<<<PAGE 853>>>）
13. **ALE OmniVista Smart Tool (OST)** — 免费安装/排障工具（PoE 向导、auto-ticket、配置备份）（<<<PAGE 1046>>>-<<<PAGE 1052>>>）
14. **Lightning Config (OLC)** — 交换机开箱即用向导（默认 192.168.0.1，仅 1/2 口触发）（<<<PAGE 77>>>-<<<PAGE 79>>>）
15. **R-Lab** — 远程实验室（rdp.al-mydemo.com，Pod25-32）（<<<PAGE 98>>>）

## 部署模式/管理
16. **Wi-Fi Express 模式** — 自管理 AP 集群（AP-Group+PVM），≤255 AP，免许可证（<<<PAGE 188>>>）
17. **Wi-Fi Enterprise 模式** — OV2500 集中管理模式，≤4000 AP（<<<PAGE 190>>>）
18. **Wi-Fi Cloud 模式** — Cirrus 云管，≤10000 AP（<<<PAGE 192>>>）
19. **AP Group** — 同 Group ID+同 VLAN 的 AP 自动成组，统一配置单元（Cloud 下按组下发 SSID/RF/策略）（<<<PAGE 205>>>、<<<PAGE 267>>>）
20. **PVM / SVM** — Primary/Secondary Virtual Manager（Controller），组内主/备管理 AP，按型号→MAC 选举（<<<PAGE 206>>>）
21. **UPAM** — Unified Policy Authentication Manager，内嵌 RADIUS + Captive Portal 的统一认证平台（<<<PAGE 385>>>）
22. **ARP (Access Role Profile)** — 接入角色档案：VLAN/QoS/ACL/L7 规则/位置/时段的集合（<<<PAGE 394>>>）
23. **UNP (User Network Profile)** — OmniSwitch 侧用户网络档案（VLAN+Policy List+ACL+QoS+Location+Period）（<<<PAGE 755>>>）
24. **Access Guardian** — 基于 UNP 的角色化接入控制（802.1X/MAC 认证后套用 UNP）（<<<PAGE 754>>>）
25. **Device Catalog** — Cirrus 设备目录，按 SN 宣告并跟踪激活状态至 OV Managed（<<<PAGE 326>>>）
26. **Call Home** — 设备周期性主动联系云激活服务器（默认间隔 30 分钟）（<<<PAGE 332>>>）
27. **cloud-agent** — AOS 交换机上负责 Cirrus 注册/VPN 的代理进程（cloud-agent.cfg 存激活 URL）（<<<PAGE 332>>>）
28. **RAP (Remote AP)** — 远程站点 AP，经 Wireguard VPN 隧道回连总部 VPN VA（Tunnel/Local breakout 两模式）（<<<PAGE 904>>>）

## 交换技术
29. **VFL (Virtual Fabric Link)** — Virtual Chassis 成员间堆叠互联链路（<<<PAGE 468>>>）
30. **Virtual Chassis** — 多台交换机虚拟成单逻辑设备（ISIS-VC 管理，ISSU 升级）（<<<PAGE 468>>>）
31. **ISSU** — In-Service Software Upgrade，逐台 slave 重启的在线升级（<<<PAGE 478>>>）
32. **RCD** — Remote Chassis Detection，VC 分裂的带外检测（走 EMP）（<<<PAGE 476>>>）
33. **LACP (802.3ad)** — 动态链路聚合控制协议，actor admin key 关联端口（<<<PAGE 576>>>）
34. **DHL (Dual-Home Link)** — Active-Active 双归属链路，按 VLAN 划分活跃链路防环（替代 STP）（<<<PAGE 628>>>）
35. **VRRP** — 虚拟路由冗余协议（虚拟 MAC 00-00-5E-00-01-VRID）（<<<PAGE 674>>>）
36. **STP/RSTP/MSTP；flat/per-VLAN(1x1)** — 生成树协议与两种模式（OmniSwitch 默认 per-VLAN）（<<<PAGE 604>>>）
37. **802.1Q / 802.1p** — VLAN 打 tag（12bit VID）/tag 内 3bit 优先级（<<<PAGE 169>>>）
38. **Mobile Tag** — 允许移动口收 802.1Q tag 并动态入 VLAN（话机场景）（<<<PAGE 172>>>）
39. **Loopback0** — 不绑 VLAN 的稳定管理/服务源地址接口（<<<PAGE 659>>>）
40. **EMP** — Ethernet Management Port，带外管理口（master emp 地址命令配置）（<<<PAGE 70>>>）

## PoE
41. **802.3af/at/bt（PoE/PoE+/PoE++）** — 15.4W/30W/60-100W 以太网供电标准（Type1-4）（<<<PAGE 150>>>）
42. **Fast PoE / Perpetual PoE** — 开机即供电 / 重启不断电（需 FPGA 升级）（<<<PAGE 147>>>-<<<PAGE 148>>>）
43. **EEE (802.3az)** — 空闲低功耗节能以太网（仅铜口 100/1000M）（<<<PAGE 149>>>）
44. **PoE Midspan/Injector** — 非 PoE 交换机旁路供电设备（OAW-PD-xxx 系列）（<<<PAGE 43>>>、<<<PAGE 872>>>）

## WLAN/RF
45. **SSID** — 服务集标识（Wi-Fi 网络名）；Cirrus 建 SSID 走五步向导（<<<PAGE 383>>>）
46. **Captive Portal** — 访客 Web 认证门户（AP 内置或 UPAM/外部）（<<<PAGE 216>>>）
47. **Walled Garden** — 访客认证前即可访问的白名单网站列表（<<<PAGE 238>>>、<<<PAGE 428>>>）
48. **MU-MIMO** — 多用户多输入多输出（M 发 N 收，多用户复用空间流）（<<<PAGE 912>>>）
49. **OFDMA / BSS Coloring / TWT** — Wi-Fi 6 高效率三件套：子载波调度/同频染色/目标唤醒时间（<<<PAGE 911>>>）
50. **MLO** — Multi-Link Operation，Wi-Fi 7 多链路并发（<<<PAGE 48>>>）
51. **DFS (802.11h)** — 动态频率选择，检测雷达避让信道（<<<PAGE 927>>>）
52. **802.11r/k/v** — 快速切换/邻居报告/BSS 切换管理三大漫游增强（<<<PAGE 938>>>-<<<PAGE 940>>>）
53. **CNCS (Client Network Context Sharing)** — AP 间客户端上下文共享，漫游判定基础（<<<PAGE 842>>>）
54. **L3 Roaming (GRE tunnel)** — 跨子网漫游时新 AP↔Home AP 建 L2 GRE 隧道（<<<PAGE 894>>>）
55. **DRM (Dynamic Radio Manager)** — Stellar 射频自动管理（ACS/APC、自愈、负载均衡、频段引导）（<<<PAGE 841>>>）
56. **DPI (Deep Packet Inspection)** — AP 内置应用识别，配合 OV 做应用可视与带宽管控（<<<PAGE 875>>>）
57. **WIPS/WIDS** — 无线入侵防护/检测（Rogue AP 检测与压制）（<<<PAGE 993>>>）
58. **Stellar Asset Tracking / Ekahau RTLS** — 基于 BLE 信标 / RSSI 三角定位的资产与人员定位（<<<PAGE 880>>>）
