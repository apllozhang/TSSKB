---
name: ov2500-upgrade-deploy
description: 何时用：规划 OV 2500 4.9R2 升级路径、HA 升级顺序、容量选型、首次部署与网络/防火墙准备时。
source_book: OV2500 4.9R2 Release Notes
---

# OV 2500 升级路径与部署规则

## R · 原文引用

> "you can only directly upgrade to OV 2500 NMS 4.9R2 from OV 2500 NMS 4.9R1 ... Upgrading an OV 2500 NMS from 4.9R1 to 4.9R2 automatically includes a required upgrade to a 4.9R1 Patch 1 ... ensure that the 4.9R1 upgrade to 4.9R1 Patch 1 occurs first, before the upgrade to 4.9R2." (p9, p15-16)

> "The HA upgrade procedure requires first updating the Standby node then updating the Active node ... An L3 HA cluster is supported only with a fresh HA installation; you cannot convert an L2 HA cluster to an L3 HA cluster" (p15, p19-20)

> "Total Number of Managed Devices 500 / 2,000 / 5,000 / 10,000 ... Minimum Reserved OmniVista VA RAM for Standalone 20GB / 36GB / 64GB / 64GB ... The High-Availability Feature supports up to 4,000 devices." (p17-19)

> "First upgrade to OV 2500 NMS 4.9R2; then upgrade your Stellar APs to 5.0.2 ... when upgrading Stellar APs in a Mesh Network, you must upgrade them starting from the last node and proceeding hop-by-hop. You cannot use OmniVista Resource Manager for the upgrade" (p14, p19)

## I · 方法论骨架

升级项目分六个工作包，按序推进：

1. **路径判定**（p11）：只有 4.9R1 能直升 4.9R2；老版本先升 4.9R1。4.7R1 出发的完整链：4.7R1 Patch 2 → 4.8R1 → 4.8R2 → 4.9R1 → 4.9R2（五步）。4.9R1→4.9R2 用全新工作流，自动先打 4.9R1 Patch 1，严格按 Installation and Upgrade Guide 操作。
2. **HA 顺序**（p12）：先 Standby 后 Active。升完 Standby 等所有服务起来再升 Active（ce66 同步警告的解法）。
3. **容量选型**（p13）：四档 Low/Medium/High/Very High——设备 500/2000/5000/10000；AP 上限 500/2000/4000/4000；单机 RAM 20/36/64/64GB，HA 40/64/64GB；磁盘 HDD1:50GB + HDD2:512/1024/2048/2048GB。硬规则：HA ≤4000 台且须 Medium 以上。
4. **首次部署六规则**（p14）：配置并重启前不加新磁盘；RAM 不超宿主机可用；预留 RAM；CPU Shares=High；超 500 台用 VA 菜单扩 HDD2；SNMPv3+AES 建议 Intel AES-NI。
5. **网络准备**（p16）：放行五个外联域名（ovrepo/ep1/us.fluentnetworking.com、api.fingerbank.org、api.bcti.brightcloud.com）；关键端口：SNMP 161/162、MQTT 1883、RADIUS 1812/1813（转发 1814/1815）、CoA 3799、VMM 135+49152-65535、HA 节点间 TCP 8000/7801/2224 + UDP 5405、cliadmin SSH 2222。无直连外网必须配代理。
6. **设备侧升级**（p15）：先升 OV 4.9R2，再升 Stellar AP 到 AWOS 5.0.2；Mesh 网络从最末节点逐跳升级，用 AP Web GUI 而非 Resource Manager。

## A1 · 书中案例

- 单机转 HA：4.9R2 单机由 4.3R2 或更新 Standalone 升级而来才可转 HA；由 4.3R1 升级来的不行（ce69）。
- KVM 扩容盘检测不到前两块：disk1/disk2 各给 1KB 占位，容量给 disk3，占位盘不许删（ce61）。
- VMware Flexible NIC 升 4.8R1 失败：换网卡类型重配 IP 再升（ce60）。
- 许可三档：Starter 免费 30 台不过期；Evaluation 免费 60 台 90 天；Production 全功能，上限 10000 设备 / 4000 AP / 5000 VM（p17）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：制定升级方案、变更窗口排期、新装 VA、扩容、HA 架构设计、License 采购决策。
- 区分：只查"某机型固件配不配" → 用 `ov2500-49r2-features-compat`；升级中/后出现故障 → 用 `ov2500-known-issues`；升级风险评审（不可降级、强制改密等）→ 用 `ov2500-danger-traps`。

## E · 可执行步骤

1. 确认当前 OV 版本，套用路径规则得出升级步骤数；写变更计划时把 4.9R1 Patch 1 列为独立步骤。
2. HA 环境：先备份点，先升 Standby → 验证服务全起 → 再升 Active → 验证 → 复查 WCF 状态（升级+failover 组合会致 WCF 失效，重启 WMA，ce40）。
3. 按设备数选规模档，核对 RAM/磁盘/CPU 与 HA 上限；HA 主机名 ≤15 字符且不用大写。
4. 首次部署按六规则执行；KVM 环境按占位盘操作法扩容。
5. 防火墙按端口表与五域名放行；纯内网配代理（注意：运行后改系统端口会断代理外联，改回 Proxy 端口，ce53）。
6. 升 AP：全网 AWOS 5.0.2，Mesh 逐跳、Web GUI 操作。
7. 升级完成后：验证 Watchdog 已启动（启动排障第一步，p18）、默认凭据 admin/switch 会强制改密（p19）。

## B · 边界与陷阱

- HA 七条硬限制（ce69）：L3 无集群 IP；4.3R1 链不能转 HA；建集群后不能改 IP/主机名；主机名禁大写；不做内存同步；重同步期间禁 failover；L2 不能转 L3。
- 老路径历史坑：4.4R2→4.5R1/4.5R1→4.5R2 必须选 "Download and Upgrade"，"Download Only" 会失败（ce56）。
- 备份完整性：OS6900 AOS 8.3.1 全量备份丢 SSH Key 与 User Table，恢复后要手工补（ce13）。
- L3 HA failover 后 Top N 采集断档属已知问题，报表预期要设好（ce62）。

---
来源条目: p11, p12, p13, p14, p15, p16, p17, p18, p19, ce13, ce40, ce53, ce56, ce58, ce60, ce61, ce62, ce66, ce69, g02, g07, g14, g15
