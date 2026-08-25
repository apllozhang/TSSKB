# cases — OmniSwitch 6870 Hardware Users Guide（安装/更换/配置流程候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

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
