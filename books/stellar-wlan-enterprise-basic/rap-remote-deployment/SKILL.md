---
name: rap-remote-deployment
description: 何时用：把 Stellar AP 部署到远程站点（门店/展会/家庭），经 Cirrus 注册与 ALE VPN Server 隧道广播企业 SSID 时。
source_book: DT00XTE368EN Stellar WLAN Enterprise Basic
---

# RAP 远程部署（Cirrus + VPN Server）

## R · 原文引用

> "1 – Stellar Access Point Startup & Registration. [PRE] – Settings to be Entered by the Administrator. 2 - VPN & OmniVista 2500 Settings Retrieval. 3 - VPN Tunnel (Management Traffic) Establishment. 4 – Configuration Settings Retrieval. 5 – VPN Tunnel (Clients Traffic) & Client Connection." (p439)

> "RAP = Remote Access Point. Goal: Extend the corporate network to remote site(s)... Equipment: OmniVista Cirrus 4 (Freemium with OV2500 / Premium) + ALE VPN Server + Stellar AP (AP1101 not compatible)." (p429-430)

> "Click on Export VPN Settings -> download <VPN Server name>.conf... Transfer the .conf file in /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile... In the Data VPN Setting, select the Data VPN Server(s)... Select Use Tunnel; Enter the Tunnel ID (must be 0)." (p467-497)

## I · 方法论骨架

1. **三件套**：Cirrus 4（Freemium 配 OV2500 / Premium 全云）+ ALE VPN Server 虚机 + Stellar AP（AP1101 不兼容）。
2. **双隧道模型**：管理 VPN（AP↔VPN Server，传 OV2500 管理流量）+ 数据 VPN（L2GRE，传客户端流量回公司网段）。
3. **五步上线**：[PRE] 管理员预录序列号/MAC、VPN 参数、OV2500 地址 → AP 上电自动连 Cirrus 按 MAC 识别 → 下发参数建管理隧道 → 经隧道从 OV2500 拉配置 → 建第二条数据隧道、远程用户接入企业 SSID。
4. **SSID 侧开关**：Default VLAN/Network 选 Use Tunnel + Tunnel ID=0 + 指定 Data VPN Server。

## A1 · 书中案例（Lab 精要）

c10（p467-497）完整流程：Cirrus 4（registration.ovcirrus.com）Inventory > Device Catalog 录序列号/MAC 并勾 Is this a Remote AP=YES；配管理 VPN（公网 IP:6550、Server VPN IP 192.168.0.1、客户端池 192.168.0.2-20、OV2500 IP），Export VPN Settings 导出 .conf；ALE VPN Server 虚机（OVF 部署）设双网卡（eth0 公网/eth1 私网），FileZilla 把 .conf 传到 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile，建 vpn_mgmt 服务导入 endpoint，Apply 后重启 AP，Maintenance > VPN Status 应见 peer 握手；OV2500 虚机加默认路由（192.168.0.0/24 网关 10.130.5.251）；再建数据 VPN（10.7.0.61、客户端池 10.7.0.55-60、端口 6551 绑 eth2），AP Group 的 Data VPN Setting 选中；建 EmployeesX 时选 Use Tunnel、Tunnel ID=0。验证：远程客户端连 EmployeesX 过 802.1X，拿到员工网段地址。

## A2 · 触发场景（含与相邻 skill 的区分）

- 分支/门店/展会/居家需要广播企业 SSID 且流量回总部——用本 skill。
- 站点内 AP 常规上线（局域网内 OV2500 可达）——转 enterprise-mode-onboarding。
- L3 漫游的 GRE 隧道是 home/foreign AP 之间，与本 skill 的 VPN 隧道不同机制，勿混。

## E · 可执行步骤

1. 确认 AP 型号非 AP1101；读尾部标签取序列号/MAC。
2. Cirrus 4 录入设备并勾 Remote AP；配置管理 VPN 参数并 Export VPN Settings 导出 .conf（务必保存好）。
3. 部署 ALE VPN Server 虚机：控制台设 admin 密码、公网/私网 IP、网关/DNS，开 SSH。
4. 把 .conf 传入 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile，建 vpn_mgmt 服务（绑公网 IP:6550）并导入 VPN endpoint，Apply 后重启 AP。
5. OV2500 虚机菜单加去程路由；AP REGISTRATION 选国家码后 RAP 出现在 Managed AP。
6. 建 Data VPN Server（Server IP + 客户端池），导出 .conf 同样导入 VPN 服务器（vpn_data、端口 6551、绑 eth2）。
7. AP Group 的 Data VPN Setting 选中数据 VPN；SSID 的 Default VLAN/Network 选 Use Tunnel、Tunnel ID=0，下发。
8. 验证：远程客户端过 802.1X 拿到企业网段地址，VPN Status 有 peer 与握手记录。

## B · 边界与陷阱

- AP1101 不兼容 RAP。
- Tunnel ID 必须填 0。
- .conf 文件丢失只能重新导出——导出后立即备份。
- Freemium 方案含 OV2500 环节（配置经本地 OV 下发），Premium 少这一步，方案选型影响步骤数。
- 远程站点若有本地出口需求，用 Local Breakout + VLAN 标签区分本地与回传业务。

---
来源条目: f15, c10, g42, g43
