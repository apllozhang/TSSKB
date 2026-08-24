# counter-examples 候选 — DT00XTE301 LAN & WLAN Installation & Configuration for SMB

## CE01. R-Lab 默认配置不是空配置，重置后所有端口被禁用
- 页码：<<<PAGE 89>>>
- 原文摘录（WARNING）："THE OMNISWITCH SWITCHES DEFAULT CONFIGURATION IS NOT AN EMPTY CONFIGURATION! WHEN CLICKING ON THE SHORTCUT: A SPECIFIC CONFIGURATION IS APPLIED TO THE SWITCHES, ALL THE INTERFACES ARE DISABLED. DURING THE NEXT LABS, IT WILL BE ASKED TO ENABLE THE INTERFACES THAT YOU WILL USE."
- 陷阱：以为重置=干净出厂；实际端口全 disabled，不通时先 `interfaces x admin-state enable`。

## CE02. 不要把实验室交换机恢复真出厂配置
- 页码：<<<PAGE 105>>>
- 原文摘录（Warning）："DON'T TEST THE FOLLOWING PART ON YOUR LAB! THE SWITCHES … ARE LOADED WITH A SPECIFIC DEFAULT CONFIGURATION. REINITIALIZING THEM TO THEIR FACTORY DEFAULT CONFIGURATION MAY LEAD TO ISSUES!"
- 陷阱：教学/托管环境里 `rm vcboot.cfg` + reload 会破坏预置基线。

## CE03. `reload all` 无条件从 certified 启动
- 页码：<<<PAGE 132>>>
- 原文摘录（Warning）："IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS"
- 陷阱：用 `reload all` 验证新配置会回退到 certified 旧配置；应用 `reload from working no rollback-timeout`。

## CE04. 未保存配置时断电/重启即丢失
- 页码：<<<PAGE 133>>>
- 原文摘录（Warning）："IF THE OMNISWITCH IS REBOOTED NOW …, ALL THE CHANGES IN THE RUNNING CONFIGURATION WILL BE OVERWRITTEN … IN OUR CASE, THE VLAN 2, 3 AND 99 WILL BE LOST"
- 陷阱：RAM 中的 VLAN 修改未 `write memory`，重启即丢。

## CE05. Certified 运行模式下无法保存任何修改
- 页码：<<<PAGE 135>>>
- 原文摘录：`write memory` 返回 "ERROR: Write memory is not permitted when switch is running in certified mode"
- 陷阱：从 certified 启动后做配置全部白做；须先 `modify running-directory working` 或换启动目录。

## CE06. AP 加入 AP Group 后本地配置被清除
- 页码：<<<PAGE 266>>>
- 原文摘录（Warning）："WHEN AN OMNIACCESS STELLAR ACCESS POINT GETS IN AN AP GROUP, ITS CONFIGURATION IS DELETED AND REPLACED BY THE CONFIGURATION SENT FROM THE PRIMARY VIRTUAL MANAGER (PVM) ACCESS POINT."
- 陷阱：单点调好的 AP 一旦成组，配置被 PVM 下发的组配置覆盖。

## CE07. Raspberry Pi 有线网卡不可触碰
- 页码：<<<PAGE 85>>>（原文页 2000–2003 行对应 Lab 文档页 6）
- 原文摘录（Warning）："Never touch the Ethernet card (configuration or disconnection), because it is from the wired network that you can join the raspberry pi desktop."
- 陷阱：误改/误拔树莓派有线口会直接失联。

## CE08. "Hunting Group Busy" = 控制台会话被占用
- 页码：<<<PAGE 82>>>
- 原文摘录（Tips）："If you get a message 'Hunting Group Busy' when you open a TeraTerm console, it means that another TeraTerm session has already been opened (from your account or another account)."
- 陷阱：不是设备故障，是并发 console 占用。

## CE09. Firefox 剪贴板问题导致实验指南无法粘贴
- 页码：<<<PAGE 79>>>
- 原文摘录："Other web browser may have some issue with copy/paste from a lab guide to the remote terminal session. Known workaround for FireFox: https://sudoedit.com/firefox-async-clipboard/"
- 陷阱：推荐 Chrome/Edge 访问 R-Lab。

## CE10. 不要删除 OV Cirrus 组织
- 页码：<<<PAGE 340>>>
- 原文摘录（Warning）："DO NOT use the action Delete on your Organization."
- 陷阱：MSP 视图下误删组织不可恢复。

## CE11. Captive Portal 重定向需要 non-https URL
- 页码：<<<PAGE 422>>>
- 原文摘录（Notes）："you have to open your web browser manually and open any non-https URL to be redirected to the Captive Portal"（Debian 树莓派不会自动弹门户）
- 陷阱：访问 https 站点不会触发重定向，易误判门户故障。

## CE12. 访客账号字段区分大小写
- 页码：<<<PAGE 226>>>
- 原文摘录："The username and password fields are case sensitive (ex. The username 'Guest' is different than 'guest')"
- 陷阱：大小写不一致导致门户登录失败。

## CE13. Lightning Config 前禁止把新交换机接入网络/互联
- 页码：<<<PAGE 477>>>、<<<PAGE 486>>>
- 原文摘录："Do not pre-cable the ALE switch to the network. / Do not connect the ALE switch to any other switch. / Do not connect the ALE switch to a DHCP server."；"Never connect an out-of-box ALE switch to another without running Lightning Config first."
- 陷阱：多台未配置交换机同网段会 IP 冲突（默认都是 192.168.0.1）；另外"Do NOT skip the Recommended Defaults!"（<<<PAGE 484>>>）。

## CE14. 物理环路未做防环会拖垮全网
- 页码：<<<PAGE 494>>>
- 原文摘录："Physical loops in networks can be very bad … cause communication … to continually circle the network and slow down or even halt effective communication. … please STOP and consult with the solution architect to ensure they have implemented loop avoidance"
- 陷阱：按模板接线出现环路前必须确认 STP 等防环已启用。

## CE15. AP1101 / AP1201L/H/HL 不支持 OV Cirrus 云管
- 页码：<<<PAGE 290>>>
- 原文摘录："All Stellar models supported, except: AP1101, AP1201L/H/HL. Software version: AWOS 4.0.6 GA or higher"
- 陷阱：老/入门 AP 型号或低版本 AWOS 无法上云。

## CE16. OS2360（AOS 5.2）无法 onboard 到 Cirrus
- 页码：<<<PAGE 337>>>
- 原文摘录："We can onboard in OVC only switches with AOS 8.9R1 or higher so we can't onboard OmniSwitch 2360 AOS 5.2."
- 陷阱：AOS 版本低于 8.9R1 的交换机只能 CLI 管理，VLAN 需手工配置。

## CE17. cloudagent.cfg 缺失则交换机无法注册 Cirrus
- 页码：<<<PAGE 338>>>
- 原文摘录（Warning）："IF THE FILE IS NOT PRESENT, TYPE THE FOLLOWING COMMAND TO COPY IT FROM A BACKUP DIRECTORY: -> cp /flash/cirrus/cloudagent.cfg /flash/working/cloudagent.cfg"
- 陷阱：working 目录丢文件时激活服务器 URL 丢失。

## CE18. FPoE/PPoE 与 delayed-start 互斥；P10A 不支持 FPoE/PPoE
- 页码：<<<PAGE 154>>>、<<<PAGE 144>>>–<<<PAGE 145>>>
- 原文摘录："Fpoe and Ppoe is not supported on enabling this feature (delayed-start)."；"Note: OS6360 – P10A does not support FPoE / PPoE"
- 陷阱：特性组合与具体子型号限制，规划供电时须核对。

## CE19. 升级窗口内设备不可用、客户端断线
- 页码：<<<PAGE 452>>>
- 原文摘录："when a device is upgraded, it will reboot with the new image. It will then become unavailable during this upgrade duration and all the end clients connected to this device will be disconnected."
- 陷阱：计划升级需安排在业务空闲时段。

## CE20. 多 AP 同时默认 IP 192.168.1.254 会冲突
- 页码：<<<PAGE 101>>>
- 原文摘录："By default, all the OmniAccess Stellar AP have the same administration IP address (192.168.1.254)."
- 陷阱：静态管理多台新 AP 前必须逐台改 IP 或直接依赖 DHCP；AP 改 IP 后旧地址访问失效（<<<PAGE 103>>>）。

## CE21. boot.md5 拷贝报 Permission denied 属正常
- 页码：<<<PAGE 136>>>
- 原文摘录（Tips）："it tries to copy the boot.md5 file but a 'permission denied' message is displayed. This file is auto generated so ignore this error and proceed."
- 陷阱：复制 working 目录到 user 目录时的预期报错，不代表复制失败。
