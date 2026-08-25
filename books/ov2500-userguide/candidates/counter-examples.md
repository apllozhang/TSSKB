# counter-examples 候选提取 · OmniVista 2500 NMS 4.9R2 User Guide

来源: source/fulltext.md（页码为原文 <<<PAGE N>>> 标记）

## X1. sFlow 包不能经 EMP 端口发送 <<<PAGE 75, 92>>>
"sFlow packets cannot be sent through the EMP Port. If you want to gather Top N App data from a switch you cannot use the EMP IP when discovering the switch."

## X2. 未定义 FTP 凭据时逐台被询问 <<<PAGE 43>>>
"If you do not define the FTP login names and passwords and you attempt to save, restore, or update configuration files...you will be individually queried for the FTP login name and password of each individual switch"

## X3. PolicyView QoS 执行后不保存则配置丢失 <<<PAGE 44>>>
"once PolicyView QoS has executed, all AOS devices will be left with their running configuration in the Unsaved state. It is important to save the running configuration to the working directory and then the certified directory"

## X4. 未知设备的 sFlow 数据不进报表 <<<PAGE 67>>>
"If the device is not known to OmniVista (or if the Analytics Application is not supported on the device), sFlow information is sent to OmniVista, but the information is not included in those reports."

## X5. "Others" 类别不是数据缺失 <<<PAGE 68>>>
"There may be many others in the profile that are not in the 'top' 10 or 20. The 'Others' category gives you an idea of all of the other applications...with low utilization rates"

## X6. 外部 RADIUS 登录用户无法生成定时报表 <<<PAGE 64>>>
见 principles P13——用外部 RADIUS 认证的管理员只能出实时报表。

## X7. 改交换机 IP 后 Top N App & Clients Profile 失效 <<<PAGE 131>>>
"If you change the IP address of a switch after assigning a 'Top N App & Clients Profile' to the switch, you must re-assign the profile to the switch."

## X8. Statistics 采集静默失败：SNMP 源 IP 与发现 IP 不一致 <<<PAGE 119>>>
见 principles P24——设备侧 SNMP service 源地址与 OV 发现地址不同时收不到数据，无显式报错提示。

## X9. 删除 Statistics/View Profile 连带删除全部历史统计 <<<PAGE 121, 129>>>
"deleting a profile also deletes all statistical data associated with the profile"

## X10. 健康阈值修改最长 1 小时后才可见 <<<PAGE 100>>>
"changes made to health thresholds will not appear until the next polling cycle (up to an hour)"

## X11. AP 802.1X 客户端模式下不支持 untagged WLAN 与 Mesh <<<PAGE 140>>>
见 principles P32。

## X12. "Enable Statistics Automatically On" 选 All 大量加设备有性能风险 <<<PAGE 134>>>
"if you choose 'All' and you add a large number of network devices, there is a risk of performance impact"；新装默认 2000 台、升级默认 0 台——升级环境统计不会自动开启。

## X13. 默认客户端/服务器证书不安全 <<<PAGE 141>>>
"Do not rely on the Default Client Certificate on APs and the Default Server Certificate on UPAM. It is recommended that you install Custom...Certificates"

## X14. Default AP Group / Default BLEGW Group 不可删除，关键字段不可改 <<<PAGE 165, 172>>>
"Both the 'default group' and the 'default BLEGW group' can be edited; however, they cannot be deleted"；且 "You cannot edit the Group Name, Group Description, or Auto Group VLANs fields on the Default AP Group or Default BLEGW Group"。

## X15. 开启 Extended SSID Scale 后低配机型无法入组 <<<PAGE 166>>>
"When enabled (On), only AP models that support up to 14 SSIDs can join the AP Group"；6GHz 每组固定 4 SSID。

## X16. 无扫描射频的 AP 开专用扫描会断所有客户端 <<<PAGE 146>>>
"AP models without scanning radio—regular WLAN services are stopped on the AP and all clients are disconnected"；AP1451 的 6GHz 客户端也会断（可漫游至 2.4/5G）。

## X17. Zigbee 门锁 OUI 不能加进 Auto-Accept 列表 <<<PAGE 148>>>
"Do not enter the MAC OUI for supported door locks. These devices must be 'Manually Accepted' and enabled in the Zigbee Devices Table"

## X18. SNMP trap 目的地址填 OV 自身造成重复告警 <<<PAGE 169>>>
见 principles P43。

## X19. Migrate to Other OV 后 AP 在对端显示为 Unmanaged <<<PAGE 149>>>
"The AP will be released from your OmniVista Server and migrate to the other server, where it will be displayed in the Unmanaged AP Tab"——需对端管理员重新授权配置。

## X20. Root Password Seed 仅 AWOS 4.0.0+ 生效 <<<PAGE 167>>>
"A Root Account Password Seed will not be configured for any APs in the group running a lower AWOS"

## X21. 含不支持 AV 的 AP 的 AP Group 应用签名档案：操作"成功"但部分 AP 未生效 <<<PAGE 209>>>
"If a Signature Profile is applied to an AP Group that contains APs that do not support Application Visibility (AP1201, AP1201H, AP1101), the profile will not be applied to those APs. If none of the APs in the group support Application Visibility, the profile apply operation will still succeed."

## X22. 应用 Signature Profile 会清掉设备上 CLI 配置的 AV 配置 <<<PAGE 209>>>
"any pre-existing Application Visibility configuration on a device is erased and the new profile configuration is used, including any Application Visibility configuration done from the CLI"

## X23. 签名档案向导里配了 Access Role Profile 不会自动下发设备 <<<PAGE 208>>>
"this workflow will not assign the selected Access Role Profile to the devices. You must first assign the Access Role Profile to the devices from Unified Profile Application"

## X24. 删除认证服务器不影响交换机继续使用 <<<PAGE 221-222, 226>>>
"deleting an authentication server...will not cause switches that currently use that [LDAP/RADIUS] Server to cease using it"——会产生"幽灵服务器"状态。

## X25. UPAM RADIUS Shared Secret 改动须同步 NAS Client <<<PAGE 224>>>
"If you change the Shared Secret of the UPAM Radius Server, you also must update Shared Secret of NAS Client on the NAS Clients Screen (UPAM - Authentication - NAS Clients)"

## X26. 组内应用在组里的应用已被应用则 VPN Server / Signature File / Signature Profile 均不可删 <<<PAGE 196, 206, 209>>>
"you cannot delete a Signature File that has been assigned to switches"；"you cannot delete a Signature Profile that has been applied to devices"；Data VPN Server 同理。

## X27. Scheduled Upgrade 会降级高于目标版本的设备 <<<PAGE 296>>>
"The device will be downgraded. A message will inform the user that the device will be downgraded."

## X28. Unsaved 设备被升级计划静默跳过 <<<PAGE 296>>>
"If a device is 'unsaved' the device will not be upgraded. It will be skipped."

## X29. Stellar AP 手工加进 Managed Devices 吞掉第三方 License <<<PAGE 257-258>>>
见 principles P73。

## X30. REST API 轮询凭据错误引发 trap 风暴 <<<PAGE 300>>>
"Incorrect credentials may result in switches periodically generating many authentication failure traps."

## X31. 混选不同软件类型设备时 Set Same Version 只剩 Do Not Upgrade <<<PAGE 293-294>>>
"If you select devices that use different software (e.g., OAW-AP1221 and OS6450), 'Do Not Upgrade' will be your only option."

## X32. IoT 固定端口默认不上报指纹 <<<PAGE 309>>>
"When IoT is enabled on a switch, it is enabled globally on all UNP Ports. However, it is not enabled on fixed ports"——须逐口 CLI 开启。

## X33. AOS 设备上的 Stellar AP 自身出现在 IoT Inventory <<<PAGE 313>>>
"To prevent a Stellar AP from being displayed in the Inventory List, you must disable IoT profiling on the switch port connected to the AP using...device-profile port slot/port admin-state disable"

## X34. Provisioning 模板含禁用命令必失败 <<<PAGE 442>>>
"Certain commands that are handled by the Configuration Manager in AOS cannot be included in a Configuration Template (e.g., user admin password, write memory, configuration apply). If these commands are included...provisioning will fail."

## X35. OV 收不到配置确认回执时谎报成功 <<<PAGE 455>>>
见 principles P131——连接丢失/SSH 超时场景下 Results 显示 Succeeded 但配置可能未应用。

## X36. Certified 目录运行的交换机不能 Enforce Golden Config <<<PAGE 452>>>
"You cannot enforce the Golden Configuration on a switch running from the Certified Directory."

## X37. 从 Certified 目录 provision 的配置是临时的 <<<PAGE 434, 435>>>
"the configuration is temporary and will not be persisted. The switch will lose its configuration if it reboots"——须 reload working 后 Force Provision。

## X38. Quarantine 对无线客户端不进 Banned 而进 Client Blocklist <<<PAGE 460>>>
见 principles P132；旧版本（4.9R1 前）Banned 的无线客户端不会自动迁移。

## X39. 重复禁用同端口产生空 MAC 双条目，Release Banned 不会自动恢复端口 <<<PAGE 465>>>
"when you use the Banned Screen to release a MAC address, the port will not be re-enabled. The Network Administrator will have to manually re-enable the port by releasing the port from the Disabled Ports List"；端口要等所有引发封禁的条目都释放才启用。

## X40. QMR 与 QoS inner VLAN/802.1p 策略互斥 <<<PAGE 459>>>
"Configuring QMR and QoS inner VLAN or inner 802.1p policies is mutually exclusive...also true with QMR and VLAN Stacking services."

## X41. 备份文件拷贝到其他机器可能搞瘫网络 <<<PAGE 493>>>
"The saved files contain binary configuration information, including the IP address/MAC address of the source machine, and using these files on another machine could bring the network down."

## X42. Image 文件不真正备份，Restore 前须先导镜像 <<<PAGE 489, 490>>>
"Image files will not be FTPed from a device. OmniVista will only record file version(s). Therefore, before Restore is to proceed, the required image file set must be stored in the Upgrade Image Repository."

## X43. FTP 5 分钟超时导致大镜像升级失败 <<<PAGE 497>>>
"The switch FTP timeout default is 5 minutes...increase the FTP timeout in switches you are upgrading...session ftp timeout <time>"

## X44. Image 与 U-Boot 升级顺序不能颠倒 <<<PAGE 497>>>
"you must complete the image file upgrade before upgrading the U-Boot and Miniboot files."

## X45. Periodic 报表不能手动生成；外部 RADIUS 用户不能排程 <<<PAGE 484-486>>>
"You cannot manually generate a report configured with a 'Periodic' schedule"；"only users authenticated through the Local OmniVista Authentication Server can schedule reports."

## X46. 首次建报表配置生成的是空白报表 <<<PAGE 485>>>
"a blank report is automatically generated...because you have not yet associated the report with an application"

## X47. 混合地图备份漏掉 Stellar AP <<<PAGE 488>>>
"if a map contains AOS Devices and Stellar APs, the Stellar APs will not be backed up. Stellar APs can only be backed up by AP Group."

<!-- APPEND -->
