---
name: OmniSwitch 6570M 运维与排障（Dying Gasp 三通道、温度双阈值、LED 诊断、安全红线）
description: 需要配置 OS6570M Dying Gasp 告警（SNMP/Syslog/802.3ah OAM PDU）、巡检温度与模块状态（show module/temperature）、判读 OK/VC/PS LED 与 150W 电源六态灯、处置温度超限与遵守激光/ESD/锂电池安全红线时使用。
source_book: OmniSwitch 6570M Hardware Users Guide
---

## R（触发场景）
- 失电通告建设：Dying Gasp 三通道（SNMP trap/Syslog/802.3ah OAM PDU）配置
- 日常巡检：show module / show temperature 硬件巡检与温度阈值判读
- LED 诊断：OK/VC/PS1/PS2 系统灯与 150W 电源六态灯排障
- 温度超限处置：Warning trap / Danger 关机恢复
- 首次登录与安全红线：aaa 解锁、锂电池返厂、激光/ESD 警告

## I（核心理念）
高可用双支柱框架（F3，<<<PAGE 12>>>/<<<PAGE 35>>>/<<<PAGE 46>>>/<<<PAGE 47>>>）：供电侧=电源冗余+独立电路+Dying Gasp 三通道通告；运行侧=温度双阈值固化+LED 三层+show 巡检。DG 三通道语义（P28，<<<PAGE 46>>>/<<<PAGE 47>>>）：SNMP trap（前 3 站，含槽号/主备电源类型/失效时间）+Syslog"Dying Gasp Power Failure Event Occurred"（前 3 服务器）+4 个 802.3ah OAM Information PDU（Dying Gasp 位置位）；PDU 按端口优先级"上联口优先"发送（P29）。温度双阈值固化不可改（P12/X3）：Warning 发 trap 业务不停；Danger 自动关机且必须手动重启（X4）。

## A1（行动框架）
1. 巡检三步：show module 查槽位→show temperature 查五列（Current/Range/Danger/Thresh/Status）→UNDER THRESHOLD 即正常（C14/P13，<<<PAGE 45>>>）
2. 温度超限分诊（C15，<<<PAGE 45>>>/<<<PAGE 46>>>）：Warning=查气流遮挡+查室温；Danger=已关机，先处理诱因再手动重启
3. DG 接收端建设（C17）：snmp station 配 SNMP 站+swlog output socket 加 Syslog 服务器，各前 3 目标生效
4. DG 触发三场景预防（P30，<<<PAGE 46>>>）：唯一电源失效/主备先后失效/后备主先后失效——每电源接独立电源源
5. LED 三层诊断（P26，<<<PAGE 27>>>）：OK 灯（稳绿 OK/闪绿进行中/稳琥珀失败）→VC 灯（角色与 unit 号）→PS 灯（U28 三态/12 口两态）

## A2（操作步骤）
- **DG OAM 配置**：efm-oam admin-state enable→efm-oam port 1/1/23-24 admin-state enable→efm-oam port 1/1/23-24 propagate-events dying-gasp enable（C16，<<<PAGE 47>>>）
- **DG 告警接收配置**：snmp station+swlog output socket（C17，<<<PAGE 46>>>/<<<PAGE 47>>>）
- **首次登录六步**：console（9600-8N1，DCE）→admin/switch→aaa authentication 解锁会话→password 改密→system timezone/contact 等→show system→write memory（C2，<<<PAGE 16>>>-<<<PAGE 19>>>）
- **150W 电源六态灯判读**：稳绿=正常/闪绿=待机可接管/闪红=本舱无 AC 邻舱有电/闪绿红=告警/稳红=故障/灭=全机无输入（P19，<<<PAGE 38>>>/<<<PAGE 39>>>）
- **EMP 带外管理**：对交换机用直通线、对计算机用交叉线（P35，<<<PAGE 16>>>）

## E（实证案例）
- DG 三通道完整配置与上联口 PDU 优先（C16/C17/P28/P29，<<<PAGE 46>>>/<<<PAGE 47>>>）
- 温度 Warning/Danger 双阈值处置流程（C15，<<<PAGE 45>>>/<<<PAGE 46>>>）
- 12/12D 与 U28 阈值分化排障：12 口机 85/88°C vs U28 69/74°C——光口机热预算更紧（P9，<<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>）

## B（反例与坑）
- 阈值固化不可改（Warning/Danger 均出厂设定）；Danger 关机不会自动恢复，须手动重启（X3/X4，<<<PAGE 45>>>/<<<PAGE 46>>>）
- aaa authentication 一次只能指定一类会话；密码覆盖受限，忘记密码恢复困难（X5/X6，<<<PAGE 18>>>）
- 锂电池更换须返厂 ALE，错换有爆炸风险（X22，<<<PAGE 58>>>）
- Class 1M 激光开盖勿用光学仪器直视；空光口勿直视并加盖（X23/X24，<<<PAGE 54>>>/<<<PAGE 55>>>）
- 雷暴禁作业；运行中勿触背板与电源舱；搬运前断全部电源（X16/X17/X18，<<<PAGE 55>>>-<<<PAGE 56>>>）
- ESD 防护强制，操作组件前消除人体静电（X21，<<<PAGE 57>>>）

来源：OmniSwitch 6570M Hardware Users Guide（Ch2-Ch3+附录 A，p16-58）
