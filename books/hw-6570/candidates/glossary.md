# glossary — 术语表（OmniSwitch 6570M Hardware Users Guide）

格式：`- **术语**：中文解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 机型家族（Ch1）

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
