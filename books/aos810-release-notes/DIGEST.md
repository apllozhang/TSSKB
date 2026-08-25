# DIGEST — OmniSwitch AOS Release 8.10R4 Release Notes 精华

本书是 ALE OmniSwitch 全产品线 AOS 8.10R4 的版本发布说明（105 页），信息密度极高且大量内容为"手册里没有"的独占信息（原书自述 "Since much of the information in these release notes is not included in the hardware and software user manuals, it is important that you read all sections"）。结构上由升级前提（Prerequisites）、新特性、许可体系、Open/Fixed CR、热插拔规范与 12 个升级附录构成。以下按四个技能单元摘要，页码均指原书。

## 一、知识地图（四技能单元）

1. **升级方法论与固件三件套**（aos-rn-upgrade-path）：升级前巡检/基线/固件核对、标准升级五步、ISSU 十二步、FPGA/U-Boot/CPLD/ONIE 升级、回退（Appendix D-H，<<<PAGE 67-82>>>）。
2. **Secure Boot、ALE CA 与包管理**（aos-rn-secure-boot）：三平台 Secure Boot 启用次序、ALE CA 证书生命周期、pkgmgr 包管理、弱加密禁用与首访改密（<<<PAGE 26-34>>>/<<<PAGE 101-105>>>）。
3. **Open CR 已知问题排障库**（aos-rn-known-issues）：光模块/链路类、软件/协议类已知未修问题与平台端口级限制（<<<PAGE 14-21>>>/<<<PAGE 41-46>>>）。
4. **新特性与废弃变更**（aos-rn-new-features-deprecations）：8.10R4 新特性盘点、特性许可四层模型、跨版本废弃/行为变更清单（<<<PAGE 15-40>>>/<<<PAGE 52-61>>>）。

## 二、四单元要点串讲

### 1. 升级方法论：Standard vs ISSU 二分 + 固件三件套
升级方法论二分（F1，<<<PAGE 67-76>>>）：Standard 一次中断换确定性，ISSU 逐成员/逐 CMM 演进保业务；选型三问——平台支持否（6360/6465/6560/6570M 不支持 ISSU，X2）、源版本在支持清单否、要不要保留 running 目录名。固件三件套（F2）：AOS 镜像/U-Boot·ONIE·BIOS 引导件/FPGA·CPLD 逻辑件三者独立演进，`show hardware-info` 对 Minimum 列是升级第一动作（C3，<<<PAGE 4>>>）。标准升级五步以 `copy running certified` 收尾、`reload from certified` 兜底（C4）；ISSU 十二步的灵魂是 SSH 到 Slave（VFL 内网 IP 127.10.x.65）清同名目录 + 等全部 System ready 再认证（C5，<<<PAGE 74-76>>>）。ONIE 机型 CPLD 升级后只回 Certified 不回 running（X18）。

### 2. Secure Boot：平台分型决定次序
Secure Boot 三件配合：引导件升级+专用镜像+（ONIE 型）BIOS 使能（P1）。U-Boot 型（6360/6465/6560/6570M）次序颠倒则重启回落 Certified（X1/P2）；ONIE 型升镜像→BIOS 启用→装 onie deb（C10）；例外型（6860(E)/6865/9900/6900-V72·C32·V48C8·C32E）不支持或需 BIOS（X4）；混 VC 用最小公分母——非 Secure Boot 镜像（X3）。配套安全层：ALE CA 设备证书 5 年有效、到期前 1 年更新（P5）；首访强制改密打断 REST 自动化（X8）；su 口令忘却只能恢复出厂（P4）；TLS 默认 1.0→1.2（P8）；pkgmgr install 后必须 write memory 否则镜像校验失败（X16）。

### 3. Open CR：先对号再排障
硬件类：SFP-10G-T 只认 10G 对端（X38）、SFP-GIG-T 10M 场景反复 admin 翻动不稳（X39/X43）、CNI-U8 4x25G DAC 换 SR4 光纤（X40）、VFL 4X25G splitter CRC 调 inter-frame-gap=13（X44）。软件类：toggle 触发掉流一族（EVPN 对称 IRB/PIM+非对称 BGP/非对称 OSPF，X54）、聚合禁成员哈希失衡（X47）、BFD 在 VRRP VLAN toggle 丢包（X50）、二次 vc-takeover 丢 sdp/sap MAC（X56）。多数"无解"只能绕行——部署前对号可省无效变更。平台端口级限制（MACsec 端口矩阵 X22/X23、P48Z16 聚合口位 X21、6920/6575-MP16 无 VC X28/X29）是设计即如此。

### 4. 新特性与废弃：迁移硬前提
8.10R4 要点：Router/Edge-router Mode 规模切换、EVPN 多站点模型库+手工 RD/RT、PEG/OISM 组播网关、SPB 上 6570M/6575、Multi-Site SPB（SBN/site-id 突破 500-1000 节点上限）、DHL Active-Standby（无缝 failover 128 VLAN/1000 MAC 边界，P44）、Threat-Insight（DGA/MITM/JA3）、Telemetry IPFIX 管道。废弃红线：带 EVB 配置禁止升 8.5R4+（X6）；8.10R3+ 旧 EVPN 配置必须手工迁 VRF（X5）；OVSDB 移除（X68）；6560 Metro 特性转收费（X11）。许可四层：Feature/Performance→Metro→Advanced Routing（6560 版限 2 OSPF 区域、8.10R4 加 BGP）→Premium 捆绑（VC 内 Match/Local-Only 语义，P36）。

## 三、高价值页码索引

- 升级前置检查：<<<PAGE 70-71>>>；标准升级：<<<PAGE 72-73>>>；ISSU：<<<PAGE 74-76>>>；FPGA/U-Boot：<<<PAGE 79-80>>>；CPLD/ONIE：<<<PAGE 81-82>>>
- Prerequisites 必读：<<<PAGE 15-18>>>；许可：<<<PAGE 19-20>>>；新硬件：<<<PAGE 21-22>>>；新特性：<<<PAGE 23-40>>>
- Open CR：<<<PAGE 41-46>>>；热插拔：<<<PAGE 47-49>>>；Feature Matrix：<<<PAGE 52-61>>>；MACsec 平台：<<<PAGE 62-63>>>；SPB BVLAN：<<<PAGE 64-66>>>；Fixed CR：<<<PAGE 83-100>>>；包管理：<<<PAGE 101-102>>>；Secure Boot：<<<PAGE 104-105>>>

## 四、条目统计与技能对应

verified 计数：principles 48 / cases 19 / counter-examples 75 / frameworks 4 / glossary 63。技能对应：aos-rn-upgrade-path（F1/F2+C1-C8）；aos-rn-secure-boot（F3+C9-C13/C16）；aos-rn-known-issues（X 主体）；aos-rn-new-features-deprecations（F4+P 新特性+X 废弃）。
