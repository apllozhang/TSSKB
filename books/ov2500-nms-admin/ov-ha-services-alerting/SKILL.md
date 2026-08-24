---
name: OV2500 系统运维：HA、Watchdog 与告警通知
description: OV2500 日常运维场景——高可用（HA）双实例、服务状态排查（Watchdog/Control Panel）、邮件告警（Trap Responder/SMTP）、告警声音、用户权限与 2FA 双因素认证。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- OV 服务器单点故障会导致全网失去监控、UPAM 认证停摆，需要规划 HA
- OV 某功能异常，需要检查服务（Watchdog）状态或查看调度任务历史
- 需要把设备 Trap 转成邮件告警，或按用户角色收紧权限、启用 2FA

## I（核心理念）
OV2500 的可用性分两层：服务器层靠 HA 双实例（Main/Standby 常驻、状态同步、故障自动接管），应用层靠 Watchdog 管理各个服务。告警链路是"设备 Trap → Trap Responder 匹配 → 邮件/声音"，账号安全则由用户组权限 + 按角色的 2FA（TOTP）构成。

## A1（行动框架）
1. **HA 部署**：购买 HA Service License，Main/Standby 双实例常驻；"All functions are handled by the Main OV. The Main OV keeps the standby OV in sync"；安装设置只填一次，后台磁盘同步；Trap 自动为双实例配置，failover 时自动 Trap Replay 并显示告警横幅（<<<PAGE 17-19>>>）
2. **服务排查**：Administrator → Control Panel → Watchdog Screen：查看所有 OV 服务状态、点服务看描述/状态/依赖、滑块启停，或 Start All/Restart All/Shutdown（<<<PAGE 71/221>>>）；Scheduler → Scheduler History 查看 Asset Management 事件历史（<<<PAGE 221>>>）
3. **邮件告警**：Administration > Preferences > System Settings > Email：填 SMTP 服务器（如 10.130.5.6）、From 地址、Send Test E-mail 验证（<<<PAGE 191>>>）
4. **Trap Responder**：Network → Notifications → Trap Responders → "+"：Agent Type=Device、IP 范围（如 192.168.200.1-8）→ Trap Type 关掉 Normal → Response=Send an e-mail → Create；拔链路触发 trap 后到邮箱验证（<<<PAGE 192-194>>>）
5. **告警声音**：Administration – Preferences – User Settings – Sounds → Alarm Sounds 启用 Notifications → For All Severities → Apply（可按级别分设）（<<<PAGE 195>>>）
6. **用户与权限**：Security → Users & User Groups → Group：建组并选 Group Rights（如 Read）；User：建账号，密码强度指示 Risky–Weak–Fair–OK；登出后用新账号验证只读效果（<<<PAGE 216-218>>>）
7. **2FA**：按 User Role 启用 2FA → 手机装 Google Authenticator → 登录页出现二维码扫码 → 在 TOTP Code 字段输 6 位码 → Verify（<<<PAGE 157-159>>>）

## A2（进阶应用）
- HA 容量认证：up to 4K AP w/1.5K Switches（<<<PAGE 19>>>）
- 无 HA 时故障后果要评估：管理员失去监控与配置能力；"If using UPAM, no new additional clients would be able to authenticate"（<<<PAGE 18>>>）
- 验证告警链路可用非断链事件："Try different events, i.e. logging in to the switch with an incorrect username or password and notice the trap being generated"（<<<PAGE 194>>>）
- 会话管理：Session Management 列出所有客户端登录会话，可强制登出某会话；System Health 提供 VA 的 CPU/内存/网络流量概览与配置问题提示（<<<PAGE 72-73>>>）

## E（实证案例）
- SMTP + Trap Resemailer 断链邮件告警演练——cases·SMTP 与 Trap Responder（<<<PAGE 191-194>>>）
- 只读用户组演练（Training 组 + training_user，登录验证不可改配置）——cases·用户与用户组（<<<PAGE 216-218>>>）
- 2FA 初始设置（Google Authenticator 扫码 + TOTP）——cases·2FA（<<<PAGE 158-159>>>）

## B（边界与陷阱）
- Trap Responder 必须禁用 Normal 级别，否则正常事件涌入邮件（<<<PAGE 192>>>）；前置条件：交换机端口需 `interfaces <slot>[/port] link-trap enable`（<<<PAGE 192>>>）
- Control Panel 误停服务风险："(DO NOT modify or stop any process unless directed by your instructor!)"（<<<PAGE 221>>>）
- 远程实验室环境无音频设备，听不到通知声音；Firefox 复制粘贴有已知问题（workaround: sudoedit.com/firefox-async-clipboard）（<<<PAGE 195/81>>>）

## 来源
- principles·HA 双实例（<<<PAGE 17-19>>>）、无 HA 后果（<<<PAGE 18>>>）、Watchdog（<<<PAGE 71/221>>>）、System Health/Session（<<<PAGE 72-73>>>）、2FA（<<<PAGE 157-159>>>）
- cases·SMTP/Trap Responder/声音/用户组/Control Panel/2FA（<<<PAGE 191-195/216-221/158-159>>>）
- counter-examples·Normal trap 未禁用/误停服务/远程实验室限制（<<<PAGE 192/221/195/81>>>）
