# 验证通过条目 · stellar-wlan-adv-trouble-update（阶段 1.5）

> 验证规则：V1 原文真实性（quote 在对应页命中）+ V2 可操作价值（新特性配置/参数/Lab）+ V3 独特性（非常识）
> 原文抽查基于 source/fulltext.md（页标记 `<<<PAGE N>>>`）；quote 与 OCR 表格存在换行/排版归一化差异，内容均能在对应页命中。

## 汇总

| 类型 | 候选 | 通过 | 淘汰 |
|---|---|---|---|
| frameworks | 8 | 7 | 1（f03） |
| principles | 22 | 20 | 2（p01、p03） |
| cases | 12 | 12 | 0 |
| counter-examples | 10 | 10 | 0 |
| **合计** | **52** | **49** | **3** |

淘汰明细见 `rejected/` 目录（frameworks.md、principles.md）。

## 通过条目清单

### frameworks（7 条）

- **f01** SSID 向导三步创建流程（p242-250）——V1 命中（p243 起 Wizard driven tool / WLAN service (expert) 对照）；V2 含向导三步与 Expert 模式入口；V3 OV2500 特有流程。
- **f02** Enterprise 模式设备上线工作流（p213-232）——V1 命中（DHCP relay/PoE 前置清单原文）；V2 完整纳管操作流；V3 option 138 + AP Group 纳管为 ALE 特有。
- **f04** 用户带宽控制四层判定流程（p284）——V1 命中（p284 判定树：DPI→ACL→Access Role→SSID Shared）；V2 含三层配置入口；V3 厂商私有判定顺序。
- **f05** RAP 上线 Premium 四步（p377-382）——V1 命中（四步流程图原文）；V2 含管理员预录入项清单；V3 ALE RAP 方案特有。
- **f06** RAP 上线 Freemium 五步双隧道（p384-390）——V1 命中（五步流程图原文）；V2 含管理/数据双隧道与 VPN Server 三网卡要求；V3 特有。
- **f07** Cirrus 4 设备注册流程（p413-421）——V1 命中（注册流程清单原文）；V2 含 failsafe/firstboot 与 cloud-agent 停用命令；V3 特有。
- **f08** 备份-恢复-升级三段工作流（p426-432）——V1 命中（Resource Manager 备份说明原文）；V2 含备份类型/调度/升级双路径；V3 特有。

### principles（20 条）

- **p02** Wi-Fi 7 双雄规格 AP1511/AP1521（p152-153）——V1 命中（Tri radio 规格表）；V2 选型参数（EHT320、PoE 档位、上联速率）；V3 ALE 型号专属。
- **p04** 三种管理模式与规模红线（p169-176）——V1 命中（255/32/64/4000 上限原文）；V2 容量规划硬数字；V3 特有。
- **p05** IPv6 客户端支持差异（p178-179）——V1 命中（Express/Enterprise IPv6 对照原文）；V2 IPv6 项目模式选型依据；V3 特有差异表。
- **p06** WPA3 SAE 与 CNSA 192 位（p256）——V1 命中（SAE/CNSA/AP1101 例外原文）；V2 含 CNSA 开关对终端兼容的影响；V3 含 AP1101 例外这类厂商细节。
- **p07** SSID Usage 模板与安全级别映射（p245）——V1 命中（p245 Usage 模板表）；V2 向导选型映射表；V3 特有。
- **p08** WLAN Service 加密类型全集与必填项（p261）——V1 命中（DYNAMIC_WEP…WPA3_PSK_SAE_AES 枚举原文）；V2 必填项清单（AAA/Passphrase/Default Access Role）；V3 特有。
- **p09** 广播/组播优化参数（p270-271）——V1 命中（15 分钟轮换、90%/6 客户端阈值原文）；V2 具体默认值与熔断阈值；V3 特有。
- **p10** WMM QoS 推荐 DSCP/802.1p 映射（p273）——V1 命中（p273 Recommended/Default 两张表）；V2 两组映射数值可直接套用；V3 OV 默认值与推荐值不一致是厂商细节。
- **p11** 漫游特性参数（p188-191）——V1 命中（OKC/11r/RSSI 10/15 原文）；V2 特性-安全级别绑定关系与推荐阈值；V3 特有。
- **p12** RSSI 与 dBm 换算 dBm=RSSI−96（p186, p365）——V1 命中（p186 RSSI-dBm 表、p365 subtract 96 原文）；V2 配置阈值前必须换算，可操作；V3 换算基线 96 是 ALE 体系特有。
- **p13** BLE Beaconing 参数（p194）——V1 命中（iBeacon/UUID/Major/Minor 原文）；V2 按 AP Group 配置的参数清单；V3 特有。
- **p14** Wi-Fi Mesh 规格红线（p399-401）——V1 命中（4 跳/5 台/16 台/5 SSID 原文）；V2 组网硬限制；V3 特有。
- **p15** Bridge 与 Mesh 属性差异及 VLAN tagging 兼容性（p398-399）——V1 命中（AP1101/1201/1201H 不兼容原文）；V2 选型兼容红旗；V3 特有。
- **p16** Cirrus 4 订阅与许可模型（p409-411）——V1 命中（Freemium/Premium/5000/50+50 原文）；V2 上云商务与容量规划依据；V3 特有。
- **p17** Cirrus 4 最低软件版本（p414）——V1 命中（AOS/AWOS 版本表原文）；V2 上云前第一张检查表；V3 特有版本矩阵。
- **p18** RAP 部署设备与账号要求（p375）——V1 命中（AP1101 不兼容 + 两种账号组合原文）；V2 前提条件清单；V3 特有。
- **p19** Stellar AP 备份规则（p427, p430）——V1 命中（按地图备份不含 AP / 不支持 Restore 原文）；V2 变更管理规则；V3 特有。
- **p20** 外接天线判定规则（p158）——V1 命中（ends with "2" 原文）；V2 型号尾数判定可直接套用；V3 ALE 命名规则特有。
- **p21** UPAM 系统级 NAS 项与共享密钥 123456（p307）——V1 命中（All Managed Devices / 123456 原文）；V2 802.1X 排障第一怀疑点；V3 默认密钥是厂商细节。
- **p22** DPI/WCF 硬件支持范围（p281, p287）——V1 命中（AP1101/AP1201H 排除原文）；V2 策略全覆盖的清点清单；V3 特有支持矩阵。

### cases（12 条）

- **c01** AOS 交换机发现 Lab（p213-223）——V1 命中（snmpuserv3/Superuser=1/SNMPv3 Profile 参数原文）；V2 含 CLI 与排障分层；V3 特有。
- **c02** Stellar AP 云上线 Lab（p224-239）——V1 命中（option 138 链路描述原文）；V2 含 VLAN Manager/lanpower/串口排障命令；V3 特有。
- **c03** Employee SSID + 802.1X Lab（p290-310）——V1 命中（EmployeesX/WPA3_AES/PEAP 参数原文）；V2 全流程 + Expert 七对象 + AP 侧排障链；V3 特有。
- **c04** 对接 AD 认证 Lab（p311-316）——V1 命中（LDAP/AD Configuration 字段原文）；V2 两步切换认证源样板；V3 特有。
- **c05** Guest SSID + Captive Portal Lab（p317-338）——V1 命中（KickOff/Add to Blocklist 原文）；V2 含 Unified Policy 附录与排障；V3 特有。
- **c06** WCF 按类别过滤 Lab（p339-349）——V1 命中（WCF-guests 规则与 Apply to Devices 警告原文）；V2 四步落地 + DNS 原理链路；V3 Brightcloud 集成特有。
- **c07** BYOD SSID 动态 VLAN 迁移 Lab（p350-361）——V1 命中（预认证 Guest VLAN/过门户迁 Employee VLAN 原文）；V2 不建新 VLAN 的设计套路可复用；V3 特有。
- **c08** RF Profile 与 Association RSSI 阈值 Lab（p362-371）——V1 命中（阈值 90 vs -18dBm=78 原文）；V2 含 rfprofile.conf 核验命令；V3 特有。
- **c09** RAP Freemium 双隧道全流程 Lab（p451-481）——V1 命中（VPN 字段/vpn_profile 路径/Use Tunnel 原文）；V2 最重的端到端实操；V3 特有。
- **c10** 备份/恢复/升级 Lab（p423-432）——V1 命中（reload from working 原文）；V2 含"恢复不生效"现场复现；V3 特有。
- **c11** 拓扑监控与 Trap 邮件告警 Lab（p433-443）——V1 命中（Trap Responder/SMTP 字段原文）；V2 监控闭环配置可操作；V3 特有。
- **c12** Heat Map 与 Floor Plan Lab（p444-450）——V1 命中（Scale the Map/WallsHeavy/Auto Deployment 原文）；V2 RF 规划工具操作 + 手工/算法布点对比；V3 OV2500 工具特有。

### counter-examples（10 条）

- **ce01** Band Steering 默认关闭的原因（p364）——V1 命中（coverage holes/Force 5GHz 无退路原文）；V2 含正确做法与 Exclude MAC OUI 对策；V3 特有设计权衡。
- **ce02** 国家码选错导致 AP 拒绝工作（p231）——V1 命中（USA/JAPAN/ISRAEL 警告原文）；V2 跨境调拨前置检查；V3 特有。
- **ce03** 评估许可两种导入方式二选一（p209-210）——V1 命中（Don't do both / 只贴密钥原文）；V2 具体操作坑；V3 特有。
- **ce04** Restore 显示成功但不生效（p429）——V1 命中（NOT applied on RUNNING / reload 原文）；V2 变更窗口必算 reload 时间；V3 AOS 三目录模型特有。
- **ce05** 固件包 WinZip 自解压不可手动解压（p431）——V1 命中（p431 WinZip executables 段，跨行导致整串 grep 未中，分段命中）；V2 升级操作红线；V3 ALE 交付格式特有。
- **ce06** OV2500 无 DNS 则 WCF Not in service（p287, p348）——V1 命中（两页原文）；V2 前置检查项与修复路径；V3 特有。
- **ce07** 策略只在认证瞬间应用（p338）——V1 命中（大写警告原文）；V2 改配置三步闭环（推送→重连→重认证）；V3 特有下发模型。
- **ce08** 漫游撞后台扫描（p192）——V1 命中（voice aware 原文）；V2 两个对策（关扫描/专职扫描 AP）；V3 语音感知豁免是 ALE 行为细节。
- **ce09** Roaming RSSI 阈值两头是坑（p191）——V1 命中（too low/too high 原文）；V2 调参方法（从推荐值起步小幅调）；V3 特有。
- **ce10** Stellar AP 不能 Restore（p430）——V1 命中（原文完整命中）；V2 给出替代恢复路径；V3 AP Group 下推架构特有。
