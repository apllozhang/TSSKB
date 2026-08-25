# principles — bp-stellar-ap-datasheets（Stellar AP 选型速查）

## Wi-Fi 6 / 6E 代

- **P1 AP1261：室外 11ac Wave2 老将** <<<PAGE 1>>>
  "high performance 802.11ac wave2 access point used in outdoor settings... With a maximum concurrent data rate of 1.2Gbps (867Mbps in 5GHz and 300Mbps in 2.4GHz)"
  要点：双频 2x2、IP67、-20~55°C、802.3at 20W、单 GbE 口。升级替代看 AP1360/1561。

- **P2 AP1301：Wi-Fi 6 入门双频 2x2** <<<PAGE 6>>>
  "supporting a maximum aggregate data rate of ˜1.77 Gbps (1.2 Gbps in 5 GHz and 574 Mbps in 2.4 GHz)"
  要点：802.3af 即可全功能（13.1W），512 客户端，双 GbE 上联，性价比主力。

- **P3 AP1301H：酒店/客房墙面专用形态** <<<PAGE 14>>>
  "The OmniAccess Stellar AP1301H brings unparalleled connectivity... for in-room applications such as hotels, classrooms, dormitories, clinics, remote office/home office"
  要点：1 GbE 上联 + 4 GbE 下联（1 口 802.3af PSE 供 IPTV/终端）+ RJ-45 直通对（模拟话机）+ BLE/Zigbee；单 gang 86mm 墙盒尺寸。

- **P4 AP1301H 容量翻倍于 AP1301** <<<PAGE 19>>>
  "Up to 16 SSID per radio (total 32 SSID) / Up to 1024 associated client devices"（对比 AP1301 512，p11）
  要点：MTBF 150 年，墙面部署但并发能力不缩水。

- **P5 AP1331：Wi-Fi 6 中高端 4x4+4x4 + 专用扫描射频** <<<PAGE 22>>>
  "four built-in radios: two radios, 2.4Ghz/5Ghz band...; one full-band radio dedicated for scanning... and an integrated Bluetooth®/Zigbee radio"
  要点：3.55Gbps，双 5GE 多千兆上联（PoE 冗余/负载分担），1024 客户端，TPM 2.0。

- **P6 AP1351：Wi-Fi 6 旗舰三射频 8x8** <<<PAGE 30>>>
  "five built-in radios, three radios 2.4Ghz/5Ghz Low/5Ghz High... maximum aggregate data rate of ˜10Gbps (9.6Gbps in 5 GHz and 1.2Gbps in 2.4GHz). The access points dual 10Gbps uplinks"
  要点：双 5GHz（低+高）拆分，1536 客户端，超高密场景（礼堂/大堂）。

- **P7 AP1360 系列：室外 Wi-Fi 6 全能（三种天线形态）** <<<PAGE 37>>>
  "AP1361 integrated omni / AP1361D integrated directional (H80°x V80°) / AP1362 6 N-type female external antenna connectors, integrated 6KA lightning protection"（p41）
  要点：~3Gbps（5G 4x4 + 2.4G 2x2），2.5GE 上联 + SFP 长距回传 + GbE PSE 下联，IP67、-40~65°C、抗 165MPH 阵风。

- **P8 AP1360 系列多千兆 + bt 供电 64W** <<<PAGE 40>>> / <<<PAGE 42>>>
  "1x 10/100/1000/2500 Mbps IEEE 802.3bz compliant... uplink port... PoE 802.3at/bt compliant" + "64W (802.3bt Type4 PoE in) with ENET1 802.3at PSE enabled"
  要点：可同时给下联 IoT 设备反向供电（PSE 输出随输入等级）。

- **P9 AP1431：Wi-Fi 6E 三频入门** <<<PAGE 48>>>
  "three radios 2.4GHz/5GHz/6GHz serving high density Wi-Fi clients, and an integrated Bluetooth/Zigbee radio... 4.2Gbps (574Mbps in 2.4GHz, 1.2Gbps in 5GHz, 2.4Gbps in 6GHz)"
  要点：三频 2x2，6GHz 支持到 HE160，双 2.5GE 上联，A built-in multi-band filter（p48 "enables 5GHz and 6GHz operation across all available channels"）。

- **P10 AP1451：Wi-Fi 6E 旗舰（6G 4x4 + 5G 8x8）** <<<PAGE 57>>>
  "Tri Radio, 6 GHz High 4x4:4, 5 GHz 8x8:8, and 2.4 GHz 4x4:4... maximum aggregate data rate of 10 Gbps... dual 10 Gbps uplinks provide PoE resiliency and load sharing"
  要点：五射频（含专用扫描 + BLE/Zigbee），1536 客户端，双 10GE。

## Wi-Fi 7 代（15xx）

- **P11 Wi-Fi 7 核心特性集** <<<PAGE 67>>> / <<<PAGE 118>>>
  "Multi-Link Operation (MLO)... simultaneously send and/or receive data across different frequency bands and channels" + "4096-QAM boosts peak data-rates by as much as 25 percent" + "Support for 512 Compressed Block Ack" + "Triggered uplink access"
  要点：MLO/4096-QAM/320MHz(EHT320)/512 压缩块确认/触发上行，全面后向兼容 a/b/g/n/ac/ax。

- **P12 AP1501：Wi-Fi 7 低成本入门（branch/零售）** <<<PAGE 66>>>
  "delivers an accessible entry point into Wi-Fi 7, combining next-generation wireless performance with the cost efficiency enterprises expect. Built for mid-density and distributed environments such as branch offices, retail locations and small campuses"
  要点：2x2x3，9.328Gbps，单 2.5GE 口，仅 802.3at（22.19W）；每射频 256 客户端；支持 DPGPSK。

- **P13 AP1511：Wi-Fi 7 入门 + IoT 射频 + 5GE + MACsec** <<<PAGE 77>>>
  "three radios serving Wi-Fi clients and an integrated Bluetooth/Zigbee radio... The access point provides 1 x 5GE Power over Ethernet (PoE) uplink" + p78 "supports 802.1ae MACsec in the uplink port"
  要点：比 AP1501 多 BLE/Zigbee（蓝牙 5.4）、5GE 上联、FTM 精确定位；768 客户端/AP。

- **P14 AP1521：Wi-Fi 7 中端（5GHz 4x4 + 专用三频扫描）** <<<PAGE 87>>>
  "five built-in radios, three radios 2.4GHz/5GHz/6GHz..., one full band radio dedicated to scanning... 12.2 Gbps (688 Mbps in 2.4GHz, 5.76 Gbps in 5GHz, 5.76 Gbps in 6GHz). The access point provides one 10GE PoE uplink and one GE uplink/downlink"
  要点：10GE 上联，1280 客户端，MACsec；at 供电进入"degraded mode"（见 X 条目）。

- **P15 AP1540 系列：超高密旗舰 4x4x3 / 18.67Gbps** <<<PAGE 97>>>
  "ultra-high-performance Wi-Fi 7 access point, designed to meet the requirements of high-density enterprise environments... 18.67 Gbps (1376.5 Mbps in 2.4GHz, 5.76 Gbps in 5GHz, 11.5 Gbps in 6GHz)"
  要点：6GHz EHT320 4x4 达 11.52Gbps（p101）；双 10GE（其一 combo SFP/SFP+）；1536 客户端；AP1541 内置天线/ AP1542 8x RP-SMA 外置天线（高顶棚/走廊/仓库）。

- **P16 AP1540 AFC/RFC 与 6GHz→5GHz 软切换** <<<PAGE 100>>>
  "complies with worldwide regulatory requirements, supporting both Automatic Frequency Coordination (AFC) and Regulator Frequency Coordination (RFC)... the 6GHz radio is software configurable to operate in 5GHz, allowing the use of the three radios where 6GHz band is still not allowed in 2.4GHz + 5GHz + 5GHz configuration"
  要点：6GHz 未开放地区三射频不浪费，可跑 2.4+5+5。

- **P17 AP1561：室外 Wi-Fi 7 经济型（5GE、仅 at）** <<<PAGE 108>>>
  "The AP is powered by a 5GE Multigig Ethernet uplink port, allowing to connect existing LAN Access OmniSwitch layers without investing in upgrading the access layer. AP1561 features Wi-Fi 7 serving radios and is optimized to work with IEEE 802.3at"
  要点：保护现网接入交换机投资（不要求 bt/多千兆升级）；IP67；6GHz AFC 就绪、软件可切 5GHz；768 客户端。

- **P18 AP1570 系列：室外 Wi-Fi 7 旗舰（10GE combo + 光回传）** <<<PAGE 117>>>
  "powered by a 10GE Multigig Ethernet uplink combo port. This combo port supports either 10GE multi-gigabit with an RJ45 interface or an SFP/SFP+ optical interface, allowing the AP1570 series model to be connected to the network via optical fiber (active or passive) for long-distance backhaul"
  要点：五射频（三服务+三频扫描+BLE6.0/Zigbee）；1GE PSE 下联；AP1572 外置 N 头 + 6KA 防雷；IP67。

## 共性平台能力

- **P19 三种管理模式、同一软件镜像** <<<PAGE 7>>>（各型号同述）
  "The access points can be deployed in three different modes, all through a single version of software, simplifying IT operations."
  要点：Wi-Fi Express（无控制器集群）/ OmniVista 本地 / OmniVista Cirrus 云，同一软件切换。

- **P20 无控制器集群架构** <<<PAGE 2>>> / <<<PAGE 8>>>
  "The access point (AP) cluster is an autonomous system... managed by one AP that is elected as the primary virtual manager. One AP cluster supports up to 255 APs."（AP1360 系列为 256，p39）
  要点：免控制器，首台配置后全网分钟级自动同步。

- **P21 管理规模阶梯** <<<PAGE 72>>> / <<<PAGE 83>>> / <<<PAGE 104>>>
  "Up to 30K APs when managed by OmniVista Cloud / Up to 10K APs when managed by OmniVista Terra"（AP1501）；"Up to 5K APs (OVT) / Up to 12K APs (OVC)"（AP1511/1521/1561/1570）；"Up to 20K APs when managed by OmniVista Cirrus"（AP1540）；"Up to 4K APs with OmniVista 2500"
  要点：Wi-Fi 7 代支持的管理规模上限显著高于 Wi-Fi 6 代（2500 仅 4K）。

- **P22 安全基线：WPA3/CNSA/OWE + TPM 2.0** <<<PAGE 26>>> / <<<PAGE 52>>>
  "Integrated Trusted Platform Module (TPM 2.0)... WPA3, Enterprise with CNSA Option, Personal (SAE)... Wi-Fi Enhanced Open based on Opportunistic Wireless Encryption (OWE)"
  要点：中高端从 AP1331 起带 TPM 2.0 硬件安全芯片；1360/15xx 支持 Enhanced Open 认证。

- **P23 MACsec 上联加密（Wi-Fi 7 代标配趋势）** <<<PAGE 78>>> / <<<PAGE 119>>>
  "supports 802.1ae MACsec in the uplink port. This way, the path from the AP to the network access switch can be protected... protection against man-in-the-middle attacks"
  要点：AP1511/1521/1540/1561/1570 均支持；AP1540 双上联口都支持（p98）。

- **P24 DPGPSK 动态私有组密钥** <<<PAGE 67>>> / <<<PAGE 98>>>
  "support Dynamic Private-Group Pre-Shared Key (DPGPSK) deployments for massive private groups in hospitality, MDUs and residential"
  要点：酒店/多住户/住宅大规模 PSK 运营利器，AP1501/1540 起支持。

- **P25 BLE/Zigbee IoT 射频分级** <<<PAGE 17>>>（1301H Bluetooth 5）/<<<PAGE 25>>>（1331 BLE+Zigbee）/<<<PAGE 80>>>（1511 Bluetooth 5.4）/<<<PAGE 120>>>（1570 Bluetooth 6.0）
  要点：定位/楼宇自动化能力看代际：BT5 → BT5.1（1360）→ BT5.4 → BT6.0。

- **P26 全线硬件终身保修** <<<PAGE 4>>>（各型号订购节同述）
  "OmniAccess Stellar Access Points come with Hardware Limited Lifetime Warranty (HLLW)."
  要点：HLLW 标配；Wi-Fi 6 代另含一年合作伙伴 SUPPORT 软件。

- **P27 制造规格横向速查（选型核对表）**
  | 型号 | 聚合速率 | 上联 | 供电 | 客户端 | 页 |
  |---|---|---|---|---|---|
  | AP1261 | 1.2G | 1x GbE | at 20W | 384 | p3-4 |
  | AP1301 | 1.77G | 2x GbE | af 13.1W | 512 | p9-11 |
  | AP1301H | 1.77G | 1x GbE(+4 下联) | at 25W/af 12.7W | 1024 | p17-19 |
  | AP1331 | 3.55G | 2x 5GE | bt 28W | 1024 | p25-27 |
  | AP1351 | ~10G | 2x 10GE | bt 45W | 1536 | p33-34 |
  | AP1360 | ~3G | 2.5GE+SFP+GbE PSE | bt 64W | 1024 | p40-42 |
  | AP1431 | 4.2G | 2x 2.5GE | bt 34W | 512/radio | p51-53 |
  | AP1451 | 10G | 2x 10GE | bt 49W | 1536 | p60-62 |
  | AP1501 | 9.328G | 1x 2.5GE | at 22.19W | 256/radio | p69-72 |
  | AP1511 | 9.328G | 1x 5GE | at/bt 23.4W | 768 | p80-83 |
  | AP1521 | 12.2G | 10GE+GE | bt 40.2W | 1280 | p90-93 |
  | AP1540 | 18.67G | 10GE+10GE/SFP+ combo | bt 51W | 1536 | p101-103 |
  | AP1561 | 9.328G | 1x 5GE | at 23.64W | 768 | p111-114 |
  | AP1570 | 9.328G | 10GE combo+1GE PSE | bt 50W | 768 | p120-124 |
