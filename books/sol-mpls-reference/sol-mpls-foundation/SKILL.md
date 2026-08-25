---
name: MPLS 基础体系（标签栈/LDP 消息与模式/PHP/underlay 前提）
description: 需要理解或规划 AOS MPLS 底层机制时使用：32 位 shim 标签结构、双标签封装（transport+service）、LDP 邻居发现与会话建立、DoD/DU-ILD/OLD-CLR/LLR 模式、PHP 与 implicit NULL、LDP MD5 认证与 AOS 支持边界。
source_book: MPLS Reference Design Guide
---

## R（触发场景）
- 规划 IP/MPLS 底层：IGP underlay、/32 loopback、LSR ID 唯一性
- 排查 LDP 邻居/会话建立失败（hello、hold-timer、keepalive、MD5）
- 解释标签封装与转发（push/swap/pop、标签栈、FTN/ILM 表项）
- 确认 AOS 8.9R3+ 的 LDP 模式支持边界（仅 DU+ILD+LLR+MD5）

## I（核心理念）
标签隧道换 BGP-free core（P1/P2，<<<PAGE 5>>>）：MPLS 用预分配标签做精确匹配转发，核心 LSR 无需承载大量路由。双层解耦模型（F4，<<<PAGE 20>>>）：服务标签在底、传输标签在顶，中间 LSR 只处理传输标签（P6，<<<PAGE 21>>>）。LDP 是"依 IGP 而生"的信令（P3，<<<PAGE 10>>>）：先有 IGP 全可达，LDP 才能从 eLER 向 iLER 上游泛洪标签（P19）。会话可靠性靠 hello/keepalive 双定时器双保险（P23，<<<PAGE 12>>>）。

## A1（行动框架）
1. 标签分发/控制/保留模式选型框架（F1，<<<PAGE 13-14>>>）：分发 DoD（按需）vs DU（主动）；控制 ILD（独立即刻通告）vs OLD（有序等下游）；保留 CLR（只留有效）vs LLR（全保留）。AOS 唯一组合 = DU+ILD+LLR（X16，<<<PAGE 13-17>>>）
2. 部署定位框架（F3，<<<PAGE 24-25>>>）：园区中小型网从接入到核心端到端 MPLS；城域/Smart City 核心+汇聚跑 MPLS、接入保持以太交换。共同前提：IGP + /32 loopback 唯一 Router-ID
3. Best Practice 清单（P22，<<<PAGE 28>>>）：每台 /32 loopback → Router-ID 全网唯一 → p2p routed 接口 + BFD → /31 互联地址

## A2（操作步骤）
- **标签结构解读**：32 位 = 20-bit Label（16 起步，0-15 保留）+ 3-bit EXP + 1-bit S(BoS) + 8-bit TTL；shim 头位于以太头与 IP 头之间故称 Layer 2.5（P28/P33，<<<PAGE 9>>>）
- **保留标签识别**：0=IPv4 Explicit NULL、1=Router Alert、2=IPv6 Explicit NULL、3=Implicit NULL、14=OAM Alert（<<<PAGE 9-10>>>）
- **LDP 邻居发现**：所有链路发 UDP 646 组播 hello（224.0.0.2）→ hello 交换后 TCP 646 建会话 → LDP Initialization 协商参数（C3，<<<PAGE 12>>>）
- **会话参数核对**：show mpls ldp session 应见 "Downstream Unsolicited / Liberal / GR Enabled / Helper"（C17，<<<PAGE 33>>>）
- **MD5 认证**：双方配同一 MD5 key，为每个 TCP 段附加签名；不符则静默丢弃（P18/X6/X7，<<<PAGE 14-15>>>）
- **表项验证**：show mpls ftn-table（Push 条目）/ ilm-table / forwarding-table；OpCode 1=PUSH、2=POP、3=SWAP（C16，<<<PAGE 32>>>）
- **MPLS backbone 五步**（R1 视角，C11，<<<PAGE 29-31>>>）：接口 → 单区域 OSPF（p2p+BFD+SPF delay 0）→ 安装 uosn-mpls-v1.deb → mpls interface → mpls ldp interface

## E（实证案例）
- 双标签封装-解封端到端流程：iLER push service 标签再 push transport 标签，eLER 依次 pop（C2，<<<PAGE 20-21>>>）
- push/swap/pop 三操作数据面走包（C5，<<<PAGE 16>>>）
- LDP 邻居发现与会话建立全流程（C3，<<<PAGE 12>>>）
- LDP 会话协商结果输出（DU/Liberal/GR Helper）（C17，<<<PAGE 33>>>）
- FTN/ILM 真实表项解读（C16，<<<PAGE 32>>>）

## B（反例与坑）
- 不用 MPLS 则核心被迫承载大量路由、成本上升（X1，<<<PAGE 5>>>）
- LSR ID（loopback）不唯一导致不可预测行为（X2/P15，<<<PAGE 13>>>）
- hello hold-timer 超时即判死邻居删 adjacency；keepalive 超时终结会话（X3/X4，<<<PAGE 12>>>）
- 会话参数谈不拢则反复重谈，会话不稳（X5，<<<PAGE 12>>>）
- MD5 密钥不匹配建不起会话；MD5 本身强度不足，RFC 建议 keychain+SHA（X6/X7/X8，<<<PAGE 14-15>>>）
- 一对 LSR 多链路仍只建一个直连会话，勿误判为故障（P20，<<<PAGE 13>>>）
- LSP 单向，双向流量需两条（P7，<<<PAGE 8>>>）
- hold-timer 取双方较低值，接口级覆盖全局（P16，<<<PAGE 12>>>）
- LDP 不在面向 CE 的接口使能（P17，<<<PAGE 12>>>）
- 未装 Site/Node-based license 则 MPLS 接口起不来（X18，<<<PAGE 30>>>）
- AOS 不支持：DoD、OLD、CLR、非 MD5 认证、explicit NULL、QoS over EXP、TTL manipulation（X16，<<<PAGE 13-19>>>）

来源：MPLS Reference Design Guide（Fundamentals Ch + Control Plane + Configuration 节，p5-17、p24-33）
