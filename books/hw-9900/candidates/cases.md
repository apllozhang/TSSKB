# cases — OmniSwitch 9900 Series Hardware Users Guide（安装/更换/配置流程候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 机箱安装

- **C1** 机架安装纪律：11RU/17RU 高整机；三人作业——"Use two additional people to help lift and position the chassis"；先装机架下部防头重；机架螺丝按机架厂商规格（不附带）；非标机架需联系 ALE 选装硬件 <<<PAGE 36>>>
- **C2** 独立安装流程：稳固平面承满配重量（32.83/64.36kg 起）；两人以上搬运空机箱正位放置；保证气流间隙与 AC 插座可达 <<<PAGE 36>>>
- **C3** 满载机箱搬运禁令+空箱组装策略："Do not attempt to move or install a fully loaded chassis."——先就位空机箱再逐件装模块 <<<PAGE 32>>>

## 组件安装

- **C4** 装 CFM 六步：①确认遮挡槽位的风扇托盘已拆 ②模块电路板元件面朝左，板边插入上下 card guides 并部分推入 ③到中板连接器时上下锁杆保持 open 推到停 ④同时压上下锁杆至竖直（locked）位使模块紧固中板 ⑤手紧上下 captive 螺丝 ⑥重复装其他 CFM 后回装风扇托盘 <<<PAGE 36>>>-<<<PAGE 38>>>
- **C5** 装风扇托盘三步：①手持上下把手、底部朝外斜角把顶部两 tab 插入槽位顶部 ②推底部入槽至 firmly seated ③手紧底部拇指螺丝 <<<PAGE 39>>>-<<<PAGE 41>>>
- **C6** 装 NI 模块三步：①电路板板边插入机箱左右两侧凹槽 ②锁杆 open 位推模块至背板连接器 ③向面板中心拉紧锁杆至 90 度全闭锁固，手紧左右拇指螺丝 <<<PAGE 42>>>
- **C7** 装电源四步：①拆电源槽盲板留存 ②一手扶前面、一手托底承重，手柄 down（open）位后滑至背板 ③手柄上翻竖直（locked）位锁定并拧紧拇指螺丝 ④插电源线并接易触及接地插座（禁延长线）<<<PAGE 43>>>/<<<PAGE 44>>>

## 上电与首次登录

- **C8** 上电流程：全部电源线插入接地插座自动开机；多电源数秒内相继插电保证启动全程供电；启动完成前不判 LED 状态 <<<PAGE 45>>>
- **C9** 启动成功判据（主 CMM LED）：PRI 稳绿 + PS 稳绿 + FAB 稳绿 + TEMP 稳绿；LED 持续报错则联系客服 <<<PAGE 45>>>
- **C10** 首次登录七步：console 登录（admin/switch，RJ45 或 Micro-USB）→ 设 EMP IP → 解锁会话类型 → 改密码 → 设时区 → 设日期时间 → 设可选项并 `write memory` <<<PAGE 45>>>/<<<PAGE 46>>>
- **C11** EMP 设 IP：console 先行 → `ip interface emp address 168.22.2.120 mask 255.255.255.0` → `show ip interface` 验证；默认 192.168.1.1/24；未解锁会话类型前 EMP 不能远程访问 <<<PAGE 46>>>/<<<PAGE 47>>>
- **C12** 解锁会话：全部 `aaa authentication default local`；单个如 `aaa authentication telnet local`（console/telnet/ftp/http/snmp/ssh）<<<PAGE 47>>>
- **C13** 改密码与可选项：`password` 两输入；`system timezone`/`system time`/`system date`；`system contact`/`system name`/`system location`；`show system` 查看；`write memory` 保存 <<<PAGE 47>>>-<<<PAGE 49>>>

## 机箱功率预算管理

- **C14** 变更前查预算：加 NI/冗余 CMM/PoE 设备或拔电源前 `show chassis` 看 Power Left（示例输出 2041W 可用于新组件与 PD）；功率不足时新组件可能不上电并引发电源错误中断数据流 <<<PAGE 49>>>

## PoE 配置

- **C15** PoE 物理激活：`lanpower slot 2/1 service start`（逐 slot 首次激活唯一途径）；被断电口重激活 `lanpower port 2/1/1-24 admin-state enable` <<<PAGE 52>>>
- **C16** 关 PoE：单口 `lanpower port 1/1/12 admin-state disable`；整 slot `lanpower slot 1/1 service stop` <<<PAGE 52>>>/<<<PAGE 53>>>
- **C17** 调口/槽上限：`lanpower power`（须全三段 chassis/slot/port）；`lanpower slot 3/1 maxpower 400`（slot 降 400W，可致低优先级口断电）<<<PAGE 53>>>
- **C18** 设口优先级：`lanpower port 1/1/6 priority critical`（关键任务 PD 专用口）<<<PAGE 54>>>
- **C19** 电容检测：`lanpower slot 3/1 capacitor-detection enable`（仅传统 IP 话机）<<<PAGE 54>>>
- **C20** Priority Disconnect 开关：`lanpower slot 2/1 priority-disconnect disable|enable`（默认启用）<<<PAGE 55>>>
- **C21** 定时供电规则：`lanpower power-rule` 可按日期/时间开关 PoE（详见 CLI Reference）<<<PAGE 53>>>
- **C22** 状态查看：`show powersupply`（逐槽 Total/Used/Voltage/Type/Status）；`show lanpower slot 1/4`（逐口最大功率/实际用量/状态/优先级/Class/Type + slot 预算与已分配 PoE 总量）<<<PAGE 50>>>/<<<PAGE 51>>>

## 组件拆除

- **C23** 拆电源四步：①电源线从电源源与电源面板双端拔出，松前面拇指螺丝 ②手柄下拉至水平（open）位 ③一手握手柄部分拉出、另一手托底承重取出 ④空槽装盲板；不托底会导致电源壳尾部坠落损坏设备 <<<PAGE 57>>>/<<<PAGE 58>>>
- **C24** 拆风扇托盘三步：①松拇指螺丝 ②持上下把手拉出下把手使底部脱开，再向外向下拉出直至脱离顶部 tab ③"Three fan trays are required at all times. For switches currently operating, complete any maintenance and reinstall the fan tray as quickly as possible." <<<PAGE 58>>>/<<<PAGE 59>>>
- **C25** 拆 CFM：先拆遮挡的风扇托盘 → 松模块上下拇指螺丝、锁杆外拉释放 → 持前面板/锁杆滑出，全程托承模块重量防坠落 <<<PAGE 59>>>-<<<PAGE 61>>>
- **C26** 拆 NI 模块：松左右拇指螺丝、锁杆向外压释放 → 持前面板/锁杆滑出并托承重量 <<<PAGE 62>>>
- **C27** NI 热换完整流程：断模块全部网线 → 拔全部光模块 → 等 30 秒 → 插同类替代模块（"can only be hot swapped with like modules"）→ 回插光模块 → 重接网线；随后按提示操作 <<<PAGE 63>>>
