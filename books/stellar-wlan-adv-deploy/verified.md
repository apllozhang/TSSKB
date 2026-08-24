# verified · 三重验证通过条目（stellar-wlan-adv-deploy / DT00XTE361）

## 汇总

| 类型 | 候选 | 通过 | 淘汰 | 说明 |
|---|---|---|---|---|
| frameworks | 12 | 11 | 1 | f12（Guest Tunnel 附录）V1 不通过 |
| principles | 24 | 23 | 1 | p19（实验室凭据）V2 不通过 |
| cases | 13 | 13 | 0 | — |
| counter-examples | 13 | 13 | 0 | ce12 引文措辞需按原文修正 |
| glossary | 60 | 60 | 0 | 免验保留 |
| **合计** | **122** | **120** | **2** | 通过率 98.4%（除 glossary 外 62 条中 60 条，96.8%） |

验证方式：剥离空字节后对 fulltext.md 逐条抽查 source_quote 特征片段（约 60 组关键词全部 grep 定位到原文行号，含 QoE 四阈值、Mesh 限制、WMM 映射表、漫游失败三判据、athXYY、signalStrengthThreshold、Tx-Power=3dBm 等）。淘汰明细见 rejected/ 目录。

---

## frameworks（11 条通过）

- **f01 QoE 分析六指标体系**（p125-129, p158）
  - V1："six metrics to be monitored" 命中原文；V2：六指标+失败分类器是监控分析的核心模型；V3：OmniVista Cirrus 专属指标体系，非常识。
- **f02 QoE 仪表盘分析流程**（p125-126）
  - V1："QOE DASHBOARD" 命中（原文 9 处）；V2：过滤→阈值→摘要→下钻的标准操作路径；V3：产品专属工作流。
- **f03 网络分析工作流**（p138-145）
  - V1：Channel Distribution/Utilization 等要素在原文对应页命中；V2：信道→设备健康→端口级下钻可操作；V3：产品专属。
- **f04 客户端分析工作流**（p147-153）
  - V1：CLIENT ANALYTICS 系列组件名命中；V2：五维度分析+加 AP/换型号判断依据；V3：产品专属。
- **f05 有线客户端 MAC 认证四步配置流程**（p90-95）
  - V1：示例 MAC 11:22:33:44:55:66 命中原文 3 处；V2：完整可复用配置流程；V3：ARP/UPAM 体系专属。
- **f06 Mesh/Bridge 配置与监控流程**（p118-120）
  - V1："Is Root"（3 处）、"Mesh Topology"（3 处）命中；V2：Mesh/Bridge 配置属规则明确认可的价值类型；V3：产品专属路径。
- **f07 设备运维工作流**（p224-236）
  - V1："Scheduled Upgrades"（原文 4540/4996 行）、Collect Support Info 命中；V2：升级/备份/排障/支持信息四大运维抓手；V3：产品专属。
- **f08 全流程部署综合演练**（p286-299）
  - V1："The purpose of this exercise is to practice on Stellar Access Points..." 命中（5880 行）；V2：交付 checklist 含大量具体参数（-50dBm 门限、限 1Mbit/s、阈值组）；V3：训练场景独有整合。
- **f09 VoWLAN 部署五阶段流程**（p305-311）
  - V1：255 m²/20-25 users/36 Mbps/-62dBm 等关键常数全部命中；V2：容量与漫游规划常数可直接套用；V3：语音无线专属规划体系。
- **f10 组织清理流程**（p313-319）
  - V1："it is not possible to revert the configuration back to the default" 命中（6666 行）；V2：云管逆向拆除顺序可操作；V3："云管无一键恢复"及其对策非常识。
- **f11 无线/客户端排障 CLI 检查清单**（p260-274）
  - V1：iwconfig/sta_list/kes_syslog/wam.log/athXYY 全部在原文对应页命中；V2：CLI 命令级排障清单；V3：Stellar AP 专属命令体系。

## principles（23 条通过）

- **p01 Time To Connect 阈值 2-20s 默认 2s**（p158）— V1：原文 3215 行逐字命中；V2/V3：QoE 阈值参数。
- **p02 Roaming 阈值 0.2-2s 默认 0.2s**（p158）— V1：3224 行命中；V2/V3：同上。
- **p03 Coverage 阈值 -90~-55dBm 默认 -66dBm**（p158）— V1：3233 行命中；V2/V3：同上。
- **p04 Available Capacity 阈值 10%-50% 默认 10%**（p158）— V1：3240 行命中；V2/V3：同上。
- **p05 WMM 四类推荐 DSCP/802.1p 映射**（p80-81）— V1：原文 2248-2262 行推荐表逐项命中（"18 - AF 21"带空格，grep "AF21" 不中属格式差异，内容属实）；V2/V3：QoS 映射表。
- **p06 广播密钥轮换默认 15 分钟**（p78）— V1："15 min" 命中；V2/V3：GTK 安全参数。
- **p07 组播优化两个自动停用上限（90%/6 客户端）**（p79）— V1：multicast optimization 5 处命中；V2/V3：非显而易见的自动行为。
- **p08 WiFi4EU 会话超时可配至 12 小时**（p82）— V1：2289 行逐字命中；V2/V3：欧盟公共 Wi-Fi 计划专属要求。
- **p09 Mesh 容量限制与最佳实践**（p114-115）— V1：2805-2812 行六条限制+最佳实践逐字命中；V2/V3：硬性限制与"信道>100"实践，Mesh 价值类型。
- **p10 Bridge/Mesh 三要素两端必须一致**（p114-115）— V1："Must be the same on both APs" 6 处命中；V2/V3：建链硬规则。
- **p11 IoT 设备识别：MAC OUI + DHCP 指纹（option 55/60）**（p103）— V1："DHCP FingerPrinting" 命中；V2/V3：IoT 价值类型。
- **p12 热力图最少 3 台 AP**（p177）— V1：3496 行逐字命中；V2/V3：部署前置条件。
- **p13 排障前先做 NTP 全网时间同步**（p191）— V1："Synchronize all equipment" 命中；V2：排障前置动作；V3：跨设备日志关联的实战铁律。
- **p14 AP 串口参数 115200 8N1**（p192）— V1："115 200" 命中；V2：串口连接直接可用；V3：产品专属参数+默认账号。
- **p15 VoWLAN 信号标准 RSSI≥-67dBm（值29）/SNR≥25**（p272-273）— V1：5494 行逐字命中；V2/V3：语音无线量化标准+RSSI 换算表。
- **p16 VoWLAN 规划常数（-62dBm/20-25用户/1AP每255m²）**（p307-308）— V1：6489-6509 行逐字命中；V2/V3：可直接套用的规划常数。
- **p17 升级必然重启且终端断连**（p253）— V1："will be disconnected" 命中；V2：变更影响评估+四步向导；V3：点破"升级=断线"的变更盲区。
- **p18 场景化监控阈值基准（70%/20%/90%/25%）**（p298）— V1：6306 行等命中；V2/V3：阈值对齐业务用途的方法论与实例。
- **p20 漫游失败三大原因判据**（p264）— V1：5344 行起三条逐字命中；V2/V3：排障判据，含 untagged/tagged 不能漫游这类冷知识。
- **p21 拓扑状态颜色语义**（p247-248）— V1：Green/Orange/Red/Blue/Solid-Grey 条目命中；V2：读图即判态；V3：产品专属色约定。
- **p22 无线接口命名 athXYY**（p260）— V1：命中；V2：CLI 解读直接可用；V3：产品命名规则。
- **p23 Captive Portal 首连时序**（p220）— V1："Redirection URL" 命中；V2/V3：门户打不开的排查顺序依据。
- **p24 抓包两条路径（br-wan tcpdump / AP Web 空口抓包）**（p238-240）— V1："br-wan"、tcpdump 命中；V2/V3：具体命令+产品专属接口名。

## cases（13 条全部通过）

- **c01 远程实验室连接与环境发现**（p35-42）— V1："three-tier end user topology" 命中；V2：Lab 属认可价值；V3：POD 拓扑与"Hunting Group Busy"等环境细节。
- **c02 实验室复位与基础 WLAN 配置**（p43-73）— V1：reset_PODX、状态机序列命中；V2：从复位到双 SSID 验证的完整上线链路（Lab）。
- **c03 AP 有线口 MAC 认证示例**（p89-98）— V1：示例 MAC 命中；V2：f05 的实操版（Lab）。
- **c04 Mesh/Bridge 配置**（p117-121）— V1：Stellar-MESH/Is Root/Mesh Topology 命中；V2：Mesh 配置+Auto Mesh 免配置组网（Lab/配置价值类型）。
- **c05 QoE、网络与客户端分析实操**（p156-163）— V1：命中；V2：三大分析模块操作路径（Lab）。
- **c06 监控（客户端、访问记录与报表）**（p183-187）— V1：Create Report/Analytics Data Report 命中；V2：监控+报表操作（Lab）。
- **c07 设备目录与拓扑**（p242-249）— V1：拓扑应用描述命中；V2：Actions 全集与拓扑用法（Lab）。
- **c08 AP 运维五件套**（p250-257）— V1：Device Troubleshooting/setDateTime 命中；V2：升级/事件/支持信息/告警/远程命令（Lab）。
- **c09 全流程部署综合演练**（p286-299）— V1：与 f08 同源命中；V2：交付考核 checklist（Lab）。
- **c10 组织清理**（p313-319）— V1：与 f10 同源命中；V2：29 步逆向拆除+依赖报错处理（Lab）。
- **c11 排障用例：看不到 SSID**（p276）— V1："3) Country Code of the AP?" 命中（5637 行）；V2/V3：国家码三问+信道规避法。
- **c12 排障用例：拿不到 IP/掉线/802.1X 失败**（p277-284）— V1：Final_role filter DHCP（5667 行）、Tx-Power、aaaProfile（5790 行）命中；V2/V3：三段对照排障法+真实案例参数。
- **c13 排障用例：高 CPU 与僵尸进程**（p214-217）— V1：drm 进程 81%、Zombie 命中；V2/V3：top/ps 判读与进程状态语义。

## counter-examples（13 条全部通过）

- **ce01 复位中按键掉进 Miniboot**（p46）— V1："press any key during the reset"/Miniboot 命中；V2/V3：操作禁忌。
- **ce02 误删云管组织不可恢复**（p47）— V1："Delete on your Organization" 命中；V2/V3：毁灭性操作警告。
- **ce03 树莓派有线网卡不能动**（p41）— V1：命中；V2：Lab 环境实操禁忌（Lab 属认可价值）；V3：环境专属。
- **ce04 预置设备不得管理配置**（p38, p291）— V1：DO NOT MANAGE/ MODIFY 命中；V2/V3：变更边界。
- **ce05 untagged/tagged VLAN 间不能漫游**（p264）— V1：5344 行命中；V2/V3：漫游静默失败根因，非常识。
- **ce06 RSSI 门限过高主动踢客户端**（p281）— V1：signalStrengthThreshold:70 命中（4 处）；V2/V3：真实案例参数。
- **ce07 发射功率压到最小致弱信号掉线**（p279-280）— V1：Tx-Power=3dBm 案例命中；V2/V3：真实案例。
- **ce08 僵尸进程吃光内存**（p217）— V1：命中；V2/V3：X/Z 状态判读。
- **ce09 Portal 无 IP 时重定向必失败**（p220）— V1：命中；V2/V3：先查 IP 再查门户的排障顺序。
- **ce10 老款 AP 桥接不支持 VLAN 打标**（p113）— V1："VLAN tagging over a bridge" 逐字命中；V2/V3：选型限制，冷知识。
- **ce11 国家码不匹配致 SSID 不可见**（p276）— V1："Wrong country code" 命中；V2/V3：现象与根因错位的典型案例。
- **ce12 训练环境勿真执行升级计划**（p252）— V1：命中（原文为小写 "do not complete this upgrade process"，候选引文系大写改写，**后续蒸馏时引文应修正为原文措辞**）；V2/V3：演练/生产变更控制。
- **ce13 云管删除有依赖顺序**（p316）— V1："only be deleted if no custom provisioning" 命中；V2/V3：清理报错的真实解法。

## glossary（60 条，免验保留）

按流水线规则 glossary 不执行三重验证，60 条整体保留，进入下一阶段。

---

### 遗留事项（供阶段 2 处理）

1. ce12 引文措辞与原文有出入（大写改写），蒸馏时修正为原文 "Use this section only as a configuration guide, and do not complete this upgrade process."
2. f12（Guest Tunnel 附录）被淘汰，若后续拿到可读的原版 PDF 附录，可重新候选。
