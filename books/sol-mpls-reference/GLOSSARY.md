# GLOSSARY · MPLS Reference Design Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按基础术语/标签结构/LDP 体系/模式/QoS-TTL/服务模型/L2VPN/OAM/license 分组，精选 45 条。

## 基础术语
- **MPLS (Multiprotocol Label Switching)**：基于预分配标签的标签交换，转发不看内层 IP 头 <<<PAGE 5>>>
- **LER (Label Edge Router)**：MPLS 域边缘路由器（即 PE），push/pop 标签；分 iLER/eLER <<<PAGE 7>>>
- **LSR (Label Switch Router)**：域内路由器，执行 swap；LER 也算 LSR <<<PAGE 7>>>
- **LSP (Label Switched Path)**：iLER 到 eLER 的预确定传输隧道；单向，双向需两条 <<<PAGE 8>>>
- **FEC (Forwarding Equivalence Class)**：赋同一标签的相似包集合（前缀/QoS 标记等） <<<PAGE 8>>>
- **LDP (Label Distribution Protocol)**：RFC 5036 标签信令，依 IGP 路由建传输 LSP <<<PAGE 8>>>
- **T-LDP (Targeted-LDP)**：远端 LER 间单播 UDP/TCP 会话，交换服务标签，抗链路故障保会话 <<<PAGE 15>>>
- **MP-BGP**：RFC 2283，为服务交换路由+服务标签并自动发现同服务 PE <<<PAGE 15>>>

## 标签结构
- **MPLS 标签结构**：32 位 shim 头 = 20-bit Label + 3-bit EXP + 1-bit S + 8-bit TTL；Layer 2.5 协议 <<<PAGE 9>>>
- **EXP bits**：标签头 3 个实验位，承载 QoS；仅顶层标签被处理 <<<PAGE 9>>>
- **S Bit / BoS**：标签栈底标志位 <<<PAGE 9>>>
- **保留标签 0-15**：0=IPv4 Explicit NULL、1=Router Alert、2=IPv6 Explicit NULL、3=Implicit NULL、14=OAM Alert <<<PAGE 9-10>>>
- **标签栈 (Label Stacking)**：LIFO 多标签；VPN 顶为 transport、底为 service；厂商普遍 4-6 层 <<<PAGE 10>>>
- **FTN (FEC-To-NHLFE)**：FIB 中面向 Push 的条目 <<<PAGE 10>>>
- **ILM (Ingress Label Mapping)**：面向 Swap/Pop 的条目；本地与远端标签绑定均存于此 <<<PAGE 10>>>
- **NHLFE**：下一跳标签转发表项 <<<PAGE 10>>>
- **push / swap / pop**：LSR 三种标签操作（imposition/disposition 为别称） <<<PAGE 16>>>

## LDP 体系
- **LDP 消息四类**：Discovery/Session/Advertisement/Notification；UDP 646 发现、TCP 646 会话、224.0.0.2 组播 hello <<<PAGE 11-12>>>
- **Label Mapping / Withdraw / Release**：标签映射通告/撤销/释放三类核心通告消息 <<<PAGE 11-13>>>
- **LDP ID**：6 字节 = 4 字节 LSR 标识（loopback）+ 2 字节标签空间（0=per-platform） <<<PAGE 13>>>
- **LDP MD5 认证**：每 TCP 段附 MD5 签名防伪造，双方同钥；不符静默丢弃 <<<PAGE 14-15>>>
- **LDP Graceful Restart**：RFC 3478，控制面重启期间保留转发状态（NSF）；仅计划内接管 <<<PAGE 19>>>
- **hold-timer / keepalive 双定时器**：hello adjacency 判死 / 会话完整性监测 <<<PAGE 12>>>
- **LSR ID 唯一性**：loopback 必须全网唯一，否则不可预测行为 <<<PAGE 13>>>

## 分发/控制/保留模式
- **DoD (Downstream-on-Demand)**：仅应答请求才发标签 <<<PAGE 13>>>
- **DU (Downstream Unsolicited)**：主动发标签；AOS 唯一支持；常配 LLR <<<PAGE 13>>>
- **ILD (Independent Label Distribution)**：随时通告标签映射；AOS 唯一支持 <<<PAGE 13-14>>>
- **OLD (Ordered Label Distribution)**：收到下游标签或自身为 egress 才通告 <<<PAGE 14>>>
- **CLR (Conservative Label Retention)**：只保留有效下一跳绑定 <<<PAGE 14>>>
- **LLR (Liberal Label Retention)**：保留所有绑定；AOS 唯一支持 <<<PAGE 14>>>

## QoS/TTL/PHP
- **PHP (Penultimate Hop Popping)**：eLER 以 implicit NULL 请求倒数第二跳弹传输标签省一次查表 <<<PAGE 16>>>
- **Implicit NULL (label 3)**：PHP 信号标签 <<<PAGE 10-16>>>
- **Explicit NULL (0/2)**：保留 EXP 的 PHP 替代；AOS 不支持 <<<PAGE 16-17>>>
- **QoS uniform mode**：客户 IP precedence 复制进 EXP，出域回写 <<<PAGE 18>>>
- **QoS pipe mode**：EXP 按运营商策略设定，客户 DSCP 不动 <<<PAGE 18>>>
- **TTL uniform/pipe mode**：uniform 逐跳递减；pipe 中 L3VPN 两端各减 1、L2VPN 不变 <<<PAGE 19>>>

## 服务模型
- **SAP (Service Access Point) / AC**：UNI 侧逻辑端口绑定客户流量；同端口可多 SAP 复用 <<<PAGE 20>>>
- **SDP (Service Distribution Point) / VC**：NNI 侧单向逻辑连接到远端；本地唯一 ID <<<PAGE 20>>>
- **Service Tunnel**：传输 LSP 内承载服务流量的虚拟链路（FEC=服务标识） <<<PAGE 20>>>
- **Transport Tunnel**：基于 FEC 的单向传输路径（FEC=各 LSR loopback） <<<PAGE 20>>>

## L2VPN
- **VPLS (Virtual Private LAN Service)**：E-LAN 多点；全互联 PW + per-VPLS MAC 学习/桥接/复制 <<<PAGE 21>>>
- **PW (Pseudowire)**：LER 间虚拟线路；VPLS 全互联成网；split horizon：PW 进 PW 出禁止 <<<PAGE 21>>>
- **VPWS (Virtual Private Wire Service)**：E-LINE 点对点；不学 MAC 透明转发；RFC 8077 <<<PAGE 21-22>>>
- **EPL (Ethernet Private Line)**：MEF 6.3 整端口 VPWS <<<PAGE 22>>>
- **EVPL (Ethernet Virtual Private Line)**：按 C-VLAN 复用多条 PW 于同一端口 <<<PAGE 22>>>
- **VE-ID / VBO / VBS**：BGP VPLS 站点标识与标签块偏移/尺寸参数 <<<PAGE 38-39>>>

## OAM 与 license
- **LSP Ping / Traceroute**：RFC 4379 数据面验证；目的 127/8、UDP 3503；trace 靠 TTL 递增 <<<PAGE 23-24>>>
- **show mpls ftn-table / ilm-table / forwarding-table**：FTN/ILM/转发表巡检；OpCode 1=PUSH 2=POP 3=SWAP <<<PAGE 32>>>
- **show service vpls/vpws/bind-sdp/mesh-sdp + show mac-learning domain vpls**：业务面验证命令族 <<<PAGE 31-44>>>
- **Site-based license**：浮动共享，最多 4 节点（可为 8 单元虚拟机箱），SILOS 站点服务器管理 <<<PAGE 26>>>
- **Node-based license**：绑定单 MPLS 节点、不绑硬件序列号/MAC；SWLIC 为机上客户端 <<<PAGE 26>>>
- **uosn-mpls-v1.deb**：MPLS 功能 Debian 安装包（配置第一步） <<<PAGE 30>>>

---
合计：45 条。
