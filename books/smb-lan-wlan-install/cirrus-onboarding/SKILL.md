---
name: OV Cirrus 云管设备上线
description: 当需要把交换机或 Stellar AP onboard 到 OmniVista Cirrus 云平台、创建 AP Group/SSID 云侧配置或处理许可订阅时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 交换机/AP 要上云集中管理，需要完成 call-home 激活与 Device Catalog 申报
- Cirrus 侧要建 Site 层级、AP Group、Provisioning 配置并下发 SSID
- 需要购买/导入 OVC 许可订阅

## I（核心理念）
Cirrus 上线是"设备侧 call-home + 云侧申报"的双向握手：交换机的 cloud-agent 周期性（默认 30 分钟）呼叫激活服务器，云侧 Device Catalog 按序列号建档，状态机走到 "OV Managed" 才算完全受管。云管前提是版本：交换机 AOS ≥ 8.9R1、AP AWOS ≥ 4.0.6 GA 且不在排除型号清单内。配置模型三层继承：AP → AP Group → Provisioning Configuration。

## A1（行动框架）
1. 上线前检查前提（P45，<<<PAGE 290>>>）：防火墙开 9093/30123/30124/30125 入站、443/80/123/53 出站；DHCP 标准 option 1,2,6,28,42,43（代理场景另加 129-133,138）；AP 全系支持除 AP1101/AP1201L/H/HL；交换机 AOS 8.9R1+。
2. 交换机上线（C18，<<<PAGE 338>>>–<<<PAGE 346>>>）：
   ```
   -> vlan 1305 name SW-MANAGEMENT
   -> ip interface "int_sw-mgmt" address 10.130.5.5/24 vlan 1305
   -> vlan 1305 members port 1/1/3 tagged
   -> ip static-route 0.0.0.0/0 gateway 10.130.5.7
   -> aaa authentication default local
   -> snmp security authentication all
   -> ntp client admin-state enable
   -> ip domain-name remote-lab.com
   -> ip name-server 9.9.9.9
   -> ip domain-lookup
   -> cloud-agent admin-state enable
   ```
   激活不动时强制重呼：`cloud-agent admin-state disable force` → `cloud-agent admin-state enable`（或 reload）。验证：`show cloud-agent status`（DeviceManaged / Certificate Consistent）。
3. 云侧建档：建 Site/Building/Floor > Device Catalog > Create Device（贴 `show chassis` 序列号）> 等 "OV Managed"。
4. AP 上线（C19，<<<PAGE 352>>>–<<<PAGE 357>>>）：Console（support/aos2016）`showsysinfo` 取 SN > Create Device（Stellar AP）> Create Access Point Group（如 My-AP-Group）> Create Provisioning Configuration（Name/Site/Default RF Profile/Timezone 为必填）> 绑组 > 重启 AP 加速 call-home（`ssudo firstboot -y; ssudo reboot`）> AP CLI `ocloud_show` 验证 VPN connected。
5. 云侧 SSID（F04 四步 + F05 五步）：申报（SN/QR/XLS）→ 分配 AP Group → 下发配置（SSIDs/RF/Rules）→ 确认 OV Managed。SSID 向导：通用设置 → 认证 → 访问策略 → VLAN/隧道 → AP Group 指派与排程（<<<PAGE 282>>>、<<<PAGE 365>>>）。
6. 许可（C29/F13，<<<PAGE 297>>>–<<<PAGE 300>>>）：eBuy 下单（Other Services & Items 填许可号+数量）> Subscription Manager 选 OmniVista CIRRUS > Create a subscription（数量 + 客户唯一名/国家）> 记录 Subscription ID + Order ID > OVC UI 导入。SKU 规则如 OVCX-68-BAS-3Y（等级 BASE/BUSINESS/PREMIUM，年限 1Y/3Y/5Y）。

## A2（进阶应用）
- 激活状态机：Registered > Obtaining Certificate > Assigned > VPN Configuring > Connected to OV > Provisioning > OV Managed；含 Failed To Get Certificate / Factory Reset Required 等失败态（P46，<<<PAGE 314>>>、<<<PAGE 309>>>–<<<PAGE 310>>>）。
- cloud-agent discovery-interval 默认 30 分钟，出错时按此周期重试（P46，<<<PAGE 314>>>）。
- AP Group（Cirrus 版）继承 SSIDs/防火墙/认证/RF 策略，组内可混插任意 AP 型号、上限 10000（P48，<<<PAGE 277>>>、<<<PAGE 329>>>、<<<PAGE 331>>>）。
- 平台容量：最多 12000 台设备（10000 AP + 2000 交换机）（glossary·<<<PAGE 286>>>–<<<PAGE 287>>>）。
- 云管运维：Scheduled Upgrades 四步（Schedule Setting 时长 6h > AP Groups > Set Software Version > Review）；Collect Support Info 一键收集；Golden Config 标记基准配置用于审计漂移（C24，<<<PAGE 451>>>–<<<PAGE 456>>>；glossary·<<<PAGE 439>>>）。

## E（实证案例）
- OS6360 完整上线：管理 VLAN + 静态路由 + NTP/DNS + cloud-agent enable，force 重呼后 `show cloud-agent status` 显示 DeviceManaged（C18，<<<PAGE 338>>>–<<<PAGE 346>>>）。
- Stellar AP 上线：showsysinfo 取 SN > Create Device > 建 My-AP-Group/My-Provisioning-Config > 重启 AP 加速 call-home > ocloud_show 见 VPN connected（C19，<<<PAGE 352>>>–<<<PAGE 357>>>）。
- 云侧 Employees SSID：Create SSID（802.1X + WPA2_AES）> UPAM 建账号 > Network Assignments 绑 My-AP-Group/VLAN 20 > 客户端 PEAP/MSCHAPv2 上线，Authentication Records 查记录（C20，<<<PAGE 390>>>–<<<PAGE 396>>>）。

## B（边界与陷阱）
- cloudagent.cfg 缺失则交换机无法注册 Cirrus；从备份目录恢复：`cp /flash/cirrus/cloudagent.cfg /flash/working/cloudagent.cfg`（CE17，<<<PAGE 338>>>）。
- AOS 低于 8.9R1 的交换机（如 OS2360 AOS 5.2）无法 onboard，只能 CLI 管理（CE16，<<<PAGE 337>>>）。
- AP1101、AP1201L/H/HL 不支持云管；AWOS 需 4.0.6 GA+（CE15，<<<PAGE 290>>>）。
- 不要在 MSP 视图下 Delete 组织，不可恢复（CE10，<<<PAGE 340>>>）。
- eBuy 下单的许可最长 24 小时后才出现在 Subscription Manager（C29，<<<PAGE 297>>>–<<<PAGE 300>>>）。
- 升级窗口内设备重启不可用、所连客户端全部断线，须排业务空闲时段（CE19，<<<PAGE 452>>>）。

## 来源
- case·OV Cirrus 交换机上线全流程（<<<PAGE 338>>>–<<<PAGE 346>>>）
- case·Stellar AP 上线与 AP Group/Provisioning 创建（<<<PAGE 352>>>–<<<PAGE 357>>>）
- case·云侧 Employees SSID（802.1X + UPAM）（<<<PAGE 390>>>–<<<PAGE 396>>>）
- case·云侧 Guests SSID + 踢出客户端（<<<PAGE 418>>>–<<<PAGE 425>>>）
- case·Cirrus 许可订阅创建（<<<PAGE 297>>>–<<<PAGE 300>>>）
- case·计划升级/支持信息收集/设备排障（<<<PAGE 451>>>–<<<PAGE 456>>>）
- framework·Onboarding 四步流程（<<<PAGE 282>>>）
- framework·许可订购与订阅生成（<<<PAGE 295>>>–<<<PAGE 300>>>）
- principle·Cirrus 网络前提（<<<PAGE 290>>>）
- principle·cloud-agent 呼叫机制与激活状态机（<<<PAGE 314>>>、<<<PAGE 309>>>–<<<PAGE 310>>>）
- principle·AP Group 配置继承模型（<<<PAGE 277>>>、<<<PAGE 329>>>、<<<PAGE 331>>>）
- counter·cloudagent.cfg 缺失（<<<PAGE 338>>>）
- counter·OS2360 无法 onboard（<<<PAGE 337>>>）
- counter·AP 型号/AWOS 版本限制（<<<PAGE 290>>>）
