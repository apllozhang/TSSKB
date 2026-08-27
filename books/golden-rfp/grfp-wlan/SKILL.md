---
name: Stellar WLAN Golden RFP 精粹（无控制器自组网/RF 管理/wIDS-wIPS/AP Type 分级选型）
description: 写无线标书或选型 Stellar AP 时使用：OmniAccess Stellar WLAN Golden RFP 6.0.2 的管理架构（AP 自组群集免控制器）、RF 与客户端引导通用需求（ACS/APC/CSA/RSSI 门限/airtime 公平调度）、wIDS/wIPS 内置、RAP 远程接入与 Mesh，以及 Type A-Q2 共 22 类 AP（WiFi 5/6/6E/7）的关键规格抽样。
source_book: Alcatel-Lucent OmniAccess Stellar WLAN Golden RFP 6.0.2 (August 2026)
---

## R（何时用）
- 投标无线网络项目，需要逐条应答 WLAN 需求
- 按场景给 AP 定档：办公高密 / 酒店墙壁面板 / 室外远距 / IoT 融合
- 解释 Stellar 架构话术：控制面嵌在 AP 里、"management server down 不影响转发"

## I（核心理念）
Stellar 的差异化主线是**分布式自治 + 可平滑升级到集中管理**：AP 能互发现、自动成组（cluster）、推举 Virtual Manager（不需要任何外部服务器或额外许可证，条目 2.1.1–2.1.7）；迁入 OmniVista 云端/本地集中管理后可扩到本地 4000 AP / 云 10K AP（2.2.4/2.2.5）；数据面本地转发不依赖控制器，管理服务器宕机 AP 照常转发（3.2.1、2.2.6–2.2.7）。需求组织为：Section 2 管理 → Section 3 共性（法规认证/RF/方案要求）→ Section 4 按 Type A-Q2 共 22 类 AP 的逐台规格。版本锚点：6.0.2 = AWOS 5.0.5 + OVCX/OVTX 10.6.1 + OVE 4.9R3。

## A1（决策要点）
1. **AP 选型轴**：代际（WiFi 5 仅剩一款室外 Type A；WiFi 6 为 B-H；WiFi 6E 为 I-K；WiFi 7 为 L-Q）× 场景（室内普通/酒店面板带 RJ45 下联口 Type C / 高密三射频 / 室外 harsh）× 天线（内置 vs 外置 E2/O2/Q2 带 RP-SMA 或 N 型口）。
2. **容量分档看两个数**：并发终端（512 → 1024 → 1536）与聚合速率（1.7G → 3G → 3.5G → 9.3G+），见 A2 表。
3. **供电规划**：多数室内型号 802.3at 起；入门型标 802.3af；多 gig 上联口是中高端标配（E 系起 2.5G，O/N/P/Q 到 10G）。 outdoor Q2 支持外接天线避雷、N 型连接器。
4. **6GHz 合规**：标准功率 6GHz 需 AFC（FCC/ISED 辖区）；室外不许 6GHz 的辖区可把 6GHz 射频软件配置为 5GHz 工作（4.22.13）。

## A2（细节速查表）

**Management 抽样**
| 条目 | 要点 | 编号 |
|---|---|---|
| 任意 AP 可当 cluster manager，高级 AP 加入可抢占升级为 manager | 免许可自组网 | 2.1.1/2.1.7 |
| 本地部署 ≤4000 AP / 云 ≥10K AP | 规模上限口径 | 2.2.4/2.2.5 |
| 分布式转发，本地桥接不依赖中心控制器 | 数据面承诺 | 2.2.6 |
| wIDS/wIPS 内置免额外设备与许可，rogue AP 反制、MAC 前缀黑白名单 | 无线安全卖点 | 2.3.11–2.3.15 |
| RAP 远程 AP 建 IPSec 隧道回总部 + split tunneling；Guest 流量 GRE 隧道隔离 | 远程/访客两件套 | 2.3.3–2.3.6 |
| Bridge mode 点对点无线互联、Mesh 多站点 | 视距外布线替代 | 2.3.8–2.3.9 |

**RF 通用需求抽样**（Section 3.1）
| 条目 | 要点 | 编号 |
|---|---|---|
| ACS 自动选信道且"client aware"防无谓切信道；CSA 可配计数 | 信道管理 | 3.1.8–3.1.11 |
| APC 自动功率 + 功率上下限设定 | 功率管理 | 3.1.13–3.1.14 |
| 感知语音视频呼叫（SIP/H.323）回避后台扫描 | 多媒体保障高频考点 | 3.1.21 |
| 5GHz 引导/强制新客户端、AP 间负载均衡、RSSI 准入门限（分 band 配置）+ 低 RSSI 强制漫游 | 客户端引导五连 | 3.1.22–3.1.27 |
| airtime 公平切片分配（per band 可配） | 时分公平 | 3.1.28 |
| part-time/dedicated air monitoring 双模式 | 频谱侦察 | 3.1.17 |

**方案级**（3.2）：分布式控制架构；基于用户角色/SSID/策略的选择性隧道（企业本地出、特定流集中走）；RBAC；应用识别分类；IoT 终端识别；单 AP 一张license 含全部核心功能；相邻大版本固件互通。附加能力（3.3）：按需抓包导出、设备指纹免专用探针、实时策略执行。

**代表性 AP 型号对比**（Section 4）
| Type | 型号 | 代际/定位 | 射频配置 | 聚合速率 | 并发 | 以太口 |
|---|---|---|---|---|---|---|
| B | AP1301 | WiFi 6 入门室内 | 2×2 + 2×2 MU-MIMO | ≥1.7 Gbps | 512 | 2×GE (802.3af) |
| C | AP1301H | WiFi 6 酒店面板+RJ45下联 | 2×2+2×2 | ≥1.7 Gbps | 1024 | 上联 PoE(at/af)+下联含 PSE 供电+RJ45 直通电话口 |
| E1/E2 | AP1321/1322 | WiFi 6 中档（E2 外置天线 RP-SMA≥4 接口） | 三射频：2.4G 2×2 + 5G 4×4 + 专扫射频 | ≥3 Gbps | 1024 | ≥1 个 multi-gig(2.5G)+1 GE |
| F | AP1331 | WiFi 6 中高档 | 2.4G 4×4 + 5G 4×4 + 扫描射频 | ≥3.5 Gbps | — | multi-gig |
| H1-H3 | AP1361/1361D/1362 | WiFi 6 室外 harsh（H2 含定向天线、H3 外置口） | 同档双频 | — | — | 工业防护 |
| K | AP1451 | WiFi 6E 高端室内 | 三频含 6GHz | 高密旗舰 | — | multi-gig |
| N | AP1521 | WiFi 7 中档 | 三频 6GHz+MLO | — | — | multi-gig |
| O1/O2 | AP1541/1542 | WiFi 7 高端（O2 外置天线） | 三频 | 高密旗舰 | — | 10G 级 |
| P | AP1561 | WiFi 7 室外 premium | 三频 | — | — | 避雷+N 型外置 |
| Q1/Q2 | AP1571/1572 | WiFi 7 室外 harsh 中档 | 三频（320MHz@6GHz、4096-QAM、MLO） | — | ≥768 | ≥1×10G + 1GE |

WiFi 7 关键共性条目（以 4.22 为例）：IEEE 802.11a/b/g/n/ac/ax/be 全兼容；2.4/5/6 GHz 全射频同时工作不降性能；MLO 多链路操作及跨链路 QoS 时延优化；6GHz 320MHz 信道宽、4096-QAM；AFC（室外 6GHz 法规要求）；BLE/Zigbee IoT 射频内置。

## E（场景案例/怎么用）
- 校园高密投标：E1/F/K/N 组合 + 引 3.1.21（语音感知扫描）+ 3.1.24-27（负载均衡与漫游），全部标 C 附 AWOS 5.0.5 数据表。
- 连锁门店：RAP 条目 2.3.3-2.3.5 应答"无 IT 驻场远程组网"，配合 2.1.x 免控制器自组网讲 TCO。
- 工业园区外围覆盖：Type P/Q2（IP 等级、-40~65°C 工作温区、避雷、N 型外置天线）对标户外 harsh 要求。

## B（限制与坑）
- **可用性脚注必读**：Type A 在美国不可售（RW 区域可用）；Type D 计划 2026 年停产——引用型号前核对原文脚注和区域可用性。
- 许可证话术只覆盖"单 AP 单 license"（3.2.6）；OmniVista/OVTX 侧订阅另算，报价时别打包混谈。
- ovng 文档明确不含 Stellar WLAN 特性；反之本文档的 OmniVista 功能描述也只是引用级别，平台侧应答应以 grfp-nms 单元为准。
- Guest 访问/Captive Portal 详细功能在另外的材料（Stellar Guest 相关 Golden RFP），本卷只有接口级条目。
- 型号-能力对应关系写死在 Section 4 各小节；跨节抄参数（如把 K 的速率抄给 N）会出错，每条都带 4.x.y 编号定位。

来源：AlcatelLucentOmniAccesss-Stellar-WLAN_Golden-RFP_en.docx 6.0.2, August 2026（sources/grfp-wlan.md，约 1700 行）
