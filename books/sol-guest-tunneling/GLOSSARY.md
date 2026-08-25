# GLOSSARY · Guest Traffic Tunnelling Services Application Note

> 页码为原书 `<<<PAGE N>>>` 标记。

- **GTTS（Guest Traffic Tunneling Services，访客流量隧道服务）**：OmniAccess Stellar 与 OmniSwitch 联合特性，把无线用户流量从 AP 灵活隧道到一台或多台 OmniSwitch 隧道聚合端点；虽名为"访客"，也用于安全策略旁挂与架构迁移。<<<PAGE 3>>>
- **L2 GRE（Layer 2 Generic Routing Encapsulation，二层通用路由封装）**：GTTS 底层协议，在 IP 网上承载二层 overlay，识别并隔离设备流量；以 service 形式实现，可关联 UNP profile，实现思路同 OmniSwitch VXLAN。<<<PAGE 4>>>
- **tunnel aggregation switch（隧道聚合交换机）**：L2 GRE 隧道的交换机侧终点，通常部署在 DMZ 等防火墙围护的安全区；解封装后经 Hairpin 把流量送入 VLAN 域。<<<PAGE 4>>>
- **Hairpin**：同一台交换机上两个端口用一根线自环；一侧 SAP 口出隧道，另一侧 ACCESS 口落 VLAN；其线速封顶 SSID 带宽。<<<PAGE 4>>>
- **SAP port（Service Access Point port，业务接入点端口）**：Hairpin 的隧道侧端口，创建 service 并映射到此口，隧道流量从此出隧道；冗余设计中可换成 linkagg。<<<PAGE 4>>>
- **ACCESS port（Hairpin 的接入侧端口）**：Hairpin 另一侧的普通传统接入端口，映射 VLAN；隧道流量由此进入 VLAN 域，下行流量反向先经此口进隧道。<<<PAGE 4>>>
- **ARP（Access Role Profile，访问角色档案）**：Stellar 的角色配置对象（含 ACL/QoS/用户 VLAN/Portal 等）；GTTS 隧道粒度可细到 ARP 级，每个 ARP 同一时刻只对应一条活跃隧道。<<<PAGE 3>>><<<PAGE 7>>>
- **Tunnel Profile（隧道档案）**：包含建立 L2 GRE 隧道全部参数的配置对象；单 SSID 多 ARP 场景下每个 ARP 各映射一个 Tunnel Profile，在 OV2500 Expert 模式创建。<<<PAGE 5>>><<<PAGE 11>>>
- **VPN ID**：service l2gre 的隧道标识，AP 侧 Tunnel ID、主备交换机 vpnid 必须一致，AP 依此开隧道；与 ACCESS 口 VLAN ID 不必相同。<<<PAGE 9>>><<<PAGE 16>>>
- **Tunnel ID**：AP 侧 SSID 隧道配置中的隧道编号，必须与交换机侧配置一致。<<<PAGE 10>>>
- **GRE Tunnel Server IP / Data VPN Server**：SSID 隧道配置中主隧道聚合交换机的 IP 地址。<<<PAGE 10>>>
- **Backup GRE Tunnel Server IP**：备隧道聚合交换机 IP；与 Primary 无同/异网段要求，失联 Primary 时隧道切换到此机（R2 冗余）。<<<PAGE 10>>><<<PAGE 17>>>
- **Preemption（抢占）**：R2 冗余选项；Primary 恢复后按 Preemption Countdown Timer 到期回收 Master 角色，AP 把全部会话迁回 Primary。<<<PAGE 10>>><<<PAGE 17>>>
- **Entropy（熵）**：AP 侧 SSID 隧道配置项，文档以 Important 标注必须启用，否则 GTTS 不可用。<<<PAGE 10>>>
- **auto-discover（自动发现）**：交换机特性，动态接受远端 AP 发起的隧道；默认开启，关闭则需逐台手工登记 AP MAC。命令 `service l2gre auto-discover enable`。<<<PAGE 8>>>
- **l2profile（L2 服务档案）**：交换机侧服务端口模板，建 GTTS SAP 口时创建并丢弃 stp/gvrp/mvrp，配合 vlan-xlation 启用。<<<PAGE 9>>>
- **vlan-xlation（VLAN translation，VLAN 转换）**：service access port 与 service 上的开关，Hairpin 两侧 VLAN 映射所需。<<<PAGE 9>>>
- **One ARP 规则**：每台 AP 同一时刻对一个 ARP 只能有一条活跃隧道指向一台聚合交换机；N 个不同 ARP 的隧道 SSID 需要 N 台聚合交换机。<<<PAGE 7>>>
- **Layer 3 hop（三层跳变）**：强制架构前置——AP 管理 IP 与 GRE Tunnel Server IP 必须不同子网，中间存在三层路由。<<<PAGE 7>>>
- **Virtual-Chassis（虚拟机箱）**：OmniSwitch 堆叠技术；R3 冗余用它替代 Primary-Backup，两台聚合交换机组 VC 后配合跨成员 linkagg 实现亚秒收敛。<<<PAGE 17>>>
- **DMZ（Demilitarized Zone，非军事区）**：企业内网与外部网之间的缓冲区，由防火墙分隔；GTTS 聚合交换机与专属 DHCP 通常部署于此。<<<PAGE 4>>><<<PAGE 11>>>
- **Multi-tenancy（多租户）**：运营商场景下多个客户的流量集中终结于同一台（或多台）GTTS 聚合交换机且保持客户间逻辑隔离；每客户一个 AP Group，链路可为 SD-WAN/SPB/MPLS。<<<PAGE 3>>><<<PAGE 13>>>
- **AP Group（接入点组）**：GTTS 的配置粒度单位；组内 AP 广播同一 SSID 指向同一隧道终点，是园区多站规模化与多租户隔离的基础。<<<PAGE 3>>><<<PAGE 12>>>
- **Filter-id**：802.1X 认证返回字段，可用于把一个 SSID 的用户分类到不同 ARP，进而进不同隧道。<<<PAGE 5>>>
- **linkagg / LACP（链路聚合）**：R1/R3 冗余中把 Hairpin 的 SAP 侧与 ACCESS 侧各自做成聚合（跨 VC 成员则双机各出一口），端口级冗余并提升 Hairpin 带宽。<<<PAGE 15>>><<<PAGE 17>>>
