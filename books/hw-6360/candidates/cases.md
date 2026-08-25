# cases — OmniSwitch 6360 Hardware Users Guide（安装/配置流程案例候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 上架前准备

- **C1** 安装前工具清单：接地腕带、Phillips 螺丝刀、平口螺丝刀；VC 配置另行参考 Switch Management Guide <<<PAGE 17>>>
- **C2** 站点准备流程：核对机箱规格表温湿度范围→预留前 6"/后 6"/侧 2" 气流间隙→确认每电源一个接地插座、电源线 2m 内可达且不接延长线 <<<PAGE 17>>>/<<<PAGE 19>>>
- **C3** 开箱清点流程：机箱（含电源）、按订单光模块、盲板、机架托架、国别电源线、橡胶桌脚、螺钉附件；就近开箱减少搬运 <<<PAGE 18>>>/<<<PAGE 19>>>

## 上电与首次登录

- **C4** 上电流程：接好网线/管理线→电源线插入易达的接地插座→自动上电启动；多电源时各线"rapid succession"（数秒内先后插上）保证启动全程供电充足 <<<PAGE 20>>>
- **C5** 首次登录六步流程：console 连接→admin/switch 登录→`aaa authentication default local`（或逐类 telnet/http/ftp）解锁会话→`password` 改密（输两遍，实时保存）→`system timezone`/`system time`/`system date` 设时间→`system contact`/`system name`/`system location` 设可选信息→`show system` 核对→`write memory` 保存 <<<PAGE 21>>>-<<<PAGE 24>>>

## 机箱安装

- **C6** 机架安装流程（全宽 24/48 口）：双人作业→一人抬机对准机架孔位→第二人先穿每侧法兰底部螺丝并拧紧→再上顶部螺丝全部紧固；重设备放机架下部防头重脚轻；机架螺丝用机架厂商的（ALE 不提供）<<<PAGE 48>>>/<<<PAGE 50>>>/<<<PAGE 51>>>
- **C7** 机架法兰安装流程：弹簧夹拨到 out（脱开）位→tab 插入机箱槽→按压法兰至"CLICK"锁入 in 位→附赠螺丝固定→对侧重复 <<<PAGE 49>>>/<<<PAGE 50>>>
- **C8** 桌面独立安装流程：4 个橡胶脚垫插入底板孔→正放于稳固平面（禁止顶面/侧面朝上运行）→接网络与管理线缆<<<PAGE 51>>>
- **C9** 半宽机型机架安装流程（OS6360-RM-19-L L 支架套件）：长短托架可左右互换装于机箱前部两侧→法兰孔对机架孔→先下孔后上孔穿螺丝紧固；部分套件需先拆出厂螺丝 <<<PAGE 52>>>/<<<PAGE 53>>>
- **C10** 壁挂安装流程（仅 10/P10，OS6360-WALL-MNT）：两侧前部装朝下托架→后部再装两个朝下托架→双人定位并在墙上标记孔位→预钻孔→用承重达标的紧固件固定（穿通软墙面入墙 stud）；建议机箱侧立、面板朝侧 <<<PAGE 54>>>/<<<PAGE 55>>>
- **C11** 盲板安装流程：电源槽位盲板箭头朝上→插入空槽→附赠螺丝固定；空槽任何时候都应盖盲板 <<<PAGE 48>>>

## 接地与监控

- **C12** 机箱 supplemental 接地流程：后板 lug 无漆区装 Panduit LCD8-10A-L 接地耳→8AWG 铜导线→扭矩 30-60 in-lb<<<PAGE 55>>>
- **C13** 硬件状态巡检流程：`show module`/`show module long` 看槽位→`show temperature` 看各传感器 Current/Range/Danger/Thresh/Status（UNDER THRESHOLD 为正常）→超 Warning 阈值查气流与室温，超 Danger 关机处理后手动重启 <<<PAGE 55>>>-<<<PAGE 57>>>

## PoE 配置流程

- **C14** PoE 首次激活流程：`show powersupply` 确认电源 UP→`lanpower slot 2/1 service start` 启动 slot 供电→`show lanpower slot 1/1` 核对端口 Maximum/Actual/Status/Priority/Class 与预算余量 <<<PAGE 60>>>/<<<PAGE 61>>>/<<<PAGE 62>>>
- **C15** PoE 关断两级操作：单口 `lanpower port 1/1/12 admin-state disable`；整槽 `lanpower slot 1/1 service stop`；admin-state enable 仅用于复活被 service 命令断电的口 <<<PAGE 62>>>/<<<PAGE 63>>>
- **C16** 端口功率限额调整案例：`lanpower port 1/1/24 power 3000` 把 24 口上限压到 3000mW——既可给高耗 PD 放量也可省预算 <<<PAGE 63>>>
- **C17** 槽级预算调整案例：`lanpower slot 3/1 maxpower 400` 把 3/1 槽上限设 400W；下调若低于当前总耗，低优先级口立即失电 <<<PAGE 64>>>
- **C18** 端口优先级配置案例：`lanpower port 1/1/6 priority critical` 把 6 口设为最高级，留给关键 PD；断电顺序 low→high→critical <<<PAGE 64>>>
- **C19** Class 检测启用流程：`lanpower slot class-detection`（默认关）开启严格按类限功率——注意会复位全机 PoE 口 <<<PAGE 61>>>/<<<PAGE 62>>>
- **C20** 802.3bt/4pair 使能流程：`lanpower 4pair` 开 4 对 60/75/95W（PoH）；`lanpower 8023bt` 开 bt 类型（Class 5-8）<<<PAGE 62>>>
- **C21** 电容检测启用（legacy 话机专用）：`lanpower slot 3/1 capacitor-detection enable`；仅兼容老 IP 话机，不符 IEEE，需向销售/支持确认型号 <<<PAGE 65>>>
- **C22** Guard Band 拒载处置案例：余 50W、新 PD 只需 4W 但口上限 75W 被拒载→`lanpower power 1/1/1 power 10000` 把口上限降到 10W→PD 放行 <<<PAGE 65>>>/<<<PAGE 66>>>
- **C23** Priority Disconnect 开关流程：默认启用；`lanpower slot 2/1 priority-disconnect disable` 关闭（此后新 PD 一律拒载）、`... enable` 恢复 <<<PAGE 66>>>/<<<PAGE 67>>>
- **C24** PoE 运行监控流程：`show lanpower 1` 输出逐口 Maximum/Actual Used/Status/Priority/On/Off/Class + 槽上限/预算已用/余量/电源数；尾部 `*` 号表示 4pair 口正跑在 2pair 模式 <<<PAGE 61>>>/<<<PAGE 68>>>/<<<PAGE 69>>>

---
合计：24 条（C1-C24）。
