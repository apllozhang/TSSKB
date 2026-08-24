# rejected/principles.md · 淘汰条目（阶段 1.5 三重验证）

共 36 条候选，淘汰 1 条（p31），其余 35 条见 verified.md。

---

## p31 · OV2500 服务参数默认值：VPN MTU 默认 1500 字节

- **淘汰原因：V3 独特性不过**
- V1 通过：source_quote 与 fulltext.md p102 逐字对应（"VPN MTU - Set the VPN MTU. The largest frame size, in octets, that the Service can handle. (Default = 1,500)"），原文真实。
- V2 勉强成立：可作为 OV2500 建服务时的默认值确认，但"默认值=以太网标准 MTU"，不改变任何操作决策——不填也是 1500，填 1500 与默认无差异，无预测增量。
- V3 不过：1500 字节是以太网默认 MTU，属于任何网工都知道的常识值；该条目的全部载荷只是确认工具默认与常识重合，无"只有读了这本书才知道"的信息。对照任务判例（"VLAN 隔离广播域"不过 / "AOS 支持 16 个 BVLAN 推荐 4 个"过），本条落在常识侧。
- 补充说明：同页其他 OV2500 参数规则已由 p32（I-SID 范围 256-16777214、untagged SAP 封装值 0）承载，该条有真实预测力并通过，p31 淘汰不造成信息缺口。
