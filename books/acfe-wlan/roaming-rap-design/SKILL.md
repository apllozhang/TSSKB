---
name: roaming-rap-design
description: 何时用：规划 L2/L3 漫游与 802.11r/OKC 快速漫游、处理粘滞客户端与静态邻居，以及 RAP 远程接入点双隧道部署。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# 漫游设计与 RAP 远程接入

## R · 原文引用

> "Check the roaming conditions ... Based on the VLAN ID between the 'home' and 'foreign' AP, select either: Layer 2 Roaming (default) / Layer 3 Roaming ... OKC can be enabled with WPA2/WPA3 Enterprise only; 802.11r (Fast Roaming) can be enabled with WPA/WPA2 encryption only (Personal or Enterprise)" (p489)

> "Client Context exists on the new AP? / WLAN service and Access Role Profile exist ...? / Client Context VLAN ID = VLAN ID mapped to the ARP on the new AP? — Yes/Yes/Yes → L2 Roaming; Yes/Yes/No → L3 Roaming; No → No Roaming, new client" (p476)

> "[PRE] – Settings to be Entered by the Administrator: 1 – Stellar Access Point Startup & Registration; 2 - VPN & OmniVista 2500 Settings Retrieval; 3 - VPN Tunnel (Management Traffic) Establishment; 4 – Configuration Settings Retrieval; 5 – VPN Tunnel (Clients Traffic) & Client Connection" (p499)

## I · 方法论骨架

**1. 漫游默认状态**
- L2 漫游：恒开；L3 漫游：默认关，SSID 配置里开（home/foreign AP 间 L2 GRE 隧道）
- Fast Roaming：默认关，按 SSID 开

**2. L2/L3 判定表（三条件）**

| 上下文存在 | WLAN service/ARP 存在 | 上下文 VLAN=新 AP 映射 VLAN | 结果 |
|---|---|---|---|
| 否 | — | — | 不漫游，按新客户端 |
| 是 | 否 | — | 不漫游，按新客户端 |
| 是 | 是 | 是 | L2 漫游 |
| 是 | 是 | 否 | L3 漫游（GRE 回 home AP） |

典型触发：同一 SSID 在不同 AP Group 映射了不同 VLAN。上下文的 Add/Del 消息在"新 AP 不属同一 OVC / 无相同 WLAN service"时被丢弃。

**3. 快速漫游协议前提**
- OKC：仅 WPA2/WPA3 Enterprise
- 802.11r（FT，省 RADIUS 重认证）：要求 WPA2/WPA3 加密（Personal 或 Enterprise）
- 规划顺序：先按 VLAN 选 L2/L3，再按 SSID 安全级别选快漫游协议，最后 Heat Map 分频段核对覆盖重叠。

**4. 粘滞客户端组合拳**
Roaming RSSI Threshold（范围 0-100；推荐 2.4G=10、5G=15）+ 802.11v（给漫游目标）+ 802.11k（引导到最优 AP）。语义区分：关联阈值管"能不能连"，漫游阈值管"何时该走"。地理相邻但空口互不可见（直角走廊）→ 两台 AP 互加静态 Neighbor AP，上下文改走 LAN。

**5. RAP 五步上线时序**
预置三段管理面配置后，AP 上电自动：序列号向 Cirrus 注册 → 取回 RAP 模式/VPN 公网地址/客户端池/OV2500 地址 → 建管理 VPN 隧道 → 从 OV2500 拉配置 → 建第二条客户端数据 GRE 隧道。

管理面三段：
1. Cirrus：建 RAP 专用组织（trial 选 RAP=Yes）→ 声明序列号 → Mgmt VPN Settings（Server 公网 IP/端口、Server VPN IP、OV2500 IP、客户端池）→ 导出 .conf
2. VPN Server 虚机：双网卡（公网/私网）→ .conf 上传 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile → Network Services 建 vpn_mgmt → endpoint 导入应用
3. OV2500：加回程路由 → 发现 RAP → 建 Data VPN Server（新 .conf 二次导入，绑 vpn_data）→ 挂到 AP Group → 建 SSID 选 Use Tunnel（Tunnel ID=0）
参考地址（实验）：vpn_mgmt 192.168.0.1 / 池 .2-20；vpn_data 10.7.0.61 / 池 .55-60；OV2500 10.130.5.50。

## A1 · 书中案例（Lab 步骤精要）
- **c21/p549-572**：RAP-Organization + Mgmt VPN → OVF 部署 VPN Server VA（admin 密码、双 NIC、SSH 6550、FileZilla 传 .conf）→ endpoint Apply → AP 重启建管理隧道（VA 控制台 VPN Status 见 peer/握手/字节）→ OV2500 控制台 [8]Configure Route 加 192.168.0.0/24 网关 10.130.5.251 → AP Registration 发现 RAP → Data VPN（导出第二个 .conf，端口 6551，绑 eth2）→ SSID（WPA3_AES + Use Tunnel）→ 远端 Windows 连 EmployeesX 拿员工网段地址。

## A2 · 触发场景（含与相邻 skill 的区分）
- 用户拿着终端移动出现断线/重认证/粘住旧 AP，或要把企业网延伸到门店/展会/家庭办公（RAP）时用。
- **区分**：单纯信号差/覆盖洞 → `site-survey-troubleshooting`；RF 参数阈值类调优 → `rf-optimization-baseline`；本 skill 管"跨 AP/跨站点的移动性与远程接入"。

## E · 可执行步骤
1. 规划漫游域：同一漫游域的 AP 必须同一 OVC 管理、同一 SSID/WLAN service；AP Group 间 VLAN 映射差异要有意识设计（它决定 L2/L3）。
2. 按 SSID 安全级别核快漫游前提（OKC=Enterprise；11r=WPA2/WPA3 加密），开放 Guest 只能普通漫游。
3. 粘滞客户端：设 Roaming RSSI（2.4G=10/5G=15 起步）+ 开 11k/v，用客户端会话历史漫游时间线验证。
4. 走廊直角等互不可见场景：两台 AP 互加静态 Neighbor AP。
5. RAP：避开 AP1101 → Cirrus 建专用组织+Mgmt VPN 导出 .conf → VA 部署导入 → OV2500 加回程路由+Data VPN → SSID Use Tunnel（Tunnel ID=0）→ VPN Status 确认 peer 后远端验证。

## B · 边界与陷阱
- 跨 OVC/无相同 WLAN service → Add/Del 消息被丢弃，漫游退化为全新接入（重认证重取 IP）（ce31）。
- Roaming RSSI 两难：太低粘滞拖垮吞吐，太高频繁切换丢包；从推荐值起步（ce30）。
- 地理相邻互不可见=无漫游；Heat Map 分频段核对（2.4/5/6G 覆盖不同）（ce29）。
- RAP 三坑：AP1101 不兼容；导出的 .conf 必须留存（要导入 VPN Server VA）；OV2500 不加回程路由 RAP 发现不了（ce34）。
- L3 漫游走 GRE 隧道回 home AP，路径长、依赖隧道健康，非必要不制造 VLAN 不一致。

---
来源条目: f18, f24, p56, p57, p58, p59, p60, c21, ce28, ce29, ce30, ce31, ce34 · 术语锚点: g28, g29, g31, g02, g03, g04, g44, g32, g14
