---
name: industry-use-cases
description: 何时用：医院/酒店/高校/学院/轮渡/政府/零售行业投标需要案例页话术，或竞品（Aruba/Cisco/Ubiquiti）替换项目论证时。
source_book: DT00XPS288EN Stellar WLAN Presales
---

# 行业用例弹药库（七大案例 + 竞品替换共存路径）

## R · 原文引用

> "Recently, an hospital merged with 3 others for a total of 1000 beds … Total staff 1500 including 1100 caregivers. Replacement of the existing Aruba infrastructure."（p171）

> "Renewal of existing Wi-Fi infrastructure (Cisco). Deployment of an evolutionary Wi-Fi solution supporting 600 APs at the end of the project … EDUROAM SSID Authentication Compatibility … phase 1: Indoor AP (AP1321) & OV Cirrus."（p180-182）

> "Environmental challenges: Thick concrete walls, lack of accessible cabling, thunderstorms. Robust hardware required. Flexible solution that can accommodate the 400 daily users or up to 2000 users during events."（p184）

> "The metallic structure of the ferry impacts the radio coverage. … Increased number of outdoor AP1251 required to cover all parts of the bridge."（p188/p190）

## I · 方法论骨架

**四段式论证模板**：Identity（客户身份与规模）→ Challenges（业务+技术挑战，常含"替换某竞品"）→ Why ALE?（决定性理由）→ Benefits（技术/财务/体验收口）+ Technical Description（落到型号配置）。可直接改写为投标案例页。

反复出现的赢单理由（话术库）：**BP/ALE 联合 POC**、**无控制器架构降维护成本**（渡轮机舱没地方放控制器）、DPI 控流量、LAN/WLAN 统一管理、部署快、价格/性能/功能比优。

| 案例 | 行业 | 替换对象 | 关键弹药 |
|---|---|---|---|
| c01 千床医院 | 医疗 | Aruba | 双认证（PSK/WPA2）、UCOPIA 访客画像、VPN MPLS 拓扑、医疗专项认证 POC |
| c02 五星→宫殿酒店 | 酒店 | 改造 | 802.11ac wave2、AP1321/1322/1361、8 SSID/每射频 64 客户端、DPI、Chromecast 房间投屏、Ekahau 装后审计 |
| c03 理工大学 4000 人 | 教育 | Cisco | EDUROAM 兼容（802.1X/PEAP）、Chillispot 门户、GRE 访客隧道兜底、600 AP 演进 |
| c04 文理学院 | 教育 | Ubiquiti | 混凝土墙/雷暴→AP1361、400→2000 用户弹性、第三方交换机互通、BP 远程运维、两年零硬件故障 |
| c05 轮渡 20 船×1500 客 | 交通 | 既有 Wi-Fi | 金属船体 Ekahau 装前审计、客舱 VoD、室外 AP1251 加量 |
| c06 音乐学院 200 用户 | 政府/智慧城市 | — | UPAM/LDAP、UCOPIA、OPEN 门户 500 会话、Palo Alto 共存、100×AP1321 |
| c07 零售 40+ 门店 | 零售 | 增量 | ESL 电子价签复用 AP USB 口（详见 special-topologies） |

**竞品替换降风险双路径（c12，p117）**：Case A——新 Stellar 网对接存量 Aruba ClearPass 做认证；Case B——用新 OmniVista/UPAM 反向接管存量 Aruba Controller/IAP。认证层先行共存，避免一次性割接。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：行业客户投标写案例页；客户现网是 Aruba/Cisco/Ubiquiti 问"怎么换不伤业务"；要 POC 方案叙事。
- 区分：本 skill 是商务论证与话术；具体客房 AP 数量公式去 `rf-scenario-baseline`；ESL/Bridge/Mesh 等组网细节去 `special-topologies`。

## E · 可执行步骤

1. 按客户行业对号入座选 1-2 个最接近案例。
2. 套四段式模板改写：换入客户规模数字、竞品名、对应挑战。
3. Why ALE 段优先调用话术库三件套：联合 POC、controllerless TCO、统一管理。
4. 竞品存量客户：引用 c12 双路径设计认证共存/接管过渡方案。
5. Technical Description 落到具体型号（参考 `ap-selection-matrix`）。

## B · 边界与陷阱

- 全部案例只讲赢单、无翻车复盘；引用时补自己的风险披露更可信（ce23）。
- 轮渡案例的反面教训：金属环境装前勘察推翻 AP 规划、被迫加量——报价写"以勘察结果为准"调价条款（ce18）。
- 酒店案例装后审计发现信道重叠、靠缩信道宽度整改——把装后审计写进交付标准（ce17）。

---
来源条目: f13, c01, c02, c03, c04, c05, c06, c07, c12, ce17, ce18；glossary: EDUROAM、UPAM、GRE Guest Tunneling、DPI、Rainbow、Captive Portal、Hotspot 2.0、Ekahau
