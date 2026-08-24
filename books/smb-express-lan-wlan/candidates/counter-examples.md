# counter-examples 候选 — DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express

> 陷阱与反例（WARNING 页、错误配置、故障边界、模式选错后果）。共 17 条。

## X1. reload all 无条件从 certified 启动（丢未认证配置）
- <<<PAGE 126>>>
- 原文摘录："Warning > The 'reload all' command particularity: IF THE OMNISWITCH IS REBOOTED WITH THE 'RELOAD ALL' COMMAND, IT WILL REBOOT FROM THE CERTIFIED DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS"

## X2. RAM 未保存就重启 → 配置全部回滚
- <<<PAGE 127>>>
- 原文摘录："Warning > What if the OmniSwitch reboots now? … ALL THE CHANGES IN THE RUNNING CONFIGURATION WILL BE OVERWRITTEN … IN OUR CASE, THE VLAN 2, 3 AND 99 WILL BE LOST"

## X3. Certified 模式下禁止 write memory（典型报错）
- <<<PAGE 129>>>
- 原文摘录："-> vlan 4 / -> write memory / ERROR: Write memory is not permitted when switch is running in certified mode"
- 解法：`reload from working no rollback-timeout` 或 `modify running-directory working`。

## X4. AP 加入 AP Group 时其自身配置会被 PVM 覆盖删除
- <<<PAGE 243>>>
- 原文摘录："Warning：WHEN AN OMNIACCESS STELLAR ACCESS POINT GETS IN AN AP GROUP, ITS CONFIGURATION IS DELETED AND REPLACED BY THE CONFIGURATION SENT FROM THE PRIMARY VIRTUAL MANAGER (PVM) ACCESS POINT."
- 要点：多 AP 混部前务必先把目标配置做到 PVM，否则新入组 AP 的本地配置丢失。

## X5. R-Lab 交换机恢复出厂会破坏实验环境
- <<<PAGE 123>>>
- 原文摘录："Warning：DON'T TEST THE FOLLOWING PART ON YOUR LAB! THE SWITCHES THAT ARE USED IN OUR REMOTE-LAB ARE LOADED WITH A SPECIFIC DEFAULT CONFIGURATION. REINITIALIZING THEM TO THEIR FACTORY DEFAULT CONFIGURATION MAY LEAD TO ISSUES!"
- 通用原则：预配置设备（汇聚/核心/服务器）不要动出厂（另见 <<<PAGE 100>>> "DO NOT MANAGE AND CONFIGURE the core switch OS6900"、<<<PAGE 358>>> "DO NOT use the action Delete on your Organization"）。

## X6. AP 默认口令安全基线（8.10R3 警告 / R4 强制改密）
- <<<PAGE 64>>>-<<<PAGE 65>>>
- 原文摘录："Login : admin / Password : switch"；"Beginning in 8.10R3 a warning message will be displayed urging for the default password to be changed … Beginning in 8.10R4 changing the default password will be mandatory."

## X7. OVC4→OVC10 迁移：序列号不能同时在两个平台
- <<<PAGE 318>>>
- 原文摘录："The serial number of a network device cannot be declared in both OmniVista CIRRUS 4 and OmniVista CIRRUS 10. Make sure to remove all your equipment first"
- 迁移步骤：先在 OVC4 删除全部设备→OVC10 宣告→等 call home（AP 最长 30 分钟，交换机 30 分钟或重启 cloud-agent）。

## X8. call home 太慢 → 手动强制激活（推荐 disable force/enable 而非整机重启）
- <<<PAGE 331>>>、<<<PAGE 363>>>
- 原文摘录："cloud-agent admin-state disable force / cloud-agent admin-state enable … 或 reload from working no rollback-timeout"；cloud-agent.cfg 缺失时需 `cp /flash/cirrus/cloudagent.cfg /flash/working/cloudagent.cfg`（<<<PAGE 356>>> Warning）。

## X9. 改 VRRP priority 未先 disable → 配置不生效
- <<<PAGE 689>>>
- 原文摘录："Warning：THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY"

## X10. 端口有 VLAN/默认 VLAN 配置时无法加入 linkagg
- <<<PAGE 640>>>
- 原文摘录："-> linkagg lacp port 2/1/3 actor admin-key 8 / ERROR: Port cannot be added to Linkagg, please remove other configuration on this port"
- 解法：先 `no vlan XX members port …` 清干净再加入聚合。

## X11. DHL 与 STP 互斥 + MAC 老化风险（默认 mac-flushing=none）
- <<<PAGE 630>>>、<<<PAGE 642>>>
- 原文摘录："Problem: No topology change after changeover of DHL links … None (default): The staled MAC address entries are kept in the MAC table"；实验："Spanning Tree is disabled on all the DHL enabled ports"（<<<PAGE 642>>> Note）。
- 要点：生产建议显式配置 `dhl 1 mac-flushing raw`（或 mvrp），否则倒换后可能保留过期 MAC。

## X12. 802.11r 与旧终端兼容性：不支持的设备可能无法关联
- <<<PAGE 938>>>、<<<PAGE 940>>>
- 原文摘录："devices which do not support 802.11r may not be able to associate to a 802.11r WLAN, then ALE recommends set specific WLAN for devices supporting 802.11r, 802.11k and 802.11v"；"8158s and 8168s handsets reject the APs 802.11v request in their current version"（<<<PAGE 940>>>）
- 要点：按终端能力分 SSID；81x8s 话机当前版本忽略/拒绝 802.11v。

## X13. RAP 部署三禁区（总部勿用、带宽减半、同地两 RAP 无切换）
- <<<PAGE 904>>>
- 原文摘录："It is not recommanded to use RAP in headquarter due to VPN tunnel constraints … the expected encrypted performance with AP1201H configured as RAP is about 100Mbps while … 433Mbps … In case 2 RAPs are geographically collocated, 8168s handover between 2 RAPs is not supported."

## X14. 模式选错的规模/功能边界（Express 无 DPI 分析、AP1101 组规模腰斩）
- <<<PAGE 875>>>、<<<PAGE 826>>>
- 原文摘录："The voice application bandwidth control in Wifi-Express mode is managed directly by Stellar DPI, through the PVM … There no Voice analytics and Voice application visibility in Wifi-Express mode."（<<<PAGE 875>>>）；"One AP1101 only AP-Group supports up to 64 OmniAccess® Access points, 256 concurrent clients"（<<<PAGE 868>>>，低于 AP13XX 的 255/512）
- 要点：要语音可视化/大规模就必须 Enterprise/Cloud，选 Express 前核对 AP-Group 规模表。

## X15. Lightning Config 使用前提（顺序错了向导不触发）
- <<<PAGE 79>>>、<<<PAGE 1025>>>
- 原文摘录："The easy configuration process (lightning configuration) starts only if: Only first or second physical port connected with the client, no other ports connected • No prior switch configuration exist • No DHCP address assignment occurs after bootup • No remote configuration load (RCL) server and OmniVista NMS connection exists"；"Do not pre-cable the ALE switch to the network … Never connect an out-of-box ALE switch to another without running Lightning Config first"（<<<PAGE 1034>>>）
- 要点：保存配置后默认 IP 192.168.0.1 会被内部移除（<<<PAGE 79>>>）。

## X16. 2.4GHz 语音 + 信道聚合是反模式
- <<<PAGE 908>>>-<<<PAGE 909>>>、<<<PAGE 913>>>
- 原文摘录："HT40 configuration in the 2.4GHz radio band remains possible for a hot spot (using few APs) but is not adapted to a large deployment due to the 3-channels limitation"；"This implementation (Voice on 2.4GHz) is possible but not recommended as 2.4GHz radio band is prone to interferences from Bluetooth, microwave oven and intrusion radar"
- 要点：语音走 5GHz（802.11a/n/ac/ax），2.4GHz 信道聚合在多 AP 部署中会自扰。

## X17. Port Mirroring 与 Port Monitoring 不能同端口、镜像会话数有限
- <<<PAGE 554>>>、<<<PAGE 718>>>
- 原文摘录："Cannot use port monitoring and mirroring on same port"（<<<PAGE 554>>>）；"Port mirroring and monitoring cannot be configured on the same port"（<<<PAGE 718>>>）；6870 上镜像会话上限 2（<<<PAGE 568>>> "The maximum number of mirroring sessions is limited to two"），而部分新型号 8.9R3 提升到 4（<<<PAGE 552>>>）。
