---
name: Resource Manager 与模板化 Provisioning
description: 需要备份/恢复交换机配置、导入镜像并批量升级（含 Scheduled Upgrades）、生成 Inventory 报表，或用 Provisioning Rule/Golden Config/Thin Client 做零 touch 配置管理时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 变更前要备份配置、误改后要恢复，或需要把某台设备回滚到"黄金配置"
- 需要给一批交换机升级固件（立即或定时），并确认升级真正生效
- 新交换机上线希望自动匹配规则推送配置（Template Based Provisioning）

## I（核心理念）
Resource Manager 解决"存量设备的配置与固件生命周期"（备份/恢复/升级/清单），Provisioning 解决"新设备的零接触上线"（三阶段状态模型：Factory-default → Bootstrapped → Provisioned）。核心机制是规则匹配：交换机每 5 分钟联系 OV 一次，命中 Rule（序列号/MAC/型号）即推送管理与配置模板。

## A1（行动框架）
1. **配置备份**：Configuration → Resource Manager → Backup/Restore → Backup → Backup by Devices → Switch Picker 选设备 → （提示 FTP 认证则 Add FTP Authentication：admin/switch）→ Backup Type=Configuration Only → Backup（<<<PAGE 197-198>>>）
2. **恢复配置**：Restore → Add/Remove Backup Files → 选文件 → Restore → 确认 Yes（<<<PAGE 199-201>>>）
3. **镜像升级**：Upgrade Image → Import（*.zip）→ Install → 选固件 → Add/Remove Device（OV 只列出兼容该版本的交换机）→ Install Software；完成后 **SSH 到交换机从 working 目录 reload，重启后执行 Copy Working Certified**（<<<PAGE 203-206>>>）
4. **定时批量升级**：Discovery → Scheduled Upgrades：可多台同时升级、立即或定时、每台可设不同版本与安装目录；完成后到 Managed Devices 检查安装目录与状态是否 successful（<<<PAGE 124-126>>>）
5. **Inventory 报表**：Resource Manager → Inventory → Create Report → Select Devices → 选报告类型 → Create → 点链接浏览器打开（<<<PAGE 202>>>）
6. **Provisioning Rule**：字段含 Serial Number/MAC、Switch Model、Switch Config Template（追加到现有配置）、Value Mapping（动态模板必填）、Mgmt Users Template（默认推送）、Save and Certify；Results 表查看尝试过的交换机（<<<PAGE 461-462>>>）
7. **Golden Config / 强制下发**：Golden Config 列点 Edit，从最近三次备份中选一并 Apply；"The Force Provisioning Config button is used to push a Provisioning Rule configuration to a matching switch the next time the switch contacts the OmniVista server."（<<<PAGE 466-467>>>）

## A2（进阶应用）
- 动态模板 + 值映射：模板分 Static（无变量）与 Dynamic（带 $VLAN/$PORTS 变量）；动态模板必须建 Value Mappings，由模板+变量值表推导实际下发配置（<<<PAGE 463-464>>>）
- 引导方式：DHCP Option 43 Sub-Option 128 指向本地 OV 激活服务器（推荐），或 DNS 把 activation.myovcloud.com 解析到 OV；存量交换机改 cloudagent.cfg 的 Activation Server URL（as-lite.*.ove.local）并 `cloud-agent admin-state enable`（<<<PAGE 460>>>）
- 部署场景矩阵：①Mobile App 离线 ②Mobile App 在线 ③Advanced DHCP+RCL（企业/园区）④仅 Advanced DHCP；场景 1/2 依赖尚未发布的 Mobile App 功能，当前不可实施（<<<PAGE 418/451/415>>>）
- Thin Client 模式：交换机零本地配置（仅 vcboot.cfg 保底网络可达），开机经 activation/call-home 从 OV 取配置；Incremental Template 只在下一次周期 call-home（默认 30 分钟）应用一次（<<<PAGE 75-77>>>）；Rule 可配 Thin Switch Yes/No 与 Desired Switch Config（Template+Incremental/最新备份快照/Golden 快照）（<<<PAGE 76>>>）
- Golden Configuration 审计："Configuration selected from a list of the three most recent switch backups that can be applied to a switch in the event there is an unwanted configuration change"；可周期审计、标记 golden、偏离告警（<<<PAGE 467/417>>>）

## E（实证案例）
- 配置备份与恢复（含 FTP 凭据补充）——cases·备份恢复（<<<PAGE 197-201>>>）
- 镜像导入升级 + 升级后手工 reload/Copy Working Certified——cases·镜像升级（<<<PAGE 203-206>>>）
- Provisioning Rule 创建与 Golden Config/Force Provision——cases·Provisioning（<<<PAGE 462-467>>>）

## B（边界与陷阱）
- 升级完成的收尾动作不能漏：需 SSH reload + Copy Working Certified，漏做则升级不生效；实验环境镜像升级节"DO NOT perform this section unless directed by your instructor."（<<<PAGE 203/206>>>）
- 备份向导可能因交换机缺 FTP 凭据中断："Click on Add FTP Authentication if prompted."（<<<PAGE 198>>>）
- Thin Client 模式下"All configuration changes should be done in OV 2500"——本地改配置无意义/会被覆盖；且仅 AOS 8.8R1+ 支持（<<<PAGE 75>>>）

## 来源
- frameworks·Provisioning 四场景矩阵（<<<PAGE 414/418/451>>>）、动态模板+值映射（<<<PAGE 463-464>>>）
- principles·Rule 匹配机制（<<<PAGE 461>>>）、Golden Config 审计（<<<PAGE 417/467>>>）、RCL/Bootstrap（<<<PAGE 460>>>）、NaaS 许可状态（<<<PAGE 127>>>）、Thin Client（<<<PAGE 75-77>>>）
- cases·备份恢复/镜像升级/Inventory/Scheduled Upgrades/Provisioning/Thin Client 规则（<<<PAGE 197-206/202/124-126/462-467/76>>>）
- counter-examples·升级环境约束与收尾/FTP 凭据/Thin Client 直改配置（<<<PAGE 203-206/198/75>>>）
