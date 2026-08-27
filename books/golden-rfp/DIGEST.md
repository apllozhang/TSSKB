# 全书精华串讲：按"写标书流程"串起 Golden RFP

## 第一步：拿到招标书，先定规矩（grfp-guide）

打开任何一份 ALE Golden RFP，第一页 Introduction 都在讲同一件事：这是一份**预先写好的应答库**，每条需求后面跟着 C / PC / NC 三格。三个铁律决定生死——**逐条必答**（The bidder must answer every requirement）；**空白、横线、"见数据表"一律视为不满足**（A blank cell, a dash, or "see datasheet" will be treated as Non-Compliant，出自 aidc 卷）；**每个 C 都要附公开数据表、版本说明或测试报告佐证**。

先把客户标书里的产品版本对齐自己的母本：交换机软件类是 8.10R4，无线是 AWOS 5.0.5 / OmniVista 10.6.1（wlan 6.0.2），网管是 10.5.2，AI-DC 是 Phase 2 v1。版本错位时宁可降级答 PC 也不要硬标 C。

## 第二步：硬件参数章节 → 抄机型文档（grfp-lan-access）

标书里密密麻麻的端口/PoE/功耗/MTBF 表，直接从四个机型族文档搬：

- **桌面轻量**走 2260：半宽无风扇，P48 也只有 63.2W 满载功耗，PoE 最高 370W；
- **SME 堆叠**走 2360：4 台虚拟 chassis，全光口 U 系列覆盖光纤到房，注意原文是法文版、"68,4 Mpps" 要读成 68.4；
- **园区主力**走 6360：8 台 virtual chassis 单 IP，Multi-Gig 型号 PoE 预算拉到 760W，喂饱 WiFi 7 AP；
- **工业场景**走 6465：-40~75°C、DIN 导轨、全口 256-bit MACsec + 1588v2 授时，交通/电力行业的应答几乎可以整页照抄。

四族共同的反造假句式记得带上："不能算 combo 口，所有端口必须同时可用"。

## 第三步：软件功能章节 → 按 Section 抽矩阵（grfp-sw-features）

功能条款不是逐字读 97 页，而是按域抽取：高可靠抽 Virtual chassis 8 节点/VCSP 脑裂保护；二层抽 ERPv2 环网和 Port Mapping；QoS 抽 8 硬件队列+语音自动提优先级；安全分三层讲——供应链（Signed AOS/Secure Boot/CC 认证）、数据面（MACsec-over-VXLAN/IPsec）、接入面（UNP 动态下发 VLAN/QoS/ACL + IoT 设备识别）。中高端机型再叠加 SPB 全家桶（E-LINE/E-LAN/E-Tree/L3 VPN over I-SID）与 EVPN-VXLAN fabric。关键纪律：每条注明它在哪个档位机型出现，低阶没有的别乱抄。

## 第四步：数据中心/AI 项目 → 换一套语言（grfp-aidc）

AI-DC 卷的开场白值得背下来：AI 训练流量是集合通信同步突发，几条慢流就能卡死整个训练作业，JCT 取决于尾延迟而非平均吞吐。由此推出的需求全是"硬"的：RoCEv2 无损、cut-through 转发、ASIC 内 <1ms 硬件链路倒换、per-flowlet 自适应路由防哈希极化、带内 INT 遥测免外置探针、PFC watchdog 防 PAUSE 死锁。方案骨架三网分离（backend GPU 互联 / frontend 存储通用 / OOB 管理），GPU 服务器 OC8100 的 8×MI325X + 8×400G scale-out 口，Spine 有 51.2T/800G 和 25.6T/400G 两档，投标方必须同时给出 Clos 与 rail-optimized 两套 BOM。还有评标级细节：EVPN 只支持 Type 2 路由直接判 NC，REST API 只做 CLI 代理也算 NC。

## 第五步：无线项目 → 架构叙事 + 分档选型（grfp-wlan）

Stellar 的叙事主线一句话：AP 自己就是控制器——互发现、自成群、推举 Virtual Manager，不需要外部服务器也不需要额外许可；上云或上 OmniVista 后本地扩到 4000 台、云上 10K 台；管理面挂了转发照常。RF 章节五连招（ACS 客户端感知切信道、APC 自动功率、语音视频感知避扫描、RSSI 门限准入+强制漫游、airtime 公平切片）几乎是所有无线标书共性需求的答案。选型按 Type A-Q2 对号入座：酒店面板找 AP1301H（下联口还能给电话供电），室外严酷环境找 AP1561/1572（N 型外置天线+避雷+-40~65°C），WiFi 7 记住三个词 MLO、320MHz、4096-QAM。注意脚注：Type A 美国不可售、Type D 2026 年停产。

## 第六步：网管平台章节 → 72 条编号即答（grfp-nms）

OmniVista release 10 一套代码两种形态（云 OVCX / 本地 OVTX 特性等效），数据主权诉求推 Terra 版。应答素材按章取用：多租户运营引 #20-24，安全合规引 RADsec/双因素/SSO（#36-38），分析报表引 QoE 根因与 30 天历史（#44-47），NAC 是重头戏——内置 RADIUS/LDAP/Captive Portal 且 RADIUS 不拆开售卖（#60-61），DPI 到 L7 连 HTTPS 应用都能管控计费（#66）。边界提醒写两次都不嫌多：这份卷不管 Stellar WLAN 的无线特性，反之亦然。

---

全书六个单元串完一条主线：**懂规矩（guide）→ 填硬件（lan-access）→ 填软件（sw-features）→ 换赛道打 AI（aidc）→ 无线另成体系（wlan）→ 平台收尾（nms）**。下一步建议从 grfp-guide 开始精读，然后按手头项目类型挑对应单元；每个单元的 B 段都列了版本时效与 OCR 数据陷阱，引用数字前先查一眼。
