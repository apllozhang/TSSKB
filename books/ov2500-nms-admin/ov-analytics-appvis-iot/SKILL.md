---
name: Analytics、Application Visibility 与 IoT 监控
description: 需要做流量分析报表（Top N Apps/Clients/Ports）、应用识别与封禁（Signature Profile）、统计采集上仪表盘、定期 PDF 报表、IoT 终端画像或 OVNA 云端协同时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 老板要看 Top N 应用/客户端/端口利用率报表，或交换机健康趋势上仪表盘
- 需要识别并封禁社交/游戏类应用（Facebook/Bet365 等）
- 网络里 IoT 终端（打印机/摄像头等）需要自动识别与分类管理

## I（核心理念）
Analytics 的数据面是 sFlow 采样：交换机发 sFlow 包 → OV Analytics Service → Mongo DB → WebServer 呈现，应用识别靠 sFlow 里的 TCP/UDP 端口。AppVis 在此之上用签名文件做深度识别并可下发 enforcement（DROP）。所有 Profile 都有"一机一档"限制：一台交换机同一时刻只能属于一个同类 Profile。IoT 画像靠 MAC OUI + DHCP 指纹（Option 55/60）。

## A1（行动框架）
1. **AppVis 配置四步**（<<<PAGE 371-375>>>）：Network → Application Visibility → 先在 Devices Management 确认设备无 Profile → Signature Files 导入（如 AppSig.upgrade_kit_3）→ Signature Profiles → "+"：Name=OS6860_Profile、选 Signature File → Monitor Flow Count 组建 App Group（如 MyApps：Facebook/Twitter/youtube/bet365）→ Bandwidth Usage and Enforcement 组选 MyApps、ACL/QoS 字段点 N/A 设 Disposition=DROP → Create Profile → Apply to Devices（选设备与端口 1/1/1、1/1/5）
2. **验证 AppVis**：交换机日志出现 "Kit update complete"；PolicyView Users and Groups > Unified Policies 出现自动生成策略（含 MyApps）；CLI：`show app-mon config`、`show app-mon ipv4-flow-table monitor|enforcement verbose`、`show app-mon app-record hourly`；客户端访问 facebook.com 被阻断（<<<PAGE 376-382>>>）
3. **Analytics Profile**：Network → Analytics → Profiles → "+"：Profile Name、Profile Type（Top N Apps & Clients / Top N Ports Utilization）→ 选交换机并 Add Ports → Create；Reports 页查看 Top N Clients/Ports/Applications（<<<PAGE 384-389>>>）
4. **统计采集与仪表盘**：NETWORK > ANALYTICS > Statistics → Collection 编辑 Default Profile 属性集；Statistics → Selectors：Attributes（Switch Health CPU/内存/温度、Port Rx/Tx Bytes）+ Devices + Counters → View 图形/View Table → Save Selection As…（My_View_Profile，刷新 2 分钟）→ 首页 Performance Monitoring → Add Widget 绑定 Profile（<<<PAGE 390-394>>>）
5. **定期 PDF 报表**：Report Configuration → Create：Report Title、Purging Policy、Schedule（Now/Periodically，Simple 或 Cron）；再到各报表右上 Export → Add to Report 挂入视图；Report → List 下载/删除 PDF（<<<PAGE 354-357>>>）
6. **IoT**：Managed Devices List 勾选设备 → Enable IoT；IoT Inventory 展示 End Point MAC/IP、Status（Active/Offline/Error）、Category、Manufacturer、Port/ESSID、起止时间，可导出 .xls（<<<PAGE 404-405>>>）

## A2（进阶应用）
- 报表体系分两类（<<<PAGE 317-318>>>）：Visibility（Top N Apps/Clients/Ports/POE，需先建 Analytics Profile）与 Availability（设备状态/Alarms）；KPI 对应机制：Top N Apps ← sFlow 采样+端口识别、Top N Switches ← CPU/内存/温度派生指数、Top N Port ← SNMP MIB Polling（<<<PAGE 321>>>）
- Top N Ports 趋势预测（机器学习）：按 Training Timeout 采样历史，在 Training Error 内预测未来利用率；预测区间随查看区间变化（24h→12h、7 Days→3 Days、4 Weeks→2 Weeks）（<<<PAGE 334>>>）
- 应用端口映射双模式：Range-Based（范围内端口被监控，未映射标 Unknown）vs Enumerated（只监控定义过的端口）；.json 映射文件导入会**覆盖**现有映射（<<<PAGE 350-351>>>）
- 签名机制：Signature File → Signature Profile，一机一 Profile；OS6860E/N 支持 Auto-Update，OV 自动从 ALE 签名仓库检查下载并更新 Profile（<<<PAGE 360/372>>>）
- IoT 画像与执法：识别用 MAC OUI + DHCP FingerPrinting（Option 55 参数请求列表、Option 60 厂商标识）（<<<PAGE 400>>>）；Enforcement 按 Category 关联 Access Role Profile 做类级认证，可按 SSID/MAC/AP Group/IP 豁免（<<<PAGE 408>>>）
- OVNA 云边协同：五步集成——OVE API Key（Security > External Apps）→ OVNA UUID → OVNA 侧 Declare OVE（填 URL/API Key）→ OVE 侧 Enable OmniVista Network Advisor（填名称/IP/UUID）→ Rainbow bubble 监控；同步周期每小时；设备需配管理 IP、syslog 且可达 OVNA；设备要求 OS 6xxx/9xxx AOS 8.7R2+、Stellar AP AWOS 4.0.3 MR-3+（<<<PAGE 422-434>>>）
- VM Manager：单一 vCenter 接口跟踪 VM 及其网络关联、管理 VM 的 UNP VLAN、误配置未加入 UNP 时告警（<<<PAGE 30>>>）

## E（实证案例）
- OS6860-B 监控+封禁社交/游戏应用（MyApps → DROP，客户端访问 facebook.com 被阻断）——cases·AppVis 实验（<<<PAGE 371-382>>>）
- Analytics Profile 创建与报表/Widget 展示——cases·Analytics Profile（<<<PAGE 384-389>>>）
- 统计采集自定义 View Profile 上仪表盘——cases·Statistics（<<<PAGE 390-394>>>）

## B（边界与陷阱）
- 一机一档：Analytics Profile、Signature Profile、统计采集 Profile 均要求一台交换机只属于一个同类 Profile；新建前须先从 Default Profile 解绑（<<<PAGE 342/372/391>>>）
- "NO DATA AVAILABLE" 多为数据生成时延而非故障：App Discovery 只显示流量生成后的数据，需 "Wait for 15-20 minutes before the applications are displayed in the OV widgets."（<<<PAGE 380/382>>>）
- 自定义数据仅存 3 个月，到达上限滚动覆盖（<<<PAGE 324>>>）
- IoT 仅 IPv4："IoT is supported on IPv4 devices only."；端点刷新周期 Stellar AP 5 分钟、AOS 交换机 15 分钟（<<<PAGE 404/405>>>）
- AppVis Apply 时 Check Service Stats 警告弹窗属已知提示，点 Ok 即可（<<<PAGE 376>>>）
- OVNA 设备不出现：等下次每小时同步，并核对设备管理 IP/syslog/可达性（<<<PAGE 433-434>>>）

## 来源
- frameworks·AppVis 四步框架（<<<PAGE 373-375/365-366>>>）、Analytics 报表体系（<<<PAGE 317-321>>>）
- principles·sFlow 原理（<<<PAGE 316/322/325>>>）、采样率（<<<PAGE 341>>>）、趋势预测（<<<PAGE 334>>>）、端口映射双模式（<<<PAGE 350>>>）、签名机制（<<<PAGE 360/372>>>）、AppMon（<<<PAGE 377-383>>>）、IoT 画像与执法（<<<PAGE 400-408>>>）、OVNA（<<<PAGE 422-423>>>）、统计采集分离（<<<PAGE 343/391>>>）、VM Manager（<<<PAGE 30>>>）
- cases·AppVis/Analytics/Statistics/PDF 报表/OVNA/IoT（<<<PAGE 371-394/354-357/424-434/404-405>>>）
- counter-examples·一机一档/NO DATA/3 个月上限/映射覆盖/IoT IPv4/OVNA 排障（<<<PAGE 342/372/391/380/382/324/351/404/433-434>>>）
