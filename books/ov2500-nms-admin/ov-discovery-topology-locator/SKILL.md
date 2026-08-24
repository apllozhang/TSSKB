---
name: Discovery、拓扑与 Locator 定位
description: 需要把设备批量发现纳管（Discovery Profile）、建拓扑站点/地图、按 IP/MAC/授权用户定位终端（Locator）、或接入第三方设备（自定义 Mibset）时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 新网络要批量发现交换机并纳入 Managed Devices
- 拓扑图缺链路、需要按物理站点组织地图、关键链路想加强监控
- 排障时需要查"某个 IP/MAC/用户现在或历史上接在哪台交换机哪个端口"

## I（核心理念）
Discovery 的核心是 Profile 三段式（General/SNMP/Advanced）+ IP 范围 + Discover Now；拓扑链路靠 AMAP/LLDP 自动发现，关键链路建议手工添加（持久化、down 时显示红色）。Locator 是取证/排障工具，支持 Live 与 Historical 两种检索，命中后可在拓扑图定位。

## A1（行动框架）
1. **建 Discovery Profile**：Network → Discovery → Discovery Profiles → "+"（<<<PAGE 170-172/110-112>>>）
   - General：Name（如 Training）、CLI/FTP 用户（admin/switch）
   - SNMP：SNMPv3、Timeout 5000、Retry 3、User snmpuserv3、SHA+DES、密码
   - Advanced：Trap Station User=admin、Discover Link=Normally、Shell=SSH、GetBulk on、Max Repetitions 10
2. **发起发现**：Managed Devices → Discover New Devices → Start/End IP（192.168.200.0-192.168.200.8）/Mask → 关联 Profile → Create → Discover Now → Finish（<<<PAGE 170-172/113-114>>>）
3. **建拓扑**：Network → Topology → Create Site（Site Name、Street Address、选交换机）→ 选中站点 → Go to Topology → 拖拽排布（<<<PAGE 175-176>>>）
4. **Locator 定位**：Network → Locator → 输入 IP/MAC/授权用户 → Locate（可切 Live/Historical）→ Locate on Map 跳转拓扑；Browse → ADD → Use Picker 选交换机看 MAC 表；视图含 Location/Classification/Data Center/Layer 3（<<<PAGE 187-188/136-137>>>）
5. **第三方设备**：建 Mibset（OID/Display Name/MIB Directory），MIB-2 兜底就填 mib-2；MIB 文件须 .mib 后缀；支持 Web/Telnet/SSH、Custom Icons、Traps、Locator（<<<PAGE 121-123>>>）

## A2（进阶应用）
- 拓扑缺链路时："If a link is not being shown in the map, select the switch and look for the Operations window on the right. Select Poll Device or Poll Link"（<<<PAGE 176>>>）
- 手工链路："Manual links are persistent and displayed in RED when the link goes down. Recommended to configure critical links providing better monitoring capabilities."（<<<PAGE 117-118>>>）
- Ethernet OAM/SAA：可创建/编辑/删除交换机对之间的 SAA，统计 Jitter、RTT、Packet Loss，Dashboard 折线/柱状图展示（<<<PAGE 140-141>>>）

## E（实证案例）
- 创建 Training Discovery Profile 并发现 192.168.200.0 段设备——cases·Discovery Profile（<<<PAGE 170-172>>>）
- 创建拓扑站点与地图，用 Poll Device/Poll Link 补链路——cases·拓扑站点（<<<PAGE 175-176>>>）
- Locator 按 IP 定位并 Locate on Map——cases·Locator（<<<PAGE 187-188>>>）

## B（边界与陷阱）
- 前提是设备侧 SNMP 已配好（见"OmniSwitch 纳管准备"技能）；默认设备不可被管理（<<<PAGE 97/164>>>）
- Advanced 段的 Shell Preference（Telnet/SSH）决定后续 CLI 会话方式，与设备实际配置一致才能用（<<<PAGE 110-112>>>）

## 来源
- frameworks·Discovery 三段式流程（<<<PAGE 110-114/170-172>>>）
- principles·Locator 原理（<<<PAGE 30/136-137>>>）、链路发现机制（<<<PAGE 117-118>>>）、第三方设备支持（<<<PAGE 121-123>>>）、Ethernet OAM/SAA（<<<PAGE 140-141>>>）
- cases·Discovery/拓扑/Locator（<<<PAGE 170-176/187-188>>>）
