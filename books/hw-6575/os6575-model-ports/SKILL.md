---
name: OmniSwitch 6575 机型与端口体系（P12/U28/MP16 选型、M12/M23 连接器、Port Bypass、VFL）
description: 需要在 OS6575-P12/U28/MP16 三机型间按安装形态选型、解码 M12 D-code/X-code 与 M23 防水连接器、规划 Uplink/VFL 堆叠口与 MP16 四段端口阵列（at/bt/Bypass）、核对输入电压域与 PoE 等级时使用。
source_book: OmniSwitch 6575 Hardware Users Guide
---

## R（触发场景）
- 6575 家族选型：P12（DIN 导轨）/U28（1U 机架）/MP16（壁装工业）三选一
- 解码 MP16 四段端口阵列与 M12/M23 防水连接器 pinout、选配件线缆
- 规划 Uplink/VFL 双角色 SFP+ 上联堆叠口
- 核对输入电压域与 PoE 等级（U28 三档、48V 以下禁 PoE）

## I（核心理念）
6575 选型三轴矩阵（F1，<<<PAGE 11>>>/<<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 60>>>）：轴一=安装形态（P12=DIN 导轨/壁装配电柜；U28=19 英寸机架 1U；MP16=壁装工业现场）；轴二=端口与连接器（P12=8×bt 60W RJ45；U28=全光 24 SFP+4 combo；MP16=M12 防水四段阵列）；轴三=供电与 PoE（P12=外置 BPNS/BPNSX；U28=后装双 BPR/BPRD 或 BPNSX；MP16=20-110VDC 宽压直挂）。全家族无风扇、Tmra -40~75°C（P1）。MP16 独有 Port Bypass 断电旁路："失电或故障时自动直连两口保通信"（P3，<<<PAGE 12>>>/<<<PAGE 25>>>）。铁律：48VDC 以下一律禁 PoE（P11/X1）。

## A1（行动框架）
1. 按物理环境定形态：P12=17×9.1×16.1cm/2.5kg（最小）；MP16=17.5×27×8cm/3.4kg（超薄挂墙）；U28=44×29.5×4.34cm/5.6kg（1U）（P8，<<<PAGE 22>>>/<<<PAGE 24>>>/<<<PAGE 26>>>）
2. 按 PD 等级定 PoE 段：at 30W / bt 60W / Bypass 保链路——MP16 四段一口一功能（P2）
3. 按输入电压核对 PoE 档位（U28，P10，<<<PAGE 24>>>）：50-57V=at 150W；44-57V=af 120W；24-60V=纯系统无 PoE；<48V 禁 PoE
4. 堆叠规划：Uplink/VFL 双角色口——P12 的 9-12 与 U28 的 29-32，LED 绿=uplink/琥珀=VFL 分色（P4）
5. MP16 连接器选型：数据口 D-code（10/100）/X-code（千兆）、Power M23 5-pin、Console/USB/Alarm 全 M12 A-code（P5，<<<PAGE 25>>>/<<<PAGE 53>>>-<<<PAGE 55>>>）

## A2（操作步骤）
- **MP16 四段阵列核对**：1-4 纯 10/100（D-code）；5-8 at 30W（D-code）；9-12 bt 60W（X-code）；13-16 Bypass 千兆（X-code）——速率与 PoE 按段固定（P2，<<<PAGE 11>>>/<<<PAGE 25>>>）
- **M12 X-code PoE pinout**：1-4 脚带 PoE-(G1)/PoE+(G1)、5-8 脚带 PoE-(G2)/PoE+(G2)；D-code PoE 为 1/3 脚 PoE+、2/4 脚 PoE-（P6，<<<PAGE 54>>>）
- **M23 5-pin 电源**：PWR-1±/FGND/PWR-2± 双路输入（<<<PAGE 25>>>/<<<PAGE 53>>>）
- **配件线缆选型**：M12-CONSOLE-5P/USB-2P/ALARM-6P、M12-DC-M/RJ45F/RJ45M-8P（D-code 族）、M12-XC-*（X-code 族）、M23-PWRCONN-5P（<<<PAGE 55>>>）
- **端口 LED 判读**：稳/闪绿=非 PoE 链路、稳/闪琥珀=PoE 链路（P23，<<<PAGE 27>>>）

## E（实证案例）
- MP16 四段阵列工业现场部署：at 段接摄像头、bt 段接高功率 PD、Bypass 段接关键链路（P2/P3）
- U28 全光 + combo PoE 90W 混合接入（P1，<<<PAGE 11>>>/<<<PAGE 23>>>）
- P12 DIN 导轨配电柜部署：8×bt 60W + 4×SFP+ VFL（P1，<<<PAGE 21>>>）

## B（反例与坑）
- 48VDC 以下禁 PoE（三机型面板注记；第三方电源同理须 ≥48V）（X1/P11，<<<PAGE 21>>>/<<<PAGE 23>>>/<<<PAGE 25>>>/<<<PAGE 61>>>）
- MP16 各段速率与 PoE 等级固定，不能软件改段（P2）
- M12 非 RJ45：普通网线不能直插，须配 D-code/X-code 转 RJ45 配件线缆（P5，<<<PAGE 55>>>）
- U28 输入电压低档（24-60V/1.5A）仅为系统供电，误按 at 满配 PoE 会拒载（P10，<<<PAGE 24>>>）

来源：OmniSwitch 6575 Hardware Users Guide（Ch1/Ch3，p11-26、p53-55）
