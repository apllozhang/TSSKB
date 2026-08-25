# frameworks — 体系框架（OmniSwitch AOS 8.10R4 Release Notes）

格式：编号 F# ｜ 框架名 ｜ 结构与运用 ｜ 页码

- **F1** AOS 升级方法论二分框架：Standard（传镜像到 Running 目录→reload→验证→copy running certified，全程一次中断）vs ISSU（逐成员/逐 CMM 升级、双归属主机不断链）；选型三问——平台是否支持 ISSU（6360/6465/6560/6570M 不支持）、源版本是否在 ISSU 支持清单、是否需要保留 running 目录名（ISSU 后可 make-running-directory 切回）。升级前置四查：certified 配置、U-Boot/FPGA 版本、tech-support 基线、EMP/console 带外通道。 <<<PAGE 67>>>-<<<PAGE 76>>>
- **F2** 固件三件套分层框架：AOS 镜像（功能性升级）／引导件 U-Boot·ONIE·BIOS（Secure Boot 信任链、NAND/eUSB 修复、启动模式）／逻辑件 FPGA·CPLD（电源、风扇、PoE、端口 PHY 行为）三者独立演进、版本矩阵按机型×部件列 Minimum/Current；排障口诀——先 `show hardware-info` 对 Minimum，再决定是否走 `update fpga-cpld`/`update uboot`/`pkgmgr install *-onie`。CR 驱动：每条 FPGA/U-Boot 升级都对应 CRAOS8X 编号，可反查"我这个现象要不要升固件"。 <<<PAGE 4>>>-<<<PAGE 14>>>/<<<PAGE 77>>>-<<<PAGE 82>>>
- **F3** Secure Boot 平台分型框架：U-Boot 型（6360/6465/6560/6570M——先升 U-Boot 再升镜像，之后只认 Secure Boot 镜像）／ONIE 型（6860N/6870/6900-X 系列——BIOS 使能+ONIE 包，过渡期兼容非 SB 镜像）／例外型（6860(E)/6865/9900/6900-V72·C32·V48C8·C32E 不支持或需 BIOS）；混 VC 用"最小公分母"（非 Secure Boot 镜像）。 <<<PAGE 104>>>/<<<PAGE 105>>>
- **F4** Feature Matrix 特性核对法：13 平台 × 特性 × 首次支持版本（Y=历来支持 / N=不支持 / 版本号=该版引入 / EA=Early Availability 未完整验证不支持）；选型/排障三步——先定平台列，再看特性行版本，最后对照 Licensed Features 表确认是否要许可（Feature/Performance、Metro、Advanced Routing、Premium 四类）。 <<<PAGE 52>>>-<<<PAGE 61>>>/<<<PAGE 19>>>

---
合计：4 条（F1-F4）。
