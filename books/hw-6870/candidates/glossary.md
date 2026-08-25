# glossary — OmniSwitch 6870 Hardware Users Guide（术语表候选）

格式：`- **术语**：解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 机型（Ch1/Ch3）

- **OS6870-24**：24×1G RJ45 + 4×SFP28 + 2×QSFP28 固定配置 1U 非 PoE 机型，待机 71W <<<PAGE 12>>>/<<<PAGE 23>>>/<<<PAGE 24>>>
- **OS6870-48**：48×1G RJ45 + 4×SFP28 + 2×QSFP28 固定配置 1U 非 PoE 机型，待机 73W <<<PAGE 12>>>/<<<PAGE 29>>>/<<<PAGE 30>>>
- **OS6870-P24M**：模块化 24 口多千兆（至 10G）95W bt PoE + 2×QSFP56 + 上行模块槽，待机 219.6W <<<PAGE 12>>>/<<<PAGE 25>>>/<<<PAGE 26>>>
- **OS6870-P48M**：模块化 48 口多千兆（至 5G）95W bt PoE + 2×QSFP56 + 上行模块槽，待机 251.8W <<<PAGE 12>>>/<<<PAGE 31>>>/<<<PAGE 32>>>
- **OS6870-P24Z**：固定 24 口多千兆（至 2.5G）60W bt PoE + 6×SFP28 + 2×QSFP28，待机 90.2W <<<PAGE 12>>>/<<<PAGE 27>>>/<<<PAGE 28>>>
- **OS6870-P48Z**：固定 48 口多千兆（至 2.5G）60W bt PoE + 6×SFP28 + 2×QSFP28，待机 92.4W <<<PAGE 12>>>/<<<PAGE 33>>>/<<<PAGE 34>>>
- **OS6870-V12**：12×SFP28 全光机型 + 2×QSFP56 + 上行模块槽，无铜口 <<<PAGE 12>>>/<<<PAGE 35>>>/<<<PAGE 36>>>
- **OS6870-CNI-U2**：2×QSFP28 100G 上行扩展节点机箱 <<<PAGE 12>>>/<<<PAGE 37>>>
- **OS6870-LNI-U6**：6×SFP56 50G 上行扩展节点机箱 <<<PAGE 12>>>/<<<PAGE 38>>>
- **Uplink Module Slot**：M 系列/V12 具备的上行模块插槽，上行形态可后置扩展 <<<PAGE 12>>>/<<<PAGE 25>>>
- **SFP28**：支持 1G/10G/25G 的小封装光模块口（25G 推荐用于 VFL）<<<PAGE 23>>>等
- **QSFP28**：支持 40G/100G/4X10G/4X25G 的四通道光模块口 <<<PAGE 23>>>等
- **QSFP56**：支持 40G/100G/200G/4X10G/4X25G 的增强四通道光模块口 <<<PAGE 25>>>等
- **VFL（Virtual Fabric Link）**：ALE 虚拟光纤链路技术，端口可作 VFL 或普通上行（LED 琥珀=VFL）<<<PAGE 23>>>/<<<PAGE 39>>>
- **多千兆（Multi-gigabit）**：2.5G/5G/10G RJ45 端口技术，配 802.3bt 大功率 PoE <<<PAGE 12>>>

## 电源（Ch3）

- **PS-250W-AC（OS6870-BP）**：250W AC 电源（100-240VAC，12V/20.8A 输出，无 PoE 输出）<<<PAGE 48>>>
- **PS-250W-DC（OS6870-BP-D）**：250W DC 电源（-42~-60V/8A 输入）<<<PAGE 49>>>
- **PS-550W-AC-2（OS6870-BPH）**：550W AC 电源（12V/45.8A，V12 机型用）<<<PAGE 50>>>
- **PS-600W-AC-POE-2（OS6870-BPPH）**：600W PoE 电源（54.5V/11A，P 系列用）<<<PAGE 51>>>
- **PS-1200W-AC-POE-2（OS6870-BPPX）**：1200W PoE 电源（54.5V/22.02A；高 PoE 功率需 190-240VAC）<<<PAGE 52>>>
- **PS-2000W-AC-POE-2（OS6870-BPXL）**：2000W PoE 电源（54.5V/36.7A；仅 P24M/P48M）<<<PAGE 53>>>
- **负载分担（Load Sharing）**：双电源均分供电负荷（含 PoE）<<<PAGE 47>>>/<<<PAGE 51>>>
- **电源混插（Mixing wattage）**：同一机箱允许安装不同瓦数电源 <<<PAGE 51>>>
- **Lock Tab（锁片）**：电源就位"咔哒"锁定/按压释放的机构 <<<PAGE 55>>>/<<<PAGE 57>>>
- **Smart on**：电源待机智能开启状态（绿闪 LED 表示）<<<PAGE 48>>>/<<<PAGE 50>>>
- **12VSB**：电源待机输出（12V standby，0.1A）<<<PAGE 48>>>等
- **CBN（Common Bonding Network）**：共同联结网络，DC 设备设计安装环境 <<<PAGE 54>>>
- **Isolated DC Return（DC-I）**：隔离式 DC 回流导体（黑线 return）<<<PAGE 54>>>

## LED 与监控（Ch3）

- **OK LED**：稳绿=诊断与 AOS 启动 OK、闪绿=进行中、稳琥珀=启动失败 <<<PAGE 38>>>
- **VC LED**：稳绿=Master、稳琥珀=Slave、灭=未知/错误 <<<PAGE 38>>>
- **PS LED**：稳绿=电源正常、稳琥珀=单/双电源故障、灭=无电源 <<<PAGE 38>>>
- **GRN (Leaf) LED**：稳绿=省电模式（power saving）、灭=正常模式 <<<PAGE 38>>>
- **VC ID LED**：多灯数值相加等于 VC 单元号 <<<PAGE 39>>>
- **RJ45 四色速率 LED**：绿=10/100/1000、蓝=2.5G、品红=5G、琥珀=10G <<<PAGE 39>>>
- **EMP port**：后部以太网管理端口 <<<PAGE 23>>>等
- **show module / show module long**：槽位基本/详细信息命令 <<<PAGE 58>>>
- **show temperature**：温度监控命令（Current/Range/Danger/Thresh/Status）<<<PAGE 58>>>
- **Warning 阈值**：用户可配温度告警阈值，超限发 trap 业务继续 <<<PAGE 58>>>/<<<PAGE 59>>>
- **Danger 阈值**：出厂固化温度阈值，超限自动关机须手动启动 <<<PAGE 59>>>
- **Dying Gasp**：掉电告别机制（SNMP trap + Syslog + Link OAM PDU 三通道）<<<PAGE 59>>>
- **efm-oam propagate-events dying-gasp**：端口发 Dying Gasp OAM PDU 的使能命令 <<<PAGE 60>>>
- **swlog output socket**：添加 Syslog 服务器命令 <<<PAGE 60>>>
- **snmp station**：配置 SNMP 接收站命令 <<<PAGE 60>>>

## PoE（Ch4）

- **PSE（Power Source Equipment）**：供电设备，检测 PD、可选分级、供电、监控、回缩 <<<PAGE 61>>>
- **PD（Powered Device）**：受电设备（AP/IP 话机/以太网集线器等）<<<PAGE 61>>>
- **802.3bt**：第 4 代 PoE 标准（Type 3/4，Class 5-8：45/60/75/90-99W，4 对线）<<<PAGE 62>>>/<<<PAGE 65>>>
- **PoH**：Power over Harness，配合 `lanpower 4pair` 提供 60/75/95W <<<PAGE 65>>>
- **lanpower slot service**：逐 slot 物理激活/停止 PoE（首次激活唯一途径）<<<PAGE 63>>>/<<<PAGE 65>>>
- **lanpower port admin-state**：单口 PoE 管理开关（仅限重激活/关断，不能首次激活）<<<PAGE 65>>>
- **lanpower power / lanpower slot maxpower**：设单口/整槽功率上限（不预留）<<<PAGE 63>>>/<<<PAGE 66>>>
- **lanpower priority**：设口优先级 low/high/critical（默认 low）<<<PAGE 63>>>/<<<PAGE 67>>>
- **lanpower 4pair / lanpower 8023bt**：开 4 对 60-95W / 开 bt Class 5-8 <<<PAGE 65>>>
- **lanpower slot class-detection**：开 Class 检测（复位全部 PoE 口）<<<PAGE 65>>>
- **lanpower capacitor-detection**：开电容检测（仅老式 IP 话机，不符 IEEE）<<<PAGE 63>>>/<<<PAGE 67>>>
- **lanpower slot priority-disconnect**：开关 priority disconnect（默认启用）<<<PAGE 63>>>/<<<PAGE 69>>>
- **Guard Band**：剩余预算小于口上限/类最大值即拒载新 PD 的机制 <<<PAGE 67>>>/<<<PAGE 68>>>
- **Priority Disconnect**：预算不足时按优先级+物理端口号（1 最高→48 最低）裁决 <<<PAGE 68>>>/<<<PAGE 69>>>
- **show powersupply / show lanpower slot**：电源状态 / PoE 逐口与预算状态命令 <<<PAGE 63>>>/<<<PAGE 64>>>/<<<PAGE 71>>>

## 管理与登录（Ch2）

- **admin/switch**：出厂默认管理员账号/密码 <<<PAGE 18>>>
- **aaa authentication**：解锁会话类型命令族（default/telnet/http/ftp 等逐个解锁）<<<PAGE 19>>>
- **rollover 线**：console 串口反转线缆类型 <<<PAGE 17>>>
- **115200-8N1**：console 默认串口参数（波特率 115200、8 数据位、无校验、1 停止位）<<<PAGE 17>>>
- **system location**：设置交换机物理位置（远程定位用）<<<PAGE 20>>>
- **show system / write memory**：查看系统信息 / 保存配置 <<<PAGE 21>>>
- **WebView**：ALE 内嵌 Web 管理界面（可从 OmniVista 或浏览器启动）<<<PAGE 62>>>

## 安装部件（Ch3）

- **弹簧夹法兰（Spring Clip Flange）**：out 位插 tab、按至"CLICK"入 in 位的免工具机架法兰 <<<PAGE 42>>>/<<<PAGE 43>>>
- **后支架/后支架导轨（Rear Bracket / Rear Bracket Guide）**：机架后部支撑件 <<<PAGE 44>>>
- **橡胶桌脚（Rubber Feet）**：桌面安装四脚垫 <<<PAGE 46>>>
- **盲板（Blank Cover Panel）**：盖空槽位、导气流、护内部件；电源槽安装箭头朝上 <<<PAGE 40>>>/<<<PAGE 41>>>
- **接地 lug（Panduit LCD8-10A-L）**：后部双螺纹孔接地端子，配 8AWG、10-32 3/8" 螺丝、30-60 in-lb <<<PAGE 54>>>/<<<PAGE 57>>>
- **Chassis 温度 vs Ambient 温度**：机箱内部传感器读数 vs 近似室温（前者恒高）<<<PAGE 24>>>等

## 标准与合规（附录 A）

- **UL 62368-1 / IEC 62368-1**：音视频与 IT 设备安全标准 <<<PAGE 76>>>
- **EN 55032 / EN 55035**：EMI 与抗扰度标准 <<<PAGE 77>>>
- **Hi-Pot Test**：IEEE 802.3 耐压测试（全部以太网口 2250VDC）<<<PAGE 77>>>
- **FCC Part 15 Class A**：商用级电磁干扰限值（住宅干扰需自费整改）<<<PAGE 78>>>
- **Class 1M Laser**：开启时有 1M 级激光辐射、勿用光学仪器直视 <<<PAGE 23>>>等/<<<PAGE 79>>>
- **Prop 65**：加州 65 号提案警告（铅化合物）<<<PAGE 75>>>
- **WEEE / RoHS**：欧盟回收指令 / 有害物质限制（中国、台湾表）<<<PAGE 72>>>-<<<PAGE 74>>>
- **CDE（Cable Discharge Event）**：线缆静电放电事件；接线前对地放电 <<<PAGE 15>>>
- **ESD 腕带（Wrist Strap）**：防静电腕带，接触部件前消除人体/环境静电 <<<PAGE 83>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安保措施的维护人员可进入的安装位置 <<<PAGE 83>>>
