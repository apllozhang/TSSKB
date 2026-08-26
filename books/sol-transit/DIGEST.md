# 全书精华串讲

这两份 ALE（Alcatel-Lucent Enterprise）设计指南讲的是同一件事：怎么用 SPB（Shortest Path Bridging，最短路径桥接）智能织构（iFab）给轨道交通和智能交通（ITS）建一张多业务统一承载网。通用版 70 页是最新全本，SPB 版 42 页是被它吸收的早期方案版。全书的主线可以压缩成五句话。

**第一句：一张网装所有业务，靠 VPN 容器切分。** 轨交网上跑的业务分四类——Control（信标、ATC）、Safety（CCTV、紧急呼叫、消防）、Communications（电话、WLAN）、Information（PIS、广播、Infotainment、上网）。几十个系统共享一张物理网，靠 VPN/容器做逻辑隔离，每个系统一个 VPN、一个流量等级，单级 QoS 就够。唯一的例外是信号系统：它要 50ms 收敛，SPB 做不到（一般 200ms 以上，8.5R2 目标压到 100ms 以内），必须走独立的 SDH/MPLS 网——这是全书最重要的一条边界。

**第二句：架构上环网打底、OCC/BCC 双中心、站点 L2 或 L3 二选一。** 环是沿线路冗余互联的天然拓扑。站点架构是全书最核心的取舍：L2 VPN 把站点 VLAN 一比一映射 ISID，全网 VLAN/MAC/ARP 全压在 OCC/BCC 两台 BEB 上，规模很快见顶；L3 VPN 让站点 BEB 做 VRRP 网关，接入 VLAN 只在本地有意义，只有共享的上行 VLAN 经 hairpin 映射 ISID，路由靠 IS-IS 的 TLV 随骨干自动扩散——IP 能汇总、MAC 不能，所以 L3 天然更能扩。站点双归两台 BEB 消单点，同站双机省光纤、本地+远端省设备，运维复杂度相反。

**第三句：SPB 细节设计处处是"反直觉"。** 环上多数节点对之间只有一条最短路径，所以环网配一个 BVLAN 就够，配两个反而让故障收敛翻倍变慢；SPB 骨干 LAG 是 MAC-in-MAC 封装，默认哈希只看 B-MAC、随机性不足，必须开 tunnel-protocol 用 C-MAC/IP 做哈希；link metric 默认恒为 10 不分速率，要手工按速率反比调表，还要把 OCC-BCC 链路调大避免站间流量绕行控制中心；QoS 在 SAP 入口一次分类定终身，骨干内因封装无法再分类。

**第四句：组播与容量是轨交网的两道生死关。** BUM 复制三模式里，Head-End 省资源费带宽，Tandem (S,G) 每链路一份最省带宽，L2 共享 VLAN/ISID + Head-End 的组合会让站源组播按 N×(N+1) 平方爆炸——这是原文反复敲的黑名单。容量规划按"故障后单路径扛全网"的最坏口径：20 站轻轨案例里，480 台摄像机（4Mbps 直播 + 2Mbps 存档 + 20% 开销）撑起去 OCC 方向 3590Mbps，加小系统预算与 30% 缓冲合计 5188Mbps，10G 够用——但换一个视频编码器就可能翻盘。

**第五句（仅通用版）：安全与选型是落地的最后两块板。** 安全走纵深防御：IoT 终端四项加固、系统间通信只过防火墙、交换机管理面禁明文协议、内置 DoS 过滤、MACsec 在公共空间链路做线速加密、Access Guardian 三种准入认证返回 UNP 动态绑策略、SPB 容器天然分段、IDS 与 OmniVista 联动隔离攻击端口。选型按角色映射：骨干 9900/6900，轨道旁加固 6865（L3）与 6465（L2 价值型，带 USB 备份恢复和告警继电器两个轨交专属硬件特性）。轨交是十年级投资，8.5R1 及以上产品线有 10 年长期支持，须在最后订购日前至少 6 个月下单。

读法建议：先 transit-overview 与 transit-architecture 建立骨架，再按需下钻 spb-design / multicast / capacity 三个设计单元，attachment 与 ops 覆盖接入和运维，security 与 products 收尾。两版重叠处以通用版为准；通用版内嵌的评审批注（hairpin 官方支持口径、SPB 节点规模、LBD 状态、组播章节未过实验室验证）是识别"未定论结论"的关键线索，写方案前应向 ALE 逐项确认。
