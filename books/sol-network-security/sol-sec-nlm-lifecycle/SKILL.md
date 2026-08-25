---
name: NLM 网络生命周期管理（视频监控网络 7 阶段/Five S's/Lightning Config/冗余升级/退役擦除）
description: 需要规划或运营视频监控等关键业务网络的全程生命周期时使用：7 阶段 NLM 框架（规划-部署-运营-维护-升级-合规-退役）、Five S's 规划要素、UNP/Lightning Config 快速部署、Milestone VMS 与 Network Advisor 监控、冗余零停机升级、wIPS 与无线安全配套、退役数据擦除。
source_book: Maximizing Security and Performance Whitepaper
---

## R（触发场景）
- 规划视频监控/IP 视频网络（Five S's 五要素拆解）
- 部署阶段提速：UNP、Lightning Config、边缘认证上线
- 运营监控：Milestone VMS 插件、API 集成、Network Advisor AI 告警
- 零停机固件升级与容量规划
- 合规（网络保险）与设备退役数据擦除
- 无线侧配套：wIPS rogue 治理、WPA3/OWE、客户端隔离

## I（核心理念）
"装完就不管"不成立（P86/X25，<<<PAGE 95>>>）：视频监控网络需要系统化生命周期管理以适应技术、运营与安全需求的演进（P81，<<<PAGE 89>>>）。物理安全依赖网络安全（P88，<<<PAGE 99>>>）：看门的摄像头被远程禁用即物理失守。设计期即面向未来（P82，<<<PAGE 91>>>）：生命周期思维要在设计阶段进入；冗余设计支撑零停机升级（P87，<<<PAGE 96>>>）。无线侧 wIPS 持续运营是 rogue 防治关键（P68，<<<PAGE 63>>>）。

## A1（行动框架）
视频监控网络生命周期 7 阶段框架（F4，<<<PAGE 89>>>）：
1. 规划与设计：Five S's = Software / Surveillance IoT / Servers-Storage / Switches / Services-Support
2. 部署：UNP、Lightning Config、边缘认证上线
3. 运营管理：持续监控、API/VMS 集成、主动补丁
4. 故障维护：固件升级、冗余切换、软件工具包
5. 升级优化：AI、Network Advisor、分阶段换新
6. 合规与文档：安全审计、网络保险、文档留存
7. 退役与重部署：数据安全迁移、按隐私法擦除处置

## A2（操作步骤）
- **规划**：按 Five S's 拆解（<<<PAGE 90>>>）；容量规划不足会导致减速、丢数据、昂贵返工（X26/P83，<<<PAGE 91>>>）；入门级交换机跑不动 AI 系统，边缘设备纳入生命周期管理（P83/P84，<<<PAGE 91-92>>>）
- **部署**：Lightning Config 让受训 50 分钟的技术员 5 分钟装好设备（C18，<<<PAGE 93>>>）；UNP 按用户/设备/应用动态下发网络行为（<<<PAGE 93>>>）
- **运营**：交换机信息经 Milestone XProtect VMS 插件可视化（C20，<<<PAGE 95>>>）；PoE 向导一键诊断每台 PD（C19，<<<PAGE 97>>>）；Z-Score 以 30 天小时级端口利用率为基线标记异常（C15，<<<PAGE 78>>>）；Quarantine Manager 联动 Fortinet 等 IPS 在接入交换机/AP 级隔离可疑终端、阻断横向移动（C16/P79，<<<PAGE 83-84>>>）
- **维护/升级**：冗余系统承载业务时另一侧升固件，零停机（P87，<<<PAGE 96>>>）；Network Advisor AI 实时监控与修复（<<<PAGE 98>>>）
- **无线配套**：wIPS 三类 AP（interfering 非直接威胁/rogue 接有线即威胁/friendly 允许）+ Containment 发 DEAUTH 驱离 + allow/blocklist + Dynamic blocklist（C14，<<<PAGE 63-66>>>）；WPA3/SAE 优先（WPA2-PSK 可被离线字典攻击，X17/P69）、开放 SSID 启用 OWE（X19/P70）、访客客户端隔离（P71）、漫游上下文 DTLS 加密（P72）；WPA3_AES256 对不支持 AP 自动回退 WPA2_AES、漫游域默认空口令须改（X20/X21，<<<PAGE 68-70>>>）
- **合规与退役**：过网络安全标准以满足网络保险（P89，<<<PAGE 99>>>）；含敏感信息的设备按数据隐私法擦除处置（P90，<<<PAGE 99>>>）

## E（实证案例）
- Lightning Config 五分钟部署（C18，<<<PAGE 93>>>）
- PoE 向导一键诊断（C19，<<<PAGE 97>>>）
- Milestone VMS 插件打通视频与网络监控（C20，<<<PAGE 95>>>）
- wIPS rogue AP 治理组合拳（allowlist/blocklist/Suppress DEAUTH/Dynamic blocklist）（C14，<<<PAGE 63-64>>>）
- Z-Score 端口利用率异常检测（C15，<<<PAGE 78>>>）
- Quarantine Manager 与 IPS 联动隔离（C16，<<<PAGE 83-84>>>）
- Stellar AP 作为 802.1X 客户端五种上线场景（C17，<<<PAGE 61-62>>>）

## B（反例与坑）
- "装完就不管"心态不适用于视频网络（X25/P86，<<<PAGE 95>>>）
- 容量规划不足导致减速、丢数据、昂贵改造（X26，<<<PAGE 91>>>）
- 贪便宜设备导致反复 truck rolls，长期成本反升（X27/P92，<<<PAGE 100>>>）
- Air Gap 空气隔离在联网化的 IP 视频网络已不现实（P85，<<<PAGE 93>>>）
- 干扰 AP 与 rogue AP 混淆误报：interfering 未接有线不算直接威胁（X16，<<<PAGE 63>>>）
- WPA2/PSK 可被离线字典攻击；PMF 可选时代未开启则受去认证攻击（X17/X18，<<<PAGE 68>>>）
- 客户端隔离不跨 AP 生效，跨 AP 隔离需 SSID 级 ACL（X22，<<<PAGE 70>>>）
- 过度工程可作未来预留，但须与成本权衡（P91，<<<PAGE 100>>>）

来源：Maximizing Security and Performance Whitepaper（p87-100）+ Network Security Guidelines 无线章（p47-70）
