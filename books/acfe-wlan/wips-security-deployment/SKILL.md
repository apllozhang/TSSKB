---
name: wips-security-deployment
description: 何时用：部署/调参 WIPS——外部 AP 三分类、Rogue 策略四条件、遏制杀伤半径控制、攻击检测与客户端黑名单。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# WIPS 无线入侵防护部署

## R · 原文引用

> "Interfering AP: Any other APs discovered over the air ... APs managed by the same OVC 10 are excluded. Rogue AP: Based on the Rogue AP Policy ... Rogue AP Containment – enabled by default. The scanning Stellar AP sends de-auth request to all clients associated to the rogue AP. Friendly AP ... can be set as Friendly AP manually" (p514)

> "Signal Strength Threshold: Default –70 dbm; Range -50 to -90 dbm. Detect Valid SSID: The detected foreign AP is broadcasting a SSID that is configured in OmniVista Cirrus ... Detect Rogue SSID Keyword ... Rogue OUI" (p515)

> "Do not modify the parameters, unless instructed to. Actions applied to Rogue AP can have big consequences to other wireless networks. ... your Stellar Access Point sends a de-authentication packet to the Wi-Fi clients associated to rogue Access Points." (p523)

## I · 方法论骨架

**1. 三分类框架**

| 类 | 来源 | 处置 |
|---|---|---|
| Interfering | 空口发现的默认分类（本 OVC 管理的除外） | 仅记录 |
| Rogue | 命中 Rogue AP Policy 任一条件 | Containment：扫描 AP 向其客户端发 de-auth（默认开） |
| Friendly | 人工添加 | 永不判 Rogue；Friendly OUI 默认含 ALE OUI，可追加 |

**2. Rogue 判定四条件**
1. Signal Strength Threshold：信号强于阈值（默认 -70dBm，范围 -50~-90；实验界面默认 Disabled）
2. Detect Valid SSID：广播了我方 Cirrus 里配置的合法 SSID（默认启用）
3. Detect Rogue SSID Keyword：SSID 名含黑名单关键词
4. Rogue OUI：MAC OUI 匹配

**3. 攻击检测与黑名单**
- 无线攻击检测默认开启，分 AP 攻击/客户端攻击，级别 Custom/High/Medium/Low
- Client Blocklist Policy 默认禁用；开启后触发条件 60 秒内认证失败 10 次拉黑，老化 1 天
- 局限：攻击源 MAC 可能是 AP/BSSID/伪造网卡 MAC，只有真实无线客户端 MAC 拉黑才有意义

**4. 前提与副作用**
- WIPS 全局作用于 OV 管理的全部 AP，且依赖背景扫描开启（见 rf-optimization-baseline 的扫描/性能权衡）
- 每 AP 每 SSID 双频各一个 BSSID：干扰列表中同一 AP 会出现多条，加 Friendly 时按 OUI 全选

## A1 · 书中案例（Lab 步骤精要）
- **c19/p521-525**：策略总览（四条件默认值核对）→ Interfering AP 标签搜相邻学员 SSID "EmployeesX"，按 OUI dc:08:56 勾选全部条目 → Action > Add to Friendly → 勾 Detect Rogue SSID Keyword 填 EmployeesX 验证：这些 AP 仍不进 Rogue 标签、客户端连接正常、WIPS Analytics 无 Rogue Detected/DeAuth 记录——证明 Friendly 一票豁免。

## A2 · 触发场景（含与相邻 skill 的区分）
- 客户要求无线入侵检测、发现陌生 AP 要分类处置、或已发生 rogue/攻击事件要做遏制时用。
- **区分**：UNP/认证层面的仿冒 AP 准入盲区 → `device-cloud-onboarding`（B 节）与 `ssid-authentication-suite`；本 skill 管"空口侧的检测与反制"。扫描参数的性能代价 → `rf-optimization-baseline`。

## E · 可执行步骤
1. 确认背景扫描开启（WIPS 必要条件）。
2. 保持默认策略起步：Detect Valid SSID=Enabled、阈值条件 Disabled、Containment=Enabled。
3. 盘点周边合法外部 AP（邻居公司、其他 POD），逐批加 Friendly（按 OUI 全选双频 BSSID）。
4. 需要收紧时逐条加条件（关键字/OUI/阈值），每次评估反制半径后再应用。
5. 开启攻击检测分级（按环境选 High/Medium/Low）；Blocklist 按需开并知晓触发常数（10 次/60s、老化 1 天）。
6. 监控：Network > Analytics > WIPS Analytics（Access Points / Clients 两标签）。

## B · 边界与陷阱
- Rogue 反制杀伤半径大：de-auth 会波及邻居网络，参数过宽=持续攻击合法 AP，引发投诉甚至法律风险；教材明令"未经指示不要改参数"（ce32）。
- Friendly 一票豁免绝对有效——连 Rogue 关键字命中都不判；名单要定期复核（ce32 验证）。
- 黑名单拉的是源 MAC，未必是真实客户端，不是万能措施（ce33）。
- 同一 AP 多 BSSID 重复条目，加 Friendly 漏勾某个 BSSID 仍会被判 Rogue。
- 关掉背景扫描=WIPS 失明；扫描调优去 RF skill。

---
来源条目: f19, p61, p62, p63, c19, ce32, ce33 · 术语锚点: g55, g46, g24, g27
