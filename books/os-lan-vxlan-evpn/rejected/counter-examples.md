# rejected/counter-examples.md · 淘汰条目

## ce06 传统 STP+VLAN 模型与裸 VXLAN flood-and-learn 的固有问题 —— 淘汰

- **V1 原文真实性：部分通过（转述而非原文）**。核心论点确在原文（p164 "Inefficient use of resources: The use of Spanning Tree Protocol (STP)..."、p166 "Constant flooding over the fabric..."），但 candidate 的 source_quote 把 p164 原文 "Operational complexity and administrative tax: VLANs are also required to be configured at every switch..." 改写成了 "Operational complexity (VLANs configured at every switch)"，属转述缩写，未严格逐字引用。
- **V3 独特性：不通过**。STP 阻塞冗余链路、VLAN 12bit/4096 上限、静态网关导致流量绕行（tromboning）、无控制面 VXLAN 依赖泛洪学习——这些是 EVPN 领域的入门级常识与所有厂商迁移论证的标准话术，不满足"非常识"门槛。
- **信息冗余**：该条论证链的核心内容已被 f09（EVPN 总体架构模型，含同页四痛点引用且引用更完整）覆盖，保留会产生重复单元。

**处置**：淘汰。如后续需要"为什么上 EVPN"的论证素材，直接使用已通过的 f09。

---

其余 8 条 counter-examples（ce01-ce05、ce07-ce09）均通过三重验证，见 `../verified.md`。
