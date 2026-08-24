---
name: ov2500-49r2-features-compat
description: 何时用：评估 OV 2500 4.9R2 新特性、认证固件矩阵与功能边界，做版本选型或纳管能力核对时。
source_book: OV2500 4.9R2 Release Notes
---

# OV 2500 4.9R2 新特性与兼容矩阵

## R · 原文引用

> "OmniVista 2500 NMS 4.9R2 is installed as a Virtual Appliance, and can be deployed on the following hypervisors: Vmware ESXi 6.5, 6.7. 7.0.2, 8.0; MS Hyper-V: 2012 R2, 2016, 2019, and 2022; MS Hyper-V on Windows 10 Professional; Linux KVM/Ubuntu 22.04" (p5)

> "The following new switch models are now supported: OS6870 ... AOS 8.9R4 MR ... AOS 8.10R2 ... AOS 8.10R3 ... AWOS 5.0.2 – OmniVista 2500 NMS now supports AWOS 5.0.2 on all previously supported Stellar APs." (p6)

> "A new Require Message Authenticator flag is now available to specify whether to check RADIUS packets for the Message-Authenticator attribute ... resolves CVE-2024-3596 (#Blast-RADIUS)" (p8-9)

> "The VM Manager (VMM) application is supported on Hyper-V 2012, 2012 R2, and 2016. VMM is not supported on Hyper-V 2019 or higher ... Dynamic VLAN configuration is not supported on OS2260 and OS2360 switches" (p10-13)

## I · 方法论骨架

评估 4.9R2 是否适合现网，按"平台 → 固件矩阵 → 新特性价值 → 功能边界"四步走：

1. **平台核对**：现有 hypervisor 是否在支持列表（ESXi 6.5-8.0 / Hyper-V 2012R2-2022 / Win10 Pro Hyper-V / KVM Ubuntu 22.04）。OV 只以虚拟设备（VA）形态交付，没有物理机安装。
2. **认证固件矩阵**（p13-14）：OS2260/2360=5.2R5-R7；OS6350/6450=6.7.2.R06-R08；OS6360/6465/6560/6570M/6860E/6860N/6865=8.9R4/8.10R2/8.10R3；OS6870=仅 8.10R2/R3（无 8.9R4）；OS6900-X20/X40/T20/T40/Q32/X72=仅 8.9R4；OS9907/9912=8.9R4/8.10R2/8.10R3。Stellar AP 推荐 AWOS 5.0.2。
3. **新特性清单**：密码有效期策略 + CLI 管理员找回（p7）、SNMPv3 全量加密组合（p7）、Enhanced Open 过渡模式（p7）、6GHz Backward Compatibility（p7-8）、Blast-RADIUS 防护（p8-9）、Oracle Linux 8.10 + 10 项 CVE（p9）。
4. **功能边界**：逐条核对"不支持清单"，再决定方案。

## A1 · 书中案例

- OS6870 新接入但有边界：OV 不能做 CPLD 升级；Application Monitoring 需 AOS 8.10R3+；Application Enforcement 本版不支持 (p03)。
- Blast-RADIUS 三场景：UPAM 做 RADIUS 服务器时 OmniSwitch 默认不带 Message-Authenticator，须在交换机执行 `aaa radius message-authenticator`（AOS 8.10R2+）(p09)。
- PALM 下线：依赖 PALM 的流程迁移到 Fleet Supervision（myfleet.ovcirrus.com）(p04)。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：版本选型、升级前能力评估、"4.9R2 支不支持某机型/功能"、安全合规清单（CVE）核对。
- 区分：只关心升级步骤与顺序 → 用 `ov2500-upgrade-deploy`；遇到具体故障现象排障 → 用 `ov2500-known-issues`；升级高危风险评审 → 用 `ov2500-danger-traps`。

## E · 可执行步骤

1. 列出现网 hypervisor，对照 p5 支持列表；不在列表内则 4.9R2 无法部署。
2. 导出现网设备型号 × 固件版本表，对照 p13-14 认证矩阵，标出"不认证"组合。
3. 核对新特性依赖：Enhanced Open 需 AP AWOS 4.0.8+；Blast-RADIUS CLI 命令需交换机 AOS 8.10R2+；Message-Authenticator 响应校验需 AWOS 5.0.2+。
4. 过功能边界清单：VMM 仅 Hyper-V 2012/2012R2/2016 英文版、无 VLAN 配置；OS2260/2360 无动态 VLAN；IoT Enforcement 仅 OS6560-P48Z16 部件号 904044-90；WCF/DPI 的 AP 排除表（AP1101/AP1201H/L/HL、AP15XX；AP132x/136x 签名包 ≥3.6.11，AP1301/H/1311 ≥3.8.3）。
5. 第三方纳管：Cisco/Extreme 需在 Discovery 手工提供 OID 映射 mib-2；CLI Scripting 不能下发到 Stellar AP/第三方设备。

## B · 边界与陷阱

- 6GHz SSID 开 Backward Compatibility 后与 MLO 互斥：MLO Band 含 6GHz 时该选项自动禁用 (p08)。
- 密码有效期策略对新用户立即生效，老用户要等下次改密 (p05)；升级后强口令会被自动开启（见 danger-traps，ce67）。
- OS6870 认证矩阵与其他 8.x 机型不同：没有 8.9R4 档位。
- 浏览器仅 Chrome/Firefox/Edge；IE 已弃用 (p18)。

---
来源条目: p01, p02, p03, p04, p05, p06, p07, p08, p09, p10, p18, p20, ce64, ce70, ce71, ce72, ce73, g01, g02, g03, g04, g05, g09, g10, g11, g12
