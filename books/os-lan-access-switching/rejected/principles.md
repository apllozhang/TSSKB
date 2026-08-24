# rejected · principles

## 淘汰清单（1 条）

- **p18 VLAN 1 是不可删除的默认 VLAN**
  - 淘汰原因：V3 独特性不足。"VLAN 1 不可删除"是 Cisco/Juniper/H3C 等各厂商交换机的通识事实，quote 与 summary 均为通用概念描述，未带 AOS 特有实现细节（仅泛提 admin-state，无 AOS 独有命令语义）。且同一事实已由 ce10（counter-examples，"VLAN 1 不能删除，只能停用"，带 AOS Lab 清理场景与 no vlan 1 不被支持的 CLI 细节）覆盖，保留 p18 会造成知识单元重复。
  - 备注：V1 已核实 quote 真实命中（fulltext.md "This VLAN CANNOT be deleted, but it can be disabled if desired"）；仅 V3 不通过。

## 其他类型淘汰情况

- frameworks：0 条淘汰
- cases：0 条淘汰
- counter-examples：0 条淘汰
- glossary：免验，0 条淘汰
