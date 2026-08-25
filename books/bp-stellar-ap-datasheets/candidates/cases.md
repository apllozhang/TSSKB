# cases — bp-stellar-ap-datasheets（AP 选型决策案例）

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
