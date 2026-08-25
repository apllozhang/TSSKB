# principles — OmniSwitch AOS 8.10R4 Transceivers Guide（光模块机制候选）

格式：编号 P# ｜ 机制要点 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

## MSA 与识别机制

- **P1** SFP MSA 标准接口：20 针插座 + 笼式外壳，模块内置串行接口提供能力/接口/厂商等识别信息——这是交换机识别模块与读取 DDM 的物理基础："Each SFP module contains a serial interface to provide identification information that describes the SFP capabilities." <<<PAGE 13>>>
- **P2** 认证模块红线：仅兼容矩阵中的 ALE 认证 PN 可用，他用模块导致不可预期行为、性能无保障且失保 <<<PAGE 1>>>
- **P3** 光/铜模块可同机混插，全部支持热插拔（hot-swappable），覆盖短距与长距场景 <<<PAGE 11>>>

## 安装与安全纪律

- **P4** 拔插间隔纪律：拔出模块后同端口至少等 10 秒再插入，给软件留出拔出检测时间："wait for a minimum of 10 seconds before re-inserting any transceiver into the same port." <<<PAGE 14>>>
- **P5** 三种释放机构对应操作：铰链式开到 90° 拉出（插入时须闭合）、bail wire 拉下压杆拔出（插入时闭合）、弹出器按钮用随机工具顶出后再夹出；任何时候不得强行插拔 <<<PAGE 15>>>/<<<PAGE 16>>>
- **P6** OS6865 机框特性：笼体有轻微压力，模块难拔时左右轻晃同时稳拉 <<<PAGE 14>>>
- **P7** 三大安全注意：ESD（腕带贴皮肤接机壳/接地柱）、防尘（不用的模块套回橡胶防尘帽）、激光（Class 1 激光，规范使用外可能有害辐射；25G/40G/50G/200G/400G 章节另有 CLASS 1M 开盖勿直视警示）<<<PAGE 14>>>/<<<PAGE 40>>>等
- **P8** QSFP 拔除用橡胶/金属释放手柄直拉 <<<PAGE 16>>>

## 线缆机制

- **P9** QSFP↔QSFP 40G/100G 直连：MPO trunk 8 芯或 12 芯（只用 8 芯），必须 Type-B 交叉 <<<PAGE 17>>>
- **P10** 40G MPO 拆 4×10G：MTP-LC 母头 splitter，8 芯对应 4 个 LC，LC 可手工重排收发 <<<PAGE 17>>>
- **P11** DAC 三级长度体系：1G 无 DAC；10G DAC 60cm-7m；25G/50G 0.5-5m；40G 40cm-7m；100G 40cm-5m；200G/400G 0.5-3m——机柜内布线用 DAC、跨柜用 AOC/光纤 <<<PAGE 34>>>-<<<PAGE 63>>>
- **P12** AOC 有源光缆跨柜短距：10G 无（用光模块）；25G A20M 20m；40G AOC20M 20m；100G A20M 20m；200G A20M 20m；400G A10M 10m <<<PAGE 42>>>-<<<PAGE 62>>>

## DDM 与协商机制

- **P13** DDM 支持与型号强相关：光模块多数支持，铜口模块（SFP-GIG-T/SFP-1G-T/SFP-10G-T）与全部 DAC 一律 Not Supported；QSFP-40G-SR 等 DDM 仅报 V/T/mA/Input 四参，阈值为 0 时显示 NS <<<PAGE 20>>>-<<<PAGE 24>>>/<<<PAGE 44>>>
- **P14** DDM 读数存在个体偏差：实际值与上报值在收发两侧均可能有轻微 variance <<<PAGE 74>>>
- **P15** 双速模块手工定速原则：dual-speed 收发器建议两端手工配速防止速率失配（100BASE-FX/1000BASE-LX 双态）："it's recommended to manually configure the speed on both ends to prevent speed mismatch." <<<PAGE 25>>>
- **P16** SFP28 口与 1G 模块不协商：6860N/6900 的 SFP28 口不支持与 1G 模块自协商，必须在对端交换机禁用自协商："SFP28 ports do not support auto-negotiation with 1G transceivers. Always disable auto-negotiation on the peer switch." <<<PAGE 92>>>/<<<PAGE 102>>>
- **P17** 10G-T 新旧件版本双轨：老 PN（903866-90 HW Rev -43/-54）配任意 AOS；新 Rev A53 需 ≥8.9R3、Rev V1.0 需 ≥8.10R2；SFP-GIG-T/SFP-DUAL-MM-N 新序列号（APxx…）需 ≥8.9R3——同型号模块看硬件修订/序列号定最低版本 <<<PAGE 24>>>/<<<PAGE 34>>>/<<<PAGE 25>>>
- **P18** 2019 年 5 月采购分界：BX-D/U 等模块 2019-05 之后采购的最低版本提到 8.6R1 <<<PAGE 82>>>/<<<PAGE 99>>>

## 拆分与 VFL 机制

- **P19** 40G/100G 拆分体系：QSFP-40G-SR/PSM4 支持 4X10G splitter 模式；QSFP-100G-SR4 支持 4X25G；QSFP-4X10G-SR/C 与 QSFP-4X25G-C 是专用拆分模块/线缆；400G SR4.2 可拆 4×QSFP-100G-SR1.2 <<<PAGE 44>>>/<<<PAGE 53>>>/<<<PAGE 48>>>/<<<PAGE 55>>>/<<<PAGE 63>>>
- **P20** 拆分模式牺牲自动 VFL：6870 的 QSFP-100G-SR4 在 splitter 模式不支持 Auto-VFL <<<PAGE 96>>>
- **P21** VFL 连接专用/禁用模块清单：QSFP-40G-AOC20M 与 OS6860-CBL 系列为"VFL 连接专用"（AOC20M 仅 20G VFL、CBL 为 20G VFL 线）；SFP-10G-BX 系列与 QSFP-40G-SR-BD 明确"不支持 VFL 连接"——VFL 口选件要看此标注 <<<PAGE 88>>>/<<<PAGE 49>>>/<<<PAGE 37>>>/<<<PAGE 44>>>
- **P22** QSFP-40G-C7M 跨厂商验证：7m DAC 仅在 OmniSwitch 之间验证过，接他厂设备建议先验证再上量 <<<PAGE 48>>>

## 功耗与选型机制

- **P23** 功耗梯度（每口散热预算）：1G/10G 光模块 ≤1-1.5W；10G-T 铜口 2.5W@30m；25G 1.2-1.5W；40G 1.5-3.5W；50G 2-3.3W；100G 3.5-4.5W；200G 4.5-6W；400G 高达 10-12W——高密 400G 要先核电源与风冷 <<<PAGE 32>>>-<<<PAGE 63>>>
- **P24** 温度两档：商用 0~70°C（个别 -5/-20/85 端点）；工业 iSFP 系列 -40~85°C（配 6575/6465 工业平台）；部分长距模块（LH40/LH70/EZX）上限收窄到 -10/-5~70°C <<<PAGE 18>>>-<<<PAGE 73>>>
- **P25** 单双纤配对原则：BX（Bi-Directional）系列必须 D/U 成对使用（一端 D 发 1490/收 1310，另一端 U 反之）——设计单纤链路时两端 PN 必须配对下单："Designed for use with SFP-GIG-BX-U." <<<PAGE 21>>>-<<<PAGE 24>>>等
- **P26** 距离档位体系（SMF）：LR/CLR=10/2km，LH40/ER/ER4=40km，LH70=70km，ZR=80km，EZX=120km；MMF 按 OM2/OM3/OM4 递减表选型（如 25G-SR：OM2 20m/OM3 70m/OM4 100m）<<<PAGE 18>>>-<<<PAGE 57>>>
- **P27** 100G A20M 特例：需禁用自协商并把 FEC 配成 RS <<<PAGE 55>>>
- **P28** 6865 平台用 iSFP 工业模块体系（6575 同），而 6360/6560/6860/6870 等商用平台用对应商用 PN——同代际两套 PN 并行 <<<PAGE 77>>>/<<<PAGE 93>>>等
- **P29** 10G-GIG-SR/LR 双速（10G/1G 自适应）按光纤分级：OM1 33m@10G、OM2 82m、OM3 300m；1G 时 OM1 275m/OM2·OM3 550m——旧布线升级 10G 的过渡件 <<<PAGE 36>>>
- **P30** 兼容矩阵双列最小版本语义（如"8.7R2 or 8.9R3"）：前者为老硬件最低版、后者为新硬件修订最低版，二者满足其一即可 <<<PAGE 75>>>/<<<PAGE 98>>>等

---
合计：30 条（P1-P30）。
