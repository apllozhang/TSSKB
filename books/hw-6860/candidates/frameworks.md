# frameworks — OmniSwitch 6860/6860E/6860N Hardware Users Guide（体系框架候选）

格式：编号 F# ｜ 框架名 ｜ 结构与运用 ｜ 页码

- **F1** 6860 三代选型矩阵：轴一=代际（基础=at PoE+20G VC 口最省钱；E=协处理器+EMP+HPoE 60/75W 私有高功率；N=bt 95W 多千兆+25G SFP28+QSFP28 VFL，M 型带上联模块槽）。轴二=下行口形态（24/48 铜、U28 全光、Z 多千兆混合、M 模块化上联）。轴三=电源档（非 PoE=150W AC/DC；PoE=600/920W；N 大功率=2000W 仅 M 型、230V 才满额）。选型口诀：普通办公选基础，要协处理器/EMP/私有 60W 选 E，Wi-Fi6/2.5G-5G AP 与 25G 上联选 N；预算按 N 型矩阵查（双 920W 最高 1500-1545W，P48M 双 2000W 达 3390W）。 <<<PAGE 14>>>/<<<PAGE 15>>>/<<<PAGE 69>>>/<<<PAGE 93>>>
- **F2** PoE 预算-抢占上限联动框架：三层预算闸门——层一=物理预算（机型×电源×数量矩阵，双电源约 2.4-2.7 倍于单电源；2000W 电源 115V 打对折）；层二=priority disconnect 上限（920W→780W/只、600W→450W/只，超限部分只供不抢）；层三=Guard Band（剩余预算须大于口 maxpower 才上电）。部署四查：查矩阵定预算、查电源档定抢占上限、调口 maxpower 解 Guard Band、按 24/48 口模型设优先级（端口号越大越高，与其他家族相反）。 <<<PAGE 93>>>/<<<PAGE 99>>>/<<<PAGE 100>>>/<<<PAGE 102>>>
- **F3** VC 堆叠高可用框架：链路侧=2×20G VC 口（N 代 QSFP28 VFL）+VC LED/闪琥珀报 unit 号；供电侧=1+1 双电源负载分担+独立电路+UPS（911 纪律）+DG 三通道（SNMP/Syslog 前 3 目标+4×OAM PDU，同时发 PDU 口数=10−服务器数，上联口优先）；PoE 侧=Fast PoE（上电数秒供电，FPGA 默认使能）+Perpetual PoE（软重启不断 PD 电）+per-slot service/maxpower/priority 三级管控；运行侧=温度双阈值（Warning trap→Danger 关机手动恢复，VC 内逐机箱独立）+五色端口 LED+show module/temperature/powersupply/lanpower 巡检。 <<<PAGE 15>>>/<<<PAGE 69>>>/<<<PAGE 70>>>/<<<PAGE 87>>>/<<<PAGE 96>>>
- **F4** 三代端口演化框架（讲解用）：基础代（千兆铜+SFP+ 10G 上联+20G VC）→E 代（+协处理器/EMP/OK2 双系统灯/HPoE 60-75W 私有高功率/E-P24Z8 首入 2.5G）→N 代（bt 95W 全覆盖、2.5G-10G 多千兆铜口、SFP28 25G 四口组〔组内禁 1G/10G 与 25G 混跑〕、QSFP28 VFL、M 型上联模块化）。讲选型史或替换规划时按此轴展开。 <<<PAGE 14>>>/<<<PAGE 46>>>/<<<PAGE 48>>>/<<<PAGE 56>>>

---
合计：4 条（F1-F4）。
