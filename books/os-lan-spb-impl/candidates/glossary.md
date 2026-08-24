# GLOSSARY · OmniSwitch LAN SPB Concepts & Implementation (DT00XTE323EN Edition 12)
# 提取自全书实施视角（重点 p56/p91/p142 组件图与各配置章），40 条，按字母序排列。

- id: g01
  term: AOS
  full: Alcatel-Lucent OmniSwitch Operating System
  source_chapter: "p9, p26, p30"
  definition: |
    OmniSwitch 统一网络操作系统；OmniFabric 的核心卖点之一是 SPB、EVPN、MPLS 三种织物技术同跑一个 AOS（p30"All Technology fabric under the same Operating System - AOS"）。
    实施视角：全部课程命令（spb/service/unp/erp 系）都是 AOS CLI；IS-IS 在系统启动时自动加载，无需像 OSPF 那样 ip load（p84 Note）。

- id: g02
  term: B-MAC
  full: Backbone MAC Address
  source_chapter: "p56, p69, p79"
  definition: |
    每台 SPB 桥的唯一桥 MAC（=System Base MAC），IS-IS 以 SYS-ID 形式通告；BEB 用自己的 B-MAC 做封装源地址，BCB 只按 B-MAC 头转发。
    实施用法：show spb isis info 取本端与对端 B-MAC；mac-ping dst-mac <B-MAC> vlan <BVLAN> 验证转发；ERP 过 SPB 时 spb-remote-system 填对端 BEB 的 B-MAC。

- id: g03
  term: BCB
  full: Backbone Core Bridge
  source_chapter: "p56, p62"
  definition: |
    SPB 骨干核心桥：只感知 B-MAC 头做转发，不感知任何服务（"BCB is unaware of services"），只学 BEB 地址、跑 IS-IS SPB 选路与 PBB 数据面。
    实施要点：服务/SAP/UNP 一律不配在 BCB 上；两层拓扑里可以没有 BCB（BEB 直连全互联，p61），三层拓扑里 BCB 居核心、BEB 居汇聚。

- id: g04
  term: BEB
  full: Backbone Edge Bridge
  source_chapter: "p56, p61"
  definition: |
    SPB 边缘桥：服务终结点，做 VLAN→I-SID 映射、SAP 接入、IS-IS MAC 学习、PBB 封装/解封；所有 L2/L3 服务与 UNP 动态功能都只在 BEB 上配。
    冗余靠 VC 双机或双 BEB + LACP（p61）。Lab 拓扑中 OS6860/6870 做 BEB，OS6900 可 BEB 可 BCB。

- id: g05
  term: B-VID / B-TAG
  full: Backbone VLAN ID / Backbone TAG (802.1ah)
  source_chapter: "p58"
  definition: |
    802.1ah 封装外层标签（Ethertype 802.1ad 承载）中的骨干 VLAN ID，决定帧在骨干里走哪棵最短路径树（对应 BVLAN）。
    与 I-SID 分工：B-VID 选路，I-SID 选服务。show spb isis unicast-table bvlan X 按其逐个查看转发表。

- id: g06
  term: BUM
  full: Broadcast, Unknown-unicast, Multicast
  source_chapter: "p138"
  definition: |
    广播/未知单播/组播流量（ARP、DHCP/Boot-P 等）的统称。SPBM 用 Head-End（默认）或 Tandem（S,G / *,G）两种方式复制分发。
    实施要点：不开 IPMS 时 BUM 无差别泛洪到所有 SAP/SDP；模式配置见 service spb X multicast-mode 与 spb isis bvlan N tandem-multicast-mode。

- id: g07
  term: BVLAN
  full: Backbone VLAN
  source_chapter: "p56, p66"
  definition: |
    承载 SPB 控制与封装流量的特殊 VLAN：无 STP、不学客户源 MAC、不泛洪；每 BVLAN 独立算 SPT；AOS 最多 16 个。
    创建：spb bvlan N（可加 ect-id）；教材惯例 2000/2001/2002（Lab）或 4001-4004（理论示例）。控制 BVLAN 专载 IS-IS 报文并可挂带内管理 IP。

- id: g08
  term: Control BVLAN
  full: Control Backbone VLAN
  source_chapter: "p66, p67"
  definition: |
    承载 IS-IS 控制 PDU 的 BVLAN（单标签），用 spb isis control-bvlan N 指定，只能在协议禁用时更改。
    支持挂 IP 接口做带内管理（ip interface "spb-mgmt" ... vlan N），ISIS-SPB 直接通告该子网并做 MAC-IP 映射免 ARP；OV2500 纳管即依赖它（Lab 用 172.30.1.0/24 vlan 2000）。ERP 场景下 ERP 服务 VLAN 的 SPB 服务必须建在控制 BVLAN 上（p242）。

- id: g09
  term: C-VID / C-TAG
  full: Customer VLAN ID / Tag (802.1Q)
  source_chapter: "p56, p58"
  definition: |
    客户原始 VLAN 标签（802.1Q）。SAP 按 C-VID（或 QinQ 双标签、untagged、all）识别客户流量并归入 I-SID 服务；客户帧整体被封装进 MAC-in-MAC，骨干不感知其内容。
    实施语法：sap port 1/1/3:2（C-VID 2）、:0（untag）、:30.32（QinQ）、:all。

- id: g10
  term: DHL
  full: Dual-Home Link
  source_chapter: "p250"
  definition: |
    AOS 接入交换机特性：不跑 STP 实现核心-边缘快速倒换。每机一个 DHL 会话、两条 link（物理口或 linkagg）、VLAN 池双挂 + vlan-map 指定每链路服务的 VLAN，切换时 mac-flushing raw 清 MAC。
    Lab 用法：Sw3 经 linkA（1/1/7→Sw7）/linkB（1/1/8→Sw8）双上联，VLAN 40 定向 linkB；与 SPB 服务/VRRP 组合做接入冗余。

- id: g11
  term: DIS
  full: Designated Intermediate System
  source_chapter: "p228"
  definition: |
    multi-access 共享网上的伪节点代表：负责 LSDB 同步与 LSP 泛洪，所有最短路径都经 DIS。选举取接口优先级最高者（默认 64，同分取最高 B-MAC）；无备份，重选约 3 秒。
    实施命令：spb isis interface port X type multi-access priority 90；查看 show spb isis interfaces port X 的 Desg IS 字段。

- id: g12
  term: Dynamic SAP
  full: UNP 动态业务接入点
  source_chapter: "p262, p263"
  definition: |
    由 UNP 服务 profile 自动创建的 SAP：终端经认证（MAC/802.1x）或分类命中 profile 后，系统按 profile 参数（VLAN tag→I-SID→BVLAN）自动建 SAP 并转发。配 unp port X port-type access 后生效，show 中 SAP Type 显示 Dynamic、带 * 号。
    与静态 SAP（service spb X sap ...）相对；仅动态 SAP 支持 multi-untag-sap；隔离用户重定向补救不被支持（p262 星号注）。

- id: g13
  term: E-LAN / E-LINE / E-TREE
  full: Ethernet LAN / Line / Tree 服务模型
  source_chapter: "p54, p94, p318"
  definition: |
    三种以太业务形态：E-LAN=多点任意互通（SPB 默认）；E-LINE=点对点（伪线，service X ... pseudo-wire enable）；E-TREE=有根多点、Leaf 间隔离（service X ... e-tree enable）。
    AOS 原生三者都支持（p54"Supports E-LINE/E-LAN/E-TREE"）。

- id: g14
  term: ECT
  full: Equal Cost Tree (Algorithm)
  source_chapter: "p70"
  definition: |
    等价树算法：16 个预定义算法（ECT 1-16），每个 BVLAN 对应一个（建 BVLAN 时自动按序分配或手工 spb isis bvlan N ect-id X）。metric 与跳数都相同时用 ECT 掩码对 BridgeID 逐字节 XOR 打破平局，单播组播同算法保证对称。
    ECT1(0x00) 取最小 BridgeID、ECT2(0xFF) 取最大，依此交错实现 BVLAN 间负载分担。

- id: g15
  term: ERP
  full: Ethernet Ring Protection (G.8032)
  source_chapter: "p239, p243"
  definition: |
    以太环保护协议：RPL owner 阻塞环上一口防环，故障时快速倒换，恢复后按 wait-to-restore-timer 重新阻塞。可与 SPB 互操作——环经 BEB 的 SAP 端口延伸过 SPB 云，控制帧走控制 I-SID，BEB 不能做 RPL 节点。
    命令族：erp-ring N port1/port2 service-vlan V level L（L 为 MEG 维护等级，Lab 用 1）、rpl-node、sap-neighbor、access-tagged ... spb-remote-system <BMAC>、erp-ring N enable。

- id: g16
  term: GRT / GRM / IPRM
  full: Global Routing Table / Global Route Manager / IP Route Manager
  source_chapter: "p188, p190"
  definition: |
    L3-VPN 的路由汇聚三层组件：每个 VRF 内 IPRM（IP 路由管理器）管理 RIB/FIB；VRF 路由经 export 进入 GRT（全局路由表，ISIS-SPB IPVPN 路由表），SPB-ISIS 用 IPVPN TLV 跨骨干分发；GRM 统筹 VRF↔I-SID 的双向进出，对端再经 import 从 GRT 取回 VRF。
    查看：show ip global-route-table（isid/vrf 两类来源）、show spb ipvpn route-table（含源桥 B-MAC）。

- id: g17
  term: Head-End Replication
  full: 头端复制（BUM 分发模式，默认）
  source_chapter: "p139"
  definition: |
    入口 BEB 对每个远端有同 I-SID 的 BEB 复制一份、用对端单播 B-MAC 封装发送；组播走单播树和同一张 FDB。适合兴趣社区稀疏、组播带宽低的场景。
    show service X 显示 Multicast-Mode: Headend；伪线服务强制此模式。

- id: g18
  term: Hybrid Access Port
  full: 混合接入端口
  source_chapter: "p315, p316"
  definition: |
    AOS 8.9.R03 起，一个端口同时做桥端口（默认 VLAN+tag VLAN 走 VLAN 域）与业务接入口（SAP VLAN tag 流量走服务域）。
    命令：service access port X hybrid enable|disable。适合聚合交换机下联口：SAP 流量进 SPB 服务、常规流量本地桥接。

- id: g19
  term: I-SID
  full: Backbone Service Instance Identifier
  source_chapter: "p56, p92"
  definition: |
    24 位骨干服务实例标识，标识一个 MAC-in-MAC 服务实例，全网必须一致（service 号才可本机不同）。一个 I-SID 只绑一个 BVLAN；容量 1024 I-SID/BVLAN。
    配置：service spb <svc> isid <isid> bvlan <vid>；UNP 动态服务按 10,000,000+域ID×10,000+(VLAN mod 512) 公式生成。

- id: g20
  term: IS-IS SPB (SPB-ISIS)
  full: SPB 控制面协议
  source_chapter: "p69, p71"
  definition: |
    IEEE IS-IS SPB 扩展：承载拓扑发现（IIH，控制 MAC 01:80:c2:00:00:14）、邻接、SPF/ECT 计算、I-SID 成员通告（T/R 位）、L3-VPN IPVPN TLV 路由。
    实施三步：spb isis interface port X [type p2p|multi-access]、spb isis admin-state enable、metric/priority 可调。IS-IS 在 AOS 开机自动加载。

- id: g21
  term: L2 Profile
  full: Layer 2 Control Frame Profile
  source_chapter: "p115, p116"
  definition: |
    定义 access 口上各类控制帧（STP/802.1X/802.1AB LLDP/802.3AD LACP/GVRP/AMAP/MVRP）的处理动作：tunnel（封装穿越骨干）/peer（与对端按协议交互，LACP 即此档）/drop（无条件丢弃）。
    静态口默认 def-access-profile，UNP 动态口默认 unp-def-access-profile；自定义 service l2profile <name> <proto> <action> 后挂 service access port X l2profile。

- id: g22
  term: L3-VPN (SPB)
  full: SPB L3-VPN（IS-IS IPVPN TLV 方式）
  source_chapter: "p186, p187"
  definition: |
    复用 SPB IS-IS 实例、经 IPVPN TLV 携带 VRF 路由的 L3 VPN，无需另跑 OSPF/BGP；概念对标 BGP-L3VPN over MPLS，1 VRF↔1 I-SID 映射。
    配置核心：spb ipvpn bind vrf <v> isid <i> gateway <ip> {all-routes|route-map} + vrf export/import + 可选 redist 泄漏。

- id: g23
  term: LBD
  full: Loopback Detection
  source_chapter: "p120, p121"
  definition: |
    接入口自动环路检测：周期发私有组播帧（D-MAC 0x01-20-DA-02-01-71），检测到环路即 shutdown 端口+trap+日志，可定时/手工恢复；不需要 STP。
    命令：loopback-detection enable（全局）、loopback-detection service access port X enable、show loopback-detection [statistics] port X。裁决：关较高 BridgeID 侧端口/同机较高 PortID 口；linkagg 上任一成员成环全组关闭。

- id: g24
  term: mac-ping
  full: SPB 专用 MAC 层 ping
  source_chapter: "p147"
  definition: |
    AOS 私有 OAM：按目的 B-MAC+BVLAN 验证 SPB 转发面连通与时延（微秒级）。每包超时固定 1 秒；目标不能是广播/组播/空 MAC。
    语法：mac-ping dst-mac <mac> vlan <vid> [priority|drop-eligible|count|interval|size|isid-check]。

- id: g25
  term: NNI / UNI
  full: Network-to-Network Interface / User-to-Network Interface
  source_chapter: "p65, p91"
  definition: |
    SPB 术语里的两类接口：NNI=网络侧接口（SPB network port，跑 IS-IS、承载 BVLAN/PBB 封装，对应 SDP 方向）；UNI=用户侧接口（access port，挂 SAP，客户流量入口）。
    配置框架图（p65/89）即按"Control Plane (NNI ports)"与"Data Plane (UNI ports)"分层。

- id: g26
  term: OmniFabric
  full: ALE 多技术网络织物
  source_chapter: "p26, p30"
  definition: |
    ALE 的多技术织物品牌：单一 AOS 上集成 SPB/MPLS/EVPN，主打零信任架构下端到端安全、IT/OT 融合、内置 IoT 自动检测分段。SPB 定位园区/DC/IoT，EVPN 定位 DC，MPLS 定位运营商与关键业务（p31 矩阵）。
    实施课开场用它回答"何时选 SPB"。

- id: g27
  term: OmniVista 2500 (OV2500)
  full: ALE 网管系统
  source_chapter: "p290, p296"
  definition: |
    ALE NMS：经 SNMP 纳管交换机后可做 SPB 服务开通（SPB Profile：Tag Value/ISID/BVLAN/VLAN Translation/Multicast Mode）、SAP/SDP 监控、SPB 网络拓扑呈现（Topology→SPB Network→Poll Latest Data，可按 BVLAN 查看）。
    SPB Profile 可映射 Access Role Profile，终端认证/分类命中后自动建 SAP。

- id: g28
  term: Overload
  full: IS-IS 过载状态机制
  source_chapter: "p130"
  definition: |
    IS-IS 通告"本节点接近/超出能力"的位：邻居看到后把穿越流量改道（直连目的地除外）。可人为触发用于维护引流（spb isis overload timeout N）或开机保护（spb isis overload-on-boot [timeout]）。
    资源不足时系统也会自动进入该状态。

- id: g29
  term: Persistent SAP
  full: 持久 SAP（不老化）
  source_chapter: "p272, p273"
  definition: |
    经 unp port X profile <name> 静态指派 profile 生成的 SAP：不随设备 MAC 老化而撤销，直到显式移除；适合静默设备（无声终端、传感器）与需要常通的业务。
    每 UNP 口最多挂 8 个 SPB 服务 profile。配套属性 mac-mobility（unp profile <name> mac-mobility，需全局 unp mac-mobility）：SAP 支持_MAC 移动不老化，专用于 VRRP 主备通告持续传递，只对映射 SPB 服务的 profile 有效。

- id: g30
  term: Pseudo-wire
  full: SPB 点对点透明电路
  source_chapter: "p94, p95"
  definition: |
    SPB 上的 E-LINE 服务：两 SAP 间透明转发，自动关 MAC 学习、强制 head-end 组播、无泛洪复制。可在同一机箱本地两 SAP 之间或跨 SPB 网两 SAP 之间。
    命令：service <id> spb isid <i> bvlan <v> pseudo-wire enable [remote-node <BMAC>]。

- id: g31
  term: RPL
  full: Ring Protection Link
  source_chapter: "p243, p256"
  definition: |
    ERP 环的被阻塞保护链路及其 owner 节点：erp-ring N rpl-node port X 声明，wait-to-restore-timer 控制故障恢复后重新阻塞的等待。约束：BEB 不能做 RPL 节点、RPL 口不能在 SPB 网内或做 SAP neighbor。

- id: g32
  term: SAA
  full: Service Assurance Agent
  source_chapter: "p148, p149"
  definition: |
    AOS 主动探测代理：saa spb auto-start 自动为每个发现的 BVLAN-B-MAC 对建 mac-ping 会话（LAG 目的遍历所有成员链路），默认 1 分钟/轮、5 包、RTT 阈值 500us、抖动 100us；历史统计写 /flash/network/saa.xml。
    查看 show saa spb / show saa statistics aggregate。

- id: g33
  term: SDP
  full: Service Distribution Point
  source_chapter: "p91"
  definition: |
    NNI 侧子接口概念：两 BEB 间自动动态建立的 802.1ah 逻辑隧道（B-MAC+BVLAN 组合），远端客户 MAC 绑定在其上；SPB 里自动配置无需手工建。
    查看 show service sdp spb / show service sdp <id>；FDB 里远端 MAC 显示 sdp:<id>:<isid>。ERP 场景下有专门的 SDP ERP port。

- id: g34
  term: SAP
  full: Service Access Point
  source_chapter: "p91, p97"
  definition: |
    UNI 侧子接口：access 端口+封装标识（VLAN/QinQ/untag/all）唯一确定，客户流量进出服务的点；只能建在 access 口（静态或 UNP 动态）。本地客户 MAC 绑定在 SAP 上。
    静态命令：service spb <svc> sap port <p>:<encap> [admin-state enable] [stats enable]；查看 show service spb <id> sap ...。CoS 分类也只在 SAP 边缘完成（p118）。

- id: g35
  term: SPSourceID
  full: SPB 源节点短标识
  source_chapter: "p142"
  definition: |
    20 位短型节点 ID（由系统自动派生，show spb isis info 可见，如 04-77-7d）。用于编码 tandem 组播组 B-MAC（翻转进组地址前 3 字节）与 I-SID（24 位，编码进末 3 字节）。

- id: g36
  term: Tandem Replication (S,G / *,G)
  full: 中继复制模式
  source_chapter: "p140, p141"
  definition: |
    BUM 的中继复制两型：S,G=每 I-SID 每源建源特定组播树（带宽效率高，show spb isis multicast-table 按源显示组地址）；*,G=每 BVLAN 一棵共享树、最低 Bridge ID 节点为根（资源最省，组地址 01:1e:83:... 形式）。
    配置：spb isis bvlan N tandem-multicast-mode {sgmode|gmode}；BVLAN 内所有 I-SID 共用。

- id: g37
  term: UNP
  full: Universal Network Profile
  source_chapter: "p261, p264"
  definition: |
    AOS 统一网络档案：把端口类型、认证（MAC/802.1x/captive-portal/kerberos）、分类规则（MAC/IP/VLAN 七级优先）、服务映射（service-type spb tag-value ... isid ... bvlan ...）打包成 profile，终端上线自动归档并生成动态 SAP。
    配置骨架：unp profile <name> → map service-type spb ... → unp port X port-type access [802.1x|mac authentication] → aaa radius-server/device-authentication。

- id: g38
  term: vlan-xlation
  full: VLAN Translation（出向 VLAN 改写）
  source_chapter: "p100"
  definition: |
    UNI 出口把客户 VLAN tag 改写为另一 CVLAN 的特性，用于两端 CVLAN 编号不一致的服务对接；服务级与 access 口级均可配，默认 disable。
    特殊行为：服务绑定 IP 接口后被隐式启用（Y (Auto)）且锁定不可改（p163）。

- id: g39
  term: VPN-Lite (IP-VPN Lite)
  full: IP-VPN Lite over SPB
  source_chapter: "p156, p173"
  definition: |
    在 L2 SPB 服务之上叠加常规路由协议（OSPF/BGP/静态）实现的 L3 VPN：SPB 充当物理媒体，VRF 的路由协议邻接穿越 PBB 网建立；每 VRF 每 BEB 需一个路由协议实例，收敛受协议叠加拖累（IS-IS 先收敛 OSPF 才能收敛）。
    配置见 p176/p180 Lab：vrf 1 ip interface ... service 10 + ospf 五件套或静态路由。两个 VRF 不能共享同一 I-SID（p175）。

- id: g40
  term: VRRP
  full: Virtual Router Redundancy Protocol
  source_chapter: "p169, p221"
  definition: |
    虚拟路由冗余协议，SPB 场景的标准网关冗余手段：两台 BEB 对同一服务各建内联 IP 接口（.1/.2），配同一 VRID 与 .254 虚地址，优先级交叉实现主备/分担；VRRP 通告可穿越 PBB 网（VPN-Lite 回环口，p175）。
    命令三件套：ip vrrp <vrid> interface <if> priority N / address <vip> / admin-state enable；验证 show ip vrrp [statistics]。UNP 动态 SAP 场景需持久 SAP+mac-mobility 保住通告通路（p273）。
