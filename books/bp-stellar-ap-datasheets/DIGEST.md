# DIGEST — ALE OmniAccess Stellar AP 数据表合集 精华

本书是 ALE Stellar 无线接入点数据表合集（14 份文档 128 页），覆盖 Wi-Fi 6 → Wi-Fi 6E → Wi-Fi 7 三代、室内/室外/墙面三大形态 20+ SKU。定位"售前选型速查"：什么场景选哪个型号、上联/供电/管制域边界。

## 一、知识地图（四技能单元）

1. **Wi-Fi 7 旗舰**（bp-ap-wifi7-flagship）：AP1540 超高密、AP1561/1570 室外、供电降级链、6G 切 5G（p97-128）。
2. **Wi-Fi 6/6E/7 中端矩阵**（bp-ap-wifi6-midrange）：1301→1331→1351 与 1501→1511→1521 双阶梯、上联分水岭（p6-96）。
3. **特殊用途**（bp-ap-special-purpose）：AP1301H 墙面一口多用、AP1360 室外三天线形态、AP1261 老室外、RTLS 定位（p1-47）。
4. **管理规模与平台**（bp-ap-platform-scale）：Express 集群 255 / OV2500 4K / Terra 5K / Cirrus 12K-30K、三模式同一镜像（散布各型号 Management 节）。

## 二、四单元要点串讲

### 1. Wi-Fi 7 旗舰：三档与供电红线
室内超高密 AP1540（4x4x3/18.67G/双 10GE 含 combo SFP+，1541 内置 vs 1542 8x RP-SMA 外置）；室外经济 AP1561（5GE、仅 at——保护现网接入层）；室外旗舰 AP1570（10GE combo 光回传、五射频、PSE 下联、1572 外置 6KA 防雷）。共同：AFC/RFC 合规、6GHz 软件切 5GHz 跑 2.4+5+5（<<<PAGE 100>>>/<<<PAGE 108>>>）。供电红线：1540 at 全频降 2x2 关光口（X6）；1570 at 上下联禁用（X7）。

### 2. 中端矩阵：上联是分水岭
Wi-Fi 6 线 1301（1.77G/af）→1331（3.55G/双 5GE）→1351（~10G/双 10GE）；Wi-Fi 7 线 1501（最便宜，砍 BLE/扫描/第二口）→1511（+BLE5.4+5GE+FTM+MACsec）→1521（4x4 5GHz+扫描+10GE）。上联阶梯（F3）同步决定接入交换机多千兆投资；中高端 at 供电必降级（1331 af 降 1x1、1521 进 degraded mode）。

### 3. 特殊用途：一口多用与三天线
AP1301H：1 上联+4 下联（1 口 af PSE 供 IPTV）+RJ45 直通（模拟话机）+BLE/Zigbee，at 25W 才开 PSE。AP1360 系：1361 全向/1361D 定向 H80°xV80°/1362 外置 6N 头，2.5GE+SFP+GbE PSE 下联，bt Type4 才能下联输出 at。AP1261 为 11ac Wave2 老将。定位：全线支持 Stanley/Aeroscout RTLS，Wi-Fi 7 代加 FTM。

### 4. 管理规模：三模式同一镜像
Wi-Fi Express 集群 255（1360 系 256）→ OV2500 4K → Terra 5K → Cirrus 12K-30K。三模式同一软件镜像切换（<<<PAGE 7>>>）。规模数字随版本增长，下单前核实。

## 三、本书在知识库中的位置

与 stellar-wlan-* 系列（部署/排障操作）和 NMS 彩页书互补：本书管"选哪个型号"，NMS 书管"选哪层网管怎么买"。跨书易混点：Wi-Fi 7 代数据表普遍只列 SNMPv2（老代多为 v2+v3）；RW 版禁售地名录各型号写法不一（1561 含 ME）；吊装/壁装套件除 1261/1301H 外全部另购。

## 来源
bp-stellar-ap-datasheets（14 份文档 128 页）。verified.md：cases C1-C12；counter-examples X1-X24（无 X17）；frameworks F1/F3/F4/F5；principles P1-P27；glossary 约 80 条。
