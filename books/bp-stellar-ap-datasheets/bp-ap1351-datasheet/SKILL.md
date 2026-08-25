---
name: AP1351 数据表速查（Wi-Fi 6 旗舰三射频 ~10Gbps）
description: 售前核对 ALE OmniAccess Stellar AP1351（5GH 8x8/双 10GE/五射频/1536 客户端/bt 45W）规格与 at 降级链时使用。
source_book: bp-stellar-ap-datasheets（AP1351 p30-36）
---

## R（触发场景）
- 超高密室内 Wi-Fi 6：大礼堂、开放密集办公、报告厅
- 接入层已备 10GE/bt，核对双 10GE 上联与 45W 供电预算
- 判断 1331 → 1351 的密度阶梯，或与 Wi-Fi 7 的 1540 对比（C6）

## I（核心理念)
Wi-Fi 6 室内旗舰"五射频"：三服务射频（5GHz High 8x8:8 + 5GHz Low 4x4:4 + 2.4GHz 4x4:4）+ 全频 1x1 专用扫描 + BLE/Zigbee；~10Gbps（9.6G@双 5G + 1.2G@2.4G），双 10GE 上联 PoE 冗余/负载分担（P，<<<PAGE 30>>>/<<<PAGE 33>>>）。5GHz 拆高低两段是它对抗高密的独门架构。

## A1（选型差异）
- vs AP1331：1331 是 4x4+4x4 双频 3.55G；1351 加第三个 5GHz 射频且 5GH 升 8x8，~10G、双 10GE、1536 客户端
- vs AP1451：1451 把第三频段换成 6GHz（6G 4x4 + 5G 8x8 + 2.4G 4x4，10Gbps），Wi-Fi 6E 版旗舰
- vs AP1540：要 Wi-Fi 7（4x4x3 + 6G EHT320 11.52G + 18.67G + combo SFP+）选 1540
- 供电红线：at 单口 24W 即三射频降 2x2（X2）

## A2（规格速查表）
| 项目 | 规格 | 页码 |
|---|---|---|
| 射频架构 | 三服务射频：5GHz High 8x8:8（4.8G，8SS HE80/4SS HE160）+ 5GHz Low 4x4:4（4.8G，4SS HE160）+ 2.4GHz 4x4:4（1.147G）；另全频 1x1 专用扫描 + BLE/Zigbee | <<<PAGE 33>>> |
| 聚合速率 | ~10Gbps（9.6G@5G + 1.2G@2.4G） | <<<PAGE 30>>> |
| MIMO/速率档 | HE20/40/80/160；11ac VHT20-160；OFDMA、MU-MIMO、1024-QAM、TWT、TxBF、ACC | <<<PAGE 33>>> |
| 以太网口 | 2x 多千兆 1/2.5/5/10GE 自动侦测，Eth0-Eth1，802.3bt PoE，EEE；Console | <<<PAGE 33>>> |
| PoE/供电 | bt 45W：全功能；双 at 42W：USB 关；at 24W：USB+Eth1 关且三射频降 2x2（X2） | <<<PAGE 34>>> |
| USB-IoT | 1x USB 3.0 Type A（5V 500mA） | <<<PAGE 33>>> |
| 蓝牙 | Bluetooth 5/Zigbee：6dBm（class 1）、-93dBm | <<<PAGE 33>>> |
| 天线 | 内置全向：3.9dBi @2.4G/5GH/5GL、BLE 3.5dBi | <<<PAGE 33>>> |
| 发射功率 | 聚合 24dBm@2.4G / 27dBm@5GH / 24dBm@5GL（每链 18dBm）；巴西 24/27dBm | <<<PAGE 33>>> |
| 工作温度 | 0°C ~ 45°C | <<<PAGE 34>>> |
| Mount | 吊顶/壁装，套件另购（AP-MNT-IN-BE/CE） | <<<PAGE 34>>> |
| 容量 | 每射频 8 SSID（24/AP），硬件就绪 16/射频（48/AP）；1536 客户端 | <<<PAGE 34>>> |
| 尺寸重量 | 260x260x60mm，2372g；MTBF 572,332h（65.33 年） | <<<PAGE 34>>> |
| 管理平台 | OV2500 4K / Express 集群 255 / Cirrus；SNMPv2+v3 | <<<PAGE 34>>> |
| 安全 | TPM 2.0、WPA3 CNSA/SAE、OWE*、DPI、wIPS/wIDS | <<<PAGE 33>>> |
| 订购 | OAW-AP1351-RW（禁 US/Egypt/Japan）/ -ME（Egypt/Israel）/ -US | <<<PAGE 35>>> |
| 配件 | POE60U-1BT-X-R（bt 60W 10G Midspan）、ADP-50GR BE | <<<PAGE 35>>> |

## E（适用场景）
- 超高密大礼堂/开放密集区：双 5GHz 拆段 + 8x8 高密度收敛（C6，<<<PAGE 30>>>）
- 需要双 10GE 上联 + PoE 冗余的核心区域布线（<<<PAGE 30>>>）
- 全时扫描 wIPS + BLE 定位都要的最高安全要求场所（<<<PAGE 30>>>）

## B（限制与坑）
- at 单口 24W 三射频降 2x2、Eth1/USB 关（X2，<<<PAGE 34>>>）：10G 旗舰必须 bt 45W
- SSID 软件档 8/射频（硬件就绪 16）：SSID 规划超 8 时确认软件版本（<<<PAGE 34>>>）
- OWE 硬件就绪待软件（X22，<<<PAGE 31>>>）
- 机身 260mm 见方 2.37kg：吊顶承重与吊装套件（另购，X20）提前确认
- 无 6GHz：频谱拥堵场景考虑 1451（6E）或 15xx（Wi-Fi 7）

来源：bp-stellar-ap-datasheets fulltext.md p30-36；verified.md C6/X2/X18/X20/X22/F3/F5/P27
