# frameworks — OmniSwitch 6865 Hardware Users Guide（结构化框架候选）

格式：编号 F# ｜ 框架 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

- **F1** 6865 三机型选型矩阵（PoE 密度 vs 上行密度）：
  | 机型 | 形态 | 10G SFP+ | 1G SFP | 75W HPoE/bt 口 | 30W PoE+ 口 | VFL | 定位 |
  |---|---|---|---|---|---|---|---|
  | P16X | 半宽 2RU | 2 | 2 | 4 | 8 | 无 | PoE 供电密集（话机/AP/摄像头） |
  | U12X | 半宽 2RU | 2 | 6 | 4 | 0 | 无 | 光纤上行紧凑型 |
  | U28X | 全宽 1RU | 4 | 20 | 4 | 0 | 2×QSFP+ | 大量光纤上行 + 少量 PoE |
  共性：无风扇、1588v2、双电源（1主1备）、TMRA -40~74°C（有气流）<<<PAGE 42>>>-<<<PAGE 48>>>

- **F2** 加固交换机"环境-电源-PoE 预算"三环校验框架（选型/部署前逐环过）：
  ① 环境环：现场最高温决定气流需求（≥65°C 需气流、74°C 需封闭机柜）与顶部间隙档位（1/2 RU vs 1 RU）；DNV 盖一律按 55°C 降额 <<<PAGE 9>>>/<<<PAGE 11>>>/<<<PAGE 42>>>
  ② 电源环：AC(BP 180W) vs DC(BP-D 140/180W，-24V 输入预算再低 20-40W)；单/双电源；双电必须分电路分源 <<<PAGE 49>>>/<<<PAGE 50>>>/<<<PAGE 56>>>
  ③ PoE 环：预算=电源组合×温度档（60/65/74°C）查表（如双 BP@65°C 仅 150W）；再叠加 Guard Band（口上限 vs 剩余预算）与 Priority Disconnect（优先级+端口号 1 高 28 低）裁决规则 <<<PAGE 56>>>/<<<PAGE 57>>>/<<<PAGE 63>>>
  三环联动的铁律：任何一环升档（更热/更少电源/更大 PD）都要重查另两环。

- **F3** 五种安装形态决策树（6865 特有）：
  机架（默认，侧装托盘；U28X 加 REAR-MNT 后固定套件 / 双托盘用 TRAY-1U）→ 桌面（后装托盘+桌脚，散热片面朝外）→ DIN 导轨（工业柜，电源与机箱可分别上轨，垂直装仅限不可燃表面）→ 墙装（自备螺丝锚入墙柱）→ DNV 船用（FRCK 全架/HRCK 半架套件+电源盖，温度限 55°C）<<<PAGE 13>>>/<<<PAGE 21>>>/<<<PAGE 25>>>/<<<PAGE 28>>>/<<<PAGE 34>>>

- **F4** Dying Gasp 掉电告警部署框架（三通道覆盖）：
  ① SNMP：`snmp station` 配置接收站（仅前 3 个生效，含槽位/电源类型/时间）② Syslog：`swlog output socket` 加服务器（前 3 个，固定文案 "Dying Gasp Power Failure Event Occurred"）③ Link OAM：`efm-oam` + `propagate-events dying-gasp enable`（发 4 个 802.3ah PDU）；资源约束：并发 PDU 口数 = 10 - 已配 SNMP/Syslog 服务器数，上行口优先 <<<PAGE 54>>>/<<<PAGE 55>>>
