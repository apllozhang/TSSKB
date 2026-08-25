# Verified 候选（V1 原文真实性核对 + V2/V3 抽查）

## cases

## 升级前置（Appendix D）
- **C1** 升级前健康巡检：`show system`（确认日期/版本/型号/Flash 余量）→ 删旧日志 `rm *.log`、`rm *.tar` → 检查 /flash/pmd 与 /flash/pmd/work（<10 天的新文件先联系 Support）→ `show running-directory` 确认 CERTIFIED+SYNCHRONIZED，不是则 `write memory flash-synchro`。 <<<PAGE 70>>>
- **C2** 升级前基线采集：`show tech-support` / `show tech-support layer2` / `show tech-support layer3`（自动落日志到 /flash）+ `show tech-support eng complete`（TAR 含多份日志与 SWLOG），导出留档。 <<<PAGE 71>>>
- **C3** 固件版本核对：`show hardware-info` 查当前 U-Boot/FPGA 版本，对照 System Specifications 表的 Minimum 列，低于最小值走 FPGA/U-Boot 升级流程。 <<<PAGE 4>>>
## 标准升级（Appendix E，独立机箱或 VC）
- **C4** 五步标准升级：①下载镜像（6360=Nosa.img、6465/6560=Nos.img、6570M=Wos.img、6860/6865=Uos.img、6860N=Uosn.img、6870=Kaos.img、6900=Yos.img、9900=Mos.img+Mhost.img+Meni.img）→ ②FTP 二进制传到 Running 目录 → ③`reload from working no rollback-timeout`（VC 会自动复制镜像到全部 Slave 并整环重启，5-20 分钟）→ ④验证 `show microcode`（含 Secure Boot 列）+ `show running-directory`（CERTIFY NEEDED）→ ⑤`copy running certified` 固化。回退：`reload from certified no rollback-timeout`。 <<<PAGE 72>>>/<<<PAGE 73>>>
## ISSU（Appendix F，VC 或模块化机箱）
- **C5** 十二步 ISSU：`mkdir /flash/issu_dir` → `debug show virtual-chassis connection` 查 Slave VFL IP（127.10.x.65）→ `ssh 127.10.2.65`（密码 switch）→ Slave 上 `rm -r /flash/issu_dir` 清同名目录 → `exit` → Master `cp /flash/working/*.cfg /flash/issu_dir` → FTP 镜像+issu_version 到 ISSU 目录 → `ls /flash/issu_dir` 核对 → `issu from issu_dir` → `show issu status`（pending→not active 即完成；期间禁改配置，等 [L8]/System ready）→ `debug show virtual-chassis topology` 确认全部 System Ready → `write memory flash-synchro` 认证 → 可选 `copy certified working make-running-directory` 恢复原运行目录。 <<<PAGE 74>>>-<<<PAGE 76>>>
## FPGA / U-Boot 升级（Appendix G）
- **C6** FPGA/CPLD 升级：下载 kit（如 fpga_kit_9631）→ FTP 到 /flash → `update fpga-cpld cmm all file fpga_kit_9022`（all 参数覆盖 VC 全部成员）→ 显示 "Reload required to activate new firmware" 后重启。 <<<PAGE 79>>>/<<<PAGE 80>>>
- **C7** U-Boot 升级：FTP u-boot tar 包到 /flash → `update uboot cmm all file /flash/u-boot.8.10.R04.37.tar.gz` → 重启生效。 <<<PAGE 80>>>
## CPLD/ONIE 升级（Appendix H，ONIE 机型）
- **C8** ONIE 机型 CPLD/ONIE 升级：确认配置 certified+synchronized、建议接 console → FTP updater kit 到 /flash → `update fpga-cpld cmm all file updater_kit_8629`（多 CPLD 需多次执行，无升级会提示 no pending）→ 手动 reload 进 "ONIE: Update ONIE" 模式（勿按键）→ 自动更新 CPLD 后只启动到 Certified 目录 → OS6860N（除 U28）自动上电循环，其他机型手动 power cycle → ONIE 更新 `pkgmgr install uosn-onie-v1.deb`（6870 用 kaos-onie-v1.deb）→ reload 回 running 目录。 <<<PAGE 81>>>/<<<PAGE 82>>>
- **C9** U-Boot 平台（6360/6465/6560/6570M）：先 `update uboot` 到 8.10.37.R04 → 再用 Secure Boot 镜像升 AOS。 <<<PAGE 105>>>
- **C10** ONIE 平台（6860N/6870/6900-X48C6 等）：用 Secure Boot 镜像升 AOS → 重启进 BIOS 启用 Secure Boot →（仅 6860N/6870）`pkgmgr install uosn-onie-v1.deb` + `write memory flash-synchro` 升 ONIE/Diag。 <<<PAGE 105>>>
- **C11** 6900-V48C8/C32E：先升 BIOS（C32E v40.01.01.03 / V48C8 v40.01.01.04，联系 Support）→ 再升 Secure Boot 镜像 → 重启进 BIOS 启用。 <<<PAGE 105>>>
## 包管理与密码治理（Appendix J）
- **C12** 包安装/卸载：`pkgmgr verify nos-mrp-v1.deb`（MD5 校验）→ `pkgmgr install nos-mrp-v1.deb` → `write memory`（不 commit 重启会镜像校验失败）→ `show pkgmgr`（+ 未保存、* 待 reload）；卸载 `pkgmgr remove mrp` → `write memory` → `rm /flash/working/pkg/nos-mrp-v#.deb`。 <<<PAGE 101>>>/<<<PAGE 102>>>
- **C13** 升级前 AMS/IoT-Profiler 密码加密化：升级 8.7R1+ 前删 `/flash/<running>/pkg/ams/ams-broker.cfg`（每台 VC 成员）→ 升级 → 重配 broker（密码自动加密）；AMS-APPS 同理删 `pkg/ams-apps/install.sh`，升级后 ovbroker.cfg 密码加密。 <<<PAGE 102>>>
## 热插拔与电源（Hot-Swap Guidelines）
- **C14** 模块热插拔规程：拆线 → 拔光模块 → 拔板卡等 ≥30 秒再插同型号（CMM 插后等 15-20 分钟；NI 拔插间隔 30 秒；新模块插入间隔 5 分钟且 LED 回正常）→ 重插光模块 → 接线；CFM 一次只换一个、120 秒内完成、风扇框必须全程在位。 <<<PAGE 47>>>/<<<PAGE 48>>>
- **C15** fast/perpetual PoE 机型换异种电源（6860N-P48M）：禁 fpoe/ppoe（lanpower 已启才需）→ 保存同步配置 → 换电源 → reload 机箱 → 启 lanpower → 重新启 fpoe/ppoe → 保存同步。 <<<PAGE 48>>>/<<<PAGE 49>>>
## 安全加固与特性运维（散点）
- **C16** 弱加密禁用与查看：`system security crypto-strong-security enable` + `show system security`；弱密钥探测 `ssh strong-hmacs enable`。 <<<PAGE 28>>>/<<<PAGE 16>>>
- **C17** SPB BVLAN 收敛运维：`show spb isis bvlans` 查 In Use（全网视图）→ 维护窗内把业务删并重建到 4 条 BVLAN → 空闲 BVLAN 全网删除（无影响）。 <<<PAGE 66>>>
- **C18** Celona PD 降级规避：`lanpower {slot | port} autoclass disable`。 <<<PAGE 34>>>
- **C19** MKA VLAN 隧道化配置：`interfaces <c/s/p> macsec mode dynamic mka-vlan <vid> [mka-tpid <tpid>]`；撤销 `no interfaces <c/s/p> macsec mka-vlan`；验证 `show interfaces macsec mka-info`。 <<<PAGE 35>>>

---
合计：19 条（C1-C19）。

## counter-examples

## 升级陷阱（Secure Boot / ISSU / 版本迁移）
- **X1** Secure Boot 先升 U-Boot 再升 AOS：6360/6465/6560/6570M 必须 U-Boot ≥8.10.37.R04 才能升 8.10R4，次序颠倒则装了 Secure Boot 镜像重启回落 Certified："This will require a U-boot upgrade on the OS6360, OS6465, OS6570 and OS6570 platforms prior to upgrading to AOS 8.10R4." <<<PAGE 18>>>/<<<PAGE 104>>>
- **X2** ISSU 在 6360/6465/6560(E)/6570M 全系不支持（因 Secure Boot U-Boot 升级要求），只能标准升级："ISSU is not supported on the OS6360, OS6465, OS6560 or OS6570M platforms due to U-boot upgrade requirement for Secure Boot." <<<PAGE 69>>>
- **X3** 6900 双镜像分裂：V72/C32/V48C8/C32E 只能用非 Secure Boot 镜像（V48C8/C32E 需 BIOS 升级但尚未提供）；这些型号与其它 6900 混 VC 时全网必须用非 Secure Boot 镜像："If an OS6900-V72/C32/V48C8/C32E needs to be mixed with other OS6900 platforms in a VC then the non-Secure Boot image must be used on all platforms." <<<PAGE 104>>>
- **X4** Secure Boot 不支持平台清单：6860(E)、6865、6900-V72/C32/V48C8/C32E（无 BIOS 升级时）、9900 <<<PAGE 104>>>
- **X5** 8.10R3 起 EVPN 强制 VRF 语境：升级到 8.10R3+ 后旧版 EVPN 配置必须手工迁入对应 VRF context，否则失效："any existing EVPN configurations from earlier releases must be manually reconfigured under the appropriate VRF context." <<<PAGE 18>>>
- **X6** EVB 配置存在则无法升级：8.5R4 起移除 EVB，带 EVB 配置的交换机禁止升到 8.5R4 及以上："Any switches with an EVB configuration cannot be upgraded to 8.5R4 or above." <<<PAGE 16>>>
- **X7** 6570M 出厂 U-Boot 8.10.42.R02 只认签名镜像（8.9R4+），要降级到更早 AOS 必须先降 U-Boot 到 <8.9.70.R04 再降 AOS："To use AOS releases prior to 8.9R4 the u-boot version must first be downgraded to a version below 8.9.70.R04 before downgrading AOS." <<<PAGE 18>>>
- **X8** 8.10R4 首访强制改密会打断自动化：admin 默认口令的 REST API/脚本必须改 <<<PAGE 18>>>/<<<PAGE 27>>>
- **X9** 8.7R2 起新用户口令策略默认收紧（禁含用户名、大写/小写/数字/非字母各≥1），存量用户不受影响 <<<PAGE 17>>>
- **X10** 6560 两款电源强制最低 AOS 8.8R1：OS6560-BP-PH（600W）与 OS6560-BP-PX（920W）在旧版被软件拦截 <<<PAGE 17>>>
- **X11** 8.9R1 起 6560 Metro 特性转收费：CPE Test Head/PPPoE-IA/Ethernet OAM/SAA/Link OAM/VLAN Stacking/DPA/硬件环回/IPMVLAN 需 Metro 许可 <<<PAGE 19>>>
- **X13** 升级后 SPB 控制 MAC 回落缺陷（已修）：8.9R2→8.10R2 升级曾把配置的 SPB 控制 MAC（09:00:2b）回落为默认（01:80:c2）导致邻接丢失，8.10R4 修正 <<<PAGE 94>>>
- **X14** ISSU 期间禁止改配置：等 System ready/[L8] 再做 write-memory/配置变更 <<<PAGE 76>>>
- **X15** Slave 存在同名 ISSU 目录会破坏升级：ISSU 依赖交换机自行在 Slave 建目录，预先存在的同名目录有 adverse effect，须 SSH 到 Slave（VFL 内网 IP 127.10.x.65）删除 <<<PAGE 75>>>
- **X16** 包未 commit 会引发镜像校验错误：reload 时 image validation errors，pkgmgr install 后必须 write memory <<<PAGE 101>>>
- **X17** 升级前 AMS/IoT-Profiler 明文密码处理：升级 8.7R1+ 前必须先删 ams-broker.cfg / install.sh（每台 VC 成员），否则密码不会转加密 <<<PAGE 102>>>
- **X18** ONIE 机型 CPLD 升级后不回 running 目录：只启动到 Certified，需手动再切 <<<PAGE 82>>>
- **X19** 出厂 diag.img 可安全删除（内部诊断用），勿当作系统文件保留 <<<PAGE 15>>>
- **X20** 长期运行陷阱：6450 动态路由在 uptime 超 828.5 天后老化复位抖动（自动恢复）——超长不重启的网关设备要留意 <<<PAGE 90>>>
## 平台与端口级限制
- **X21** OS6560-P48Z16（903954-90 旧版）1G 口 1-32 不支持链路聚合，仅 33-52（多千兆/10G）支持；升级时旧配置里的非法 linkagg 会被静默移除；且 1-32 口入方向不丢超长帧；同型号其他 PN 是新版无此限制，只能靠 PN 区分："The 1G ports (ports 1-32) do not support link aggregation (CRAOSX-1766)." <<<PAGE 15>>>
- **X22** MACsec 端口矩阵例外：6870-24 口 25-26、6870-48 口 49-50 不支持；6870 VFL 模式端口不支持；6860E-P24Z8 2.5G 口不支持；6865 系列不支持；6900 仅 X48C4E（Dynamic only）；9900 CNI-U8 不支持 <<<PAGE 62>>>
- **X23** 6860N 不支持 MACsec Static 模式（仅 Dynamic 128-bit），且扩展模块上任何 4X10G splitter 光模块都不支持 <<<PAGE 17>>>/<<<PAGE 63>>>
- **X24** 快速收敛例外清单：铜口/铜模块、VFL 口、splitter 口（4X10G/4X25G）、OS6865-P16X·U12X 口 3/4、OS6570M-12/12D 口 9/10 不支持 <<<PAGE 15>>>
- **X25** 6560 X4 系列 10G 性能许可只解锁特定口：24X4/P24X4 口 25/26、48X4/P48X4 口 49/50（默认 1G）；6570M-U28 口 25-28、6870-LNI-U6（50G）同理 <<<PAGE 19>>>
- **X28** 6920 本版无 VC 支持；不支持 IP-IP/GRE/配置 IPv6/6to4 隧道 <<<PAGE 21>>>/<<<PAGE 43>>>
- **X29** 6575-MP16 无 VC 支持（P12/U28 支持最多 4 机箱 VC） <<<PAGE 21>>>
- **X30** 9900 XNI 板用于 CMM2/OS9912 机箱前必须先升 U-Boot 与 FPGA；OS99-XNI-U12Q 与 OS9912 机箱不兼容："Existing OS9900 NIs that are to be used with a CMM2 or in an OS9912 chassis must first have the Uboot and FPGA upgraded." <<<PAGE 14>>>
- **X31** SPB BVLAN 修改不支持在线改：服务必须删除重建到新 BVLAN，收敛操作要安排维护窗 <<<PAGE 65>>>
- **X33** WebView 法语支持 8.8R2 起移除，默认法语的设备升级后回落英语 <<<PAGE 17>>>
- **X34** 6570M TDR 仅限铜口：12/12D 口 1-8；U28 仅 hybrid 口 21-24 且 hybrid-mode=copper <<<PAGE 38>>>
- **X35** PKI 私钥与 installsshkey 曾不随 VC 主备同步（8.10R4 修复，复制到 /flash/switch/.profiles 并全机箱应用） <<<PAGE 87>>>
- **X36** FTP 用户名（RCD）上限 15 字符（规范限制，8.10R4 文档化） <<<PAGE 91>>>
- **X37** vcboot.cfg 含明文 key 会导致哈希错误：即使 show 显示 hash-key，RADIUS 会话也建不起来，必须用交换机生成的 hash-key/hash-salt <<<PAGE 91>>>
## Open CR — 光模块/硬件类已知问题（8.10R4 未修）
- **X38** SFP-10G-T 只支持 10G 对端：1G/100M 对端链路 down；100M 长时间连接+多次翻动后可能回 10G 也恢复不了："Recommend peer end to be strictly at 10G." <<<PAGE 42>>>
- **X39** SFP-GIG-T 配 10M 时反复 admin disable/enable 会端口不稳定（假 linkup/无流量）；1G/100M 配置无此问题 <<<PAGE 42>>>
- **X40** OS99-CNI-U8 4x25G DAC 某些 lane 不起来，workaround 换 QSFP-100G-SR4 光纤 <<<PAGE 42>>>
- **X41** SFP-DUAL-BX-U/D 在 6870-P24Z/P48Z/LNI-U6 不 link up，只能用于 6870-24/48/V12 的 1G <<<PAGE 43>>>
- **X42** 6570M-U28 口 25 + SFP-10G-T 对端反复 admin 翻动会出现仅本地 linkup 或 LED 亮链路 down <<<PAGE 42>>>
- **X43** SFP-GIG-T 对端从 10M 变 100M/1G 间歇性链路 down（对端 up）：U28 热插拔模块恢复，12/12D 可能要整机重启 <<<PAGE 42>>>
- **X44** VFL 用 4X25G splitter 出 CRC：需两侧 inter-frame-gap=13（首选）或 FEC FC+关自协商（会引起链路复位） <<<PAGE 42>>>
- **X46** OS6860N-U28 控制台可能打印 smgrOpenLicenseFile 错误，无功能影响 <<<PAGE 43>>>
## Open CR — 软件/协议类已知问题（8.10R4 未修）
- **X47** OS9912 聚合口禁用某成员后哈希失衡，流量可能全压一条剩余链路，无解 <<<PAGE 41>>>
- **X48** PTP 打戳 PHY 口↔PHYless 口交叉时不正确（6870-V12 1-12 ↔ 13-14/CNI/LNI；6570-U28 1-24 ↔ 25-30），高 2wayTimeError，无解 <<<PAGE 41>>>
- **X49** breakout 模式 subport A 的 LED1 链路/活动状态可能不反映真实状态，用 CLI 确认 <<<PAGE 41>>>
- **X50** BFD 在 VRRP VLAN 接口 toggle 时丢包，无解 <<<PAGE 41>>>
- **X51** CFM2+XNI-U48 板违规恢复比 WTR 15 秒多花约 2 分钟 <<<PAGE 41>>>
- **X52** OS6575 8 成员 LAG 禁主口后组播/广播负载失衡（降到 7 成员时某成员停转广播），无解 <<<PAGE 41>>>
- **X53** OS6920 多项协议缺口：ICMP redirect（type5 code1）不转发、Snap 头场景 ARP 解析失败、IPv6 隧道不转发 ICMPv6、组播 VLAN source-timeout 不可配、IPMSv6 nack 口收流量、IP Options ICMP 回包 ID 错、组播 MAC 广播不转发 <<<PAGE 43>>>/<<<PAGE 44>>>
- **X54** EVPN 一组 toggle 触发掉流：对称 IRB service toggle 掉流（含 6870）、PIM+非对称 BGP admin-state toggle 掉流、非对称 OSPF admin-state toggle 掉流；多站点删 BL/改 pod id/禁 BGP 后动态学习服务不 down，均无解 <<<PAGE 44>>>
- **X55** IPMVLAN+rvlan 在 VC takeover 后残留 L3 模式行为，无解 <<<PAGE 43>>>
- **X56** 二次 vc-takeover 后 sdp/sap MAC 可能从 show mac-learning 丢失，重发流量可恢复 <<<PAGE 45>>>
- **X57** OS9900 chassis-2 偶发 cmm-takeover 后 VC 分裂，无解 <<<PAGE 45>>>
- **X58** 端口违规恢复偶发多 5 秒 <<<PAGE 45>>>
- **X59** OS99-XNI-P24Z8 前 8 口 dynamic MACsec reload 后状态 down，需手动 toggle MACsec admin state <<<PAGE 45>>>
- **X60** 静态 MACsec 无加密时 key 不匹配流量仍通（有加密则正常）——安全审计注意 <<<PAGE 45>>>
- **X61** CMM2 NI 卡上 policy mac group alaPhones 默认 802.1p 信任行为变化，执行 `qos apply` 恢复 <<<PAGE 45>>>
- **X62** OS6900-V48 无损 TC 上限 40：DCB-2/4 profile（全 TC 无损）最多 5 端口，更多端口需自定义 QSP DCB profile 只配必要无损 TC，否则丢包/入口降速 <<<PAGE 45>>>/<<<PAGE 46>>>
- **X63** OS6575 启用 policy rule Redirect_All 后掉流量，无解 <<<PAGE 46>>>
- **X64** ERP 环端口/节点 down/up 摆动时收敛次数偏高（10 次迭代平均），无解 <<<PAGE 43>>>
- **X65** OS6575 组播 UNP policy list v4/v6 规则计数不更新（仅显示问题） <<<PAGE 44>>>
- **X66** 多 SAP 口上部分 SAP 配 port-security 时，全端口 SAP 的 ARP 包都被 trap 学习 <<<PAGE 44>>>
- **X67** 极小流量（10 包）SPB 测试偶发丢包，正常流量模式不见 <<<PAGE 44>>>
## 行为变更与废弃（部署前必查）
- **X68** OVSDB 8.10R2 起移除；automatic fabric admin-state 8.10R2 起默认禁用 <<<PAGE 17>>>
- **X69** 分布式 ARP、WRED、`qos dscp-table` 于 8.6R2 移除；`ip helper`→`ip dhcp relay`（8.6R1，旧格式 vcboot.cfg 兼容）；SAA vlan-priority/drop-eligible 废弃；DHCPv6 Guard 接口名格式改为 vlan 形式 <<<PAGE 16>>>
- **X70** mrp interconnect 三条命令在 8.8R1 存在但不支持（part of AOS but not supported） <<<PAGE 17>>>
- **X71** Kerberos Snooping 8.7R3 不支持 bridge mode <<<PAGE 17>>>
- **X72** SPB Auto Fabric BVLAN 默认 16→4（8.7R1），仅对出厂默认且无 vcboot.cfg 的设备生效，升级不改存量 <<<PAGE 17>>>
- **X73** NTP 的 `ip service source-ip ntp` 参数 8.5R4 废弃、8.6R2 恢复——跨版本升级注意配置漂移 <<<PAGE 17>>>
- **X74** 8.8R1 起 CVE-2024-6387（regreSSHion）修复默认内建 <<<PAGE 17>>>
- **X75** 软件获取卡停止随箱附带（环保），软件走 Business Portal <<<PAGE 16>>>

---
合计：75 条（X1-X75）。

## frameworks

- **F1** AOS 升级方法论二分框架：Standard（传镜像到 Running 目录→reload→验证→copy running certified，全程一次中断）vs ISSU（逐成员/逐 CMM 升级、双归属主机不断链）；选型三问——平台是否支持 ISSU（6360/6465/6560/6570M 不支持）、源版本是否在 ISSU 支持清单、是否需要保留 running 目录名（ISSU 后可 make-running-directory 切回）。升级前置四查：certified 配置、U-Boot/FPGA 版本、tech-support 基线、EMP/console 带外通道。 <<<PAGE 67>>>-<<<PAGE 76>>>
- **F2** 固件三件套分层框架：AOS 镜像（功能性升级）／引导件 U-Boot·ONIE·BIOS（Secure Boot 信任链、NAND/eUSB 修复、启动模式）／逻辑件 FPGA·CPLD（电源、风扇、PoE、端口 PHY 行为）三者独立演进、版本矩阵按机型×部件列 Minimum/Current；排障口诀——先 `show hardware-info` 对 Minimum，再决定是否走 `update fpga-cpld`/`update uboot`/`pkgmgr install *-onie`。CR 驱动：每条 FPGA/U-Boot 升级都对应 CRAOS8X 编号，可反查"我这个现象要不要升固件"。 <<<PAGE 4>>>-<<<PAGE 14>>>/<<<PAGE 77>>>-<<<PAGE 82>>>
- **F3** Secure Boot 平台分型框架：U-Boot 型（6360/6465/6560/6570M——先升 U-Boot 再升镜像，之后只认 Secure Boot 镜像）／ONIE 型（6860N/6870/6900-X 系列——BIOS 使能+ONIE 包，过渡期兼容非 SB 镜像）／例外型（6860(E)/6865/9900/6900-V72·C32·V48C8·C32E 不支持或需 BIOS）；混 VC 用"最小公分母"（非 Secure Boot 镜像）。 <<<PAGE 104>>>/<<<PAGE 105>>>
- **F4** Feature Matrix 特性核对法：13 平台 × 特性 × 首次支持版本（Y=历来支持 / N=不支持 / 版本号=该版引入 / EA=Early Availability 未完整验证不支持）；选型/排障三步——先定平台列，再看特性行版本，最后对照 Licensed Features 表确认是否要许可（Feature/Performance、Metro、Advanced Routing、Premium 四类）。 <<<PAGE 52>>>-<<<PAGE 61>>>/<<<PAGE 19>>>

---
合计：4 条（F1-F4）。

## glossary

- **GA（General Availability）**：正式发布版，如 8.10.86.R04 (GA)，区别于 MR（维护版）与 EA <<<PAGE 4>>>
- **MR（Maintenance Release）**：维护版本（如 8.9.130.R04 MR1），作为 ISSU 源版本时常被列出 <<<PAGE 68>>>
- **EA（Early Availability）**：早期可用特性——可配置但未走完整验证流程、不受官方支持："they have not gone through the complete AOS validation cycle and are therefore not officially supported." <<<PAGE 15>>>
- **U-Boot**：嵌入式引导加载器；Secure Boot 镜像要求 8.10.37.R04（6360/6465/6560/6570M），`show hardware-info` 查版本 <<<PAGE 4>>>
- **FPGA**：现场可编程门阵列固件，承载电源/风扇/PoE/端口物理行为，按机型有 Minimum/Current 两列 <<<PAGE 4>>>
- **ONIE**：开放网络安装环境，6860N/6870/6900/6920 等 ONIE 型机型的引导/安装层，升级走 pkgmgr 装 deb 包 <<<PAGE 10>>>
- **CPLD**：复杂可编程逻辑器件，ONIE 机型多颗（Main/CPU/LED），updater kit 逐颗升级 <<<PAGE 11>>>
- **Coreboot-Uboot / Control FPGA / Power FPGA**：9900 平台的引导与控制/电源固件三层 <<<PAGE 13>>>
- **diag.img**：出厂可能附带的内部诊断镜像文件，可安全删除 <<<PAGE 15>>>
- **imgsha256sum**：镜像校验文件，仅 Common Criteria 模式需要 <<<PAGE 72>>>

## 升级机制（Appendix D-F）
- **Standard Upgrade（标准升级）**：镜像放 Running 目录整机/整 VC 重启的升级方式 <<<PAGE 67>>>
- **ISSU（In Service Software Upgrade）**：在服务软件升级，VC 按 chassis-id 低到高逐台重启、模块化机箱先备 CMM，业务中断最小化 <<<PAGE 67>>>
- **Certified/Working 目录**：认证（回滚兜底）/工作（试验运行）双目录机制；`copy running certified` 固化、`reload from certified` 回退 <<<PAGE 70>>>
- **rollback-timeout**：reload 参数（no rollback-timeout），用于跳过回滚等待直接切换 <<<PAGE 73>>>
- **write memory flash-synchro**：保存配置并同步 Flash（VC 成员/CMM 间），升级前置与 ISSU 后认证均用 <<<PAGE 70>>>
- **issu_version**：ISSU 升级包内的版本描述文件，ISSU 目录必备 <<<PAGE 74>>>
- **VFL（Virtual Fabric Link）**：VC 内部互联链路；内网固定 IP 127.10.<chassis>.65；4X25G splitter 场景需调 inter-frame-gap 防 CRC <<<PAGE 75>>>/<<<PAGE 42>>>
- **chassis-id**：VC 成员编号；出厂首启自动 VC 会固定为 1，可能引发重复 chassis-id 冲突 <<<PAGE 15>>>
- **vcboot.cfg / vcsetup.cfg**：VC 启动/设置配置文件；明文 key 直接加载会导致哈希错误 <<<PAGE 15>>>/<<<PAGE 91>>>

## 许可体系（Licensed Features）
- **CAPEX License**：一次性买断型许可，区别于订阅 <<<PAGE 19>>>
- **MACsec Site License（OS-SW-MACSEC）**：8.6R1 起 MACsec 需站点许可（免费生成、免重启生效） <<<PAGE 15>>>/<<<PAGE 19>>>
- **Performance License（OS####-SW-PERF）**：解锁端口速率（6560 的 10G、6570M 的 25G、6870 的 50G），默认端口降速运行 <<<PAGE 19>>>
- **Metro License**：8.9R1 起 6560 的城域特性包（CPE Test Head/PPPoE-IA/OAM/SAA/VLAN Stacking/DPA/IPMVLAN 等） <<<PAGE 19>>>
- **Advanced Routing License（OS6570M-SW-AR / OS6560-SW-AR）**：OSPF/PIM/VRF/ISIS/GRE/IP-IP/BGP 等路由特性；6560 版限 2 OSPF 区域、8.10R4 新增 BGP <<<PAGE 20>>>
- **Premium (Bundle) License（OS6570-SW-PRMxx / OS6870-SW-PRMx）**：8.10R4 引入的捆绑许可，单文件多子许可（SPB/AR/25G/50G/VxLAN-EVPN） <<<PAGE 20>>>
- **VC Parity: Match / Local-Only**：子许可 VC 生效语义——Match=全成员一致才生效；Local-Only=仅本机生效 <<<PAGE 20>>>
- **NAAS 2.0 Licensing**：Network-as-a-Service 许可框架，8.10R4 扩到 6575 <<<PAGE 28>>>
- **SILOS（Site License Client/Manager）**：站点许可客户端/管理器，6870/6900-X 系列支持 <<<PAGE 53>>>

## 8.10R4 新特性（New Features）
- **Router Mode / Edge-router Mode**：capability profile 切换的转发规模形态（6870 router mode；6900 edge-router 更大 MAC 规模，需重启生效） <<<PAGE 26>>>/<<<PAGE 37>>>
- **Secure su Account**：su 超级用户提示符必须设口令，仅 admin 可配 <<<PAGE 26>>>
- **Change Password on First Access**：admin 默认口令首登强制改密 <<<PAGE 27>>>
- **ALE CA Signed Certificate**：ALE 内部 CA 签发的设备 X.509 证书（5 年有效、到期前 1 年更新），取代自签证书，存 /flash/switch/cert.d/ <<<PAGE 27>>>
- **Crypto Strong Security**：弱加密算法（SHA/MD5 等）禁用开关 <<<PAGE 28>>>
- **Lightning Config Mode（闪电配置）**：出厂/EMP 口的快速开局模式；6575 支持 1/1/1-1/1/2，6920 支持 EMP 口 <<<PAGE 28>>>
- **AAA Certificate convert-cert**：CER/CRT/DER/P7B/PKCS#12 证书转 PEM <<<PAGE 26>>>
- **Session Prompt 64**：CLI 提示符长度 32→64 字符 <<<PAGE 26>>>
- **AOS 内嵌 Linux 命令**：watch/cut/paste/tee 经包装直接在 AOS CLI 使用，免进 su <<<PAGE 28>>>
- **DPA / MAC Forced Forwarding**：动态代理 ARP（6560/6570M 8.10R4 支持） <<<PAGE 29>>>
- **PIM over GRE**：GRE 隧道上跑 PIM 组播路由邻接 <<<PAGE 29>>>
- **sFlow BGP Gateway**：sFlow 样本携带 BGP 网关归因字段 <<<PAGE 30>>>
- **PEG（PIM EVPN Gateway）**：EVPN 网络与外部 PIM 域的网关 <<<PAGE 31>>>
- **OISM**：优化的跨子网组播，fabric 内选择性转发 <<<PAGE 31>>>
- **ERP over SPB / spb-remote-flush**：ERP 环跑在 SPB 上时让 MAC flush 传播到 SDP 端口的特性 <<<PAGE 31>>>
- **Manual RD/RT**：EVPN 服务手工路由目标配置，支撑多站点/PoD 选择性导入与 E-Tree <<<PAGE 33>>>
- **Threat-Insight**：AppMon 集成的每流威胁智能（DGA/MITM/JA3） <<<PAGE 36>>>
- **DGA Score / MITM Score / JA3 Fingerprint**：域名生成算法评分／中间人概率／TLS Client Hello 指纹三属性 <<<PAGE 36>>>
- **RoCEv2 / DCQCN**：RDMA over Converged Ethernet v2 与基于 ECN+PFC 的拥塞控制（6900/6920） <<<PAGE 36>>>
- **DCBX**：数据中心桥接能力交换协议（LLDP TLV 承载） <<<PAGE 36>>>
- **PROFINET**：工业协议，6575 通过 IO-Device 认证 <<<PAGE 37>>>
- **DHL Active-Standby**：双归链路 LACP 主备模式，standby 秒级接替+pre-empt 回切 <<<PAGE 37>>>
- **Telemetry（IPFIX 推送）**：本地 Redis DPI/流数据按 IPFIX (RFC 7011) 推送到 Telegraf/InfluxDB/Grafana <<<PAGE 39>>>
- **Multi-Site SPB / SBN / site-id**：多站点层级 SPB——站点内 ISIS L1、站点边界节点（SBN）以 3 字节 site-id 互联成 L2 <<<PAGE 40>>>
- **MKA VLAN Tag / TPID（alaSecyMkaVlan/Tpid）**：MKA 控制包打指定 VLAN 标签隧道化过中间节点 <<<PAGE 35>>>
- **PKIX SSH / CAC·PIV**：智能卡 X.509 证书 SSH 登录（JITC STIGS） <<<PAGE 33>>>
- **Device Profiling 自动启用**：全局启用后边缘端口默认启用设备画像 <<<PAGE 37>>>
- **ISFv6 on SAPs**：业务域 IPv6 源过滤（dhcpv6-snooping ipv6-source-filter service） <<<PAGE 31>>>

## 硬件与光模块（New Hardware / Open CR）
- **OS6575 家族**：-40~75°C 加固工业交换机（P12/U28/MP16 三形态） <<<PAGE 21>>>
- **OS6920-D32**：1RU 32×400G QSFP-DD 平台 <<<PAGE 21>>>
- **QSFPD-400G 系列**：400G QSFP-DD 光模块/DAC/AOC（C/DR4 500m/FR4 2km/LR4 10km/A10M 10m/SR4.2 100m 可 4×100G 拆分） <<<PAGE 22>>>
- **QSFP-100G-SR1.2 / PSM4**：100G 新模块（SR1.2 配 SR4.2 拆分；PSM4 MPO 2km） <<<PAGE 22>>>
- **SFP-10G-T / SFP-GIG-T**：10G/1G 铜口光模块，Open CR 多条涉及其速率协商缺陷 <<<PAGE 42>>>
- **Splitter（4X10G/4X25G 拆分）**：高速口拆分模式，快速收敛与部分 MACsec 不支持 <<<PAGE 15>>>/<<<PAGE 63>>>
- **VFL**：VC 内部互联用的专用上行口组（6575/6570M/6870） <<<PAGE 15>>>
- **EMP 端口**：以太网管理端口；Lightning Config 与静态 IP 支持相关 <<<PAGE 28>>>
- **RTC（实时时钟）**：6360 无 RTC，断电丢时间，需 NTP <<<PAGE 17>>>

## 运维与支持（Hot-Swap / Support / Appendices）
- **Hot-Swap（热插拔）**：运行中插拔模块；NI 间隔 30 秒、CMM 15-20 分钟、插入后 5 分钟+LED 正常，且必须同型号 <<<PAGE 47>>>
- **Fast PoE / Perpetual PoE（fpoe/ppoe）**：快速/持续供电，换异种电源前须禁用并 reload <<<PAGE 48>>>
- **Dying Gasp**：断电临终告警（trap/syslog），非默认 SNMP 端口场景 8.10R4 修复 <<<PAGE 52>>>/<<<PAGE 98>>>
- **RCD（Remote Chassis Detection）**：远程机箱检测/零触摸开局特性 <<<PAGE 53>>>
- **AMS（AOS Micro Services）**：AOS 微服务框架（deb 包形态） <<<PAGE 52>>>
- **pkgmgr**：AOS/第三方 Debian 包管理器（verify/install/remove） <<<PAGE 101>>>
- **HSP（Hitless Security Patch Upgrade）**：不打断业务的安全补丁升级 <<<PAGE 52>>>
- **Signed AOS Image**：签名 AOS 镜像（6570M 8.9R4 起，需配套 U-Boot） <<<PAGE 53>>>
- **CMM / NI / CFM**：机箱管理模块／网络接口模块／风扇模块（9900/6900 机箱语境） <<<PAGE 47>>>
- **Severity 1-4**：ALE 技术支持严重度分级（1=生产网中断……4=咨询） <<<PAGE 50>>>
- **CRAOS8X-xxxxx**：ALE 问题报告编号体系（8X=AOS 8.x），Fixed/Open CR 的索引键 <<<PAGE 41>>>
- **show tech-support eng complete**：生成含 SWLOG 的完整诊断 TAR，升级基线必备 <<<PAGE 71>>>
- **FOSS（/flash/foss）**：第三方开源组件许可声明目录 <<<PAGE 51>>>

---
合计：63 条。

## principles

## 管理与安全机制
- **P1** Secure Boot 通过启动期认证校验保证只运行可信软件，需 U-Boot/ONIE/BIOS 升级 + Secure Boot 专用镜像三件配合："Secure Boot is a important security mechanism that ensures an OmniSwitch boots with only verified and trusted software." <<<PAGE 34>>>
- **P2** U-Boot 平台（6360/6465/6560/6570M）升级 8.10R4 前必须先把 U-Boot 升到 8.10.37.R04，否则装了 Secure Boot 镜像会回落 Certified 镜像启动："If a Secure Boot image is loaded on a switch that doesn't have the 8.10R4 U-boot version installed, it will reboot from the Certified image." <<<PAGE 104>>>
- **P3** 首访强制改密：8.10R4 起 admin/switch 默认口令登录必须改密且符合 password-policy，REST API/脚本必须适配："Any REST APIs or scripts must be modified to account for the required password change." <<<PAGE 27>>>
- **P4** su 账户口令只有 admin 能配、可授权其他用户、reset-to-factory 会重置、忘记口令只能恢复出厂："The super-user password cannot be recovered. In the case of a forgotten password a factory reset will need to be performed." <<<PAGE 26>>>
- **P5** ALE CA 设备证书机制：每台设备唯一密钥对 + 内部 CA 签 X.509，有效期 5 年、到期前 1 年内更新，单 PEM 文件存证书+私钥+链；已装自定义 CA 证书的升级后继续沿用不替换 <<<PAGE 27>>>
- **P6** Crypto Strong Security 开启后用户创建只允许强算法（SHA224/256/384 及 AES 变体），禁 SHA/MD5/SHADES/MD5DES/SHAAES <<<PAGE 28>>>
- **P7** ssh-rsa（SHA-1 签名）默认禁用，替代为 rsa-sha2-256/512 与 ecdsa-sha2-nistp256/384/521；可用 `ssh strong-hmacs enable` 探测服务器弱密钥 <<<PAGE 16>>>
- **P8** 8.10R4 默认 TLS 版本从 1.0 升到 1.2，并可配 TLS 1.3（RADIUS/LDAP/SYSLOG NG/SNMP 客户端与 WebView）："The default TLS version is also changed from 1.0 to 1.2." <<<PAGE 33>>>
- **P9** PKIX SSH（CAC/PIV 智能卡）：独立 PKIX SSH 服务器 + X.509v3 证书/公钥映射本地用户 + 持久信任库与 CRL 吊销检查 <<<PAGE 33>>>
- **P10** IP 分片攻击防护新增 tear-drop（重叠/畸形分片丢弃）与 icmp-frag-drop（分片 ICMP 丢弃）两类 DoS 控制 <<<PAGE 34>>>
- **P11** IPv6 DoS 检测运行于 NI、上报 CMM 生成统计/日志/SNMP trap，支持 8 种攻击类型（Ping of Death/Land/Loopback Source/无效地址/Ping Overload/NDP Flood/分片 Tear-Drop/ICMP 分片丢弃）："IPv6 DoS detection operates on the Network Interface (NI) and reports events to the Chassis Management Module (CMM)." <<<PAGE 38>>>
- **P12** MACsec 站点许可从 8.6R1 起强制（免费生成），升级后未装许可特性禁用，装许可无需重启："After upgrading, the feature will be disabled until a license is installed. There is no reboot required after applying the license." <<<PAGE 15>>>
- **P13** MKA VLAN Tag/TPID 机制：中间节点不支持 MACsec 时，MKA 控制包需打 VLAN 标签在 NNI/业务 VLAN 中隧道化，否则被中间 NNI 接口丢弃："these packets are getting dropped on the intermediate NNI interfaces." <<<PAGE 35>>>
- **P14** MACsec 平台密钥长度分层：9900-CMM2/CNI-U20、6870、6570M、6575 为 Dynamic 256-bit；6860N 仅 Dynamic 128-bit；6900-X48C4E 仅 Dynamic；6560/6465/6860(E) Static+Dynamic 128-bit（见 Appendix B 端口矩阵） <<<PAGE 62>>>/<<<PAGE 63>>>
- **P15** 802.1X max-req 从 1-3 扩到 1-50，覆盖 PC 启动/瞬时网络导致的 EAP-Response 延迟场景 <<<PAGE 33>>>
## L2/L3 与业务机制
- **P16** Router Mode（6870）：capability profile 切换扩容转发表——64K MAC/312K IPv4 路由/156K IPv6 路由/24K ARP/8K IPv6 主机 <<<PAGE 26>>>
- **P17** Edge-router Mode（6900 除 V72/C32）：比 router-mode 更大 MAC 规模，启用后必须保存配置并重启生效；V72/C32 不能与启用 edge-router 的 6900 混 VC <<<PAGE 37>>>/<<<PAGE 38>>>
- **P18** DHL Active-Standby：LACP 聚合内一条成员 Active 一条 Standby 的确定性冗余，故障即秒级接替，不依赖 STP，支持 pre-empt 与 pre-empt timer 回切 <<<PAGE 37>>>
- **P19** IPv6 BGP 路由聚合：合并多条明细属性为单条聚合路由向邻居通告（admin-state/as-set/community/local-preference/metric/summary-only） <<<PAGE 29>>>
- **P20** PIM over GRE：PIM 可在 GRE 隧道接口上建邻并转发组播，覆盖原生组播不可达的远程网络："allowing multicast routing adjacency formation and traffic forwarding between remote networks where native multicast is not supported." <<<PAGE 29>>>
- **P21** sFlow BGP Gateway：流样本携带扩展网关字段（next-hop/AS/communities/local-pref），采集器拿到的是路由归因后的流量 <<<PAGE 30>>>
- **P22** EVPN 多站点部署模型库：Clos-3/Collapsed Core/Clos-5/DCI/Multi-PoD/Multi-site，选择取决于规模、泛洪域、PoD/站点间 L2/L3 无缝切换（greenfield）与 VXLAN→VLAN L3 无缝（brownfield） <<<PAGE 30>>>
- **P23** 手工 RD/RT 配置：多站点/PoD 各自 RT 体系下选择性导入导出 EVPN 路由，配合 E-Tree 拓扑避免 PoD 内 leaf 间无谓的东西向隧道 <<<PAGE 33>>>
- **P24** PEG（PIM EVPN Gateway）：边界 leaf 桥接 EVPN 网络与外部 PIM 域，OISM 优化 fabric 内跨子网组播；DR 选举支持原生 PIM hello 与 DF 选举算法两种 <<<PAGE 31>>>
- **P25** ERP over SPB 单播客户端 MAC flush 问题：SAP 口 flush 正确但不传播到 BEB 的 SDP 口导致残留 MAC——需 `erp-ring spb-remote-flush` 让 flush 事件传播到 SDP："Stale MAC entries flush can be achieved by enabling the SPB remote flush feature for MAC flush." <<<PAGE 31>>>
- **P26** SPB 引入 6570M/6575：6570M 需 premium bundle 许可、6575 默认支持；default 与 Fabric TCAM profile 都支持，推荐 Fabric TCAM 获得更好性能与扩展性 <<<PAGE 31>>>
- **P27** Multi-Site SPB 层级（PoC）：站点内 ISIS Level-1、站点间 Site Border Node（SBN）以唯一 site-id 构建 Level-2，突破平面 SPB 500-1000 节点上限，支持 L2VPN/L3VPN/组播窥探与 ECT 负载分担："The overall limitation for number of nodes supported in a flat SPB network typically is in the range of 500 to 1000 nodes." <<<PAGE 40>>>
- **P28** SPB BVLAN 收敛原则：业务分散在 >4 条 BVLAN 时应收敛到 4 条以内，减少控制面地址更新规模、提升稳定性与收敛 <<<PAGE 65>>>
- **P29** BVLAN 判活网络级语义：`show spb isis bvlans` 的 In Use=Yes 是全网视图，远端节点挂了服务本机也显示活跃——活跃 BVLAN 即使本机无服务也不能删："Even if the service is not local to a node the node can act as a transit node for the active BVLAN. For this reason the BVLAN cannot be deleted from the network." <<<PAGE 66>>>
- **P30** LPS on VXLAN：LPS 从端口/linkagg 扩展到 EVPN VXLAN SAP，限单归属（single-homing）场景 <<<PAGE 32>>>
- **P31** Telemetry 推送管道：交换机本地 Redis 存 DPI/流数据 → IPFIX（RFC 7011）封装 → 导出 Telegraf/InfluxDB/Grafana，近实时可视与 AI/自动化供数 <<<PAGE 39>>>
- **P32** Threat-Insight 集成 AppMon：每流威胁智能三属性——DGA Score（算法生成域名）、MITM Score（TLS 中间人概率）、JA3 Fingerprint（Client Hello 指纹），v4/v6 流表实时分析 <<<PAGE 36>>>
- **P33** RoCEv2 无损以太（6900/6920）：PFC+ETS+DCBX 符合 MSFT 要求；LLDP 扩展 DCBX TLV 与 802.3 最大帧长 TLV；ECN profile + DCQCN 拥塞控制 <<<PAGE 36>>>
- **P34** 快速收敛（Improved Convergence）：SFP/SFP+/QSFP+/QSFP28 光口可更快收敛；铜口、VFL 口、splitter 口、6865-P16X/U12X 口 3/4、6570M-12/12D 口 9/10 除外 <<<PAGE 15>>>
- **P35** LACP 组数扩容：6570M 从 32 提到 96（`linkagg lacp agg size`） <<<PAGE 26>>>
- **P36** Premium（捆绑）许可：单许可文件含多个子许可（SPB/AR/25G/50G/VxLAN-EVPN），按 MAC/序列号生成；VC 内 Match=各成员子许可必须一致才生效、Local-Only=仅本机生效："Match - Sub-Licenses on all units of a VC must match for feature to operational." <<<PAGE 20>>>/<<<PAGE 32>>>
- **P37** ISSU 机理：VC 按 chassis-id 从低到高逐台从 ISSU 目录重启，Slave 全部完成后 Master 重启引发 takeover，原 Master 回来变 Slave；模块化机箱则是备 CMM 先升转主、原主再升："Each element of the VC is upgraded individually allowing hosts and switches which are dual-homed to the VC to maintain connectivity." <<<PAGE 67>>>
- **P38** 标准升级认证回滚机制：working 目录 reload 试验成功后 `copy running certified` 固化；出问题用 `reload from certified no rollback-timeout` 回退 <<<PAGE 73>>>
- **P39** ONIE 机型 CPLD 升级语义：kit 内含多 CPLD updater，命令按平台/CPLD 类型逐个升级需多次执行，升级后手动 reload 进 "ONIE: Update ONIE" 模式（不得按键），完成后只回 Certified 目录不回 running <<<PAGE 82>>>
- **P40** 出厂首启 VC 自动化副作用：vcboot.cfg/vcsetup.cfg 只写 working 不写 certified → 下次重启 Running Configuration 落到 certified、脱离出厂默认模式且 chassis-id=1，可能在 VC 里引发 chassis-id 冲突，需 `reset-to-factory` 纠正 <<<PAGE 15>>>
- **P41** NTP 遵循 RFC 不再同步 stratum 16（未同步）服务器，OmniSwitch 之间级联对时的存量部署会断同步 <<<PAGE 16>>>
- **P42** Celona AP autoclass 降级问题机理：PD 侧硬件信号错误使 Class 6/8 设备被识别为 Class 4 限到 30W，交换机无法纠正，禁用 autoclass 规避："Since this is a hardware behavior on the Celona side and cannot be corrected by the switch, the workaround is to disable autoclass." <<<PAGE 34>>>
- **P43** ERP 与 MACsec 交互语义：MACsec/MKA 单侧关闭时 R-APS 仍可从不受影响端口交换，ERP 环可能回到 Idle/RPL 阻塞——属预期行为（8.10R4 文档化） <<<PAGE 90>>>/<<<PAGE 91>>>
- **P44** DHL 无缝切换规模边界：4000 VLAN/大 MAC 场景下无缝 failover 支持 128 VLAN/1000 MAC，超出需把 pre-empt timer 从默认 30 秒提到 60 秒防残留 MAC："DHL supports up to 128 VLANs and 1000 MACs for seamless failover." <<<PAGE 97>>>
- **P45** OS6920 400G 平台定位：1RU 32×400G QSFP-DD、低时延 L2/L3，本版无 VC 支持 <<<PAGE 21>>>
- **P46** OS6575 工业平台特性：-40°C~75°C 加固无风扇，P12（8×bt+4×SFP+ VFL，360W PoE）、U28（1U 机架，210W）、MP16（M12 连接器墙装，Bypass 功能，无 VC，120W）；支持 VC 最多 4 机箱（P12/U28）<<<PAGE 21>>>
- **P47** 认证升级双通道：HSP（Hitless Security Patch Upgrade）与 Signed AOS Image 平台覆盖见 Feature Matrix，签名镜像要求 U-Boot 支撑（6570M 8.9R4 起）<<<PAGE 53>>>
- **P48** 许可分层模型：Data Center 许可（本版均不支持 DCB/FIP/FCoE）→ Feature/Performance 许可（MACsec/10G/MPLS/50G）→ Metro 许可（8.9R1 起 6560 收费）→ Advanced Routing 许可（6560 版限 2 OSPF 区域、无 VRF/ISIS/隧道；8.10R4 加 BGP）→ Premium 捆绑 <<<PAGE 19>>>/<<<PAGE 20>>>

---
合计：48 条（P1-P48）。
