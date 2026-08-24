# verified.md · 三重验证通过条目（阶段 1.5）

## 汇总

| 类型 | 候选 | 通过 | 淘汰 | 淘汰原因 |
|---|---|---|---|---|
| frameworks | 17 | 17 | 0 | — |
| principles | 40 | 39 | 1 | p11（V3：客户端 Windows 命令属通用常识） |
| cases | 14 | 13 | 1 | c14（V3：环境预检为通用方法论，非本书特有） |
| counter-examples | 20 | 20 | 0 | — |
| glossary | 42 | 42（免验保留） | 0 | — |
| **合计** | **133** | **131** | **2** | |

验证方式：V1 对全部 91 条非 glossary 条目的 quote 片段在 source/fulltext.md 做 grep 命中检查（含 CLI 截取与 PDF 断行变体），全部命中；V2/V3 逐条判读。仅 2 条因 V3（常识性、无本书独特增量）淘汰，明细见 rejected/。

---

## Frameworks（17/17 通过）

- **f01 结构化排障总流程**：V1 命中（"Gather symptom / Divide and Conquer" 等片段均命中）；V2 全书主方法论流程图+七步法；V3 配合 AOS 命令与 OSI 定位，保留。
- **f02 OSI 分层排障六种切入方法**：V1 命中（Bottom-Up/Top-Down/Divide and Conquer/Move the problem）；V2 方法选择有判据（p58）；V3 通用方法但作为后续所有章节的框架骨架，保留。
- **f03 OSI 各层症状-原因对照表**：V1 命中（Attenuation/Noise 等原文命中）；V2 快速定位故障域索引；V3 含 AOS 特有症状项，保留。
- **f04 启动序列排障与密码恢复/USB 恢复**：V1 命中（setAdminPasswordDefault / run rescue / onie-nos-install 均命中）；V2 高频应急操作流程；V3 ALE 特有命令链（U-Boot/ONIE 双路径），强保留。
- **f05 交换系统硬件排障命令链**：V1 命中（show running-directory / show hardware-info 等）；V2 show 命令判读主线；V3 AOS 命令族，保留。
- **f06 高 CPU 排障流程**：V1 命中（maintenance shell 上下文 top/ps 原文命中）；V2 排障流程完整；V3 维护 shell + TAC 升级边界是 ALE 特有，保留。
- **f07 二层连通性排障三层走法**：V1 命中（Native VLAN mismatch 等）；V2 物理→配置→ARP 分层流程；V3 含 show vlan member 判读等 AOS 细节，保留。
- **f08 STP 桥接环路排障八步清单**：V1 命中（checklist recapitulating）；V2 清单级可操作；V3 swlog appid 细分/12500 尺寸等 AOS 参数，强保留。
- **f09 Virtual Chassis 排障流程**：V1 命中（show virtual-chassis consistency）；V2 四层递进+NOK 码定位；V3 VC/NOK 码纯 ALE 特有，强保留。
- **f10 L3/IP 连接问题排障决策树**：V1 命中（fulltext 4358-4381 行流程图原文，PDF 断行）；V2 决策树清晰；V3 配 AOS show ip 命令族，保留。
- **f11 丢包排障双工具流程**：V1 命中（icmptype 8 / matched:accept）；V2 QoS 计数+抓包两步法可操作；V3 policy condition/qos apply/port-monitoring 为 AOS 命令，保留。
- **f12 OSPF 邻居/路由排障流程**：V1 命中（maximum verbosity）；V2 状态机→参数→debug 流程；V3 swlog appid ospf_0 调级方式 AOS 特有，保留。
- **f13 组播排障流程**：V1 命中（show ip multicast forward）；V2 L2/DVMRP/PIM 分层；V3 AOS debug 子应用分区，保留。
- **f14 VRRP 排障流程**：V1 命中（Skew_Time）；V2 三角核对法；V3 show ip vrrp 判读 AOS 特有，保留。
- **f15 OVNA 安装部署三步流程**：V1 命中（dpkg -i ale-ovna / ale-ovna install）；V2 部署可操作；V3 ALE 产品特有（Ubuntu/k3s/端口矩阵），保留。
- **f16 OVNA 纳管设备与告警处置流程**：V1 命中（ddm enable / swlog output socket）；V2 LAB5 完整处置闭环；V3 OVNA 自动推送命令与 10514 端口 ALE 特有，保留。
- **f17 Teams Bot 对接四阶段流程**：V1 命中（Phase 1 of 4 / Bot Management / Download the app package，Phase 3-4 原文为 "Get your IDs"/"Grand admin consent" 的变体命中）；V2 是 f16 通知渠道的前置部署流程；V3 ALE+Entra 对接细节特有，保留。

## Principles（39/40 通过；p11 淘汰）

- **p01 排障文档先行九类**：V1 命中；V2 排障前提清单+LAB1 重建命令；V3 含 show lldp remote-system 等 AOS 命令，保留。
- **p02 ALE 开案最小信息与严重级别**：V1 命中（Minimum Information）；V2 升级 TAC 流程；V3 ALE eService 特有，保留。
- **p03 TKC 用例结构与检索**：V1 命中（natural language）；V2 查库方法；V3 ALE TKC 特有，保留。
- **p04 show system 三判读点**：V1 命中（Up Time 原文）；V2 show 输出判读；V3 串联日志对时思路，保留。
- **p05 POWER ON + DOWN 指向软件问题**：V1 命中；V2 关键判别判据；V3 AOS 模块状态判读，保留。
- **p06 硬件版本对照 release note**：V1 命中（update uboot/fpga-cpld 命令原文在 1627-1628 行）；V2 升级门槛判断；V3 AOS 升级顺序铁律，强保留。
- **p07 show health CPU 水位与四大根因**：V1 命中；V2 判读+根因索引；V3 AOS 下钻命令，保留。
- **p08 温度双阈值机制**：V1 命中（UNDER THRESHOLD）；V2 trap/关断行为判读；V3 CMM 行为特有，保留。
- **p09 面板 LED 判读速查**：V1 命中（SOLID GRN）；V2 硬件速查表；V3 ALE 面板灯语义特有，保留。
- **p10 show interfaces 端口级判读**：V1 命中（Bytes Received is incrementing）；V2 计数器采样判读法；V3 AOS 输出列判读，保留。
- ~~p11 终端侧排障命令五件套~~：**淘汰（V3）**，见 rejected/principles.md。
- **p12 show vlan member 三要素**：V1 命中；V2 判读要点；V3 default/qtagged 端口类型 AOS 特有，保留。
- **p13 ARP 五步法与 debug ip packet 判读**：V1 命中（五步原文）；V2 流程+1R/1S 判读；V3 AOS 命令细节，保留。
- **p14 静默设备对策**：V1 命中（aging-time / static mac 命令）；V2 对策命令；V3 AOS 命令语法，保留。
- **p15 swlog 架构参数**：V1 命中（Loopback0 have to be configured / 1250KB）；V2 容量规划参数；V3 R8 上限数值 AOS 特有，保留。
- **p16 swlog 级别与 appid/subapp 调级**：V1 命中；V2 调级命令；V3 28 个 OSPF 子应用编号表纯 AOS 特有，强保留。
- **p17 show log swlog 三大过滤技巧**：V1 命中（CUSTLOG）；V2 检索技巧；V3 reverse/_readable AOS 特有，保留。
- **p18 VC 启动与配置同步机制**：V1 命中（vcboot.cfg from the Master）；V2 机制理解支撑排障；V3 vcsetup/vcboot/Auto-VC 纯 ALE，强保留。
- **p19 VC NOK 码速查**：V1 命中（NOK_08/17）；V2 错误码定位表；V3 NOK 码 ALE 特有，强保留。
- **p20 STP 阻塞端口判读**：V1 命中；V2 两大原因判据；V3 show spantree 输出列判读，保留。
- **p21 STP 参数与拓扑变化计数**：V1 命中（timers need to be consistent）；V2 判读要点；V3 保留。
- **p22 MAC flapping 三板斧**：V1 命中（Number of Status Change 13 处）；V2 检测方法；V3 slNi macmove 调级 AOS 特有，强保留。
- **p23 debug stp bpdu-stats**：V1 命中（bpdu-stats）；V2 收发统计判读；V3 AOS debug 命令，保留。
- **p24 STP 防故障设计九原则**：V1 命中（Loop Guard）；V2 设计清单；V3 qos user-port filter 等含 AOS 元素，保留。
- **p25 MSTP 三致性检查**：V1 命中（unpredictable）；V2 检查清单；V3 保留。
- **p26 QoS 规则计数判读**：V1 命中（matched:accept 9 处）；V2 丢包定位判据；V3 AOS policy 语法，保留。
- **p27 DHCP 中继排障判据**：V1 命中；V2 Tx Server 计数判据+LAB3 根因；V3 AOS 命令族，保留。
- **p28 RIP 版本/认证兼容规则**：V1 命中（Responds with a RIP-1 / auth-type or auth-key）；V2 检查点清单；V3 v1/v2 交互细节保留。
- **p29 OSPF 接口参数判读**：V1 命中（Hello Interval (seconds)）；V2 参数核对清单；V3 AOS 输出判读，保留。
- **p30 OSPF 日志错误样例判读**：V1 命中（oversized LSA 在 5212-5213 行原文）；V2 日志直接给答案的判读样例；V3 AOS 日志格式，强保留。
- **p31 VRRP 定时器公式与虚拟 MAC**：V1 命中（Skew_Time）；V2 公式+LAB4 根因；V3 保留。
- **p32 组播 L2 设计五规则**：V1 命中（querier / TTL equal 1）；V2 部署核查规则；V3 IPMS 参数 ALE 特有，保留。
- **p33 DVMRP DF 选举判读**：V1 命中（Designated forwarder）；V2 排错路径；V3 dvmrp_0 debug 分区 AOS 特有，保留。
- **p34 PIM-SM 监控命令族**：V1 命中（candidate-rp）；V2 命令分工+LAB4 根因；V3 保留。
- **p35 QoS 配置生命周期四命令**：V1 命中（qos revert）；V2 apply/revert/flush/reset 语义区分；V3 AOS 命令语义，保留。
- **p36 UNP/802.1X：RADIUS 测试先行**：V1 命中（test-radius-server）；V2 aaa test 命令判读；V3 AOS 特有工具，保留。
- **p37 镜像工具边界（RPM 专用 VLAN/不镜像清单）**：V1 命中（No other traffic is allowed）；V2 抓包结论解读边界；V3 六类不镜像清单 ALE 特有，保留。
- **p38 ip service source-ip 固定源地址**：V1 命中（force the Syslog / source-ip loopback0 swlog）；V2 多 IP 设备排障要点；V3 AOS 命令与应用清单，保留。
- **p39 OVNA 系统要求与端口清单**：V1 命中（Quad-core / Internet access is mandatory）；V2 部署硬参数；V3 ALE 产品规格，保留。
- **p40 logger 注入测试日志**：V1 命中（easy way to add log entries / logger -t）；V2 无损演练全链路的方法；V3 ALE 特有测试技巧，保留。

## Cases（13/14 通过；c14 淘汰）

- **c01 TKC 检索两个已知缺陷**：V1 命中（OS6900-V48C8 / In progress）；V2 版本相关缺陷检索训练；V3 真实缺陷编号+版本号，保留。
- **c02 LAB1 主案例（UNP+VLAN+接口三元故障）**：V1 命中；V2 完整排查路径+三处修复命令；V3 LAB 环境根因组合，保留。
- **c03 LAB2 案例1（VC 组建失败）**：V1 命中；V2 .err 文件定位法+修复命令；V3 stackport 平台限制与编号规则 ALE 特有，强保留。
- **c04 LAB2 案例2（VLAN 278 无 STP 成环）**：V1 命中（arp info overwritten 11 处 / invalid ip from 7 处）；V2 完整环路排障路径；V3 DoS invalid-ip + VRRP 虚拟 MAC 判别口诀 ALE 特有，强保留。
- **c05 LAB3 案例1（DHL 双链路 blocking）**：V1 命中（dhl-blocking 13 处）；V2 native VLAN 一致性判据；V3 DHL 为 ALE 特有特性，强保留。
- **c06 LAB3 案例2（DHCP 中继目的地配错）**：V1 命中（172.168.100.102）；V2 计数判据+修复命令；V3 LAB 根因+判据沉淀，保留。
- **c07 LAB4 案例1（VRRP 三连错）**：V1 命中（VRID Errors 6 处）；V2 三根因叠加排查路径；V3 保留。
- **c08 LAB4 案例2（OSPF 双错叠加）**：V1 命中（alcatell 20 处 / invalid helloInterval）；V2 日志直读根因+复测流程；V3 日志样例含真实密钥值，强保留。
- **c09 LAB4 案例3（组播不通漏配 PIM）**：V1 命中（231.1.1.1 / Security Camera）；V2 traceroute+逐接口核 PIM 方法；V3 保留。
- **c10 LAB5 用例1（模拟 DDoS 一键处置）**：V1 命中（ping overload 6 处）；V2 完整闭环演练；V3 OVNA 处置链 ALE 特有，保留。
- **c11 LAB5 用例2（模拟 PMD 崩溃）**：V1 命中（PMD generated）；V2 崩溃类处置方向差异；V3 PMD 文件路径与 remediation 分级 ALE 特有，保留。
- **c12 LAB5 用例3（linkagg 成员口 down）**：V1 命中（Sync Out）；V2 日志因果链样板；V3 LACP 状态机日志判读，保留。
- **c13 LAB5 用例4（认证失败 Acknowledge）**：V1 命中（pam_authenticate）；V2 三级处置动词最轻一级示例；V3 OVNA 处置分级 ALE 特有，保留。
- ~~c14 LAB1 环境预检（配置漂移）~~：**淘汰（V3）**，见 rejected/cases.md。

## Counter-examples（20/20 通过）

- **ce01 环路时必须走 console**：V1 命中（EMP's IP）；V2/V3 管理面可达性+EMP 兜底，保留。
- **ce02 su 维护 shell 不是后门**：V1 命中（not trivial）；V2 使用边界；V3 ALE 支持管控要求，保留。
- **ce03 debug ip packet 裸跑刷屏**：V1 命中（dump a lot of information）；V2 过滤参数表；V3 AOS debug 参数维度，保留。
- **ce04 swlog 忘记调回 info**：V1 命中；V2 收尾 SOP；V3 与 AOS 调级机制绑定，保留。
- **ce05 上电但 DOWN 误判硬件**：V1 命中；V2 误诊防范判据；V3 保留。
- **ce06 手工编辑 vcsetup.cfg 触发 error mode**：V1 命中（unable to read a valid chassis）；V2 后果+正解；V3 ALE 特有文件与保护机制，强保留。
- **ce07 stackport 平台不支持 static VFL**：V1 命中（not supported for stackport platform 2 处）；V2/V3 平台坑 ALE 特有，强保留。
- **ce08 member-port 编号与 chassis-id 不一致**：V1 命中（Chassis id needs to be consistent 2 处）；V2 复制粘贴错判别；V3 编号规则 ALE 特有，保留。
- **ce09 FPGA/U-Boot 升级顺序颠倒**：V1 命中（p102 原文 Note）；V2 顺序铁律；V3 保留。
- **ce10 高峰期核心上 clear arp-cache**：V1 命中（slight interruption）；V2 影响评估；V3 保留。
- **ce11 ONIE 密码恢复只能 console**：V1 命中（only possible from the switch console）；V2 路径限定；V3 ONIE 恢复流程 ALE 特有，强保留。
- **ce12 RADIUS 测试失败的 MD5/PAP 前提**：V1 命中（can only be MD5 or PAP）；V2 假阴性判别；V3 AOS 测试工具限制，保留。
- **ce13 QoS 策略只匹配 ingress**：V1 命中（applies only ingressing）；V2 出向分析替代方案；V3 AOS 限制+port-monitoring，强保留。
- **ce14 RPM 镜像 VLAN 复用/控制报文不可见**：V1 命中（No other traffic is allowed）；V2 抓包结论边界；V3 六类清单 ALE 特有，保留。
- **ce15 VRRP 虚拟 IP 抄错一位**：V1 命中（VRID Errors 上下文）；V2 误诊为攻击的判别；V3 保留。
- **ce16 MSTI VLAN 未 tagged**：V1 命中（unpredictable）；V2 隐性故障判别；V3 保留。
- **ce17 随手调 STP 定时器**：V1 命中；V2 设计纪律红线；V3 保留。
- **ce18 write memory 弹 chassis missing 警告随手确认**：V1 命中（erased permanently）；V2 永久删除风险；V3 VC 特有警告+Client Secret 类比，保留。
- **ce19 DoS 告警刷屏误判攻击**：V1 命中（invalid ip from）；V2 判别口诀；V3 00:00:5e 虚拟 MAC 判读，强保留。
- **ce20 只修一层就收工**：V1 命中（check if there is not another problem）；V2 复测纪律；V3 LAB4 原文流程支撑，保留。

## Glossary（42/42 免验保留）

按阶段规则 glossary 免三重验证，全部 42 条原样保留（g01-g42），进入下一阶段直接使用 candidates/glossary.md 内容。
