---
name: GTTS 机制与配置（L2 GRE/Hairpin/交换机五步/AP 隧道面板）
description: 需要理解或配置 OmniAccess Stellar + OmniSwitch GTTS（访客流量隧道服务）时使用：L2 GRE/Hairpin 机制、One ARP 与 L3 hop 等架构前置、交换机侧五步 CLI 配置、AP 侧 Use Tunnel/Entropy 配置、服务部署（DHCP/Portal）约束与容量/MTU 规划。
source_book: Guest Traffic Tunnelling Services Application Note (23032701, April 2023)
---

## R（触发场景）
- 需要把无线流量（访客/安全 scrub/迁移）从 AP 隧道到中心 OmniSwitch 终结
- 配置隧道聚合交换机：l2profile/service/sap/Hairpin ACCESS 口
- AP 侧 SSID 勾 Use Tunnel、填 Tunnel ID 与 GRE Server IP、开 Entropy
- 隧道建不起来排障：VPN ID 不一致 / L3 hop / auto-discover / 版本不足
- 规划隧道数上限（按机型三档）与 MTU（+24 字节）

## I（核心理念）
数据路径统一模型（F3，<<<PAGE 4-5>>>）：AP 收流量 → 按 ARP 分类进 L2 GRE service profile → 加 GRE 头过隧道 → 聚合交换机解封装 → 经 Hairpin（SAP 口→自环线→ACCESS 口）落 VLAN 域出 Internet。双向对称。三前置纪律：One ARP（一个 ARP 同时只有一条活跃隧道，N 个隧道 SSID 需 N 台交换机，P8/X1，<<<PAGE 7>>>）；L3 hop（AP 管理 IP 与 GRE Server IP 不同子网，P9/X3，<<<PAGE 7>>>）；版本（AOS ≥8.4.1.R02 / AWOS ≥3.0.2.19，P14，<<<PAGE 6>>>）。两条容量红线：Hairpin 线速封顶 SSID 带宽（P10，<<<PAGE 8>>>）、单机隧道数按机型 1000/2000/6000 且 VC 不抬高（P13/X6，<<<PAGE 8>>>）。服务约束：DHCP 流量也在隧道内，DHCP/Portal/DNS/NTP 必须从聚合交换机可达，最佳是隧道 SSID 专属服务（P4/X10，<<<PAGE 4-5>>>）。

## A1（行动框架）
1. 需求定位：用例三选一——访客隔离/安全策略串行/迁移免扩 VLAN（F1，<<<PAGE 3>>>）
2. 前置核查：版本 → One ARP 交换机数量 → L3 hop → MTU+24B（跨运营商链路提前协商）→ auto-discover 开启
3. 交换机侧：五步配置（见 A2-C1）
4. AP 侧：SSID Use Tunnel 面板四要素 + Entropy 必开
5. 服务部署：聚合交换机同区配 DHCP/Portal/DNS/NTP（专属为佳）
6. 粒度细化（可选）：单 SSID 多 ARP——Filter-id/IoT Enforcement/设备专属 ARP，Expert 模式建 Tunnel Profile（P15，<<<PAGE 5>>><<<PAGE 11>>>）

## A2（操作步骤）
- **交换机五步**（C1，<<<PAGE 9>>>）：
  1. `service l2profile "name" stp drop gvrp drop mvrp drop`
  2. `service access port X/X/XX vlan-xlation enable l2profile "name"`
  3. `service "id" l2gre vpnid "vpn-id" stats enable vlan-xlation enable remove-ingress-tag enable`（vpnid 必须与 SSID 侧一致；service 编号本机自选）
  4. `service "id" sap port X/X/XX:"vpn-id"`
  5. `vlan "VLAN-ID" members port X/X/XX untagged`（Hairpin 另一侧 ACCESS 口）
  - 样例：SAP=1/1/49A、ACCESS=1/1/50、vpnid/VLAN=50（两 ID 一致仅为方便，不强制）
- **AP 面板**（C2，<<<PAGE 10-11>>>）：SSID 创建勾 Use Tunnel → Tunnel ID（=交换机 vpnid）→ GRE Tunnel Server IP → Backup GRE Tunnel Server IP（可选）→ Preemption+倒计时（可选）→ **Entropy 必须启用**
- **auto-discover 确认**（P12，<<<PAGE 8>>>）：`service l2gre auto-discover enable`（默认开）
- **单 SSID 多 ARP**（P15，<<<PAGE 11>>>）：OV2500 Expert 模式建多 ARP → 各配 Tunnel Profile → 不同设备分类进不同隧道终点

## E（实证案例）
- 交换机完整配置样例（guest-l2profile + service 100 + vlan 50，<<<PAGE 9>>>）
- 验证环境硬件清单：OS6900-V48C8/X48C6/T48C6/T24C2/X24C2 + AOS 8.7.98/8.9.78、AP1201/AP1331 + AWOS 4.0.5.2038、OV2500 4.7R1（<<<PAGE 7>>>）

## B（反例与坑）
- N 个不同 ARP 的隧道 SSID 只配 1 台交换机 → 其余隧道建不起来（X1，<<<PAGE 7>>>）
- 多 SSID 共用同一 ARP：技术上可行但零收益，配置全同（X2，<<<PAGE 7>>>）
- AP 管理 IP 与 GRE Server IP 同网段 → 违反 L3 hop 硬前置（X3，<<<PAGE 7>>>）
- 跨公司网络未协商 MTU：+24 字节开销静默丢大包（X4，<<<PAGE 8>>>）
- auto-discover 被关 → 逐台手工登记 AP MAC（X5，<<<PAGE 8>>>）
- Tunnel ID/VPN ID 主备交换机与 AP 三处不一致 → 隧道对不上（X11，<<<PAGE 9-10>>><<<PAGE 16>>>）
- Entropy 未启用 → GTTS 不工作（文档 Important 级强制，X9，<<<PAGE 10>>>）
- DHCP/Portal 留内网不复署 → 隧道内 DHCP 拿不到地址（X10，<<<PAGE 4-5>>>）

来源：Guest Traffic Tunnelling Services Application Note，Configuration 章（p4-11）
