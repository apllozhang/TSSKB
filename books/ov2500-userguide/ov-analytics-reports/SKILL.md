---
name: Analytics 分析与报表排程
description: 需要出 Top N Applications/Clients/Ports/PoE 报表、配置 sFlow/Analytics Profile、Network Health 健康阈值、Statistics Collection/Chart View Profile、Application Visibility 签名档案、创建定时 PDF 报表时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- 要回答"网上最耗带宽的应用/客户端/端口是谁"
- 需要周期性采集端口利用率并画趋势图、做异常检测
- 为链路容量规划出定时 PDF 报表并邮件分发
- 部署 Application Visibility（L7 应用识别 + Enforcement）

## I（核心理念）
Analytics 是 Profile 驱动的报表体系：Top N Apps/Clients/Ports 报表必须先建 Analytics Profile（设备+端口+信息类型），实时类报表（Availability/Alarms/Health/SIP）免 Profile；Top N Apps-Advanced 由 Application Visibility 的 Signature Profile 驱动。数据面是 sFlow：建 Profile 时 OV 自动成为 sFlow Receiver，应用识别靠 sFlow 包中的 TCP/UDP 端口。统计采集与查看解耦：Collection Profile（采集什么）+ View Profile（怎么看）。

## A1（行动框架）
报表选型（frameworks·F3，<<<PAGE 66-67>>>）：
1. 要 Top N Apps/Clients/Ports Utilization/PoE → 先 Profiles 建 Analytics Profile（<<<PAGE 130-131>>>）
2. 要 Top N Apps-Advanced（L7 签名级）→ 先 Application Visibility 三步（<<<PAGE 202-203>>>）
3. 要 Network Availability / Alarms / Network Health / SIP → 直接出，无需 Profile
4. 要端口利用率趋势/预测/异常检测 → Statistics 基础统计四屏（frameworks·F5，<<<PAGE 117>>>）
5. 数据下钻粒度固定：月→周→日→时→15 分钟（frameworks·F4，<<<PAGE 72-74>>>）

## A2（操作步骤）
- **建 Analytics Profile**：Profiles→Add→Configuration（Profile Type：Top N Apps & Clients / Top N Ports Utilization / Top N PoE Ports Utilization；Sampling Rate；PoE Usage Threshold 1-99 默认 99 仅 AOS 8.x）→Device/Port Selection（可用 Default Ports Template 批量套端口如 1/1-1/10）→Create；PoE Profile 无需选端口（cases·C9，<<<PAGE 130-131>>>）
- **出 Top N Applications 报表**：Analytics→Reports→Top N Applications；默认 Summary 饼图（过去 24 小时）；Filter by Profile/Select Devices 过滤；点饼图扇区下钻 Clients/Switches；Configuration 配 Top 数(1-20)/Interval Type/Time Interval(24h|7d|4w)；Actions→Add to Report 转定时 PDF（cases·C4，<<<PAGE 74-82>>>）
- **App Advanced 过滤**：Filter Bar 设 Time Slice/Application/App Group/Source IP/Device/UNP/Time Range（Most Recent-最近 7 天 / Custom）（cases·C5，<<<PAGE 85-86, 89-90>>>）
- **健康阈值**：Network Health→选类别(CPU/Memory/Temperature)→ADD 选设备（一次最多 20 台）→Configure Health Thresholds→逐设备 Edit→Save；可直通 Configure Traps 向导（cases·C6，<<<PAGE 99-100>>>）
- **Collection Profile**：Statistics→Collection→Add：Poll Interval 1-60 默认 5 分钟、Data Retention 1-180 天默认 30、选设备+属性→Create；排程先 Stop→Schedule→重启（cases·C7，<<<PAGE 120-121>>>）
- **Chart View Profile**：Chart Views→Add：属性、设备、Counters（>50 个时须手动挑 ≤50）、Line Options、Scale(0.001-1000)→Create；可 Switch to Table / Save to PNG（cases·C8，<<<PAGE 122-124>>>）
- **端口↔应用映射**：Applications Management：Range-Based 或 Enumuated 模式；可 Import/Export .json（导入覆盖现有）；映射端口不可改只能删除重建（cases·C10，<<<PAGE 132-133>>>）
- **Application Visibility 三步**：导入 Signature File（可自动更新）→建 Signature Profile（监控组+Enforcement 组，Enforcement 还需 Unified Access 配 Access Role Profile）→应用到交换机/端口（cases·C21，<<<PAGE 202-203>>>）
- **创建定时报表**：Report→Add：Title/Purging Policy/Schedule(Now|Periodically Simple|Cron)/E-Mail（单一收件人，前置 Preferences Email）→Create（先产生空白报表）；再到目标屏 Add to Report 绑定（cases·C48，<<<PAGE 484-485>>>）

## E（实证案例）
- Top N Applications 从建 Profile 到饼图下钻再到定时报表（cases·C4，<<<PAGE 74-82>>>）
- Collection Profile 建+排程（Stop→Schedule→重启）（cases·C7，<<<PAGE 120-121>>>）
- Network Health 阈值 + Configure Traps 直通（cases·C6，<<<PAGE 99-100>>>）
- Application Visibility 从签名文件到交换机应用（cases·C21，<<<PAGE 202-203>>>）

## B（反例/坑）
- sFlow 包不能经 EMP 端口发送——发现交换机不能用 EMP IP，否则收不到 Top N App 数据（counter·X1，<<<PAGE 75, 92>>>）
- 未定义 FTP 凭据时备份/恢复/升级会逐台弹窗询问（counter·X2，<<<PAGE 43>>>）
- 外部 RADIUS 登录的管理员只能出实时报表、不能排程（counter·X6 / principles·P13，<<<PAGE 64>>>）
- 改交换机 IP 后已指派的 Top N App & Clients Profile 失效，须重新指派（counter·X7，<<<PAGE 131>>>）
- 统计采集静默失败：设备 SNMP 源 IP 与 OV 发现 IP 不一致时收不到数据且无报错（counter·X8 / principles·P24，<<<PAGE 119>>>）
- 删除 Statistics/View Profile 连带删除全部历史统计（counter·X9，<<<PAGE 121, 129>>>）
- 健康阈值修改最长 1 小时（下个轮询周期）后才可见（counter·X10 / principles·P20，<<<PAGE 100>>>）
- 健康阈值一次最多 20 台，超过按钮不激活（principles·P19，<<<PAGE 99>>>）
- "Enable Statistics Automatically On" 选 All 且设备量大有性能风险；升级环境默认 0 台不会自动开启（counter·X12，<<<PAGE 134>>>）
- Periodic 报表不能手动 Generate；首次建报表配置生成的是空白报表（counter·X45/X46，<<<PAGE 484-486>>>）
- 端口利用率低于 1%、PoE 为 0% 的端口不显示；PoE 报表需 CLI 预先启用（principles·P21，<<<PAGE 101, 106>>>）
- 一台交换机同一 Profile Type 只能入一个 Profile；移除端口连带删 sFlow 配置（principles·P27，<<<PAGE 130-131>>>）
- 异常检测最少需 11 天数据、季节性最多学 30 天（principles·P29，<<<PAGE 133-134>>>）
- 含不支持 AV 的 AP 的组应用签名档案：操作"成功"但部分 AP 未生效；会清掉 CLI 配置的 AV 配置（counter·X21/X22，<<<PAGE 209>>>）
- 签名档案向导里配的 Access Role Profile 不会自动下发设备（counter·X23，<<<PAGE 208>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 3 章 Analytics（<<<PAGE 64-136>>>）、第 6 章 Application Visibility（<<<PAGE 201-211>>>）、第 26 章 Report（<<<PAGE 484-486>>>）。条目来源：frameworks F3/F4/F5/F6；cases C4-C10/C21/C48；counter-examples X1/X2/X4/X5/X6/X7/X8/X9/X10/X12/X21/X22/X23/X45/X46；principles P12-P29。
