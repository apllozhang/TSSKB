---
name: ov2500-sizing-and-platform-planning
description: 何时用：规划 OV2500 4.9R2 部署的规模档位、虚拟化平台兼容性与 CPU/内存/磁盘配置时。
source_book: OV2500 4.9R2 Installation and Upgrade Guide
---

# OV2500 部署规划与系统配置（四档规模 · 三平台矩阵 · 资源常数）

## R · 原文引用

> "Total Number of Managed Devices 500 / 2,000 / 5,000 / 10,000 ... Hypervisor Processor 2.4 GHz, 8 Logical Processors (12 for High/Very High) ... Minimum Reserved OmniVista VA RAM for Standalone 20GB / 36GB / 64GB / 64GB ... Minimum Reserved RAM for HA N/A / 40GB / 64GB / 64GB ... Minimum Storage Read/Write Speed 100 / 150 / 200 / 200 MB/s" (p9)

> "OV 2500 NMS 4.9R2 is distributed as a Virtual Appliance only. There are no other standalone installers (e.g., Windows/Linux)... VMware ESXi: 6.5, 6.7 and 7.0.2, 8.0; MS Hyper-V: 2012 R2, 2016, 2019, and 2022; MS Hyper-V on Windows 10 Professional; Linux KVM/Ubuntu 22.04." (p8)

> "When provisioning RAM for a new VM for OmniVista, never allocate more memory than is available on the Host Server... it is recommended that you reserve that RAM for the OmniVista VM to prevent performance issues. Set CPU Shares to 'High'. Do not exceed the number of Logical Processors recommended for your network size." (p10)

> "OmniVista will not allow you to configure a network size that cannot be supported by the VA configuration. For example, if you allocate 20GB of memory for the OmniVista VA, OmniVista will only allow you to configure a Low network size (fewer than 500 devices)." (p8-9)

## I · 方法论骨架

1. **定档位**：按管理设备总数选 Low(<500)/Medium(500-2000)/High(2000-5000)/Very High(5000-10000)，四档常数见下表。
2. **定平台**：仅 VA 交付、无裸机安装器；在 ESXi 6.5-8.0 / Hyper-V 2012R2-2022（含 Win10 专业版）/ KVM（Ubuntu 22.04）三平台中选，并核对不支持项。
3. **配资源**：CPU 2.4GHz、8 或 12 逻辑核（不超配）；内存不超宿主机实际可用、在 Hypervisor 里"预留"、CPU Shares=High；存储读写速度达标。
4. **通网络**：443 端口放行 6 个外部域名（或配代理）；管理端口按默认/范围规划。

核心常数表：

| 项目 | Low | Medium | High | Very High |
|---|---|---|---|---|
| 管理设备总数 | 500 | 2,000 | 5,000 | 10,000 |
| Stellar AP 上限 | 500 | 2,000 | 4,000 | 4,000 |
| AP 客户端关联 | 5 万 | 20 万 | 20 万 | 20 万 |
| UPAM 认证客户端 | 2 万 | 5 万 | 7.5 万 | 10 万 |
| 逻辑处理器 | 8 | 8 | 12 | 12 |
| 内存（Standalone） | 20GB | 36GB | 64GB | 64GB |
| 内存（HA） | 不支持 | 40GB | 64GB | 64GB |
| 磁盘分区 2 | 512GB | 1TB | 2TB | 2TB（分区 1 固定 50GB） |
| 存储读写速度 | 100 | 150 | 200 | 200 MB/s |

混合换算：High 档 4000 台 Stellar AP 时最多再带 500 台 AOS 交换机；Very High 档 4000 AP 时 AOS 可达 1000 台（HA Very High 1500 台）。

外部站点白名单（443 端口）：ovrepo.fluentnetworking.com（ALE 中央仓库）、ep1.fluentnetworking.com（AV 签名库）、myfleet.ovcirrus.com（Fleet Supervision）、us.fluentnetworking.com（Call Home）、api.fingerbank.org（设备指纹）、api.bcti.brightcloud.com（网页内容过滤）。不直连互联网必须配代理（VA 菜单 Configure Proxy）。

端口常数：OV Web 默认 HTTP 80 / HTTPS 443；Captive Portal 默认 8080 / 8443；合法范围均 1024-65535 且不得重复；SSH 2222（cliadmin）、SFTP 22。

评估许可：生成日起 90 天全功能，单文件含全部设备与服务许可；ALE 门户 lds.al-enterprise.com，Customer ID=99999、Order Number=evaluation、Passcode=omnivista。

## A1 · 书中案例

- 只给 VA 分 20GB 内存 → OmniVista 只允许配 Low 档（500 台以下），系统直接拒绝超配档位（p8-9）。
- 宿主机 128GB 已分出 96GB 给其他 VM，再给 OV 按 64GB 档分配即超出实际可用——内存必须按宿主机实余量规划（p10）。
- Hyper-V 用户想用 Live Migration 在线挪 OmniVista VM、或在新版 Hyper-V 2019+ 上跑 VM Manager——两者均不受支持，规划平台版本时要避开（p19）。

## A2 · 触发场景（含与相邻 skill 的区分）

- **用本 skill**：新部署前的容量选型、平台版本核对、CPU/内存/存储/端口/代理/许可规划——即"装之前"的所有决策。
- 与 `ov2500-install-on-esxi-hyperv-kvm` 的区分：那一个是"装的时候"三平台逐步操作与初始向导；本 skill 只管决策常数。规格数字不确定时先回本 skill 查表。
- 与 `ov2500-ha-cluster-design-and-conversion` 的区分：HA 拓扑选型（L2/L3）、转换步骤归那一个；本 skill 只提供"HA 必须 Medium 及以上、上限 4000 设备"这个容量门槛。

## E · 可执行步骤

1. 统计目标网络设备数（AOS 交换机 + 第三方 + Stellar AP），对照常数表定档位；AP 达 4000 且还需大量 AOS 时按混合换算复核。
2. 确认 Hypervisor 平台与版本在兼容矩阵内；Hyper-V 场景记录两条禁项（不支持 Live Migration；VM Manager 仅 2012/2012R2/2016）。
3. 按档位分配资源：2.4GHz CPU、8/12 逻辑核不超配；内存按 Standalone/HA 列配足并在 Hypervisor 中勾选预留（Reservation），CPU Shares 设 High；分区 1 50GB + 分区 2 按档；存储实测读写 ≥100/150/200/200 MB/s。
4. Intel CPU 检查 AES-NI（SNMPv3 AES 性能依赖）：BIOS 开启且未被 Hypervisor 屏蔽（mask）。
5. 防火墙放行 6 个域名:443，或规划代理；记录管理端口（默认 80/443/8080/8443，如改须在 1024-65535 内且不重复）。
6. 试用场景走评估许可流程；正式场景提前在 ALE 门户生成许可文件。
7. 输出一页规划清单（档位/平台/资源/端口/代理/许可）供安装阶段照单执行。

## B · 边界与陷阱

- **没有 Windows/Linux 独立安装器**——客户坚持裸机部署时无解，只能上三平台 Hypervisor 之一。
- Low 档不支持 HA；HA 上限 4000 设备且必须 Medium 及以上规格（p11）。
- 内存超配宿主机、逻辑核超过档位推荐值、不预留内存，都是官方明示的性能事故来源（p10）。
- Hyper-V 上不支持 Live Migration；VM Manager 不支持 Hyper-V 2019+（p19）。
- 版本强绑定 4.9R2，常数随版本可能变化（如 4.6R2 起 Medium 内存上调至 Standalone 36GB / HA 40GB，见升级 skill）。
- 云部署（Azure/AWS）不在本册范围。

---
来源条目: p01, p02, p03, p04, p05, p06, p22, p23, p30, p31, g16, g21, ce17
