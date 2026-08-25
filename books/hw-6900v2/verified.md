# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

- **C1** 开箱清单：机箱（含按订单电源）、盲板、机架托架、国别电源线、橡胶桌脚、附赠螺丝与防静电袋；尽量靠近安装位开箱；空箱最重 7.78kg、满配可达 10.86kg（不含光模块/线缆）<<<PAGE 16>>>
- **C2** 上电流程：全部电源线插入易触及接地插座（禁延长线）→ 自动上电；多电源纪律——"be sure to plug in each power supply in rapid succession, (i.e., within a few seconds of each other)" <<<PAGE 20>>>
- **C3** 首次登录七步（比接入交换机多一步 EMP 设 IP）：console 登录（admin/switch）→ 设 EMP IP 地址 → 解锁会话类型 → 改密码 → 设时区 → 设日期时间 → 设可选项并 `write memory` <<<PAGE 21>>>
- **C4** EMP 设 IP：先 console 连接 → `ip interface emp address 168.22.2.120 mask 255.255.255.0` → `show ip interface` 验证；默认 192.168.1.1/24 <<<PAGE 22>>>
- **C5** 解锁会话类型：全部 `aaa authentication default local`；单个 `aaa authentication telnet local` / `aaa authentication http local`；一条命令一个类型，多条连用 <<<PAGE 23>>>
- **C6** 改密码四步：admin 登录 → `password` 回车 → 输新密码 → 再输一次；实时保存、重启保留 <<<PAGE 23>>>/<<<PAGE 24>>>
- **C7** 时间与可选项：`system timezone`/`system daylight-savings-time`（默认 UTC）；`system time hh:mm:ss`/`system date mm/dd/yyyy`；`system contact`/`system name`/`system location`；`show system` 查看；`write memory` 保存 <<<PAGE 24>>>/<<<PAGE 25>>>
## 机架与独立安装
- **C8** 机架安装八步（双人+后支撑）：①预标记孔位 ②左右侧装 slot rails ③一人抬起法兰贴平机架立柱 ④孔位对齐 ⑤第二人先装每侧底部螺丝拧紧 ⑥机箱后方把滑入式支撑（slide-in braces）插入 slot rails 直抵机架立柱 ⑦校水平并使支撑法兰对准机架前孔 ⑧四法兰装齐全部螺丝拧紧 <<<PAGE 54>>>/<<<PAGE 55>>>
- **C9** 中装（Mid-Mount）流程：①拆前法兰与侧 slot rails ②法兰装到机箱中部螺纹孔 ③预标记机架孔 ④抬起使中装法兰贴平立柱 ⑤对孔 ⑥第二人装底部螺丝 ⑦装齐剩余螺丝 <<<PAGE 56>>>/<<<PAGE 57>>>
- **C10** 独立桌面安装：稳固平面承满配重量；保证气流间隙与 AC 插座可达；机箱必须正放 <<<PAGE 58>>>
## 电源安装与更换（热插拔）
- **C11** 装电源三步：①电源插座朝右、手柄竖直方向滑入 ②后滑至 securely seated 接背板——"the lock tab will click and hold the power supply in place" ③电源线插入电源插座（接电即开机）<<<PAGE 67>>>/<<<PAGE 68>>>
- **C12** 拆电源：先从电源源断线并拔出电源线 → 按锁片释放 → 按住锁片直向后拉出；不回装时空槽装盲板 <<<PAGE 69>>>
- **C13** DC 线缆连接（V/X 系）：连接器插入电源接口至"clicks firmly into place"；另一端三根 12AWG 线（绿黄=地/黑=return/红=-48VDC）接熔丝面板或 -48V 源 <<<PAGE 66>>>
- **C14** OS6920 DC 环形端子：电源不附带线缆，按规格自制——电源端子 8AWG（孔径 4.3mm 等 9 项尺寸）、接地端子 6AWG（孔径 6.4mm 等），接电源的 power 与 ground 端子 <<<PAGE 67>>>
- **C15** 机箱接地：后部 paint-free 双螺纹孔装 Panduit LCD8-10A-L lug + 10-32 3/8" 螺丝 + 8AWG 铜导线，扭矩 30-60 in-lb <<<PAGE 73>>>
## 风扇托盘更换（热插拔）
- **C16** 风扇托盘更换四步（限时 60 秒内完成）：①松开 captive 螺丝 ②直拉出托盘 ③新托盘直插至背板连接器 ④左右两侧 captive 螺丝拧紧；全程防止过热 <<<PAGE 72>>>
## 监控
- **C17** 硬件监控四命令：`show module` / `show module long` / `show temperature`（Warning/Danger 阈值与状态）/ `show fan`（风扇托盘状态）<<<PAGE 74>>>/<<<PAGE 75>>>
- **C18** 温度告警处置：Warning→查气流阻塞/室温/`show fan` 风扇状态；Danger→查气流阻塞或方向失配/室温/风扇，处理后手动开机 <<<PAGE 75>>>
- **C19** LOC 定位用法：LOC LED 闪琥珀表示远程管理已激活用于识别该设备（机柜中定位单台交换机）<<<PAGE 48>>>

## counter-examples

## 气流与端口限制（本书特有重点）
- **X1** 气流方向必须一致："The airflow direction of the power supplies and fan tray must be the same."（电源与风扇托盘方向不同即失配）<<<PAGE 50>>>
- **X2** 气流失配循环重启："Eventually the mismatched configuration will cause the chassis to reboot to avoid overheating."（启动时失配=OK/PS 绿琥珀交替闪+持续重启；运行中热插失配件=OK/PS 闪琥珀+到 Danger 阈值重启）<<<PAGE 50>>>/<<<PAGE 52>>>
- **X3** 端口组速率不可混（V72）："The OS6900-V72 doesn't support a mix of 10G and 25G speeds on the 4-port groups of ports 1-48."（12 个 4 口组内必须同为 10G 或 25G）<<<PAGE 28>>>
- **X4** 端口组速率不可混（X48C4E/V48C8）："Ports within a port group must all run at either 1G/10G speed or 25G speed. Mixing 1G and 10G speeds is supported."（V48C8 端口组编号非连续，规划前必查分组表）<<<PAGE 38>>>/<<<PAGE 40>>>
- **X5** DAC 与 QSFP 混插禁令（T48C6/X48C6）："Mixing Direct-attached cables (DAC) and QSFPs is not supported on ports 52 and 53. If both ports are populated they must be of the same type." <<<PAGE 34>>>/<<<PAGE 36>>>
- **X6** OS6920 后→前气流温度降额：后→前气流 Tmra 仅 0-35°C（前→后为 0-45°C）："The installation site must maintain a temperature between 0° and 35° Celsius... for the OmniSwitch 6920 with back-to-front airflow." <<<PAGE 14>>>/<<<PAGE 47>>>
- **X7** 气流阻塞后果："Restricted airflow can cause your switch to overheat, which can lead to switch failure." / "Never obstruct chassis air vents." <<<PAGE 17>>>/<<<PAGE 50>>>
## 电源限制
- **X8** 两代电源不可混："Do not mix OS6900-V72/C32/C32E/X48C4E/V48C8 power supplies with OS6900-T48C6/X48C6/T24C2/X24C2 power supplies."（650W 系与 400W 系外观相近但互不兼容）<<<PAGE 60>>>-<<<PAGE 65>>>
- **X9** AC+DC 混插允许（正面对照）："Mixing an AC and DC power supply in the same chassis is supported." <<<PAGE 60>>>等
- **X10** 拆电源先断源："When removing a power supply, first disconnect the power cord from the power source." <<<PAGE 69>>>
- **X11** 无电源开关语义：接电即开机、断全部电源线即关机 <<<PAGE 59>>>
- **X12** OS6920 AC 低压输入降额：100-127V 时 12V 输出仅 83.33A（220-240V 为 125A）；且 "The system hold time for this power supply at 100% load is less than 20ms." <<<PAGE 64>>>
- **X13** DC 过流与线规（OS6920）："The branch circuit overcurrent protection must be rated 50A. Use 6AWG copper conductors."（远大于 V/X 系 12AWG）<<<PAGE 66>>>
- **X14** DC 源必须在受限场所："The power source must be installed in a restricted access location." <<<PAGE 66>>>
- **X15** DC 地线 EMC 强制："For EMC/EMI, each DC/DC power supply requires that the ground wire is connected from each DC/DC power supply to Earth Ground." <<<PAGE 87>>>
- **X16** IEC 60945 场景专用线缆：X48C6+OS6900X-BPD-F 需 IEC 60945 认证时必须用 OS-DNV-DC-PWR 线缆（双磁环）<<<PAGE 63>>>
- **X17** 禁用延长线："each supplied AC power cord is 2 meters (approx. 6.5 feet). Do not use extension cords." <<<PAGE 15>>>/<<<PAGE 20>>>
- **X18** 多电源快速上电："be sure to plug in each power supply in rapid succession, (i.e., within a few seconds of each other)." <<<PAGE 20>>>
- **X19** 电涌违规范即失保："Failure to follow the above recommendations could result in voiding the warranty of the affected ALE product." <<<PAGE 16>>>
- **X20** CDE 静电放电风险："Category 5e, Category 6, and Category 6a cables can store large amounts of static electricity... could lead to a Cable Discharge Event (CDE)." <<<PAGE 15>>>/<<<PAGE 16>>>
## 风扇与安装限制
- **X21** 风扇托盘必装："The fan tray is a required component. Never attempt to operate the switch without a fan tray installed." <<<PAGE 70>>>
- **X22** 60 秒更换窗口："The switch should not run without a fan tray more than 60 seconds to prevent over heating." <<<PAGE 72>>>
- **X23** 风扇型号不可乱装："Do not attempt to install incompatible fan models in a chassis."（风扇分 F/R 气流方向且随机型专用）<<<PAGE 71>>>
- **X24** 仅前法兰安装禁令："Never rack mount OS6900 switches using only the front-installed rack mount flanges. Due to the chassis overall depth, OS6900 switches must be mounted using additional support braces (available from Alcatel-Lucent) or by attaching flanges to the mid portion of the chassis... Failure to properly mount the switch may result in the chassis sagging in the rack or damage to the switch and its components." <<<PAGE 55>>>/<<<PAGE 56>>>
- **X25** 后支撑强制："Because of the overall chassis depth, additional support braces are used to support the rear of the chassis and prevent sagging in the rack. These braces are required for all rack-mount installations." <<<PAGE 54>>>
- **X26** 禁止倒放/侧放："Chassis must be placed 'right side up.' Never attempt to operate a switch while it is placed on its top or side." <<<PAGE 58>>>
- **X27** 盲板必须常装："Because they regulate airflow and help protect internal chassis components, blank cover panels should be installed over empty module slots and power supply bays at all times." <<<PAGE 53>>>/<<<PAGE 85>>>
- **X28** 机架螺丝自备："Alcatel-Lucent does not provide rack-mount screws. Use the screws supplied by the rack vendor."；双人机架纪律 <<<PAGE 54>>>
- **X29** 专业安装者要求："Alcatel-Lucent switches must be installed by a professional installer." <<<PAGE 14>>>
## 功能未启用与设备限制
- **X30** 预留口未激活（C32E/V48C8/OS6920）："SFP+ ports (Ports 33-34 - 1G/10G) - Not currently functional"（同型还有 V48C8 57-58 口、OS6920 33 口）——规划时不可当可用口 <<<PAGE 32>>>/<<<PAGE 40>>>/<<<PAGE 46>>>
- **X31** 双 EMP 口仅一个可用（T48C6/X48C6）："Only top port is functional." <<<PAGE 34>>>/<<<PAGE 36>>>
- **X32** EMP 远程访问前置条件："Although you have configured the EMP with valid IP address information, you will not be able to access the switch through this port (i.e. TELNET, FTP, HTTP, SSH or SNMP) until you have unlocked these remote session types." <<<PAGE 22>>>
## 温度与人身安全
- **X33** Danger 阈值不可配置："The danger threshold is factory-set and cannot be configured by the user."（超限自动关机须手动启动）<<<PAGE 75>>>
- **X34** 运行中勿触电源槽/背板："To reduce the risk of electrical shock, keep your hands and fingers out of power supply bays and do not touch the backplane while the switch is operating." <<<PAGE 86>>>
- **X35** 多电源检修全断电："Your switch is equipped with multiple power supplies. To reduce the risk of electrical shock, be sure to disconnect all power connections before servicing or moving the unit."（西语版：可能有三根电源线）<<<PAGE 86>>>/<<<PAGE 90>>>
- **X36** 雷暴作业禁令："To avoid a shock hazard, do not connect or disconnect any cables or perform installation, maintenance, or reconfiguration of this product during an electrical storm." <<<PAGE 85>>>
- **X37** Class 1M 激光警告："CLASS 1M LASER RADIATION WHEN OPEN. DO NOT VIEW DIRECTLY WITH OPTICAL INSTRUMENTS." <<<PAGE 84>>>
- **X38** 不可见激光辐射："Lasers emit invisible radiation from the aperture opening when no fiber-optic cable is connected. When removing cables do not stare into the open apertures."（空口装保护盖）<<<PAGE 86>>>
- **X39** 锂电池规格与处置：CR1220 型（适用 X48C6/T48C6/X48C4E/V48C8）；"There is danger of explosion if the Lithium battery in your chassis is incorrectly replaced."；UN3091 分类不得入生活垃圾 <<<PAGE 80>>>/<<<PAGE 81>>>
- **X40** 室外裸线禁令："Never install exposed network cables outdoors." <<<PAGE 18>>>/<<<PAGE 85>>>
- **X41** Class A 住宅禁用："To avoid electromagnetic interference, this product should not be installed or used in residential environments."（台湾 BSMI 版；另有 FCC/CISPR22/VCCI/Korea 同义条款）<<<PAGE 84>>>
- **X42** FCC 擅改失权："Changes and modifications made to the equipment without approval of the manufacturer could void the user's authority to operate this equipment." <<<PAGE 83>>>
- **X43** 接地 lug 规范强制：Panduit LCD8-10A-L + 10-32 3/8" 螺丝 + 8AWG，扭矩 30-60 in-lb <<<PAGE 66>>>/<<<PAGE 73>>>
- **X44** 密码丢失后果："Be sure to remember or securely record all new passwords; overriding configured passwords on an OmniSwitch is restricted." <<<PAGE 23>>>
- **X45** ESD 纪律："you must follow proper procedures to eliminate ESD from your person and the surrounding area before handling switch components." <<<PAGE 88>>>
- **X46** 受限场所要求："This equipment should be installed in a location that restricts access." <<<PAGE 88>>>

## frameworks

- **F1** 6900 十机型选型矩阵（介质 × 下行密度 × 上行）：
  | 机型 | 下行 | 上行 | 深度 | 定位 |
  |---|---|---|---|---|
  | OS6900-T24C2 | 24×10GBaseT | 2×SFP+ +2×QSFP28 | 47.3cm | 铜口入门 |
  | OS6900-X24C2 | 24×SFP+ | 2×SFP+ +2×QSFP28 | 47.3cm | 光口入门 |
  | OS6900-T48C6 | 48×10GBaseT | 6×QSFP28 | 47.3cm | 铜口汇聚 |
  | OS6900-X48C6 | 48×SFP+ | 6×QSFP28 | 47.3cm | 10G 光汇聚 |
  | OS6900-X48C4E | 40×SFP+ +8×SFP28 | 4+2×QSFP28 | 51.5cm | 10G/25G 混合 |
  | OS6900-V48C8 | 48×SFP28 | 8×QSFP28+2×SFP+ | 53.6cm | 25G 高密 |
  | OS6900-V72 | 48×SFP28 | 6×QSFP28 | 51.5cm | 25G+100G |
  | OS6900-C32 | 32×QSFP28 | — | 51.5cm | 100G 汇聚 |
  | OS6900-C32E | 32×QSFP28 | 2×SFP+(未启用) | 51.5cm | 100G+管理辅助 |
  | OS6920-D32 | 32×QSFP-DD | 1×SFP+(未启用) | 59cm | 400G 核心/超融合 |
  决策三问：铜还是光（T/X）；25G/100G/400G 档位；机架深度是否容纳 51.5-59cm 深机箱 <<<PAGE 12>>>/<<<PAGE 28>>>-<<<PAGE 47>>>
- **F2** 气流方向"三件套一致性"框架（6900 部署第一课）：
  ① 定方向：机房冷热通道决定前→后（F 后缀）或后→前（R 后缀；部件紫色标识）② 三件套对齐：风扇托盘 + 电源1 + 电源2 必须同方向（F/R 后缀逐一核对）③ 失配后果链：trap 告警 → 启动时失配=循环重启；运行中失配=达 Danger 温度阈值重启 ④ 温度联动：OS6920 后→前气流 Tmra 降额至 35°C，机柜规划按 35°C 校验 <<<PAGE 50>>>/<<<PAGE 52>>>/<<<PAGE 14>>>/<<<PAGE 47>>>
- **F3** 深机箱机架安装三方案决策树：
  ① 标准机架且可触及机箱后方 → 前法兰+滑入式后支撑（slot rails + slide-in braces，全部安装必用后支撑）② 深度受限/开放式机架 → 中装法兰（mid-mount，用机箱中部螺纹孔）③ 禁止方案：仅前法兰（机箱下垂/损坏风险，官方明令 Never）<<<PAGE 54>>>-<<<PAGE 57>>>
- **F4** 电源体系两阵营对照框架（选型/备件防错）：
  | 维度 | V 系（V72/C32/C32E/X48C4E/V48C8） | X 系（T48C6/X48C6/T24C2/X24C2） | OS6920 系 |
  |---|---|---|---|
  | AC 电源 | OS6900C-BP-F/R 650W | OS6900X-BP-F/R 400W | OS6920-BP-F/R 1500W |
  | DC 电源 | OS6900C-BPD-F/R 650W（36-72V） | OS6900X-BPD-F/R 200/400W（-20~-75V） | OS6920-BPD-F/R 1600W（-40~-75V/50A/6AWG） |
  | 跨阵营混插 | 禁止 | 禁止 | 禁止 |
  | AC+DC 混插 | 允许 | 允许 | 允许 |
  通用规则：F/R 后缀对应气流方向；1+1 冗余第二电源为 standby；接电即开机 <<<PAGE 59>>>-<<<PAGE 65>>>/<<<PAGE 12>>>

## glossary

- **OS6900-V72**：48×SFP28(10/25G)+6×QSFP28 机型，深度 51.5cm，188/400W <<<PAGE 12>>>/<<<PAGE 28>>>/<<<PAGE 29>>>
- **OS6900-C32**：32×QSFP28(100G) 机型，145/543W <<<PAGE 12>>>/<<<PAGE 30>>>/<<<PAGE 31>>>
- **OS6900-C32E**：32×QSFP28+2×SFP+（33/34 口 Not currently functional），175/510W <<<PAGE 12>>>/<<<PAGE 32>>>等
- **OS6900-T48C6**：48×1G/10GBaseT+6×QSFP28 机型；52/53 口 DAC 与 QSFP 不可混插 <<<PAGE 12>>>/<<<PAGE 34>>>等
- **OS6900-X48C6**：48×SFP+ +6×QSFP28 机型，114/392W <<<PAGE 12>>>/<<<PAGE 36>>>等
- **OS6900-X48C4E**：40×SFP+ +8×SFP28+6×QSFP28 机型，端口组 41-48 分 2 组锁速 <<<PAGE 12>>>/<<<PAGE 38>>>等
- **OS6900-V48C8**：48×SFP28+8×QSFP28+2×SFP+（57/58 未启用），226/532W，端口组编号非连续 <<<PAGE 12>>>/<<<PAGE 40>>>等
- **OS6900-T24C2**：24×10GBaseT+2×SFP+ +2×QSFP28 机型，91/209W <<<PAGE 12>>>/<<<PAGE 42>>>等
- **OS6900-X24C2**：24×SFP+ +2×SFP+ +2×QSFP28 机型，75/197W <<<PAGE 12>>>/<<<PAGE 44>>>等
- **OS6920-D32**：32×QSFP-DD(400G)+1×SFP+（未启用）机型，深 59cm，最高 1400W；后→前气流限 35°C <<<PAGE 12>>>/<<<PAGE 46>>>/<<<PAGE 47>>>
- **ToR（Top-of-Rack）**：数据中心机柜顶交换机部署模式，6900 家族第二定位 <<<PAGE 12>>>
- **QSFP-DD**：400G 双密度四通道光模块接口（支持 400G/2X200G/4X100G，向下兼容 QSFP56/28/+）<<<PAGE 46>>>
- **QSFP28**：100G 光模块口（4X10G/40G/4X25G/100G）<<<PAGE 28>>>等
- **SFP28**：25G 光模块口（1G/10G/25G）<<<PAGE 28>>>等
- **端口组（Port Group）**：4 口一组的速率锁定单元（V72/X48C4E/V48C8），组内 10G 与 25G 不可混 <<<PAGE 28>>>/<<<PAGE 38>>>/<<<PAGE 40>>>
- **Splitter 功能**：T48C6/X48C6 的 51/54 口支持分支（一拆四）功能 <<<PAGE 34>>>/<<<PAGE 36>>>
- **DAC（Direct-attached Cable）**：直连铜缆；T48C6/X48C6 52/53 口与 QSFP 光模块不可混插 <<<PAGE 34>>>等

## 电源（Ch3）
- **OS6900C-BP-F / -R**：650W AC 电源（12V/52.9A），V 系机型用，F=前→后/R=后→前 <<<PAGE 60>>>
- **OS6900X-BP-F / -R**：400W AC 电源（12V/33.34A），X 系机型用 <<<PAGE 61>>>
- **OS6900C-BPD-F / -R**：650W DC 电源（36-72VDC 输入），V 系用 <<<PAGE 62>>>
- **OS6900X-BPD-F / -R**：200/400W DC 电源（-20~-75VDC 两档输出），X 系用 <<<PAGE 63>>>
- **OS6920-BP-F / -R**：1500W AC 电源（100-127V/12A 或 220-240V/8A；hold time <20ms）<<<PAGE 64>>>
- **OS6920-BPD-F / -R**：1600W DC 电源（-40~-75V/50A，12V/133.33A），DC 端子+接地端子 <<<PAGE 65>>>
- **1+1 冗余（1+1 Redundant）**：双电源热插拔冗余，第二电源为 standby 角色 <<<PAGE 12>>>/<<<PAGE 59>>>
- **Lock Tab（锁片）**：电源就位"咔哒"锁定/按压释放机构 <<<PAGE 67>>>等
- **5VSB**：电源待机输出（5V standby）<<<PAGE 60>>>等
- **OS-DNV-DC-PWR**：IEC 60945 认证 DC 线缆（双磁环），X48C6+BPD-F 船用认证场景必备 <<<PAGE 63>>>
- **环形端子（Ring Terminal）**：OS6920 DC 电源接线端子（电源 8AWG/接地 6AWG，规格九项尺寸）<<<PAGE 67>>>
- **CBN / Isolated DC Return（DC-I）**：共同联结网络 / 隔离式 DC 回流 <<<PAGE 66>>>

## 风扇与气流（Ch3）
- **风扇托盘（Fan Tray）**：机箱后部 5/6 个独立热插拔风扇模块，主温控部件 <<<PAGE 28>>>等/<<<PAGE 70>>>
- **OS6900V-FT-F/R**：V72/C32/C32E/X48C4E 风扇托盘（F/R=气流方向）<<<PAGE 70>>>
- **OS6900-T48C6/X48C6-FT-F/R**：T/X 系风扇托盘（拇指螺丝在右上）<<<PAGE 70>>>
- **OS6900-V48C8-FT-F/R / OS6920-FT-F/R**：V48C8 / OS6920 专用风扇托盘 <<<PAGE 70>>>/<<<PAGE 71>>>
- **前→后气流（Front-to-Rear）**：顶部前进风、后部排风；部件标准色 <<<PAGE 51>>>/<<<PAGE 52>>>
- **后→前气流（Rear-to-Front）**：后部进风、前顶排风；部件紫色标识 <<<PAGE 51>>>/<<<PAGE 52>>>
- **气流失配（Airflow Mismatch）**：电源与风扇方向不一致引发的告警-重启机制 <<<PAGE 50>>>/<<<PAGE 52>>>
- **紫色编码（Purple Color Coding）**：后→前部件的防差错颜色标识 <<<PAGE 52>>>
- **滑入式支撑（Slide-in Braces）**：深机箱机架安装的强制后支撑件 <<<PAGE 54>>>/<<<PAGE 55>>>
- **中装法兰（Mid-Mount Flanges）**：装于机箱中部螺纹孔的替代安装方式 <<<PAGE 56>>>

## LED 与监控（Ch3）
- **PS1/PS2 LED**：绿=正常、琥珀=错误、灭=不在位 <<<PAGE 48>>>
- **Diag LED**：绿=正常、琥珀=自检故障 <<<PAGE 48>>>
- **Fan LED**：绿=正常、琥珀=错误（任一风扇意外停转即转琥珀并发 trap）<<<PAGE 48>>>/<<<PAGE 75>>>
- **LOC LED**：闪琥珀=远程定位激活 <<<PAGE 48>>>
- **QSFP-DD LED 色表**：青=400G、紫=200G、蓝=100G、橙=40G、红=端口故障等 12 态 <<<PAGE 48>>>
- **show module / show module long**：槽位基本/详细信息命令 <<<PAGE 74>>>
- **show temperature**：温度与 Warning/Danger 阈值状态命令 <<<PAGE 74>>>
- **show fan**：风扇托盘状态命令 <<<PAGE 75>>>
- **Warning 阈值**：可查/可配温度告警阈值，超限发 trap 业务继续 <<<PAGE 75>>>
- **Danger 阈值**：出厂固化，超限自动关机须手动启动 <<<PAGE 75>>>

## 管理口与登录（Ch2/Ch3）
- **EMP（Ethernet Management Port）**：RJ45 10/100/1000 带外管理口；默认 192.168.1.1/24 <<<PAGE 12>>>/<<<PAGE 18>>>/<<<PAGE 22>>>
- **EMP 线缆规则**：接交换机用直通线、接计算机用交叉线 <<<PAGE 18>>>
- **ip interface emp**：改 EMP IP 地址命令 <<<PAGE 22>>>
- **admin/switch**：出厂默认账号/密码 <<<PAGE 21>>>
- **aaa authentication**：解锁会话类型命令族 <<<PAGE 23>>>
- **115200-8N1 + rollover**：console 默认参数与线缆类型 <<<PAGE 18>>>
- **XON/XOFF**：软件流控（console 无 RTS/CTS 硬件握手）<<<PAGE 76>>>
- **Reset 按钮**：前面板系统重启按钮 <<<PAGE 28>>>等
- **RCL（Remote Configuration Load）**：远程配置加载（详见 Switch Management Guide）<<<PAGE 21>>>
- **show system / write memory**：查看系统信息 / 保存配置 <<<PAGE 25>>>
- **system location**：设置交换机物理位置 <<<PAGE 24>>>

## 标准与合规（附录 A）
- **UL 60950-1 / IEC 60950-1**：IT 设备安全标准（第二版）<<<PAGE 82>>>
- **EN 60825-1/-2**：激光产品安全标准 <<<PAGE 82>>>
- **FCC Part 15 Class A / CISPR 22**：Class A 电磁干扰限值 <<<PAGE 82>>>/<<<PAGE 84>>>
- **ETS 300 019**：环境试验标准（存储 1.1/运输 2.3/固定使用 3.1）<<<PAGE 83>>>
- **Class 1M Laser**：1M 级激光辐射、勿用光学仪器直视 <<<PAGE 84>>>
- **CR1220**：机箱 RTC 锂电池型号（X48C6/T48C6/X48C4E/V48C8）<<<PAGE 81>>>
- **UN3091**：设备内含锂金属电池的运输分类（不得入生活垃圾）<<<PAGE 80>>>
- **Prop 65 / WEEE / RoHS**：加州 65 号 / 欧盟回收 / 有害物质限制 <<<PAGE 78>>>-<<<PAGE 80>>>
- **CDE（Cable Discharge Event）**：线缆静电放电事件；接线前对地放电 <<<PAGE 15>>>
- **ESD 腕带**：防静电腕带，接触部件前消除静电 <<<PAGE 88>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安保措施的维护人员可进入 <<<PAGE 88>>>
- **Tmra**：最大额定环境温度（封闭机架内按此折减）<<<PAGE 49>>>

## principles

## 定位与家族架构
- **P1** 定位双栖：汇聚层 + 数据中心机柜顶："The OmniSwitch 6900 (OS6900) is a family of aggregation switches that can also be installed as top-of-rack boxes in data centers." <<<PAGE 12>>>
- **P3** 十机型端口谱系：V72=48×SFP28+6×100G；C32=32×100G；C32E=32×100G+2×SFP+；T48C6=48×10GBaseT+6×100G；X48C6=48×SFP+ +6×100G；X48C4E=40×SFP+ +8×SFP28+6×100G；V48C8=48×SFP28+8×100G+2×SFP+；T24C2/X24C2=24 下行+2×SFP+ +2×100G；OS6920-D32=32×QSFP-DD 400G <<<PAGE 12>>>
- **P4** OS6920-D32 单口多形态：QSFP-DD 口支持 400G/2X200G/4X100G，向下兼容 QSFP56(200G)、QSFP28(100G)、QSFP+(40G) <<<PAGE 46>>>
- **P5** 全家族统一管理接口三件套：RJ45 10/100/1000 EMP 带外管理口 + console（USB 或 RJ45 按机型）+ USB 2.0 高速口（480Mbps），多数机型另有 Reset 按钮 <<<PAGE 12>>>
- **P7** 全家族统一环境包络：Tmra 0-45°C、存储 -40~70°C、湿度 5%-95%；例外——OS6920 后→前气流限 0-35°C <<<PAGE 14>>>/<<<PAGE 29>>>等/<<<PAGE 47>>>
- **P8** 机箱深度三档：T48C6/X48C6/T24C2/X24C2 为 47.3cm；V72/C32/C32E/X48C4E/V48C8 为 51.5-53.6cm；OS6920-D32 深 59cm（23.23"）——决定机架深度与后支撑需求 <<<PAGE 29>>>等/<<<PAGE 35>>>等/<<<PAGE 47>>>
- **P9** 功耗谱系：桌面级 X24C2=75/197W → 中档 T48C6=139/315W → 高档 V48C8=226/532W、C32=145/543W → OS6920-D32 最高 1400W <<<PAGE 45>>>等/<<<PAGE 35>>>/<<<PAGE 41>>>/<<<PAGE 31>>>/<<<PAGE 47>>>
- **P10** chassis vs ambient 温度语义 + 机型差异："Due to different airflow characteristics, chassis temperatures will vary by model."（机箱温度恒高于室温且随机型变化）<<<PAGE 29>>>等
## 可用性与冗余机制
- **P11** 1+1 电源冗余模型："OS6900 switches provide 1+1 redundant hot-swappable power supplies and a hot-swappable fan tray."（第二电源装入后处于 standby 角色）<<<PAGE 12>>>/<<<PAGE 59>>>
- **P12** 热插拔三件：电源、光模块、风扇托盘——"The following hardware components can be hot-swapped: Power supplies / Transceivers / Fan tray." <<<PAGE 13>>>
- **P13** 三大可用性支柱：Power Supply Redundancy、Hot-Swapping、Hardware Monitoring（自动 trap + LED + 用户 show 命令）<<<PAGE 13>>>
## 气流机制（本书核心）
- **P14** 双向气流架构："The switch supports both Front-to-Rear and Rear-to-Front airflow depending on the fan tray and power supplies installed. The airflow direction of the power supplies and fan tray must be the same." <<<PAGE 50>>>
- **P15** 气流失配三段式后果：错误+trap 显示 → 若启动时检测到则 OK/PS LED 绿琥珀交替闪、GRN 闪绿且"the switch continuously reboots until the issue is corrected"；若运行中热插入失配件则 OK/PS 闪琥珀，到温度 Danger 阈值才重启 <<<PAGE 50>>>/<<<PAGE 52>>>
- **P17** 气流路径双向设计：前→后=顶部前进风口吸入→穿越模块舱与电路板→后部风扇/电源排风；后→前=反向（后部吸入、前顶排出）<<<PAGE 51>>>
- **P18** 盲板气流机制："When blank cover panels are missing, air does not take the direct route from the air intake vents... normal airflow is disrupted and an extra task is placed on the fan tray to cool the chassis." <<<PAGE 53>>>
## 电源机制
- **P19** 六型电源两代阵营：V 系（650W AC/DC，配 V72/C32/C32E/X48C4E/V48C8）与 X 系（400W 或 200/400W AC/DC，配 T48C6/X48C6/T24C2/X24C2）+ OS6920 专用（1500W AC/1600W DC）；每型均分 F（前→后）/R（后→前）两气流版本 <<<PAGE 60>>>-<<<PAGE 65>>>
- **P20** 电源混插两条规则："Do not mix OS6900-V72/C32/C32E/X48C4E/V48C8 power supplies with OS6900-T48C6/X48C6/T24C2/X24C2 power supplies. Mixing an AC and DC power supply in the same chassis is supported."（代际不可混、AC+DC 可混）<<<PAGE 60>>>-<<<PAGE 65>>>
- **P21** 无总开关设计："Connecting an installed power supply to a power source will boot the switch. Likewise, disconnecting all installed power supplies from a power source will power off the switch." <<<PAGE 59>>>
- **P22** OS6920 电源双压输入：AC 1500W 在 100-127V 输出 12V/83.33A、220-240V 输出 12V/125A（高压输入得全功率）；"The system hold time for this power supply at 100% load is less than 20ms." <<<PAGE 64>>>
- **P23** 电源 LED 三态（全家族统一）：稳绿=正常供电、稳红=电源故障、灭=无 AC/DC 输入 <<<PAGE 60>>>-<<<PAGE 65>>>
- **P24** DC 供电纪律（OS6920 级）：接地 -40~-75V SELV 源；分支过流保护 50A；6AWG 铜导体；现场布线含断开装置；电源源须在受限进入场所；回流导体为 Isolated DC Return（DC-I）；设备设计装于 CBN <<<PAGE 66>>>
- **P25** IEC 60945 认证线缆：OS6900-X48C6 配 OS6900X-BPD-F 且需 IEC 60945（船用）认证时须用 OS-DNV-DC-PWR 线缆（双磁环）<<<PAGE 63>>>
- **P26** 冗余 AC 分电路原则："It is recommended that each AC outlet resides on a separate circuit." <<<PAGE 15>>>
## 风扇托盘机制
- **P27** 多风扇托盘架构：机箱后部 5 或 6 个独立风扇托盘（V72/C32/C32E/X48C4E/V48C8/OS6920 为 6 个；T48C6/X48C6/T24C2/X24C2 为 5 个），是机箱主温控部件 <<<PAGE 28>>>等
- **P28** 风扇托盘必装件："The fan tray is a required component. Never attempt to operate the switch without a fan tray installed." <<<PAGE 70>>>
- **P29** 风扇托盘分气流方向型号（F/R 后缀）且随机型专用："Do not attempt to install incompatible fan models in a chassis." <<<PAGE 70>>>/<<<PAGE 71>>>
- **P30** 60 秒更换窗口："The switch should not run without a fan tray more than 60 seconds to prevent over heating." <<<PAGE 72>>>
## LED 机制
- **P31** 系统 LED 五组：PS1/PS2（绿/琥珀/灭）；Diag（绿=正常/琥珀=自检故障）；Fan（绿/琥珀）；LOC（闪琥珀=远程定位激活）<<<PAGE 48>>>
- **P32** 端口速率 LED 分色：RJ45/SFP+（琥珀=1G、绿=10G）；SFP28（绿=25G、琥珀=10G、1G）；QSFP28 V/C 系（蓝=100G、琥珀=40G、LED1-4 白=4X25G、绿=4X10G）<<<PAGE 48>>>
- **P33** QSFP-DD 十二态色表：青=400G、紫=200G、蓝=100G、橙=40G、紫/绿=2X200G、蓝/绿=2X100G、黄/绿=2X50G、蓝/绿×3=4X100G、黄/绿×3=4X50G、白/绿×3=4X25G、全绿=4X10G、红=端口故障 <<<PAGE 48>>>
## 监控与温度机制
- **P34** 温度双阈值机制：Warning 超限→发 trap 业务继续（查气流阻塞/室温/风扇状态 `show fan`）；Danger 超限→自动关机直到人工处理并手动启动，Danger 出厂固化不可配置 <<<PAGE 75>>>
- **P35** 风扇自动监控："If any of the switch's fans unexpectedly shuts down, the switch sends out a trap and the FAN LED on the chassis front panel displays amber." <<<PAGE 75>>>
- **P36** 硬件监控命令族：`show module` / `show module long` / `show temperature` / `show fan` <<<PAGE 74>>>/<<<PAGE 75>>>
## 管理口机制
- **P37** EMP 线缆类型规则：EMP 接交换机用直通线（straight-through）、接计算机/工作站用交叉线（crossover）<<<PAGE 18>>>
- **P38** EMP 默认带外地址：IP 192.168.1.1 / 掩码 255.255.255.0；改址用 `ip interface emp address … mask …`，改前必须先走 console；未解锁会话类型前无法经 EMP 远程访问 <<<PAGE 22>>>
- **P39** console 流控机制："No hardware handshaking (RTS, CTS) is used. Instead, software flow control (XON, XOFF) is required."（RJ45 console 8 针定义：3=TXD、6=RXD、4/5=GND）<<<PAGE 76>>>
- **P40** 电涌防护军规五条：全设备等电位接地（≤0.01Ω）；室外/近交流线路用 STP Cat5e+；室外铜口串接浪涌保护器；防室外设备传浪涌给上游；Cat5e/6/6a 蓄静电须先对地放电防 CDE；违者可失保 <<<PAGE 15>>>/<<<PAGE 16>>>
