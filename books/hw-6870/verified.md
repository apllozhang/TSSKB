# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 快速入门与上电
- **C1** 开箱检查清单：机箱（含按订单电源/光模块）、Console 线、盲板、机架托架、国别电源线、橡胶桌脚、附赠螺丝与防静电袋；尽量靠近安装位开箱 <<<PAGE 16>>>
- **C2** 上电流程：全部电源线插入易触及的接地插座（禁延长线）→ 自动上电启动；多电源纪律——"be sure to plug in each power supply in rapid succession, (i.e., within a few seconds of each other)"（保证启动全程供电充足）<<<PAGE 17>>>/<<<PAGE 18>>>
- **C3** 首次登录六步：console 登录（admin/switch）→ 解锁会话类型 → 改密码 → 设时区 → 设日期时间 → 设可选项并 `write memory` 保存 <<<PAGE 18>>>/<<<PAGE 21>>>
- **C4** 解锁会话类型：全部 `aaa authentication default local`；单个解锁 `aaa authentication telnet local` / `aaa authentication http local`；一条命令只能一个会话类型，多条连用解锁多个 <<<PAGE 19>>>
- **C5** 改密码四步：admin 登录 → `password` 回车 → 输新密码 → 再输一次；实时保存进本地用户库、重启保留 <<<PAGE 19>>>/<<<PAGE 20>>>
- **C6** 时间与可选项：`system timezone`/`system daylight-savings-time`（默认 UTC）；`system time hh:mm:ss`/`system date mm/dd/yyyy`；`system contact`/`system name`/`system location`（位置信息便于远程定位）；查看 `show system`；保存 `write memory` <<<PAGE 20>>>/<<<PAGE 21>>>
## 机架与桌面安装
- **C7** 弹簧夹法兰安装五步：①弹簧夹置 out（脱开）位 ②tab 插入机箱槽位 ③按压法兰至"CLICK"入 in（锁定）位 ④附带螺丝固定 ⑤对侧重复；再加后支架导轨与后支架 <<<PAGE 42>>>/<<<PAGE 43>>>/<<<PAGE 44>>>
- **C8** 机架装机六步（双人）：①预标记孔位 ②一人抬起使法兰贴平机架立柱 ③孔位对齐 ④第二人先插入每侧法兰底部螺丝并拧紧 ⑤装顶部螺丝全部拧紧 ⑥后支架滑入导轨并固定到机架 <<<PAGE 44>>>/<<<PAGE 45>>>
- **C9** 机架安装纪律：双人（一人抬一人拧）；机架螺丝由机架厂商提供（ALE 不附）；尽量装机架下部防头重；relay rack 按机架厂商规范固定 <<<PAGE 41>>>/<<<PAGE 42>>>
- **C10** 盲板安装两步：①盲板箭头朝上对准空电源槽位 ②插入空槽用附带螺丝固定；空模块槽与电源槽位任何时候都应装盲板 <<<PAGE 40>>>/<<<PAGE 41>>>
- **C11** 独立桌面安装三步：①4 个橡胶脚垫插入底面板孔 ②"right side up"正放于稳固平面（承重按满配重量）③接网络/管理线缆；保证气流间隙且在 AC 插座可达范围 <<<PAGE 46>>>/<<<PAGE 47>>>
## 电源安装与更换（热插拔）
- **C12** 装电源两步：①电源插入机箱后部电源槽并后滑至 securely seated 接入背板——连接器完全就位时锁片（lock tab）"咔哒"锁定 ②电源线插入电源插座（接电即开机，无开关）<<<PAGE 55>>>/<<<PAGE 56>>>
- **C13** 拆电源三步：①先从电源源断开电源线，再从电源壳拔出电源线 ②向电源中心按压锁片释放 ③按住锁片将电源直向后拉出槽位；不回装时须装盲板盖空槽 <<<PAGE 56>>>/<<<PAGE 57>>>
- **C14** DC 线缆连接：线缆连接器端插入电源接口直至"clicks firmly into place"；另一端三根 12AWG 线（绿黄=地/黑=return/红=-48VDC）接熔丝面板或 -48VDC 源，注意极性 <<<PAGE 54>>>
- **C15** DC 安全五则：接可靠接地 -48VDC SELV 源；分支过流保护 15A；12AWG 铜导体；现场布线含易触及断开装置；必须安装在受限进入场所 <<<PAGE 54>>>
- **C16** 机箱接地：后部 paint-free 双螺纹孔装 Panduit LCD8-10A-L lug + 10-32 3/8" 螺丝 + 8AWG 铜导线，接大地，扭矩 30-60 in-lb <<<PAGE 57>>>
## 监控与 PoE 配置
- **C17** 硬件监控三板斧：`show module` / `show module long` / `show temperature`（含各槽位 Danger/Thresh/Status）<<<PAGE 58>>>
- **C18** Dying Gasp Link OAM 配置三命令：`efm-oam admin-state enable` → `efm-oam port 1/1/23-34 admin-state enable` → `efm-oam port 1/1/23-24 propagate-events dying-gasp enable` <<<PAGE 60>>>
- **C19** PoE 物理激活：`lanpower slot 2/1 service start`（逐 slot，首次激活唯一途径）；被断电端口重启用 `lanpower port 2/1/1-24 admin-state enable` <<<PAGE 65>>>
- **C20** 关 PoE：单口 `lanpower port 1/1/12 admin-state disable`；整 slot `lanpower slot 1/1 service stop` <<<PAGE 66>>>
- **C21** 开 4pair/bt：`lanpower 4pair`（60/75/95W，802.3at 4 对+PoH）；`lanpower 8023bt`（bt Type3/4 Class 5-8）<<<PAGE 65>>>
- **C22** 调口/槽功率上限：`lanpower port 1/1/24 power 3000`（口上限降 3W）；`lanpower slot 3/1 maxpower 400`（slot 上限降 400W，注意可致低优先级口断电）<<<PAGE 66>>>
- **C23** 设口优先级：`lanpower port 1/1/6 priority critical`（关键任务 PD 专用）<<<PAGE 67>>>
- **C24** 电容检测开关：`lanpower slot 3/1 capacitor-detection enable`（仅传统 IP 话机兼容）<<<PAGE 67>>>
- **C25** Priority Disconnect 开关：`lanpower slot 2/1 priority-disconnect disable|enable`（默认启用）<<<PAGE 69>>>
- **C26** Guard Band 放行小功率 PD：余 50W、口上限 75W 拒载时 `lanpower power 1/1/1 power 10000`（口上限降 10W）即可放行 4W PD <<<PAGE 68>>>
- **C27** PoE 状态查看：`show powersupply`（电源类型/瓦数/状态）；`show lanpower slot 1/1` 或 `show lanpower 1`（逐口最大功率/实际用量/状态/优先级/开关/Class + slot 总预算/剩余）<<<PAGE 63>>>/<<<PAGE 64>>>/<<<PAGE 70>>>/<<<PAGE 71>>>

## counter-examples

## 环境与安装限制
- **X1** 禁止倒放/侧放运行："Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 46>>>
- **X2** 气流阻塞后果："Restricted airflow can cause your switch to overheat, which can lead to switch failure."；"Never obstruct chassis air vents." <<<PAGE 16>>>/<<<PAGE 40>>>
- **X3** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover plates should remain installed at empty module slots and power supply bays at all times." <<<PAGE 41>>>/<<<PAGE 79>>>
- **X4** 盲板方向限制：装电源槽盲板时箭头必须朝上："When installing blank cover panels over power supply slots, orient the cover panels with the arrows pointing up." <<<PAGE 41>>>
- **X5** 机架螺丝自备："Alcatel-Lucent does not provide rack-mount screws. Use the screws supplied by the rack vendor." <<<PAGE 42>>>
- **X6** 专业安装者要求："Switches must be installed by a professional installer. It is the responsibility of the installer to ensure that proper grounding is available and that the installation meets applicable local and national electrical codes." / "Only personnel knowledgeable in basic electrical and mechanical procedures should install or maintain this equipment." <<<PAGE 14>>>/<<<PAGE 80>>>
- **X7** 双人机架纪律："Two people are required to rack mount the switch: One person to lift the chassis into position and one person to secure the chassis to the rack using the rack mount screws." <<<PAGE 41>>>
- **X8** 顶部/底部免间隙但不可叠压："No clearance is necessary at the top or bottom of the chassis."（对照：桌面安装须用四脚垫起）<<<PAGE 17>>>/<<<PAGE 46>>>
## 电气与电源警告
- **X9** 禁用延长线："each supplied AC power cord is 2 meters (approx. 6.5 feet). Do not use extension cords." <<<PAGE 14>>>/<<<PAGE 17>>>
- **X10** 多电源须快速相继上电："If you have more than one power supply installed, be sure to plug in each power supply in rapid succession, (i.e., within a few seconds of each other). This ensures that there will be adequate power for all components throughout the boot process." <<<PAGE 18>>>
- **X11** 高压输入才得高 PoE 功率："High power PoE wattages for this power supply are available at voltage inputs between 190-240VAC."（1200W/2000W 电源在 100-120V 市电降额）<<<PAGE 52>>>/<<<PAGE 53>>>
- **X12** 拆电源前先断源："When removing a power supply, first disconnect the power cord from the power source."（锁片释放后直向后拉）<<<PAGE 56>>>
- **X13** 无电源开关语义："Connecting an installed power supply to a power source will boot the switch. Likewise, disconnecting all installed power supplies from a power source will power off the switch." <<<PAGE 47>>>
- **X14** DC 极性三线规则：Green/yellow=ground、Black=return、Red=-48VDC；"Observe proper polarity when connecting to a fuse panel." <<<PAGE 54>>>
- **X15** DC 强制受限场所："It must be installed in a restricted access location."（DC 供电机型）<<<PAGE 54>>>
- **X16** DC 过流与线规："The branch circuit overcurrent protection must be rated 15A. Use 12AWG copper conductors." <<<PAGE 54>>>
- **X17** DC 地线 EMC 强制："For EMC/EMI, each DC/DC power supply requires that the ground wire is connected from each DC/DC power supply to Earth Ground." <<<PAGE 82>>>
- **X18** 电涌违规范即失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product." <<<PAGE 15>>>
- **X19** CDE 静电放电风险："Category 5e, Category 6, and Category 6a cables can store large amounts of static electricity... could lead to a Cable Discharge Event (CDE)."（接线前先对地放电）<<<PAGE 15>>>
- **X20** 室外裸线禁令："Never install exposed network cables outdoors." <<<PAGE 17>>>/<<<PAGE 79>>>
- **X21** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 80>>>
- **X22** 运行中勿触电源槽/背板："To reduce the risk of electrical shock, keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 81>>>
- **X23** 多电源检修全断电："Your switch is equipped with multiple power supplies. To reduce the risk of electrical shock, be sure to disconnect all power connections before servicing or moving the unit."（西语版特别提示可能有三根电源线）<<<PAGE 81>>>/<<<PAGE 85>>>
- **X24** 双电同源风险："Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 59>>>
## PoE 限制
- **X25** lanpower port admin-state 不能首次激活："You cannot use the lanpower port admin-state command to initially activate PoE on a port."（首次必须 lanpower slot service）<<<PAGE 65>>>/<<<PAGE 66>>>
- **X26** 开 Class 检测复位全机 PoE 口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 65>>>
- **X27** 电容检测不符 IEEE："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 67>>>
- **X28** 调低 slot 上限可致断电："Decreasing the slot-wide power could cause lower priority ports to lose power if the new value is less than the total PoE power currently being consumed." <<<PAGE 66>>>
- **X29** Guard Band 不保已在电 PD："The Guard Band functionality does not apply to PDs that are already powered up."（预算缩减改由 priority disconnect 裁决）<<<PAGE 68>>>
- **X30** Z 系列电源限制：PS-2000W-AC-POE-2 仅支持 OS6870-P24M/P48M，P24Z/P48Z 标 N/A（预算规划不可套用 2000W）<<<PAGE 47>>>/<<<PAGE 63>>>
## 温度与监控限制
- **X31** Danger 阈值不可配置："The danger threshold is factory-set and cannot be configured by the user."（超限即自动关机须手动重启）<<<PAGE 59>>>
- **X32** 温度超限处置顺序：Warning→查气流阻塞/室温/阈值是否设得过低；Danger→查气流阻塞/室温后手动开机 <<<PAGE 58>>>/<<<PAGE 59>>>
## 操作与人身安全警告
- **X33** Class 1M 激光警告："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."（全机型前面板固定标识）<<<PAGE 23>>>等
- **X34** 不可见激光辐射："Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When removing cables do not stare into the open apertures."（空口装保护盖）<<<PAGE 81>>>
- **X35** ESD 纪律："Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 83>>>
- **X36** 受限场所要求："This equipment should be installed in a location that restricts access." <<<PAGE 83>>>
- **X37** 锂电池更换纪律（西语警告）："Hay un peligro de la explosión si la batería del litio en su chasis se substituye incorrectamente."（只能换同型号/等效型号，旧电池寄回工厂）<<<PAGE 84>>>
- **X38** 半双工不支持："Does not support half-duplex connections."（全部 RJ45 机型）<<<PAGE 23>>>等
- **X39** 密码丢失后果："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 20>>>
- **X40** 解锁远程会话即开放远程访问："When you unlock session types, you are granting switch access to non-local sessions (e.g., Telnet)." <<<PAGE 19>>>
- **X41** 单命令单会话类型："You cannot specify more than one session type in a single command line."（解锁多个须连发多条 aaa authentication）<<<PAGE 19>>>
- **X42** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments."（台湾 BSMI 版；另有 FCC/CISPR22/VCCI/Korea 同义条款）<<<PAGE 79>>>
- **X43** FCC 擅改失权："Changes and modifications made to the equipment without approval of the manufacturer could void the user's authority to operate this equipment."（建议只用屏蔽接地线缆）<<<PAGE 78>>>
- **X44** 接地lug规范强制："connect a Panduit Corporation UL listed Lug, (Part number LCD8-10A-L) to the two threaded holes... using protective earthing conductor wire and 8AWG copper conductors. Torque to between 30-60 inch pounds." <<<PAGE 54>>>
- **X45** VFL 推荐 25G：SFP28 口 "(25G recommended for VFL)"（VFL 应用建议跑 25G 速率）<<<PAGE 23>>>等

## frameworks

- **F1** 6870 九机型选型矩阵（PoE 等级 × 上行速率 × 模块化）：
  | 机型 | 下行 | 下行 PoE | 上行 | 模块槽 |
  |---|---|---|---|---|
  | OS6870-24 | 24×1G RJ45 | 无 | 4×SFP28(25G)+2×QSFP28(100G) | 无 |
  | OS6870-48 | 48×1G RJ45 | 无 | 4×SFP28+2×QSFP28 | 无 |
  | OS6870-P24M | 24×多千兆(10G) | 95W bt | 2×QSFP56(200G) | 有 |
  | OS6870-P48M | 48×多千兆(5G) | 95W bt | 2×QSFP56 | 有 |
  | OS6870-P24Z | 24×多千兆(2.5G) | 60W bt | 6×SFP28+2×QSFP28 | 无 |
  | OS6870-P48Z | 48×多千兆(2.5G) | 60W bt | 6×SFP28+2×QSFP28 | 无 |
  | OS6870-V12 | 12×SFP28 | 无 | 2×QSFP56 | 有 |
  | OS6870-CNI-U2 | — | — | 2×QSFP28 | 无 |
  | OS6870-LNI-U6 | — | — | 6×SFP56(50G) | 无 |
  决策三问：要不要 95W AP（→M）；要不要 200G/后配上行（→M/V12）；预算型 60W PoE（→Z）<<<PAGE 12>>>/<<<PAGE 23>>>-<<<PAGE 38>>>
- **F2** PoE 供电预算四变量联动框架：
  ① 机型（决定可用电源型号与每口能力）② 电源瓦数（600W/1200W/2000W；Z 系列上限 1200W）③ 单/双电源（双电负载分担、预算非简单翻倍，如 P24M 双 600W=788W）④ 市电电压（双值条目=低压/高压输入；1200W/2000W 需 190-240VAC 才得高 PoE 功率）→ 查预算表得总瓦数，再叠加 Guard Band（口上限 vs 剩余）与 Priority Disconnect（low/high/critical + 端口号 1 高 48 低）两级裁决；落地检查命令 `show lanpower slot` <<<PAGE 47>>>/<<<PAGE 51>>>-<<<PAGE 53>>>/<<<PAGE 63>>>/<<<PAGE 67>>>-<<<PAGE 70>>>
- **F3** 6870 上电-入网标准七步流程（cangjie 可执行框架）：
  ① 安装（机架双人/桌面四脚，盲板常装）② 多电源数秒内相继插电 ③ 观察 OK/PS LED 至启动完成 ④ console 115200-8N1 rollover 登录 admin/switch ⑤ 解锁会话（aaa authentication … local）⑥ 改密+时区+时间+contact/name/location ⑦ `write memory` 保存；PoE 机型追加 `lanpower slot service start` 物理激活 <<<PAGE 17>>>-<<<PAGE 21>>>/<<<PAGE 65>>>
- **F4** 电源选型与演进框架（同一 P 系列机箱内三档平滑升级）：
  600W（入门，P24M 单电 242W/P48M 单电 216W PoE）→ 1200W（中档，双电 1516-1880W；190-240VAC 建议）→ 2000W（高密 95W bt，仅 M 系列，P48M 双电最高 3309W）；支持混插（"Mixing different wattage power supplies in a chassis is supported"），扩容可先混后替 <<<PAGE 47>>>/<<<PAGE 51>>>-<<<PAGE 53>>>/<<<PAGE 63>>>

## glossary

- **OS6870-24**：24×1G RJ45 + 4×SFP28 + 2×QSFP28 固定配置 1U 非 PoE 机型，待机 71W <<<PAGE 12>>>/<<<PAGE 23>>>/<<<PAGE 24>>>
- **OS6870-48**：48×1G RJ45 + 4×SFP28 + 2×QSFP28 固定配置 1U 非 PoE 机型，待机 73W <<<PAGE 12>>>/<<<PAGE 29>>>/<<<PAGE 30>>>
- **OS6870-P24M**：模块化 24 口多千兆（至 10G）95W bt PoE + 2×QSFP56 + 上行模块槽，待机 219.6W <<<PAGE 12>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **OS6870-P48M**：模块化 48 口多千兆（至 5G）95W bt PoE + 2×QSFP56 + 上行模块槽，待机 251.8W <<<PAGE 12>>>/<<<PAGE 31>>>/<<<PAGE 32>>>
- **OS6870-P24Z**：固定 24 口多千兆（至 2.5G）60W bt PoE + 6×SFP28 + 2×QSFP28，待机 90.2W <<<PAGE 12>>>/<<<PAGE 27>>>/<<<PAGE 28>>>
- **OS6870-P48Z**：固定 48 口多千兆（至 2.5G）60W bt PoE + 6×SFP28 + 2×QSFP28，待机 92.4W <<<PAGE 12>>>/<<<PAGE 33>>>/<<<PAGE 34>>>
- **OS6870-V12**：12×SFP28 全光机型 + 2×QSFP56 + 上行模块槽，无铜口 <<<PAGE 12>>>/<<<PAGE 35>>>/<<<PAGE 36>>>
- **OS6870-CNI-U2**：2×QSFP28 100G 上行扩展节点机箱 <<<PAGE 12>>>/<<<PAGE 37>>>
- **OS6870-LNI-U6**：6×SFP56 50G 上行扩展节点机箱 <<<PAGE 12>>>/<<<PAGE 38>>>
- **Uplink Module Slot**：M 系列/V12 具备的上行模块插槽，上行形态可后置扩展 <<<PAGE 12>>>/<<<PAGE 25>>>
- **SFP28**：支持 1G/10G/25G 的小封装光模块口（25G 推荐用于 VFL）<<<PAGE 23>>>等
- **QSFP28**：支持 40G/100G/4X10G/4X25G 的四通道光模块口 <<<PAGE 23>>>等
- **QSFP56**：支持 40G/100G/200G/4X10G/4X25G 的增强四通道光模块口 <<<PAGE 25>>>等
- **VFL（Virtual Fabric Link）**：ALE 虚拟光纤链路技术，端口可作 VFL 或普通上行（LED 琥珀=VFL）<<<PAGE 23>>>/<<<PAGE 39>>>
- **多千兆（Multi-gigabit）**：2.5G/5G/10G RJ45 端口技术，配 802.3bt 大功率 PoE <<<PAGE 12>>>

## 电源（Ch3）
- **PS-250W-AC（OS6870-BP）**：250W AC 电源（100-240VAC，12V/20.8A 输出，无 PoE 输出）<<<PAGE 48>>>
- **PS-250W-DC（OS6870-BP-D）**：250W DC 电源（-42~-60V/8A 输入）<<<PAGE 49>>>
- **PS-550W-AC-2（OS6870-BPH）**：550W AC 电源（12V/45.8A，V12 机型用）<<<PAGE 50>>>
- **PS-600W-AC-POE-2（OS6870-BPPH）**：600W PoE 电源（54.5V/11A，P 系列用）<<<PAGE 51>>>
- **PS-1200W-AC-POE-2（OS6870-BPPX）**：1200W PoE 电源（54.5V/22.02A；高 PoE 功率需 190-240VAC）<<<PAGE 52>>>
- **PS-2000W-AC-POE-2（OS6870-BPXL）**：2000W PoE 电源（54.5V/36.7A；仅 P24M/P48M）<<<PAGE 53>>>
- **负载分担（Load Sharing）**：双电源均分供电负荷（含 PoE）<<<PAGE 47>>>/<<<PAGE 51>>>
- **电源混插（Mixing wattage）**：同一机箱允许安装不同瓦数电源 <<<PAGE 51>>>
- **Lock Tab（锁片）**：电源就位"咔哒"锁定/按压释放的机构 <<<PAGE 55>>>/<<<PAGE 57>>>
- **Smart on**：电源待机智能开启状态（绿闪 LED 表示）<<<PAGE 48>>>/<<<PAGE 50>>>
- **12VSB**：电源待机输出（12V standby，0.1A）<<<PAGE 48>>>等
- **CBN（Common Bonding Network）**：共同联结网络，DC 设备设计安装环境 <<<PAGE 54>>>
- **Isolated DC Return（DC-I）**：隔离式 DC 回流导体（黑线 return）<<<PAGE 54>>>

## LED 与监控（Ch3）
- **OK LED**：稳绿=诊断与 AOS 启动 OK、闪绿=进行中、稳琥珀=启动失败 <<<PAGE 38>>>
- **VC LED**：稳绿=Master、稳琥珀=Slave、灭=未知/错误 <<<PAGE 38>>>
- **PS LED**：稳绿=电源正常、稳琥珀=单/双电源故障、灭=无电源 <<<PAGE 38>>>
- **GRN (Leaf) LED**：稳绿=省电模式（power saving）、灭=正常模式 <<<PAGE 38>>>
- **VC ID LED**：多灯数值相加等于 VC 单元号 <<<PAGE 39>>>
- **RJ45 四色速率 LED**：绿=10/100/1000、蓝=2.5G、品红=5G、琥珀=10G <<<PAGE 39>>>
- **EMP port**：后部以太网管理端口 <<<PAGE 23>>>等
- **show module / show module long**：槽位基本/详细信息命令 <<<PAGE 58>>>
- **show temperature**：温度监控命令（Current/Range/Danger/Thresh/Status）<<<PAGE 58>>>
- **Warning 阈值**：用户可配温度告警阈值，超限发 trap 业务继续 <<<PAGE 58>>>/<<<PAGE 59>>>
- **Danger 阈值**：出厂固化温度阈值，超限自动关机须手动启动 <<<PAGE 59>>>
- **Dying Gasp**：掉电告别机制（SNMP trap + Syslog + Link OAM PDU 三通道）<<<PAGE 59>>>
- **efm-oam propagate-events dying-gasp**：端口发 Dying Gasp OAM PDU 的使能命令 <<<PAGE 60>>>
- **swlog output socket**：添加 Syslog 服务器命令 <<<PAGE 60>>>
- **snmp station**：配置 SNMP 接收站命令 <<<PAGE 60>>>

## PoE（Ch4）
- **PSE（Power Source Equipment）**：供电设备，检测 PD、可选分级、供电、监控、回缩 <<<PAGE 61>>>
- **PD（Powered Device）**：受电设备（AP/IP 话机/以太网集线器等）<<<PAGE 61>>>
- **802.3bt**：第 4 代 PoE 标准（Type 3/4，Class 5-8：45/60/75/90-99W，4 对线）<<<PAGE 62>>>/<<<PAGE 65>>>
- **PoH**：Power over Harness，配合 `lanpower 4pair` 提供 60/75/95W <<<PAGE 65>>>
- **lanpower slot service**：逐 slot 物理激活/停止 PoE（首次激活唯一途径）<<<PAGE 63>>>/<<<PAGE 65>>>
- **lanpower port admin-state**：单口 PoE 管理开关（仅限重激活/关断，不能首次激活）<<<PAGE 65>>>
- **lanpower power / lanpower slot maxpower**：设单口/整槽功率上限（不预留）<<<PAGE 63>>>/<<<PAGE 66>>>
- **lanpower priority**：设口优先级 low/high/critical（默认 low）<<<PAGE 63>>>/<<<PAGE 67>>>
- **lanpower 4pair / lanpower 8023bt**：开 4 对 60-95W / 开 bt Class 5-8 <<<PAGE 65>>>
- **lanpower slot class-detection**：开 Class 检测（复位全部 PoE 口）<<<PAGE 65>>>
- **lanpower capacitor-detection**：开电容检测（仅老式 IP 话机，不符 IEEE）<<<PAGE 63>>>/<<<PAGE 67>>>
- **lanpower slot priority-disconnect**：开关 priority disconnect（默认启用）<<<PAGE 63>>>/<<<PAGE 69>>>
- **Guard Band**：剩余预算小于口上限/类最大值即拒载新 PD 的机制 <<<PAGE 67>>>/<<<PAGE 68>>>
- **Priority Disconnect**：预算不足时按优先级+物理端口号（1 最高→48 最低）裁决 <<<PAGE 68>>>/<<<PAGE 69>>>
- **show powersupply / show lanpower slot**：电源状态 / PoE 逐口与预算状态命令 <<<PAGE 63>>>/<<<PAGE 64>>>/<<<PAGE 71>>>

## 管理与登录（Ch2）
- **admin/switch**：出厂默认管理员账号/密码 <<<PAGE 18>>>
- **aaa authentication**：解锁会话类型命令族（default/telnet/http/ftp 等逐个解锁）<<<PAGE 19>>>
- **rollover 线**：console 串口反转线缆类型 <<<PAGE 17>>>
- **115200-8N1**：console 默认串口参数（波特率 115200、8 数据位、无校验、1 停止位）<<<PAGE 17>>>
- **system location**：设置交换机物理位置（远程定位用）<<<PAGE 20>>>
- **show system / write memory**：查看系统信息 / 保存配置 <<<PAGE 21>>>
- **WebView**：ALE 内嵌 Web 管理界面（可从 OmniVista 或浏览器启动）<<<PAGE 62>>>

## 安装部件（Ch3）
- **弹簧夹法兰（Spring Clip Flange）**：out 位插 tab、按至"CLICK"入 in 位的免工具机架法兰 <<<PAGE 42>>>/<<<PAGE 43>>>
- **后支架/后支架导轨（Rear Bracket / Rear Bracket Guide）**：机架后部支撑件 <<<PAGE 44>>>
- **橡胶桌脚（Rubber Feet）**：桌面安装四脚垫 <<<PAGE 46>>>
- **盲板（Blank Cover Panel）**：盖空槽位、导气流、护内部件；电源槽安装箭头朝上 <<<PAGE 40>>>/<<<PAGE 41>>>
- **接地 lug（Panduit LCD8-10A-L）**：后部双螺纹孔接地端子，配 8AWG、10-32 3/8" 螺丝、30-60 in-lb <<<PAGE 54>>>/<<<PAGE 57>>>
- **Chassis 温度 vs Ambient 温度**：机箱内部传感器读数 vs 近似室温（前者恒高）<<<PAGE 24>>>等

## 标准与合规（附录 A）
- **UL 62368-1 / IEC 62368-1**：音视频与 IT 设备安全标准 <<<PAGE 76>>>
- **EN 55032 / EN 55035**：EMI 与抗扰度标准 <<<PAGE 77>>>
- **Hi-Pot Test**：IEEE 802.3 耐压测试（全部以太网口 2250VDC）<<<PAGE 77>>>
- **FCC Part 15 Class A**：商用级电磁干扰限值（住宅干扰需自费整改）<<<PAGE 78>>>
- **Class 1M Laser**：开启时有 1M 级激光辐射、勿用光学仪器直视 <<<PAGE 23>>>等/<<<PAGE 79>>>
- **Prop 65**：加州 65 号提案警告（铅化合物）<<<PAGE 75>>>
- **WEEE / RoHS**：欧盟回收指令 / 有害物质限制（中国、台湾表）<<<PAGE 72>>>-<<<PAGE 74>>>
- **CDE（Cable Discharge Event）**：线缆静电放电事件；接线前对地放电 <<<PAGE 15>>>
- **ESD 腕带（Wrist Strap）**：防静电腕带，接触部件前消除人体/环境静电 <<<PAGE 83>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安保措施的维护人员可进入的安装位置 <<<PAGE 83>>>

## principles

## 家族与端口架构
- **P1** 九机型三分类：非 PoE 固定（-24/-48/V12/CNI-U2/LNI-U6）；`P*M` 模块化（95W bt 多千兆 + QSFP56 200G + 1 上行模块槽）；`P*Z` 固定（60W bt 多千兆到 2.5G + QSFP28 100G + 6 SFP28）<<<PAGE 12>>>
- **P2** 上行速率阶梯：SFP28 支持 1G/10G/25G（25G 推荐用于 VFL）；QSFP28 支持 40G/100G/4X10G/4X25G；QSFP56 支持 40G/100G/200G/4X10G/4X25G <<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 35>>>
- **P3** M 系列独占 Uplink Module Slot（上行模块槽），P24M/P48M/V12 三机型具备，上行形态可后置扩展 <<<PAGE 12>>>/<<<PAGE 25>>>/<<<PAGE 31>>>/<<<PAGE 35>>>
- **P4** V12 全光机型：12× SFP28（25G 推荐 VFL）+ 2× QSFP56 200G + 上行模块槽，无铜口 <<<PAGE 12>>>/<<<PAGE 35>>>
- **P6** 全家族统一环境包络：Tmra 0-45°C、存储 -40~85°C、湿度 5%-95% 无凝结、1U（4.4cm 高）<<<PAGE 24>>>-<<<PAGE 36>>>
- **P8** 待机/满载功耗阶梯：-24=71/100.9W；P24M=219.6/313.2W；P24Z=90.2/173.6W；-48=73/105.2W；P48M=251.8/343.9W；P48Z=92.4/215W；V12=73/157.8W <<<PAGE 24>>>-<<<PAGE 36>>>
- **P9** chassis 与 ambient 温度语义区分："Chassis temperature refers to the sensor reading of the internal switch temperature (threshold or danger). Ambient temperature refers to the approximate room temperature."（机箱温度恒高于室温）<<<PAGE 24>>>等
## 可用性特性
- **P10** 三大可用性支柱：Power Supply Redundancy（双电源负载分担）、Hot-Swapping（不断电增删部件）、Hardware Monitoring（自动：内置传感器超阈值立即发 trap；LED；用户主动 show 命令）<<<PAGE 13>>>
## 电源机制
- **P11** 六型电源矩阵：PS-250W-AC(12V/20.8A)、PS-250W-DC(-42~-60V/8A)、PS-550W-AC(V12 专用)、PS-600W/1200W/2000W-AC-POE(54.5V 输出，P 系列用)；250W 仅 -24/-48/V12；2000W 仅 P24M/P48M <<<PAGE 47>>>/<<<PAGE 48>>>-<<<PAGE 53>>>
- **P12** 负载分担与混插："If a second power supply is installed the two power supplies will load share." / "Mixing different wattage power supplies in a chassis is supported." <<<PAGE 47>>>/<<<PAGE 51>>>-<<<PAGE 53>>>
- **P13** 无总开关设计："The chassis does not provide an on/off switch. Connecting an installed power supply to a power source will boot the switch."（拔掉全部电源线即关机）<<<PAGE 47>>>/<<<PAGE 56>>>
- **P14** PoE 电源高压输入才有全功率：1200W 与 2000W 电源 "High power PoE wattages for this power supply are available at voltage inputs between 190-240VAC."（100-120V 输入时降额）<<<PAGE 52>>>/<<<PAGE 53>>>
- **P15** 电源双 LED 语义（PoE 型为 DC+AC 双灯）：绿闪+绿=仅待机输出；绿+绿=正常；红+绿=故障/关断；绿闪+红=AC 不在位 <<<PAGE 51>>>-<<<PAGE 53>>>
- **P16** 250W AC 单 LED 五态：绿=正常；琥珀=AC 线拔出或掉电（另一电源仍在）/严重事件关断；绿闪=Smart on 待机；琥珀闪=带告警运行；灭=全电源无 AC <<<PAGE 48>>>/<<<PAGE 49>>>
- **P17** DC 三线色彩语义：绿黄=ground、黑=return、红=-48VDC；回流导体为 Isolated DC Return（DC-I）；设备设计安装于 CBN（共同联结网络）<<<PAGE 54>>>
- **P18** 冗余 AC 分电路原则："It is recommended that each AC outlet resides on a separate circuit." <<<PAGE 14>>>
- **P19** 温度双阈值机制：Warning（用户可配）超限→发 trap 但业务继续，应查气流/室温/阈值设置；Danger 超限→自动关机直到人工处理并手动启动，且 Danger 出厂固化："The danger threshold is factory-set and cannot be configured by the user." <<<PAGE 58>>>/<<<PAGE 59>>>
- **P21** Dying Gasp 机制与三通道：全电源丢失时维持电力发 SNMP trap（前 3 站，含槽位/电源类型/时间）+ Syslog "Dying Gasp Power Failure Event Occurred"（前 3 服务器）+ 4 个 802.3ah OAM PDU（Dying Gasp bit 置位，上行口优先）<<<PAGE 59>>>/<<<PAGE 60>>>
- **P22** 系统 LED 五组：OK（稳绿=诊断与启动 OK/闪绿=进行中/稳琥珀=失败）；VC（稳绿=Master/稳琥珀=Slave/灭=未知）；PS（稳绿=正常/稳琥珀=单双电源故障/灭=无电源）；GRN（稳绿=省电模式/灭=正常模式）；VC ID（多灯数值相加=VC ID）<<<PAGE 38>>>
- **P23** RJ45 口四色速率 LED：绿=10/100/1000、蓝=2.5G、品红=5G、琥珀=10G（稳/闪=链路/活动）；LED2 琥珀=PoE 使能 <<<PAGE 39>>>
- **P24** SFP28/QSFP28/QSFP56 端口 LED 两色：绿=有效上行、琥珀=有效 VFL <<<PAGE 39>>>
## PoE 机制
- **P25** 911/UPS 供电纪律："It's recommended that PoE-enabled switches with attached IP telephones should have operational power supply redundancy at all times for 911 emergency requirements." <<<PAGE 61>>>
- **P26** PoE 标准栈：802.3/802.3af/802.3at/802.3bt；每口范围 at 口 3000-30000mW、bt 口 3000-95000mW；Class 0-8 梯度表（Class 5=45W/6=60W/7=75W/8=90-99W，4 对线 Type 3/4）<<<PAGE 62>>>/<<<PAGE 65>>>
- **P27** PoE 预算四变量模型：机型 × 电源瓦数（600/1200/2000W）× 单/双电源 × 电压输入档（双值条目=低压/高压输入），如 P24M 双 1200W=1516W/1880W、双 2000W=1516W/2280W；P48M 双 2000W 最高 3309W；Z 系列不支持 2000W 电源 <<<PAGE 63>>>
- **P28** PoE 激活两级模型：软件默认 administratively enabled，但必须逐 slot `lanpower slot service start` 物理激活："you must issue the lanpower slot service command on a slot-by-slot basis before any connected PDs will receive inline power." <<<PAGE 65>>>
- **P29** 4pair 与 8023bt 使能链：`lanpower 4pair` 开 60/75/95W（802.3at 4 对 + PoH）；`lanpower 8023bt` 开 bt 双 Type 四 Class（5-8）<<<PAGE 65>>>
- **P30** Class 检测默认关：不开启也按预算供电；严格按类限功率需 `lanpower slot class-detection` 显式开启，且开启复位全机 PoE 口："Enabling class detection will reset all PoE ports on the chassis." <<<PAGE 65>>>
- **P31** 端口/槽最大功率语义：只设上限不做预留："Changing the maximum power available to a slot or port does not reserve or immediately allocate that power." <<<PAGE 67>>>
- **P32** 三级端口优先级：low（默认，先断）/high（次保）/critical（尽量保），`lanpower port priority` 逐口设置 <<<PAGE 67>>>
- **P33** Priority Disconnect 四场景裁决：禁用→一律拒新 PD；启用+同级→按物理端口号（1 最高→48 最低）；启用+新 PD 最高优先级→新 PD 必得电，先断最低优先级口、同级断物理端口号最大口；启用+新 PD 最低→拒新 PD <<<PAGE 69>>>/<<<PAGE 70>>>
- **P34** Guard Band 拒载机制：剩余预算 < 端口最大功率或 PD 类最大值即拒载，即使实际只需 4W（例：余 50W、口上限 75W→拒；调上限 10W→放行）；不作用已在电 PD，预算缩减场景由 priority disconnect 裁决 <<<PAGE 67>>>/<<<PAGE 68>>>
- **P35** 电容检测默认禁用："The capacitive detection method should only be enabled to support legacy IP phones. This feature is not compatible with IEEE specifications." <<<PAGE 67>>>
## 安装与安全机制
- **P36** 电涌防护军规五条：全设备等电位接地（≤0.01Ω）；室外/近交流线路用 STP Cat5e+；室外铜口串接浪涌保护器；防室外设备传浪涌给上游；Cat5e/6/6a 蓄静电须先对地放电防 CDE；违者可失保 <<<PAGE 15>>>
- **P37** 盲板气流机制："If your switch is not fully populated and blank cover panels are not installed over empty slot locations, airflow is adversely affected."（气流改道、风扇加负、内部件暴露）<<<PAGE 40>>>
- **P38** 接地规范：后部两螺纹孔（paint-free 保证金属接触）接 Panduit LCD8-10A-L lug、10-32 3/8" 螺丝、8AWG 铜导线、扭矩 30-60 in-lb，作为电源线接地的补充 <<<PAGE 54>>>/<<<PAGE 57>>>
- **P39** 气流间隙三向要求：前 6"、后 6"、左右各 2"，顶底免间隙："No clearance is necessary at the top or bottom of the chassis." <<<PAGE 16>>>/<<<PAGE 17>>>
- **P40** 机架安装五大考量（IEC 纪律）：Tmra（封闭机架内温度高于室温）、Reduced Air Flow、Mechanical Loading（防不均衡载荷）、Circuit Overloading、Reliable Earthing（经电源排接入尤须注意）<<<PAGE 39>>>
