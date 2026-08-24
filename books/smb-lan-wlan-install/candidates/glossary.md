# glossary 候选 — DT00XTE301 LAN & WLAN Installation & Configuration for SMB

## 产品与平台

1. **OmniSwitch** — ALE 的 LAN 交换机产品线，覆盖接入/汇聚/核心（<<<PAGE 11>>>）。
2. **OmniSwitch 6360** — Value 级 AOS L2+ 千兆接入交换机，本课程主力实验机型（<<<PAGE 12>>>）。
3. **OmniSwitch 2360** — WebSmart L2 入门交换机，运行 AOS 5.2，不能上 Cirrus（<<<PAGE 13>>>、<<<PAGE 337>>>）。
4. **OmniSwitch 6870** — 新一代 Advanced L3 交换机，支持 10/25/40/50/100G 上联（<<<PAGE 12>>>）。
5. **OmniSwitch 6900 / 9900** — 汇聚/核心与模块化机箱旗舰（<<<PAGE 12>>>）。
6. **OmniAccess Stellar** — ALE 无控制器架构 Wi-Fi AP 产品族，覆盖 Wi-Fi 6/6E/7（<<<PAGE 16>>>–<<<PAGE 18>>>）。
7. **AP1301 / AP1311** — Wi-Fi 6 入门级 AP，2x2:2 双频 + 扫描射频（<<<PAGE 26>>>、<<<PAGE 28>>>）。
8. **AP1321/1322** — Wi-Fi 6 中端 AP；尾号 2 支持外置天线（<<<PAGE 29>>>、<<<PAGE 41>>>）。
9. **AP1301H** — 酒店/宿舍场景 Wi-Fi 6 AP，带 4 个下行 GE 口与 PoE 下行（<<<PAGE 27>>>）。
10. **AP1351 / AP1451** — Wi-Fi 6 / 6E 高端三射频 AP，8x8:8 5GHz（<<<PAGE 31>>>、<<<PAGE 35>>>）。
11. **AP136x** — Wi-Fi 6 户外加固 AP，-40~+65°C（<<<PAGE 32>>>）。
12. **AP1411 / AP1431** — Wi-Fi 6E 入门/中端 AP，6GHz 射频（<<<PAGE 33>>>、<<<PAGE 34>>>）。
13. **AP1511 / AP1521 / AP157x** — Wi-Fi 7（802.11be）AP 家族（<<<PAGE 36>>>、<<<PAGE 37>>>、<<<PAGE 18>>>）。
14. **OmniVista Cirrus (OVC)** — 云端 SaaS 网管平台，支持最多 12000 台设备（10000 AP + 2000 交换机）（<<<PAGE 286>>>、<<<PAGE 287>>>）。
15. **OmniVista 2500 / Terra** — 本地部署 NMS，对应 Enterprise 模式（<<<PAGE 11>>>、<<<PAGE 187>>>）。
16. **OV Cirrus 10 Device Catalog** — Cirrus 设备目录，管理设备申报与激活状态（<<<PAGE 308>>>）。
17. **R-Lab (Remote Labs)** — ALE 远程实验室，浏览器 RDP 接入 POD（<<<PAGE 5>>>、<<<PAGE 79>>>）。
18. **ALE Knowledge Hub / eBuy / MyPortal / Spacewalkers** — 培训平台 / 许可下单 / 合作伙伴门户 / 技术社区（<<<PAGE 8>>>、<<<PAGE 297>>>）。
19. **OmniVista Smart Tool (OST)** — 免费安装排障工具，含 PoE 向导、自动开票、流量分析（<<<PAGE 498>>>–<<<PAGE 504>>>）。
20. **OXO Connect** — ALE 中小语音平台，与 Stellar ZTP 集成（<<<PAGE 186>>>）。
21. **Rainbow** — ALE 协作云，可作为 Social Login 凭据源（<<<PAGE 369>>>、<<<PAGE 409>>>）。

## 部署模式与管理架构

22. **Express 模式（Wi-Fi Express）** — AP 自管理独立集群，最多 255 台，免许可，Web 向导配置（<<<PAGE 185>>>）。
23. **Enterprise 模式（Wi-Fi Enterprise）** — 由本地 OV2500 集中管理，最多 4000 AP（<<<PAGE 187>>>）。
24. **Cloud 模式（Wi-Fi Cloud）** — 由 OmniVista Cirrus 云管，最多 10000 AP（<<<PAGE 189>>>）。
25. **AP Group** — 同 Group ID + 同 VLAN 的 AP 自动组成的管理组，统一 Web 界面（<<<PAGE 202>>>；Cirrus 版见 <<<PAGE 277>>>）。
26. **PVM (Primary Virtual Controller)** — AP Group 中当选的主控 AP，承载统一管理界面（<<<PAGE 203>>>）。
27. **SVM (Secondary Virtual Manager)** — 备份主控，PVM 故障时接管（<<<PAGE 203>>>）。
28. **Provisioning Configuration** — Cirrus 中挂在 AP Group 下的配置档（Name/Site/RF Profile/Timezone 等）（<<<PAGE 331>>>）。
29. **Distributed Control** — 无控制器架构下 AP 间空口/LAN 直接交换漫游上下文与 RF 参数（<<<PAGE 280>>>）。
30. **Thin Client 模式** — 交换机不在本地存配置，全部从 OV2500 拉取（<<<PAGE 127>>>）。

## 认证与安全

31. **UPAM (Unified Policy Authentication Manager)** — Cirrus/OV 内嵌统一策略认证模块，含 RADIUS 服务器与 Captive Portal（<<<PAGE 188>>>、<<<PAGE 367>>>）。
32. **ASA (Authenticated Switch Access)** — 交换机管理通道认证框架，按 Console/Telnet/SSH/HTTP 等服务分别锁定（<<<PAGE 58>>>）。
33. **ARP (Access Role Profile)** — 六元组用户策略档案：VLAN/QoS/防火墙/L7 规则/位置/时段（<<<PAGE 376>>>；注意与地址解析协议 ARP 区分）。
34. **Captive Portal** — Web 认证门户，支持账号/接入码/条款/社交登录/自助注册（<<<PAGE 213>>>、<<<PAGE 409>>>）。
35. **Walled Garden** — 访客认证前即可访问的白名单站点集合（<<<PAGE 235>>>）。
36. **GuestOperator 账号** — 仅能管理访客账号的受限管理界面（<<<PAGE 234>>>）。
37. **802.1X** — 基于端口的接入认证，员工 SSID 常用（PEAP/MSCHAPv2）（<<<PAGE 211>>>、<<<PAGE 395>>>）。
38. **MAC 认证** — 按 MAC 地址到 RADIUS/UPAM 验证，可回传 Filter-ID 指定 ARP（<<<PAGE 384>>>）。
39. **Filter-ID** — RADIUS 属性，用于向 AP 下发应套用的 ARP 名（<<<PAGE 385>>>）。
40. **WPA2 / WPA3** — Wi-Fi 安全协议代际，Wi-Fi 6 起支持 WPA3（<<<PAGE 45>>>）。
41. **IEC 62443-3-3 Level 2** — 工控安全标准，8.10R3 起支持强制密码刷新（<<<PAGE 62>>>）。

## 交换机技术

42. **AOS R8** — OmniSwitch Release 8 操作系统（<<<PAGE 117>>>）。
43. **Working / Certified 目录** — Flash 中"待验证配置"与"已认证配置"双目录，支撑回滚（<<<PAGE 118>>>、<<<PAGE 131>>>）。
44. **Running Directory / Running Configuration** — 当前运行目录及 RAM 中的运行配置（<<<PAGE 131>>>）。
45. **vcboot.cfg / vcsetup.cfg** — 交换机启动与设置配置文件（<<<PAGE 131>>>）。
46. **write memory flash-synchro** — 保存并同步 certified 的组合命令（<<<PAGE 122>>>）。
47. **reload all** — 无条件从 certified 目录重启的命令（<<<PAGE 132>>>）。
48. **EMP (Ethernet Management Port)** — 交换机带外管理口，直连 CMM（<<<PAGE 66>>>）。
49. **CMM** — 交换机控制/管理模块（chassis 管理大脑）（<<<PAGE 66>>>）。
50. **Virtual Chassis (VC)** — 多台物理交换机虚拟化为一台逻辑设备（<<<PAGE 12>>>）。
51. **WebView** — 交换机内嵌 Web 管理界面，默认强制 HTTPS/TLS1.2（<<<PAGE 68>>>、<<<PAGE 69>>>）。
52. **Lightning Config (OLC)** — 开箱 5 分钟级快速配置向导，默认 IP 192.168.0.1（<<<PAGE 73>>>、<<<PAGE 475>>>）。
53. **Fast PoE (FPoE)** — 上电数秒内即向 PD 供电，不等系统完全启动（<<<PAGE 144>>>）。
54. **Perpetual PoE (PPoE)** — 交换机软重启期间对 PD 不断电（<<<PAGE 145>>>）。
55. **Delayed-start** — lanpower 延迟启动（120–600s）以等系统稳定（<<<PAGE 154>>>）。
56. **EEE (802.3az)** — 能效以太网，空闲低功耗，仅铜缆 100/1000M（<<<PAGE 146>>>）。
57. **PoE Class** — PD 功率等级，Class 1–8（bt Type 4），决定预算分配（<<<PAGE 147>>>）。
58. **802.1Q** — VLAN 打标标准，12bit VID 共 4096 个（<<<PAGE 165>>>、<<<PAGE 166>>>）。
59. **802.1p** — 802.1Q 头内 3bit 优先级字段，8 级 CoS（<<<PAGE 166>>>）。
60. **VLAN Mobile Tag** — 允许移动端口接收带标签帧并按 VID 动态入组，优先级高于其他 VLAN 规则（<<<PAGE 169>>>）。

## 无线与网络协议

61. **SSID** — 无线网络服务标识（网络名），与 VLAN 映射实现用户分流（<<<PAGE 215>>>）。
62. **mywifi-XXXX** — Stellar AP 出厂默认 SSID（MAC 后四位），默认管理 IP 192.168.1.254:8080（<<<PAGE 199>>>）。
63. **DHCP Option 138** — DHCP 下发 OV2500 地址、引导 AP 进 Enterprise 模式的选项（<<<PAGE 198>>>；Cirrus 代理场景见 <<<PAGE 290>>>）。
64. **MU-MIMO** — 多用户多入多出，Wi-Fi 5 起的下行、Wi-Fi 6 起上下行（<<<PAGE 45>>>）。
65. **MLO (Multi-Link Operation)** — Wi-Fi 7 多链路操作，提升可靠性与时延（<<<PAGE 44>>>）。
66. **AFC (Automated Frequency Coordination)** — Wi-Fi 7 标准 6GHz 自动频率协调（<<<PAGE 44>>>）。
67. **BLE / Zigbee** — AP 内置 IoT 射频技术，用于物联网与定位（<<<PAGE 28>>>）。
68. **DPI (Deep Packet Inspection)** — 深度包检测，AP/交换机应用识别能力（<<<PAGE 19>>>）。
69. **WIDS / WIPS** — 无线入侵检测/防护，含 Rogue 遏制（<<<PAGE 188>>>）。
70. **STP/RSTP/MSTP (802.1d/w/s)** — 生成树协议族，收敛 50s / <1s / <1s（<<<PAGE 238>>>）。
71. **Path Cost** — STP 端口路径开销，16bit/32bit 两套标准值（<<<PAGE 239>>>）。
72. **LACP (802.3ad)** — 链路聚合控制协议，LACPDU 协商动态聚合（<<<PAGE 252>>>）。
73. **Linkagg / admin-key** — AOS 聚合组及其端口归属键（<<<PAGE 254>>>）。
74. **Hash-control (brief/extended)** — 聚合/ECMP 负载分担哈希算法选择（<<<PAGE 259>>>）。
75. **cloud-agent** — 交换机上负责呼叫 Cirrus 激活服务器的代理进程（<<<PAGE 314>>>）。
76. **Call Home / Discovery Interval** — 设备周期性联系云管的机制，默认 30 分钟（<<<PAGE 314>>>）。
77. **OV Managed** — Cirrus 激活状态机的最终态，表示完全受管（<<<PAGE 310>>>）。
78. **ocloud_show** — Stellar AP 侧查看云连接状态的 CLI 命令（<<<PAGE 327>>>、<<<PAGE 357>>>）。
79. **QoE Analytics** — Cirrus 中来自设备的体验质量分析事件流（<<<PAGE 453>>>）。
80. **Golden Config** — Cirrus 中标记为基准的运行配置，用于审计漂移（<<<PAGE 439>>>）。
81. **GRE Tunnel（Use Tunnel）** — SSID 用户经 GRE 隧道集中到远端解除的映射方式（<<<PAGE 369>>>）。
82. **PoE Injector / Midspan** — 为非 PoE 交换机环境补供电的注入器（<<<PAGE 39>>>）。
83. **Mounting Kit** — AP 天花板/墙面安装套件（<<<PAGE 40>>>）。
84. **VMS (Video Management System)** — 视频监控管理系统，Lightning Config 提供组播参数选项（<<<PAGE 74>>>、<<<PAGE 492>>>）。
85. **RCL (Remote Configuration Load)** — 交换机远程配置加载服务器，存在时 Lightning Config 不触发（<<<PAGE 75>>>）。
