# principles · OmniSwitch LAN Access Switching (DT00XTE215EN)
# 来源: source/fulltext.md（页码为教材 PDF 页 / <<<PAGE N>>> 标记）

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

- id: p18
  title: VLAN 1 是不可删除的默认 VLAN
  type: principle
  source_chapter: "p145"
  source_quote: |
    "In its untagged configuration, the switch has only one VLAN, the VLAN 1. This is the default VLAN and
    all ports are initially associated with it. This VLAN CANNOT be deleted, but it can be disabled if
    desired."
  summary: |
    出厂所有端口都在 VLAN 1；VLAN 1 无法删除（no vlan 1 不可行），只能 admin-state 停用。安全
    实践（Lab 中反复出现）是业务口改挂别的 VLAN、上行链路用其他 VLAN 做 untagged，避免用
    VLAN 1 承载业务。
  tags: [VLAN1, 默认VLAN]

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
