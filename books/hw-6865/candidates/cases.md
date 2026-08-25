# cases — OmniSwitch 6865 Hardware Users Guide（安装/更换/配置流程候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 电源托盘与机箱组装

- **C1** 侧装电源托盘两步：①确认四类支架位置正确且"Front Chassis 与 Front Tray 支架"对齐（支架可能出厂预装）②托盘与机箱孔位对齐后用附带螺丝紧固成单一组件 <<<PAGE 13>>>/<<<PAGE 14>>>
- **C2** 后装电源托盘：先拆除出厂预装的侧装支架；将托盘 tab 插入机箱后板槽位，托盘面与后板贴平后插入并拧紧附带的 2 颗 M4（机箱后部预装 4 颗 M4 供侧装用）+ 4 颗 M3X6 螺丝 <<<PAGE 14>>>/<<<PAGE 15>>>
- **C3** 机架法兰安装：法兰左右各一，孔位对准机箱/托盘侧面螺纹孔，插入并拧紧螺丝 <<<PAGE 16>>>
- **C4** 桌面脚安装（提供底部 1/2 RU 间隙）：按机箱/托盘侧面螺纹孔装脚；不同机型用孔位不同（U28X 用 mounting holes 'B' 4 孔 + 4 颗 M4X6；U12X/P16X 用 'C' 4 孔或 'D'4+'E'1 共 5 颗 M4X6）<<<PAGE 16>>>/<<<PAGE 17>>>

## 电源安装

- **C5** 侧装托盘装电源四步：①电源滑入托盘、底部后侧 tab 插入托盘底部槽位 ②对齐并拧紧前面拇指螺丝 ③电源-机箱连接线（DB-15）分别插入电源与机箱后部 DB-15 ④冗余配置在托盘另一侧重复 <<<PAGE 18>>>/<<<PAGE 19>>>
- **C6** 后装托盘装电源：电源按图方向摆放，DB-15 两侧导向销插入机箱后部导向孔，推入至连接器完全就位后拧紧拇指螺丝；冗余在另一侧重复 <<<PAGE 19>>>/<<<PAGE 20>>>
- **C7** 上电纪律：全部电源与电源-机箱电缆安装完毕且交换机就绪后才接电源——"Do not connect to a power source until all power supplies and power supply-to-chassis cables are installed and the switch is ready to boot."（插上电源线即自动上电，无开关）<<<PAGE 19>>>/<<<PAGE 20>>>
- **C8** 拆装电源总原则："Whenever connecting or disconnecting a power supply to/from a chassis, the power supply must be disconnected from the power source." <<<PAGE 17>>>

## 机架 / 桌面 / DIN / DNV 安装

- **C9** 机架安装七条建议：用机架厂商推荐螺丝（不附带）；预留间隙；预标记孔位；双人搬运；先装下部防头重脚轻；U28X 用 OS6865-REAR-MNT 套件固定后部；双托盘并排用 OS6865-TRAY-1U 套件 <<<PAGE 21>>>
- **C10** OS6865-REAR-MNT 后固定套件（U28X）四步：装侧导轨 → 装前支架 → 后支架滑入侧导轨 → 固定；孔位分"机箱+后电源托盘"与"仅机箱"两种模式（A/B/C/D 孔组，M4X6 螺丝）<<<PAGE 22>>>/<<<PAGE 23>>>
- **C11** 桌面安装两步：放置前核对全部环境/间隙要求 → 用适合桌面材质的螺栓/螺丝把组件固定到桌面 <<<PAGE 24>>>/<<<PAGE 25>>>
- **C12** DIN 导轨装电源四步：DIN 卡扣用 M4X6 螺丝装到电源 → 卡扣底部钩住 DIN 导轨下沿 → 上推压缩卡扣底部张力弹簧 → 卡扣顶部越过导轨后释放弹簧确认上下均锁定 <<<PAGE 25>>>
- **C13** DIN 导轨拆电源两步：上推压缩弹簧 → 顶部越过导轨后整体抬起取下 <<<PAGE 26>>>
- **C14** DIN 导轨装机箱（OS6865-DIN-MNT 套件）四步：两块平支架各用 4 颗 M5X10 螺丝装到机箱前后侧装支架 → 卡扣顶部钩住导轨顶部 → 旋下组件并下拉卡扣strap让底部钩住导轨底部 → 松开 strap 锁定 <<<PAGE 26>>>
- **C15** DIN 导轨拆机箱两步：下拉 strap 释放卡扣底部 → 底部旋离导轨后整体抬起 <<<PAGE 27>>>
- **C16** DNV 全架安装（OS6865-DNV-FRCK 套件）四步：①装侧导轨+后支架+电源托盘（侧导轨 7×M4X8、托盘 4×M4X8、支撑板）②装电源 ③装电源盖 ④总装（盖 4×M3X6、填充板 2×M3X6、滑板 2×M3X6）<<<PAGE 28>>>/<<<PAGE 29>>>/<<<PAGE 30>>>
- **C17** DNV 半架安装（OS6865-DNV-HRCK 套件）六步：①装/对齐前后机箱-托盘支架 ②托盘与机箱紧固 ③装前支架与侧导轨（前支架 4×M4X6 孔'B'）④拇指螺丝装电源（拇指螺丝朝前）⑤装电源盖 ⑥总装 <<<PAGE 31>>>-<<<PAGE 34>>>
- **C18** 墙装强度纪律：墙体与墙装螺丝（不附带）须能稳固支撑机箱+托架+电源总成；推荐 3.5mm×25mm 以上长螺丝穿透软面（石膏板）锚入墙柱或 plywood <<<PAGE 34>>>

## DC 电源接线

- **C19** DC 线束接电源：连接器插入电源接口直至"咔哒"锁紧（表示就位），再拧紧固定螺丝 <<<PAGE 51>>>
- **C20** DC 三线接线五步：①剥线 6-7.5mm（12AWG 三线，先确保未接电源）②小平口螺丝刀插入圆形孔旋松开夹打开地线槽 ③地线推入至触底（约半英寸）④旋紧孔上螺丝夹紧（拉线不应脱出）⑤正/负线重复 ②-④ <<<PAGE 52>>>/<<<PAGE 53>>>
- **C21** DC 线扎纪律：红黑双绞线按图"1.5 圈/25mm、半圈/12.5mm"间距绑扎 <<<PAGE 51>>>

## 首次上电与登录

- **C22** 上电与确认：电源线插入电源前面板再插接地插座（禁延长线）→ 自动上电启动 → 接冗余电源线 → 启动完成前不判断 LED 状态："Be sure the boot process is complete before checking LED status." <<<PAGE 38>>>
- **C23** 首次登录六步清单：console 登录（admin/switch）→ 解锁会话类型 → 改密码 → 设时区 → 设日期时间 → 设可选项并保存 <<<PAGE 39>>>/<<<PAGE 41>>>
- **C24** 解锁会话类型：远程会话（Telnet/FTP/WebView/SNMP）默认锁定；全部解锁 `aaa authentication default local`，单独解锁如 `aaa authentication telnet local` <<<PAGE 39>>>/<<<PAGE 40>>>
- **C25** 改密码四步：以 admin 登录 → `password` 回车 → 输入新密码 → 再输一次确认；密码实时存本地用户库、重启保留，无需额外保存命令 <<<PAGE 40>>>
- **C26** 时间设置：`system timezone` + `system daylight-savings-time`（默认 UTC）；`system time hh:mm:ss` + `system date mm/dd/yyyy` <<<PAGE 40>>>/<<<PAGE 41>>>
- **C27** 可选参数：`system contact`（管理联系人）与 `system name`（系统名，自由文本描述）<<<PAGE 41>>>

## PoE 配置

- **C28** PoE 物理激活：`lanpower slot 2/1 service start`（逐 slot）；端口曾被管理断电后重启用 `lanpower port 1/1/1-16 admin-state enable` <<<PAGE 58>>>
- **C29** 关 PoE：单口 `lanpower port 1/1/12 admin-state disable`；整 slot `lanpower slot 1/1 service stop` <<<PAGE 59>>>
- **C30** Fast PoE 开启：`lanpower slot 1/1 fpoe enable`；Perpetual PoE 开启：`lanpower slot 1/1 ppoe enable` <<<PAGE 59>>>
- **C31** 调口/槽功率上限：`lanpower power`（须带 chassis/slot/port 全三段）；`lanpower slot 1/1 maxpower 150`（slot 上限降为 150W，注意调低可致低优先级口断电）<<<PAGE 59>>>/<<<PAGE 60>>>
- **C32** 设口优先级：`lanpower port 1/1/6 priority critical`（关键任务 PD 专用口）<<<PAGE 61>>>
- **C33** 电容检测开关：`lanpower slot 1/1 capacitor-detection enable`（仅传统 IP 话机兼容用）<<<PAGE 61>>>
- **C34** Priority Disconnect 开关：`lanpower slot 1/1 priority-disconnect disable|enable`（默认启用）<<<PAGE 62>>>
- **C35** Dying Gasp Link OAM 配置三命令：`efm-oam admin-state enable` → `efm-oam port 1/1/23-24 admin-state enable` → `efm-oam port 1/1/23-24 propagate-events dying-gasp enable` <<<PAGE 54>>>
- **C36** PoE 状态查看：`show powersupply`（电源类型/状态）；`show lanpower slot`（PoE 状态与新 PD 可用功率）<<<PAGE 57>>>
