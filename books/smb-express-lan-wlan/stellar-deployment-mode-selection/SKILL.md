---
name: Stellar 三部署模式选型与分布式架构
description: 当需要为 OmniAccess Stellar WLAN 选择 Express / Enterprise / Cloud 管理模式、理解 AP 自动选模逻辑、或部署 AP Group 与 PVM/SVM 选举时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 新项目要决定 Wi-Fi 用哪种管理模式（免许可证自管理 / 本地 OV2500 / Cirrus 云管）
- AP 上电后不确定它进入了哪种模式，需要理解自动判定链
- 多台 AP 需要统一成组管理（AP Group / PVM / SVM）

## I（核心理念）
Stellar 是无控制器分布式架构：AP 上电后按 "DHCP option 138（OV2500）→ Cirrus 注册（MAC/序列号）→ 都没有则 Express" 三级判定自动进入管理模式。同 Group ID + 同管理 VLAN 的 AP 自动成组并选举 PVM/SVM，从 PVM 统一下发配置。

## A1（行动框架）
1. **按规模选模式**（<<<PAGE 188>>>-<<<PAGE 198>>>）：Express 自管理 standalone 集群 ≤255 AP、免许可证；Enterprise（OV2500 本地 NMS 集中管理）≤4000 AP；Cloud（OmniVista Cirrus）≤10000 AP。
2. **核对选型边界**：要语音可视化/大规模就必须 Enterprise/Cloud——Express 模式无 Voice analytics 与 Voice application visibility（<<<PAGE 875>>>）；AP1101 单 AP-Group 仅支持 64 AP / 256 并发客户端，低于 AP13XX 的 255/512（<<<PAGE 868>>>）。
3. **理解自动选模判定**：AP 发 DHCP REQUEST → DHCP 下发 option 138（OV2500 IP）则注册 OV2500 → 已在 Cirrus 声明（MAC/SN）则从 Cirrus 取配置 → 否则进 Express 模式（<<<PAGE 201>>>、<<<PAGE 264>>>）。
4. **多 AP 成组**：出厂默认 Group ID=100 / VLAN 1，同 VLAN+同 Group ID 自动成组；PVM/SVM 选举规则：先比最高 AP 型号、再比最高 MAC（<<<PAGE 204>>>-<<<PAGE 207>>>）。
5. **改组**：System > General 设 Group name / Management IP / Group ID（<<<PAGE 240>>>-<<<PAGE 245>>>）。

## A2（进阶应用）
- **分布式控制面**：AP 间 Over the Air 交换 RF 设置/功率/信道/RSSI，Over the LAN 交换漫游客户端上下文（MAC、密钥、Access Role Profiles），即 CNCS（<<<PAGE 270>>>）。
- **混部组网**：AP1301 + AP1321 同 VLAN+同 Group ID 自动成组，PVM 落在型号更高的 AP1321 上（<<<PAGE 240>>>-<<<PAGE 245>>>）。
- **出厂默认行为速查**：广播 SSID "mywifi-XXXX"、IP 192.168.1.254、Web `http://<AP IP>:8080`（<<<PAGE 202>>>）。

## E（实证案例）
- 多交换机多 AP 实验：OS2360 上配 VLAN tagged/untagged 后，两台 AP 自动成组，PVM=AP1321（型号更高），并从 System>General 修改组参数（<<<PAGE 240>>>-<<<PAGE 245>>>）。
- 选型反例：需要语音可视化的项目误选 Express，只能拿到 DPI 带宽管控而拿不到 Voice analytics（<<<PAGE 875>>>）。

## B（边界与陷阱）
- **AP 入组配置即被覆盖**：AP 加入 AP Group 后，其自身配置被删除并由 PVM 下发的配置替换（<<<PAGE 243>>> WARNING）——多 AP 混部前务必先把目标配置做到 PVM。
- Express 无语音分析/可视化（<<<PAGE 875>>>）；AP1101 组规模腰斩（64 AP/256 客户端，<<<PAGE 868>>>），选 Express 前核对 AP-Group 规模表。
- OVC4→OVC10 迁移时序列号不能同时在两个平台，须先在 OVC4 删干净（<<<PAGE 318>>>）。

## 来源
- frameworks·F1 部署模式自动选择决策流程（<<<PAGE 201>>>、<<<PAGE 264>>>）
- frameworks·F2 三模式定位与规模决策（<<<PAGE 188>>>、<<<PAGE 190>>>、<<<PAGE 192>>>、<<<PAGE 198>>>）
- frameworks·F12 AP Group/PVM-SVM 选举（<<<PAGE 204>>>-<<<PAGE 207>>>、<<<PAGE 270>>>）
- principles·P17 出厂默认行为（<<<PAGE 202>>>、<<<PAGE 205>>>）
- principles·P18 分布式控制面（<<<PAGE 270>>>）
- cases·C16 多交换机多 AP 自动成组（<<<PAGE 240>>>-<<<PAGE 245>>>）
- counter-examples·X4 入组配置被覆盖（<<<PAGE 243>>>）
- counter-examples·X14 模式选错的功能/规模边界（<<<PAGE 875>>>、<<<PAGE 868>>>）
