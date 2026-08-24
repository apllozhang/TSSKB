# DIGEST · ACFE WLAN 基础部署精华——一台 Stellar AP 从开箱到运营的全生命周期

> 教材：DT00XTE360EN Edition 04（ALE 培训服务，2025-11，585 页，5 天实验课）
> 本文是"不读全书、只看精华"的交付工程师版速读。数字后括注页码，可直接对照原书。

---

## 一、一页看懂这门课

这门课回答一个问题：**一台 OmniAccess Stellar AP 从纸箱里拿出来，到成为一个可运营的园区无线网的一份子，中间每一步怎么做。**

完整生命周期是：上电 → 判定管理模式（Enterprise/Cloud/Express，p100）→ 网络前置准备（PoE/VLAN/DHCP，p25）→ 云管开通（License/组织，p173）→ 设备 Onboarding 上云（p261）→ 建 SSID（员工/访客/BYOD，p312）→ 策略与带宽管控（p408）→ RF 优化（p451）→ 漫游与远程接入（p476/p499）→ WIPS 安全防护（p514）→ 勘测验收（p526）→ 最后是组织清理回退（p544）。

课程主线用 OmniVista Cirrus 云管（OV2500 本地管不在此课）。每章配远程实验室（R-Lab），是边讲边做的工程师手册，尤其适合当交付 SOP 素材库用。

一个贯穿全书的架构认知是**三平面模型**：管理平面（网管/Cirrus，管理流量恒 untagged）、控制平面（每台 AP 的空口邻居发现）、数据平面（AP 本地终结，按 SSID 恒 tagged 上行，纯二层、无隧道回网管，路由交给 LAN）。端口规划和排障都从这个模型推。

---

## 二、交付主线七阶段（串起 10 个 skill）

1. **模式判定**：AP 上电三级判定——DHCP offer 带 option 138（OV2500 地址）→ Enterprise；无 138 但序列号已在 Cirrus 登记 → Cloud；都不满足 → Express 默认广播 mywifi-ABCD（p100）。反向用就是模式规划。→ `express-mode-bootstrap`
2. **网络前置**：PoE trunk（Native=管理 VLAN，SSID VLAN 全 tagged）、每个 VLAN 的 DHCP 作用域、DNS、三层路由、按型号核对供电等级（p25）。Express 集群上限 255 台、选举先比型号再比 MAC（p11）。
3. **Cirrus 组织**：eBuy 下单（品号 OVCX-系列-级别-年限-类别）→ Subscription Manager 建订阅（**最长 24h 延迟**，p175）→ 组织内 Import Licenses → 指派设备（p173）。账号层级 MSP > Organization > Site > Building > Floor。→ `cirrus-license-org-lifecycle`
4. **设备 Onboarding**：交换机侧二选一（手动 VLAN 分类 vs UNP+LLDP 自动分类，p284）→ 取序列号声明 → 建AP Group + Provisioning（四必填：Name/Site/RF Profile/Timezone）→ 等激活状态机走到 OV Managed，每个中间态正常 ≤5 分钟（p261）。→ `device-cloud-onboarding`
5. **SSID 全家桶**：三段式创建——SSID Settings（Usage 模板套认证模型）→ Network Assignments（Site + AP Group）→ Schedule & VLAN Mappings（p312）。Employee=802.1X，Guest=门户+可选隧道，BYOD=先落 Guest VLAN、门户认证后切 Employee VLAN（p391）。→ `ssid-authentication-suite`
6. **策略与 RF**：Unified Policy 按 Condition → Action → Group → 挂 SSID 的固定顺序（p413）；带宽三层落点执行序为策略 > 角色 > SSID（p408）。RF Profile 走"创建 → 绑 Provisioning → QoE 验证 → 回 Default"闭环（p463）。→ `upam-policy-bandwidth` + `rf-optimization-baseline`
7. **安全与验收**：WIPS 三分类（Interfering/Rogue/Friendly）+ Rogue 四条件 + Containment（p514-515）；勘测三步法拿图 → 观察 → 纠正（p537-540）；漫游按三条件判定 L2/L3（p476）；RAP 五步双隧道上线（p499）。→ `wips-security-deployment` + `site-survey-troubleshooting` + `roaming-rap-design`

`rlab-lab-manual` 是横向工具：管实验环境连接重置，并把 15 个 Lab 索引到上述各 skill。

---

## 三、开局检查清单（可直接照抄）

**上电前逐项打勾：**

- [ ] PoE：端口供电等级满足型号（AP1311 严禁 af 下开 PSE/USB；AP1230 需 at 60W；AP1351 需 bt；`show lanpower` 核对）
- [ ] 端口：AP 口为 trunk，Native/untagged=管理 VLAN，全部 SSID VLAN tagged（管理 VLAN 没 untagged 到 AP 口是最常见根因）
- [ ] DHCP：管理 VLAN + 全部 SSID VLAN 各建作用域；Enterprise 模式管理作用域加 option 138（isc-dhcp-server 需先声明 `option ovwma code 138 = ip-address;` 并按 vendor-class 前 4 字节 "HAP." 匹配，p33）
- [ ] DNS：覆盖全部管理/SSID 子网
- [ ] 路由：所有 VLAN 有三层接口
- [ ] 云管防火墙：入向放行 9093 / 30123 / 30124 / 30125；出向放行 443 / 80 / 123 / 53；至少 1 台 NTP
- [ ] 版本盘点：AP 固件 AWOS 4.0.6 GA+；AP1101/AP1201L/H/HL 与 AOS release 5 交换机不被 Cirrus 支持
- [ ] License 至少提前一天下单（24h 延迟红线，p175）

---

## 四、SSID 认证与密钥体系速查表

**认证选型（信任从低到高）**：Open+门户 < MAC（可伪造）< PSK < 802.1X。产品级组合：哑设备用 DSPSK/PPSK，人员用 802.1X（ce21）。

| SSID 类型 | 认证模型 | 关键开关 |
|---|---|---|
| Employee | WPA2_AES + 802.1X | UPAMRadiusServer、RADIUS 1812/1813、重试 2 超时 5s |
| Guest | Open/MAC + Captive Portal | Portal=YES、Allow All EAPs=Yes、可按 ARP 建 L2 GRE 隧道 |
| BYOD | 802.1X/MAC + BYOD 门户 | SSID 级 VLAN=Guest（预认证沙箱）→ Post Portal Enforcement 绑 ARP 切 Employee VLAN（p391） |
| Protected | PSK（+可选门户） | 见下四级 |

**PSK 四级密钥体系（p326-330，运维粒度递进）**：

1. 全局 PSK：一钥全员
2. DSPSK：按 MAC 发专属口令（Force=取消全局口令，Prefer=保留兜底；与 AUTO_WPA_WPA2 互斥）
3. PPSK：多条"口令+角色"，用哪条落哪个 ARP
4. 动态 PPSK：口令直接绑 VLAN ID + ARP，配 Priority 定归属

---

## 五、RF 优化参数基线表（官方推荐值照抄，p445-451）

| 参数 | 推荐值/状态 | 备注 |
|---|---|---|
| Band Steering | Enable | 前提双频覆盖对等；5G 覆盖弱时禁用（p459） |
| 关联 RSSI/SNR 阈值 | 低 10 / 高 25 二选一 | 10 收弱终端拉低吞吐；25 拒弱终端保吞吐（p451） |
| 关联 RSSI（负载均衡版） | 2.4G=5、5G=10 | p445 |
| Dynamic Load Balance | Enable | — |
| 背景扫描 | Enable（WIPS 依赖）；间隔 20s / 时长 50ms 保持默认 | 范围 5-10800s / 50-110ms（p448） |
| Voice/Video Awareness | Enable | 检测 SIP/H.323 跳过扫描 |
| SGI | Enable（约 +11% 速率） | 环境差时关 |
| 信道/功率 | Auto（ACS/APC） | 优于静态 |
| 信道宽度 | 默认；密集=窄、稀疏=宽 | 2.4G 默认 20；5G 默认 40 |
| 功率范围 | 3-23 dBm（或 Auto） | — |
| 最小数据速率 | 2.4G=12、5G=24、6G=24 Mbps | — |
| 频段引导差值阈值 | 10（5G 与 2.4G 客户端数差） | — |
| 漫游 RSSI 阈值 | 2.4G=10、5G=15 | 关联阈值管"能不能连"，漫游阈值管"何时该走" |

RSSI 判读：dBm = RSSI − 96；RSSI<20（约 −76dBm 以下）Bad 不宜音视频，>30 为 Desired。

---

## 六、学习路径（10 个 skill 对应 5 天课程节奏）

| 天 | 顺序 | Skill | 对应书内容 |
|---|---|---|---|
| Day1 上午 | 1 | rlab-lab-manual | c01-c02 连接与重置（p69-80） |
| Day1 | 2 | express-mode-bootstrap | c03-c04/c08 模式判定+前置（p100-129/p33） |
| Day1 下午 | 3 | cirrus-license-org-lifecycle | c09 许可与组织（p169-238） |
| Day1 | 4 | device-cloud-onboarding | c10-c12 上云（p241-306） |
| Day1 末-Day2 | 5 | ssid-authentication-suite | c13-c16 三种 SSID+PSK 四级（p312-395） |
| Day2 | 6 | upam-policy-bandwidth | c17/c23 策略与账号（p408-434） |
| Day2 | 7 | rf-optimization-baseline | c18 RF 管理（p445-466） |
| Day2 | 8 | roaming-rap-design | 漫游章节 + c21 RAP（p476-572） |
| Day2 | 9 | wips-security-deployment | c19 WIPS（p514-525） |
| Day2 | 10 | site-survey-troubleshooting + 清理 | c22 勘测（p526-540）+ c20 清理（p544-547） |

---

## 七、交付陷阱 TOP10

1. **模式切换丢配置**：Express → Enterprise/Cloud 无配置迁移，集群配置全丢；切换前导出全部 SSID/密码/VLAN/Portal 账号，按"重新开局"排期（ce01）。
2. **255 上限**：Express 单组上限 255 台 AP，>64 台必须做弹性设计（每台 OmniSwitch ≤32 AP、每堆叠 ≤64，p11）。
3. **国家码射频全关**：AP 向导里国家码选错（或漏选），射频按法规全关、一个 SSID 都发不出来——Express 开局向导里改密/国家/建 SSID 一步都不能漏（c03/p108-119）。
4. **option 138 配错/序列号未声明 → AP 静默落 Express**：不报错，直接广播 mywifi-XXXX，还可能与已有集群意外成组；用 `getmode` 排查（ce02）。
5. **License 24h 延迟**：交付当天下单必卡现场；eBuy 订单最长 24h 才出现在 Subscription Manager（p175，ce06）。
6. **删 Site 是级联删除**：楼宇、楼层与设备归属连带删除，纳管关系丢失（ce36）；且云上无一键恢复，清理必须按依赖逆序拆 25 步（p544-547）。
7. **关联 RSSI 阈值设高于客户端信号 = 全网拒联**：隐蔽全局故障；实验里设 90 后客户端立即无法关联（c18/p456-466），变更后必看 QoE 并准备回 Default RF Profile（ce25）。
8. **WIPS 遏制杀伤半径**：de-auth 反制会波及邻居合法网络，参数过宽等于持续攻击别人；教材明令"未经指示不要改参数"（p523，ce32）。Friendly 一票豁免绝对有效，名单要定期复核。
9. **Band Steering 默认关有原因**：5G 覆盖弱/有洞时把终端逼进弱信号区；覆盖问题回勘测解决，不要用参数硬扛（p459，ce24）。
10. **UNP 自动分类的安全盲区**：AP 不过 802.1X，仿冒 AP 的 tagged 流量照样进内网 VLAN；高安全环境补 ACL/WIPS（p291，ce17）。另记："Factory Reset Required" 表示 VPN profile 变更过，唯一解是现场恢复出厂（ce14）。

---

> 本文由 cangjie-skill 流水线从 DT00XTE360EN 蒸馏生成。
