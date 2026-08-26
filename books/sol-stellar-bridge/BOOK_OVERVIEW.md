# 书籍理解 BOOK_OVERVIEW

## 书籍定位

《OmniAccess Stellar Bridging / Multi-Point Meshing Guidelines》（ALE Network Solution Guide for SMB，Edition 01，AWOS 4.0.4 + OmniVista Cirrus 4.6.2，2022）是 ALE 官方的 Stellar 无线桥接与多点网状组网方案指南。面向网络工程师与售前/销售工程师，回答三个问题：

- **什么时候用**：bridge（两站点 LAN 延伸）vs Multi-Point mesh（难布线区域多点覆盖），覆盖室外、工业室内与家庭三类场景
- **怎么设计**：架构约束（角色、带宽减半、16 AP/5 SSID 上限）、室外工程（天线/Fresnel/法规/防雷）、距离-吞吐权衡、Ekahau PRO 勘测
- **怎么配置与运维**：OV2500 Enterprise 模式四步配置 + APUI Express 模式 + SSH 控制台监控排障

书的结构：p5-8 架构（含 Auto-Mesh、WDS）→ p8-17 用例与前提（室外 bridge、室外/室内多点、家庭）→ p11-15 室外工程与距离 → p18-20 勘测 → p20-27 配置（Enterprise/APUI）→ p27-32 监控。

## 单元导航

| 单元 | 主题 | 覆盖页码 |
|---|---|---|
| sol-bridge-mesh-overview | 架构总览：bridge vs mesh 选型、root/mesh 角色、双 root、WDS 4 地址、Auto-Mesh、带宽共享、下联口与 PoE 输出 | p5-8 |
| sol-bridge-mesh-usecases | 三大用例与前提：室外 bridge、室外多点、室内多点/家庭；mesh 节点六条规则；各场景支持 AP 清单 | p8-11, 15-17 |
| sol-bridge-mesh-outdoor-design | 室外工程与勘测：天线摆位、Fresnel 60% 净空、法规防雷、配件清单、距离-吞吐、长距天线门槛、Ekahau PRO | p11-15, 18-20 |
| sol-bridge-mesh-config | 配置流程：OV2500 AP Group/RF Profile/SSID/角色/uNP 下联口 + APUI 配置 | p20-27 |
| sol-bridge-mesh-monitor | 监控排障：SSH 开启、rfprofile.conf、iwlist/iwconfig/wlanconfig、链路质量与客户端指标 | p27-32 |

## 读者路径建议

- **售前/设计**：overview → usecases → outdoor-design（选型、限制、勘测报价）
- **实施/运维**：overview → config → monitor（照路径配置、SSH 排障）
- **快速查限制**：usecases 的 A2 表（16 AP、5 SSID、无漫游、VoIP 尽力转发、吞吐 ÷2）
