# frameworks — OmniSwitch 9900 Series Hardware Users Guide（结构化框架候选）

格式：编号 F# ｜ 框架 ｜ 页码（fulltext.md 真实 `<<<PAGE N>>>` 标记）

- **F1** 9907 vs 9912 机箱选型矩阵：
  | 维度 | OS9907 | OS9912 |
  |---|---|---|
  | 高度 | 11RU | 17RU |
  | 总槽位 | 7（2 CMM + 5 NI） | 12（2 CMM + 10 NI） |
  | slot2 双角色 | CMM 或 NI（NI 仅 8 口活、失 CMM 冗余） | 仅 CMM |
  | 风扇托盘 | 3×（每托 3 扇） | 3×（每托 5 扇） |
  | 重量 | 32.83kg | 64.36kg |
  | CFM 带宽/块 | 2.56T（CFM）/12.8T（CFM2） | 25.6T |
  | 9912 不支持 NI | — | P48Z16/P24Z8/UP24Q2/U12Q |
  | VC-of-2 | 支持（三组合） | — |
  共性：4 电源槽 N+1、CFM3/4 预留、仅前→后气流、23" 深 <<<PAGE 5>>>/<<<PAGE 6>>>/<<<PAGE 11>>>/<<<PAGE 22>>>/<<<PAGE 24>>>-<<<PAGE 26>>>

- **F2** CMM/CFM 兼容组合决策表（升级与采购防错）：
  支持的三种同箱组合：①CMM+CMM / CFM+CFM（旧体系）②CMM+CMM / CFM2+CFM2（CFM2 需 AOS≥8.9R1）③CMM2+CMM2 / CFM2+CFM2（CMM2 需 AOS≥8.10R2）；禁止：任何新旧混插。VC-of-2 双机箱只允许两箱对称（CMM+CFM↔CMM+CFM 等）。升级路径只有整代切换：先备份数据→确认 AOS 版本→整箱换 CMM2+CFM2 <<<PAGE 17>>>/<<<PAGE 20>>>/<<<PAGE 22>>>

- **F3** 机箱功率预算三步法（变更前必走）：
  ① 查现状：`show chassis` 看 Power Left（可用瓦数）② 算增量：新增组件功耗（CMM 64/74W、CFM 119W、NI 56-402W、风扇 112/200W、PoE PD 预算）+ PoE 模块 slot 默认 1800W ③ 执行纪律：组件插入中板即生效功率需求，不足则不上电甚至中断数据流；单电源不可热拔，四电源 N+1 负载分担；拆件间隔 30s、插件间隔 5 分钟+LED 无错 <<<PAGE 23>>>-<<<PAGE 26>>>/<<<PAGE 29>>>/<<<PAGE 49>>>/<<<PAGE 63>>>

- **F4** 组件安装/拆除标准作业序列（满载机箱从头搭建）：
  空机箱就位（三人）→ 装 CFM（先拆风扇托盘→锁杆三步→装回风扇）→ 装 NI 模块（锁杆 90 度闭锁）→ 装 CMM → `show chassis` 核功率余量 → 装电源（手柄 down 入位→up 锁定→数秒内相继插电）→ 判主 CMM 四绿（PRI/PS/FAB/TEMP）→ console 9600-8N1 首次登录七步；拆除逆序且各守纪律（电源托底、风扇托盘速装回、CFM≤120s、NI 同类替换）<<<PAGE 36>>>-<<<PAGE 45>>>/<<<PAGE 57>>>-<<<PAGE 63>>>
