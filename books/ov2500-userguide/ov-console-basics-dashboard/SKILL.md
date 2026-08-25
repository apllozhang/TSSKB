---
name: OV2500 控制台入门与仪表盘定制
description: 需要了解 OmniVista 2500 4.9R2 的应用菜单结构（LAN+WLAN / WLAN 两种视图）、定制 Dashboard 与 Widget、配置表格过滤器/Favorites、告警底栏、用户/用户组与 2FA 权限时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- 第一次登录 OV2500，不知道"某个功能在哪个应用里配"
- 要把常用的 Analytics 图表、告警摘要放到首页 Dashboard
- 不同角色（netadmin / writer / user）的访问权限划分、2FA 开关
- 表格数据太多，要建可复用的过滤器

## I（核心理念）
OV2500 是按 GUI 菜单 A-Z 组织的参考型网管平台：两种菜单视图（LAN+WLAN Menu / WLAN Menu）内容相同、仅入口重组；首页 Dashboard 是 Widget 容器（Global / WLAN Advanced / IoT / Performance Monitoring 四标签）；所有页面底部有 Unacknowledged Alarm 实时告警栏；权限由 用户组 × 用户角色（地图×应用读写×VLAN 对象）三维度叠加决定。

## A1（行动框架）
1. **找功能先看总地图**：Network（Discovery/Topology/AP Registration/SAA/Locator/Notifications/VM Manager/Analytics/Application Visibility/Provisioning/IoT）、Configuration（VLANs/Services/VXLANs/IP Multicast/CLI Scripting/PolicyView/SIP/Captive Portal/Groups…）、Unified Access、Security（含 Quarantine Manager）、Administration（Control Panel/Preferences/Audit/License/OV System Health）、UPAM、WLAN 共七大区（frameworks·F1，<<<PAGE 31-32>>>）。无线团队可切 WLAN Menu 视图：SSID/APs/Analytics/Clients/IoT/Guest-BYOD/Authentication/Policies/RF/Security/Alarms-Logs/Administration 分组，内容与 LAN+WLAN 相同（<<<PAGE 33-34>>>）
2. **Dashboard 按标签定制**：Performance Monitoring 标签挂 Analytics Chart View Profile 图表（最多 20 个 widget，删 Profile 则 widget 一并移除）（frameworks·F2，<<<PAGE 45, 54-56>>>）
3. **权限规划**：预置 admin（Account Admin，唯一能改用户/组，密码 switch，必须改）/netadmin/writer/user 四账号；User Role = 可访问地图 × 应用读写 × VLAN/VXLAN 对象限制三维度，可多角色叠加（principles·P187/P188，<<<PAGE 780-808>>>）

## A2（操作步骤）
- **添加/删除/布局 Widget**：Settings 图标→Add Widget→列表选一个→OK（一次只能加一个，加到左上角）；删除点 widget 右上角 x；布局 Settings→Change Layout，默认 Auto（cases·C2，<<<PAGE 34-36, 52-53>>>）
- **Widget 刷新率**：最小与默认均为 5 分钟（principles·P1，<<<PAGE 37>>>）
- **Favorites**：应用快捷方式加入 Favorites Widget 后同步出现在主导航 Favorites 标签（<<<PAGE 36>>>）
- **自定义表格过滤器**：点 filter 按钮→Add→Filter Name→条件严格度 ANY/ALL→have/not have + contains/begins with/ends with/equal/not equal→大小写敏感开关；可加新条件或新条件组（cases·C3，<<<PAGE 38>>>）
- **Table View vs List View**：List View 不能用 Print 按钮打印，打印前须切 Table View（principles·P2，<<<PAGE 37, 39>>>）
- **用户设置**：User Settings 任何用户可改（Locale/主题/超时/温度单位/Device Naming/颜色/声音），System Settings 需 Account Admin；Inactivity Timeout 15 分钟~25 周默认 15；声音 .wav/.mp3 ≤500KB（principles·P118，<<<PAGE 416-420>>>）
- **2FA**：Google Authenticator 六位时间码，按 Role 启用；仅能全局启用/禁用，Verify 卡住用 Reset 2FA（principles·P187/P188，<<<PAGE 780-808>>>）
- **Watchdog 启停 OV 服务**（运维入门）：Control Panel→Watchdog 滑块启停单个服务（连带依赖）；停 ActiveMQ/Tomcat 会关掉 Web 须手工恢复（cases·C24，<<<PAGE 249-250>>>；principles·P68）

## E（实证案例）
- Dashboard 增删 widget 与 Change Layout 全流程（cases·C2，<<<PAGE 34-36, 52-53>>>）
- 自定义表格过滤器（ANY/ALL + 多条件组）（cases·C3，<<<PAGE 38>>>）
- Watchdog 批量 Start All/Restart All（cases·C24，<<<PAGE 249-250>>>）

## B（反例/坑）
- List View 数据打印不出来——不是故障，是设计如此，切 Table View（principles·P2，<<<PAGE 37, 39>>>）
- 大表（如 VLANs）默认不显示数据：需用 Device Selection Bar 选设备；选择结果在会话内持久、登出复位（principles·P3，<<<PAGE 40>>>）
- admin 默认密码 switch、四个预置账号默认密码全部为 switch，至少要改掉（principles·P187，<<<PAGE 780-789>>>）
- admin 用户不可删、Administrators/Default 组不可删、系统 Role 不可改（principles·P188，<<<PAGE 790-808>>>）
- 用户属多组时权限取最高特权组，不是叠加投票（principles·P188，<<<PAGE 790-808>>>）
- Stellar AP 的 Unsaved 变更告警无害——AP 重启自动取最新配置，可在 Settings 关闭该通知（principles·P11，<<<PAGE 31, 46>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 1-2 章（<<<PAGE 31-64>>>）、Control Panel 章（<<<PAGE 249-253>>>）、Users/User Groups 相关（<<<PAGE 780-808>>>）。条目来源：frameworks F1/F2；cases C2/C3/C24；principles P1/P2/P3/P11/P68/P118/P187/P188。
