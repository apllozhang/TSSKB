---
name: Stellar 桥接与 Mesh 用例与前提（室外桥接/室外多点/室内多点/家庭 mesh/支持 AP 清单/mesh 节点规则）
description: 需要核对 outdoor bridge、Multi-Point outdoor/indoor mesh、家庭 mesh 各用例的部署前提、mesh AP 数量与 SSID 上限、无漫游/尽力转发限制、各场景支持的 AP 型号清单时使用。
source_book: Network Solution Guide — OmniAccess Stellar Bridging/Multi-Point Meshing Guidelines (AWOS 4.0.4 / OV2500 Cirrus 4.6.2)
---

## R（何时使用）
- 确认某型号 Stellar AP 能否用于 bridge 或 indoor/outdoor mesh
- 核对 mesh 集群规模、每 AP SSID 数、漫游能力、VoIP 承载等硬性限制
- 规划室内工业场景（厂房/仓库）或家庭 mesh 的 RF 指标与天线选型
- 用 Access Role Profile（ARP）规划 bridge 远端端口的 VLAN 角色

## I（核心理念）
**用例三分法**：室外 Bridge（两站点 LAN 延伸）、Multi-Point mesh（室外难布线区域 + 室内工业/家庭覆盖）是三大落地形态（P8/P10/P15，<<<PAGE 8>>>）。

**mesh 节点六条规则是硬约束**，室内室外通用：16 AP 上限、5 SSID 上限、吞吐 ÷2、无漫游、VoIP 尽力转发（P11/P17，<<<PAGE 11>>>）。

家庭场景是 mesh 的轻量入口：Express 模式 + 入门 AP1301 即可企业级组网，体现 Stellar"从家庭到企业同一套 mesh 架构"的定位（P16，<<<PAGE 16>>>）。

## A1（决策要点）
1. **室外 Bridge 前提**（P9，<<<PAGE 9>>>）：仅用于连接两个可管理远端站点、仅限室外；root 可双；不建议同一 bridge 配多个 Bridge AP（若配，下联选 RSSI 最好的）；必须用定向或高定向天线
2. **室外 mesh 前提**（P11，<<<PAGE 11>>>）：最多 16 个 mesh AP；root 可双；root 用全向/半定向 MIMO 天线；nLoS 可行但半定向天线波束边缘至少损耗 3dB
3. **天线一致性**（P9/P11，<<<PAGE 9>>>）：链路两端天线型号与极化必须一致；MU-MIMO 天线（±45° 双斜极化）推荐；同一 mesh 用同系列 AP（Wi-Fi 6 才能享受 802.11ax）
4. **频宽建议**（P9/P11，<<<PAGE 9>>>）：数据走 5GHz，40MHz 及以上信道宽度（802.11ac/ax）；VLAN 0-4095 全部可透传
5. **室内 RF 指标**（P16，<<<PAGE 16>>>）：SNR ≥20dB（语音更好）、RSSI ≥-67dBm；用全向外置高增益天线（如 AP1322 直挂 ANT-O-6）；patch 天线不推荐用于室内 mesh
6. **家庭 mesh 要点**（P16-17，<<<PAGE 16>>>）：root 接路由器旁、用路由器 DHCP、mesh 距离不超过 2 个房间（约 5 米）、Express 模式逐 AP 管理、按 SSID 配 QoS

## A2（细节速查表）
| 项目 | 内容 | 页码 |
|---|---|---|
| mesh AP 数量上限 | 16 个 mesh AP / mesh 配置（室内外相同） | <<<PAGE 11>>> / <<<PAGE 17>>> |
| 每 mesh AP SSID 上限 | 5 个客户端 WLAN 服务 | <<<PAGE 11>>> / <<<PAGE 17>>> |
| root 容量共享 | root 总吞吐被所有 mesh AP 与客户端共享；每 mesh AP 每 SSID 吞吐 ÷2 | <<<PAGE 11>>> |
| 漫游 | mesh AP 之间无漫游，无 PMK/OKC/密钥交换处理 | <<<PAGE 11>>> |
| VoIP/实时业务 | 仅尽力转发（best effort） | <<<PAGE 11>>> |
| 自动入网 | root 旁出厂配置且未接 LAN 的 AP 会自动以 mesh AP 接入并继承 root 的客户端 SSID | <<<PAGE 11>>> |
| Bridge VLAN 透传 | 0-4095 tagged VLAN | <<<PAGE 9>>> |
| Bridge AP 支持 | 室外 IP67：AP1361/1362/1361D（Wi-Fi 6）、AP1251（Wi-Fi 5）；室内 AP1322（Wi-Fi 6，外置 patch 天线）、AP1222（Wi-Fi 5） | <<<PAGE 10>>> |
| 室外 mesh AP 支持 | AP1361/1362/1361D、AP1251；AP1361/AP1251 可抱杆安装，root 可 nLoS | <<<PAGE 11>>> |
| 室内 mesh AP 支持（Wi-Fi 6） | AP1301/1311/1321/1322/1331/1351/1361 | <<<PAGE 17>>> |
| 室内 mesh AP 支持（Wi-Fi 5） | AP1201/1221/1222/1231/1232/1251 | <<<PAGE 17>>> |
| Bridge 端口角色 | Enterprise 模式用 Access Role Profile（ARP）按 VLAN/端口定义 ACL 与 QoS | <<<PAGE 8>>> |
| 家庭 mesh 设备 | AP1301（入门 Wi-Fi 6），OAW-AP-MNT-W 壁挂套件 + 48V 电源块 | <<<PAGE 16-17>>> |
| 家庭连接形态 | 单 SSID + 密码，双频；2.4GHz 笔记本、5GHz 手机/Chromecast/电视/主机 | <<<PAGE 16>>> |

## E（场景案例）
- 隔街两栋楼：AP1361D 定向天线 Bridge，ENET0 分发企业 VLAN，ENET1 给 IP 摄像头 PoE 供电（P8，<<<PAGE 8>>>）
- 工业园区难布线区域：root 双冗余 + 多个 AP1361 抱杆 mesh 节点，每节点带 Wi-Fi 覆盖与下联口（P10-11，<<<PAGE 10>>>）
- 工厂车间室内覆盖延伸：AP1322 + ANT-O-6 全向外置天线，SNR 20dB / RSSI -67dBm 达标（P15-16，<<<PAGE 15>>>）
- 家庭办公：路由器旁放 root AP1301，各房间 mesh AP1301，3-5 米距离高吞吐，5GHz 80MHz 给双频 Wi-Fi 6 设备（P16-17，<<<PAGE 16>>>）

## B（限制与坑）
- **同一 bridge 不建议配多个 Bridge AP**，下联会连到 RSSI 最好的那个，行为不易控（P9，<<<PAGE 9>>>）
- **mesh AP 间无漫游**——手机在 mesh 节点间移动会断连重连，不能按传统 WLAN 漫游承诺（P11，<<<PAGE 11>>>）
- **VoIP 与实时应用只有尽力转发**，不要给客户承诺语音质量（P11，<<<PAGE 11>>>）
- 5 SSID、16 AP 上限是硬顶，超了要拆集群（P11/P17，<<<PAGE 11>>>）
- 混用 Wi-Fi 5 与 Wi-Fi 6 AP 会拉低整链路到低代际速率，保持同系列（P9/P11，<<<PAGE 9>>>）
- 室内 mesh 用 patch 天线是反模式，patch 只适合特定覆盖（P16，<<<PAGE 16>>>）
- 家庭 mesh 链路距离超过 2 个房间（5 米）性能不保（P16，<<<PAGE 16>>>）

来源：OmniAccess Stellar Bridging/Multi-Point Meshing Guidelines，p8-11、p15-17（Use cases + 前提 + 支持型号 + mesh 规则）
