---
name: express-cluster-onboarding
description: 何时用：Stellar AP 开箱上线、建 Express 集群、规划分域扩容与远程运维时。
source_book: DT00XTE455EN Stellar WLAN Express
---

# Stellar Express 开箱与集群上线

## R · 原文引用

> "In an AP group, one AP supports the role of centralized management. It is called PVM. (Primary Virtual Manager). All other APs are under management of the PVM of the group. They are called Members. Another AP is responsible for rescuing the centralized management role. It is called Secondary Virtual Manager (SVM)... an election process is perform to select the PVM. Highest Model Type, Highest MAC address. AP with the second highest MAC is designated as the SVM." (p79-80)

> "A Group can not contain more than 255 APs. The 256th AP is not taken into account and will stay in 'joining' mode. To have more than 255 APs on a network it is necessary to configure several Group-ids or to configure two separate VLANs. VLAN X > GROUP ID X, VLAN Y > GROUP ID Y. Limitations: No Layer 3 Roaming. No Layer 2 Roaming between clusters." (p81)

> "Via a single IP interface (Group Mgt IP): Configuration synchronization, Group Management Interface, Notifications." (p84)

> "AP Group can be managed remotely (opening the Firewall settings for AP Group Management IP). All operations supported (except AP Group image upgrade)." (p86)

## I · 方法论骨架

Express 模式 = 无控制器、无云管的"AP 自组织集群"。上线主线是四层递进：

1. **单台上线（六步）**：前置条件确认 → 上电（PoE/DC）→ IP 获取（DHCP，失败兜底 192.168.1.254）→ 连出厂 SSID mywifi → 访问 Web 界面 → 向导式初始配置。
2. **集群成形（三角色 + 选举）**：同 VLAN 多台 AP 同时启动触发选举，判据为先比型号等级（Highest Model Type）、再比 MAC（最高者任 PVM，MAC 第二高任 SVM），PVM 产生后广播组配置 SSID（如 mywifi-0102），其余 AP 以 Member 加入。
3. **分域设计（超 255 台）**：口诀"一 VLAN 一 Group ID，一集群一 PVM"。集群间无 L2/L3 漫游，边界要放在低移动区域。
4. **运维收敛（单 IP + 远程）**：管理面收敛到 Group Mgt IP（配置同步/组管理界面/通知）；远程管理需防火墙放行该 IP，唯一例外是 AP Group 镜像升级必须本地执行。

选型背景：Express 上限 255 台（混合型号集群）；超此规模迁 Enterprise（OV2500）或 Cloud（Cirrus），两者均 4000 台、功能基本等同，差别只在本地/云端。

## A1 · 书中案例

- 选举演示：同一 VLAN 内 AP 同时上电，最高型号/最高 MAC 者自动成为 PVM 并广播 mywifi-0102 型组配置 SSID，其余 AP 加入为 Member（p79-80）。
- 第 256 台静默失效：某网络 AP 数超过 255 后，新增 AP 无报错地永远停在 joining 状态，现场极易误判为网络/配置问题（p81）。
- 远程运维规划：某项目把全网固件升级排成纯远程批次，卡在 AP Group image upgrade 这一步——其余操作都可远程，唯升级必须到场（p86）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：新购 Stellar AP 首次上线、规划集群分域、扩容撞 255 上限、需要远程运维方案、售前被问"无网管能管到什么规模"。
- 区分：AP 已上线但**入不了集群/拿不到 IP/不上电**的故障处置，用 `ap-side-troubleshooting`；SSID/Portal/认证等业务配置用 `ssid-portal-auth`；回程组网用 `bridge-mesh-deployment`；覆盖与信号质量用 `rf-survey-tuning`。本 skill 管"从零到可管"与"规模/域的规划"，不管故障与业务配置。

## E · 可执行步骤

单台上线：
1. 核对供电与线缆，上电（PoE 802.3af/at 或 48V DC，双源时 DC 优先）。
2. 终端连出厂 SSID **mywifi**；DHCP 失败时 PC 配同网段直连默认 IP **192.168.1.254** 进 Web。
3. Web 向导完成初始配置（IP 模式确认设为 DHCP）。

集群建立与确认：
4. 所有 AP 放入同一 VLAN、同一 Group ID，上电后等待选举完成。
5. 排障/巡检第一步：确认谁是 PVM/SVM（判据：先型号后 MAC），日常配置与集群动作一律面向 PVM 执行。
6. 记录并使用 **Group Mgt IP** 作为整组唯一管理入口。

分域扩容（>255 台）：
7. 按"VLAN X → Group ID X"映射拆多集群；每集群独立 PVM 与射频域。
8. 移动连续区域（仓储搬运、移动查房）划入同一集群——集群间不漫游。
9. 入组排障时核对当前型号组合允许的上限（32/64/255 三档，混入低端型号会拉低整组）。

远程运维：
10. 防火墙为 Group Mgt IP 放行（集群端口：32767 承载 PVM 报文、32768 承载 AP→PVM 报文，须放行）。
11. 固件/镜像升级排入现场批次，其余操作远程执行（get/set 模式）。

## B · 边界与陷阱

- **255 是硬上限且静默失效**：第 256 台不停 joining、不被纳管、无任何报错。看到 joining 卡死先数集群规模，再查 Group ID 与子网。
- **集群实际上限随型号组合变化**（32/64/255），排障时勿默认 255。
- **跨集群无 L2/L3 漫游**：终端跨集群必掉线重连，多集群设计的移动预期必须写清。
- **远程管理做不了 AP Group 镜像升级**——升级计划别排成纯远程。
- 引用校注：p82 型号清单原文为 "1350"，按谱系应为 AP1351，引用时保留校注。
- Express 能力不残缺（802.1X/WPA3/WIPS/DFS/TPC/内置 DHCP-DNS-NAT/Mesh/证书/GuestOperator 受限角色/ZTP），售前答疑可对照 p41 清单；UPAM 等网管级能力仅在 Enterprise/Cloud 模式。

---
来源条目: f01, f02, f03, f06, f10, p01, p02, p03, p04, p05, p06, p11, p14, p15, p16, p26, ce01, ce02, ce08, g01-g09, g24, g25, g33, g36
