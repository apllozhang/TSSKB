---
name: Stellar AP Onboarding
description: 当需要把 Stellar AP 宣告（declare）进 Cirrus/Terra、排查激活失败状态、或从 OVC4/Cirrus 迁移设备到新平台时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 新购 Stellar AP 需要批量宣告进平台并确认到达 OV Managed 状态
- AP 激活卡在中间状态或报错，需要排查
- 从 OmniVista Cirrus 4 迁移到 OVC，或从 Cirrus 切到 Terra

## I（核心理念）
AP Onboarding 的本质是"宣告 + 激活状态机"：Device Catalog 跟踪设备从 Registered 一路到 OV Managed 终态（正常链最长 5 分钟）。激活的核心原理是平台为设备签发数字证书并建立安全 VPN 通道，因此曾归属其他平台的残留证书是激活失败的头号根源。

## A1（行动框架）
1. **Terra 前置三步**（Cirrus 不需要）（<<<PAGE 141>>>）：
   - 曾由 Cirrus 管理的 AP 删证书：`> rm -rf /.ocloud/callhome_hash.json /.ocloud/certificateFile.cert /.ocloud/cloudCaChain.pem /.ocloud/privateKey.key /.ocloud/csr.csr /.ocloud/publicKey.key ./privateKey.key.dec`
   - DHCP option 43 指向 activation.myovterra.com，并重启 DHCP 服务
   - AP 上执行 `firstboot` + `reboot`
2. **宣告设备**：单台宣告，或用 XLSX/CSV 模板批量宣告（"Import and declare multiple Stellar Access Points in a single file"，<<<PAGE 142>>><<<PAGE 143>>><<<PAGE 144>>>）。
3. **跟踪激活状态**：Device Catalog 看 Activation Status，正常链最长 5 分钟；排障看 Activation Log；AP CLI 用 `> ocloud_show`（<<<PAGE 146>>><<<PAGE 148>>><<<PAGE 150>>>）。
4. **确认终态**：OV Managed = Device is ready for full management（<<<PAGE 147>>>）。

## A2（进阶应用）
- **激活状态机**（排障地图）：Registered → Obtaining Certificate → Upgrade/Upgrading → Assigned → VPN Configuring → Connected to OV → OV Managed（<<<PAGE 146>>><<<PAGE 147>>><<<PAGE 166>>><<<PAGE 167>>>）。
- **OVC4 → OVC 迁移**：先在新平台手工重建 AP Group/Provisioning/SSID/Access Policy 并与 OVC4 核对配置 → 从 OVC4 Device Catalog 删除所有设备 → 新平台添加并等 Call Home（AP 最长 30 分钟，或重启设备加速）（<<<PAGE 69>>><<<PAGE 70>>>）。
- AP CLI 查看云代理状态：`ocloud_show`（<<<PAGE 150>>>）。

## E（实证案例）
- **案例 1**：二手/退库 AP 接入 Terra 后激活反复失败——AP 曾被 Cirrus 管理，/.ocloud/ 下残留云证书导致激活异常；删证书 + DHCP option 43 + firstboot/reboot 三步后恢复（<<<PAGE 141>>>）。
- **案例 2**：OVC4 直接 onboard 到 OVC 冲突——设备序列号不能同时存在于两个平台，必须先在 OVC4 删除全部设备（<<<PAGE 70>>>）。

## B（边界与陷阱）
- **序列号唯一性**：同一设备不能同时声明在 OVC4 和 OVC，旧平台必须先删（<<<PAGE 70>>>）。
- **OVC4→OVC 无自动迁移工具**：AP Group/Provisioning/SSID/Access Policy 全部手工重建核对（<<<PAGE 69>>>）。
- **激活失败状态族**：Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required；其中 "Provisioning Failed" = 设备无法处理供给配置或平台无法发现设备；"Unsupported Device Model" = 平台不支持该设备（<<<PAGE 146>>><<<PAGE 147>>>）。
- **VPN profile 变更必恢复出厂**："Factory Reset required: The VPN profile was changed/updated."（<<<PAGE 147>>>）。
- **不支持型号**：AP1101、AP1201L/H/HL（<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>）。

## 来源
- frameworks·Stellar AP Onboarding 流程（<<<PAGE 141>>><<<PAGE 142>>><<<PAGE 143>>><<<PAGE 144>>>）
- frameworks·OVC4 → OV Cirrus 迁移流程（<<<PAGE 69>>><<<PAGE 70>>>）
- principles·Device Catalog 激活状态机（<<<PAGE 146>>><<<PAGE 147>>><<<PAGE 166>>><<<PAGE 167>>>）
- principles·激活失败状态集合（<<<PAGE 146>>><<<PAGE 147>>>）
- principles·证书与 VPN 通道的激活原理（<<<PAGE 147>>>）
- cases·Stellar AP 单台/批量宣告（<<<PAGE 142>>><<<PAGE 143>>><<<PAGE 144>>>）
- cases·AP 查看激活状态与日志（含 AP CLI）（<<<PAGE 146>>><<<PAGE 148>>><<<PAGE 150>>>）
- counter-examples·曾被 Cirrus 管理的 AP 接入 Terra 前必须清除证书（<<<PAGE 141>>>）
- counter-examples·设备序列号不能同时存在于 OVC4 与 OVC（<<<PAGE 70>>>）
- counter-examples·OVC4→OVC 无自动迁移工具（<<<PAGE 69>>>）
- counter-examples·激活失败状态族与排查入口（<<<PAGE 146>>><<<PAGE 147>>>）
- counter-examples·VPN profile 变更后设备需恢复出厂（<<<PAGE 147>>>）
- counter-examples·不支持的 AP 型号（<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>）
