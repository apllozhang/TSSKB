# principles — 代表章命令族语义与关键默认值（P1…P34）

来源：定点深读代表章正文（页码为 `<<<PAGE N>>>` 标记）。默认值/取值范围均摘自原书 Defaults/Syntax Definitions 表。

## 端口与 PoE（第 1、2 章）

- **P1 `interfaces` 命令族（第 1 章，<<<PAGE 67>>>）**：以太网端口软件负责硬件诊断、链路状态通知、线路参数配置与统计采集。`interfaces speed|duplex|fec|break-out|eee|ddm` 等 30+ 子命令覆盖物理层全部可调参数；`violation`/`clear violation` 管理端口违例恢复。
- **P2 端口监视与统计（第 1 章）**：`show interfaces status/counters/counters errors/traffic/ddm` 按场景拆分展示；`interfaces link-monitoring link-flap-threshold/link-error-threshold` 提供链路抖动自动检测。
- **P3 PoE 供电管理（第 2 章，<<<PAGE 254>>>）**：`lanpower` 族管理 PSE 供电预算、端口优先级与 power rule；802.3bt（固件 3.xx）下 class-detection 自动启用，无需手工配置；power rule 需先创建再绑定到槽位/端口才生效。
- **P4 PoE 平台差异（第 2 章）**：OmniSwitch 6465 无法自动检测电源类型，必须手工配置电源型号才能正确显示系统与 PoE 功率信息。

## 二层与 VLAN（第 5、7 章）

- **P5 `vlan` 命令（第 5 章，<<<PAGE 428>>>）**：`vlan vlan_id [admin-state {enable|disable}] [name description | prompt-on-deletion]`。默认 admin-state=enable、prompt-on-deletion=disable；支持 `vlan 10-15` 连续区间写法；删除 VLAN 前自动剥离全部成员端口，端口回退默认 VLAN 1。
- **P6 VLAN 语义（第 5 章）**：所有物理端口初始属于 VLAN 1；VLAN 在至少一个成员端口 active 前不会操作生效；admin-state disable 保留静态端口归属但停止转发。
- **P7 私有 VLAN（第 5 章）**：`pvlan`/`pvlan secondary`/`pvlan mapping` 三级结构（primary/secondary/isolated-community），MIB 为 ALCATEL-IND1-VLAN-MGR-MIB。
- **P8 VLAN Stacking/QinQ（第 7 章，<<<PAGE 476>>>）**：以 reserved VLAN 承载业务，用户 VLAN 打外层标签；reserved VLAN 不能用标准 vlan 命令配置；NNI 口 TPID 在已成为 stacking 口后不可修改。

## 冗余与环网（第 8、13 章）

- **P9 分布式 STP（第 8 章，<<<PAGE 567>>>）**：基于 802.1D，STP 计算分布在主管理模块与接口模块之间，主备倒换时仍能响应 BPDU，提高鲁棒性；`spanty`/`bridge`/`spantree` 命令族 50 条。
- **P10 链路聚合（第 13 章，<<<PAGE 1092>>>）**：`linkagg` 支持静态与动态（LACP）聚合；动态聚合仅兼容 IEEE 802.3ad 标准实现；hash-control brief 模式下哈希退化为仅源 MAC（L2）或仅源 IP（L3）。

## SPB 骨干与服务（第 10、11 章）

- **P11 SPBM 架构（第 10 章，<<<PAGE 743>>>）**：SPB-M 按 IEEE 802.1aq 用 PBB（802.1ah MAC-in-MAC）封装穿越骨干，最短路径树由 ISIS-SPB（IS-IS + SPB TLV 扩展）计算；分 backbone（控制面）与 services（数据面）两层，服务层命令在第 11 章 Service Manager。
- **P12 `spb bvlan`（第 10 章，<<<PAGE 745>>>）**：BVLAN ID 取值 1–4094，支持区间（如 10-20）；默认 admin-state=enable；BVLAN 配置必须在每台 SPB 桥上完全一致，否则 ISIS-SPB 邻居发现与最短路径计算失败。平台：6360/6465/6560 不支持，6570M 起支持。
- **P13 BVLAN 与普通 VLAN 差异（第 10 章）**：BVLAN 上 STP 自动禁用、全部端口保持转发态。
- **P14 `spb isis bridge-priority`（第 10 章，<<<PAGE 750>>> 附近）**：默认 32768，数值越小优先级越高；桥优先级占 8 字节 SPB Bridge ID 的高 2 字节，低 6 字节为桥 MAC（system ID）。
- **P15 SPB IP VPN（第 10 章，<<<PAGE 744>>>）**：`spb ipvpn bind/redist` 把 ISID 绑定/重分发进 VRF；同一 ISID 不能绑定并重分发进同一 VRF 实例。

## IP 与路由（第 21、28、31 章）

- **P16 IP 命令章规模（第 21 章，<<<PAGE 1549>>>）**：113 条，`ip interface`/`ip route`/`ip domain`/ARP/`ip helper` 等构成单播路由底座；路由协议均需先 `ip load <protocol>` 加载。
- **P17 OSPF 定位（第 28 章，<<<PAGE 2392>>>）**：链路态 IGP，符合 RFC 1370/1850/2328/2370/3101/3623；命令按 Global/Area/Interface/BFD/VRF 分组；DR/BDR 机制。
- **P18 `ip ospf spf-timer`（第 28 章，<<<PAGE 2409>>>）**：`[delay seconds] [hold seconds]`，取值均 0–65535；默认 delay=5、hold=10；任一值设 0 则拓扑变化立即触发 SPF 且可背靠背计算。平台：6360/6465 不支持，6560 起支持。
- **P19 `ip ospf interface hello-interval`（第 28 章，<<<PAGE 2434>>>）**：取值 0–65535 秒；默认 broadcast/点对点=10、NBMA/点对多点=30；值 0 创建被动（passive）OSPF 接口。
- **P20 BGP 定位（第 31 章，<<<PAGE 2744>>>）**：BGP-4 + 多协议扩展（MP-BGP 支持 IPv6 单播前缀与 IPv6 邻居会话），符合 RFC 4271/4760/2545/7947 等；命令分 Global/Aggregate/Network/Neighbor/Address-family/VRF 组；peer 与 neighbor 术语互换使用。
- **P21 `ip bgp default local-preference`（第 31 章，<<<PAGE 2759>>>）**：取值 0–4294967295，默认 100；值越高越优；local-pref 只在本 AS 内传递，不广告给外部 peer；使用前必须先用 `ip bgp admin-state` 停协议。
- **P22 `ip bgp maximum-paths`（第 31 章，<<<PAGE 2776>>>）**：等价多路径（ECMP）开关，默认 disabled；启用后在忽略 router-id 判等时把全部等价路径装表；同样要求先停 BGP。

## QoS 与策略（第 38、39 章）

- **P23 策略模型（第 39 章，<<<PAGE 3953>>>）**：policy rule = policy condition + policy action；rule 编入 policy list 后生效；策略可经 CLI/SNMP/PolicyView（LDAP 端 GUI）三种途径创建。
- **P24 CLI 与 PolicyView 优先级（第 39 章）**：PolicyView 创建的规则不能经 CLI 修改，但 CLI 创建的策略可覆盖 PolicyView 策略的优先级。
- **P25 条件子命令族（第 39 章，<<<PAGE 3955>>>）**：`policy condition` 40+ 子命令，覆盖 ip/ipv6/ip-port/tcp-port/udp-port/ethertype/tcpflags/service/icmp/ip-protocol/flow-label/tos/dscp/mac/vlan/802.1p/port/vrf/fragments/app-mon 等，inner 前缀支持 QinQ 内层字段。
- **P26 动作子命令族（第 39 章，<<<PAGE 3956>>>）**：`policy action` 提供 disposition（accept/drop/deny）、cir（承诺信息速率，bps + cbs/pir/pbs）、maximum bandwidth/depth、802.1p/dscp/tos 改写与 map 映射、redirect port/linkagg、mirror、port-disable、permanent gateway 等。
- **P27 group 复用机制（第 39 章）**：`policy network/mac/port/vlan/map/service group` 把同类对象成组，供多个 condition 引用，减少重复定义。
- **P28 QoS 硬件章（第 38 章，<<<PAGE 3797>>>）**：与第 39 章策略软件互补，管理硬件队列、调度与端口 QoS 参数（70 条）。

## 安全与准入（第 41、42 章）

- **P29 Access Guardian 架构（第 42 章，<<<PAGE 4470>>>）**：UNP（Universal Network Profile）为统一框架——端口使能 UNP 后对用户认证/分类进 profile，profile 映射 VLAN 或 SAP；组件含 BYOD（UPAM/ClearPass 联动，含 mDNS/SSDP GRE 隧道）、Captive Portal（内置 Web 服务器内外部认证）、QMR（隔离与补救）、IoT Device Profiling（DHCP 指纹 + MAC OUI）。199 条为全书最大命令章。
- **P30 UNP 命令分组（第 42 章，<<<PAGE 4471>>>）**：全局配置（dynamic-vlan-configuration、auth-server-down、redirect 族、mac-mobility 等）与 profile 配置（trust-tagged-vlans、qos-policy-list、captive-portal 等）两大类，另加 port/domain/user/show 组。
- **P31 AAA 支撑（第 41 章，<<<PAGE 4205>>>）**：119 条，RADIUS/TACACS+/LDAP 服务器组与认证方法链，为 Access Guardian 提供 AAA 底座（原书明确指引联动）。

## 监测与 OAM（第 18、50-57 章）

- **P32 LLDP（第 18 章，<<<PAGE 1390>>>）**：802.1AB 以 LLDPDU 与邻居交换信息并维护邻居数据库；`ethernet-service uni` 控制带标签/无标签 LLDPDU 的处理（默认两者均丢弃）。
- **P33 双 OAM 体系（第 55、56 章）**：Ethernet OAM/CFM（802.1ag，MEP/MAID/远端 MEP 状态，<<<PAGE 5358>>>）面向连通性故障管理；LINK OAM（802.3ah，<<<PAGE 5432>>>）面向单链路监测，两章共 69 条。

## 系统与管理（第 61、66 章）

- **P34 配置管理模型（第 61、66 章，<<<PAGE 5697>>>/<<<PAGE 6060>>>）**：`working-set`/`configuration` 命令族支持 VC 多机箱批量配置与 running/committed 双区管理；Chassis Management 章 91 条覆盖风扇/电源/温度/防雷等硬件运维。
