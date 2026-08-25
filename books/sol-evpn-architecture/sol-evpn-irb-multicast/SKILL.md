---
name: EVPN IRB 与组播（对称/非对称 IRB/DAG/OISM-PEG/外部连通）
description: 需要设计 EVPN 跨子网路由——对称 vs 非对称 IRB 选型、SBD/Fabric-VPN、分布式任播网关 DAG（anycast IP/MAC 派生）、OISM+PEG 跨子网组播、border leaf+GRM 外部连通与路由汇总防回声时使用。
source_book: EVPN Architecture Guide（evpn-architecture-guide-en.pdf）
---

## R（触发场景）
- 规划 EVPN 内跨子网（东西向）路由：选 IRB 模型
- 部署分布式网关 DAG 替代 VRRP
- 跨子网组播设计（OISM/IPMS/PEG 与外部 PIM 互通）
- 数据中心/园区 fabric 对接外部网络（border leaf、路由汇总、双 leaf 防回声）

## I（核心理念）
IRB 模型选型框架（F3，<<<PAGE 24>>>）：对称 IRB 配置简、扩展好、是主流推荐（P9）；每 PE 只维护本地 ARP/MAC-VRF（P10，<<<PAGE 25>>>）；每 VRF 一个 L3EVI（SBD/AOS 中记 Fabric-VPN）提供跨 EVI 可达（P11，<<<PAGE 25>>>）。DAG（<<<PAGE 28>>>）：所有共 EVI 的 PE 配同一 anycast IP+MAC（每 VRF 一个 VMAC），网关全分布式、同 PE 主机间流量不过 fabric（P8，<<<PAGE 22>>>），免 VRRP 类冗余协议。外部连通框架（F5，<<<PAGE 29>>>/<<<PAGE 48>>>）：border leaf+Fabric-VPN+GRM 注入；对外只重分发聚合路由（P34）；双 border leaf 调 import 路由优先级防 OSPF 回声（P35）。

## A1（行动框架）
1. IRB 选型判定（F3）：host-based（R-T2 /32，对称/非对称皆可）vs prefix-based（R-T5，仅对称）；对称 IRB 下服务只配在主机接入 PE（C14，<<<PAGE 48-72>>>）
2. DAG 部署：anycast MAC 每 VRF 一个、同 VRF 全子网共用（P42，<<<PAGE 28>>>）；自动派生规则 00:00:5e:00:01:<VRF-ID>（C17，<<<PAGE 69>>>），须确认不与在用 MAC 碰撞（X10，<<<PAGE 29>>>）
3. BUM 复制选型（F5，<<<PAGE 29>>>）：AOS 仅支持 ingress replication（R-T3 构建列表，简单但单播复制低效）；tandem replication 需组播底层、核心高效但复杂
4. 跨子网组播：OISM（RFC 9625，Fabric-VPN+R-T6，无需 PIM，8.10R3 EA）为主；源发现选 R-T10 而非 (*,*) 默认 SBD-SMET 省带宽（P40，<<<PAGE 38-39>>>）
5. 外部连通五要素（P33-P35，<<<PAGE 46-48>>>）：对称 IRB+Fabric-VPN 强制 → border leaf 做 GRM 注入 → route-map+ACL 只放聚合路由 → 双 leaf 防回声 → PEG 对接外部 PIM

## A2（操作步骤）
- **Inter-subnet 对称 IRB 走包**（C4，<<<PAGE 31-32>>>）：ARP 网关→IP-VRF 查 SBD overlay index→递归解析对端 IRB MAC→VXLAN 封装→对端 SBD IP-VRF→MAC-VRF 下发
- **Intra-subnet 走包**（C3，<<<PAGE 31>>>）：ARP request→源 PE 查 proxy ARP 缓存代答→单播 VXLAN→对端解封装桥接
- **OISM 转发**（C7，<<<PAGE 37-38>>>）：IGMP join→R-T6 带 Fabric-VPN RT→源 PE IPMS 建组表项→隧道转发
- **PEG 外部互通**（C8/C9，<<<PAGE 38-39>>>）：双 PEG 冗余+按 VRF 负载分担，PEG 间用专用 L3 链路保 RP 可达；R-T10 源发现：首包→R-T10(S,G)→DR PEG 注册外部 RP→PIM join 回来→PEG 发 R-T6 拉流
- **路由汇总实操**（P34，<<<PAGE 48>>>）：IRB 子网下主机路由聚合，route-map 绑 ACL 只放行聚合路由对外重分发

## E（实证案例）
- Intra-subnet 五步/Inter-subnet 六步走包分析（C3/C4，<<<PAGE 31-32>>>）
- OISM 跨子网组播与双 PEG 冗余案例（C7/C8，<<<PAGE 37-38>>>）
- border leaf+GRM 外部路由注入（C13，<<<PAGE 47>>>）
- Duplicate IP（DAD）场景：新 ARP 同 IP 视为 IP Mobility，Confirm 探测旧主（C11，<<<PAGE 39-40>>>）；静默主机静态绑 MAC+sticky 位防误迁移（C12/P21，<<<PAGE 40>>>）

## B（反例与坑）
- 非对称 IRB 全 PE 维护全网 ARP/MAC-VRF/IRB 接口，资源与配置密集（X12，<<<PAGE 24>>>）
- VRRP 集中网关低效：tromboning+控制面开销——用 DAG（X9，<<<PAGE 28>>>）
- 自动派生 anycast MAC 有碰撞风险，不确定时手工指定（X10，<<<PAGE 29>>>）
- (*,*) 默认 SBD-SMET 让 PEG 收全部组播流量，核心带宽浪费（X19/P40，<<<PAGE 38-39>>>）
- R-T10 源发现建流有少量额外时延（X23，<<<PAGE 39>>>）
- border leaf 泄漏主机路由压垮外部路由器控制/数据面（X20，<<<PAGE 48>>>）
- 双 border leaf 路由回声：import 路由优先级须高于 OSPF（数值更低）（X21/P35，<<<PAGE 48>>>）
- IP+MAC 同迁（VM motion）不算 DAD，勿误报（P38，<<<PAGE 40>>>）

来源：EVPN Architecture Guide（p23-48）
