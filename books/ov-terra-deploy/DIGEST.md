# OmniVista Cirrus/Terra 部署与配置 · 知识精华（DIGEST）

来源：DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration。本文是全书 176 条已验证候选的浓缩串讲，所有论断均带原书页码。

## 一、知识地图

全书的知识可以摊成一条交付主线加三条支线：

**主线（从零到可用）**：平台选型 → 账号与组织 → License/Trial → 设备 Onboarding（AP/交换机）→ 业务下发（无线/有线）→ 运维监控。对应十个技能单元：

1. **平台选型与前置条件**（platform-selection-prereqs）——Cirrus vs Terra、容量、端口、版本门槛
2. **账号与组织体系**（account-org-system）——Partner/Customer/MSP 三级账号、组织、用户权限
3. **Terra 3-VM 部署**（terra-3vm-deployment）——OVA、控制台、WebAdmin、Build、DNS
4. **License 与 Trial 转正**（license-and-trial）——eBuy、Subscription Manager、导入订阅
5. **Stellar AP Onboarding**（ap-onboarding）——宣告、激活状态机、迁移
6. **OmniSwitch Onboarding**（switch-onboarding）——cloud-agent、证书、激活 URL
7. **有线业务配置下发**（wired-switch-config）——CLI 模板、VLAN/IP Interface、MAC 认证、Golden Config
8. **无线业务下发**（wireless-service-delivery）——站点楼层、AP Group、SSID、Guest/UPAM
9. **射频与漫游优化**（rf-roaming-optimization）——DRM、负载均衡、WIPS、漫游、Mesh/RAP
10. **监控运维**（monitoring-operations）——QoE、Heat Map、升级、备份、排障

**三条支线**：商业链路（账号→Trial→eBuy→订阅→导入）、平台切换链路（OVC4→OVC、Cirrus→Terra 的证书与 URL 清理）、无线体验链路（RF 参数→漫游→QoE 度量闭环）。

## 二、十个最重要知识点串讲

### 1. Cirrus 与 Terra 的本质分工
Cirrus 是 SaaS、"Zero Deployment"（<<<PAGE 5>>>）；Terra 是 On-Premises、客户自托管 3-VM 集群、单租户（<<<PAGE 13>>><<<PAGE 14>>>）。容量差一个量级：Cirrus 最多 12000 台（10000 AP + 2000 交换机），Terra 最多 2000 台（1600 AP + 400 交换机）（<<<PAGE 6>>><<<PAGE 14>>>）。但两者功能对等、商业结构一致、UI 一致（<<<PAGE 17>>>），所以技能跨平台通用，只是门槛参数不同：AP 最低版本 Cirrus 要 AWOS 4.0.6 GA、Terra 要 AWOS 4.0.7.14；交换机分别要 AOS 8.9R1 与 8.9.82R01（<<<PAGE 9>>><<<PAGE 18>>>）。AP1101、AP1201L/H/HL 两边都不支持（<<<PAGE 140>>>）。

### 2. 防火墙端口是激活的隐形门槛
Cirrus 场景 AP→云必须开 9093/30123/30124/30125 加出向 443/80/123/53；Terra 只需出向 443/80/123/53（<<<PAGE 9>>><<<PAGE 18>>><<<PAGE 140>>>）。DHCP 需标准 options 1,3,6,28,42,43（用代理加 129-133,138），至少 1 个 NTP（<<<PAGE 9>>>）。设备"宣告了没反应"先查这张清单。

### 3. 三级账号体系与单邮箱陷阱
Partner 账号创建即 MSP 级用户（可建组织、邀用户），Customer 账号不挂 MSP（<<<PAGE 37>>><<<PAGE 50>>>）；组织 = 企业或实体、含多站点（<<<PAGE 50>>>）。权限三档 Admin/Viewer/Limited（<<<PAGE 50>>>）。最大的坑：OVC 10.4.3 一个邮箱只能绑一个 MSP 门户，多 MSP 要用子地址 MyMail+sub@MyCompany.com，且激活链接仍发原始邮箱（<<<PAGE 49>>>）。组织脱离 MSP 后该 MSP 全部用户立即失访（<<<PAGE 59>>>）。

### 4. License 三段链路与两个时间陷阱
eBuy 下单 → Subscription Manager 建订阅 → OV 实例导入（<<<PAGE 24>>>）。陷阱一：eBuy 下单后订阅最长 24 小时才出现在 Subscription Manager（<<<PAGE 26>>>）。陷阱二：勾选 "Activate subscription" 即开始订阅倒计时，不要提前激活（<<<PAGE 101>>>）。Terra 导入比 Cirrus 多一步：需从 Admin Center 取 OmniVista ID 并下载 license 文件 (.json)，与 Subscription ID + Activation Code 三件套一起导入（<<<PAGE 100>>><<<PAGE 114>>>）。Trial 转正走 License Management > import licenses > CAPEX Subscription，upgrade 后确认 paid mode（<<<PAGE 62>>>~<<<PAGE 67>>>）。SKU 编码读法：OVCX-68-BAS-3Y = 等级（BAS/BIZ/PRM）+ 年限（1Y/3Y/5Y，Terra 另有 7Y）+ 品类（APL 为低端 AP）（<<<PAGE 23>>><<<PAGE 95>>>）。

### 5. Terra 部署：硬件红线与四域名 DNS
3 台 VM 组成 Kubernetes 集群（Active-Active L3 高可用，含 VPN Server/Load balancer、Kafka/MQTT）（<<<PAGE 17>>>）。硬件：ESXi 8+、每台 8 vCPU@3GHz / 32GB RAM / SSD / System 200GB / Data 3TB；CPU 必须支持 AVX/AVX2，vCenter 集群 EVC 基线推荐 Ice Lake、最低 Broadwell——低于 Broadwell 必失败（<<<PAGE 75>>>）。流程：OVA 部署 → 控制台配 hostname/IP/DNS（必须能解析 myovterra.myovcloud.com）→ WebAdmin `<Node_IP>:3000` 建 admin、填 General Info 与集群节点、定义 Main/VPN/Captive Portal/Radius 四个 IP、配 SMTP → 上传 build (.7z) → DNS 配四域名（activation/as、vpn、images、myovterra.myovcloud.com，<<<PAGE 90>>>）→ 首登。失败时 Install 菜单点 Download the logs 取证（<<<PAGE 89>>>）。

### 6. 激活状态机是排障的地图
设备宣告后的正常链：Registered → Obtaining Certificate → Upgrade → Assigned → VPN Configuring → Connected to OV → OV Managed（终态，最长约 5 分钟）（<<<PAGE 146>>><<<PAGE 147>>>）。原理：平台为设备签发数字证书，证书用于建设备与平台间的安全 VPN 通道（<<<PAGE 147>>>）。失败状态族：Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required；VPN profile 变更过就必须恢复出厂（<<<PAGE 147>>>）。推论：残留旧证书是激活失败头号根源——曾被 Cirrus 管的 AP 进 Terra 前要 `rm -rf /.ocloud/` 下证书文件（<<<PAGE 141>>>）；交换机切 Terra 要删 switch/cloud 下五类证书文件并把 /working/cloudagent.cfg 首行改成 activation.myovterra.com（<<<PAGE 161>>>）。

### 7. 交换机侧的 cloud-agent 机制
cloud-agent 是交换机与平台对接的代理：`show cloud-agent status` 看 Activation Server State（期望 completeOK）与 Device State（期望 DeviceManaged）；`cloud-agent admin-state disable force` 重建 VPN；发现间隔默认 30 分钟（Call Home），等不及就重启进程或设备（<<<PAGE 170>>><<<PAGE 171>>><<<PAGE 172>>>）。

### 8. 无线配置模型：AP Group 承载一切
同 AP Group 的 AP 共享配置（SSID/RF Profile/模板），与物理网络无关，每组最多 20000 AP、可混型号（<<<PAGE 152>>>）。Provisioning Configuration 必填 Name/Site/RF Profile/Timezone，另含 SSH、SNMP、IoT Radio、Syslog（最多4）等（<<<PAGE 154>>>）。SSID 是向导式：Usage 预设（Guest/Employee/BYOD/Enterprise）决定参数走向（<<<PAGE 214>>><<<PAGE 218>>>）；认证安全等级从 Open+CP → MAC → PSK → 802.1X 递增（<<<PAGE 215>>>）。PSK 精细化：DSPSK 按 MAC 发专属 passphrase（不支持 AUTO_WPA_WPA2，<<<PAGE 232>>>）、PPSK 多密码各绑 ARP、Dynamic PGPSK 条目直绑 VLAN+ARP（<<<PAGE 231>>><<<PAGE 233>>><<<PAGE 234>>>）。访客体系：UPAM 内置 RADIUS + MAC 认证服务器（<<<PAGE 240>>>），Guest Tunneling 按 ARP 建 L2 GRE 隧道隔离访客流量（<<<PAGE 256>>>），Registration Profile 管时间/数据配额及耗尽处理（<<<PAGE 283>>>）。带宽判定顺序：ACL 规则 → ARP → SSID 级（<<<PAGE 268>>><<<PAGE 269>>>）。

### 9. 射频与漫游：分布式决策 + 参数红线
DRM 全分布式：AP 空口发现邻居、LAN 共享 RF 上下文、自主决策，不依赖 AP Group/管理 VLAN（<<<PAGE 364>>>）。关键参数与推荐值：Band Steering 门限 2.4G=5 / 5G=10（<<<PAGE 370>>>）；信道利用率 1 分钟均值超 70% 判 Overloaded（<<<PAGE 371>>>）；扫描默认 20s/50ms，扫描期间客户端无数据、WIPS 依赖扫描（<<<PAGE 373>>>）；Roaming RSSI 2.4G=10 / 5G=15，阈值过低客户端滞留弱信号、过高频繁漫游丢包（<<<PAGE 416>>>）。漫游判定看 VLAN：home/foreign VLAN 一致走 L2，不一致走 L3（L2 GRE 隧道，默认禁用）（<<<PAGE 394>>><<<PAGE 400>>>）。OKC 仅 Enterprise、802.11r 仅 WPA2/WPA3（<<<PAGE 402>>>）。特殊场景：地理相邻但互相看不见的 AP 要两端手工互加 Neighbor AP（<<<PAGE 415>>>）；Mesh 最多 16 AP/4 跳，最佳实践 5GHz、信道>100（<<<PAGE 439>>>）；RAP 需 OV Cirrus + ALE VPN Server VM + OV2500 三块配置、五步开通（<<<PAGE 423>>>~<<<PAGE 432>>>）。

### 10. 运维闭环：度量、变更、取证
QoE Analytics 量化连接/漫游时间（失败原因 Association/Authorization/DHCP/Portal）、RSSI（OV 平均值 vs AP 瞬时值，Bad 区间别跑音视频，<<<PAGE 379>>>）、信道利用率、uptime（<<<PAGE 296>>>）。变更：Scheduled Upgrade 按 Site/AP Group/单 AP 分窗分版本（<<<PAGE 356>>>）；备份支持即时与计划（scope 到 switch/site/floor，<<<PAGE 355>>>）；Golden Configuration 周期审计配置偏离（<<<PAGE 195>>><<<PAGE 351>>>）。取证：Collect support info，AP 下载 tar.gz 快照、交换机打包 Swlog/Cfg/Tech-support（<<<PAGE 358>>><<<PAGE 359>>>）。Heat Map 注意最少 3 个 AP 才能生成（<<<PAGE 337>>>）。

## 三、交付检查清单（浓缩版）

- [ ] 选型：规模 >2000 台只能 Cirrus；防火墙端口/版本门槛核对
- [ ] 账号：区域 URL（eu/us）→ Partner/Customer → 组织（强密码策略 + 时区）
- [ ] License：Trial 申请（ALE 联系人必填）→ eBuy 下单（等 24h）→ 建订阅 → 导入（Terra 带 .json 文件）
- [ ] Terra：EVC 基线 ≥ Broadwell → 3 节点 OVA → WebAdmin 首设 → build → 四域名 DNS
- [ ] Onboarding：旧平台删设备（序列号唯一）→ 删证书 + 改激活 URL → 宣告 → 等 OV Managed
- [ ] 业务：站点楼层 → AP Group + Provisioning（四必填）→ SSID（按 Usage）→ 有线模板/VLAN
- [ ] 运维：QoE 基线 → 升级窗口 → 备份计划 → Golden Config 审计
