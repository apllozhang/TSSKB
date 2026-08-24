---
name: cluster-bootstrap-pvm
description: 何时用：Stellar AP Express 模式首次开局、组网规划、PVM 选举预判或无 DHCP 应急接入时。
source_book: AWOS 5.0.3 Stellar AP User Guide
---

# Express 集群开局与 PVM 选举

## R · 原文引用

> The ALE WLAN solution is based on a cluster architecture. A maximum of 255 APs are supported in one AP cluster/group. All APs have the same cluster ID that uniquely defines the AP group and all APs have to be in the same VLAN because the communication between group members is based on multicast. (p13)

> By default, the AP group will advertise the pre-defined SSID 'mywifi-xxxx' and you can connect to 'mywifi-xxxx' to browse the AP group GUI through http://mywifi.al-enterprise.com:8080 to the initializing wizard. After you complete Using the Initializing Wizard, the SSID 'mywifi-xxxx' will be deleted. (p13)

> PVM/SVM election priority: AP1451>AP1351>AP1431/AP1331>AP1521>AP1320/AP1360>AP1511/AP1411>AP1311/AP1301>AP1301H>AP1220/AP1230/AP1251/AP1201>... Among the APs with same priority, the one with highest MAC address will be selected as PVM. (p18)

> Group Management IP - A virtual IP address for AP group management, default is 10.0.0.1 ... Group ID - Identification of the AP group, default is 100. ... you can manage the AP group via accessing the URL: http://GMIP:8080 by wired or wireless. (p31-32)

## I · 方法论骨架

开局三部曲：**物理接入 → 初始化向导 → 组管理入口固化**。

1. 组网前提先行核对：同 VLAN、同 cluster ID（默认 100）、≤255 台（低端机型当 PVM 时 ≤32 台）。
2. 一次只上一台 AP 完成向导，再逐台加入同步。
3. 向导后用 GMIP（默认 10.0.0.1）替代漂移的 DHCP 地址做长期管理入口。
4. PVM/SVM 由机型优先级链 + MAC 最大者自动选举，可预判、也可手动 "Update to PVM" 干预。

## A1 · 书中案例

- 无 DHCP 场景：AP 默认 IP 192.168.1.254；笔记本直连，配 192.168.1.100/24、网关 192.168.1.254、DNS 指向 192.168.1.254，访问 http://192.168.1.254:8080。
- 弹性配比：每 64 台 AP 网段至少放 4 台中高端机型；扩到 255 台需集群内至少 16 台同档（AP12XX/13XX/14XX/15XX 任一档）。
- ZTP 场景：AP 从 ALE OXO 服务器取 IP、下载固件与配置，自动重启成组。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：新装机房/楼宇首次上电开局；PVM 归属预判；换 PVM 硬件；DHCP 故障导致全组失联的应急。
- 区分：只调 SSID/射频/Portal 参数 → 用 `ssid-radio-tuning`；配 802.1X/RadSec/证书 → 用 `wlan-security-enterprise`；备份/升级/扩组/Mesh → 用 `ap-ops-upgrade-mesh`。

## E · 可执行步骤

1. 核对组网前提：全部 AP 同 VLAN、同 cluster ID（默认 100）、机型容量满足 255/32 分级。
2. 按机型优先级链预判 PVM；混入 AP1201 时若被选为 PVM，手动把 AP1220/1230/1251 提升为 PVM。
3. 单台 AP 上电，终端连预置 SSID `mywifi-xxxx`，访问 http://mywifi.al-enterprise.com:8080（或 http://AP-IP:8080）。
4. 走完五步向导：改管理员密码（默认 admin）→ 国家码/时区（-RW 机型）→ 建 WLAN。全程终端不得离开 mywifi-xxxx。
5. 向导完成后补 VLAN 映射（向导阶段不可配，走 "Modify Your WLAN"）。
6. 规划 GMIP：从 AP 网段选空闲 IP（默认 10.0.0.1），确保管理终端可路由，此后统一用 http://GMIP:8080 管理。
7. 改密清单：Web Administrator/Viewer/GuestOperator + CLI root 与 support（root 凭据由 AP 生成、仅客户持有）。
8. 逐台插入其余 AP 等待配置同步。
9. 双上行机型：上游交换机确认 LACP；AP1351/AP1451 Class 7 需 802.3bt 交换机 + PoE 固件 3.XX。

## B · 边界与陷阱

- **多台同时首上电各自成组**：一次只接一台（Note 3-2）。
- **向导中断**：终端中途切网导致向导失败；完成后 mywifi-xxxx 自动删除，无线管理须改连向导新建的 WLAN。
- **VLAN 两段式**：向导不能配 VLAN，规划时必须留出向导后补配步骤。
- **DHCP 失效灾难模式**：AP 重启时 DHCP 不可达 → 全组回退 192.168.1.254，同广播域 IP 冲突、各自成 PVM。先修 DHCP，别逐台手工处理。
- **GUI 上限**：每台 AP 最多 3 个并发 GUI 连接；浏览器基线 Chrome 102+/Firefox 100+/Edge 92+。
- **低端 PVM 容量**：AP1101/AP1201H/AP1201L/AP1201HL 当 PVM → 集群上限跌到 32 台。
- **锁定策略**：默认 3 次失败登录锁 1 分钟。

---
来源条目: p01, p02, p03, p04, p05, p06, p07, p08, p27, ce01, ce02, ce03, ce04, ce05, ce06, g01, g02, g03, g04, g05, g06, g07, g08, g09, g10, g35
