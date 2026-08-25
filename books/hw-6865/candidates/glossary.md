# glossary — OmniSwitch 6865 Hardware Users Guide（术语表候选）

格式：`- **术语**：解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 机型与机箱（Ch1-Ch2）

- **OmniSwitch 6865-P16X**：16 口 PoE 加固型，2 SFP+ + 2 SFP + 4×75W HPoE/bt + 8×PoE+，半宽 2RU，待机 30W <<<PAGE 42>>>/<<<PAGE 44>>>
- **OmniSwitch 6865-U12X**：12 口上行型加固交换机，2 SFP+ + 6 SFP + 4 HPoE 口，半宽 2RU，待机 29W <<<PAGE 45>>>/<<<PAGE 46>>>
- **OmniSwitch 6865-U28X**：28 口上行型加固交换机，4 SFP+ + 20 SFP + 4 HPoE + 2 QSFP+ VFL，全宽 1RU，待机 50W <<<PAGE 47>>>/<<<PAGE 48>>>
- **加固型（Hardened）**：面向严苛电气与宽温环境（-40~74°C）设计的交换机品类 <<<PAGE 42>>>
- **TMRA**：最大额定环境温度（Tmra），封闭机架内按此折减 <<<PAGE 9>>>
- **DNV**：挪威船级社（Det Norske Veritas）；DNV 2.4 为船用认证标准，装 DNV 电源盖后温度限 55°C <<<PAGE 42>>>/<<<PAGE 68>>>
- **VFL（QSFP+ VFL Ports）**：U28X 后部 29/30 口的 QSFP+ 虚拟光纤链路端口 <<<PAGE 49>>>
- **1588v2**：IEEE 精密时间同步协议，全 6865 家族支持（电力/工业场景用）<<<PAGE 43>>>
- **半宽 2RU / 全宽 1RU**：P16X/U12X 为 8.5 英寸宽 2RU 机箱；U28X 为 17.2 英寸宽 1RU 机箱 <<<PAGE 42>>>/<<<PAGE 47>>>

## 电源与供电（Ch2）

- **OS6865-BP**：180W 模块化 AC 电源（100-240VAC，+56VDC/3.22A 输出），最多装 2 个 <<<PAGE 49>>>
- **OS6865-BP-D**：180W/140W 模块化 DC 电源（-20~-28V/12A 或 -36~-72V/6A 输入；-56V 输出两档），最多装 2 个 <<<PAGE 50>>>
- **DB-15 连接器（带导向销）**：电源与机箱之间的供电连接接口，后装托盘靠导向销定位 <<<PAGE 19>>>/<<<PAGE 50>>>
- **电源托盘（Power Supply Tray）**：承载 1-2 个外置电源的托架，可侧装（机架用）或后装（桌面用）<<<PAGE 13>>>
- **Dying Gasp**：掉电告别机制——全电源丢失瞬间维持电力发 SNMP trap/Syslog/Link OAM PDU 后关机 <<<PAGE 53>>>
- **SELV**：安全特低电压电路；DC 电源须接可靠接地的 -24V/-48V SELV 源 <<<PAGE 51>>>
- **AHJ（Authority Having Jurisdiction）**：有管辖权的地方电气管理机构；DC 线超 3 米须咨询 <<<PAGE 51>>>
- **DC 回流（DC Return）**：DC 回流导体应接设备机框，各电源共用回流连接 <<<PAGE 51>>>
- **12AWG**：DC 供电线要求的铜导体线规（双导体）；接地引脚线用 22AWG <<<PAGE 51>>>/<<<PAGE 73>>>
- **Panduit LCD8-10AL**：后部接地双螺孔用的 UL 认证接地 lug 型号，配 8AWG 铜导线、扭矩 30-60 in-lb <<<PAGE 73>>>
- **CDE（Cable Discharge Event）**：电缆静电放电事件——Cat5e/6/6a 可蓄静电，接线前先对地放电 <<<PAGE 11>>>
- **UPS**：不间断电源；带 IP 话机的 PoE 交换机交换机与电源均应接 UPS <<<PAGE 56>>>

## PoE（Ch3）

- **PoE 预算（PoE Power Budget）**：按电源数量/类型与环境温度三档查表的可供电总瓦数 <<<PAGE 56>>>/<<<PAGE 57>>>
- **HPoE 口（75W）**：P16X/U12X/U28X 上支持 75W HPoE 或 60W 802.3bt 的 RJ45 口 <<<PAGE 44>>>/<<<PAGE 46>>>/<<<PAGE 48>>>
- **PD（Powered Device）**：受电设备，如 AP、IP 话机、摄像头 <<<PAGE 57>>>
- **PSE**：供电设备（交换机侧），浪涌保护器串接在 PSE 与 PD 之间 <<<PAGE 11>>>
- **Class 检测（Class Detection）**：按 802.3at 电流特征把 PD 分为 Class 0-4 并按类限功率；默认关闭，开启会复位全部 PoE 口 <<<PAGE 57>>>/<<<PAGE 58>>>
- **Fast PoE**：上电数秒即供电（PoE 默认态固化在 FPGA 镜像、配置存控制器 EEPROM），不等 AOS 启动完成 <<<PAGE 59>>>
- **Perpetual PoE**：软重启/重载期间 PD 供电不间断；MCU 固件升级例外 <<<PAGE 59>>>
- **Guard Band**：剩余预算小于端口最大功率或 PD 类最大值时拒载新 PD 的保护带机制 <<<PAGE 63>>>
- **Priority Disconnect**：预算不足时按端口优先级（low/high/critical）+物理端口号（1 最高→28 最低）裁决新 PD 去留；默认启用 <<<PAGE 61>>>/<<<PAGE 62>>>
- **电容检测（Capacitor Detection）**：为老式 IP 话机兼容提供的检测法，不符 IEEE 规范，默认禁用 <<<PAGE 61>>>
- **lanpower slot service**：逐 slot 物理激活/停止 PoE 供电的命令（首次激活唯一途径）<<<PAGE 56>>>/<<<PAGE 58>>>
- **lanpower power / lanpower slot maxpower**：分别设单口/整槽最大功率上限（不做功率预留）<<<PAGE 59>>>/<<<PAGE 60>>>
- **lanpower priority**：设端口优先级（low/high/critical）<<<PAGE 60>>>/<<<PAGE 61>>>
- **lanpower slot fpoe / ppoe**：开启 Fast PoE / Perpetual PoE <<<PAGE 59>>>
- **lanpower slot priority-disconnect**：开关 priority disconnect（默认启用）<<<PAGE 62>>>
- **lanpower capacitor-detection**：开关电容检测 <<<PAGE 61>>>
- **show powersupply / show lanpower slot**：查看电源状态 / PoE 状态与可用功率 <<<PAGE 57>>>

## 链路与告警（Ch2）

- **Link OAM / 802.3ah**：链路层操作管理维护协议；Dying Gasp 经其 PDU 的 Dying Gasp bit 上报 <<<PAGE 54>>>
- **efm-oam propagate-events dying-gasp**：让端口在 Dying Gasp 事件时发 802.3ah PDU 的命令 <<<PAGE 54>>>
- **SNMP trap**：SNMP 告警陷阱；Dying Gasp 发给前 3 个已配 SNMP 站 <<<PAGE 54>>>
- **swlog output socket**：添加 Syslog 服务器（接收 Dying Gasp 消息）的命令 <<<PAGE 54>>>

## 安装部件与套件（Ch1）

- **OS6865-REAR-MNT**：U28X 机架后固定套件（侧导轨+前/后支架）<<<PAGE 21>>>/<<<PAGE 22>>>
- **OS6865-TRAY-1U**：1U 空间并排安装两个电源托盘的机架套件 <<<PAGE 21>>>/<<<PAGE 24>>>
- **OS6865-DIN-MNT**：机箱 DIN 导轨安装套件（平支架+DIN 卡扣）<<<PAGE 26>>>
- **OS6865-DNV-FRCK / HRCK**：DNV 全架/半架安装套件（含 DNV 电源托盘 182343-10、电源盖、填充板、滑板）<<<PAGE 28>>>
- **DIN 导轨（DIN Rail）**：工业控制柜标准安装导轨；电源与机箱可分别安装/拆卸 <<<PAGE 25>>>/<<<PAGE 26>>>
- **张力弹簧卡扣（Tension Spring Clip）**：DIN 卡扣底部弹簧，上推压缩后挂钩/脱钩 <<<PAGE 25>>>
- **桌脚（Table Mount Feet）**：提供桌面安装底部 1/2 RU 间隙的必备脚垫 <<<PAGE 16>>>
- **机架法兰（Rack Mount Flanges）**：机架安装前左右必装的法兰板 <<<PAGE 16>>>
- **DB9-RJ45 连接器**：随箱附带的控制台串口转接头 <<<PAGE 12>>>
- **拇指螺丝（Thumb Screw）**：电源免工具固定螺丝 <<<PAGE 18>>>/<<<PAGE 19>>>

## LED 与管理（Ch1）

- **OK LED**：稳绿=正常运行、闪绿=诊断中、稳琥珀=软件错误 <<<PAGE 38>>>
- **VC LED**：灭=启动中、闪绿=VC Master、闪琥珀=VC Slave；闪烁次数=VC 单元号（每 5 秒停顿）<<<PAGE 38>>>
- **PS1/PS2 LED**：灭=电源不在位、稳绿=正常、稳琥珀=电源故障 <<<PAGE 38>>>
- **端口 LED 颜色语义**：RJ45 绿=非 PoE 链路、琥珀=PoE 链路；SFP 琥珀=100M；闪烁=有活动 <<<PAGE 38>>>
- **aaa authentication**：解锁会话类型（console/telnet/ftp/http/snmp/ssh）的命令族 <<<PAGE 39>>>
- **admin/switch**：出厂默认管理员登录名/密码 <<<PAGE 39>>>
- **system timezone / system time / system date**：时区（默认 UTC）/时间/日期设置命令 <<<PAGE 40>>>/<<<PAGE 41>>>
- **system contact / system name**：管理联系人/系统名可选参数命令 <<<PAGE 41>>>

## 标准与合规（附录 A）

- **IEEE 802.3 / 802.3af / 802.3at**：PoE 支持的标准栈（含 Hi-Pot 2250VDC 测试）<<<PAGE 56>>>/<<<PAGE 67>>>
- **ISA 12.12.01 (UL 1604)**：危险场所工业安全标准 <<<PAGE 67>>>
- **IEC 61850-3 / IEEE 1613**：变电站/电力环境 EMC 标准 <<<PAGE 67>>>
- **EN 50121-4 / IEC 62236-4**：铁路应用 EMC 标准 <<<PAGE 68>>>
- **NEMA TS-2**：交通控制设备标准 <<<PAGE 68>>>
- **UL 62368-1 / IEC 62368-1**：音视频与信息技术设备安全标准 <<<PAGE 65>>>
- **FCC Part 15 Class A**：商用环境电磁干扰限值（住宅环境可能干扰，需自费整改）<<<PAGE 70>>>
- **Prop 65**：加州 65 号提案警告（铅化合物致癌/生殖危害）<<<PAGE 69>>>
- **WEEE**：欧盟废弃电子电气设备指令（分类回收标志）<<<PAGE 70>>>
- **RoHS（中国/台湾）**：有害物质限制表 <<<PAGE 68>>>/<<<PAGE 69>>>
- **ESD 腕带（Wrist Strap）**：防静电腕带，接机箱右上接地 lug；电源须装好并接接地插座才有效 <<<PAGE 75>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安防措施的维护人员可进入的安装位置 <<<PAGE 74>>>
