# verified · OmniSwitch LAN Access Switching (DT00XTE215EN)
# 阶段 1.5 三重验证通过条目（V1 原文真实性 / V2 可操作价值 / V3 独特性）

## 汇总

| 类型 | 候选 | 通过 | 淘汰 |
|---|---|---|---|
| frameworks | 14 | 14 | 0 |
| principles | 40 | 39 | 1（p18） |
| cases | 15 | 15 | 0 |
| counter-examples | 14 | 14 | 0 |
| glossary | 40 | 40（免验保留） | 0 |
| 合计 | 123 | 122 | 1 |

## 验证说明

- V1：全部 quote 在 source/fulltext.md 对应页命中（个别语句在原文因 PDF 换行断行，逐段核对后确认命中，如 f05 ISSU 序列、p19/p31 参数范围）。
- V2：frameworks/cases 均为可执行配置工作流或 Lab CLI 序列；principles 均含 AOS 参数默认值/规格/目录模型；counter-examples 均为可操作的陷阱规避规则。
- V3：AOS 特有的 certified/working/running 目录模型、VC（ISIS-VC/chassis-id/flash-synchro/ISSU/VCSP）、DHL、UNP、swlog/command-log、hash-control 型号默认值等均判定独特；通用概念（802.1Q、STP、LACP、VRRP、Loopback、静态路由）均带 AOS 实现细节（命令语法、默认值、型号差异），按规则保留。唯一淘汰 p18：VLAN 1 不可删除为各厂商通识事实，条目无 AOS 实现细节，且与 ce10 信息重复。

## 通过条目明细

### frameworks

- **f01** AOS R8 配置管理模型（Certified/Working/Running 三层与回滚机制） — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f02** R8 开机引导序列与启动目录选择流程 — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f03** Virtual Chassis 静态部署五步流程 — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f04** VC 主从同步流程（write memory flash-synchro / copy running certified） — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f05** ISSU 不中断升级流程 — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f06** 静态 VLAN 与 802.1Q 配置工作流 — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f07** 动态 VLAN（UNP）设备分类配置工作流 — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f08** LACP 动态链路聚合配置工作流 — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f09** STP 配置工作流（模式→协议→优先级→路径成本→监控） — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f10** DHL Active-Active 双归属配置工作流 — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f11** VRRP 网关冗余配置工作流（基础+优先级+跟踪） — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f12** QoS/ACL 策略三元组工作流（condition→action→rule→apply） — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f13** Access Guardian（UNP+802.1X/MAC 认证）部署工作流 — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）
- **f14** 软件升级工作流（镜像+U-Boot/FPGA+认证） — 通过（V1 quote 命中；V2 配置工作流；V3 AOS 特有）

### principles

- **p01** AOS CLI 行规：缩写补全、管道过滤、? 帮助与历史 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p02** Flash 目录结构与每型号镜像文件命名 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p03** Running directory 与 running configuration 的定义 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p04** 冷启动目录选择规则：内容一致从 running 启动，不一致回退 certified — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p05** 三条保存命令的语义层级（write memory / copy running certified / flash-synchro） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p06** Certified 运行模式锁定规则：不可保存、不可搬文件 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p07** 配置备份/恢复：configuration_backup.tar 与 10 份上限 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p08** USB 备份/恢复规则（usb backup / auto-copy，可加密） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p09** 默认账户与本地用户库规则（admin/switch、userTable9、64 用户） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p10** AAA 多服务器 fail-through 与 exit-on-fail 语义 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p11** 管理会话数规格（Telnet 6 / SSH 8 / 总 20 / SNMP 50） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p12** Lightning Configuration（易配置模式）触发条件 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p13** VC Master 选举四准则（priority → uptime → chassis ID → MAC） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p14** VC Takeover/Failover 行为规则（新 master 不让位） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p15** Auto VFL 默认候选端口矩阵 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p16** VC 脑裂防护：RCD 与 VC Split Protocol 的处理规则 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p17** VC chassis-group 与 priority 参数规则 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p19** VLAN oper 状态与 IP 接口联动规则（无活动成员则 DOWN） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p20** 802.1Q 标签规则：4096 个 tag、802.1p 3bit、物理口恒有一个桥接 VLAN — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p21** UNP 分类规则次序与三种规则优先级 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p22** swlog 日志参数与文件轮转规则 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p23** swlog 严重级与应用 ID 调级规则 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p24** 命令日志（command-log）规则：100 条、需启用、删文件即删史 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p25** 端口镜像（Port Mirroring）规格：同速端口、4 会话、4 个 MTP 索引 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p26** 端口监控（Port Monitoring）规格：单会话、64 字节、默认 64KB — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p27** 静态 vs 动态链路聚合限制（静态仅 OmniSwitch 间、组内同速） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p28** hash-control 负载哈希算法与各型号默认值 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p29** STP 两种模式三种协议与收敛时间（默认 per-vlan + RSTP） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p30** STP 默认路径成本表（16bit 与 32bit 两套） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p31** STP priority 与 path-cost 参数范围 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p32** DHL 会话约束与定时器/冲刷参数 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p33** DHCP Relay 两种模式互斥与默认参数 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p34** Loopback0 接口规则与用途 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p35** 静态路由规则：静态优于动态、metric 定主备 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p36** VRRP 关键参数与虚拟 MAC 规则 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p37** QoS 默认值与生效规则（默认启用、802.1p 默认 0、端口默认不信任） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p38** IP 电话流量自动优先级（alaPhones MAC 组，优先级 5） — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p39** PoE 标准/预算规则与端口优先级、延迟上电 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）
- **p40** LLDP 默认行为与配置层级规则 — 通过（V1 quote 命中；V2 参数默认值/规格；V3 AOS 特有或带 AOS 实现细节）

### cases

- **c01** Lab 远程交换机访问（SSH + WebView 建删 VLAN） — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c02** Lab Working/Running/Certified 目录全流程实验 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c03** Lab Virtual Chassis-6360 双机组建与监控 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c04** Lab VLAN 建网、VLAN 间路由与动态 VLAN（UNP/MAC） — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c05** Lab 基础维护与诊断工具（swlog/命令日志/镜像/监控/健康/RMON） — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c06** Lab LACP 动态聚合（6360 VC ↔ 6870-A）与故障演练 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c07** Lab 802.1Q 打标签（跨三交换机多 VLAN 单链路） — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c08** Lab STP 根桥控制、端口状态与 1x1 负载分担 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c09** Lab DHL Active-Active 双活配置与切换测试 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c10** Lab DHCP Server & DHCP Relay（全局中继） — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c11** Lab VRRP 主备网关与手动优先级/故障切换 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c12** Lab QoS：端口默认优先级、信任与策略限速 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c13** Lab ACL：L2/L3/ICMP 过滤与服务组（HTTP/FTP 分权） — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c14** Lab Access Guardian（RADIUS+802.1X+UNP）完整认证流 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）
- **c15** Lab LLDP 邻居发现与管理 TLV 增强 — 通过（V1 quote 命中；V2 Lab CLI 工作流；V3 AOS Lab 场景）

### counter-examples

- **ce01** 陷阱：reload all 无论目录状态一律从 certified 启动 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce02** 反例：certified 模式下 write memory 被拒绝 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce03** 陷阱：RAM 中未保存的配置在重启后全部丢失 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce04** 陷阱：VC 中改 chassis-id 后 write memory 的清除警告 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce05** 反例：端口带着 VLAN 成员身份无法加入 linkagg — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce06** 反例：VRRP 优先级在实例运行中修改无效，必须先禁用 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce07** 陷阱：VC 的 chassis priority / chassis-id 改动须重启才生效 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce08** 约束：端口监控与端口镜像不能共用同一端口 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce09** 陷阱：QoS 端口改动和策略不经 qos apply 不生效 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce10** 反例：VLAN 1 不能删除，只能停用 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce11** 陷阱：VLAN 无活动成员时 IP 接口 DOWN 且不被路由宣告 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce12** 约束：静态链路聚合只能用在 OmniSwitch 之间 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce13** 陷阱：DHL 故障链路恢复后不立即回切，要等 pre-emption 30 秒 — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）
- **ce14** 约束：LLDP 不能配置在 linkagg 级别；U 盘拔出前必须 usb disable — 通过（V1 quote 命中；V2 陷阱规避规则；V3 AOS 特有陷阱）

### glossary

- **g01** Certified 目录（认证目录） — 通过（免验保留）
- **g02** Working 目录（工作目录） — 通过（免验保留）
- **g03** Running 目录 / Running configuration（运行目录/运行配置） — 通过（免验保留）
- **g04** User-defined 目录（用户自定义目录） — 通过（免验保留）
- **g05** vcboot.cfg / vcsetup.cfg — 通过（免验保留）
- **g06** CMM（Chassis Management Module，机箱管理模块） — 通过（免验保留）
- **g07** EMP（Ethernet Management Port，以太网管理口） — 通过（免验保留）
- **g08** Virtual Chassis（VC，虚拟机箱） — 通过（免验保留）
- **g09** VFL（Virtual Fabric Link，虚拟机箱互联链路） — 通过（免验保留）
- **g10** ISIS-VC（VC 内部路由/拓扑协议） — 通过（免验保留）
- **g11** RCD（Remote Chassis Detection，远程机箱检测） — 通过（免验保留）
- **g12** VCSP（VC Split Protection / VC Split Protocol） — 通过（免验保留）
- **g13** ISSU（In Service Software Upgrade，不中断升级） — 通过（免验保留）
- **g14** ASA（Authenticated Switch Access，交换机认证接入） — 通过（免验保留）
- **g15** WebView（内嵌 Web 管理） — 通过（免验保留）
- **g16** Lightning Configuration（闪电配置/快速开局） — 通过（免验保留）
- **g17** Thin Client 模式（瘦客户端） — 通过（免验保留）
- **g18** UNP（User Network Profile，用户网络档案） — 通过（免验保留）
- **g19** Access Guardian（接入卫士） — 通过（免验保留）
- **g20** 802.1Q / 802.1p（VLAN 标签与优先级） — 通过（免验保留）
- **g21** Mobile Tag（移动标签） — 通过（免验保留）
- **g22** Linkagg / LACP 与 Actor Admin Key（链路聚合） — 通过（免验保留）
- **g23** STP 模式：flat 与 per-vlan（1x1） — 通过（免验保留）
- **g24** DHL（Dual-Home Link，动态双归属）及 RAW/MVRP 冲刷 — 通过（免验保留）
- **g25** DHCP Relay（DHCP 中继 / IP Helper）与 Option 82 — 通过（免验保留）
- **g26** Loopback0 接口 — 通过（免验保留）
- **g27** VRRP（虚拟路由冗余协议）/ VRID / 虚拟 MAC — 通过（免验保留）
- **g28** QSI / QSP（队列集实例/队列集模板） — 通过（免验保留）
- **g29** 策略三元组：policy condition / action / rule — 通过（免验保留）
- **g30** PBR（Policy Based Routing，策略路由） — 通过（免验保留）
- **g31** RPM / 策略镜像（Remote & Policy Based Mirroring） — 通过（免验保留）
- **g32** ACL disposition（accept/drop/deny） — 通过（免验保留）
- **g33** UserPorts / DropServices（保留策略组） — 通过（免验保留）
- **g34** swlog（交换机日志） — 通过（免验保留）
- **g35** sFlow 与 RMON（流量采样/远程监控） — 通过（免验保留）
- **g36** LLDP / LLDP-MED（链路层发现协议） — 通过（免验保留）
- **g37** PoE（以太网供电）与 FPoE / PPoE / EEE — 通过（免验保留）
- **g38** Auto Fabric / RCL（智能织物/自动远程配置） — 通过（免验保留）
- **g39** write memory flash-synchro（同步保存命令） — 通过（免验保留）
- **g40** ssh-chassis（VC 成员跳转登录） — 通过（免验保留）

## 通过条目全文（供阶段 2 使用）

### frameworks

```yaml
- id: f01
  title: AOS R8 配置管理模型（Certified/Working/Running 三层与回滚机制）
  type: framework
  source_chapter: "p69-71"
  source_quote: |
    "Command to force reboot from CERTIFIED directory: -> reload all
    Command to force reboot from WORKING directory or user defined directory:
    -> reload from working no rollback-timeout
    * Running configuration (RAM): current operating configuration of the switch retrieved from the running
    directory in addition to any configuration changes made by the user.
    * Except when the Running directory is the Certified directory"
  summary: |
    AOS 用"目录式配置"管理交换机：certified（认证基线）/working（测试暂存）/user-defined（用户目录）
    都存放 image + vcboot.cfg/vcsetup.cfg；RAM 中的 running configuration 是当前运行配置。
    配置改动先落在 RAM（立即生效、重启即丢），write memory 写回运行目录，copy running certified
    认证到基线，write memory flash-synchro 一步完成两者。回滚路径：目录内容不一致时重启自动回退。
  tags: [AOS, certified, working, running-directory, write-memory, 回滚]

- id: f02
  title: R8 开机引导序列与启动目录选择流程
  type: framework
  source_chapter: "p68"
  source_quote: |
    "System Boot Sequence: Bootstrap Basic Operation (U-Boot) / Hardware Initialization / Memory Diagnostics /
    Image selection / AOS is copied and loaded into RAM / The image contains its own copy of the kernel
    specific to the SW version"
  summary: |
    启动五步：U-Boot 引导 → 硬件初始化 → 内存诊断 → 镜像选择（按启动目录取 kernel.lnk）→ AOS 镜像
    连同自带内核加载进 RAM。结合 p81 规则：冷启动时若 running 目录（working 或 user-defined）与
    certified 内容（镜像+vcboot.cfg）一致则从 running 目录启动，不一致则回退 certified。
  tags: [AOS, 启动流程, U-Boot, 目录选择]

- id: f03
  title: Virtual Chassis 静态部署五步流程
  type: framework
  source_chapter: "p105-107"
  source_quote: |
    "Assign a Chassis ID / Assign a Chassis Group ID and a Priority / Configure VFL link & ports -Automatic or
    static / Restart Chassis to Virtual-Chassis Directory
    Assign a Chassis Group number: Must be the same on all the switches belonging to the Virtual Chassis.
    Define a Priority: Between 0 to 255, switch with the highest priority is elected Master."
  summary: |
    手工组建 VC 的标准顺序：(1) 每台分配全局唯一 chassis ID（必须互不相同）；(2) 分配相同的
    chassis-group 号并用 priority（0-255）预定 master；(3) 配置 VFL——auto 模式指定 auto-vf-link-port
    或 static 模式建 VFL ID 并挂成员口；(4) write memory；(5) 从含 vcsetup.cfg 的目录 reload 两台机箱。
  tags: [VC, chassis-id, chassis-group, priority, VFL, 部署流程]

- id: f04
  title: VC 主从同步流程（write memory flash-synchro / copy running certified）
  type: framework
  source_chapter: "p109-110"
  source_quote: |
    "-> copy running certified  This command can also be used to synchronize the virtual chassis
    -> write memory flash-synchro
    SYNCHRONIZATION STATUS / Flash Between CMMs : SYNCHRONIZED, / Running Configuration : SYNCHRONIZED"
  summary: |
    VC 中配置只保存在 master，write memory 后 show running-directory 会显示 "Flash Between CMMs:
    NOT SYNCHRONIZED"。用 copy running certified 或 write memory flash-synchro 把镜像和配置同步到
    所有 slave 的 certified 目录，状态转为 SYNCHRONIZED。slave 收到新镜像/配置后需重启才生效。
  tags: [VC, 同步, flash-synchro, copy-running-certified]

- id: f05
  title: ISSU 不中断升级流程
  type: framework
  source_chapter: "p101"
  source_quote: |
    "Upload new code, vcsetup.cfg and vcboot.cfg in a new directory (ex. issu_dir). Launch the dedicated issu
    command. The image and configuration files are then copied to all of the Slaves. The Slaves are then
    reloaded from the ISSU directory in order from lowest to highest chassis ID"
  summary: |
    ISSU 用于 VC 整体升级且业务影响最小：先把新代码+vcsetup.cfg+vcboot.cfg 上传到新目录（如
    issu_dir），执行 issu 命令，系统把文件复制到所有 slave，然后按 chassis ID 从小到大逐台从 ISSU
    目录重启，逐台升级而不是整机中断。
  tags: [VC, ISSU, 升级]

- id: f06
  title: 静态 VLAN 与 802.1Q 配置工作流
  type: framework
  source_chapter: "p127"
  source_quote: |
    "-> vlan 2
    -> vlan 2 members port <chassis/slot/port> untagged
    -> vlan 4 admin-state enable
    -> vlan 4 name Engineering
    -> vlan 10-15 100-105 200 name "Training Network"
    -> show vlan 4 / show vlan members / show ip interface"
  summary: |
    定义 VLAN → 加端口成员（untagged 或 tagged）→ 可选启用/命名（多词名称加引号，支持
    "vlan 10-15" 批量）→ show vlan / show vlan members 监控。802.1Q 侧（p140）：
    vlan 2-4 members port 1/1/24 tagged 把多个 VLAN 打标签送上同一链路。
  tags: [VLAN, 802.1Q, 配置工作流]

- id: f07
  title: 动态 VLAN（UNP）设备分类配置工作流
  type: framework
  source_chapter: "p133"
  source_quote: |
    "-> unp profile corporate / -> unp profile corporate map vlan 20
    -> unp profile def_unp / -> unp profile def_unp map vlan 10
    -> unp classification-rule rule1 mac-address-range 08:00:27:00:98:0A 08:00:27:00:98:FF
    -> unp classification-rule rule1 profile1 corporate
    -> unp port 1/1/1 port-type bridge / -> unp port 1/1/1 default-profile def_unp"
  summary: |
    设备导向动态 VLAN 六步：建 VLAN → 建 UNP profile 并 map vlan → 建默认 profile（兜底）→
    建分类规则（MAC/MAC 段/IP 等）并绑定 profile → 端口 port-type bridge 启用 UNP → 指定
    default-profile。验证：show unp user。
  tags: [UNP, 动态VLAN, classification, 配置工作流]

- id: f08
  title: LACP 动态链路聚合配置工作流
  type: framework
  source_chapter: "p201"
  source_quote: |
    "Configuring a Dynamic Link Aggregation Group / Assigning ports to the Dynamic Link Aggregation Group
    -> linkagg lacp agg <agg_num> size <size> admin-state enable
    -> linkagg lacp agg <agg_num> actor admin-key <actor_admin_key>
    -> linkagg lacp port <chassis/slot/port> actor admin-key <actor_admin_key>"
  summary: |
    三步建动态聚合：(1) linkagg lacp agg N size X 建组并分配 actor admin-key；(2) 把物理口按同一
    admin-key 绑进组（admin-key 仅本地有效，无需与组号一致）；(3) 激活端口 admin-state enable。
    VLAN 挂载用 vlan <id> members linkagg <n> untagged|tagged。监控 show linkagg / show linkagg port。
  tags: [LACP, linkagg, admin-key, 配置工作流]

- id: f09
  title: STP 配置工作流（模式→协议→优先级→路径成本→监控）
  type: framework
  source_chapter: "p231-236"
  source_quote: |
    "-> spantree mode {flat | per-vlan}
    -> spantree [cist | vlan vlan_id] protocol {stp | rstp | mstp}
    Ex: ->spantree vlan 20 priority 20000  Ex: ->spantree vlan 200 port 2/1/1 priority 15
    -> spantree path-cost-mode {auto | 32bit}
    -> show spantree vlan 20 ports active"
  summary: |
    顺序化配置：先选模式（flat=每机一实例 / per-vlan=每 VLAN 一实例，默认 per-vlan），再选协议
    （stp/rstp/mstp），然后按 VLAN 调 bridge priority 或端口 priority/path-cost，必要时设
    path-cost-mode，最后 show spantree [vlan N] [ports] 验证根桥、端口角色与阻塞状态。
  tags: [STP, RSTP, priority, 配置工作流]

- id: f10
  title: DHL Active-Active 双归属配置工作流
  type: framework
  source_chapter: "p257-259"
  source_quote: |
    "-> dhl 1
    -> dhl 1 linka linkagg 1 linkb linkagg 2
    -> dhl 1 vlan-map linkb 30
    -> dhl 1 admin-state enable
    -> dhl 1 mac-flushing raw / -> dhl 1 mac-flushing mvrp"
  summary: |
    DHL 会话五步：建唯一会话 ID → 把 linkA/linkB 绑到端口或 linkagg（两链路须同属一个默认 VLAN）→
    vlan-map 指定 linkB 承载的 VLAN（其余自动归 linkA）→ admin-state enable（DHL 端口上 STP 自动
    禁用）→ 配置 MAC 冲刷方式（raw / mvrp，默认 none）。监控 show dhl [1 [linka|linkb]]。
  tags: [DHL, 双归属, 高可用, 配置工作流]

- id: f11
  title: VRRP 网关冗余配置工作流（基础+优先级+跟踪）
  type: framework
  source_chapter: "p301-303"
  source_quote: |
    "ip vrrp 1 interface int_20
    ip vrrp 1 interface int_20 address 192.168.20.254
    ip vrrp 1 interface int_20 priority 100 preempt interval 100
    ip vrrp 1 interface int_20 admin-state enable
    -> ip vrrp track 3 admin-state enable priority 30 port 1/1/3
    -> ip vrrp 1 interface int_20 track-association 3"
  summary: |
    建 VRID 并绑定 IP 接口 → 配虚拟 IP（两台共用）→ 可调 priority（默认 100，大者优先做 master）/
    preempt（默认允许抢占）/interval → admin-state enable。跟踪：先建 track 策略（端口/IP/VLAN 等，
    失败降 priority），再 track-association 绑到虚拟路由器。监控 show ip vrrp [statistics]。
  tags: [VRRP, 网关冗余, tracking, 配置工作流]

- id: f12
  title: QoS/ACL 策略三元组工作流（condition→action→rule→apply）
  type: framework
  source_chapter: "p317-328"
  source_quote: |
    "policy condition client_traffic source vlan 20
    policy action priority_5 802.1p 5
    policy rule rule1 condition client_traffic action priority_5
    qos apply
    A policy (or a policy rule) is made up of: 1. a condition 2. an action"
  summary: |
    所有 QoS/ACL 共用一套策略引擎：policy condition 定义匹配条件（L1-L4：端口/MAC/VLAN/IP/端口/
    服务/DSCP 等），policy action 定义动作（priority/bandwidth/802.1p 标记/redirect/mirror/
    disposition 等），policy rule 把条件与动作（及 precedence、log、count）组装，最后 qos apply
    下发生效。规则未 apply 不激活；可用 policy group（port/mac/network/service）复用条件。
  tags: [QoS, ACL, policy, condition, action, rule, 配置工作流]

- id: f13
  title: Access Guardian（UNP+802.1X/MAC 认证）部署工作流
  type: framework
  source_chapter: "p389"
  source_quote: |
    "-> aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent
    -> aaa authentication 802.1x my_radius
    -> unp profile corporate / -> unp profile corporate map vlan 20
    -> unp port 1/1/1 port-type bridge / -> unp port 1/1/1 default-profile def_unp
    -> unp port-template 802.1X-template / -> unp port 1/1/1 port-template 802.1x-template"
  summary: |
    部署顺序：声明 RADIUS 服务器并挂 802.1x/MAC 认证与计费 → 建 VLAN 与 UNP profile（map vlan、
    可挂 qos-policy-list/location-policy/period-policy）→ 端口 port-type bridge + 认证方式
    （802.1x/mac）+ default-profile → 可选 port-template 批量下发认证参数与 pass-alternate 兜底
    profile。认证成功后 RADIUS 以 Filter-Id 返回 profile 名自动套用。
  tags: [Access Guardian, UNP, 802.1x, RADIUS, 配置工作流]

- id: f14
  title: 软件升级工作流（镜像+U-Boot/FPGA+认证）
  type: framework
  source_chapter: "p452-456"
  source_quote: |
    "-> update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz
    -> update fpga-cpld cmm all file fpga_kit_3312
    -> reload from working no rollback-timeout
    -> copy running certified
    Note: If there are any issues after upgrading the switch can be rolled back to the previous certified version"
  summary: |
    升级流程：先读 release note 分析内存/U-Boot/FPGA 要求 → 从 BPWS 下载解压对应型号镜像 →
    FTP/SFTP/USB/WebView 把升级文件传入 running 目录 → reload from working 验证运行与网络稳定 →
    copy running certified 固化；需要时先 update uboot / update fpga-cpld。出问题可回滚旧 certified。
  tags: [升级, uboot, fpga, certified, 配置工作流]
```

### principles

```yaml
- id: p01
  title: AOS CLI 行规：缩写补全、管道过滤、? 帮助与历史
  type: principle
  source_chapter: "p77"
  source_quote: |
    "Completion: Recognize partial keywords to CLI command syntax. Eg : sh vl for show vlan
    Built-in Filtering: -> show vlans | more / -> show mac-learning | grep 00:20:da:55:56:76
    Online Help: A '?' can be used to get a list of all possible commands"
  summary: |
    AOS CLI 四条通用规则：(1) 支持部分关键字补全（sh vl = show vlan）；(2) 内置管道过滤
    |more / grep / egrep / sort / less；(3) '?' 在线帮助列出可用参数；(4) history 查看命令历史；
    目录管理沿用 Unix 命令（pwd/cd/mkdir/ls/dir/mv/cp/rm）。
  tags: [CLI, 语法, 帮助, 过滤]

- id: p02
  title: Flash 目录结构与每型号镜像文件命名
  type: principle
  source_chapter: "p67"
  source_quote: |
    "FLASH MEMORY: WORKING / CERTIFIED / NETWORK / USER. DIR. ... Configuration files vcboot.cfg vcsetup.cfg
    ... image files (AOS): Nosa.img Nos.img Wos.img Uos.img Uosn.img kaos.img Tos.img Yos.img ..."
  summary: |
    每个目录（working/certified/user-defined）由三件套构成：AOS 镜像（型号专属命名，如 6360 用
    Nos.img、6900 V72/C32 系用 kaos.img 等）、vcboot.cfg（启动配置）、vcsetup.cfg（VC 设置）。
    certified 是授权基线，working 是待测试暂存，user 目录由用户自建可存多套配置。
  tags: [目录结构, vcboot.cfg, vcsetup.cfg, 镜像]

- id: p03
  title: Running directory 与 running configuration 的定义
  type: principle
  source_chapter: "p80"
  source_quote: |
    "The running directory is the directory where the configuration changes will be saved. The running
    configuration, stored in the RAM, contains the current operating parameters of the OmniSwitch obtained
    from the image and configuration files."
  summary: |
    running directory = 交换机启动时加载的目录（certified/working/user-defined 之一），是 write
    memory 的落盘目标；running configuration = RAM 中的当前运行参数，等于启动目录内容叠加用户
    未保存的改动。例外：running directory 是 certified 时无法保存任何改动。
  tags: [running-directory, running-config, RAM]

- id: p04
  title: 冷启动目录选择规则：内容一致从 running 启动，不一致回退 certified
  type: principle
  source_chapter: "p81"
  source_quote: |
    "At the time of a normal boot (cold start): The switch will reboot from certified directory if contents
    (images and vcboot.cfg) are different from the running directory... If contents are the same, the switch
    will reboot from the running directory"
  summary: |
    判断依据是"镜像 + vcboot.cfg"是否一致：working/user 目录与 certified 相同 → 从 running 目录
    启动；不同 → 自动回退 certified 启动。show running-directory 的 Certify/Restore Status
    （CERTIFIED / CERTIFY NEEDED）即指示这一比较结果。
  tags: [启动规则, certified, 回退]

- id: p05
  title: 三条保存命令的语义层级（write memory / copy running certified / flash-synchro）
  type: principle
  source_chapter: "p70-71"
  source_quote: |
    "sw7 (OS6860-A) -> write memory
    sw7 (OS6860-A) -> copy running certified
    sw7 (OS6860-A) -> write memory flash-synchro = write memory + copy running certified"
  summary: |
    write memory 只把 RAM 配置写回 running 目录（working 变 CERTIFY NEEDED）；copy running
    certified 把运行配置连同镜像覆盖 certified（仅验证后使用）；write memory flash-synchro 是组合
    命令，一次完成保存+认证，VC 场景下还会同步所有成员。
  tags: [write-memory, certified, flash-synchro]

- id: p06
  title: Certified 运行模式锁定规则：不可保存、不可搬文件
  type: principle
  source_chapter: "p73"
  source_quote: |
    "When the switch boots from the CERTIFIED directory, changes made to the switch cannot be saved and
    files cannot be moved between directories."
  summary: |
    running directory 是 certified 时进入锁定态：CLI 改动只在 RAM 生效，write memory 报错，目录
    间文件移动被禁止。要恢复可保存状态，必须 reload from working（或 user 目录）切回非 certified
    运行目录。
  tags: [certified, 锁定, write-memory]

- id: p07
  title: 配置备份/恢复：configuration_backup.tar 与 10 份上限
  type: principle
  source_chapter: "p74"
  source_quote: |
    "The configuration backup command creates a .tar file where are stored the collected files. The tar file
    name is "configuration_backup.tar" and will be placed in "/flash/config-backup-recovery" folder.
    Up to 10 .tar files can be stored"
  summary: |
    备份内容为会话 banner、userTable（用户表）和 vcboot.cfg，打包成 configuration_backup.tar 存于
    /flash/config-backup-recovery，最多保留 10 份；restore 时从该目录解包恢复三类文件。
  tags: [备份, restore, config-backup]

- id: p08
  title: USB 备份/恢复规则（usb backup / auto-copy，可加密）
  type: principle
  source_chapter: "p75"
  source_quote: |
    "If a USB drive is plugged in, switch will store image files, power supply and system configuration files
    to USB storage drive automatically upon user commands "write memory" or "copy running-certified"
    "copy flash-synchro" if USB backup is enabled.
    usb backup admin-state {enable | disable} [key <> | hash-key<>]"
  summary: |
    usb backup admin-state enable 后，write memory / copy running certified / write memory
    flash-synchro 会把 certified 与 running 目录的镜像和配置复制到 /uflash/<型号>/<目录>；新设备
    用 usb auto-copy 可从 U 盘恢复；启用时配的 key 会让备份内容加密。
  tags: [USB, 备份, auto-copy]

- id: p09
  title: 默认账户与本地用户库规则（admin/switch、userTable9、64 用户）
  type: principle
  source_chapter: "p38-39"
  source_quote: |
    "The Local userDB file is named userTable9. Path: flash/system directory. By default : 2 users "admin
    and default". Login : admin Password : switch. Up to 64 users can be configured in the local switch
    database. Beginning in 8.10R3 a warning message will be displayed urging for the default password to be
    changed... Beginning in 8.10R4 changing the default password will be mandatory."
  summary: |
    出厂默认只有 admin/switch（另有 default 账户），本地用户库文件 userTable9 存于 /flash/system，
    最多 64 个用户，权限按命令域/族划分读写。8.10R3 起登录 admin 提示改默认密码，8.10R4 起强制
    修改；可用 user password-refresh 强制下次登录刷新密码。
  tags: [账户, admin, 密码, userTable]

- id: p10
  title: AAA 多服务器 fail-through 与 exit-on-fail 语义
  type: principle
  source_chapter: "p41"
  source_quote: |
    "aaa authentication {console | telnet | ftp | http | snmp | ssh | default} server1 [server2...] [local]
    [exit-on-fail {enable | disable}]
    exit-on-fail Configures if the switch must authenticate using all servers in the list or only the first
    available server."
  summary: |
    一条 aaa authentication 可声明多个认证服务器（RADIUS/LDAP/local 依次排队）。exit-on-fail
    enable=只用列表里第一台可用服务器；disable=逐台尝试（fail-through）。例：aaa authentication
    default Radius01 Radius02 local。no aaa authentication http 可直接拒绝 HTTP 管理接入。
  tags: [AAA, radius, exit-on-fail, 认证]

- id: p11
  title: 管理会话数规格（Telnet 6 / SSH 8 / 总 20 / SNMP 50）
  type: principle
  source_chapter: "p45"
  source_quote: |
    "Telnet (V4 or V6) 6 / FTP (V4 or V6) 4 / SSH + SFTP (V4 or V6 secure session) 8 / HTTP 4 /
    Total sessions (Secure Shell, Telnet, FTP, HTTP, and console) 20 / SNMP 50"
  summary: |
    并发管理会话上限：Telnet 6、FTP 4、SSH+SFTP 8、HTTP 4，五类合计（含 console）20，SNMP 50。
    SSH 公钥认证支持 Password 与 DSA/RSA/ECDSA 公钥。规划带外管理规模时按此约束。
  tags: [会话数, telnet, ssh, snmp, 规格]

- id: p12
  title: Lightning Configuration（易配置模式）触发条件
  type: principle
  source_chapter: "p51"
  source_quote: |
    "The easy configuration process (Lightning configuration) starts if: Only first or second physical port
    connected with the client, no other ports connected / No prior switch configuration exist / No DHCP
    address assignment occurs after boot up / No remote configuration load (RCL) server and OmniVista NMS
    connection exists"
  summary: |
    出厂新机仅当：只连 1/1/1-2 口、无已有配置、启动后没拿到 DHCP 地址、无 RCL/NMS 连接时，才进入
    Lightning 模式（默认 VLAN1 192.168.0.1/24，给客户端发 192.168.0.200，仅 HTTPS 经 1/1/1-2 访问）。
    一旦 write memory 保存过配置，默认 IP 即被内部移除。
  tags: [lightning, 零配置, webview]

- id: p13
  title: VC Master 选举四准则（priority → uptime → chassis ID → MAC）
  type: principle
  source_chapter: "p95"
  source_quote: |
    "Master/Slave election based on virtual chassis protocol (ISIS-VC)
    Highest chassis priority value / Longest chassis uptime (if difference in uptime >10 mn) /
    Smallest Chassis ID value / Smallest chassis MAC address"
  summary: |
    ISIS-VC 选 master 依次比较：chassis priority 最大者胜（0-255）；优先级平手且开机时长差
    >10 分钟则开机久者胜；再看 chassis ID 最小；最后比机箱 MAC 最小。想固定 master 就显式把
    优先级调大（如 200）。
  tags: [VC, 选举, priority, ISIS-VC]

- id: p14
  title: VC Takeover/Failover 行为规则（新 master 不让位）
  type: principle
  source_chapter: "p96"
  source_quote: |
    ""MAC retention" is always enabled. When the master reloads or fails, the slaves reelect a new master...
    When the "original" master comes back, no election will be processed, and the "new" Master will retain
    its Master role"
  summary: |
    master 故障只影响自身，slave 流量不受损；MAC retention 恒开启，slave 本地重选出新 master 并
    确认。原 master 恢复后不重新选举，新 master 保持角色，原 master 以 slave 身份回归——避免二次
    抖动。
  tags: [VC, failover, mac-retention]

- id: p15
  title: Auto VFL 默认候选端口矩阵
  type: principle
  source_chapter: "p98"
  source_quote: |
    "Auto VFL detection process will run only on auto VFL ports. Both ends of the link must be auto VFL
    ports for an auto VFL port to be able to become VFL.
    OS6360-24 ports models - Ports 27/28. OS6360-48 ports models - Ports 51/52."
  summary: |
    auto VFL 检测只在两端都是 auto VFL 候选口的链路上运行；vcsetup.cfg 已存在时仅对显式配置的
    auto-vf-link-port 生效。默认候选口按型号：OS6900 X/T=每槽最后 5 口，6360-24 用 27/28、
    6360-48 用 51/52，6465-P28 用 27/28，6560X4 用专用 VFL 口+最后两个 10G SFP+，9900 仅静态。
  tags: [VC, auto-vfl, 端口矩阵]

- id: p16
  title: VC 脑裂防护：RCD 与 VC Split Protocol 的处理规则
  type: principle
  source_chapter: "p99-100"
  source_quote: |
    "The former Slave chassis will shutdown all its front-panel user ports to prevent duplicate IP and
    chassis MAC addresses in the network. The Slave's chassis status will be modified from Running to
    Split-Topology... Use the virtual-chassis split-protection admin-state and ... helper linkagg commands
    to enable VCSP"
  summary: |
    VFL 全断会造成 MAC/IP 重复。带外：EMP 上的 RCD 协议检测到 split 后，前 slave 关闭全部用户口
    （状态 Split-Topology），VFL 恢复后自动重启回归。带内：VCSP 借助上/下游 helper 交换机经
    VCSP LAG 检测，推荐每个 VC 成员各出一口到 helper。
  tags: [VC, split, RCD, VCSP, 脑裂]

- id: p17
  title: VC chassis-group 与 priority 参数规则
  type: principle
  source_chapter: "p106"
  source_quote: |
    "Assign a Chassis Group number: Must be the same on all the switches belonging to the Virtual Chassis.
    Define a Priority: Between 0 to 255, switch with the highest priority is elected Master.
    Assign a Chassis ID: Must be different for each switch belonging to the Virtual Chassis"
  summary: |
    组网三参数约束：chassis-group 全 VC 成员必须相同（不同组的机器不成 VC）；chassis ID 每台必须
    唯一；priority 0-255、最大者当选 master。改 chassis ID 或 priority 后必须 write memory 并
    reload 才生效。
  tags: [VC, chassis-group, priority, 参数]

- id: p19
  title: VLAN oper 状态与 IP 接口联动规则（无活动成员则 DOWN）
  type: principle
  source_chapter: "p135"
  source_quote: |
    "IP routing is active as soon as at least one IP interface is associated with a VLAN
    The operational status of a VLAN remains inactive as long as no active port is associated with this VLAN"
  summary: |
    IP 接口绑定 VLAN 后：VLAN 没有任何 active 成员口 → IP 接口 Status=DOWN、Forward=NO，不响应
    ping、不进路由更新，但不影响 L2 广播域；端口 link up 成员变为 forwarding 后接口才 UP。
    排障第一步就是 show vlan members 看有没有 active 口。
  tags: [VLAN, ip-interface, 联动, 排障]

- id: p20
  title: 802.1Q 标签规则：4096 个 tag、802.1p 3bit、物理口恒有一个桥接 VLAN
  type: principle
  source_chapter: "p139"
  source_quote: |
    "VLAN Tag: 802.3 MAC header change / 4096 unique VLAN Tags (addresses) / VLAN ID == GID == VLAN Tag
    802.1P: Three-bit field within 802.1Q header / Allows up to 8 different priorities"
  summary: |
    802.1Q 在 MAC 头插入 4 字节 tag：12bit VLAN ID（4096 个）+3bit 802.1p 优先级（8 级），需硬件
    支持。规则（p222）：物理口永远有且仅有一个 VLAN 以 untagged 桥接（端口默认 VLAN），其余
    VLAN 以 tagged 传送——trunk 两端要对同一组 VLAN 打标签。
  tags: [802.1Q, 802.1p, tagging]

- id: p21
  title: UNP 分类规则次序与三种规则优先级
  type: principle
  source_chapter: "p129-132"
  source_quote: |
    "UNP Port classification rules: 1. Port/Linkagg 2. Domain 3. MAC address 4. MAC-OUI 5. MAC address range
    6. LLDP 7. Auth-type 8. IP address 9. VLAN tag
    Precedence: Extended rule > Binding Rule > Simple Rule"
  summary: |
    收到帧后按 9 级次序匹配分类规则（Port/Linkagg 最先，VLAN tag 最后）；规则组合方式优先级为
    Extended rule（命名规则列表，可设 precedence）> Binding rule（多条件与）> Simple rule（单条件）。
    认证关闭或失败时 UNP 分类规则直接作用于端口流量。
  tags: [UNP, 分类规则, 优先级]

- id: p22
  title: swlog 日志参数与文件轮转规则
  type: principle
  source_chapter: "p161-162"
  source_quote: |
    "Switch events can be logged to Switch console / Local text file (Configurable default file size 1250
    Kbytes) / Multiple remote devices (syslog) 12 max
    Up to 8 Swlog logs files can be stored in the /flash directory (from swlog_chassis1 to 1.6).
    An Swlog archive can store up to 40 files"
  summary: |
    swlog 默认运行并输出到 console+flash；单文件默认 1250KB（swlog output flash-file-size 可改），
    /flash 下轮转 swlog_chassis1~1.6 共 8 个文件，swlog_archive 归档最多 40 个；syslog 远端最多
    12 台。默认 console 显示级别 info（数值 6）。
  tags: [swlog, syslog, 日志轮转]

- id: p23
  title: swlog 严重级与应用 ID 调级规则
  type: principle
  source_chapter: "p164-166"
  source_quote: |
    "Default severity level is "info". The numeric equivalent for the level "info" is 6. It is also possible
    to assign different severity levels to different switch applications
    sw1 (6900-A) -> swlog appid ospf_0 subapp all level 8"
  summary: |
    所有进程默认级别 6（info）。可按 appid（ospf_0、stpCmm、vcmCmm 等百余个）甚至 subapp
    （如 ospf hello）单独调级（1-8 或名称如 debug3）。Readable Customer Event 用 swlog appid all
    subapp all level event + show log events 输出客户可读事件。
  tags: [swlog, severity, appid]

- id: p24
  title: 命令日志（command-log）规则：100 条、需启用、删文件即删史
  type: principle
  source_chapter: "p171"
  source_quote: |
    "Creates command.log file in /flash directory / Command results stored in command.log / Deleting
    command.log deletes log history / Cannot be deleted while command logging is enabled / Stores 100 most
    recent commands / Must be enabled -> command-log enable/disable"
  summary: |
    command-log 记录命令、用户、时间、来源 IP 与执行结果（含报错原文），存 /flash/command.log；
    默认关闭须 command-log enable；只保留最近 100 条；日志开启期间文件不可删。审计"谁改了配置"
    的第一工具。
  tags: [command-log, 审计]

- id: p25
  title: 端口镜像（Port Mirroring）规格：同速端口、4 会话、4 个 MTP 索引
  type: principle
  source_chapter: "p174-175"
  source_quote: |
    "Port requirements - must be of identical capacity
    The same destination port can be used in different port mirroring sessions and the maximum port-mirroring
    sessions has been increased from 2 to 4. There is a limit of 4 Mirror-to-port (MTP) indexes.
    Bi-directional counts as two MTP indexes"
  summary: |
    镜像源/目的口容量必须相同；8.9R3 起 6860(E)/6860N/6865/6900 最多 4 个会话、4 个 MTP 索引，
    双向镜像每个目的口占 2 个索引；同一目的口可被多会话复用（同向只计 1 次）。6560（8.9R3）支持
    经 linkagg 做远程镜像。
  tags: [port-mirroring, MTP, 抓包]

- id: p26
  title: 端口监控（Port Monitoring）规格：单会话、64 字节、默认 64KB
  type: principle
  source_chapter: "p177"
  source_quote: |
    "Captures first 64-bytes of frame / Session supported per switch or stack: 1 / Default file size: R8: 64
    KB (max = 2 MB) / Round-Robin or stop capture when max storage reached / Cannot use port monitoring and
    mirroring on the same port"
  summary: |
    端口监控把抓包以 Sniffer（.enc）格式存到 /flash（默认 pmonitor.enc）：每交换机/堆叠仅 1 个
    会话，每帧只抓前 64 字节，文件默认 64KB、最大 2MB，写满可轮转或停止；支持 pause/resume/
    disable/timeout；与端口镜像不能落在同一物理口。
  tags: [port-monitoring, 抓包, enc]

- id: p27
  title: 静态 vs 动态链路聚合限制（静态仅 OmniSwitch 间、组内同速）
  type: principle
  source_chapter: "p199"
  source_quote: |
    "Static: Port parameters MUST be exactly the same at both ends and within the group. same speed...
    Only works between Alcatel-Lucent OmniSwitches
    Dynamic: IEEE 802.3ad LACP. LACP will negotiate the optimal parameters for both ends using LACPDU...
    It also works between two different devices such as switches, servers and storage systems."
  summary: |
    静态聚合两端与组内端口参数必须完全一致（同速），且只能在 OmniSwitch 之间用；动态 LACP 用
    LACPDU 自动协商参数、组内同速即可，可跨厂商连接服务器/存储。异构组网一律选 LACP。
  tags: [linkagg, LACP, 静态, 限制]

- id: p28
  title: hash-control 负载哈希算法与各型号默认值
  type: principle
  source_chapter: "p206"
  source_quote: |
    "Two hashing algorithms available: Brief Mode (UDP/TCP ports not included, Only Source IP and destination
    IP) / Extended (UDP/TCP ports to be included)
    Switch Default Hashing Mode: 9900 extended / 6900 brief / 6870 extended / 6860 extended / 6865 extended
    / 6560 extended / 6465 brief / 6360 brief"
  summary: |
    聚合/ECMP/SLB 的哈希可全局切换：brief 只用源/目 IP；extended 纳入 UDP/TCP 端口、分流更均匀。
    默认值按型号：6900、6465、6360 为 brief，9900/6870/6860/6865/6560 为 extended。命令
    hash-control brief | extended。组播默认走聚合主端口，启用 non-ucast 选项才参与哈希（p207）。
  tags: [hash-control, 负载均衡, 默认值]

- id: p29
  title: STP 两种模式三种协议与收敛时间（默认 per-vlan + RSTP）
  type: principle
  source_chapter: "p227"
  source_quote: |
    "Supports two Spanning Tree operating modes: flat (single STP instance per switch) / per-VLAN (single STP
    instance per VLAN) (By default on OmniSwitch)
    STP (802.1d): Convergence time: 50 secs / RSTP (802.1w): < 1 sec / MSTP (802.1s): < 1 sec"
  summary: |
    OmniSwitch 默认 per-vlan（1x1）模式，即每 VLAN 一个 STP 实例；flat 为整机单实例。协议收敛：
    802.1d 约 50 秒，802.1w/802.1s 亚秒。show spantree 可见每 VLAN 的协议与优先级。
  tags: [STP, per-vlan, flat, 收敛时间]

- id: p30
  title: STP 默认路径成本表（16bit 与 32bit 两套）
  type: principle
  source_chapter: "p228"
  source_quote: |
    "IEEE Recom. Value - 16 bit: 10 Mbps 100 / 100 Mbps 19 / 1 Gbps 4 / 10 Gbps 2
    IEEE Recom. Value - 32 bit: 10 Mbps 2,000,000 / 100 Mbps 200,000 / 1 Gbps 20,000 / 10 Gbps 2,000"
  summary: |
    802.1d/w 用 16bit 成本（10M=100、100M=19、1G=4、10G=2）；802.1s 用 32bit 成本
    （10M=2,000,000 … 10G=2,000）。path-cost-mode auto 表示随激活协议自动选 16/32bit，
    也可强制 32bit。
  tags: [STP, path-cost, 默认值]

- id: p31
  title: STP priority 与 path-cost 参数范围
  type: principle
  source_chapter: "p234"
  source_quote: |
    "A bridge or port priority value. The valid range for the bridge priority is 0-65535. The valid range for
    the port priority is 0-15. If MSTP is the active flat mode protocol, enter a value that is a multiple of
    4096. Path cost 0 -> 65535 for 16-bit, 0 -> 200000000 for 32-bit - Default: 0"
  summary: |
    网桥优先级 0-65535（默认 32768/0x8000）；端口优先级 0-15；MSTP 平面模式下网桥优先级须为
    4096 的倍数。端口路径成本 16bit 0-65535、32bit 0-200000000、默认 0。控制根桥用
    spantree vlan N priority X（越小越优，比 MAC 更可控）。
  tags: [STP, priority, path-cost, 参数范围]

- id: p32
  title: DHL 会话约束与定时器/冲刷参数
  type: principle
  source_chapter: "p252-253"
  source_quote: |
    "Only one session per switch is allowed. Each session has only two links (linkA and linkB). A physical
    port or a link aggregate (linkagg) ID could be a DHL link. The same port or link aggregate is not
    configurable as both linkA or linkB. DHL is not supported on mobile, 802.1x-enabled, GVRP, or UNI ports
    Pre-Emption timer: 0 to 600 seconds"
  summary: |
    每台交换机只允许 1 个 DHL 会话、恰好 2 条链路（物理口或 linkagg，不能同口兼任 A/B）；mobile、
    802.1x、GVRP、UNI 口不支持。DHL 端口上 STP 自动禁用；pre-emption timer 0-600 秒（Lab 默认
    30 秒）决定故障恢复后回切等待；MAC 冲刷三选一：raw / mvrp / none（默认，保留过期 MAC）。
  tags: [DHL, pre-emption, mac-flushing, 约束]

- id: p33
  title: DHCP Relay 两种模式互斥与默认参数
  type: principle
  source_chapter: "p275-277"
  source_quote: |
    "Two types of DHCP relay agents: global and per-interface... They are mutually exclusive.
    By default, the DHCP Relay feature is disabled.
    Max number of hops = 16, Forward Delay(seconds) = 0, DHCP Relay Opt82 Format = Base MAC"
  summary: |
    DHCP relay 默认关闭；全局模式（ip dhcp relay destination + admin-state enable，任意 VLAN 的
    DHCP 包都转发）与接口模式（ip dhcp relay per-interface-mode + interface if_name destination）
    互斥只能选一。默认最大跳数 16、转发延迟 0、Option-82 格式 Base MAC。相关：UDP Relay 可按
    服务（tftp/dns/ntp 等）定向转发（p279）。
  tags: [DHCP, relay, option82, 默认值]

- id: p34
  title: Loopback0 接口规则与用途
  type: principle
  source_chapter: "p282"
  source_quote: |
    "Identify a consistent address for network management purposes / Not bound to any VLAN / Always remain
    operationally active (as long as at least one VLAN is active) / Automatically advertised by RIP and OSPF
    protocols when the interface is created (not by BGP)"
  summary: |
    接口名取 Loopback0 即创建/32 环回口：不绑 VLAN、只要有一个 VLAN active 就恒 UP；创建即被
    RIP/OSPF 自动宣告（BGP 除外）。典型用途：NMS 标识、RADIUS/NTP 源 IP、sFlow agent、OSPF
    router-id、BGP peering、PIM RP。配源接口用 ip service source-ip loopback0 <应用>。
  tags: [loopback0, 管理地址, source-ip]

- id: p35
  title: 静态路由规则：静态优于动态、metric 定主备
  type: principle
  source_chapter: "p285-286"
  source_quote: |
    "Gateway or NextHop address is mapped to a particular interface on the switch. Associated interface needs
    to be up and running. By default, static routes have preference over dynamic routes. Priority can be set
    by assigning a metric value
    -> ip static-route 0.0.0.0/0 gateway 1.1.1.1 metric 1 / -> ip static-route 0.0.0.0/0 gateway 2.2.2.2 metric 2"
  summary: |
    ip static-route <目的/掩码> gateway <下一跳> [metric …]；下一跳接口必须 up 路由才有效。静态
    路由默认优先于动态路由；多条默认路由用 metric 排主备（metric 1 为主、2 为备）。show ip router
    database 可见 inactive 静态路由。
  tags: [静态路由, metric, 默认路由]

- id: p36
  title: VRRP 关键参数与虚拟 MAC 规则
  type: principle
  source_chapter: "p297-302"
  source_quote: |
    "Multicast - 224.0.0.18 / Virtual MAC address: 00-00-5E-00-01-{VRID}
    At least two virtual routers must be configured on the LAN-a master router and a backup router.
    ip vrrp 1 interface int_20 priority 100 preempt interval 100"
  summary: |
    VRRP 通告走组播 224.0.0.18；虚拟 MAC 固定为 00-00-5E-00-01-{VRID}，master 切换不改 MAC，
    终端无需重新 ARP。默认 priority 100（大者为 master，全部相等则比较 router ID）、preempt
    默认允许（可 no pre-empt 关闭）、V2 同 VRID 实例须用相同 interval。改优先级前必须先禁用
    实例。
  tags: [VRRP, VRID, 虚拟MAC, preempt]

- id: p37
  title: QoS 默认值与生效规则（默认启用、802.1p 默认 0、端口默认不信任）
  type: principle
  source_chapter: "p318-326"
  source_quote: |
    "By default, QoS is enabled on the switch... disposition Default: Accept
    By default, the port default values for 802.1p and ToS/DSCP are 0... By default, switched ports are
    untrusted. (p346) The global setting is active immediately; however, modifying a port configuration
    requires qos apply to activate the change."
  summary: |
    QoS 默认启用；端口默认 802.1p/ToS/DSCP 值为 0、默认 untrusted（untrusted 口的流量统一按
    default 值重标）；策略 disposition 默认 accept（未命中任何规则的流默认放行）。端口级修改必须
    qos apply 才生效；qos flush 清策略、qos reset 回默认、qos revert 删 pending 配置。
  tags: [QoS, 默认值, qos-apply, trust]

- id: p38
  title: IP 电话流量自动优先级（alaPhones MAC 组，优先级 5）
  type: principle
  source_chapter: "p333"
  source_quote: |
    "Automatic Prioritization for IP Phone Traffic / Enable by default on the switch
    Mac adress = ALE Phone > Priority 5 / Non ALE Phone > Default / On trusted and un-trusted ports
    -> qos phones [priority priority_value | trusted] / -> qos no phones"
  summary: |
    交换机默认按 alaPhones MAC 组（00:80:9F、78:81:02、00:13:FA、48-7A-55 等 ALE/厂商话机段）
    识别话机流量并给优先级 5，trusted/untrusted 口都生效。qos phones priority N 改值、qos phones
    trusted 改为仅信任、qos no phones 关闭；追加话机段需重定义 policy mac group alaPhones。
  tags: [QoS, IP电话, auto-qos]

- id: p39
  title: PoE 标准/预算规则与端口优先级、延迟上电
  type: principle
  source_chapter: "p434-441"
  source_quote: |
    "802.3af: 15.40 W (EPS max) / 802.3at Type 2: 30.0 W / 802.3bt Type 3: 60 W / Type 4: 100 W
    Default priority level for a port is low... Critical: In the event of a power management issue, inline
    power to critical ports is maintained as long as possible
    <num> - specific delay value in seconds in multiples of 5. Value should be within 120 to 600 seconds"
  summary: |
    PoE 档位：af=15.4W、at(PoE+)=30W、bt Type3=60W、bt Type4=100W（型号带 P 才支持，预算查规格
    书）。端口优先级 low（默认，先断电）/high/critical（尽量保电）。FPoE/PPoE 用于快速与不断电
    供电（6360-P10A 不支持）；delayed-start 可延迟 120-600 秒（5 的倍数）上电等系统稳定，启用后
    不支持 FPoE/PPoE，且必须 write memory 才在重启后生效。
  tags: [PoE, 功率表, 优先级, delayed-start]

- id: p40
  title: LLDP 默认行为与配置层级规则
  type: principle
  source_chapter: "p409"
  source_quote: |
    "IEEE 802.1AB - Link Layer Discovery Protocol (LLDP) / L2 discovery protocol / Enabled by default on the
    OmniSwitches (p423) LLDP is configured at port level (or NI or chassis), but not at linkagg level."
  summary: |
    LLDP（802.1AB）默认收发双开，周期发 TLV（chassis ID/port ID/TTL+可选 802.1/802.3/MED 扩展）
    维护邻居库。配置层级只有端口/槽位(chassis)，不能在 linkagg 上配。可按口开关 lldpdu
    tx/rx/tx-and-rx/disable、notification 开关与 TLV 管理字段（system-name、
    management-address 等）。LLDP-MED 用于话机策略下发（network policy TLV：VLAN+L2 优先级+DSCP）。
  tags: [LLDP, LLDP-MED, 默认开启]
```

### cases

```yaml
- id: c01
  title: Lab 远程交换机访问（SSH + WebView 建删 VLAN）
  type: case
  source_chapter: "p54-63"
  source_quote: |
    "sw3 (6560-A) -> session cli timeout 60
    sw3 (6560-A) -> write memory
    File /flash/working/vcsetup.cfg replaced. File /flash/working/vcboot.cfg replaced.
    sw3 (6560-A) -> show aaa authentication ... Service type = Ssh / 1st authentication server = local
    Vlan : 59 / Description : Student / sw3 (6560-A) -> show vlan"
  summary: |
    首个 Lab：先用 show aaa authentication 确认 SSH/HTTP 用本地库认证（若 denied 用 aaa
    authentication ssh local），Tera Term SSH 登录（admin/switch）；改 CLI 不活动超时 session cli
    timeout 60 并 write memory；再走 WebView（https://管理IP，R8 强制 SSL）在 Security>ASA 改
    CLI/HTTP 超时，Layer2>VLAN 建 VLAN 59（Student）再删，CLI 用 show vlan 双向验证。
  tags: [Lab, SSH, WebView, aaa, session-timeout]

- id: c02
  title: Lab Working/Running/Certified 目录全流程实验
  type: case
  source_chapter: "p79-88"
  source_quote: |
    "sw3 (6560-A) -> vlan 2 / vlan 3 / vlan 99
    sw3 (6560-A) -> write memory  ... Running configuration : CERTIFY NEEDED
    sw3 (6560-A) -> reload all ... Running configuration : CERTIFIED
    sw3 (6560-A) -> write memory / ERROR: Write memory is not permitted when switch is running in certified mode
    sw3 (6560-A) -> mkdir lab / -> cp working/*.* lab / -> reload from lab no rollback-timeout
    sw3 (6560-A) -> copy running certified"
  summary: |
    目录机制实验主线：建 VLAN 2/3/99（只在 RAM）→ show running-directory 看到 NOT SYNCHRONIZED →
    write memory 后变 CERTIFY NEEDED → reload all 回退 certified、VLAN 全丢 → reload from working
    找回 → certified 模式下 write memory 报错 → mkdir lab 建 user 目录、cp working/*.* lab（
    boot.md5 Permission denied 可忽略）→ reload from lab → copy running certified 固化。附 USB
    备份：usb enable / usb backup admin-state enable / write memory flash-synchro（拔 U 盘前必须
    usb disable）。
  tags: [Lab, 目录管理, reload, certified, USB]

- id: c03
  title: Lab Virtual Chassis-6360 双机组建与监控
  type: case
  source_chapter: "p112-122"
  source_quote: |
    "sw5 (6360-A) -> virtual-chassis chassis-group 1
    sw5 (6360-A) -> virtual-chassis chassis-id 1 configured-chassis-priority 200
    sw6 (6360-B) -> virtual-chassis chassis-id 1 configured-chassis-id 2
    sw5 (6360-A) -> virtual-chassis vf-link-mode auto / auto-vf-link-port 1/1/27 (P10: 1/1/11)
    sw5 (6360-A) -> interfaces 1/1/27-28 admin-state enable
    sw5 (6360-A) -> write memory flash-synchro / -> ssh-chassis admin@2"
  summary: |
    6360-A（chassis-id 1、priority 200）与 6360-B（configured-chassis-id 2）组 VC：两边同
    chassis-group 1 → 配 auto VFL 口（P24 用 1/1/27-28/2/1/27-28，P10 用 11-12）→ write memory
    后各 reload（priority/chassis-id 改动必须重启生效；B 端 write memory 会警告 Chassis 1
    missing）→ 激活端口后 B 自动重启入 VC。监控：show virtual-chassis topology（"+"=未保存）、
    show virtual-chassis vf-link member-port、show virtual-chassis consistency、ssh-chassis
    admin@2 登从机、write memory flash-synchro 同步。
  tags: [Lab, VC, 6360, vf-link, flash-synchro]

- id: c04
  title: Lab VLAN 建网、VLAN 间路由与动态 VLAN（UNP/MAC）
  type: case
  source_chapter: "p144-157"
  source_quote: |
    "sw5 (6360-A) -> ip interface int_1 address 192.168.10.5/24 vlan 1
    sw5 (6360-A) -> vlan 50 / -> ip interface int_50 address 192.168.50.5/24 vlan 50
    sw5 (6360-A) -> vlan 50 members port 1/1/2 untagged
    sw5 (6360-A) -> unp profile employee / unp profile employee map vlan 40
    sw5 (6360-A) -> unp classification mac-address 00:50:56:90:ee:0a profile1 employee
    sw5 (6360-A) -> unp port 2/1/1 port-type bridge / unp user flush port 2/1/1"
  summary: |
    VLAN Lab：先看 VLAN 1 默认态（无成员 oper down）→ 建 IP 接口并绑 VLAN（可合写一条命令）→
    激活成员口让接口 UP → 建 VLAN 50 + 客户机静态 IP，show ip routes 出现两条 LOCAL 网段实现
    VLAN 间路由 → 动态 VLAN：unp profile employee map vlan 40 + MAC 分类规则 + unp port
    port-type bridge，flush 后 show unp user 看到 2/1/1 自动进 VLAN 40（unpUntag）→ 收尾
    no ip interface/no vlan/no unp 系列清理（VLAN 1 不可删）。
  tags: [Lab, VLAN, ip-interface, inter-vlan, UNP]

- id: c05
  title: Lab 基础维护与诊断工具（swlog/命令日志/镜像/监控/健康/RMON）
  type: case
  source_chapter: "p187-195"
  source_quote: |
    "sw7 (6870-A)-> swlog appid all subapp all level event / -> show log events
    sw7 (6870-A)-> command-log enable / -> show command-log
    sw7 (6870-A)-> port-mirroring 1 source port 1/1/1 destination port 1/1/10 / port-mirroring 1 enable
    sw7 (6870-A)-> port-monitoring 1 source port 1/1/1 enable / port-monitoring 1 pause / resume / disable
    sw7 (6870-A)-> show health / -> show rmon probes stats 1"
  summary: |
    在 6870-A 上依次演练：swlog enable/disable 与 show log swlog（CTRL+C 停）；Readable Event 用
    level event + show log events 输出客户可读事件；command-log enable 后建删 VLAN 验证审计；
    端口镜像 1 复制 1/1/1→1/1/10；端口监控抓包到 /flash/pmonitor.enc（可暂停/恢复，show
    port-monitoring file 回显）；show health 看 CPU/内存；show rmon probes [history|stats] 看探针。
  tags: [Lab, 诊断, swlog, command-log, port-mirroring, health, rmon]

- id: c06
  title: Lab LACP 动态聚合（6360 VC ↔ 6870-A）与故障演练
  type: case
  source_chapter: "p209-217"
  source_quote: |
    "sw5 (OS6360-A) -> linkagg lacp agg 7 size 2 actor admin-key 7
    sw5 (6360-A) -> linkagg lacp port 1/1/3 actor admin-key 7 / linkagg lacp port 2/1/4 actor admin-key 7
    sw7 (OS6870-A) -> linkagg lacp port 1/1/3-4 actor admin-key 7
    sw5 (6360-A) -> vlan 57 members linkagg 7 untagged
    sw7 (6870-A) -> interface 1/1/3 admin-state disable / show linkagg port"
  summary: |
    两端各建 linkagg 7（size 2、admin-key 7，admin-key 仅本地意义），VC 侧跨机箱 1/1/3+2/1/4，
    6870 侧 1/1/3-4；单边配好时 show linkagg 显示 DOWN（Att/Sel 0 0），对端配完即 UP。把默认
    VLAN 改为 57（vlan 57 members linkagg 7 untagged），两端客户端 192.168.57.105/107 互 ping，
    再 disable 成员口 1/1/3 演示单链路存活冗余（show linkagg port 看 DOWN/UP）。
  tags: [Lab, LACP, linkagg, 冗余测试]

- id: c07
  title: Lab 802.1Q 打标签（跨三交换机多 VLAN 单链路）
  type: case
  source_chapter: "p218-224"
  source_quote: |
    "sw5 (6360-A) -> vlan 58 members port 2/1/3 untagged
    sw5 (6360-A) -> vlan 20 members linkagg 7 tagged / vlan 30 members linkagg 7 tagged
    sw5 (6360-A) -> vlan 20 members port 2/1/3 tagged / vlan 30 members port 2/1/3 tagged
    sw7 (6870-A) -> ip interface int_20 address 192.168.20.7/24 vlan 20
    A PHYSICAL PORT ALWAYS HAS 1 VLAN (THE DEFAULT VLAN FOR THE PORT) THAT BRIDGES TRAFFIC (LEVEL 2)"
  summary: |
    先建 VLAN 58 做物理口默认（untagged 桥接）VLAN，再在链路两端把 VLAN 20/30 以 tagged 加到
    linkagg 7/78 与级联口（2/1/3、1/1/3）；6870/6860 分别做 VLAN 20/30 网关。show vlan members
    port 验证一口同时承载 tagged 20/30 + untagged 58（6860-B 上 20/30 因 STP 阻塞属正常）。
    Client5(VLAN20)/Client6(VLAN30) 互 ping 验证 L2/L3 混合路径，最后 write memory flash-synchro。
  tags: [Lab, 802.1Q, tagged, trunk, VLAN]

- id: c08
  title: Lab STP 根桥控制、端口状态与 1x1 负载分担
  type: case
  source_chapter: "p238-248"
  source_quote: |
    "sw7 (6870-A) -> spantree vlan 20 priority 20000 / spantree vlan 30 priority 20000
    sw5 (6360-A) -> show spantree vlan 20 ports ... 2/1/3 BLK ... ALT / 0/7 FORW ... ROOT
    sw5 (6360-A) -> linkagg lacp agg 7 admin-state disable
    sw7 (6870-A) -> spantree vlan 30 priority 32768 / Sw8 (6860-B)-> spantree vlan 30 priority 20000"
  summary: |
    用 spantree vlan N priority 20000 把 6870-A 设为 VLAN 20/30 根桥（Bridge ID==Designated
    Root 即为根）；show spantree vlan 20 ports 分析根口/指定口/ALT 阻塞口，默认全 32768 时比
    最小 MAC。禁用 linkagg 7 演示 RSTP 亚秒收敛（Topology age 归零、阻塞口转 FORW）。第三段做
    1x1 负载分担：VLAN 20 根=6870（pri 20000）、VLAN 30 根=6860（6870 恢复 32768），两上行口
    各为一个 VLAN 转发。
  tags: [Lab, STP, 根桥, blocking, 1x1负载分担]

- id: c09
  title: Lab DHL Active-Active 双活配置与切换测试
  type: case
  source_chapter: "p261-266"
  source_quote: |
    "sw5 (6360-A) -> linkagg lacp agg 8 size 2 actor admin-key 8 / linkagg lacp port 1/1/4 actor admin-key 8
    sw5 (6360-A) -> vlan 57 members linkagg 8 untagged / vlan 20 members linkagg 8 tagged
    sw5 (6360-A) -> dhl 1 / dhl 1 linka linkagg 7 linkb linkagg 8 / dhl 1 vlan-map linkb 30
    sw5 (6360-A) -> dhl 1 admin-state enable / dhl 1 mac-flushing raw
    sw5 (6360-A) -> linkagg lacp agg 7 admin-state disable ... 0/8 tagged forwarding"
  summary: |
    前置：先清端口上的 VLAN 成员再入聚合（否则报错），新建 6360↔6860 的 linkagg 8 并把 57 设为
    untagged 默认、20/30 tagged。DHL：dhl 1 建会话，linkA=linkagg 7（去 6870）、linkB=linkagg 8
    （去 6860），vlan-map linkb 30（VLAN 30 走 B，其余走 A），enable（DHL 口 STP 自动关）+ mac-
    flushing raw。show dhl 1 看 Protected/Active VLAN；ping 中禁用 linkagg 7 验证无缝切换（0/8
    变 forwarding），恢复后等 30 秒 pre-emption 回切。
  tags: [Lab, DHL, active-active, failover]

- id: c10
  title: Lab DHCP Server & DHCP Relay（全局中继）
  type: case
  source_chapter: "p289-293"
  source_quote: |
    "sw7 (6870-A) -> ip dhcp relay destination 192.168.100.102
    sw7 (6870-A) -> ip dhcp relay admin-state enable
    sw5 (6360-A) -> vlan 20 members port 1/1/1 untagged / interfaces 1/1/1-2 admin-state enable
    sw7 (6870-A) -> show ip dhcp relay statistics / Reception From Client : Total Count = 43"
  summary: |
    先 show ip routes + ping 确认两台核心（6870/6860）可达 DHCP 服务器 192.168.100.102；两台分别
    ip dhcp relay destination + admin-state enable（全局模式，Relay Mode=Global）；确认 6360 上
    客户端口正确挂在 VLAN 20/30；客户端改自动获取 IP/DNS 后 show ip dhcp relay statistics 的
    Reception/Tx 计数增长验证中继成功。注：多 DHCP 服务器分网段时可改 per-interface 模式。
  tags: [Lab, DHCP, relay, statistics]

- id: c11
  title: Lab VRRP 主备网关与手动优先级/故障切换
  type: case
  source_chapter: "p305-312"
  source_quote: |
    "sw7 (6870-A) -> ip vrrp 1 interface int_20 / ip vrrp 1 interface int_20 address 192.168.20.254
    sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state enable
    THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY
    sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state disable / priority 150 / admin-state enable"
  summary: |
    6870/6860 各建 VRID 1（int_20，虚 IP 192.168.20.254）与 VRID 2（int_30，192.168.30.254）。
    默认优先级同为 100 时比 router ID，6870 全做 Master；客户端网关改 .254 后 arp -a 可见虚拟
    MAC 00-00-5E-00-01-01。负载分担：改优先级必须先 admin-state disable → priority 150 →
    enable，6870 主备 VLAN 20、6860 主备 VLAN 30。重启 Master 演示 Backup 秒级接管（Become
    Master 计数 +1）。
  tags: [Lab, VRRP, master/backup, 虚拟IP, failover]

- id: c12
  title: Lab QoS：端口默认优先级、信任与策略限速
  type: case
  source_chapter: "p344-350"
  source_quote: |
    "sw5 (6360-A) -> qos port 1/1/1 default 802.1p 7
    sw5 (6360-A) -> qos port 1/1/1 trusted / qos apply
    sw5 (6360-A) -> policy condition client_traffic source vlan 20
    sw5 (6360-A) -> policy action priority_5 802.1p 5 / policy action priority_5 maximum bandwidth 100k
    sw5 (6360-A) -> policy rule rule1 condition client_traffic action priority_5 / qos apply
    C:\> ping -l 65000 192.168.30.xx ... Red Packets = 148"
  summary: |
    先 qos flush 复位。实验一：qos port default 802.1p 7 给未打标流量最高优先级，trusted 口保留
    原值（需 qos apply）。实验二：condition(source vlan 20)+action(802.1p 5)+rule 组合并 apply，
    show active policy rule 看命中计数；加 maximum bandwidth 100k 后普通 ping 仍 Green，大包
    ping -l 65000 出现 Red（TCM 三色丢弃）。收尾演示 policy rule disable / no policy * 清理与
    policy rule log + show qos log 日志法。
  tags: [Lab, QoS, policy, 限速, TCM]

- id: c13
  title: Lab ACL：L2/L3/ICMP 过滤与服务组（HTTP/FTP 分权）
  type: case
  source_chapter: "p369-374"
  source_quote: |
    "sw5 (6360-A) -> policy condition cond1 source mac <Client 5 MAC address>
    sw5 (6360-A) -> policy action DenyTraffic disposition deny / policy rule Filter1 condition cond1 action DenyTraffic
    sw5 (6360-A) -> policy condition ftpfromvlan20 source vlan 20 destination ip-port 20-21 ip-protocol 6
    sw5 (6360-A) -> policy service http1 destination ip-port 80 protocol 6 ... policy service group http from cli http1 http2 http3 http4 http5
    sw5 (6360-A) -> policy port group Userports 1/1/1-2 / qos user-port shutdown bpdu"
  summary: |
    按员工(VLAN20 禁 FTP)/承包商(VLAN30 禁 HTTP) 用例：L2 拒绝按源 MAC；ICMP 过滤按
    ip-protocol 1 + destination ip；FTP 按 destination ip-port 20-21 protocol 6；HTTP 用 5 条
    policy service(80/8080/8000/443/4343) 组成 service group 再入条件，规则 precedence 65535。
    每轮 qos apply 后在 Client5/9 分别验证 FTP/HTTP 可达性差异。安全收尾：policy port group
    UserPorts 防源 IP 欺骗（自动对路由流量生效），qos user-port shutdown bpdu 使用户口收到 STP
    帧即关闭。
  tags: [Lab, ACL, policy, service-group, UserPorts]

- id: c14
  title: Lab Access Guardian（RADIUS+802.1X+UNP）完整认证流
  type: case
  source_chapter: "p397-406"
  source_quote: |
    "sw5 (6360-A) -> aaa radius-server my_radius host 192.168.100.102 key alcatel-lucent
    sw5 (6360-A) -> aaa device-authentication 802.1x my_radius / aaa accounting mac my_radius
    sw5 (6360-A) -> policy list deny_employees type unp enable / policy list deny_employees rules deny_ftp_employee
    sw5 (6360-A) -> unp profile UNP-employee qos-policy-list deny_employees / map vlan 20
    sw5 (6360-A) -> unp port 1/1/1 802.1x-authentication / mac-authentication
    -> aaa test-radius-server my_radius type authentication user employee password password"
  summary: |
    声明 RADIUS（含 802.1x/mac 认证与计费、source-ip Loopback0）；ACL 规则改 no default-list 后
    装入 policy list（type unp）；建 UNP-employee/UNP-contractor 各挂 qos-policy-list 并 map
    vlan 20/30；端口开 802.1x+mac 认证。客户端启用 IEEE 802.1X（PEAP-MSCHAPv2）后 unp user
    flush port 1/1/1 重认证：employee 登录进 VLAN 20+deny_employees 角色、contractor 进 VLAN
    30，show unp user [status|details] 全程可见；RADIUS 无 MAC 条目时该用户 Status=Block。
    aaa test-radius-server 可独立验证服务器连通与 Filter-Id 返回。
  tags: [Lab, Access Guardian, 802.1x, RADIUS, UNP]

- id: c15
  title: Lab LLDP 邻居发现与管理 TLV 增强
  type: case
  source_chapter: "p422-426"
  source_quote: |
    "sw5 (6360-A) -> lldp port 1/1/3 notification enable
    sw5 (6360-A) -> lldp port 1/1/3 tlv management port-description enable
    all -> lldp chassis tlv management system-name enable / system-description enable
    all -> lldp chassis tlv management management-address enable
    sw7 (6870-A) -> show lldp statistics / show lldp remote-system"
  summary: |
    三台交换机互联口逐个开 notification（拓扑变化通知）与 port-description TLV；再在 chassis
    级开 system-name/system-description/system-capabilities/management-address 四个管理 TLV。
    show lldp statistics 看每口 Tx/Rx；show lldp remote-system 对比开 TLV 前后（前：System
    Name=(null)，后：Pod20sw7、管理 IP 192.168.254.7 等）；show lldp local-system 看本机
    30s 发送间隔、TTL×4 等参数。注意 LLDP 只能在端口/槽位/整机级配，不能配在 linkagg 上。
  tags: [Lab, LLDP, TLV, 邻居发现]
```

### counter-examples

```yaml
- id: ce01
  title: 陷阱：reload all 无论目录状态一律从 certified 启动
  type: counter-example
  source_chapter: "p81"
  source_quote: |
    "Warning > The "reload all" command particularity
    IF THE OMNISWITCH IS REBOOTED WITH THE "RELOAD ALL" COMMAND, IT WILL REBOOT FROM THE CERTIFIED
    DIRECTORY, NO MATTER WHAT THE CONTENT OF THE RUNNING DIRECTORY IS (SAME/DIFFERENT THAN THE
    CERTIFIED DIRECTORY CONTENT)"
  summary: |
    想验证 working/user 目录里的新配置时用 reload all 会直接回退 certified，看不到预期配置。
    正确做法：reload from working no rollback-timeout 或 reload from <user-dir> no rollback-timeout
    强制从目标目录启动。教材在 p81/83/85 三处 Warning 反复强调。
  tags: [reload-all, certified, 回退, 陷阱]

- id: ce02
  title: 反例：certified 模式下 write memory 被拒绝
  type: counter-example
  source_chapter: "p84"
  source_quote: |
    "sw3 (6560-A) -> vlan 4
    sw3 (6560-A) -> write memory
    ERROR: Write memory is not permitted when switch is running in certified mode"
  summary: |
    交换机 running 目录为 certified 时（如 reload all 之后），命令能敲、RAM 里也生效，但
    write memory 直接报错，且目录间不能移动文件。此时应先 reload from working 切回可写目录再
    改配置保存，否则改动断电即丢。
  tags: [certified, write-memory, ERROR]

- id: ce03
  title: 陷阱：RAM 中未保存的配置在重启后全部丢失
  type: counter-example
  source_chapter: "p82"
  source_quote: |
    "Warning > What if the OmniSwitch reboots now?
    IF THE OMNISWITCH IS REBOOTED NOW... ALL THE CHANGES IN THE RUNNING CONFIGURATION WILL BE
    OVERWRITTEN, AND THE OMNISWITCH WILL ROLL BACK TO THE WORKING DIRECTORY... IN OUR CASE, THE VLAN 2,
    3 AND 99 WILL BE LOST, AS THEY ARE NOW STORED IN THE RUNNING CONFIGURATION."
  summary: |
    刚建完 VLAN 2/3/99、show running-directory 显示 NOT SYNCHRONIZED 时断电或重启：因 working
    与 certified 内容一致，机器回滚 working，RAM 改动全部蒸发。规则：改动生效≠已保存，维护窗口
    内改完必须 write memory 才算落盘。
  tags: [running-config, 丢配置, write-memory]

- id: ce04
  title: 陷阱：VC 中改 chassis-id 后 write memory 的清除警告
  type: counter-example
  source_chapter: "p116"
  source_quote: |
    "sw6 (6360-B) -> write memory
    WARNING - Virtual chassis topology change detected. Chassis 1 missing!
    Configuration associated with missing chassis will be erased permanently!
    Confirm to continue (Y/N) : y"
  summary: |
    VC 场景下 topology 变化（如改了 chassis ID、成员缺失）时 write memory 会弹保护性警告：
    缺失机箱的配置段将被永久清除。看懂再按 Y——误确认会把原机箱相关配置（端口/VLAN 归属）清空。
  tags: [VC, write-memory, 配置清除, warning]

- id: ce05
  title: 反例：端口带着 VLAN 成员身份无法加入 linkagg
  type: counter-example
  source_chapter: "p263"
  source_quote: |
    "sw5 (6360-A) -> linkagg lacp port 2/1/3 actor admin-key 8
    ERROR: Port cannot be added to Linkagg, please remove other configuration on this port
    sw5 (6360-A) -> no vlan 58 members port 2/1/3 / no vlan 20 members port 2/1/3 / no vlan 30 members port 2/1/3"
  summary: |
    端口上还残留 VLAN membership（哪怕只是 untagged 默认 VLAN 之外的配置）时加聚合直接报错。
    正确顺序：先 show vlan members port 确认，用 no vlan N members port 清掉所有成员关系，再
    linkagg lacp port ... actor admin-key 入组。
  tags: [linkagg, 端口冲突, ERROR, 清配置]

- id: ce06
  title: 反例：VRRP 优先级在实例运行中修改无效，必须先禁用
  type: counter-example
  source_chapter: "p312"
  source_quote: |
    "Warning
    THE VRRP INSTANCE MUST BE DISABLED BEFORE CHANGING THE PRIORITY
    sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state disable
    sw7 (6870-A) -> ip vrrp 1 interface int_20 priority 150
    sw7 (6870-A) -> ip vrrp 1 interface int_20 admin-state enable"
  summary: |
    对已启用的 VRRP 实例直接敲 priority 会失败/不生效。标准三步：admin-state disable →
    priority 150 → admin-state enable。教材以此完成 6870 主 VLAN20、6860 主 VLAN30 的负载分担。
  tags: [VRRP, priority, disable-first]

- id: ce07
  title: 陷阱：VC 的 chassis priority / chassis-id 改动须重启才生效
  type: counter-example
  source_chapter: "p114-116"
  source_quote: |
    "Notes: A reload is mandatory to consider the chassis priority
    sw5 (6360-A) -> reload from working no rollback-timeout ... Pri 200 (after reload)
    Notes: A reload is mandatory to take into account the new chassis-id"
  summary: |
    配置 configured-chassis-priority 200 后 show virtual-chassis topology 里 Oper Pri 仍是 100，
    直到 reload 才变 200；改 configured-chassis-id 同样必须重启。规划 master 角色时要算上这次
    重启窗口（Lab 环境约 4-5 分钟）。
  tags: [VC, priority, reload, 生效时机]

- id: ce08
  title: 约束：端口监控与端口镜像不能共用同一端口
  type: counter-example
  source_chapter: "p177"
  source_quote: |
    "Session supported per switch or stack: 1 ... Round-Robin or stop capture when max storage reached
    Cannot use port monitoring and mirroring on the same port"
  summary: |
    同一物理口不能同时做 port-monitoring 抓包源/目的和 port-mirroring 的目的口；且 port
    monitoring 每机只有 1 个会话、文件上限 2MB。排障前先 show port-mirroring status / show
    port-monitoring status 排除冲突，规划好哪个口抓包、哪个口镜像。
  tags: [port-monitoring, port-mirroring, 冲突]

- id: ce09
  title: 陷阱：QoS 端口改动和策略不经 qos apply 不生效
  type: counter-example
  source_chapter: "p346-348"
  source_quote: |
    "The global setting is active immediately; however, modifying a port configuration requires qos apply
    to activate the change.
    - The rule is not active on the switch until it has been applied:
    sw5 (6360-A) -> policy rule rule1 condition client_traffic action priority_5 / qos apply"
  summary: |
    常见失误：配完 policy condition/action/rule 或 qos port trusted 后直接测试，发现规则未命中
    ——因为还没 qos apply。端口级与策略配置都必须 apply 才下发硬件；show active policy rule 里
    看不到规则即说明没 apply 或规则被 disable。
  tags: [QoS, qos-apply, 生效时机]

- id: ce10
  title: 反例：VLAN 1 不能删除，只能停用
  type: counter-example
  source_chapter: "p156"
  source_quote: |
    "Notes
    VLAN 1 cannot be deleted. It is only possible to deactivate.
    sw5 (6360-A) -> no ip interface int_50 / no vlan 50 / no ip interface int_1"
  summary: |
    清理实验配置时 no vlan 50、no ip interface 都可以，但 no vlan 1 不被支持——默认 VLAN 1 只能
    admin-state 停用或把端口移走。脚本化清理时要把 VLAN 1 从删除清单里剔除，否则脚本中断。
  tags: [VLAN1, 删除限制, 清理]

- id: ce11
  title: 陷阱：VLAN 无活动成员时 IP 接口 DOWN 且不被路由宣告
  type: counter-example
  source_chapter: "p221"
  source_quote: |
    "Our VLAN 20 and 30 IP interfaces are currently down because we have no members in the two VLANs.
    Remember, if there are no members of a VLAN the IP interface is not only down but will not be
    advertised to the Layer 3."
  summary: |
    int_20/int_30 刚建好 Status=DOWN，不是配错，而是 VLAN 20/30 还没有任何成员口。后果比
    "down" 更严重：接口不响应 ping、也不会进路由协议宣告。排障顺序：先 show vlan members
    挂成员/激活端口，再查路由表。
  tags: [ip-interface, VLAN成员, DOWN, 排障]

- id: ce12
  title: 约束：静态链路聚合只能用在 OmniSwitch 之间
  type: counter-example
  source_chapter: "p199"
  source_quote: |
    "Static: Port parameters MUST be exactly the same at both ends and within the group... Only works
    between Alcatel-Lucent OmniSwitches
    Dynamic: IEEE 802.3ad LACP... It also works between two different devices such as switches, servers
    and storage systems."
  summary: |
    与服务器、存储或第三方交换机做聚合时选 static linkagg 会对接失败——静态聚合是 ALE 私有
    实现，仅限两台 OmniSwitch 之间；跨厂商场景必须用 linkagg lacp（802.3ad），且组内端口同速。
  tags: [linkagg, 静态聚合, 互操作, 选型]

- id: ce13
  title: 陷阱：DHL 故障链路恢复后不立即回切，要等 pre-emption 30 秒
  type: counter-example
  source_chapter: "p266"
  source_quote: |
    "Notes
    It can takes a few seconds for the VLAN 20 to be forwarded back on the link aggregation 8: when the
    failed link comes back up, DHL waits a configurable amount of time (default: 30 secs) before the link
    resumes forwarding of its assigned VLAN traffic."
  summary: |
    演练 DHL 回切时常见"链路已 up 但流量还走在备用链路"的误判：show vlan 20 members 里原链路仍
    dhl-blocking。这是 pre-emption timer（默认 30 秒，可配 0-600）在等待，防止链路抖动导致
    VLAN 反复横跳；等满时间才恢复该链路承载自己的 VLAN。
  tags: [DHL, pre-emption, 回切延迟]

- id: ce14
  title: 约束：LLDP 不能配置在 linkagg 级别；U 盘拔出前必须 usb disable
  type: counter-example
  source_chapter: "p423"
  source_quote: |
    "Tips
    LLDP is configured at port level (or NI or chassis), but not at linkagg level.
    (p86) +++ CAUTION: Do usb disable before removing usb"
  summary: |
    两个易踩的小坑：(1) LLDP 的 notification/TLV 只能按端口、槽位或整机配置，聚合逻辑口上没有
    LLDP 命令，要逐个成员口配；(2) USB 备份后直接拔 U 盘有风险，系统日志明确提示先 usb
    disable 再移除。
  tags: [LLDP, linkagg, USB, 操作规范]
```

### glossary

```yaml
- id: g01
  title: Certified 目录（认证目录）
  type: term
  source_chapter: "p80"
  source_quote: |
    "The certified directory contains files that have been certified by an authorized user as the default
    files for the switch."
  summary: |
    Flash 上经授权用户认证的默认镜像+配置目录，是故障回退的基线。running 目录与 certified 内容
    不一致时冷启动自动回退到这里；运行于 certified 时配置不可保存。
  tags: [目录, certified, AOS]

- id: g02
  title: Working 目录（工作目录）
  type: term
  source_chapter: "p80"
  source_quote: |
    "The working directory is a holding place for new files. Files in the working directory must be tested
    before committing them to the certified directory."
  summary: |
    新镜像/配置的测试暂存目录。升级或改配流程：先在 working 验证（reload from working），
    验证通过 copy running certified 固化。
  tags: [目录, working, AOS]

- id: g03
  title: Running 目录 / Running configuration（运行目录/运行配置）
  type: term
  source_chapter: "p80"
  source_quote: |
    "The running directory is the directory where the configuration changes will be saved. The running
    configuration, stored in the RAM, contains the current operating parameters."
  summary: |
    running directory 是本次启动实际加载的目录（certified/working/user 之一）；running
    configuration 是 RAM 里的现行配置 = 启动目录内容 + 未保存改动。show running-directory 查看。
  tags: [目录, running, RAM]

- id: g04
  title: User-defined 目录（用户自定义目录）
  type: term
  source_chapter: "p67"
  source_quote: |
    "Additional User-defined directories: Created by the user (any name). Can be used to store additional
    switch configurations. Configuration changes CAN be saved directly to any user-defined directory"
  summary: |
    用户自建目录（任意命名），性质类似 working：可存整套装镜像+配置，可直接保存配置，也能
    reload from <目录> 启动，用于保存多套实验/回退点。
  tags: [目录, user-defined]

- id: g05
  title: vcboot.cfg / vcsetup.cfg
  type: term
  source_chapter: "p67"
  source_quote: |
    "Configuration files: vcboot.cfg vcsetup.cfg ... image files (AOS)"
  summary: |
    每个目录的两份文本配置：vcsetup.cfg 保存 Virtual Chassis 参数（chassis-id/group/VFL 等），
    vcboot.cfg 保存启动配置。write memory 同时替换两者；判断目录是否"一致"就是比镜像+vcboot.cfg。
  tags: [配置文件, vcboot, vcsetup]

- id: g06
  title: CMM（Chassis Management Module，机箱管理模块）
  type: term
  source_chapter: "p44"
  source_quote: |
    "Remotely manage the switch directly via the CMM (not available in all switches). The EMP port IP
    address of the master chassis (Virtual Chassis) ip interface master emp address 172.25.167.203"
  summary: |
    交换机的管理主控模块，带外管理（EMP 口）直连 CMM 绕过业务网板；show running-directory 里的
    Running CMM、CMM Slot 均指它。
  tags: [硬件, 管理, CMM]

- id: g07
  title: EMP（Ethernet Management Port，以太网管理口）
  type: term
  source_chapter: "p44"
  source_quote: |
    "ACCESS VIA THE EMP PORT: Bypass the network interface modules (NI). Remotely manage the switch
    directly via the CMM. USB Ethernet Dongle... This interface is treated just like an EMP interface."
  summary: |
    独立于业务面的带外管理网口；无 EMP 口的型号（6360/6465/6560）用 USB-Ethernet dongle 等效
    替代，所有 EMP 命令同样适用。VC 场景配 master 的 EMP 地址即可管理整个 VC，RCD 也走它。
  tags: [带外管理, EMP]

- id: g08
  title: Virtual Chassis（VC，虚拟机箱）
  type: term
  source_chapter: "p91"
  source_quote: |
    "Virtual Chassis = Group of switches which appears as a single router or bridge. Single Point of
    management / Single Logical Switch / No STP/VRRP between Access and Core switches / No license needed"
  summary: |
    多台交换机经 VFL 互联后对外呈现为一台逻辑设备：单一管理点、跨机箱冗余、免 STP/VRRP、无需
    许可。拓扑可为链形/环形/全互联，规模按型号 2-10 台不等。
  tags: [VC, 堆叠]

- id: g09
  title: VFL（Virtual Fabric Link，虚拟机箱互联链路）
  type: term
  source_chapter: "p91"
  source_quote: |
    "Switches inter-connected via dedicated or optional SFP+, QSFP ports. Mesh or Ring topology ... VFL"
  summary: |
    VC 成员间的专用互联链路，可用专用堆叠口或占用业务 SFP+/QSFP 口，支持 auto（自动检测+自动
    分配 VFL ID，须两端都是 auto 候选口）与 static 两种模式。show virtual-chassis vf-link 查看。
  tags: [VC, VFL, 堆叠链路]

- id: g10
  title: ISIS-VC（VC 内部路由/拓扑协议）
  type: term
  source_chapter: "p94"
  source_quote: |
    "VC topology managed by ISIS-VC. Private TLV report the switch's capability and numbering. Exchange
    IS-IS HELLO for adjacencies and updates. Maintains a loop-free topology for BUM traffic"
  summary: |
    VC 私有控制协议：基于 IS-IS HELLO 维护成员邻接与无环拓扑、承担 master 选举、在成员间建转
    发库并按 SPBM 式确定性打破等价路径。
  tags: [VC, ISIS-VC, 控制]

- id: g11
  title: RCD（Remote Chassis Detection，远程机箱检测）
  type: term
  source_chapter: "p99"
  source_quote: |
    "Out of Band: EMP Remote Chassis Detection (RCD). A switch sends an announcement whenever its chassis
    VC information changes. RCD protocol will detect this split topology."
  summary: |
    带外脑裂检测：经 EMP 管理网互发机箱 VC 信息通告，VFL 全断（split）时识别出伪 master 并让其
    关闭所有用户口防止 MAC/IP 重复。地址偏好：NVRAM 里的 CMM IP > EMP IP。
  tags: [VC, split, RCD]

- id: g12
  title: VCSP（VC Split Protection / VC Split Protocol）
  type: term
  source_chapter: "p100"
  source_quote: |
    "In Band: VC Split Protocol. Requires an upstream or downstream device to act as helper switch.
    Every VC member switch recommended to have one port as part of the VCSP LAG to the helper device"
  summary: |
    带内脑裂防护：借上/下游 helper 交换机，VC 成员各出一口组成 VCSP LAG 到 helper；用
    virtual-chassis split-protection [helper] admin-state/linkagg 命令启用。
  tags: [VC, split, VCSP]

- id: g13
  title: ISSU（In Service Software Upgrade，不中断升级）
  type: term
  source_chapter: "p101"
  source_quote: |
    "Used to upgrade the software on a VC with minimal network disruption. Each element is upgraded
    individually ... The Slaves are then reloaded from the ISSU directory in order from lowest to highest
    chassis ID"
  summary: |
    VC 逐台成员滚动升级机制：新代码放独立目录后由 issu 命令分发并按 chassis ID 从小到大逐台
    重启，网络冲击最小化。
  tags: [VC, ISSU, 升级]

- id: g14
  title: ASA（Authenticated Switch Access，交换机认证接入）
  type: term
  source_chapter: "p57"
  source_quote: |
    "Authenticated Switch Access (ASA) provides the ability to restrict which users can configure the
    switch remotely... ASA applies to Telnet, FTP, SNMP, SSH, HTTP, and the console and modem ports."
  summary: |
    管理面接入控制：按 console/telnet/ftp/http/snmp/ssh/default 七类服务分别指定本地库或
    RADIUS/LDAP 认证链，show aaa authentication 查看每类服务的认证服务器与 exit-on-fail 状态。
  tags: [管理安全, AAA, ASA]

- id: g15
  title: WebView（内嵌 Web 管理）
  type: term
  source_chapter: "p47"
  source_quote: |
    "The WebView application is embedded in the switch and is accessible via a web browser.
    webview force-ssl enable (default=enabled)"
  summary: |
    交换机内置的单机 Web 管理界面，默认启用且 R8 强制 SSL（HTTP 自动跳 HTTPS）；配置分
    Physical/L2/Networking/Service/Security/QoS/Device 七大组。仅限单台设备视图。
  tags: [管理, webview]

- id: g16
  title: Lightning Configuration（闪电配置/快速开局）
  type: term
  source_chapter: "p49"
  source_quote: |
    "The switch starts with default IP address, VLAN 1, lightning-config interface, IP 192.168.0.1/24 ...
    A Quick Config Dashboard window opens. We get access of the mandatory and pre-selected options"
  summary: |
    出厂零配置开局模式：仅 1/1/1-2 接入客户端时经 HTTPS 打开 Quick Config 向导（NTP/IP/网关/
    DNS/VMS 等），可导出/导入配置文件；首次 write memory 后默认 IP 失效。
  tags: [开局, 零配置]

- id: g17
  title: Thin Client 模式（瘦客户端）
  type: term
  source_chapter: "p76"
  source_quote: |
    "No configuration is stored on the switch. It will contact OmniVista 2500 to retrieve the config...
    In thin-client mode, no configuration is saved in the 'running' directory ... All configuration
    changes should be done in OV 2500."
  summary: |
    激活流程中声明的托管模式：交换机启动后向 OV 2500 注册拉取配置，本地不留配置、write memory
    不落盘，一切变更在 OV 2500 集中完成（仅留最小网络可达的 vcboot.cfg）。
  tags: [OV2500, 集中管理]

- id: g18
  title: UNP（User Network Profile，用户网络档案）
  type: term
  source_chapter: "p142"
  source_quote: |
    "UNP R8: VLAN ID / Policy List / ACL / QoS / Location / Period"
  summary: |
    统一的用户/设备接入档案：一个 profile 聚合 VLAN 映射、QoS/ACL 策略列表、位置与时段策略，
    通过分类规则或 RADIUS Filter-Id 命中后套用到端口上的用户。
  tags: [UNP, profile]

- id: g19
  title: Access Guardian（接入卫士）
  type: term
  source_chapter: "p377"
  source_quote: |
    "Role Based Access Control with UNP (Universal Network Profile). Auto-sensing, multi-client
    authentication on a port"
  summary: |
    ALE 的接入安全方案：端口上自动识别 802.1X（supplicant）或 MAC（非 supplicant）认证，经
    RADIUS 的 Filter-Id 返回 UNP，实现按人/设备角色下发 VLAN+QoS+ACL；服务器不可达可走
    auth-server-down profile。
  tags: [接入安全, 802.1x, UNP]

- id: g20
  title: 802.1Q / 802.1p（VLAN 标签与优先级）
  type: term
  source_chapter: "p139"
  source_quote: |
    "VLAN Tag: 802.3 MAC header change, 4096 unique VLAN Tags (addresses), VLAN ID == GID == VLAN Tag.
    802.1P: Three-bit field within 802.1Q header, Allows up to 8 different priorities"
  summary: |
    802.1Q 在以太帧头插 4 字节标签：12bit VLAN ID（4096 个）+3bit 802.1p 优先级（8 级）。
    trunk 口上每个 VLAN 可 tagged 传送，物理口保留一个 untagged 桥接 VLAN。
  tags: [VLAN, 标签, 优先级]

- id: g21
  title: Mobile Tag（移动标签）
  type: term
  source_chapter: "p416"
  source_quote: |
    "Mobile Tag: Allows mobile ports to receive 802.1Q tagged packets / Not supported on mobile ports(802.1Q
    Tag) / Triggers dynamic assignment of tagged mobile port traffic to one or more VLANs"
  summary: |
    与 802.1Q tag 相对的机制：普通 802.1Q 只能配在固定端口，mobile tag 允许 UNP mobile 口接收
    tagged 流并动态归入对应 VLAN——LLDP-MED 话机场景常用（UNP profile mobile-tag + map vlan）。
  tags: [UNP, mobile-tag, 语音]

- id: g22
  title: Linkagg / LACP 与 Actor Admin Key（链路聚合）
  type: term
  source_chapter: "p211"
  source_quote: |
    "The link aggregation number and ports are associated to a dynamic link aggregation using the actor
    admin key. Although in the above example the actor admin key matches the link aggregation number, this
    is not a requirement as the admin key has local significance only."
  summary: |
    把多条物理链路合成一条逻辑链路（增带宽/冗余）。静态 linkagg 仅限 OmniSwitch 间；动态
    linkagg lacp 按 802.3ad 用 LACPDU 协商可跨厂商。actor admin key 是端口入组的关联键，仅本地
    有效、不必等于组号。聚合口可像物理口一样挂 VLAN（tagged/untagged）。
  tags: [链路聚合, LACP, admin-key]

- id: g23
  title: STP 模式：flat 与 per-vlan（1x1）
  type: term
  source_chapter: "p227"
  source_quote: |
    "Supports two Spanning Tree operating modes: flat (single STP instance per switch) / per-VLAN (single
    STP instance per VLAN) (By default on OmniSwitch)"
  summary: |
    flat=整机一个 STP 实例；per-vlan（1x1）=每 VLAN 一个实例（OmniSwitch 默认）。1x1 下可按
    VLAN 设不同根桥实现上行链路负载分担。协议可选 802.1d(STP)/802.1w(RSTP)/802.1s(MSTP)。
  tags: [STP, 模式]

- id: g24
  title: DHL（Dual-Home Link，动态双归属）及 RAW/MVRP 冲刷
  type: term
  source_chapter: "p251"
  source_quote: |
    "High availability feature. Provides fast failover between Core/Aggregation and Access switches without
    using STP. DHL Active-Active splits VLANs between two active links"
  summary: |
    接入交换机双上行到两台核心的无 STP 双活方案：每 VLAN 只在一条链路转发（防环），故障时 VLAN
    整体切到另一条，带宽 100% 利用。每机 1 会话、2 链路；MAC 冲刷三选一——RAW Flooding（以旧
    MAC 为源广播触发重学习）、MVRP Enhanced（带 new 标志的 join）、none（默认，保留旧表项）。
  tags: [DHL, 高可用, mac-flushing]

- id: g25
  title: DHCP Relay（DHCP 中继 / IP Helper）与 Option 82
  type: term
  source_chapter: "p275"
  source_quote: |
    "Two types of DHCP relay agents: global and per-interface ... They are mutually exclusive.
    DHCP Relay Opt82 Format = Base MAC"
  summary: |
    把客户端的 DHCP 广播跨网段转给服务器；global 模式面向全网、per-interface 模式按 IP 接口
    指定服务器，两者互斥。默认携带 Option 82（格式 Base MAC）标识来源交换机。
  tags: [DHCP, relay, option82]

- id: g26
  title: Loopback0 接口
  type: term
  source_chapter: "p282"
  source_quote: |
    "Identify a consistent address for network management purposes. Not bound to any VLAN. Always remain
    operationally active ... Automatically advertised by RIP and OSPF"
  summary: |
    名字固定为 Loopback0 的 /32 环回接口：不绑 VLAN、恒 UP，自动被 RIP/OSPF 宣告，常作 NMS/
    RADIUS/NTP/sFlow 的稳定源地址与 router-id。
  tags: [环回, 管理地址]

- id: g27
  title: VRRP（虚拟路由冗余协议）/ VRID / 虚拟 MAC
  type: term
  source_chapter: "p297"
  source_quote: |
    "Protocol for electing a switch as the master virtual router. Default gateway = Virtual Router IP.
    Multicast - 224.0.0.18. Virtual MAC address: 00-00-5E-00-01-{VRID}"
  summary: |
    默认网关冗余协议（RFC 2338/2787）：同网段多台路由器共享 VRID+虚拟 IP，优先级最高者为
    master 转发并应答 ARP；虚拟 MAC 00-00-5E-00-01-{VRID} 使 master 切换无需终端重新 ARP。
    支持 track 策略联动端口/IP 降优先级。
  tags: [VRRP, 网关冗余]

- id: g28
  title: QSI / QSP（队列集实例/队列集模板）
  type: term
  source_chapter: "p319-320"
  source_quote: |
    "QSet Profile 1: Q1 = SP7, 100% BW ... Q8 = SP0 (8SP)
    -> qos qsi port 1/2/1 qsp 2 / qos qsp system-default 2"
  summary: |
    出口拥塞管理单元：QSP（QSet Profile）是队列调度模板（如 QSP1=8 个严格优先级队列、QSP2=1
    EF+7 SP），QSI 是端口/聚合上的实例。qos qsi port X qsp N 按口指定，qos qsp system-default
    N 改全局默认。
  tags: [QoS, 队列, 拥塞管理]

- id: g29
  title: 策略三元组：policy condition / action / rule
  type: term
  source_chapter: "p322-327"
  source_quote: |
    "A policy (or a policy rule) is made up of: 1. a condition 2. an action
    -> policy rule r1 precedence 200 condition c1 action a1 log"
  summary: |
    QoS/ACL 统一策略模型：condition 匹配 L1-L4 字段（含 group 复用），action 定义处置
    （priority/bandwidth/标记/redirect/mirror/disposition），rule 以 precedence 组装两者并可加
    log/trap/count/validity-period，qos apply 生效。
  tags: [QoS, ACL, policy]

- id: g30
  title: PBR（Policy Based Routing，策略路由）
  type: term
  source_chapter: "p335-336"
  source_quote: |
    "QoS policies that will override the normal routing mechanism for traffic matching the policy
    condition ... -> policy action <action_name> permanent gateway ip <ip address>"
  summary: |
    用 QoS 策略改写转发路径：action 里 permanent gateway ip 指定下一跳覆盖路由表（如把源
    10.10.0.0/16 全部引流到防火墙），硬件实现；条件里加 source port 防回流环路。支持
    6570M/6860/6865/6900/9900。
  tags: [PBR, 策略路由]

- id: g31
  title: RPM / 策略镜像（Remote & Policy Based Mirroring）
  type: term
  source_chapter: "p340-342"
  source_quote: |
    "Allows traffic to be carried over the network to a remote switch. Achieved by using a dedicated remote
    port mirroring VLAN. (p341) Mirroring is done based on a QoS policy instead of a specific port.
    -> policy action a1 ingress egress mirror 1/1/1"
  summary: |
    RPM 用专用镜像 VLAN 把流量跨交换机送到远端抓包口（该 VLAN 不许跑别的流量，LACP/LLDP/802.1x
    等控制包不被镜像）；策略镜像按 QoS condition（IP/MAC/协议/VLAN）决定镜像，action 加
    ingress/egress mirror <口>。
  tags: [镜像, RPM, 抓包]

- id: g32
  title: ACL disposition（accept/drop/deny）
  type: term
  source_chapter: "p354"
  source_quote: |
    "DISPOSITION accept | drop | deny ... policy action a1 disposition accept"
  summary: |
    ACL 动作里的处置三态：accept 放行（默认）、drop 丢弃、deny 拒绝。规则未命中任何策略的流
    默认被接受；配合 UserPorts 组可实现防 IP 欺骗、协议过滤与端口自动关闭。
  tags: [ACL, disposition]

- id: g33
  title: UserPorts / DropServices（保留策略组）
  type: term
  source_chapter: "p362-363"
  source_quote: |
    "UserPorts: Reserved Group. Used by default to prevent spoofed IP addresses on ports ... qos user-port
    {filter | shutdown} {spoof|bgp|bpdu|rip|ospf|vrrp|...}
    DropServices ... Any services belonging to this group will be dropped if seen on ports included in the
    UserPorts group"
  summary: |
    两个保留 port/service 组：把用户口加进 UserPorts 即获得防源 IP 欺骗（可扩展过滤
    rip/ospf/bpdu/dhcpserver 等，甚至违规自动 shutdown）；DropServices 里的服务（如 tcp135/
    445、udp137）在 UserPorts 口上一律丢弃——不用写规则即全局生效。
  tags: [ACL, 安全, 保留组]

- id: g34
  title: swlog（交换机日志）
  type: term
  source_chapter: "p161"
  source_quote: |
    "Event logging utility. Useful in maintaining and servicing the switch. Switch events can be logged to
    Switch console / Local text file / Multiple remote devices (syslog) 12 max"
  summary: |
    系统事件日志子系统：输出到 console/flash（swlog_chassis1~1.6 轮转+archive）/syslog（最多
    12 台）；按 appid/subapp 调级别，level event + show log events 输出客户可读事件。
  tags: [日志, swlog]

- id: g35
  title: sFlow 与 RMON（流量采样/远程监控）
  type: term
  source_chapter: "p184-185"
  source_quote: |
    "Traffic flows monitoring and sampling technology embedded within switches. One Sampler for each
    interface Collects packet samples. One Poller for each interface Collects counter samples.
    -> sflow sampler 1 port 1/1/6 receiver 1 rate 5 sample-hdr-size 64"
  summary: |
    sFlow（RFC 3176）：内嵌 agent 按口配 sampler（采包头，rate 抽样）与 poller（采计数器）发到
    receiver，用于流量画像/异常检测/容量规划。RMON：端口统计探针（以太统计/历史/告警/事件四
    组）供 OmniVista 等 NMS 拉取（show rmon probes）。
  tags: [sFlow, RMON, 监控]

- id: g36
  title: LLDP / LLDP-MED（链路层发现协议）
  type: term
  source_chapter: "p409-415"
  source_quote: |
    "IEEE 802.1AB - Link Layer Discovery Protocol (LLDP). L2 discovery protocol. Enabled by default on the
    OmniSwitches ... LLDP-MED: Provides VoIP-specific extensions to base LLDP protocol"
  summary: |
    邻居发现协议（802.1AB，默认收发开启），以 TLV 交换 chassis/port/系统信息；LLDP-MED 扩展
    面向话机：Network Policy TLV 下发 VLAN+L2 优先级+DSCP、位置、电源与资产清单（show lldp
    remote-system med inventory）。
  tags: [LLDP, 发现协议, 语音]

- id: g37
  title: PoE（以太网供电）与 FPoE / PPoE / EEE
  type: term
  source_chapter: "p429-433"
  source_quote: |
    "The PoE (Power over Ethernet) passes a voltage in addition to the data on an ethernet cable.
    Fast PoE ... Used to provide PoE power a few seconds after powering up the chassis.
    Perpetual PoE ... Provides uninterrupted power to the connected device (PD) even when the switch is
    restarting"
  summary: |
    网线同时传数据与电力（af 15.4W / at 30W / bt 最高 100W，型号带 P 表示支持）。FPoE 开机秒级
    供电、PPoE 重启期间不断电（均需升级 FPGA/CPLD）；EEE（802.3az）空闲低功耗仅限铜口
    100/1000M。lanpower 命令族管理预算/优先级。
  tags: [PoE, FPoE, PPoE, EEE]

- id: g38
  title: Auto Fabric / RCL（智能织物/自动远程配置）
  type: term
  source_chapter: "p460-465"
  source_quote: |
    "AUTO-FABRIC - PLUG-N-PLAY ZERO TOUCH DEPLOYMENT: 1- Auto-VC 2- Automatic remote configuration 3-
    Auto-LACP 4- Auto-Routing 5- Auto-SPB Fabric 6- Auto-Network Profiling 7- Auto-MVRP"
  summary: |
    零接触部署框架：开机自组 VC、经 RCL（在 VLAN 1/127 各试 3 次 DHCP 拉取指令/配置文件）下发
    配置，再自动发现 LACP/OSPF/ISIS/SPB（BVLAN 4000-4015）、生成网络档案并启用 MVRP；auto-
    fabric admin-state enable / auto-config-abort 管理。
  tags: [零配置, auto-fabric, RCL]

- id: g39
  title: write memory flash-synchro（同步保存命令）
  type: term
  source_chapter: "p71"
  source_quote: |
    "sw7 (OS6860-A) -> write memory flash-synchro = write memory + copy running certified"
  summary: |
    组合保存命令：一步完成"RAM→running 目录"和"running→certified"（VC 中还同步所有成员的
    Flash Between CMMs）。Lab 收尾的标准动作，等价于依次执行两条命令。
  tags: [保存命令, flash-synchro]

- id: g40
  title: ssh-chassis（VC 成员跳转登录）
  type: term
  source_chapter: "p102"
  source_quote: |
    "A user can access to remote CLI console of any VC with secure shell protocol (SSH).
    ssh-chassis <username>@<chassis-id>
    -> ssh-chassis admin@2 ... Local Chassis: 2"
  summary: |
    在 master CLI 上直接 SSH 到指定 chassis-id 成员的本机控制台（底层 ssh admin@127.10.x.65），
    提示符不变，用 show virtual-chassis topology 的 Local Chassis 值确认所在成员，logout 返回。
  tags: [VC, ssh-chassis, 运维]
```

