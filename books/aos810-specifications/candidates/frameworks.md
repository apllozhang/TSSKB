# frameworks — 体系框架（OmniSwitch AOS 8.10R4 Specifications Guide）

格式：编号 F# ｜ 框架名 ｜ 结构与运用 ｜ 页码

- **F1** AOS 文档地图四阶段法：Stage 1 首次开箱（硬件指南+Release Notes）→ Stage 2 熟悉单机（硬件指南+Switch Management Guide）→ Stage 3 入网（Network Config / Advanced Routing / Data Center Switching）→ Anytime（CLI Reference 全量命令）；本手册自身定位为四本配置手册的规格表配套，只答"能到多少"不答"怎么配"。 <<<PAGE 8>>>/<<<PAGE 9>>>
- **F2** 平台规模三梯队选型框架：接入级（6360/6465/6560：MAC 16K、路由 32-2K、聚合 32 组）→ 汇聚级（6570M/6575/6860 系：MAC 32-64K、路由 12-13K、聚合 128）→ 核心/数据中心级（6870/6900/6920/9900：MAC 104-228K、路由 113-384K、聚合 252+）；同级内再看 SM/RM/ER 转发 profile 二次放大。规划口诀：先选梯队、再选 profile、最后对 TCAM 档位。 <<<PAGE 30>>>/<<<PAGE 42>>>
- **F3** TCAM profile 零和分配框架：TCAM 总量固定，profile 在 QoS 入规则/SAP 分类/VSTK 翻译/业务隧道/DHCP snooping/UNP 用户/PVLAN 之间做此消彼长（如 6870 QoS ACL 档 QoS 4096 但 SAP 1024；6570M Fabric 档隧道+UNP 换掉 PVLAN/VSTK）；选型三步——列出必开特性清单→逐 profile 核对资源列→接受牺牲项后 reload 生效。 <<<PAGE 87>>>-<<<PAGE 92>>>
- **F4** VC 规格解读框架：所有 maximum 默认作用于整 VC（非单机）→ 三类例外要辨明——按机箱×成员数扩的（UNP 用户脚注 1 平台）、VC 封顶的（脚注 2 平台、6900 ARP 取最低模块）、仅单机的（1588v2 VC-of-1）；混搭先查白名单（6900 系内/6860+6865/6465 系内），6860N 是孤岛。 <<<PAGE 12>>>/<<<PAGE 23>>>/<<<PAGE 24>>>

---
合计：4 条（F1-F4）。
