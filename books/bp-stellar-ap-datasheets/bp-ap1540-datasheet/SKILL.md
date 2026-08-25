---
name: AP1540 系列数据表速查（室内 Wi-Fi 7 超高密旗舰 18.67Gbps）
description: 售前为高密礼堂/会议厅选 AP1541 内置或 AP1542 外置 8x RP-SMA，核对 4x4x3/双 10GE combo SFP+/AFC/6G 切 5G 与 at 供电全频降 2x2 时使用。
source_book: bp-stellar-ap-datasheets（AP1540 series p97-107）
---

## R（触发场景）
- 高密礼堂/大会议室/教室/酒店公区 Wi-Fi 7 超高密：AP1541 内置 vs AP1542 外置怎么选（C2）
- 双 10GE + combo SFP+ 光口上联与 bt 51W 供电预算
- 6GHz 未开放国家/地区：软件切 5GHz 跑 2.4+5+5（C4）

## I（核心理念)
室内 Wi-Fi 7 超高密旗舰"五射频"：三服务射频全 4x4（6G 4x4 EHT320 达 11.52Gbps、5G 4x4、2.4G 4x4），聚合 18.67Gbps；全频扫描 + BLE 5.4/Zigbee；双 10GE（其一 combo SFP/SFP+）；AFC/RFC 合规，6GHz 射频软件可切 5GHz（P15/P16，<<<PAGE 97>>>/<<<PAGE 100>>>/<<<PAGE 101>>>）。

## A1（选型差异）
- AP1541 vs AP1542：1541 内置全向天线（标准高密：礼堂/教室/会议/酒店公区）；1542 8x RP-SMA 外置天线（高顶棚场馆/长走廊/仓库定向覆盖），天线 TBC 另购（X14）
- vs AP1521：1521 是 5G 4x4 + 其余 2x2、12.2G、单 10GE；1540 三频全 4x4、18.67G、双 10GE + 光口、1536 客户端、Cirrus 20K
- vs AP1570：室外形态选 1570；1540 是室内旗舰
- 供电红线：at 26.6W 三频全降 2x2、Eth1/SFP+/USB 关（X6）

## A2（规格速查表）
| 项目 | 规格 | 页码 |
|---|---|---|
| 射频架构 | 五射频：6GHz 4x4:4（11.52G，4SS EHT320，软件可切 5GHz High）+ 5GHz 4x4:4（5.76G，4SS EHT160）+ 2.4GHz 4x4:4（1.376G）+ 全频扫描 + BLE 5.4/Zigbee（6dBm/-93dBm） | <<<PAGE 101>>> |
| 聚合速率 | 18.67Gbps（1376.5M@2.4G + 5.76G@5G + 11.5G@6G） | <<<PAGE 97>>> |
| MIMO/速率档 | MLO、OFDMA（多非连续 RU）、MU-MIMO、4096-QAM、TxBF、FTM；EHT20-320；11be 到 6G EHT320 11529Mbps | <<<PAGE 98>>>/<<<PAGE 101>>> |
| 频段 | 2.4G/5G 四段/6GHz 四段 | <<<PAGE 101>>> |
| 以太网口 | combo 口 Eth0：10GE RJ45（802.3bt PoE）或 SFP/SFP+ 二选一；Eth1：1x 10GE RJ45（802.3bt，上联/下联）；USB 2.0 Type-C（5V 1A）+ console + Kensington 锁 | <<<PAGE 101>>> |
| PoE/供电 | bt 51W（单/双口）：全功能（双 bt 冗余、双 at 负载分担）；at 26.6W：Eth0 降 2.5GE、Eth1/SFP+/USB 关、三射频全降 2x2（扫描/IoT 射频保留）（X6） | <<<PAGE 103>>> |
| USB-IoT | 1x USB 2.0 Type C（5V 1A） | <<<PAGE 101>>> |
| 蓝牙 | Bluetooth 5.4/Zigbee（内置全向天线 4.5dBi）+ FTM | <<<PAGE 101>>> |
| 天线 | AP1541 内置全向：5.9dBi@2.4G / 5.3dBi@5G / 4.2dBi@6G；AP1542：8x RP-SMA 母头外置（4 个 2.4/5G + 4 个 5/6G，MIMO 4x4），天线 TBC 另购（X14） | <<<PAGE 102>>>/<<<PAGE 105>>> |
| 发射功率 | 聚合 29dBm@2.4G / 29dBm@5G / 28dBm@6G（全系列最高档）；巴西 24dBm | <<<PAGE 101>>> |
| 工作温度 | 0°C ~ 50°C | <<<PAGE 103>>> |
| Mount | 吊顶/壁装，套件另购（AP-MNT-IN-BE/CE/WE/WE2） | <<<PAGE 103>>> |
| 容量 | 每射频 16 SSID；1536 客户端 | <<<PAGE 103>>> |
| 尺寸重量 | 260x260x57.4mm，1950g；MTBF 554,332h（63.28 年） | <<<PAGE 103>>> |
| 管理平台 | Terra 5K / Cirrus 20K / Express 集群 255；SNMP 仅 v2 | <<<PAGE 104>>> |
| 安全 | TPM 2.0、WPA3 CNSA/SAE、OWE、DPI、双上联口均支持 802.1ae MACsec、DPGPSK、AFC/RFC 合规 | <<<PAGE 98>>>/<<<PAGE 100>>> |
| 订购 | OAW-AP1541-RW/-US、OAW-AP1542-RW/-US（1540 系列 RW 禁 US/Egypt/Japan） | <<<PAGE 105>>> |
| 配件 | POE60U-1BT-X-R；External antennas for AP1542 TBC | <<<PAGE 105>>> |

## E（适用场景）
- 普通高密（礼堂/大教室/会议/酒店公区）：AP1541 内置全向（C2，<<<PAGE 97>>>）
- 高顶棚场馆/长走廊/仓库定向覆盖：AP1542 外置天线自配波瓣（C2）
- 6GHz 未开放域：6G 射频软件切 5GHz，三射频跑 2.4+5+5，投资不打水漂（C4/P16，<<<PAGE 100>>>）
- 光纤上联楼宇：combo SFP+ 口直连（<<<PAGE 97>>>）

## B（限制与坑）
- at 26.6W：三频全降 2x2、Eth1/SFP+/USB 全关——旗舰变入门（X6，<<<PAGE 103>>>），必须 bt 51W
- AP1542 外置天线 "TBC" 未定型号另购（X14，<<<PAGE 105>>>）：报价注明不含天线
- 6GHz 未开放域室内标准功率 + 外置天线可能需频率协调（AFC/RFC，<<<PAGE 100>>>）
- SNMP 仅 v2（X12 关联，<<<PAGE 104>>>）
- 吊装套件另购（X20）；260mm 机身 1.95kg 承重核对
- 室外场景勿用：防护等级非 IP67（数据表标注 Indoor）

来源：bp-stellar-ap-datasheets fulltext.md p97-107；verified.md C2/C4/P15/P16/P23/P24/X6/X14/X18/X20/F5
