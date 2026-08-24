---
name: ovna-deployment-teams-bot
description: 何时用：部署/升级 OmniVista Network Advisor、纳管交换机、对接 Teams Bot 与 Rainbow 告警、演练异常处置闭环。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# Network Advisor（OVNA）部署与 Teams Bot 对接

## R · 原文引用

> "Step by Steps: Step 1 - System Requirements ... Step 2 - Package Installation ... Step 3 - OVNA Configuration. $ sudo dpkg -i ale-ovna.deb ... $ sudo ale-ovna install" (p346)

> "Each time a new device of type Switch is added, the application will push the following commands to the switch: -> swlog output socket <ip_address> 10514 vrf-name <vrf> -> interfaces ddm enable ... -> interfaces ddm-trap enable" (p333)

> "Phase 1 of 4: Creating the Entra App and Teams Bot ... Phase 4 of 4: Enable Graph API authorizations" (p406)

> "The logger command provides an easy way to add log entries from the command line to the switch to make tests. logger -t swlogd ipni dos WARN: VRF 0: DoS type ping overload from ..." (p380)

## I · 方法论骨架

1. **部署三步**（f15/p39）：系统要求（四核/8GB/50GB，200 台内；1000 台 120GB、2000 台 210GB；Ubuntu 22.04 / Debian 11/12 / RHEL 9.3；端口 TCP 80/443、UDP+TCP 10514、TCP 6514 TLS、TCP 22；**必须可上外网**）→ 包安装（Debian 系 dpkg -i ale-ovna.deb，RHEL 系 rpm -ivh 且先 systemctl disable firewalld --now；再 ale-ovna install）→ Web 向导（https://<IP> → New to OVNA：公司信息 → 2FA → 时区 → 通知渠道 → OmniVista 同步 → 许可 30 天试用）。
2. **纳管与处置闭环**（f16）：Add device 后自动推送三条命令（syslog 指向 10514、ddm enable、ddm-trap enable，show swlog 应出现 Log Device 2）。处置链：设备 syslog → 模式匹配 → 通知（Rainbow 气泡/Teams 频道，含设备/MAC/端口与修复建议）→ 用户选处置动作 → OVNA 经 SSH 执行 → 结果回传 → Anomaly History 留档。多 IP 设备先 `ip service source-ip loopback0 swlog` 固定源。
3. **Teams Bot 四阶段**（f17，须在装 OVNA **前**完成）：① 建 Entra 应用与 Bot（dev.teams.microsoft.com → Bot Management → New bot → 公网可达 endpoint https://.../msteams 默认端口 10510 → Client secret **只显示一次** → 记 Bot ID）；② 建 Teams 应用并挂 Bot（Personal+Team scope）→ Publish → Download app package；③ 取 Application (client) ID 与 Directory (tenant) ID；④ 加 Graph API 权限（Team.ReadBasic.All、Channel.Create、Group.ReadWrite.All 等）并 Grant admin consent。
4. **许可与门槛**（p39）：纳管需 AOS 8.7.R2+（OS6xxx/9xxx）；OS2xxx 需 5.2.R1+。许可按设备 IP 计（NETAD-SWITCH/AP-1Y/3Y/5Y），试用 5 交换机+5 AP，激活即倒计时。
5. **异常对象模型**（g34-g36/g37）：预置异常类别（环路/端口 flap/DDoS/风暴/VC takeover/OSPF-BGP 状态变化/电源 POE/IP 重复/高 CPU/SFP 阈值等）；可自建自定义异常；Anomaly History 供行为模式分析。三类处置动词：Disable Port（执行变更）/ Collect Logs（取证）/ Acknowledge（仅确认）。
6. **无损演练**（p40）：su 维护 shell 用 Linux logger 注入符合异常模式的日志（DoS ping overload / PMD generated），即可走完检测→通知→处置→留档全链路，不必制造真实故障。前置：与 OVNA/外网连通 + NTP 对时。

## A1 · 书中案例（LAB 故障根因）

- **c10（LAB5 用例1，p380-382）**：logger 注入 DoS ping overload → syslog 到 OVNA 命中 DDoS 模式 → Rainbow 通知带处置选项 → 选 Disable Port → OVNA SSH 下发 `interfaces port 1/1/1 admin-state disable`（交换机 CLI log 可见 result: SUCCESS）→ Anomaly History 留档。完整闭环样板。
- **c11（LAB5 用例2，p383）**：注入 "PMD generated at /flash/pmd/..." → 处置方向是收集日志与 PMD 文件并联系 ALE 支持——崩溃类异常不提供网络侧自愈动作，转向取证与升级 TAC（PMD 见 g33）。
- **c12（LAB5 用例3，p384）**：禁用 linkagg 成员口 → 日志因果链：portMgrNi LINKSTS DOWN → linkAggNi "Convergence port down" + LACP Sync Out（partner:Out actor:In）→ linkAggCmm 端口离开 agg 17 → OVNA LinkAgg Down 异常。人工排障 linkagg 时对读此因果链。
- **c13（LAB5 用例4，p385）**：错误用户名登录 → CUSTLOG "Authentication failure detected: user admin" → 无破坏性动作，Acknowledge 即可——三类处置动词最轻一级示例。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：部署/升级 OVNA、纳管设备后收不到告警、配 Teams/Rainbow 通知、演练告警闭环、告警处置选型。
- 区分：**告警只反映现象，根因还在各协议 skill**——DoS 告警判环在 stp-loop、OSPF 告警判读在 l3；本 skill 解决"工具链部署与处置动作"层面。syslog 调级/检索手法在 app-logging-qos skill。

## E · 可执行步骤

1. 部署前：若要 Teams 通知，先完成四阶段（f17）拿到 Bot ID/Client ID/Tenant ID 与 app package。
2. 装机：确认外网可达 → dpkg/rpm 安装 →（RHEL）disable firewalld → `ale-ovna install`（交互选 IP/代理/TLS）。
3. Web 向导：管理员信息 → 2FA → 时区 → 通知渠道（Rainbow Bubble 或 Teams + SMTP）→ 许可激活。
4. 纳管：Device Management → Add device（IP/SSH 凭据）；多 IP 设备先在交换机 `ip service source-ip loopback0 swlog`；show swlog 验证 Log Device 2 出现、show log swlog 验证 syslog 外发。
5. 演练：su 进维护 shell → logger -t swlogd 注入目标异常日志 → show log swlog |grep 验证 → 在气泡/频道收通知并选处置 → 交换机 show interfaces status 验证动作生效 → Anomaly History 核对留档。
6. 升级：ale-ovna update（跨版本先装新包；小版本加 -c）。迁移：备份 → 新机安装 → 导入 → 补配置 → 导许可。

## B · 边界与陷阱

- Teams 四阶段必须在装 OVNA 前做完，产出的 ID 在 OVNA 安装向导中要用（f17）。
- Client secret 只显示一次，错过只能重建（与 VC write memory 警告同属"不可逆操作"类，ce18 类比）。
- 无外网访问装不了（k3s 与镜像下载依赖互联网），隔离网环境需评估代理方案。
- 崩溃类（PMD）异常没有一键修复动作，正确处置是收集证据升级 TAC（c11）。
- 注入测试日志前提是 NTP 对时，否则通知与日志时间对不上（p40）。
- 端口镜像/监控与六类不镜像流量的边界见 app-logging-qos skill（ce14）；DDoS 告警先判环再谈攻击（ce19，stp skill）。

---
来源条目: f15, f16, f17, p39, p40, c10, c11, c12, c13, g33, g34, g35, g36, g37
