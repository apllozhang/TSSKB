---
name: wlan-trouble-methodology
description: 何时用：接手任意 WLAN 故障（连不上/慢/掉线）需要系统化定位时，先用本 skill 定流程、定层、收窄范围，再进各专项 skill。
source_book: DT00XTE478EN Stellar WLAN Advanced Troubleshooting
---

# WLAN 排障总方法论：七步流程 · 三域根因地图 · 访谈四问

## R · 原文引用

> Identify: Determine if problem exists, Ask questions & collect infos. Locate: Tied to physical space, Tied to specific devices, Use OSI model to define layer. Isolate: Identify OSI Layer, Specific devices, Specific locations, Driver versions. Re-Create: If you can't recreate this issue, return to step one and ask more questions. Solve: Formulate & Implement plans. Verify: Extensive testing to confirm and verify the solution did indeed solve the issue. Document: Document initial issues, processes, diagnostics & resolutions. (p10)

> Wireless: End User, Wi-Fi Device, Client, RF Medium, Stellar AP. Local Network: LAN, Switch, Firewall & WAN Router, Servers (DHCP Configuration, Lease duration, Address Pool scope, DHCP options; DNS; 802.1X/RADIUS; LDAP/AD). Internet: Bandwidth Throttling, Jitter, Latency, External DNS, External Captive Portal - Issues independent from the network administrator. (p5-8)

> Same behavior for all users? Yes - The issue is not related to a specific device/hardware. In the same section of the building - Not a global OmniVista configuration issue. The impacted clients are all associated to the Stellar APs connected to the same access switch? Yes - The issue might come from the SSID configuration or the access switch configuration. Same issue on other SSIDs in the same location? No, only the connection to the Employee SSID is impacted. (p17)

> Test the solution in your environment. Apply the correction in the customer environment. Document the troubleshooting case: Issue description, Topology, Firmware versions, Diagnostic, Resolution. Follow the case - Check that the solution is permanent - No side effects due to the resolution. (p13-14)

## I · 方法论骨架

**七步流程（含回退规则）**

1. **Identify 识别**：问问题、收集信息，确认问题真实存在
2. **Locate 定位**：绑定物理空间、具体设备，用 OSI 模型定层
3. **Isolate 隔离**：锁定 OSI 层、具体设备、具体位置、驱动版本
4. **Re-Create 复现**：在自有环境重建；**无法复现 → 回到第 1 步重新提问**（核心回退规则）
5. **Solve 解决**：制定并实施方案（驱动/配置/设计变更）
6. **Verify 验证**：充分测试确认修复有效
7. **Document 记录**：记录问题、过程、诊断、解决方案，沉淀到 ALE TKC 知识库

**三域根因地图（排障前扫一遍，保证不漏层）**

| 域 | 检查要素 |
|---|---|
| 无线侧 | 终端用户技能/设备开关、驱动、射频能力、802.1X 配置文件、最低速率要求、漫游算法、关联/认证/加密/上层协议、RF 介质（RSSI/SNR/覆盖）、AP 配置与固件 |
| 本地网络侧 | PoE/天线/布放/物理层、交换机 VLAN/端口速率/QoS、防火墙 ACL/NAT/限速、DHCP（租期/地址池/选项）、DNS、RADIUS/LDAP/AD 服务器群 |
| 互联网侧 | 出口带宽、抖动时延、外部 DNS、外部门户——**不在网络管理员管控内**，先划出去再排 |

**访谈四问（逐级收窄，每个答案决定下一问方向）**

| 问 | 答案 → 推断 → 下一步 |
|---|---|
| 1. 所有用户都受影响？ | 是 → 排除个别终端硬件问题 |
| 2. 固定位置还是全楼？ | 固定区域 → 排除全局 OmniVista 配置问题 |
| 3. 都挂在同一台接入交换机下？ | 是 → 指向 SSID 配置或该交换机配置 |
| 4. 同位置其他 SSID 正常？ | 只影响单个 SSID → 锁定该 SSID 的 VLAN/配置 |

**定层后导航（先低层后高层）**

- 基础层（AP 硬件/系统/门户/集群）→ `stellar-ap-system-health`
- 无线层（SSID/RF/热图/漫游）→ `wireless-rf-roaming-trouble`
- 客户端层（关联/取址/掉线/认证）→ `client-connection-trouble`、`dot1x-radius-trouble`
- 网络层（AP 取址/连通/邻居/服务器）→ `network-side-trouble`

## A1 · 书中案例

主案例（p11-18）：整栋楼客户端登不进 Employee SSID。访谈四问锁定范围后取 AP 日志与交换机配置比对：OmniVista 里 SSID 映射 VLAN 10，接入交换机 Building_A 上配的是 VLAN 20，tagged VLAN 不一致导致认证后拿不到正确子网。Resolution：更新交换机 tagged VLAN ID=20。教训：**全员连不上而 AP 本身正常 → 优先怀疑交换机侧 VLAN**。

复现法案例（p12）：向客户采集四类配置——接入交换机 vcboot.cfg、OmniVista 组织配置、Stellar AP 配置备份、服务器配置备份——在自有环境 1:1 重建拓扑后重现问题，排除客户描述偏差与隐藏根因。

## A2 · 触发场景（含与相邻 skill 的区分）

- 任何故障刚接手、还不知道从哪查起时，**必先走本 skill**。
- 与专项 skill 的区分：本 skill 只负责"怎么问、怎么定层、怎么收窄、怎么收尾"；具体命令与阈值在四个分层 skill 与工具箱 skill 中。已明确是某层问题的直接进对应 skill。
- TKC 检索：当故障疑似已知问题时，按"版本比对三分支"查 TKC——同版本看 Resolution；案例版本更旧则可能已被新 build 修复；套用前**必须亲自重复诊断步骤且结论一致**，否则换用例或联系技术支持创建新用例（p127-130）。

## E · 可执行步骤

1. 排障前置：确认全网（AP、OmniVista、接入交换机）同步到同一 NTP 服务器，否则多设备日志无法对齐成时间线（p22）。
2. 执行访谈四问，写下每一问的答案与推断。
3. 对照三域根因地图列出嫌疑项，按 OSI 从低层到高层排序。
4. 需要复现时按四类配置清单采集（vcboot.cfg / OmniVista 组织 / AP 备份 / 服务器备份），自有环境重建并复现；复现失败回第 2 步重新提问。
5. 制定方案 → 先自有环境测试 → 应用到客户环境 → 让客户用日常业务（Rainbow、语音、邮件）验证稳定性。
6. 关单标准：方案永久有效且无副作用；记录五字段（问题描述/拓扑/固件版本/诊断/解决方案），沉淀 TKC。

## B · 边界与陷阱

- **无 NTP 的代价**：教材演示 Error 10 事件，AP 日志显示 10/11/2019 08:15:30，OmniVista 与交换机显示 15/11/2019 13:15:30，相差五天，关联分析直接失效。跳过对时直接翻日志是第一大弯路。
- 一上来就怀疑高层（认证/DNS）而实际是 PoE/VLAN 底层问题——先低层后高层。
- 复现失败时不要硬造解释，规则明确要求回第一步重新提问。
- 修复后不做客户真实业务验证就关单，副作用无从发现。
- 本 skill 不含具体命令；阈值与命令判读见各分层 skill。

---
来源条目: f01, f02, f03, f04, f05, f08, f10, ce01, ce19, p01（术语 g10 Cluster, g12/g13 OmniVista, g14 TKC, g31 Final_role, g32 NTP）
