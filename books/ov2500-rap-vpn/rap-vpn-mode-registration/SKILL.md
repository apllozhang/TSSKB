---
name: rap-vpn-mode-registration
description: 何时用：规划 ALE 远程 AP（RAP）方案时选 OVE 全隧道还是 OVC 仅数据隧道，并完成版本核对、Freemium 账号与 Device Catalog 注册。
source_book: OV2500 4.9R2 RAP and VPN VA Installation
---

# RAP VPN 模式选型与注册规划

## R · 原文引用

> "A Remote Access Point (RAP) is an AP with a management tunnel and a data tunnel to a remote OmniVista Enterprise (OVE) Server. An OmniVista Cirrus (OVC) Managed AP is technically not considered a RAP since there are no Management VPN Server details to be configured. An OVC managed AP already uses an OpenVPN connection for Management communications with a VPN Server in the OVC Cloud infrastructure. However, it is possible that an OVC Managed AP might need a Data VPN Tunnel to a VPN Server in the Enterprise." (p4)

> "1. The first connection, out-of-the-box, is to the OVC Device Registration Server. It retrieves the setup parameters for RAP including the OVE IP to which it will connect. 2. The keys and parameters are exported to the RAP VPN Server at corporate HQ. 3. The RAP then establishes a Wireguard VPN tunnel over which it connects to be managed by OVE." (p4)

> "ESXi versions 6.5, 6.7, 7.0.2, 8.0 are supported (ESXi 5.5 is not supported). Hyper-V 2016, 2019, and 2022. Supported Stellar RAP version is AWOS 5.0.2 and higher. RAP VPN VA version 4.9.2.2." (p5)

> "Server's VPN IP - The VPN Server's Private IP address within the virtual network (must be in the same network as the client pool). ... Client VPN IP Address Pool - The range of addresses available to assign to Remote APs." (p10-11)

## I · 方法论骨架

1. **第一道分岔——管理模式决定隧道数量**：AP 由企业本地 OVE 管理 → 真 RAP，需管理隧道（WireGuard）+ 数据隧道两条 VPN；AP 由 OVC 云管理 → 技术上不算 RAP，管理通道走 OVC 云内 OpenVPN，仅在数据流量需回传总部时才另建 Data VPN。
2. **可达性判断**：本地 AP 经 DHCP option 138 拿到 OV 地址直接管理；远程站点 AP 对企业 OV 不可直达，连接与管理通信必须走 VPN 隧道。
3. **版本前置核对**（任何一项不满足即返工）：ESXi 6.5/6.7/7.0.2/8.0（5.5 排除）；Hyper-V 2016/2019/2022；AWOS 5.0.2+；VPN VA 4.9.2.2（与 OV2500 4.9R2、OVC 4.9.2 认证配套）；另支持 Ubuntu 22.04 LTS + KVM。
4. **注册顺序约束**：先建 OmniVista Cirrus Freemium 账号 → 先确定 VPN Server 四参数再往 Device Catalog 加 AP → 加 AP 时预置 VPN VA 公网 IP / OVE 内网 IP / Security Keys。
5. **四个 VPN Server 参数语义**：Public IP = 公网出口；Port = 公网端口；VPN IP = 虚拟网络私网 IP，必须与客户端池同网段；Client VPN IP Pool = 分给 RAP 的地址段。

## A1 · 书中案例

- OVE 模式五步：开箱首连 OVC Device Registration Server 取回 RAP 参数（含 OVE IP）→ 密钥导出到总部 RAP VPN Server → 建 WireGuard 管理隧道接受 OVE 管理 → OVE 上配 Data VPN 隧道并导密钥 → 数据隧道承载业务。
- OVC 模式四步：开箱首连注册服务器确认 → AP 建 OpenVPN 连接由 OVC 管理 → OVC 配 Data VPN 隧道并导出密钥到总部 → 隧道承载业务。
- Device Catalog 加 AP 时要填"第 3 步才部署"的 VPN Server 信息——先定 Server 再开工，否则顺序颠倒隧道建不起来。
- CSV 批量导入：模板中 RAP 字段必须为 TRUE 才携带 VpnSettingName。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户要做居家办公/分支 AP 回连方案，问"选哪种模式""要不要 Management VPN Server""AP 怎么注册"；或在老 hypervisor 上规划部署前核对版本。
- 与 `vpn-va-deploy-capacity` 的区分：本 skill 只做**选型与注册规划**（纸面设计 + Device Catalog 操作）；选定模式后虚拟机怎么装、网卡怎么配、给多少资源，转部署 skill。
- 与 `rap-data-tunnel-config` 的区分：本 skill 不碰隧道 SSID、Data VPN Server 界面配置与设置文件导出。

## E · 可执行步骤

1. 判断管理模式：远程 AP 归 OVE 管 → 规划两条隧道（WireGuard 管理 + L2GRE 数据）；归 OVC 管 → 规划零或一条隧道（仅数据回传时建 Data VPN）。
2. 核对版本矩阵：ESXi 6.5/6.7/7.0.2/8.0 或 Hyper-V 2016/2019/2022 或 Ubuntu 22.04+KVM；AWOS ≥5.0.2；VPN VA 4.9.2.2 配 OV2500 4.9R2 / OVC 4.9.2。
3. 注册 registration.ovcirrus.com 建 Freemium 账号（验证邮件来自 noreply@ovcirrus.com，正文含设备 OS 下载链接）。
4. 先定 VPN Server 四参数（Public IP / Port / VPN IP 与客户端池同网段 / Client Pool），再到 Network→Inventory→Device Catalog 加 AP 并预置 Security Keys；首次 VPN Settings 用 Create New，后续 AP 用 Choose Existing 复用。
5. 批量场景：下载 CSV 模板，确认 RAP 列 = TRUE 后导入。

## B · 边界与陷阱

- **ESXi 5.5 明确不支持**（ce01）——老环境迁移前先升级 hypervisor。
- **AWOS 版本文档内三处口径打架**：前置条件 5.0.2+（p5-6）、Freemium 邮件写 5.0.1（p7）、SSID 界面写 4.0.1（p71，疑笔误）；交付按最严的 5.0.2+ 核对（ce11）。
- **CSV 里 RAP 列 FALSE/留空**：导入看似成功但 AP 不带隧道配置（ce12）。
- OVC 管理的 AP 不配 Management VPN Server——别照 RAP 流程多配一条管理隧道。

---
来源条目: p01, p02, p03, p04, ce01, ce11, ce12, g01, g02, g03, g05, g06, g10, g11, g12, g13, g14
