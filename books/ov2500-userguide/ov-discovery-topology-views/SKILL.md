---
name: 设备发现、四级轮询与拓扑视图
description: 需要执行设备发现（Range + Discovery Profile）、管理 Managed Devices 条目与设备操作集（Ping/Trap/Backup/Reboot）、配置四级自动发现轮询、构建 Topology 三层地图/Geo 站点/手工链路、用 Locator 定位终端时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- 新交换机批次要纳管：配 IP 范围、SNMP 凭据、Discover Now
- 拓扑图缺链路/设备状态不对，要 Poll Links 或查轮询档位
- 要按楼层/站点组织地图、给核心链路做手工链路监控
- 查"某个终端现在插在哪个口"（Locator）

## I（核心理念）
发现 = Range（IP 范围）× Discovery Profile（凭据/协议参数，多档案按序回退）。自动发现按四级轮询（Full ⊇ Occasional ⊇ Regular ⊇ Frequent，间隔随网络规模分档）持续更新。Topology 是三层地图体系：Physical Network Map（自动、不可删）→ Child Map → Logical Map，外加 Dynamic Map（过滤器驱动）；Geo Map 是默认视图，站点（Site/Sub-Site）自动生成同名逻辑图。Locator 一切搜索最终归结为 MAC。

## A1（行动框架）
1. **首次纳管五步法**（cases·C1，<<<PAGE 40-44>>>）：Discovery→Discover New Devices 输 IP 范围（可用 Default Profile）→Managed Devices 里 Edit 修正主 IP/write community/CLI-FTP 凭据/SNMP 版本→Notifications 配 trap（Topology 需 coldStart/warmStart/linkUp/linkDown）→Copy Working/Running to Certified 保存→需 QoS 时跑 PolicyView 后再保存
2. **地图体系选型**（frameworks·F14，<<<PAGE 580-581>>>）：Physical Network Map 全网自动建；从父图建 Child Map（设备从父图移入）；Logical Map 无父图、设备可同时在多图；Dynamic Map 用过滤器动态加减（不能与 Logical 互转）；Admin 建删图、Netadmin/Write 编辑；大图减少设备可提升渲染性能
3. **轮询档位**（principles·P85，<<<PAGE 298-299>>>）：规模 Low(≤500)/Medium/High/Very High 对应 Full 8/10/12/18 小时、Occasional 4/6/8/12h、Regular 1/2/4/8h、Frequent 5/15/30min/2h

## A2（操作步骤）
- **执行发现**：Discovery→Managed Devices→Discover New Devices→Ranges List：现有 Range 直接 Discover Now 或 Add 新建（Start/End IP/Subnet Mask + 勾选 Discovery Profiles，可拖拽排序）→完成后设备入 Managed Devices；更新单台用 Rediscover（cases·C26，<<<PAGE 256>>>）
- **手工添加/克隆/多选编辑**：Add 填 General(IP/Site/CLI-FTP 凭据)+SNMP+Advanced(Trap Station User/Discover Link/Shell Preference/Get Bulk)；Clone 后改 IP 密码；多选编辑用 Click to Overwrite 统一赋值、Retain Original Values 反悔（cases·C27，<<<PAGE 257-261>>>）
- **设备操作集**：Ping/Poll For Traps/Poll Links/Configure Health Thresholds/Locate End Stations/Webpage/Device Inventory/Backup Device/SSH/SSH Custom(SecureCRT)/Configure Traps/View Traps/Reboot(选目录+延迟)/Copy Working↔Certified/Save to Running/Scheduled Upgrades（cases·C28，<<<PAGE 262-264>>>）
- **MIB 导入**：先在 Third-Party Devices Support 建 OID 条目（只填 enterprises 后段）→Import MIBs→Upload Files→箭头调编译顺序→Apply（cases·C31，<<<PAGE 288>>>）
- **Network Advisor 启用**：先在 Global Dashboard 的 NA widget 声明实例（Name/URL/Application UUID）→选设备→Features→Enable→选实例（cases·C30，<<<PAGE 264-267>>>）
- **手工链路**：持久显示、断链变红，适合核心链路监控；自动链路不可达时从拓扑消失（principles·P83，<<<PAGE 290>>>）
- **Locator 定位**：Search by IP/Host Name、MAC、Auth User→Historical/Live 切换（Live 可 1st Match Only/All Matches）→看 ARP 表 + Netforward 表；行内 Action 可 Locate On Map/Quarantine Manager/端口启停（cases·C35，<<<PAGE 337-339>>>）
- **状态颜色**：设备绿=Up（AOS 的 Up 不代表可管理，看 SNMP Status）/橙=Warning/红=不可达；通知圈橙 Warning/紫 Minor/黄 Major/红 Critical；ping sweep 后链路等下次轮询或手动 Poll Links（principles·P156，<<<PAGE 554-561>>>）
- **SPB/ERP 专题视图**：均在交换机 CLI 配置、OV 只读展示；SPB 数据每 3 小时自动轮询；ERP 按 Ring ID 过滤（principles·P157，<<<PAGE 565-574>>>）
- **Geo 站点**：Site 自动生成同名逻辑图；Sub-Site=Building/Floor；设备只属一个 Site/Sub-Site；推荐先建空 Site 再建 Sub-Site 时分配设备（principles·P158，<<<PAGE 575-578>>>）

## E（实证案例）
- 首次纳管设备五步法全流程（cases·C1，<<<PAGE 40-44>>>）
- Range+Profile 执行发现（cases·C26，<<<PAGE 256>>>）
- SecureCRT 作为 SSH Custom 客户端（cases·C29，<<<PAGE 268-270>>>）
- Locator 定位终端 + Netforward 多视图（cases·C35，<<<PAGE 337-339>>>）

## B（反例/坑）
- IP 范围不得含广播地址：划了子网就一子网一个 Range（principles·P71，<<<PAGE 255>>>）
- 多 VLAN 设备发现时主 IP 可能选错（第一个响应 ping 的 IP），需手工 Edit 修正（principles·P4，<<<PAGE 42>>>）
- write community 发现后默认 public，且不能从 OV 改——只能登录交换机本端配（principles·P5，<<<PAGE 42>>>）
- CLI/FTP 凭据只用于 FTP，不用于 Telnet（principles·P6，<<<PAGE 43>>>）
- 重新发现不会用新档案参数覆盖已录入的设备级参数（principles·P72，<<<PAGE 256>>>）
- 手工添加 Down 状态的 Stellar AP 会占用第三方 License 且 AP Up 后无法释放——正确做法走 AP Registration 的 Unmanaged 页签（counter·X29 / principles·P73，<<<PAGE 257-258>>>）
- REST API 轮询凭据错误会引发 trap 风暴（counter·X30 / principles·P86，<<<PAGE 300>>>）
- Discovery 设备可见性按用户角色过滤：非 Admin/Netadmin 只看到其角色关联地图里的设备（principles·P70，<<<PAGE 255>>>）
- Locator Live Search 不轮询 Stellar AP（找不到其客户端）；仅支持 IPv4（principles·P95，<<<PAGE 336-339>>>）
- 自定义 Netforward 视图每用户最多 2 个，新建替换旧的（principles·P96，<<<PAGE 341>>>）
- MIB 导入后不立即解析——发现对应 OID 设备或重启服务器时才解析（principles·P81，<<<PAGE 287-288>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 12 章 Discovery（<<<PAGE 255-301>>>）、第 18 章 Locator（<<<PAGE 336-349>>>）、第 31 章 Topology（<<<PAGE 554-587>>>）、入门章（<<<PAGE 40-44>>>）。条目来源：frameworks F14；cases C1/C26-C31/C35；principles P4-P8/P70-P86/P95/P96/P101/P156-P158/P160；counter-examples X29/X30。
