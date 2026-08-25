---
name: AP1331 数据表速查（Wi-Fi 6 中高端 4x4+专用扫描）
description: 售前核对 ALE OmniAccess Stellar AP1331（3.55Gbps/双 5GE/四射频含专用扫描+BLE/TPM2.0）规格与 af 单口双射频降 1x1 的供电降级链时使用。
source_book: bp-stellar-ap-datasheets（AP1331 p22-29）
---

![AP1331 数据表速查（Wi-Fi 6 中高端 4x4+专用扫描） · 产品实物图（官方彩页）](images/ap1331.jpeg)
## R（触发场景）
- 中高密办公/开放区 Wi-Fi 6：需要专用扫描射频（全时 wIPS）+ BLE/Zigbee IoT 定位
- 接入交换机具备 5GE 多千兆 + bt/dual-at 供电，核对上联与 PoE 预算
- 判断 1301 → 1331 → 1351 的密度阶梯（C6）

## I（核心理念)
Wi-Fi 6 中高端"四射频"机型：2.4G 4x4 + 5G 4x4 双服务射频、1x1 全频段专用扫描射频、Bluetooth 5/Zigbee IoT 射频；3.55Gbps，双 5GE 上联提供 PoE 冗余与负载分担，TPM 2.0 起步标配（P5，<<<PAGE 22>>>/<<<PAGE 25>>>/<<<PAGE 26>>>）。

## A1（选型差异）
- vs AP1301：4x4 对 2x2、3.55G 对 1.77G、双 5GE 对双 GbE、加扫描+BLE+TPM；af 即全功能（1301）对必须 bt/dual-at（1331）
- vs AP1351：1351 是三服务射频旗舰（5GH 8x8、~10G、双 10GE、1536 客户端、bt 45W）；1331 覆盖中高密够用
- vs AP1521：要 Wi-Fi 7 同档（5G 4x4 + 扫描 + 10GE）看 1521（12.2G、MACsec、FTM）
- 供电红线是主要坑：af 单口直接双射频降 1x1（X1）

## A2（规格速查表）
| 项目 | 规格 | 页码 |
|---|---|---|
| 射频架构 | 四射频：5G 4x4:4（2.4Gbps，4SS HE80 或 2SS HE160/80+80）+ 2.4G 4x4:4（1.147Gbps，4SS HE40）+ 全频 1x1 专用扫描 + BLE/Zigbee | <<<PAGE 25>>> |
| 聚合速率 | 3.55Gbps（2.4G@5G + 1.15G@2.4G） | <<<PAGE 22>>> |
| MIMO/速率档 | HE20/40/80/160(80+80)、OFDMA、MU-MIMO、1024-QAM、TWT、TxBF、ACC；11ac 到 VHT160 | <<<PAGE 25>>> |
| 以太网口 | 2x 多千兆 1/2.5/5GE（802.3bz）Eth0-Eth1，PoE 冗余/负载分担，EEE；管理 Console RJ-45 | <<<PAGE 26>>> |
| PoE/供电 | bt 28W 或双 at：全功能；at 25W：USB 关；双 af 23W：USB+Eth1 关；af 12.5W：USB+Eth1 关且双射频降 1x1（X1） | <<<PAGE 27>>> |
| USB-IoT | 1x USB 3.0 Type A（5V 500mA） | <<<PAGE 26>>> |
| 蓝牙 | Bluetooth 5/Zigbee：6dBm（class 1）、-93dBm；BLE 天线 3.7dBi | <<<PAGE 25>>> |
| 天线 | 内置全向：3.9dBi @2.4G / 4.6dBi @5G；优化吊装水平朝向、最大增益下倾约 30° | <<<PAGE 26>>> |
| 发射功率 | 聚合 24dBm@2.4G / 24dBm@5G（每链 18dBm）；巴西 24dBm | <<<PAGE 25>>> |
| 工作温度 | 0°C ~ 45°C | <<<PAGE 27>>> |
| Mount | 吊顶/壁装，套件另购（AP-MNT-IN-BE/CE、OAW-AP-MNT-W） | <<<PAGE 27>>>/<<<PAGE 28>>> |
| 容量 | 每射频 16 SSID（总 32）；1024 客户端 | <<<PAGE 27>>> |
| 尺寸重量 | 210x210x40mm，985g；MTBF 572,332h（65.33 年） | <<<PAGE 27>>> |
| 管理平台 | OV2500 4K / Express 集群 255 / Cirrus；SNMPv2+v3 | <<<PAGE 27>>> |
| 安全 | TPM 2.0、WPA3 CNSA/SAE、OWE*、DPI、wIPS/wIDS | <<<PAGE 26>>> |
| 订购 | OAW-AP1331-RW（禁 US/Egypt/Japan）/ -ME（Egypt）/ -US | <<<PAGE 28>>> |
| 配件 | POE60U-1BT-X-R（bt 60W 10G Midspan）、ADP-50GR BE | <<<PAGE 28>>> |

## E（适用场景）
- 中高密办公/开放区/教室：4x4 双频 + 全时扫描防护 + BLE 定位一站齐（P5，<<<PAGE 22>>>）
- 需要 PoE 冗余的双上联布线（双 5GE 负载分担，<<<PAGE 22>>>）
- 医疗 RTLS（Stanley/Aeroscout）中等规模部署（<<<PAGE 27>>>）

## B（限制与坑）
- 供电降级链四级（X1，<<<PAGE 27>>>）：af 单口 12.5W 时双射频降 1x1——现网 af 交换机直接废一半性能，务必核对 PSE 等级
- OWE 仍是"硬件就绪待软件"（X22，<<<PAGE 23>>>）
- 吊装套件另购（X20，<<<PAGE 27>>>）
- at 25W 即关 USB：IoT 外设场景必须 bt 或双 at（<<<PAGE 27>>>）
- 无 6GHz：要 6G 频谱上 1431/1451（Wi-Fi 6E）或 15xx（Wi-Fi 7）

来源：bp-stellar-ap-datasheets fulltext.md p22-29；verified.md C6/P5/X1/X18/X20/X22/F3/F5
