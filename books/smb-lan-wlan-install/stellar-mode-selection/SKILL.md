---
name: Stellar AP 部署模式选型与组网
description: 当需要为 SMB Wi-Fi 选择 Express/Enterprise/Cloud 部署模式、做 AP 首次配置向导、扩容多 AP 自动成组或恢复 AP 出厂时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 新部署 Wi-Fi，要决定用 AP 自管理（Express）、本地 OV2500（Enterprise）还是 Cirrus 云管（Cloud）
- 新 AP 开箱需要首次配置向导、改管理 IP 或恢复出厂
- AP 数量增长，要多台 AP 自动成组统一管理

## I（核心理念）
Stellar 是无控制器架构：AP 间通过空口直接交换漫游上下文、通过 LAN 交换 RF 参数，管理面按规模三选一——Express 自管理集群（255 台）、Enterprise 本地 OV2500（4000 台）、Cloud Cirrus（10000 台）。AP 上电后按"DHCP option 138 → Cirrus 注册检查 → Express"三段决策树自动落到某个模式。多台 AP 同 Group ID + 同 VLAN 即自动成组并选举 PVM/SVM 主备。

## A1（行动框架）
1. 模式选型（F02，<<<PAGE 195>>>、<<<PAGE 185>>>–<<<PAGE 189>>>）：
   - Express：自管理独立集群、Web 向导、最多 255 AP、免许可 → SMB 小规模；
   - Enterprise：OV2500 本地 NMS 集中管理、最多 4000 AP → 中大型/本地运维；
   - Cloud：OmniVista Cirrus 云管、最多 10000 AP → 多分支/托管。
2. AP 首次配置向导（C02，<<<PAGE 99>>>–<<<PAGE 103>>>）：浏览器访问 `192.168.1.254:8080`（默认口令 admin）→ 改管理员密码 → 选国家/时区 → 创建首个 SSID（替换默认 mywifi-XXXX）→ IP Mode 改 Static（如 192.168.1.3，网关指向交换机）→ 用新 IP 重连。
3. 模式判定（F01，<<<PAGE 198>>>）：DHCP offer 带 option 138 → 向 OV2500 注册（Enterprise）；无 138 → 联系 Cirrus，MAC/SN 已注册 → Cloud；未注册 → Express。
4. 切 DHCP 模式后用域名管理：Web 界面 AP > IP Mode > Edit > DHCP > Save，此后 `mywifi.al-enterprise.com:8080` 访问；交换机侧 `show mac-learning` 交叉定位 AP（C10，<<<PAGE 176>>>–<<<PAGE 181>>>）。
5. 多 AP 扩容（F09，<<<PAGE 262>>>–<<<PAGE 268>>>）：新交换机把 AP 管理 VLAN untagged 到 AP 口、tagged 到上联 → AP 通电取 DHCP → 与既有 AP 同 VLAN + 同 Group ID 自动成组 → 统一 Web 管理，PVM 为型号最高者（本例 AP1321）。
6. 恢复出厂（C03，<<<PAGE 104>>>）：Reset 键按 10 秒松开；或 Console（support/aos2016）`ssudo firstboot -y` → `ssudo reboot`。

## A2（进阶应用）
- AP Group 出厂默认 Group ID 100、VLAN 1；改 Group 名/ID/管理 IP 在 System > General（C17，<<<PAGE 264>>>–<<<PAGE 268>>>；P34，<<<PAGE 202>>>）。
- PVM/SVM 选举双准则：先比 AP 型号高低，再比 MAC 大小（F15/P35，<<<PAGE 203>>>）。
- 分布式控制：空口交换漫游上下文/MAC/密钥/ARP，LAN 交换 RF 设置/功率/信道/RSSI（P47，<<<PAGE 280>>>）。
- AP 选型速查：Wi-Fi 代际九维对照（Wi-Fi 6 = 802.11ax 9.6Gbps WPA3，Wi-Fi 7 = 802.11be 46Gbps 320MHz 16x16 MU-MIMO）（F11，<<<PAGE 45>>>）；型号尾数 2 = 支持外置天线，其余内置全向（P50，<<<PAGE 41>>>）。
- 无控制器架构下 AP 自带 DHCP/DNS/NAT 三件套服务（P37，<<<PAGE 216>>>）。
- AP LED 状态判读：绿闪 = 已启动广播默认 SSID，蓝 = 双频，蓝红闪 = 升级中，红 = 启动中（P42，<<<PAGE 52>>>）。

## E（实证案例）
- Express 向导：新建 SSID AdminX 替换默认 mywifi-XXXX，AP 改静态 IP 后用新地址重连（C02，<<<PAGE 99>>>–<<<PAGE 103>>>）。
- OS2360 接入 + AP 自动成组：两台 AP 出现在同一 AP Group，PVM 为 AP1321（C17，<<<PAGE 264>>>–<<<PAGE 268>>>）。
- AP 切 DHCP 后用 mywifi.al-enterprise.com:8080 域名访问管理页（C10，<<<PAGE 176>>>–<<<PAGE 180>>>）。

## B（边界与陷阱）
- 多台新 AP 默认管理 IP 都是 192.168.1.254 会冲突；静态管理多台前必须逐台改 IP 或直接依赖 DHCP；AP 改 IP 后旧地址访问失效（CE20，<<<PAGE 101>>>、<<<PAGE 103>>>）。
- AP 加入 AP Group 后本地配置被清除并替换为 PVM 下发的组配置——单点调好的配置会丢（CE06，<<<PAGE 266>>>）。
- 出厂即广播 mywifi-XXXX（MAC 后四位），管理口 8080（P33，<<<PAGE 199>>>）。
- Console 凭据 support/aos2016（C03/C19，<<<PAGE 104>>>、<<<PAGE 352>>>–<<<PAGE 357>>>）。

## 来源
- case·Stellar AP1321 首次配置向导（<<<PAGE 99>>>–<<<PAGE 103>>>）
- case·AP 恢复出厂两条路径（<<<PAGE 104>>>）
- case·AP 切 DHCP 模式与域名重连（<<<PAGE 176>>>–<<<PAGE 181>>>）
- case·多交换机多 AP 自动成组（<<<PAGE 264>>>–<<<PAGE 268>>>）
- framework·三模式自动选择决策树（<<<PAGE 198>>>、<<<PAGE 274>>>、<<<PAGE 195>>>）
- framework·三部署模式定位与规模选型（<<<PAGE 195>>>、<<<PAGE 185>>>–<<<PAGE 189>>>）
- framework·多 AP 环境扩展流程（<<<PAGE 262>>>–<<<PAGE 268>>>）
- framework·PVM/SVM 选举准则（<<<PAGE 203>>>）
- framework·Wi-Fi 代际演进对照（<<<PAGE 45>>>）
- principle·AP 出厂默认行为（<<<PAGE 199>>>）
- principle·AP Group 成组条件（<<<PAGE 202>>>）
- counter·多 AP 默认 IP 冲突（<<<PAGE 101>>>）
- counter·入组后本地配置被清除（<<<PAGE 266>>>）
