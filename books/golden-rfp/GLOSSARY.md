# 术语词典

| 术语 | 全称 | 中文/解释 | 出处语境 |
|---|---|---|---|
| Golden RFP | — | ALE 预制标准化需求清单文档：把产品可应答需求整理成矩阵，供投标方逐条引用响应、招标方对照评判 | 全书 |
| C / PC / NC | Compliant / Partially Compliant / Non-Compliant | 应答三级：完全满足 / 部分满足（必须写明差距）/ 不满足；空白或"见数据表"视为 NC，C 须附公开证据 | aidc Introduction 定义最完整；全书通用 |
| AOS | Alcatel-Lucent Operating System | ALE 交换机操作系统；8.10R4 为本套交换机文档锚定版本 | sw-features、6360/6465 |
| AOS-X | — | ALE 新一代数据中心 NOS：容器化模块化、开放 SAI、安全启动签名镜像 | aidc |
| ASON (ALE SONiC) | Alcatel-Lucent SONiC | SONiC 的 ALE 硬化发行版，针对 OS7900 优化，后端 AI fabric 的 NOS 选项之一 | aidc |
| AWOS | ALE Wireless Operating System | Stellar AP 固件；wlan 卷锚定 AWOS 5.0.5 | wlan |
| OVCX / OVTX | OmniVista Cirrus 10（云）/ OmniVista Terra 10（本地） | OmniVista release 10 同一平台的两种交付形态，特性集等效 | ovng |
| UPAM | Unified Policies Access Manager | OmniVista 的 NAC 模块：企业认证、角色管理、访客/BYOD 策略 | ovng |
| UNP | User Network Profile | 用户网络档案：认证通过后动态下发 VLAN/ACL/QoS 的接入管控逻辑实体 | sw-features S11、2260/2360 |
| LPS | Learned Port Security | MAC 地址学习授权机制（按时限/按数量），又称 MAC lockdown | sw-features S10、lan-access |
| Virtual chassis | — | 多台物理交换机虚拟成一台统一管理（6360 ≤8 台、2360/6465 ≤4 台）；含分裂检测 VCSP/RCD 脑裂保护 | sw-features S2 |
| ERPv2 | Ethernet Ring Protection v2 | ITU-T G.8032/Y.1344 以太环网保护（50ms 级倒换） | sw-features S3 |
| SPB / SPBM | Shortest Path Bridging (IEEE 802.1aq) | 最短路径桥接二层 fabric；配套 PBB 802.1ah、I-SID 业务实例、E-LINE/E-LAN/E-Tree 服务模型 | sw-features S8/S9 |
| EVPN-VXLAN | Ethernet VPN over VXLAN | 基于 BGP-EVPN 控制面的 VXLAN overlay（RFC 7432/8365），需支持 Type 1/2/4/5 路由否则判 NC | aidc、sw-features S8/S9 |
| MACsec | IEEE 802.1ae | 二层点对点链路加密；6465 全口 256-bit，中高端支持 over SPB/L2GRE/VXLAN | grfp-6465、sw-features S10 |
| RoCEv2 | RDMA over Converged Ethernet v2 | 融合以太网上的远程直接内存访问，AI 后端 fabric 无损传输基石（InfiniBand Spec Vol.1 Annex A17） | aidc |
| PFC / ECN / DCQCN / HPCC | Priority Flow Control (802.1Qbb) / Explicit Congestion Notification (RFC 3168) 等 | 无损以太网拥塞控制组合拳；PFC watchdog 防 PAUSE 死锁自恢复 | aidc |
| DLB / GLB / INT | Dynamic/Global Load Balancing / In-band Network Telemetry | 逐队列动态负载均衡与跨 spine 全局均衡（per-flowlet 硬件决策）；带内遥测免外置探针 | aidc |
| VXLAN RIOT | VXLAN Routing In and Out of Tunnel | 同一物理口上同时做 VXLAN 路由+桥接且线速 | aidc |
| ONIE | Open Network Install Environment | 出厂预装的开源 NOS 安装环境，允许用户后续换装兼容 NOS | aidc（7900 必备项） |
| SAI | Switch Abstraction Interface | ASIC 硬件抽象层标准，使同一 NOS 可跨厂商芯片移植；"封闭闭源单体 OS 不可接受"的对立面 | aidc |
| Rail-optimized topology | — | 按轨道（每 GPU 一条rail 上联对应 leaf）组织的 GPU 集群拓扑，区别于 classic Clos；投标须双方案给 BOM | aidc |
| JCT | Job Completion Time | 训练作业完成时间；由尾延迟与丢包行为而非平均吞吐决定——AI-DC 所有需求的推理起点 | aidc |
| MLO | Multi-Link Operation | WiFi 7 (802.11be) 多链路并发操作，含跨链路 QoS 时延优化 | wlan Section 4 |
| AFC | Automated Frequency Coordination | 6GHz 标准功率室外 AP 所需的自动频率协调（FCC/ISED 辖区） | wlan Glossary/4.22 |
| wIDS/wIPS | wireless Intrusion Detection/Prevention System | Stellar 内置无线入侵检测反制，免额外设备与许可，黑白名单按 MAC 前缀分类 rogue AP | wlan 2.3.11-15 |
| ACS / APC / CSA | Automatic Channel Selection / Automatic Power Control / Channel Switch Announcement | RF 自动化管理三件套：自动选信道（client-aware）、自动功率、切信道预告 | wlan 3.1 |
| RAP | Remote Access Point | 远程接入点：建 IPSec 隧道回总部 + split tunneling 分流 | wlan 2.3.3-5 |
| QoE | Quality of Experience | 用户体验质量指标；OmniVista 对 WLAN 客户端出 QoE 与根因分析 | ovng #44-45、wlan 2.3.18 |
| MSP | Managed Service Provider | 托管服务商；多租户分级管理（supervisor → tenant 组织）需求主角 | ovng 第 4 章 |
| RADsec | RADIUS over TLS | 加密的 RADIUS 承载；ovng 云版认证客户端要求 | ovng #36 |
| MTBF | Mean Time Between Failures | 平均无故障时间，各机型 @25°C 小时数（如 2260-10 达 2,174k h）；注意工业机型随是否配 PSU 数值不同 | lan-access |
| Perpetual / Fast PoE | — | 断电保持供电 / 立即恢复供电两项 PoE 增强，全系 PoE 机型的标配应答句式 | sw-features S16、lan-access |
