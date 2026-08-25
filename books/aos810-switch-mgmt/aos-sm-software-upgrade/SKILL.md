---
name: AOS 8 代码升级与软件包管理（reload/ISSU/签名镜像/回滚/USB）
description: 需要在 OmniSwitch AOS 8 上执行软件升级（standalone/VC 标准 reload 升级或 ISSU 在线升级）、升级前维护基线采集、管理 pkgmgr/appmgr Debian 包、签名镜像与 Secure Boot、USB 自动升级/备份/灾难恢复时使用。
source_book: OmniSwitch AOS Release 8.10R4 Switch Management Guide
---

## R（触发场景）
- 计划把交换机/VC 从旧版本 AOS 升级到 8.10R4（标准 reload 升级或 ISSU 最小中断升级）
- 升级前要做维护例行：清旧文件、确认 certified/synchronized、采 tech-support 基线
- 安装/移除 Debian 应用包（NTP、Cirrus Agent、Nutanix 插件等），或免重启启停应用
- 处理签名镜像降级、u-boot/ONIE 版本匹配、镜像完整性校验
- 用 USB 闪存做自动批量升级、备份或灾难恢复（含 ONIE 设备）

## I（核心理念）
标准升级模型（P13）：上传新镜像到 Running 目录 → reload → 验证 → certify；VC 场景 Master 先把镜像拷给 Slave 再统一重启。ISSU（P14）按 chassis-id 从低到高逐台重启 Slave、最后重启 Master，实现最小网络 disruption。目录结构即回滚体系（certified 保底）。安全链：ALE Secured Code + ASLR（P18）→ RSA-2048/SHA-256 签名镜像（P19）→ Secure Boot 启动链验证（P20）。包管理双组件（P21）：pkgmgr 管验证/安装/移除，appmgr 管免重启启停；安装必须 `write memory` 持久化（P23）。

## A1（决策框架）
1. **standalone/普通 VC 选标准升级**：维护前置 → 下载 → FTP 到 RUNNING 目录 → reload → 验证 → certify（C1，<<<PAGE 23-24>>>）
2. **不能中断的 VC/机箱选 ISSU**：Master 建 ISSU 目录（清理旧 ISSU 目录）→ 拷当前 Running 配置进 ISSU 目录 → FTP 新镜像+验证文件 → issu 执行 → 验证 certify → 复位 NI（C2，<<<PAGE 24>>>）
3. **升级前必做维护基线**：`show system` → 清 *.log/*.tar 与 /pmd → `show running-directory` 确认 certified/synchronized → `show tech-support` 基线（C3，<<<PAGE 23>>>；P17）
4. **非 AOS 软件走包管理**：`pkgmgr verify`（MD5+兼容版本）→ install → write memory（C17）；应用启停用 appmgr 免重启（C18）
5. **批量/灾备场景用 USB**：自动拷贝需 aossignature 签名文件防误触发（P90）；灾难恢复用 Trescue.img 或 ONIE Rescue（P91）

## A2（操作步骤）
- **标准升级**：维护例行（C3）→ 下载升级文件 → FTP 到 RUNNING 目录 → `reload` → 验证 → certify（C1，<<<PAGE 23-24>>>）
- **ISSU**：`issu` 执行 → 验证 → certify → 复位 NI（NI 未按时复位则系统按槽位升序逐个强制复位，P16）（C2，<<<PAGE 24>>>）
- **包安装**：包放 /flash/working/pkg → `pkgmgr verify yos-ntpd-v1.deb` → `pkgmgr install yos-ntpd-v1.deb` → `write memory` → `show pkgmgr`；移除 `pkgmgr remove ntpd` + write memory（C17，<<<PAGE 87-88>>>）
- **应用启停**：`appmgr start|stop|restart ams config-dbase` + `write memory`；`show appmgr`（+ 表示未跨重启保存）（C18，<<<PAGE 89-90>>>）
- **镜像完整性**：`image integrity check` 比对目录镜像 SHA256 与 key file；`image integrity get-key` 显示哈希（P92，<<<PAGE 118>>>）
- **USB 自动升级**：USB 根放 aossignature 空文件 + 6900/working 目录放镜像 → `usb enable` → `usb auto-copy enable copy config enable` → 插 USB；备份 `usb backup admin-state enable`（C24，<<<PAGE 113-114>>>）
- **USB 灾难恢复**：传统——USB 建 6900/certified|working + 根放 Trescue.img → 重启 → miniboot/uboot 下 `run rescue`；ONIE——根放 Yos.img → Onie Menu > Onie Rescue → `blkid` 找盘 → mount → `onie-nos-install /var/tmp/Yos.img`（C25，<<<PAGE 116>>>）

## E（实证案例）
- 标准升级（standalone/VC）全流程（C1，<<<PAGE 23-24>>>）
- ISSU 升级流程含验证文件与 NI 复位（C2，<<<PAGE 24>>>）
- 升级前维护例行基线（C3，<<<PAGE 23>>>）
- Debian 包安装/验证/移除以 NTP 为例（C17，<<<PAGE 87-88>>>）
- USB 升级/备份与灾难恢复（C24/C25，<<<PAGE 113-116>>>）

## B（反例/坑）
- 签名镜像机型降级到旧版 AOS 必须先降 u-boot（X9，<<<PAGE 66>>>）
- 同一应用不能同时装多个 Debian 包，且包须与当前 AOS 发行版同版本（X16，<<<PAGE 87>>>）
- 包未 write memory 保存则重启/VC takeover 后丢失（X17，<<<PAGE 87>>>；P23）
- 安全补丁类包（OpenSSL 等）删除后必须重启才回滚到镜像内置版本（X18，<<<PAGE 88>>>）
- U-boot 访问禁用 + 镜像损坏 = 只能返厂（X19）；U-boot 密码遗忘 + flash 损坏同样返厂（X20）；ONIE 密码遗忘无法灾备只能 RMA（X21）（<<<PAGE 91-92>>>）
- ISSU 后 NI 必须复位，超时由系统按槽位升序强制执行（P16，<<<PAGE 24>>>）
- USB 自动拷贝重启后自动关闭；auto-copy 与 backup 互斥（P90，<<<PAGE 113-114>>>）

## 来源
OmniSwitch AOS 8.10R4 Switch Management Guide 第 1 章 Upgrading AOS（<<<PAGE 21-24>>>）、第 3 章 Loading Software / Secured Code / Package Management / U-boot & ONIE（<<<PAGE 62-92>>>）、第 4 章 USB（<<<PAGE 113-118>>>）。条目来源：cases C1/C2/C3/C17/C18/C24/C25；principles P13-P25/P90-P92；counter-examples X9/X16-X21；frameworks F6。
