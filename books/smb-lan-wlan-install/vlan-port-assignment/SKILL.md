---
name: VLAN 规划与端口分配
description: 当需要在 OmniSwitch 上创建 VLAN、做 tagged/untagged 端口分配、规划多 VLAN（管理/员工/访客）或激活 VLAN 间路由时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- SMB 网络要按管理/员工/访客分网段，需要在交换机上划 VLAN
- AP 口要同时承载管理 VLAN（untagged）与业务 VLAN（tagged）
- 需要用 WebView 图形界面或 CLI 建/删 VLAN 并交叉验证

## I（核心理念）
VLAN 逻辑分段 LAN，所有端口默认属于 VLAN 1；端口的 untagged VLAN 就是它的 default VLAN，多个 VLAN 走同一物理口时其余打 802.1Q tag。典型 AP 口模式：管理 VLAN untagged + 业务 VLAN tagged。任一 VLAN 绑定 IP 接口即自动激活三层路由，交换机成为各网段的虚拟网关。

## A1（行动框架）
1. 建 VLAN（多词名字要加引号）：
   ```
   -> vlan 10 name Management-AP
   -> vlan 20 name Employees
   -> vlan 30 name Guests
   ```
   （P21，<<<PAGE 159>>>–<<<PAGE 160>>>）
2. 上联口打标：`-> vlan 10|20|30 members port 1/1/3 tagged`
3. AP 口混合模式：
   ```
   -> vlan 10 members port 1/1/6 untagged
   -> vlan 20 members port 1/1/6 tagged
   -> vlan 30 members port 1/1/6 tagged
   -> show vlan members port 1/1/6    // 验证
   ```
   （C09，<<<PAGE 173>>>–<<<PAGE 175>>>）
4. 激活 VLAN 间路由：`-> ip interface <name> address <ip/mask> vlan <vlan_id>`，任一 IP 接口绑定即开启路由（P22，<<<PAGE 162>>>）。
5. WebView 路线：Layer 2 > VLAN > "+" > 填 VLAN 59 / 描述 Student > SUBMIT > Save > CLI `show vlan` 交叉验证；删除同理（勾选后点 Delete 图标）（C06，<<<PAGE 113>>>–<<<PAGE 114>>>）。

## A2（进阶应用）
- 端口入组四途径：Static Configuration / Mobility（含认证）/ 802.1Q / VLAN Mobile Tag（P20，<<<PAGE 158>>>）。
- 802.1Q 标签结构：4 字节 = 12bit VLAN ID（共 4096 个）+ 3bit 802.1p 优先级（8 级 CoS）（P23，<<<PAGE 166>>>）。
- Mobile Tag 允许移动端口收带标签帧并按 VID 动态入组，优先级高于一切 VLAN 规则；802.1Q 静态打标不支持移动端口（P24，<<<PAGE 170>>>）。
- DHCP 地址规划参考（实验基线）：VLAN10 管理 192.168.10.70-79 / VLAN20 员工 192.168.20.70-79 / VLAN30 访客 192.168.30.70-79（C30，<<<PAGE 88>>>）。
- 客户端定位：`-> show mac-learning` 按 MAC 找端口（如 dc:08:56:00:0c:e0 在 1/1/6）（C10，<<<PAGE 181>>>）。

## E（实证案例）
- 三 VLAN 规划：vlan 10 Management-AP / 20 Employees / 30 Guests，上联 1/1/3 全 tagged，AP 口 1/1/6 为 VLAN10 untagged + VLAN20/30 tagged，`show vlan members port 1/1/6` 验证（C09，<<<PAGE 173>>>–<<<PAGE 175>>>）。
- WebView 建 VLAN 59（Student）后用 `show vlan` 交叉验证（C06，<<<PAGE 113>>>–<<<PAGE 114>>>）。
- 员工 SSID 客户端落在 192.168.20.70-79，网关 192.168.20.7 是交换机 VLAN20 的 IP 接口地址（C11，<<<PAGE 221>>>–<<<PAGE 224>>>）。

## B（边界与陷阱）
- 端口对某 VLAN 是 untagged 的只能有一个（即 default VLAN），其余必须 tagged，混用会导致 AP 拿错网段地址。
- 多词 VLAN 名必须加引号（P21，<<<PAGE 159>>>–<<<PAGE 160>>>）。
- 未 `write memory` 的 VLAN 修改重启即丢（CE04，<<<PAGE 133>>>）。
- OS2360（AOS 5.2）无法 onboard Cirrus，其 VLAN 只能手工 CLI 配置（CE16，<<<PAGE 337>>>）。

## 来源
- case·三 VLAN 规划与端口分配（<<<PAGE 173>>>–<<<PAGE 175>>>）
- case·WebView 建/删 VLAN（<<<PAGE 113>>>–<<<PAGE 114>>>）
- principle·默认 VLAN 与静态端口分配（<<<PAGE 159>>>–<<<PAGE 160>>>）
- principle·VLAN 间路由触发条件（<<<PAGE 162>>>）
- principle·802.1Q 标签结构（<<<PAGE 166>>>）
- principle·端口入组四途径（<<<PAGE 158>>>）
