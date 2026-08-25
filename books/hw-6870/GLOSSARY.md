# GLOSSARY · OmniSwitch 6870 Hardware Users Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按机型/电源/LED 监控/PoE/管理/合规分组，精选 45 条。

## 机型
- **OS6870-24 / OS6870-48**：24/48×1G RJ45 + 4×SFP28 + 2×QSFP28 固定配置非 PoE，待机 71W/73W <<<PAGE 12>>>/<<<PAGE 23>>>/<<<PAGE 24>>>/<<<PAGE 29>>>/<<<PAGE 30>>>
- **OS6870-P24M**：模块化 24 口多千兆（至 10G）95W bt + 2×QSFP56 + 上行模块槽，待机 219.6W <<<PAGE 12>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **OS6870-P48M**：模块化 48 口多千兆（至 5G）95W bt + 2×QSFP56 + 上行模块槽，待机 251.8W <<<PAGE 12>>>/<<<PAGE 31>>>/<<<PAGE 32>>>
- **OS6870-P24Z / P48Z**：固定 24/48 口多千兆（至 2.5G）60W bt + 6×SFP28 + 2×QSFP28，待机 90.2W/92.4W；不支持 2000W 电源 <<<PAGE 12>>>/<<<PAGE 27>>>/<<<PAGE 28>>>/<<<PAGE 33>>>/<<<PAGE 34>>>/<<<PAGE 47>>>
- **OS6870-V12**：12×SFP28 全光 + 2×QSFP56 + 上行模块槽，无铜口 <<<PAGE 12>>>/<<<PAGE 35>>>/<<<PAGE 36>>>
- **OS6870-CNI-U2 / LNI-U6**：2×QSFP28 100G / 6×SFP56 50G 上行扩展节点机箱 <<<PAGE 12>>>/<<<PAGE 37>>>/<<<PAGE 38>>>
- **Uplink Module Slot**：M 系列/V12 的上行模块插槽，上行形态后置扩展 <<<PAGE 12>>>/<<<PAGE 25>>>
- **SFP28 / QSFP28 / QSFP56**：1/10/25G 小封装口 / 40/100G 四通道口 / 40/100/200G 增强四通道口 <<<PAGE 23>>>/<<<PAGE 25>>>
- **VFL（Virtual Fabric Link）**：ALE 虚拟光纤链路；SFP28 口 25G 推荐用于 VFL（LED 琥珀=VFL）<<<PAGE 23>>>/<<<PAGE 39>>>
- **多千兆（Multi-gigabit）**：2.5G/5G/10G RJ45 端口技术，配 802.3bt 大功率 PoE <<<PAGE 12>>>
- **chassis vs ambient 温度**：机箱内部传感器读数 vs 近似室温（前者恒高）<<<PAGE 24>>>

## 电源（Ch3）
- **PS-250W-AC（OS6870-BP）**：250W AC 电源（12V/20.8A，无 PoE 输出）<<<PAGE 48>>>
- **PS-250W-DC（OS6870-BP-D）**：250W DC 电源（-42~-60V/8A 输入）<<<PAGE 49>>>
- **PS-550W-AC-2（OS6870-BPH）**：550W AC 电源（V12 机型用）<<<PAGE 50>>>
- **PS-600W-AC-POE-2（OS6870-BPPH）**：600W PoE 电源（54.5V/11A，P 系列用）<<<PAGE 51>>>
- **PS-1200W-AC-POE-2（OS6870-BPPX）**：1200W PoE 电源；高 PoE 功率需 190-240VAC <<<PAGE 52>>>
- **PS-2000W-AC-POE-2（OS6870-BPXL）**：2000W PoE 电源；仅 P24M/P48M <<<PAGE 53>>>/<<<PAGE 47>>>
- **负载分担（Load Sharing）**：双电源均分供电负荷（含 PoE）<<<PAGE 47>>>/<<<PAGE 51>>>
- **电源混插（Mixing wattage）**：同一机箱允许不同瓦数电源（本家族特性）<<<PAGE 51>>>
- **Lock Tab（锁片）**：电源就位"咔哒"锁定/按压释放 <<<PAGE 55>>>/<<<PAGE 57>>>
- **Smart on / 12VSB**：电源待机智能开启（绿闪 LED）/12V 待机输出 0.1A <<<PAGE 48>>>
- **CBN / Isolated DC Return（DC-I）**：共同联结网络 / 隔离式 DC 回流（黑线 return）<<<PAGE 54>>>
- **Panduit LCD8-10A-L**：后部双螺纹孔接地 lug，配 8AWG、10-32 3/8" 螺丝、30-60 in-lb <<<PAGE 54>>>/<<<PAGE 57>>>

## LED 与监控（Ch3）
- **OK LED**：稳绿=诊断与 AOS 启动 OK/闪绿=进行中/稳琥珀=失败 <<<PAGE 38>>>
- **VC LED / VC ID LED**：稳绿=Master/稳琥珀=Slave；VC ID 多灯数值相加=单元号 <<<PAGE 38>>>/<<<PAGE 39>>>
- **PS LED / GRN(Leaf) LED**：电源状态灯 / 省电模式灯（稳绿=power saving）<<<PAGE 38>>>
- **RJ45 四色速率 LED**：绿=10/100/1000、蓝=2.5G、品红=5G、琥珀=10G；LED2 琥珀=PoE <<<PAGE 39>>>
- **光口 LED 两色**：绿=有效上行、琥珀=有效 VFL <<<PAGE 39>>>
- **EMP port**：后部以太网管理端口 <<<PAGE 23>>>
- **show module / show module long / show temperature**：槽位与温度监控（Danger/Thresh/Status）<<<PAGE 58>>>
- **Warning / Danger 阈值**：用户可配告警阈值（超限发 trap）/出厂固化阈值（超限自动关机须手动启动）<<<PAGE 58>>>/<<<PAGE 59>>>
- **Dying Gasp**：掉电告别三通道（SNMP trap+Syslog+Link OAM PDU）<<<PAGE 59>>>
- **efm-oam propagate-events dying-gasp / snmp station / swlog output socket**：DG 配置三命令 <<<PAGE 60>>>

## PoE（Ch4）
- **PSE / PD**：供电设备（检测/分级/供电/监控/回缩）/受电设备 <<<PAGE 61>>>
- **802.3bt**：第 4 代 PoE（Type 3/4，Class 5-8：45/60/75/90-99W，4 对线）<<<PAGE 62>>>/<<<PAGE 65>>>
- **PoH**：Power over Harness，配合 lanpower 4pair 提供 60/75/95W <<<PAGE 65>>>
- **lanpower 4pair / lanpower 8023bt**：开 4 对 60-95W / 开 bt Class 5-8 <<<PAGE 65>>>
- **lanpower slot service**：逐 slot 物理激活/停止 PoE（首次激活唯一途径）<<<PAGE 63>>>/<<<PAGE 65>>>
- **lanpower port admin-state**：单口 PoE 管理开关（不能首次激活）<<<PAGE 65>>>
- **lanpower power / slot maxpower / priority**：口/槽功率上限（不预留）/三级优先级（默认 low）<<<PAGE 63>>>/<<<PAGE 66>>>/<<<PAGE 67>>>
- **lanpower class-detection / capacitor-detection**：Class 检测（开启复位全机口）/电容检测（不符 IEEE）<<<PAGE 65>>>/<<<PAGE 67>>>
- **Priority Disconnect**：预算不足按优先级+物理口号（1 最高→48 最低）裁决；默认启用 <<<PAGE 68>>>/<<<PAGE 69>>>
- **Guard Band**：剩余预算小于口上限/类最大值即拒载新 PD <<<PAGE 67>>>/<<<PAGE 68>>>
- **show powersupply / show lanpower slot**：电源状态 / PoE 逐口与预算状态 <<<PAGE 63>>>/<<<PAGE 64>>>/<<<PAGE 71>>>

## 管理与登录（Ch2）
- **admin/switch / aaa authentication**：默认登录与会话解锁（一条命令一个会话类型）<<<PAGE 18>>>/<<<PAGE 19>>>
- **rollover 线 / 115200-8N1**：console 反转线与默认串口参数（全系 115200）<<<PAGE 17>>>
- **system location / show system / write memory**：物理位置设置 / 系统查看 / 配置保存 <<<PAGE 20>>>/<<<PAGE 21>>>
- **WebView**：内嵌 Web 管理界面（OmniVista 或浏览器启动）<<<PAGE 62>>>

## 安装部件与合规
- **弹簧夹法兰 / 后支架**：out→tab→CLICK→in 四步法兰；机架后部支撑件 <<<PAGE 42>>>/<<<PAGE 43>>>/<<<PAGE 44>>>
- **盲板（Blank Cover Panel）**：盖空槽导气流；电源槽安装箭头朝上 <<<PAGE 40>>>/<<<PAGE 41>>>
- **CDE / ESD 腕带 / 受限场所**：电缆静电放电 / 防静电腕带 / 仅限维护人员进入的位置 <<<PAGE 15>>>/<<<PAGE 83>>>
- **Hi-Pot Test / FCC Class A / Class 1M Laser**：2250VDC 耐压 / 商用 EMC（住宅禁用）/激光警告 <<<PAGE 77>>>/<<<PAGE 78>>>/<<<PAGE 79>>>
