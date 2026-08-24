---
name: ssid-radio-tuning
description: 何时用：调 SSID 射频参数、优化高密/时延场景、配内置 Portal/DHCP 服务或做无线体检时。
source_book: AWOS 5.0.3 Stellar AP User Guide
---

# SSID 射频调优与内置服务

## R · 原文引用

> By default, the working channel and transmitting power are automatically managed by Radio Dynamic Adjustment™ (RDA) technology. ... If you want to set the channel and power values for an AP manually, you need to disable the ACS/APC function on the AP. ... In manual mode the AP transmit power can be adjusted in 1 dB increments. (p40-41)

> By default, band steering is enabled. ... The thresholds for client density is 10, channel utilization is 70% for 2.4G and 70% for 5G. By default, Load Balance is enabled. ... Recommended 2.4G (5), 5G (10), 6G (10). ... Recommended 2.4G (10), 5G (15), 6G (15). (p46-47)

> Maximum 2000 accounts supported in AP local database for internal captive portal authentication. ... Specify the cycle for uploading user behavior logs to FTP server, can be set to 1 hour, 2 hours and 4 hours. (p50)

## I · 方法论骨架

调优决策序：**默认值盘点 → 场景偏差项 → 逐项改并记录代价**。

1. RDA（ACS+APC）默认开启即最优起点；只有明确需求才关，关后必须两频段分别手配，功率 1 dB 步进。
2. 高密场景按推荐值开 RSSI Threshold / Roaming RSSI；时延敏感场景调后台扫描，但要接受 RDA/wIPS 精度损失。
3. 内置服务（Portal/DHCP）有硬容量与作用域边界，选型先核对限制。

## A1 · 书中案例

- 时延敏感部署：后台扫描从默认 20 秒加大间隔或只扫工作信道（间隔 >1 分钟影响 RDA 与 wIPS 精度）。
- 高密部署：RSSI Threshold 推荐 2.4G=5、5G=10、6G=10；Roaming RSSI 推荐 2.4G=10、5G=15、6G=15（配 802.11k/v）。
- 160MHz：仅 5G/6G、仅静态配置，ACS 不会选 160MHz。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：高密办公/礼堂容量优化；语音时延调优；AP 侧开 DHCP/Portal；Client Health 体检；速率准入控制。
- 区分：涉及 802.1X/RADIUS/WPA3/CNSA → `wlan-security-enterprise`；首次开局流程 → `cluster-bootstrap-pvm`；扫描模式踢客户端的机型核对见本文边界节。

## E · 可执行步骤

1. 盘点默认值：Beacon 100ms（60-500 可调）、CSA 默认启用（计数 1-10）、Short GI 启用、DTIM=1、UAPSD 启用、后台扫描 20s（5s-3h）。
2. 手动指定信道/功率：先在该 AP 上关闭 ACS/APC → 两个频段分别设 → 功率按 1 dB 步进。160MHz 仅静态、仅 5G/6G、仅支持机型（AP1451/AP1431/AP1411/AP132X/AP136X/AP1351）。
3. 高密优化：开 RSSI Threshold 配推荐值；开 Roaming RSSI 配推荐值并确认 802.11k/v；Band Steering 保持默认 Prefer 5G，双频强制上 5G 才用 Force 5G；Load Balance 默认已开（密度阈值 10、利用率 70%）。
4. 速率准入：2.4G 最低 12 Mbps、5G/6G 最低 24 Mbps；管理帧速率避开 2.4G Beacon 的 9/18 Mbps（会自动改用 11/24）与 5G 的 9 Mbps（自动改 12）。
5. 客户端管理：空闲超时关闭时固定 600s，开启可配 60-12000s；每 BSSID 最大客户端 1-256，默认 64；健康度 Best>30 / Good 15~30 / Fair<15；监控刷新默认 30s（30/60/120 可选）。
6. AP 侧 DHCP（Service → DHCP）：租约默认 24h；DHCP 池只能绑定配了静态 IP 的 Network，且 VLAN 须先映射到 SSID 才出现。
7. 内置 Portal：本地库 ≤2000 账户（支持 Excel 模板导入）；行为日志上传 TFTP/SFTP/Syslog，FTP 周期 1/2/4 小时。
8. Walled Garden：认证前要放行的资源须预先知道 IP/域名并加入。

## B · 边界与陷阱

- **关后台扫描的代价**：外部 AP 检测与 rogue 抑制直接停止、RDA 精度下降；间隔 >1 分钟同样劣化 RDA/wIPS。
- **Allowlist 作用域**：仅对 captive portal 认证生效，不能豁免 Enterprise/Personal WLAN 凭据；Blocklist 才是全局封禁。
- **Portal 账号登录只认本地库**：不支持外部认证服务器；且单账号可被多设备同时使用，防蹭网靠访问码轮换/日志审计。
- **扫描模式踢客户端**：无扫描射频机型进扫描模式会断全部客户端；AP1451 仅 6GHz 服务中断；带扫描射频的 Wi-Fi 6/7 机型不受影响。One Time 模式 5 分钟自动恢复。
- **160MHz 不会出现在 ACS 结果里**；AP1311/AP1301 不支持。
- 组播转单播（IGMP snooping）最多对 6 个客户端生效。
- Voice/Video Awareness 与 Airtime Fairness 默认关闭。

---
来源条目: p10, p11, p12, p13, p14, p15, p18, p19, p23, p25, ce07, ce08, ce12, ce14, g11, g12, g13, g16, g17, g24, g25, g26, g27, g28, g29, g36
