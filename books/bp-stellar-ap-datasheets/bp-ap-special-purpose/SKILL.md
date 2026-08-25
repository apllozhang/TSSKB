---
name: Stellar 特殊用途 AP 选型（AP1301H 墙面 / AP1360 室外 / 外置天线 / 老代室外）
description: 售前为酒店病房墙面覆盖（AP1301H 一口多用）、室外补盲定向（AP1361/1361D/1362）、老室外站替换（AP1261）、医疗 RTLS 定位等特殊场景选型时使用。
source_book: bp-stellar-ap-datasheets（AP1261 p1-5 / AP1301H p14-21 / AP1360 系列 p37-47）
---

## R（触发场景）
- 酒店/病房/宿舍/教室墙面覆盖：一张 AP 解决 Wi-Fi+IPTV 供电+IP 话机+模拟话机
- 室外补盲/定向覆盖：全向/定向/外置天线三形态取舍
- 室外 AP 需 SFP 长距回传 + 给下联设备反向供电
- 医疗 RTLS 资产追踪：BLE/Zigbee + FTM 选型
- 老室外 11ac 站点替换评估（AP1261）

## I（核心理念）
特殊形态三件套：AP1301H 是"墙面一口多用"（1 GbE 上联 + 4 GbE 下联含 1 口 af PSE 供 IPTV + RJ45 直通对接模拟话机 + USB + BLE/Zigbee，单 gang 86mm 墙盒，P3，<<<PAGE 14>>>）；AP1360 系列是"室外三天线形态 + 多千兆 + bt 64W 反向供电"（全向 1361 / 定向 1361D H80°xV80° / 外置 6x N 头 1362 含 6KA 防雷，2.5GE+SFP+GbE PSE，P7/P8，<<<PAGE 37>>>/<<<PAGE 40>>>/<<<PAGE 42>>>）；AP1261 是室外 11ac Wave2 老将（1.2G/IP67/at 20W，升级看 1360/1561，P1，<<<PAGE 1>>>）。定位能力分级：老代靠 BLE/Zigbee，Wi-Fi 7 代加 FTM 精确测距（C9，<<<PAGE 11>>>/<<<PAGE 80>>>）。

## A1（行动框架）
1. 墙面场景（1301H）：核对房间终端清单——Wi-Fi+IPTV+IP 话机+模拟话机一张卡板全包；供电必须 at 25W（af 时 Eth1 PSE 关闭）
2. 室外场景（1360 系）：覆盖形态选天线（全向/定向/外置）；要 SFP 长距回传+PSE 下联供电选本系列；bt Type4 才能下联输出 at 30W
3. 老室外替换（1261→1360/1561）：1261 无 USB/无第二口/无 BLE、仅 384 客户端
4. 定位项目：医疗 RTLS 全线支持 Stanley Healthcare/Aeroscout；高精度优先 Wi-Fi 7 代（1511 起 FTM）

## A2（选型速查表）
| 型号 | 形态 | 速率 | 端口 | 供电 | 定位/备注 | 页码 |
|---|---|---|---|---|---|---|
| AP1301H | 墙面（单 gang 86mm） | 1.77G | 1 GbE 上联+4 GbE 下联（1 口 af PSE）+RJ45 直通对+USB | at 25W（af 12.7W 时 PSE 关） | BLE/Zigbee；1024 客户端；MTBF 150 年 | <<<PAGE 14-19>>> |
| AP1361 | 室外全向 | ~3G | 2.5GE 上联+SFP+GbE PSE 下联 | bt 64W | beamforming 12.5dBi@5G；IP67 | <<<PAGE 37-42>>> |
| AP1361D | 室外定向 | ~3G | 同上 | 同上 | H80°xV80°，走廊/街面 | <<<PAGE 41>>> |
| AP1362 | 室外外置天线 | ~3G | 同上 | 同上 | 6x N 头自配增益；6KA 防雷免避雷器 | <<<PAGE 41>>> |
| AP1261 | 室外 11ac Wave2 | 1.2G | 1x GbE | at 20W | 无 USB/无 BLE；384 客户端；IP67 | <<<PAGE 1-4>>> |
| PSE 输出阶梯（1360） | bt Type4=ENET1 at PSE；bt Type3=af PSE；at=关 PSE/USB | | | <<<PAGE 42>>> | | |

## E（选型决策案例）
- 酒店病房：AP1301H 一张 AP 解决房间 Wi-Fi+IPTV 供电+IP 话机+模拟话机直通；注意 at 供电才开 PSE（C5，<<<PAGE 14>>>/<<<PAGE 19>>>）
- 室外补盲：全向选 1361、定向（走廊/街面）选 1361D、自配增益+防雷选 1362；需要 SFP 长距回传+下联供电选本系列而非 1561/1570（C8，<<<PAGE 40>>>/<<<PAGE 41>>>）
- 医疗 RTLS：全线支持 Stanley/Aeroscout；定位精度高的资产追踪优先 1511/1540（FTM），老代靠 BLE/Zigbee（C9，<<<PAGE 11>>>/<<<PAGE 80>>>）

## B（反例与坑）
- AP1301H af 供电（12.7W）时 Eth1 PSE 关闭——靠 AP 给 IPTV 供电必须 at 25W（X8，<<<PAGE 19>>>）
- AP1360 想让下联口输出 at 30W，上联必须 bt Type4；Type3 只能输出 af（X9，<<<PAGE 42>>>）
- 巴西项目 5.150-5.350GHz 禁用，信道规划避开低段 5G（X21，<<<PAGE 40>>>）
- AP1261 部分功能受本地管制设置限制（X23，<<<PAGE 4>>>）
- 室内 AP 吊装/壁装套件全部另购（仅 1261 室外与 1301H 墙面默认附），报价加 OAW-AP-MNT-*/AP-MNT-* 行项（X20，<<<PAGE 11>>>）
- AP1362 免额外避雷器的前提是 6KA 内置防雷+可靠接地（同 1572 纪律，<<<PAGE 41>>>）

来源：bp-stellar-ap-datasheets verified.md（C5/C8/C9/X8/X9/X20/X21/X23/P1/P3/P4/P7/P8）
