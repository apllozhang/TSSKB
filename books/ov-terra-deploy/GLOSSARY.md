# OmniVista Cirrus/Terra 术语表（GLOSSARY）

来源：DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration，整理自 verified.md glossary 候选（去重后 68 条），按类别分组，保留原书页码。

## 一、平台与产品

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| OmniVista Cirrus (OVC) | ALE 云管网络平台（SaaS 模式），统一管理 Stellar AP 与 OmniSwitch | <<<PAGE 5>>> |
| OmniVista Terra (OVTX) | OmniVista 的本地部署（On-Premises）版本，客户自托管 3-VM 集群，单租户 | <<<PAGE 13>>><<<PAGE 14>>> |
| Stellar / OmniAccess Stellar | ALE 无线品牌，Stellar AP 即 Wi-Fi 接入点产品线 | <<<PAGE 9>>> |
| OmniSwitch | ALE 有线交换机产品线，运行 AOS 系统 | <<<PAGE 9>>> |
| AWOS | Stellar AP 的操作系统软件（如 AWOS 4.0.6 GA） | <<<PAGE 9>>> |
| AOS | Alcatel-Lucent Operating System，OmniSwitch 操作系统（如 8.9R1） | <<<PAGE 9>>> |
| WebAdmin UI | Terra 管理 UI，端口 3000（<Node_IP>:3000），用于首装与 Admin Center | <<<PAGE 82>>> |
| Build (.7z) | Terra 的软件构建包，WebAdmin 上传后触发 K8s 部署 | <<<PAGE 76>>><<<PAGE 87>>> |
| EVC mode | VMware vCenter 集群的 CPU 兼容基线（需 Broadwell 及以上以支持 AVX/AVX2） | <<<PAGE 75>>> |

## 二、账号、组织与 License

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| MSP (Managed Services Provider) | 托管服务提供商，MSP 级用户可创建/配置组织并邀请用户 | <<<PAGE 47>>><<<PAGE 50>>> |
| Organization | Cirrus/Terra 的管理租户单元，可为一家企业或实体，含多个站点 | <<<PAGE 50>>> |
| Partner Account | 伙伴账号，创建后即为 MSP 级用户 | <<<PAGE 37>>> |
| Customer Account | 客户账号，挂接组织、不关联 MSP | <<<PAGE 42>>> |
| Trial Period | 组织试用期（Terra 组织自动激活 90 天 Trial），可申请后转订阅 | <<<PAGE 53>>><<<PAGE 110>>> |
| eBuy | ALE 渠道订购平台（ebuy.businesspartner.al-enterprise.com），License 下单入口 | <<<PAGE 25>>> |
| Subscription Manager | 订阅管理器，创建/管理订阅（续订、增购、延期、转移） | <<<PAGE 24>>><<<PAGE 26>>> |
| CAPEX Subscription | 买断式订阅，导入 License 时选择的订阅类型 | <<<PAGE 63>>> |
| Activation Code | 激活码，与 Subscription ID 一起用于在 OV 实例导入 License | <<<PAGE 63>>> |

## 三、设备纳管与激活

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| Device Catalog | 设备目录，设备宣告/清单/激活状态/激活日志所在应用 | <<<PAGE 145>>> |
| Activation Status | 激活状态，设备从宣告到 OV Managed 的状态机（Registered→Obtaining Certificate→…→Connected to OV） | <<<PAGE 146>>><<<PAGE 147>>> |
| OV Managed | 激活终态：设备已就绪可被完全管理 | <<<PAGE 147>>> |
| Call Home | 设备定期主动联系云/平台服务器的机制（交换机默认 30 分钟一次） | <<<PAGE 69>>><<<PAGE 171>>> |
| cloud-agent | OmniSwitch 上与 OV 云/平台对接的代理进程（CLI：cloud-agent …） | <<<PAGE 171>>> |
| ocloud | Stellar AP 上的云代理组件（证书存于 /.ocloud/ 目录，CLI：ocloud_show） | <<<PAGE 141>>><<<PAGE 150>>> |
| DHCP Option 43 | 厂商自定义 DHCP 选项，用于向设备下发激活服务器 URL（如 activation.myovterra.com） | <<<PAGE 141>>> |

## 四、无线配置模型

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| AP Group | AP 分组：同组共享配置（SSID/RF Profile/模板），与物理网络无关，每组最多 20000 AP | <<<PAGE 152>>> |
| Provisioning Configuration | 供给配置，绑定到 AP Group 的 AP 配置模板（必填 Name/Site/RF Profile/Timezone） | <<<PAGE 154>>> |
| SSID Usage | SSID 用途预设模板（Guest/Employee/BYOD/Enterprise 等），决定向导参数 | <<<PAGE 214>>><<<PAGE 218>>> |
| VLAN Pooling | VLAN 池：一个 SSID 分配最多 256 个 VLAN，避免大广播域 | <<<PAGE 224>>> |

## 五、认证与策略

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| UPAM (Unified Policy Authentication Manager) | 统一策略认证管理器：Guest/BYOD 接入 + 内置 RADIUS + 内置 MAC 认证服务器 | <<<PAGE 240>>> |
| Captive Portal | 强制门户：Web 认证页面，可定制 Logo/背景/按钮 | <<<PAGE 258>>><<<PAGE 259>>> |
| BYOD (Bring Your Own Device) | 员工自带设备接入，经 BYOD 门户注册认证 | <<<PAGE 241>>> |
| Guest Self-Registration | 访客自注册：访客自建账号，可由员工审批 | <<<PAGE 247>>> |
| Guest Operator | 访客操作员账号：前台/运营人员创建访客账号并审批自注册请求 | <<<PAGE 287>>> |
| Service Level | 访客服务等级：绑定 ARP+Policy List+注册 Profile+有效期+删除策略，最多 5 个 | <<<PAGE 282>>> |
| Registration Profile | 注册 Profile：按用户定义有效期、时间/数据配额及配额耗尽处理 | <<<PAGE 283>>> |
| Guest Tunneling | 访客隧道：按 ARP 从 AP 到交换机/路由器的 L2 GRE 隧道，可加备份隧道 | <<<PAGE 256>>> |
| GRE | Generic Routing Encapsulation，通用路由封装（L2 GRE 用于 L3 漫游与访客隧道） | <<<PAGE 256>>><<<PAGE 394>>> |
| Access Role Profile (ARP) | 接入角色模板：定义用户 VLAN、带宽、默认 Policy List 等 | <<<PAGE 220>>> |
| Access Auth Profile | 接入认证 Profile：有线端口认证方法（802.1X/MAC/CP）与 AAA 服务器绑定 | <<<PAGE 454>>> |
| Policy List | 策略列表：ACL/QoS 规则集合（Accept/Drop、限速、802.1p/DSCP 标记），双向执行 | <<<PAGE 264>>> |
| DSPSK (Device Specific PSK) | 设备专属预共享密钥：按 MAC 分配独立 passphrase（Force/Prefer 两档） | <<<PAGE 231>>> |
| PPSK (Private Group PSK) | 私有组 PSK：多个 passphrase 各绑一个 ARP | <<<PAGE 233>>> |
| Dynamic Private Group PSK | 动态私有组 PSK：条目同时绑定 VLAN ID 与 ARP，免去为每个 VLAN 建 ARP | <<<PAGE 234>>> |
| Walled Garden | 围墙花园：社交登录等认证前放行的预授权域名范围 | <<<PAGE 219>>> |
| RadSec | 基于 TCP/TLS 的 RADIUS 安全传输 | <<<PAGE 8>>> |

## 六、射频管理

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| RF Profile | 射频模板：国家码、Smart Load Balance、扫描、信道/功率设置 | <<<PAGE 366>>><<<PAGE 367>>> |
| DRM (Distributed Radio Management) | 分布式射频管理：AP 间空口发现邻居 + LAN 上共享 RF 上下文，各 AP 自主射频决策 | <<<PAGE 364>>> |
| ACS (Auto Channel Selection) | 自动信道选择，管理员可在 DRM 中限定 5G/6G 候选信道列表 | <<<PAGE 368>>> |
| Smart Load Balance | 智能负载均衡（含 Band Steering 与 Dynamic Load Balance） | <<<PAGE 370>>> |
| Band Steering | 频段引导：把客户端引导到 5G/6GHz 频段 | <<<PAGE 370>>> |
| Dynamic Load Balance | 动态负载均衡：相邻 AP 按负载计时，引导新客户端接入最轻负载 AP | <<<PAGE 372>>> |
| Smart Air Share | SSID 级速率控制（2.4G 最低速率建议 12、5G/6G 建议 24）提升 802.11a/n 客户端体验 | <<<PAGE 369>>> |
| Scanning (Background) | 背景扫描：射频周期扫空口，WIPS 必需；默认间隔 20s、时长 50ms | <<<PAGE 373>>> |
| RSSI | Received Signal Strength Indicator 接收信号强度指示（OV 上为平均值，AP 上为瞬时值） | <<<PAGE 378>>> |

## 七、安全（WIPS）

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| WIPS / WIDS | 无线入侵防护/检测系统：识别 Interfering/Rogue/Friendly AP 并自动反制 | <<<PAGE 384>>> |
| Rogue AP Containment | 流氓 AP 反制：扫描 AP 向 Rogue AP 的客户端发 de-auth（默认启用） | <<<PAGE 384>>> |
| WIPS Attack Containment / Client Blocklist | 攻击反制的客户端黑名单（默认禁用，仅对真实无线客户端 MAC 有意义） | <<<PAGE 387>>> |

## 八、漫游与无线回程

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| Sticky Client Avoidance | 粘滞客户端规避：用 802.11k/v + Roaming RSSI 阈值引导客户端切换 AP | <<<PAGE 404>>><<<PAGE 416>>> |
| OKC (802.11k) | Opportunistic Key Caching，密钥缓存快速漫游，仅 WPA2/WPA3 Enterprise | <<<PAGE 402>>> |
| 802.11r (FT) | Fast BSS Transition 快速漫游，仅 WPA2/WPA3 加密（Personal 或 Enterprise） | <<<PAGE 402>>> |
| RAP (Remote Access Point) | 远程接入点：经 VPN 隧道把企业网络延伸到远程站点/家庭办公 | <<<PAGE 420>>> |
| WiFi Bridge | Wi-Fi 桥接：替代物理布线连接两地网络，不给无线客户端提供服务 | <<<PAGE 437>>> |
| WiFi Mesh | Wi-Fi 网状网：AP 间无线回程（最多 16 AP/4 跳），同时可服务客户端 | <<<PAGE 437>>><<<PAGE 439>>> |
| Auto Mesh | 自动 Mesh：LAN 上的 root AP 广播隐藏 SSID "Stellar-MESH"，未联网 AP 自动入网 | <<<PAGE 440>>> |

## 九、有线与运维

| 术语 | 中文解释 | 页码 |
|------|---------|------|
| UNP | Unified Network Policy，OmniSwitch 上的统一网络策略（有线客户端/port 视图） | <<<PAGE 193>>><<<PAGE 313>>> |
| Golden Configuration | 黄金配置：交换机基准备份配置，偏离则 Non-Compliant | <<<PAGE 195>>> |
| QoE Analytics | 体验质量分析：连接时间/漫游时间/RSSI/信道利用率/uptime 及失败原因 | <<<PAGE 292>>> |
| Heat Map | 热图：按站点/AP 展示覆盖与客户端密度（红高/黄中/绿低），最少 3 个 AP | <<<PAGE 337>>> |
| IoT Device Profiling | IoT 设备识别：基于 MAC OUI 与 DHCP 指纹（option 55/60）分类并映射 ARP | <<<PAGE 464>>> |
