---
name: spb-micro-segmentation
description: 客户问"零信任/微分段怎么落地"时，用认证→分类→供给三步流水线和校园弹性演示场景讲 SPB/UNP 方案。
source_book: DT00XPS279EN SPB Presales
---

# SPB 宏/微分段落地法（零信任三步流水线）

## R · 原文引用

> "MACRO AND MICRO-SEGMENTATION — ✓ Authenticate ✓ Classify ✓ Provision — Users; ✓ Authenticate ✓ Classify ✓ Provision — HVAC; ✓ Zero-trust framework; ✓ Software-defined segmentation."（p11）

> "Dynamic SAPs supported from UNP service profiles. Device assignment to an SPB service profile. Automatic SAP creation... MAC auth? 802.1x auth? Classification Rules?"（p56）

> "Services stretch and contract as needed. Policy and identity driven. Reduced attack surface."（p15-17）

## I · 方法论骨架

把"零信任"从概念落到三步可执行流水线，对每类接入对象（用户、暖通 HVAC 等 IoT 设备）统一执行：

```
认证（MAC 认证 / 802.1x） → 分类（分类规则） → 供给（SPB service profile 自动下发）
```

- **宏分段**：粗粒度隔离（I-SID 级，一个服务实例一个隔离域）；
- **微分段**：细粒度策略（profile 内含 VLAN Tag→I-SID→BVLAN 映射、组播模式、VLAN 转换、ACL/QoS 策略表）；
- **动态 SAP**（p18）：设备认证通过后被指派到 SPB 业务 profile，SAP 自动创建——分段边界随身份动态建立，不需手工配端口。

三卖点话术：服务按需伸缩（stretch and contract）、策略与身份驱动、攻击面收敛。

## A1 · 书中案例

p15-17 用同一校园场景连续三页演示动态弹性：体育场/宿舍/图书馆/STEM 实验室/教职工/学生各属不同分段，一个 STEM PROJECT 临时把跨楼宇成员拉进同一专用服务，项目结束服务自动收缩。p11 配官方演示视频（youtu.be/IttOgoATWpY，主题即认证-分类-供给三步）。

## A2 · 触发场景

- 教育/园区客户问"微分段具体怎么落地、IoT 怎么管"；
- 需要一个零信任入门故事脚本打动非技术决策人时。
与相邻 skill 区分：只讲"为什么换 SPB"的总体卖点走 `spb-presales-battlecard`；SAP 封装/组播等数据面细节走 `spb-edge-services`；OV2500 上配置 UNP Profiling 的操作走 `spb-ov2500-delivery`。

## E · 可执行步骤

1. 盘点接入对象类型（用户终端、打印机、HVAC/摄像头等 IoT），每类画一行"认证方式 → 分类规则 → 目标 service profile"。
2. 用 STEM 项目场景讲弹性价值：临时业务拉专服务、结束自动收缩、全程策略驱动。
3. 演示路径：UNP profile 认证派生动态 SAP（或经 OV2500 的 UNP Profiling 向导），展示攻击面收敛。

## B · 边界与陷阱

- 分段粒度靠 I-SID（24 位，千万级空间）承载，不要用 BVLAN 做业务/分段维度（BVLAN 全网仅 16 个、推荐 4 个——见拓扑 skill 的 ce05）。
- 动态 SAP 依赖端侧认证方式：无 supplicant 的 IoT 设备走 MAC 认证，有 supplicant 的终端走 802.1x，方案里要逐类写清。
- 教材只给了场景与机制，具体 profile 字段与策略表以现网 AOS 版本文档为准。

---
来源条目: f04, p18, c15, g35
