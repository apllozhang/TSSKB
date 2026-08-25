# glossary — OmniSwitch 9900 Series Hardware Users Guide（术语表候选）

格式：`- **术语**：解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 机箱（Ch1）

- **OS9907**：11RU 模块化机箱，7 槽（2 CMM+5 NI），32.83kg，23 英寸深 <<<PAGE 5>>>/<<<PAGE 6>>>
- **OS9912**：17RU 模块化机箱，12 槽（2 CMM+10 NI），64.36kg <<<PAGE 11>>>
- **CMM（Chassis Management Module）**：机箱管理模块，管控 NI/CFM/配电；2 槽 1+1 冗余 <<<PAGE 16>>>
- **CFM（Chassis Fabric Module）**：机箱交换矩阵模块，藏于风扇托盘之后、经中板连接；4 槽中 CFM1/2 可用 <<<PAGE 10>>>/<<<PAGE 20>>>
- **中板（Mid-plane）**：CFM 与机箱连接的背中板结构（NI 走 backplane）<<<PAGE 20>>>
- **NI（Network Interface）模块**：网络接口模块，装前面板槽位（9907 有 3-7、9912 有 3-12）<<<PAGE 7>>>/<<<PAGE 13>>>
- **VC-of-2**：两台 OS9907 机箱虚拟化为一台虚拟机箱的配置 <<<PAGE 22>>>
- **N+1 冗余**：4 电源负载分担/3 风扇托盘冗余设计 <<<PAGE 8>>>/<<<PAGE 28>>>
- **铝头拇指螺丝**：模块固定螺丝新形态，替代紫色塑料头，机械性能相同 <<<PAGE 6>>>/<<<PAGE 12>>>
- **Wrist Strap Grounding Connector**：机箱前/后部 ESD 腕带接地点 <<<PAGE 8>>>/<<<PAGE 9>>>

## CMM 与 CFM（Ch1）

- **OS99-CMM**：初代管理模块，2×40G QSFP+ 上行，功耗 64W，仅 9907 支持 <<<PAGE 16>>>
- **OS99-CMM2**：新一代管理模块，4×100G QSFP28 上行/VFL，74W，需 AOS ≥8.10R2，不可与 CMM 混插 <<<PAGE 17>>>
- **Micro-USB console**：CMM 上的第二 console 口，需安装驱动 <<<PAGE 16>>>/<<<PAGE 17>>>
- **OS9907-CFM / CFM2**：9907 交换矩阵（2.56T / 12.8T 每块，119W；CFM2 需 AOS ≥8.9R1）<<<PAGE 20>>>
- **OS9912-CFM**：9912 交换矩阵（25.6T 每块，222W）<<<PAGE 21>>>
- **PRI LED**：CMM 主备状态灯（稳绿=主/闪绿=备/稳黄=停运/闪黄=升级中）<<<PAGE 18>>>
- **FAB LED**：CFM 状态灯（稳绿=正常/稳黄=降级运行/闪黄=CFM 电源或 PCIe 上报失败）<<<PAGE 18>>>
- **五灯同闪（PCIe link failure）**：PRI/VC/FAB/PS/TEMP 同时闪黄=全部 CFM PCIe 硬链路失效 <<<PAGE 18>>>

## NI 模块（Ch1）

- **OS99-XNI-48**：48 口 1/10GBaseT 模块，402W <<<PAGE 23>>>
- **OS99-XNI-U48**：48 口 1/10G SFP+ 模块，305W（slot2 只活 8 口）<<<PAGE 23>>>/<<<PAGE 7>>>
- **OS99-GNI-48**：48 口 10/100/1000BaseT + 2×10G，56W <<<PAGE 23>>>
- **OS99-GNI-P48**：48 口千兆 PoE 模块（前 8 口 HPoE 75W），54W（不含 PD）<<<PAGE 24>>>
- **OS99-GNI-U48**：48 口 1G SFP 模块，70W <<<PAGE 24>>>
- **OS99-XNI-P48Z16**：32 口 1/10G at PoE + 16 口多千兆 at PoE（前 8 口 HPoE），402W；不支持 9912 <<<PAGE 24>>>
- **OS99-XNI-P24Z8**：16+8 口 PoE 组合模块，187W；不支持 9912 <<<PAGE 25>>>
- **OS99-XNI-U24**：24 口 1/10G SFP+ 模块，153W <<<PAGE 25>>>
- **OS99-CNI-U8**：8 口 10/25/40/100G QSFP28 模块，117W <<<PAGE 25>>>
- **OS99-CNI-U20**：20 口 100G QSFP28 模块（13-20 口支持 splitter），314W <<<PAGE 26>>>
- **OS99-XNI-UP24Q2**：12×SFP+ +12×多千兆 HPoE(75W) +2×QSFP+，117W；不支持 9912 <<<PAGE 26>>>
- **OS99-XNI-U12Q**：12×SFP+ +1×QSFP+，117W；不支持 9912 <<<PAGE 26>>>
- **HPoE 口**：PoE 模块前 8 口、面板有 "HPoE" 标注、支持 75W <<<PAGE 24>>>
- **Speed LED（NI）**：模块最大端口速率指示灯 + HW/SW 心跳状态（稳绿=HW OK/闪绿=SW 心跳/稳黄=SW 故障）<<<PAGE 27>>>

## 电源与风扇（Ch1/Ch2/Ch4）

- **OS99-PS-A**：AC 电源（100-240V；输出 1200W/21.4A 或 3000W/53.5A 两档），热插拔，System+PoE <<<PAGE 29>>>
- **OS99-PS-D**：DC 电源（-40~-72VDC/75A；输出 2500W/44.6A@56V），热插拔 <<<PAGE 30>>>
- **分路保护额定值**：每电源建议 30A（AC）/110A（DC）断路器 <<<PAGE 29>>>
- **FCI 10080598-2ED0006LF**：DC 电源要求的 4P PWRBLADE 专用连接器 <<<PAGE 31>>>
- **10AWG**：DC 供电双铜导体线规 <<<PAGE 30>>>
- **AHJ（Authority Having Jurisdiction）**：有管辖权的地方电气机构（DC 线 >3m 时咨询）<<<PAGE 31>>>
- **风扇托盘（Fan Tray）**：3 件常驻、N+1 冗余、仅前→后气流；9907 每托 3 扇、9912 每托 5 扇 <<<PAGE 28>>>

## 安装与登录（Ch2）

- **三人机架作业**：两人抬一人拧（"Use two additional people"）<<<PAGE 36>>>
- **锁杆（Lock Levers）**：CFM/NI 模块闭锁机构（90 度全闭锁定）<<<PAGE 38>>>/<<<PAGE 42>>>
- **9600-8N1**：console 默认串口参数（RJ45 或 Micro-USB）<<<PAGE 44>>>
- **EMP 线缆规则**：接交换机用直通线、接计算机用交叉线 <<<PAGE 45>>>
- **EMP 默认地址**：192.168.1.1/255.255.255.0；改址命令 `ip interface emp` <<<PAGE 46>>>
- **admin/switch**：出厂默认账号/密码 <<<PAGE 46>>>
- **aaa authentication**：解锁会话类型命令族 <<<PAGE 47>>>
- **show chassis / Power Left**：机箱信息与可用功率预算查看 <<<PAGE 49>>>
- **DB9-RJ45 Connector**：随箱附带的 console 转接头 <<<PAGE 34>>>

## PoE（Ch3）

- **lanpower slot service**：逐 slot 物理激活/停止 PoE（首次激活唯一途径）<<<PAGE 50>>>/<<<PAGE 52>>>
- **lanpower power / lanpower slot maxpower**：单口/整槽功率上限（slot 默认 1800W；不预留）<<<PAGE 50>>>/<<<PAGE 53>>>
- **lanpower priority**：口优先级 low/high/critical（默认 low）<<<PAGE 50>>>/<<<PAGE 54>>>
- **lanpower capacitor-detection**：电容检测（仅老式 IP 话机、不符 IEEE、默认关）<<<PAGE 50>>>/<<<PAGE 54>>>
- **lanpower slot priority-disconnect**：优先级断电裁决开关（默认启用）<<<PAGE 50>>>/<<<PAGE 55>>>
- **lanpower power-rule**：按日期/时间的 PoE 供电规则命令 <<<PAGE 53>>>
- **Priority Disconnect**：预算不足时按优先级+物理端口号（48 最高→1 最低，与接入平台相反）裁决 <<<PAGE 55>>>
- **Class 检测**：Class 0-4 分级限功率；默认关；开启复位全部 PoE 口 <<<PAGE 51>>>/<<<PAGE 52>>>
- **show powersupply / show lanpower slot**：电源/PoE 逐口与预算状态命令 <<<PAGE 50>>>/<<<PAGE 51>>>
- **HPoE（75W）**：前 8 口 75000mW 大功率 PoE；at 口 30000mW <<<PAGE 50>>>

## 热插拔（Ch4）

- **热插拔节律**：拆件间隔 30 秒、插件间隔 5 分钟+LED 无错 <<<PAGE 63>>>
- **同类替换（like modules）**：NI 模块热换只能换同型号 <<<PAGE 63>>>
- **CFM 120 秒窗口**：CFM 热换须在 120 秒内完成 <<<PAGE 63>>>

## 标准与合规（附录 A）

- **UL 60950 / IEC 60950-1**：IT 设备安全标准 <<<PAGE 64>>>
- **IEEE 802.3 Hi-Pot + 1.5kV surge**：铜口耐压与浪涌要求 <<<PAGE 64>>>
- **FCC Part 15 Class A / CISPR 22**：Class A 电磁干扰限值 <<<PAGE 64>>>
- **CLASS 1 LASER PRODUCT**：CMM/NI 模块面板激光产品标识 <<<PAGE 16>>>等
- **Prop 65 / WEEE / RoHS（中国、台湾）**：加州警告/欧盟回收/有害物质限制 <<<PAGE 65>>>-<<<PAGE 67>>>
- **Panduit LCD8-10AL / CT-940CH**：接地 lug 及压接工具型号，8AWG、30-60 in-lb <<<PAGE 71>>>
- **22AWG**：机框接地与 DC 回流引线线规 <<<PAGE 70>>>
- **ESD 腕带**：防静电腕带（电源装好并接接地插座才有效）<<<PAGE 72>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安保措施的维护人员可进入 <<<PAGE 71>>>
- **Tmra**：最大额定环境温度（封闭机架折减依据）<<<PAGE 32>>>
