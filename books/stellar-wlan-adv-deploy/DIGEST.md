# DIGEST · Stellar WLAN 进阶部署与云管运维（DT00XTE361EN）精华版

> 不读全书、只看精华。这是 ALE 培训教材 OmniAccess Stellar WLAN Advanced Deployment with OmniVista（330 页）的蒸馏长文：QoE 六指标、云管运维四件套、有线/IoT 接入、全流程交付清单、CLI 排障速查，一次读完即可上手。

## 一、一页看懂这门课

这本教材（DT00XTE361EN）是 T360（Stellar WLAN 基础部署）的进阶续集，面向售后新人，讲 Cirrus 云管环境下的三件事：

1. **高级功能**（DAY 1 前半，p3-121）：SSID 高级选项（QoS/密钥轮换/广播组播优化/访客门户）、有线客户端 MAC 认证、IoT 设备识别、Bridge 点对点桥接与 Mesh 无线回传。
2. **可观测性**（p125-187）：QoE Analytics、网络分析、客户端分析三层仪表盘——这是 Cirrus 的卖点，也是交付后的运维抓手。
3. **运维与排障**（DAY 2，p258-319）：监控告警、设备生命周期（升级/备份/支持信息）、进阶 CLI 排障、全流程部署综合演练、VoWLAN 规划、组织清理。

一句话主线：**云管环境下的可观测性与运维**。分析告诉你问题在哪，监控让问题主动找你，CLI 排障把问题钉死在设备层，综合演练把 T360+T361 的全部技能串成一条可复用的交付流程。

## 二、QoE 分析六指标详解

QoE（体验质量）从终端视角回答"用户体验好不好"。Cirrus 提供六个监控指标（p158）：

| 指标 | 含义 | 阈值范围 | 默认值 |
|---|---|---|---|
| Successful Connects | 成功连接数 | 计数器，无阈值 | — |
| Time To Connect | 关联/授权/DHCP/Portal 四阶段总耗时 | 2-20s | 2s |
| Roaming | 漫游成功率 | 0.2-2s | 0.2s |
| Coverage | 信号高于阈值的时间占比 | -90 ~ -55dBm | -66dBm |
| Available Capacity | RF 信道可用时间占比 | 10%-50% | 10% |
| Device Uptime | 设备在线率 | — | — |

工作流（p156-163）：Network > Analytics > QoE → Filters 选站点与时间范围（建议先 Last 7 days）→ Summary 圈定异常指标 → 点 More details 看失败分类器（DHCP、Association、Weak Signal、上下行不对称、Wi-Fi 干扰等），按连接模式/设备类型/OS/SSID 的失败会话明细定位原因。

配套两层：**网络分析**（p138）看信道分布与利用率、AP/交换机 CPU/内存/闪存健康；**客户端分析**（p147）看连接曲线、频段/AP 分布、吞吐，判断要不要加 AP。三个坑：失败分类器要有失败样本才显示，时间窗太短会"看不到问题"；交换机只有 Device Uptime 一项 QoE 指标；阈值按站点配置，多站点不能一刀切。

## 三、云管运维四件套

设备进入运维期后，日常抓手就四样（p233-257）：

1. **监控**：拓扑状态色扫一遍——绿=正常、橙=未知或 warning/major、红=critical（但连通仍在）、灰=失联（别把红读成断网）；Network Events 按 AP/Switch/QoE 三类 trap 浏览、按 Severity 过滤、逐条 Acknowledge。
2. **热力图**：按站点/AP 生成，硬性前提**至少 3 台 Stellar AP**（p177）；密度红/黄/绿对应高/中/低，用来核对覆盖与客户端分布。
3. **设备目录**（Device Catalog）：所有 Actions 的入口——Edit Device、SSH/Web UI（需先在 Provisioning 启用并设凭据）、Configuration Management、下发排障命令（Device Troubleshooting）、Collect Support Info 收日志包（AP 为 tar.gz 快照；交换机 swlog/cfg/Tech Support 分 L2/L3/Engineering 层级）。
4. **升级与备份**：升级四步向导（Schedule Setting → 选设备 → 定版本 → Review），默认 6 小时窗口——**升级等于重启、终端必断连**，必须纳入变更通知；配置备份可含安全文件，按交换机/站点/楼层排程。再加报表排程（如周一 8:00 周报，邮件自动送达）。

这四件套把整套 skill 串起来：监控发现问题 → QoE 分析定位 → 设备目录取证/下命令 → 仍不明确才登 AP 走 CLI；而升级备份和报表是例行动作。

## 四、有线与 IoT 接入要点

**有线客户端 MAC 认证**（p89-98）：哑终端（打印机/摄像头/POS）接 AP 有线口（如 Eth1）做准入。认证链四步：AAA Server Profile（内置 UPAMRadiusServer，用途选 MAC）→ Access Auth Profile（方法 MAC、默认角色 ARP_DEFAULT 受限+限带宽、应用到 AP 组与端口）→ Access Policy（认证源 Local Database、通过角色 ARP_PASS）→ 本地数据库录入 MAC。验证看 Device Catalog > Wired Ports 与 Analytics > Clients。

**IoT 双识别**（p103）：MAC OUI（厂商前缀）+ DHCP 指纹（option 55 参数请求列表 + option 60 厂商标识）；识别分类可绑定 Access Role Profile 自动强制。两个坑：静态 IP 哑终端不发 DHCP，只能靠 OUI；误分类绑定强制会直接断业务，先小范围验证。

**Mesh/Bridge**（p113-121）：跨楼无线桥接或回传组网。建链三要素——SSID、频段、密码两端完全一致；容量红线：全网 ≤16 AP、每 Root ≤8 从 AP、≤4 跳、单跳点对多点 ≤5 AP；回传用 5GHz、信道选 100 以上。AP1101/AP1201/AP1201H 桥上不支持 VLAN 打标，选型就要排除。

## 五、全流程部署演练清单（当交付 checklist 用）

综合演练 Lab（p286-299）把全书技能串成七段主线，交付照此打勾：

1. **复位与连通验证**：复位设备，ping DHCP 服务器与外网。
2. **组织建模**：Organization > Site（含预留站点）> Building > Floor，楼层挂平面图；设备必须归属站点。
3. **设备上线**：show chassis 取序列号逐台入目录，等 OV Managed 状态；非云管型号（如 OS-2360）只能手工配。
4. **WLAN**：三个差异化 SSID——EmployeesX（WPA2-Enterprise 802.1X、仅 5GHz、VLAN 20、按角色封 HTTP）、GuestsX（内部门户、限 1Mbit/s、客户端隔离、VLAN 30、账号限时限量）、PrinterX（仅 2.4GHz、最小功率、固定信道、DPSK 按设备 PSK）；RF Profile 开 Band Steering/Load Balance、关联门限 -50dBm。
5. **安全**：WIPS 流氓 AP 分类规则（同 SSID 名+指定 MAC OUI）、认证失败黑名单（5 次/分钟）、关闭 AP SSH/Web 管理。
6. **运维**：Golden Config、配置备份、VLAN 模板变量化、标签、周报排程、场景化阈值（健康 70%、2.4G 利用率 20%、客户端健康 90%、可用容量 25%）。
7. **拓扑变更**：按需把两台 AP 改 Mesh（AP1321 为 Root、WPA2-Personal），全量回归验证。

**清理是逆向拆除**（p313-319）：云管没有一键恢复默认（p315 明说），按创建反序删——运行任务 → WIPS → AP 组/Profile 解绑（删不掉先把引用改回 Default）→ SSID → 策略/门户 → 账号 → Golden Config → 报表 → 阈值 → 站点 → 确认设备目录空。误删 Organization 不可恢复。

## 六、CLI 排障速查

前置铁律：**先 NTP 全网同步**，否则跨设备日志对不上时间戳。接入：SSH（Provisioning 启用）或串口 115200 8N1（support/aos2016）。四大用例（p260-284）：

| 用例 | 命令与判据 |
|---|---|
| 看不到 SSID | `iwconfig` 三问：SSID 在目标射频广播？频段兼容？国家码被客户端支持？（国家码错可在 RF Profile 手工指定兼容信道规避）接口 athXYY：X=0/1/2 对应 2.4/5/6GHz |
| 拿不到 IP | `ssudo sta_list` 核对 VLAN/Final_role；`ssudo tcpdump -i br-wan -w test.pcap udp port 53` 双侧对照 DHCP 丢在哪侧 |
| 频繁掉线 | `iwlist txpower`（案例压到 3dBm）；查 rfprofile.conf 的 signalStrengthThreshold（案例 70 过高主动踢弱信号客户端）；空口抓包看去关联帧 |
| 802.1X 失败 | 客户端（账号/证书）↔ AP（AAA_server.conf 的 IP/端口/共享密钥）↔ RADIUS（用户库/NAS IP/1812、1813 放行）三段对照 |

漫游失败三判据（p264）：AP 互为邻居、untagged 与 tagged VLAN 之间**不能**漫游（静默失败）、源/目标 AP 间 RSSI 过低。用 `adme show` 看邻居、wam.log 搜 roaming。RSSI 读数换算：29≈-67dBm、20≈-76dBm、10≈-86dBm。

## 七、学习路径与陷阱

**路径**：先过 SSID 高级选项与有线/IoT 接入（配得进去）→ 再学 QoE/网络/客户端三层分析（看得懂）→ 然后监控四件套（管得住）→ 最后 CLI 排障与综合演练（修得了、交付得出）；VoWLAN 五阶段（Prepare/Plan/Design/Implement/Operate，p306）作为专项规划方法，需要时直接套常数：1 AP/255m²、每 AP 20-25 用户保 36Mbps、802.11ac 语音门槛 RSSI ≥ -67dBm（读数 ≥29）且 SNR ≥ 25、漫游重叠带按 -62dBm 留余量。

**高频陷阱清单**：升级必重启且终端断连；少于 3 台 AP 无热力图；组播优化"失效"多为自动停用（信道利用率 90% 或 6 个高吞吐客户端，是设计行为）；密钥轮换仅 Enterprise SSID 可用；门户首连 IP 为 0.0.0.0 发不出重定向是正常时序，先查 IP 再查门户；僵尸进程累积吃内存，发现后开票附进程清单别只重启；交换机重启阶段按键会掉进 Miniboot；语音标准（-67dBm）别错用到数据场景，会过度建设。

---
*由 cangjie-skill 流水线从 DT00XTE361EN 蒸馏生成。*
