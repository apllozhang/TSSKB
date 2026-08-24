# DIGEST · OV 2500 NMS 4.9R2 精华长文（不读全书版）

> 原始文档：ALE《OmniVista 2500 NMS 4.9R2 Release Notes》，2025-10，93 页。本文是升级评估、变更评审、故障排查三件事的"先看这里"入口，页码均指向原书。

## 一、一页看懂 4.9R2

4.9R2 是 OmniVista 2500 网管平台的维护增强版，只以虚拟设备（VA）形态交付，支持的宿主机：VMware ESXi 6.5/6.7/7.0.2/8.0、Hyper-V 2012R2-2022、Win10 Pro Hyper-V、KVM Ubuntu 22.04（p5）。

这版值得升的理由集中在安全与无线两块：

- **安全加固**：Blast-RADIUS 防护（新增 Require Message Authenticator 校验，解决 CVE-2024-3596，p8-9）；SNMPv3 全量加密组合；密码有效期策略 + CLI 管理员密码找回（p7）；底层换 Oracle Linux 8.10 并修 10 项 CVE（p9）。
- **无线能力**：Enhanced Open 过渡模式（需 AP AWOS 4.0.8+，p7）、6GHz Backward Compatibility（注意与 MLO 互斥，p7-8）、Stellar AP 全面支持 AWOS 5.0.2（p6）。
- **新机型**：新增 OS6870 纳管等一批交换机型号认证（p6）。

**谁应该升**：有安全合规压力（CVE 清单要过）、Stellar 无线网规模大、或现网在 4.9R1 想吃维护红利的用户。**谁缓一缓**：强依赖 PALM 的流程（已下线，须迁移到 Fleet Supervision，p04）、Hyper-V 2019+ 上依赖 VMM 应用的场景（VMM 只支持到 Hyper-V 2016，p10-13）。

## 二、升级路径速查

- **只有 4.9R1 能直升 4.9R2**（p11），且 4.9R1→4.9R2 用全新工作流：系统会自动先打 4.9R1 Patch 1 再升 4.9R2，变更单里把 Patch 1 列为独立步骤（p9, p15-16）。
- 从 4.7R1 出发的完整链是五步：4.7R1 Patch 2 → 4.8R1 → 4.8R2 → 4.9R1 → 4.9R2（p11）。
- **HA 环境**：先升 Standby，等所有服务起来，再升 Active（p12, p15）；升完组合 failover 后 WCF 可能失效，重启 WMA 服务即可（ce40）。L2 HA 不能转 L3 HA，L3 集群只能全新安装（p19-20）。
- **停机窗口**：升完全员被强制登出改密（见下文陷阱 2），窗口公告要发；默认凭据 admin/switch 升级后也会强制改密（p19）。
- **设备侧顺序**：先升 OV 到 4.9R2，再把 Stellar AP 升到 AWOS 5.0.2；Mesh 网络 AP 要从最末节点逐跳升级，且只能用 AP Web GUI，不能用 Resource Manager（p14, p19）。
- **网络准备**：放行五个外联域名（ovrepo/ep1、fluentnetworking、fingerbank、brightcloud）和关键端口（SNMP 161/162、MQTT 1883、RADIUS 1812/1813、CoA 3799、VMM 135+49152-65535、HA 间 TCP 8000/7801/2224 + UDP 5405、cliadmin SSH 2222）；纯内网必须配代理（p16）。
- **容量**：四档 500/2000/5000/10000 设备，单机 RAM 20/36/64/64GB；HA 上限 4000 台且须 Medium 档以上（p17-19）。

## 三、三大危险陷阱详解（升级前必读）

**1. OS6570M U-Boot 签名门闩——变砖级、不可逆（p37-38, PR# OVE-13356）**
U-Boot 和 AOS 升到 8.9R4 及以上后，再降回 8.9R3 并重启，交换机将无法重启。原因：8.9R4 的 U-Boot 只接受签名镜像，而 OS6570M 是唯一"只有签名镜像、没有非签名镜像"的机型——过了这道门就回不去。其他机型 8.9R4+ U-Boot 虽也只认签名镜像，但仍有非签名镜像可救。前置措施：凡涉及 OS6570M 固件升级的变更单，必须标注"过 8.9R4 即单向、不可回退"。

**2. 强口令自动启用——全员锁出（p38-39, PR# OVE-13859）**
在 4.9R1 里关闭了 Enforce Strong Password 的环境，升级到 4.9R2 后该设置会被自动重新启用，OmniVista 把所有用户登出并强制改密。这是版本行为，没有开关可以关闭。前置措施：升级公告必发项，预告所有用户"升级后首次登录须改密"，避免升级当晚工单爆炸。注意别和密码有效期策略（p05，新用户立即生效、老用户下次改密生效）混为一谈。

**3. HA 同步期 failover——备节点缺数据升不了主（p35, PR# OVE-1629）**
数据同步进行中发生主备切换，会打断同步，Standby 节点因缺最新数据无法成为 Active。前置措施：变更窗口避开同步期。已经发生的恢复路径：SSH 到备节点，进 HA Virtual Appliance 菜单，选 3 – Configure Cluster，再选 14 – Cluster Error Check。

## 四、已知问题检索指南

全书已知问题 63 条排障条目，按 13 个模块分组，排障时"先定模块、再对症状"：

① AP 注册（p24）② Discovery（p24）③ Locator（p25，OS2200 不支持定位属功能边界）④ mDNS（p25-26）⑤ PolicyView（p26）⑥ Resource Manager（p26-27）⑦ Topology（p27）⑧ Unified Access（p28-29）⑨ UPAM（p29-31，条目最多）⑩ VMM（p31-32）⑪ WCF（p32-33）⑫ WLAN（p33-34）⑬ 其他/系统（p34-39）。完整症状-处置表见 `ov2500-known-issues` skill。

**高频 TOP10**（一线最常撞）：
1. 大批 AP "Save to Running" 极慢，约 10 秒/台，无 workaround——按此估算窗口、分批操作（p24, ce04）。
2. Web 报 "Fail to get current user"——重启 ovclient 或 tomcat（p36, ce54）。
3. 外部 LDAP 用户密码加密（MD5/SHA）致 UPAM 认证失败——改明文密码（p29, ce26）。
4. LDAPS 服务器停服带崩 freeradius 且无法重启——恢复 LDAP 或先在 UPAM 禁用 LDAP/AD（ce30）。
5. Drop 策略开 Reflexive 选项漏丢包——安全阻断类策略禁用 Reflexive（p28, ce21，有安全影响）。
6. 认证失败后授权残留不撤销——AP 侧升 AWOS 5.0.1+，交换机侧无解（ce23，安全影响）。
7. AOS 8.8R1 × AWOS 4.0.4 组合 LLDP 链路不显示——AOS 8.8R2 修复，先核版本组合（ce18）。
8. 有线 CP 认证失败——客户端网络需 DNS 且解析到 OV 辅助 IP（ce28）。
9. 手机 App 流量绕过 WCF——无解，方案阶段就算 App 豁免（ce38）。
10. Firefox 大列表卡顿——换 Chrome/Edge，或调 about:config 两个参数（ce57）。

判读三原则：先查版本组合（大量问题绑定 AOS/AWOS/OV 版本）；区分 bug 与功能边界（改方案而非等修复）；No workaround 条目转为预期管理（估算窗口、告警降噪）。每条带 PR 号，可向 ALE TAC 交叉确认修复版本。

## 五、兼容矩阵要点

- **交换机固件**（p13-14）：OS2260/2360 = 5.2R5-R7；OS6350/6450 = 6.7.2.R06-R08；OS6360/6465/6560/6570M/6860E/6860N/6865 = 8.9R4 / 8.10R2 / 8.10R3；**OS6870 特殊，只有 8.10R2/R3，没有 8.9R4 档**；OS6900-X20/X40/T20/T40/Q32/X72 = 仅 8.9R4；OS9907/9912 = 8.9R4 / 8.10R2 / 8.10R3。Stellar AP 推荐 AWOS 5.0.2。
- **浏览器**：仅 Chrome / Firefox / Edge，IE 已弃用（p18）；Firefox 处理大列表有已知性能问题。
- **OS/宿主机**：ESXi 6.5-8.0、Hyper-V 2012R2-2022、Win10 Pro、KVM Ubuntu 22.04（p5）；底层操作系统 Oracle Linux 8.10（p9）。VMM 应用锁死在 Hyper-V 2012/2012R2/2016。
- **新特性依赖**：Enhanced Open 需 AP AWOS 4.0.8+；Blast-RADIUS 交换机侧命令 `aaa radius message-authenticator` 需 AOS 8.10R2+；Message-Authenticator 响应校验需 AWOS 5.0.2+。

一句话收束：4.9R2 的升级决策 = 路径判定（4.9R1 直升、其余先上 4.9R1）+ 三大陷阱前置（OS6570M 单向门闩、强口令公告、避开同步期 failover）+ 兼容矩阵过一遍。做完这三件事再动变更单，93 页原书里 90% 的坑已经绕开。

---
由 cangjie-skill 流水线从 OV2500 4.9R2 Release Notes 蒸馏生成
