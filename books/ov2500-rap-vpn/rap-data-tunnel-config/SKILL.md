---
name: rap-data-tunnel-config
description: 何时用：VPN VA 就绪后配置 Data VPN 隧道、导入设置文件、配隧道 SSID 与 Local Breakout 路由及下行口认证。
source_book: OV2500 4.9R2 RAP and VPN VA Installation
---

# 数据隧道配置：设置文件、SSID 与 Local Breakout

## R · 原文引用

> "SFTP the VPN Settings File (e.g., LAB4.conf) to the vpn_profile Directory (/opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile) on the VPN VA. ... Important Note: Do not change the name of the VPN Settings file. ... Any time you modify VPN settings you must generate a New VPN Settings File and FTP the file to the VPN Server." (p62-63)

> "Go to Network –> AP Registration -> Data VPN Server to add a Data VPN Server. ... Assign the Data VPN Server to the AP Group (mandatory to set up the Data VPN Tunnel). ... An L2GRE tunnel will be created between the Remote AP and the VPN Server." (p67-68)

> "Use Tunnel: checked; Tunnel ID: 0; GRE Tunnel Server IP Address/data VPN Server: select profile created at previous section; Support of Entropy: Disabled; Allow Local Breakout: Disabled" (p71)

> "only one VLAN inside the tunnel (tunnel ID must be set to 0) can be enabled with Local Breakout. ... The static routes specified will be accumulated on an AP across all SSIDs assigned to the AP." (p73-74)

## I · 方法论骨架

1. **设置文件生命周期**：Device Catalog/Data VPN Server 界面导出（AP 入目录即可，无需 Registered）→ SFTP 上传到 vpn_profile 目录 → 文件名不可改 → 任何配置变更或加 AP 都必须重走"导出→上传→VA 重配"。
2. **两步服务绑定**：先建 VPN Service（绑公网 IP 网卡 + 端口），再建 VPN Endpoint 挂设置文件；管理隧道接口选 None，数据隧道选无 IP 桥接网卡（eth2）。
3. **Data VPN 五步链**：建 Data VPN Server → 绑 AP Group（必做，不绑隧道建不起来）→ 导出文件 → SFTP 上传 → 配服务与端点。
4. **隧道 SSID 参数块**：Use Tunnel 勾选、Tunnel ID=0、选 Data VPN Server profile、WPA3_AES、Entropy 禁用、Local Breakout 默认禁用。
5. **Local Breakout 路由三红线**：单 VLAN + Tunnel ID 0；路由跨 SSID 累积、子网唯一；隧道 VLAN 网段禁手工配路由。
6. **调参表**：DS-Lite 场景按表改 TCPMSS/MTU；License 门槛：下行口认证需 Premium/Business。

## A1 · 书中案例

- 设置文件样例：LAB4.conf 内含全部 RAP 对端的 WireGuard PublicKey 与 AllowedIPs（如 10.180.2.7/32），按 VPN Settings Name 命名。
- 五步链样例：Data VPN Server 参数 Name/公网 IP/Port/VPN IP（与客户端池同网段）/Client Pool；导出文件含 192.168.1.2/32 样例；最终 RAP↔VPN Server 间建立 L2GRE 隧道承载员工数据流量。
- 路由累积样例：SSID1 用 T1 配路由 A/B、SSID2 用 T2 配 C/D，则 A/B/C/D 对两个 SSID 都生效。
- Local Breakout DNS 故障样例（p83-84）：AP 双 DNS 随机选用致 OVC 掉线；客户端 DNS 192.168.10.177 命中 192.168.10.0/24 路由被送进隧道变慢；解法统一为配正确的总部 DNS。
- 1201H 下行口隧道化：Tunnel Profile → Access Role Profile（Map to VLAN and Tunnel）→ Access Auth Profile，应用到 AP/AP Group。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：VA 部署完成（`vpn-va-deploy-capacity` 已就绪），要打通数据隧道：建 Data VPN Server、导出/上传设置文件、配 SSID 走隧道、开 Local Breakout，或 1201H 下行口认证。
- 与 `vpn-va-deploy-capacity` 的区分：那边管虚拟机与网卡；本 skill 从"VA 上的 VPN 服务与 OV 侧隧道配置"开始。
- 与 `rap-vpn-troubleshooting` 的区分：这边是正向配置；隧道建不起来、客户端拿不到 IP 转排障 skill。
- 与 `rap-vpn-mode-registration` 的区分：模式与注册参数已在规划期确定，本 skill 直接消费那些参数。

## E · 可执行步骤

1. 建 VPN 服务：Network Services→Configure a Network Service→VPN，命名 vpn_management / vpn_data，绑公网 IP 网卡 + 端口。
2. 建 Data VPN Server：Network→AP Registration→Data VPN Server，填四参数（VPN IP 与客户端池同网段）。
3. 绑 AP Group：Network→AP Registration→AP Group 编辑并绑定 Data VPN Server（必做）。
4. 导出设置文件：AP 加入 Device Catalog 即可 Export VPN Settings（无需等 Registered）；SFTP 到 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile，**不改名**。
5. 配 VPN Endpoint：挂设置文件到服务；管理隧道接口选 None，数据隧道选无 IP 的 eth2；Apply Configuration Changes。
6. 配隧道 SSID：Use Tunnel 勾选、Tunnel ID=0、选 Data VPN Server profile、Allowed Band=All、WPA3_AES、Support of Entropy 禁用；RADIUS 认证（如 UPAMRadiusServer）；关联 AP Group 后 OV2500 自动推送。交换机侧 VLAN：AOS 8.x `vlan [n] member port [p] tagged/untagged`；AOS 6.x `vlan [n] 802.1q [p]` / `vlan [n] port default [p]`。
7. 开 Local Breakout（如需）：确认 Tunnel ID=0 且隧道内仅一个 VLAN 开启；配静态路由避开三红线（见 B）。
8. DS-Lite 调参（如需）：管理 TCPMSS 1380/1352、数据 TCPMSS 1380/1300、MTU 1500/1546/1376；入口分别为 Freemium VPN Servers、Data VPN Server、WLAN→SSIDs 界面。
9. 下行口认证（如需）：确认 Premium/Business 账号 → Tunnel Profile → Access Role Profile → Access Auth Profile 应用到 AP/AP Group（最多 Eth1-Eth3 三口）。

## B · 边界与陷阱

- **设置文件三类失效**（ce04）：手工改名致 VA 识别失败；改配置不重传致 VA 用旧配置；导出后又加 AP，新公钥不在旧文件，必须重走导出→SFTP→重配全流程。管理与数据隧道文件同规则。
- **AP Group 不绑 Data VPN Server = 隧道建不起来**（p68 明确 mandatory）。
- **Local Breakout 路由三雷**（ce07）：为隧道 VLAN 网段手工配路由（AP 自动生成，再配致混乱/性能下降）；跨 SSID 重复同一目的子网；路由与 AP 本地网段重叠（AP 访问本地网的包被推进隧道发往总部，AP 与本地网失联）。
- **Local Breakout DNS 三故障**（ce10）：AP 双 DNS 随机选用可能掉出 OVC；客户端 DNS 命中 Breakout 网段绕道隧道变慢；本地无该 DNS 或拿到异地运营商 DNS（如 219.141.136.10）。解法：配正确的总部 DNS。
- SSID 界面"AWOS 4.0.1 支持 Local Breakout"疑为文档笔误，按 AWOS 5.0.2+ 最严口径核对（ce11）。
- 下行口认证仅 Premium/Business 账号、仅 AP1201H/1201HL/AP1311；组内不支持的 AP/端口自动忽略（p75）。

---
来源条目: p12, p13, p14, p15, p16, p17, p18, ce04, ce07, ce10, g07, g08, g09, g15, g18, g19, g20
