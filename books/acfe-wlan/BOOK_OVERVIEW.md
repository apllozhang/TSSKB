# BOOK_OVERVIEW · ACFE WLAN — Basic Deployment With OmniVista (DT00XTE360EN Edition 04)

> 教材: Alcatel-Lucent Enterprise Training Services, 2025-11 · 585 页 · 参训者指南（ACFE 认证路径售后课）
> 定位: Stellar 无线 + OmniVista Cirrus 云管的**售后实操部署课**（5 天实验室节奏：Day1-Day5 + Lab），从 AP 开箱到 WIPS/勘测全覆盖

## 一、结构（书的骨架）

- **DAY 1** (p3-347)：AP 硬件总览 → 远程实验室连接 → Express 模式发现/开局（PoE/VLAN/DHCP）→ Wi-Fi 网络创建 → **OmniVista Cirrus 入门**（License/订阅、账号组织、站点用户、环境创建与 OmniSwitch Onboarding）→ AP 云 Onboarding（方法/AP Group）→ Employee SSID 创建
- **DAY 2** (p348-…): UPAM Guest 与 BYOD 访问（Guest SSID / BYOD-Employee SSID）→ 无线客户端访问与限制（Unified Policies、Client Accounts）→ **RF 管理**（优化、调优）→ 无线特性（漫游 802.11r/k/v、RAP 远程接入 AP）→ WIPS 无线入侵防护 → Wi-Fi 勘测 → 组织清理
- **附录**：RAP 部署详解

本书每章都配 Lab（远程实验室操作），是"边讲边做"的工程师手册。

## 二、解释（核心论点）

- 这是认证路径（ACFE）的无线部署课，把售前书里的"三种管理模式"落到实操：Express 模式开局（Day1 前半）→ Cirrus 云管全流程（Day1 后半至 Day2）；
- 主线是"**一台 AP 从开箱到上线运营的完整生命周期**"：发现 → 纳管 → Onboarding → SSID（员工/访客/BYOD）→ 策略管控 → RF 优化 → 漫游/远程 → 安全（WIPS）→ 勘测验收；
- UPAM（统一策略与准入）+ Unified Policies 是策略中枢，Guest/BYOD/员工三种身份的差异化处理都收敛到这一套配置模型。

## 三、批判（局限）

- 强依赖远程实验室（Stellar Remote-Lab），无实验环境时 Lab 章节只能读不能练；
- 以 Cirrus 云管为主线，OV2500 本地管的 GUI 操作不在此课；
- 内容与《Stellar WLAN Presales》(DT00XPS288) 有概念重叠，但视角完全不同（怎么做 vs 怎么卖）。

## 四、应用（对售后/交付的价值）

- 新人交付工程师 5 天上手路径；
- 交付 SOP 素材库：开局检查项、Onboarding 步骤、SSID 模板、策略配置、RF 优化流程、WIPS 部署、验收勘测。

## 五、术语速览

Express 模式、Onboarding、AP Group、Employee/Guest/BYOD SSID、UPAM、Unified Policies、RF Management、802.11r/k/v 漫游、RAP、WIPS、Wi-Fi Survey、Cirrus 组织/站点、Remote-Lab
