# cases — OmniSwitch 6465 Hardware Users Guide（安装/配置流程案例候选）

格式：编号 C# ｜ 流程要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 上电与首次登录

- **C1** 上电流程：多电源时数秒内先后插电（rapid succession）；冗余 AC 建议每路接独立电路（"It is recommended that each AC outlet resides on a separate circuit"） <<<PAGE 15>>>/<<<PAGE 17>>>
- **C2** 首次登录六步流程：console（9600-8N1，DCE）→admin/switch→aaa authentication 解锁会话（default local 或逐类）→password 改密（实时保存）→system time/date/timezone→system contact/name/location→show system→write memory <<<PAGE 16>>>-<<<PAGE 20>>>

## 机箱安装

- **C3** DIN 导轨安装流程：顶卡扣挂轨顶→下旋至底卡扣锁定；拆卸：下拉卡扣释放→外旋抬出（卡扣难够到用长螺丝刀）<<<PAGE 39>>>
- **C4** 全宽机架安装流程（P28）：两侧装托架→标记机架孔→抬机对齐→先穿每侧底部螺丝紧固→再上其余螺丝（自备机架螺丝）<<<PAGE 40>>>/<<<PAGE 41>>>
- **C5** 半宽单机机架流程（OS6465T-RM-19-L）：长短 L 托架装前部两侧（可互换）→法兰孔对机架孔→先下孔后上孔穿螺丝紧固 <<<PAGE 41>>>/<<<PAGE 42>>>
- **C6** 双机并排机架流程（OS6465T-DUO-MNT）：slot/slide 托架用 M3 沉头螺丝装于两机前后→前后中置托架对齐滑合→板件+拇指螺丝锁定→两侧装机架托架→双人抬装上机架先下孔后上孔固定 <<<PAGE 43>>>-<<<PAGE 45>>>
- **C7** 侧挂/壁挂流程（OS6465-WALL-MNT，P6/P12/T 机型）：2 个侧托架各 3 颗 M4X8→2 个后托架各 M4X8→贴安装面标记打孔→每托架用 2×M5X15 螺栓+4 垫圈+2 螺母固定 <<<PAGE 45>>>/<<<PAGE 46>>>
- **C8** DNV 船用安装流程（P28）：装侧轨/后托架/电源托盘（各按 M4X8 定位）→装电源（托盘+拇指螺丝）→盖电源罩→装 filler 板与滑托架完成总成；P6/P12 用 DNV-DIN 左右电源罩+DIN 卡扣 <<<PAGE 46>>>-<<<PAGE 49>>>

## 电源安装与接换

- **C9** 后托盘电源安装流程：电源 DB-15 两侧导柱对准机箱后导孔→推入至连接器完全就位→拧前部拇指螺丝→冗余配置时对侧连接器/螺孔重复 <<<PAGE 56>>>/<<<PAGE 57>>>
- **C10** ROJ 输出线接线流程：红线入 V- 端子（电源顶前+机箱负端）、黑线入 V+（正端）→每端子扭矩 3.5 in-lb→地线用附赠螺丝固定到电源与机箱接地端（松动方孔内夹片即开）<<<PAGE 59>>>
- **C11** ROJ 输入线接线流程：黑/棕→L、白/蓝→N、绿/绿黄→保护地（电源底前）→按电源标注扭矩紧固；确认前严禁插 NEMA 5-15 入电 <<<PAGE 60>>>
- **C12** 最终上电连接：输出线插机箱 PS1/PS2→NEMA 5-15 插易达插座（Pluggable Type A，插座须近设备）<<<PAGE 60>>>
- **C13** 电源类型配置流程：`powersupply 1 name ALE-75W-ps1 type ale lo-ac`（双电源逐一配置）——系统不能自动识别，不配则功率/PoE 信息错误 <<<PAGE 60>>>/<<<PAGE 61>>>
- **C14** 电源热换流程：冗余时任一电源可不断电更换——断电源→松输入端子拆线→松输出端子拆线→按接线流程装新电源 <<<PAGE 61>>>
- **C15** 机箱 supplemental 接地：LCD8-10A-L 接地耳+8AWG 铜线+30-60 in-lb（前或后 lug 无漆区）<<<PAGE 62>>>

## 告警与监控配置

- **C16** 告警输入→输出映射流程：`alarm in temperature-alarm-in action alarm-out admin-state enable`→`alarm out alarm-out-1 admin-state enable`→`alarm map temperature-alarm-in out alarm-out-1` <<<PAGE 64>>>
- **C17** 系统事件→告警输出流程（认证失败示例）：`alarm event auth-fail-event event authentication-failure admin-state enable`→`alarm out set-alarm-out-chassis-1`→`alarm map auth-fail-event out set-alarm-out-chassis-1`→`show alarm event config` 核对→触发后 `show alarm status` 查看 <<<PAGE 64>>>
- **C18** 告警手工清除：`alarm clear status`（8 类事件条件恢复时自动清除）<<<PAGE 65>>>
- **C19** Dying Gasp OAM 通告配置：`efm-oam admin-state enable`→`efm-oam port 1/1/23-24 admin-state enable`→`efm-oam port 1/1/23-24 propagate-events dying-gasp enable`（PDU 上联口优先）<<<PAGE 68>>>/<<<PAGE 69>>>
- **C20** 硬件巡检流程：show module / show module long 看槽位→show temperature 看传感器（UNDER THRESHOLD 正常）→超 Warning 查气流与室温，Danger 关机处理后手动启动 <<<PAGE 66>>>/<<<PAGE 67>>>

## PoE 配置

- **C21** PoE 首次激活流程：先 `powersupply type` 配好电源→`show powersupply` 确认→`lanpower slot 1/1 service start` 激活→`show lanpower slot` 核对（Max Watts 按温度档显示）<<<PAGE 60>>>/<<<PAGE 75>>>/<<<PAGE 76>>>/<<<PAGE 77>>>
- **C22** 端口功率/优先级配置：`lanpower port 1/1/4 power 3000` 限 3W；`lanpower slot 1/1 maxpower 400` 槽上限；`lanpower port 1/1/4 priority critical` 关键口 <<<PAGE 77>>>/<<<PAGE 78>>>-<<<PAGE 79>>>
- **C23** Guard Band 拒载处置：余 50W、口上限 75W 拒 4W PD→`lanpower power 1/1/1 power 10000` 降到 10W 放行 <<<PAGE 80>>>
- **C24** Priority Disconnect 开关与理解：默认启用；`lanpower slot 2/1 priority-disconnect disable/enable`；同级新 PD 按物理口号裁决（1 最高 8 最低）<<<PAGE 82>>>/<<<PAGE 83>>>

---
合计：24 条（C1-C24）。
