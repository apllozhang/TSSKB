---
name: AOS 8 组播高级（地址边界/DVMRP/PIM-SM-DM-SSP/MBR）
description: 需要在 OmniSwitch AOS 8 上配置组播地址边界（239/8 域复用）、DVMRP（含隧道）、PIM 密集/稀疏模式（RP/BSR/Anycast-RP/SPT 切换）、SSM、IPv6 PIM、或 PIM-DVMRP 边界路由器（MBR）互通时使用。
source_book: OmniSwitch AOS Release 8.10R4 Advanced Routing Guide
---

## R（触发场景）
- 要隔离/复用私组播地址段：ip mroute-boundary 地址边界，多布线间复用同一段 239 地址
- 要跑 DVMRP（含 DVMRP 隧道穿越非组播网络）或 PIM-DM（泛洪-剪枝）
- 要部署 PIM-SM：C-RP/C-BSR/静态 RP 选型、Anycast RP 冗余、Register 打包调优、SPT 切换
- 要启用 SSM（232/8、FF3x::/32）或 IPv6 PIM；要打通 PIM 与 DVMRP 两域（MBR）

## I（核心理念）
组播路由三范式（F7）：密集模式（DVMRP/PIM-DM，广播-剪枝按源建树）→ 稀疏模式（PIM-SM，接收者显式 Join，RP 共享树 + SPT 切换）→ SSM（显式频道订阅免 RP）。域隔离体系（F9）：239/8 管理作用域 + mroute-boundary 让同段地址多域并发复用 + MBR 连接 PIM/DVMRP 两域。PIM-SM 控制体系五要素（F8）：RP（解封装 Register）、BSR（域内唯一分发 RP-set）、DR（源侧封装/接收侧 Join）、RPT 共享树、SPT 切换（末跳 DR 收到首包即切换）。RPF 逆向路径检查是全部组播转发的公共底层（P95）。

## A1（决策框架）
1. **地址域设计**：边界地址必须是 239/8 作用域段（X46）；同一 239 段可在多个被边界隔离的域并发复用（P93/C33）
2. **模式选型**：接收者密集/小网用 DM（泛洪-剪枝）；稀疏/WAN 用 SM；接收者明确知道源用 SSM（免 RP 直连源）
3. **RP 供给三选一**：C-RP+BSR（自动选举）；静态 RP（全网手配）；Anycast RP（多机同地址+IGP 通告，收敛与 IGP 同级，P120）
4. **Register/Join-Prune 调优**：大源量网络开打包降低控制面丢包（P121）；register-mtu 不建议盲目调大（X66）
5. **跨域互通用 MBR**：同机 DVMRP 实例+PIM 实例（RFC 2715）；注意每接口只能跑一个组播协议（X44）

## A2（操作步骤）
- **地址边界**：`ip load pim` → `ip mroute-boundary vlan-3 239.120.0.0 255.255.0.0` → `show ip mroute-boundary`；多域复用例：核心配 239.0.0.0/8，两个布线间各配 239.188.0.0/16（C32/C33，<<<PAGE 220, 226-228>>>）
- **DVMRP 五步**：`ip load dvmrp` → `ip interface vlan-2 ...` → `ip dvmrp interface vlan-2` → `ip dvmrp admin-state enable` → `write memory`；`show ip dvmrp [interface]`（C34，<<<PAGE 231>>>）
- **DVMRP 隧道**：`ip interface "tnl-1" tunnel source 23.23.23.1 destination 155.2.2.2`；源地址接口与隧道接口都要 `ip dvmrp interface` 使能（C35，<<<PAGE 244>>>）
- **PIM-DM 六步**：`ip load pim` → `ip interface vlan-2` → `ip pim interface vlan-2` → `ip pim dense group 225.0.0.0/24` → `ip pim dense admin-state enable` → `write memory`（C36，<<<PAGE 252>>>）
- **PIM-SM RP 体系**：C-RP `ip pim candidate-rp 50.1.1.1 225.16.1.1/32 priority 100 interval 100`；C-BSR `ip pim cbsr 50.1.1.1 priority 100 mask-length 4`；静态 `ip pim static-rp 225.0.0.0/24 10.1.1.1 priority 10`；`show ip pim group-map/candidate-rp/cbsr`（C37，<<<PAGE 270-273>>>）
- **Anycast RP**：两 RP 各配 Loopback1=10.10.10.1（IGP 通告）；全网 `ip pim static-rp 224.0.0.0/4 10.10.10.1`；两 RP 各配完整 RP set（`ip pim anycast-rp 10.10.10.1 192.168.1.1` + 对端）；`show ip pim anycast-rp`（C38，<<<PAGE 275-276>>>）
- **Register/J-P 调优**：`ip pim register-packing enable|force-enable`、`ip pim register-mtu 1000`、`ip pim register-delay 100`（C39，<<<PAGE 278-279>>>）
- **IPv6 PIM**：`ipv6 pim interface vlan-2` → `ipv6 pim dense group ff0e::1234/128` → enable；SM 侧 candidate-rp/cbsr/static-rp/rp-switchover 全套（C40，<<<PAGE 283-292>>>）
- **MBR**：PIM 与 DVMRP 各自 load+接口+全局使能 → `ip mroute mbr admin-state enable`；可选 DVMRP 默认路由通告（`ip dvmrp interface "vlan-6" mbr-default-information enable`）或 `ip pim mbr all-sources`；`show ip mroute mbr` 看 "Protocols Registered = DVMRP PIM"（C41，<<<PAGE 298-303>>>）

## E（实证案例）
- 组播地址边界（核心+双布线间复用 239.188/16）（C33，<<<PAGE 226-228>>>）
- PIM-SM Bootstrap/RP 三路配置与验证（C37，<<<PAGE 270-273>>>）
- Anycast RP 双机配置（C38，<<<PAGE 275-276>>>）
- IPv6 PIM-DM + Bootstrap/RP 全套（C40，<<<PAGE 283-292>>>）
- MBR 三例（默认/DVMRP 默认路由/PIM all-sources）（C41，<<<PAGE 298-303>>>）

## B（反例/坑）
- 每接口仅支持一个组播路由协议，PIM 与 DVMRP 不能同接口共存（X44，<<<PAGE 238, 266>>>）
- 协议未加载即配置报 "application is not loaded"（X45，<<<PAGE 237, 265>>>）
- 边界地址必须是 239.0.0.0-239.255.255.255 作用域段（X46，<<<PAGE 224>>>）
- DVMRP：prune-lifetime 谨慎改（X47）；show ip dvmrp prune 只显示发出的 prune（X48）；隧道两端都要使能 DVMRP 否则不 operational（X49）；flash-interval 必须小于 report-interval（X50）；老版本用 Route Report 做邻居发现（X51）（<<<PAGE 233-244>>>）
- OmniSwitch PIM 只兼容 SMv2 不兼容 SMv1（X53）；Hello 无法区分 DM/SM 邻居，DM 不应与 SM 直接交互（X54）（<<<PAGE 254, 258>>>）
- SPT 状态关闭则 SPT 切换不发生（X55）；SSM 默认段（232/8、FF3x::/32）不自动启用须手动配置（X56）；IGMP 代理场景必须 v3 否则 SSM 不工作（X57）（<<<PAGE 262-264, 282>>>）
- 改 max-rps 前必须全局禁用 PIM-SM（X58）；C-RP 配在未使能 PIM 的接口上会报错（X59）；每交换机只支持一个 RP 地址（X60）；priority 与 override 互斥（X61）（<<<PAGE 268-273>>>）
- Anycast RP 地址不能与 Router ID 相同（X62）；静态 RP 必须配在域内所有 PIM 路由器而非仅 RP 成员（X63）；register-packing 配 Anycast-RP 时仅 RP set 全体支持才启用（X64）（<<<PAGE 275-278>>>）
- Register/J-P 打包仅 SM/SSM/BIDIR 支持，DM 不支持（X65）；register-mtu 盲目调大会致分片重组（X66）；J/P 实际最大尺寸取接口 IP MTU 与配置值较小者（X67）（<<<PAGE 279-280>>>）
- MBR 不支持 PIM-SSM，也不支持 PIM 与其他协议或多个 PIM 域互通（X68）；MBR 使能但 PIM/DVMRP 未各有 enabled 接口前不 operational（X69）；DVMRP 默认路由不能向 MBONE 通告（X70）（<<<PAGE 299-302>>>）
- 高级路由协议需购买附加包（X71，<<<PAGE 12>>>）

## 来源
OmniSwitch AOS 8.10R4 Advanced Routing Guide 第 5 章 Multicast Address Boundary（<<<PAGE 220-228>>>）、第 6 章 DVMRP（<<<PAGE 229-244>>>）、第 7 章 PIM（<<<PAGE 247-296>>>）、第 8 章 MBR（<<<PAGE 297-303>>>）。条目来源：cases C32-C41；principles P91-P127；counter-examples X44-X71；frameworks F7/F8/F9/F10（组播部分）。
