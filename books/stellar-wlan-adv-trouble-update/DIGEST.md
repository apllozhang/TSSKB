# DIGEST · OmniAccess Stellar WLAN Advanced Troubleshooting and Update（DT00XTE378EN）

> 不读全书、只看精华。488 页售后 Experienced 教材，拆成 4 个可执行 skill；排障方法论不再重复，去 T478 查。

## 一、一页看懂这本书

这本教材是两本书的合体：**排障篇（p3-133）与 T478 完全相同**——方法论、工具箱、基础/无线/客户端/网络排障、勘测、TKC，一个字没多，排障问题直接去查 T478 的蒸馏成果即可；**真正的增量在 Features Update 篇（p134-487）**：新硬件（Wi-Fi 7 AP 家族）、新特性（AD 对接、WCF、BYOD、RAP）、远程实验室、以及随 AWOS/Cirrus 新版本演进的实操 Lab。一句话定位：**前 1/3 教怎么修（去 T478 查），后 2/3 教新版本有什么、怎么配（本册四个 skill 的地盘）**。存量网络升级评估、上云盘点、新特性对比，价值都在后 2/3。

## 二、Enterprise 上线与 SSID 策略进阶要点

**设备进网管（Enterprise 模式）是四层递进**（p213-239）：网络层 Backbone VLAN 互 ping → 交换机侧 SNMPv3（`snmpuserv3 ... sha+des`）+ OV2500 Discovery Profile 参数一致 → AP 上线链路（DHCP relay 的 Offer 带 **option 138 = OV2500 地址**，这是 ALE 私有引导，p224-239）→ Unmanaged 刹 Trust、入 AP Group。记住一条铁律：**OV2500 只认 AP Group，不进组的 AP 一切配置不生效**。

国家码是隐形地雷（p231）：OV2500 首次 AP Registration 选的国家码决定信道与功率，与 AP 硬件销售区域不符则设备完好却拒绝工作——跨境调拨和二手设备先查标签。

SSID 侧（p243-338）：向导选 Usage 模板定骨架（Guest/Employee BYOD/Enterprise for Employees/Protected），认证源三级可切（UPAM 本地库 → AD，端口 389 → 外部 RADIUS）。三个高频坑：

- **策略只在认证瞬间应用**（p338）：推完配置必须让客户端断开重连，否则误判"配置有错"。
- **UPAM 系统级 NAS 项 "All Managed Devices" 共享密钥固定 123456**（p307）——802.1X 排障第一怀疑点。
- **改 Access Role Profile 必须点 Apply to Devices**，不点只改在服务器本地。

限速走四层判定（p284）：DPI 应用规则 → ACL → 用户级 Access Role → SSID 共享，从细到粗选入口。

## 三、RAP 与云运维三件套

**RAP 双模式**（p384-390）：Premium 只靠 Cirrus 云管、四步上线；Freemium 是"Cirrus 引路 + 本地 OV2500"五步双隧道——管理 VPN（端口 6550）连 OV2500，数据 VPN 走 L2GRE（端口 6551）承载客户端流量，SSID 的 Default VLAN 选 **Use Tunnel 且 Tunnel ID 必须 0**。两种模式都要公司侧部署 ALE VPN Server 虚机，Freemium 的要三块网卡。**AP1101 不支持 RAP**，远程站点选型避开。

**备份-恢复-升级**（p429-430）：Save All 存 Running，AP 只能按 AP Group 备份（按地图备份不含 AP，p19）。两个反直觉结论：恢复后 Result 显示 SUCCESS 但配置只落 WORKING/CERTIFIED，**必须 `reload from working no rollback-timeout`** 才生效（约 3 分钟）；**Stellar AP 根本不能 Restore**——配置来自 AP Group 下推，"恢复"AP 的实际路径是修 AP Group 或恢复出厂重新入组。

**监控告警**：Trap Responder 按严重级别（如 Critical）发邮件，Agent 粒度可到 AP Group，主题支持 `$TrapAgent$` 变量；配 SMTP 后人为重启一台 AP 验证送达。规划侧用 Heat Map（5 米标尺 + WallsHeavy 描墙看真实覆盖）和 Floor Plan Auto Deployment 自动布点。

## 四、新硬件速览

**Wi-Fi 7 双雄**（p152-153）：AP1511 入门——三射频 2x2，6GHz EHT320 5.76Gbps，32 SSID/512 客户端，PoE ≤35W；AP1521 中档——同射频但上联 1/2.5/5/**10GE** multi-gig、802.3bt ≤**60W**。要 10G 上联或大供电选 1521，成本敏感选 1511。

**规模红线**（p169-176）：Express 自组集群 ≤255 AP（单交换机 32、单堆叠 64，堆叠内至少 2 台 AP123X/13xx/14xx/15X1 当 PVM/SVM）；Enterprise ≤4000 AP。管理面要 IPv6 只能 Express——Enterprise 下 AP 管理走 IPv4。Mesh 四条硬限制（p399-401）：≤4 跳、单跳 ≤5 台、全网 ≤16 台、每台 ≤5 个客户端 SSID。

**dBm 换算**（p186, p365）：**dBm = RSSI − 96**。OV2500 客户端列表显示 dBm，AP RF 设置用 RSSI，两侧比较前必须统一单位——这是 RF 调优第一大坑（-18dBm = RSSI 78，想挡住它阈值得设 ≥78）。

## 五、升级与迁移陷阱清单

1. 恢复成功 ≠ 生效，必跟 reload from working（p429）。
2. 固件包是 WinZip 自解压格式，**切勿手动解压**，OV 导入自动解包。
3. 上 Cirrus 前查版本底线：AOS 8.4.1.R03+ / 6.7.2.R03+ / 5.1R1+（按交换机型号），AWOS 3.0.2+（全部 AP）。
4. Freemium vs Premium 由账号组合决定架构：Freemium 必须配本地 OV2500，别按"全云"规划。
5. WPA3 CNSA 192 位开启后 WPA2 终端被拒；升级 SSID 安全级别时回查漫游特性（OKC 仅 WPA2-Enterprise，11r 在 WPA2 下推荐）。
6. WCF/DPI 硬件排除 AP1101 与 AP1201H，混装区域策略只部分生效；WCF Not in service 先查 OV2500 虚机 DNS。
7. 评估许可：文件导入与密钥手填二选一，密钥只贴键值不贴整行。
8. Band Steering 默认关闭是设计决策：5G 有覆盖洞时开了反而有害。

## 六、学习路径

1. `stellar-enterprise-onboarding`——设备进网管：交换机发现、AP 云注册（option 138）、AP Group 纳管。
2. `stellar-ssid-policy-advanced`——空口业务：802.1X/AD/访客门户/WCF/BYOD 与限速四层判定。
3. `stellar-rap-backup-upgrade-ops`——远程 AP 与云运维：双模式、备份恢复升级、监控告警。
4. `stellar-wifi7-hardware-rf-quickref`——选型与调优：Wi-Fi 7 规格、规模红线、RF 阈值、Mesh/Bridge。

顺序即依赖：先纳管（1）→ 再配业务（2）→ 需要远程/云/变更时用（3）→ 体验与覆盖问题查（4）。**排障方法论与分层工具箱不在本册——那是 T478 的地盘，直接引用。**

---
*由 cangjie-skill 流水线从 DT00XTE378EN 蒸馏生成*
