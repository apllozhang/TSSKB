# counter-examples — sol-mpls-reference（书中警告的失败模式，英文原句 + 真实页码）

- **X1 核心 BGP 规模爆炸（不用 MPLS 时）**："the core routers do not need to support a large number of routes"（反面即核心被迫承载大量路由、成本上升）。<<<PAGE 5>>>
- **X2 LSR ID 不唯一导致不可预测行为**："It is important that the LSR ID, or the loopback address is unique in the MPLS domain to avoid any unpredictable behavior." <<<PAGE 13>>>
- **X3 Hello hold-timer 超时判死邻居**："if the timer expires without receiving a matching hello packet from the peer, LSR concludes that the peer is no longer alive and then deletes the Hello adjacency." <<<PAGE 12>>>
- **X4 Keepalive 超时终结会话**："If this timer expires, the LSR concludes that the transport connection is bad or that the peer has failed, and it terminates the LDP session by closing the transport connection." <<<PAGE 12>>>
- **X5 会话参数谈不拢则反复重谈**："If they agree, they maintain the LDP session, otherwise they will try to re-negotiate." <<<PAGE 12>>>
- **X6 MD5 密钥不匹配则建不起会话**："Authentication must be configured on both LDP peers using the same MD5 key (password), otherwise the peer session will not be established." <<<PAGE 14>>>
- **X7 MD5 签名不符静默丢弃 TCP 段**："silently rejects the TCP segment if the computed MD5 signature doesn't match with received MD5 signature." <<<PAGE 14-15>>>
- **X8 MD5 本身强度不足（RFC 建议更强算法）**："Currently MD5 key based authentication is proposed in the RFC but it also mentions that keychains with a stronger encryption algorithm like SHA can be implemented." <<<PAGE 14>>>
- **X9 implicit NULL 弹标签丢掉 EXP/QoS**："When the last LSR removes the top label, the EXP bits are also removed, thus removing any QoS values in the header." <<<PAGE 16-17>>>
- **X10 非 PHP 让 eLER 做两次查表**："This is to avoid performing two lookups in the MPLS FIB."（反面：不省性能）。<<<PAGE 16>>>
- **X11 OAM Alert Label 未广泛实现**："The Operation and Maintenance (OAM) Alert Label differentiates OAM packets from normal user data packets, but it is not widely implemented." <<<PAGE 10>>>
- **X12 非 GR 场景（非计划接管/链路断）流量中断**："supported only for planned takeovers... not unplanned takeovers (for example, the primary Chassis Management Modules (CMMs) unexpectedly fails) or when a link goes down between the two routers." <<<PAGE 19>>>
- **X13 无 T-LDP 时链路故障直接丢 LDP 会话**："when a link between two LSRs in an LSP fails without T-LDP, then the LDP session is lost." <<<PAGE 15>>>
- **X14 PW 回环风险（若无 split horizon）**："a PE must never send a packet on a PW if that packet has been received from a PW. This ensures that traffic cannot form a loop over the backbone network using PWs." <<<PAGE 21>>>
- **X15 MPLS 复杂度与性能成正比**："It's complexity is proportional to it's performance."（结论章自认的代价）。<<<PAGE 44>>>
- **X16 AOS 当前不支持项清单**："Only Downstream Unsolicited Mode is supported in the current release." / "Only Independent Label Distribution control is supported" / "Only Liberal Label Retention Mode is supported" / "Only MD5 key-based authentication is supported" / "Explicit NULL is currently not supported in AOS implementation." / "QOS over EXP bit is not supported" / "TTL manipulation is not supported for MPLS tag." <<<PAGE 13-17-19>>>
- **X17 配置示例偏离自身最佳实践（/24 代替 /31）**："It is recommended to consider using (/31) contiguous addresses for point-to-point links, but we have used in this configuration (/24)." <<<PAGE 29>>>
- **X18 未装 license 则 MPLS 接口起不来**："It is also required to install Site-based or Node-based license for MPLS interface to be up and running." <<<PAGE 30>>>
