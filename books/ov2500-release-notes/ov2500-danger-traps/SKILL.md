---
name: ov2500-danger-traps
description: 何时用：升级/变更前做高危风险评审——不可降级、强制改密、HA 同步期 failover 等会造成停机、锁死或安全漏洞的陷阱核对。
source_book: OV2500 4.9R2 Release Notes
---

# OV 2500 危险陷阱 TOP 清单

## R · 原文引用

> "If the U-Boot and AOS version is 8.9R4 or above and you downgrade the AOS version to 8.9R3 and reboot the switch, the switch cannot reboot. The 8.9R4 U-Boot only accepts signed images. OS6570M has a signed image; there is no unsigned image. PR# OVE-13356" (p37-38)

> "If you disable the Enforce Strong Password setting in OmniVista 4.9R1, then upgrade to release 4.9R2 ... The Enforce Strong Password setting is automatically enabled. OmniVista logs you out and requires you to change your password. PR# OVE-13859" (p38-39)

> "Since the failover interrupts the data sync, the Standby Node will not come up as the Active Node because it does not have the latest data ... On the HA Virtual Appliance Menu select 3 – Configure Cluster, then select 14 – Cluster Error Check. PR# OVE-1629" (p35)

> "When a user configured a Layer 3 Destination IP address Unified Policy to 'Drop' traffic with the Reflexive option, some packets were not dropped. Workaround: Do not turn on the Reflexive option. PR# OVE-10083" (p28)

## I · 方法论骨架

按"损失类型"把陷阱分四类，升级/变更评审时逐类过一遍：

1. **不可逆门闩**（升上去就回不来）：签名校验、单向升级链。
2. **大面积锁死**（用户层面集体受影响）：强制改密、认证依赖连锁故障。
3. **集群脑裂/数据丢失**：同步期 failover、备份不完整。
4. **安全静默失效**（策略看似生效实际漏防）：漏丢包、授权残留、过滤绕过。

判读原则：这类条目的共同特征是"事后恢复代价远高于事前一条检查"，所以全部前置到变更评审，排障时遇到优先怀疑。

## A1 · 书中案例（TOP 陷阱表）

| # | 陷阱 | 触发动作 | 后果 | 前置措施 | id |
|---|---|---|---|---|---|
| 1 | OS6570M 签名门闩 | U-Boot/AOS 升到 8.9R4+ 后降回 8.9R3 并重启 | 交换机无法重启（变砖），无签名镜像可救 | 升级评审必查"能否回退"；OS6570M 一旦过 8.9R4 即单向 | ce63 |
| 2 | 升级后强口令自动启用 | 4.9R1 关闭强口令 → 升 4.9R2 | 全员强制登出改密 | 升级公告必发项，预告所有用户 | ce67 |
| 3 | HA 同步期 failover | 节点数据同步中发生切换 | 备节点缺最新数据无法升主 | 变更窗口避开同步期；已发生则 SSH 备节点 → VA 菜单 3 Configure Cluster → 14 Cluster Error Check | ce51 |
| 4 | Reflexive 漏丢包 | Drop 策略叠加 Reflexive 选项 | 部分报文未拦截，安全放行漏洞 | 安全阻断类策略禁用 Reflexive | ce21 |
| 5 | 认证授权残留 | 客户端认证成功后再失败 | 交换机保留成功时的 Access Role Profile，账号失效权限不撤 | AP 侧升 AWOS 5.0.1+；交换机侧无解，审计时注意 | ce23 |
| 6 | LDAPS 停服带崩 RADIUS | LDAPS 服务器关停 | freeradius 崩且无法重启 | LDAP 维护窗口前预警；或先在 UPAM 禁用 LDAP/AD | ce30 |
| 7 | 带口令私钥证书锁死 Web | 导入私钥加密的 SSL 证书 | Nginx 起不来，重启 VM 无效 | 证书 SOP 硬规则：私钥不得加密 | ce52 |
| 8 | U-Boot 文件名/双文件陷阱 | 文件名缺点号；OS9907/9912 混装 NI 模块 | U-Boot 升级失败或不工作 | 改名 u-boot.5.2.R03.3.tar.gz；Denverton（CMM2/CNI-U20）与 Rangeley（CMM1/其余）分两次各用对应文件 | ce14, ce15 |
| 9 | 拔线 failover 后原主自动重启 | HA 演练拔主节点网线再回接 | 原主节点重连时自动重启（双节点随后正常） | 演练预期管理，勿当二次故障 | ce65 |
| 10 | HA 升级同步警告 | HA 4.9R1→4.9R2 升级中 | 提示"数据未完全同步" | 升完 Standby 等足够时间让服务全起再升 Active | ce66 |
| 11 | VMware Flexible NIC 升级失败 | Flexible NIC 的 VA 升 4.8R1 | 升级失败 | 换网卡类型重配 IP | ce60 |
| 12 | 备份丢 SSH Key/用户表 | OS6900 AOS 8.3.1 全量备份 | 恢复后管理凭据缺失 | 恢复演练必含手工补这两项 | ce13 |

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：升级变更评审会、回退方案编制、HA 演练预案、安全策略上线前核查、证书/备份 SOP 制定。
- 区分：已经出现故障要定位 → `ov2500-known-issues`；查版本/固件兼容 → `ov2500-49r2-features-compat`；排升级步骤 → `ov2500-upgrade-deploy`。本 skill 只管"事前一颗雷"清单——后果严重且必须前置规避的条目。

## E · 可执行步骤

1. 升级评审时打印 TOP 陷阱表，逐条问"本次变更是否触及该触发动作"。
2. 涉及交换机固件升级的，先列机型×当前版本×目标版本，凡 OS6570M 过 8.9R4 标记"不可回退"并在变更单注明。
3. OV 升级公告模板固定包含：升级后强口令自动启用、全员将被迫改密（ce67）。
4. HA 变更窗口检查项：不在数据同步期做 failover（ce51）；升完 Standby 等服务全起再升 Active（ce66）；演练后复查 WCF 状态（ce40）。
5. 证书替换前核验私钥未加密；LDAPS 维护前预警 freeradius 连锁故障。
6. 安全阻断策略上线前核对 Reflexive 选项未开启；权限审计把"认证失败后授权残留"列入检查项。

## B · 边界与陷阱

- ce63 的单向门闩只影响 OS6570M（唯一只有签名镜像的机型）；其余机型 8.9R4+ U-Boot 虽只认签名镜像，但仍存在非签名镜像可用。
- ce67 是版本行为（4.9R1→4.9R2 触发），不是可配置关闭的选项；密码有效期策略本身（p05）对新老用户生效时点不同，别混为一谈。
- ce23 交换机侧无 workaround，只能靠 AP 升级 + 审计补偿，不要承诺"账号禁用立即生效"。
- HA 七条安装限制（ce69）属架构设计约束，完整清单见 `ov2500-upgrade-deploy`。

---
来源条目: ce63, ce67, ce51, ce65, ce66, ce21, ce23, ce30, ce52, ce13, ce14, ce15, ce40, ce60, p05；关联 ce69 详见 upgrade-deploy
