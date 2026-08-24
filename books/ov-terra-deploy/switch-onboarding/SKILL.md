---
name: OmniSwitch Onboarding
description: 当需要把 OmniSwitch 交换机接入 Cirrus/Terra（含从 Cirrus 切换到 Terra 的证书清理与激活 URL 修改）、用 cloud-agent CLI 排查时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- OmniSwitch 需要宣告进平台并确认 DeviceManaged 状态
- 交换机从 Cirrus 平台切换到 Terra
- 交换机 VPN 通道异常需要重建，或需要调整发现间隔

## I（核心理念）
交换机通过内置的 cloud-agent 进程与平台对接：宣告后经 Activation Server 获取证书、建 VPN 通道，最终 Device State = DeviceManaged。发现机制默认 30 分钟一次（Call Home），重激活的本质是重启 cloud-agent 进程或重启设备。切换平台时必须删旧证书并改 cloudagent.cfg 中的激活 URL。

## A1（行动框架）
1. **Terra 前置两步**（<<<PAGE 161>>>）：
   - 删证书：`cd switch/cloud` → `rm -f client.crt cloudCAchain.pem csr.crt private.key public.key`
   - 编辑 /working/cloudagent.cfg，修改首行 "Activation Server URL: activation.myovterra.com"
   （注：同一套流程适用于 Cirrus 与 Terra 两个平台的 OmniSwitch onboarding，<<<PAGE 164>>>）
2. **宣告设备**：单台宣告，或用 XLSX/CSV 模板批量（<<<PAGE 164>>>）。
3. **状态与排障 CLI**（<<<PAGE 171>>><<<PAGE 172>>>）：
   - `cloud-agent admin-state enable/disable`（默认 enable）
   - `cloud-agent admin-state disable force` —— 重建 VPN
   - `cloud-agent discovery-interval`（默认 30 分钟）
   - `show cloud-agent status`：看 Activation Server State（期望 completeOK）、Device State（期望 DeviceManaged）
   - `show cloud-agent vpn status`：示例输出 Activation Server: activation.ovng.myovcloud.com:443、VPN Server: vpnb.ovng.myovcloud.com:443
4. **重激活**：重启 cloud-agent 进程，或手动重启设备（<<<PAGE 170>>>）。

## A2（进阶应用）
- 迁移等不及 30 分钟 Call Home 周期时，重启设备或 cloud-agent 立即触发（<<<PAGE 69>>>）。
- 激活失败状态族（与 AP 共用）：Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required（<<<PAGE 146>>><<<PAGE 147>>>）。

## E（实证案例）
- **案例 1**：客户从 Cirrus 整体切换 Terra，交换机 onboard 后无反应——cloudagent.cfg 首行仍是旧 Activation Server URL，且 switch/cloud 下残留旧证书；删证书 + 改 URL 后恢复（<<<PAGE 161>>>）。
- **案例 2**：`show cloud-agent status` 显示 VPN 异常，执行 `cloud-agent admin-state disable force` 强制重建 VPN 后恢复（<<<PAGE 171>>>）。

## B（边界与陷阱）
- **切平台必清证书 + 必改 URL**：只做其中一步都不够，残留证书或旧激活 URL 都会导致激活异常（<<<PAGE 161>>>）。
- **发现周期错觉**：默认 30 分钟 Call Home，"宣告后没动静"可能只是在等周期，可重启进程加速（<<<PAGE 171>>><<<PAGE 69>>>）。
- **VPN profile 变更需恢复出厂**（<<<PAGE 147>>>）。

## 来源
- frameworks·OmniSwitch Onboarding 流程（<<<PAGE 161>>><<<PAGE 162>>><<<PAGE 163>>><<<PAGE 164>>>）
- principles·交换机激活 cloud-agent 机制（<<<PAGE 170>>><<<PAGE 171>>><<<PAGE 172>>>）
- cases·交换机 cloud-agent CLI 操作集（<<<PAGE 171>>><<<PAGE 172>>>）
- cases·交换机重激活操作（<<<PAGE 170>>>）
- counter-examples·交换机切 Terra 需改 cloudagent.cfg 激活 URL 并删证书（<<<PAGE 161>>>）
- counter-examples·激活失败状态族与排查入口（<<<PAGE 146>>><<<PAGE 147>>>）
- counter-examples·VPN profile 变更后设备需恢复出厂（<<<PAGE 147>>>）
