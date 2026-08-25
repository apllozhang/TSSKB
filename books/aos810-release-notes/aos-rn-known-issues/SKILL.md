---
name: AOS 8.10R4 Open CR 已知问题排障库（硬件/软件/平台端口限制）
description: OmniSwitch AOS 8.10R4 网络出现链路异常、光模块不兼容、组播/EVPN/VC 行为诡异、端口聚合或 MACsec 例外时，先查本库判断是否为已知未修问题（Open CR）或平台端口级限制。
source_book: OmniSwitch AOS Release 8.10R4 Release Notes
---

## R（触发场景）
- 链路起不来/翻动/CRC，涉及 SFP-10G-T、SFP-GIG-T、DUAL-BX、4X25G splitter、DAC
- 升级或换板后聚合哈希失衡、组播/广播负载异常、VC takeover 后 MAC 丢失
- EVPN/组播/VRRP/BFD 出现 toggle 掉流、丢包、残留行为
- 选型或部署前核对平台端口级限制（MACsec 端口矩阵、快速收敛例外、聚合限制）
- 判断"这是缺陷还是配置问题"——先查 Open CR 再排障

## I（核心理念）
Release Notes 的 Open Problem Reports 是手册里没有的独占排障库：按 CRAOS8X-xxxxx 编号索引，Fixed CR（Appendix I，<<<PAGE 83-100>>>）为已修，Open CR（<<<PAGE 41-46>>>）为发布时未修、多数"无解"只能绕行。排障口诀：现象先对号 Open CR（避免无效变更）→ 不是 CR 再走配置排障；硬件类 CR 多与光模块速率协商/批次相关，软件类 CR 多与 toggle/admin-state 操作触发相关。平台端口级限制（MACsec 端口矩阵、快速收敛例外、性能许可口）是"设计即如此"，升级不能解决。

## A1（决策框架）
1. **光模块/链路类故障**：对号 X38-X44 清单——多数 workaround 是换模块类型、固定速率、调 inter-frame-gap/FEC
2. **协议行为异常**：对号 X47-X67——toggle 类问题避免不必要的 admin-state 操作；无解项记录为已知风险
3. **特性部署前**：查平台缺口（X21-X25/X28-X31）——P48Z16 聚合口位、MACsec 端口例外、6920/6575-MP16 无 VC、SPB BVLAN 不支持在线改
4. **硬件换代**：X30 类（9900 XNI 板进 CMM2/OS9912 机箱先升 U-Boot+FPGA）

## A2（操作步骤）
- **光模块 CR 绕行**：SFP-10G-T 对端强制 10G（X38，<<<PAGE 42>>>）；SFP-GIG-T 避开 10M 配置下的反复 admin disable/enable（X39，<<<PAGE 42>>>）；OS99-CNI-U8 4x25G DAC 起 lane 不来换 QSFP-100G-SR4 光纤（X40，<<<PAGE 42>>>）；SFP-DUAL-BX-U/D 只用于 6870-24/48/V12 的 1G（X41，<<<PAGE 43>>>）；VFL 4X25G splitter CRC 两侧 inter-frame-gap=13 或 FEC FC+关自协商（X44，<<<PAGE 42>>>）
- **MACsec 部署核对**：端口矩阵例外——6870-24 口 25-26、6870-48 口 49-50 不支持；6865 系列不支持；6900 仅 X48C4E（Dynamic only）；6860N 仅 Dynamic 128-bit 且 splitter 光模块不支持；9900 CNI-U8 不支持（X22/X23，<<<PAGE 62>>>/<<<PAGE 17>>>/<<<PAGE 63>>>）
- **平台缺口预查**：6920 本版无 VC、不支持 IP-IP/GRE/IPv6 隧道（X28，<<<PAGE 21>>>/<<<PAGE 43>>>）；6575-MP16 无 VC（X29，<<<PAGE 21>>>）；P48Z16(903954-90) 1G 口 1-32 不支持聚合，只能靠 PN 区分（X21，<<<PAGE 15>>>）；快速收敛例外：铜口/VFL/splitter 口、6865-P16X·U12X 口 3/4、6570M-12/12D 口 9/10（X24，<<<PAGE 15>>>）
- **6560 X4 系列 10G 解锁口**：24X4/P24X4 口 25/26、48X4/P48X4 口 49/50（默认 1G）；6570M-U28 口 25-28、6870-LNI-U6（50G）同理（X25，<<<PAGE 19>>>）
- **SPB BVLAN 收敛运维**：`show spb isis bvlans` 查全网 In Use → 维护窗内业务删除重建到 4 条 BVLAN → 空闲 BVLAN 全网删除（在线改不支持）（C17，<<<PAGE 66>>>/X31 <<<PAGE 65>>>）

## E（实证案例）
- SPB BVLAN 收敛到 4 条的运维操作（C17，<<<PAGE 66>>>）
- Celona PD 降级规避：`lanpower {slot | port} autoclass disable`（C18，<<<PAGE 34>>>）
- MKA VLAN 隧道化：`interfaces <c/s/p> macsec mode dynamic mka-vlan <vid> [mka-tpid <tpid>]`，验证 `show interfaces macsec mka-info`（C19，<<<PAGE 35>>>）
- 模块热插拔规程：拔线→拔光模块→拔板卡等 ≥30 秒再插同型号（CMM 15-20 分钟；新模块插入间隔 5 分钟且 LED 回正常）→重插光模块→接线；CFM 一次只换一个、120 秒内完成（C14，<<<PAGE 47-48>>>）

## B（反例/坑）
- SFP-GIG-T 对端从 10M 变 100M/1G 间歇性链路 down：U28 热插拔模块恢复，12/12D 可能要整机重启（X43，<<<PAGE 42>>>）；6570M-U28 口 25 + SFP-10G-T 对端反复 admin 翻动出现仅本地 linkup（X42，<<<PAGE 42>>>）
- OS9912 聚合口禁用某成员后哈希失衡，流量可能全压一条剩余链路，无解（X47，<<<PAGE 41>>>）
- PTP 打戳 PHY 口↔PHYless 口交叉时不正确（6870-V12 1-12↔13-14/CNI/LNI；6570-U28 1-24↔25-30），无解（X48，<<<PAGE 41>>>）
- BFD 在 VRRP VLAN 接口 toggle 时丢包，无解（X50，<<<PAGE 41>>>）
- EVPN 一组 toggle 触发掉流：对称 IRB service toggle、PIM+非对称 BGP admin-state toggle、非对称 OSPF admin-state toggle（X54，<<<PAGE 44>>>）
- OS6920 多项协议缺口：ICMP redirect 不转发、Snap 头 ARP 解析失败、IPv6 隧道不转发 ICMPv6、组播 MAC 广播不转发等（X53，<<<PAGE 43-44>>>）
- 二次 vc-takeover 后 sdp/sap MAC 可能从 show mac-learning 丢失，重发流量可恢复（X56，<<<PAGE 45>>>）；OS9900 chassis-2 偶发 cmm-takeover 后 VC 分裂，无解（X57，<<<PAGE 45>>>）
- 静态 MACsec 无加密时 key 不匹配流量仍通——安全审计注意（X60，<<<PAGE 45>>>）
- OS99-XNI-P24Z8 前 8 口 dynamic MACsec reload 后状态 down，需手动 toggle admin state（X59，<<<PAGE 45>>>）
- OS6900-V48 无损 TC 上限 40：全 TC 无损 DCB profile 最多 5 端口，更多需自定义 QSP 只配必要无损 TC（X62，<<<PAGE 45-46>>>）
- OS6575 启用 policy rule Redirect_All 后掉流量，无解（X63，<<<PAGE 46>>>）；8 成员 LAG 禁主口后组播/广播负载失衡（X52，<<<PAGE 41>>>）
- OS6860N-U28 控制台 smgrOpenLicenseFile 错误无功能影响（X46，<<<PAGE 43>>>）；CMM2+XNI-U48 板违规恢复比 WTR 多约 2 分钟（X51，<<<PAGE 41>>>）

## 来源
OmniSwitch AOS Release 8.10R4 Release Notes Open Problem Reports（<<<PAGE 41-46>>>）、Prerequisites（<<<PAGE 14-21>>>）、Appendix B MACsec Platform Support（<<<PAGE 62-63>>>）、Appendix C SPB（<<<PAGE 64-66>>>）、Hot-Swap Guidelines（<<<PAGE 47-49>>>）。条目来源：counter-examples X21-X25/X28-X31/X38-X44/X46-X48/X50-X53/X54-X57/X59/X60/X62/X63/X65；cases C14/C17-C19。
