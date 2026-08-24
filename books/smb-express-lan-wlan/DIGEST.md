# DIGEST · OmniSwitch LAN Access & OmniAccess Stellar WLAN Express 精华长文

> 来源：DT00XTE310 教材 verified 候选（154 条），页码以 <<<PAGE N>>> 标注。配套 10 个 SKILL.md 见各子目录。

## 一、知识地图

全书可拆成四层十域：

**平台层**
1. AOS 双分区配置管理（working/certified/user-defined 状态机、备份、镜像升级）
2. Cirrus 云管上线（许可证→订阅→SN 宣告→激活状态机）

**有线网络层**
3. VLAN 与 VLAN 间路由（802.1Q、IP interface）
4. PoE 管理与功率预算
5. 交换机高可用（Virtual Chassis / LACP / STP / DHL / VRRP）
6. QoS / ACL / Access Guardian 策略

**无线网络层**
7. 无线技术基础（Wi-Fi 4→7 代际演进）
8. Stellar 三部署模式选型与分布式架构（Express / Enterprise / Cloud）
9. Wi-Fi Express 模式日常操作（SSID、内置 DHCP、访客账号）
10. Voice over WLAN 部署（覆盖、QoS、漫游、容量）

外加一条贯穿全书的**故障排查方法论**（分层递进 + 分侧取证）。

## 二、十个最重要知识点串讲

### 1. AOS 双分区：配置即文件，冷启动有回滚保护

AOS R8 用 working / certified / user-defined 三目录管理配置（<<<PAGE 85>>>）。`write memory` 把 running 写入 working，`copy running certified` 完成认证，`write memory flash-synchro` 是三合一（<<<PAGE 89>>>）。冷启动时交换机比较 working 与 certified 内容：相同则从 running 启动，不同则从 certified 启动（<<<PAGE 88>>>、<<<PAGE 126>>>）。这带来两个必记的坑：`reload all` 无条件从 certified 启动，未认证配置必丢（<<<PAGE 126>>>）；certified 模式下运行是只读的，`write memory` 会报 "not permitted when switch is running in certified mode"（<<<PAGE 129>>>），解法是 `reload from working no rollback-timeout` 或 `modify running-directory working`。备份有两条路：内置命令打 .tar（最多 10 份，<<<PAGE 92>>>）和 USB 自动备份（<<<PAGE 93>>>、<<<PAGE 132>>>-<<<PAGE 133>>>）。

### 2. VLAN 间路由：绑定 IP interface 即开路由

AOS 上 IP interface 与 VLAN 绑定后，三层路由立即激活——网关即虚拟路由器端口（<<<PAGE 165>>>）。要注意 VLAN 的 operational 状态依赖活动成员端口：无活动端口则 IP 接口 DOWN、不参与路由（<<<PAGE 512>>>）。每个物理端口恒有一个默认（untagged）VLAN 做二层桥接（<<<PAGE 599>>>）；802.1Q tag 提供 4096 个 VID 与 3bit 的 802.1p 优先级（<<<PAGE 169>>>）。AP 口的典型配置是"管理 VLAN untagged + 业务 VLAN tagged"（<<<PAGE 177>>>-<<<PAGE 183>>>），这也是上云排障时"管理 VLAN 须 untagged"的由来（<<<PAGE 377>>>）。

### 3. Stellar 三模式自动选型：AP 自己会"找组织"

AP 上电后走三级判定：DHCP 下发 option 138（OV2500 地址）则进 Enterprise；已在 Cirrus 声明（MAC/序列号）则进 Cloud；两者皆无则落 Express（<<<PAGE 201>>>、<<<PAGE 264>>>）。规模边界：Express ≤255 AP 免许可证、Enterprise（OV2500）≤4000 AP、Cloud（Cirrus）≤10000 AP（<<<PAGE 188>>>-<<<PAGE 198>>>）。选 Express 前核对功能边界：Express 无语音分析与可视化（<<<PAGE 875>>>），AP1101 组规模仅 64 AP/256 客户端（<<<PAGE 868>>>）。

### 4. 分布式架构：同组 AP 自动成组，PVM 统一管理

无控制器架构下，同 Group ID + 同 VLAN 的 AP 自动成组（出厂 Group ID=100/VLAN 1，<<<PAGE 205>>>），按"最高型号 → 最高 MAC"选举 PVM/SVM（<<<PAGE 206>>>）。AP 间通过空口交换 RF 设置、通过 LAN 交换漫游客户端上下文（MAC、密钥、Access Role Profiles）（<<<PAGE 270>>>）。最大的坑：AP 入组后自身配置被 PVM 下发配置整体覆盖删除（<<<PAGE 243>>>）——先把目标配置做到 PVM，再扩成员。

### 5. 云管上线流水线与激活状态机

交换机上云序列：确认 cloudagent.cfg 在 working（缺则从 /flash/cirrus 拷贝，<<<PAGE 356>>>）→ 管理_VLAN/IP/静态路由 → SNMP/NTP/DNS → `cloud-agent admin-state enable` → Cirrus 建 Site 后用 `show chassis` 的 SN 建 Device → 强制激活 `cloud-agent admin-state disable force` + `enable` → `show cloud-agent status` 见 completeOK（<<<PAGE 353>>>-<<<PAGE 364>>>）。激活状态机每步有明确定义：Registered → Obtaining Certificate → VPN Configuring → Connected → OV Managed；失败态含 Factory Reset Required 等（<<<PAGE 327>>>-<<<PAGE 328>>>）。迁移 OVC4→OVC10 时序列号不能双平台并存，先删后宣（<<<PAGE 318>>>）；call home 慢优先 disable force/enable 而非重启（<<<PAGE 331>>>）。

### 6. SSID 与策略：五步向导 + ARP 三级裁决

SSID 创建走五步向导：General → Authentication → Access Policy → Default VLAN/Network → Assignment & Schedule（<<<PAGE 383>>>）；访客多出 Guest Access Strategy（Portal 模板/Login 方式/自注册，<<<PAGE 427>>>）。用户策略由 ARP（Access Role Profile）承载——VLAN tag/QoS/防火墙 ACL/L7 规则/位置/时段的集合（<<<PAGE 394>>>），裁决优先级：外部 RADIUS/LDAP 下发 > 认证策略内 > SSID 默认（<<<PAGE 400>>>）。802.1X 员工 SSID 全流程与访客 Portal + Kick Off 的实操见 <<<PAGE 407>>>-<<<PAGE 414>>>、<<<PAGE 437>>>-<<<PAGE 443>>>。

### 7. 交换机高可用：五件套按需组合

- **Virtual Chassis**：多台虚拟成单逻辑设备，VFL 互联，ISIS-VC 管理拓扑，免 STP/VRRP/许可证（<<<PAGE 468>>>、<<<PAGE 471>>>）；Master 选举按 priority → uptime → chassis ID → MAC（<<<PAGE 472>>>）；分裂双检测 RCD（带外走 EMP，原 Slave 关全部用户口）+ VSCP（<<<PAGE 476>>>-<<<PAGE 477>>>）；ISSU 逐台 slave 升级（<<<PAGE 478>>>）。
- **LACP**：`linkagg lacp agg N size 2 actor admin-key N` 关联端口（<<<PAGE 576>>>、<<<PAGE 588>>>）；负载哈希 extended 含四层端口更均匀（<<<PAGE 583>>>）。
- **STP**：默认 per-VLAN 模式，RSTP 亚秒收敛（<<<PAGE 604>>>）；1x1 模式按 VLAN 分根桥做负载分担（<<<PAGE 606>>>）。
- **DHL**：按 VLAN 划分活跃链路的双活方案，DHL 端口自动关 STP；默认 mac-flushing=none 会留过期 MAC，生产显式配 `dhl 1 mac-flushing raw`（<<<PAGE 628>>>-<<<PAGE 630>>>、<<<PAGE 642>>>）。
- **VRRP**：虚拟 MAC 00-00-5E-00-01-VRID，多 VRID 负载分担；改 priority 必须先 disable（<<<PAGE 674>>>-<<<PAGE 675>>>、<<<PAGE 689>>>）。

### 8. PoE：功率是预算，优先级是保险

四档标准：802.3af（PD 12.95W）→ at（25.5W）→ bt Type3（51W）→ Type4（71W）（<<<PAGE 150>>>）。管理三板斧：`show lanpower slot`（看 Actual Used/Power Budget）、`lanpower slot maxpower`（W）、`lanpower port priority critical`（<<<PAGE 153>>>-<<<PAGE 157>>>）。功率不足按 low→high→critical 断电（<<<PAGE 154>>>），关键口务必显式设 critical。Dynamic PoE Allocation 按需供电最省（<<<PAGE 150>>>）；Fast/Perpetual PoE 需 FPGA 升级（<<<PAGE 147>>>-<<<PAGE 148>>>）。

### 9. VoWLAN：覆盖、QoS、漫游三线并进

覆盖按 -70dBm、漫游按 -62~-64dBm、边界交叠 8dB、SNR≥25dB 设计（<<<PAGE 928>>>-<<<PAGE 931>>>）；容量基准 1 AP/255m²、每 AP 20-25 用户（<<<PAGE 253>>>），AP13XX 约 35 条语音流（<<<PAGE 892>>>）。QoS 映射 Voice=DSCP46/802.1p6，信令 DSCP 26（<<<PAGE 874>>>、<<<PAGE 933>>>）。质量门限：时延 <250ms、重传 <15%、Jitter <100ms、丢包 <2%（<<<PAGE 933>>>）。漫游靠 802.11r/k/v（<<<PAGE 938>>>-<<<PAGE 940>>>），L3 漫游由新 AP 向 Home AP 建 GRE 隧道（<<<PAGE 894>>>）。禁区：不支持 11r 的终端可能连不上 11r WLAN，按终端能力分 SSID（<<<PAGE 938>>>）；语音走 5GHz，2.4GHz 信道聚合在大部署自扰（<<<PAGE 908>>>-<<<PAGE 909>>>、<<<PAGE 913>>>）；RAP 勿放总部、加密带宽约 100Mbps、同地两 RAP 话机不切换（<<<PAGE 904>>>）。

### 10. 排查方法论：分层递进，命令说话

AP 不上线的五步法：`show lanpower slot`（PoE）→ `show vlan members port`（管理 VLAN untagged）→ AP 侧 `getmode`/`cat /etc/config/network` → `show ip interface` + ping 激活域名 → Cirrus Activation Log（<<<PAGE 376>>>-<<<PAGE 378>>>）。SSID 连不上在 AP CLI 走 iwconfig → sta_list → AAA_server.conf → tcpdump 抓 RADIUS（<<<PAGE 415>>>-<<<PAGE 418>>>）；Portal 不弹页查 date/resolv.conf → eag 进程与 eag.log（<<<PAGE 444>>>-<<<PAGE 448>>>）。安全红线：预配置设备（实验室核心、Organization）不要动出厂/删除（<<<PAGE 123>>>、<<<PAGE 100>>>、<<<PAGE 358>>>）；Lightning Config 只在"仅 1/2 口接客户端、无既有配置、无 DHCP 分配、无 NMS 连接"时触发（<<<PAGE 79>>>、<<<PAGE 1025>>>）。

## 三、一句话总结

这本书的骨架是"两个操作系统（AOS/AWOS）+ 三种管理模式（Express/Enterprise/Cloud）+ 一套分层排障法"：先想清配置落在哪个目录、AP 归哪个组、策略由谁裁决，再动手敲命令，最后用 show/logs 验证闭环。
