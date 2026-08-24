# verified · OV 2500 NMS 4.9R2 Release Notes（阶段 1.5 三重验证结果）

## 汇总

| 类别 | 输入 | 通过 | 淘汰 | 验证方式 |
|---|---|---|---|---|
| principles | 20 | 20 | 0 | V1 全量核对 quote（含页码归位）；V2/V3 逐条判定 |
| counter-examples | 73 | 73 | 0 | V1 实际全量核对（73/73，超出抽查 30 条要求）；V2/V3 逐条判定 |
| glossary | 15 | 15 | 0 | 免验保留 |
| **合计** | **108** | **108** | **0** | |

- V1 原文真实性：所有 quote 关键句在 fulltext.md 对应页命中。两处 grep 直查未命中（p12 的 "Standby node then updating the Active"、p13 的 "Total Number of Managed Devices"）经人工核对为 PDF 换行拆词，原文逐字存在（fulltext.md L1142、L1334-1339），非编造。
- V2 可操作价值：counter-examples 全部为已知问题/workaround/功能边界/版本要求，principles 全部为兼容矩阵/升级路径/容量规划/端口白名单，均满足。
- V3 独特性：本册已知问题清单与 4.9R2 认证固件矩阵为版本特有信息，含 ce63（OS6570M 不可降级）、ce67（升级后强口令自动启用）、ce66（HA 4.9R1→4.9R2 同步警告）等本版本新增条目，全部独特。
- 页码归位抽查：ce63（L2316→p37-38）、ce67（L2377→p39）、ce68（L2379→p39）、ce69（L1490→p19-20）、ce70-73（L942→p12）均与 source_chapter 一致。

## principles（20/20 通过）

| id | 标题 | 通过理由 |
|---|---|---|
| p01 | 部署形态与虚拟化平台支持 | V1 命中 p5；V2 升级评估第一步核对 hypervisor 列表；V3 4.9R2 认证平台清单版本特有 |
| p02 | 新增软硬件版本支持与认证固件矩阵 | V1 命中 p6/p13-14；V2 固件基线规划直接引用；V3 认证矩阵为 4.9R2 特有 |
| p03 | OS6870 支持边界（CPLD/应用监控） | V1 命中 p6；V2 明确三项能力边界；V3 OS6870 为本版新增机型 |
| p04 | PALM 下线，Fleet Supervision 接替 | V1 命中 p6；V2 依赖 PALM 的流程须迁移；V3 本版本变更项 |
| p05 | 密码有效期策略与 CLI 管理员找回 | V1 命中 p7；V2 两次改密生效差异 + VA 菜单找回路径；V3 新特性 |
| p06 | SNMPv3 供给加密算法全量扩展 | V1 命中 p7（SHA384+AES 命中）；V2 非标加密组合设备可直接纳管；V3 新特性 |
| p07 | Wi-Fi Enhanced Open 过渡模式 | V1 命中 p7；V2 AWOS 4.0.8+ 硬门槛与回退风险；V3 新特性 |
| p08 | 6GHz SSID Backward Compatibility | V1 命中 p7-8（WPA3_PSK_SAE_AES 命中）；V2 与 MLO 互斥规则可操作 |
| p09 | Blast-RADIUS 防护开关 | V1 命中 p8-9（CVE-2024-3596 命中）；V2 三场景行为+交换机 CLI 命令；V3 本版安全修复 |
| p10 | Oracle Linux 8.10 与 10 项 CVE | V1 命中 p9；V2 安全合规升级引用清单；V3 本版 CVE 列表 |
| p11 | 升级路径总则（4.9R1 直升/Patch 1） | V1 命中 p9/p15-16；V2 升级路径硬规则；V3 4.9R2 特有工作流 |
| p12 | HA 升级顺序与集群转换规则 | V1 命中 p15/p19-20（L1142，换行拆词已核对）；V2 先备后主铁律 |
| p13 | 网络规模分档与资源配置表 | V1 命中 p17-19（L1334-1389，换行拆词已核对）；V2 容量规划直接引用 |
| p14 | VA 首次部署六条硬规则 | V1 命中 p18-19；V2 部署 checklist |
| p15 | Stellar AP 升级顺序与 Mesh 逐跳 | V1 命中 p14/p19；V2 升级顺序 + Resource Manager 禁用场景 |
| p16 | 防火墙白名单与关键端口表 | V1 命中 p16-17；V2 五域名+端口表网络准备必需 |
| p17 | 许可证体系与容量上限 | V1 命中 p20-21；V2 三档许可与上限决策依据 |
| p18 | 浏览器支持/入口地址/Watchdog | V1 命中 p22；V2 启动排障第一步 |
| p19 | 默认凭据与首次强制改密 | V1 命中 p23；V2 安全基线核对 |
| p20 | 功能矩阵关键限制（VMM/动态 VLAN 等） | V1 命中 p10-13；V2 多条硬限制汇总；V3 本版矩阵特有 |

## counter-examples（73/73 通过）

按 V1 核对方式：每条以 PR 号或特征句在 fulltext.md 定位并核对页码，实际完成 73/73（超出 30 条抽查要求）。V2 判定口径：已知问题（No workaround 亦有排障/预期管理价值）、workaround、功能边界、版本要求、升级遗留全算可操作价值。V3 判定口径：本册 Known Problems 清单为 4.9R2 版本特有，含多条老版本遗留（ce12/ce34/ce47/ce56）——它们仍在官方升级路径可达范围内（4.7R1→…→4.9R2），保留。

| id | 标题（简） | 通过理由 |
|---|---|---|
| ce01 | IE11 打不开 AP Web 管理 | 已知问题+workaround，PR OVE-2096 命中 p24 |
| ce02 | 同名 Key File 无法再上传 | workaround（换文件名），PR OVE-12732 命中 |
| ce03 | Reason Down 字段不恢复空白 | 监控误报判读口径，PR OVE-2131 命中 |
| ce04 | 大批 AP Save to Running 极慢 | 变更窗口估算依据，PR OVE-2264 命中 |
| ce05 | NaaS 降级模式无理由失败 | 排障思路，PR OVE-11354 命中 |
| ce06 | Locator 不支持 OS2200 | 功能边界，PR OVE-1226 命中 |
| ce07 | Chromecast 跨 VLAN 不可见 | workaround+AOS 8.7R2 修复版本，PR OVE-8941 命中 |
| ce08 | mDNS 配置顺序敏感 | workaround（先配后放用户），PR OVE-9848 命中 |
| ce09 | 禁用 mDNS 后 AirPlay 仍续传 | 安全审计须知，PR OVE-9112 命中 |
| ce10 | AP1351/1301 仅 Eth1 不能跑 mDNS | workaround（Eth0/聚合），PR OVE-11033 命中 |
| ce11 | OS6900-Q32 专家模式无 Port Type | 策略设计规避，PR 201688 命中 |
| ce12 | Send Trap 属性策略推不下去 | 升级遗留+workaround，PR OVE-653 命中 |
| ce13 | OS6900 8.3.1 备份丢 SSH Key/用户表 | 备份完整性风险，PR 219688 命中 |
| ce14 | U-Boot 文件名缺点号升级失败 | workaround（改名），PR OVE-13346 命中 |
| ce15 | OS9907/9912 U-Boot 按 CPU 分两次 | Denverton/Rangeley 双文件规则，PR 命中 |
| ce16 | ERP-RPL 用 LLDP 替代 AMAP | workaround（换邻接协议），PR 177202 命中 |
| ce17 | SPT 链路只支持两台选择 | 使用习惯约束，PR OVE-1491 命中 |
| ce18 | AOS 8.8R1 LLDP 链路不显示 | 版本组合定位，8.8R2 修复，PR 命中 |
| ce19 | Q32/X72 Device Config 显示错误 | 以 CLI 为准的核对口径，PR 219133 命中 |
| ce20 | AOS 8.2.1 看不到 ARP 档案 | 功能边界，PR 220259 命中 |
| ce21 | Reflexive 选项致 Drop 漏丢包 | 安全漏洞规避，PR OVE-10083 命中 |
| ce22 | OS6465/6560 策略不含源 MAC | AOS 限制规避，PR OVE-10696 命中 |
| ce23 | 认证失败后 ARP 授权残留 | 安全影响+AWOS 5.0.1 修复，PR OVE-13317 命中 |
| ce24 | 拆 VC 后 vcpolicy.cfg 残留 | workaround（删文件重启），PR OVC-9896 命中 |
| ce25 | HSTS 二次访问不重定向 | 浏览器差异验收注意，PR OVE-779 命中 |
| ce26 | LDAP 加密密码致 UPAM 失败 | workaround（明文密码），PR OVE-818 命中 |
| ce27 | 门户页不支持完整 HTML 定制 | 方案阶段能力边界，PR OVE-834 命中 |
| ce28 | 有线 CP 依赖 DNS 解析 UPAM 地址 | workaround（DNS 配置），PR OVE-1693 命中 |
| ce29 | Windows LDAP 不支持 | workaround（OpenLDAP/AD），PR OVE-3000 命中 |
| ce30 | LDAPS 停服带崩 freeradius | 维护窗口风险+workaround，PR OVE-8986 命中 |
| ce31 | Guest 账户过期仍显示 Enabled | workaround（删除策略），PR OVE-10128 命中 |
| ce32 | WiFi4EU 有效期 24 小时合规 | workaround（改有效期），PR OVE-11164 命中 |
| ce33 | TLS RADIUS 无端口字段 | workaround（填 Authentication Port 2083），PR OVE-12747 命中 |
| ce34 | Analytics 权限连带的继承行为 | 升级行为须知，PR OVE-1847 命中 |
| ce35 | VM 模板被当虚拟设备计数 | 许可统计须知，PR 163314 命中 |
| ce36 | 多网卡 VM 显示多行按 UUID 计一台 | 许可误读澄清，PR 163885 命中 |
| ce37 | 删 LAG 默认 UNP 后 MAC 表延迟 | "短暂失联自愈"判读，PR 174181 命中 |
| ce38 | 手机 App 流量绕过 WCF | 方案边界（App 豁免），PR OVE-10205 命中 |
| ce39 | 代理上网使 WCF 失效 | 部署前提（DNS 直连），PR OVE-11466 命中 |
| ce40 | HA 升级+failover 后 WCF 失效 | workaround（重启 WMA），PR OVE-13159 命中 |
| ce41 | GRE 隧道 Entropy/Tunnel ID 组合规则 | 四合法/两非法组合表，p33 命中 |
| ce42 | 2 万 rogue AP 查询超时 | 大规模数据源可靠性判定，PR OVE-9693 命中 |
| ce43 | AP1201BG 不支持 RF Profile | BLE 网关排除，PR OVE-10781 命中 |
| ce44 | 备节点 WMA 显示 Not Responding | 巡检误报澄清，PR OVE-10513 命中 |
| ce45 | 时区不一致致摘要缺信息 | workaround（统一时区），PR OVC-9976 命中 |
| ce46 | OS6450 U-Boot 显示 NA | 盘点基线须知，PR 181085 命中 |
| ce47 | Win2012R2 IE 按 IP 本地访问失败 | workaround（hosts+localhost），PR 194913 命中 |
| ce48 | SNMP community 不能含撇号 | 自动化凭据过滤，PR 195715 命中 |
| ce49 | 主机名上限 15 字符 | 命名规范约束，PR CRNOV-793 命中 |
| ce50 | Hyper-V 添加报错（DCOM/端口） | 两步 workaround，PR OVE-1568 命中 |
| ce51 | 同步期间 failover 备节点起不来 | HA 应急手册步骤，PR OVE-1629 命中 p35 |
| ce52 | 带口令私钥证书致 Nginx 不启动 | 证书 SOP 硬规则，PR OVE-1776 命中 |
| ce53 | 改系统端口后代理断网 | workaround（改回代理端口），PR OVE-2127 命中 |
| ce54 | Fail to get current user | 快速恢复手段（重启 ovclient/tomcat），PR OVE-2220 命中 |
| ce55 | IPv6 策略需 AOS 6.7.2R7+/8.6R2+ | 版本要求+升级 workaround，PR OVE-5793 命中 |
| ce56 | 4.4R2→4.5R1 Download Only 失败 | 升级路径历史坑，PR OVE-8050 命中 |
| ce57 | Firefox 大列表卡顿 | about:config 调参，PR OVE-8019 命中 |
| ce58 | DRBD stdin/stdout 警告可忽略 | 告警降噪，PR OVE-10576 命中 |
| ce59 | cockpit.socket 提示属正常 | 告警降噪，PR OVE-12730 命中 |
| ce60 | VMware Flexible NIC 升级失败 | workaround（换网卡类型），PR OVE-12783 命中 |
| ce61 | KVM 检测不到前两块新增盘 | 占位盘扩容操作法，PR OVE-13167 命中 |
| ce62 | L3 HA 接管后 Top N 断档 | 报表数据断档预期，PR OVE-13474 命中 |
| ce63 | OS6570M 8.9R4+ 只认签名镜像不可降级 | 单向门闩、升级评审必查，PR OVE-13356 命中 p37-38 |
| ce64 | AP1511/1521 不支持 DPI | 选型排除，p38 命中 |
| ce65 | 拔线 failover 后原主自动重启 | 演练预期管理，PR OVE-13650 命中 |
| ce66 | HA 4.9R1→4.9R2 同步警告 | workaround（等同步），PR OVE-13842 命中 |
| ce67 | 升级后强口令自动启用强制改密 | 升级公告必发项，PR OVE-13859 命中 p38-39 |
| ce68 | 8.10R3 下发 DPI 档案报错 | 存量/新增差异处置，CRAOS8X-53944 命中 p39 |
| ce69 | HA 安装七条硬限制 | 架构设计核对清单，p19-20 命中（L1490 等） |
| ce70 | VMM 仅 Hyper-V 2012/2012R2/2016 | 功能边界，p12 命中 |
| ce71 | OS2260/2360 不支持动态 VLAN | VLAN 自动化规避，p12 命中 |
| ce72 | IoT Enforcement 限部件号 904044-90 | 采购核对项，p12 命中（L942） |
| ce73 | WCF/DPI 的 AP 型号排除清单+签名包版本 | 无线功能规划排除表，p12 命中 |

## glossary（15/15 免验保留）

g01-g15 全部按规则免验保留：g01 OV 2500、g02 VA 与 VA 菜单、g03 AOS、g04 AWOS、g05 Stellar AP、g06 UPAM、g07 HA、g08 NaaS 与降级模式、g09 PALM/Fleet Supervision、g10 Blast-RADIUS、g11 Enhanced Open、g12 WCF、g13 mDNS 三角色、g14 U-Boot/CPLD、g15 UNP。

## 结论

108/108 全部通过，无淘汰。候选集质量高：quote 逐字忠实（仅 PDF 换行差异），已知问题清单与兼容矩阵均为 4.9R2 版本特有且可操作性强。可直接进入下一阶段。
