# BOOK_OVERVIEW · OmniAccess Stellar WLAN Presales (DT00XPS288EN Edition 28)

> 教材: Alcatel-Lucent Enterprise Training Services, 2025-02 · 273 页 · 参训者指南
> 定位: Stellar 无线售前全科书 —— AP 产品矩阵 → 三种管理模式 → License/报价（OV2500 / Cirrus 4 / Cirrus 10 三套）→ 行业用例 → VoWLAN → Network Advisor

## 一、结构（书的骨架）

1. **硬件总览** (p8-38) —— AP 全家族：Wi-Fi 5/6/6E/7 各代、室内/室外/加固/医疗（AP1301H）/多射频（AP1221/1322），USB 口玩法
2. **网管模式** (p39-101) —— **三种管理模式的选型是本书第一根主轴**：
   - Stellar Express（无 License，免云管，5 个永久 AP License）
   - Stellar Enterprise On-Premise（OV2500 本地管）
   - Stellar Enterprise Cloud（OmniVista Cirrus 云管）
   - 无控制器架构（Controller-less）是贯穿卖点
3. **模式特性对比** (p79-125) —— 各模式支持的功能矩阵（RF 管理/Guest/WIPS/报表…）+ 通用特性（DPI/应用管控/Bonjour 网关/定位）
4. **License 与报价** (p126-168) ★商务核心
   - OV2500：AP/Guest/OnBoarding/HA/WCF 五类 License，part number 规则（OV-AP-NM-X-N 等），维护合约 PW/SP 编码
   - Cirrus 4：Freemium（免费不限量）vs Premium 订阅；LAN Core/Essential/Advanced 分类；Base/Business/Premium 服务包
   - **Cirrus 10**（新一代）：OVCX-[类别7]-[级别3]-[时长3]=63 个 part number 的命名语法，eBuy→Subscription Manager→云导入激活全流程
5. **行业用例** (p169-199) —— 医院（换 Aruba）/五星酒店/理工大学（换 Cisco，EDUROAM）/文理学院（换 Ubiquiti）/轮渡船队/音乐学院/零售 ESL 电子价签（AP USB 口接 ESL dongle）
6. **VoWLAN** (p200-212) —— 话机矩阵（8118/8128/8158s/8168s + Rainbow 软终端）、五步部署法（Prepare→Plan→Design→Implement→Operate）、语音容量经验值（1 AP/255m²、20-25 客户/AP、-62dBm 漫游阈值）
7. **Network Advisor** (p213-235) —— AI 运维伴侣（异常库 40+ 预置、Rainbow/Teams 一键修复），License 按设备每年（AP $50/年、交换机 $100/年）
8. **AP 配置部署指引** (p236-266) —— 快速开局流程

## 二、解释（核心论点）

- **第一主轴"模式选型"**：同一个 AP 硬件，用 Express/本地/云三种玩法，分别打 SMB、安全敏感型、多分支连锁三类客户 —— 这是 ALE 无线商务模型的核心（硬件+订阅分离）；
- **"无控制器"叙事**：所有用例里反复出现"controllerless 降低维护成本/渡轮机舱没地方放控制器"，把架构差异转成 TCO 优势；
- **License 三套并存的现实**：OV2500（永久式）、Cirrus 4（过渡云）、Cirrus 10（新 SaaS 订阅）同场销售，书用大量篇幅教"怎么报价不出错"（63 个 part number 的语法拆解就是防错设计）；
- **用例即话术库**：每个案例都是 Identity→Challenges→Why ALE?→Benefits 四段式，直接可改成投标案例页；
- VoWLAN 章给出可背的工程常数（每 AP 用户数、RSSI 阈值、5GHz 优先），是售前答技术质疑的底牌。

## 三、批判（局限与盲点）

- 三套 License 体系并存本身就是本书最大的"乱"，Cirrus 4 与 10 的迁移路径（老订阅怎么办）着墨少；
- 用例只讲赢的原因，无落选/翻车复盘；
- Wi-Fi 7（AP15xx）内容较浅，无与竞品（Cisco Catalyst 9130 等）的对比数据；
- Network Advisor 报出的美元价是目录价，区域折扣未提。

## 四、应用（对售前的可执行价值）

- 客户说"我只要简单的 WiFi" → Express 模式 5 分钟讲完 + 5 免费 License；
- 中型客户云管报价 → Cirrus 10 的 OVCX 语法直接拼 part number（如 OVCX-68-BIZ-3Y）；
- 医院/酒店/学校投标 → p169-199 对应案例四段式改写；
- 语音覆盖勘察 → p207-209 的容量常数 + 五步法做方案骨架。

## 五、术语速览（详词典见 GLOSSARY.md）

Stellar Express/Enterprise（免管/企业管理模式）、OV2500-NG-AP（AP License part number 族）、OVCX-[Category]-[Level]-[Duration]（Cirrus 10 License 语法）、Freemium（免费版云管）、VoWLAN（无线语音）、ESL（电子货架标签）、UPAM（认证）、EDUROAM（教育网漫游 SSID）、Ekahau（无线勘察工具）、Network Advisor（AI 运维）
