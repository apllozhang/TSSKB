---
name: license-wwpl-pricing
description: 查 WWPL 价表、按五件套组 BOM、配各机型软件许可（含 MACsec 站点许可与 Demo 许可陷阱），守住报价商务底线。
source_book: DT00XPS281EN Campus LAN Presales
---

# License、WWPL 与下单 BOM

## R · 原文引用

> "OMNISWITCH ORDERING GUIDELINES — OmniSwitch model / Backup & POE Power-Supply / Stacking Interface, Cables, Transceivers and Accessories / Licenses. Switch model with '-ZZ' extension have no power cord included … For OS6860N models with '-00' extension PS must be ordered separately" (p328)

> "Product Availability: Standard … two (2) weeks ARO. Extended … Four (4) weeks. Contact: Product is announced but not released … Sales category designations are A, B, C … Consult your contract or channel partner for actual discount level." (p326)

> "Demo License: Available once for MPLS … Valid for 30 days total; Activated as soon as MPLS is run on a node. Permanent License … Each one is unique (serialized)" (p346)

## I · 方法论骨架

**BOM 五件套**：①整机型号 ②备份/PoE 电源 ③堆叠接口/线缆/光模块/附件 ④软件 License ⑤（配套）电源线。后缀规则：**-ZZ 不含电源线、-00 不含电源**（均需另下订单行）；P=PoE 机型、D=带 DC 电源 bundle。

**各机型许可要点（防漏行矩阵）**

| 机型 | 许可规则 |
|---|---|
| OS6570M | Metro 内置免许可；PRM12 开 AR+SPB；PERF 开 U28 额外 10G 口；PRM28 开 25G+AR+SPB |
| OS6870 | PERF 每台；PRM1 开 M/V 型 VXLAN EVPN+50G；PRM2 开 24/48/Z 型 VXLAN EVPN |
| OS6860N | MACsec 每台免费、MPLS 每台收费 |
| OS6560 | Metro/AR 许可制；上联口可许可升 10G |
| OS6360/6465 | MACsec 免费；6360 有 10G 升级许可 |
| OS6900/6920 | OS-SW-MACSEC（免费必须列入）+ MPLS 许可 |

**MACsec 站点许可**：OS-SW-MACSEC 每客户一份、零费用但必须显式下单；8.6R1 起不装即禁用，装后免重启。

**WWPL 读表与商务规则**：条目 = Family/Item + Sales Category（折扣级字母 A-Z/NA）+ Service Category（两位数字）+ Availability + List Price；USD/EUR 双币；**价格随时可变不另行通知；升级件（UPG/U SKU）不打折**。查价流程：MyPortal 下载当月 WWPL（含 Addendum 促销/新品/EOS）→ 查列表价与折扣级 → 按合同折扣算净价 → 标注供货分级。**供货分级**：Standard 平均 2 周 ARO、Extended 平均 4 周、Contact 已发布未上市须询 ALE 代表（标书写"交期待确认"）。

**Demo vs 永久许可**：Demo 仅 MPLS、每客户一次、30 天、节点上一跑 MPLS 即激活倒计时；永久许可序列化绑定特性集+平台。

## A1 · 书中案例

p246 订阅服务算例（详见 nms skill）：50 AP + 42 交换机 1 年 Advisor 订阅直接按设备数追加 BOM 行——"设备数=许可数"方法可迁移到一切按设备订阅的服务报价。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：拿到机型清单要出可下单 BOM；POC 排期涉及 demo 许可；投标前核价与交期承诺。
- 区分：本 skill 管**报价与下单的商务规则**；选哪台机器走 `omniswitch-model-selection`；网管平台自身许可走 `nms-platform-and-network-advisor`；MACsec 端口支持范围（技术侧）走 `security-unified-access`。

## E · 可执行步骤

1. 每机型过五件套清单（机型/电源/堆叠与光模块/License/电源线），检查 -ZZ/-00 后缀。
2. 对照许可矩阵补 ** 项：SPB/MPLS/AR/Metro/PRM/PERF/MACsec 逐行加。
3. 拉当月 WWPL，逐项查列表价、Sales Category 折扣级、Availability 分级。
4. 标注 Contact 项"交期待确认"；升级件按无折扣计价。
5. POC 项目：把 demo license 当一次性火柴，只在验收窗口激活，同时排永久许可采购流程。

## B · 边界与陷阱

- ce11：现网升级 8.6R1+ 后 MACsec 自动禁用直到装许可——升级步骤里必须排进 license 安装。
- ce12：Demo 许可一激活就倒计时，实验室顺手跑 MPLS 命令即耗光唯一额度。
- ce13：WWPL 三坑——升级件不打折、价格随时可变、Contact 交期无期；旧价目表报价可能废标或亏本。
- 功能矩阵打 ** 的项忘加 license 等于不支持（应标偏离）。
- 教材时点数据（Ed29），EOS 状态与价格以当月 WWPL 为准。

---
来源条目: f25, f26, f27, p23, p28, p29, p30, p31, p46, ce11, ce12, ce13, g05, g20, g37, g50
