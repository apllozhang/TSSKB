# 全书精华串讲

## 一句话全书

Stellar 用同一套 mesh 架构（root 网关 + mesh 节点 + WDS 透明桥接）覆盖从企业室外 bridge、工厂室内多点 mesh 到家庭 Express 组网的全场景，代价是带宽逐跳减半、无漫游、实时业务尽力转发——设计就是在这组硬约束里做取舍。

## 架构骨架（p5-8）

- **两种角色**：root（接有线的 LAN 网关）/ mesh（无线节点）；所有数据流量经 root 进出
- **两种形态，互斥不可组合**：
  - Bridge：单链路 Point-to-Point，纯 LAN 延伸，无 SSID 广播，企业最常用
  - Multi-Point mesh：多点覆盖，root 与每个 mesh AP 都可广播 WLAN 服务并带下联口
- **冗余**：同一 AP group 配双 root，mesh AP 按 RSSI 选最优 root
- **带宽物理约束**：
  - mesh 链路带宽由 backhaul 与客户端业务共享
  - Multi-Point 下同频同射频收发，需回传的吞吐每节点 ÷2
- **Auto-Mesh 开局**：root 连 LAN 激活，周边空配置 AP 自动以默认 mesh 链路接入
- **WDS 传输**：4 地址帧实现 AP 间透明以太桥接，统一广播域，可承载多个企业 VLAN（0-4095）
- **远端能力**：mesh AP 以太口透传 tagged/untagged VLAN 做下联；AP1361/1362/1361D 的 ENET1 口还能输出 802.3af/at PoE 给远端设备（免单独 PoE 注入器）

## 硬性限制清单（p9-11, 17，全场景通用）

- mesh 集群最多 **16 个 mesh AP**，root 可双
- 每 mesh AP 最多广播 **5 个客户端 SSID**
- root 总吞吐被所有 mesh AP 与客户端分摊，每 SSID 吞吐再 ÷2
- **mesh AP 之间无漫游**（无 PMK/OKC/密钥交换）
- **VoIP 与实时应用只有尽力转发**
- Bridge 与 mesh 拓培不能组合
- 链路两端天线型号与极化必须一致；mesh 内保持同系列 AP（混代际会降速）
- 数据业务走 5GHz，信道宽度 40MHz 起步

## 用例地图（p8-17）

- **室外 Bridge**（p8-10）：隔街两栋楼、屋顶 LoS 安装、定向天线、ENET0 分发 VLAN、ENET1 给摄像头供电；Enterprise 模式用 ARP 按 VLAN/端口定义 ACL 与 QoS
- **室外 Multi-Point**（p10-11）：工业/活动场地/营地；root 用全向/半定向 MIMO 天线；nLoS 可行但半定向天线波束边缘至少 -3dB
- **室内多点**（p15-17）：厂房/仓库；RF 要求 SNR ≥20dB、RSSI ≥-67dBm；全向外置天线（AP1322 直挂 ANT-O-6）是最佳实践，patch 天线不推荐；恶劣环境可用 IP67 的 AP1361/AP1251 吸顶
- **家庭 mesh**（p16-17）：AP1301 入门 Wi-Fi 6 + Express 模式手机管理；root 接路由器旁、用路由器 DHCP、mesh 距离 ≤2 房间（约 5 米）；3-5 米内高吞吐，80MHz 宽信道服务双频 Wi-Fi 6 终端；流媒体/游戏单独 SSID + 按 SSID 的 QoS

## 支持型号速记（p10-11, 17）

| 场景 | Wi-Fi 6 | Wi-Fi 5 |
|---|---|---|
| Bridge（室外） | AP1361/1362/1361D（IP67）；室内 AP1322（外置 patch） | AP1251（IP67）；室内 AP1222 |
| 室外 mesh | AP1361/1362/1361D | AP1251（均 IP67，可抱杆） |
| 室内 mesh | AP1301/1311/1321/1322/1331/1351/1361 | AP1201/1221/1222/1231/1232/1251 |

## 室外工程要点（p11-15）

- **净空**：Fresnel 区至少 60% 净空；安装高度 = 遮挡物高度 + 余量；优先屋顶；天线主瓣互对（LoS）
- **合规**：无线电辐射报民航/地方主管；信道符合当地法律
- **防雷**：浪涌保护 + 规范接地（参考 TIA-6076B）；天线与 AP 间可加避雷器
- **供电**：室外 PoE 注入器必须 IP67、功率覆盖 af/at（新 Wi-Fi 6 AP 需 bt）、带电源保护
- **配件订货号**：AP-MNT-OUT-H（安装套件）、PD-9001GO-ET/AC 与 PD-9601GO/AC（室外 PoE 注入器）、PD-OUT/MBK/ET 与 PD-OUT/MBK/S（注入器杆/墙挂）、PWR-CORD-XX（国别电源线）、AP-OUT-SFP-KIT（SFP 套件）
- **距离-吞吐**：性能表基于 RF 链路预算（自由空间损耗 + 10dB 系统余量抗风雨）+ Ekahau 速率估算，5GHz 40MHz 起步；短距可上 80MHz
- **长距（≥1/5 英里）**：只配高增益 MIMO 兼容定向天线 + 较低 HE/HT 速率；适合语音这类速率不敏感业务。第三方栅格/抛物面天线门槛：5GHz、极化分集 MIMO（≥2x2）、50Ω、线损 <1.5dB、N 型接头、DC 接地

## 勘测（p18-20）

- mesh 规划必备勘测，**bridge 强制勘测**；Ekahau 站点勘测可由 ALE 以服务提供并辅助报价
- Ekahau PRO 10.4 内置 Stellar AP1301-1360 系列与 ANT-O-6/ANT-O-M2-5/ANT-O-M4-9/ANT-S-M4-60 天线
- 仿真能力：按天线参数/发射功率 EIRP/摆位/MU-MIMO 流数/GI 仿真传播，输出吞吐与链路质量（接收功率 + SNR）
- 实测样例：AP1361D 定向链路，5GHz 信道 106（80MHz）、4x4 MU-MIMO、MCS5 QAM64，无线 HE 速率超 1Gbps

## 配置主线（p20-27）

1. **准备**：识别入组 AP；DHCP 做 IP 保留，bridge 理想全静态
2. **专用 AP Group**：NETWORK -> AP REGISTRATION -> AP Group；时区 UTC、SSH（Support/root）、AP WEB（Admin）
3. **专用 RF Profile**：WLAN -> RF Management -> RF Profile；Force 5G、Load balance、Airtime Fairness、Background Scanning 关闭、5G 信道 [100,104,108,112]、80MHz、DFS/TPC 15dBm、MU-MIMO + High Efficiency；**组内所有 AP 的 RF 参数必须一致**
4. **SSID**：WLAN -> SSIDs；示例 WPA3 SAE AES、双频、Untagged VLAN 94；HT Control A-MSDU/A-MPDU 默认
5. **多 VLAN**：用 ARP 配置分发 VLAN
6. **角色**：逐 AP Edit Mesh Configuration：MESH Enable=Yes、Is Root=Yes/No、SSID=Stellar-MESH、Band=5GHz
7. **上线**：mesh AP 脱离原网搬迁上电，初始化数分钟；拓扑 mesh 图标高亮即成功
8. **bridge 下联口**：uNP Access Auth Profile（UNIFIED ACCESS -> UNIFIED PROFILE -> Template）：AP Mode=Disabled、Trust tag=Enabled、Bypass VLAN 列表；先 Apply to Devices 到组，再逐端口应用
9. **APUI（Express/救急）**：Backhaul0 接口设角色与 mesh SSID；Enet0/1/2/3 设 trust/bypass VLAN

## 监控排障（p27-32）

- 前提：mesh AP Group 启用 root 账户 SSH
- **RF 核对**：`/tmp/config/rfprofile.conf` 看 AP 实际生效配置
- **信道与 DFS**：`iwlist athXX channel`；UNII-2 雷达检测直接打控制台
- **链路**：`iwconfig athap1`——Link Quality、Signal、Noise、Bit Rate；质量骤降查距离/频率/安装/nLoS
- **SSID 接口**：`iwconfig` 全量，区分 backhaul（athap1）与客户端接口（ath01/ath11）
- **客户端**：`wlanconfig athXX list`——速率、RSSI、SNR、频段、HT/VHT/MU 能力
- **DRM 只在 root 生效**（mesh SSID 的远端客户端）

## 全书最容易被忽略的五个坑

1. Bridge 与 mesh 不能组合，规划必须二选一（p11）
2. mesh 无漫游、VoIP 尽力转发——别对客户做错承诺（p11/17）
3. 组内 RF 参数不一致是链路故障常见根因，用专用 RF Profile 统一推送（p21）
4. bridge 不做勘测直接安装是违规操作（p18）
5. AP WEB/SSH 不预开，临场没有 APUI 与控制台救急手段（p21/25/27）
