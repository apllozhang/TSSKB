---
name: AP1301H 数据表速查（酒店墙面 Wi-Fi 6 一口多用）
description: 售前为酒店/病房/宿舍客房墙面覆盖选 ALE OmniAccess Stellar AP1301H（1 上联+4 下联含 1 口 af PSE+RJ45 直通+BLE/Zigbee），核对 at 25W 才开 PSE 等供电边界时使用。
source_book: bp-stellar-ap-datasheets（AP1301H p14-21）
---

![AP1301H 数据表速查（酒店墙面 Wi-Fi 6 一口多用） · 产品实物图（官方彩页）](images/ap1301h.jpeg)
## R（触发场景）
- 酒店/病房/教室/宿舍/诊室/远程办公房间：一张 AP 解决房间 Wi-Fi + IPTV 供电 + IP 话机 + 模拟话机直通（C5）
- 核对 OAW-AP1301H-RW/ME/US 规格与单 gang 86mm 墙盒安装
- 客房要 BLE/Zigbee IoT 定位（门锁、手环）但不想加网关

## I（核心理念）
酒店客房专用墙面 Wi-Fi 6：双频 2x2 1.77Gbps + 集成 Bluetooth/Zigbee 射频，接口形态是卖点——1x GbE 上联 + 4x GbE 下联（其中 1 口 802.3af PSE 给 IPTV 等下联设备供电）+ 一对 RJ-45 直通口（模拟话机）+ USB 2.0（P3，<<<PAGE 14>>>）。容量翻倍于 AP1301：1024 客户端、每射频 16 SSID（P4，<<<PAGE 19>>>）。

## A1（选型差异）
- vs AP1301：同速率代际；1301H 多 4 下联 + PSE + 直通对 + BLE5 + 容量 1024（1301 为 512），面向房间级而非开放办公
- vs AP1331：1331 面向中高密开放区（4x4、双 5GE、扫描射频）；1301H 面向单房间多业务接入
- 下代墙面：暂无 Wi-Fi 7 墙面对应型号，客房 Wi-Fi 7 需求通常用 AP1501/1511 吸顶+面板替代方案

## A2（规格速查表）
| 项目 | 规格 | 页码 |
|---|---|---|
| 射频架构 | 双射频：5GHz ax 2x2:2（1.2Gbps，2SS HE80）+ 2.4GHz ax 2x2:2（573Mbps，2SS HE40） | <<<PAGE 17>>> |
| 聚合速率 | ~1.77Gbps | <<<PAGE 14>>> |
| MIMO/速率档 | DL/UL MU-MIMO、OFDMA、1024-QAM、BSS Coloring、ER、TWT、TxBF；ACC 蜂窝共存 | <<<PAGE 15>>>/<<<PAGE 17>>> |
| 以太网口 | 上联 1x GbE（at/af）；下联 1x GbE PSE（802.3af 输出）+ 3x GbE；一对无源 RJ-45 直通（背/底） | <<<PAGE 17>>> |
| PoE/供电 | at 25W：全功能（PSE 开）；af 12.7W：Eth1 PSE 关闭（X8）；DC 48V±5% 优先 | <<<PAGE 19>>> |
| USB-IoT | 1x USB 2.0 Type C（5V 500mA） | <<<PAGE 17>>> |
| 蓝牙 | Bluetooth 5 / Zigbee：6dBm（class 1）、-93dBm；内置 BLE 天线 3.2dBi | <<<PAGE 17>>>/<<<PAGE 18>>> |
| 天线 | 内置全向 2x2：3.92dBi @2.4G / 4.41dBi @5G | <<<PAGE 18>>> |
| 发射功率 | 聚合 21dBm（每链 18dBm）；巴西 21dBm | <<<PAGE 17>>> |
| 工作温度 | 0°C ~ 45°C | <<<PAGE 19>>> |
| Mount | 随附墙面套件（single gang 86mm 墙盒）；可选桌面套件 AP-MNT-DSK-B | <<<PAGE 19>>>/<<<PAGE 20>>> |
| 容量 | 每射频 16 SSID（总 32）；1024 客户端 | <<<PAGE 19>>> |
| 尺寸重量 | 86x29x162.5mm，320g；MTBF 1,314,000h（150 年） | <<<PAGE 19>>> |
| 管理平台 | OV2500 4K / Express 集群 255 / Cirrus；SNMPv2+v3 | <<<PAGE 19>>> |
| 安全 | WPA3 Enterprise CNSA/Personal(SAE)、OWE*、DPI、wIPS/wIDS、PSE 独立 LED | <<<PAGE 18>>>/<<<PAGE 15>>> |
| 订购 | OAW-AP1301H-RW（禁 US/Egypt/Japan）/ -ME（Egypt/Israel）/ -US | <<<PAGE 20>>> |

## E（适用场景）
- 酒店客房：Wi-Fi + IPTV（PSE 口）+ IP 话机（下联）+ 模拟话机（直通对）一机四用（C5，<<<PAGE 14>>>）
- 病房/宿舍/教室/远程办公房：房间级全覆盖 + BLE 门锁/手环定位（<<<PAGE 14>>>）
- GuestOperator 角色给前台自助开访客账号（<<<PAGE 16>>>）

## B（限制与坑）
- af 供电（12.7W）时 Eth1 PSE 关闭（X8，<<<PAGE 19>>>）：靠 AP 给 IPTV 供电的项目必须按 at 25W 预算
- OWE 硬件就绪、待软件更新（X22，<<<PAGE 15>>>）
- 上联单 GbE：4 下联 + 无线共享 1G 回程，全占用时带宽要算
- MTBF 150 年是标称值，选型宣传可用但别当承诺（<<<PAGE 19>>>）
- 管制域：1301H-RW 禁 US/Egypt/Japan，ME 版域为 Egypt/Israel（<<<PAGE 20>>>）
- 墙面套件默认附带（X20 的例外机型之一）；桌面套件另购

来源：bp-stellar-ap-datasheets fulltext.md p14-21；verified.md C5/P3/P4/P25/X8/X18/X20/X22
