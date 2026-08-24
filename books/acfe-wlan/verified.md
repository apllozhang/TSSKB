# verified.md · ACFE WLAN Basic Deployment With OmniVista Ed04 · 三重验证通过条目（流水线阶段 1.5）

## 汇总

- **通过 206 / 淘汰 5**（候选合计 211；glossary 免验计入通过）
  | 类型 | 通过 | 淘汰 |
  |---|---|---|
  | frameworks | 26 | 2 |
  | principles | 62 | 3 |
  | cases | 23 | 0 |
  | counter-examples | 40 | 0 |
  | glossary | 55（免验） | 0 |

- **V1 抽查情况**：frameworks 28/28、principles 29/65、cases 12/23、counter-examples 23/40（均满足"每 5 条至少验 2 条"），另对 30+ 处特征常数（256 VLAN 池、UP=100kB/s、KEEP THIS CONF FILE、Add/Del Message discarded、外置天线型号尾数"2"等）做全文 grep 复核。**全部命中 fulltext.md 对应页，未发现任何编造或错位引用**；唯一非 fulltext 来源 ce40 如实标注引自 BOOK_OVERVIEW.md 且原文存在。
- **淘汰原因集中**：5 条全部倒在 V3（网工通识：Wi-Fi 代际速率表、认证信任梯度、信号衰减材质/四类原因清单），其书内独特部分均已被其他条目覆盖（p33/p11/f21/ce39/c22）。

---

## frameworks（26 通过）

- f01 | AP 网络部署模式自动选择决策树（Express / Enterprise / Cloud） | option 138→Cirrus 序列号登记→Express 三级判定逐字命中 p100，开局模式规划的唯一权威依据
- f02 | Stellar AP 三平面流量分析模型 | 管理 untagged/数据 tagged 纯二层无隧道命中 p266/269，端口规划与"流量走哪条路"排障框架
- f03 | AP 接入网络前置条件清单 | PoE trunk/VLAN/DHCP(option 138)/DNS/路由五项清单命中 p25，上线失败逐项核对可用
- f04 | Express 集群 AP Group 与 PVM/SVM 选举机制 | 选举两级判据+组上限 255 命中 p105，换 PVM/扩容场景可预测行为
- f05 | Express 开箱默认行为与首次 Web 管理接入 | mywifi-ABCD/192.168.1.254/:8080 命中 p101，无网管环境首次接触 AP 的标准路径
- f06 | AP 云管 Onboarding 方法选择（手动 VLAN 分类 vs UNP 自动分类） | 两方法与 UNP 不做 802.1X 的安全权衡命中 p284-291，交换机侧准备选型框架
- f07 | 设备云上线激活状态机与失败状态对照表 | 中间态约 5 分钟+六种失败态命中 p261，云上线卡住的定位速查表
- f08 | 设备不被云管发现的分层排障流程 | L2→L3→激活日志三层链命中 p252，AP 版命令扩展于 p304-306，全书复用的排障骨架
- f10 | Cirrus SSID 创建三段式向导流程 | 设置→网络指派→计划与 VLAN 映射命中 p312，所有 SSID 类型复用的 GUI 流程
- f11 | PSK 密钥体系四级选型 | 全局/DSPSK/PPSK/动态组 PSK 逐级演进命中 p326-330，按运维粒度选型的决策框架
- f12 | UPAM Guest 访问策略工作流 | 访客 SSID 六步开通命中 p360，门户认证+后置限权的完整工作流
- f13 | UPAM BYOD 访问策略工作流 | 预认证 Guest VLAN→认证后 Employee VLAN 切换命中 p365/391-393，BYOD 准入核心流程
- f14 | Unified Policy 条件—动作—绑定配置流程 | "先策略后绑定"固定顺序命中 p413-414，顺序错了策略不生效
- f15 | 三层带宽控制模型与执行优先级 | SSID/ARP/策略三层合同及"策略>角色>SSID"优先序命中 p408-409，套餐设计分层模型
- f16 | RF Profile 创建—绑定—验证—回退流程 | 换绑生效与回退路径命中 p463，含 Band Steering 默认关的原因与 Exclude MAC OUI 豁免
- f17 | RF 优化参数推荐基线表 | 阈值 10/25、扫描默认、Auto 信道功率等官方基线命中 p451，可直接照抄的调优起点
- f18 | 漫游模式判定决策表与快速漫游配置指南 | L2/L3 判定+OKC/802.11r 加密前提+粘客户端阈值组合命中 p489-492
- f19 | WIPS 三分类框架与 Rogue 判定策略矩阵 | Interfering/Rogue/Friendly 分类与遏制默认开命中 p514-515，安全调参的风险框架
- f20 | Wi-Fi 勘测类型选型矩阵 | 三类型测量差异与项目阶段映射命中 p529-530 并衔接 RSSI 判读标尺，勘测选型可直接套用
- f21 | 现场无线排障三步法 | Step0 问题定义→平面图→五项观察→纠正措施命中 p537-540，性能投诉的结构化处理 SOP
- f23 | 客户端接入故障排障命令链 | 802.1X 与门户两套 AP 侧 CLI 链命中 p343-347/385-388，客户端连不上时的速查手册
- f24 | RAP 远程接入点五步上线流程 | 预配置+五步时序+管理面三段配置命中 p499/508，远程部署完整流程框架
- f25 | Cirrus 组织清理与配置回退流程 | 云管无一键恢复、按依赖逆序拆除命中 p544-547，换设备/搬场/重配的拆除 SOP
- f26 | OmniVista Cirrus 许可订阅生命周期流程 | eBuy→订阅→导入→验证横跨三系统命中 p173-216，含 24h 延迟等排期常数
- f27 | 访客账号配额治理框架 | Registration Profile/Service Level(≤5)/配额耗尽处理三层对象命中 p427-431，访客运营模型
- f28 | Express 模式员工与访客 SSID 创建流程 | 内嵌门户三选一认证+AP 内置 DHCP 三步命中 p147-157，SMB 无网管开局全套

## principles（62 通过）

- p01 | 部署模式判定规则：DHCP option 138 决定模式 | 判据命中 p17/p100，开局排障第一查项
- p02 | Express 模式出厂默认值 | mywifi-ABCD/192.168.1.254/8080 三常数命中 p101，首次登录必用
- p03 | AP Group 出厂成组规则 | Group ID 100+VLAN 1 自动同组命中 p104，解释开箱即成组行为
- p04 | PVM/SVM 选举规则 | 先比最高型号再比最高 MAC、255 上限命中 p11，预测谁是主管理器
- p05 | Express 集群规模与弹性建议 | 255/64/32/64 常数命中 p13，Express 扩容的容量依据
- p06 | 模式切换规则：改模式即丢配置 | "No configuration migration"命中 p18，迁移项目的关键风险边界
- p07 | 三平面标签规则 | 管理恒 untagged、数据恒 tagged 且纯 L2 命中 p21/p24，端口规划根基规则
- p08 | 开局网络拓扑检查清单 | PoE trunk/DHCP/DNS/路由逐项命中 p25，可勾选的开局核查单
- p09 | 管理平台规模上限 | OV2500 4000AP/Cirrus 12000 设备/组 2000AP 命中 p164/p27，选型测算常数
- p11 | AP 型号 PoE 供电等级与降级规则 | 各型号 af/at/bt 需求与降级后果、SSID/客户端容量命中 p44-57，供电选型表
- p12 | BLE 信标配置规则 | 按组配置/默认关/默认 iBeacon/UUID+Major/Minor 命中 p278，IoT 定位配置规则
- p13 | ISC-DHCP 识别 Stellar AP 与自定义 option 138 写法 | HAP. 类匹配+option ovwma 声明命中 p33，Linux DHCP 服务器落地写法
- p14 | AP 恢复出厂与默认控制台凭据 | Reset 10 秒与 support/aos2016、firstboot/reboot 命中 p119/p304
- p15 | OmniSwitch 出厂默认 | 仅控制台可管、admin/switch、PoE 默认开、show lanpower 验证命中 p110-122
- p16 | AP 接入端口 VLAN 分配规则 | 管理 untagged/SSID tagged 命令序列命中 p123，AP 端口配置标准模板
- p17 | 培训实验网 IP/DHCP 规划常数 | VLAN10/20/30 与 .70-.79 池命中 p79，R-Lab 全部验证步骤的判定基准
- p18 | Express 模式员工/访客 SSID 认证模型 | 密码或 802.1X 两方式+访客 Open+门户命中 p134/138
- p19 | 每 SSID 自动 VLAN 分配与 AP 内置服务 | SSID↔VLAN 映射与内置 DHCP/DNS/NAT/QoS 模板命中 p140-142
- p20 | 内置 Captive Portal 三种认证模式 | 账号/接入码/条款三选一+大小写敏感命中 p151，无网管访客管理规则
- p21 | AP 内置 DHCP 服务器：先建 Pool 再 Bind Network | 建池五字段+必须 Bind 才生效命中 p155，含 40 地址=40 并发常数
- p22 | OV Cirrus 网络前置条件清单 | 防火墙 9093/30123-25 入+443/80/123/53 出、DHCP options、NTP 命中 p167
- p23 | Cirrus License 编码规则 | OVCX-级别-年限-类别解析规则命中 p172，下单编码速查
- p24 | License 订购与订阅流程 | eBuy→Subscription Manager→导入三步与 24h 延迟命中 p175，开通排期依据
- p25 | 账户-组织层级规则与一邮箱一 MSP 限制 | 子地址技巧+组织迁移/脱离后果命中 p198-209，多租户账号规划规则
- p26 | OVC4→OVC 迁移规则 | 序列号禁止双登记+先删后迁+Call Home 30 分钟命中 p218-219
- p27 | 设备激活状态机与 Call Home 强制方法 | 状态链+5 分钟中间态+cloud-agent restart 强制命中 p250-261
- p28 | AP Group/Provisioning Configuration 强制字段 | Name/Site/RF Profile/Timezone 四必填命中 p273，建组配置硬约束
- p29 | Onboarding 方法一：手工 VLAN 分类及其扩展代价 | 逐口手工配 VLAN 的限制原文命中 p286，选型权衡依据
- p30 | Onboarding 方法二：UNP 自动分类 | defaultWLANProfile+LLDP 自动识别与 Dummy VLAN 命中 p288
- p31 | Stellar AP 排障 CLI 工具箱 | 串口 115200-8-N-1+全套命令（getmode/ocloud_show/sta_list 等）命中 p305
- p33 | SSID Usage 模板映射表 | Usage→安全模型自动模板映射命中 p313，Cirrus 建 SSID 选型速查
- p34 | SSID 的 VLAN/Tunnel 映射与 VLAN 池 | 单 VLAN/池(≤256)/Guest 隧道选项命中 p319，大广播域规避设计
- p35 | 全局 PSK 与设备专用 PSK | DSPSK Force/Prefer 语义与三项约束命中 p326-327
- p36 | 私有组 PSK 与动态私有组 PSK | 条目绑定 ARP/VLAN 与 Priority 选项命中 p328-330，按组隔离密钥工程
- p37 | Employee SSID（802.1X）创建要点与客户端 PEAP 参数 | WPA2_AES+Local Database+Linux PEAP/MSCHAPv2 命中 p338/341
- p38 | UPAM RADIUS 常数 | 1812/1813/重试 2/超时 5s 命中 p347，认证排障常数
- p39 | UPAM 组成与可选认证源 | 四大件+本地/外部 RADIUS/IMSI/Azure AD 命中 p351/354
- p40 | Guest Access Strategy 三大配置块 | 登录策略/后置执法/自注册审批命中 p357，访客策略对象模型
- p41 | Guest SSID 配置规则 | Allow All EAPs=Yes/Source=None/WebAuth=Guest 三开关命中 p379
- p42 | Guest Tunneling 规则 | 按 ARP 建 L2 GRE 隧道+自动建隧道+备份隧道命中 p367
- p43 | BYOD SSID 的 VLAN 流转 | 预认证 Guest VLAN→认证后 Employee VLAN 命中 p391，双阶段准入核心规则
- p44 | 统一策略与三级带宽控制及执行顺序 | 策略>ARP>SSID 优先序命中 p408-409，限速设计判定链
- p45 | 客户账号类型与必填字段 | 四类账号必填项+Service Level≤5 命中 p426-428，账号体系建模
- p46 | Registration Profile：数据/时间配额与耗尽处理 | 100MB/每天 4h、阻断或降速 UP=100/DOWN=1000kB/s 实例命中 p429-430
- p47 | DRM 分布式射频管理原则 | 空口发现/LAN 共享上下文/邻居域/不依赖组命中 p439，无控制器架构原理
- p48 | Smart Air Share 最小数据速率推荐值 | 2.4G=12/5G=24/6G=24 命中 p444，速率控制调优常数
- p49 | 智能负载均衡与关联 RSSI 阈值推荐 | 2.4G=5/5G=10 及阈值 90 实验佐证命中 p445/460-463
- p50 | Band Steering 判定阈值与信道过载定义 | 差值阈值 10、过载 70%/1 分钟、默认禁用原因命中 p446/459
- p51 | 背景扫描参数 | 默认 20 秒/50 毫秒+WIPS 依赖+语音视频感知命中 p448
- p52 | 信道宽度选项与发射功率范围 | 各频段宽度选项与功率 3-23dBm 命中 p450，显式射频参数范围表
- p53 | RF 优化推荐参数总表 | 官方推荐基线全表命中 p451，调优起点清单
- p54 | RSSI-dBm 换算表与信号质量分级 | dBm=RSSI-96 换算与 Bad/OK/Desired 分级命中 p454，ALE 专属标尺
- p55 | SGI 增益、MU-MIMO/HE 开关与 RF Profile 下发路径 | SGI≈11%、HE 降级 VHT、rfprofile.conf 验证命中 p462-466
- p56 | 漫游默认状态与快漫游协议约束 | L2 恒开/L3 与快漫游默认关+OKC/11r 加密前提命中 p471
- p57 | L2/L3 漫游判定表 | 上下文/WLAN 服务/VLAN 三条件判定命中 p476，漫游形态预测依据
- p58 | 粘滞客户端规避与 Roaming RSSI 阈值 | 2.4G=10/5G=15+802.11k/v 组合命中 p492
- p59 | 相邻 AP 互相看不见时的静态邻居配置 | 直角走廊场景互加 Neighbor AP 修复命中 p491
- p60 | RAP 部署设备要求与开局五步 | AP1101 不兼容+五步时序+三段预置参数命中 p497-508
- p61 | WIPS 三类 AP 分类与 Rogue 遏制默认开启 | 分类规则+遏制 de-auth+ALE OUI 白名单命中 p514
- p62 | Rogue AP 策略四条件与信号阈值默认 -70dBm | 四条件与 -50~-90 范围命中 p515，误判风险评估依据
- p63 | 无线攻击检测与客户端黑名单触发常数 | 10 次/60 秒拉黑、老化 1 天命中 p516-517/524
- p64 | 勘测三类型与适用阶段 | 被动/主动/预测定义与阶段映射命中 p529-530，勘测方法选择原则

## cases（23 通过）

- c01 | 连接并使用 Stellar 远程实验室（R-Lab） | R-Lab URL/POD 账号/拓扑入口/控制台快捷方式命中 p69-75，实验环境操作手册
- c02 | R-Lab 设备重初始化（Reset_PodX 脚本） | 重置流程/时长常数/"默认配置非空且端口全禁"警告命中 p77-80
- c03 | 设备启动与连接（6360 控制台+AP1321 向导） | 端口启用/IP/向导改密建 SSID/改静态 IP 全步骤命中 p108-119
- c04 | PoE、VLAN 与 DHCP 配置 | show lanpower/VLAN 划分/AP 改 DHCP+域名访问命中 p121-129
- c05 | Express 模式员工与访客 SSID 创建 | EmployeesX/GuestsX 建立与验证、门户账号命中 p144-153
- c06 | 把 Stellar AP 配置为内嵌 DHCP 服务器 | Network→DHCP→Bind Network 三步与池参数命中 p154-157
- c07 | 用户行为日志、Operator 账号与外部 RADIUS | 行为跟踪+受限账号+外部 RADIUS 三附录命中 p158-160
- c08 | isc-dhcp-server 用 DHCP Option 138 指向 OmniVista | 完整配置样例（类匹配/自定义 option/pool）命中 p33
- c09 | Cirrus 账号创建、组织与许可证订阅流程 | eBuy 下单→订阅→组织→导入全流程截图链命中 p169-238
- c10 | 远程实验室重初始化（Cirrus 预配置加载） | reset_PODX 脚本+Miniboot 警告+连通性验证命中 p238-240
- c11 | 环境创建与 OmniSwitch 上云 Onboarding | 站点/楼宇/楼层/平面图+交换机声明激活排障命中 p241-253
- c12 | Stellar AP 上云与 AP Group/Provisioning 配置 | AP 声明/建组建配置/激活验证与全套排障命中 p293-306
- c13 | Employee SSID 创建（802.1X + UPAM）及排障 | VLAN→IP 接口→SSID→账号→测试→监控→CLI 排障全链命中 p332-347
- c14 | PSK 家族四种密钥方案配置样例 | PSK/DSPSK/PPSK/动态组逐屏配置命中 p324-330
- c15 | Guest SSID 创建（开放+OV-UPAM 门户）与踢下线 | VLAN30→门户→策略→踢下线→eag 排障命中 p372-388
- c16 | BYOD SSID 创建（双 VLAN 切换） | 预认证 VLAN30→认证后 VLAN20 实验与验证命中 p389-395
- c17 | Unified Policy 创建与绑定（Block_SSH） | 基线测试→建策略→绑 SSID→复测对比命中 p411-416
- c18 | RF 管理实验（RF Profile+RSSI 阈值） | 建 Profile→读 RSSI→阈值 90 拒联→回退闭环命中 p456-466
- c19 | WIPS 配置与 AP 分类 | Friendly 添加+Rogue 关键字对 Friendly 无效验证命中 p521-525
- c20 | 组织配置清理（25 步） | 按依赖逆序删除全部对象的完整清单命中 p542-547
- c21 | RAP 远程接入点部署 | OVC10/VPN Server/OV2500/双隧道全流程与地址规划命中 p549-572
- c22 | Wi-Fi 现场勘测方法论 | 三类型选择+四类根因+三步排障（默认 17dBm）命中 p526-540
- c23 | 客户端账号与配额管理样例 | 四类账号界面操作与 100MB/4h 配额触发实例命中 p417-434

## counter-examples（40 通过）

- ce01 | 模式切换不迁移配置 | Express 转 Enterprise/Cloud 丢整个集群配置的规避方案命中 p18
- ce02 | option 138 配错则 AP 进错模式 | 静默落 Express 广播 mywifi-XXXX 的根因与 getmode 排查命中 p100
- ce03 | isc-dhcp-server 不认识 option 138 | 必须先自定义 option 的踩坑点与完整写法命中 p33
- ce04 | 云管前置清单不满足则不上线 | 防火墙/NTP/型号/版本任一缺失的失败模式汇总命中 p167
- ce05 | OVC4 迁移序列号禁止双登记 | 先删旧云再登记+Call Home 加速命中 p219
- ce06 | eBuy 许可最长 24 小时延迟 | 交付当天下单会卡现场的排期风险与规避命中 p175
- ce07 | 一邮箱账号只能归属一个 MSP | 子地址派生注册的 workaround 命中 p198
- ce08 | 组织级破坏性操作 | Disassociate 全员失访+删除组织的破坏半径与检查项命中 p208/243
- ce09 | Reset 脚本默认配置非空且全端口禁用 | 实验室 gotcha 与"脚本基线+手动增量"类比命中 p80
- ce10 | 重置期间按键落 Miniboot | 一次回车中断重启的操作禁忌命中 p240
- ce11 | 不要对实验室交换机真恢复出厂 | 专用预配置承载隐性依赖的警告与生产类推命中 p120
- ce12 | 树莓派以太网卡是管理生命线 | 管理通道先保住的交付守则命中 p75
- ce13 | 改 AP 管理 IP/切 DHCP 后失联 | 用新地址或 mywifi.al-enterprise.com:8080 重连命中 p127
- ce14 | 激活失败状态集反推原因 | 七种失败态映射（VPN profile 变更须现场恢复出厂）命中 p261-262
- ce15 | Call Home 间隔太久强制上线 | 交换机 cloud-agent restart/AP 重启的加速手段命中 p250
- ce16 | AP 不上云三层排障链 | PoE/VLAN→模式/DHCP→L3/DNS 完整链与最常见根因命中 p304-306
- ce17 | UNP 的 802.1X 安全盲区 | 未认证 AP 的 tagged 流量仍被转发的 rogue 风险命中 p291
- ce18 | 手动分类逐口配 VLAN 的扩展陷阱 | 漏配即不通且故障隐蔽，规模化改 UNP 命中 p286
- ce19 | AOS release 5 交换机不被 Cirrus 支持 | 版本盘点与"半纳管"交付边界命中 p242
- ce20 | DSPSK 不支持 AUTO_WPA_WPA2 | 加密互斥约束与 Force/Prefer 规划命中 p327
- ce21 | MAC/共享 PSK 的安全弱点与规避 | 哑设备用 DSPSK/PPSK、人员用 802.1X 的产品级组合命中 p310
- ce22 | 门户排障三查 | AP 时间/DNS/非 https 触发+eag_cli 工具链命中 p385-388
- ce23 | 802.1X 连不上查 AAA conf+tcpdump | 三个配置文件核对与抓包路径命中 p347
- ce24 | Band Steering 默认禁用的原因 | 5G 覆盖弱/有洞时把终端推进弱信号区的风险命中 p459-460
- ce25 | 关联 RSSI 阈值设高全网拒联 | 隐蔽全局故障的 QoE 验证与回退命中 p463-464
- ce26 | 扫描与性能天生互斥 | 20s/50ms 平衡点+语音视频感知+专用扫描模式命中 p448
- ce27 | Client-aware 关闭时 ACS 打断客户端 | 换信道闪断风险与 kes_syslog 定位命中 p461
- ce28 | 漫游协议加密前提 | OKC 仅 Enterprise、802.11r 仅 WPA2/WPA3 加密命中 p471
- ce29 | 地理相邻 AP 互相看不见则无漫游 | 静态 Neighbor AP 修复方案命中 p491
- ce30 | Roaming RSSI 阈值两难 | 太低粘滞/太高频繁切换丢包与推荐值命中 p492
- ce31 | 跨云/无 WLAN service 上下文被丢弃 | Add/Del 消息丢弃退化为全新接入命中 p475
- ce32 | Rogue 反制的杀伤半径 | de-auth 波及邻居网络+Friendly 一票豁免命中 p523-525
- ce33 | 黑名单攻击源 MAC 局限 | 源 MAC 未必是真实客户端的适用面分析命中 p517
- ce34 | RAP 部署三坑 | AP1101 不兼容/conf 留存/OV2500 回程路由 checklist 命中 p497/557/566
- ce35 | 云管无一键恢复须逆序拆 25 步 | 依赖顺序拆除 SOP 命中 p544-547
- ce36 | 删除 Site 是级联操作 | 楼栋楼层与设备归属连带删除命中 p547
- ce37 | 内置 DHCP 池=并发上限 | 40 地址=40 设备与"误判为无线故障"提醒命中 p155
- ce38 | 员工账号默认弱密码策略 | 收紧入口与外部认证源升级路径命中 p422
- ce39 | 四类信号杀手现场归因 | 含 4m 穿墙 -70dBm 不够 VoWLAN、默认 17dBm 等常数命中 p532-540
- ce40 | 教材自身局限 | R-Lab 依赖/不含 OV2500 GUI/与售前课重叠，指导本 KB 使用边界（源自 BOOK_OVERVIEW.md，原文核实）

## glossary（55 条，免验保留，词表无重复）

统一判定理由：产品/平台术语与本书语境绑定（默认值、配置入口、容量上限、与 Lab 的关联），作为知识库查询锚点保留；逐条比对 55 个 term 无重复，无需去重合并。

g01 802.1X · g02 802.11k · g03 802.11r · g04 802.11v · g05 Access Role Profile · g06 Active Survey · g07 AP Group · g08 Background Scanning · g09 Band Steering · g10 Bandwidth Control · g11 BYOD · g12 Call Home · g13 Captive Portal · g14 Client Context Sharing · g15 Cloud Mode · g16 DHCP Option 138 · g17 D-PGPSK · g18 DRM · g19 DSPSK · g20 Ekahau · g21 Employee SSID · g22 Enterprise Mode · g23 Express Mode · g24 Friendly AP · g25 Guest SSID · g26 Guest Tunneling · g27 Interfering AP · g28 L2 Roaming · g29 L3 Roaming · g30 MSP · g31 OKC · g32 OmniVista 2500 · g33 OmniVista Cirrus · g34 Onboarding · g35 Organization · g36 Passive Survey · g37 Planes of Operation · g38 PoE · g39 PPSK · g40 Predictive Survey · g41 Provisioning Configuration · g42 PSK · g43 PVM · g44 RAP · g45 RF Profile · g46 Rogue AP · g47 RSSI · g48 Site · g49 Smart Air Share · g50 Smart Load Balance · g51 Stellar Remote-Lab · g52 SVM · g53 UPAM · g54 Unified Policy · g55 WIPS
