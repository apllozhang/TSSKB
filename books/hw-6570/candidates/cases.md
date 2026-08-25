# cases — OmniSwitch 6570M Hardware Users Guide（安装/配置流程案例候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 上电与首次登录

- **C1** 上电流程：各电源线插入易达接地插座（禁延长线）；多电源数秒内先后插电；冗余 AC 每路独立电路——接电即自动开机 <<<PAGE 13>>>/<<<PAGE 16>>>
- **C2** 首次登录六步：console 连接（9600-8N1，DCE）→admin/switch 登录→aaa authentication 解锁会话类型→password 改密→system timezone/time/date→system contact/name/location→show system 核对→write memory 保存 <<<PAGE 16>>>-<<<PAGE 19>>>
- **C3** 会话类型按类解锁：aaa authentication default local 全解锁；或逐类 aaa authentication telnet local / http local / ftp local 连续多条执行 <<<PAGE 18>>>

## 机箱安装（三套方案）

- **C4** 全宽机架安装流程（U28）：两侧装法兰→标记机架孔位→抬举对齐→先下孔螺丝后上孔螺丝全紧固；螺丝自备（not provided） <<<PAGE 29>>>/<<<PAGE 30>>>
- **C5** 单半宽机架安装流程（RM-19-L 套件）：L 支架长短臂任意侧装于机箱前部两侧→法兰孔对准机架孔→先下孔后上孔插入螺丝紧固 <<<PAGE 30>>>/<<<PAGE 31>>>
- **C6** 双半宽并排安装流程（DUO-MNT 套件）：slot 支架+slide 支架用 M3 平头螺丝装于两机前后→两机前后中央支架对齐滑合→盖板压前后支架用拇指螺丝固定→两侧装法兰→双人抬举入机架→先下孔后上孔紧固 <<<PAGE 32>>>-<<<PAGE 34>>>
- **C7** 现场准备检查单：维持机型规格表温湿度范围；预留机型对应气流间隙（12 口侧 2"/上下 1"；U28 上下 1RU/侧 2"）；每电源一个接地插座；2 米原装电源线；专业安装师负责接地与电气规范 <<<PAGE 13>>>/<<<PAGE 28>>>
- **C8** 开箱核对清单：机箱与电源按订单、光模块按订单、盲板、机架法兰、国别电源线、橡胶桌脚、螺丝、防静电袋与说明卡；就近开箱减少搬运 <<<PAGE 15>>>

## 电源安装与更换

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
