# 全书精华串讲

## 一句话主线

终端在局域网（交换机/AP）上通过 MAC、802.1x 或 captive portal 完成一次认证，UPAM 体系把"IP ↔ 用户名/角色"的映射推给下一代防火墙，防火墙从此按身份而非仅按 IP 做策略、日志与取证——这就是 UPAM 与防火墙 SSO 集成的全部要义。

## 为什么值得做：零信任

传统防火墙按"接在哪里"划分信任，内网隐式可信。移动办公与 IoT 让这套失效：BYOD 可能带毒、IoT 设备天然脆弱、内部用户也可能恶意。零信任的核心动作是先确认身份，再谈授权。下一代防火墙（Fortinet FSSO、PAN User-ID）为此准备了身份接收机制，缺的只是一个可靠的身份源——对没有 AD 账号的 BYOD/IoT 终端，这个身份源就是 UPAM。

## 先做路线判断

- 终端是 AD 域设备 → 集成点直接放 AD/NPAS，走防火墙厂商的 AD 集成文档，不要绕道 UPAM。
- 终端是 BYOD/IoT，直接对 UPAM 本地库（或 AD 之外的外部 RADIUS）认证 → 集成点就是 UPAM，即本书两条配置线的主题。

## 身份怎么推：两条通道

| | Fortinet（FSSO/RSSO） | PAN（User-ID） |
|---|---|---|
| 协议 | RADIUS Accounting | Syslog |
| 端口 | UDP 1813 | UDP 514 |
| 发送方 | 交换机/AP 直发（不经 UPAM） | UPAM 自身 |
| 角色字段 | Filter-Id（=ARP/uNP 名） | filterID（=ARP/uNP 名） |
| 防火墙侧组织 | RSSO 用户组（Attribute Value=ARP 名） | Syslog Parse Profile + 策略直接引用角色 |

两种方案里 UPAM 侧前半段配置几乎一致：AAA Server Profile → Authentication Strategy + Access Policy → Access Auth Profile 挂到交换机/AP 组。差别从"记账发往哪"开始分叉。

## 身份映射的三个关键设计决策

1. **映射用户名还是角色**：MAC 认证下用户名就是 MAC 地址，拿它做策略可读性差。按角色（Filter-Id/filterID）做策略最省事，防火墙本地零用户；代价是防火墙日志只见角色不见真实用户名——补救办法是让 UPAM 同时向另一台 syslog 服务器发一份日志留档，靠时间同步做取证关联。
2. **设备 IP 何时到位**：DHCP 要等认证后才完成，认证成功消息里通常没有 IP，真正的映射信息在 accounting 消息里。所以 interim accounting 必须开（默认 600 秒一次）；若设备 IP 出现在第二笔起，调小 interim 能加快防火墙侧更新。
3. **超时与登出**：PAN 侧每个 syslog 源只能挂一个解析过滤器，笔记选了信息最全的 Accounting 过滤器，因此过滤不了 Disconnect——用户断线后映射要等 User Identification Timeout（默认 45 分钟）收不到更新才清除。硬约束：interim interval 必须小于这个超时，否则活跃用户会被误登出。

## 排障检查清单（两方案通用 + 各自专属）

- 通用：默认 ARP 是否先建好并映射到交换机/AP 组；Access Auth Profile 是否已套用到设备；中间链路是否放行对应 UDP 端口（1813/514）。
- Fortinet：RSSO 连接器属性必须 SSH 用 CLI 配（GUI 做不了）；两处共享密钥必须一致；RSSO 用户组的 Attribute Value 必须逐字等于 ARP 名。验证：Firewall Users 面板 / `diagnose firewall auth list`。
- PAN：syslog 连接测试报"连不上"是预期行为（PAN 不回应测试）；Interface Management 里要勾 Syslog Listener 并登记 UPAM IP、套到接收接口；策略里角色一律小写。验证：`show user ip-user-mapping all` / Monitor → Logs → Traffic。

## 收益收口

集成完成后：可视化按用户/角色而非 IP；策略实现最小权限（只放有业务需要者）；日志、报表与取证按用户/角色过滤，缩小攻击面。两份笔记的结论章对此表述几乎逐句一致。
