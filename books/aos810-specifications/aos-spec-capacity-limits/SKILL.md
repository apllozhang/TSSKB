---
name: AOS 8 容量红线速查（VC/链路/SPB/VXLAN/EVPN/路由/DHCP/组播/QoS/接入）
description: 规划 OmniSwitch AOS 8 网络时核对各特性容量上限——SPB I-SID/BVLAN、VXLAN VTEP/VNI、EVPN 主机、OSPF/IS-IS/BGP/VRF、DHCP Snooping、IPMS 组播流、QoS 策略、UNP/AG 用户、镜像监控会话等规格红线时使用。
source_book: OmniSwitch AOS Release 8 Specifications Guide (8.10R4)
---

## R（触发场景）
- 网络设计/扩容评审，核对业务规模是否超平台规格
- SPB/VXLAN/EVPN fabric 规模画像（I-SID/VTEP/VNI/主机数）
- 路由协议规模评估（OSPF 区域/LSDB、BGP 对等/路由、VRF 实例）
- 接入侧用户数（UNP/AG/QMR/Captive Portal）、DHCP Snooping 条目、组播流数
- 监控会话（镜像/sFlow/RMON）资源分配

## I（核心理念)
本手册是"能到多少"的权威底座：规格表按"特性 × 13 平台"给最大值，配合 F2 三梯队与 F4 VC 语义解读。关键规律：许多容量互相反比（DHCP Snooping 条目按 VLAN 数反比缩放，P33）；VC 场景注意脚注（UNP 用户脚注 1/2 两种语义，X35）；组播接口有全局预算（PIMv4+PIMv6+DVMRP 合计 384 接口，P31）；EVPN 主机数与生成路由数有换算（10K 主机生成 20K RT2，P23）。

## A1（决策框架）
1. **骨干选 SPB 还是 VXLAN/EVPN**：SPB（BVLAN 16/I-SID 512-8K 按平台，P19/P20）vs VXLAN（段 1600 万/SAP 8K/VTEP 500/VNI 4K/组播组 500，P22）vs EVPN on 6900（主机 10K/业务 50/VRF 4/前缀路由 500/接入连接 140，P23）
2. **路由规模定档**：硬件路由 6360 256 → 6900-X RM 312K；IPv6 双轨 128-bit/64-bit（P24/P26）；超限走软件路由（P16）
3. **VRF 档位**：MAX profile（64/VC）与 LOW profile（128/VC）二选一；每 VLAN 仅 1 VRF；OSPF/RIP VRF 实例 16、BGP 32（P27）
4. **接入侧数用户**：AG 用户系统级 320-1K、QMR 隔离 256-1K、UNP profile 4K/VC（P40）；注意 X35 的 VC 脚注语义
5. **监控资源预留**：镜像会话 2-7、监控会话仅 1、N-to-1 128:1（P43）；RMON 仅基础 4 组（X39）

## A2（操作步骤）·容量红线速查
- **SPB**：ISIS-SPB 实例每 VC 1；BVLAN 16（RN 建议收敛到 4）；I-SID 6570M/6575=512、6860 系=2K、6900-X48C6 等=8K、9900=1K；每 I-SID VLAN/SVLAN 2K-4K；SPB MTU 9K（6860 系当前不可配）（P19/P20/X49）；RFP 域最多 8 且与其它 Ethernet OAM 域共享预算（X50，<<<PAGE 34>>>）
- **VXLAN/EVPN**：见 P22/P23（<<<PAGE 39-40>>>）；Fabric VPN 4/VRF 对应 1
- **链路层**：PVLAN 每端口/聚合成员 6560/6570M/6575/6920=256、6860 系/6870/6900=1；主 VLAN 下每口共存 secondary VLAN 仅 1（X24）；STP per-VLAN 实例多数 100（6900/6920/9900 128）、Flat 模式 MSTI 16（X25）；HA VLAN 6570M/6575/6860 系/6870=16、6865N=32、6360/6465/6560/6920/9900 不支持（X26）；MVRP VLAN 6360/6465=256、其余 512（X27）；ERP 每节点 64 环、每环推荐 16 节点（X28）
- **IP/路由**：IP 接口每系统 128-4K（6465 仅 24）、每 VLAN 路由接口 8-32（P24）；6360 静态路由仅 256（黑洞计入）、IPv6 接口 4、IPv6 静态路由 4（X31）；IPv6 单播地址每接口 1（6575 需 AR 许可 50）（X32）；RIP 接口 8-16、路由 128-10K（6560/6570M 256，ECMP 下 1024）（X33）；OSPF 区域 2-15、LSDB 1K-100K、路由 512-64K；IS-IS 区域 3、L1/L2 邻接每口 70、路由 24K；BGP 对等 32-512（每 VRF 32）、路由 2K-256K（P29）；BFD 每机箱 32/每 VC 100，IPv6 不支持、仅异步 Echo（P30/X15）
- **DHCP**：Snooping 条目反比缩放（6860 系 32 VLAN×223 客户端 / 4 VLAN×251；端口级 253-254）（P33）；内部 Server 租约 8000、租约文件 375K（P34）；DHCPv6 snooping VLAN 数全平台 64、guard VLAN 64（X47）
- **组播**：IPMS 流接入 1K、6860 系 12K-40K、6900-X 40K、9900 128K；v6 对应 1K-128K（P37）；PIM+DVMRP 接口合计 384、RP 100、BSR 1（P31）
- **QoS**：策略规则/条件/动作三值相等 128-4K（6870 依 TCAM profile 2K/4K）；每口 8 CoS 队列；策略列表 32；WRED 全平台 N/S（P38/X13）
- **接入**：认证服务器单 authority 4（6900/6920 8）、AG 每认证类型 4 认证+4 计费（P39/X34）；Captive Portal 同时登录均值 40、profile 8（X36）；L2 GRE Access 隧道多数平台仅 1（6560/6570M 为 8）——BYOD 规划瓶颈（X37）；LPS 每口学习 1000/过滤 100/范围 8、聚合口不适用（P42）
- **OAM/监控**：OAM MD 8/MA 128/MEP 256、最小 CCM 100ms（P48）；SAA 128 会话、SPB SAA 每 BVLAN 128（P50）；sFlow 实例 2（P44）

## E（实证案例）
- 本书为纯规格手册，无配置案例；"场景"即容量评审：按 A2 红线逐项核对设计方案，超线项回到 aos-spec-platform-tiers 换梯队/profile 或回到配置手册做架构调整

## B（反例/坑）
- VC 的 ARP 容量短板效应：6900 VC 总量=最低能力模块的值（X6，<<<PAGE 42>>>）
- UNP 用户 VC 上限两种语义：多数平台=每机箱×成员数（脚注 1），6860 系/6900/6920 为 VC 封顶不随成员增加（脚注 2）（X35，<<<PAGE 61>>>）
- 端口监控会话仅 1；镜像+监控合并会话 2-7（X38，<<<PAGE 66>>>）
- RMON 只有 4 基础组，Host/Matrix/Filter/捕获等 RMON2 功能必须外置探针（X39，<<<PAGE 69>>>）
- VLAN Stacking service 仅 4 个；SAP profile 一旦分配优先级/带宽，8K 降到 1K（X40，<<<PAGE 71>>>）
- OSPF 区域上限：6560=2（AR 许可下）、6860/6870/6570M=4-8——6560 只能单区域+骨干（X46，<<<PAGE 79>>>）
- 6570M/6575 的 VRF、OSPF/OSPFv3/IS-IS、BGP 均需 Advanced Routing license；6560 的 OSPF/BGP 同（X44，<<<PAGE 44>>>/<<<PAGE 79-82>>>）
- BFD 不支持 IPv6 协议、不支持 Demand 模式（X15，<<<PAGE 49>>>）；SLB 仅 6860/6860N/6865/6870/6900-X（X16）；MBR 不支持 6360/6465/6560/6570M（X18）；MRP 仅 6465/6575/6865（X19）

## 来源
OmniSwitch AOS Release 8 Specifications Guide Ch2 Network Configuration（<<<PAGE 27-76>>>）、Ch3 Advanced Routing（<<<PAGE 77-86>>>）。条目来源：principles P16/P19-P31/P33-P40/P42-P44/P48/P50；counter-examples X6/X15/X16/X18/X19/X24-X28/X31-X33/X34-X40/X44/X46/X47-X50；frameworks F2/F4。
