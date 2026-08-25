---
name: OmniSwitch 6575-MP16 数据表速查（IP67 壁挂工业加固）
description: 售前为轨旁/交通/室外轨旁小点位选型 OS6575-MP16（IP67 壁挂 16 口加固），核对 D-code/X-code 端口分配、120W PoE 预算、M23 双电源、Bypass 口与 VC 4 台限制时使用。
source_book: bp-omniswitch-datasheets（DOC 9 omniswitch_6575，p73-81）
---

![OmniSwitch 6575-MP16 数据表速查（IP67 壁挂工业加固） · 产品实物图（官方彩页）](images/omniswitch_6575.jpeg)
## R（触发场景）
- 轨道交通沿线、智能交通、智慧城市、电力等室外/壁挂小点位接入
- 需要 IP67 防护等级与 -40~75°C 全加固的 16 口小盒
- 端口 Bypass（旁路）功能保障链路故障不断业务的设计
- M23 6 针双电源输入与告警继电器接线规划

## I（核心理念)
OS6575-MP16 是"加固、全管理、无风扇的壁挂 GbE 交换机"（<<<PAGE 73>>>："ruggedized, fully manageable and fan-less... wall mountable switch"），IP67 整机防护、全系 60W bt PoE、全口 MACsec-256、M23 双电源、告警继电器。层级：工业加固接入小点位档，工业阵营（6465/6465T/6865）中防护等级最高的壁挂型。

## A1（与相邻系列选型差异）
- vs OS6465：6465 机柜 DIN/19"（IP44 级、VC 4 台）；6575 壁挂 IP67、单型号 16 口、路由能力更强（OSPF/IS-IS/BGP/VRF/SPB-M 内置，<<<PAGE 78>>>）。机柜内多口选 6465，轨旁小点位选 6575（C6）。
- vs OS6865：6865 是工业 L3 旗舰（-40~74°C、75W bt、SPB-M VPN、10G 上联 U28X）；6575 仅 60W、千兆环网，胜在 IP67 与 Bypass 口。
- 端口形态独特：D-code（M12 4 针 100M）/X-code（M12 8 针 1G）工业连接器，非 RJ45——布线成本与线缆定制要提前算。

## A2（规格细节速查表）
机型（单一型号，<<<PAGE 75>>>）：
| 端口组 | 数量 | 规格 |
|---|---|---|
| 100M D-code 无 PoE | 4 | 10/100 BaseT |
| 100M D-code PoE | 4 | 802.3at 30W |
| 1G X-code PoE | 4 | 10/100/1000，802.3bt 60W |
| 1G X-code Bypass | 4 | 10/100/1000，带旁路功能 |
上联与堆叠：无 SFP 上联（全铜口）；VC 最多 4 台 + 远程 VC 支持（<<<PAGE 74>>>）；远程 VC 最远 10 km 容错堆叠（<<<PAGE 77>>>）。
交换容量与包转发（<<<PAGE 75>>>）：17.6 Gb/s / 13.09 Mpps。
电源体系：M23 6 针连接器双电源输入（不支持热插拔，<<<PAGE 74>>>）；最大 PoE 预算 120W；Fast/Perpetual PoE 支持断电保持与秒级恢复（<<<PAGE 74>>>）。
Layer 特性（<<<PAGE 78>>>）：L3 内置 OSPFv2/v3、IS-IS、BGP v4（MP-BGP）、多 VRF + inter-VRF 路由泄漏、GRE/IP 隧道、PIM-SM/SSM/DM/BiDir/DVMRP；SPB-M + in-band management（<<<PAGE 79>>>）；G.8032 环保护、IEC 62439-2 MRP；8k IPv4 路由、32k MAC、4k VLAN（<<<PAGE 76>>>）；全口 MACsec-256（免费站点许可 OS-SW-MACSEC，<<<PAGE 81>>>）。
硬件平台：4GB flash、2GB RAM、无风扇（<<<PAGE 75>>>）。
功耗/环境：-40~75°C、IP67、2KV 浪涌、海拔 13000ft；待机 ~13W；MTBF 219k 小时（仅主机，<<<PAGE 75>>>）；尺寸 270x175x78mm、3.4kg，壁挂。
工业认证（<<<PAGE 76>>>/<<<PAGE 77>>>）：EN 50155/EN 61373（铁路）、NEMA TS-2（交通）、UL 61010、Class I Div 2 危险场所、IEC 60068 冲击振动。
规格红线：MTBF 仅 219k 小时（约 25 年 vs 6465 的 1.4M+）；无光口上联；交换容量小。

## E（适用场景）
- 轨旁/交通控制室外小盒子：IP67 + 壁挂 + 双电源 + 告警继电器（C6）
- 收费站 PTZ 摄像头/室外 AP 供电（60W bt + Fast/Perpetual PoE）
- 对业务连续性敏感的链路：4 口 Bypass 保证设备断电时链路直通
- 需要完整动态路由 + SPB 的小型工业环网（内置 OSPF/IS-IS/BGP，无需许可，对比 6570M/6360 的许可制）

## B（限制与坑）
- 路由表 8K IPv4 / MAC 32K——大路由表场景不适用（X7，<<<PAGE 76>>>）
- VC 最多 4 台（<<<PAGE 76>>>）——堆叠规模按 4 设计
- M23 双电源不支持热插拔（<<<PAGE 74>>>："not hot-swappable"）——换电源要断电窗口
- 无 SFP 光口——光纤上联必须另配光电转换或选 6465/6865
- MTBF 219k 小时明显低于同阵营（<<<PAGE 75>>>）——关键点位考虑备件
- M12 连接线缆需专用订购（M12-XC/M12-DC 系列，<<<PAGE 81>>>），普通 RJ45 线不能直连
- MACsec 需免费站点许可 OS-SW-MACSEC（<<<PAGE 81>>>）

来源：bp-omniswitch-datasheets DOC 9（p73-81，DID24062601EN June 2026）；verified.md C6/X7/P18/F1/F4
