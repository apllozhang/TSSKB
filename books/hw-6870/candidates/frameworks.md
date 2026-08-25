# frameworks — OmniSwitch 6870 Hardware Users Guide（结构化框架候选）

格式：编号 F# ｜ 框架 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

- **F1** 6870 九机型选型矩阵（PoE 等级 × 上行速率 × 模块化）：
  | 机型 | 下行 | 下行 PoE | 上行 | 模块槽 |
  |---|---|---|---|---|
  | OS6870-24 | 24×1G RJ45 | 无 | 4×SFP28(25G)+2×QSFP28(100G) | 无 |
  | OS6870-48 | 48×1G RJ45 | 无 | 4×SFP28+2×QSFP28 | 无 |
  | OS6870-P24M | 24×多千兆(10G) | 95W bt | 2×QSFP56(200G) | 有 |
  | OS6870-P48M | 48×多千兆(5G) | 95W bt | 2×QSFP56 | 有 |
  | OS6870-P24Z | 24×多千兆(2.5G) | 60W bt | 6×SFP28+2×QSFP28 | 无 |
  | OS6870-P48Z | 48×多千兆(2.5G) | 60W bt | 6×SFP28+2×QSFP28 | 无 |
  | OS6870-V12 | 12×SFP28 | 无 | 2×QSFP56 | 有 |
  | OS6870-CNI-U2 | — | — | 2×QSFP28 | 无 |
  | OS6870-LNI-U6 | — | — | 6×SFP56(50G) | 无 |
  决策三问：要不要 95W AP（→M）；要不要 200G/后配上行（→M/V12）；预算型 60W PoE（→Z）<<<PAGE 12>>>/<<<PAGE 23>>>-<<<PAGE 38>>>

- **F2** PoE 供电预算四变量联动框架：
  ① 机型（决定可用电源型号与每口能力）② 电源瓦数（600W/1200W/2000W；Z 系列上限 1200W）③ 单/双电源（双电负载分担、预算非简单翻倍，如 P24M 双 600W=788W）④ 市电电压（双值条目=低压/高压输入；1200W/2000W 需 190-240VAC 才得高 PoE 功率）→ 查预算表得总瓦数，再叠加 Guard Band（口上限 vs 剩余）与 Priority Disconnect（low/high/critical + 端口号 1 高 48 低）两级裁决；落地检查命令 `show lanpower slot` <<<PAGE 47>>>/<<<PAGE 51>>>-<<<PAGE 53>>>/<<<PAGE 63>>>/<<<PAGE 67>>>-<<<PAGE 70>>>

- **F3** 6870 上电-入网标准七步流程（cangjie 可执行框架）：
  ① 安装（机架双人/桌面四脚，盲板常装）② 多电源数秒内相继插电 ③ 观察 OK/PS LED 至启动完成 ④ console 115200-8N1 rollover 登录 admin/switch ⑤ 解锁会话（aaa authentication … local）⑥ 改密+时区+时间+contact/name/location ⑦ `write memory` 保存；PoE 机型追加 `lanpower slot service start` 物理激活 <<<PAGE 17>>>-<<<PAGE 21>>>/<<<PAGE 65>>>

- **F4** 电源选型与演进框架（同一 P 系列机箱内三档平滑升级）：
  600W（入门，P24M 单电 242W/P48M 单电 216W PoE）→ 1200W（中档，双电 1516-1880W；190-240VAC 建议）→ 2000W（高密 95W bt，仅 M 系列，P48M 双电最高 3309W）；支持混插（"Mixing different wattage power supplies in a chassis is supported"），扩容可先混后替 <<<PAGE 47>>>/<<<PAGE 51>>>-<<<PAGE 53>>>/<<<PAGE 63>>>
