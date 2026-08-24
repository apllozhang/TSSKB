---
name: virtual-chassis-design
description: 设计虚拟机箱堆叠方案：VC 台数、VFL 规则、主从选举、防脑裂（RCD/VCSP）与远程堆叠部署。
source_book: DT00XPS281EN Campus LAN Presales
---

# 虚拟机箱（VC）堆叠设计

## R · 原文引用

> "STACKING / VIRTUAL CHASSIS TOPOLOGIES — 8 x OmniSwitch [6465] T/P6/P12/P28 models; 4 x OS6465; 6 x OS6900-X/T/V/C; 2 x OS9907; 4 x OS6360 … OS6560/E OS6860E* OS6865* OS6570M OS6860N OS6870 (up to 8, ring)" (p59)

> "Master/Slave election based on virtual chassis protocol (ISIS-VC): Highest chassis priority value; Longest chassis uptime (if difference in uptime >10 mn); Smallest Chassis ID value; Smallest chassis MAC address" (p66)

> "Failures on VFL links cause potential MAC/IP duplication. 2 mechanisms: Out of Band: EMP Remote Chassis Detection (RCD); In Band: VC Split Protocol. … One sub-VC assumes 'MASTER' status & other 'Protection' status … Shuts off all user ports" (p71-74)

## I · 方法论骨架

**VC 台数规则（免 license）**

| 机型 | 最大台数 / 拓扑 |
|---|---|
| OS6900 家族 | 6 台 mesh |
| OS9907 | 2 台（chassis-id 必须静态配） |
| OS6920 | 初版 2 台（roadmap 4） |
| OS6360（24/48 口型） | 4 台（10/P10 型不做 VC） |
| OS6465 | 4 台（p59 另标 8 台，矛盾需注版） |
| OS6575 P12/U28 | 4 台 |
| 6560/E、6860E、6865、6570M、6860N、6870 | 8 台环形（专用 VFL 口） |

**VFL 硬规则**：单 trunk 按机型最多 16 成员口；速率不可混；6860N 与 6870 不可同 VC（6860/6860E/6865 可混）；6860N 100G VFL 远程必须暗光纤；9900 VFL：10G 用 CMM QSFP 40G→10G 分支、100G 用 CMM2 QSFP28；6920-D32 最多 8 口、50-400G。

**两大阵营**：9900/6900 阵营静态/自动 chassis-id（9900 强制静态，每台写 vcsetup.cfg）；其余阵营自动分配、2-8 台环形。默认 VFL 口号速查：6560/E 24 口型 29-30、48 口型 53-54；6465-P28 27/28；6360 11/12（10 口）、27/28（24 口）、51/52（48 口）。

**主从选举四级判据**：优先级 → uptime（差 >10 分钟才算）→ 最小 chassis ID → 最小 MAC。规划主备时把目标 master 的优先级配高即可。

**防脑裂双机制（方案必预置其一）**：
- 带外 RCD：走 EMP 口；选址顺序先 NVRAM 的 CMM IP、再 chassis EMP IP；无 EMP 口机型（6360/6560 等）须加 USB 转 Ethernet 适配器，仅支持 ASIX 8817 与 RealTek RTL8153。
- 带内 VCSP：借上/下游 helper 交换机，建议每个 VC 成员出一个口加入 VCSP LAG。分裂后非 Master 子 VC 进 Protection 模式关闭全部用户口（保留 LAG/VFL 口）。

## A1 · 书中案例

c09（p309）：8×OS6860N 组 VC（100m 内远程堆叠，VFL 20/40/100G），384 千兆口或 192 多千兆口、95W PoE 供 Wi-Fi 6/7 AP，4×25G LACP 上联 OS6900 核心。c15（p79）：OS6870 中型核心 + 各楼宇接入机经 10/25/40/100G 链路做远程 VC 跨楼堆叠成单一管理实体。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：客户要"多台当一台管"、跨楼宇远程堆叠、或高密度接入边缘（8 台 VC）；售前防守"堆叠不如机箱"。
- 区分：本 skill 管 **VC/VFL 机制与台数设计**；"要不要选 VC 这个路线"的高可用对比在 `campus-design-tiering-and-ha`；具体机型容量在 `omniswitch-model-selection`；auto-VC 开箱自动组网行为在 `ifab-zero-touch-automation`。

## E · 可执行步骤

1. 按机型查台数上限与拓扑（mesh 还是 ring），确认家族可否混插。
2. 规划 VFL：同速率、专用口或指定口、按跨堆叠流量定成员口数；远程堆叠选对光模块（6860N 100G 用暗光纤）。
3. 定主备：目标 master 配最高优先级；9900 阵营逐台写 vcsetup.cfg 静态 chassis-id。
4. 预置防脑裂：有 EMP 口走 RCD；无 EMP 口加 USB 适配器（ASIX 8817/RTL8153）或改 VCSP + helper LAG。
5. 输出 VC 设计页：台数/拓扑/VFL 口与速率/主备优先级/防裂机制，交 BOM（适配器别漏）。

## B · 边界与陷阱

- ce01：脑裂是 VC 最大单点风险——VFL 全断则 MAC/IP 双主，未预置 RCD/VCSP 即裸奔。
- ce02：无 EMP 机型做 RCD 必须自购指定型号 USB 适配器，售前最易漏配的小物件。
- ce05：VFL 速率混用不成立；6860N+6870 混 VC 不成立；6860N 100G VFL 走波分会不通。
- p07 矛盾标注：p59 对 6465 同时标 8 台与 4 台（p22 称 4 台），引用需注版并按 datasheet 复核。
- 网管许可不吃 VC 的账：每台成员单独计 license（见 license skill ce15）。

---
来源条目: p07, p08, p09, p10, p11, c09, c15, ce01, ce02, ce05, g35, g43, g44, g45
