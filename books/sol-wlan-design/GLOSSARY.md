# GLOSSARY · Stellar 高密设计 + 微调最佳实践 + 部署协助服务

> 页码为全册连续 `<<<PAGE N>>>` 标记。按高密设计/RF 管理/漫游与负载/组播广播/架构与运维/三级配置/服务分组，精选 48 条。

## 高密设计
- **HD / VHD**：High-density / Very-high density，体育场看台为 VHD 典型 <<<PAGE 5-6>>>
- **容量规划（Capacity planning）**：事件期并发客户端数与并发带宽测算 <<<PAGE 6>>>
- **预测勘测（Predictive survey）**：基于数字地图部署前预测点位与覆盖 <<<PAGE 7, 74>>>
- **30% 并发率**：连接人数占总观众比例的经验值 <<<PAGE 12>>>
- **AP 计数标准**：看台 120 终端/AP（150 座/AP）；其余 1 AP/100m² <<<PAGE 12>>>
- **25% VHD 折减系数**：体育场 VHD 场景扣 CCI/ACI/非 Wi-Fi 干扰/中等占空比的折减 <<<PAGE 11>>>
- **AP 型号-场景映射**：AP1360 户外/监控、AP1322 看台定向、AP1361D 猫道、AP1331/1351 媒体大厅、AP1311 办公 <<<PAGE 13>>>
- **扇区天线（Sector antenna）**：ANT-S-M4-30/60 定向天线，屋顶定向覆盖看台 <<<PAGE 17, 40>>>
- **NEMA 防护盒**：座椅下/猫道安装的防护外壳（IP3/IP4） <<<PAGE 13>>>
- **卫星机柜**：约每 3200 座一个，配 24 口交换机 <<<PAGE 17>>>
- **信道复用因子**：可用/已用信道之比，VHD 力争逼近 1，座椅部署最高 3 <<<PAGE 21>>>
- **LAN 带宽公式**：复用因子 × AP 数 × 每 AP 客户端 × 每客户端带宽，再 +50% 有线冗余 <<<PAGE 21>>>
- **QoE（体验质量）**：连接成功率/时长/漫游/容量可用性综合评分 <<<PAGE 25, 64>>>

## RF 管理与微调
- **CCI / ACI**：同频干扰 / 邻频干扰 <<<PAGE 8>>>
- **RDA / DRM**：Radio Dynamic Adjustment / Dynamic Radio Management，自动信道+功率调整 <<<PAGE 48, 56>>>
- **ACS / APC**：自动信道选择 / 自动功率控制 <<<PAGE 48>>>
- **背景扫描**：wIDS/wIPS/RDA 基础，默认开，间隔建议 <40s（>60s 损精度） <<<PAGE 49, 56>>>
- **Airtime Fairness**：空口时间公平，默认关、高密必开 <<<PAGE 8, 56>>>
- **专用扫描射频**：Wi-Fi 6 AP 独立全频扫描射频，工作信道不受影响 <<<PAGE 9>>>
- **DFS 信道**：与雷达等共用的频率（UNII-2e 100-140），看台高密优选 <<<PAGE 8, 26>>>
- **20MHz 基准带宽**：高密基准信道宽度，宽信道带来 CCI+3dB 噪声惩罚 <<<PAGE 8, 49>>>
- **信道利用率红线**：≥50% 即显著损害 WLAN 容量 <<<PAGE 52>>>
- **SSID 空口开销**：SSID 数×同信道 AP 数的 beacon/probe 开销；12AP×10SSID=50% <<<PAGE 53>>>
- **OFDMA / MU-MIMO / BSS Coloring**：Wi-Fi 6 高密三大利器 <<<PAGE 12, 51>>>
- **MCS**：调制编码方案；MCS8=256QAM 3/4，速率越高 SNR 要求越高 <<<PAGE 11, 49>>>
- **2x2:2 MIMO**：当前主流客户端天线配置 <<<PAGE 9>>>
- **信号强度基准表**：-67dBm 时敏（VoIP/视频）/ -70dBm 邮件网页 / -80dBm 最低连接不可靠 <<<PAGE 54>>>

## 负载均衡与漫游
- **Band Steering**：引导双频客户端优先 5GHz；Apple iOS 可能拉黑 SSID 数分钟 <<<PAGE 54, 66>>>
- **Force 5GHz**：拒绝全部 2.4G 关联，仅纯双频环境适用 <<<PAGE 54>>>
- **RSSI 阈值**：以 -96dBm 底噪换算；关联 22=-74dBm、漫游 25=-71dBm <<<PAGE 55, 66>>>
- **最低客户端数据速率**：低于门限拒绝关联；推荐 2.4G=12M、5G=24M <<<PAGE 10, 55>>>
- **最低管理帧速率（Minimum MGMT Rate）**：须 ≤ 关联最低数据速率 <<<PAGE 55, 71>>>
- **Sticky client（粘滞客户端）**：抱住信号变差的原始 AP 不漫游 <<<PAGE 57>>>
- **802.11k / 802.11v**：邻居报告 / BSS 过渡引导，解粘滞客户端正解；依赖客户端支持 <<<PAGE 57-58>>>
- **802.11r（Fast BSS Transition）+ OKC**：快速切换 + 机会性密钥缓存（复用 PMK）免完整 802.1X 重认证 <<<PAGE 57-58, 70>>>
- **FDB Update on Association**：漫游后 AP 发 ARP 通知交换机刷新转发表 <<<PAGE 30, 57>>>
- **Smart Load Balance（SLB）**：引导客户端去空闲 AP、拒弱信号关联的功能集；解决不了粘滞客户端 <<<PAGE 52, 58>>>
- **Dynamic Load Balance**：相邻 AP 间按客户端数分担 <<<PAGE 27, 66>>>

## 组播/广播/QoS
- **Multicast Optimization**：组播转单播，Number of Clients 默认 6 <<<PAGE 37, 59>>>
- **IGMP Snooping**：按组播成员端口定向转发 <<<PAGE 38, 59>>>
- **Broadcast Filter ARP / All**：AP 作 ARP 代理只发不播 / 丢弃除 DHCP/ARP 外全部广播 <<<PAGE 32, 60>>>
- **Broadcast Key Rotation**：广播密钥轮换（1-1440 分钟，默认 15） <<<PAGE 32, 59>>>
- **Bandwidth Contract**：SSID 级上/下行及突发带宽合约（0-2621440 Kbps） <<<PAGE 32, 72>>>
- **WMM / 802.1p / DSCP 映射**：AC_BK/BE/VI/VO 与有线 QoS 互转；Trust Original DSCP <<<PAGE 32, 63>>>
- **Voice and Video Awareness**：语音视频会话期间暂停背景扫描 <<<PAGE 61, 66>>>

## 架构、模式与运维
- **Enterprise / Express 模式**：OmniVista 集中（4000 AP/组） vs 集群自治（256 AP/集群） <<<PAGE 47>>>
- **OmniSwitch 6900 双核心**：40G 保底/100G 峰值、虚拟机箱、autofabric <<<PAGE 18-19>>>
- **OmniVista 2500 HA**：双数据库高可用 NMS，单机 4000 AP <<<PAGE 19, 22>>>
- **Captive Portal**：访客 Web 认证；OV2500 托管或第三方（UCOPIA ≥15,000 用户） <<<PAGE 19>>>
- **Custom Dashboard / 客户端密度图**：Cirrus 10 专区聚合仪表盘 / 密度可视化（10.4.1+） <<<PAGE 23-24>>>
- **DTIM Interval**：组播/广播传递指示，Apple 互通建议 3 <<<PAGE 71>>>
- **High Efficiency（HE）模式**：802.11ax 开关，关闭降级 VHT <<<PAGE 68>>>

## 三级配置与服务
- **RF Profile**：区域级——频段/信道计划（DRM/Channel List）/宽度/功率范围/信标/扫描 <<<PAGE 27-38, 66-72>>>
- **AP Group**：设备组级——SSH/SNMP/IGMP Snooping/日志上送 <<<PAGE 27-38>>>
- **SSID 级配置**：认证/最低速率/漫游（11r/k/v/OKC/FDB）/带宽合约/广播组播/QoS <<<PAGE 27-38>>>
- **Beacon Interval**：默认 100ms，极高负载可至 150ms <<<PAGE 29, 68>>>
- **部署协助服务（Deployment Assistance）**：预测勘测+现场勘测+辅导+培训+ACSE，5 天交付，PS-PAER-5-NET <<<PAGE 73-75>>>
- **ACFE / ACSE 认证 / HLD**：服务前置基础认证 / 完成后技术支持准入 / 订购前必须完成的高层设计 <<<PAGE 75>>>
- **Ekahau Pro**：业界预测勘测与干扰分析工具 <<<PAGE 49, 74>>>

---
合计：50 条。
