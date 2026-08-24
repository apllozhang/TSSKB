---
name: lan-troubleshooting-methodology
description: 何时用：开始排任意网络故障前，确定切入方法（OSI 六法）、准备文档基线、先查 TKC 知识库再动手。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# LAN 排障总方法论与 TKC 知识体系

## R · 原文引用

> "Flow chart of a structured troubleshooting approach: Gather symptom -> Isolate the problem -> Implement Corrective action -> Problem Fixed ? ... Document the solution and save the change" (p51)

> "Three different approaches use OSI as a troubleshooting framework: Bottom-Up, Top-Down, Divide and Conquer ... Three other approaches: Follow the path, Spot the differences, Move the problem" (p57)

> "Documentation is critical to being able to troubleshoot a network: Logical topology diagram, Inventory, Design documents, IP Addresses, Physical topology diagram, Interconnections, Configuration management, Blue print, Baseline performance levels" (p53)

> "TKC – a Database composed of technical articles. These articles are written by the Technical Support ... In the search box, you can use natural language to write your search." (p24/p31)

## I · 方法论骨架

1. **七步主流程**（p52）：Identify → Re-Create → Isolate → Locate（用 OSI 定位层/设备/物理位置）→ Solve → Verify → Document。不可复现则回到第一步继续追问。
2. **六种切入方法**（p57-58）：基于 OSI 的 Bottom-Up（物理层往上，适合硬件线缆类，慢）、Top-Down（应用往下，适合软件导向）、Divide and Conquer（中间层二分，适合复杂新问题）；另外三种 Follow the path / Spot the differences（对比正常与异常设备配置差异）/ Move the problem（组件换位观察）。选择依据：老问题直接套经验，新问题按硬件/线缆/软件导向选层。
3. **症状-原因索引**（p61-65）：物理层（性能低于基线/断连 ← 电源、布线、衰减噪声、超设计极限）；链路层（广播过量/成帧错误 ← STP 环路、ARP 缓存、速率双工不匹配）；网络层（路由表/邻居/拓扑库、IP 重复、ACL）；传输层（重传/分片/NAT）；高层（DNS、协议故障）。
4. **排障前提九类文档**（p53）：没有就先用命令重建——show lldp remote-system、show vlan members、show linkagg port 画出物理/逻辑拓扑（LAB1 即如此要求）。
5. **先查库再动手**（p24-31）：TKC（Partner Portal / My Portal 进入）用自然语言检索，用例结构固定为 Case Description（拓扑/场景/环境/诊断）+ Resolution（配置/热补丁/固件升级）。第二渠道：Spacewalkers 开放社区（www.spacewalkers.com）论坛历史帖。
6. **升级 TAC 的门槛**（p54）：开 eService Request 必须备齐最小信息与 Case Severity 定义，信息齐全直接缩短处理周期。

## A1 · 书中案例（LAB 故障根因）

- **c01（LAB1 前置，p132）**：TKC 检索两个真实缺陷——N1：OS6900-V48C8 VC 重载后 10G linkagg 链路保持 DOWN（版本 8.8.56.R02/8.9.73.R01/8.9.106.R02，软件缺陷，TKC 给修复版本）；N2：OS6560 VC（AOS 8.5.265.R02）部分 UNP 用户卡 "In progress"。训练点：版本相关故障先查 TKC，用例里的版本号能直接命中。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：接到任何故障报告、开始排障前的第一动作；或排障陷入僵局需要换切入方法。
- 与后续 skill 的区分：本 skill 只定"怎么查、查什么文档、先查哪个库"，不涉及任何具体故障域。一旦定位到某层/某协议（启动、L2、STP、VC、L3、组播、应用），转对应 skill 执行。

## E · 可执行步骤

1. 确认九类文档在手；缺失则用 `show lldp remote-system`、`show vlan members`、`show linkagg port` 重建拓扑基线。
2. 用自然语言把现象描述进 TKC 检索；命中则直接取 Resolution（配置/热补丁/固件升级），先试后查。
3. 按症状在 OSI 各层"症状→原因"表（p61-65）上初步定位故障域。
4. 选择切入方法：硬件/线缆线索 → Bottom-Up；应用软件线索 → Top-Down；复杂新问题 → Divide and Conquer；多设备对比 → Spot the differences。
5. 走七步流程：收集症状 → 复现 → 隔离 → 定位 → 修复 → **验证**（复测到基线才算修好）→ 记录方案并保存变更。
6. 无法解决准备开案：按 p54 备齐最小信息（拓扑、版本、日志、已做动作）再提 eService Request。

## B · 边界与陷阱

- 不可复现的问题不要跳到"修复"步骤——回到第一步继续追问（p52 流程图明确回路）。
- TKC/文档优先原则：一线先查库，开案信息不全会被打回（p02）。
- 本 skill 的 OSI 表只是索引，各层具体命令族在对应故障域 skill 中；不要在本层直接开 debug。
- Spot the differences 需要一台"正常"参照设备，实验室可用，生产环境常缺——退化为与历史配置基线比对。

---
来源条目: f01, f02, f03, p01, p02, p03, c01, g01, g02
