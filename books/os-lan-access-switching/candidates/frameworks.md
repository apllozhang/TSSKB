# frameworks · OmniSwitch LAN Access Switching (DT00XTE215EN)
# 来源: source/fulltext.md（页码为教材 PDF 页 / <<<PAGE N>>> 标记）

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
