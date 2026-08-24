---
name: upam-policy-bandwidth
description: 何时用：认证之后要做限制——Unified Policy 条件动作配置、三层带宽控制选层、访客账号配额与 Service Level 分级运营。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# UPAM 统一策略、三层带宽控制与访客配额治理

## R · 原文引用

> "The first step is to create a Policy Condition. A policy Condition defines the type of traffic that will be inspected ... The next step is to define the Action. A policy action defines the treatment that will be given to the traffic that matches the condition." (p413-414)

> "Bandwidth contract at SSID level: Bandwidth assigned per SSID and per AP, shared between all users connected to the SSID ... at Access Role Profile level: Bandwidth assigned to the users using this profile ... at Role level: A Policy List (ACL/QoS) can restrict the Bandwidth as an action" (p408)

> "Defines, per user, a validity period, a time and data quota and an exhaustion handling, when the quotas are reached. ▪Data Quota ▪Time Quota ▪Exhaustion Handling: Block for remaining Duration (Redirection URL) / Reduced up/down bandwidth (in kB/s)" (p429)

## I · 方法论骨架

**1. Unified Policy 配置流程（顺序固定：先策略后绑定）**
```
1. Policy Condition（L3 目的子网 + L4 服务端口；端口对象不存在先建 Service Port）
2. Action（Accept/Drop、优先级标记 802.1p/DSCP、限速、三色标记 TCM）——双向执行
3. Group Assignment（指定生效的 AP Group，勿含 default）
4. 把策略（列表）挂到 SSID 的 ACL/QoS 框（或 ARP 默认策略/RADIUS 账号属性）才生效
```
另有 Location Policy（限定接入位置）与 Period Policy（限定日/时段）。
验证手法：先测基线（ping/SSH 通）→ 挂策略 → 复测对比。

**2. 三层带宽控制与执行优先级**

| 层 | 落点 | 粒度 |
|---|---|---|
| SSID 合同 | Detailed SSID Settings | 每 SSID 每 AP，组内用户共享（兜底） |
| ARP 合同 | Bandwidth Control 段 | 使用该角色的每用户 |
| 策略规则 | Policy List 的 ACL/QoS 动作 | 命中流量的应用级 |

执行判定序：**策略 > 角色 > SSID**——先匹配 Policy List 命中即按 ACL；未命中看 ARP；再无看 SSID 合同；都无则不限速。
套餐设计映射：全员总量=SSID 合同，身份差异化=ARP，应用级=策略。

**3. 访客账号体系（四类账号）**
- Employee：登录/密码必填；可配 Session timeout、计费间隔、上下行带宽上限
- Company Property：MAC 必填，用于 BYOD/DSPSK，可绑员工账号/ARP/Policy List，可下发专属 PSK
- Guest：登录/密码/失效日期/Service Level 或 Registration Profile 必填；支持批量建号与票据打印
- Guest Operator：前台账号，专属门户只管访客开户/审批自注册/批量导入 XLSX/CSV

**4. 三层治理对象**
- Registration Profile：数据配额（MB）+ 时间配额（每日小时/总小时）+ 有效期 + Remember Device/最大设备数 + 耗尽处理（阻断可加重定向 URL，或降速分设上行/下行 kB/s）
- Service Level（最多 5 档）：打包 ARP + Unified Policy List + Registration Profile + 有效期 + 删除策略
- 全局设置：批量生成、过期删除策略（Never/到期/N 天后）、密码策略

书中配额实例：100MB + 每天 4h；耗尽降速 UP=100kB/s、DOWN=1000kB/s；Day1 用 90MB/3h 无动作，Day2 累计 115MB 触发。

## A1 · 书中案例（Lab 步骤精要）
- **c17/p411-416**：基线 ping/ssh 192.168.20.7 均通 → 建 Block_SSH（Condition L3=192.168.20.0/24 + L4=TCP 22，无 SSH 选项先建 Service Port）→ Action=Drop → Group Assignment=My-AP-Group → 挂到 EmployeesX 的 ACL/QoS → 复测 ping 通 SSH 拒。
- **c23/p417-434**：四类账号界面操作 + Registration Profile 配额触发实例 + Guest Operator 门户（建号/审批/批量导入）。

## A2 · 触发场景（含与相邻 skill 的区分）
- "认证已经通了，现在要限速/禁某些应用/给访客配额/分级服务"时用。
- **区分**：让终端进门（Employee/Guest/BYOD 的认证与 VLAN）→ `ssid-authentication-suite`；本 skill 管"进门之后给什么待遇"。RF 层调优（信号/信道）→ `rf-optimization-baseline`。

## E · 可执行步骤
1. 明确限制目标，按三层模型选落点（总量/身份/应用）。
2. 按"Condition → Action → Group → 挂 SSID/ARP"顺序建策略，勿颠倒。
3. 带宽设计按优先序唯一化：避免三层重复设值造成解释困难。
4. 访客运营：建 Registration Profile（配额+耗尽处理）→ 建 Service Level 打包 → 交 Guest Operator 日常开号。
5. 验证：策略做前后对比测试；配额跑两天观察触发；Authentication Records 审计。
6. 收紧员工密码策略（最小长度+复杂度），高安全场景认证源改外部 RADIUS/LDAP/Azure AD。

## B · 边界与陷阱
- 顺序错了策略不生效：不挂到 SSID 的 ACL/QoS 或 ARP，策略只是摆设。
- Group Assignment 含 default 组会导致策略作用面失控。
- 员工账号默认弱密码/弱用户名策略，生产必须收紧（ce38）。
- SSID 级合同是共享池：单个用户可占满全组带宽，需精细控制时下沉到 ARP/策略层。
- 策略动作双向执行，改 Drop 类动作前先明确影响面（参考基线-复测法）。

---
来源条目: f14, f15, f27, p44, p45, p46, c17, c23, ce38 · 术语锚点: g54, g10, g05
