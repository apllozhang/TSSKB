# DIGEST · GTTS（访客流量隧道服务）应用笔记精华——把无线流量从 AP 隧道到 OmniSwitch 终结的全套打法

> 教材：Guest Traffic Tunnelling Services Application Note（ALE，23032701，2023-04，19 页）
> 本文是"不读全文、只看精华"的交付工程师版速读。页码可直接对照原书（<<<PAGE N>>>）。

---

## 一、一页看懂这份应用笔记

它回答一个问题：**Stellar 本是无控制器分布式架构，怎样把部分无线流量隧道到中心 OmniSwitch 上集中终结、隔离与施策，并且不把这个中心做成单点。**

核心机制一句话：AP 上的流量按 ARP（访问角色档案）分类 → 加 L2 GRE 头（+24 字节）过隧道 → 隧道聚合交换机（通常在 DMZ）解封装 → 经 Hairpin（同机两口自环：SAP 口出隧道、ACCESS 口落 VLAN）进 VLAN 域出 Internet。DHCP、Portal、DNS、NTP 全部跟着流量走隧道，所以这些服务必须部署在聚合交换机可达的同区域。

三条硬前置（文档明示 mandatory）：One ARP（一个 ARP 同一时刻只有一条活跃隧道；N 个隧道 SSID 需 N 台交换机）、L3 hop（AP 管理 IP 与 GRE Server IP 不同子网）、版本（AOS ≥8.4.1.R02 / AWOS ≥3.0.2.19）。

## 二、技能地图（3 个 skill）

| Skill | 覆盖内容 | 对应原书 |
|---|---|---|
| `sol-gtts-architecture-config` | L2 GRE/Hairpin 机制、三前置、交换机五步 CLI、AP Use Tunnel 面板与 Entropy、服务部署/容量/MTU | Configuration 章 p4-11 |
| `sol-gtts-deployment-scenarios` | 三用例定位（访客/安全/迁移）、DMZ 三区基线、Campus AP Group 汇聚、单机多租户 | p3 + Scenarios 章 p11-13 |
| `sol-gtts-redundancy-designs` | R0-R4 五级冗余阶梯、R1/R3 完整 linkagg CLI、R2 Preemption、选型决策 | Redundancy 章 p14-19 |

依赖关系：先读 architecture-config 掌握机制与五步配置；scenarios 决定架构落点；redundancy 在任何生产部署上叠加。

## 三、配置主线速查（交换机五步 + AP 四要素）

**交换机（<<<PAGE 9>>>）**：
1. `service l2profile "name" stp drop gvrp drop mvrp drop`
2. `service access port X/X/XX vlan-xlation enable l2profile "name"`（SAP 口）
3. `service "id" l2gre vpnid "vpn-id" stats enable vlan-xlation enable remove-ingress-tag enable`
4. `service "id" sap port X/X/XX:"vpn-id"`
5. `vlan "VLAN-ID" members port X/X/XX untagged`（ACCESS 口）

**AP（<<<PAGE 10>>>）**：SSID 创建勾 Use Tunnel → Tunnel ID（=vpnid）→ GRE Tunnel Server IP → Backup IP（可选）→ Preemption（可选）→ **Entropy 必开**。
开局必查：`service l2gre auto-discover enable`（默认开，<<<PAGE 8>>>）。

## 四、部署场景速查表

| 场景 | 架构 | 关键动作 | 页码 |
|---|---|---|---|
| DMZ 访客隧道 | Corporate/DMZ/External 三区防火墙分隔 | Guest SSID 终点=DMZ 聚合交换机，DHCP 同区，只出 Internet | p11 |
| Campus 园区 | 多站点 + 1 数据中心 | 全站 AP 入同一 AP Group，套用 GTTS SSID，统一隧道到 DC | p12 |
| 单机多租户 | 运营商 SP + 多客户 | 每客户一 AP Group（可各有 OV2500），配 SP 交换机 IP，走 SD-WAN/SPB/MPLS | p13 |

用例三选一（p3）：访客隔离 / IPS 类安全串行 / 控制器迁移免扩边缘 VLAN。

## 五、冗余等级速查表（R0-R4）

| 等级 | 做法 | 保护范围 | 收敛 | 页码 |
|---|---|---|---|---|
| R0 | 单交换机+单 Hairpin | 无 | — | p14 |
| R1 | SAP/ACCESS 各建 linkagg（可与 R2-R4 叠加，Hairpin 不限 2 条） | 各 1 端口故障无感；带宽翻倍 | 无感 | p15-16 |
| R2 | 备机同配置（vpnid 一致）+ SSID 填 Backup GRE Server IP（可开 Preemption 回切） | 整机故障 | 秒级 | p16-17 |
| R3 | 两机组 Virtual-Chassis + 跨成员 linkagg | 整机+连接+Hairpin | 亚秒 | p17-18 |
| R4 | 每 SSID 一对交换机（建议异地），Primary-Backup 或 VC 实现 | 地理故障仅伤单 SSID | 同 R2/R3 | p18-19 |

## 六、交付陷阱 TOP8

1. **One ARB 换算错交换机数**：3 个不同 ARP 的隧道 SSID 必须配 3 台聚合交换机（p7）。
2. **L3 hop 违规**：AP 管理 IP 与 GRE Server IP 同子网，GTTS 不工作（p7）。
3. **Tunnel ID/VPN ID 三处不一致**（AP/主机/备机）：隧道建不起来的第一嫌疑（p9-10/p16）。
4. **Entropy 没开**：文档 Important 级强制（p10）。
5. **DHCP/Portal 不在隧道终点区**：连 DHCP 都在隧道里跑，服务不可达=用户上不了线（p4-5）。
6. **跨运营商链路 MTU**：+24B 封装开销，不提前协商就静默丢大包（p8）。
7. **把 R1 当整机冗余**：只保端口级，交换机与连接仍单点（p15）。
8. **容量两误区**：Hairpin 线速封顶 SSID 带宽（多 Hairpin 扩容）；VC 不抬高单机隧道数上限（1000/2000/6000 按机型，p8）。

---

> 本文由 cangjie-skill 流水线从 23032701 应用笔记蒸馏生成。
