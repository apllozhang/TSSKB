# principles — OmniSwitch AOS 8.10R4 Specifications Guide（规格机制候选）

格式：编号 P# ｜ 规格要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## 平台资源基线（Ch1）

- **P1** 13 平台镜像文件名体系：6360=Nosa.img、6465/6560=Nos.img、6570M=Wos.img、6575=Dos.img、6860/6865=Uos.img、6860N=Uosn.img、6870=Kaos.img、6900=Yos.img、6920=Ypos.img、9900=Mhost.img+Mos.img+Meni.img；VC 配置文件 vcboot.cfg/vcsetup.cfg <<<PAGE 14>>>
- **P2** 管理会话并发上限全平台一致：Telnet 6、SSH 8、HTTP(WebView) 4；SSH 公钥支持 Password/DSA/RSA/ECDSA <<<PAGE 14>>>
- **P3** 文件管理基线：文件传输 FTP(v4/v6)/SFTP/SCP/TFTP；FTP 客户端仅 IPv4；并发 FTP/SFTP 会话 4；文件/目录名最长 255 字符（作 RUNNING 目录时 30）；名称区分大小写、除 '/' 外任意 ASCII； Vi 编辑器 <<<PAGE 15>>>
- **P4** 内存/Flash 平台矩阵：6360=1G/1G、6570M=2G/8G、6575=2G/4G、6860N=4G/16G、6870=8G/32G、6900-X 系列=8G/32G（V48C8/C32E=16G/64G 物理 32G 分区）、6920=32G/64G、9900=16G（9907 2G Flash/9912 32G）<<<PAGE 16>>>
- **P5** USB 灾难恢复按平台用对应 rescue 镜像（Narescue/Nrescue/Wrescue/Drescue/Urescue/Mrescue.img），6860N/6870/6900/6920 为 ONIE-based；ALE 认证 U 盘必须 FAT32、目录名小写 <<<PAGE 17>>>
- **P6** 用户数据库全平台统一：用户名最长 63、口令最长 30、本地账户最多 50；WebView 统一 2.0 <<<PAGE 19>>>
- **P7** SNMPv3 安全栈：认证 SHA/MD5、加密 DES/AES，请求类型覆盖非认证/认证/加密三档 Sets/Gets/Get-Nexts；v1/v2 仅 community 无加密 <<<PAGE 20>>>
- **P8** Web Services：HTTP/HTTPS + Python API，响应 XML/JSON，最大 4 会话；内嵌 Python 3；AMS 全平台支持 <<<PAGE 21>>>
- **P9** OpenFlow 仅 6860 支持：Normal/Hybrid(API) 模式、版本 1.0/1.3.1、每逻辑交换机 3 控制器、最多 3 逻辑交换机（Hybrid 1）、流表 1535、MAC 表 48K、TCP 6633、支持 VC <<<PAGE 22>>>
- **P10** NTP：RFC 5905（NTPv4），密钥文件 /flash/network，每客户端最多 12 台服务器、最多 512 关联 <<<PAGE 26>>>

## VC 与链路（Ch1-2）

- **P11** VC 成员数平台档：6360 24/48 口=8（10 口=4）、6465=4、6560/6570M/6860/6865/6870=8、6575=4、6900-X=6、9907=2、9912/6920 不支持；chassis-id/priority/group 范围 1-8/0-255/0-255 <<<PAGE 23>>>
- **P12** VFL 规格三档：多数平台每机箱 2 peer、每 VFL 8 成员口、VFL id 0-1；6900 每 5 peer、16 成员口、VFL id 0-4；控制 VLAN 2-4094、hello 间隔 1-65535 <<<PAGE 23>>>
- **P13** VC 最大值语义：文档中的 maximum 对整个 VC 生效而非单机，除非另行说明："Any maximum limitation values documented apply to the entire Virtual Chassis and not to each individual switch unless stated otherwise." <<<PAGE 12>>>
- **P14** 最大帧长两级：10/100M 口 1553 字节、1G/10G/40G/100G 口 9216 字节（巨帧）；EEE/802.3az 全平台 <<<PAGE 29>>>
- **P15** MAC 容量三模式体系（SM/RM/ER）：集中式 MAC 学习规模随 Switch/Router/Edge-router profile 变化——如 6900-X48C6 228K(SM)/128K(ER)/32K(RM)，9900 128K(SM)/80K(ER)；数值为硬件指示值，随路由配置浮动 <<<PAGE 30>>>
- **P16** 路由软超载机制：硬件路由超限时旧的不常用路由移入软件、活跃路由保硬件，总路由量取决于内存——超出即部分流量走软件路由："Exceeding the maximum hardware routes will result in some traffic being routed in software." <<<PAGE 43>>>
- **P17** 聚合规模梯度：6360/6465/6560=32 组×8 口；6570M 静态 32/LACP 96；6860 系=128×16；6870=252 组；6920=253 组×16；9900 ID 0/126/127 保留 <<<PAGE 35>>>/<<<PAGE 36>>>
- **P18** DHL 每系统仅 1 会话（V72/C32、6920 不支持） <<<PAGE 36>>>

## SPB/VXLAN/EVPN（Ch2）

- **P19** SPB 实现为 SPBM(MAC-in-MAC)+IP over SPBM；ISIS-SPB 实例每 VC 1 个；BVLAN 16（但 Release Notes 建议 Auto Fabric 默认收敛到 4）；ECT 算法 1-16 可选 <<<PAGE 33>>>
- **P20** I-SID/SAP 规模梯队：6570M/6575=512、6860 系=2K、6900-X48C6 等=8K（X/T24C2 2K）、9900=1K；每 I-SID VLAN/SVLAN 数 2K-4K；SPB MTU 9K（6860 系当前不可配） <<<PAGE 33>>>/<<<PAGE 34>>>
- **P21** SPB L3 两种路由形态：Inline Routing（6570M/6575/6860N/6900-X/9900）与 External Loopback Routing（6860/6865/6860N/6900-X48C6 类/9900），平台互补 <<<PAGE 34>>>
- **P22** VXLAN（6860N/6870/6900）：段 1600 万、业务实例/SAP 8K、VTEP 500、VNI 4K、组播组 500（BIDIR-PIM）、UDP 目的端口可配 8 个（默认 4789）、每接入口 VLAN 范围 SAP 8 个 <<<PAGE 39>>>
- **P23** EVPN（6900）规模画像：主机 10K（生成 20K RT2）、业务 50（全 IRB）、VRF 4、Fabric VPN 4、前缀路由 500、组播组 200（OISM+PEG 全启用）、接入连接 140（100 单归属+40 多归属）；RFC 7432/9135/9136/9161/9251/9625 <<<PAGE 40>>>

## IP/IPv6/路由（Ch2-3）

- **P24** IP 接口规模：每系统 128-4K（6465 仅 24）；每 VLAN 路由接口 8-32；硬件路由从 6360 的 256 到 6900-X RM 312K 梯度分布（SM/RM/ER 三态） <<<PAGE 42>>>
- **P25** GRE/IPIP 隧道：每 VC 127（6570M 需 AR 许可）；IPv6 配置隧道 255、6to4 隧道 1 <<<PAGE 42>>>/<<<PAGE 45>>>
- **P26** IPv6 硬件路由 128-bit/64-bit 双轨：如 6900-X48C6 RM 156K(128-bit)/64K(64-bit)；IPv6 主机（ND）SM/RM/ER 三态（如 6900-X 32K SM/24K ER/8K RM）<<<PAGE 46>>>
- **P27** VRF 两档 profile：MAX profile（64 实例/VC，6900-X 达 28-300 LOW 混布）与 LOW profile（128/VC）；每 VLAN 仅 1 VRF；OSPF/RIP VRF 实例 16、BGP 32 <<<PAGE 44>>>
- **P28** IPsec 仅 6860/6865：ESP 加密 NULL/3DES-CBC/AES-CBC(128/192/256)，AH 认证 HMAC-SHA1/MD5/AES-XCBC/SHA256/384/512，仅 Transport 模式，策略优先级 1-1000、规则 index 1-10、SPI 256-999999999 <<<PAGE 47>>>
- **P29** 路由协议规模基线：OSPF 区域 2-15、接口 8-200、LSDB 1K-100K、路由 512-64K（9900）；IS-IS 区域 3、L1/L2 邻接每口 70、路由 24K（L1 12K+L2 12K）；BGP 对等 32-512（每 VRF 32）、路由 2K-256K（9900）<<<PAGE 79>>>-<<<PAGE 82>>>
- **P30** BFD 会话：每机箱 32 / 每 VC 100；联动 BGP/OSPF/VRRP 远地址跟踪/静态路由；IPv6 协议不支持；仅异步 Echo 模式 <<<PAGE 49>>>
- **P31** 组播接口预算：PIMv4+PIMv6+DVMRP 合计 384 接口；PIM 与 DVMRP 不能同接口；RP 100、BSR 1、SSM v4 段 232.0.0.0/8、v6 段 FF3x::/32 <<<PAGE 84>>>/<<<PAGE 85>>>

## DHCP/接入/安全（Ch2）

- **P32** DHCP relay 目标数两档：接入级平台 256、汇聚级（6860 起）1536；UDP relay 服务每 VC 12-30；DHCPv6 relay 每 relay 接口 5 个目的地、snooping VLAN 64 <<<PAGE 50>>>/<<<PAGE 51>>>
- **P33** DHCP Snooping 源过滤条目按 VLAN 数反比缩放：如 6860 系 32 VLAN×223 客户端 / 4 VLAN×251 客户端；端口级 253-254 客户端；VC 的 VLAN 级条目=单机值×VC 成员数 <<<PAGE 51>>>
- **P34** 内部 DHCP Server：租约 8000、租约文件 375K；静态 BootP/静态 DHCP/动态 DHCP 三种分配；v4 配置 dhcpd.conf/pcy/dhcpsrv.db、v6 同构三件套 <<<PAGE 53>>>
- **P35** VRRP：v2+v3 虚拟路由器 255、每实例 16 IP（全平台一致）<<<PAGE 54>>>
- **P36** SLB（6860/6865/6870/6900-X）：32 集群×32 物理服务器；L3 按目的 IP、L2 走 QoS 条件；健康检查 Ping+链路；高可用=硬件 failover/VRRP/CMM 冗余 <<<PAGE 55>>>
- **P37** 组播流（IPMS）规模梯队：接入 1K、6860 系 12K-40K（6860N 40K）、6900-X 40K、9900 128K；v6（MLD v1/v2）对应 1K-128K <<<PAGE 56>>>/<<<PAGE 57>>>
- **P38** QoS 规模：策略规则/条件/动作三值相等（128-4K，6870 依 TCAM profile 2K/4K）；组数 1023-2047；每组条目 128-1024（service 组 256）；每口 8 CoS 队列；QSP 2-4（6920 NBDC-2/DCB-4）；策略列表 32（含默认）、每 UNP 1 个；WRED 全平台 N/S <<<PAGE 58>>>
- **P39** AAA 服务器：认证服务器单/多 authority 模式各 4-8；AG 每认证类型（MAC/802.1X/CP）4 认证+4 计费服务器；AAA profile 8、CP profile 8；BYOD 服务器 CPPM/UPAM；COA RFC 3576 支持限 ClearPass <<<PAGE 60>>>/<<<PAGE 62>>>
- **P40** UNP/AG 用户规模：AG 用户系统级 320-1K（6900 每 NI 1K/VC 2K）；QMR 隔离 256-1K；Captive Portal 同时登录均值 40；UNP profile 4K/VC（6920 2K）；UNP 用户每机箱 80-2K、每 VC 求和或封顶（依平台脚注 1/2）<<<PAGE 61>>>/<<<PAGE 62>>>
- **P41** L2 GRE 隧道：Access 隧道多数平台 1（6560/6570M 8）；Aggregation 隧道 6860 系 2K（6900 8K、9900 1K）；mDNS/SSDP GRE 仅 IPv4 <<<PAGE 62>>>/<<<PAGE 63>>>
- **P42** LPS 规则：每口学习 MAC 1000、过滤 MAC 100、MAC 范围 8；聚合口与 trunk 聚合口不适用 <<<PAGE 65>>>
- **P43** 端口镜像/监控会话：镜像会话 2-7、监控会话 1；合并上限与镜像会话同值；N-to-1 镜像 128:1；镜像目的地每会话 1-2（9900 128）；RPMIR 每会话 1 VLAN；监控文件格式 ENC（Sniffer）<<<PAGE 66>>>/<<<PAGE 67>>>
- **P44** sFlow：Receiver/Sampler/Polling 实例 2；采样字段含帧长/类型/MAC/VLAN/优先级/IP/端口/TCP flags/TOS；轮询 10 项计数器 <<<PAGE 68>>>
- **P45** RMON 仅基础 4 组（Statistics/History/Alarm/Events），10 组与 RMON2 需外置探针；History 间隔 1-3600 秒、Alarm 间隔 1-2147483647 秒、trap Rising/Falling <<<PAGE 69>>>
- **P46** Switch Health 语义：资源利用率记录当前/1 分钟均值/1 小时均值/1 小时最大，原始样本保留 60 秒；利用率 0=未测量、1=<2% 的非零值；阈值跨 switch/module/port 全层级自动生效 <<<PAGE 70>>>
- **P47** VLAN Stacking（QinQ）：service 4、SVLAN 4K、SAP 8K；SAP profile 8K（分配优先级/带宽时降为 1K）；每 SAP CVLAN 4K（6860 3.5K）；6900 系 SAP-UNI-CVLAN 3072 <<<PAGE 71>>>
- **P48** Syslog：RFC 5424、12 服务器、级别 2-9（Alarm→Debug3）；Ethernet OAM（802.1ag/Y.1731）MD 8/MA 128/MEP 256、最小 CCM 100ms <<<PAGE 72>>>
- **P49** Link OAM（802.3ah）支持 6465-6575-6860 系-6870，镜像口不支持；CPE Testhead（6465/6560/6570M/6575）每机 32 测试 ID、同时仅 1 活动测试、角色 Generator/Analyzer/Loopback <<<PAGE 73>>>/<<<PAGE 74>>>
- **P50** SAA 128 会话；SPB SAA 每 BVLAN 128（9900 320）；MRP（6465/6575/6865）3 环、50 节点、重组时间 200/500ms（IEC 62439-2）<<<PAGE 75>>>/<<<PAGE 76>>>

## TCAM Profile 机制（Ch4）

- **P51** TCAM profile 机制本质：按应用分配不同数量的 TCAM 规则，配置后必须 reload 激活；6870 五档（Default/Metro services/QoS ACL/Source IPv6 ACL/Bidirectional IPv6 ACL），6570M 两档（Default/Fabric），6575 三档（Default/Fabric/Source IPv6 ACL）："The user can configure the required TCAM profile and reload the switch to activate the configured TCAM profile." <<<PAGE 87>>>
- **P52** 6870 TCAM 权衡典型：QoS Ingress Default 2048→QoS ACL 4096，但 SAP 分类从 2048 降到 1024；Metro services 档 VSTK 出方向翻译升到 1024 但业务隧道降到 1024、UNP 用户降到 1024——档位间是零和重分配 <<<PAGE 89>>>
- **P53** 6570M Fabric 档：服务隧道 256→513（U28 达 1536）、UNP 用户 256→750（U28），代价是 QoS 入规则 384→256、PVLAN/VSTK 归零——fabric 场景牺牲 VPN 特性换隧道容量 <<<PAGE 90>>>
- **P54** 6575 双 fabric 特例：Fabric 档把隧道 225→512，且 DHCPv6 ISF 保持 0；要 IPv6 snooping 只能选 Source IPv6 ACL 档（DHCP6_RLY_ISF 81、AntiSpoofv6 53），代价 QoS 入 384→128 <<<PAGE 92>>>

---
合计：54 条（P1-P54）。
