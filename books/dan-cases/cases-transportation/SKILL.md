---
name: 交通客户案例集（12 例）
description: 查交通行业（航空、机场、铁路、公路、地铁、物流）客户用了哪些 ALE 产品与方案时使用。GRU Airport、SBB、Gotthard 隧道、Transit Wireless、NDOT、OmniSwitch 6855 Hardened、OmniPCX Enterprise
source_book: dan-cases（customer-reference-ebook-en-2024 p23-35）
---

## R（何时用）
- 售前打机场、航空公司、铁路、公路交通部门、地铁、公交、港口物流客户，需要同行业标杆案例做证据
- 客户痛点在：恶劣环境（隧道/地下/户外）网络、交通枢纽高密度连接、ITS（智能交通系统）骨干、跨国/跨站点统一通信、仓储物流 WLAN
- 需要论证"加固型交换机（Hardened Switch）+ 大规模骨干"在交通关键基础设施场景的可靠性

## I（核心理念）
交通章 12 例，覆盖航空（东航、GRU 机场、Atlasonline）、公路（Kanton Aargau、NDOT、LCRCA）、铁路（Gotthard 隧道、SBB）、地铁（Transit Wireless）、物流（Zibatra、Movis、Bolloré）。行业痛点：交通安全是人命问题（"safety first"）、网络必须耐受极端环境（隧道、地下、户外温差）、枢纽场景人流/设备密度极高、多站点跨国通信成本高。两大方案主线：一是 Hardened 加固交换机（6865/6855/6465）构建 ITS/隧道/地铁骨干（Gotthard、Transit Wireless、NDOT、LCRCA）；二是 OXE 统一通信降本增效（东航国际话费省 50%、Atlasonline 24/24 服务、Bolloré 全网 IP 化）。明星产品：OmniSwitch 6855/6865 Hardened（4 例骨干）、OXE（5 例）、OmniVista 2500 网管。

## A1（案例速查表）
| 客户 | 国家/地区 | 项目背景/挑战 | 采用的 ALE 方案与产品 | 成效关键数字 | 页码 |
|---|---|---|---|---|---|
| China Eastern Airlines | 中国 | 提升旅客与员工服务质量、降运营成本 | Communication：OXE Communication Server | 国际长途（香港/日本）路由节省 50% 话费 | p24 |
| GRU Airport（圣保罗国际机场） | 巴西 | 大规模改扩建：航站楼、物流、停机坪、跑道，多干系人语音网络 | Converged：OXE、OmniStack LS 6200/6400、OmniAccess AP61、8 Series IP Touch、OmniVista 4760 | 更高效的运营系统与旅客服务 | p25 |
| Kanton Aargau 土木工程部 | 瑞士 | 约 1200 公里州道网养护运营，网络安全与可用性持续优化 | Network：OmniSwitch 6560/6860/6900、6465/6865 Hardened、OmniAccess AP、OmniVista 2500 | 2013 年至今网络持续高可用（"It just runs"） | p26 |
| Atlasonline（摩洛哥航空子公司） | 摩洛哥 | 700 用户+200 呼叫中心坐席全球集中 IP 化 | Converged：OXE、OmniTouch Contact Center Standard、OmniSwitch 6450 | 24/24 服务连续性，软硬件持续可扩展 | p27 |
| Nevada DOT (NDOT) | 美国 | 5400 英里高速公路+1000+桥梁的 ITS 网络，"safety first" | Network：OmniSwitch 6865 Hardened、6860E、6900 | 保障每年 250 亿车英里的安全出行信息服务 | p28 |
| Liverpool City Region Combined Authority (LCRCA) | 英国 | 智慧交通转型：船岸通信、渡轮连接、云应用、智能票务 | Converged：OXE、OmniSwitch 6900/6450/6865/6860E、OmniVista 2500（NMS 服务化） | 24x365 服务连续，网络整合最大化投资回报 | p29 |
| Transtec Gotthard | 瑞士 | 152 公里 Gotthard Base Tunnel 隧道 IP 网络，168 条横通道零中断 | Network：OmniSwitch 6855 Hardened | 隧道设计寿命 100 年，ALE 已稳定运行其中 8 年；合作视频获 AVA Digital 与 Muse Creative 奖 | p30 |
| Schweizerische Bundesbahnen (SBB) | 瑞士 | 智慧车站：储物柜按乘客需求动态调整 | Network：OmniSwitch 6465 Compact Hardened、Nokia 骨干网管、第三方储物柜系统 | 实时监控+即时干预，储物柜服务更高效更友好 | p31 |
| Zibatra Logistik AG | 瑞士 | 办公区+27000 平方米仓库 WLAN 全覆盖 | Network：OmniSwitch 6860/6450、Stellar AP1221/AP1222（外置扇区天线）、OmniVista 2500 | 全仓库高性能可靠覆盖，消除闲置、提升生产力 | p32 |
| Transit Wireless | 美国 | 纽约地铁 4 区约 276 个车站光纤网，高流量密度+恶劣地下环境 | Network：OmniSwitch 6855 Hardened | 每天 33 万+用户在纽约地铁使用免费 Wi-Fi | p33 |
| Movis | 科特迪瓦 | 语音数据网分离，需走向数据共享、增强网络能力 | Network：OmniSwitch 6850E、6250 | 连接非洲市场与国际贸易更高效；计划扩展 UC 到 San Pedro 站点 | p34 |
| Bolloré Africa Logistics | 刚果（布） | 非洲最大综合物流网络重建：全 IP 电话、全员移动 | Converged：OXE、IP Touch 4018/4028、OmniTouch 4135 会议模块、OmniSwitch 6865/6450、OmniVista 4760 | 全网融合语音数据，使用更流畅；持续扩建中 | p35 |

## A2（精选案例详解）

### 1. Transtec Gotthard（瑞士，p30）——极端环境网络可靠性标杆
- 挑战：152 公里 Gotthard Base Tunnel 是全球最长铁路隧道之一，168 条横通道中任何微小网络中断都可能危及施工与乘客安全；全球首批大规模引入 IoT 的工程之一。
- 方案：OmniSwitch 6855 Hardened LAN Switch 构建隧道 IP 骨干。
- 成效：隧道按 100 年寿命设计，客户公开表示"ALE 过去 8 年掌控良好，未来 92 年也没问题"；双方合作视频获 AVA Digital 与 Muse Creative 两项大奖。售前要点：交通关键基础设施场景最有说服力的"可靠性叙事"。

### 2. Transit Wireless（美国，p33）——纽约地铁级高密度无线
- 挑战：跨 4 个区、约 276 个车站的大型光纤网，需在恶劣地下环境承载极高流量密度。
- 方案：OmniSwitch 6855 Hardened LAN Switch。
- 成效：每天 33 万以上用户在纽约地铁访问免费 Wi-Fi；客户计划继续提升带宽与质量并探索网络变现。售前要点：单一产品线撑起全球最繁忙地铁的公共 Wi-Fi。

### 3. China Eastern Airlines（中国，p24）——OXE 降本最直接证据
- 挑战：提升旅客与员工服务质量，同时显著降低运营成本。
- 方案：OmniPCX Enterprise Communication Server 统一通信平台。
- 成效：国际通信路由至香港/日本方向，节省 50% 话费（客户 IT 解决方案总经理原话）。售前要点：中国航空央企背书 + 明确百分比数字，打中国客户可直接引用。

### 4. Nevada DOT（美国，p28）——ITS 加固网络
- 挑战：5400 英里公路、1000+桥梁的州公路网 ITS 网络，目标"safety first"。
- 方案：OmniSwitch 6865 Hardened + 6860E + 6900。
- 成效：为每年 250 亿车英里的出行者提供准确出行信息、减少在途时间；客户称 ALE"全程超出预期"。

### 5. LCRCA（英国，p29）——区域交通局 Converged 全景
- 挑战：利物浦城市区智慧交通转型：渡轮船岸通信、云应用、智能票务扩展，关键系统 24x365 不能停。
- 方案：OXE + OmniSwitch 6900/6450/6865/6860E + OmniVista 2500 NMS（以服务方式交付）。
- 成效：多网络整合最大化投资回报，支撑面向未来的 IoT 就绪基础设施。

## E（售前怎么用这些案例）
- 按痛点选案例：隧道/地下/户外严酷环境 → Gotthard、Transit Wireless、NDOT（三板斧都是 Hardened 交换机）；国际话费降本 → 东航（50%）；呼叫中心/票务 → Atlasonline（200 坐席）；智慧车站 IoT → SBB；仓储物流 WLAN → Zibatra（27000 ㎡）；区域智慧交通 → LCRCA。
- 打中国客户优先用东航（央企+量化 50%）；打欧洲铁路客户用 Gotthard+SBB（瑞士双案例）。
- 量化话术：Transit Wireless"每天 33 万地铁用户"、NDOT"5400 英里/250 亿车英里"、Gotthard"152 公里/168 横通道/100 年寿命"。
- Hardened 交换机（6865/6855/6465）是交通章的差异化武器，其他行业章中很少出现，遇到严苛物理环境需求优先引用本章。

## B（引用注意）
- GRU、Bolloré 使用 OmniVista 4760、IP Touch 40xx 等老型号，Movis 案例为 2015 年前项目，报价时须替换为在售型号。
- 东航"省 50%"为特定路由（香港/日本）的客户口径，勿泛化为"OXE 省一半话费"。
- Gotthard 案例含 Nokia 与第三方组件，网络部分并非纯 ALE 方案，引用时说明边界。

来源：dan-cases · customer-reference-ebook-en-2024，p23-35
