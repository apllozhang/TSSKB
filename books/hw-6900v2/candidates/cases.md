# cases — OmniSwitch 6900 Hardware Users Guide（安装/更换/配置流程候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 快速入门与上电

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
