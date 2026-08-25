---
name: Stellar AP 管理规模与平台配套（Express 集群 / OV2500 4K / Terra 5K / Cirrus 12K-30K）
description: 售前为 AP 部署选管理模式（Wi-Fi Express 无控制器集群 255 台 / OmniVista 本地 Terra / 云 Cirrus）、核对 AP 数量上限与三模式同一镜像切换时使用。
source_book: bp-stellar-ap-datasheets（各型号 Management 节：p2/p7/p39/p68/p72/p83/p104 等）
---

## R（触发场景）
- AP 数量从小到大：免控制器集群够不够、何时必须上网管
- Wi-Fi 7 大规模部署的网管选型（超 4K AP）
- MSP 多租户或数据不出境项目配本地 OmniVista
- 同一网络多管理模式混用与后续切换规划

## I（核心理念）
管理规模阶梯（P21，<<<PAGE 72>>>/<<<PAGE 83>>>/<<<PAGE 104>>>）：Wi-Fi Express 无控制器集群 255 台（1360 系 256）→ OV2500 老网管仅 4K → Terra 本地 5K-10K → Cirrus 云 12K-30K（随型号与版本不同）。三种模式同一软件镜像切换（P19，<<<PAGE 7>>>）：Wi-Fi Express / OmniVista 本地 / OmniVista Cirrus，业务不锁死。Wi-Fi 7 代数据表已把 OmniVista 表述为云/本地两形态，2500 退居兼容角色（C11，<<<PAGE 68>>>）。规模数字随版本增长，报价前与 ALE 销售核实（X24）。

## A1（行动框架）
1. 数 AP：≤255 台且无集中管理诉求 → Wi-Fi Express 集群（免控制器、首台配置全网分钟级同步）
2. 数规模：≤4K 老网管 OV2500 尚可；超 4K 必须新一代 OmniVista（Terra 本地 / Cirrus 云）
3. 问主权与租户：数据不出境选 Terra；MSP 多租户选 Cirrus（结合 NMS 书平台选型 skill）
4. 按型号核对上限：1501 场景 Cirrus 30K；1540 场景 Terra 5K/Cirrus 20K；1511/1521/1561/1570 场景 OVT 5K/OVC 12K
5. 下单前与销售确认当前版本规模数字（持续增长中）

## A2（选型速查表）
| 管理模式 | 规模上限 | 适用 | 页码 |
|---|---|---|---|
| Wi-Fi Express 集群（virtual controller） | 255 AP/集群（1360 系 256） | 免控制器；Admin/Viewer/GuestOperator 三角色 | <<<PAGE 2>>>/<<<PAGE 8>>>/<<<PAGE 39>>> |
| OmniVista 2500 | 4K AP | 上一代本地网管（兼容角色） | <<<PAGE 83>>> 脚注 |
| OmniVista Terra（OVT，本地） | 5K（AP1511/1521/1561/1570/1540）；AP1501 场景 10K | 数据主权/本地合规 | <<<PAGE 83>>>/<<<PAGE 104>>>/<<<PAGE 72>>> |
| OmniVista Cirrus（OVC，云） | 12K（1511/1521/1561/1570）；20K（1540）；30K（1501） | MSP 多租户/云运维 | <<<PAGE 83>>>/<<<PAGE 104>>>/<<<PAGE 72>>> |
| 三模式切换 | 同一软件镜像 | Express ↔ OmniVista ↔ Cirrus 业务不锁死 | <<<PAGE 7>>> |

## E（选型决策案例）
- Wi-Fi 7 大规模部署：AP1501 场景 Cirrus 可到 30K；AP1540 场景 Terra 5K/Cirrus 20K；OV2500 只有 4K——超 4K AP 项目必须上新一代 OmniVista（C10，<<<PAGE 72>>>/<<<PAGE 104>>>/<<<PAGE 83>>>）
- 电信级/MSP 或数据不出境：Wi-Fi 7 代数据表明示 OmniVista 本地形态解决数据主权与安全合规（C11，<<<PAGE 68>>>）

## B（反例与坑）
- OV2500 上限仅 4K AP，Wi-Fi 7 大项目勿再按老网管规划（C10，<<<PAGE 83>>>）
- 管理规模数字随 OmniVista 版本增长，下单前与 ALE 销售核实当前数字（X24，<<<PAGE 83>>>/<<<PAGE 124>>> 脚注）
- L3 漫游需 OmniVista，纯 Express 集群只有 L2 漫游（<<<PAGE 11>>>）
- wIDS/wIPS 需 OmniVista 配合，无网管模式不能提供全时防护（<<<PAGE 1>>>）
- 集群规模口径差异：多数系列 255 台、1360 系 256 台，方案文档写规格时勿混（P20，<<<PAGE 2>>>/<<<PAGE 39>>>）

来源：bp-stellar-ap-datasheets verified.md（C10/C11/X24/P19-P21/P23/P26）
