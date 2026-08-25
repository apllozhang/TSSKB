# cases — OmniSwitch 6575 Hardware Users Guide（安装/配置流程案例候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 上电与首次登录

- **C1** 上电流程：各电源线插入易达接地插座（禁延长线）；多电源数秒内先后插电；冗余 AC 每路独立电路；接电即自动开机 <<<PAGE 13>>>/<<<PAGE 16>>>
- **C2** 首次登录六步：console（rollover 线，9600/无流控/8N1，DCE）→admin/switch→aaa authentication 解锁会话→password 改密→system timezone/time/date→system contact/name/location→show system→write memory <<<PAGE 15>>>-<<<PAGE 19>>>
- **C3** 会话类型按类解锁：aaa authentication default local 全解锁；或 telnet/http/ftp local 逐条连续执行（一次只能一类） <<<PAGE 17>>>

## 机箱安装

- **C4** U28 前装机架流程：两侧装法兰→标记机架孔位→抬举对齐→先下孔螺丝后上孔螺丝紧固；螺丝自备 <<<PAGE 29>>>/<<<PAGE 30>>>
- **C5** U28 后装机架流程（OS6575-REAR-MNT 套件：2 侧轨+2 后支架+1 支撑支架+18×M4X8MM；另 OS6575-TRAY-1U 电源托盘）：装侧轨（各 7×M4，按孔位 A/C）+后支架+支撑支架（3×M4）→装电源托盘（4×M4）→装电源→整机入机架以拇指螺丝固定 <<<PAGE 31>>>/<<<PAGE 32>>>
- **C6** P12 DIN 导轨安装：DIN Rail Bracket 选件装于机箱→挂扣 DIN 导轨（"DIN Mounted Chassis"） <<<PAGE 33>>>
- **C7** P12 壁装流程：Wall Bracket 选件安装→挂壁（"The OmniSwitch-P12 is wall mountable"） <<<PAGE 34>>>
- **C8** MP16 壁装流程：利用机箱 Mounting Holes（后面板四角）直接螺丝挂壁 <<<PAGE 26>>>/<<<PAGE 35>>>
- **C9** 现场准备检查单：维持 -40~75°C 温湿度域；预留通风空间；每电源一个接地插座；2 米原装电源线；专业安装师负责接地与电气规范 <<<PAGE 13>>>/<<<PAGE 29>>>
- **C10** 开箱核对清单：机箱与电源按订单、光模块按订单、盲板、机架法兰、国别电源线、橡胶桌脚、螺丝、防静电袋与说明卡 <<<PAGE 15>>>

## 电源安装与 ROJ 接线

- **C11** 后装托盘电源安装流程（U28）：电源定向→DB-15 两侧导柱对准机箱后部导孔滑入→推至连接器完全就位→拧电源前端拇指螺丝→冗余配置在对侧连接器与螺孔重复 <<<PAGE 41>>>
- **C12** ROJ 输出线接线流程（电源→机箱）：红线插电源顶部前端 V- 端子与交换机电源连接器(-)端→黑线插 V+ 与(+)端→螺丝刀每端子拧 3.5 in-lb→绿线 ring 端子用附带螺丝固定电源地端并连交换机地端 <<<PAGE 43>>>/<<<PAGE 44>>>
- **C13** ROJ 输入线接线流程（市电→电源）：黑/棕线插底部前端 L 端子→白/蓝线插 N 端子→绿/绿黄条纹线插保护地端子→按电源标签力矩拧紧各端子 <<<PAGE 45>>>
- **C14** 最终上电连接：输出线插机箱前面板 PS1/PS2 电源连接器→AC 线 NEMA 5-15 头插易达 AC 源——插头在接到提示前不得插入电源或带电插座 <<<PAGE 45>>>/<<<PAGE 43>>>
- **C15** 电源热拔流程：从电源源侧拔插头→松开全部输入端子拆 AC 输入线→松开全部输出端子拆输出线→按接线流程装新电源（冗余下单电源可换不影响运行） <<<PAGE 46>>>
- **C16** 电源类型声明：powersupply 1 name ALE-75W-ps1 type ale lo-ac（逐电源声明；不能自动检测） <<<PAGE 46>>>

## 接地

- **C17** 机箱 supplemental 接地：Panduit LCD8-10A-L lug+10-32 螺丝装于接地耳无漆区→8AWG 铜线接大地→力矩 30-60 in-lb <<<PAGE 47>>>

## Alarm Relay 配置

- **C18** 告警输入→输出联动配置：alarm in temperature-alarm-in action alarm-out admin-state enable→alarm out alarm-out-1 admin-state enable→alarm map temperature-alarm-in out alarm-out-1 <<<PAGE 49>>>
- **C19** 系统事件→输出映射（认证失败例）：alarm event auth-fail-event event authentication-failure admin-state enable→alarm out set-alarm-out-chassis-1→alarm map auth-fail-event out set-alarm-out-chassis-1；show alarm event config 核对、show alarm status 看实时、alarm clear status 清除 <<<PAGE 49>>>

## 监控与 PoE 配置

- **C20** 硬件巡检流程：show module / show module long→show temperature（UNDER THRESHOLD 正常）→show powersupply（Total Power/PS Type/Status/Location）<<<PAGE 50>>>/<<<PAGE 62>>>
- **C21** DG 告警接收配置：snmp station 配 SNMP 站（trap 前 3 站生效）；swlog output socket 加 Syslog 服务器 <<<PAGE 52>>>
- **C22** PoE 首次激活流程：先 powersupply type 声明电源→lanpower slot 1/1 service start→show lanpower 1/1 核对逐口 Maximum/Actual/Status/Priority/On-Off/Class 与槽预算 <<<PAGE 46>>>/<<<PAGE 64>>>/<<<PAGE 71>>>
- **C23** PoE 关断两级：单口 lanpower port 1/1/4 admin-state disable；整槽 lanpower slot 1/1 service stop；admin-state enable 仅复活被断口 <<<PAGE 64>>>
- **C24** 端口/槽功率调节：lanpower port 1/1/4 power 3000（降口限额保预算）；lanpower slot 1/1 maxpower 400（调槽上限，注意调低可致低优先级口掉电） <<<PAGE 64>>>/<<<PAGE 65>>>
- **C25** 端口优先级设置：lanpower port 1/1/4 priority critical——低/高/关键三档，关键口在电力管理事件中最后断电 <<<PAGE 65>>>
- **C26** Guard Band 解锁小功率 PD：剩余预算 < 端口 maxpower 时 PD 不上电→lanpower power 1/1/1 power 10000 调低口上限至低于剩余预算→PD 正常上电 <<<PAGE 67>>>
- **C27** Priority Disconnect 开关：lanpower slot 2/1 priority-disconnect disable/enable——禁用后新 PD 一律按预算拒供不抢电 <<<PAGE 68>>>

---
合计：27 条（C1-C27）。
