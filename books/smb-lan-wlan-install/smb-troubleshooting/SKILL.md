---
name: SMB 网络分层排障与 LED 判读
description: 当 AP/交换机失联、设备不出现在 Cirrus、SSID 连不上或认证失败，需要按分层思路定位并使用诊断命令时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 新上的 AP 不上线 / 设备不出现在 OV Cirrus
- 客户端连不上 SSID、拿到错网段地址或 802.1X/门户认证失败
- 需要在 Stellar AP 上做无线侧诊断（信号、客户端列表、抓包）

## I（核心理念）
排障按层走：先物理（线缆/PoE/LED），再二层（VLAN 成员/MAC 学习），再三层（IP 接口/DNS/激活域名），最后平台侧（激活日志/认证记录）。无线侧 Stellar AP 的 support 凭据下有一整套 iw*/ssudo/eag_cli 工具链可直接看客户端与认证内部状态。多数"故障"其实是环境默认行为（端口 disabled、non-https 才触发门户、会话被占用）。

## A1（行动框架）
1. 设备未上 Cirrus 分层排查（C23，<<<PAGE 347>>>–<<<PAGE 348>>>、<<<PAGE 358>>>–<<<PAGE 360>>>）：
   - L2：`show interfaces 1/1/5` 查线缆 → `show vlan members port` 查 VLAN → `show lanpower slot 1/1` 查 PoE
   - L3：`show ip interface` → `ping eu.activation.ovng.myovcloud.com`
   - AP 侧：`getmode`（须 OVNG）、`cat /etc/config/network`（proto 须 dhcp）、`getovinfo`
   - Cirrus 侧：Action > Diagnostic Tools > View Activation Log
2. AP 无线诊断命令集（C22，<<<PAGE 397>>>–<<<PAGE 400>>>、<<<PAGE 426>>>–<<<PAGE 430>>>，support 登录）：
   ```
   iwconfig                          # ESSID/频率/功率/信号
   iwlist ath01 channel|txpower|bitrate
   ssudo sta_list                    # 客户端 + VLAN + Final_role
   wlanconfig ath01 list
   ssudo wam_debug sta_list          # JSON：assignedVLAN/assignedAR/认证来源
   cat /proc/kes_syslog | grep "<MAC>"
   ```
3. 802.1X 排查：`cat /var/config/wlanservice.conf`、`cat /var/config/AAA_profile.conf`、`cat /var/config/AAA_server.conf`；抓包 `tcpdump -i br-wan -s 0 host <radiusIP>`。
4. Captive Portal 排查：`ps |grep eag`、`eag_cli show user all`、`eag_cli kick user index 1`、`tail -f /tmp/log/eag.log`。
5. LED 快速判读：
   - AP：绿闪 = 启动完成广播默认 SSID；蓝 = 双频；蓝红闪 = 升级中；蓝红绿闪 = 定位模式；红 = 启动中（P42，<<<PAGE 52>>>）
   - 交换机 OK/PWR：OK 绿 = 自检通过，闪绿 = 进行中，琥珀 = 失败；PWR 绿 = 电源正常，闪绿 = 在位但故障（P43，<<<PAGE 50>>>）
   - PoE 口：琥珀 = 已受电，绿 = 连接未受电（P44，<<<PAGE 143>>>）

## A2（进阶应用）
- 客户端定位链：交换机 `show mac-learning | grep <MAC>` 找端口（C10，<<<PAGE 181>>>）→ AP `ssudo sta_list` 看 Final_role 与 VLAN（C22）。
- 云管排障：Cirrus Device Troubleshooting 可 Assign Command 下发（如 setDateTime）并等回显；Collect Support Info 对 AP 一键 tar.gz、交换机可选 swlog/cfg/Tech Support（C24，<<<PAGE 451>>>–<<<PAGE 456>>>）。
- 认证记录：Cirrus Network > Access Records > Authentication Records 查 802.1X 结果（C20，<<<PAGE 390>>>–<<<PAGE 396>>>）。
- 踢出问题客户端：Network > Analytics > Clients > Actions > Kick Off（C21，<<<PAGE 418>>>–<<<PAGE 425>>>）。
- OmniVista Smart Tool (OST)：免费安装排障工具，含 PoE 向导、自动开票、流量分析（glossary·<<<PAGE 498>>>–<<<PAGE 504>>>）。
- R-Lab 实验环境重置：Reset_PodX 一键重置（交换机约 5 分钟、AP 约 1.5–2 分钟），WifiClientX 清已存无线网络（C30，<<<PAGE 89>>>–<<<PAGE 92>>>）。

## E（实证案例）
- 设备不上 Cirrus：沿 L2 线缆/VLAN/PoE → L3 IP 接口 → ping 激活域名 → AP getmode/getovinfo → Cirrus 激活日志逐层收敛（C23，<<<PAGE 347>>>–<<<PAGE 348>>>、<<<PAGE 358>>>–<<<PAGE 360>>>）。
- 802.1X 失败：tcpdump 抓 RADIUS 报文 + 检查 AAA_server.conf（C22，<<<PAGE 397>>>–<<<PAGE 400>>>）。
- 门户用户异常：`eag_cli show user all` 列表 + `tail -f /tmp/log/eag.log` 实时日志（C22，<<<PAGE 426>>>–<<<PAGE 430>>>）。

## B（边界与陷阱）
- "Hunting Group Busy" 不是设备故障，是另一个 TeraTerm 会话已占用 console（CE08，<<<PAGE 82>>>）。
- Firefox 从实验指南向远程终端粘贴有剪贴板问题，推荐 Chrome/Edge（CE09，<<<PAGE 79>>>）。
- 树莓派有线网卡不可改不可拔——那是唯一的管理通道（CE07，<<<PAGE 85>>>）。
- R-Lab 重置后交换机所有端口 disabled，"端口不通"先查 admin-state（CE01，<<<PAGE 89>>>）。
- 门户不弹出多为访问了 https 站点，必须手动开 non-https URL（CE11，<<<PAGE 422>>>）。

## 来源
- case·设备未在 Cirrus 出现的分层排障流程（<<<PAGE 347>>>–<<<PAGE 348>>>、<<<PAGE 358>>>–<<<PAGE 360>>>）
- case·Stellar AP Wi-Fi 故障诊断命令集（<<<PAGE 397>>>–<<<PAGE 400>>>、<<<PAGE 426>>>–<<<PAGE 430>>>）
- case·Cirrus 运维排障命令（<<<PAGE 451>>>–<<<PAGE 456>>>）
- case·R-Lab 环境重置（<<<PAGE 89>>>–<<<PAGE 92>>>）
- principle·Stellar AP LED 状态语义（<<<PAGE 52>>>）
- principle·交换机 OK/PWR LED 语义（<<<PAGE 50>>>）
- principle·PoE 端口 LED 判读（<<<PAGE 143>>>）
- counter·Hunting Group Busy（<<<PAGE 82>>>）
- counter·树莓派有线网卡不可触碰（<<<PAGE 85>>>）
