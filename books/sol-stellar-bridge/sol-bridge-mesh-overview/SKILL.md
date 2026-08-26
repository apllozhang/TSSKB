---
name: Stellar 桥接与 Multi-Meshing 总览（bridge vs mesh 选型/root-mesh 角色/WDS/Auto-Mesh/带宽减半）
description: 需要判断远端站点该用 Point-to-Point bridge 还是 Multi-Point mesh、理解 root/mesh 角色与冗余 root、WDS 4 地址帧转发、Auto-Mesh 免配置上线、mesh 链路带宽共享机制时使用。
source_book: Network Solution Guide — OmniAccess Stellar Bridging/Multi-Point Meshing Guidelines (AWOS 4.0.4 / OV2500 Cirrus 4.6.2)
---

## R（何时使用）
- 远端建筑/园区无法布线，要在 bridge（纯 LAN 延伸）与 mesh（多节点 + WLAN 覆盖）之间做选型
- 设计 mesh 集群拓扑：root 网关位置、是否双 root 冗余
- 需要向客户解释 mesh 吞吐为什么每跳减半、backhaul 与客户端业务如何共享带宽
- 评估 Auto-Mesh 快速开局、WDS 透明桥接对 VLAN 传输的支持

## I（核心理念）
Stellar mesh 是"无线 AP 组成的路由器集群"，所有流量经 root 角色的 AP 网关进出有线 LAN（P5-6，<<<PAGE 5>>>）。

**Bridge 与 mesh 是两种互斥的配置形态，不能组合**（P11，<<<PAGE 11>>>）：
- **Bridge**：单链路 Point-to-Point，只延伸企业 LAN，不广播 SSID，企业内最常用（P6，<<<PAGE 6>>>）
- **Multi-Point mesh**：面向无法布线区域的多节点覆盖，root 和每个 mesh AP 都可广播 WLAN 服务（P6/P10，<<<PAGE 10>>>）

**带宽是核心约束**：mesh 链路带宽由 backhaul 与无线客户端共享；Multi-Point 模式下每个 mesh 节点同频同射频收发，需回传的数据吞吐逐跳除以 2（P7，<<<PAGE 7>>>）。

WDS 模式用 4 地址帧实现 AP 间透明以太桥接，统一广播域、可承载多个企业 VLAN（P7，<<<PAGE 7>>>）。

## A1（决策要点）
1. **形态选型**（P6，<<<PAGE 6>>>）：只延长 LAN 到一个远端站点 → Bridge；多节点区域需要 Wi-Fi 覆盖 + 有线下联 → Multi-Point mesh
2. **角色规划**（P5-6，<<<PAGE 5>>>）：root 角色 = LAN 网关（接有线），mesh 角色 = 无线节点；数据流量全部经 root 转发
3. **root 冗余**（P6，<<<PAGE 6>>>）：同一 AP group 可配两个 root，mesh AP 自动选 RSSI 最好的 root 连接——bridge 与 mesh 的 root 都支持双 root
4. **频段规划**（P7，<<<PAGE 7>>>）：双频/三频 Wi-Fi 6 AP 上 backhaul 可配在 5GHz 或 2.4GHz，5GHz 首选；WLAN 服务可在双频同时下发
5. **开局方式**（P7，<<<PAGE 7>>>）：Auto-Mesh——root 连 LAN 激活后，邻居空配置 AP 自动用默认 mesh 链路接入，无需预配置
6. **管理面**（P5，<<<PAGE 5>>>）：mesh 集群既可 Enterprise 模式（OmniVista 2500/Cirrus）统一管理 AP group、RF、VLAN、SSID、QoS、远端端口，也可 Express 模式（家庭场景）

## A2（细节速查表）
| 项目 | 内容 | 页码 |
|---|---|---|
| 集群本质 | AP 组成无布线路由器集群，mesh 基础设施固定，逐 AP 按定义转发 | <<<PAGE 5>>> |
| 两种角色 | mesh 角色（集群节点）/ root 角色（LAN 网关），每 AP 一个角色 | <<<PAGE 5>>> |
| 流量模型 | 所有数据流量从/到 root 网关转发；双 root 时按最佳 RSSI 选路 | <<<PAGE 6>>> |
| Bridge 配置 | 单 mesh 链路 + 单 mesh AP 接远端站点；无 SSID 广播；整个企业 LAN 桥接到远端 | <<<PAGE 6>>> |
| Multi-Point 场景 | 室外工业/活动场地/园区，室内工厂/仓库/存储，家庭 | <<<PAGE 6>>> |
| 带宽共享 | backhaul 与客户端共享链路带宽；Multi-Point 每节点吞吐 ÷2 | <<<PAGE 7>>> |
| 距离权衡 | AP 间距对链路性能影响大，距离 vs 性能始终是折中（室外影响最大） | <<<PAGE 7>>> |
| Auto-Mesh | root 连 LAN 激活即可，周边空配置 AP 自动以 mesh AP 接入 | <<<PAGE 7>>> |
| WDS | 4 地址帧透明以太桥接、统一广播域、承载多企业 VLAN；Bridge/Multi-Point 均支持 | <<<PAGE 7>>> |
| 远端下联口 | mesh AP 以太口可透传 tagged/untagged VLAN 做下联；AP1361/1362/1361D 有额外千兆口 | <<<PAGE 8>>> |
| PoE 输出 | AP1361/1362/1361D 的 ENET1 口支持 802.3af/at PSE 输出给远端设备（如 IP 摄像头） | <<<PAGE 8>>> |

## E（场景案例）
- 两栋楼隔街相望、无法跨公共道路布线：Bridge 单链路延伸整个企业 LAN，ENET1 口直接给远端 IP 摄像头供电（P6/P8，<<<PAGE 8>>>）
- 工厂仓库部分区域布线不可达：Multi-Point mesh，root 接有线，各 mesh AP 同时提供 Wi-Fi 覆盖与有线下联口（P6，<<<PAGE 6>>>）
- 临时活动场地快速开通：Auto-Mesh 只需激活 root，周边 AP 上电即自动入网（P7，<<<PAGE 7>>>）
- LAN 设备经 WDS AP 访问远端桥接设备：802.3 帧经 4 地址 802.11 帧中继，两端在 802.3 层建立连接（P7，<<<PAGE 7>>>）

## B（限制与坑）
- **Bridge 与 mesh 拓扑不能组合使用**，规划时必须二选一（P11，<<<PAGE 11>>>）
- Bridge 模式不对远端 Wi-Fi 客户端广播 WLAN 服务——需要远端无线上网就选 mesh（P6/P8，<<<PAGE 8>>>）
- Multi-Point 模式吞吐逐跳 ÷2，多跳链路末端速率会快速衰减，级联深度要克制（P7，<<<PAGE 7>>>）
- mesh 基础设施一旦定义即固定，不能当动态自组网用（P5，<<<PAGE 5>>>）
- AP 间距直接影响共享带宽，室内感觉不到的衰减在室外会被距离放大（P7，<<<PAGE 7>>>）

来源：OmniAccess Stellar Bridging/Multi-Point Meshing Guidelines，p5-8（Architecture + Auto-Mesh + WDS + 下联口）
