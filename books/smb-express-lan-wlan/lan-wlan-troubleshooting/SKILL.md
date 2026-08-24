---
name: LAN/WLAN 故障排查
description: 当 AP/交换机/客户端上不了线、SSID 连不上、访客 Portal 不跳转、或需要用镜像/监控抓流量定位问题时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- AP 不上线/不上云，需要从 PoE→线缆→VLAN→AP 状态→L3 逐层排查
- 员工 SSID（802.1X）连接失败，需要看 AP CLI 无线状态与 RADIUS 配置
- 访客 Captive Portal 不弹页面；需要抓包或镜像端口定位

## I（核心理念）
排查走"分层递进 + 分侧取证"：有线侧自下而上（电→VLAN→IP→云），无线侧在 AP CLI 用 iwconfig/sta_list 看空口与角色，认证侧核对 AAA 配置与日志进程。每层都有明确命令与预期输出，失败点即故障层。

## A1（行动框架）
1. **AP 上线排障五步法**（<<<PAGE 376>>>-<<<PAGE 378>>>、<<<PAGE 365>>>-<<<PAGE 366>>>）：
   - PoE：`show lanpower slot 1/1`；
   - VLAN：`show vlan members port 1/1/6`（管理 VLAN 须 untagged）；
   - AP 状态：Console 下 `getmode`（须 OVNG）、`cat /etc/config/network`（proto dhcp）、`getovinfo`；
   - 交换机 L3：`show ip interface` + `ping eu.activation.ovng.myovcloud.com`；
   - 云侧：Cirrus Action > Diagnostic Tools > View Activation Log。
2. **员工 SSID 连接排障**（AP CLI，<<<PAGE 415>>>-<<<PAGE 418>>>）：`iwconfig`（ESSID/Tx-Power/SNR）→ `iwlist ath01 channel` / `iwlist ath01 txpower` → `ssudo sta_list`（VLANID/Final_role）→ `ssudo wam_debug sta_list`（JSON：assignedVLAN/assignedAR）→ `cat /proc/kes_syslog | grep "<MAC>"` → `cat /var/config/AAA_profile.conf` + `AAA_server.conf` 核对 RADIUS IP/secret → 仍失败 `tcpdump -i br-wan -s 0 host <radiusIP>`。
3. **Captive Portal 排障**（<<<PAGE 444>>>-<<<PAGE 448>>>）：前置 `date`（账号有效期）与 `cat /etc/resolv.conf`（DNS 必需）→ `ps | grep eag`（/usr/sbin/eag_app 存活）→ `eag_cli show user all` → `eag_cli kick user index 1` → `tail -f /tmp/log/eag.log`、`cat /var/log/eag.log`。
4. **交换机首次接入排障**（<<<PAGE 113>>>-<<<PAGE 114>>>）：Console 登录 → `interfaces 1/1/6 admin-state enable`（端口默认禁用）→ `ip interface int_1 address 192.168.1.2/24 vlan 1` → `show ip interface` → `write memory flash-synchro`。
5. **远程接入**（<<<PAGE 135>>>-<<<PAGE 139>>>）：`aaa authentication ssh local`、`aaa authentication http local` → `show webview`（Force-SSL Enabled）→ HTTPS 登录 WebView 管理。

## A2（进阶应用）
- **R-Lab 环境恢复**：用 Reset_PodX 脚本一键复位，交换机约 5 分钟、AP 约 1min30-2min（<<<PAGE 108>>>）；复位后交换机加载的是"特定默认配置、所有端口禁用"，并非空配置（<<<PAGE 107>>>）。
- **Port Mirroring 抓包**：镜像会话数有限——6870 上限 2（<<<PAGE 568>>>），部分新型号 8.9R3 提升到 4（<<<PAGE 552>>>）；Port Monitoring 与 Mirroring 不能配在同一端口（<<<PAGE 554>>>、<<<PAGE 718>>>）。
- **AP Web 连通替代路径**：AP 改 DHCP 模式后可用域名 `mywifi.al-enterprise.com:8080` 重连（<<<PAGE 177>>>-<<<PAGE 183>>>）。
- **客户端行为取证**：Client Behavior Tracking 日志含 Event date/client MAC/IP/AP MAC/SSID/ONLINE-OFFLINE（<<<PAGE 236>>>-<<<PAGE 237>>>）。

## E（实证案例）
- 上云排障五步法完整走位：PoE→VLAN（管理 VLAN untagged 检查）→getmode/cat network→ip interface+ping 激活域名→OVC Activation Log（<<<PAGE 376>>>-<<<PAGE 378>>>、<<<PAGE 365>>>-<<<PAGE 366>>>）。
- 802.1X 排障链：iwconfig→sta_list（看 assignedVLAN）→AAA_server.conf 核对→tcpdump 抓 RADIUS（<<<PAGE 415>>>-<<<PAGE 418>>>）。
- Portal 排障链：date/resolv.conf 前置检查→eag 进程→eag_cli 用户列表→eag.log（<<<PAGE 444>>>-<<<PAGE 448>>>）。

## B（边界与陷阱）
- **不要对预配置设备恢复出厂**：R-Lab 交换机装有特定默认配置，恢复出厂会破坏实验环境（<<<PAGE 123>>>）；同理不要动实验室核心 OS6900（<<<PAGE 100>>>）、不要对 Organization 用 Delete（<<<PAGE 358>>>）。
- **Lightning Config 触发条件苛刻**：仅第一/二物理口接客户端、无任何既有配置、开机后无 DHCP 分配、无 RCL/OmniVista 连接时才触发（<<<PAGE 79>>>、<<<PAGE 1025>>>）；不要预先把新交换机接进网络，也不要把两台开箱交换机直连（先跑 Lightning Config，<<<PAGE 1034>>>）；保存配置后默认 IP 192.168.0.1 被移除（<<<PAGE 79>>>）。
- **镜像与监控互斥**：同一端口不能同时配 Port Mirroring 和 Port Monitoring；镜像会话数有型号上限（<<<PAGE 554>>>、<<<PAGE 718>>>、<<<PAGE 568>>>、<<<PAGE 552>>>）。
- R-Lab 复位后所有端口禁用，需手工 `interfaces ... admin-state enable`（<<<PAGE 107>>>、<<<PAGE 113>>>）。

## 来源
- cases·C19 上云排障五步法（<<<PAGE 376>>>-<<<PAGE 378>>>、<<<PAGE 365>>>-<<<PAGE 366>>>）
- cases·C22 员工 SSID 排障（<<<PAGE 415>>>-<<<PAGE 418>>>）
- cases·C23 Captive Portal 排障（<<<PAGE 444>>>-<<<PAGE 448>>>）
- cases·C2 R-Lab 一键复位（<<<PAGE 104>>>-<<<PAGE 110>>>）
- cases·C3 首次 Console 登录（<<<PAGE 113>>>-<<<PAGE 114>>>）
- cases·C8 SSH/WebView 远程接入（<<<PAGE 135>>>-<<<PAGE 139>>>）
- counter-examples·X5 勿动预配置设备（<<<PAGE 123>>>、<<<PAGE 100>>>、<<<PAGE 358>>>）
- counter-examples·X15 Lightning Config 前提（<<<PAGE 79>>>、<<<PAGE 1025>>>、<<<PAGE 1034>>>）
- counter-examples·X17 镜像/监控互斥与会话上限（<<<PAGE 554>>>、<<<PAGE 718>>>、<<<PAGE 568>>>、<<<PAGE 552>>>）
