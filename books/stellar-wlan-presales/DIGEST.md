# DIGEST · Stellar WLAN 售前精华：不读全书，只看这一篇

> 原书：DT00XPS288EN《OmniAccess Stellar WLAN Presales》Edition 28，ALE 培训服务部 2025-02，273 页。本文是全书与 8 个蒸馏 skill 的浓缩版，数字均标注原书页码。

---

## 一、一页看懂 Stellar WLAN 售前

Stellar 是 ALE 的无线产品线，打法一句话：**硬件 + 管理订阅分离，同一台 AP，三种玩法卖三类客户**。

**产品线骨架**（p8-38）：

- AP 家族覆盖 Wi-Fi 5/6/6E/7 四代，形态分室内（Indoor）、室外三防（Outdoor Rugged，-40~+65°C）、客房/病房壁挂（Hosp. AP1301H）、多射频高密（AP1231/AP1321 三射频）；
- Wi-Fi 7 目前只有 AP1511（入门，5GE 上联）和 AP1521（中档，10GE 多速率口，5GHz 4x4 2.88Gbps + 6GHz 5.76Gbps，p27）；
- 下单编码规则：`OAW-APxxxx-Region`（RW/JP/ME/US），区域码写错设备注册直接失败；
- 尾数"2"的机型（AP1322/AP1362）支持外接天线，其余全是内置天线（p32）。

**贯穿全书的叙事是"无控制器"（Controller-less）**：AP 之间自组集群、自己选主备（PVM/SVM），不需要买 AC（无线控制器）。书里每个行业案例都拿这条打 TCO——轮渡项目最典型："机舱里根本没地方放控制器"（p188/p190）。售前把架构差异翻译成"省一台 AC 的钱、少一个故障点、部署更快"，就是 Stellar 的第一话术。

三根主轴撑起全书：**模式选型**（第 2 节）→ **License 报价**（第 3 节）→ **行业用例 + 场景常数**（第 4、5 节）。

---

## 二、模式选型三岔口

教材 p41 给出三种管理模式，选型就两个变量：**网络规模 × 管理偏好**。

| 维度 | Express（免管） | Enterprise（OV2500 本地） | Cloud（Cirrus 云管） |
|---|---|---|---|
| 面向客户 | SMB | 中大型 / 安全敏感 | 各规模、多分支连锁 |
| License | 免，送 5 个永久 AP License | 永久买断 | 订阅制 |
| 容量红线 | **255 AP/集群**（p46） | 4000 AP / 10 万客户端 | 4000 AP / 10 万客户端 |
| 典型话术 | "我只要简单的 WiFi" | "数据不能出机房" | 40 家门店统一管 |

**决策树与红线**：

1. 客户只要简单 WiFi → Express 零软件成本起步；但记住 255 上限的坑——**第 256 台 AP 静默卡在 joining 状态，不报任何错**（p46），扩容前必须拆 Group 或升级模式。
2. 合规要求本地部署 → OV2500；注意管理面只支持 IPv4（Express 反而支持 v6，ce16），纯 v6 管理的客户别硬应标。
3. 多分支 / 有远程运维诉求 → Cirrus 云管（文理学院案例 c04 就是 BP 用 Cirrus 远程运维）。

**两个工程细节**：Express 集群里，OmniSwitch 每台 ≤32 AP、每堆叠 ≤64 台且至少 2 台可任 PVM/SVM；模式判定开关是 DHCP 有无 Option 138——出厂即 Express，切换模式必须恢复出厂，**集群配置全部丢失、不迁移**（p66），"Easy conversion"话术与这个现实冲突，割接方案要单独报实施工作量。

**排障口诀**（AP 上线但射频全关）：查 License 数量 → 查 Trust 手动确认（批量开局"全部没信号"最常见根因就是没点 Trust）→ 查国家码与 RF Profile 匹配（p68）。

---

## 三、License 三体系通关指南

**铁律：先锁管理模式，再选对应 part number 表——三套语法相近但互不通用，混用会被 eBuy 退回或激活失败**（p126-168）。

| 体系 | 语法规则 | 关键要点 |
|---|---|---|
| OV2500（永久式） | 必选 `OV2500-NG-AP`；选配 Guest / OnBoarding / `OV-NMS-HA` / `OV-AP-WCF`（p131） | 按档位向上取整；Starter Pack 免评估 60 天、附 10 Guest + 10 BYOD；WCF 按 ceil(AP 数/10) 买，零头也要整份 |
| Cirrus 4（旧云订阅） | `OVC-AP-BAS/BIZ/XY` | 每 AP 1 License 附 50 Guest + 50 BYOD；Freemium 免费不限量但**只能看不能改**，别当"免费云管"卖；单订阅 ≤5000 License |
| Cirrus 10（新 SaaS） | **`OVCX-[类别7]-[级别3]-[时长3]`** = 7×3×3 共 63 个 PN（p153） | 类别：APL（低端 AP1x0x/1x1x/1x2x）/APH（如 AP1431）/63/64/65/68/69（交换机型号系）；级别 BAS/BIZ/PRM；时长 1Y/3Y/5Y |

Cirrus 10 拼码示例：客户用 OS6860X24 交换机（→类别 68）、要 TAC 和硬件更换（→BIZ）、签 3 年（→3Y），即 `OVCX-68-BIZ-3Y`。

维保编码逐位拆（p137）：`PW2R-OVBYOD100N` = P(Partner) + W(软件支持) + 2 年 + R(续保) + 产品缩写 + 数量；SP 前缀则是终端客户 Support Plus 含 AVR。

**云订阅激活三步**：eBuy 下单 → Subscription Manager 建订阅拿 Subscription ID + 激活码 → Cirrus 10 License Management 导入并逐台分配。这份流程可直接当实施交接清单。

**防混淆清单**：Base 档不含设备 TAC 与 AVR 硬件服务（Cirrus 4 与 10 皆然），压价时最容易翻车；Cirrus 10 排除 AP1101/AP1201H/L/LH，交换机须 8.9R 版本；维保、Network Advisor 均为目录价，区域折扣另询。

---

## 四、七大行业用例速览表

教材 p169-199，每个案例都是 Identity → Challenges → Why ALE? → Benefits 四段式，可直接改写成投标案例页。

| 案例 | 行业 | 客户画像 | 替换竞品 | 关键收益/弹药 |
|---|---|---|---|---|
| c01 千床医院 | 医疗 | 4 院合并、1000 床、1500 员工（p171） | Aruba | 双认证 PSK/WPA2、UCOPIA 访客画像、医疗专项 POC |
| c02 五星→宫殿酒店 | 酒店 | 802.11ac wave2 改造 | 既有改造 | AP1321/1322/1361、8 SSID、Chromecast 投屏、Ekahau 装后审计 |
| c03 理工大学 4000 人 | 教育 | 600 AP 演进（p180-182） | Cisco | EDUROAM 兼容（802.1X/PEAP）、Chillispot 门户、GRE 访客隧道 |
| c04 文理学院 | 教育 | 混凝土墙+雷暴、400→2000 用户弹性（p184） | Ubiquiti | AP1361 三防、第三方交换机互通、两年零硬件故障 |
| c05 轮渡 20 船×1500 客 | 交通 | 金属船体（p188/p190） | 既有 Wi-Fi | Ekahau 装前审计、客舱 VoD、室外 AP1251 加量 |
| c06 音乐学院 200 用户 | 政府/智慧城市 | UPAM/LDAP、Palo Alto 共存 | — | OPEN 门户 500 会话、100×AP1321 |
| c07 零售 40+ 门店 | 零售 | 150 台 AP、40+ 门店 | 增量 | ESL 电子价签复用 AP USB 口（p197） |

反复出现的赢单三件套：**联合 POC、无控制器 TCO、LAN/WLAN 统一管理**。竞品存量客户的降风险路径见 c12（p117）：Case A 新网对接存量 Aruba ClearPass 认证；Case B 用 OmniVista/UPAM 反向接管存量 Aruba——认证层先行共存，避免一次性割接。

---

## 五、VoWLAN 与场景化容量常数速查

这部分是售前答技术质疑的"可背底牌"。

**语音（VoWLAN，p200-212）**：

- 密度：**1 AP / 255 m²**（p207）；每 AP 承载 **20-25 个语音用户**，提供 36 Mbps 用户吞吐（p208）；
- 漫游：**RSSI ≥ -62dBm** 才能保证正确漫游（p208）；5GHz 优先（更稳、性能更好）；
- 漫游协议：802.11r 适配 Personal + Enterprise，OKC 仅限 WPA2-Enterprise——选错认证方式漫游必卡（ce12）；终端门槛 iOS 8+、三星 S7+，11v 要 S9+（p203）；
- 部署方法论：五步法 Prepare→Plan→Design→Implement→Operate（p206），每步有输出物，可直接当 WBS；
- 话机矩阵：8118/8128/8158s/8168s（Ascom，NOE+SIP）+ Rainbow 软终端。

**数据场景（p236-266）**：

- **酒店客房公式**（p243）：`AP 数 = M/2 + N + (M+N)×5%`，向上取整。M=普通墙房间（隔房装，15dB 衰减）、N=承重墙房间（30dB 衰减，必须一房一台）。例：20 普通 + 10 承重 = 21.5 → 22 台 AP1301H；
- **高密场馆**（p249）：1500 人 × 约 50% 并发 ≈ 750 用户 → **8-10 台**三射频 AP1231/1321；
- **会议室**（p258）：40-60 客户端 1 台、80-120 两台、160-200（报告厅）4 台；
- **户外**：并发按 20% 估，AP1361 约 6-8 台/200 并发，开阔区抱杆装最高点；
- 配置基线的精髓是"同一特性不同场景取值相反"：场馆手动锁信道（ACS 关）、信道带宽 HT20；会议室反而开 HT80；客房关 ATF 是为保护无 AP 房间的体验。

---

## 六、学习路径：8 个 skill 按什么顺序读

1. **ap-selection-matrix** —— 先认硬件：代际×形态×档位三维选型 + 需求五问（p239）；
2. **management-mode-selection** —— 再定玩法：Express/OV2500/Cirrus 三岔口 + 255 红线 + 排障口诀；
3. **license-quotation** —— 然后学报价：三体系 part number + 维保编码 + 激活三步；
4. **rf-scenario-baseline** —— 学算数量：客房公式/场馆/会议室/户外四套估算 + 配置基线；
5. **vowlan-deployment** —— 补语音：255m²、20-25 用户、-62dBm 常数 + 五步法；
6. **special-topologies** —— 补组网：Bridge/Mesh 单判据二分（要不要给终端发 WiFi）、RAP、ESL、Zigbee/RTLS；
7. **industry-use-cases** —— 最后攒弹药：七大案例四段式模板 + 竞品替换双路径；
8. **network-advisor-aiops** —— 加购项：AI 运维三循环（Identify→Mitigate→Optimize）+ 按台年订阅定价（AP $50/年、交换机 $100/年，p231，约占总网成本 1.8%）。

前三个解决"卖什么、怎么管、怎么报"，中间三个解决"怎么算、怎么配、怎么答质疑"，后两个解决"怎么讲赢"。

---

## 七、边界与诚实话术

给读者的三句提醒，也是这套书的坑位图：

1. **三套 License 并存本身就是最大的乱**。OV2500 永久、Cirrus 4 过渡云、Cirrus 10 新 SaaS 同场销售，教材花了 40 多页教"怎么报价不出错"，但 Cirrus 4 存量客户怎么迁到 Cirrus 10，书里没讲清（ce01）——续约场景须单独向 ALE 确认迁移政策，别替厂家承诺。
2. **机型例外清单要背**：Zigbee 不支持 AP1301/AP1230（IoT 项目报入门机型会侵蚀利润）；RAP 不支持 AP1101；AP1101/AP1201/AP1201H 桥接不打 VLAN 标；Cirrus 10 排除 AP1101/AP1201H/L/LH；Mesh 红线 16 台/4 跳/8 从 AP。
3. **教材本身有笔误**：p243 把 AP1301H 误标为 802.11ac（应以 p17 硬件章的 Wi-Fi 6 为准）；p95 出现不存在的"AP1421"（应为 AP1521）；p155 把 Premium 缩写误印为 BAS。另外全部案例只讲赢、无翻车复盘，引用时补自己的风险披露反而更可信；所有美元/欧元价均为目录价。

---

*本文由 cangjie-skill 流水线从 DT00XPS288EN 蒸馏生成。*
