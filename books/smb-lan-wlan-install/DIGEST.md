# 《LAN & WLAN Installation & Configuration for SMB》精华digest

来源书：DT00XTE301 LAN & WLAN Installation & Configuration for SMB（ALE OmniSwitch + OmniAccess Stellar + OmniVista Cirrus 产品线，SMB 场景安装配置教材）

## 一、本书核心知识地图

全书沿"设备 → 交换机基础 → 无线 → 云管 → 排障"一条主线展开，可拆为六块：

1. **产品与选型**：OmniSwitch LAN 家族按"Gig/10G/Hardeded/大型 + 接入-汇聚-核心"两轴定位（<<<PAGE 12>>>–<<<PAGE 13>>>）；Stellar AP 覆盖 Wi-Fi 6/6E/7（<<<PAGE 16>>>–<<<PAGE 18>>>）；Wi-Fi 代际九维对照表（Wi-Fi 6 = 9.6Gbps/WPA3，Wi-Fi 7 = 46Gbps/320MHz/MLO，<<<PAGE 45>>>）。
2. **交换机基础管理**：默认凭据 admin/switch、Console 115200 8N1（<<<PAGE 60>>>、<<<PAGE 65>>>）、ASA 各管理通道独立认证开关（<<<PAGE 58>>>–<<<PAGE 59>>>）、Lightning Config 开箱 5 分钟交付（<<<PAGE 474>>>–<<<PAGE 490>>>）。
3. **AOS 配置管理**：working/certified/user-defined 三层目录 + RAM 运行配置的状态机与回滚模型（<<<PAGE 118>>>–<<<PAGE 137>>>）。
4. **二层/三层组网**：VLAN 划分与 tagged/untagged 分配（<<<PAGE 158>>>–<<<PAGE 175>>>）、PoE 四标准预算（<<<PAGE 147>>>）、STP 防环与 LACP 聚合（<<<PAGE 238>>>–<<<PAGE 260>>>）。
5. **无线**：Stellar 三部署模式（Express/Enterprise/Cloud）与 AP Group 自动成组、PVM/SVM 选举（<<<PAGE 185>>>–<<<PAGE 268>>>）、SSID→VLAN→认证策略设计（<<<PAGE 215>>>–<<<PAGE 235>>>、<<<PAGE 365>>>–<<<PAGE 425>>>）。
6. **云管与运维**：OV Cirrus 上线状态机到 OV Managed（<<<PAGE 282>>>–<<<PAGE 360>>>）、许可订阅生命周期（<<<PAGE 295>>>–<<<PAGE 300>>>）、计划升级与支持信息收集（<<<PAGE 451>>>–<<<PAGE 456>>>）。

对应的 9 个技能单元：switch-first-setup / aos-config-management / vlan-port-assignment / poe-power-design / stp-lacp-basics / stellar-mode-selection / ssid-security-design / guest-access-design / cirrus-onboarding / smb-troubleshooting（排障为横向技能）。

## 二、最重要的 10 个知识点串讲

**1. AOS 三层目录状态机——一切配置操作的底层模型。**
Flash 分 certified（已认证稳定目录）与 working（待验证目录），运行配置在 RAM。`write memory flash-synchro` = 保存 + 认证同步一步完成（<<<PAGE 122>>>）。三个致命特例：`reload all` 无条件从 certified 启动（<<<PAGE 132>>>）；未保存的修改重启即丢（<<<PAGE 133>>>）；从 certified 运行时 `write memory` 直接报错（<<<PAGE 135>>>）。验证新配置永远用 `reload from working no rollback-timeout`。

**2. Lightning Config——开箱交付的标准路径。**
五项前置（仅 1/2 口接入、无既有配置、无 DHCP 分配、无 RCL/NMS）满足时，Chrome 访问 https://192.168.0.1 走向导，单台 5 分钟通流量（<<<PAGE 75>>>、<<<PAGE 474>>>–<<<PAGE 490>>>）。红线：配置前禁止接入网络或互联——所有新机默认同 IP 192.168.0.1 必冲突（<<<PAGE 486>>>）。

**3. PoE 预算与优先级断电顺序。**
四标准：af 15.4W / at 30W / bt Type3 60W / Type4 100W（PD 可用 12.95/25.5/51/71W，<<<PAGE 147>>>）。超预算按 Low → High → Critical 断电，AP 上联口应设 `priority critical`（<<<PAGE 151>>>）。特性三选：Fast PoE 秒级供电、Perpetual PoE 重启不断电、delayed-start 等系统稳定（但与 FPoE/PPoE 互斥，<<<PAGE 154>>>）。

**4. STP 防环是二层生存底线。**
OmniSwitch 默认 per-VLAN 模式；RSTP/MSTP 收敛 <1 秒 vs STP 50 秒（<<<PAGE 238>>>）。按 VLAN 调 `spantree vlan 20 priority 20000` 可让阻塞端口错开，白拿负载分担（<<<PAGE 240>>>）。物理环路未防环会拖垮全网，接线前必须确认 loop avoidance（<<<PAGE 494>>>）。

**5. LACP 优于静态聚合。**
静态聚合仅 ALE 设备互通；LACP 经 LACPDU 跨厂商协商最优参数（<<<PAGE 252>>>）。`hash-control extended` 把四层端口纳入哈希、分担更均匀（<<<PAGE 259>>>）；组播默认走聚合主端口，需显式开启 non-ucast 哈希（<<<PAGE 260>>>）。

**6. Stellar 三模式决策树——AP 上电自动选型。**
DHCP option 138 有 OV2500 地址 → Enterprise；否则联系 Cirrus，MAC/SN 已注册 → Cloud；未注册 → Express 落地（<<<PAGE 198>>>）。规模上限 255 / 4000 / 10000 台对应选型（<<<PAGE 185>>>–<<<PAGE 189>>>）。

**7. AP Group 自动成组与 PVM 选举。**
同 Group ID + 同 VLAN 即自动成组，出厂 Group ID 100（<<<PAGE 202>>>）；PVM/SVM 先比型号高低再比 MAC 大小（<<<PAGE 203>>>）。两大坑：多台新 AP 默认 IP 都是 192.168.1.254 会冲突（<<<PAGE 101>>>）；AP 入组后本地配置被 PVM 下发的组配置覆盖（<<<PAGE 266>>>）。

**8. SSID→VLAN→认证三级分流。**
客户端连 SSID 自动落入预定义 VLAN（<<<PAGE 215>>>）；认证三档：Personal 密码、Enterprise 802.1X（UPAM 或外部 RADIUS）、Open + Captive Portal（访客）。用户策略用 ARP（Access Role Profile）六元组描述：VLAN/QoS/防火墙/L7/位置/时段（<<<PAGE 376>>>），裁决顺序外部源 > 内部库 > 认证策略 > SSID 默认（<<<PAGE 382>>>）。三角色基线：员工全访问高带宽、访客仅 internet 低优先级、话机低带宽高优先级（<<<PAGE 217>>>）。

**9. Cirrus 上线 = 设备 call-home + 云侧申报双向握手。**
前提：交换机 AOS ≥ 8.9R1（OS2360 不行，<<<PAGE 337>>>）、AP AWOS ≥ 4.0.6 且排除 AP1101/AP1201L/H/HL（<<<PAGE 290>>>）、防火墙与 DHCP option 就绪。cloud-agent 默认 30 分钟重试（<<<PAGE 314>>>），状态机走 Registered → … → OV Managed 才算受管（<<<PAGE 309>>>–<<<PAGE 310>>>）。云侧四步：申报 SN → 分组 → 下发配置 → 确认 OV Managed（<<<PAGE 282>>>）。

**10. 分层排障方法论。**
L2（线缆/VLAN/PoE）→ L3（IP 接口/ping 激活域名）→ 设备侧（getmode/ocloud_show）→ 平台侧（激活日志/认证记录）（<<<PAGE 347>>>–<<<PAGE 360>>>）。无线侧 support 凭据下有 iwconfig / ssudo sta_list / wam_debug sta_list / eag_cli / tcpdump 完整工具链（<<<PAGE 397>>>–<<<PAGE 430>>>）。LED 是最快的物理层判读：AP 绿闪 = 就绪、蓝红闪 = 升级中（<<<PAGE 52>>>）；PoE 口琥珀 = 受电、绿 = 未受电（<<<PAGE 143>>>）。

## 三、一句话总结

SMB 交付的本质是三条确定性链路：配置链（Lightning Config → working/certified 状态机 → flash-synchro 固化）、供电与链路链（PoE 预算 + critical 优先级 + STP/LACP 防环扩带宽）、管理链（三模式选型 → AP Group 成组 → 按需上 Cirrus 到 OV Managed）；排障永远分层走，先怀疑环境默认行为（端口 disabled、non-https 门户、IP 冲突），再怀疑故障。

（全文约 2600 字，页码均出自 verified.md 已核对条目）
