# DIGEST — ALE 网络管理与运维工具彩页合集 精华

本书是 ALE 网管与运维工具彩页/数据表合集（5 份文档，23 页），覆盖 OmniVista 管理平台全家族（新一代 Cirrus/Terra + 上一代 OV2500/Cirrus 4）与四个配套工具（Network Advisor / Fleet Supervision / Milestone Plugin / Smart Tool）。定位是"售前选型速查"：什么场景选哪个管理工具、订阅怎么买、版本前提是什么。

## 一、知识地图（五技能单元，每份彩页一个）

1. **Network Advisor 数据表**（bp-network-advisor-datasheet）：AI/ML 运维伴随工具，识别/缓解/优化闭环，Rainbow Bot 交互；2000 设备上限、自备虚机、AOS 8.7R2+/AWOS 4.0.3MR-3+ 门槛、NETAD-* SKU（p1-4）。
2. **Fleet Supervision 方案页**（bp-fleet-supervision-sheet）：免费自助注册的资产盘点与支持合规工具——盘点/生命周期/软件版本/故障换新四合一，NIS2 抓手（p5-6）。
3. **Milestone Plugin 方案页**（bp-milestone-plugin-sheet）：OmniSwitch×Milestone VMS 集成，VMS 界面内远程复位摄像机，>90% 问题快速解决，端口级 PoE 可视+按摄像机优先级（p7-8）。
4. **OmniVista 主数据表**（bp-ov2500-nms-datasheet）：Cirrus 云 / Terra 本地双形态、OV2500 代际迁移、UPAM/QoE/热图/SPB 功能集、Terra ≤5000 设备与 ESXi 8 虚机规格、全量 OVCX/OVTX/OVC-C 订购 SKU（p9-21）。
5. **Smart Tool 方案页**（bp-smart-tool-sheet）：OT/IoT 现场独立工具，免云免 CLI；PoE Wizard 60 秒修复、一键 PoE Power Cycle（保留人工确认）、TDR 线缆测试（p22-23）。

## 二、五单元要点串讲

### 1. Network Advisor（p1-4）
AI/ML 运维伴随（非网管替代）：识别风险→一键/自动修复→调优建议闭环，本地+云混合架构。前提：用户须有 Rainbow 账号、虚拟机自备（2000 设备 210GB）、设备 AOS 8.7R2+/AWOS 4.0.3MR-3+；第三方设备仅 syslog+手工规则；不强制先买 Cirrus。订阅 NETAD-AP/SWITCH/TP × 1/3/5 年，按台计。

### 2. Fleet Supervision（p5-6）
免费自助注册，资产盘点/生命周期（EoS/EoL）/软件版本/故障换新四合一；资产采集=自动（多 OmniVista 系统）+手工导入序列号；NIS2 合规是欧洲抓手；在线换新需有效最终客户支持合同。只是盘点合规层，不含网管功能。

### 3. Milestone Plugin（p7-8）
VMS 界面内远程复位摄像机，省现场拜访；>90% 摄像机问题快速解决；按端口看 PoE 消耗、按摄像机设 PoE 优先级、端口锁定防篡改。硬前提：Milestone VMS + OmniSwitch。

### 4. OmniVista 主数据表（p9-21）
新一代双形态：Cirrus 云端原生微服务（多租户/MSP、SOC1/SOC2、Flexible Pay），Terra 本地（数据主权、≤5000 设备、1-3 虚机×8vCPU/32GB/3TB、Active-Active L2、仅预付、多 7 年期）。多租户只有 Cirrus，Terra 仅 Multi-sites。OV2500/Cirrus 4 迁移设备基本免重配、迁移工具随标准包。硬边界：AP1101/AP1201H 排除；交换机 AOS ≥8.9R1；Stellar 15xx AWOS ≥5.0.1MR；Terra 仅 VMware/Hyper-V、ESXi ≥8、AVX/AVX2、SSD/NVMe ≥50MB/s。订购三轴：形态（云/本地）× 服务档（Base→Business→Premium）× 设备档（APL/APH；Flexible Pay 分 Essential/Advanced，12-60 月按月）。

### 5. Smart Tool（p22-23）
OT 现场独立工具：免云免 CLI，装维外包人员零网络背景可用。PoE Wizard 60 秒诊断修复、一键 PoE Power Cycle 保留人工确认（监狱/赌场/银行）、TDR 线缆测试、Lightning Config 首装向导；90%+ 摄像机问题为电力/布线相关，直击根因。

## 三、本书在知识库中的位置

与 ov2500-* 系列（上一代本地网管操作手册）、ov-terra-deploy（Terra 部署）互补：本书提供"选哪层工具、怎么买"的售前视角，操作细节见对应书。跨工具易混点：Network Advisor 与 OmniVista 平台是伴随关系非替代；Fleet Supervision 只是盘点合规层；Smart Tool/Milestone Plugin 面向现场与视频运维人员；同一网络可同时部署多工具（F4）。

## 来源
bp-nms-brochures（5 份文档 23 页）。verified.md：cases C1-C10；counter-examples X1-X15；frameworks F1-F5；principles P1-P38；glossary 约 50 条。
