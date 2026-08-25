# cases — OmniSwitch 6860/6860E/6860N Hardware Users Guide（安装/配置流程案例候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 上电与首次登录

- **C1** 上电流程：各电源线插入易达接地插座（禁延长线）；多电源数秒内先后插电；冗余 AC 每路独立电路；接电即自动开机 <<<PAGE 18>>>/<<<PAGE 22>>>
- **C2** 首次登录七步：console（Micro USB，9600-8N1；N 型 115200）→admin/switch→（E 型）EMP 设 IP→aaa authentication 解锁会话→password 改密→system timezone/time/date→system contact/name/location→show system→write memory <<<PAGE 22>>>-<<<PAGE 26>>>
- **C3** EMP 地址配置（E 型）：默认 192.168.1.1/255.255.255.0；ip interface emp address 168.22.2.120 mask 255.255.255.0 修改→show ip interface 核对；解锁会话前经 EMP 的 Telnet/FTP/HTTP/SSH/SNMP 均不可入 <<<PAGE 24>>>
- **C4** 会话类型按类解锁：aaa authentication default local 全解锁；或 telnet/http/ftp local 逐条执行（一次一类） <<<PAGE 25>>>

## 机箱安装

- **C5** 法兰安装流程：弹簧夹置 out（disengaged）→tab 插入机箱槽→按压法兰至"CLICK"锁定（clip 转 in/engaged）→附带螺丝固定→对侧重复；N-P48Z/P48M 加装 rear bracket guide 与 rear bracket <<<PAGE 64>>>/<<<PAGE 65>>>
- **C6** 机架整机安装流程：双人作业（一人抬一人拧）→标记孔位→法兰对齐机架柱→先下孔螺丝后上孔螺丝全紧固；重设备下置；机架螺丝自备；N-P48Z/P48M 后支架滑入导轨并固定机架 <<<PAGE 64>>>/<<<PAGE 66>>>/<<<PAGE 67>>>
- **C7** 桌面安装流程：4 橡胶脚垫入底板孔→正放（禁倒放/侧放）→接线缆；桌面须承载整备重量（至 8.16kg） <<<PAGE 68>>>
- **C8** 盲板安装流程：电源槽盲板箭头朝上→插入空槽→附带螺丝固定；空槽必须常盖 <<<PAGE 63>>>
- **C9** 现场准备检查单：0-45°C/95% 湿度域；前后 6"/侧 2" 间隙（上下免）；每电源一个接地插座；2 米原装线；专业安装师负责接地 <<<PAGE 18>>>/<<<PAGE 21>>>
- **C10** 开箱核对清单：机箱与电源按订单、光模块按订单、盲板、机架法兰、Micro USB-to-USB 线、国别电源线、橡胶脚垫、螺丝、防静电袋 <<<PAGE 20>>>

## 电源安装与 DC 接线

- **C11** 电源安装流程：电源插入后部电源舱→滑入至背板锁扣"click"锁定→插电源线（接电即开机）——四款电源及风扇托盘步骤通用 <<<PAGE 79>>>/<<<PAGE 80>>>
- **C12** 电源拆卸流程：先从电源源侧拔线→拔出电源线→按锁扣向中心→直拉抽出；不回装则盖盲板 <<<PAGE 81>>>/<<<PAGE 82>>>
- **C13** DC 线束接线流程（BP-D）：三芯 12AWG 线束插电源三孔（至 click）→另一端按极性接 -48VDC 熔丝面板（绿黄=地/黑=return/红=-48V）→绿黄接大地；前提：-48VDC SELV/15A/12AWG/易达断路/受限场所 <<<PAGE 78>>>/<<<PAGE 79>>>
- **C14** 机箱 supplemental 接地：Panduit LCD8-10A-L lug+10-32 螺丝装后部接地耳无漆区→8AWG 铜线接大地→力矩 30-60 in-lb <<<PAGE 83>>>

## 上联模块与风扇托盘

- **C15** 上联模块安装流程：模块插入 Slot 2→滑入至就位→captive 螺丝固定；拆卸：松螺丝→握牢直拉抽出（M 型 OS68-XNI/QNI/VNI/CNI 四款通用）<<<PAGE 84>>>
- **C16** 风扇托盘装拆：按电源装拆步骤执行（锁扣同构）——FANTRAY NONPOE 仅非 PoE 机型，占一个 150W 电源位 <<<PAGE 85>>>

## 监控与 Dying Gasp 配置

- **C17** 硬件巡检流程：show module / show module long→show temperature（VC 内逐机箱 CMMA/Slot 行，UNDER THRESHOLD 正常）→show powersupply（如 1/1 920 AC UP Internal）<<<PAGE 86>>>/<<<PAGE 87>>>/<<<PAGE 91>>>
- **C18** Dying Gasp OAM 配置：efm-oam admin-state enable→efm-oam port 1/1/23-24 admin-state enable→efm-oam port 1/1/23-24 propagate-events dying-gasp enable——同时发 PDU 的口上限=10−已配 SNMP/Syslog 服务器数 <<<PAGE 70>>>
- **C19** DG 告警接收配置：snmp station 配 SNMP 站（trap 前 3 站）；swlog output socket 加 Syslog 服务器（前 3 服务器）<<<PAGE 70>>>

## PoE 配置

- **C20** PoE 首次激活流程：show powersupply 确认（如 920 AC UP）→lanpower slot 2/1 service start→show lanpower slot 1/1 核对逐口/槽预算（Max Watts 780/BPS power: Not Available） <<<PAGE 91>>>/<<<PAGE 92>>>/<<<PAGE 95>>>
- **C21** PoE 关断两级：单口 lanpower port 1/1/12 admin-state disable；整槽 lanpower slot 1/1 service stop；admin-state enable 仅复活 <<<PAGE 96>>>
- **C22** 端口/槽功率与优先级调节：lanpower port 1/1/24 power 3000 降口限额；lanpower slot 3/1 maxpower 400 调槽上限（调低可致低优先级口掉电）；lanpower port 1/1/6 priority critical 设关键口 <<<PAGE 96>>>-<<<PAGE 98>>>
- **C23** Guard Band 解锁小功率 PD：剩余预算 < 口 maxpower 时 PD 不上电→lanpower power 1/1/1 power 10000 调低口上限至低于剩余预算→PD 上电 <<<PAGE 102>>>
- **C24** Priority Disconnect 开关：lanpower slot 2/1 priority-disconnect disable/enable——920W 电源上限 780W/电源、600W 上限 450W/电源 <<<PAGE 99>>>
- **C25** PoE 定时规则：lanpower power-rule 按日期/时间开关 PoE 供电（详见 CLI Reference） <<<PAGE 98>>>

---
合计：25 条（C1-C25）。
