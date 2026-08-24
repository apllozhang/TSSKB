# OV2500 4.9R2 部署精华：不读全书，先看这一篇

> 目标读者：要交付、改造或升级 OmniVista 2500 网管平台的工程师。数字全部带页码，出处为 OV2500 4.9R2 Installation and Upgrade Guide（326 页）。

## 一、一页看懂 OV2500 部署

**交付形态只有一种**：4.9R2 以虚拟设备（VA，Virtual Appliance）发布，没有 Windows/Linux 裸机安装器，客户坚持物理机部署无解，只能上 Hypervisor（p8）。支持三平台：VMware ESXi 6.5/6.7/7.0.2/8.0、Microsoft Hyper-V 2012R2-2022（含 Win10 专业版）、Linux KVM（Ubuntu 22.04）（p8）。

规模四档（p9），装之前先把档位定死——系统会按 VA 实际资源拒绝超配，分了 20GB 内存就只能选 Low 档（p8-9）：

| 项目 | Low | Medium | High | Very High |
|---|---|---|---|---|
| 管理设备总数 | 500 | 2,000 | 5,000 | 10,000 |
| Stellar AP 上限 | 500 | 2,000 | 4,000 | 4,000 |
| 逻辑处理器（2.4GHz） | 8 | 8 | 12 | 12 |
| 内存 Standalone / HA | 20GB / 不支持 | 36GB / 40GB | 64GB / 64GB | 64GB / 64GB |
| 数据分区（分区1固定50GB） | 512GB | 1TB | 2TB | 2TB |
| 存储读写速度 | 100 | 150 | 200 | 200 MB/s |

资源三条硬规矩：内存不超宿主机实余量且必须预留（Reservation）、CPU Shares 设 High、逻辑核不超档位推荐值（p10）。另需放行 6 个外部域名的 443 端口（或配代理），评估许可在 lds.al-enterprise.com 用 99999/evaluation/omnivista 生成，90 天全功能（p22-23）。

## 二、安装主线：部署 → 向导 → 首检

1. **导 VA**：按平台取包（ESXi 用 OVF+VMDK，KVM 用 qcow2 双盘），部署 VM 但**不要提前挂扩展盘**——必须等 OmniVista 配置完并重启后再加（p10）。KVM 系统盘选 VirtIO 总线并设 Discard=unmap（p33）。
2. **初始向导**（VM Console）：设 Technical Support Code 密码 → 设 cliadmin 密码（**丢失无法找回，只能重装**）→ 主机名（≤15 字符小写）→ 三个 IP（OV / Captive Portal / 附加 Web，推荐各自独立子网+独立网卡）→ NTP。
3. **首检**：重启后加盘/加网卡；首次登录 https://<服务器IP> 导入许可；Watchdog 里确认全部服务 Running。日常菜单入口：Console 或 SSH 2222 端口 cliadmin，SFTP 22 传证书和备份（p272）。

## 三、HA 双集群要点

- **资格**：HA License 已导入、规格 ≥Medium、设备 ≤4000；来源必须是全新 4.9R2 或从 ≥4.3R2 升级而来（4.3R1 来源不能转，p40-41）。
- **L2 还是 L3（一锤定音）**：L2 两节点同子网+虚拟 Cluster IP，设备零改动、功能完整；L3 跨子网，受限一串——sFlow、AOS Policy、Captive Portal 不支持，IoT 需重应用，Syslog 需外部服务器，L3 冗余仅 AP13XX+（AWOS 5.0+），且必须配 Preferred Node（p41-42）。**L2 不能转 L3，L3 只能全新搭建**（p40-41）。能同子网就选 L2；最佳实践是把原 Standalone IP 腾出来当 Cluster IP（p21, p40）。
- **转换步骤**：备份+快照后，Node1 菜单 12 Convert to Cluster → Node2 菜单 13 Join Cluster，全程 Console 做、禁止 SSH；转换向导里已配置的 Captive Portal 保持默认回车，别改（p46）。网络基线：节点间 1Gbps 带宽、1ms 延迟（p42）。
- **脑裂防护/日常铁律**：任何操作前看 Show OV Cluster Status，Data Sync 必须 "Up to Date"（显示百分比=同步中，此时做配置变更可能被覆盖分叉，p296）；集群级操作只在 Active 节点做；集群初始化后不要改 Peer Node 信息，要改先备份再联系客服（p303）；被 Remove 的节点视同报废不可复用（p299）。Standby 节点上 upam、nginx 显示 Stopped 是预期行为，不是故障（p52）。

## 四、升级路径速查

- **升级链（唯一路径，逐级走）**：4.5R1→4.5R2→4.5R3→4.6R1→4.6R2→4.7R1→4.7R1 Patch 2→4.8R1→4.8R2→4.9R1→4.9R2（p6-7）。旧于 4.5R1 不升级，改"备份+全新安装+重导配置"。
- **停机窗口（报审批用）**：Standalone 全程不可管理 1-4 小时（p60-61）；HA 管理持续可用，仅 failover 中断约 5-10 分钟；例外是 4.7R1→Patch 2 的 HA 升级全程停机。
- **HA 滚动升级（≥4.8R1 新流程）**：确认同步 Up to Date → Active 启维护模式（一次启用双节点生效）→ **先升 Standby** → 升完立即重启并 failover（此时屏幕黄色 WARNING 要忽略）→ 新 Active 服务全起后升原 Active → 验证（p67）。角色互换是正常状态。老流程（≤4.7R1 Patch2）重启时机相反：Standby 升完忍住不重启，两台都升完一起重启——新旧文档混用是最常见事故源（p155-167）。
- **快照时机**：升级/转换前删全部旧快照→拍新快照→操作→验证通过→立即删快照。快照是一次性保险，不是备份；拖着旧快照跑会持续拖累性能（p8）。内置备份保留 1-30 天（默认 7）、份数 1-30（默认 5），恢复只认**同版本**备份文件（p289）。
- **两个菜单陷阱**：4.7R1 Patch 2 不在默认仓库，须建 PatchRepo 自定义仓（URL 不带 https:// 前缀，p143, p146）；4.9R1→4.9R2 必须执行 "3 - To New Release → 0 - Exit → 2 - To 4.9R1" 特殊序列，官方原文 "DO NOT SKIP THIS STEP FOR ANY REASON"（p62）。

## 五、运维红线清单（18 条）

1. 没有裸机安装器，只支持三平台 Hypervisor（p8）。
2. 首装禁止预挂扩展盘；不支持改既有虚拟盘容量（p10）。
3. cliadmin / Technical Support Code 密码丢失无法找回，只能重装。
4. 内存超配宿主机、不预留内存、逻辑核超档位——官方明示的性能事故来源（p10）。
5. Hyper-V 不支持 Live Migration；VM Manager 仅支持 2012/2012R2/2016（p19）。
6. 改 OV IP 不动网络侧：sFlow 接收器、policy server、SNMP trap、Stellar 的 DHCP 与 WLAN 配置全要手动重推（p276）。
7. 升级/HA 转换全程 VM Console，SSH 升级=升级不完整（p60）。
8. 升级只能逐级，没有跨版本直升；升级菜单选项 4 在线场景不受支持（p63）。
9. Low 档不支持 HA；HA 上限 4000 设备、必须 Medium 及以上（p11）。
10. L2 不能转 L3；4.3R1 来源的 Standalone 不能转 HA（p40-41）。
11. Data Sync 同步中（显示百分比）严禁做配置变更（p296）。
12. 集群初始化后改 Peer Node 信息必须先备份并联系客服（p303）；被移除节点报废不可复用（p299）。
13. HA 滚动升级窗口内冻结一切配置变更——Standby 升级阶段的变更会丢（p69）。
14. 恢复只认同版本备份；HA 备份 4.5R1 起才支持（p289）。
15. 快照用完即删，不做长期备份（p8）。
16. 扩容只能加新盘；KVM 新盘必须 SATA 总线且只从第三块起识别——先加两块 1KB 占位盘且永远别删（p280）。
17. 关机必须 Watchdog → Stop All Services → VA 菜单 Power Off；直接关宿主机断电是数据损坏禁忌（p292）。
18. L3 failover 后 AP 假 down 5-10 分钟是正常窗口，别误判去重启设备（p42）。

---
*由 cangjie-skill 流水线从 OV2500 4.9R2 Installation and Upgrade Guide 蒸馏生成*
