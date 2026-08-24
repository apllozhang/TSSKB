# 验证通过条目 · OmniAccess Stellar WLAN Express (DT00XTE455EN)

> 阶段 1.5 三重验证结果：V1 原文真实性（quote 抽查在 source/fulltext.md 对应页命中）、V2 可操作价值（集群规则/默认值/排障案例）、V3 独特性（非常识）。
> 验证日期：2026-08-23。原文抽查范围：全部 65 条候选（frameworks 10 + principles 26 + cases 14 + counter-examples 15）的 source_quote 逐条与 fulltext.md 比对；glossary 36 条按规则免验保留。

## 汇总

| 类型 | 候选 | 通过 | 淘汰 | 通过率 |
|---|---|---|---|---|
| frameworks | 10 | 10 | 0 | 100% |
| principles | 26 | 25 | 1 (p25) | 96% |
| cases | 14 | 12 | 2 (c01, c02) | 86% |
| counter-examples | 15 | 14 | 1 (ce12) | 93% |
| glossary（免验） | 36 | 36 | 0 | — |
| **合计** | **101** | **97** | **4** | **96%** |

淘汰明细见 `rejected/` 目录（frameworks.md 为空说明、principles.md、cases.md、counter-examples.md）。

---

## 框架/流程（10/10 通过）

### f01 集群角色模型与 PVM/SVM 选举流程
- V1: quote 在 p79-80 命中（PVM/SVM/Member 定义、Highest Model Type/Highest MAC 选举、mywifi-0102、255 上限均在）。
- V2: 排障第一步"先确认谁是 PVM/SVM"直接可用。
- V3: 选举判据（先型号后 MAC）为 Stellar 专有规则。

### f02 集群扩展与分域设计流程（Group ID/VLAN 隔离 + 单 IP 管理）
- V1: quote 由 p81/p83/p84 三页原文拼合，各片段均逐字命中。
- V2: 超 255 台拆分法与 Group Mgt IP 单入口是 Express 规划的核心操作指南。
- V3: "一 VLAN 一 Group ID"映射是产品专有设计法。

### f03 AP 开箱到首次配置上线的六步流程
- V1: 六步标题在 p57-62 逐页命中。
- V2: 含默认 IP 192.168.1.254 兜底、出厂 SSID mywifi 等具体入口。
- V3: 弱项在流程本身偏通用，但 mywifi/默认 IP 等 Stellar 专属细节保住了独特性。通过。

### f04 WiFi Bridge 点对点部署流程（四属性一致 + 单根原则）
- V1: p113 四属性逐字命中，p112 示例参数（STELLAR-BRIDGE/5GHz/ALCATEL123!）命中。
- V2: 可直接照抄的配置清单。
- V3: "三同一根"为产品规则。

### f05 WiFi Mesh 部署与 Auto Mesh 快速建网流程
- V1: p114-115 命中（AUTO MESH 行为、隐藏 SSID Stellar-MESH、5GHz）。
- V2: "通电即入网"部署法 + 回程最佳实践。
- V3: 隐藏 SSID 名与自动非根行为为产品专有。

### f06 三种部署模式选型框架（Express/Enterprise/Cloud）
- V1: p40/p42/p44 三页特性逐字命中。
- V2: 选型决策（255/4000 分界、管理面差异）直接可用。
- V3: 具体上限与平台对应关系为产品事实。

### f07 勘测类型选择框架（预测/被动/主动 × 部署前后）
- V1: p164-165 命中（三类勘测定义 + 阶段映射）。
- V2: 项目阶段→勘测类型的映射是明确决策规则。
- V3: 勘测分类属行业半常识，但"哪阶段用哪类"的映射保留了操作价值。通过（V3 边缘，建议保留）。

### f08 现场勘测排障三步流程（平面图→现场观测→纠正措施）
- V1: p172-175 命中（Step1/2/3 全部要点）。
- V2: "WiFi 表现不佳"工单的标准作业流程。
- V3: 观测五问（型号一致/RF 重叠/无覆盖/功率默认与否/位置）是教材独有的 SOP。

### f09 排障案例三级分类体系（AP 侧/客户端侧/性能侧 × 15 案例）
- V1: p126-160 各案例标题逐条命中。
- V2: 接单先归域再套案例的索引结构。
- V3: 教材自有的分类骨架。

### f10 集群维护与远程管理操作框架
- V1: p85-86 命中（MAINTENANCE 四项、REMOTE CLUSTER MANAGEMENT 三点、get/set），p88 "JOIN A CLUSTER" 在。
- V2: 远程管理前提（防火墙放行）与例外（镜像升级）影响运维计划。
- V3: 产品专有管理架构。

---

## 原则/参数（25/26 通过）

### p01 Express 集群规模硬上限 255 台，第 256 台不纳管
- V1: p81 逐字命中（含 "The 256th AP is not taken into account and will stay in 'joining' mode"）。
- V2: 规模规划硬约束。V3: 静默失效行为非常识。

### p02 PVM 选举规则：先比最高型号，再比最高 MAC
- V1: p80 逐字命中。
- 注意：summary 引 p82 型号清单写作 "1351"，原文 p82 为 "1350"（疑似教材笔误，型号谱系中实际是 AP1351）。引用时按原文 "1350" 标注。不影响通过。
- V2/V3: 混合组网预判管理节点的规则。通过。

### p03 集群之间不做 L2/L3 漫游
- V1: p81 "Limitations: No Layer 3 Roaming. No Layer 2 Roaming between clusters." 命中。
- V2/V3: 多集群设计的能力边界。通过。与 ce02 同源不同视角（原则 vs 陷阱），保留双条。

### p04 集群实际 AP 上限随在网型号而变（32/64/255）
- V1: p138 逐字命中。V2: 入组排障检查点。V3: 混入低端型号拉低整组上限是隐蔽规则。通过。

### p05 集群通过单一 Group Mgt IP 完成同步与管理
- V1: p84 逐字命中。V2/V3: 通过。

### p06 远程集群管理的边界：防火墙放行组管理 IP，不支持远程镜像升级
- V1: p86 逐字命中。V2/V3: 通过。与 ce08 同源，保留双条。

### p07 Bridge 四属性配置原则：三同 + 单根
- V1: p113 逐字命中。V2/V3: 通过。

### p08 Mesh 允许多根，且节点可同时服务客户端
- V1: p114（Multiple APs can be defined as root）与 p112（Mesh properties）均命中。V2/V3: Bridge/Mesh 选型判据。通过。

### p09 Mesh/Bridge 回程最佳实践：5GHz（或 6GHz）、信道大于 100
- V1: p113/p114 两处 "WIFI MESH – BEST PRACTICE" 逐字命中。V2/V3: 直接套用的参数。通过。

### p10 Auto Mesh 默认参数：隐藏 SSID "Stellar-MESH"、5GHz、非 LAN 即非根
- V1: p115 逐字命中。V2/V3: 通过。与 c05/f05 同源，视角不同，保留。

### p11 Enterprise/Cloud 模式统一 4000 台上限，Cloud 功能等同 OV2500
- V1: p42/p44 逐字命中。V2/V3: 迁出 Express 的规模基线。通过。

### p12 AP 供电规格：最大 12W、48V DC、DC 与 PoE 双源时 DC 优先
- V1: p128 逐字命中。V2/V3: 供电排障基准。通过。

### p13 AP LED 状态判读表（颜色×闪烁=九种状态）
- V1: p128 LED 表逐行命中。V2/V3: 通过。

### p14 AP 出厂默认管理 IP 192.168.1.254
- V1: p129 逐字命中。V2/V3: 救援入口。通过。

### p15 Console 串口参数固定 115200-8-N-1
- V1: p130 逐字命中。V2/V3: 通过。

### p16 集群通信端口：32767 承载 PVM 报文，32768 承载 AP→PVM 报文
- V1: p137/p138 tcpdump 命令逐字命中。V2/V3: 防火墙放行与抓包排障硬参数。通过。

### p17 AP 默认发射功率 17dBm，覆盖不足时应上调
- V1: p174 逐字命中。V2/V3: 通过。

### p18 信号衰减实测基准：4 米穿 1-4 堵墙后 RSSI 跌到 -70dBm，不够 VoWLAN
- V1: p168 逐字命中（含材质清单）。V2/V3: 覆盖解释的量化基准。通过。

### p19 天线选型原则：按覆盖形状选定向或全向
- V1: p169 命中；quote 中 "No [large] Area covered" 的括号补正合理——原文 OCR 为 "No Area covered"，按幻灯片语义应为 Large（定向=Small Area 对照）。通过（引用时建议沿用括号标注）。

### p21 低吞吐/高时延五查清单（限速→协商速率→ACS→干扰→ISP）
- V1: p155 逐字命中。V2: 由近及远的检查顺序。V3: 含 ACS 开关等具体动作。通过。

### p22 覆盖优化五招与"删低速率逼终端贴近 AP"
- V1: p175 逐字命中。V2/V3: "删低速率"反直觉但有效。通过。

### p23 AP 型号规格选型基线（SSID 数/客户端数/端口与 PoE 分档）
- V1: AP1301（p14）与 AP1451（p23）两段引文逐字命中；summary 的三档归纳与 p13-25 各页参数一致。V2/V3: 选型分档规律。通过。

### p24 外置天线型号命名规则：尾数 2；全系标配内置全向天线
- V1: p30 逐字命中。V2/V3: 通过。

### p26 Express 模式内置能力清单（安全/射频/系统三组关键项）
- V1: p41 各要点逐字命中（255/802.1X/WPA3/WIPS/DFS/TPC/DHCP-DNS-NAT/MESH/证书等）。V2: 售前答疑直接引用。V3: 通过。

---

## 案例（12/14 通过）

### c03 配置实例：跨街楼宇 WiFi Bridge 点对点回程
- V1: p112-113 全部参数（STELLAR-BRIDGE/5GHz/YES/NO/ALCATEL123!）逐字命中。V2: 可照抄实例。V3: 通过。

### c04 配置实例：营地覆盖 WiFi Mesh（回程+访客双 SSID）
- V1: p112（camping 用例）+ p114（WIFI GUESTS/STELLAR-MESH 两端参数）逐字命中。V2/V3: 业务/回程 SSID 分离的完整写法。通过。

### c05 部署场景：Auto Mesh 通电即入网
- V1: p115 逐字命中。V2: 快速部署场景。V3: 通过（与 f05/p10 同源，后续组稿时可合并引用）。

### c06 排障案例 1：AP 无法上电（LED 判读法）
- V1: p128 逐字命中。V2/V3: 通过。

### c07 排障案例 2：AP 从 DHCP 拿不到 IP（三步递进）
- V1: p129-132 三步（192.168.1.254 → Console 115200 → tcpdump/pcap）逐字命中。V2/V3: 通过。

### c08 排障案例 4：AP 无法加入集群（四查）
- V1: p136-138 逐字命中（cluster_mgt –x show=self、joining 手工批准、32/64/255）。V2/V3: 通过。

### c09 排障案例 5：802.1X 认证失败（用户/AP/服务器三侧排查）
- V1: p140-141 逐字命中（tools-ping、RADIUS client 配置四项）。V2/V3: 通过。

### c10 排障案例 6：连上 Guest SSID 后 Portal 页面不弹出
- V1: p142-143 逐字命中（Portal 开关、白名单/walled garden、https 限制、ps | grep eag）。V2/V3: 通过。

### c11 排障案例 7：客户端拿不到 IP（抓包定位 VLAN 与信道错配）
- V1: p144-147 逐字命中（VLAN ID、静态 IP、beacon 信道比对）。V2/V3: 通过。

### c12 排障案例 8：客户端连不上 AP/集群（黑名单与 MaxClients）
- V1: p148-150 逐字命中（blocklist 红叉、MaxClients、wam 进程重建、kes_syslog）。V2/V3: 通过。

### c13 排障案例 11：低吞吐/高时延五查与案例 12 端口错误
- V1: p155-156 逐字命中。V2/V3: 通过（与 p21 同源，案例版含 ethtool 端口三板斧）。

### c14 勘测实例：五点标注的现场整改（AP1511 部署）
- V1: p173-174 逐字命中（AP1511、五点标注、17dBm）。V2/V3: 通过。

---

## 陷阱/警告（14/15 通过）

### ce01 陷阱：第 256 台 AP 静默失效——不停 joining、不被纳管
- V1: p81 逐字命中。V2/V3: 静默失效+误判风险。通过（与 p01 同源，陷阱视角独立保留）。

### ce02 陷阱：跨集群漫游落空——L2/L3 都不支持
- V1: p81 逐字命中。V2/V3: 移动场景设计陷阱。通过（与 p03 同源，保留双条）。

### ce03 兼容性警告：AP1101/AP1201/AP1201H 桥接不支持 VLAN 标签
- V1: p112 星号脚注逐字命中。V2/V3: 型号兼容性硬限制。通过。

### ce04 误用警告：拿 WiFi Bridge 当覆盖用——桥上不能服务客户端
- V1: p112 "Cannot provide service (WiFi) to WiFi clients"（Bridge）/ "Can provide..."（Mesh）逐字命中。V2/V3: 通过。

### ce05 限制清单：Mesh 网络四条硬上限（4 跳/单跳 5 台/全网 16 台/仅 5 个 SSID）
- V1: p114 逐字命中。V2/V3: Mesh 规模红线。通过。

### ce06 行为例外：客户端访问 https URL 不会被重定向到内置 Portal
- V1: p143 逐字命中。V2/V3: 已知产品限制+处置动作。通过。

### ce07 行为例外：白名单/walled garden 命中的客户端不弹 Portal
- V1: p143 逐字命中。V2/V3: "正常的不弹页"，可反向利用。通过。

### ce08 管理边界：远程集群管理做不了 AP Group 镜像升级
- V1: p86 逐字命中。V2/V3: 通过（与 p06 同源，保留双条）。

### ce09 排障清单：PoE 不供电的五个常见原因（线长超 100m 居首）
- V1: p157 逐字命中；原文 "802.3af or 802.3af" 确为教材笔误，候选已如实引用并加注。V2/V3: 施工侧五查清单。通过。

### ce10 部署错误：AP 装在障碍物正前方，墙后出现死角
- V1: p167 逐字命中。V2/V3: 通过。

### ce11 选型错误：天线类型与覆盖需求不匹配
- V1: p169 命中；quote 中 "[Large]" 为对原文 OCR "No Area covered" 的合理补正（与定向 "Small Area covered" 对照）。通过（沿用括号标注）。

### ce13 账户陷阱：Portal 用户有效期过期即失效、从账户列表消失
- V1: p151 逐字命中。V2/V3: 通过。

### ce14 容量陷阱：客户端数顶到 MaxClients 上限后拒绝新连接
- V1: p149 逐字命中。V2/V3: 通过（与 c12 同源，陷阱视角保留）。

### ce15 配置残留：AP 的 option proto 停在 static 导致拿不到 DHCP 地址
- V1: p131 逐字命中（cat /etc/config/network、ifconfig br-wan、改回 DHCP）。V2/V3: Console 救援路径。通过。

---

## 术语表（36/36 免验保留）

g01-g36 全部按流水线规则免三重验证，整组保留。内容与原文术语一致（PVM/SVM/Group Mgt IP/Auto Mesh/EAG/walled garden/ACS/DRM 等）。

---

## 验证备注（供阶段 2 参考）

1. **同源多视角对**：p01/ce01、p03/ce02、p06/ce08、p10/f05/c05、p21/c13、p22/f08——均为"原则 + 陷阱/案例"双视角，组稿时可互链但不必删并。
2. **两处原文笔误需在引用时保留校注**：p82 型号清单 "1350"（应为 AP1351）；p157 "802.3af or 802.3af"（应为 af/at）。
3. **两处 OCR 补正**：p169 全向天线 "No [Large] Area covered"，建议沿用候选的括号标注法。
4. **配置演示章（p66-75、p87-116 截图页）文字极薄**，c01/c02 已按 V2/V3 淘汰，阶段 2 不再从该区域补采文字型单元。
