---
name: OmniVista 新平台选型（Cirrus 云 / Terra 本地 / OV2500 代际对比）
description: 售前为新网管平台选形态（云 Cirrus vs 本地 Terra）、对比上一代 OV2500/Cirrus 4 迁移、核对多租户/数据主权/5000 设备/ESXi 8 等硬边界时使用。
source_book: bp-nms-brochures（OmniVista Platform Datasheet p9-21）
---

## R（触发场景）
- 客户要换网管平台，纠结云（Cirrus）还是本地（Terra）
- MSP/多组织集中管理选型；政务/受监管行业数据不出境选型
- OV2500 / Cirrus 4 存量客户升级谈判（重配成本、迁移工具）
- Terra 部署前虚拟机资源与虚拟化平台核对

## I（核心理念）
代际×形态双轴矩阵（F1，<<<PAGE 9>>>/<<<PAGE 10>>>）：上一代 = OV2500（本地）+ Cirrus 4（云）；新一代 = Cirrus（云端微服务/多租户/MSP）+ Terra（本地 ≤5000 设备/Active-Active L2/数据主权）。选型第一刀切形态：多租户/多组织只有 Cirrus（<<<PAGE 15>>>）；数据主权/本地合规选 Terra（<<<PAGE 9>>>）。第二刀切规模：Terra 上限 5000 设备、1-3 虚机（<<<PAGE 15>>>），超限评估拆分或多实例。第三刀切存量：OV2500/Cirrus 4 迁移设备基本免重配且迁移工具随标准包（<<<PAGE 10>>>），但 AP1101/AP1201H 被排除、交换机需 AOS 8.9R1+（<<<PAGE 15>>>）。

## A1（行动框架）
1. 问行业与合规：数据不出境/本地安全合规 → Terra（<<<PAGE 9>>>）
2. 问运营主体：MSP 或多组织集中管理 → 只能 Cirrus（Multi-tenancy 仅云版，<<<PAGE 10>>>/<<<PAGE 15>>>）；单组织多站点 → 两者皆可（Multi-sites 双支持，<<<PAGE 10>>>）
3. 问规模与资源：≤5000 设备 Terra 可行；虚机 1-3 台×(8vCPU/32GB/3TB 数据盘)，ESXi 8+/Hyper-V、AVX/AVX2、SSD/NVMe ≥50MB/s（<<<PAGE 15>>>）
4. 问存量设备：AP1101/AP1201H 不支持；交换机 AOS ≥8.9R1；Stellar 15xx 需 AWOS ≥5.0.1MR（<<<PAGE 15>>>）
5. 问付费偏好：要 OPEX 按月 → 只能 Cirrus Flexible Pay（<<<PAGE 16>>>）

## A2（选型速查表）
| 维度 | OmniVista Cirrus（云） | OmniVista Terra（本地） | 页码 |
|---|---|---|---|
| 定位 | 云 SaaS，原生微服务 | 数据主权/本地合规 | <<<PAGE 9>>> |
| 多租户/MSP | 支持（层级 MSP→租户→站点） | 仅 Multi-sites | <<<PAGE 10>>>/<<<PAGE 15>>> |
| 规模上限 | 多区域数据中心弹性 | ≤5000 设备，1-3 虚机 | <<<PAGE 15>>> |
| 高可用 | 多区域数据中心+灾备 | Active-Active L2 | <<<PAGE 10>>> |
| 虚拟化 | ALE 托管 | VMware/Hyper-V，ESXi ≥8，AVX/AVX2，SSD/NVMe | <<<PAGE 15>>> |
| 内置 NAC | UPAM（认证/角色/访客/BYOD） | UPAM | <<<PAGE 9>>> |
| 迁移来源 | Cirrus 4 / OV2500，设备免重配+迁移工具 | 同左 | <<<PAGE 10>>> |
| 设备门槛 | AOS 8.9R1+ / AWOS 5.0.1MR+ / 排除 AP1101、AP1201H | 同左 | <<<PAGE 15>>> |
| 合规 | SOC1/SOC2、GDPR/CCPA、MFA | 本地自主 | <<<PAGE 10>>>/<<<PAGE 15>>> |
| 固件升级 | 云推送 | 客户自访问 ALE 仓库 | <<<PAGE 16>>> |

## E（选型决策案例）
- MSP 管理多家客户网络 → 选 Cirrus：Multi-tenancy 仅云版支持（C1，<<<PAGE 15>>>/<<<PAGE 10>>>）
- 政务/受监管行业数据不出境 → 选 Terra（C2，<<<PAGE 9>>>）
- campus 约 4000 台 AP+交换机全本地管理 → Terra 按 1-3 虚机规划（C3，<<<PAGE 15>>>）
- OV2500 客户怕重配 → "Minimal device reconfiguration"+迁移工具随标准包（C4，<<<PAGE 10>>>）

## B（反例与坑）
- Terra 只支持 VMware/Hyper-V，ESXi 最低 8；KVM/Nutanix 不在列；磁盘必须 SSD/NVMe ≥50MB/s（X8，<<<PAGE 15>>>）
- AP1101 与 AP1201H 明确不支持新平台，存量需先换 AP（X5，<<<PAGE 15>>>）
- 交换机纳管门槛 AOS 8.9R1（比 NetAdvisor 的 8.7R2 更高），老版本先升级（X6，<<<PAGE 15>>>）
- Stellar AP 需 AWOS ≥5.0.1MR（X7，<<<PAGE 15>>>）
- 迁移工具能力因源系统与版本而异，非全自动等价迁移（X14，<<<PAGE 10>>>）
- Terra 无云推送，升级需客户自己从 ALE 仓库拉取执行（X11，<<<PAGE 16>>>）

来源：bp-nms-brochures verified.md（C1-C4/X5-X8/X11/X14/F1/P14-P19/P29-P31）
