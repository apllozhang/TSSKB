---
name: AOS 8.10R4 Secure Boot、ALE CA 证书与包管理
description: 需要在 OmniSwitch AOS 8 上启用 Secure Boot、了解各平台 U-Boot/ONIE/BIOS 升级次序、管理 ALE CA 设备证书与弱加密禁用、用 pkgmgr 安装卸载软件包时使用。
source_book: OmniSwitch AOS Release 8.10R4 Release Notes
---

## R（触发场景）
- 安全基线要求交换机只运行可信软件，要规划 Secure Boot 启用
- 升级到 8.10R4 时被 U-Boot/BIOS 版本卡住，或 Secure Boot 镜像装完重启回落 Certified
- 混合 VC 里部分平台不支持 Secure Boot，要选镜像
- 管理设备 X.509 证书（ALE CA）、禁用弱加密、适配首访强制改密
- 用 pkgmgr 安装/卸载功能包，或升级前处理 AMS 明文密码

## I（核心理念）
Secure Boot 通过启动期认证校验保证只运行可信软件，需 U-Boot/ONIE/BIOS 升级 + Secure Boot 专用镜像三件配合（P1，<<<PAGE 34>>>）。平台分型框架（F3，<<<PAGE 104-105>>>）：U-Boot 型（6360/6465/6560/6570M——先升 U-Boot 再升镜像，之后只认 Secure Boot 镜像）／ONIE 型（6860N/6870/6900-X 系列——BIOS 使能+ONIE 包）／例外型（6860(E)/6865/9900/6900-V72·C32·V48C8·C32E 不支持或需 BIOS）；混 VC 用"最小公分母"（非 Secure Boot 镜像）。证书与密码治理是配套安全层：ALE CA 设备证书（每台唯一密钥对+内部 CA 签 X.509，5 年有效、到期前 1 年更新，P5，<<<PAGE 27>>>）、首访强制改密（P3，<<<PAGE 27>>>）、su 口令不可恢复（P4，<<<PAGE 26>>>）、弱加密禁用（P6，<<<PAGE 28>>>）、TLS 默认 1.2（P8，<<<PAGE 33>>>）。

## A1（决策框架）
1. **先查平台属于哪一型**：U-Boot 型先 `update uboot` 到 8.10.37.R04 再升 Secure Boot 镜像；ONIE 型升镜像→重启进 BIOS 启用→（6860N/6870）装 onie deb 包；例外型用非 Secure Boot 镜像
2. **混 VC 判定**：含 6900-V72/C32/V48C8/C32E 的混合 VC 全网必须用非 Secure Boot 镜像（X3，<<<PAGE 104>>>）
3. **证书策略**：默认走 ALE CA（升级自动获得）；已装自定义 CA 证书的升级后继续沿用不替换（P5）
4. **包管理纪律**：pkgmgr install 后必须 `write memory` commit，否则 reload 时镜像校验失败（X16，<<<PAGE 101>>>）

## A2（操作步骤）
- **U-Boot 平台启用（6360/6465/6560/6570M）**：先 `update uboot` 到 8.10.37.R04 → 再用 Secure Boot 镜像升 AOS（C9，<<<PAGE 105>>>）
- **ONIE 平台启用（6860N/6870/6900-X48C6 等）**：Secure Boot 镜像升 AOS → 重启进 BIOS 启用 Secure Boot →（仅 6860N/6870）`pkgmgr install uosn-onie-v1.deb` + `write memory flash-synchro` 升 ONIE/Diag（C10，<<<PAGE 105>>>）
- **6900-V48C8/C32E**：先升 BIOS（C32E v40.01.01.03 / V48C8 v40.01.01.04，联系 Support）→ 再升 Secure Boot 镜像 → 重启进 BIOS 启用（C11，<<<PAGE 105>>>）
- **包安装/卸载**：`pkgmgr verify nos-mrp-v1.deb`（MD5）→ `pkgmgr install nos-mrp-v1.deb` → `write memory` → `show pkgmgr`（+ 未保存、* 待 reload）；卸载 `pkgmgr remove mrp` → `write memory` → `rm /flash/working/pkg/nos-mrp-v#.deb`（C12，<<<PAGE 101-102>>>）
- **弱加密禁用与查看**：`system security crypto-strong-security enable` + `show system security`；弱密钥探测 `ssh strong-hmacs enable`（C16，<<<PAGE 28>>>/<<<PAGE 16>>>）
- **升级前 AMS/IoT-Profiler 密码加密化**：升 8.7R1+ 前删 `/flash/<running>/pkg/ams/ams-broker.cfg`（每台 VC 成员）→ 升级 → 重配 broker；AMS-APPS 同理删 `pkg/ams-apps/install.sh`（C13，<<<PAGE 102>>>）

## E（实证案例）
- 三类平台 Secure Boot 启用路径（C9/C10/C11，<<<PAGE 105>>>）
- pkgmgr 包生命周期管理（C12，<<<PAGE 101-102>>>）
- 升级前 AMS 明文密码治理（C13，<<<PAGE 102>>>）

## B（反例/坑）
- 次序颠倒装了 Secure Boot 镜像会重启回落 Certified 镜像：6360/6465/6560/6570M 必须 U-Boot ≥8.10.37.R04 才能升 8.10R4（X1/P2，<<<PAGE 18>>>/<<<PAGE 104>>>）
- 6570M 出厂 U-Boot 8.10.42.R02 只认签名镜像（8.9R4+），降级到更早 AOS 必须先降 U-Boot 到 <8.9.70.R04（X7，<<<PAGE 18>>>）
- Secure Boot 不支持平台清单：6860(E)、6865、6900-V72/C32/V48C8/C32E（无 BIOS 升级时）、9900（X4，<<<PAGE 104>>>）
- 8.10R4 首访强制改密会打断自动化：admin 默认口令的 REST API/脚本必须改（X8/P3，<<<PAGE 18>>>/<<<PAGE 27>>>）
- 8.7R2 起新用户口令策略默认收紧（禁含用户名、大写/小写/数字/非字母各≥1），存量用户不受影响（X9，<<<PAGE 17>>>）
- 包未 commit 引发镜像校验错误：pkgmgr install 后必须 write memory（X16，<<<PAGE 101>>>）
- 升级前未删 ams-broker.cfg / install.sh 则密码不会转加密（X17，<<<PAGE 102>>>）
- ssh-rsa（SHA-1）默认禁用，替代 rsa-sha2-256/512 与 ecdsa（P7，<<<PAGE 16>>>）
- PKI 私钥与 installsshkey 曾不随 VC 主备同步（8.10R4 修复，复制到 /flash/switch/.profiles 并全机箱应用）（X35，<<<PAGE 87>>>）

## 来源
OmniSwitch AOS Release 8.10R4 Release Notes Appendix L（<<<PAGE 104-105>>>）、Prerequisites（<<<PAGE 15-18>>>）、New Features 安全类（<<<PAGE 26-34>>>）、Appendix J（<<<PAGE 101-102>>>）。条目来源：cases C9-C13/C16；principles P1-P9/P5；counter-examples X1/X3/X4/X7/X8/X9/X16/X17/X35；frameworks F3。
