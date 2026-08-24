---
name: stellar-rap-backup-upgrade-ops
description: 何时用：远程 AP（RAP）双模式部署、Cirrus 4 云注册/许可/版本核对、备份-恢复-升级与监控告警运维时。
source_book: DT00XTE378EN Stellar WLAN Adv Troubleshooting & Update
---

# RAP 与运维：远程 AP 双流程 · Cirrus 云管 · 备份/恢复/升级 · 监控告警

## R · 原文引用

> "Freemium: Self Registration, Free of charge... Premium: All OV CIRRUS capabilities... Max amount of licenses: 5000... 1 license per Access Point; 50xGuest and 50xBYOD licenses included per AP license." (p409-411)

> "1 – Stellar Access Point Startup & Registration; 2 - VPN & OmniVista 2500 Settings Retrieval; 3 - VPN Tunnel (Management Traffic) Establishment; 4 – Configuration Settings Retrieval; 5 - VPN Tunnel (Clients Traffic) & Client Connection." (p384-390)

> "The configuration files are transferred in the WORKING and CERTIFIED folders but are NOT applied on the RUNNING configuration... launch the following command: reload from working no rollback-timeout." (p429)

> "It is not possible to perform a restore on a Stellar AP, as most of the configuration is pushed when the Access Points is inserted in an AP Group." (p430)

## I · 方法论骨架

四块运维能力：

1. **RAP 双模式选型**：Premium（只靠 Cirrus，全配置在云，四步上线）/ Freemium（Cirrus 只当引路人 + 本地 OV2500，五步双隧道：管理隧道连 OV2500，数据隧道 L2GRE 承载客户端流量）。两者都需公司侧部署 ALE VPN Server 虚机（OVF 从 BPWS 下载）；Freemium 的 VPN Server 要三块网卡（公网/管理/数据）。
2. **Cirrus 上云三查**：版本底线（AOS 8.4.1.R03+〔6560/6860N/6865/6870/6900〕、6.7.2.R03+〔6350/6450〕、5.1R1+〔2260/2360〕；AWOS 3.0.2+ 全部 AP）→ 账号模式（Freemium 免费受限可升 Premium；单实例 5000 设备/4000 AP）→ 注册流程（入 Catalog → 激活 → 赋许可 → 预配置）。
3. **备份-恢复-升级三段**：Save All 存 Running（交换机另 Copy to Certified）→ Resource Manager 备份（By Devices=交换机需 FTP；By AP Group=Stellar 唯一方式；类型 Configuration Only/Full/Images Only，可调度）→ 恢复仅对 AOS 有效且必须 reload from working；升级走 Upgrade Image 或单台 AP Web。
4. **监控闭环**：Topology 状态语义 + Trap Responder 按严重级别发邮件；Heat Map/Floor Plan 做 RF 现状与规划。

## A1 · 书中案例（Lab 精要）

- **c09 RAP Freemium 全流程**：Cirrus Device Catalog 凭序列号+MAC 声明并勾 Is this a Remote AP，配管理 VPN（公网 IP:6550、客户端池、OV2500 IP），导出 .conf 传到 VPN Server `/opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile`，建 vpn_mgmt 服务绑端点；OV2500 加默认路由（网关=VPN Server 私网 IP）后 AP 进 Managed。数据 VPN 第二条（vpn_data，端口 6551，L2GRE，绑 eth2）；SSID 的 Default VLAN 选 **Use Tunnel（Tunnel ID 必须为 0）**。
- **c10 备份恢复**：故意建临时 VLAN 70-80 再恢复——Result 显示 SUCCESS 但 VLAN 仍在，需 `reload from working no rollback-timeout`（约 3 分钟）+ VLAN Manager Poll 刷新。
- **c11 告警**：Trap Responder 规则（Agent=AP Group、severity=Critical、发邮件，主题可用 $TrapAgent$ 变量）+ System Settings 配 SMTP；重启 AP 人为制造 Critical 验证送达。
- **c12 规划**：Heat Map 画 5 米标尺线 + WallsHeavy 描墙 + 拖 AP 看真实覆盖；Floor Plan Auto Deployment（质量/型号/功率输入）算法自动布点。

## A2 · 触发场景（含与相邻 skill 的区分）

- 分支/家庭办公把公司网延伸出去（RAP）；存量网络上云评估（版本+许可盘点）；变更前备份与固件升级；告警邮件体系搭建。
- 与 `stellar-enterprise-onboarding` 的区分：那本 skill 是本地 OV2500 纳管常规 AP；本 skill 的 AP 远在公网另一侧、靠 VPN 隧道回公司，且含云管 Cirrus 事项。
- 与 `stellar-ssid-policy-advanced` 的区分：SSID 常规配置在那边；本 skill 只涉及 RAP 场景下 SSID 的 Use Tunnel 特殊项。

## E · 可执行步骤

**RAP Freemium 部署**：
1. 前置核对：AP 非 AP1101（不支持 RAP）；VPN Server VA 三网卡（公网/管理/数据）。
2. Cirrus 建 Freemium 账号，Catalog 声明 AP（序列号+MAC，勾 Remote AP），配管理 VPN 参数，导出 .conf。
3. .conf 上传 VPN Server 指定目录，建 vpn_mgmt 服务（Layer 3 VPN）绑端点，Apply。
4. 重启 AP，Maintenance > VPN Status 见 peer 握手即通；OV2500 加 192.168.0.0/24 路由指向 VPN Server。
5. 建数据 VPN（L2GRE）第二个 .conf 导入 eth2 端点；AP Group 指定 Data VPN。
6. SSID 的 Default VLAN/Network 选 Use Tunnel（Tunnel ID=0 + 选 VPN Server）。

**Cirrus 注册**：
7. 盘点版本（对照四条底线，低于先本地升级）；Freemium 一次性激活；Premium 逐台赋许可 + 预配置。
8. 卡 Waiting For First Contact：AOS 停云代理 `cloud-agent admin-state disable force` 或重启；Stellar AP 开机约 20 秒按 [f] 进 failsafe 做 firstboot。

**备份/升级/监控**：
9. 变更前铃铛 Save All；Resource Manager 备份（交换机按设备+FTP，AP 按 AP Group）。
10. 恢复后必跟 `reload from working no rollback-timeout`，变更窗口预留 3 分钟以上。
11. 升级：.zip 原包直接 Import（自动解压）→ 选型号 → 选设备/AP 组 → Install；或单台 AP 走 Web（AP Group 开 AP Web）。
12. 告警：Trap Responder 建规则 + System Settings 配 SMTP 并发测试邮件。

## B · 边界与陷阱

- **AP1101 不兼容 RAP**，远程站点选型避开。
- **Freemium vs Premium 是账号组合决定架构**：Freemium 必须配本地 OV2500；Premium 全在云。
- **Restore 显示成功 ≠ 生效**：文件只落 WORKING/CERTIFIED，必须 reload（ce04）。
- **固件包是 WinZip 自解压格式，切勿手动解压**，OV 导入时自动解包（ce05）。
- **Stellar AP 不能 Restore**：配置来自 AP Group 下推；备份文件用于离线分析/给技术支持；"恢复"AP 的实际路径是修 AP Group 或恢复出厂重新入组（reset 6 秒 / `ssudo firstboot -y`）（ce10）。
- **按地图备份不含 AP**：地图里混有 AP 也不备份，AP 只能按 AP Group 备份（p19）。
- Tunnel ID 必须 0；Cirrus 卡激活先查版本底线。
- Premium 每 AP 许可附送 50 Guest + 50 BYOD 门户账号，容量规划别漏算。

---
来源条目: f05, f06, f07, f08, p16, p17, p18, p19, c09, c10, c11, c12, ce04, ce05, ce10
