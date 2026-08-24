---
name: CLI Scripting 与批量配置操作
description: 需要向多台交换机批量下发 CLI 脚本（立即或定时/周期）、开 Telnet/SSH 终端会话、查看脚本执行日志，或用 VLAN Manager 批量建 VLAN/IP 接口时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 同一段配置要在几十台交换机上执行，逐台手敲不现实
- 需要周期性（Simple/Cron）执行的运维脚本
- 脚本下发后需要核对哪些成功、哪些报语法错误

## I（核心理念）
CLI Scripting 把"ASCII 配置可复制粘贴"的 CLI 优势产品化：脚本统一存于 OV，向导式选择目标设备与调度策略，支持用户变量填充，执行结果集中留日志。GUI 批量操作（如 VLAN Manager）与脚本互补——前者靠向导防错，后者靠灵活复用。

## A1（行动框架）
1. **查看/创建脚本**：Configuration → CLI Scripting → Scripts：可查看预置脚本的命令内容（<<<PAGE 209-214>>>）
2. **发送脚本**：Send Script（向导）→ Add/Remove Devices 选交换机 → 立即 Send，或 Next 调度（Periodically + Simple/Cron）→ 填用户变量 → Send Script（<<<PAGE 209-214>>>）
3. **终端会话**：Terminal 菜单开 Telnet/SSH 会话直连设备（<<<PAGE 209-214>>>）
4. **查日志**：Logs 菜单查看脚本执行结果（Success/Error/语法错误）（<<<PAGE 209-214>>>）
5. **VLAN Manager 批量建 VLAN**：Configuration → VLANs → Create VLAN by Devices（VLAN Wizard）：填 VLAN ID → Add/Remove Devices（Add All>>）→ Q Tagged Ports Assignment（逐交换机 Add Port）→ Review → Create；再点 IP interface → "+" 建 IP 接口（Name/IP 192.168.VLAN#.Switch#/Mask/Device）→ Create → 控制台验证（<<<PAGE 180-184>>>）

## A2（进阶应用）
- 升级后收尾也是经 CLI 会话完成：Topology 选中交换机 → CLI Scripting – SSH → 从 working 目录 reload → Copy Working Certified（<<<PAGE 206>>>）
- 认证类排查命令可直接经终端执行，如 `aaa test-radius-server RADIUS_VM type authentication user employee password password`（<<<PAGE 263>>>）
- CLI vs GUI 的选择依据（<<<PAGE 22-24>>>）：CLI 胜在熟练度、脚本化、配置文件跨机复制粘贴；GUI 胜在颜色编码、易发现问题、减少 fat-finger、批量操作

## E（实证案例）
- 创建/发送脚本与查看日志（Success/Error/语法错误分类）——cases·CLI Scripting（<<<PAGE 209-214>>>）
- VLAN Wizard 批量建 VLAN + IP 接口并在控制台验证——cases·VLAN Manager（<<<PAGE 180-184>>>）

## B（边界与陷阱）
- 脚本日志中的语法错误要逐条处理，Success 不代表语义正确，仍需设备侧验证（结合 `show` 命令）（<<<PAGE 209-214>>>）
- Shell 方式（Telnet/SSH）取决于 Discovery Profile Advanced 段的 Shell Preference，与设备实际配置一致（<<<PAGE 110-112>>>）

## 来源
- cases·CLI Scripting（<<<PAGE 209-214>>>）、VLAN Manager（<<<PAGE 180-184>>>）
- principles·CLI vs GUI 取舍（<<<PAGE 22-24>>>）
- cases·镜像升级收尾经 CLI SSH（<<<PAGE 206>>>）
