# counter-examples 候选 — DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration

## CE1. eBuy 购买后订阅最长延迟 24 小时
- 页码：<<<PAGE 26>>><<<PAGE 98>>>
- 原文摘录："Note: The licenses purchased in eBuy can take up to 24h before coming up in Subscription Manager."
- 陷阱：下单后立刻在 Subscription Manager 找不到 License 并非故障。

## CE2. 一个邮箱只能绑定一个 MSP 门户
- 页码：<<<PAGE 49>>>
- 原文摘录："In OVC 10.4.3, a unique account (linked to a mail address) can only be assigned to one MSP portal. If a user want access to multiple MSP portals, he must use different mail addresses."
- 陷阱：需多 MSP 访问时用子地址（MyMail+sub@MyCompany.com）；激活链接仍发原始邮箱。

## CE3. 组织脱离 MSP 后 MSP 用户立即失去访问
- 页码：<<<PAGE 59>>>
- 原文摘录："Be aware that all users within the MSP will no longer have access to that organization once removed from the MSP."

## CE4. 设备序列号不能同时存在于 OVC4 与 OVC（迁移）
- 页码：<<<PAGE 70>>>
- 原文摘录："The serial number of a network device cannot be declared in both OmniVista CIRRUS 4 and OmniVista Cirrus. Make sure to remove all your equipment first."
- 陷阱：旧平台未删设备直接在新平台 onboard 会冲突。

## CE5. OVC4→OVC 无自动迁移工具
- 页码：<<<PAGE 69>>>
- 原文摘录："In the current version, there are no tools for migrating from OVC4 to OVC."
- 陷阱：需手工重建 AP Group/Provisioning/SSID/Access Policy 并核对配置。

## CE6. Terra CPU 指令集陷阱（AVX/AVX2 与 EVC 基线）
- 页码：<<<PAGE 75>>>
- 原文摘录："CPU must support AVX/AVX2 Instructions – in a vCenter cluster configuration, it is required to enable EVC mode with the CPU baseline set to 'Ice Lake' … As a minimum requirement, the 'Broadwell' baseline may be used."
- 陷阱：vCenter 集群 EVC 基线低于 Broadwell 会导致部署失败。

## CE7. Terra 部署失败时的取证路径
- 页码：<<<PAGE 89>>>
- 原文摘录："In the Install menu on the left, check the status of the deployment: Success / Failure / In Progress. If the deployment fails, click on the 'Download the logs' button to get the installation logs."

## CE8. Terra License "Activate subscription" 即开始倒计时
- 页码：<<<PAGE 101>>>
- 原文摘录："Enabling the option 'Activate subscription' will start the countdown of your license."
- 陷阱：过早激活会白白消耗订阅期。

## CE9. 曾被 Cirrus 管理的 AP 接入 Terra 前必须清除证书
- 页码：<<<PAGE 141>>>
- 原文摘录："Optional - If the Stellar AP is/was managed by an OmniVista Cirrus, remove the certificates: > rm -rf /.ocloud/callhome_hash.json /.ocloud/certificateFile.cert /.ocloud/cloudCaChain.pem /.ocloud/privateKey.key /.ocloud/csr.csr /.ocloud/publicKey.key ./privateKey.key.dec"
- 陷阱：残留云证书会导致激活异常；还需 DHCP option 43 指向 activation.myovterra.com 并 `firstboot`+`reboot`。

## CE10. 交换机切 Terra 需改 cloudagent.cfg 激活 URL 并删证书
- 页码：<<<PAGE 161>>>
- 原文摘录："cd switch/cloud > rm -f client.crt cloudCAchain.pem csr.crt private.key public.key … In the directory /working, edit the file cloudagent.cfg … Modify the first line 'Activation Server URL: activation.myovterra.com'"

## CE11. 激活失败状态族与排查入口
- 页码：<<<PAGE 146>>><<<PAGE 147>>>
- 原文摘录："Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required"；"Provisioning Failed: Device was unable to process the provisioning configuration … or OmniVista Cirrus 10 was unable to discover the device"；"Unsupported Device Model: OmniVista Cirrus does not support the device."

## CE12. VPN profile 变更后设备需恢复出厂
- 页码：<<<PAGE 147>>>
- 原文摘录："Factory Reset required: The VPN profile was changed/updated. A Factory Reset is required on the device."

## CE13. 不支持的 AP 型号（AP1101 / AP1201L/H/HL）
- 页码：<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>
- 原文摘录："All Stellar models supported, except: AP1101, AP1201L/H/HL"；AP1101 也不兼容 RAP 特性（p421）。

## CE14. DSPSK 不支持 AUTO_WPA_WPA2 加密
- 页码：<<<PAGE 232>>>
- 原文摘录："Encryption AUTO_WPA_WPA2 is NOT supported • PSK/PassPhrase: only active with 'Prefer Device Specific PSK' • Device Specific PSK: Enabled."

## CE15. Fast Roaming / OKC 的加密限制
- 页码：<<<PAGE 395>>><<<PAGE 402>>>
- 原文摘录："OKC can be enabled with WPA2/WPA3 Enterprise only • 802.11r (Fast Roaming) can be enabled with WPA2/WPA3 encryption only (Personal or Enterprise) • If Fast Roaming is not enabled, then standard Roaming is used."

## CE16. 地理相邻但互相看不见的 AP 无法共享上下文
- 页码：<<<PAGE 415>>>
- 原文摘录："In some cases, Stellar APs are geographical neighbors but can't see each other (i.e: radio waves blocked by corridor with right angles,…). Client context can't be shared. No roaming. Solution: On both AP, add statically the neighbor Stellar AP."
- 陷阱：需在 AP Registration > Access Point 视图手工加 Neighbor AP，且两端都要加。

## CE17. Roaming RSSI 阈值设错的两类后果
- 页码：<<<PAGE 416>>>
- 原文摘录："If the RSSI threshold is too low, the client remains on a low signal strength site, even with a stronger site nearby. If the RSSI threshold is too high, the client roams too much that could result to packet loss."

## CE18. WIPS Client Blocklist 的局限
- 页码：<<<PAGE 387>>>
- 原文摘录："The attacker source MAC can be anything (an AP mac, a BSSID mac, a wireless NIC card mac..) • Blocklisting the attacker source MAC is only relevant when the source MAC is an actual wireless client."
- 陷阱：默认禁用；拉黑 AP/BSSID MAC 无意义。

## CE19. 扫描参数的安全/性能权衡
- 页码：<<<PAGE 373>>><<<PAGE 376>>>
- 原文摘录："During scanning wireless clients are impacted – no 802.11 data • Scanning is required for WIPS"；"Higher scanning interval or lower scanning duration means intrusions are less likely being detected but client performance will be better"。

## CE20. RSSI 差（Bad 区间）不建议音视频应用
- 页码：<<<PAGE 379>>>
- 原文摘录："Bad — Not recommended for Video or Audio applications；OK – not bad；Desired and recommended"（RSSI 对照表分档）。

## CE21. Bridge 模式 VLAN tagging 兼容性
- 页码：<<<PAGE 437>>>
- 原文摘录："* AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge."

## CE22. Heat Map 至少需要 3 个 AP
- 页码：<<<PAGE 337>>>
- 原文摘录："* Minimum of 3 Stellar APs required to generate a Heat Map."
