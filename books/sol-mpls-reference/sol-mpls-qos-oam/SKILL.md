---
name: MPLS QoS/TTL 透明性与 OAM（uniform/pipe、PHP 与 EXP 保留、LSP ping/trace、AOS 不支持项）
description: 需要处理 MPLS 报文的 QoS 标记（EXP uniform/pipe 模式）、TTL 透明性（traceroute 行为）、PHP 与 explicit NULL 的 EXP 保留差异，或用 mpls ping/traceroute 验证数据面、核对 AOS 不支持清单时使用。
source_book: MPLS Reference Design Guide
---

## R（触发场景）
- 决定客户 DSCP/ToS 是否穿透运营商域（QoS uniform vs pipe）
- 解释 VPN 场景 traceroute/ttl 行为差异（L3VPN 减 2、L2VPN 不变）
- 排查"控制面正常但丢包"的数据面故障（LSP ping/traceroute）
- 核对 AOS 8.9R3/8.10R2 的 QoS/OAM 能力边界

## I（核心理念）
只有顶层（传输）标签的 EXP/TTL 被处理（P10，<<<PAGE 18-19>>>）：内层标签原样透传。QoS/TTL 透明性选型框架（F5，<<<PAGE 18-19>>>）：uniform 让客户标记穿透（复制到 EXP、出域回写），pipe 运营商自定 EXP、客户 DSCP 不动。PHP 用 implicit NULL 让倒数第二跳弹传输标签省 eLER 一次查表（P9，<<<PAGE 16>>>），代价是 EXP 随标签一起弹掉（X9）。数据面验证靠 LSP ping/trace（P32，<<<PAGE 23>>>）：IP 可达、控制面看似正常时仍可能有数据面故障。

## A1（行动框架）
1. QoS 模式决策（F5）：客户标记需端到端可见 → uniform；运营商独立 QoS 策略、客户标记不动 → pipe
2. TTL 模式决策（F5/C8，<<<PAGE 19>>>）：uniform 复制 IP TTL 逐跳递减（traceroute 可见骨干）；pipe 中 L3VPN 仅 iLER/eLER 各减 1、L2VPN 完全不变
3. OAM 排障分层（F4，<<<PAGE 20>>>）：transport 层 `show mpls *` → service 层 `show service *` → 数据面 `mpls ping/trace`
4. AOS 边界核查（X16，<<<PAGE 13-19>>>）：不支持 QoS over EXP、TTL manipulation、explicit NULL——设计前先按此过滤

## A2（操作步骤）
- **LSP ping**（C9，<<<PAGE 44>>>）：`mpls ping ldp 1.1.1.4/32`，5 发 5 中，min/avg/max=0.67/1.30/1.94 ms；目的地址取 127/8 防探测包被 IP 转发泄漏出 eLER（P21，<<<PAGE 23>>>）
- **LSP traceroute**（C10，<<<PAGE 44>>>）：`mpls trace ldp 1.1.1.4/32` 逐跳 TTL 递增，末端显示 "0 20.2.1.2 [Labels: implicit-null]" 即 PHP 生效
- **协议参数**：RFC 4379，echo request/reply 走标签转发、UDP 3503（<<<PAGE 23-24>>>）
- **PHP/QoS 核对**（C6，<<<PAGE 16-17>>>）：implicit NULL 弹标签时 EXP 一并移除；explicit NULL 可保留 EXP 于标签头，但 AOS 当前不支持
- **Graceful Restart**（P27，<<<PAGE 19>>>）：RFC 3478 控制面重启期间保留转发状态（NSF），仅计划内接管

## E（实证案例）
- QoS uniform/pipe 双模式行为对比：uniform 复制 IP precedence 到 EXP，pipe 按运营商策略设定（C7，<<<PAGE 18>>>）
- TTL 双模式：L3VPN 两端各减 1（traceroute 少 N-1 跳）、L2VPN 完全不变（C8，<<<PAGE 19>>>）
- PHP 与 explicit NULL 的 QoS 保留对比（C6，<<<PAGE 16-17>>>）
- LSP ping 5 发 5 中实测与 traceroute 逐跳发现 implicit-null（C9/C10，<<<PAGE 44>>>）

## B（反例与坑）
- implicit NULL 弹标签即丢 EXP/QoS 信息；要保留就得用 explicit NULL——AOS 不支持（X9/X16，<<<PAGE 16-17>>>）
- 不用 PHP 则 eLER 做两次查表，性能受损（X10/P9，<<<PAGE 16>>>）
- AOS 明确不支持：QoS over EXP、TTL manipulation、explicit NULL（X16，<<<PAGE 17-19>>>）
- Graceful Restart 只保计划内接管；非计划主控故障或链路断仍有流量中断（X12/P27，<<<PAGE 19>>>）
- OAM Alert Label（14）未广泛实现，勿依赖其区分 OAM 与数据包（X11，<<<PAGE 10>>>）
- OAM 探测目的地址必须 127/8，否则 echo 包可能被当普通 IP 包转出 eLER（P21，<<<PAGE 23>>>）
- MPLS 复杂度与性能成正比，能力边界外勿硬上（X15，<<<PAGE 44>>>）

来源：MPLS Reference Design Guide（Data Plane + Service Model OAM 节，p16-19、p23-24、p44）
