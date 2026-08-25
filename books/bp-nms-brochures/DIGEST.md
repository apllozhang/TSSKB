# DIGEST — ALE 网络管理与运维工具彩页合集 精华

本书是 ALE 网管与运维工具彩页/数据表合集（5 份文档，23 页），覆盖 OmniVista 管理平台全家族（新一代 Cirrus/Terra + 上一代 OV2500/Cirrus 4）与三个配套工具（Network Advisor / Fleet Supervision / Milestone Plugin / Smart Tool）。定位是"售前选型速查"：什么场景选哪个管理工具、订阅怎么买、版本前提是什么。

## 一、知识地图（四技能单元）

1. **平台选型**（bp-nms-platform-selection）：Cirrus 云 / Terra 本地双形态、OV2500 代际迁移、多租户与数据主权边界、Terra 5000 设备与 ESXi 8 虚机规格（p9-21）。
2. **订阅与许可**（bp-nms-subscription-license）：Base/Business/Premium 三档、APL/APH 与 Essential/Advanced 设备分档、Flexible Pay OPEX 条款、SKU 命名规律（p16-21）。
3. **免费切入与视频插件**（bp-nms-fleet-milestone）：Fleet Supervision 零成本资产盘点/NIS2 合规、Milestone Plugin 摄像机远程处置与端口级 PoE（p5-8）。
4. **AI 运维与现场工具**（bp-nms-advisor-smarttool）：Network Advisor 异常检测+自动修复（Rainbow 交互）、Smart Tool OT 免云免 CLI 现景工具（p1-4 / p22-23）。

## 二、四单元要点串讲

### 1. 平台选型：代际×形态双轴
新一代平台双形态（<<<PAGE 9>>>）：Cirrus 云端原生微服务，Terra 本地 ≤5000 设备/Active-Active L2/数据主权。多租户（MSP）只有 Cirrus 支持，Terra 仅 Multi-sites（<<<PAGE 10>>>/<<<PAGE 15>>>）。OV2500/Cirrus 4 迁移设备基本免重配、迁移工具随标准包（<<<PAGE 10>>>）。硬边界：AP1101/AP1201H 被排除；交换机需 AOS ≥8.9R1；Stellar 15xx 需 AWOS ≥5.0.1MR；Terra 仅 VMware/Hyper-V、ESXi ≥8、AVX/AVX2、SSD/NVMe ≥50MB/s（<<<PAGE 15>>>）。

### 2. 订阅体系：三轴模型
形态轴：Cirrus 可 Flexible Pay，Terra 仅预付但多 7 年期（<<<PAGE 16>>>）。服务档轴：Base 只保 OmniVista 软件（不含设备硬件维保）→ Business 加硬件维保+AVR → Premium 加最终客户直享支持（<<<PAGE 16>>>/<<<PAGE 17>>>）。设备档轴：AP 按 x0x/x1x/x2x 归 APL、x3x+ 归 APH；Flexible Pay 分 Essential（AP+OS63/64/65/6570M）/ Advanced（OS68 及以上），12-60 月按月（<<<PAGE 17>>>/<<<PAGE 19>>>）。

### 3. 免费切入与视频插件
Fleet Supervision 免费自助注册，资产盘点/生命周期（EoS/EoL）/软件版本/故障换新四合一，NIS2 合规是欧洲抓手；在线换新需有效最终客户支持合同（<<<PAGE 5-6>>>）。Milestone Plugin 在 VMS 界面内远程复位摄像机，>90% 问题快速解决，端口级 PoE 可视+按摄像机优先级；前提是 Milestone VMS + OmniSwitch（<<<PAGE 7-8>>>）。

### 4. AI 运维与现场工具
Network Advisor 是 AI/ML 运维伴随（非网管替代）：识别风险→一键/自动修复→调优建议闭环，本地+云混合架构（<<<PAGE 1>>>）。前提：用户须有 Rainbow 账号、虚拟机自备（2000 设备 210GB）、设备 AOS 8.7R2+/AWOS 4.0.3MR-3+；第三方设备仅 syslog+手工规则（<<<PAGE 3>>>）。Smart Tool 是 OT 现场独立工具：免云免 CLI，PoE 向导 60 秒修复、一键 PoE Power Cycle（保留人工确认）、TDR 线缆测试（<<<PAGE 22-23>>>）。

## 三、本书在知识库中的位置

与 ov2500-* 系列（上一代本地网管操作手册）、ov-terra-deploy（Terra 部署）互补：本书提供"选哪层工具、怎么买"的售前视角，操作细节见对应书。跨工具易混点：Network Advisor 与 OmniVista 平台是伴随关系非替代；Fleet Supervision 只是盘点合规层，不含网管功能；同一网络可同时部署多工具（F4）。

## 来源
bp-nms-brochures（5 份文档 23 页）。verified.md：cases C1-C10；counter-examples X1-X15；frameworks F1-F5；principles P1-P38；glossary 约 50 条。
