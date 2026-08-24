---
name: security-unified-access
description: 用 Access Guardian 四环节做准入安全方案：UNP 动态角色、IoT 画像、上下文策略、MACsec 端口矩阵与 AppMon 应用管控。
source_book: DT00XPS281EN Campus LAN Presales
---

# 安全与统一接入（AG/UNP/画像/MACsec/AppMon）

## R · 原文引用

> "ACCESS GUARDIAN SECURITY FRAMEWORK — Authentication: 802.1x, MAC, Captive Portal, RADIUS; Classification: UNP profile rules; Role-Based Access: UNP profiles, QoS policy lists, BYOD; Restrict or Block: Restricted roles, Re-authentication, Quarantine, Remediation" (p147)

> "Initial UNP (which provides the initial policy list and role) and Vlan does not change during the lifetime of the user. Only the roles change dynamically" (p152)

> "CONTEXT-BASED POLICY MANAGEMENT — User + Device + Situation = Policy to be enforced … e.g. Lower priority of all app group social media between 8:30 AM and 4:30 PM" (p157)

## I · 方法论骨架

**四环节框架**（安全方案分册骨架 + 竞标应答归类法）：认证（802.1x/MAC/Captive Portal 可同端口多法并存，2260/2360 入门机也支持）→ 分类（UNP 规则贴档案）→ 基于角色授权（VLAN+ACL+QoS 跟人走）→ 限制/阻断（受限角色、重认证、隔离、补救）。核心卖点：**内建于交换机，不需要独立 NAC 盒子**。

**UNP 两级认证模型**：L2 认证（802.1x/MAC/分类）产出初始 UNP（定 VLAN+初始策略）；L3 分类叠加 QMR/位置/时间校验，失败落受限角色。铁律：**初始 VLAN 终身不变、只有角色动态变**——排障地图即"用户落在了哪个角色"。

**上下文策略公式**：策略 = 用户 + 设备 + 情境（时间/位置/姿态/介质），输出限访问/隔离/优先级/带宽控制。需求三问：谁、用什么设备、什么时间地点——把客户口语转成策略条目（例句：工作时间降社交应用优先级、营销部外全员禁 Facebook、P2P 限 1Mbps）。

**IoT 画像闭环**：终端先入临时 UNP → 四种指纹采集（MAC OUI、DHCP option 55、option 60、最多 5 条 HTTP User-Agent）→ 按类别自动下发 UNP（内置摄像头/传感器/医疗等类别模板）→ 未知设备既不断网也不放任。无 Agent 安全的哑终端治理骨架。

**应用可视化四步**：Enable（签名库订阅、OneTouch 下发）→ Monitor（DPI Top N）→ Enforce（按角色限速/阻断）→ Analyze。常数：AppMon 免许可，仅 6860N/6870 全系，单机 8K 流、VC（8 台）64K 流，自定义签名最多 2000 条。

**MACsec 端口矩阵要点**（照表承诺，不照宣传）：6870 全机型全端口（除 24/48 的 VFL 口）；6860N-U28 全口除 VFL、P48Z/P24Z 仅 SFP28 上联；6560-P24X4 25-30 口不支持、P48X4 49-52 仅动态、53-54 不支持；6570M-12 无 Static。许可见 license skill。

## A1 · 书中案例

p157 五条策略例句（社交降级/部门禁 Facebook/P2P 限速等）证明公式可逐条落地；c09 的 6860N VC 边缘方案附带 AppMon 能力作为方案亮点。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：标书"网络准入/安全接入/应用管控"条款；客户哑终端（摄像头/传感器/医疗）入网治理；"看不见应用流量"的抱怨。
- 区分：本 skill 管**准入安全与应用管控的方案结构**；MACsec 的许可与下单在 `license-wwpl-pricing`；QMR 隔离处置与 UPAM 计价跨到 `nms-platform-and-network-advisor`；视频监控垂直方案在 `video-surveillance-design`。

## E · 可执行步骤

1. 把客户准入需求逐条归类到四环节之一，对号入座答特性。
2. 用三问法收集策略需求，按公式写成策略条目清单。
3. 哑终端场景画画像闭环图（指纹→类别→UNP 自动下发）。
4. 应用管控按四步给分阶段路径：先可视化切入，再追加管控（典型分阶段销售）。
5. 加密需求逐口核对 MACsec 端口表，只承诺支持端口之间。

## B · 边界与陷阱

- ce10：MACsec 全端口承诺会翻车——6560 的 25-30/53-54 口等多处明确不支持，堆叠 VFL 链路加密只有 6870 的 Z/M/V 型可做。
- AppMon 仅 6860N/6870 硬件支持，给其他机型承诺应用可视化为虚假应标。
- "初始 VLAN 不变"是排障关键：用户"权限不对"先查角色而非 VLAN。
- 入门机型（2260/2360）支持 AG 但无高级特性，承诺前过功能矩阵。

---
来源条目: f19, f20, f21, f22, f24, p24, p39, p40, p41, ce10, g01, g04, g09, g11, g12, g14, g24, g34, g41, g42
