# counter-examples.md · OmniSwitch LAN Troubleshooting (DT00XTE221EN) 陷阱/警告候选条目

- id: ce01
  title: 桥接环路期间 Telnet/SSH 大概率不可用，必须走 console
  type: counter-example
  source_chapter: "p171"
  source_quote: |
    "You should have console access. During a bridging loop, you will probably not be able to Telnet or SSH. Refer to chapter 'switch system'"
  summary: |
    反例：环路风暴把管理面打挂后远程登录失败，工程师在终端前干等。正解：环路类故障（高链路利用率、CPU 飙高、MAC 漂移）发生时先占住 console 口；远程场景可提前经 EMP 管理口 SSH 兜底（LAB2 p201 明确："If you do not have access to 6870 console, open an SSH session via the EMP's IP address"）。预防：把 console/EMP 访问纳入排障工具可达性检查。
  tags: [bridging-loop, console-access, emp, management-plane]

- id: ce02
  title: su 维护 shell 不是自由进出的后门
  type: counter-example
  source_chapter: "p111"
  source_quote: |
    "* The use of the 'su' command is not trivial. Also, use it only with the control of technical support when request."
  summary: |
    反例：为了看进程直接 su 进维护 shell 随意操作。教材原文警告：su 命令"并不简单"，只应在技术支持指导下使用。正解：常规排障用 show health/top 之前的 show 命令族；确需进 shell（top/ps/logger 等）时，动作限定在只读观察与 TAC 指定的操作，用完立即 exit；找到可疑进程后联系 ALE 支持获取处置流程（p112），不要自行杀进程。
  tags: [maintenance-shell, su, tac, change-control]

- id: ce03
  title: debug ip packet 不加过滤直接 start 会刷爆屏幕
  type: counter-example
  source_chapter: "p128"
  source_quote: |
    "Precaution must be taken when using the following commands as it might dump a lot of information on the screen
    -> debug ip packet start ip-address 'num.num.num.num' start"
  summary: |
    反例：debug ip packet start 裸跑，全设备全协议报文倾泻，把需要的信息冲掉还推高 CPU。正解：必须限定过滤维度（p210 参数表）：ip-address / ip-pair / protocol {tcp|udp|icmp} / ether-type / direction / board {cmm|ni} / output {file|console}，并可加 timeout（如 debug ip packet protocol udp start timeout 60）。用完 debug ip packet stop。同类警示适用 debug stp bpdu-stats（p183）。
  tags: [debug, debug-ip-packet, output-flood, cpu]

- id: ce04
  title: swlog 调到 debug 后忘记改回 info
  type: counter-example
  source_chapter: "p176"
  source_quote: |
    "Check the level debug for an appid ... To change back to original management
    sw7 (6860-A) -> swlog appid slni subapp macmove level info"
  summary: |
    反例：排障时 swlog appid X subapp Y level debug2（或 debug3），排查完不回滚。后果：debug 级日志持续高速写 flash、刷 syslog 服务器，本身就制造"高 CPU/日志风暴"这类次生故障（LAB4 p289 专门列出收尾命令 swlog appid ospf_0 subapp all level info，LAB2 p203 同样收尾）。正解：把"调回 info"写进排障 SOP 的收尾清单，与"验证恢复"同等强制。
  tags: [swlog, debug-level, rollback, hygiene]

- id: ce05
  title: 把"上电但 DOWN"误判为硬件故障返修
  type: counter-example
  source_chapter: "p100"
  source_quote: |
    "The operational status can be DOWN while the power status is ON, indicating a possible software issue"
  summary: |
    反例：show module status 看到 DOWN 就开硬件更换流程。判别点：Admin Status=POWER ON 而 Operational Status=DOWN 的组合指向软件问题（微码没起来、启动失败、软件异常），应先走软件侧排查（show microcode loaded、重启、版本核对），而不是直接换模块。物理损坏类才伴随断电/无法识别等表现。同类：LAB1 中 6860-B int_30 状态 DOWN 也是配置（未 enable）而非硬件。
  tags: [misdiagnosis, hardware, module-status, software-issue]

- id: ce06
  title: 手工编辑 vcsetup.cfg 触发 error mode，全端口禁用
  type: counter-example
  source_chapter: "p161"
  source_quote: |
    "The vcsetup.cfg file is corrupted or edited in such a way that it is unable to read a valid chassis identifier in the appropriate range. A switch start up error mode will keep all of its front-panel user ports, including the virtual-fabric links member ports disabled."
  summary: |
    反例：直接文本编辑 vcsetup.cfg 改机箱号/模式，格式或取值越界。后果：交换机进入 error mode（Inconsistent Invalid-Chassis-Id），前面板所有用户口连同 VFL 成员口保持 disabled，表现为"整机瘫"。正解：vcsetup.cfg 用 CLI 生成或严格按模板；文件中 "PLEASE DO NOT MODIFY THE AREAS OF [SAVED INFO xxx]" 区域绝对不动（p163 标注）；改动后用 cat 复核并检查 /flash 下是否生成 vcsetup.cfg.*.err 文件（LAB2 即靠它定位了两处 ERROR 行）。
  tags: [vcsetup, error-mode, config-editing, chassis-id]

- id: ce07
  title: 在 stackport 平台（6360 等）配置 vf-link-mode static 不被支持
  type: counter-example
  source_chapter: "p196"
  source_quote: |
    "6: virtual-chassis vf-link-mode static
    ERROR: This configuration is not supported for stackport platform"
  summary: |
    版本/平台坑：把静态 VFL 配置（OS6900 的做法）照搬到 6360 这类 stackport 平台。启动时 vcsetup.cfg 解析直接报错，VC 建不起来。正解：stackport 平台用 virtual-chassis vf-link-mode auto + auto-vf-link-port <端口>（LAB2 修复命令）；平台差异参考 p533 对比表——OS6900 为静态 chassis-id 分配（每台 vcsetup.cfg 手工配），OS6560/6860 支持 Auto-VC（无 vcsetup.cfg 时自动分配）。
  tags: [virtual-chassis, platform-limitation, static-vfl, version-pitfall]

- id: ce08
  title: VFL member-port 编号与 chassis-id 不一致
  type: counter-example
  source_chapter: "p196"
  source_quote: |
    "8: virtual-chassis chassis-id 2 vf-link 0 member-port 3/1/27
    ERROR: Chassis id needs to be consistent with chassis/slot/port"
  summary: |
    反例：B 台（chassis-id 2）的 VFL 成员口写成 3/1/27——端口号第一段必须等于本机 chassis-id（应为 2/1/27）。这是从其他配置复制粘贴后忘改编号的典型错。后果：该行解析失败，VFL 成员口缺失，debug status 报 NOK_08/09/14 链。正解：member-port 永远以本机 chassis-id 开头；改完 cat vcsetup.cfg 复核再 reload。
  tags: [virtual-chassis, member-port, copy-paste, numbering]

- id: ce09
  title: FPGA/CPLD/U-Boot 升级顺序颠倒
  type: counter-example
  source_chapter: "p102"
  source_quote: |
    "Note: AOS must be upgraded prior to performing an FPGA/CPLD or U-boot upgrade."
  summary: |
    反例：为了满足新版本的 U-Boot/FPGA 门槛，先升 U-Boot/FPGA 再升 AOS。铁律原文：必须先升 AOS，再做 FPGA/CPLD 或 U-Boot 升级。升级前先跑 show hardware-info 拿当前版本对照 release note 的最低要求（如 6360 的 U-Boot/FPGA 规格表，见 p102 配图），命中门槛才动，且用 update uboot cmm all file ... / update fpga-cpld cmm all file ... 的标准命令。
  tags: [upgrade-order, uboot, fpga, release-note]

- id: ce10
  title: 高峰期在核心交换机上 clear arp-cache
  type: counter-example
  source_chapter: "p129"
  source_quote: |
    "But, clearing the ARP cache might cause a slight interruption in the network, if done at peak hours and, on the Core switch. (re invoke the process of ARP learning)"
  summary: |
    反例：ARP 表疑似脏数据就直接 clear arp-cache，且在业务高峰、且在核心设备上执行。后果：全网重新 ARP 学习，造成短暂中断。正解：清 ARP 缓存前评估时段与设备位置；替代方案优先（终端配静态 MAC、修正真正的不一致条目）；确要清则选维护窗口并预告影响。
  tags: [arp, clear-arp-cache, maintenance-window, impact]

- id: ce11
  title: 以为能从网管侧做 ONIE 密码恢复
  type: counter-example
  source_chapter: "p78"
  source_quote: |
    "Password recovery from ONIE mode of OS6860N and OS6900 switches: The password recovery is only possible from the switch console"
  summary: |
    反例：OS6860N/6900 忘记密码后尝试经 SSH/Telnet 进 ONIE 恢复。原文限定：ONIE 模式密码恢复只能从交换机 console 做。正解：物理接 console，重启打断进 ONIE→DIAG→blkid/cd /mnt/ssd5/system→rm userTable8→reboot（p79 全命令序列），之后 modify running working 切目录并从 certified 重启（p80）。U-Boot 型号路径不同（setAdminPasswordDefault，p76），先分清机型再动手。
  tags: [password-recovery, onie, console-only, os6860n]

- id: ce12
  title: RADIUS 测试失败就断定服务器坏（忽略 MD5/PAP 前提）
  type: counter-example
  source_chapter: "p309"
  source_quote: |
    "Be aware that the authentication method can only be MD5 or PAP, the server may not be configured for those methods so additional RADIUS server configuration might be required"
  summary: |
    反例：aaa test-radius-server 返回 Reject/超时即判 RADIUS 服务器故障。隐藏前提：交换机测试工具只支持 MD5 或 PAP，服务器侧很可能默认未开放这两个方法，测试失败可能是方法不匹配而非服务不可用。正解：测试失败时先在服务器侧确认（或补配）MD5/PAP；结合服务器侧日志与抓包区分"链路不通/凭据错/方法不支持"三种情况，再下结论。
  tags: [radius, aaa-test, authentication, false-negative]

- id: ce13
  title: 用 QoS 策略抓出向流量——策略只匹配 ingress
  type: counter-example
  source_chapter: "p216"
  source_quote: |
    "Since policies applies only ingressing traffic we want to capture egressing icmp traffic to laptop 192.168.7.10 ... port-monitoring 1 source port 1/1/1 capture-type full enable file /flash/capture.cap"
  summary: |
    反例：想统计/镜像设备出向（egress）流量，配了 policy condition/action 却永远 0 命中。原因：QoS 策略只作用于入向流量。正解：出向分析改用端口抓包 port-monitoring（capture-type full 支持大包如 1000 字节 ping 的完整截取，存 /flash/capture.cap 后 FTP 取回）；镜像需求可用 policy action mirror（策略镜像，p306），但注意端口镜像与端口监控不能同端口配置、策略镜像同时只支持 1 会话。
  tags: [qos, ingress-only, port-monitoring, egress, capture]

- id: ce14
  title: RPM 镜像 VLAN 里捎带业务流量 / 期待抓到控制平面报文
  type: counter-example
  source_chapter: "p305"
  source_quote: |
    "RPM VLAN has to be configured on the source, destination and intermediate switches ... No other traffic is allowed on that VLAN
    The following types of traffic will not be mirrored: LACP, LLDP, 802.1x, 802.3ag (OAM), Layer 3 control packets, GARP"
  summary: |
    两个 RPM 相关误区：1) 把镜像 VLAN 当普通 VLAN 复用承载业务——RPM VLAN 必须专用于镜像，混入流量会破坏镜像数据且违反设计约束；2) 抓包里找不到 LACP/LLDP/802.1X/OAM/L3 控制/GARP 报文就怀疑设备不发——这六类流量设计上就不被镜像，判读抓包结论前先排除该项。
  tags: [rpm, mirroring, dedicated-vlan, control-traffic]

- id: ce15
  title: VRRP 两端虚拟 IP 抄错一位，症状表现为"对端疯狂刷错"
  type: counter-example
  source_chapter: "p283"
  source_quote: |
    "ip vrrp 2 interface 'int_30' address 192.168.30.154  (sw8, 应为 .254)
    VRID Errors : 41 ... ip vrrp 2 interface 'int_30' address 192.168.30.254 -> ERROR: At least one IP address must be associated with the virtual router"
  summary: |
    LAB4 双重陷阱：1) sw8 把 VRID2 虚拟地址配成 192.168.30.154（sw7 为 .254），两台互收"虚拟 IP 不匹配"的 VRRP 通告，统计上表现为 VRID Errors=41——新手容易当成攻击或版本 bug；正解是逐行比对两台 show configuration snapshot vrrp。2) 重建 VRID 时先 no 掉再 enable 报 "ERROR: At least one IP address must be associated with the virtual router"——原因不是命令错，而是 int_30 接口本身 DOWN（无可用地址）；正解先 show ip interface 查接口、ip interface int_30 admin-state enable 再启用 VRID。
  tags: [vrrp, virtual-ip, typo, vrid-errors, dependency]

- id: ce16
  title: MSTI 的 VLAN 没在互联链路 tagged，MSTP 行为不可预测
  type: counter-example
  source_chapter: "p184"
  source_quote: |
    "All VLANs within an MSTI must be tagged on all interswitch links otherwise MSTP becomes unpredictable"
  summary: |
    反例：MSTP 域内某交换机间链路上，属于某 MSTI 的 VLAN 有的没配 tagged（漏 tagging 或落成 untagged/native）。后果不是报错而是"MSTP 行为不可预测"——region 可能分裂、实例状态飘，比直接故障更难查。正解：MSTP 三一致（region 名、MSTI-VLAN 映射、同域配置全同）+ 所有 MSTI VLAN 在所有交换机间链路 tagged；排查时逐链路核 show vlan members 的端口类型。
  tags: [mstp, tagging, region, unpredictable-behavior]

- id: ce17
  title: 随手调 STP 定时器"优化收敛"
  type: counter-example
  source_chapter: "p187"
  source_quote: |
    "Take special care if you plan to change STP timers from their default values (impact on diameter and stability of the STP)
    The only parameters that you may want to change are the bridge priority (to select the root bridge) and the port cost or priority"
  summary: |
    反例：为了"快收敛"缩短 Hello/Max Age/Forward Delay。后果：影响 STP 直径计算与稳定性，网络直径超标时出现幽灵环路/震荡。教材立场：唯二可调的是桥优先级（定根）与端口 cost/priority（控冗余与负载分担），定时器保持默认（Hello=2/MaxAge=20/FwdDelay=15）。配套红线：单个阻塞口误转成转发可瘫痪大半个网络——所以"知道每个 VLAN 哪些口该阻塞"是必备文档。
  tags: [stp, timer-tuning, diameter, design-discipline]

- id: ce18
  title: VC 变更时 write memory 弹出 chassis missing 警告随手回车
  type: counter-example
  source_chapter: "p197"
  source_quote: |
    "WARNING - Virtual chassis topology change detected. Chassis 2 missing!
    Configuration associated with missing chassis will be erased permanently!
    Confirm to continue (Y/N) : y"
  summary: |
    反例：VC 拓扑处于变更/半拆状态时执行 write memory，看到警告习惯性确认。后果：缺失机箱（Chassis 2）关联的配置被永久删除。正解：读到 "erased permanently" 字样必须停——先确认拓扑变化是预期的（比如确实在移除成员）再 Y；排障中途的临时拓扑变化期避免随手保存配置。同理，Teams Bot 的 Client Secret 只在创建时显示一次（p356/p408："DO NOT forget to save it during this phase"），错过只能重建。
  tags: [virtual-chassis, write-memory, permanent-loss, confirm-dialog, secret]

- id: ce19
  title: 把 LAB 里的 DoS 告警刷屏当成真实攻击处置
  type: counter-example
  source_chapter: "p199"
  source_quote: |
    "+++ VRF 0: DoS type invalid ip from 192.168.30.8/00:00:5e:00:01:02 on port 1/1/3 +++ to 224.0.0.18 ...
    CPU 98"
  summary: |
    误诊样例（LAB2 原文场景）：6860-B 持续刷 ipni dos WARN（invalid ip → 224.0.0.18，即 VRRP 组播），表面像 VRRP 异常或攻击。真根因：VLAN 278 未开 STP，1/1/15-16 成环，本机 VRRP 通告（源 00:00:5e:00:01:02）被环回从"错误端口"收回，触发 invalid-ip 检测，同时 MAC/ARP 漂移把 CPU 打到 98-100%。判别口诀：DoS invalid ip 持续刷 + CPU 高 + 源 MAC 是 00:00:5e（VRRP 虚拟 MAC）→ 先查环（开 slni macmove debug 看 MACMOVE），不要急着上防攻击策略或封端口。
  tags: [misdiagnosis, dos-alert, vrrp, loop, high-cpu]

- id: ce20
  title: 只修一层就收工——OSPF 多重配置错叠加
  type: counter-example
  source_chapter: "p288"
  source_quote: |
    "Not solve, check if there is not another problem ...
    HELLO from 172.16.17.1 discarded...invalid helloInterval 10"
  summary: |
    LAB4 原文流程演示的反例：修完 OSPF 认证密钥（alcatel→alcatell 修正）后路由没有完全回来，教材特意写 "Not solve, check if there is not another problem"——继续深挖才找到第二个错（hello-interval 20 vs 10）。教训：配置类故障常多错叠加在同一邻接上，每修一层必须复测（邻居 Full + 路由数回基线）才能收工；只对单一致命错误成立"一次修复"假设。
  tags: [ospf, layered-faults, verify-fix, hello-interval]
