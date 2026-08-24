---
name: 交换机高可用架构（VC/LACP/STP/DHL/VRRP）
description: 当需要做交换机冗余设计——Virtual Chassis 堆叠、LACP 链路聚合、STP 防环与负载分担、DHL Active-Active、VRRP 网关冗余——时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 两台交换机要堆叠成单逻辑设备（Virtual Chassis）并配置 VFL
- 上行带宽不够/单链路故障，要做 LACP 聚合并验证倒换不丢包
- 双核心冗余：STP 根桥规划、DHL 双活、VRRP 主备/负载分担

## I（核心理念）
高可用是一组可组合的机制：VC 把多台交换机虚拟成一台（免 STP/VRRP、免许可证）；LACP 聚合带宽并抗单口故障；STP 在冗余路径上阻塞防环，per-VLAN 1x1 模式可分根桥负载分担；DHL 用"按 VLAN 划分活跃链路"替代 STP 做双活；VRRP 用虚拟 MAC 提供网关冗余。

## A1（行动框架）
1. **Virtual Chassis 堆叠**（<<<PAGE 490>>>-<<<PAGE 497>>>）：`show chassis` 定型号 → A 机 `virtual-chassis chassis-group 1` + `chassis-id 1 configured-chassis-priority 200` → `write memory` + `reload from working no rollback-timeout` → B 机 `chassis-id 1 configured-chassis-id 2` + `chassis-group 1` → 重启 → 双方 `virtual-chassis vf-link-mode auto` + `auto-vf-link-port 1/1/27` → `interfaces 1/1/27-28 admin-state enable` → `show virtual-chassis topology` → `write memory flash-synchro` 同步 → `show virtual-chassis consistency` → `ssh-chassis admin@2` 访问从机。
2. **LACP 动态聚合**（<<<PAGE 588>>>-<<<PAGE 594>>>）：双端 `linkagg lacp agg 7 size 2 actor admin-key 7` → `linkagg lacp port 1/1/3 actor admin-key 7`（VC 下可跨机箱 1/1/3+2/1/4）→ `show linkagg` 验证 → `vlan 57 members linkagg 7 untagged` 设默认 VLAN → ping -t 期间 disable 一个成员口验证不丢包。
3. **STP 根桥指定**（<<<PAGE 616>>>-<<<PAGE 625>>>）：`spantree vlan 20 priority 20000` → `show spantree vlan 20`（Bridge ID=Designated Root）→ `show spantree ports blocking` 看阻塞口 → 断聚合口验证 RSTP 秒级收敛；1x1 负载分担：6870 VLAN 20 priority 20000、6860 VLAN 30 priority 20000（各管一个 VLAN 当根）。
4. **DHL Active-Active**（<<<PAGE 640>>>-<<<PAGE 643>>>）：清端口 VLAN 配置 → 建 linkagg 8 → `vlan 57 members linkagg 8 untagged`、20/30 tagged → `dhl 1` → `dhl 1 linka linkagg 7 linkb linkagg 8` → `dhl 1 vlan-map linkb 30` → `dhl 1 admin-state enable` → `dhl 1 mac-flushing raw` → `show dhl 1` → 断 agg7 验证 VLAN20 转移到 agg8。
5. **VRRP 主备**（<<<PAGE 684>>>-<<<PAGE 689>>>）：双机各建 int_20/int_30 → `ip vrrp 1 interface int_20` + `address 192.168.20.254` + `admin-state enable` → `show ip vrrp statistics` 看 Master/Backup → 改优先级先 disable：`ip vrrp 1 interface int_20 admin-state disable` → `priority 150` → `enable` → 重启主机验证 Backup 秒级接管，客户端 ARP 表里 192.168.20.254 的 MAC=00-00-5E-00-01-01。

## A2（进阶应用）
- **VC 进阶**：Master 选举顺序为最高 priority → 最长 uptime（>10min 差）→ 最小 chassis ID → 最小 MAC（<<<PAGE 472>>>）；分裂双检测：out-of-band RCD（走 EMP，原 Slave 关闭全部前面板口防 IP/MAC 冲突）+ in-band VSCP（需上游/下游 helper switch）（<<<PAGE 476>>>-<<<PAGE 477>>>）；ISSU 逐台 slave 从低到高 chassis ID 依次重启升级（<<<PAGE 478>>>）。
- **STP 模式**：flat（单实例）/ per-VLAN（OmniSwitch 默认）× STP(802.1d, 50s) / RSTP(802.1w, <1s) / MSTP(802.1s)（<<<PAGE 604>>>）。
- **负载分担哈希**：brief 模式不含 UDP/TCP 端口，extended 含之、分流更均匀；6900/6465/6360 默认 brief，其余默认 extended（<<<PAGE 583>>>）。
- **LACP 细节**：Dynamic（802.3ad LACPDU 协商）与 Static（仅 OmniSwitch 间）两种；actor admin key 仅本地有效（<<<PAGE 576>>>、<<<PAGE 588>>>）。
- **VRRP 负载分担**：双 VRID 各主一个 VLAN（VRID1 主 VLAN20、VRID2 主 VLAN30）；虚拟 MAC 00-00-5E-00-01-{VRID}，组播 224.0.0.18（<<<PAGE 674>>>-<<<PAGE 675>>>）。

## E（实证案例）
- 6360 两台 VC 堆叠 + flash-synchro + ssh-chassis 访问从机（<<<PAGE 490>>>-<<<PAGE 497>>>）。
- LACP linkagg 7 跨 VC 机箱聚合，ping -t 期间 disable 成员口不丢包（<<<PAGE 588>>>-<<<PAGE 594>>>）。
- VRRP 双活：改优先级实现 6870 主 VLAN20 / 6860 主 VLAN30，重启主机 Backup 秒级接管（<<<PAGE 684>>>-<<<PAGE 689>>>）。

## B（边界与陷阱）
- **VRRP 改 priority 必须先 disable 实例**，否则不生效（<<<PAGE 689>>> Warning）。
- **端口有 VLAN/默认 VLAN 配置时无法加入 linkagg**：报 "Port cannot be added to Linkagg, please remove other configuration on this port"；先 `no vlan XX members port …` 清干净（<<<PAGE 640>>>）。
- **DHL 与 STP 互斥**（DHL 端口自动关 STP）且默认 mac-flushing=none 会保留过期 MAC，生产建议显式 `dhl 1 mac-flushing raw`（或 mvrp）（<<<PAGE 630>>>、<<<PAGE 642>>>）。
- VC 内无 STP/VRRP（Access-Core 之间），升级走 ISSU（<<<PAGE 468>>>、<<<PAGE 471>>>）。

## 来源
- principles·P27 Virtual Chassis 原理（<<<PAGE 468>>>、<<<PAGE 471>>>-<<<PAGE 472>>>）
- principles·P28 VC 分裂双检测（<<<PAGE 476>>>-<<<PAGE 477>>>）
- principles·P29 ISSU（<<<PAGE 478>>>）
- principles·P30 STP 模式（<<<PAGE 604>>>）
- principles·P31 STP 1x1 负载分担（<<<PAGE 606>>>、<<<PAGE 622>>>）
- principles·P32 LACP（<<<PAGE 576>>>、<<<PAGE 588>>>）
- principles·P33 哈希算法（<<<PAGE 583>>>）
- principles·P34 DHL（<<<PAGE 628>>>-<<<PAGE 630>>>）
- principles·P35 VRRP（<<<PAGE 674>>>-<<<PAGE 675>>>）
- cases·C24/C25/C27/C28/C29（<<<PAGE 490>>>-<<<PAGE 497>>>、<<<PAGE 588>>>-<<<PAGE 594>>>、<<<PAGE 616>>>-<<<PAGE 625>>>、<<<PAGE 640>>>-<<<PAGE 643>>>、<<<PAGE 684>>>-<<<PAGE 689>>>）
- counter-examples·X9/X10/X11（<<<PAGE 689>>>、<<<PAGE 640>>>、<<<PAGE 630>>>、<<<PAGE 642>>>）
