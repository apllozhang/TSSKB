# counter-examples — 限制/陷阱/已知问题（OmniSwitch AOS 8.10R4 Release Notes）

格式：编号 X# ｜ 陷阱要点 ｜ 英文原句（可选）｜ 页码。分四类：升级陷阱 / 平台与端口限制 / Open CR（未修已知问题）/ 行为变更与废弃。

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
- **X12** ONIE 机型 CPLD 升级前置：AOS 必须 ≥8.9R4 才能用 updater kit 升 CPLD <<<PAGE 81>>>
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
- **X26** 6560 Advanced Routing 许可短板：OSPF 限 2 区域、无多 VRF/ISIS/GRE/IP-IP 隧道/VRF 泄漏，BGP 8.10R4 才加且 6560 仅"Supported"（6570M 为完整许可） <<<PAGE 20>>>
- **X27** QSFP-4X25G-C 光模块插 OS99-CNI-U8 会报错（8.7R1 起显式拦截） <<<PAGE 17>>>
- **X28** 6920 本版无 VC 支持；不支持 IP-IP/GRE/配置 IPv6/6to4 隧道 <<<PAGE 21>>>/<<<PAGE 43>>>
- **X29** 6575-MP16 无 VC 支持（P12/U28 支持最多 4 机箱 VC） <<<PAGE 21>>>
- **X30** 9900 XNI 板用于 CMM2/OS9912 机箱前必须先升 U-Boot 与 FPGA；OS99-XNI-U12Q 与 OS9912 机箱不兼容："Existing OS9900 NIs that are to be used with a CMM2 or in an OS9912 chassis must first have the Uboot and FPGA upgraded." <<<PAGE 14>>>
- **X31** SPB BVLAN 修改不支持在线改：服务必须删除重建到新 BVLAN，收敛操作要安排维护窗 <<<PAGE 65>>>
- **X32** 6360 无 RTC：断电后时钟停在关机时刻，必须 NTP 对时 <<<PAGE 17>>>
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
- **X45** OS6575-MP16 电源状态更新延迟约 1 分钟 <<<PAGE 43>>>
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
