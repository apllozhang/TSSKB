# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1 连锁零售/分支办公室 Wi-Fi 7 平价换代：AP1501**
  场景：数百分支、中密度、预算敏感、接入交换机仅 GbE/af-at。依据 <<<PAGE 66>>>："delivers an accessible entry point into Wi-Fi 7... Built for mid-density and distributed environments such as branch offices, retail locations and small campuses"；单 2.5GE 上联 + 802.3at 22.19W（p71），现有布线与交换机全部沿用。若客户还要 IoT/定位（BLE/Zigbee）或 5GE，升 AP1511（p77）。
- **C2 高密礼堂/大会议厅：AP1540 系列内置 or 外置天线怎么选**
  依据 <<<PAGE 97>>>："AP1541, which has integrated omnidirectional antennas and is suitable for standard enterprise use, such as lecture halls... / AP1542, which has 8 connectors for external antennas, perfectly suited to specific targeted coverage needs and specific spaces such as high ceilings in arenas, long corridors or warehouses"。普通高密选 1541；高顶棚/长走廊/仓库定向覆盖选 1542。
- **C3 室外园区 Wi-Fi 7：AP1561 vs AP1570 系列**
  同为室外 2x2x3、9.328Gbps。选 1570 的理由 <<<PAGE 117>>>：需要光纤维回传（"SFP/SFP+ optical interface... long-distance backhaul"）、五射频（含专用三频扫描 + BT6.0）、下联 PSE 供电（"1GE uplink/downlink port, PSE 802.3at"）、外置天线版本（AP1572）。选 1561 的理由 <<<PAGE 108>>>：现网接入层只有 5GE/at，"optimized to work with IEEE 802.3at, thereby protecting existing investments"。
- **C4 6GHz 未开放国家/地区部署 Wi-Fi 7：软件切 5GHz**
  依据 <<<PAGE 108>>>（AP1561）/"<<<PAGE 100>>>"（AP1540）："As in some RF domains, the use of the 6GHz band in outdoor locations is not permitted, the 6GHz radio is software configurable to operate in 6GHz or 5GHz"。三射频在受限域跑 2.4+5+5（AP1540 p100 明示 "2.4GHz + 5GHz + 5GHz configuration"），射频投资不打水漂。
- **C5 酒店/病房墙面覆盖：AP1301H 一口多用**
  依据 <<<PAGE 14>>>："1x Gigabit ethernet uplink, 4x Gigabit downlink, with one providing 802.3af PSE to power the attached IoT device, one pair of RJ-45 passthrough ports for analog phones, and a USB 2.0 port"。一张 AP 解决房间 Wi-Fi + IPTV 供电 + IP 话机 + 模拟话机直通；注意 at 供电才开 PSE（p19 "12.7W (input IEEE 802.3af PoE), Eth1 PSE disabled"）。
- **C6 Wi-Fi 6 世代内部升级：AP1301 → AP1331 → AP1351 的密度阶梯**
  AP1301（1.77G/512 客户端）普通办公；AP1331（3.55G/1024/双 5GE/专用扫描）中高密；AP1351（~10G/1536/双 10GE/双 5GHz）超高密。依据 <<<PAGE 22>>>（1331 "dense and high-capacity needs"）、<<<PAGE 30>>>（1351 "very dense and high capacity needs"）。上联是分水岭：GbE→5GE→10GE，需同步评估接入交换机多千兆能力。
- **C7 Wi-Fi 7 中端主力选型：AP1511 vs AP1521**
  同 2.4/6GHz 2x2。1521 的差异 <<<PAGE 87>>>：5GHz 升 4x4（12.2G vs 9.328G）、专用三频扫描射频、10GE 上联、1280 客户端。预算与布线（5GE vs 10GE）+ 是否需要全时扫描防护决定取舍；1521 若只有 at 供电会进 degraded mode（p92），必须 bt。
- **C8 室外补盲/定向覆盖：AP1361 vs AP1361D vs AP1362**
  依据 <<<PAGE 41>>>：AP1361 内置全向（beamforming 增益 12.5dBi@5G）；AP1361D 内置定向（H80°xV80°，适走廊/街面）；AP1362 外置 6x N 头（自配天线增益，"6KA lightning protection, no requirement for additional lightning arrester"）。需要 SFP 长距回传 + 给下联设备供电时选本系列而非 1561/1570（p40 有 SFP + PSE 802.3at 下联）。
- **C9 医疗 RTLS 定位项目：带 BLE/Zigbee + FTM 的型号**
  依据 <<<PAGE 11>>>（"Stanley Healthcare/Aeroscout RTLS support" 全线支持）+ <<<PAGE 80>>>（AP1511 "802.11mc/az Fine timing measurement (FTM)"）。Wi-Fi 7 代（1511 起）加 FTM 精确测距，定位精度需求高的医疗资产追踪优先 1511/1540；老代 Wi-Fi 6 靠 BLE/Zigbee（1331/1351/1360/1431/1451）。
- **C10 管理平台配套：Wi-Fi 7 大规模部署的网管选型**
  依据 <<<PAGE 72>>> / <<<PAGE 104>>>：AP1501 场景 Cirrus 可到 30K AP；AP1540 场景 Terra 5K / Cirrus 20K；OV2500 老网管只有 4K（p83 脚注 "Up to 4K APs with OmniVista 2500"）。超 4K AP 的 Wi-Fi 7 项目必须上新一代 OmniVista。
- **C11 电信级/MSP 多租户或数据不出境项目：本地 OmniVista + Wi-Fi 7**
  依据 <<<PAGE 68>>>："can be managed on-premises from OmniVista, dedicated for on-premises deployment, which addresses stringent requirements for local infrastructure management, data sovereignty and advanced security compliance"。Wi-Fi 7 代数据表已把 OmniVista 表述为"两形态"（云/本地），2500 退居兼容角色。
- **C12 零售/餐饮多租户 PSK 认证：DPGPSK**
  依据 <<<PAGE 67>>>（AP1501）："supports Dynamic Private-Group Pre-Shared Key (DPGPSK) deployments for massive private groups in hospitality, MDUs and residential"。避免 802.1X 改造成本，用动态组 PSK 实现每用户隔离。

## counter-examples

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

## frameworks

- **F1 Stellar AP 代际×频段演进图**
  ```
  11ac Wave2  →  Wi-Fi 6 (ax)   →  Wi-Fi 6E (ax+6GHz)  →  Wi-Fi 7 (be)
  AP1261(室外)  AP1301/1301H/      AP1431/1451            AP1501/1511/1521/1540(室内)
               1331/1351(室内)                            AP1561/1570(室外)
               AP1360(室外)
  代际技术标志：ax=OFDMA/1024-QAM/TWT；6E=新增 6GHz；be=MLO/4096-QAM/320MHz/
  512 Compressed Block Ack/MACsec 上联/DPGPSK/AFC
  ```
  依据 <<<PAGE 1>>> / <<<PAGE 6>>> / <<<PAGE 48>>> / <<<PAGE 67>>>（MLO 定义）。
- **F3 上联端口阶梯（决定接入交换机选型）**
  ```
  1x GbE(AP1261) → 2x GbE(1301) → 2x 5GE(1331/1431) → 2.5GE+SFP(1360)
  → 1x 2.5GE(1501) / 1x 5GE(1511/1561) → 10GE(1521) / 10GE+combo SFP+(1540/1570) / 2x 10GE(1351/1451)
  ```
  配套交换机：6360/6465（GbE/多千兆）→ 6560/6570（多千兆）→ 6900 系列上行（见 OmniSwitch 书）。依据各型号 Interfaces 节。
- **F4 型号命名解码框架**
  ```
  AP 1 x y z 后缀：
    x=代际（1=Wi-Fi6 时代/2=Wi-Fi6E/5=Wi-Fi7 相关；4x=6E、5x=7）
    末位 1 = 内置全向天线；D = 内置定向天线；2 = 外置天线接口（N 型/RP-SMA）
  后缀 -RW（全球，禁 US/Egypt/Japan 等）/ -US / -ME（中东）
  例：AP1361D=定向；AP1542=8x RP-SMA 外置；OAW-AP1572-US=美国域外置天线版
  ```
  依据 <<<PAGE 41>>>（1361/1361D/1362 天线差异）、<<<PAGE 97>>>（1541/1542）、<<<PAGE 121>>>（1571/1572）、各订购节。
- **F5 射频数量演进（"几_radio" 定位法）**
  ```
  2 射频（服务+服务）：1261/1301/1301H(+BLE 合计算 IoT)
  4 射频：1331(2服务+扫描+BLE)、1360(2服务+扫描+BLE)、1431(3服务+BLE)
  5 射频：1351(3服务+扫描+BLE)、1451、1521、1540、1570
  3 射频精简：1501（无扫描无 BLE）、1511（+BLE 无扫描）、1561（无扫描无 BLE，6G 可切 5G）
  ```
  判断口诀：要不要专用扫描（wIPS 全时防护）与 BLE/Zigbee（IoT 定位）→ 直接筛掉 2/3 射频档。依据各型号 Radio specification 节。

## glossary

- **AP1261（OAW-AP1261-RW-B）**：室外 11ac Wave2，2x2，1.2Gbps，IP67，单 GbE，at 20W <<<PAGE 1>>>
- **IP67**：防尘防水等级，AP1261/1360/1561/1570 室外系列防护标准 <<<PAGE 3>>>
- **6KA lightning protection**：外置天线接口内置防雷（AP1362/1572），接地前提下免额外避雷器 <<<PAGE 41>>>

## Wi-Fi 6 室内/墙面
- **AP1301（OAW-AP1301-RW/ME/US）**：室内 Wi-Fi 6 入门，2x2，1.77Gbps，af 13.1W <<<PAGE 6>>>
- **AP1301H（OAW-AP1301H-*）**：酒店墙面 Wi-Fi 6，1 上联+4 下联（1 PSE）+RJ45 直通对+BLE/Zigbee <<<PAGE 14>>>
- **AP1331（OAW-AP1331-*）**：Wi-Fi 6 中高端 4x4+4x4，3.55Gbps，双 5GE，专用扫描+BLE <<<PAGE 22>>>
- **AP1351（OAW-AP1351-*）**：Wi-Fi 6 旗舰，2.4G 4x4+5GL 4x4+5GH 8x8，~10Gbps，双 10GE <<<PAGE 30>>>
- **AP1360 系列**：室外 Wi-Fi 6；AP1361 全向 / AP1361D 定向 / AP1362 外置 6x N 头 <<<PAGE 37>>>

## Wi-Fi 6E
- **AP1431（OAW-AP1431-RW/US）**：Wi-Fi 6E 三频 2x2x3，4.2Gbps，双 2.5GE <<<PAGE 48>>>
- **AP1451（OAW-AP1451-RW/US）**：Wi-Fi 6E 旗舰 4x4+8x8+4x4，10Gbps，双 10GE <<<PAGE 57>>>
- **Multi-band filter**：内置多频段滤波器，5G/6G 全信道无限制运行 <<<PAGE 48>>>

## Wi-Fi 7（15xx）
- **AP1501（OAW-AP1501-RW/US）**：Wi-Fi 7 入门，2x2x3，9.328Gbps，1x 2.5GE，at 供电 <<<PAGE 66>>>
- **AP1511（OAW-AP1511-RW/US）**：Wi-Fi 7 入门+BLE5.4/Zigbee，1x 5GE，MACsec <<<PAGE 77>>>
- **AP1521（OAW-AP1521-RW/US）**：Wi-Fi 7 中端，5GHz 4x4+三频专用扫描，12.2Gbps，10GE <<<PAGE 87>>>
- **AP1540 系列**：Wi-Fi 7 超高密旗舰 4x4x3，18.67Gbps；AP1541 内置天线 / AP1542 8x RP-SMA 外置 <<<PAGE 97>>>
- **AP1561（OAW-AP1561-RW/US/ME）**：室外 Wi-Fi 7，2x2x3，5GE 上联，仅 at 供电，宽口径扇区天线 <<<PAGE 108>>>
- **AP1570 系列**：室外 Wi-Fi 7 旗舰，10GE RJ45/SFP+ combo；AP1571 内置 / AP1572 6x N 型外置 <<<PAGE 117>>>

## 订购后缀与配件
- **-RW**：Unrestricted regulatory domain（但注明 not for use in US/Egypt/Japan 等） <<<PAGE 12>>>
- **-US / -ME**：美国 / 中东管制域专用版本 <<<PAGE 12>>> / <<<PAGE 20>>>
- **OAW-AP-MNT-B/W/C**：T 型龙骨/壁装/异形吊顶安装套件（1101/12xx/13xx 系列适用） <<<PAGE 12>>>
- **AP-MNT-IN-BE/CE/WE/WE2**：增强型吊顶/平面不锈钢/塑料安装套件（13xx/14xx/15xx 适用） <<<PAGE 73>>>
- **AP-MNT-OUT / AP-MNT-OUT-H**：室外抱杆壁装 / 悬挂俯仰套件 <<<PAGE 44>>>
- **PD-9001GR/AT/AC**：1 口 802.3at 千兆 PoE Midspan（30W，不含电源线） <<<PAGE 12>>>
- **POE60U-1BT-X-R**：1 口 802.3bt 万兆 PoE Midspan（60W） <<<PAGE 28>>>
- **POEO75U-1BT-X-R**：室外 IP67 单口 10GE bt PoE Midspan <<<PAGE 115>>>
- **ADP-50GRBE/ADP-50GRBD**：48V DC 电源适配器（50W/30W） <<<PAGE 12>>> / <<<PAGE 54>>>
- **PWR-CORD-XX**：按国家选配电源线 <<<PAGE 12>>>
- **ANT-O-M2-5/M4-9/M6-8、ANT-S-M6-60-9**：室外双频全向/定向天线（AP1362 用） <<<PAGE 44>>>
- **HLLW**：Hardware Limited Lifetime Warranty 硬件终身有限保修 <<<PAGE 4>>>

## Wi-Fi 标准术语
- **802.11ax / Wi-Fi 6**：OFDMA、MU-MIMO（DL/UL）、1024-QAM、BSS Coloring、TWT <<<PAGE 6>>>
- **Wi-Fi 6E**：ax 扩展至 6GHz（5.925-7.125GHz） <<<PAGE 48>>>
- **802.11be / Wi-Fi 7**：MLO、4096-QAM、EHT320、512 Compressed Block Ack、Triggered uplink access <<<PAGE 67>>> / <<<PAGE 109>>>
- **MLO（Multi-Link Operation）**：终端跨频段/信道并发收发 <<<PAGE 67>>>
- **OFDMA / RU**：正交频分多址/资源单元，最多 37 RUs <<<PAGE 38>>>
- **4096-QAM**：峰值速率提升最高 25% <<<PAGE 67>>>
- **EHT20-320**：802.11be 信道宽度档位；6GHz 才支持 320MHz <<<PAGE 69>>>
- **HE/VHT/HT**：ax/ac/n 的信道模式前缀 <<<PAGE 9>>>
- **TWT（Target Wake Time）**：目标唤醒时间，IoT 省电 <<<PAGE 6>>>
- **BSS Coloring**：空间复用着色机制 <<<PAGE 6>>>
- **AFC（Automated Frequency Coordination）**：6GHz 标准功率自动频率协调（AP1540/1561/1570） <<<PAGE 100>>> / <<<PAGE 108>>>
- **RFC（Regulator Frequency Coordination）**：管制域频率协调 <<<PAGE 100>>>

## 射频/硬件规格术语
- **MxN:K（如 4x4:4）**：M 发 N 收 K 空间流 <<<PAGE 25>>>
- **dBi**：天线增益；beamforming gain 波束赋形增益 <<<PAGE 41>>>
- **专用扫描射频（dedicated scanning radio）**：全频段 1x1，专职频谱分析与 wIPS，1331/1351/1451/1521/1540/1570 配备 <<<PAGE 25>>>
- **BLE / Zigbee**：蓝牙低功耗/Zigbee IoT 射频；BT5→5.1→5.4→6.0 随代际升级 <<<PAGE 17>>> / <<<PAGE 120>>>
- **FTM（Fine Timing Measurement, 802.11mc/az）**：精确测距/定位，Wi-Fi 7 代支持 <<<PAGE 80>>>
- **TPM 2.0**：可信平台模块，密钥安全存储，1331 起标配 <<<PAGE 26>>>
- **MACsec（802.1ae）**：上联口二层加密，AP1511 起支持 <<<PAGE 78>>>
- **ACC（Advanced Cellular Coexistence）**：蜂窝干扰共存 <<<PAGE 9>>>
- **RDA（Radio Dynamic Adjustment）+ DFS/TPC**：信道/功率自动调优 <<<PAGE 2>>>
- **Multi-Gigabit（802.3bz）**：2.5G/5G（/10G）多千兆以太网 <<<PAGE 26>>>
- **PoE 802.3af/at/bt**：15.4W/30W/60-90W 供电等级；Type3/Type4 为 bt 档 <<<PAGE 27>>> / <<<PAGE 42>>>
- **PSE**：供电设备端（AP 下联口对外供电） <<<PAGE 17>>>
- **MTBF**：平均无故障时间（小时/年） <<<PAGE 11>>>
- **UL2043 plenum rating**：吊顶风管空间防火认证 <<<PAGE 12>>>
- **Passpoint R3**：Wi-Fi 联盟热点认证版本 <<<PAGE 12>>>

## 安全与管理术语
- **WPA3 Enterprise with CNSA / Personal (SAE)**：企业级/个人级 WPA3 模式 <<<PAGE 10>>>
- **OWE / Enhanced Open**：开放网络机会性加密 <<<PAGE 7>>>
- **wIDS/wIPS**：无线入侵检测/防护（需 OmniVista 配合） <<<PAGE 1>>>
- **DPI**：深度包识别，应用监控与策略执行 <<<PAGE 7>>>
- **DPGPSK（Dynamic Private-Group PSK）**：动态私有组预共享密钥（酒店/MDU/住宅） <<<PAGE 67>>>
- **AP cluster / virtual controller**：无控制器集群，主 AP 作虚拟管理器，255 台/集群（1360 系列 256） <<<PAGE 2>>> / <<<PAGE 39>>>
- **Wi-Fi Express**：免网管集群模式，Admin/Viewer/GuestOperator 三角色 <<<PAGE 8>>>
- **GuestOperator**：前台可用的访客账号管理角色 <<<PAGE 8>>>
- **ZTP（Zero-Touch Provisioning）**：零接触开通；可配合 OXO Connect R2 <<<PAGE 8>>>
- **UPAM**：OmniVista 内置统一策略认证管理器 <<<PAGE 7>>>
- **L2/L3 roaming**：二层/三层漫游（L3 需 OmniVista） <<<PAGE 11>>>
- **OV2500 / OVT / OVC**：OmniVista 2500 / Terra / Cirrus 三种网管，管理上限 4K / 5K / 12K-30K AP <<<PAGE 83>>>
- **RTLS**：实时定位系统（Stanley Healthcare/Aeroscout） <<<PAGE 11>>>
- **Stanley Healthcare/Aeroscout**：医疗定位生态伙伴 <<<PAGE 11>>>

## principles

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
