# frameworks — OmniSwitch 6575 Hardware Users Guide（体系框架候选）

格式：编号 F# ｜ 框架名 ｜ 结构与运用 ｜ 页码

- **F1** 6575 家族选型三轴矩阵：轴一=安装形态（P12=DIN 导轨/壁装配电柜；U28=19 英寸机架 1U；MP16=壁装工业现场）；轴二=端口与连接器（P12=8×bt 60W RJ45；U28=全光 24 SFP+4 combo；MP16=M12 防水四段阵列 at/bt/纯数据/bypass）；轴三=供电与 PoE（P12=外置 BPNS/BPNSX；U28=后装双 BPR/BPRD 或 BPNSX；MP16=20-110VDC 宽压直挂）。选型口诀：按物理环境定形态，按 PD 等级定 PoE 段（at 30W/bt 60W/bypass 保链路），再按温度查预算表选电源档（高温场预算减半，双电源既有冗余又保预算）。 <<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 60>>>
- **F2** 温度-PoE 预算联动框架：预算=机型×电源×数量×温度带四元函数。部署四查：一查 Tmra 所在温度带（≤50/50-60/60-70/70-75°C）；二查机型×电源×数量的预算表（注意 MP16/U28+BPNSX 有机内封顶，加电源不扩容）；三查输入电压档位（U28：50-57V=at 150W、44-57V=af 120W、24-60V=纯系统、<48V 一律禁 PoE）；四查 Guard Band（剩余预算须大于端口 maxpower 才上电，必要时调低口上限）。 <<<PAGE 24>>>/<<<PAGE 60>>>/<<<PAGE 61>>>/<<<PAGE 67>>>
- **F3** 工业高可用三支柱框架：链路侧=MP16 Port Bypass 断电旁路（13-16 口失电自动直连保通信）；供电侧=双同规格电源+独立电路+UPS（911 纪律）+Dying Gasp 双通道（SNMP trap/Syslog 各前 3 目标）+Alarm Relay 干接点外送（NO/NC 触点 220VDC/250VAC/2A）；运行侧=无风扇宽温（-40~75°C）+温度双阈值（93/98°C：Warning 发 trap→Danger 关机手动恢复）+Alarm in/out/event 三源映射（VC 内跨机同步）。 <<<PAGE 12>>>/<<<PAGE 48>>>/<<<PAGE 50>>>-<<<PAGE 52>>>

---
合计：3 条（F1-F3）。
