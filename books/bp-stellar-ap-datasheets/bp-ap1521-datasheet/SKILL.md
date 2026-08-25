---
name: AP1521 数据表速查（Wi-Fi 7 中端 5G 4x4 + 三频专用扫描）
description: 售前核对 ALE OmniAccess Stellar AP1521（12.2Gbps/10GE 上联/五射频/1280 客户端）规格与 at 供电进 degraded mode 的红线时使用。
source_book: bp-stellar-ap-datasheets（AP1521 p87-96）
---

## R（触发场景）
- Wi-Fi 7 中端主力：需要全时三频扫描防护（wIPS）+ BLE/Zigbee + MACsec + 10GE
- 与 1511 做预算/布线取舍（C7）；与 1540 做密度取舍
- at 供电部署核对 degraded mode 后果（X5）

## I（核心理念)
Wi-Fi 7 中端"五射频"：三服务射频（2.4G 2x2 + 5G 4x4 + 6G 2x2，聚合 12.2Gbps）+ 三频专用扫描射频 + BLE 5.4/Zigbee；1x 10GE PoE 上联（MACsec）+ 1x GE 上联/下联；必须 bt 40.2W，at 25W 直接进 degraded mode（X5/P14，<<<PAGE 87>>>/<<<PAGE 90>>>/<<<PAGE 92>>>）。

## A1（选型差异）
- vs AP1511：5GHz 2x2 升 4x4（12.2G 对 9.328G）、加三频扫描射频、10GE+GE 双口（对单 5GE）、1280 客户端（对 768）、必须 bt（1511 at 可跑）
- vs AP1540：1540 是 4x4x3 + 6G EHT320 11.52G + 18.67G + 双 10GE/combo SFP+ + 1536 客户端；1521 覆盖中高密，1540 超高密
- 判断口径：需要全时扫描防护 + 10GE 布线 + bt 预算三者齐备才选 1521（C7）

## A2（规格速查表）
| 项目 | 规格 | 页码 |
|---|---|---|
| 射频架构 | 五射频：6GHz 2x2:2（5.76G，2SS EHT320）+ 5GHz 4x4:4（5.76G，EHT160）+ 2.4GHz 2x2:2（688Mbps）+ 三频专用扫描（6/5/2.4GHz）+ BLE 5.4/Zigbee（6dBm/-93dBm，4.3dBi 天线） | <<<PAGE 90>>> |
| 聚合速率 | 12.2Gbps（688M@2.4G + 5.76G@5G + 5.76G@6G） | <<<PAGE 87>>> |
| MIMO/速率档 | MLO、OFDMA（含每客户端多非连续 RU 分配）、MU-MIMO、4096-QAM、512 压缩块确认、TxBF、FTM；EHT20-320 | <<<PAGE 88>>>/<<<PAGE 90>>> |
| 频段 | 2.4G/5G 四段/6GHz 四段 | <<<PAGE 90>>> |
| 以太网口 | 1x 多千兆 100M-10GE 上联 Eth0（802.3bt PoE，EEE，MACsec）+ 1x GE 上联/下联；USB 2.0 Type-C + console | <<<PAGE 90>>> |
| PoE/供电 | bt 40.2W：全功能；at 25W：degraded mode——射频保持 2.4G 2x2/5G 4x4/6G 2x2、上联降 2.5GE，扫描射频/IoT 射频/Eth1/USB 全关（X5） | <<<PAGE 92>>> |
| USB-IoT | 1x USB 2.0 Type C（5V 500mA） | <<<PAGE 90>>> |
| 蓝牙 | Bluetooth 5.4/Zigbee + FTM | <<<PAGE 90>>> |
| 天线 | 内置全向：4.6dBi @2.4G / 5.8dBi @5G / 6.4dBi @6G | <<<PAGE 91>>> |
| 发射功率 | 聚合 26dBm@2.4G / 26dBm@5G / 27dBm@6G；巴西 24dBm | <<<PAGE 90>>> |
| 工作温度 | 0°C ~ 45°C | <<<PAGE 92>>> |
| Mount | 吊顶/壁装，套件另购（AP-MNT-IN-BE/CE/WE） | <<<PAGE 92>>> |
| 容量 | 每射频 16 SSID；2.4G 256 + 5G 512 + 6G 512 客户端，合计 1280/AP | <<<PAGE 93>>> |
| 尺寸重量 | 210x210x43mm，1020g；MTBF 650,124h（74.22 年） | <<<PAGE 92>>> |
| 管理平台 | Terra 5K / Cirrus 12K / Express 集群 255；OV2500 兼容 4K；SNMP 仅 v2 | <<<PAGE 93>>> |
| 安全 | TPM 2.0、专用扫描射频无线防护、WPA3 CNSA/SAE、OWE、DPI、MACsec Eth0 | <<<PAGE 91>>> |
| 订购 | OAW-AP1521-RW（禁 US, Japan）/ -US | <<<PAGE 94>>> |

## E（适用场景）
- 中高密办公 Wi-Fi 7 主力：全时三频扫描 wIPS + BLE 定位 + MACsec 合规（C7，<<<PAGE 87>>>）
- 10GE 上联已布到桌面/楼宇的多千兆接入层
- 医疗/金融等安全要求高、需要专用扫描射频做无线防护的行业（<<<PAGE 91>>>）

## B（限制与坑）
- at 25W degraded mode（X5，<<<PAGE 92>>>）：扫描射频、IoT 射频、Eth1、USB 全关——安全与定位能力归零，必须 bt 40.2W
- SNMP 仅 v2（<<<PAGE 93>>>）；管理规模数字随版本增长需核实（X24）
- 无 combo 光口：光纤回传场景须上 1540/1570
- 吊装套件另购（X20，<<<PAGE 92>>>）
- 6GHz 射频无"切 5G"表述（数据表未写）：未开放域 6G 射频利用率需与 ALE 确认

来源：bp-stellar-ap-datasheets fulltext.md p87-96；verified.md C7/P14/P23/X5/X18/X20/X24/F5
