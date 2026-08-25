---
name: AOS 8.10R4 升级方法论与固件三件套（标准升级/ISSU/FPGA·U-Boot·ONIE）
description: 需要在 OmniSwitch AOS 8 上规划版本升级、执行标准升级或 ISSU、核对 U-Boot/FPGA/CPLD/ONIE 最低版本、做升级前健康巡检与回退时使用。
source_book: OmniSwitch AOS Release 8.10R4 Release Notes
---

## R（触发场景）
- 计划把 OmniSwitch 升到 8.10R4（或跨版本迁移），需要选标准升级还是 ISSU
- 升级前做健康巡检、基线采集、固件版本核对
- 需要升级 U-Boot / FPGA / CPLD / ONIE 等引导件或逻辑件
- VC 或模块化机箱要业务中断最小化的在服务升级（ISSU）
- 升级出问题要用 Certified 目录回退

## I（核心理念）
升级方法论二分框架（F1，<<<PAGE 67-76>>>）：Standard（传镜像到 Running 目录→reload→验证→copy running certified，全程一次中断）vs ISSU（逐成员/逐 CMM 升级、双归属主机不断链）。选型三问——平台是否支持 ISSU（6360/6465/6560/6570M 不支持，X2，<<<PAGE 69>>>）、源版本是否在 ISSU 支持清单、是否需要保留 running 目录名。升级前置四查：certified 配置、U-Boot/FPGA 版本、tech-support 基线、EMP/console 带外通道。固件三件套分层框架（F2，<<<PAGE 4-14>>>/<<<PAGE 77-82>>>）：AOS 镜像（功能性）／引导件 U-Boot·ONIE·BIOS（信任链与启动）／逻辑件 FPGA·CPLD（电源/风扇/PoE/PHY 行为）三者独立演进，版本矩阵按机型×部件列 Minimum/Current；每条 FPGA/U-Boot 升级都对应 CRAOS8X 编号，可反查"该现象要不要升固件"。ISSU 机理（P37，<<<PAGE 67>>>）：VC 按 chassis-id 从低到高逐台从 ISSU 目录重启，Slave 全部完成后 Master 重启引发 takeover；模块化机箱则备 CMM 先升转主。

## A1（决策框架）
1. **先核对固件三件套版本**：`show hardware-info` 查 U-Boot/FPGA 当前版本，对照 System Specifications 表 Minimum 列，低于最小值先走 FPGA/U-Boot 升级（C3，<<<PAGE 4>>>）
2. **平台在 ISSU 黑名单（6360/6465/6560(E)/6570M）→ 只能标准升级**；其余平台再查源版本支持清单
3. **标准升级五步**：下载对应机型镜像→FTP 二进制传到 Running 目录→`reload from working no rollback-timeout`→验证→固化（C4，<<<PAGE 72-73>>>）
4. **ISSU 十二步**：清 Slave 同名目录→传镜像+issu_version→`issu from issu_dir`→等 System ready→认证（C5，<<<PAGE 74-76>>>）
5. **回退兜底**：`reload from certified no rollback-timeout`（P38，<<<PAGE 73>>>）

## A2（操作步骤）
- **升级前巡检**：`show system`（版本/Flash 余量）→ 删旧日志 `rm *.log`/`rm *.tar` → 检查 /flash/pmd 与 /flash/pmd/work（<10 天的新文件先联系 Support）→ `show running-directory` 须 CERTIFIED+SYNCHRONIZED，否则 `write memory flash-synchro`（C1，<<<PAGE 70>>>）
- **基线采集**：`show tech-support` / layer2 / layer3 + `show tech-support eng complete`（TAR 含 SWLOG），导出留档（C2，<<<PAGE 71>>>）
- **标准升级**：镜像名按机型（6360=Nosa.img、6465/6560=Nos.img、6570M=Wos.img、6860/6865=Uos.img、6860N=Uosn.img、6870=Kaos.img、6900=Yos.img、9900=Mos.img+Mhost.img+Meni.img）→ `reload from working no rollback-timeout`（VC 自动复制镜像到全部 Slave 并整环重启，5-20 分钟）→ 验证 `show microcode` + `show running-directory`（CERTIFY NEEDED）→ `copy running certified`（C4，<<<PAGE 72-73>>>）
- **ISSU**：`mkdir /flash/issu_dir` → `debug show virtual-chassis connection` 查 Slave VFL IP（127.10.x.65）→ `ssh 127.10.2.65`（密码 switch）删 Slave 同名目录 → `cp /flash/working/*.cfg /flash/issu_dir` → FTP 镜像+issu_version → `issu from issu_dir` → `show issu status` → `debug show virtual-chassis topology` 确认全 System Ready → `write memory flash-synchro` → 可选 `copy certified working make-running-directory`（C5，<<<PAGE 74-76>>>）
- **FPGA/CPLD**：`update fpga-cpld cmm all file fpga_kit_9022`（all 覆盖 VC 全成员）→ 见 "Reload required" 后重启（C6，<<<PAGE 79-80>>>）
- **U-Boot**：`update uboot cmm all file /flash/u-boot.8.10.R04.37.tar.gz` → 重启生效（C7，<<<PAGE 80>>>）
- **ONIE 机型 CPLD/ONIE**：`update fpga-cpld cmm all file updater_kit_8629`（多 CPLD 需多次执行）→ 手动 reload 进 "ONIE: Update ONIE" 模式（勿按键）→ OS6860N（除 U28）自动 power cycle，其他手动 → `pkgmgr install uosn-onie-v1.deb`（6870 用 kaos-onie-v1.deb）→ reload 回 running（C8，<<<PAGE 81-82>>>）

## E（实证案例）
- 升级前健康巡检与基线采集（C1/C2，<<<PAGE 70-71>>>）
- 五步标准升级与回退（C4，<<<PAGE 72-73>>>）
- 十二步 ISSU 全流程（C5，<<<PAGE 74-76>>>）
- FPGA/U-Boot/ONIE 三类固件升级（C6/C7/C8，<<<PAGE 79-82>>>）

## B（反例/坑）
- ISSU 在 6360/6465/6560(E)/6570M 全系不支持，只能标准升级（X2，<<<PAGE 69>>>）
- ISSU 期间禁止改配置：等 System ready/[L8] 再做 write-memory/配置变更（X14，<<<PAGE 76>>>）
- Slave 存在同名 ISSU 目录会破坏升级：须 SSH 到 Slave（VFL 内网 IP 127.10.x.65）删除（X15，<<<PAGE 75>>>）
- ONIE 机型 CPLD 升级后只启动到 Certified 目录，不回 running，需手动再切（X18，<<<PAGE 82>>>）
- 9900 XNI 板用于 CMM2/OS9912 机箱前必须先升 U-Boot 与 FPGA；OS99-XNI-U12Q 与 OS9912 机箱不兼容（X30，<<<PAGE 14>>>）
- 8.9R2→8.10R2 升级曾把配置的 SPB 控制 MAC 回落为默认导致邻接丢失，8.10R4 修正——跨版本升级后核查 SPB 邻接（X13，<<<PAGE 94>>>）
- 出厂首启 VC 自动化副作用：vcboot.cfg/vcsetup.cfg 只写 working 不写 certified，chassis-id 固定为 1 可能引发冲突，需 reset-to-factory 纠正（P40，<<<PAGE 15>>>）
- 6450 动态路由在 uptime 超 828.5 天后老化复位抖动——超长不重启的网关设备升级前留意（X20，<<<PAGE 90>>>）

## 来源
OmniSwitch AOS Release 8.10R4 Release Notes Appendix D（<<<PAGE 67-71>>>）、Appendix E（<<<PAGE 72-73>>>）、Appendix F（<<<PAGE 74-76>>>）、Appendix G（<<<PAGE 77-80>>>）、Appendix H（<<<PAGE 81-82>>>）、System Specifications（<<<PAGE 4-14>>>）。条目来源：cases C1-C8；principles P37-P40；counter-examples X2/X13/X14/X15/X18/X20/X30；frameworks F1/F2。
