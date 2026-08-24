# DIGEST · AWOS 5.0.3 Stellar AP 本地管理精华

> 面向读者：没有云管（Cirrus/OV2500）、要直接用 AP 内置 Web 界面开局的网络工程师。数字均标注原书页码。

## 一、一页看懂 AWOS 本地管理

Stellar AP 的 AWOS 固件支持 Express 模式：AP 自己组成集群，内置 Web GUI 完成全部开局与运维（p13）。选本地 GUI 的三种典型情况：

1. **没有网管平台**——纯 Express 模式交付，Web 界面就是唯一入口。
2. **应急排障**——断网/云管不可达时，直连 AP 或走 GMIP 改配置。
3. **ZTP 场景排障**——AP 从 OXO 服务器取配置（p9-12），出错时回到本地向导重来。

前提牢记三条（p13）：同集群最多 **255 台**、所有 AP 必须在**同一 VLAN**（组内通信走组播）、整组共用一个 cluster ID。有 OmniVista 时单网可扩到 4000 台（p86）。

## 二、开局十分钟

1. **接一台、只接一台**：多台同时首上电会各自成组（p13 附近）。
2. 终端连预置 SSID `mywifi-xxxx`，访问 `http://mywifi.al-enterprise.com:8080` 进初始化向导；无 DHCP 时 AP 默认 IP 192.168.1.254，笔记本配 192.168.1.100/24 直连（p13）。
3. 走五步向导：改管理员密码（默认 admin）→ 国家码/时区 → 建 WLAN。中途终端不得切网，完成后 `mywifi-xxxx` 自动删除。
4. **VLAN 向导里配不了**，必须向导后在 "Modify Your WLAN" 补配。
5. **PVM 选举**按机型优先级链自动选出（p18）：AP1451 > AP1351 > AP1431/1331 > AP1521 > AP1320/1360 > …；同优先级比 MAC 最大者。低端机当 PVM 会把集群上限拖到 32 台（AP1101/AP1201H/L/HL），混装时手动 "Update to PVM" 提升。
6. 向导后统一走 **GMIP（默认 10.0.0.1）:8080** 做长期管理入口，不追漂移的 DHCP 地址（p31-32）。

## 三、常用参数默认值速查表

| 类别 | 参数 | 默认值（可调范围） | 页码 |
|---|---|---|---|
| 管理 | AP 兜底 IP | 192.168.1.254 | p13 |
| 管理 | 组管理 IP / Group ID | 10.0.0.1 / 100 | p31-32 |
| 管理 | Web 端口 | HTTP 8080 / HTTPS 443 | p59+ |
| 管理 | 登录锁定 | 3 次失败锁 1 分钟 | 开局章 |
| 射频 | 信道/功率 | RDA（ACS+APC）自动；手动功率 1 dB 步进 | p40-41 |
| 射频 | Beacon 间隔 | 100 ms（60-500） | p40+ |
| 射频 | DTIM / Short GI / UAPSD | 1 / 启用 / 启用 | p40+ |
| 射频 | 后台扫描 | 20 s（5s-3h） | p40+ |
| 负载 | Band Steering | 启用，Prefer 5G | p46 |
| 负载 | Load Balance 阈值 | 客户端密度 10；利用率 2.4G/5G 各 70% | p46-47 |
| 高密 | RSSI Threshold | 推荐 2.4G=5、5G=10、6G=10 | p46-47 |
| 高密 | Roaming RSSI | 推荐 2.4G=10、5G=15、6G=15 | p46-47 |
| 客户端 | 每 BSSID 上限 | 64（1-256） | p40+ |
| 速率准入 | 最低速率 | 2.4G 12 Mbps、5G/6G 24 Mbps | p40+ |
| 认证 | RADIUS AuthPort/AcctPort | 1812 / 1813；RadSec 改 2083 | p62-63 |
| PSK | 口令格式 | 64 位十六进制 或 8-63 个 ASCII | p59 |
| 内置 Portal | 本地账户上限 | 2000 | p50 |
| AP 侧 DHCP | 租约 | 24 小时 | p50+ |
| 日志 | Syslog 级别 | Notice；本地日志 1MB FIFO | p78+ |
| Mesh | 组播速率 | 24 Mbps | p103 |

## 四、安全加固清单

- **必改默认凭据**：Web 管理员默认 admin；同时改 Viewer/GuestOperator，以及 CLI 的 root 与 support 账户（root 凭据由 AP 生成、仅客户持有）。
- **WPA3**：6GHz 只允许 WPA3 与 Enhanced Open；WPA3-Enterprise CNSA（Suite B 192 位）会强制 PMF Required（p62）。
- **CNSA 静默回退**：不支持的机型配 CNSA 不报错、直接降回 WPA2——高安全场景逐机型核对（p62）。
- **HTTPS 证书**：先装入根证书 ALE-OmniAccess-WLAN.CRT；自定义证书的 CN 必须是 `mywifi.al-enterprise.com`，登录 URL 不可改。
- **动态 VLAN**：RADIUS 下发 Tunnel-Type(64)=VLAN、Tunnel-Medium-Type(65)=802(6)、Tunnel-Private-Group-ID(81)。
- **wIPS**：Suppress 发 DEAUTH 默认关闭，按需开启；SNMPv3 固定 sha/aes128。

## 五、运维与升级要点

- **整组一份配置**：clear/backup/restore 均整组生效，无需选单台（p78）。配完立即导出备份。
- 升级：单台约 5 分钟留窗口；**升级完成后清浏览器 Cookies 与 Cache**，否则旧资源导致界面异常。
- **换 PVM 顺序不能反**：先把 SVM 升为 PVM，再断旧机；新增 AP 前 PVM 不能处于 Down。
- 扩组三法（p86）：划不同子网 / 配不同 group ID / 转 OmniVista（DHCP Option 138/43 自动下发，转换后 AP 重启注册）。
- 崩溃取证：预先启用 PMD 并指定 TFTP 服务器（默认关闭）。

## 六、机型例外与限制速查

| 机型 | 不支持/受限 |
|---|---|
| AP1101 | 全频段不支持 WPA3 CNSA |
| AP1201H / AP1201L | 2.4G 不支持 CNSA |
| AP1201/1201L/1201H/1201HL | 不支持带 VLAN 标签的无线桥接，不做网桥 |
| AP1101/1201H/1201L/1201HL | 当 PVM 时集群上限跌到 32 台 |
| AP1311 / AP1301 | 不支持 160MHz |
| AP1451 等 | 160MHz 仅 5G/6G 静态配置，ACS 不选 160MHz |
| 无扫描射频机型 | 进扫描模式断全部客户端；AP1451 仅 6GHz 中断 |

另两条易踩坑：Out-of-box Mesh（内置 SSID "Stellar-MESH"，2.4G）**一旦接过有线 uplink 即永久禁用**，只有恢复出厂能找回（p103）；组间不漫游，多组边界要规划在漫游不敏感的位置。

---
*由 cangjie-skill 流水线从 AWOS 5.0.3 User Guide 蒸馏生成。*
