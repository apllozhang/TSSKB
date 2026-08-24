# DIGEST · Stellar WLAN 高级排障精华（不读全书版）

> 目标读者：接手 Stellar Wi-Fi 故障的一线工程师。看完这一篇，能按流程定层、按表敲命令、按阈值下判断。页码对应教材 DT00XTE478EN（187 页）。

## 一、一页看懂无线排障

这本书讲的是"Wi-Fi 怎么修"，核心就两件东西：**七步流程**和**三域根因地图**（p3-18）。

**七步流程**（带一条回退规则）：

1. **Identify 识别**——先问问题、收信息，确认问题真实存在
2. **Locate 定位**——绑定物理空间和具体设备，用 OSI 模型定层
3. **Isolate 隔离**——锁定具体层、设备、位置、驱动版本
4. **Re-Create 复现**——在自有环境重建；**复现不了就回第 1 步重新提问**（p10）
5. **Solve 解决**——制定并实施方案
6. **Verify 验证**——充分测试确认修复有效，让客户用日常业务（Rainbow、语音、邮件）跑
7. **Document 记录**——问题描述/拓扑/固件版本/诊断/解决方案五字段归档，沉淀 TKC（p13-14）

**三域根因地图**——排障前扫一遍，保证不漏层（p5-8）：

| 域 | 检查要素 |
|---|---|
| 无线侧 | 终端技能/驱动、射频能力、802.1X 配置文件、漫游算法、RSSI/SNR 覆盖、AP 配置与固件 |
| 本地网络侧 | PoE/布放、交换机 VLAN/QoS、防火墙 ACL、DHCP（租期/地址池/选项）、DNS、RADIUS/LDAP/AD |
| 互联网侧 | 出口带宽、抖动时延、外部 DNS、外部门户——不在你管控内，先划出去再排 |

配套的**访谈四问**逐级收窄（p17）：所有用户都受影响？（排除个别终端）→ 固定位置还是全楼？（排除全局配置）→ 都挂同一接入交换机下？（指向 SSID 或交换机配置）→ 同位置其他 SSID 正常？（锁定单个 SSID 的 VLAN/配置）。

全书主案例（p11-18）就是这么破的：全员连不上 Employee SSID，访谈锁定范围后比对配置——OmniVista 里 SSID 映射 VLAN 10，接入交换机配的是 VLAN 20，tagged 不一致。改交换机 VLAN 解决。教训：**全员连不上而 AP 本身正常，优先怀疑交换机侧 VLAN，别先动无线配置。**

动手前还有一条纪律：全网先对齐 NTP（p22）。教材演示过无 NTP 的代价——AP 日志和 OmniVista 时间差五天，时间线对不上，关联分析全部作废。

## 二、排障决策树总图

```
接手故障
├─ 先对时（NTP）→ 访谈四问 → 三域扫一遍 → OSI 从低层往高层定层
│
├─ AP 整体不对劲（灯不对/疑似重启/高 CPU/门户不弹页）
│   → 查基础层：LED 判读（免登录）→ showsysinfo/showver/getmode
│     → date → uptime → 日志找重启原因 → top/ps 查进程 → eag_cli 查门户
│
├─ SSID 没广播 / RF 配置疑似没生效 / 换位置掉线（漫游）
│   → 查无线层：iwconfig 看 athXYY 接口与 BSSID
│     → cat /tmp/config/rfprofile.conf 比对落地
│     → adme show 查邻居表（RSSI<20=差）→ wam.log 搜 roaming-start/success
│
├─ 单个客户端连不上 / 没地址 / 频繁掉线
│   → 查客户端层：sta_list 六字段 → wam_debug 看认证 JSON
│     → 没地址：双端抓 DHCP 四步 → 查 VLANID 与 Final_role
│     → 掉线：iwlist txpower → rfprofile 阈值 → grep disassoc reason（reason 8=负载均衡，结案）
│     → 802.1X 认证失败：客户端四查 → AP 三份 AAA 配置文件 → RADIUS 服务器七查
│
├─ AP 自己拿不到 IP / ping 不通网管 / 日志不上报
│   → 查网络层：cat /etc/config/network 查 proto
│     → 上联口抓 DHCP（NAK 判据）→ ifconfig br-wan → route -n → ping 逐跳 → traceroute
│     → syslog 三步：syslog.conf → ps grep logread → logger 实测
│
└─ 整网/整区域表现不佳（覆盖/干扰/布点）
    → 勘测：被动+主动组合 → 三步法 → 五发现五动作
```

分层口诀：**先低层后高层**（p38-102）。一上来怀疑认证/DNS，实际是 PoE/VLAN 底层问题，是最常见的弯路。

## 三、必背命令与阈值速查表

**登录通道（p23-26）**

| 通道 | 参数 | 备注 |
|---|---|---|
| 串口 | 115200 / 8 数据位 / 1 停止位 / 无校验 / 无流控 | 没 IP 时唯一入口 |
| SSH | `/var/config/public_group.conf` 里 `ssh_connect=1` | support 账号；实验室默认密码 aos2016，生产以 AP Group 自定义为准 |
| Web UI | `https://<AP_IP>` 或 `http://<AP_IP>:8080` | 云管模式先在 Cirrus 开 "AP web" |

**CLI 工具箱**

| 命令 | 用途 |
|---|---|
| `ssudo sta_list` | 客户端 VLANID/IPv4/OnlineTime/RX/TX/AUTH/Final_role 六字段（p78） |
| `ssudo wam_debug sta_list` | 认证 JSON：assignedVLAN / macAuthResult / CPAuthResult |
| `wlanconfig athXX list` | RSSI/SNR/终端能力 |
| `iwconfig` / `iwlist athXXX channel\|txpower` | 接口与 BSSID / 实际信道与功率 |
| `cat /proc/kes_syslog \| grep <MAC>` | disassoc reason 判读（reason 8=负载均衡，p80） |
| `cat /tmp/config/rfprofile.conf` | RF 配置落地比对（p63-69） |
| `adme show` | 邻居表：channel/rssi/txpower，RSSI<20 判差（p69, p96） |
| `ssudo tcpdump -i br-wan -w x.pcap <过滤>` | 有线抓包（注意接口是 br-wan，不是 eth0，p30） |
| `eag_cli show user all` | 门户认证表项（p55） |
| `showsysinfo / showver / getmode / show_cluster` | 国家码/版本/管理模式/集群 |

**RSSI-SNR 判读（Stellar 正值刻度，dBm = RSSI − 96）**

| RSSI 值 | 换算 | 判定 |
|---|---|---|
| 10 | −86dBm | 差，语音/实时应用不可用 |
| 29 | −67dBm | 语音推荐下限（硬指标：RSSI≥29 且 SNR≥25） |
| 43 | −53dBm | 完美 |
| <20（邻居表） | — | 差信号，漫游病灶（p69） |

**端口与协议清单（p89-90, p170, p179）**

| 用途 | 端口/选项 |
|---|---|
| RADIUS 认证/计费 | 1812 / 1813（timeout 5、retries 2） |
| OmniVista 云管防火墙入向 | 9093、30123-30125 |
| 出向放行 | 443、80、123（NTP）、53（DNS） |
| DHCP 标准选项 | 1、2、6、28、42、43（代理另加 129-133、138） |
| syslog | 默认 514 |

空口抓包硬上限 **10MB / 5 分钟**（p31），规划过滤条件按此预算。

## 四、十大高频故障根因清单

1. **交换机 tagged VLAN 与 SSID 映射不一致**（p11-18）——全员连不上而 AP 正常，先查这里。
2. **Final_role 滤掉 DHCP**（p84）——最隐蔽的"永远拿不到 IP"：报文路径全正常，角色里没放行 DHCP。
3. **AP 发射功率被压到最小**（p85-86）——`iwlist txpower` 见 3dBm（1mW）+ RSSI 16，去 RF profile 调大。
4. **signalStrengthThreshold 过高**（p87）——阈值 70（约 −26dBm）时正常信号也被踢，功率再对也掉线。
5. **RADIUS 共享密钥不匹配**（p89）——静默失败：不报错、只见超时，逐字符比。
6. **RADIUS station IP 未登记 AP 地址**（p90）——请求被服务器直接丢，客户端只见超时。
7. **国家码不兼容导致搜不到 SSID**（p82）——showsysinfo 查国家码，不匹配就在 RF profile 手动指定兼容信道。
8. **untagged↔tagged VLAN 之间不漫游**（p69）——产品限制，信号再好也漫不过去；同 SSID 各 AP 的 VLAN 封装必须一致。
9. **地理邻居互相看不见**（p70）——直角走廊等建筑阻挡；两台 AP **对称**静态互加邻居，上下文改走 LAN。
10. **同频/邻频干扰**（p112）——吞吐下降、丢包、数据损坏三症状，换信道；用 Ekahau/WiFi Analyzer 定位重叠。

另有两条"别误判"：reason 8 掉线是系统负载均衡行为，不按故障修（p80）；AP 拿不到地址时"连 DHCP-NAK 都没有"说明报文根本没到服务器（链路/VLAN/中继问题），别当地址池耗尽（p100）。

## 五、勘测三步法与五发现五动作

三类勘测按阶段选（p106-107）：部署前用**预测**（仿真摆 AP）；部署后用**被动**（只听不关联，测信号与噪声）查 RF、用**主动**（真实关联，测丢包/重传/物理速率）查性能；排障时被动+主动组合。

**现场三步法**（p114-117）：

1. **拿图纸**——标障碍物/墙体/层高、优先覆盖区、AP 位置
2. **勘测观察五项**——AP 型号与原设计一致？RF 重叠干扰？无覆盖区？发射功率还是默认值？位置别扭？
3. **纠正动作五类**——换 AP 型号 / 重做 RF 设计 / 收窄信道宽度 / **移除低数据速率**（逼终端贴近好 AP，常被忽略）/ 改善布放

材料衰减要有敬畏（p110）：4 米穿 1-4 面墙 RSSI 就掉到 −70dBm——上网够、语音不够（语音要 −67dBm 以上）。衰减大户：混凝土墙、金属柜、钢结构、玻璃镜、砖体、水。天线装反（定向进开放区、全向进走廊）会造出"一半没信号、一半过剩"，盲区先查天线。

## 六、学习路径（8 个 skill 的顺序）

1. **wlan-trouble-methodology**——总纲：七步流程、三域地图、访谈四问。任何故障先过这里。
2. **stellar-ap-toolbox**——取证手段：串口/SSH/Web 登录、tcpdump 与空口抓包、配置备份。
3. **stellar-ap-system-health**——基础层：LED、系统、进程、门户（eag）、Express 集群。
4. **wireless-rf-roaming-trouble**——无线层：athXYY 接口、RF profile 落地、邻居表、漫游验证。
5. **client-connection-trouble**——客户端层：搜不到/连不上/没地址/掉线四条决策链。
6. **dot1x-radius-trouble**——认证专项：客户端→AP→RADIUS 三段十三查。
7. **network-side-trouble**——网络层：AP 取址、连通性、syslog、云管上线前置。
8. **site-survey-remediation**——收口：整网表现不佳时的勘测与整改。

前两个是通用底座，中间四个按 OSI 分层对应症状，最后一个是面状问题的收口。

## 七、边界提醒：何时升级 TAC / TKC 怎么用

**TKC 检索三分支**（p127-130）：疑似已知问题时查 TKC——同版本直接看 Resolution；案例版本更旧，可能已被新 build 修复；**套用任何用例前必须亲自重复其诊断步骤且结论一致**，否则换用例或联系技术支持创建新用例。

**该开票升级 TAC 的信号**：

- 进程列表出现 X（Dead）/ Z（Zombie）堆积——软件问题，附进程列表上报，别反复重启掩盖（p51-53）
- 高 CPU 疑似进程死循环（软件缺陷）（p52）
- 出现两个 cluster_mgt 线程（一运行一睡眠）——产品特定异常信号（p59）
- 自有环境复现失败、访谈再收窄也无果——回流程第 1 步；仍无进展即建新 TKC 用例

配置备份 pub-config.tar 是工单标准共享材料（p33），开票前先备好。

---
由 cangjie-skill 流水线从 DT00XTE478EN 蒸馏生成。
