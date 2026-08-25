# counter-examples — 容量限制/不支持项（OmniSwitch AOS 8.10R4 Specifications Guide）

格式：编号 X# ｜ 限制要点 ｜ 页码

## VC 组网限制

- **X1** 6920 与 OS9912 机箱完全不支持 VC；OS9907 仅 VC-of-2 且依赖 CMM/CFM 组合 <<<PAGE 23>>>/<<<PAGE 24>>>
- **X2** VC 混搭白名单只有这些：6900-V72/C32(E)/X48C6/T48C6/V48C8/X24C2/T24C2 之间（最多 6）；X48C4E 混上述型号需 mixed VFL 模式；6860+6865 可混；6465-P6/P12/P28/6465T 可混（用 1G SFP）；6360 10 口型仅 4 成员（SFP 口）。**OS6860N 与 OS686x 禁止混 VC**："OS6860N and OS686x models should not be mixed in a Virtual Chassis." <<<PAGE 24>>>
- **X3** MAC Learning Mode 在 OS6900 VC 上不支持 <<<PAGE 24>>>
- **X4** VFL 在 4X25G splitter 口上必须两侧 inter-frame gap=13，否则 CRC <<<PAGE 24>>>
- **X5** 1588v2 只支持 VC-of-1（跨 VC 不支持）；6570M/6860/6865/6870 不支持 10/100 半双工（CSMA/CD）<<<PAGE 29>>>
- **X6** VC 的 ARP 容量短板效应：6900 VC 的 ARP 总量=最低能力模块的值："Equal to capacity of module with lowest number of supported ARPs." <<<PAGE 42>>>

## 平台特性缺口（N/S 矩阵要点）

- **X7** OpenFlow 除 OS6860 外全部 N/S <<<PAGE 22>>>
- **X8** SIP Snooping 仅 OS6860 支持 <<<PAGE 41>>>
- **X9** MACsec 平台缺口：6360、6865、6900（除 X48C4E）、6920 不支持；需站点许可 <<<PAGE 29>>>
- **X10** Fast/Perpetual PoE 仅 6360/6860/6860N/6865/6870 支持（6575 无）<<<PAGE 29>>>
- **X11** Ethernet OAM(802.1ag/Y.1731) 不支持 OS6360 与 OS9900 <<<PAGE 73>>>
- **X12** Application Fingerprinting 全平台"Currently not supported"（规格表保留但无实现）<<<PAGE 64>>>
- **X13** WRED 全平台 N/S（8.6R2 起移除的遗留）<<<PAGE 58>>>
- **X14** IPsec 仅 6860/6865 支持，且只有 Transport 模式（无 Tunnel 模式）<<<PAGE 47>>>
- **X15** BFD 不支持 IPv6 协议、不支持 Demand 模式 <<<PAGE 49>>>
- **X16** SLB 仅 6860/6860N/6865/6870/6900-X 支持 <<<PAGE 55>>>
- **X17** PIM 与 DVMRP 不能在同一接口启用 <<<PAGE 84>>>
- **X18** MBR（组播边界路由）不支持 6360/6465/6560/6570M <<<PAGE 86>>>
- **X19** MRP 仅 6465/6575/6865 三平台 <<<PAGE 76>>>
- **X20** CPE Testhead 仅 6465/6560/6570M/6575 <<<PAGE 74>>>
- **X21** DHL 在 6900-V72/C32 与 6920 不支持 <<<PAGE 36>>>
- **X22** UDLD 在 6900-V72/C32 与 9900 不支持（X48C4E 除外）<<<PAGE 30>>>

## 容量上限（规划红线）

- **X23** 每口 untagged VLAN 只能 1 个（默认 VLAN）；tagged 每 4093；VLAN 总数 4094/VC <<<PAGE 31>>>
- **X24** PVLAN 每端口/聚合成员上限：6560/6570M/6575/6920=256，6860 系/6870/6900=1；主 VLAN 下每口共存 secondary VLAN 仅 1 <<<PAGE 31>>>
- **X25** STP per-VLAN 实例：多数平台 100（6900/6920/9900 128）；Flat 模式 MSTI 16（另加 MSTI 0/CIST）<<<PAGE 32>>>
- **X26** HA VLAN：6570M/6575/6860/6860N/6865/6870=16，6865N=32，6360/6465/6560/6920/9900 不支持 <<<PAGE 32>>>
- **X27** MVRP VLAN 上限：6360/6465=256，其余 512 <<<PAGE 38>>>
- **X28** ERP 每节点 64 环、每环推荐 16 节点、WTR 1-12 分钟、guard 1-200 厘秒；dual end blocking 不支持 <<<PAGE 37>>>
- **X29** LLDP 每口 network policy 8；每 VC 8-32 <<<PAGE 41>>>
- **X30** 6465 路由面极小：路由接口 24、硬件路由 32、ARP 256、ECMP 4——只能当接入交换 <<<PAGE 42>>>/<<<PAGE 43>>>
- **X31** 6360 静态路由仅 256（黑洞路由计入）；IPv6 接口 4、IPv6 静态路由 4 <<<PAGE 43>>>/<<<PAGE 46>>>
- **X32** IPv6 单播地址每接口 1 个（6575 需 AR 许可可 50）<<<PAGE 46>>>
- **X33** RIP 规模：接口 8-16、对等体 8-100、路由 128-10K；6560/6570M 路由 256（ECMP 下 1024）<<<PAGE 48>>>
- **X34** 认证服务器上限：单 authority 4（6900/6920 8）、多 authority 4/8 <<<PAGE 60>>>
- **X35** UNP 用户 VC 上限两种语义：多数平台=每机箱×成员数（脚注 1），但 6860 系/6900/6920 为 VC 封顶不随成员增加（脚注 2）："The maximum number of users per VC does not increase with additional chassis." <<<PAGE 61>>>
- **X36** Captive Portal 同时 Web 登录均值 40；profile 8；认证/计费服务器各认证类型 4 <<<PAGE 62>>>
- **X37** L2 GRE Access 隧道多数平台仅 1 条（6560/6570M 为 8）——BYOD 隧道规划瓶颈 <<<PAGE 63>>>
- **X38** 端口监控会话仅 1；镜像+监控合并会话 2-7 <<<PAGE 66>>>
- **X39** RMON 只有 4 基础组，Host/Matrix/Filter/捕获等 RMON2 功能必须外置探针 <<<PAGE 69>>>
- **X40** VLAN Stacking service 仅 4 个；SAP profile 一旦分配优先级/带宽，8K 降到 1K <<<PAGE 71>>>
- **X41** PPPoE-IA Circuit/Remote-ID 最长 63 字节、选项 5 个 <<<PAGE 75>>>
- **X42** 自动远程配置（RCD）限制：ISSU 与 IPv6 不支持；uboot/miniboot/FPGA 升级不支持；FTP/SFTP 用户名 15 字符；DHCP 租约尝试 6 次；OK LED 过程中闪琥珀 <<<PAGE 25>>>
- **X43** TCAM profile 切换必须 reload 生效——生产变更要停机窗口 <<<PAGE 87>>>
- **X44** 6570M/6575 的 VRF、OSPF/OSPFv3/IS-IS、BGP 均需 Advanced Routing license；6560 的 OSPF/BGP 同 <<<PAGE 44>>>/<<<PAGE 79>>>-<<<PAGE 82>>>
- **X45** 6575 各项 IPv6 规模显著小于 6570M（接口 4 vs 16、静态路由 512 同但主机 3K、6to4 隧道 1）且依赖 AR 许可 <<<PAGE 45>>>
- **X46** OSPF 区域上限：6560=2（AR 许可下）、6860/6870/6570M=4-8、6900-X/9900=10-15——6560 只能单区域+骨干 <<<PAGE 79>>>
- **X47** DHCPv6 snooping VLAN 数全平台 64；guard VLAN 64 <<<PAGE 51>>>/<<<PAGE 52>>>
- **X48** linkagg 聚合成员口 8-16，9900 的 ID 0/126/127 保留不可用 <<<PAGE 35>>>
- **X49** SPB MTU 在 6860 系"not configurable at this time"（固定 9K）<<<PAGE 34>>>
- **X50** SPB RFP 域最多 8（且与其它 Ethernet OAM 域共享预算，已有 OAM 域时更少）<<<PAGE 34>>>

---
合计：50 条（X1-X50）。
