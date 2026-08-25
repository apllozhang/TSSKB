---
name: AOS 8 CLI 命令地图——L2 接入域（端口/PoE/VLAN/聚合/VC/环网，第 1-8/12-17/20 章）
description: 需要在 OmniSwitch AOS 8 上配置端口物理参数、PoE 供电、VLAN/PVLAN/VLAN Stacking/MVRP、链路聚合、STP/环网保护、Virtual Chassis 时，用本地图定位 CLI Reference 对应章节与代表命令。
source_book: OmniSwitch AOS Release 810R04 CLI Reference User Guide
---

## R（触发场景）
- 要查某条 L2/接入命令的完整语法、默认值、平台支持矩阵
- 不确定某配置属于哪一章，需要"域→章→命令"导航
- 端口违例恢复、PoE 分级、聚合哈希、VLAN 删除语义等关键默认值核对

## I（核心理念）
CLI Reference 是 6240 页命令字典，每条命令按"语法→参数→默认值→平台矩阵→用法指南→示例→Release History→相关命令→MIB Objects"固定结构展开；正确用法是先定位章（按本地图），再回书按页码查命令全文，不做通读。本域覆盖接入层命令：`interfaces`（30+ 子命令）、`lanpower`、`vlan`/`pvlan`、`linkagg`、`spanty`/`bridge`、`erp`/`mrp`、`virtual-chassis`。页码取 PDF 全文标记 `<<<PAGE N>>>`（第 1 章始于 <<<PAGE 67>>>，对应书内页 1-1）。

## A1（决策框架）
1. **物理层/端口参数**→第 1 章；**PoE 供电**→第 2 章；**UDLD**→第 3 章
2. **MAC 学习**→第 4 章；**VLAN/PVLAN**→第 5 章；**HA VLAN**→第 6 章；**QinQ**→第 7 章；**MVRP**→第 17 章
3. **环路防护**→第 8 章（STP）/第 12 章（LBD）；**聚合**→第 13 章；**环网**→第 15 章（ERP）/第 16 章（MRP）
4. **VC**→第 14 章；**自动织构**→第 20 章
5. 查到章后按章首页码进原书，用命令名检索条目

## A2（操作步骤）·章节清单与代表命令
- **Ch1 Ethernet Port（<<<PAGE 67>>>，约 85 条）**：`interfaces <port> speed|duplex|fec|break-out|eee|ddm`、`interfaces link-monitoring link-flap-threshold`、`violation`/`clear violation`；`show interfaces status/counters/counters errors/ddm`（P1/P2）
- **Ch2 PoE（<<<PAGE 254>>>，约 38 条）**：`lanpower slot port ...`（供电/预算/优先级/power rule）；802.3at 须先 `lanpower slot class-detection`，802.3bt（固件 3.xx）自动启用；power rule 先创建再绑定（P3/X7）；6465 不能自动检测电源类型，必须手工配置（P4/X9）
- **Ch3 UDLD（<<<PAGE 327>>>，约 12 条）**：`udld port ...` 单向链路检测
- **Ch4 Source Learning（<<<PAGE 351>>>，约 33 条）**：`mac-address-table` 学习/过滤/老化
- **Ch5 VLAN Management（<<<PAGE 427>>>，约 13 条）**：`vlan vlan_id [admin-state {enable|disable}] [name | prompt-on-deletion]`（默认 enable/disable）；`vlan 10-15` 区间写法；删除 VLAN 自动剥离成员、端口回落 VLAN 1（P5/P6）；`pvlan`/`pvlan secondary`/`pvlan mapping`（P7）
- **Ch6 HA VLAN（<<<PAGE 455>>>，约 10 条）**：跨机箱 VLAN 高可用同步
- **Ch7 VLAN Stacking（<<<PAGE 476>>>，约 40 条）**：`vlan stacking`（QinQ 双层标签/保留 VLAN/NNI-UNI 角色）；保留 VLAN 不能用标准 vlan 命令配（X18）
- **Ch8 Distributed Spanning Tree（<<<PAGE 567>>>，约 50 条）**：`spanty`/`bridge`
- **Ch12 Loopback Detection（<<<PAGE 1070>>>，约 11 条）**：`loopback-detection`
- **Ch13 Link Aggregation（<<<PAGE 1092>>>，约 46 条）**：`linkagg ...`（静态/LACP，动态仅兼容 IEEE 802.3ad）；`hash-control brief` 模式哈希退化为源 MAC（L2）/源 IP（L3）（P10/X16）；聚合不能配在 AppMon 已启用端口（X12）
- **Ch14 Virtual Chassis（<<<PAGE 1198>>>，约 32 条）**：`virtual-chassis`（VFL/chassis group）；chassis id 下次重启才生效（X10）；VC 只支持同型号两台（如 6860 与 6900 之间不支持）（X20）
- **Ch15 ERP（<<<PAGE 1268>>>，约 16 条）**：`erp`（ITU-T G.8032 环倒换）
- **Ch16 MRP（<<<PAGE 1306>>>，约 11 条）**：`mrp`（IEC 62439-2 工业环）
- **Ch17 MVRP（<<<PAGE 1340>>>，约 23 条）**：`mvrp`（802.1ak 动态 VLAN 注册）
- **Ch20 Automatic Fabric（<<<PAGE 1523>>>，约 12 条）**：`fabric`/`auto-fabric`

## E（实证案例）
- 本系列为命令地图型 skill，不搬运配置案例；原书每条命令自带 Example 小节，定位到章后按页码回查即可（cases 原件未创建，E 段说明见书报告）

## B（反例/坑）
- 802.3at 供电必须先 `lanpower slot class-detection` 启用分级检测；802.3bt 下自动启用、手工命令不受支持（X7）
- 6465 不能自动检测电源类型，不手工配置则系统与 PoE 功率信息显示错误（X9）
- 默认删除带成员端口的 VLAN 不弹确认——误删风险由 prompt-on-deletion 兜底，默认 disable（X22，<<<PAGE 428>>>）
- VLAN Stacking 保留 VLAN 不可用标准 vlan 命令配置；NNI 口成为 stacking 口后 TPID（非 0x8100 时）不可再改（X18）
- legacy BPDU 仅 flat STP 模式支持，且只应在连 legacy 设备的 Stacking 网络端口启用（X19）
- VC 只支持同型号两台；`no virtual-chassis` 仅在无任何 VFL 配置时可用（X20）
- UNP 动态创建的 VLAN 不能用标准 `no vlan vlan_id` 删除（X15，第 42 章，详见 aos-cli-map-mgmt-oam 域说明）
- chassis identifier 到目标机箱下次重启才生效（X10）

## 来源
OmniSwitch AOS Release 810R04 CLI Reference User Guide 第 1-8、12-17、20 章（<<<PAGE 67-689、1070-1390、1523-1549>>>）。条目来源：principles P1-P7/P10；counter-examples X7/X9/X10/X12/X15/X16/X18-X20/X22；frameworks F1-F3/F5（域分组）。
