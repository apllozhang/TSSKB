---
name: ov2500-install-on-esxi-hyperv-kvm
description: 何时用：在 ESXi/Hyper-V/KVM 上实际部署 OV2500 VA、跑初始向导及装机后基础运维配置时。
source_book: OV2500 4.9R2 Installation and Upgrade Guide
---

# OV2500 三平台安装部署与装机后基础配置

## R · 原文引用

> "OV 2500 NMS 4.9R2 is distributed as a Virtual Appliance only... VMware ESXi: 6.5, 6.7 and 7.0.2, 8.0; MS Hyper-V: 2012 R2, 2016, 2019, and 2022; MS Hyper-V on Windows 10 Professional; Linux KVM/Ubuntu 22.04." (p8)

> "When deploying the OmniVista VA for the first time, do not add the new disks in the hypervisor until after OmniVista is configured and rebooted. Note that editing the size of existing virtual disks is not supported." (p10)

> "To access the Virtual Appliance Menu for a VM, launch the Hypervisor Console... You can also access the Virtual Appliance Menu by connecting via SSH using port 2222, user cliadmin." (p272)

> "If you change the OV IP address in the VA Menu, the network is NOT touched. For wired devices, you must reconfigure the sFlow receiver, policy server, and SNMP trap station... For Stellar APs, you must reconfigure the DHCP Server, and reapply WLAN Services and Global Configurations in Unified Access." (p276)

## I · 方法论骨架

1. **导 VA**：按平台取对应包（ESXi 用 OVF+VMDK；Hyper-V 用导入包；KVM 用 qcow2 双盘），部署 VM 但**不提前挂扩展盘**。
2. **初始向导**：开机进 VM Console 向导——设 Technical Support Code 密码 → 设 cliadmin 密码 → 主机名（≤15 字符小写）→ 网络（OV IP / Captive Portal IP / 附加 Web IP，推荐独立子网+独立网卡）→ NTP。
3. **配完重启后**再做加盘、加额外 NIC 等硬件动作。
4. **装机后基础运维**全部经 VA 菜单（Console 或 SSH 2222/cliadmin）：Watchdog 管服务、Service Profile 裁剪省内存、改 IP、加网卡、NTP、关机流程。

## A1 · 书中案例

- 新手想一步到位，部署 VA 前就预挂扩容盘——官方明确禁止；须等 OmniVista 配置完成并重启后再从 Hypervisor 加盘（p10）。
- 用 Configure Other Network Cards 加第二块网卡做跨子网发现：新网卡误配在主 OV IP 已管理设备的同子网，导致现有设备发不出 trap/报文；且新网卡必须与第一块同型号（eth1 与 eth0 同类型），经新网卡发现的设备 trap station 还要手动指到新网卡 IP（p285）。
- 内存紧张的中型网络：Watchdog 菜单 Choose Service Profile 选 "2 4 5"（不开 Stellar/UPAM、不开 IoT、不开 sFlow）一次裁掉三类服务（p287）。
- KVM 部署初期：两块系统盘按手册选 VirtIO 总线并设 Discard Mode=unmap（p33）。

## A2 · 触发场景（含与相邻 skill 的区分）

- **用本 skill**：拿到 VA 包后到"能登录 Web UI 并激活许可"这一段，以及装机后的常规菜单运维（服务启停、改 IP、加网卡、NTP、关机）。
- 与 `ov2500-sizing-and-platform-planning` 的区分：档位/资源/端口的决策在那边；本 skill 是照决策执行安装与菜单操作。
- 与 `ov2500-ha-cluster-design-and-conversion` 的区分：VA 菜单里 Convert/Join Cluster 相关操作归那一个；本 skill 只覆盖单机（Standalone）形态。
- 磁盘扩容完整流程（含 KVM SATA 怪癖）在升级 skill 的备份恢复/存储单元；此处只强调"首装别提前加盘"。

## E · 可执行步骤

1. 从规划清单取档位参数，在 Hypervisor 建/导 VM（三平台任一，版本在兼容矩阵内）。
2. 开机进 Console 向导：依次设 Technical Support Code 密码、cliadmin 密码（**丢失无法找回**，入密码库）、主机名（默认 omnivista，≤15 字符小写）、三 IP（OV / Captive Portal / 附加 Web，推荐各自独立子网+独立网卡）、NTP 服务器（可即时或稍后启用）。
3. 等 OmniVista 配置完成并重启，之后再从 Hypervisor 添加扩展盘/额外 NIC，回到 VA 菜单继续 Completing the OmniVista Installation。
4. 首次登录 Web UI（https://<服务器IP>），导入正式或评估许可（评估：lds.al-enterprise.com，99999/evaluation/omnivista，90 天）。
5. 日常菜单入口：Console 或 SSH 2222 端口 cliadmin 登录 VA 菜单；SFTP 22 端口用于传证书、取备份/日志。
6. 服务运维用 Watchdog（菜单 3/5）：查全部服务状态；Choose Service Profile 按需裁剪（2-不开 Stellar/UPAM，3-不开应用可视化，4-不开 IoT，5-不开 sFlow，可多选如 "2 4 5"）；可加 1-4096MB swap。注意停 ActiveMQ/Tomcat 会连带关 Web 服务器，需手动恢复。
7. 改 OV IP（如必要）：记住网络侧不受影响，须手动同步——有线设备重配 sFlow 接收器、policy server、SNMP trap station 并从 Analytics/Policy View QoS/Notification 重推；Stellar AP 重配 DHCP 服务器并在 Unified Access 重应用 WLAN 服务与全局配置；改后不可达就重启服务器。
8. 标准关机：Watchdog → Stop All Services → VA 菜单 Power Off/Reboot。任何情况下不得直接关宿主机断电。

## B · 边界与陷阱

- **禁止首装前预挂扩展盘**；不支持编辑既有虚拟盘容量（p10）。
- cliadmin / Technical Support Code 密码丢失无法找回，只能重装。
- Hyper-V：不支持 Live Migration；VM Manager 仅支持 2012/2012R2/2016（p19）。
- KVM：系统盘用 VirtIO+unmap；后续扩容盘规则完全不同（SATA 总线、前两块新盘不可见，详见扩容单元）。
- 改 OV IP 不会自动更新网络设备，trap/策略/DHCP 全要手动重推（p276）。
- Stellar AP 必须跑 Release Notes 认证的 AWOS 版本，一般在 OV 升级完成后再刷 AP 固件（p8）。
- 直接关宿主机给 VM 断电是数据损坏禁忌；长操作（扩盘等）全程不得对 VM 断电或复位（p8, p292）。

---
来源条目: p03, p07(部分), p20, p26, p27, p31, ce02, ce15, ce17, ce18, g01, g02, g13, g14, g15, g19, g20, g22, g23, g25
