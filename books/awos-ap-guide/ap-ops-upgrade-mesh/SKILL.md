---
name: ap-ops-upgrade-mesh
description: 何时用：配置备份恢复、固件升级、扩组/换机、日志与远程管理、MESH/无线桥接部署时。
source_book: AWOS 5.0.3 Stellar AP User Guide
---

# 运维、扩组与 MESH 部署

## R · 原文引用

> All configuration settings (clear, backup or restore) will be applied to the entire group. There is no need to select specific APs to apply configuration settings. The entire group of APs have one configuration file. (p78)

> To replace the current PVM: Upgrade the SVM to the PVM before disconnecting the old PVM. ... Method two: Setup up different group IDs ... Method three: Deploy Stellar AP with ALE OmniVista and scale up to 4000 AP in one network. (p86)

> By default, Stellar AP with factory configuration powered up without wired uplink will try to establish MESH link automatically with build-in configuration (MESH SSID [Stellar-MESH] and password on 2.4G band). The out-of-box will be permanently disabled once the AP ever connected to wired uplink. (p103)

## I · 方法论骨架

运维三原则：**整组一份配置 → 变更前备份 → 变更按操作顺序**。

1. 任何 clear/backup/restore 均整组生效，无需选 AP；配完即导出备份。
2. 换 PVM 必须先升 SVM 再拆旧机；扩组三法按规模选（子网划分 / 不同 group ID / OmniVista 4000 台）。
3. Mesh/桥接是硬件延伸：开箱 Mesh 免配置但有不可逆条件；桥接有机型红线。

## A1 · 书中案例

- 超 255 台的单网：改用 OmniVista 管理，单网可扩到 4000 台 AP。
- 楼宇间互联：Wireless Bridge 替代专线/光纤——但只能选支持 VLAN 标签桥接的中高端机型。
- 故障取证：PMD（Post Mortem Dump）在 AP 关键进程崩溃时把 core dump 自动发 TFTP 服务器（默认发送关闭，需先启用配置）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：上线后固化配置基线；版本升级窗口；替换故障 AP；规模超单组上限；无布线区域做 Mesh 覆盖；崩溃取证。
- 区分：开局向导与 PVM 选举规则 → `cluster-bootstrap-pvm`（本文只讲"换 PVM 的操作顺序"）；射频/Portal 日常调参 → `ssid-radio-tuning`；转 OV 管理的加密与账户 → `wlan-security-enterprise`。

## E · 可执行步骤

1. 备份基线：完成全部配置后立即在 Web UI 导出整组配置文件（单台 AP 固件升级约 5 分钟，留足窗口）。
2. 升级流程：整组升级 → 完成后清浏览器 Cookies 与 Cache（官方强烈建议，否则旧资源导致界面异常）。
3. 日志与时间：组内 AP 每 15 分钟 NTP 同步；Syslog 默认级别 Notice（0-7，含更低级别）；单 AP 本地日志 1MB FIFO 滚动。SNMPv3 认证固定 sha、加密固定 aes128。
4. 换 PVM：先把 SVM 升级为 PVM（AP Window "Update to PVM"）再断开旧 PVM；换 SVM/成员可直接换，不影响其他 AP 用户。新增 AP 前确保 PVM 不处于 Down 状态。
5. 扩组三法：a) 按交换机端口默认 VLAN 划不同子网；b) 每组配不同 group ID；c) 转 OmniVista 管理扩到 4000 台。转 OV On-Premise 可用 DHCP Option 138/43 自动下发 OV 服务器地址，转换后 AP 会重启注册（留变更窗口）。
6. Out-of-box MESH：新 AP 不接有线直接上电 → 自动用内置 SSID "Stellar-MESH"（2.4G）建链，管理员只需指定根节点。Mesh 链路根到叶必须同频段；组播速率默认 24 Mbps。
7. Wireless Bridge：按需部署点对点网桥；桥接 AP 不服务无线客户端（与 MESH 不同）。
8. 崩溃取证：预先启用 PMD 并指定 TFTP 服务器。
9. 扫描数据采集：需要 RF Environment 数据时让 AP 进扫描模式——One Time（5 分钟自动恢复）或 Always（拒绝接入）。

## B · 边界与陷阱

- **Out-of-box MESH 不可逆**：AP 一旦接过有线 uplink 即永久禁用，只有恢复出厂才能找回。Regular MESH 需逐台登录 AP UI 手工配置。
- **低端机型桥接红线**：AP1201/AP1201L/AP1201H/AP1201HL 不支持带 VLAN 标签的桥接报文，不做无线网桥；确需用联系 ALE 支持。
- **组间不漫游**：无 OmniVista 时各 AP 组独立管理、组间不漫游——多组方案要放在漫游边界清晰的位置。
- **升级后浏览器缓存**：界面异常先清 Cookies/Cache 再报障。
- **扫描模式服务中断机型差异**：无扫描射频机型全客户端掉线；AP1451 仅 6GHz 中断。
- 组内 "Contact to Cloud"（联系 OmniVista Cirrus）默认启用；AWOS 4.0.0 及之前版本的 AP 默认不允许入组（MQTT 兼容开关控制）。

---
来源条目: p09, p20, p21, p22, p24, ce10, ce11, ce13, g31, g32, g33, g34
