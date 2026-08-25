# cases — 升级/运维流程案例（OmniSwitch AOS 8.10R4 Release Notes）

格式：编号 C# ｜ 场景 ｜ 命令序列（-> 为 AOS CLI 提示符）｜ 验证命令 ｜ 页码

## 升级前置（Appendix D）

- **C1** 升级前健康巡检：`show system`（确认日期/版本/型号/Flash 余量）→ 删旧日志 `rm *.log`、`rm *.tar` → 检查 /flash/pmd 与 /flash/pmd/work（<10 天的新文件先联系 Support）→ `show running-directory` 确认 CERTIFIED+SYNCHRONIZED，不是则 `write memory flash-synchro`。 <<<PAGE 70>>>
- **C2** 升级前基线采集：`show tech-support` / `show tech-support layer2` / `show tech-support layer3`（自动落日志到 /flash）+ `show tech-support eng complete`（TAR 含多份日志与 SWLOG），导出留档。 <<<PAGE 71>>>
- **C3** 固件版本核对：`show hardware-info` 查当前 U-Boot/FPGA 版本，对照 System Specifications 表的 Minimum 列，低于最小值走 FPGA/U-Boot 升级流程。 <<<PAGE 4>>>

## 标准升级（Appendix E，独立机箱或 VC）

- **C4** 五步标准升级：①下载镜像（6360=Nosa.img、6465/6560=Nos.img、6570M=Wos.img、6860/6865=Uos.img、6860N=Uosn.img、6870=Kaos.img、6900=Yos.img、9900=Mos.img+Mhost.img+Meni.img）→ ②FTP 二进制传到 Running 目录 → ③`reload from working no rollback-timeout`（VC 会自动复制镜像到全部 Slave 并整环重启，5-20 分钟）→ ④验证 `show microcode`（含 Secure Boot 列）+ `show running-directory`（CERTIFY NEEDED）→ ⑤`copy running certified` 固化。回退：`reload from certified no rollback-timeout`。 <<<PAGE 72>>>/<<<PAGE 73>>>

## ISSU（Appendix F，VC 或模块化机箱）

- **C5** 十二步 ISSU：`mkdir /flash/issu_dir` → `debug show virtual-chassis connection` 查 Slave VFL IP（127.10.x.65）→ `ssh 127.10.2.65`（密码 switch）→ Slave 上 `rm -r /flash/issu_dir` 清同名目录 → `exit` → Master `cp /flash/working/*.cfg /flash/issu_dir` → FTP 镜像+issu_version 到 ISSU 目录 → `ls /flash/issu_dir` 核对 → `issu from issu_dir` → `show issu status`（pending→not active 即完成；期间禁改配置，等 [L8]/System ready）→ `debug show virtual-chassis topology` 确认全部 System Ready → `write memory flash-synchro` 认证 → 可选 `copy certified working make-running-directory` 恢复原运行目录。 <<<PAGE 74>>>-<<<PAGE 76>>>

## FPGA / U-Boot 升级（Appendix G）

- **C6** FPGA/CPLD 升级：下载 kit（如 fpga_kit_9631）→ FTP 到 /flash → `update fpga-cpld cmm all file fpga_kit_9022`（all 参数覆盖 VC 全部成员）→ 显示 "Reload required to activate new firmware" 后重启。 <<<PAGE 79>>>/<<<PAGE 80>>>
- **C7** U-Boot 升级：FTP u-boot tar 包到 /flash → `update uboot cmm all file /flash/u-boot.8.10.R04.37.tar.gz` → 重启生效。 <<<PAGE 80>>>

## CPLD/ONIE 升级（Appendix H，ONIE 机型）

- **C8** ONIE 机型 CPLD/ONIE 升级：确认配置 certified+synchronized、建议接 console → FTP updater kit 到 /flash → `update fpga-cpld cmm all file updater_kit_8629`（多 CPLD 需多次执行，无升级会提示 no pending）→ 手动 reload 进 "ONIE: Update ONIE" 模式（勿按键）→ 自动更新 CPLD 后只启动到 Certified 目录 → OS6860N（除 U28）自动上电循环，其他机型手动 power cycle → ONIE 更新 `pkgmgr install uosn-onie-v1.deb`（6870 用 kaos-onie-v1.deb）→ reload 回 running 目录。 <<<PAGE 81>>>/<<<PAGE 82>>>

## Secure Boot 升级（Appendix L）

- **C9** U-Boot 平台（6360/6465/6560/6570M）：先 `update uboot` 到 8.10.37.R04 → 再用 Secure Boot 镜像升 AOS。 <<<PAGE 105>>>
- **C10** ONIE 平台（6860N/6870/6900-X48C6 等）：用 Secure Boot 镜像升 AOS → 重启进 BIOS 启用 Secure Boot →（仅 6860N/6870）`pkgmgr install uosn-onie-v1.deb` + `write memory flash-synchro` 升 ONIE/Diag。 <<<PAGE 105>>>
- **C11** 6900-V48C8/C32E：先升 BIOS（C32E v40.01.01.03 / V48C8 v40.01.01.04，联系 Support）→ 再升 Secure Boot 镜像 → 重启进 BIOS 启用。 <<<PAGE 105>>>

## 包管理与密码治理（Appendix J）

- **C12** 包安装/卸载：`pkgmgr verify nos-mrp-v1.deb`（MD5 校验）→ `pkgmgr install nos-mrp-v1.deb` → `write memory`（不 commit 重启会镜像校验失败）→ `show pkgmgr`（+ 未保存、* 待 reload）；卸载 `pkgmgr remove mrp` → `write memory` → `rm /flash/working/pkg/nos-mrp-v#.deb`。 <<<PAGE 101>>>/<<<PAGE 102>>>
- **C13** 升级前 AMS/IoT-Profiler 密码加密化：升级 8.7R1+ 前删 `/flash/<running>/pkg/ams/ams-broker.cfg`（每台 VC 成员）→ 升级 → 重配 broker（密码自动加密）；AMS-APPS 同理删 `pkg/ams-apps/install.sh`，升级后 ovbroker.cfg 密码加密。 <<<PAGE 102>>>

## 热插拔与电源（Hot-Swap Guidelines）

- **C14** 模块热插拔规程：拆线 → 拔光模块 → 拔板卡等 ≥30 秒再插同型号（CMM 插后等 15-20 分钟；NI 拔插间隔 30 秒；新模块插入间隔 5 分钟且 LED 回正常）→ 重插光模块 → 接线；CFM 一次只换一个、120 秒内完成、风扇框必须全程在位。 <<<PAGE 47>>>/<<<PAGE 48>>>
- **C15** fast/perpetual PoE 机型换异种电源（6860N-P48M）：禁 fpoe/ppoe（lanpower 已启才需）→ 保存同步配置 → 换电源 → reload 机箱 → 启 lanpower → 重新启 fpoe/ppoe → 保存同步。 <<<PAGE 48>>>/<<<PAGE 49>>>

## 安全加固与特性运维（散点）

- **C16** 弱加密禁用与查看：`system security crypto-strong-security enable` + `show system security`；弱密钥探测 `ssh strong-hmacs enable`。 <<<PAGE 28>>>/<<<PAGE 16>>>
- **C17** SPB BVLAN 收敛运维：`show spb isis bvlans` 查 In Use（全网视图）→ 维护窗内把业务删并重建到 4 条 BVLAN → 空闲 BVLAN 全网删除（无影响）。 <<<PAGE 66>>>
- **C18** Celona PD 降级规避：`lanpower {slot | port} autoclass disable`。 <<<PAGE 34>>>
- **C19** MKA VLAN 隧道化配置：`interfaces <c/s/p> macsec mode dynamic mka-vlan <vid> [mka-tpid <tpid>]`；撤销 `no interfaces <c/s/p> macsec mka-vlan`；验证 `show interfaces macsec mka-info`。 <<<PAGE 35>>>

---
合计：19 条（C1-C19）。
