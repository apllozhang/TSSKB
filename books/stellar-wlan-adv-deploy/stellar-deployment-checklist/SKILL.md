---
name: stellar-deployment-checklist
description: 何时用：从零交付一套 Stellar 云管 WLAN（多 SSID/RF/安全/运维全项）或逆向拆除清理组织时，当交付 checklist 用。
source_book: DT00XTE361EN Stellar WLAN Advanced Deployment
---

# 全流程部署综合演练（交付 checklist）与组织清理

## R · 原文引用

> "The purpose of this exercise is to practice on Stellar Access Points and OmniVista Cirrus by working on a WLAN Stellar installation... You will be in charge to install and configure the network based on the given requirements." (p288)

> "As OmniVista Cirrus 10 is cloud-based, it is not possible to revert the configuration back to the default parameters with one click." (p315)

> "The AP Group can only be deleted if no custom provisioning configuration is assigned. ... If you get an error while trying to delete it, Edit this profile and set the RF profile parameter with 'Default RF Profile'." (p316)

> "This topology contains: clients, Stellar Access points, OmniSwitches, servers and an OmniVista Cirrus. It simulates a three-tier end user topology (Access, Aggregation and Core)." (p35)

## I · 方法论骨架

交付七段主线（创建顺序）：
1. **复位与连通验证**（ping DHCP 服务器/外网）；
2. **组织建模**：Organization > Site（含预留站点）> Building > Floor，楼层挂平面图；设备必须归属站点；
3. **设备上线**：show chassis 取序列号逐台入 Device Catalog，走 Waiting for first Contact → Connected to OV → Provisioning → OV Managed（约 2 分钟；交换机 cloud-agent admin-state restart 加速，AP 可 ssudo firstboot -y + reboot 触发）；不能上云管的型号（OS-2360）只能手工配；
4. **WLAN**：多 SSID 差异化设计（见 A1）；RF Profile 开 Band Steering/Load Balance、关联门限；
5. **安全**：WIPS 流氓 AP 分类规则（同 SSID 名 + 指定 MAC OUI）、认证失败黑名单（5 次/分钟）、访客客户端隔离、AP 关闭 SSH/Web 管理；
6. **运维**：Golden Config、配置备份、VLAN 模板（IP 用变量）、标签、支持信息收集、周报排程、场景化监控阈值；
7. **拓扑变更**：按需把部分 AP 改 Mesh。

清理是逆向拆除（云管无一键恢复默认）：按创建的反序删——运行任务 → WIPS → AP 组/Provisioning/RF Profile 解绑 → SSID → 策略/角色/门户 → 账号/资产 → Golden Config → 报表 → 阈值重置 → 站点 → 确认设备目录空 → CLI 模板/值映射。

## A1 · 书中案例（Lab 精要）

综合演练（p286-299）三个差异化 SSID：EmployeesX（WPA2-Enterprise 802.1X、仅 5GHz、VLAN 20、工作时间调度、按角色封 HTTP）；GuestsX（内部 Captive Portal、限 1Mbit/s、封 SSH/Telnet、VLAN 30、周一至周三调度、账号限时限量）；PrinterX（仅 2.4GHz、最小发射功率、固定信道、WPA2 PSK + 按设备 PSK/DPSK、复用 Employee VLAN）。RF Profile：负载均衡启用、关联门限 -50dBm。监控阈值（p298）：健康 70%、2.4G 利用率 20%（只跑打印机故收紧）、2.4G 客户端健康 90%、可用容量 25%。末段两 AP 建 Mesh（AP1321 为 Root、自定义 SSID、WPA2-Personal）。
基础 Lab（p43-73）补充上线细节：reset_PODX 复位 → My Site + Building A/Ground Floor（画约 1200-1300m² 楼层边界）→ 双交换机 + 双 AP 入目录 → 手工配 VLAN 10/20/30 → EmployeesX/GuestsX 映射 My-AP-Group → 树莓派验证（Employee 192.168.20.70-79 / Guest 192.168.30.70-79）。
清理 Lab（p313-319）：29 步逆向拆除全量配置，清理后设备目录回空、可重新部署。

## A2 · 触发场景（含与相邻 skill 的区分）

- 新项目交付或交付前演练验收，需要一份覆盖组织/上线/SSID/安全/运维的 checklist → 本 skill。
- 项目下线、换设备、重配网络前要清空云管配置 → 本 skill 清理流程（别去找"一键恢复"，没有）。
- 单点深入：SSID 高级选项 → stellar-ssid-advanced；Mesh → stellar-bridge-mesh；阈值业务含义 → stellar-monitoring-ops；上线后故障 → stellar-troubleshooting-cli。

## E · 可执行步骤

交付（照 A1 七段主线逐项打勾）：
1. 复位设备，ping 验证到 DHCP/外网连通。
2. 建组织层级与站点（含预留），导入楼层平面图。
3. 设备逐台录序列号上线，确认到 OV Managed；非云管型号手工配并记录。
4. 配 VLAN/IP，按设计建差异化 SSID（认证/频段/VLAN/调度/限速逐项对表），映射 AP 组。
5. 配 RF Profile（Band Steering、Load Balance、门限）并验证关联。
6. 配 WIPS 分类规则、黑名单、访客隔离、关闭 AP 管理面。
7. 立 Golden Config、备份计划、变量化 VLAN 模板、标签、周报、场景化阈值。
8. 按需改造 Mesh，全量回归验证。

清理（逆向，每步确认删除成功再走下一步）：
1. 删运行任务（升级计划/备份/排障命令）→ 2. 重置 WIPS → 3. AP 回 default device group、AP 组回 Default Provisioning → 4. 删自定义 AP 组/Provisioning/RF Profile（报错先把引用改回 Default）→ 5. 删 SSID → 6. 删策略/角色/门户 → 7. 删账号/注册 Profile/公司资产 → 8. 取消 Golden Config → 9. 删报表/支持信息 → 10. 重置分析阈值 → 11. 删站点（连带楼栋楼层）→ 12. 确认设备目录为空 → 13. 删 CLI 模板与值映射。

## B · 边界与陷阱

- 云管没有一键恢复默认；删除全部要手工逆向，漏一步就留下孤儿配置。
- 删除有依赖顺序：AP 组挂着自定义 Provisioning 删不掉；Provisioning 引用自定义 RF Profile 也删不掉——先改回 Default 再删（逆着创建顺序操作）。
- 误删组织（MSP Portal 上对 Organization 点 Delete）不可恢复，连带站点、设备与全部配置。
- 复位脚本运行中交换机重启阶段不能按任何键，否则掉进 Miniboot 且重启中断。
- 实验环境边界：核心 OS-6900、汇聚 OS-6870 预置配置与 DHCP/NAT 服务器不得改删（改删断云管连通）；树莓派有线网卡绝不能动（远程桌面走有线）。
- OS-2360 这类不能上云管的交换机只能手工配置，checklist 里别指望云管纳管它。

---
来源条目: f08, f10, c01, c02, c09, c10, ce01, ce02, ce03, ce04, ce13, g32, g33, g34, g36, g37, g38, g39, g40, g56, g57, g58
