# BOOK_OVERVIEW · Guest Traffic Tunnelling Services Application Note（23032701, April 2023）

> 出版物: ALE Application Note · 19 页 · 23032701（2023-04）
> 定位: OmniAccess Stellar + OmniSwitch **GTTS（访客流量隧道服务）** 的官方应用笔记——机制、配置、三大部署场景、五种冗余设计（R0-R4），全篇带 CLI 配置样例

## 一、结构（书的骨架）

- **OmniAccess Stellar Traffic Tunnelling** (p3)：无控制器架构下的三类隧道用例（访客隔离/安全策略旁挂/控制器迁移）
- **Configuration** (p4-11)：
  - Global knowledge (p4-5)：L2 GRE 机制、Hairpin（SAP 口+ACCESS 口）、服务部署约束（DHCP/Portal）
  - Prerequisites (p6-8)：软硬件版本（AOS ≥8.4.1.R02 / AWOS ≥3.0.2.19）、One ARP 规则、Layer 3 hop、Hairpin 线速、MTU +24B、auto-discover、按机型隧道数上限（1000/2000/6000）
  - Switch configuration (p9)：l2profile → service access port → service l2gre vpnid → sap → vlan members 五步
  - AP configuration (p10-11)：Use Tunnel / Tunnel ID / GRE Server IP / Backup IP / Preemption / Entropy 必开
- **Scenarios** (p11-13)：DMZ 访客隧道 → Campus 园区多站聚合 → 单交换机多租户
- **GTTS redundancy designs** (p14-19)：R0 无冗余 → R1 Hairpin 冗余 → R2 Primary & Secondary → R3 Virtual-Chassis → R4 每 SSID 一对交换机

## 二、解释（核心论点）

- Stellar 本是分布式无控制器架构，GTTS 用 L2 GRE 把无线流量从 AP 灵活隧道到一台或多台 OmniSwitch 隧道聚合交换机，粒度可到 ARP（Access Role Profile）级；
- 交换机侧靠 Hairpin（同一台交换机两口互联：SAP 口出隧道、ACCESS 口落 VLAN）落地，因此 SSID 带宽被 Hairpin 线速封顶，所有用户服务（DHCP/Portal/DNS/NTP）必须部署在聚合交换机可达处；
- 冗余是递进体系：R1 修端口、R2 修整机（Backup GRE 隧道，秒级收敛）、R3 修整机+链路（Virtual-Chassis，亚秒收敛）、R4 按SSID 分散地理风险。

## 三、批判（局限）

- 19 页应用笔记，只覆盖 GTTS 单特性；SSID 创建全过程、OV2500 操作细节均明确"不在此详述"；
- 配置样例基于 OV2500 4.7R1 + AWOS 4.0（p7 的软硬件清单），新版本 GUI 字段可能有差异；
- 未给性能/吞吐实测数据，Hairpin 线速只有定性描述。

## 四、应用（对售后/交付的价值）

- 交付 SOP 素材：交换机五步配置、AP 隧道面板字段、R1/R3 的 linkagg+service 完整 CLI 可直接照抄改端口；
- 选型速查：隧道数上限按机型三档（1000/2000/6000）；冗余等级 R0-R4 选型对照；
- 避坑清单：One ARP 规则、L3 hop、MTU+24B、Entropy 必开、auto-discover。

## 五、术语速览

GTTS、L2 GRE、tunnel aggregation switch、Hairpin、SAP port、ACCESS port、ARP（Access Role Profile）、Tunnel Profile、VPN ID、auto-discover、Entropy、Preemption、Virtual-Chassis、DMZ、multi-tenancy
