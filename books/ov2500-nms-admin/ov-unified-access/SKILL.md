---
name: Unified Access 三层策略与 802.1X 接入
description: 需要做有线/无线统一接入认证（RADIUS + 802.1X/MAC Auth）、配置 AAA Server Profile → Access Role Profile → Access Auth Profile 三层模板、Access Classification 回退分类或 Captive Portal 时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 园区要按用户角色（Employee/Guest）区分 VLAN、带宽、优先级
- 新上 RADIUS 服务器，要把 802.1X 认证落到接入端口
- 客户端认证失败/落错 VLAN，需要排查 UNP 匹配链路

## I（核心理念）
Unified Access 是三层模板模型：AAA Server Profile 定义认证服务器参数 → Access Role Profile 定义 UNP 属性（QoS 策略表、Access Policies、Captive Portal 认证）→ Access Auth Profile 把预定义 UNP 端口配置指派到边缘端口；Unified Policy 挂在 Access Role Profile 之下。认证不可用时由 Access Classification 规则兜底决定 profile。

## A1（行动框架）
1. **建认证服务器**：Security > Authentication Servers > RADIUS：建 RADIUS_VM（IP 192.168.100.102 / secret alcatel-lucent）（<<<PAGE 258-259>>>）
2. **AAA Server Profile**：Unified Access > Unified Profile > Templates：802.1X Primary 与 MAC Primary 均指向 RADIUS_VM（<<<PAGE 259>>>）
3. **Access Role Profile**：建 UNP-employee（**名称必须与 RADIUS 返回的 Filter-ID 完全一致**）→ Apply to Devices（Map to VLAN 80、选 6860B）（<<<PAGE 261-263>>>）
4. **Access Auth Profile**：建 UNP_template（AAA=AAA_RADIUS、Port Bounce/MAC Auth/802.1X Auth Enabled）→ Apply to Devices 选端口（如 6860B 1/1/1）（<<<PAGE 264-265>>>）
5. **验证**：`aaa test-radius-server RADIUS_VM type authentication user employee password password` 应返回 Filter-ID = UNP-employee；客户端启用 IEEE 802.1X；`unp user flush port 1/1/1` 清状态后重连；`show unp user` 应显示 employee/VLAN 80/UNP-employee；Network → Locator 按 Auth. User=employee Live 查询（<<<PAGE 263-268>>>）

## A2（进阶应用）
- 用户角色导向策略：Employee Profile → VLAN 20/更高带宽与优先级；Guest Profile → VLAN 30/仅 Internet/更低带宽优先级，由 "OV 2500 / UPAM" 下发（<<<PAGE 231>>>）
- Access Auth Profile 端口行为细节（<<<PAGE 241-242>>>）：Port Bounce——COA 后客户端换 VLAN 时端口被管理性 down 以触发 DHCP 续租与重认证；802.1X Pass Alt / Bypass Status 可跳过 802.1X 直入 MAC 认证或分类；Failure Policy、MAC Pass Alt / MAC Allow EAP；"802.1X Auth and MAC Auth only applies to wired devices."
- Access Classification 回退规则（<<<PAGE 243-244>>>）：认证不可用时按规则定 profile；有线规则类型 Port/MAC/MAC OUI/MAC+Port/MAC+IP+Port/LLDP/认证类型/IP+Port；无线规则类型 MAC/BSSID/ESSID/DHCP Option/DHCP Option 77/加密类型/位置
- Captive Portal 分层（<<<PAGE 252-255>>>）：CP Profile 仅对启用 CP 认证的 Access Role Profile 有效；Profile Domain Policy List 按登录域分配 CP Profile + QoS，Domain Policy List 按认证 realm 定义策略；定制 html/jpeg 文件构成登录页
- UPAM 代管交换机账号：Switch User Account 经 UPAM 建交换机用户，再建 AAA Profile 指定 UPAM 为访问服务器并指派给交换机；Switch Access Record 可查经 UPAM 的认证记录（<<<PAGE 166-167>>>）

## E（实证案例）
- Unified Access 全流程实验（RADIUS → AAA Profile → UNP-employee → UNP_template → 端口 1/1/1，客户端验证 VLAN 80）——cases·Unified Access（<<<PAGE 258-268>>>）
- 客户端缺认证页签：services.msc 启动 Wired AutoConfig 服务——cases·客户端排查（<<<PAGE 266>>>）

## B（边界与陷阱）
- UNP 命名不一致则匹配失败："Type the UNP name as shown as it is the value returned from the RADIUS server"（<<<PAGE 263>>>）
- 重认证前必须 `unp user flush port 1/1/1` 清残留会话；出现第二个不同 MAC 条目是物理网卡关联，勿误判异常（<<<PAGE 268>>>）
- 客户端必须取消缓存凭据、取消自动用 Windows 登录名密码、取消 Validate server certificate，否则测试不成立（<<<PAGE 267-268>>>）
- 客户端拿不到 DHCP 时先确认 AAA Training Server VM 已开机，再不行配 192.168.80.X 静态 IP/网关 192.168.80.8（<<<PAGE 290>>>）

## 来源
- frameworks·三层策略模型（<<<PAGE 235/246/259-265>>>）、用户角色导向策略（<<<PAGE 231>>>）、Access Classification（<<<PAGE 243-244>>>）
- principles·Captive Portal 分层（<<<PAGE 252-255>>>）、Access Auth Profile 端口行为（<<<PAGE 241-242>>>）
- cases·Unified Access 全流程/客户端排查（<<<PAGE 258-268>>>）
- counter-examples·认证页签不可见/未清 UNP 状态/DHCP 排障/命名不一致（<<<PAGE 266-268/290/263>>>）
