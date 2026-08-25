---
name: OmniSwitch 6920-D32 数据表速查（400G AI/HPC 骨干）
description: 售前为 AI/HPC、GPU 集群、RoCEv2 无损存储网络与 Azure Local 混合环境选型 OS6920-D32（32x400G、12.8Tb/s），核对 QSFP-DD 拆分、spine/super-spine 角色与单一型号限制时使用。
source_book: bp-omniswitch-datasheets（DOC 14 omniswitch_6920，p138-144）
---

## R（触发场景）
- AI/HPC/解耦存储/超大规模架构的 400G 骨干选型（spine/super-spine/border-leaf）
- RoCEv2 + PFC 无损 fabric（GPU 集群、RDMA 存储）方案
- 微软 Azure Local 混合/边缘环境的官方认证网络层
- 服务器接入提速（10G→25G/100G）带动的骨干带宽扩容

## I（核心理念）
OS6920-D32 是紧凑高密 400G 交换机："32 × 400G ports... Wire-rate non-blocking up to 12.8 Tb/s... With support for RoCEv2 and PFC, it enables a fully lossless fabric"（<<<PAGE 138>>>），SPB L2 VPN + Secure Boot，Azure Local 官方认证。层级：核心/DC 最高速固定档（400G 世代），与 6900（≤100G）互补。

## A1（与相邻系列选型差异）
- vs OS6900：6900 覆盖 1G~100G（6.4Tb/s、MACsec、VC 6 台）；6920 单机 12.8Tb/s 400G + 无损 fabric——要 400G/RoCEv2 上 6920，要端口多样性/MACsec 留 6900。
- vs OS9900：9900 模块化大密度（480 GbE/208 QSFP28、PoE）；6920 定向 AI/DC 骨干，无 PoE 无 GbE。
- 无 VC 堆叠能力（规格表无 VC 字段，<<<PAGE 142>>>）——扩展靠 spine-leaf 拓扑。

## A2（规格细节速查表）
机型（单一型号，<<<PAGE 139>>>/<<<PAGE 142>>>）：
| 项目 | 规格 |
|---|---|
| 端口 | 32x QSFP-DD：400G 或拆分 128x10/25G、128x50/100G、64x200G（订购描述另列 8x25/50G、4x40/100G、2x200G，<<<PAGE 143>>>） |
| 容量/缓冲 | 12.8（25.6）Tb/s 无阻塞；包缓冲最高 132MB |
| 平台 | Intel C3558 2.2GHz 四核、32GB RAM、M.2 SSD 50/64GB |
| 电源 | 1+1 热插拔：AC 1500W（200-240VAC/8A）或 DC 1600W（48VDC/40A），随机双电源 |
| 功耗 | 最小 386W（不含模块）；散热 1528 BTU/h |
| 环境 | 正吹 0~45°C（55°C 关机）；反吹 0~35°C（45°C 关机）；MTBF ~516k 小时 |
| 尺寸 | 1RU，深 59cm，整机重 14.01kg |
Layer 特性（<<<PAGE 139>>>/<<<PAGE 140>>>）：SPB-M（L2 VPN/fabric core/多租户）；完整 IPv4/IPv6 路由（OSPF/IS-IS/BGP/VRF/PIM）；RoCEv2 + PFC 无损；G.8032；RESTful API + OpenStack；Secure Boot。无 MACsec、无 VXLAN-EVPN/MPLS 条目、无 PoE。
规格红线：单型号 D32；反吹风道环境上限 35°C；深 59cm 需深机柜。

## E（适用场景）
- GPU 集群/AI 训练后台：RoCEv2+PFC 无损（C4），拆分口灵活配 spine/super-spine/border-leaf
- 高速存储（解耦存储/RDMA）网络
- Azure Local 混合与边缘 DC（官方认证，<<<PAGE 138>>>）
- 校园/企业 DC 骨干从 100G 向 400G 平滑演进

## B（限制与坑）
- 全册仅 OS6920-D32 一个型号，32x400G 固定；无 GbE/PoE 接入能力——接入层必须另配（X13）
- 反吹风道（-R）运行上限仅 35°C、45°C 关机（<<<PAGE 142>>>）——热通道机房选 -F 并规划风道
- 无 VC 堆叠——高可用靠拓扑冗余与 VRRP/BFD，不能靠堆叠
- 功耗门槛高：386W 起、满配双 1500/1600W 电源——机柜电力预算按 1.5kW+/台预留
- 400G 光模块（SR4.2/DR4/FR4/LR4）与拆分 DAC 需按拓扑单独订购（<<<PAGE 144>>>）
- 9416B 巨帧（非 9216）——与存储阵列 MTU 对齐时注意（<<<PAGE 142>>>）

来源：bp-omniswitch-datasheets DOC 14（p138-144，DID25120901EN February 2026）；verified.md C4/X13/P22/F5
