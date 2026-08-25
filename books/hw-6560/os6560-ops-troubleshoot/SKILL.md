---
name: OmniSwitch 6560 运维与排障（lanpower 全家桶/Dying Gasp/温度双阈值/LED 诊断）
description: 需要日常巡检 OS6560（show module/temperature/powersupply）、PoE 优先级与拒载排障（Guard Band/Priority Disconnect）、配置 Dying Gasp 失电通告、LED 状态诊断时使用。
source_book: OmniSwitch 6560 Hardware Users Guide
---

## R（触发场景）
- PD 上电被拒/掉电：Guard Band 拒载、优先级裁决、Class 检测排障
- 失电通告需求：配置 Dying Gasp（SNMP/Syslog/OAM PDU 三通道）
- 温度告警：区分 Warning（可配不停机）与 Danger（固化关机）
- 面板 LED 诊断：OK/VC/PWR 系统灯与 2.5G 口双灯读法

## I（核心理念）
高可用双支柱框架（F3，<<<PAGE 76-82>>>）：供电侧=双电源负载分担+独立电路+UPS+DG 失电三通道通告（SNMP trap 前 3 站/Syslog 前 3 服务器/4 个 802.3ah OAM PDU 上联口优先，P25，<<<PAGE 78-82>>>）；运行侧=温度双阈值（Warning 用户可配预警不停机→Danger 出厂固化关机，P26/X7，<<<PAGE 76>>>）+LED 三层+show 命令巡检。lanpower 命令族语义（P30，<<<PAGE 89-95>>>）：service 两级激活、admin-state 仅复活不能首启、power/maxpower 上限不预留、priority 三级、Priority Disconnect 同级按物理口号 1 高 48 低裁决。

## A1（行动框架）
PoE 排障决策树：
1. 口完全无电 → 查 slot service 是否 start（C15）
2. 新 PD 被拒 → Guard Band：余量低于口上限即拒（C18：降口上限放行）
3. 超预算掉 PD → Priority Disconnect：优先级+物理口号裁决（C19）
4. 老legacy 话机不识别 → capacitor-detection（仅此场景，X10）
5. 4pair/bt 高功率不通 → lanpower 4pair / 8023bt 使能（C20）

## A2（操作步骤）
- **巡检三命令**：show module / show temperature（UNDER THRESHOLD 正常；Warning 查气流室温；Danger 关机处理后手动启动）/ show powersupply（C13，<<<PAGE 75-76>>>/<<<PAGE 87>>>）
- **PoE 监控**：show lanpower 1 逐口 Maximum/Actual/Status/Priority/Class+槽预算（C22，<<<PAGE 96>>>）
- **优先级/限功率**：lanpower port priority critical；lanpower port power 3000 / slot maxpower 400（C16/C17，<<<PAGE 90-91>>>）
- **DG 配置**：efm-oam admin-state enable→port admin-state→propagate-events dying-gasp enable（C12，<<<PAGE 82>>>）；trap 站 snmp station / syslog swlog output socket（<<<PAGE 80-81>>>）
- **LED 读法**：OK（绿/闪绿/琥珀=启动失败）；VC（稳绿=master/琥珀=slave）；PWR（绿=正常/琥珀=故障）；2.5G 口 Speed+PoE 双灯（P15/P16，<<<PAGE 48-49>>>）

## E（实证案例）
- 硬件巡检三命令流程（C13）
- Guard Band 拒载处置：余 50W/口上限 75W 拒 4W PD→power 10000 放行（C18，<<<PAGE 92>>>）
- PoE 关断两级与复活（C15，<<<PAGE 89>>>）

## B（反例与坑）
- admin-state 不能首次激活 PoE，必须 slot service（X8，<<<PAGE 89>>>）
- class-detection 开启会复位全 PoE 口（X9）；电容检测不符 IEEE 仅限 legacy 话机（X10，<<<PAGE 89>>>/<<<PAGE 91>>>）
- Danger 阈值固化不可配；Warning 设太低会误告警（X7，<<<PAGE 76>>>）
- slot maxpower 下调可致低优先级口失电（C16 附加警告）
- BPS 状态只在 show lanpower 输出行看（P31，<<<PAGE 88>>>）
- ESD 腕带强制；锂电池同型号更换并返厂（X24/X25，<<<PAGE 108>>>/<<<PAGE 110>>>）

来源：OmniSwitch 6560 Hardware Users Guide（监控/DG/PoE Ch3-Ch4，p48-96）
