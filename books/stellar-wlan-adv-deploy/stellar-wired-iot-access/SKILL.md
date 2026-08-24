---
name: stellar-wired-iot-access
description: 何时用：要在 Stellar AP 有线口做 MAC 认证接入有线客户端，或要让云管自动识别并管控 IoT 终端时用。
source_book: DT00XTE361EN Stellar WLAN Advanced Deployment
---

# 有线客户端 MAC 认证与 IoT 设备双识别

## R · 原文引用

> "2 – Access Auth Profile Configuration; 1 – AAA Server Profile Configuration; [PRE] – Access Role Profiles Preconfigured; 3 – Access Policy Configuration; 4 – Declare Client MAC address in local database." (p90)

> "MAC OUI: allows devices to be recognized by identifying their MAC addresses. DHCP FingerPrinting... DHCP option 55 (the parameter request list) and option 60 (the vendor identifier)." (p103)

> "In this example: MAC Authentication; Stellar AP port: Ethernet1. AP « Home-AP »" (p90)

## I · 方法论骨架

两条主线：
1. **有线客户端 MAC 认证**（AP 或 OmniSwitch 有线口）：访问角色（Access Role Profile，ARP）是策略落点——ARP_DEFAULT（受限+限带宽）为默认角色、ARP_PASS（全通）为认证通过角色；认证链 = AAA Server Profile（内置 UPAMRadiusServer，用途选 MAC）→ Access Auth Profile（方法 MAC、绑定 AP 组/端口）→ Access Policy（映射条件 Authentication Type=MAC、认证源 Local Database、角色 ARP_PASS）→ 本地数据库录 MAC。
2. **IoT 设备识别与强制**：两招识别——MAC OUI（厂商前缀）+ DHCP 指纹（option 55 参数请求列表 + option 60 厂商标识）；识别结果归入预置或自定义分类，分类可绑定 Access Role Profile 做强制（Enforcement）；未知类型可向 Device Profile 服务查询。

## A1 · 书中案例（Lab 精要）

Lab（p89-98）在 AP "Home-AP" 的 Eth1 口做 MAC 认证：预置两个角色 → 配 AAA Server Profile 指向 UPAMRadiusServer → Access Auth Profile 应用到 AP 组并启用端口 Eth1 → Access Policy 匹配 MAC/Local Database/ARP_PASS/Web 重定向 None → 在 Accounts > Company Property 录入客户端 MAC 11:22:33:44:55:66 → 接上有线客户端验证。监控：Device Catalog > Wired Ports 看端口与 UNP 客户端；Analytics > Clients 看在线/历史有线会话（时间窗最近 1 小时到 1 个月）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 打印机/摄像头/POS 等哑终端要接 AP 有线口或交换机口做准入 → 本 skill MAC 认证流程。
- 要让云管"认得出"终端类型并按类型限速/限权（如 IoT 设备自动套受限角色）→ 本 skill IoT 识别部分。
- 无线终端的身份认证（802.1X/Captive Portal）属于 SSID 策略 → stellar-ssid-advanced；802.1X 失败排障 → stellar-troubleshooting-cli。
- 注意：Access Role Profile（访问角色）与地址解析协议 ARP 同名缩写，本书语境里指访问角色。

## E · 可执行步骤

1. 预置角色：创建 ARP_DEFAULT（受限 ACL+限带宽）与 ARP_PASS（全通）。
2. 配 AAA：Configure > Network Access > Unified Access，AAA Server Profile 指向 UPAMRadiusServer，用途选 MAC。
3. 配认证：Access Auth Profile——认证方法 MAC、选 AAA Profile、默认角色 ARP_DEFAULT，应用到 AP 组并启用目标端口（Eth1）；交换机则选接入端口。
4. 配策略：Access Policy——映射条件 Authentication Type = MAC、认证源 Local Database、角色 ARP_PASS、Web 重定向 None。
5. 录终端：Accounts > Company Property 把客户端 MAC（如 11:22:33:44:55:66）录入本地数据库。
6. 验证：接上有线客户端，Wired Ports / Analytics > Clients 查看会话与角色。
7. IoT 侧：在 OmniVista 开启设备画像，按 MAC OUI + DHCP 指纹核对识别分类，把分类绑定到目标 Access Role Profile 实现自动强制。

## B · 边界与陷阱

- 角色顺序别配反：未认证终端落在 ARP_DEFAULT，认证通过才升到 ARP_PASS；默认角色给了全通就失去准入意义。
- DHCP 指纹依赖终端发 DHCP：静态 IP 的哑终端只能靠 MAC OUI 识别。
- MAC 认证可被 MAC 仿冒，安全要求高的场景应升级到 802.1X。
- IoT 分类绑定 ARP 强制后策略即时生效，误分类（如把正常终端归入受限类）会直接断业务，先小范围验证。

---
来源条目: f05, c03, p11, g09, g10, g11, g12, g25, g26, g27
