---
name: WLAN RF 微调七要点（RDA 自动化/RSSI 与速率阈值/负载均衡/漫游与粘滞客户端/组播广播优化）
description: 需要对已部署的 Stellar WLAN 做 RF 参数级微调时使用：RDA/ACS/APC 自动射频管理、高密 RF 七要点、关联/漫游 RSSI 阈值与最低速率、Band Steering/Force 5G 陷阱、粘滞客户端与 802.11k/v/r+OKC、组播/广播优化、语音 QoE 与 DFS 信道细分。
source_book: OmniAccess Stellar Wireless Fine-Tuning Best Practices
---

## R（触发场景）
- 部署后优化：QoE 评分不达标、信道利用率过高、漫游体验差
- 决定哪些参数自动、哪些手工：RDA/背景扫描开关与间隔
- 处理粘滞客户端、Apple 设备兼容、DFS 漫游问题
- 语音/视频时敏业务的 SSID 与参数专门化

## I（核心理念）
自动化优先、默认开启勿关（P35/P38/P39，<<<PAGE 48-53>>>）：RDA（ACS+APC）算法自动选信道功率，手工微调勿过度——Wi-Fi 环境更适合开足自动功能后小修。容量型思维贯穿微调：小蜂窝低功率（P37）。微调的量化抓手是 QoE 评分与信道利用率（50% 红线，P40，<<<PAGE 52>>>）。粘滞客户端的正解是 802.11k/v，负载均衡解决不了（P44/X12，<<<PAGE 57-58>>>）。

## A1（行动框架）
高密 RF 管理七要点（F2，<<<PAGE 8-9>>>）：
1. 信道复用规则化降 CCI/ACI
2. 强制 5GHz + AP 间负载均衡
3. 室内低发射功率（户外按需 10-15dBm）
4. 分区信道规划：看台用 DFS、室内用非 DFS
5. 20MHz 基准带宽
6. Airtime Fairness（默认关、高密必开）
7. 选带专用全频扫描射频的 AP + 多 RF Profile 管理

## A2（操作步骤）
- **RDA/背景扫描**：保持 RDA 开启避免手工信道冲突（X3）；背景扫描默认开，间隔建议 <40s（>60s 损 RDA 精度并影响 wIPS，X2/X20，<<<PAGE 49, 56>>>）
- **RSSI 阈值**（P41/P42/C17，<<<PAGE 55>>>）：以 -96dBm 底噪换算；关联阈值 22（= -74dBm）、漫游阈值 25（= -71dBm），双频同值；时敏场景加严（某客户 2.4G=34、5G=28，C18）
- **最低速率**（P19/P43，<<<PAGE 10, 55>>>）：最低客户端数据速率 2.4G=12Mbps、5G=24Mbps；且必须 ≥ 最低管理帧速率
- **Band Steering / Force 5G**（X7/X8，<<<PAGE 54>>>）：Band Steering 开启时 Apple iOS 可能拉黑 SSID 数分钟——重度 Apple 环境慎用；Force 5G 会拒绝全部 2.4G 关联，仅纯双频客户端环境用
- **漫游套件**（P44，<<<PAGE 57-58>>>）：802.11k（邻居报告）+ 802.11v（BSS 过渡引导）解粘滞；802.11r 快速切换 + OKC 复用 PMK 免完整 802.1X 重认证；FDB Update on Association 让 AP 发 ARP 刷新交换机转发表；注意 k/v 依赖客户端支持（X13）
- **广播/组播优化**（P46，<<<PAGE 59-60>>>）：IGMP Snooping 定向转发；Multicast Optimization 组播转单播（Number of Clients 默认 6）；Broadcast Filter ARP 让 AP 作 ARP 代理只发不播（AP 不代理免费 ARP，X14）；Broadcast Key Rotation 默认 15 分钟（1-1440）
- **语音专门化**（P45/C19，<<<PAGE 61-62>>>）：语音专用仅 5GHz SSID 且关 Band Steering；会话期间暂停背景扫描（Voice and Video Awareness）；DFS 信道细分——AP1230 双 5G：5G Low 选 8 信道、5G High 选 11 信道并固定 20MHz
- **调优闭环**（C20，<<<PAGE 65>>>）：Cirrus 信道分布 widget 核对客户端分布（如各信道 9.1%、40 号偏多即调）
- **手工功率**：设置值超型号能力时 AP 按最大能力发射而非设定值（X18，<<<PAGE 67>>>）；High Efficiency 关闭会使 11ax 降级 VHT（X19，<<<PAGE 68>>>）

## E（实证案例）
- SSID×同信道 AP 空口开销矩阵与 2.4G 更糟对照（C13/C14，<<<PAGE 53>>>）
- 信号强度行业基准表：-67dBm 时敏（VoIP/视频）、-70dBm 邮件网页、-80dBm 最低连接不可靠（C16/X9，<<<PAGE 54>>>）
- RSSI-dBm 换算（-96 底噪 - 29 = -67dBm）（C17，<<<PAGE 55>>>）
- 时敏场景漫游阈值加严（2.4G=34/5G=28）（C18，<<<PAGE 55>>>）
- AP1230 双 5G 信道细分配置（C19，<<<PAGE 62>>>）
- Cirrus 信道分布 widget 调优闭环（C20，<<<PAGE 65>>>）

## B（反例与坑）
- 关背景扫描：外国 AP 检测/rogue 抑制停止、RDA 精度下降（X2，<<<PAGE 49>>>）
- 过度手工微调反受其害（X6/P39，<<<PAGE 53>>>）
- 负载均衡解决不了粘滞客户端，也不保证最优性能（X12，<<<PAGE 58>>>）
- 每次漫游都完整 802.1X 重认证会抵消移动性意义（X11，<<<PAGE 57>>>）
- -80dBm 下发包不可靠，勿当可用信号（X9，<<<PAGE 54>>>）
- iPhone/Chromebook 与 DFS 动态信道不兼容：漫游/粘滞/随机差性能（X15，<<<PAGE 60>>>）
- 802.11k/v 取决于客户端最低共同支持（X13，<<<PAGE 58>>>）

来源：OmniAccess Stellar Wireless Fine-Tuning Best Practices（p8-10、48-68）
