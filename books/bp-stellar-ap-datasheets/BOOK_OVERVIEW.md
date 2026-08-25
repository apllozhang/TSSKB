# bp-stellar-ap-datasheets 书目总览

## 主题
ALE OmniAccess Stellar 无线接入点（AP）数据表合集，14 份文档覆盖 Wi-Fi 6（802.11ax）、Wi-Fi 6E（6GHz）到 Wi-Fi 7（802.11be）三代、室内/室外/墙面三大形态共 20+ SKU。蒸馏目标是"选型速查知识"：什么场景选哪个型号、上下行/供电/管制域边界。

## 文档映射

| DOC | 型号 | 页码 | Wi-Fi 代 | 形态 | 关键特征 |
|---|---|---|---|---|---|
| 1 | AP1261 | p1-5 | 11ac Wave2 | 室外 | IP67，1.2Gbps，2x2，802.3at 20W |
| 2 | AP1301 | p6-13 | Wi-Fi 6 | 室内 | 1.77Gbps，2x2，af 供电 13.1W |
| 3 | AP1301H | p14-21 | Wi-Fi 6 | 墙面(Hospitality) | 1+4 端口含 1 PSE、RJ45 直通、BLE/Zigbee |
| 4 | AP1331 | p22-29 | Wi-Fi 6 | 室内中高端 | 4x4+4x4，3.55Gbps，双 5GE 上联，专用扫描+BLE |
| 5 | AP1351 | p30-36 | Wi-Fi 6 | 室内高端 | 三射频 4x4+8x8+4x4，~10Gbps，双 10GE |
| 6 | AP1360 系列(1361/1361D/1362) | p37-47 | Wi-Fi 6 | 室外 | 4x4+2x2，~3Gbps，IP67，2.5GE+SFP+PSE 下联，外置天线版 1362 |
| 7 | AP1431 | p48-56 | Wi-Fi 6E | 室内 | 三频 2x2x3，4.2Gbps，双 2.5GE，BLE/Zigbee |
| 8 | AP1451 | p57-65 | Wi-Fi 6E | 室内高端 | 4x4+8x8+4x4，10Gbps，双 10GE，专用扫描 |
| 9 | AP1501 | p66-76 | Wi-Fi 7 | 室内入门 | 2x2x3，9.328Gbps，1x 2.5GE，af/at，DPGPSK |
| 10 | AP1511 | p77-86 | Wi-Fi 7 | 室内入门+ | 2x2x3+BLE/Zigbee，5GE 上联，MACsec，DPGPSK |
| 11 | AP1521 | p87-96 | Wi-Fi 7 | 室内中端 | 5GHz 4x4，12.2Gbps，10GE 上联，三频专用扫描，MACsec |
| 12 | AP1540 系列(1541/1542) | p97-107 | Wi-Fi 7 | 室内超高密 | 4x4x3，18.67Gbps，双 10GE+SFP+ combo，AFC/RFC，6G 软件切换 5G |
| 13 | AP1561 | p108-116 | Wi-Fi 7 | 室外 | 2x2x3，9.328Gbps，IP67，5GE 上联，仅 802.3at，AFC |
| 14 | AP1570 系列(1571/1572) | p117-128 | Wi-Fi 7 | 室外旗舰 | 2x2x3+扫描+BLE，10GE combo(RJ45/SFP+)，PSE 下联，bt 供电 50W，AFC |

## 蒸馏重点
1. **型号命名规律**：末位 1=内置天线、D=定向天线、2=外置天线接口（1361D/1362/1572）；x0x/x1x/x2x 低端、x3x+ 中高端（对应订阅分档）。
2. **代际对比**：Wi-Fi 6 → 6E（加 6GHz）→ Wi-Fi 7（MLO/4096-QAM/320MHz/MACsec）。
3. **供电降级逻辑**：bt 全功能 → at 关 USB → af 关端口降射频，是 PoE 预算设计的硬约束。
4. **管制域**（RW/US/ME）销售地域限制；6GHz 在部分域不可用时的软件切 5GHz 方案。
5. **管理规模**：Wi-Fi Express 集群 255 AP / OV2500 4K / Terra 5K / Cirrus 12K-30K。
