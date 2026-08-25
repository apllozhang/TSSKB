# OmniSwitch R6/R8 Bootcamp Issue 25 — 术语表候选（glossary）

> 格式：`- **术语**：中文解释 <<<PAGE N>>>`，按章节分组。

## 认证与课程体系

- **ACFE**：ALE 认证资深组网工程师（F/E 级），新学员五年训练营的培养目标之一 <<<PAGE 3>>>
- **ACSE**：ALE 认证资深交换专家认证 <<<PAGE 3>>>
- **Newcomer / Experienced Track**：新学员从零培养与老学员续证两条学习轨道 <<<PAGE 3-4>>>
- **Knowledge Hub**：ALE 培训与认证历史查询门户（enterprise-education.csod.com）<<<PAGE 3>>>
- **DT00CTE120EN**：本 Bootcamp 课程编号 <<<PAGE 5>>>

## 硬件与产品线

- **OmniSwitch 6350**：入门级 L2+ 千兆堆叠交换机，SMB/分支场景 <<<PAGE 22-28>>>
- **OmniSwitch 6450**：L2+/基础 L3 千兆堆叠交换机，可选 10G 上联 <<<PAGE 113-121>>>
- **OmniSwitch 6465**：紧凑型工业加固交换机（-40~+75℃、DIN 导轨、1588v2/MACsec）<<<PAGE 42-49>>>
- **OmniSwitch 6560**：多千兆（mGIG）L2+/基础 L3 交换机，支持 2.5G/802.3bt <<<PAGE 30-39>>>
- **OmniSwitch 6860/6860E**：高级 L3 GE 接入/汇聚交换机，E 型带协处理器与 60W HPoE <<<PAGE 52-59>>>
- **OmniSwitch 6865**：下一代工业加固 L3 交换机（SPB、1588v2、75W HPoE）<<<PAGE 66-74>>>
- **OmniSwitch 6900 系列**：数据中心 TOR/园区核心（X/T/Q32/X72/V72/C32 机型）<<<PAGE 78-94>>>
- **OmniSwitch 9907/9900**：7 槽模块化低时延机箱，直连架构无背板 <<<PAGE 96-107>>>
- **CMM**：Control Management Module，交换机控制管理模块（9900/9000 系列的主控）<<<PAGE 99, 128>>>
- **NI**：Network Interface，业务线卡/网络接口模块 <<<PAGE 100-104>>>
- **CFM**：Chassis Fabric Module，9900 机箱交换网板 <<<PAGE 105>>>
- **EMP**：Ethernet Management Port，带外以太网管理口 <<<PAGE 99, 153>>>
- **VFL**：Virtual Fabric Link，虚拟机箱互联链路 <<<PAGE 292>>>
- **BPS（Omni BPS）**：高级备电柜，N+1/N+N 模式最多备 8 台 <<<PAGE 60-64>>>
- **SFP/SFP+/QSFP+/QSFP28**：光模块封装类型（1G/10G/40G/100G）<<<PAGE 91-94>>>
- **DAC**：Direct Attach Copper 直连铜缆（1/3/5/7 米）<<<PAGE 91>>>
- **Combo 口**：RJ45/SFP 复用端口 <<<PAGE 25, 166>>>
- **MGIG（mGIG）**：多千兆以太网（2.5G/5G/10G BASE-T）<<<PAGE 30-35>>>
- **EEE**：Energy Efficient Ethernet 节能以太网（802.3az）<<<PAGE 52, 710>>>
- **HPoE**：高功率 PoE（60/75W，802.3bt 级）<<<PAGE 33, 54>>>
- **1588v2 (PTP)**：精密时间协议，工业/电力场景时钟同步 <<<PAGE 43, 68>>>
- **ISSU**：In-Service Software Upgrade 不中断升级 <<<PAGE 20, 290>>>
- **CodeGuardian**：LGS 提供的交换机软件三级加固技术 <<<PAGE 108-111>>>
- **IV&V**：独立验证与确认（源码安全审计）<<<PAGE 110>>>
- **Diversified Image**：CodeGuardian 软件多样化衍生镜像（每版本 5 种）<<<PAGE 110-111>>>
- **ProActive Lifecycle Management**：基于 OmniVista 2500 的云端资产生命周期管理 <<<PAGE 1139-1140>>>
- **RCD**：Remote Chassis Detection，经 EMP 的 VC 脑裂检测 <<<PAGE 306>>>
- **VCSP**：Virtual Chassis Split Detection，经 helper 链路的 VC 分裂检测 <<<PAGE 307>>>
- **SSP**：Split Stack Protection，R6 堆叠分裂保护 <<<PAGE 274-275>>>

## AOS 系统与文件系统

- **AOS**：Ale Operating System，OmSwitch 操作系统（R6/R7/R8 三大版本系）<<<PAGE 5, 122>>>
- **Working Directory**：可写运行目录，配置改动保存目标 <<<PAGE 126, 145>>>
- **Certified Directory**：只读认证目录，升级回退基准 <<<PAGE 126, 145>>>
- **Running Directory**：当前启动来源目录（R8 概念）<<<PAGE 146>>>
- **boot.cfg**：配置文件，重启后恢复配置 <<<PAGE 127, 216>>>
- **boot.params**：启动参数文件（镜像选择等）<<<PAGE 127-128>>>
- **MiniBoot/BootROM**：引导加载器与底层硬件初始化 <<<PAGE 128>>>
- **Trescue.img**：USB 灾难恢复镜像 <<<PAGE 139>>>
- **aossignature**：USB auto-copy 触发标志文件 <<<PAGE 140>>>
- **Rollback**：配置回滚（reload 时以 certified 为备份）<<<PAGE 126, 147>>>
- **rollback-timeout**：重启回滚计时（no rollback-timeout 表示不回滚）<<<PAGE 132, 149>>>
- **flash-synchro**：跨 CMM/堆叠成员同步 flash <<<PAGE 267-268, 285>>>
- **show microcode**：查看各目录软件版本 <<<PAGE 143, 962>>>
- **write memory**：保存运行配置到运行目录 <<<PAGE 148, 264>>>
- **copy working certified**：把 working 内容认证到 certified <<<PAGE 133, 965>>>
- **modify running-directory**：R8 切换运行目录命令 <<<PAGE 148>>>
- **Configuration Snapshot**：配置快照文本，可 apply 恢复 <<<PAGE 164, 229-230>>>
- **Pre-banner**：登录前自定义提示文本（pre_banner.txt）<<<PAGE 168>>>
- **WebView**：内置 Web 管理界面 <<<PAGE 169-170>>>
- **OmniVista**：ALE 网管平台（2500 系列/高级应用/PolicyView）<<<PAGE 171-173>>>
- **ELM**：Embedded Lightweight Module，OmniVista 内嵌管理模块 <<<PAGE 171>>>
- **RCL（Remote Configuration Loading）**：开箱 DHCP+TFTP 指令文件自动装载 <<<PAGE 157-158, 941>>>
- **Instruction File**：RCL 下载的升级指令文件（固件/配置/脚本/服务器）<<<PAGE 158>>>
- **Bash shell**：R8 CLI 底层 shell（别名/管道/busybox）<<<PAGE 150-151>>>
- **Alias**：命令别名，存 boot.cfg <<<PAGE 150, 165>>>

## 账户与 AAA

- **admin 账户**：默认全权限账户（密码 switch，仅 console）<<<PAGE 176, 242>>>
- **default 账户**：新用户权限模板（非登录账户）<<<PAGE 176, 242>>>
- **ASA**：Authenticated Switch Access，管理接口认证框架 <<<PAGE 184>>>
- **AAA**：认证/授权/计费框架（RADIUS/LDAP/TACACS+）<<<PAGE 184-187>>>
- **RADIUS**：远程认证拨入用户服务 <<<PAGE 186, 662>>>
- **TACACS+**：终端访问控制器访问协议_plus <<<PAGE 184, 493>>>
- **End-User Profile**：R6 终端用户档案（限定端口/VLAN 权限）<<<PAGE 177, 182>>>
- **Password Policy**：密码复杂度/历史/年龄/锁定策略 <<<PAGE 180-181>>>
- **Account Lockout**：失败登录锁定（阈值/窗口/时长）<<<PAGE 181>>>
- **NTP**：网络时间协议（客户端/服务器/对等体，RFC1305）<<<PAGE 189-190>>>
- **Stratum**：NTP 层级数 <<<PAGE 189>>>

## 堆叠与虚拟机箱

- **Stack**：多台同家族交换机组建成单一管理实体 <<<PAGE 251>>>
- **Slot-ID**：堆叠成员槽号（boot.slot.cfg 保存）<<<PAGE 256, 251>>>
- **Pass-Through**：槽号冲突时的透传角色 <<<PAGE 255, 257>>>
- **takeover**：堆叠/VC 主备切换命令 <<<PAGE 260, 285>>>
- **MAC Retention**：堆叠主 MAC 保持机制 <<<PAGE 270-273>>>
- **boot.slot.cfg**：堆叠槽号配置文件 <<<PAGE 251, 286>>>
- **Virtual Chassis (VC)**：R8 多机虚拟化成单交换机 <<<PAGE 289-290>>>
- **Master/Slave Chassis**：VC 主/从机箱 <<<PAGE 292>>>
- **Chassis ID / Group ID**：VC 机箱号与机组号（决定组虚拟 MAC）<<<PAGE 293>>>
- **Control VLAN**：VC 内部通信保留 VLAN（仅 VFL 口）<<<PAGE 292>>>
- **vcsetup.cfg / vcboot.cfg**：VC 建立所需两文件 <<<PAGE 294>>>
- **virtual_dir**：VC 配置目录（reload from virtual_dir 恢复 VC）<<<PAGE 932>>>
- **Auto-VC**：出厂自动 VFL/Chassis ID 协商 <<<PAGE 938-940>>>
- **Demo License**：VC 出厂默认演示许可 <<<PAGE 938>>>

## 诊断

- **swlog**：交换机日志（console/flash/syslog 三输出）<<<PAGE 325-332>>>
- **appid/subapp**：日志应用/子应用标识与级别控制 <<<PAGE 330-331>>>
- **command-log**：命令及结果日志（/flash/command.log）<<<PAGE 333-335>>>
- **Port Mirroring**：端口镜像（2 会话、128:1）<<<PAGE 336-337>>>
- **RPM（Remote Port Mirroring）**：跨交换机远程镜像（专用 VLAN）<<<PAGE 338>>>
- **Policy Based Mirroring**：基于 QoS 策略的镜像 <<<PAGE 339-340>>>
- **Port Monitoring**：本机抓包（Sniffer ENC 格式、前 64 字节）<<<PAGE 341-342>>>
- **RMON**：远程监控（统计/历史/告警/事件四组）<<<PAGE 343-344>>>
- **show health**：CPU/内存资源利用率与健康阈值 <<<PAGE 345-346>>>
- **sFlow**：RFC3176 流采样监控（agent+collector）<<<PAGE 347-350>>>
- **sFlow Receiver/Sampler/Poller**：接收器/采样器/轮询器三要素 <<<PAGE 350>>>

## VLAN 与二层

- **VLAN**：虚拟局域网（广播域）<<<PAGE 360>>>
- **默认 VLAN（VLAN 1）**：出厂全部端口所属、不可删 <<<PAGE 363, 385>>>
- **Static VLAN**：端口手工指定 VLAN <<<PAGE 362-364>>>
- **Dynamic VLAN**：按规则/认证动态指派 VLAN <<<PAGE 365-371>>>
- **Mobile Port**：R6 动态 VLAN 端口类型 <<<PAGE 367, 370>>>
- **VLAN Rules**：VLAN 分类规则（MAC/网络地址/协议等）<<<PAGE 368-370>>>
- **802.1Q Tag**：VLAN 标签（12bit VID+3bit 802.1p）<<<PAGE 377-379>>>
- **802.1p**：VLAN 标签内 3bit 优先级字段 <<<PAGE 379>>>
- **Mobile Tag**：mobile 口收多 VLAN 打标签机制 <<<PAGE 381-383>>>
- **Tagged/Untagged 端口**：打标签/不打标签的 VLAN 成员口 <<<PAGE 363, 380>>>
- **Inter-VLAN Routing**：虚拟路由口间三层互通 <<<PAGE 372-374>>>
- **Virtual Router Port**：VLAN 上 IP 接口的旧称 <<<PAGE 373, 385>>>
- **Source Learning**：VLAN 内源学习 <<<PAGE 374, 385>>>
- **MVRP**：多 VLAN 注册协议（802.1ak，动态 VLAN 注册/裁剪）<<<PAGE 479, 967-971>>>
- **MVRP Registrar/Applicant Mode**：MVRP 端口注册/申请模式 <<<PAGE 970>>>
- **Dynamic VLAN（MVRP）**：MVRP 自动创建的 VLAN（type dyn）<<<PAGE 970>>>

## 链路聚合

- **Link Aggregation**：多物理口合为单逻辑链路 <<<PAGE 394>>>
- **LACP（802.3ad）**：链路聚合控制协议 <<<PAGE 396, 398>>>
- **LACPDU**：LACP 协议数据单元 <<<PAGE 396>>>
- **OmniChannel（静态聚合）**：ALE 静态聚合，仅限 OmniSwitch 间 <<<PAGE 396-397>>>
- **Actor Admin Key**：聚合端口关联键（两端一致）<<<PAGE 398, 404>>>
- **Primary Port**：聚合组主端口（组播默认出口）<<<PAGE 402, 405>>>
- **hash-control**：哈希算法控制（brief/extended/non-ucast）<<<PAGE 401-402>>>
- **DHL（Dual Home Link）**：双归属链路 Active-Active 上行冗余 <<<PAGE 476-481>>>
- **RPL（DHL 中）**：Pre-Emption timer 恢复等待定时器 <<<PAGE 479>>>
- **MAC Flushing**：DHL 变更后清陈旧 MAC（None/MVRP Enhanced/RAW）<<<PAGE 479-480>>>

## 生成树

- **STP（802.1D）**：生成树协议防环 <<<PAGE 414, 419>>>
- **RSTP（802.1w）**：快速生成树（默认），亚秒收敛 <<<PAGE 415, 421>>>
- **MSTP（802.1s）**：多生成树，多实例映射 VLAN <<<PAGE 415, 437>>>
- **Flat Mode**：每机一棵生成树 <<<PAGE 427-428>>>
- **1x1 / Per-VLAN Mode**：每 VLAN 一棵树（默认）<<<PAGE 427, 429-430>>>
- **Root Bridge**：根桥（最低 Bridge ID 选举）<<<PAGE 414, 419-420>>>
- **Bridge Priority**：桥优先级（默认 32768）<<<PAGE 425, 461>>>
- **Root Port / Designated Port**：根端口/指定端口 <<<PAGE 414, 423>>>
- **Alternate / Backup Port**：RSTP 替代/备份端口 <<<PAGE 423>>>
- **BPDU**：桥协议数据单元 <<<PAGE 419, 428>>>
- **Path Cost**：路径开销（16/32bit 两套默认值）<<<PAGE 425, 432>>>
- **PVST+**：Cisco 每 VLAN 生成树互操作 <<<PAGE 433-434>>>
- **CIST**：公共内部生成树（MSTP 实例 0）<<<PAGE 438, 442>>>
- **MSTI**：多生成树实例（最多 16 个）<<<PAGE 438>>>
- **MST Region**：MST 域（同名+同修订+同映射表）<<<PAGE 440, 443>>>
- **Region Boundary Port**：域边界端口 <<<PAGE 443>>>
- **Digest**：VLAN-实例映射表摘要（BPDU 携带）<<<PAGE 443>>>
- **CST Root / CIST Regional Root**：全网根/区域根 <<<PAGE 441-442>>>

## IP 接口与 DHCP

- **Loopback0**：常驻环回管理接口 <<<PAGE 492>>>
- **ip managed-interface**：按应用指定源接口（R8）<<<PAGE 493>>>
- **Local Proxy ARP**：本网段代理 ARP <<<PAGE 491, 495>>>
- **ARP Filter**：ARP 报文过滤 <<<PAGE 497>>>
- **DHCP Relay（ip helper）**：DHCP 中继 <<<PAGE 498, 743>>>
- **UDP Relay**：指定 UDP 端口中继（如 DNS）<<<PAGE 499>>>
- **ip interface**：三层虚拟 IP 接口 <<<PAGE 373, 496>>>
- **ECMP**：等价多路径 <<<PAGE 718, 723>>>

## LLDP

- **LLDP（802.1AB）**：链路层发现协议 <<<PAGE 509>>>
- **LLDPDU**：LLDP 协议数据单元 <<<PAGE 510>>>
- **TLV**：Type Length Value 信息单元 <<<PAGE 510>>> 
- **LLDP-MED**：媒体终端设备扩展 <<<PAGE 513-514>>>
- **Network Policy**：LLDP-MED 网络策略 TLV（VLAN+优先级+DSCP）<<<PAGE 514-515>>>
- **trust-agent**：LLDP 可信代理（ Rogue 检测）<<<PAGE 801-802>>>

## VRRP

- **VRRP**：虚拟路由器冗余协议（RFC 2338）<<<PAGE 522-524>>>
- **Virtual Router ID (VRID)**：虚拟路由器标识 <<<PAGE 524, 529>>>
- **Master/Backup Router**：主/备虚拟路由器 <<<PAGE 526>>>
- **Virtual MAC**：00-00-5E-00-01-{VRID} <<<PAGE 524, 536>>>
- **Preempt**：抢占模式 <<<PAGE 529-530>>>
- **Advertisement Interval**：VRRP 通告间隔 <<<PAGE 527>>>
- **Skew Time**：(256-Priority)/256，防多备同升 <<<PAGE 527>>>
- **VRRP Tracking**：跟踪对象联动优先级 <<<PAGE 531-532>>>
- **VRRP Group**：VRRP 集体管理组 <<<PAGE 533>>>
- **HSRP**：Cisco 热备协议（与 VRRP 不兼容）<<<PAGE 524>>>

## QoS

- **QoS**：服务质量（带宽/时延/丢弃管理）<<<PAGE 542>>>
- **CoS Queue**：每出端口 8 个服务等级队列 <<<PAGE 545-546>>>
- **Strict Priority (SP)**：严格优先调度 <<<PAGE 547, 550>>>
- **WRR**：加权轮询调度 <<<PAGE 547>>>
- **DRR**：差额轮询调度 <<<PAGE 547>>>
- **WFQ**：加权公平队列（R8 QSet Profile 3）<<<PAGE 552>>>
- **EF**：Expedited Forwarding 快速转发队列（限速保护）<<<PAGE 551-552>>>
- **QSet / QSI**：R8 队列组/队列组实例 <<<PAGE 548-549>>>
- **Policy Condition**：策略条件（L2-L4 匹配）<<<PAGE 544, 568>>>
- **Policy Action**：策略动作（标记/限速/重定向/镜像）<<<PAGE 544, 571>>>
- **Policy Rule**：策略规则（条件+动作+可选时段）<<<PAGE 545, 573>>>
- **Precedence**：规则优先级（0-65535，大者先）<<<PAGE 573, 607>>>
- **Validity Period**：规则生效时段 <<<PAGE 565>>>
- **Network/MAC/Service/Port Group**：策略复用组 <<<PAGE 569, 608>>>
- **Disposition（accept/drop/deny）**：策略处置动作 <<<PAGE 609>>>
- **qos apply / qos reset**：策略应用/清空 <<<PAGE 612, 592>>>
- **ToS/DSCP**：三层服务类型/差分服务码点标记 <<<PAGE 543, 590>>>
- **Trusted Port（qos phones trusted）**：信任端口标记 <<<PAGE 581, 590>>>
- **SIP Snooping**：SIP 信令侦听自动语音 QoS <<<PAGE 601>>>
- **Bandwidth Shaping**：带宽整形 <<<PAGE 543>>>
- **Starvation**：严格优先下低队列饿死风险 <<<PAGE 550-551>>>

## ACL 与安全

- **ACL**：访问控制列表（QoS 策略过滤子集）<<<PAGE 604-607, 618>>>
- **established**：TCP ACK/RST 已建连接条件 <<<PAGE 607, 615>>>
- **tcpflags**：TCP 标志位条件 <<<PAGE 611, 618>>>
- **Access Guardian (AG)**：端口自动感知多客户端认证 <<<PAGE 627, 630>>>
- **UNP**：Universal Network Profile 用户网络档案 <<<PAGE 631-632, 645>>>
- **Filter-ID**：RADIUS 属性下发 UNP 名 <<<PAGE 632>>>
- **Group Mobility（R6）**：UNP 前身的移动分组分类 <<<PAGE 636, 652>>>
- **UNP Classification Rule**：设备分类规则（R8 十六级）<<<PAGE 638, 652-656>>>
- **UNP Port（port-type BRIDGE）**：R8 UNP 桥接端口 <<<PAGE 643>>>
- **Location Policy**：按位置限制的 UNP 策略 <<<PAGE 649>>>
- **Period Policy**：按时段限制的 UNP 策略 <<<PAGE 650>>>
- **aaa profile（device-authentication）**：设备认证档案 <<<PAGE 662>>>
- **Captive Portal**：Web 强制门户（终结策略）<<<PAGE 635, 1014>>>
- **Learned Port Security (LPS)**：学习端口安全（限 MAC 数/列表）<<<PAGE 803-809>>>
- **port-security violation restrict/shutdown**：LPS 违规过滤/关口 <<<PAGE 805>>>
- **convert-to-static**：动态 MAC 转静态 <<<PAGE 807>>>
- **learn-trap-threshold**：学习告警阈值 <<<PAGE 809>>>
- **PBR（Policy Based Routing）**：策略路由硬件重定向 <<<PAGE 810-814>>>
- **permanent gateway**：PBR 动作指定固定网关 <<<PAGE 812-813>>>
- **UserPorts**：保留端口组（防欺骗等）<<<PAGE 816>>>
- **DropServices**：保留服务组（批量丢弃）<<<PAGE 817>>>
- **port-disable action**：命中即关闭端口动作 <<<PAGE 817>>>
- **violation-recovery-time**：违规端口自动恢复定时 <<<PAGE 818>>>
- **Directed Broadcast**：定向广播（建议关闭）<<<PAGE 819>>>
- **Early ARP Discard**：早期 ARP 丢弃（CPU 保护）<<<PAGE 819>>>
- **DoS Filtering**：拒绝服务攻击过滤 <<<PAGE 821>>>
- **ARP Defense / ARP Poisoning Detection**：ARP 防御与毒化检测 <<<PAGE 822-824>>>
- **restricted-address（arp-poison）**：ARP 毒化受限地址 <<<PAGE 824>>>
- **MACsec（802.1AE）**：二层链路加密认证 <<<PAGE 825-827>>>
- **Static SA / Dynamic SA（PSK/EAP）**：MACsec 安全关联模式 <<<PAGE 826>>>
- **SCI（sci-tx/sci-rx）**：MACsec 安全通道标识配置 <<<PAGE 1049>>>
- **DHCP Snooping**：DHCP 侦听（信任口/绑定库）<<<PAGE 828-830>>>
- **Option 82**：DHCP 中继选项（Circuit ID/Remote ID）<<<PAGE 832>>>
- **Binding Table**：DHCP 侦听绑定数据库 <<<PAGE 829>>>
- **Port Mapping**：用户口-网络口映射隔离 <<<PAGE 837-839>>>
- **Dynamic Proxy ARP**：端口映射配套代理 ARP <<<PAGE 839>>>
- **Storm Control（flood rate）**：风暴控制（bcast/mcast/unknown-unicast）<<<PAGE 886>>>
- **BPDU Guard**：BPDU 保护 <<<PAGE 799>>>
- **IoT Device Profiling**：IoT 设备画像 <<<PAGE 685-690>>>
- **DHCP Fingerprinting**：DHCP 指纹（Option 55/60）<<<PAGE 688>>>
- **MAC OUI**：组织唯一标识符（设备厂商标识）<<<PAGE 687-688>>>
- **Signature DB**：本地设备签名库 <<<PAGE 686>>>

## PoE

- **PoE（802.3af）**：以太网供电 15.4W <<<PAGE 694-695>>>
- **PoE+（802.3at）**：增强供电 30W（Class 4 34.2W PSE）<<<PAGE 695>>>
- **PSE / PD**：供电设备/受电设备 <<<PAGE 695>>>
- **PD Classification**：受电设备分级（电阻识别）<<<PAGE 695>>>
- **lanpower**：PoE 管理命令族 <<<PAGE 700-708>>>
- **Port Priority（low/high/critical）**：PoE 端口优先级 <<<PAGE 701>>>
- **Capacitor Detection**：电容检测法（旧话机）<<<PAGE 702>>>
- **Priority Disconnect**：预算不足时新 PD 拒绝机制 <<<PAGE 702>>>
- **Power Budget**：PoE 总预算 <<<PAGE 694, 703>>> 

## 路由（静态/RIP/OSPF/GR/BGP/ISIS）

- **Static Route**：静态路由 <<<PAGE 714-717>>>
- **Recursive Static Route（follows）**：递归静态路由 <<<PAGE 719-720>>>
- **Interface Static Route**：出接口型静态路由 <<<PAGE 721>>>
- **show ip router database**：路由数据库（含未用路由）<<<PAGE 718, 720>>>
- **Route Preference（ip route-pref）**：协议路由偏好 <<<PAGE 769>>>
- **RIP（v1/v2/RIPng）**：路由信息协议 <<<PAGE 722-724>>>
- **Distance Vector**：距离矢量算法 <<<PAGE 724>>>
- **Poison Reverse**：毒性逆转 <<<PAGE 725>>>
- **RIP Timers（update/invalid/garbage/holddown）**：RIP 四定时器 <<<PAGE 730-731>>>
- **Route Map（redistribution）**：路由图与重分发 <<<PAGE 726-727, 768>>>
- **OSPF**：开放式最短路径优先（RFC 2328）<<<PAGE 750-753>>>
- **Router ID**：OSPF 路由器标识 <<<PAGE 754, 780>>>
- **Area / Backbone Area**：OSPF 区域/骨干区域 0.0.0.0 <<<PAGE 755, 756>>>
- **DR（Designated Router）**：指定路由器 <<<PAGE 755>>>
- **Adjacency / Neighbor**：邻接/邻居 <<<PAGE 753, 757>>>
- **LSDB**：链路状态数据库 <<<PAGE 753, 757>>>
- **SPF**：最短路径优先算法 <<<PAGE 753, 1093>>>
- **LSA Type 1-7**：链路状态通告类型 <<<PAGE 761>>>
- **Opaque LSA（Type 9-11）**：扩展 LSA（GR 用 Type 9）<<<PAGE 762>>>
- **ABR / ASBR**：区域边界/自治系统边界路由器 <<<PAGE 760-761>>>
- **Stub / Totally Stubby / NSSA**：末节/完全末节/次末节区域 <<<PAGE 760, 764-766>>>
- **Virtual Link**：OSPF 虚链路 <<<PAGE 763>>>
- **default-originate**：ABR 向 stub 区注入默认路由 <<<PAGE 764-765>>>
- **area range（summarization）**：ABR 区域间路由汇总 <<<PAGE 767>>>
- **Graceful Restart (GR)**：优雅重启（转发不中断）<<<PAGE 770-775>>>
- **Grace LSA**：GR 宽限期通告 <<<PAGE 774-775>>>
- **Helper（restart-helper）**：GR 辅助路由器 <<<PAGE 776>>>
- **restart-interval**：GR 宽限时长 <<<PAGE 776>>>
- **BFD**：双向转发检测 <<<PAGE 711, 716>>>
- **BGP（AS/neighbor/eBGP multihop）**：边界网关协议 <<<PAGE 1079-1081>>>
- **IBGP**：内部 BGP（学到的路由不再传 IBGP）<<<PAGE 1082>>>
- **aspath-list / community-list / prefix-list**：BGP 策略列表 <<<PAGE 1086-1088>>>
- **update-source**：BGP 邻居更新源（Loopback0）<<<PAGE 1081>>>
- **IS-IS**：中间系统到中间系统路由协议 <<<PAGE 1090-1093>>>
- **NSAP 地址（Area ID/System ID/NSEL）**：OSI 网络地址 <<<PAGE 1094-1095>>>
- **AFI 49**：本地管理 IS-IS 地址标识 <<<PAGE 1094>>>
- **Level-1 / Level-2**：IS-IS 区域内/区域间层级 <<<PAGE 1094, 1106>>>
- **DIS（Designated IS）**：IS-IS 指定中间系统 <<<PAGE 1097, 1102>>>
- **Pseudo Node**：广播网伪节点 <<<PAGE 1097>>>
- **LSP（IS-IS Link-State Packet）**：IS-IS 链路状态报文 <<<PAGE 1096, 1099>>>
- **CSNP / PSNP**：完全/部分序列号报文 <<<PAGE 1096, 1100-1101>>>
- **Route Leaking**：IS-IS 两级路由泄漏 <<<PAGE 1092>>>

## VRF

- **VRF**：虚拟路由转发（多路由实例）<<<PAGE 853-855>>>
- **Default VRF**：默认路由实例 <<<PAGE 859>>>
- **VRF-aware**：协议的 VRF 感知能力 <<<PAGE 856>>>
- **VRF Route Leak（export/import route-map）**：VRF 与 GRT 间路由泄漏 <<<PAGE 863-864>>>
- **GRT**：全局路由表 <<<PAGE 863-864>>>
- **PE（Provider Edge）**：运营商边缘设备 <<<PAGE 857>>>

## 组播

- **IP Multicast**：IP 组播（单源到多接收）<<<PAGE 866-867>>>
- **Class D 地址**：组播地址范围 224.0.0.0-239.255.255.255 <<<PAGE 867>>>
- **01:00:5e MAC 映射**：组播 IP 到 MAC 的 23 位映射 <<<PAGE 867>>>
- **IGMP（v1/v2/v3）**：互联网组管理协议 <<<PAGE 870-872>>>
- **Querier**：IGMP 查询者 <<<PAGE 871, 879>>>
- **Leave Group / Fast Leave**：v2 离组/快速离开 <<<PAGE 872>>>
- **Source-Specific Join（SSM）**：v3 源特定加入 <<<PAGE 872, 908>>>
- **IPMS**：IP 组播交换（二层硬件 IGMP snooping 转发）<<<PAGE 869, 873-878>>>
- **Querier Forwarding**：组播送查询者机制 <<<PAGE 879>>>
- **IGMP Proxying**：IGMP 代理 <<<PAGE 877>>>
- **Helper Address（IGMP Relay）**：IGMP 报文中继地址 <<<PAGE 884>>>
- **max-group（Throttling）**：端口/VLAN 组数限制 <<<PAGE 885>>>
- **DVMRP**：距离矢量组播路由协议 <<<PAGE 890-896>>>
- **PIM-SM / PIM-DM**：协议无关组播 稀疏/密集模式 <<<PAGE 907-909>>>
- **RP（Rendezvous Point）**：汇聚点 <<<PAGE 492, 908>>>
- **BSR / CBSR**：自举路由器/候选 BSR <<<PAGE 908-909>>>
- **Candidate-RP**：候选汇聚点 <<<PAGE 908, 923>>>
- **SPT（Shortest Path Tree）**：最短路径树切换 <<<PAGE 903, 909>>>
- **static-rp**：静态 RP 配置 <<<PAGE 909>>>
- **groute / sgroute**：组路由/源组路由查看 <<<PAGE 912-913>>>
- **Flood Unknown**：未知组播洪泛开关 <<<PAGE 877, 886>>>

## ERP 与 Intelligent Fabric

- **ERP（G.8032/ERPv2）**：以太网环网保护 <<<PAGE 415, 926-929>>>
- **APS**：自动保护倒换协议 <<<PAGE 926>>>
- **RPL / RPL Owner**：环保护链路及其属主节点 <<<PAGE 929>>>
- **R-APS Channel**：环保护协议信道（Service VLAN 承载）<<<PAGE 928>>>
- **Service VLAN / Protected VLAN**：ERP 业务 VLAN/受保护 VLAN <<<PAGE 928>>>
- **MEG Level**：以太网维护实体组等级（ERP 用）<<<PAGE 929-930>>>
- **WTR（Wait To Restore）**：等待恢复定时器 <<<PAGE 929-930>>>
- **Guard Timer**：ERP 守护定时器 <<<PAGE 930>>>
- **Pending / Protected 状态**：ERP 环状态 <<<PAGE 930>>>
- **Intelligent Fabric (iFab)**：智能织构体系 <<<PAGE 68, 933>>>
- **Auto-fabric**：零接触自动织构发现流程 <<<PAGE 154-155, 951>>>
- **Auto-LACP / Auto-Routing / Auto-MVRP**：自动聚合/路由/VLAN 注册 <<<PAGE 155, 943-944>>>
- **SPB（Shortest Path Bridging）**：最短路径桥接织构技术 <<<PAGE 68, 73>>>
- **Auto Network Profiling**：自动用户/网络档案 <<<PAGE 155, 936>>>

## SLB

- **SLB**：服务器负载均衡 <<<PAGE 972-975>>>
- **VIP（Virtual IP）**：集群虚拟 IP <<<PAGE 974-975>>>
- **SLB Cluster**：服务器集群 <<<PAGE 974, 976>>>
- **WRR（weight）**：加权轮询分发 <<<PAGE 977-979>>>
- **QoS Condition Cluster**：按策略条件定义的集群 <<<PAGE 981, 984-985>>>
- **SLB Probe**：健康检查探针（http/ftp/mail 等）<<<PAGE 987, 995>>>
- **Proxy ARP（SLB）**：VIP 代理 ARP <<<PAGE 975, 983>>>

## IPv6

- **IPv6**：128bit 地址协议 <<<PAGE 1130-1131>>>
- **:: 缩写**：连续零段缩写（仅一次）<<<PAGE 1133>>>
- **Unicast / Multicast / Anycast**：单播/组播/任播 <<<PAGE 1134>>>
- **Link-Local Address（FE80::/10）**：链路本地地址 <<<PAGE 1136-1137>>>
- **Global Unicast**：全球单播地址 <<<PAGE 1135>>>
- **EUI-64**：由 MAC 生成接口标识（插 FFFE 翻 U/L 位）<<<PAGE 1138>>>
- **NDP（Neighbor Discovery）**：邻居发现（用 link-local）<<<PAGE 1137>>>
