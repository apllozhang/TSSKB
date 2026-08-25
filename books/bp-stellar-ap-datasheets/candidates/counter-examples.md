# counter-examples — bp-stellar-ap-datasheets（限制/边界/订购注意）

## 供电降级（PoE 预算硬约束）

- **X1 AP1331 供电降级链** <<<PAGE 27>>>
  "28W (input IEEE 802.3bt or dual IEEE 802.3at POE); Unrestricted functionality / 25W (input IEEE 802.3at POE); The USB port is disabled / 23W (input dual IEEE 802.3af POE); The USB port is disabled, Eth1 port is disabled / 12.5W (input IEEE 802.3af POE); ... dual radio downgrade to 1*1"
  要点：af 单口直接把双射频降为 1x1，性能腰斩。

- **X2 AP1351 at 供电三射频降 2x2** <<<PAGE 34>>>
  "24W (input IEEE 802.3at POE); The USB port is disabled, Eth1 port is disabled, tri radio downgrade to 2*2"
  要点：10G 旗舰必须 bt（45W）才能满血。

- **X3 AP1451 at 供电同样降级** <<<PAGE 62>>>
  "24W (input IEEE 802.3at POE); The USB port is disabled, Eth1 is disabled, tri radio downgrade to 2 x 2"

- **X4 AP1431 at 供电关 USB** <<<PAGE 52>>>
  "34W (singe input IEEE 802.3bt or dual input IEEE 802.3at POE); Unrestricted functionality / 25W (single input IEEE 802.3at POE); The USB port is disabled"

- **X5 AP1521 at 供电进 degraded mode** <<<PAGE 92>>>
  "25W (single input IEEE 802.3at PoE), operating in 'degraded mode': ... All other components are disabled. Scanning Radio, IoT Radio, Eth1, and USB port: disabled"
  要点：扫描/IoT 射频全关，安全与定位能力归零。

- **X6 AP1540 at 供电全频段降 2x2** <<<PAGE 103>>>
  "26.6W (single input IEEE 802.3at PoE); Eth0 works at 2.5GE, Eth1 disabled, SFP+ port disabled, USB port disabled, 2.4GHz radio operating in 2x2 mode, 5GHz radio operating in 2x2 mode, 6GHz radio operating in 2x2 mode"
  要点：旗舰变入门，combo 光口也没了。

- **X7 AP1570 at 供电 25W 限制** <<<PAGE 123>>>
  "25W (single input IEEE 802.3at POE): Uplink/Downlink port disabled / No PSE / USB port disabled / Uplink port set to 5Gbps"

- **X8 AP1301H af 供电 PSE 关闭** <<<PAGE 19>>>
  "12.7W (input IEEE 802.3af PoE), Eth1 PSE disabled"
  要点：靠 AP 给 IPTV 等下联设备供电的场景必须 at 25W。

- **X9 AP1360 PSE 输出依赖输入等级** <<<PAGE 42>>>
  "64W (802.3bt Type4 PoE in) with ENET1 802.3at PSE enabled / 46W (802.3bt Type3 PoE) with ENET1 802.3af PSE enabled / 24W (802.3at) with disabled ENET1 PSE, USB"
  要点：想让下联口输出 at 30W，上联必须 bt Type4。

## 硬件能力边界

- **X10 AP1261 仅 802.11ac Wave2、单口单电** <<<PAGE 3>>>
  "1× 10/100/1000BASE-T autosensing (RJ-45) port, IEEE 802.3at PoE in / Maximum... power consumption: 20W (802.3at PoE)"
  要点：无 USB/无第二口/无 BLE；384 客户端上限（p4）。

- **X11 AP1501 无 BLE/Zigbee、无第二网口** <<<PAGE 69>>>
  "1x multi-gigabit 100M/1G/2.5G Ethernet... uplink port Eth0... 1x USB2.0 Type-C port"
  要点：Wi-Fi 7 最便宜但也砍掉 IoT 射频；需要定位/IoT 至少 AP1511。

- **X12 AP1501 仅 802.3at、SNMPv2（无 v3）** <<<PAGE 71>>> / <<<PAGE 72>>>
  "22.19W (single input IEEE 802.3at POE)" + 软件特性列表仅 "SNMPv2"（对比 Wi-Fi 6 代多为 "SNMPv2, SNMPv3"）
  要点：Wi-Fi 7 代数据表普遍只列 SNMPv2，安全要求高的网管集成需确认。

- **X13 AP1431 6GHz SSID 限 4 个** <<<PAGE 53>>>
  "Up to 16 SSID/Radio (limited to 4 for 6GHz radio)"
  要点：6GHz SSID 规划受硬限制。

- **X14 AP1542 外置天线另行购买且未定** <<<PAGE 105>>>
  "External antennas for AP1542 TBC"
  要点：下单时天线选型待确认（TBC），报价需注明不含天线。

- **X15 AP1572 必须接地** <<<PAGE 121>>>
  "6 N-Type female external antenna connectors, integrated 6KA lightning protection, does not require additional lightning arrester. AP must be grounded for proper operation."
  要点：免避雷器的前提是可靠接地，安装规范要写进施工文档。

- **X16 AP1570 室外天线未列明** <<<PAGE 126>>>
  "Outdoor Antennas TBC"

- **X17 AP1261 天线角度不可调** <<<PAGE 3>>>
  "Pole/ Wall mounting (Mounting kit shipped default with AP), angle is un-adjustable."
  要点：唯一默认附送安装套件的型号，但俯仰角固定。

## 订购/管制域注意

- **X18 RW 版禁售美/埃及/日本** <<<PAGE 12>>>（各型号订购节同述）
  "Not for use in US, Egypt, Japan."（1301 RW 版）；AP1431/1451/1501/1511/1521/1540/1561/1570 的 RW 版多为 "not for use in US, Japan"（埃及限制收窄）。
  要点：下单前核对 -RW/-US/-ME 后缀与项目所在地。

- **X19 AP1561 管制域含 ME 且无 Israel 细分差异** <<<PAGE 115>>>
  "OAW-AP1561-RW... not for use in US, ME, Japan"（此处 ME 指中东域）；RW/US/ME 三版本。
  要点：1561/1570 的 RW 版限制写法与其他型号不同（US, ME, Japan），易误读。

- **X20 室内 AP 吊装/壁装套件全部另购** <<<PAGE 11>>>（"Mount kit needs to be ordered separately" 通用注记，各型同）
  要点：仅 AP1261（室外）和 AP1301H（墙面 single gang）默认附套件，其余都必须加 OAW-AP-MNT-*/AP-MNT-* 行项。

- **X21 巴西 5.150-5.350GHz 禁用（AP1360）** <<<PAGE 40>>>
  "Brazil: Frequency band 5.150 to 5.350 GHz is disabled."
  要点：巴西项目的信道规划避开低段 5G。

- **X22 Wi-Fi 6 代旧数据表 OWE 尚未激活** <<<PAGE 7>>> / <<<PAGE 15>>>（脚注）
  "* The hardware is ready, and will be supported in a future software update."（对应 Enhanced Open/OWE）
  要点：AP1301/1301H 时期 OWE 只是硬件就绪，需软件升级（1360 起数据表已写为支持）。

- **X23 AP1261 部分功能受管制限制** <<<PAGE 4>>>
  "Note: some features are limited by local regulatory settings"

- **X24 网管规模数字随版本增长，需与销售核实** <<<PAGE 83>>> / <<<PAGE 124>>>（脚注）
  "(1) Please check the current scalability from your ALE Sales representatives, as these numbers are increasing in each OmniVista release."
