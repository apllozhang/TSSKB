---
name: Resource Manager 运维：备份恢复/镜像升级/自动开通/SAA
description: 需要备份与恢复交换机配置、导入镜像并升级（含 ISSU/U-Boot）、配置 Auto Configuration 自动开通、零接触 Provisioning（含 Thin Switch）、部署 SAA 服务质量探针时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- 定期备份全网配置、恢复到原设备
- 批量升级 AOS 镜像（Image / BMF / U-Boot / ISSU）
- 新交换机零接触上线（Provisioning Rule）或瘦交换机部署
- 交换机间/VM 间 RTT、抖动、丢包拨测

## I（核心理念）
Resource Manager 管存量设备生命周期：Backup 三类型（Full/Configuration Only/Images Only），镜像不物理备份只记录版本号；Upgrade Image 走 Repository+File Set，FTP 超时 5 分钟是大文件升级的头号坑。Provisioning 是 DHCP Option 43 + Cloud Agent Call-Home + SSH 推模板的零接触链路。SAA 是交换机侧 MACSAA 探针，OV 只做编排与展示。

## A1（行动框架）
1. **备份方式选型**（principles·P143，<<<PAGE 488-493>>>）：按设备（默认）/按地图（>50 台建议）/按 AP Group（Stellar AP 只能按组备）；类型 Full（Certified 或 All）/Configuration Only（可选排除 Security Files）/Images Only
2. **Provisioning 工作流**（frameworks·F11，<<<PAGE 430-436>>>）：DHCP（Option 43 Sub128=as-lite.myovcloud.net + Sub134=443）→DNS 解析到 OV→Cloud Agent 每 5 分钟 Call-Home→匹配 Rule（序列号/MAC/型号）→SSH 推 Management+Configuration 模板→入 Managed Devices
3. **Thin Switch 模型**（frameworks·F12，<<<PAGE 436-438>>>）：AOS 8.8R1+；交换机自身不知道自己是瘦模式；write memory 失效；规则只按序列号/MAC 匹配；Desired Switch Config 三选（Template+Incremental / 备份快照 / Golden Config 快照）

## A2（操作步骤）
- **执行备份**：Resource Manager→Backup/Restore→Backup：Backup Method→Device Selection→Configuration（类型+目录+Diagnostic Dump+排程 Daily/Weekly/Monthly）→Review→Backup（cases·C49，<<<PAGE 488-491>>>）
- **升级镜像**：Upgrade Image→Import（ALE zip 自动解包）→选 File Set→Install→Firmware File Selection（AP 组全选不可取消）→Devices Selection→Software Installation（Upgrade BMF/Images/U-Boot all NIs/ISSU/目录）→Install→完成后到 Topology 重启设备→再 Copy Working to Certified（cases·C50，<<<PAGE 496-499>>>）
- **Auto Configuration 四步**：DHCP Option 66（OV TFTP 地址）+67（Instruction File 路径）→编写 Script File→文件放 FTP/SFTP→Auto Configuration→Add 建 Instruction File（.alu+主备服务器+版本号）；已部署交换机删 boot.cfg 重启触发（cases·C51，<<<PAGE 505-506>>>）
- **部署新交换机（Provisioning 全流程）**（cases·C42，<<<PAGE 433-434>>>）：DHCP/DNS 预配置→Default Mgmt Users Template 配凭据→Add 建 Rule→控制台 reload from working no rollback-timeout→8.6R1- 需 CLI 启用 Cloud Agent→接入自动匹配
- **部署 Thin Switch**（cases·C43，<<<PAGE 437-438>>>）：满足 DHCP/DNS/NTP→Rules→Add（Thin Switch=Yes）→重启或 cloud-agent enable 触发 Call-Home→OV 自动备份
- **Provisioning 排障**：Results 屏看 Last Provisioning Message；最常见是 SSH/SFTP 凭据错；日志 Audit→Configuration→resource-manager-client-service（cases·C44，<<<PAGE 439>>>）
- **创建 SAA**：前置启用 8 个 alaSaa* trap + SAA Settings；SAA→Ethernet OAM→Add：Ethernet Config（Name ≤32 字、源目的 IP、RTT/Jitter/Packet Loss 阈值、Interval）+ MAC Config（VLAN、包数、Payload）→Create（cases·C52，<<<PAGE 513-515>>>）

## E（实证案例）
- Backup by Devices 全流程（含排程）（cases·C49，<<<PAGE 488-491>>>）
- 镜像导入到 Install 到重启生效（cases·C50，<<<PAGE 496-499>>>）
- Provisioning 全流程 + 排障 + Thin Switch（cases·C42/C43/C44，<<<PAGE 433-439>>>）
- 交换机间 SAA 创建（cases·C52，<<<PAGE 513-515>>>）

## B（反例/坑）
- 备份文件含源机器 IP/MAC 二进制信息，拷到其他机器可能搞瘫网络（counter·X41，<<<PAGE 493>>>）
- Image 文件不真正备份；Restore 前必须先把镜像导入 Upgrade Image Repository（counter·X42，<<<PAGE 489-490>>>）
- FTP 默认 5 分钟超时导致大镜像升级失败——先 CLI 调大 `session ftp timeout`（counter·X43，<<<PAGE 497>>>）
- 先升 Image 再升 U-Boot/Miniboot，顺序不能颠倒（counter·X44，<<<PAGE 497>>>）
- 混合地图备份漏掉 Stellar AP——Stellar AP 只能按 AP Group 备（counter·X47，<<<PAGE 488>>>）
- Restore 只能还原到原设备；还原后必须重启（principles·P144，<<<PAGE 494>>>）
- Scheduled Upgrade：高于目标版本的设备会被降级（有提示）；Unsaved 设备被静默跳过（counter·X27/X28 / principles·P84，<<<PAGE 292-296>>>）
- Provisioning 模板含禁用命令（user admin password、write memory、configuration apply）必失败（counter·X34 / principles·P128，<<<PAGE 442-443>>>）
- OV 收不到配置确认回执时谎报 Succeeded——连接丢失/SSH 超时场景要复核（counter·X35 / principles·P131，<<<PAGE 455-456>>>）
- Certified 目录运行的交换机不能 Enforce Golden Config；从 Certified 目录 provision 的配置是临时的，重启即丢（counter·X36/X37，<<<PAGE 434-435, 452>>>）
- Thin Switch 属性一经 provision 不可改；Incremental Template 仅首次 Periodic Call-Home 后应用一次（principles·P124，<<<PAGE 437-438>>>）
- 同一设备同时有序列号与 MAC 规则时序列号优先；序列号/MAC 与型号互斥；每型号仅一条规则（principles·P127，<<<PAGE 439-440>>>）
- SAA：最多 127 个（建议 ≤50）；交换机未保存配置重启后 SAA 残留不可改删，需重新发现清除；运行中的 SAA 不能删（principles·P149，<<<PAGE 512-514>>>）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide 第 24 章 Provisioning（<<<PAGE 429-456>>>）、第 27 章 Resource Manager（<<<PAGE 487-510>>>）、第 28 章 SAA（<<<PAGE 512-521>>>）、Scheduled Upgrades（<<<PAGE 292-296>>>）。条目来源：frameworks F11/F12；cases C42-C44/C49-C52；counter-examples X27/X28/X34-X37/X41-X44/X47；principles P84/P122-P131/P143-P151。
