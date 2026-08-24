# DIGEST · OmniAccess Stellar WLAN Enterprise Basic（DT00XTE368EN）精华长文

> 教材 515 页，ALE 售后 Newcomers 路径。本文是"不读全书、只看精华"的压缩版：理论要点、OV2500 交付主线、勘测方法、参数速查、陷阱清单，一篇文章拿走。

---

## 一、一页看懂这门课

这门课是**无线基础理论 + OV2500 企业模式实操**的二合一课（教材 p3-497）：

- **前 140 页（p3-141）**：802.11 原理、标准演进（WiFi 6E/7）、天线、无线安全、企业无线架构、站点勘测基础。这是全套课程里唯一的系统性理论模块，RF/天线/安全原理讲得最全，价值独立。
- **DAY 1（p142-278）**：AP 产品硬件总览、远程实验室、Enterprise 模式网络要求、OV2500 发现（Stellar AP + OmniSwitch）。
- **DAY 2（p279-466）**：SSID 创建（Employee/AD 认证）→ UPAM Guest → 用户角色与带宽控制 → Guest SSID → Web 内容过滤 → L2 移动性与漫游 → RAP → 勘测。
- **附录（p467-497）**：RAP 部署详解、SSID 高级选项。

一句话定位：与 T360（Cirrus 云管线）互补的 **OV2500 本地管路线**——同一个"AP 上线→SSID→策略→漫游"生命周期，网管换成 OV2500。要提醒的是：理论章节每主题只有 10-20 页，属于入门级深度；OV2500 的 GUI 截图时效绑定 4.9R2 版本。

---

## 二、无线理论速成地图（四大块要点）

### 1. 802.11 原理与标准演进（p10-32）
- 基本概念链：BSS（AP + 覆盖区终端）→ BSSID（AP 的 MAC）→ ESS（多个互联 BSS）→ ESSID 即 SSID（32 字符网络名）（p10-11）。
- WiFi 6/7 技术分工：**MU-MIMO 管大包高带宽（容量），OFDMA 管小包低时延（效率）**——OFDMA 把信道切成资源单元 RU，让一个 AP 同时服务多设备；MU-MIMO 从 WiFi 5 的 4x4 仅下行，升级到 WiFi 6 的 8x8 双向（p31-32）。两者叠加使用，别用单一技术解释性能。
- QAM 密度决定速率：256（WiFi 5）→ 1024（WiFi 6）→ 4096（WiFi 7）；排障速率问题按"SNR 变差 → QAM 回落"链解释。
- 产品对应：AP1301-1360=WiFi 6，AP1411/1431/1451=6E，AP1511/1521=WiFi 7。

### 2. 天线（p49-53）
三分类选型：**全向**（内置默认，点对多点短距）、**半定向**（Patch/Panel/Yagi，走廊覆盖、点对点中短距）、**高定向**（Grid，楼宇间长距桥接）。换天线必须复核法定 EIRP。

### 3. 安全（p63 起）
- 演进链：WEP（**全书唯一 NEVER 红线，任何位宽都禁用**）→ WPA/TKIP（过渡）→ WPA2/AES-CCMP（当代最低线）→ WPA3（SAE + 可选 CNSA 192 位）。
- 认证信任梯：Open+门户 < MAC < PSK < 802.1X。
- 6 GHz 室外监管：FCC 域需 AFC（36 dBm），EU 禁标准功率室外，只允许 LPI 23 dBm / VLP 14 dBm。

### 4. 勘测基础（p85-141）
四阶段任务地图：PLAN（需求+预测）→ VALIDATE（预部署勘测→安装→后部署勘测）→ MONITOR/TROUBLESHOOT（频谱/抓包/巡检/持续监控）（p85）。核心认知：**勘测是时间快照，快照越多越懂环境**（p133）。

---

## 三、Enterprise 模式交付主线（串起 7 个 skill）

标准交付顺序，就是教材 DAY 1 到 DAY 2 的展开：

**① 开局（enterprise-mode-onboarding）**
四件套最低要求：出厂净化态 AP + PoE 交换机（管理 VLAN + dhcp-relay）+ DHCP 服务器（管理 VLAN 作用域带 **option 138** 指向 OV2500）+ OV2500（IP + 许可）。上线四步（p242）：上电 LLDP 选管理 VLAN → DHCP option 138 切 Enterprise 模式 → 向 OV2500 注册 → 分配 AP Group 下发配置。受管三条件（p243）：**Trusted + Licensed + 国家码匹配 RF Profile**，任一失败即 Unmanaged、配置不下发、射频全关。排障必背三平面规则（p159-163）：管理流量不打标、业务流量在 AP 上联口打标、无隧道模式、数据面纯 L2。

**② 员工 SSID（employee-ssid-8021x）**
向导三步（p283-289）：命名选 Usage → 定制（频段/加密/默认 VLAN/认证策略）→ 绑 AP Group。Employee 企业网=纯 802.1X，加密优先 WPA3_AES。认证源可解耦：SSID 与 VLAN 不动，从 UPAM 本地库一键切到 External LDAP/AD（声明域控、Test Connection 通过再 Apply，p326-331）。

**③ 访客与策略（upam-guest-access）**
Guest 工作流（p343）：Guest Usage 建 SSID → 勾强制门户 → 认证选内置 RADIUS → 建 Guest 账号（可配数据配额）→ 绑 Guest VLAN。带宽四级判定链（p364）：DPI 应用 → ACL → Access Role 按用户 → SSID 共享，细→粗。Web 内容过滤 WCF（p366-367）：AP DNS 嗅探 → OV2500 查 Brightcloud 类目 → 回发 AP 生成阻断 ACL 本地拦截。

**④ 漫游（roaming-l2-l3）**
判定树（p412）：新 AP 有 Client Context 且 VLAN 一致走 L2（默认开），不一致走 L3（默认关、GRE 隧道）；上下文缺失=按新客户端重接。

**⑤ 远程站点（rap-remote-deployment）**
门店/展会/居家广播企业 SSID：Cirrus 4 录序列号 + ALE VPN Server 双隧道（管理 VPN + 数据 L2GRE），五步上线（p439）。注意 AP1101 不兼容，Tunnel ID 必须填 0。

理论模块（wlan-theory-fundamentals）和勘测模块（site-survey-ekahau）横贯全程，分别回答"为什么这么配"和"AP 放哪、放多少"。

---

## 四、勘测 Ekahau 七步法精要

预测勘测七步（p110-121）：**导入楼层图 → 标比例画墙（赋 dB 衰减）→ 导入设置 → Area 圈区设终端 → Auto-Planner 自动摆 AP → 复核调参重跑 → 出报告**。

现场验证两招：
- 预部署 Stop-and-Go（p126）：AP 装三脚架通电，走测点击采样，测完 Freeze 再搬站，多点位拼整层热图。
- 后部署主动勘测（p127-128）：网内装 ePerf 吞吐服务器，Continuous Survey 匀速走测，采集认证/丢包/RTT/吞吐，出报告留作性能基线。

现场排障三步法：平面图定位 → 实测五查（AP 型号、同频/邻频、覆盖空洞、功率、布放）→ 五类纠正（换型号/重做 RF/收窄信道/删低速率/改善布放）。

两条铁律：**禁止 Over provisioning——信道数是硬上限，堆 AP 会自干扰**；勘测复现不了大规模并发负载，也建议不了天线朝向，"勘测全绿、用户吐槽"优先查并发负载与天线朝向两个盲区。

---

## 五、关键参数速查表

### 材质衰减（p136 画墙仿真用）

| 材质 | 衰减 |
|---|---|
| 石膏板 | 3 dB |
| 室内窗 | 1 dB |
| 砖墙 | 10 dB |
| 混凝土 | 12 dB |
| 卷帘门 | 11 dB |
| 钢质防火门 | 13/19 dB（保守口径门全关） |
| 金属/电梯井/镀膜玻璃 | 按屏蔽体处理（金属吸收、电梯大幅阻挡） |

### 天线与功率

| 场景 | 选型 | 要点 |
|---|---|---|
| 室内覆盖 | 内置全向 | 天线初始垂直朝向，AP 居中、高于障碍物 |
| 走廊覆盖 | 半定向 Patch/Yagi | 长走廊专用 |
| 楼宇间桥接 | 高定向 Grid | 长距，核对 EIRP |
| 6 GHz 室外 | 按 FCC AFC 36 dBm / EU LPI 23 dBm、VLP 14 dBm | EU 禁标准功率室外 |

### 安全与认证

| 对象 | 推荐配置 |
|---|---|
| 员工 | 802.1X（PEAP/MSCHAPv2）+ WPA3_AES |
| 访客 | 门户 + Open/MAC |
| 哑终端 | MAC 认证 |
| 快速漫游 | OKC 仅 WPA2/WPA3 Enterprise；802.11r 需 WPA2/WPA3 加密（p407/414） |
| 广播密钥轮换 | Enterprise 级默认 15 min |

### 漫游阈值（p424）

| 参数 | 推荐值 |
|---|---|
| 2.4 GHz Roaming RSSI | 10（范围 0-100） |
| 5 GHz Roaming RSSI | 15 |

---

## 六、学习路径（7 个 skill 的顺序）

1. **wlan-theory-fundamentals** —— 理论地基。理论薄弱的先读这个：BSS/ESS、WiFi 6/7、天线、安全演进，后面所有配置都在这条理论链上落地。
2. **enterprise-mode-onboarding** —— 第一段实操。AP 怎么上线、OV2500 怎么发现设备，不懂三平面规则后面排障没抓手。
3. **employee-ssid-8021x** —— 第一个 SSID，向导三步 + AD 对接，掌握 OV2500 的对象模型。
4. **upam-guest-access** —— 在 SSID 基础上加门户、限速、策略、内容过滤。
5. **roaming-l2-l3** —— 网络成型后调漫游，判定树 + RSSI 阈值。
6. **rap-remote-deployment** —— 进阶场景，把企业网延伸到远程站点。
7. **site-survey-ekahau** —— 勘测方法贯穿项目始终，可放在最后系统学，也可在设计阶段提前用。

最小路径建议：赶交付就 2→3→4；带新人或做售前讲解，务必从 1 开始。

---

## 七、交付陷阱 TOP10

1. **国家码不匹配 = 射频全关**（p243）。实验室禁选 USA/日本/以色列，教材统一选 FR。
2. **Express 切 Enterprise 不迁移配置**，集群配置全丢——变更窗口预留重建时间。
3. **RADIUS 只走 IPv4**，即使管理面已 IPv6 也要留 IPv4 通路。
4. **改认证源后客户端要清掉已存网络重连**，否则沿用旧凭据误判"认证失败"。
5. **RSSI 阈值双向失败**（p424）："信号差不断线"查阈值偏低（粘住弱 AP），"频繁掉线"查偏高（切换过频丢包）。漫游决定权在终端，网络只能引导。
6. **L3 漫游默认关闭**，忘开会把跨 VLAN 移动当新客户端处理——IP 变、会话断。直角走廊里两台 AP 电波互不可见则漫游不发生，需两边互配静态 Neighbor AP（p423）。
7. **OV2500 没配 DNS，WCF 停在 Not in service**——访客内容过滤验收第一步查这个；且 AP1101/AP1201H 不支持 WCF。
8. **策略在认证成功时套用**：改完必须断开重连强制重认证，否则误判"没生效"。门户重定向也只对 HTTP 触发，HTTPS 站点不跳门户。
9. **OV2500 与 AP 时间不同步**，访客账号"没过期却登不上"——两侧 `date` 核对，根治配 NTP。
10. **RAP 三坑**：AP1101 不兼容；Tunnel ID 必须填 0；VPN .conf 导出后丢失只能重导，立即备份。

外加一条勘测红线：**别承诺"测一次管五年"**——勘测预测不了未来的使用模式、扩容和外部干扰。

---

> 由 cangjie-skill 流水线从 DT00XTE368EN 蒸馏生成。
