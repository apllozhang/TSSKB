---
name: boot-system-troubleshooting
description: 何时用：交换机启动失败、忘记密码、模块 DOWN、硬件版本不符、CPU 飙高、温度/LED 异常等系统级排障与应急恢复。
source_book: DT00XTE221EN OmniSwitch LAN Troubleshooting
---

# 启动序列与交换系统排障

## R · 原文引用

> "Step1. Power cycle the switch ... Break the boot sequence ... 'Hit any key to stop autoboot:' => setAdminPasswordDefault ... => boot (6900) / => reset (6860)" (p76)

> "The operational status can be DOWN while the power status is ON, indicating a possible software issue -> show module status ... -> show module long" (p100)

> "Note: AOS must be upgraded prior to performing an FPGA/CPLD or U-boot upgrade." (p102)

> "The most common causes for high CPU utilization: An abnormal process ... AOS is under a DoS attack. Too many frames or packets are trapped to CPU. Use the commands 'top' and 'ps' in the maintenance shell" (p110-111)

## I · 方法论骨架

1. **启动机制双路径**：U-Boot 机型（6360/6560/6860）——硬件初始化→内存诊断→按 bootfile 环境变量选镜像→AOS 入 RAM（g07）；ONIE 机型（OS6860N/6900）——启动菜单选 ALE OS certified 或 ONIE（含 Install/Rescue/DIAG）（g08）。闪存双目录 certified/working 是回滚基础（g06）。
2. **系统层命令链**（f05）：show system（版本/uptime/时间）→ show chassis / show cmm → show running-directory + show microcode [loaded|certified] → show module status / show module long → show hardware-info（U-Boot/FPGA/CPLD/CPU/RAM，对照 release note）→ show health → show transceivers / show powersupply / show fan / show temperature → 面板 LED 判读。
3. **判读判据**：
   - POWER ON + operational DOWN = 软件问题优先怀疑，不是硬件返修（p05/ce05）。
   - 短 uptime = 刚发生过重启，重要线索（p04）。
   - show system 的 Date&Time 是日志对时前提，NTP 环境用 ntp client admin-state enable（p04）。
   - U-Boot/FPGA 有最低版本门槛，先升 AOS 再升 FPGA/CPLD/U-Boot（p06/ce09 铁律）。
4. **高 CPU 四大根因**（p07）：异常进程（死循环=软件缺陷）、网络规模设计不当、DoS 攻击、消息/上 CPU 报文过多（大量日志、MAC 学习、环流量）。流程（f06）：show health 确认水位（1min/1h/1day）→ show health slot/port 隔离到 NI 或端口 → su 维护 shell 用 top（N/M/P/T 排序、-b -d）/ ps -T 定位进程 → 联系 ALE 支持，不自行杀进程。
5. **温度双阈值**（p08）：Warning 发 trap；Danger 所有 NI 模块关断且需手动 boot 恢复。
6. **LED 速查**（p09）：OK 常绿=正常（VC slave）；闪绿=VC master；常琥珀=诊断或 AOS 启动失败。PS 常绿=双电源好；OK+PS 同闪琥珀=缺风扇盘或气流方向不匹配。

## A1 · 书中案例（LAB 故障根因）

本 skill 无独立 LAB，但系统层判读是 LAB 全部案例的前置：LAB4 开场先 `show system` 核对两台日期时间再查 OSPF（c08）；LAB2 中 show health CPU 98% 指向 VLAN 278 环路（c04 根因在 stp-loop skill）。崩溃类故障产物是 PMD 文件（/flash/pmd/，g33），处置方向为收集证据升级 TAC（c11，详见 ovna skill）。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：设备无法启动/密码丢失/USB 恢复；show module 异常；版本升级前门槛核对；CPU 告警；温度/风扇/电源告警；面板灯异常。
- 区分：业务口 down 但整机正常 → l2-connectivity；VC 相关的模块/chassis 状态 → virtual-chassis；CPU 高伴随 MAC 漂移/DoS 刷屏 → stp-loop（先查环）；整机崩溃出 PMD → 本 skill 判读 + ovna skill 处置链。

## E · 可执行步骤

1. **密码恢复（U-Boot 机型）**：断电重启 → "Hit any key to stop autoboot:" 打断 → `setAdminPasswordDefault` → `boot`（6900）或 `reset`（6860，或等 90 秒）。
2. **密码恢复（ONIE 机型，仅限 console）**：重启选 ONIE → DIAG 模式 → `blkid` 找分区 → `cd /mnt/ssd5/system` → `rm userTable8` → `reboot` → `modify running working` 后从 certified 重启。
3. **USB 恢复 CMM**：Trescue.img 与交换机目录结构放 U 盘根目录 → 打断启动 → `run rescue`（重格闪存约 10 分钟）→ 验证 certified/working 微码。ONIE USB 恢复：`blkid` → `mount /dev/sda1` → cp 镜像到 /var/tmp → `onie-nos-install`。
4. **改启动目录**：u-boot 下 `setenv bootfile working/Uos.img` → `saveenv` → `run bootcmd`。
5. **系统体检命令链**：show system → show chassis/show cmm → show running-directory/show microcode loaded → show module status/long → show hardware-info（对照 release note）→ show health → show temperature/powersupply/fan/transceivers。
6. **升级顺序**：先 AOS → 再 `update uboot cmm all file ...` / `update fpga-cpld cmm all file ...`。
7. **高 CPU**：show health [all cpu] → show health slot <c/s> → su 进维护 shell（top / ps -T）→ 联系 TAC 获取处置流程，用完立即 exit。

## B · 边界与陷阱

- **ce11**：ONIE 密码恢复只能从 console 做，网管侧做不了。
- **ce02**：su 维护 shell 不是后门，只在技术支持指导下用；动作限定只读观察，找到可疑进程后联系 ALE，不自行杀。
- **ce05**：POWER ON + DOWN ≠ 硬件故障，先走软件侧排查（show microcode loaded、版本核对）。
- **ce09**：升级顺序颠倒（先 U-Boot/FPGA 后 AOS）会出问题，铁律不可违反。
- 温度到 Danger 阈值后所有 NI 关断，需手动 boot 恢复（p08）。
- show hardware-info 的版本判断必须以目标 AOS 的 release note 为准，不能凭经验。

---
来源条目: f04, f05, f06, p04, p05, p06, p07, p08, p09, ce02, ce05, ce09, ce11, g03, g04, g05, g06, g07, g08
