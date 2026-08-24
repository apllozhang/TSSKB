---
name: MACsec 二层链路加密部署
description: 需要在交换机间/交换机到主机链路上部署 IEEE 802.1AE 加密（Static SA 或 Dynamic PSK/EAP）时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 核心/汇聚直连链路需要防窃听、防中间人、防重放的线级加密
- 需要选型 Static SA / Dynamic PSK / Dynamic EAP 三种模式之一
- MACsec 会话起不来或密钥轮换策略需要设计

## I（核心理念）
MACsec（802.1AE）用 GCM-AES 对直连链路上几乎所有流量（含 LLDP/LACP/DHCP/ARP）做加密+认证，报文带 SecTag（EtherType 0x88E5）与 16 字节 ICV，按包编号防重放。密钥模型是：每节点收发各一条安全通道（SCI），通道内 SA 持有 SAK；Static 模式手工配 key-chain 交叉引用，Dynamic 模式由 MKA 协商生成 SAK。

## A1（行动框架）
1. 预检：`show interfaces 1/1/27 capability`（MACsec Supported、256-bit）、`show license-info`（<<<PAGE 87>>>）；无 license 时安装：`license apply file licence.dat order-id "..."` → `show license-info` 出现 MACSEC PERM（<<<PAGE 91>>>）
2. 建密钥与密钥链：`security key 1 algorithm aes-cmac-128 hex-key 0x... keyed-name 0x...` → `security key-chain 1` → `security key-chain 1 key 1`（<<<PAGE 89>>>）
3. Dynamic PSK 模式：`interfaces port 1/1/27 macsec mode dynamic key-chain 1 encryption` + `key-rotation max-session-time 10` + `max-exchange-data 20` + `macsec admin-state enable`；验证 `show interfaces macsec dynamic`（Operation Status UP）（<<<PAGE 87>>>-<<<PAGE 90>>>）
4. Static SA 模式：本端 `interface 1/1/25 macsec admin-state enable sci-tx key-chain 1 encryption sci-rx key-chain 2 encryption`，对端 tx/rx 互换；随机密钥 `security key-chain gen-random-key`；删除顺序 disable → no macsec → no key-chain（<<<PAGE 92>>>-<<<PAGE 94>>>）

## A2（进阶应用）
- 模式决策树：交换机间可用 Static 或 Dynamic；交换机到主机用 EAP（802.1X/RADIUS VSAs 下发 CAK）（<<<PAGE 67>>>、<<<PAGE 76>>>、<<<PAGE 79>>>）
- SAK 轮换双门限：会话时长 5-120 分钟与流量 5-1000GB 同时配置，先到先触发（<<<PAGE 77>>>、<<<PAGE 89>>>）
- MKA 双密钥体系：CAK 保护控制平面，key server 动态生成 SAK（<<<PAGE 76>>>）
- 权限：MACsec 命令纳入 security 域（securityadmin read-write MACsec）（<<<PAGE 82>>>）

## E（实证案例）
- C-04 Dynamic PSK 全流程（6870-A↔6860-B）：PSK 双端一致，轮换 10 分钟/20GB（<<<PAGE 87>>>-<<<PAGE 90>>>）
- C-05 Static SA：4 把 aes-gcm-128 密钥组成两条 key-chain，本端 tx=对端 rx（<<<PAGE 92>>>-<<<PAGE 94>>>）
- C-06 免费 site license 手工安装（<<<PAGE 91>>>）

## B（边界与陷阱）
- Static 模式不支持 OS6860N；OS6870 VFL 堆叠口（24 口机型 25/26、48 口机型 49/50）不支持 MACsec（<<<PAGE 75>>>、<<<PAGE 72>>>）
- 板卡差异大：64X10G 分支光模块/扩展模块不支持；OS9900 部分板卡仅 Static——部署前逐板卡核对平台矩阵（<<<PAGE 71>>>）
- 无 license 时功能不可用，先 `show license-info` 预检避免配到一半失败（<<<PAGE 87>>>）

## 来源
- framework·F-03 模式决策树（<<<PAGE 67>>>、<<<PAGE 75>>>、<<<PAGE 76>>>、<<<PAGE 78>>>-<<<PAGE 80>>>）
- framework·F-04 密钥轮换策略（<<<PAGE 77>>>、<<<PAGE 89>>>）
- principle·P-06/P-07/P-08/P-09/P-10/P-11（<<<PAGE 67>>>-<<<PAGE 82>>>）
- case·C-04/C-05/C-06；counter·X-03/X-04/X-21
