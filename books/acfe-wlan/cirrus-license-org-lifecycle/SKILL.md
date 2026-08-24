---
name: cirrus-license-org-lifecycle
description: 何时用：开通 OmniVista Cirrus 云管——eBuy 下单/订阅导入、账号组织规划、OVC4 迁移，以及组织清理与级联删除防护。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# Cirrus 云管账号组织与 License 生命周期（含清理回退）

## R · 原文引用

> "Subscription manager: Create the subscription; Lifecycle operations: Renewal, Add-on, Extension, Transfer, ... OmniVista CIRRUS: Import of licenses (Order ID, Activation code). Alcatel-Lucent Enterprise eBuy: License ordering" (p173)

> "Note: The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager." (p175)

> "In OVC 10.4.3, a unique account (linked to a mail address) can only be assigned to one MSP portal. If a user want access to multiple MSP portals, he must use different mail addresses: Or using the sub-addressing method for his email" (p198)

> "As OmniVista Cirrus is cloud-based, it is not possible to revert the configuration back to the default parameters with one click." (p544)

## I · 方法论骨架

**1. License 生命周期（横跨三系统）**
```
eBuy 下单（品号 OVCX-系列-级别-年限-类别）
  → Subscription Manager 建订阅（记 Subscription ID + Activation Code）  [最长延迟 24h]
  → Cirrus 组织内 License Management > Import Licenses（选 CAPEX，填 ID+激活码）
  → 指派设备（自动/手工）→ 确认升级付费模式 → 核验模式/时长/数量
```
品号编码：级别 BAS/BIZ/PRM；年限 1Y/3Y/5Y；类别 APL（低端 AP1x0x/1x1x/1x2x）/APH（其余 AP）/63/64/65/68/69/99（OmniSwitch 系列）。

**2. 账号与组织层级**
- 层级：MSP 门户 > Organization > Site > Building > Floor
- 账号分 Customer/Partner；MSP 级权限 Admin/Viewer/Limited
- 一邮箱（=一账号）只能绑一个 MSP 门户；多 MSP 用子地址 MyMail+tag@company.com 派生（激活邮件仍发原地址）
- 区域入口：https://eu.manage.ovcirrus.com / https://us.manage.ovcirrus.com；密码 14-100 位含大小写+数字+特殊字符、不得含邮箱串
- 组织可在 MSP 间迁移（Change MSP）或脱离（Disassociate——脱离后该 MSP 全部用户立即失访）

**3. 网络前提（云开通前核查）**
- 防火墙入向：9093 / 30123 / 30124 / 30125；出向放行 443 / 80 / 123 / 53
- DHCP 标准选项 1,3,6,28,42,43（代理场景加 129-133、138）
- 至少 1 台 NTP；AP 固件 AWOS 4.0.6 GA+，AP1101/AP1201L/H/HL 不支持；交换机 AOS 8.9R1+（release 5 不支持）

**4. OVC4 → OVC 迁移**
1. 在新 OVC 手工重建 AP Group/SSID/策略并比对
2. OVC4 Device Catalog 删除全部设备（序列号禁止双登记）
3. 新 OVC 重新声明（手工或 XLSX/CSV 模板）
4. 等下次 Call Home：AP 最长 30 分钟（或重启 AP）；交换机重启 cloud-agent

**5. 组织清理（无一键恢复，按依赖逆序拆）**
任务/备份 → WIPS 复位 → AP 摘回 default device group → AP Group 换回默认 Provisioning 后删组 → 删 Provisioning（RF Profile 先改回 Default）→ 删 RF Profile → SSID → 统一策略/服务端口/BYOD/Guest 策略/门户模板/ARP/账号/报表 → 站点（级联删楼宇楼层与设备归属）→ 确认 Device Catalog 为空。

## A1 · 书中案例（Lab 步骤精要）
- **c09/p169-238**：eBuy 下单 OVCX-68-BAS-3Y → MyPortal > Subscription Manager 建 CAPEX 订阅 → eu.manage.ovcirrus.com 注册（子地址技巧）→ Create Organization + Request trial period（ALE 联系人/是否 RAP/Partner CRD ID）→ Import Licenses（Subscription ID + Activation Code）→ 选设备分配 → Upgrade → 验证许可模式/时长/数量。
- **c20/p542-547**：25 步组织清理全清单，即上文逆序拆除 SOP 的完整实操版。

## A2 · 触发场景（含与相邻 skill 的区分）
- 新客户开通 Cirrus、下单导入订阅、规划多 MSP/多组织账号结构时用。
- 换设备/搬场/重配网络需要"清空重来"、或从 OVC4 迁移时用。
- **区分**：账号许可就绪后要把交换机/AP 真正上云 → `device-cloud-onboarding`；本 skill 管的是"平台侧的商业与组织生命周期"，不碰设备激活。

## E · 可执行步骤
1. 至少提前一天在 eBuy 下单（24h 延迟红线），核对品号级别/年限/类别。
2. Subscription Manager 建订阅，记录 Subscription ID 与 Activation Code。
3. 网络侧按前提清单开防火墙端口、NTP、DHCP options，盘点设备型号/版本。
4. Cirrus 建组织（试用地填 ALE 联系人）→ 导入许可 → 指派设备 → 核验。
5. 多 MSP 工程师账号用子地址派生注册。
6. 清理/迁移时严格按依赖逆序执行；删除类操作前确认客户自有管理员可登录、Site 下设备已迁走。

## B · 边界与陷阱
- **24h 延迟**：交付当天下单会卡现场（ce06）。
- 序列号禁止 OVC4/OVC 双登记，旧云不删新云注册不上（ce05）。
- Disassociate 全员失访；Delete Organization 丢整个管理面，教材明令禁止在培训组织上执行（ce08）。
- 删 Site 是级联操作：楼宇楼层与设备归属连带删除，设备纳管关系丢失（ce36）。
- 云上无一键恢复，删除顺序错了会报错；搭建环境时就记录创建对象清单，拆除逆序执行（ce35）。
- 前提清单任一缺失都表现为"Call Home 失败/不上线"，型号/版本/防火墙/NTP 任一不行都卡（ce04）。

---
来源条目: f25, f26, p22, p23, p24, p25, p26, c09, c20, ce04, ce05, ce06, ce07, ce08, ce35, ce36 · 术语锚点: g30, g33, g35, g48
