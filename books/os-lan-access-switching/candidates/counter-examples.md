# counter-examples · OmniSwitch LAN Access Switching (DT00XTE215EN)
# 来源: source/fulltext.md（页码为教材 PDF 页 / <<<PAGE N>>> 标记）

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
