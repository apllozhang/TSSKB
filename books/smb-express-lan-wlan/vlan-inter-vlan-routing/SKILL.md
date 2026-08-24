---
name: VLAN 与 VLAN 间路由
description: 当需要规划 VLAN 划分、配置 802.1Q tag/untagged 端口、跨交换机打 trunk、或通过 IP interface 实现 VLAN 间路由时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 要给员工/访客/AP 管理划分不同 VLAN 并配置端口成员
- 两台交换机互联需要多 VLAN 打 tag（trunk）
- 需要 VLAN 之间互相路由（单臂网关式）

## I（核心理念）
在 AOS 上，VLAN 是二层数据结构，IP interface 绑定 VLAN 后三层路由即刻激活——"网关即虚拟路由器端口"。物理端口恒有一个默认（untagged）VLAN 桥接二层流量，802.1Q tag 则承载 4096 个 VID 与 3bit 优先级。

## A1（行动框架）
1. **建 VLAN 并命名**：`vlan 10 name Management-AP` / `vlan 20 name Employees` / `vlan 30 name Guests`（<<<PAGE 177>>>-<<<PAGE 183>>>）。
2. **端口成员**：上行口 `vlan 10 members port 1/1/3 tagged`；AP 口 `vlan 10 members port 1/1/6 untagged` + `vlan 20/30 members port 1/1/6 tagged`（AP 口同时承载管理+业务 VLAN）。
3. **验证**：`show vlan members port 1/1/6`；`show mac-learning` 验证 MAC 学习（<<<PAGE 184>>>）。
4. **VLAN 间路由**：`ip interface int_1 address 192.168.1.2/24 vlan 1` → `show ip interface` 验证（<<<PAGE 114>>>）。
5. **跨交换机 trunk**：互联链路两侧打 tag，如 `vlan 20 members linkagg 7 tagged` / `vlan 20 members port 2/1/3 tagged`，`show vlan members port 2/1/3` 应见 20/30 tagged + 默认 VLAN untagged，客户端互 ping 验证 L2/L3 路径（<<<PAGE 596>>>-<<<PAGE 601>>>）。

## A2（进阶应用）
- **VLAN 状态机制**：VLAN 无活动成员端口时 IP 接口 operational inactive，不参与路由（<<<PAGE 512>>>）——排障时先查成员再查路由。
- **Mobile Tag vs 静态 Tag**：Mobile Tag 允许移动口（话机口）接收 802.1Q tag 并动态加入 VLAN；静态 802.1Q Tag 在 mobile 口不支持（<<<PAGE 173>>>、<<<PAGE 793>>>），话机场景配合 LLDP-MED/UNP 使用。
- **AP 管理口规则**：AP 管理 VLAN 必须 untagged（上云排障经验，<<<PAGE 377>>>）。
- **UNP 动态 VLAN 分类优先级**：Port/Linkagg > Domain > MAC > MAC-OUI > MAC range > LLDP > Auth-type > IP > VLAN tag（<<<PAGE 506>>>），做动态分 VLAN 时按此顺序排错。

## E（实证案例）
- PoE/VLAN/DHCP 联调：三个 VLAN 划分、AP 口 tagged+untagged 组合、AP 改 DHCP 模式后用 `mywifi.al-enterprise.com:8080` 域名重连（<<<PAGE 177>>>-<<<PAGE 183>>>）。
- 802.1Q 跨三台交换机多 VLAN 打 tag，show 验证 20/30 tagged + 58 untagged 后客户端互 ping（<<<PAGE 596>>>-<<<PAGE 601>>>）。

## B（边界与陷阱）
- 每个物理端口恒有且仅有一个默认（untagged）VLAN 做二层桥接，配 tag 前先想清默认 VLAN 是谁（<<<PAGE 599>>>）。
- VLAN 无活动端口时 IP interface 直接 DOWN（<<<PAGE 512>>>），ping 不通未必是路由问题。
- AP 管理 VLAN 必须落在 untagged 上（<<<PAGE 377>>>）。

## 来源
- principles·P12 VLAN 间路由原理（<<<PAGE 165>>>、<<<PAGE 512>>>）
- principles·P13 802.1Q Tag 帧结构（<<<PAGE 169>>>、<<<PAGE 516>>>）
- principles·P14 物理端口默认 VLAN（<<<PAGE 599>>>）
- principles·P15 Mobile Tag 区别（<<<PAGE 173>>>、<<<PAGE 793>>>）
- principles·P16 UNP 动态 VLAN 分类优先级（<<<PAGE 506>>>）
- cases·C10 PoE/VLAN/DHCP 联调（<<<PAGE 177>>>-<<<PAGE 184>>>）
- cases·C26 802.1Q 跨交换机多 VLAN（<<<PAGE 596>>>-<<<PAGE 601>>>）
- cases·C3 首次登录 ip interface 配置（<<<PAGE 113>>>-<<<PAGE 114>>>）
