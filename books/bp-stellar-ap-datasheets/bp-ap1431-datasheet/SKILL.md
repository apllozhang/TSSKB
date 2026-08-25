---
name: AP1431 数据表速查（Wi-Fi 6E 三频入门 2x2x3）
description: 售前核对 ALE OmniAccess Stellar AP1431（4.2Gbps/6GHz HE160/双 2.5GE/bt 34W/多频滤波器）规格与 6GHz SSID 限 4 个等边界时使用。
source_book: bp-stellar-ap-datasheets（AP1431 p48-56）
---

![AP1431 数据表速查（Wi-Fi 6E 三频入门 2x2x3） · 产品实物图（官方彩页）](images/ap1431.jpeg)
## R（触发场景）
- 6GHz 频谱干净的 Wi-Fi 6E 首次引入：中高密办公升级到三频
- 核对双 2.5GE 上联与 bt 34W 供电；at 25W 会关 USB
- 6GHz SSID 数量规划（每射频 16，但 6GHz 限 4）

## I（核心理念)
Wi-Fi 6E 三频入门：2.4G/5G/6G 各 2x2（6GHz 支持 HE160 到 2.4Gbps），聚合 4.2Gbps，四射频（三服务 + BLE/Zigbee）；内置多频段滤波器（multi-band filter）让 5G/6G 全信道无限制运行——这是 6E 机型关键卖点（P9，<<<PAGE 48>>>）。双 2.5GE 上联提供 PoE 冗余。

## A1（选型差异）
- vs AP1301/1331（Wi-Fi 6）：1431 的价值就是 6GHz 第三频段（HE160、干净频谱）；射频规格仍是 2x2 档
- vs AP1451：1451 是 6E 旗舰（6G 4x4 + 5G 8x8 + 扫描射频 + 双 10GE + 10Gbps）；1431 无专用扫描射频
- vs AP1501（Wi-Fi 7 入门）：同价位档，1501 速率 9.328G 更高（be/EHT320），但砍 BLE 且单口；要 IoT + 6G 频谱 + 双口冗余选 1431

## A2（规格速查表）
| 项目 | 规格 | 页码 |
|---|---|---|
| 射频架构 | 四射频：6GHz High 2x2:2（2.4Gbps，2SS HE160）+ 5GHz 2x2:2（1.2Gbps，2SS HE80）+ 2.4GHz 2x2:2（574Mbps，2SS HE40）+ BLE/Zigbee | <<<PAGE 51>>> |
| 聚合速率 | 4.2Gbps（574M@2.4G + 1.2G@5G + 2.4G@6G） | <<<PAGE 48>>> |
| 频段 | 2.400-2.4835 / 5.150-5.850 四段 / 6GHz 四段（5.925-7.125） | <<<PAGE 51>>> |
| MIMO/速率档 | HE20/40/80/160；OFDMA、MU-MIMO、1024-QAM、TWT、TxBF、ACC | <<<PAGE 51>>> |
| 以太网口 | 2x 多千兆 2.5/1GE 自动侦测 Eth0-Eth1，PoE 802.3bt；Console | <<<PAGE 51>>> |
| PoE/供电 | bt 34W 或双 at：全功能；at 25W：USB 关（X4）；DC 48V±5% 优先 | <<<PAGE 52>>> |
| USB-IoT | 1x USB 3.0 Type A（5V 1A） | <<<PAGE 51>>> |
| 蓝牙 | Bluetooth 5/Zigbee：6dBm（class 1）、-93dBm；内置全向天线 4.1dBi | <<<PAGE 51>>> |
| 天线 | 内置全向：4.1dBi @2.4G / 4.5dBi @5G / 4.7dBi @6G | <<<PAGE 52>>> |
| 发射功率 | 聚合 25dBm @2.4G/5G/6G（每链 18dBm）；巴西 24dBm | <<<PAGE 51>>> |
| 工作温度 | 0°C ~ 45°C | <<<PAGE 53>>> |
| Mount | 吊顶/壁装，套件另购（AP-MNT-IN-BE/CE、OAW-AP-MNT-W，注明适用 14xx） | <<<PAGE 53>>>/<<<PAGE 54>>> |
| 容量 | 每射频 16 SSID（6GHz 限 4）（X13）；每射频 512 客户端 | <<<PAGE 53>>> |
| 尺寸重量 | 210x210x40mm，1020g；MTBF 838,108h（95.67 年） | <<<PAGE 53>>> |
| 管理平台 | OV2500 4K / Express 集群 255 / Cirrus；SNMPv2+v3 | <<<PAGE 53>>> |
| 安全 | TPM 2.0、WPA3 CNSA/SAE、OWE（已支持）、DPI、wIPS/wIDS | <<<PAGE 52>>> |
| 订购 | OAW-AP1431-RW（禁 US, Japan——注意 6E 代埃及限制收窄）/ -US | <<<PAGE 54>>> |
| 配件 | POE60U-1BT-X-R、ADP-50GRBD（48V/30W） | <<<PAGE 54>>> |

## E（适用场景）
- 5GHz 拥堵、终端开始支持 6GHz 的企业：三频分流（P9，<<<PAGE 48>>>）
- 需要多频滤波器保证 5G/6G 全信道可用的管制复杂地区（<<<PAGE 48>>>）
- BLE/Zigbee IoT + Wi-Fi 一体的中等密度办公

## B（限制与坑）
- 6GHz SSID 硬限制 4 个（X13，<<<PAGE 53>>>）：6G 多 SSID 规划前必须核对
- 无专用扫描射频：全时 wIPS 防护没有，只能 part-time（对比 1451）
- at 25W 关 USB（X4，<<<PAGE 52>>>）
- 6GHz 空口取决于管制域开放情况；未开放域 6G 射频闲置（对比 Wi-Fi 7 代可软切 5G）
- 吊装套件另购（X20，<<<PAGE 53>>>）；RW 版禁售名录写 "US, Japan"（埃及已不在，X18 演进）

来源：bp-stellar-ap-datasheets fulltext.md p48-56；verified.md P9/X4/X13/X18/X20/F1
