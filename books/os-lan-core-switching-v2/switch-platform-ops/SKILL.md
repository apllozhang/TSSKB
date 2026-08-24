---
name: 交换机平台运维（链路聚合/SLB/软件升级）
description: 需要配置链路聚合、服务器负载均衡（SLB/VIP/健康探测）或执行 AOS 软件升级（含 uboot/FPGA 回滚）时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 上行/核心互联带宽扩容与冗余，需要 LACP 链路聚合
- 本地服务器集群需要 VIP 负载分担与健康探测容灾
- 计划升级 AOS 版本，要求可回滚、含 uboot/FPGA 的完整流程

## I（核心理念）
平台层三件事的共同底座是 working/certified 双镜像目录：升级先落在 working、验证无误再 `copy running certified`，出问题 reload 即回滚。SLB 的本质是"交换机用 proxy ARP 截住发往 VIP 的桥接流量并强制路由"，配合权重轮询与探测实现本地容灾；WRR 权重 0 表示备份服务器，总权重不超过 32。

## A1（行动框架）
1. 链路聚合：`linkagg lacp agg 1 size 2...`；加口前必须先清掉端口上的 VLAN 配置（`no vlan 58/20/30 members port 2/1/3`），否则报 "Port cannot be added to Linkagg, please remove other configuration on this port"（<<<PAGE 316>>>）
2. SLB：`ip slb admin-state enable` → `ip slb cluster Web vip 128.241.130.204` → `ip slb server ip 128.241.130.127 cluster Web`；备份用 `weight 0`（主 `weight 1`）；探测 `ip slb probe http_test http` + `ip slb server ip ... probe http_test`（<<<PAGE 655>>>-<<<PAGE 658>>>、<<<PAGE 667>>>）
3. 服务器侧：在服务器 loopback 接口上配 VIP（Windows/Linux 附录 p671-672）；VIP 必须与服务器同网段（<<<PAGE 653>>>-<<<PAGE 654>>>）
4. 软件升级流程链：读 release note → FTP 上传 → 升级 image → 验证 → certified → 按需升 uboot/FPGA：`update uboot cmm all file u-boot.8.4.1.R03.141.tar.gz` / `update fpga-cpld cmm all file fpga_kit_3312` → `reload from working no rollback-timeout` → `copy running certified`（<<<PAGE 676>>>-<<<PAGE 680>>>）

## A2（进阶应用）
- SLB 桥接网络原理：cluster 自动对 VIP 生成 proxy ARP（交换机 MAC），把桥接包强制引到路由路径（<<<PAGE 654>>>、<<<PAGE 662>>>）
- 8.9R4 起 auto-bypass/wait-to-restore 容灾增强（<<<PAGE 665>>>）
- 实验环境回收：删除用户自定义目录后 `reload from working no rollback-timeout`（<<<PAGE 62>>>-<<<PAGE 63>>>）
- 无 STP/LAG 场景的接入冗余可用 DHL（Dual-Home Link）双归链路快速倒换（<<<PAGE 318>>>、<<<PAGE 607>>>）

## E（实证案例）
- C-40 SLB 集群：VIP+WRR（weight 1/0 主备）+ HTTP probe（<<<PAGE 655>>>-<<<PAGE 658>>>、<<<PAGE 667>>>）
- C-38 软件升级含 uboot/FPGA 与 certified 收尾（<<<PAGE 676>>>-<<<PAGE 680>>>）

## B（边界与陷阱）
- 端口有 VLAN membership 时不能加入聚合组，先清 VLAN 配置（<<<PAGE 316>>>）
- WRR 所有服务器权重之和不超过 32；weight 0 表示备份（<<<PAGE 656>>>）
- certified 之前reload 可回滚——升级验证未完成前不要急着 `copy running certified`（<<<PAGE 680>>>）

## 来源
- framework·F-15 SLB 部署框架（<<<PAGE 655>>>-<<<PAGE 658>>>、<<<PAGE 665>>>）
- principle·P-67 SLB VIP 与 Proxy ARP（<<<PAGE 653>>>、<<<PAGE 654>>>、<<<PAGE 662>>>）
- case·C-03/C-38/C-40；counter·X-13
- glossary·working/certified directory（<<<PAGE 53>>>、<<<PAGE 680>>>）、DHL（<<<PAGE 318>>>、<<<PAGE 607>>>）
