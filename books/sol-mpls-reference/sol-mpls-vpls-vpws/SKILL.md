---
name: MPLS L2VPN 业务（VPLS/VPWS、EPL/EVPL、T-LDP 与 BGP 信令、SDP/SAP 配置）
description: 需要设计或配置 AOS 的 VPLS（多点 E-LAN）与 VPWS（点对点 E-LINE/EPL/EVPL）业务时使用：服务模型（SAP/SDP/双标签）、T-LDP 与 MP-BGP l2vpn-vpls 信令选型、split horizon、五步/四步配置流程与验证命令。
source_book: MPLS Reference Design Guide
---

## R（触发场景）
- 规划二层 VPN 业务：多点局域网互连（VPLS）或点对点专线（VPWS/EPL/EVPL）
- 选信令：T-LDP（手工 SDP）vs MP-BGP l2vpn-vpls（自动发现+信令）
- 配置 SAP（面向 CE）与 SDP（面向远端 PE）、mesh/spoke bind-sdp
- 排查 VPLS 环路、MAC 学习、PW 状态问题

## I（核心理念）
服务与传输解耦（F4/P4，<<<PAGE 20>>>）：服务只在有站点的 LER 上创建，SAP（AC）面向 CE、SDP（VC）面向远端；传输隧道可由 LDP/RSVP-TE/静态任一种承载而不动服务层。VPLS 是 VPWS 超集（P30，<<<PAGE 21>>>）：VPLS 需全互联 PW + per-VPLS MAC 学习/桥接/复制；VPWS 点对点透明转发、不学客户 MAC。防环靠 split horizon：PW 进 PW 出禁止（P11，<<<PAGE 21>>>）。T-LDP 保会话抗链路故障（P14，<<<PAGE 15>>>）。

## A1（行动框架）
L2VPN 服务选型框架（F2，<<<PAGE 21-22>>>）：
1. 连通需求：E-LAN 多点 → VPLS；E-LINE 点对点 → VPWS
2. VPWS 细分：EPL（整端口一条 PW）vs EVPL（按外层 C-VLAN 复用多条 PW 于同一端口，P31）
3. 信令选型：T-LDP（手工 SDP far-end，适合少量站点）vs MP-BGP l2vpn-vpls（自动发现+信令一体；单 AS 需 full-mesh 或 RR，P26）

## A2（操作步骤）
- **LDP-VPLS 五步**（C12，<<<PAGE 33-34>>>）：access port → SDP far-end → `service vpls vplsid` + `signaling ldp` → SAP port 1/1/4:0 → `bind-sdp 102 103`（mesh，R1/R6/R7）
- **BGP-VPLS 四步**（C13，<<<PAGE 34-35>>>）：`ip bgp address-family l2vpn-vpls` → neighbor activate l2vpn-vpls → `service 2 vpls vplsid 11 signaling bgp ve-id 1` → SAP
- **VPWS 四步**（C14，<<<PAGE 41-42>>>）：`service vpws vcid 100` → SDP far-end → `bind-sdp 20 spoke` → 两端 SAP port 1/1/1:0、1/1/2:0，即 PE1/PE2 端口间虚拟桥
- **BGP 自动发现验证**：`show ip bgp l2vpn-vpls path 50` 看 VPLS-ID、VE Block Offset、Label Base、RT+MTU 扩展团体（C18，<<<PAGE 38-39>>>）
- **业务验证命令族**（C15，<<<PAGE 31-44>>>）：`show service [vpls|vpws|bind-sdp|mesh-sdp]`、`show mac-learning domain vpls`、`show ip bgp l2vpn-vpls [path]`
- **T-LDP 部署**：远端 LER 间单播 UDP 发现 + 单播 TCP 会话，交换服务标签（C4，<<<PAGE 15>>>）

## E（实证案例）
- LDP-VPLS 五步配置（R1/R6/R7 三站 mesh）（C12，<<<PAGE 33-34>>>）
- BGP-VPLS 四步配置与 VE-ID 参数（C13，<<<PAGE 34-35>>>）
- VPWS E-Line 配置：两 SAP + spoke bind-sdp 成虚拟桥（C14，<<<PAGE 41-42>>>）
- BGP VPLS 自动发现 path 输出解读（VBO/Label Base 53122/MTU 9194）（C18，<<<PAGE 38-39>>>）

## B（反例与坑）
- 无 split horizon 则 PW 可成骨干环路——PE 绝不从 PW 收到的包再发往 PW（X14/P11，<<<PAGE 21>>>）
- 无 T-LDP 时两 LSR 间链路故障直接丢 LDP 会话（X13/P14，<<<PAGE 15>>>）
- VPWS 不提供任何 L2/L3 功能，需要 MAC 层互通就上 VPLS（P30，<<<PAGE 21>>>）
- VPLS PE 必须具备 per-VPLS MAC 学习/桥接/复制，低端设备需核对（P12，<<<PAGE 21>>>）
- T-LDP 仍依赖传输隧道（LDP/RSVP-TE/静态），传输不通则服务隧道建不起来（P24，<<<PAGE 15>>>）
- BGP VPLS 单 AS 不用 RR 就要 LER 全互联，站点多时扩展性差（P26，<<<PAGE 21>>>）
- SAP 只建在有站点的 LER 上，中间 LSR 不感知服务（P4/P6，<<<PAGE 20-21>>>）

来源：MPLS Reference Design Guide（Service Model Ch + Configuration 节，p15-22、p33-42）
