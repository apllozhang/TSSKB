---
name: Hybrid POL 光园区方案与选型（POL+以太混合/两种推荐架构/降本模型）
description: 需要评估或设计 ALE Hybrid POL（HPOL）混合无源光园区——POL 光分配网+ALE 以太/Stellar 边缘、按需求分档选 SFP ONT+OmniSwitch 还是纯 ONT+Stellar AP、核算铜缆/机房/能耗降本时使用。
source_book: ALE Hybrid POL Solution Brochure（sol-campus-architecture DOC2）
---

## R（触发场景）
- 大园区/长距离布线场景评估 POL 混合方案 vs 纯铜缆以太
- 决定两档推荐架构：SFP ONT+OmniSwitch 接入 vs 纯 ONT+Stellar AP
- 向客户核算降本点：铜缆横布、机房与制冷、有源设备、能耗
- 规划 2.5G→10/40G 演进路径

## I（核心理念）
混合架构框架（F6，<<<PAGE 45>>>）：Nokia POL 光分配网（单纤点对多点+ONT）作物理承载 + ALE 以太接入交换机/Stellar AP 作服务边缘；POL 补距离与布线成本，以太边缘补 IP 端口密度与高功率 PoE（P63，<<<PAGE 45>>>）。点对多点光基础设施在密集部署中可去掉汇聚交换层（P64，<<<PAGE 45>>>）；光纤投资面向未来，保证 2.5G→10/40G 演进（P66，<<<PAGE 46>>>）。定位画像：大园区、长距离、中高用户密度（X21，<<<PAGE 46>>>）——并非处处适用。

## A1（行动框架）
1. 适用性判断（X21，<<<PAGE 46>>>）：大园区/长距离/中高密度→HPOL 理想；小园区纯以太更简
2. 两档架构选型（P65，<<<PAGE 46>>>）：需全层冗余/SPB/MACsec/高密 PoE/高级特性→SFP ONT+OmniSwitch 接入交换机；仅需基础特性/低 IP 密度→纯 ONT+Stellar AP（X22 对比其能力边界）
3. 降本核算四类（P62，<<<PAGE 45>>>）：铜缆横布减少+去专用电信间与制冷+有源设备减少+能耗降低
4. 容量与演进：2.5G 起步，光纤到桌面保证 10/40G 演进（P66，<<<PAGE 46>>>）

## A2（操作步骤）
- 边缘补强：在需高 IP 端口密度与 HPoE 预算的位置布 ALE 接入交换机（P63，<<<PAGE 45>>>）
- 密集部署场景以点对多点光基础设施替代汇聚层（P64，<<<PAGE 45>>>）

## E（实证案例）
- 两档推荐架构的适用对比：全冗余+SPB/MACsec 场景 vs 基础特性场景（P65/X22，<<<PAGE 46>>>）

## B（反例与坑）
- HPOL 并非处处适用：定位大园区、长距离、中高用户密度（X21，<<<PAGE 46>>>）
- 纯 ONT 架构能力边界：无全层冗余、仅基础网络特性、无统一接入要求、仅 PoE/PoE+、低 IP 端口密度——超界需求选 SFP ONT 架构（X22，<<<PAGE 46>>>）

来源：ALE Hybrid POL Solution Brochure（sol-campus-architecture DOC2，p44-47）
