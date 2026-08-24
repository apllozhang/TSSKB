---
name: ov2500-ha-cluster-design-and-conversion
description: 何时用：设计或把 Standalone OV2500 转成 L2/L3 HA 集群、以及集群日常运维（同步/切换/节点替换）时。
source_book: OV2500 4.9R2 Installation and Upgrade Guide
---

# OV2500 HA 集群：L2/L3 选型、转换与集群运维

## R · 原文引用

> "Layer 2 Configuration - In a Layer 2 HA Configuration, both OmniVista Server VMs must be on the same subnet. In this configuration, you configure a virtual Cluster IP address... Layer 3 Configuration - In a Layer 3 HA Configuration the OmniVista Server VMs are on different subnets, with a unique IP address for each server." (p41)

> "You can convert a 4.9R2 Standalone Installation to a 4.9R2 HA Installation if the 4.9R2 Standalone installation was upgraded from a 4.3R2 or newer Standalone Installation. You cannot convert... if... upgraded from a 4.3R1 Standalone Installation. Converting an L2 HA installation to an L3 HA installation is not supported. Only a fresh L3 HA installation is supported." (p40-41)

> "The recommended network bandwidth is 1Gbps. The recommended network latency is 1ms." (p42)

> "Enter 17 and press Enter to change the IP address and Hostname (maximum of 15 characters) of the Peer Node. It is not recommended to re-configure the Peer Node once a cluster is initialized. If you change the configuration, you must take a backup of OmniVista and contact Customer Support to re-configure the Cluster." (p303)

## I · 方法论骨架

1. **资格校验**：HA License 已导入？规格 ≥Medium、设备 ≤4000？来源版本：全新 4.9R2 Standalone 或自 ≥4.3R2 升级而来（4.3R1 来源不能转）。
2. **拓扑选型**（一锤定音，L2 不能改 L3）：
   - **L2**：两节点同子网 + 虚拟 Cluster IP。设备零改动（把原 Standalone IP 腾出来当 Cluster IP 是最佳实践）。功能完整。
   - **L3**：两节点跨子网、各有独立 IP。设备须能同时连两节点；须配 Preferred Node（cliadmin）；受限：设备回连类功能（sFlow、Policy 对 AOS）不支持、IoT 需 failover 后重应用、Syslog 需外部服务器、DNS/Provisioning 需重配、Captive Portal 被禁用；L3 冗余仅 AP13XX+（AWOS 5.0+）。
3. **地址与命名规划**：Node1/Node2 物理 IP；L2 专属 OV 虚拟 IP、可选 Captive Portal 虚拟 IP 与附加 OV Web 虚拟 IP（须与对应静态 IP 同子网）；主机名 ≤15 字符全小写（ov1 非 OV1）。
4. **转换执行**：Node 1 菜单 12 Convert to Cluster → Node 2 菜单 13 Join Cluster（输 Node 1 物理 IP 与 cliadmin 密码）。
5. **集群运维铁律**：操作前看 Show OV Cluster Status，Data Sync 必须 "Up to Date"；集群级操作只在 Active 节点做。

## A1 · 书中案例

- 已有 Standalone（IP 10.1.1.10）转 L2 HA：转换 Node 1 时给它分配新物理 IP，把 10.1.1.10 腾出来作 Cluster IP——全网设备不用改地址（p21, p40）。
- 转换向导中手痒改了已有 Captive Portal 配置——结果所有 Captive Portal 相关设备配置（含 Unified Profile 的 Global Settings）全部要手动重配；正确做法是保持原配置直接回车（p46）。
- Standby 节点巡检发现 upam、nginx 服务 "Stopped"——这是预期行为不是故障，别急着"修复"（p52）。
- L3 failover 后界面显示 AP down 长达 5-10 分钟——AP 实际仍在线，只是在与新节点重建会话，误判会导致无谓重启设备（p42）。

## A2 · 触发场景（含与相邻 skill 的区分）

- **用本 skill**：客户要求网管高可用、单机要改双机、或集群已建需日常运维/节点替换/failover 排障。
- 与 `ov2500-upgrade-backup-restore` 的区分：**升级**一个已存在的 HA 集群（维护模式、先升 Standby、重启时机）归升级单元；本 skill 管"建集群"和"平时管集群"。扩盘（HA 两节点 Extend Partitions）也在升级单元的存储部分。
- 与 `ov2500-sizing-and-platform-planning` 的区分：那一边只给容量门槛（≥Medium、≤4000 设备）；选型落地的全部细节在本 skill。

## E · 可执行步骤

1. 前置校验：导入 HA License；确认规格 ≥Medium、设备数 ≤4000、来源版本 ≥4.3R2（全新 4.9R2 安装亦可）。
2. 选拓扑：能同子网就选 L2（设备零改动、功能全）；必须跨子网才选 L3，并逐项核对 L3 功能受限清单与 AP 型号门槛（AP13XX+ / AWOS 5.0+），确认 Captive Portal 被禁可接受。
3. 网络基线：节点间带宽 1Gbps、延迟 1ms；宿主机网卡驱动最新（Hyper-V Broadcom b57nd60a.sys ≥16.8；VMware Tg3-3.133d.v55.1-101300361+）。
4. 规划地址清单：两节点物理 IP；L2 的 Cluster IP（建议用原 Standalone IP）及可选虚拟 IP；主机名（≤15 字符小写）。
5. 备份 + 快照后执行转换：Node 1 菜单 12 Convert to Cluster（Captive Portal 已配置则保持默认回车）；Node 2 菜单 13 Join Cluster。转换全程在 Console 做，禁止 SSH。
6. 验证：Show OV Cluster Status 确认 Data Sync "Up to Date"、集群状态正常；L3 集群注意 Active 由系统随机指派，确认谁是 Active。健康判据：Active 全服务 Running；Standby 除 upam/nginx（及自定义 RADIUS 证书时的 ovradius）外全 Running。
7. 日常运维：任何配置/升级/扩盘前先确认 "Up to Date"（同步中严禁操作）；集群级参数（Cluster IP、Manual Failover、Maintenance Mode、Preferred Active Node）只在 Active 节点改。
8. 节点故障替换：Remove Peer Node From Cluster（仅 Active 可发）后该节点即报废不可复用——只能新起 VM、扩数据分区到与旧节点一致后 Join Cluster。

## B · 边界与陷阱

- **L2 不能转 L3**，L3 只能全新搭建（仅有的例外：全新 4.9R1 Standalone 加第二节点组 L3；4.8R2 升 4.9R1 后转 L3）。
- 4.3R1 升级来源的 Standalone 不能转 HA（p40-41）。
- 集群初始化后**不要**改 Peer Node 信息或本节点 IP/端口——必须先备份并联系客服重配集群（p303）；改 Cluster IP/虚拟 IP/端口是支持的（仅 Active 节点，同子网）。
- 被移除节点保留 HA 菜单、无法加入其他集群，视同报废（p299）。
- Data Sync 显示百分比（同步中）时在该节点做配置，变更可能被覆盖/分叉（p296）。
- L3 功能受限清单见方法论第 2 步；L3 必须配 Preferred Active Node（默认不设，p302）。
- L3 failover 后 AP 假 down 5-10 分钟是正常窗口（p42）；L3 升级 ov1 前必须停 ovactivemq（详见升级单元 g26 场景）。
- HA 安装的备份/恢复自 4.5R1 起才支持。

---
来源条目: p02, p15, p16, p17, p18, p19, p20, p21, p24, ce11, ce12, ce13, ce14, ce16, g03, g04, g05, g06, g07, g08, g09, g10, g11, g12, g26, g27, g28
