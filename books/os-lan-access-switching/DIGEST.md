# DIGEST · OmniSwitch LAN Access Switching 精华长文

> 目标读者：不读全书、只要能用的新工程师。教材 DT00XTE215EN（ALE 售后 Newcomers 路径，500 页，3 天课）。本文按"概念 → 配置模型 → 速查 → Lab → 路径 → 避坑"组织，数字均带原书页码。

---

## 一、一页看懂接入层基础（AOS 特有概念地图）

把 OmniSwitch AOS R8 和你熟悉的思科 IOS 对照着记，有三样东西是 ALE 独有的，先立住概念再动手：

- **目录式配置**：没有单一 startup-config，配置和镜像一起放在 certified / working / user-defined 目录里（详见第二节）。这是 AOS 与所有主流网络 OS 拉开差距的地方。
- **Virtual Chassis（VC，虚拟机箱）**：多台交换机经 VFL 链路互联后呈现为一台逻辑设备——单管理 IP、跨机箱端口聚合、免 STP/VRRP、免许可（p95）。两台核心"组 VC"和"配 VRRP"是两条不同的路，别混。
- **DHL（Dynamic Dual Homing Link，动态双归属）**：接入交换机双上行两台核心，不用 STP 阻塞就能防环——每个 VLAN 只在一条链路转发，故障时整体切换（p257-259）。这是 ALE 接入层替代"STP+VRRP"组合的招牌方案。

其余概念与业界通用：VLAN/802.1Q trunk、LACP 聚合、STP/RSTP、VRRP、DHCP Relay、QoS/ACL、PoE——但命令语法和默认值各有 AOS 特色，见第三节速查表。

管理接入第一课：默认账户 admin/switch，本地用户库 userTable9 存 /flash/system，上限 64 用户；8.10R4 起强制改默认密码（p38-39）。带外管理走 EMP 口；无 EMP 的 6360/6465/6560 用 USB-Ethernet dongle 等效（switch-management-access skill）。

## 二、AOS 配置管理模型：certified / working / boot 三目录（重点讲透）

**这一节是全书最值钱的一页。** 大量新手事故不是配错命令，是没搞清"我的配置存在哪、重启后会怎样"。

### 2.1 三个目录 + 一个 RAM

- **certified**：认证基线。冷启动时的保底目录。
- **working**：测试暂存区。新镜像、试验配置先放这。
- **user-defined**：用户自建目录，可多套（如 lab、issu_dir）。
- **running configuration（RAM）**：当前实际生效的配置 = 启动目录内容 + 你敲了还没保存的改动。**改动立即生效，但断电即丢**（p69-71）。

每个目录都是三件套：AOS 镜像 + vcboot.cfg（启动配置）+ vcsetup.cfg（VC 参数）。镜像按型号命名（6360=Nos.img，6900 V72/C32=kaos.img），拷目录时不可混用。

### 2.2 保存语义三层楼（p70-71）

```
write memory                  # RAM → running 目录（只保到当前运行目录）
copy running certified        # 固化为认证基线
write memory flash-synchro    # 一步做两件事（VC 场景同步到所有成员）
```

判断当前状态用 `show running-directory`，三个结果：NOT SYNCHRONIZED（有未保存改动）→ CERTIFY NEEDED（写了 working 没固化）→ CERTIFIED（干净）。

### 2.3 回滚即重启（p81）

冷启动时交换机比较 running 目录与 certified 的"镜像+vcboot.cfg"：
- 内容不同 → 自动从 certified 启动（自动回滚）；
- 内容相同 → 从 running 目录启动。

VC 场景下 flash-synchro 会把镜像+配置同步到所有 slave 的 certified（p95-99）。

### 2.4 升级流程（p452-456）

读 release note → 传新镜像入 running 目录 → `reload from working no rollback-timeout` 验证 → 观察无误 → `copy running certified` 固化。固化前出问题随时回滚旧 certified。必要时先 `update uboot` / `update fpga-cpld`。

## 三、功能速查表

| 功能 | 关键命令 | 关键参数与默认值 | 页码 |
|---|---|---|---|
| VC 部署 | `virtual-chassis chassis-group N` | priority 0-255，最大者为 master；选举链：priority → uptime(差>10分钟才比) → chassis ID → MAC；chassis-id/priority 改动须 reload 生效 | p95-107 |
| LACP | `linkagg lacp agg N size X actor admin-key K` | admin-key 仅本地有效，不必等于组号；静态聚合仅限 OmniSwitch 之间，对接第三方必须 LACP；单边配好显示 DOWN 属正常 | p201-217 |
| STP | `spantree vlan N priority 20000` | 模式 flat/per-vlan（默认 per-vlan）；bridge priority 默认 32768 越小越优；STP 收敛 50s，RSTP <1s；路径成本 16bit：1G=4、10G=2 | p227-248 |
| DHL | `dhl 1 linka linkagg A linkb linkagg B` | 每机仅 1 会话 2 链路；回切 pre-emption timer 默认 30s（0-600 可配）；DHL 口 STP 自动禁用 | p257-266 |
| VRRP | `ip vrrp 1 interface int_20 address <虚IP>` | priority 默认 100，大者为 master；虚拟 MAC 00-00-5E-00-01-{VRID}；**运行中改优先级无效，必须先 disable → 改 → enable** | p297-312 |
| DHCP Relay | `ip dhcp relay destination <IP>` | global 与 per-interface 互斥；默认关闭；默认跳数 16，Opt82 格式 Base MAC | p275-293 |
| QoS | `policy condition/action/rule` + `qos apply` | QoS 默认启用；端口 802.1p/DSCP 默认 0、默认 untrusted；未命中规则默认 accept；**不 qos apply 不生效** | p317-346 |
| ACL | 同上引擎，action 加 `disposition deny` | UserPorts 组入组即防源 IP 欺骗；PBR 仅 6570M/6860/6865/6900/9900 支持 | p369-374 |
| PoE | `lanpower …` | af=15.4W / at=30W / bt T3=60W / T4=100W；端口优先级默认 low，critical 尽量保电 | p434-441 |

## 四、Lab 精要索引（15 个 Lab 一句话）

| Lab | 页码 | 一句话摘要 |
|---|---|---|
| 远程访问 | p54-63 | 验证 AAA 认证链、SSH/WebView 登录、改会话超时并保存 |
| 目录全流程 | p79-88 | 建 VLAN 只存 RAM → reload all 全丢 → reload from working 找回 → 自建 lab 目录 → 固化 |
| Virtual Chassis | p112-122 | 6360 双机组 VC：chassis-group/priority/VFL auto 口，重启生效后看拓扑 |
| LACP 基础 | p209-217 | 跨 VC 机箱建 4 口聚合，单边配好 DOWN 属正常，拔链路演练 |
| LACP 故障 | p209-217 | disable 成员口，验证单链路存活与流量不中断 |
| 802.1Q trunk | p218-224 | 一口同载 tagged 20/30 + untagged 58，跨 VLAN ping 验证 |
| STP 根桥 | p238-248 | priority 20000 定根，看 ROOT/ALT/BLK，VLAN20/30 分根做负载分担 |
| DHL | p261-266 | linkA/linkB 双聚合，禁 A 验证无缝切换，恢复等 30s 回切 |
| DHCP Relay | p289-293 | 两核心配 relay 指向 DHCP 服务器，客户端自动获取后看计数 |
| VRRP | p305-312 | 双 VRID 主备分担，改优先级三步法，重启 Master 演示秒级接管 |
| 诊断工具 | p187-195 | swlog 调级、command-log 审计、port-mirroring/monitoring 抓包、show health |
| QoS | p344-350 | 未打标流量给 802.1p 7，VLAN20 限速 100k，大包触发三色丢弃 |
| ACL | p369-374 | VLAN20 禁 FTP、VLAN30 禁 HTTP，收尾挂 UserPorts 防欺骗 |
| 动态 VLAN | p144-157 | UNP 按 MAC 分类自动入 VLAN 40，flush 触发重分类 |
| Access Guardian | p397-406 | RADIUS + 802.1X/MAC 认证，employee/contractor 各进各 VLAN，LLDP 看邻居（p422-426） |

## 五、学习路径（8 个 skill 对应 3 天课）

按依赖关系顺序学，每个 skill 就是一个知识块：

| 序 | Skill | 对应课程日 | 前置 |
|---|---|---|---|
| 1 | switch-management-access（登录/AAA/开局） | DAY 1 | 无 |
| 2 | aos-config-management（三目录/保存/回滚） | DAY 1 | 1 |
| 3 | virtual-chassis-deployment（VC 堆叠） | DAY 1 | 2 |
| 4 | vlan-link-redundancy（VLAN/LACP/STP/DHL） | DAY 1-2 | 2 |
| 5 | poe-ops-diagnostics（日志/抓包/PoE/升级） | DAY 2 | 2 |
| 6 | ip-services-basic（IP 接口/DHCP/VRRP） | DAY 2 | 4 |
| 7 | qos-acl-policy（QoS/ACL 统一策略引擎） | DAY 3 | 4 |
| 8 | access-guardian-unp（UNP/准入/LLDP） | DAY 3 | 4、7 |

节奏建议：DAY 1 把 1-3 吃透（管理面+配置模型+堆叠是地基），DAY 2 走 4-6（L2/L3 转发面），DAY 3 收 7-8（策略与安全面）。每个 skill 都有 Lab，动手比看文档重要。

## 六、新人常踩的坑（B 节精华）

1. **reload all 恒从 certified 启动**，与 running 目录内容无关（p81/83/85 三处大写 Warning）。想验证 working/user 目录的配置必须 `reload from working no rollback-timeout`，用错命令试验配置直接蒸发。
2. **certified 运行模式下 write memory 直接报错**（"Write memory is not permitted when switch is running in certified mode"），目录间也移不了文件——先 reload from working 切回来。
3. **RAM 未保存改动断电即丢**：改动生效 ≠ 已保存。working 与 certified 一致时重启直接回滚，Lab 里建的 VLAN 2/3/99 全失（p79-88 演示过一遍）。
4. **VC 里 write memory 弹 "Chassis 1 missing! … erased permanently" 确认框**：拓扑变化时按 Y 会永久清除缺失机箱的配置段，看懂再按（p112-122）。priority/chassis-id 改完必须 reload 才生效，别以为配了 200 就完事。
5. **VLAN 1 删不掉**，只能停用/移端口，清理脚本要把它剔除；**VLAN 无活动成员时 IP 接口 DOWN 且不进路由宣告**——排障先 show vlan members 再查路由。
6. **端口带 VLAN 成员身份加不进 linkagg**（报 "Port cannot be added to Linkagg"）：先 `no vlan N members port …` 清干净再入组。
7. **VRRP 运行中改优先级无效**：必须 disable → priority → enable 三步（教材大写 Warning，p305-312）。
8. **QoS 不 qos apply 不下发硬件**；端口默认 untrusted 会把已有标记抹成 0——要保留原始标记先 `qos port <口> trusted`。
9. **AAA 的 exit-on-fail 语义反直觉**：enable 是"只用第一台可用服务器"，disable 才是逐台 fail-through——多 RADIUS 容灾场景要 disable（p41）。
10. **DHL 回切等 30 秒**（pre-emption 默认值），别误判故障；monitoring 与 mirroring 不能落同一物理口，抓包前先规划口的角色。

---

*由 cangjie-skill 流水线从 DT00XTE215EN 蒸馏生成*
