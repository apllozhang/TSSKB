# cases — OmniSwitch 6560 Hardware Users Guide（安装/配置流程案例候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 上电与首次登录

- **C1** 上电流程：各电源线插入易达接地插座；多电源数秒内先后插电；冗余 AC 建议每路独立电路 <<<PAGE 16>>>/<<<PAGE 19>>>
- **C2** 首次登录六步流程：console（9600-8N1 DCE）→admin/switch→aaa authentication 解锁会话→password 改密→system time/date/timezone→system contact/name/location→show system→write memory <<<PAGE 19>>>-<<<PAGE 22>>>

## 机箱安装

- **C3** 机架法兰安装流程：弹簧夹置 out→tab 入机箱槽→按压至"CLICK"锁定→螺丝固定→对侧重复 <<<PAGE 54>>>/<<<PAGE 55>>>
- **C4** 机架整机安装流程：双人作业（一人抬一人拧）→标记孔位→对齐→先下孔螺丝后上孔螺丝全紧固；重设备下置；机架螺丝自备 <<<PAGE 53>>>/<<<PAGE 56>>>
- **C5** 桌面安装流程：4 橡胶脚垫入底板孔→正放稳固平面（禁倒放/侧放）→接线缆 <<<PAGE 57>>>
- **C6** 盲板安装流程：电源槽盲板箭头朝上→插入空槽→附赠螺丝固定；空槽常盖 <<<PAGE 52>>>
- **C7** DNV 安装流程（P48X4/X10）：OS-DNV-MNT 套件侧轨+后托架固定机箱后部→前托架入位→OS-DNV-FILTER 滤波器串接在电源与机箱之间（C14 入/C15 出，随机架托架与线扣固定） <<<PAGE 58>>>/<<<PAGE 59>>>
- **C8** 机箱 supplemental 接地：LCD8-10A-L 接地耳+8AWG 铜线+30-60 in-lb（后板无漆区）；DC 场景双接地孔装 lug 接大地 <<<PAGE 74>>>/<<<PAGE 68>>>

## 电源安装与接线

- **C9** 电源安装流程：电源插入后部电源舱→滑入至背板就位（锁扣"click"锁定）→插电源线——接电即开机 <<<PAGE 70>>>/<<<PAGE 71>>>
- **C10** 电源拆卸流程：先从电源侧拔线→按锁扣向中心→直拉抽出；不回装则盖盲板 <<<PAGE 72>>>/<<<PAGE 73>>>
- **C11** DC 线束接线流程（BP-D）：三芯 12AWG 线束一端插电源三孔连接器（至 click）→另一端按极性接 -48VDC 熔丝面板（绿黄=地/黑=return/红=-48V）→绿黄线接大地；前提：-48VDC SELV 可靠接地源、15A 过流保护、易达断路装置、受限场所 <<<PAGE 68>>>/<<<PAGE 69>>>
- **C12** Dying Gasp OAM 配置：efm-oam admin-state enable→efm-oam port 1/1/23-24 admin-state enable→efm-oam port 1/1/23-24 propagate-events dying-gasp enable <<<PAGE 82>>>
- **C13** 硬件巡检流程：show module/long→show temperature（UNDER THRESHOLD 正常；Warning 查气流/室温/阈值是否被设低，Danger 关机处理后手动启动）→show powersupply <<<PAGE 75>>>/<<<PAGE 76>>>/<<<PAGE 87>>>

## PoE 配置

- **C14** PoE 首次激活流程：show powersupply 确认（如 920 AC UP）→lanpower slot 2/1 service start→show lanpower slot 1/1 核对逐口/Max Watts/预算/BPS 状态 <<<PAGE 87>>>/<<<PAGE 88>>>/<<<PAGE 89>>>
- **C15** PoE 关断两级：单口 lanpower port 1/1/12 admin-state disable；整槽 lanpower slot 1/1 service stop；admin-state enable 仅复活 <<<PAGE 89>>>
- **C16** 端口/槽功率配置：lanpower port 1/1/24 power 3000 限口；lanpower slot 3/1 maxpower 400 限槽（下调可致低优先级口失电）<<<PAGE 90>>>
- **C17** 优先级配置：lanpower port 1/1/6 priority critical（low/high/critical 三级）<<<PAGE 90>>>/<<<PAGE 91>>>
- **C18** Guard Band 拒载处置：余 50W/口上限 75W 拒 4W PD→lanpower power 1/1/1 power 10000 降上限放行 <<<PAGE 92>>>
- **C19** Priority Disconnect 开关：默认启用；lanpower slot 2/1 priority-disconnect disable/enable；同级按物理口号（1 最高 48 最低）裁决 <<<PAGE 93>>>/<<<PAGE 94>>>
- **C20** bt/4pair 使能：lanpower 4pair 开 60/75/95W；lanpower 8023bt 开 Class 5-8 <<<PAGE 89>>>
- **C21** Class 检测/电容检测：lanpower slot class-detection（复位全 PoE 口）；lanpower slot 3/1 capacitor-detection enable（仅 legacy 话机）<<<PAGE 89>>>/<<<PAGE 91>>>
- **C22** PoE 监控：show lanpower 1 输出逐口 Maximum/Actual/Status/Priority/On-Off/Class + 槽预算/已用/余量/电源数 <<<PAGE 96>>>

---
合计：22 条（C1-C22）。
