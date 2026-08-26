---
name: Stellar Mesh 配置流程（OV2500 Enterprise：AP Group/RF Profile/SSID/Mesh 角色/下联口 uNP + APUI 配置）
description: 需要在 OmniVista 2500 Enterprise 模式下创建 mesh/bridge AP 组、专用 RF Profile、下发 SSID、设置 AP 的 root/mesh 角色、配置 bridge 下联口 uNP 认证配置，或用 APUI 逐台配置 mesh 角色与端口 VLAN 时使用。
source_book: Network Solution Guide — OmniAccess Stellar Bridging/Multi-Point Meshing Guidelines (AWOS 4.0.4 / OV2500 Cirrus 4.6.2)
---

## R（何时使用）
- Enterprise 模式（OV2500）下从零配置一个 mesh/bridge 集群
- 规划 mesh 专用 AP Group、RF Profile（国家/信道/频宽/功率/MU-MIMO）与 SSID 参数
- 给指定 AP 设置 Mesh Enable / Is Root / mesh SSID / 频段
- Bridge 场景管理 ENET0/1 下联口：uNP 认证配置、trust tag、bypass VLAN
- Express 模式下用 APUI 直接改 mesh 角色与端口 VLAN

## I（核心理念）
**配置主线：把普通 AP group 管理中的部分 AP"特化"为 root 或 mesh 角色**（P20，<<<PAGE 20>>>）。OV2500 原有 AP group / RF profile / access profile 管理框架不变，mesh group 是在此之上做角色专化。

**四个关键动作**：专用 AP Group → 专用 RF Profile → SSID/ARP 下发 → 逐 AP 设 mesh 角色（P20-23，<<<PAGE 20>>>）。

**mesh 全员 RF 一致**：工作频率、法规、信道、发射功率（含 802.11ax 激活与长 GI）必须对 mesh/bridge 组内所有 AP 相同——所以强烈建议专用 RF Profile（P21，<<<PAGE 21>>>）。

IP 地址建议静态或 DHCP 保留，bridge 场景理想情况下全静态（P21，<<<PAGE 21>>>）。

## A1（决策要点）
1. **前置准备**（P21，<<<PAGE 21>>>）：AP REGISTRATION 里识别入组 AP；DHCP 场景为全部未来 mesh AP 做 IP 保留，bridge 建议直接静态 IP
2. **专用 AP Group**（P21，<<<PAGE 21>>>）：路径 `OV2500 -> NETWORK -> AP REGISTRATION -> AP Group -> +`；组内配置：本地时间 + UTC 时区、Support/root 账户启用 SSH、Administrator 账户启用 AP WEB（后面 APUI 要用）
3. **专用 RF Profile**（P21-22，<<<PAGE 21>>>）：路径 `OV2500 -> WLAN -> RF Management -> RF Profile -> +`；示例参数：Country FR-France、Band steering Force 5GHz、Load balance 启用、Airtime Fairness 双频启用、Background Scanning 关闭（选 Wi-Fi 6 非工作信道）、5G 信道列表 [100,104,108,112]、5G 频宽 80MHz、DFS/TPC 15dBm（室内）、MU-MIMO 与 High Efficiency（Wi-Fi 6）启用；Profile 应用到 Mesh AP Group
4. **SSID 下发**（P22，<<<PAGE 22>>>）：路径 `OV2500 -> WLAN -> SSIDs -> +`；示例：Personal 安全级别、Allowed Band All、WPA3 SAE AES、Untagged VLAN（示例 94）；Advanced 里 HT Control 保持 A-MSDU/A-MPDU；保存并应用到 mesh AP Group
5. **多 VLAN 场景**（P22，<<<PAGE 22>>>）：用 ARP（Access Role Profile）处理要经 mesh 链路分发的 VLAN；mesh AP 上管理 VLAN 分配（802.1x 客户端认证场景）
6. **设 mesh 角色**（P23，<<<PAGE 23>>>）：路径 `OV2500 -> NETWORK -> AP REGISTRATION -> Access Points -> 选 AP -> Edit Mesh Configuration`；root AP：MESH Enable=Yes、Is Root=Yes、SSID=Stellar-MESH、Band=5GHz；mesh AP：Is Root=No，其余同
7. **上线**（P23，<<<PAGE 23>>>）：配置完成后 mesh AP 可脱离原 LAN 搬到最终位置（室内吸顶/bridge 屋顶），上电后 mesh 初始化需数分钟；OV2500 拓扑上 mesh 图标高亮即确认在跑
8. **下联口管理**（P24，<<<PAGE 24>>>）：bridge 场景用 uNP 认证配置管理 ENET0/1 下联口——路径 `OV2500 -> UNIFIED ACCESS -> UNIFIED PROFILE -> Template -> Access Auth Profile -> +`；Default Settings：AP Mode=Disabled；No Auth/Failure/Alternate：Trust tag=Enabled、Bypass VLAN=待旁路 VLAN 列表；Profile 应用到 Mesh AP Group（Apply to Devices），再选具体端口应用
9. **APUI 管理**（P25-26，<<<PAGE 25>>>）：Express 模式经各 AP 的 @IP 进 APUI；Enterprise 模式从 AP 列表 Action -> AP web 进（登录用 group 的 administrator 账户）；mesh 角色在 `APUI -> NETWORK -> AP INTERFACE -> Backhaul0 -> Edit Interface`（Mesh/Bridge/Is Root + SSID 频段/密码）；端口 VLAN 在 `APUI -> NETWORK -> AP INTERFACE -> Enet0/1/2/3 -> Edit Interface`（enable + trust/bypass VLAN）

## A2（细节速查表）
| 步骤 | 路径/参数 | 页码 |
|---|---|---|
| 识别 AP | OV2500 -> NETWORK -> AP REGISTRATION -> Access Points | <<<PAGE 20>>> |
| 建 AP Group | NETWORK -> AP REGISTRATION -> AP Group -> +；UTC 时区 / SSH（Support+root）/ AP WEB（Admin） | <<<PAGE 21>>> |
| 建 RF Profile | WLAN -> RF Management -> RF Profile -> +（示例 FR-France） | <<<PAGE 21>>> |
| RF Profile RF 项 | Band steering Force 5G、Load balance、Airtime Fairness 2.4/5G | <<<PAGE 21>>> |
| RF Profile 信道项 | Background Scanning 关闭（选 Wi-Fi 6 非工作信道）、Channel DRM 5G 启用、5G 信道 [100,104,108,112]、频宽 80MHz、DFS/TPC 15dBm | <<<PAGE 22>>> |
| RF Profile Wi-Fi 6 项 | MU-MIMO 启用、High Efficiency 启用 | <<<PAGE 22>>> |
| 建 SSID | WLAN -> SSIDs -> +；Personal / All band / WPA3 SAE AES / Untagged VLAN 94 | <<<PAGE 22>>> |
| SSID 高级项 | HT Control：A-MSDU/A-MPDU（默认启用） | <<<PAGE 22>>> |
| 设 mesh 角色 | Access Points -> 选 AP -> Edit Mesh Configuration：MESH Enable=Yes、Is Root=Yes/No、SSID=Stellar-MESH、Band=5GHz | <<<PAGE 23>>> |
| 上线确认 | 搬迁上电，初始化数分钟；Stellar 拓扑 mesh 图标高亮 | <<<PAGE 23-24>>> |
| uNP 下联口 | UNIFIED ACCESS -> UNIFIED PROFILE -> Template -> Access Auth Profile -> +；AP Mode=Disabled、Trust tag=Enabled、Bypass VLAN 列表；Apply to Devices 后选端口 | <<<PAGE 24>>> |
| APUI 入口 | Express：集群列表点 @IP；Enterprise：AP 列表 Action -> AP web，Admin 登录 | <<<PAGE 25>>> |
| APUI mesh 角色 | NETWORK -> AP INTERFACE -> Backhaul0 -> Edit Interface（角色 + SSID 频段/密码） | <<<PAGE 26>>> |
| APUI 端口 | NETWORK -> AP INTERFACE -> Enet0/1/2/3 -> Edit Interface（enable + trust/bypass VLAN） | <<<PAGE 26>>> |

## E（场景案例）
- 书中实操：2 台室内 Stellar AP 组 mesh——Storage1 设 root、Storage2 设 mesh，mesh SSID Stellar-MESH 走 5GHz，配置后拆除 Storage2 的有线搬到目标位置吸顶安装（P20-24，<<<PAGE 20>>>）
- bridge 下联口：bridge AP 的 ENET0/1 通过 uNP 认证配置做远端有线流量下联，trust tag 透传企业 VLAN（P24，<<<PAGE 24>>>）
- Express 模式家庭 mesh：逐台 AP 进 APUI 的 Backhaul0 设 root/mesh 角色与 SSID，Enet 口设 trust/bypass VLAN（P25-26，<<<PAGE 25>>>）

## B（限制与坑）
- **组内 AP 的 RF 参数（频率/法规/信道/功率/802.11ax/长 GI）必须完全一致**，漏一台不一致链路就出问题——务必用专用 RF Profile 统一推送（P21，<<<PAGE 21>>>）
- AP WEB（APUI）入口要在 AP Group 里预先给 Administrator 账户启用，否则后面临场没法用 APUI 救急（P21/P25，<<<PAGE 25>>>）
- SSH 监控也要提前在 AP Group 启用 root 账户（P21/P27，<<<PAGE 27>>>）
- mesh 上电初始化要几分钟，别当成故障反复重启（P23，<<<PAGE 23>>>）
- 配 mesh 角色前 AP 还在原 LAN 上由 OV2500 管；角色设完再搬走，顺序不能反（P23，<<<PAGE 23>>>）
- uNP 认证配置 Profile 建好后还要两步：Apply to Devices 到 Mesh AP Group，再逐端口应用——漏第二步端口不生效（P25，<<<PAGE 25>>>）

来源：OmniAccess Stellar Bridging/Multi-Point Meshing Guidelines，p20-27（Enterprise 配置 + 下联口 + APUI）
