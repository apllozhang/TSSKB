# principles 候选 — DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express

> 每条含页码引用 <<<PAGE N>>> 与原文摘录。共 42 条。

## P1. Wi-Fi 代际性能对比（Wi-Fi 4/5/6/6E/7）
- <<<PAGE 49>>>
- 原文摘录："Wi-Fi 4 … 802.11n 1.2 Gbps / Wi-Fi 5 … 3.5 / Wi-Fi 6 … 9.6 / Wi-Fi 7 … 46 Gbps；Security WPA2→WPA3；Channel width Up to 320 MHz；Modulation 4096-QAM, OFDMA；MIMO 16x16 MU-MIMO"
- 要点：速率、频段、加密、信道宽度、调制、MIMO 随代际演进的全表。

## P2. Wi-Fi 7 关键技术（MLO / 320MHz / 4096-QAM / MRU / AFC）
- <<<PAGE 48>>>
- 原文摘录："Wider Channel Bandwidth 320 MHz … MU-MIMO up to (16x16:16) … Multi-Link Operation (MLO) Reliability, Efficiency & Performance … 4096-QAM +20% raw speed increase … Automated Frequency Coordination (AFC)"
- 要点：Wi-Fi 7 五大增强及各自收益。

## P3. Wi-Fi 6 高效率技术（OFDMA / BSS Coloring / TWT / 扫描射频 / BLE-Zigbee）
- <<<PAGE 47>>>、<<<PAGE 910>>>-<<<PAGE 911>>>
- 原文摘录："Stellar WLAN brings integrated Bluetooth/Zigbee, dedicated Wi-Fi scanning radio technology"（<<<PAGE 47>>>）；"802.11ax: OFDMA access, BSS coloring, Additional Multi-User-MIMO streams downlink and uplink (up to 8), TWT (Target Wake Time)"（<<<PAGE 911>>>）

## P4. MU-MIMO 原理（MxN 定义与空间流复用）
- <<<PAGE 912>>>
- 原文摘录："802.11n technology has introduced the MIMO … 802.11ac/ax technologies enhance the MIMO with the ability to multiplex several users on each spatial stream … Multi-User MIMO is defined as MxN: e.g. 2x2, 3x3 and up to 4x4. M = number of transmit antennas, N = number of antennas at the receiver."
- 要点：话机 1x1 走视距+分集，MU-MIMO 客户端复用多径空间流。

## P5. PoE 标准演进与功率预算（802.3af/at/bt Type1-4）
- <<<PAGE 150>>>
- 原文摘录："802.3af PoE 12.95W@PD / 15.40W@PSE / 350mA；802.3at Type 2 PoE+ 25.50W / 30.0W / 600mA；802.3bt Type 3 51W / 60W / 600mA per pair；802.3bt Type 4 71W / 100W / 960mA per pair；Energy Management 三/四/六/八级 class"
- 要点：四档 PoE 的 PD 可用功率、PSE 供给功率、电流与供电等级完整对照。

## P6. PoE 端口优先级与断电顺序（Low/High/Critical）
- <<<PAGE 154>>>
- 原文摘录："Low: In the event of a power management issue, inline power to low-priority ports is interrupted first … Critical: inline power to critical ports is maintained as long as possible"
- 要点：功率不足时按 low→high→critical 顺序断电，默认 low。

## P7. PoE 动态分配原理（Dynamic PoE Allocation）
- <<<PAGE 150>>>
- 原文摘录："Dynamic PoE Allocation: Provide only the amount of power needed by powered devices (PD) up to the total energy budget for the most efficient power consumption possible"

## P8. Fast PoE / Perpetual PoE 原理
- <<<PAGE 147>>>-<<<PAGE 148>>>
- 原文摘录："Fast PoE … Allows the chassis to immediately provide PoE power to any connected device after powering up without waiting for the chassis to finish booting"；"Perpetual PoE … Provides uninterrupted power to the connected device (PD) even when the switch is restarting"
- 要点：两者都需升级 FPGA/CPLD；OS6360-P10A 不支持。

## P9. EEE 节能以太网（802.3az）
- <<<PAGE 149>>>
- 原文摘录："Protocol to allow chipset to go to a low power mode state when idle … EEE is only applicable to OmniSwitch copper ports operating at 100/1000 Mbps speed"，光口 U 型号不支持。

## P10. AOS 双分区启动判定规则
- <<<PAGE 126>>>、<<<PAGE 88>>>
- 原文摘录："The switch will reboot from certified directory if contents (images and vcboot.cfg) are different from the running directory … If contents are the same, the switch will reboot from the running directory"；"reload all" 无论何时都从 certified 启动（<<<PAGE 126>>> WARNING）
- 要点：冷启动默认比较 working 与 certified 内容决定启动目录；这是防"半配置"开机的回滚保护机制。

## P11. Certified 模式只读原理
- <<<PAGE 91>>>、<<<PAGE 129>>>
- 原文摘录："When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved and files cannot be moved between directories"；实测 "ERROR: Write memory is not permitted when switch is running in certified mode"（<<<PAGE 129>>>）

## P12. VLAN 间路由原理（IP interface 绑定 VLAN 即开路由）
- <<<PAGE 165>>>、<<<PAGE 512>>>
- 原文摘录："IP interfaces are associated with VLANs • IP routing is active as soon as at least one IP interface is associated with a VLAN -> ip interface <int_name> address <ip address/mask> vlan <vlan_id>"；"The operational status of a VLAN remains inactive as long as no active port is associated with this VLAN"（<<<PAGE 512>>>）
- 要点：网关即虚拟路由器端口；VLAN 无活动成员时 IP 接口 DOWN、不参与路由通告。

## P13. 802.1Q VLAN Tag 帧结构（12bit VID + 3bit 802.1p）
- <<<PAGE 169>>>、<<<PAGE 516>>>
- 原文摘录："802.3 MAC header change • 4096 unique VLAN Tags (addresses) … 802.1P Three bits field within 802.1Q header allows up to 8 different priorities"
- 要点：4 字节 tag = Ethertype + Priority + VID。

## P14. 物理端口恒有一个默认（untagged）VLAN 桥接
- <<<PAGE 599>>>
- 原文摘录："A PHYSICAL PORT ALWAYS HAS 1 VLAN (THE DEFAULT VLAN FOR THE PORT) THAT BRIDGES TRAFFIC (LEVEL 2)"

## P15. VLAN Mobile Tag 与 802.1Q Tag 的区别
- <<<PAGE 173>>>、<<<PAGE 793>>>
- 原文摘录："Mobile Tag: Allows mobile ports to receive 802.1Q tagged packets … Triggers dynamic assignment … 802.1Q Tag: Not supported on mobile ports … Statically assigns (tags) fixed ports"

## P16. UNP 动态 VLAN 分类规则优先级（Port/Domain/MAC/LLDP/IP/Tag）
- <<<PAGE 506>>>
- 原文摘录："UNP Port classification rules 1. Port/Linkagg 2. Domain 3. MAC address 4. MAC-OUI 5. MAC address range 6. LLDP 7. Auth-type 8. IP address 9. VLAN tag"

## P17. Stellar 默认出厂行为（mywifi SSID + 192.168.1.254 + Group ID 100）
- <<<PAGE 202>>>、<<<PAGE 205>>>
- 原文摘录："BROADCASTS A SSID 'MYWIFI-ABCD' … HAS THE IP@ = 192.168.1.254 … HTTP://<IP@ OF THE AP>:8080"；"Identical Group ID (Group ID 100) • Identical default VLAN (VLAN 1)"

## P18. Stellar 分布式控制面：空口+LAN 交换 RF/客户端上下文
- <<<PAGE 270>>>
- 原文摘录："Over the Air Exchange: Radio Frequency settings, Power, Channel, RSSI … Over the LAN Exchange: Roaming client's context, MAC addresses, Keys, Access Role Profiles"
- 要点：无控制器架构下 AP 间通过空口/LAN 同步 RF 决策与漫游上下文（CNCS）。

## P19. Stellar L3 漫游原理（Home AP + L2 GRE 隧道）
- <<<PAGE 894>>>、<<<PAGE 843>>>
- 原文摘录："A mobile IP Tunnel (L2 GRE) is created between the two AP groups by the 'New associated AP3', to the Home AP2"；"Stellar allows automatically the tunneling of client traffic from the Home AP … keeping all policies including QoS and security ACLs maintained"
- 要点：跨子网漫游时新 AP 到 Home AP 建 GRE 隧道，用户 IP 不变。

## P20. 802.11r/k/v 快速漫游机制
- <<<PAGE 938>>>-<<<PAGE 940>>>、<<<PAGE 127>>>（附录页码同 <<<PAGE 938>>> 段）
- 原文摘录："802.11r -Fast Transition (FT) … allows the client-AP handshake and key exchange with new AP to be done before the client roams"；"802.11k standard allows clients to request reports containing information about known neighbor APs"；"802.11v – BSS Transition Management … AP will try to assist in the roaming decision making"
- 要点：over-the-air FT 为默认模式；11k 邻居报告省去全信道扫描；11v 由 AP 主动建议漫游目标；不支持 11r 的终端可能无法关联 11r WLAN，需分 SSID。

## P21. 语音小区规划 RSSI 门限（-70dBm 覆盖 / -62~-64dBm 漫游 / 8dB 重叠）
- <<<PAGE 928>>>-<<<PAGE 931>>>
- 原文摘录："a -70 dBm RSSI (or better) is required … generally a -62dBm RSSI (or better) is required to ensure a correct roaming"；"The APs should be placed to overlap their boundaries by approximately 8 dB"；"SNR 25 dB or better, Noise level < -92 dBm, RSSI > -67 dBm"

## P22. 智能手机 EIRP 不对称问题
- <<<PAGE 931>>>
- 原文摘录："Smartphones set generally lower EIRP than APs in 5 GHz band … with only 11dBm … the RF range provided by the iPhone is much shorter than the Access Point RF range (EIRP here is 8 times lower)"
- 要点：降低 AP 功率匹配手机不可取（AP 数量暴涨）；手机 VoWLAN 只能 Best Effort。

## P23. WMM/DSCP/802.1p QoS 映射（Voice=EF46/6, Video=4, BE=0）
- <<<PAGE 874>>>、<<<PAGE 932>>>
- 原文摘录："Voice: DSCP 46 (48,56) → 802.1p 6；Video: 40 → 4；Best effort: 0 → 0；Background: 8 → 1"；话机侧 "a DSCP value of 46 is recommended for the Voice traffic and a value of 26 is recommended for the Voice signaling"（<<<PAGE 933>>>）

## P24. VoWLAN 质量门限（MOS≈4 的网络指标）
- <<<PAGE 933>>>、<<<PAGE 1007>>>
- 原文摘录："Network round trip delay must be less than 250 ms • 802.11 retransmissions should be kept under 15% • Jitter must be less than 100 ms • Packet loss must be less than 2%"；MOS 表：4=Good R-value 80-90（<<<PAGE 1008>>>）

## P25. 语音 AP 容量基准（每 AP 并发语音流 / 带宽）
- <<<PAGE 892>>>
- 原文摘录："All Stellar AP13XX in 11ax: 14Mbps (400Kbps per user) … Up to 35 Voice streams (18)；All Stellar AP12XX in 11ac: 13Mbps … Up to 32 Voice streams (16)；Rainbow Audio/Video HD: Up to 105Mbps (3Mbps) / 35 streams"
- 要点：G.711/Opus NB 编码下各代 AP 的语音容量对照。

## P26. 网状/桥接带宽衰减规律（4 跳/4 方向、每 mesh 点 /4）
- <<<PAGE 899>>>
- 原文摘录："4 voice mesh hops max - the bandwidth will be divided by 3 when reaching a mesh point … 4 voice mesh directions max - … equivalent to the mesh root AP bandwidth divided by 4 … Max transit capacity of about 15 8158s/8168s per root AP"
- 要点：Mesh 拓扑中 VoIP 只能 Best Effort（11r/PMK key 处理限制）。

## P27. Virtual Chassis 原理（VFL 互联=单逻辑交换机，ISIS-VC 拓扑管理）
- <<<PAGE 468>>>、<<<PAGE 471>>>
- 原文摘录："Virtual Chassis = Group of switches which appears as a single router or bridge • No STP/VRRP between Access and Core switches • Upgrade via ISSU • No license needed"；"VC topology managed by ISIS-VC … Maintains a loop-free topology for BUM traffic"
- 要点：Master 选举顺序：最高 priority → 最长 uptime（>10min 差）→ 最小 chassis ID → 最小 MAC（<<<PAGE 472>>>）。

## P28. VC 分裂（Split Chassis）双检测机制（RCD out-of-band + VSCP in-band）
- <<<PAGE 476>>>-<<<PAGE 477>>>
- 原文摘录："Out of Band: EMP Remote Chassis Detection (RCD) … The former Slave chassis will shutdown all its front-panel user ports to prevent duplicate IP and chassis MAC addresses"；"In Band: VC Split Protocol … requires an upstream or downstream device to act as helper switch"

## P29. ISSU 原理（逐台 slave 升级、最小中断）
- <<<PAGE 478>>>
- 原文摘录："Used to upgrade the software on a VC with minimal network disruption • Each element is upgraded individually … The Slaves are then reloaded from the ISSU directory in order from lowest to highest chassis ID"

## P30. STP 模式与协议（flat/per-vlan × STP/RSTP/MSTP）
- <<<PAGE 604>>>
- 原文摘录："Supports two Spanning Tree operating modes: flat (single STP instance per switch), per-VLAN … (By default on OmniSwitch)；STP (802.1d): Convergence time : 50 secs；RSTP (802.1w): < 1 sec；MSTP (802.1s)"

## P31. STP 1x1 负载分担原理（按 VLAN 改 priority 分根桥）
- <<<PAGE 606>>>、<<<PAGE 622>>>
- 原文摘录："per vlan (1x1) - load balancing … To take advantage of the 1x1 mode and provide load-balancing, it may be necessary to modify bridge priority"；示例：6870 为 VLAN 20 根、6860 为 VLAN 30 根。

## P32. LACP 动态聚合原理（actor admin key 关联端口）
- <<<PAGE 576>>>、<<<PAGE 588>>>
- 原文摘录："Dynamic: IEEE 802.3ad LACP • LACP will negotiate the optimal parameters for both ends using LACPDU … Static: Only works between Alcatel-Lucent OmniSwitches"；"the actor admin key has local significance only"（<<<PAGE 588>>> Note）

## P33. 负载分担哈希算法（brief vs extended）
- <<<PAGE 583>>>
- 原文摘录："Brief Mode: UDP/TCP ports not included … Extended: UDP/TCP ports to be included in the hashing algorithm → more efficient load balancing"；默认值：6900/6465/6360 brief，其余 extended。

## P34. DHL Dual-Home Link Active-Active 原理（按 VLAN 划分活跃链路防环）
- <<<PAGE 628>>>-<<<PAGE 630>>>
- 原文摘录："DHL Active-Active splits VLANs between two active links • The forwarding status of each VLAN is modified by DHL to prevent network loops"；"Spanning Tree is automatically disabled on DHL ports"；MAC flushing 三选项 RAW Flooding / MVRP Enhanced / None（默认）

## P35. VRRP 原理（虚拟 MAC 00-00-5E-00-01-VRID、多 VRID 负载分担）
- <<<PAGE 674>>>-<<<PAGE 675>>>
- 原文摘录："Virtual MAC address: 00-00-5E-00-01-{VRID} … Multicast 224.0.0.18"；"Two virtual routers with their hosts splitting traffic between them"（<<<PAGE 675>>>）
- 要点：修改 priority 前必须先 disable 实例（<<<PAGE 689>>> Warning）。

## P36. DHCP Option 138/43 与 AP 云注册
- <<<PAGE 280>>>、<<<PAGE 877>>>（troubleshooting 138/43）
- 原文摘录："Enable DHCP standard options: 1, 2, 6, 28, 42, 43. And, when using proxy: 129, 130, 131, 132, 133, 138"；"The DHCP Server sends the OmniVista IP address to the Stellar AP via a specific option (138/43)"（<<<PAGE 377>>>）

## P37. Loopback0 接口用途（管理面稳定源地址）
- <<<PAGE 659>>>
- 原文摘录："Identify a consistent address for network management purposes • Not bound to any VLAN • Always remain operationally active … Use: RP in PIMSM, sFlow Agent IP address, Source IP of RADIUS authentication, NTP Client, BGP peering, OSPF router-id, Switch and Traps Identification"

## P38. QoS Policy 三件套（condition + action + rule）
- <<<PAGE 699>>>
- 原文摘录："A policy (or a policy rule) is made up of: 1. a condition 2. an action"；condition 可达 L1-L4（source port/MAC/VLAN/IP/DSCP/TCP-UDP port），action 含 disposition accept|drop|deny、priority、bandwidth、mirror、redirect。
- 要点：qos apply 才下发硬件；规则默认 accept 不匹配流量。

## P39. ACL 安全组（UserPorts/DropServices/Port Disable）
- <<<PAGE 739>>>-<<<PAGE 740>>>
- 原文摘录："UserPorts … Used by default to prevent spoofed IP addresses on ports … -> qos user-port {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|vrrp|…}"；DropServices 保留服务组可按服务丢包；port-disable 命中即管理关闭端口。

## P40. LLDP-MED 网络策略 TLV（语音 VLAN + L2 priority + DSCP 自动下发）
- <<<PAGE 787>>>-<<<PAGE 794>>>
- 原文摘录："-> lldp network-policy 1 application voice vlan 151 l2-priority 5 dscp 46 … Switch send a LLDP Frame"；"MED: Power and Capability, Inventory Management, Network Policy"；实例 "unp profile 'voip-temp' mobile-tag … lldp med-endpoint ip-phone classification"（<<<PAGE 794>>>）
- 要点：IP 话机上电经 LLDP-MED 自动获得语音 VLAN/QoS，配合 UNP mobile-tag 动态入 VLAN。

## P41. 漫游判定逻辑（CNC 表判定 L2/L3 漫游）
- <<<PAGE 917>>>
- 原文摘录："Client Network Context exists? … Client Ntw Context VLAN Id = AP Access Role VLAN Id? Yes → Layer 2 roaming / No → Layer 3 roaming"

## P42. RAP（Remote AP）两种模式（Tunnel / Local breakout）
- <<<PAGE 904>>>
- 原文摘录："Tunnel mode: all traffic between Remote AP and VPN VA goes through a VPN tunnel … Local breakout: Traffic between 2 users at remote location remains local"；"expected encrypted performance with AP1201H configured as RAP is about 100Mbps while the same … in headquarter has about 433Mbps"
- 要点：RAP 不建议部署在总部；两台 RAP 同地不支持 8168s 互相切换（handover）。
