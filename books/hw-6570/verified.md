# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 上电与首次登录
- **C1** 上电流程：各电源线插入易达接地插座（禁延长线）；多电源数秒内先后插电；冗余 AC 每路独立电路——接电即自动开机 <<<PAGE 13>>>/<<<PAGE 16>>>
- **C2** 首次登录六步：console 连接（9600-8N1，DCE）→admin/switch 登录→aaa authentication 解锁会话类型→password 改密→system timezone/time/date→system contact/name/location→show system 核对→write memory 保存 <<<PAGE 16>>>-<<<PAGE 19>>>
- **C3** 会话类型按类解锁：aaa authentication default local 全解锁；或逐类 aaa authentication telnet local / http local / ftp local 连续多条执行 <<<PAGE 18>>>
- **C4** 全宽机架安装流程（U28）：两侧装法兰→标记机架孔位→抬举对齐→先下孔螺丝后上孔螺丝全紧固；螺丝自备（not provided） <<<PAGE 29>>>/<<<PAGE 30>>>
- **C5** 单半宽机架安装流程（RM-19-L 套件）：L 支架长短臂任意侧装于机箱前部两侧→法兰孔对准机架孔→先下孔后上孔插入螺丝紧固 <<<PAGE 30>>>/<<<PAGE 31>>>
- **C6** 双半宽并排安装流程（DUO-MNT 套件）：slot 支架+slide 支架用 M3 平头螺丝装于两机前后→两机前后中央支架对齐滑合→盖板压前后支架用拇指螺丝固定→两侧装法兰→双人抬举入机架→先下孔后上孔紧固 <<<PAGE 32>>>-<<<PAGE 34>>>
- **C7** 现场准备检查单：维持机型规格表温湿度范围；预留机型对应气流间隙（12 口侧 2"/上下 1"；U28 上下 1RU/侧 2"）；每电源一个接地插座；2 米原装电源线；专业安装师负责接地与电气规范 <<<PAGE 13>>>/<<<PAGE 28>>>
- **C8** 开箱核对清单：机箱与电源按订单、光模块按订单、盲板、机架法兰、国别电源线、橡胶桌脚、螺丝、防静电袋与说明卡；就近开箱减少搬运 <<<PAGE 15>>>
- **C9** 电源安装流程：电源插入后部电源舱→滑入至背板锁扣"click"锁定→插电源线（接电即开机） <<<PAGE 41>>>
- **C10** 电源热拔流程：先从电源源头断电并拔出电源线→按锁扣向电源中心→按住锁扣直拉抽出；不回装则盖盲板 <<<PAGE 42>>>/<<<PAGE 43>>>
- **C11** 电源托盘安装流程：托盘 4 螺丝固定机箱→电源装托盘并以支架 2 螺丝固定→盖板 2 螺丝→附赠扎带理线；AC/DC 电源共用同款托盘 <<<PAGE 44>>>
## DC 接线与接地
- **C12** DC 线束接线流程（BP-D）：三芯 12AWG 线束连接器端插电源三孔（至牢固 click）→另一端按极性接 -48VDC 熔丝面板（绿黄=地/黑=return/红=-48VDC）→绿黄线接大地；前提五条（-48VDC SELV 可靠接地源/15A 过流/12AWG/易达断路装置/受限场所） <<<PAGE 40>>>
- **C13** 机箱 supplemental 接地流程：Panduit LCD8-10A-L lug 装 10-32 螺丝至接地耳无漆区→8AWG 铜线接大地；DC 场景后板双接地孔同规格加装——补充 AC 线接地 <<<PAGE 40>>>/<<<PAGE 45>>>
## 监控与 Dying Gasp 配置
- **C14** 硬件巡检流程：show module / show module long 查槽位→show temperature 查 Current/Range/Danger/Thresh/Status（UNDER THRESHOLD 为正常） <<<PAGE 45>>>
- **C15** 温度超限处置流程：Warning（trap 已发、业务未停）→查气流遮挡+查室温；Danger（已自动关机）→查气流遮挡+查室温→处理后手动重启 <<<PAGE 45>>>/<<<PAGE 46>>>
- **C16** Dying Gasp OAM 配置：efm-oam admin-state enable→efm-oam port 1/1/23-24 admin-state enable→efm-oam port 1/1/23-24 propagate-events dying-gasp enable——PDU 上联口优先发送 <<<PAGE 47>>>
- **C17** DG 告警接收配置：snmp station 配置 SNMP 站（收 trap，前 3 站生效）；swlog output socket 加 Syslog 服务器（收"Dying Gasp Power Failure Event Occurred"，前 3 服务器生效） <<<PAGE 46>>>/<<<PAGE 47>>>

---
合计：17 条（C1-C17）。

## counter-examples

## 平台与电源限制
- **X1** 全机型不支持半双工："The OS6570M-12 does not support half-duplex connections."（12D/U28 同句） <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>
- **X2** 双冗余电源必须同规格："both power supplies must have identical output wattage and identical nominal output voltage. Use of dissimilar power supplies could result in unexpected behavior and is not supported."（12D；U28 双舱同理适用） <<<PAGE 24>>>
- **X3** 温度阈值固化不可改："The threshold values are factory-set and cannot be modified."（Warning/Danger 均不可配） <<<PAGE 45>>>
- **X4** Danger 超限必须手动重启："the switch will power off until the temperature conditions have been addressed and the switch is manually booted."——不会自动恢复 <<<PAGE 46>>>
- **X5** aaa authentication 一次一类："You cannot specify more than one session type in a single command line." <<<PAGE 18>>>
- **X6** 密码覆盖受限："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 18>>>
- **X7** 非本机文档范围："it is not intended as a software users guide"——软件配置需查 AOS 8 各软件手册 <<<PAGE 8>>>
## 安装与环境警告
- **X8** 禁延长线："Do not use extension cords."（电源要求与上电流程两处） <<<PAGE 13>>>/<<<PAGE 16>>>
- **X9** 非 ALE 电源线需自证合规："If using a non-ALE provided power cord the installer shall confirm it meets the minimum electrical requirements of the power source."（ALE 线 UL 认可 IEC 62368-1） <<<PAGE 13>>>
- **X10** 违反电涌军规可能失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product."（五条：接地 0.01 欧姆以下/STP/浪涌保护器/室外线缆防雷电流上传/CDE 静电放电先接地） <<<PAGE 14>>>
- **X11** 室外禁裸线缆："Never install exposed network cables outdoors." <<<PAGE 15>>>/<<<PAGE 54>>>
- **X12** 气流遮挡致失效："Restricted airflow can cause your switch to overheat, which can lead to switch failure." <<<PAGE 28>>>
- **X13** 密闭多机架环温偏高："If installed in a closed or multi-rack assembly, the operating ambient temperature of the environment may be greater than the room's ambient temperature."——按 Tmra 留余量 <<<PAGE 28>>>
- **X14** 机架螺丝自备："insert a rack mount screw (not provided)"——ALE 不随机提供机架螺丝；DUO-MNT 并排安装需双人抬举 <<<PAGE 29>>>/<<<PAGE 34>>>
- **X15** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover plates should remain installed at empty module slots and power supply bays at all times."（拆电源不回装须盖盲板） <<<PAGE 43>>>/<<<PAGE 54>>>
## 电气与作业安全
- **X16** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 55>>>
- **X17** 运行中勿触背板："keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 56>>>
- **X18** 搬运前断全部电源："be sure to disconnect all power connections before servicing or moving the unit."（多电源设备逐路全断） <<<PAGE 56>>>
- **X20** DC 电源接地强制（EMC/EMI）："each DC/DC power supply requires that the ground wire is connected from each DC/DC power supply to Earth Ground." <<<PAGE 57>>>
- **X21** ESD 防护强制："Because electrostatic discharge (ESD) can damage switch components, you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components."（随机附防静电腕带） <<<PAGE 57>>>
- **X22** 锂电池更换须返厂："There is a danger of explosion if the lithium battery is incorrectly replaced. Replace only with the same or equivalent type recommended by the manufacturer... Return the module with the lithium battery to Alcatel-Lucent." <<<PAGE 58>>>
## 激光与场所限制
- **X23** Class 1M 激光警告："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS."（三机型面板同注） <<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 54>>>
- **X24** 空光口勿直视："Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected... install protective aperture covers to fiber ports with no cable connected." <<<PAGE 55>>>
- **X25** 受限场所安装："This equipment should be installed in a location that restricts access. A restricted access location is one where access is secure and limited to service personnel..."（DC 接线前提亦含 restricted access location） <<<PAGE 40>>>/<<<PAGE 57>>>
- **X26** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments."（Class A 数字设备，多国声明一致） <<<PAGE 53>>>/<<<PAGE 54>>>

---
合计：26 条（X1-X26）。

## frameworks

- **F1** 6570M 家族选型三轴矩阵：轴一=下行口形态（12/12D=8 铜口+2 SFP 混合，适合柜边小汇聚；U28=20 纯 SFP+4 combo 全光，适合光纤入柜）；轴二=供电制式（12=内置 AC 65W、12D=内置 DC 30W（18-75VDC 宽压，电池/直流场景）；轴三=上联与堆叠需求（12/12D=2 个 SFP+，U28=6 个 SFP+——堆叠带宽与上联密度按此定）。选型口诀：直流场景选 12D，全光密集选 U28，铜口小规模选 12；需要双机 1U 并排时用 12/12D+DUO-MNT 套件。 <<<PAGE 11>>>/<<<PAGE 22>>>/<<<PAGE 26>>>/<<<PAGE 35>>>
- **F2** 半宽空间利用框架：12/12D 半宽机（21.72cm）三态部署——单机桌面（橡胶脚垫正放）/单半宽入 19 英寸机架（RM-19-L L 支架）/双机并排占 1U（DUO-MNT slot+slide 支架+中央支架+盖板）；U28 全宽独占 1U 且上下各留 1RU。空间账：两台 12 并排=16 铜口+4 SFP+4 SFP+ 上联/堆叠口，仍省出机架深度（28cm vs U28 35cm）。 <<<PAGE 28>>>-<<<PAGE 34>>>/<<<PAGE 5>>>
- **F3** 高可用双支柱框架：供电侧=内置电源+外置备份电源（12/12D）或双 150W 舱冗余/负载分担（U28）+独立电路+多电源数秒内先后上电+Dying Gasp 三通道通告（SNMP trap 前 3 站/Syslog 前 3 服务器/4×802.3ah OAM PDU 上联口优先）；运行侧=温度双阈值固化（12/12D 85/88°C、U28 69/74°C：Warning 发 trap 不停机→Danger 关机待手动重启）+LED 三层（OK/VC/PS 系统、端口链路、电源六态）+show module/temperature 巡检。 <<<PAGE 12>>>/<<<PAGE 35>>>/<<<PAGE 46>>>/<<<PAGE 47>>>

---
合计：3 条（F1-F3）。

## glossary

- **OS6570M-12**：半宽定配置机，8×10/100/1000Base-T + 2×100/1000Base-X SFP + 2×SFP+ 上联/堆叠，内置 AC 电源+外部电源连接器，待机 23W <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 22>>>
- **OS6570M-12D**：12 的 DC 版（内置 DC 电源），待机 24W，存储温度 -40~85°C <<<PAGE 11>>>/<<<PAGE 23>>>/<<<PAGE 24>>>
- **OS6570M-U28**：全宽全光上联型，20×SFP + 4×SFP/RJ45 combo（21-24）+ 6×SFP+（25-30），双电源舱，待机 71W，独有 VC ID LED <<<PAGE 11>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **Uplink/Stacking SFP+ 口**：1G/10G 双角色口——上联与 Virtual Chassis 堆叠共用 <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 25>>>
- **combo 口**：同口位 SFP 光口与 RJ45 铜口二选一（U28 21-24） <<<PAGE 11>>>/<<<PAGE 25>>>
- **Availability Features**：可用性特性——防子系统失效丢流的软硬件保障（电源冗余/热插拔/硬件监控） <<<PAGE 11>>>/<<<PAGE 12>>>
- **Hot-Swapping**：热插拔——不断电、不中断其他组件地加/换硬件 <<<PAGE 12>>>

## 快速入门（Ch2）
- **Grounding wrist strap**：接地防静电腕带——安装三件套之一（另为 Phillips/Flat-blade 螺丝刀） <<<PAGE 13>>>
- **Redundant AC Power**：冗余交流供电——建议每 AC 插座独立电路，单路故障余电源存活 <<<PAGE 14>>>
- **Electrical Surge Warning**：电涌警告五条军规——接地/STP/浪涌保护器/室外雷电流/CDE 电缆放电，违者可能失保 <<<PAGE 14>>>
- **CDE（Cable Discharge Event）**：电缆静电放电事件——Cat5e/6/6a 介质储静电，接线前先将铜缆瞬时接地 <<<PAGE 14>>>
- **STP/UTP**：屏蔽/非屏蔽双绞线；室外或近交流导体场景建议 STP Cat5e 以上 <<<PAGE 14>>>
- **Console port**：控制台串口——默认 DCE 连接，首次登录必经 <<<PAGE 15>>>
- **Serial Default Settings**：串口默认参数——9600 波特/无校验/8 数据位/1 停止位 <<<PAGE 16>>>
- **EMP（Ethernet Management Port）**：带外管理以太网口——连交换机用直通线，连计算机用交叉线 <<<PAGE 16>>>
- **aaa authentication**：会话类型解锁命令（default/telnet/http/ftp local）——默认仅 console 可用 <<<PAGE 17>>>/<<<PAGE 18>>>
- **admin/switch**：出厂默认登录名/密码 <<<PAGE 17>>>
- **system timezone / system daylight-savings-time**：时区与夏令时配置命令（默认 UTC） <<<PAGE 18>>>
- **system contact / system name / system location**：管理联系人/系统名/物理位置可选参数命令 <<<PAGE 19>>>
- **show system / write memory**：查看配置/保存配置命令 <<<PAGE 19>>>

## 机箱与 LED（Ch3）
- **Tmra（Ambient Operating Temperature）**：环境工作温度 0-50°C——近似室温，通常低于内部温度 <<<PAGE 22>>>/<<<PAGE 28>>>
- **Warning Threshold（Thresh）**：内部温度警告阈值——12/12D 为 85°C、U28 为 69°C，超限发 trap 不停机 <<<PAGE 22>>>/<<<PAGE 26>>>/<<<PAGE 46>>>
- **Danger Threshold**：内部温度危险阈值——12/12D 为 88°C、U28 为 74°C，超限自动关机待手动重启 <<<PAGE 22>>>/<<<PAGE 26>>>/<<<PAGE 46>>>
- **OK LED**：系统诊断/AOS 启动灯——稳绿 OK/闪绿进行中/稳琥珀失败 <<<PAGE 27>>>
- **VC LED**：虚拟机箱角色灯——稳绿 master/稳琥珀 slave/闪琥珀（12 口机型）以次数报 unit 号/灭=关机或非 VC <<<PAGE 27>>>
- **Virtual Chassis ID LED**：VC 识别 LED——U28 前面板独有 <<<PAGE 25>>>
- **PS1/PS2 LED**：电源状态灯——U28 三态（绿正常/琥珀异常/灭不在位）；12 口机两态（绿/灭） <<<PAGE 27>>>
- **1/CMMA**：show temperature 输出中的机箱/设备传感器标识 <<<PAGE 45>>>
- **UNDER THRESHOLD**：show temperature 正常状态值 <<<PAGE 45>>>

## 安装套件（Ch3）
- **OS6570M-RM-19-L**：单半宽机 19 英寸机架安装套件（L 支架，长短臂可任意侧） <<<PAGE 30>>>
- **OS6570M-DUO-MNT**：双半宽机并排安装套件（slot 支架/slide 支架/前后中央支架/盖板与拇指螺丝） <<<PAGE 32>>>
- **Slot-bracket / Slide-bracket**：DUO-MNT 套件中分别固定两机与滑合连接的支架（M3 平头螺丝） <<<PAGE 32>>>
- **Rack mount screw (not provided)**：机架螺丝不随机提供，需用机架厂商螺丝 <<<PAGE 29>>>
- **Rubber table-mounting feet**：桌面安装橡胶脚垫 <<<PAGE 15>>>
- **Minimum Clearances**：最小间隙——12 口：上下各 1 英寸（有邻设备时）/侧 2 英寸；U28：上下各 1.75 英寸（1RU）/侧 2 英寸 <<<PAGE 28>>>

## 电源体系（Ch3）
- **Internal AC Power Supply（65W）**：12 机内置电源，100-240V/50-60Hz 输入，12V/5.42A 输出 <<<PAGE 35>>>
- **Internal DC Power Supply（30W）**：12D 机内置电源，36-72VDC 输入，12V/5.42A 输出 <<<PAGE 35>>>
- **OS6570-12-BP（PS-60W-AC，DA-60Z12）**：12 机外置备份电源，100-240VAC→12V/5A（60W） <<<PAGE 36>>>
- **OS6570-12-BP-D（PS-30W-DC，DDR-30L-12）**：12D 机外置备份电源，18-75VDC 宽压输入→12V/2.5A（30W），双态 LED <<<PAGE 37>>>
- **OS6570-BP（PS-150W-AC）**：U28 用 150W AC 电源，100-240VAC/3-1.5A→150W/12.5A，0.88kg，六态 LED <<<PAGE 38>>>
- **OS6570-BP-D（PS-150W-DC）**：U28 用 150W DC 电源，-36~-72VDC/1.8-6A→150W/12.5A，六态 LED <<<PAGE 39>>>
- **Lock Tab**：电源锁扣——插入至"click"锁定；拆卸按向中心后直拉 <<<PAGE 38>>>/<<<PAGE 41>>>/<<<PAGE 42>>>
- **Power Supply Tray**：电源托盘——AC/DC 通用，4+2+2 螺丝+扎带固定 <<<PAGE 44>>>
- **External Power Connector**：12/12D 后部外部电源连接器——接外置备份电源 <<<PAGE 11>>>/<<<PAGE 22>>>

## DC 接线与接地（Ch3）
- **DC Cable Harness**：DC 三芯线束——12AWG，绿黄=地/黑=return/红=-48VDC <<<PAGE 40>>>
- **-48VDC SELV**：安全特低电压直流源——DC 接线的可靠接地前提 <<<PAGE 40>>>
- **CBN（Common Bonding Network）**：共模连接网络——产品设计安装目标 <<<PAGE 40>>>
- **DC-1（Isolated DC Return）**：隔离直流回流——电池回流导体类型 <<<PAGE 40>>>
- **LCD8-10A-L**：Panduit UL 认证接地 lug——配 10-32 螺丝与 8AWG 铜线 <<<PAGE 40>>>/<<<PAGE 45>>>
- **Grounding Lug**：机箱接地耳——前/后面板，无漆区金属接触 <<<PAGE 22>>>/<<<PAGE 45>>>
- **Branch circuit overcurrent protection 15A**：支路过流保护额定 15A——DC 前提之一 <<<PAGE 40>>>

## 监控与 Dying Gasp（Ch3）
- **show module / show module long**：槽位基础/详细信息查看命令 <<<PAGE 45>>>
- **show temperature**：温度状态查看命令（Current/Range/Danger/Thresh/Status 五列） <<<PAGE 45>>>
- **Dying Gasp**：临终告警——整机失电时电容余量发三通道通告 <<<PAGE 46>>>
- **Dying Gasp Power Failure Event Occurred**：DG Syslog 消息原文（发前 3 个 Syslog 服务器） <<<PAGE 47>>>
- **efm-oam propagate-events dying-gasp**：在口上使能 DG 触发 802.3ah OAM PDU 的命令 <<<PAGE 47>>>
- **802.3ah OAM Information PDU**：链路 OAM 报文——DG 时发 4 个，Dying Gasp 位置位，上联口优先 <<<PAGE 47>>>
- **snmp station / swlog output socket**：配置 SNMP 站/Syslog 服务器以接收 DG 告警 <<<PAGE 46>>>/<<<PAGE 47>>>

## 法规与安全（附录 A）
- **CE Mark / DoC**：欧盟符合性声明（2014/30/EU EMC、2014/35/EU LVD、2011/65/EU RoHS 等） <<<PAGE 48>>>
- **WEEE**：废弃电子电气设备指令——EU 终端分类回收标志 <<<PAGE 48>>>
- **China/Taiwan RoHS**：有害物质表 <<<PAGE 49>>>/<<<PAGE 50>>>
- **California Proposition 65**：加州 65 号提案警告（含铅化合物） <<<PAGE 50>>>
- **Class A**：A 级数字设备——Class A 住宅环境禁用警告（FCC/VCCI/BSMI/Korea 多版本） <<<PAGE 52>>>/<<<PAGE 53>>>/<<<PAGE 54>>>
- **Class 1M Laser**：1M 级激光——开盖时勿用光学仪器直视 <<<PAGE 21>>>/<<<PAGE 54>>>
- **Hi-Pot Test**：耐压测试——IEEE 802.3，全部以太网口 2250V DC <<<PAGE 52>>>
- **Restricted Access Location**：受限访问场所——仅持钥匙/权限的服务人员可达 <<<PAGE 57>>>
- **ESD（Electrostatic Discharge）**：静电放电——操作组件前须消除人体与环境静电 <<<PAGE 57>>>
- **Lithium Battery Warning**：锂电池警告——错换有爆炸风险，须返厂 ALE 更换 <<<PAGE 58>>>
- **GR-63-CORE**：电信设备环境耐用性标准 <<<PAGE 52>>>

## principles

## 家族与端口架构
- **P1** 家族三机型：OS6570M-12（8×10/100/1000Base-T + 2×100/1000Base-X SFP + 2×Uplink/Stacking SFP+ 1G/10G + 内置 AC + 外部电源连接器）；OS6570M-12D（同端口、内置 DC）；OS6570M-U28（20×100/1000Base-X SFP + 4×SFP/RJ45 combo + 6×Uplink/Stacking SFP+ + 双电源舱）——"Fixed-configuration chassis" <<<PAGE 11>>>
- **P2** Uplink/Stacking 双角色口：SFP+ 口标注"Uplink/Stacking SFP+ Ports (1G/10G)"——同一对/组口既做上联又做 Virtual Chassis 堆叠链路（12 口机 11-12，U28 机 25-30 共 6 个） <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 25>>>
- **P3** combo 口机制：U28 的 21-24 口为"100/1000Base-X SFP or 10/100/1000Base-T RJ45 combo ports"——一口两位（光/铜），同口位光铜互斥 <<<PAGE 11>>>/<<<PAGE 25>>>
- **P5** 半宽/全宽双包络：12/12D=21.72cm 宽×28.07cm 深×1.7kg（半宽）；U28=44cm 宽×35cm 深×4.08kg（不含电源，全宽 19 英寸）——半宽机可两台并排占 1U <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P6** 待机功耗梯度：12=23W、12D=24W、U28=71W——光口密度推高基线功耗 <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
## 可用性体系
- **P7** 可用性三特性定义：Power Supply Redundancy（多电源冗余/负载分担）、Hot-Swapping（不断电加/换件）、Hardware Monitoring（"the switch immediately sends a trap to the user"）<<<PAGE 12>>>
## 温度机制
- **P9** 温度阈值按机型分化：12/12D 内部 Warning 85°C / Danger 88°C；U28 Warning 69°C / Danger 74°C——光口机热预算更紧，阈值低 16°C <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P10** Tmra 统一 0-50°C；存储温度分化：12=-20~60°C、12D/U28=-40~85°C；湿度一律 5-95% 非凝结 <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P11** 内部温度 vs Tmra 语义："Internal temperature refers to the sensor reading... Ambient temperature (Tmra) refers to the approximate room temperature. The ambient temperature will typically be lower." <<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>
- **P12** 温度双阈值行为：Warning 超限发 trap 且"switch operations remain active"（处置=查气流遮挡/室温）；Danger 超限"the switch will power off until...manually booted"——阈值出厂固化不可改 <<<PAGE 45>>>/<<<PAGE 46>>>
- **P13** show temperature 输出结构：Chassis/Device（1/CMMA）｜Current｜Range（15 to 85）｜Danger（88）｜Thresh（85）｜Status（UNDER THRESHOLD） <<<PAGE 45>>>
## 电源体系
- **P14** 双层电源架构（12/12D）：内置电源（12=AC 65W、12=DC 30W，均 12V/5.42A 输出）+ External Power Connector 外部电源连接器（可插 OS6570-12-BP 60W AC 或 OS6570-12-BP-D 30W DC 备份） <<<PAGE 11>>>/<<<PAGE 35>>>
- **P15** 外置备份电源对：OS6570-12-BP（DA-60Z12，100-240VAC→12V/5A 60W）配 12；OS6570-12-BP-D（DDR-30L-12，18-75VDC 宽压输入→12V/2.5A 30W）配 12D——AC/DC 各随其主机型 <<<PAGE 35>>>/<<<PAGE 36>>>/<<<PAGE 37>>>
- **P16** 12D 外置 DC 宽压输入：18-75VDC（Tolerances Included）——比 U28 的 150W DC（-36~-72VDC）范围更宽，适配电池直挂场景 <<<PAGE 37>>>/<<<PAGE 39>>>
- **P17** 30W DC 双态 LED：Solid Green=DC power is good；Solid Red=There is a DC power issue <<<PAGE 37>>>
- **P18** U28 双 150W 电源：OS6570-BP（PS-150W-AC，100-240VAC/3-1.5A→150W/12.5A，0.88kg）与 OS6570-BP-D（PS-150W-DC，-36~-72VDC/1.8-6A→150W/12.5A）——双舱可冗余/负载分担 <<<PAGE 35>>>/<<<PAGE 38>>>/<<<PAGE 39>>>
- **P19** 150W 电源六态 LED 语义：稳绿=供电正常；闪绿=待机可接管（"power supply is on standby"）；闪红=本电源无 AC 但邻舱有电；闪绿红=告警；稳红=故障；灭=全机无任何电源输入 <<<PAGE 38>>>/<<<PAGE 39>>>
- **P20** 无电源开关语义："The chassis does not provide an on/off switch. Connecting a the power supplies to a power source will boot the switch." <<<PAGE 42>>>
- **P21** 电源热插拔锁扣机制：插入滑至背板"the lock tab will click and hold"；拆卸按锁扣向中心（"Pressing the lock tab toward the center of the power supply"）后直拉 <<<PAGE 41>>>/<<<PAGE 42>>>/<<<PAGE 43>>>
- **P22** 电源托盘通用化："The same power supply tray is used for both AC and DC power supplies"——4 螺丝固定托盘+2 螺丝支架+2 螺丝盖板+附赠扎带理线 <<<PAGE 44>>>
- **P23** DC 供电五条安全前提：可靠接地 -48VDC SELV 源、支路过流保护 15A、12AWG 铜导线、易达断路装置、受限场所安装 <<<PAGE 40>>>
- **P24** DC 三芯极性约定：Green/yellow=ground、Black=return、Red=-48VDC；"The battery return conductor is an Isolated DC Return (DC-1)"；产品按 CBN（Common Bonding Network）设计 <<<PAGE 40>>>
- **P25** 机箱 supplemental 接地：前/后接地耳用 10-32 螺丝+无漆区金属接触；Panduit LCD8-10A-L lug + 8AWG 铜线；后板双接地孔同样规格——补充而非替代电源线接地 <<<PAGE 40>>>/<<<PAGE 45>>>
## LED 与面板机制
- **P26** 四组状态 LED：OK 三态（稳绿=诊断与 AOS 启动 OK/闪绿=进行中/稳琥珀=启动失败）；VC 四态（稳绿=master/稳琥珀=slave/闪琥珀=12 口机型以闪烁次数报 unit 号/灭=关机或不在 VC）；PS1/PS2 按机型两套语义（U28 三态含琥珀故障；12 口机仅绿=正常/灭=不在位）<<<PAGE 27>>>
- **P27** 端口 LED 全绿色系：千兆/SFP/SFP+ 口均稳绿=有效链路、闪绿=链路活动——无 PoE 琥珀色维度（本家族无 PoE） <<<PAGE 27>>>
## Dying Gasp 机制
- **P28** DG 三通道：整机失电时发 SNMP trap（前 3 个已配 SNMP 站，含槽号/主备电源类型/失效时间）+ Syslog"Dying Gasp Power Failure Event Occurred"（前 3 服务器）+ 4 个 802.3ah OAM Information PDU（Dying Gasp 位置位，发往 link OAM 使能且 operational 的口）<<<PAGE 46>>>/<<<PAGE 47>>>
- **P29** DG PDU 优先级："Dying gasp packets will be sent in the following order based on port priority: 1. Uplink ports 2. All other ports"——电容余量优先保上联通告 <<<PAGE 47>>>
- **P30** DG 触发三场景：唯一电源失效；主后备先后失效；后备主先后失效——"Connect each power supply to a separate independent power source to avoid simultaneous power failures." <<<PAGE 46>>>
## 安装机制
- **P31** 机架安装五项通则：Tmra（密闭多机架环温高于室温）、Reduced Air Flow、Mechanical Loading（防不均衡装载）、Circuit Overloading（过载对过流保护影响）、Reliable Earthing（尤其经电源排接线时）<<<PAGE 28>>>
- **P32** 间隙按机型分化：12 口机上下各 1 英寸（仅当有邻设备；无邻设备 N/A）+ 侧 2 英寸；U28 上下各 1.75 英寸（1RU）+ 侧 2 英寸；前后均 N/A <<<PAGE 28>>>
- **P33** 三套机架方案：全宽法兰（U28）；单半宽 OS6570M-RM-19-L（L 支架长短任意侧）；双半宽 OS6570M-DUO-MNT（slot/slide 支架+前后中央支架+盖板拇指螺丝，两台半宽并排成 19 英寸）<<<PAGE 29>>>/<<<PAGE 30>>>/<<<PAGE 32>>>
- **P34** 先下孔后上孔紧固纪律："insert a rack mount screw (not provided) through the bottom hole of each bracket. Tighten both screws until they are secure"——先承重后定位，三套方案一致 <<<PAGE 29>>>/<<<PAGE 34>>>
- **P35** EMP 线缆规则：EMP to a Switch=Straight-through；EMP to a Computer or Workstation=Crossover——带外管理口线序按对端设备类型选 <<<PAGE 16>>>
- **P36** 多电源上电时序："plug in each power supply in rapid succession, (i.e., within a few seconds of each other)"——保证启动全程供电充足 <<<PAGE 16>>>

---
合计：36 条（P1-P36）。
