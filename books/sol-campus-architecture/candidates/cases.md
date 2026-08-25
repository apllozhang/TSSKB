# cases — sol-campus-architecture（C1…，部署/配置流程）

- **C1 VLAN 域 AP 发现配置流程**：`vlan 125 name "AP Management VLAN"` → 上联口打标 `vlan 125 members port 1/1/24 tagged` → `unp profile defaultWLANProfile map vlan 125` → AP 口设 UNP bridge `unp port 1/1/1 port-type bridge` → 按需 `unp port 1/1/1 ap-mode` → `mvrp enable` 传播管理与客户端 VLAN → 可选关认证/配 QoS 策略列表/认证旗标 → 配 system name/location/端口 alias 供 LLDP 向 AP 传位置信息 <<<PAGE 23>>>
- **C2 服务域（SPB）AP 发现配置流程**：`service l2profile "ap-SvcUnp" 802.1ab peer` → `unp port 1/1/1 port-type access` + `l2-profile ap-SvcUnp` + `ap-mode` → `unp profile defaultWLANAccessProfile map service-type spb tag-value 0 isid 1000 bvlan 4000` → 为客户端建服务画像 `unp profile spb10 map service-type spb tag-value 10 isid 1010 bvlan 4000` → 分类规则 `unp classification vlan-tag 10 profile1 spb10` <<<PAGE 25>>>
- **C3 AP 安全模式认证时序**：AP 发 LLDP-MED TLV 自证身份 → 交换机 UNP 规则归入 defaultWLANProfile 并回发带 Port VLAN ID 与位置的 LLDP → EAP Identity Request/Response → 802.1x 服务器认证成功 → AP 经 DHCP 拿地址并从 Option 138 得 OmniVista 地址 → MQTT 建管通道接收配置 <<<PAGE 20>>>
- **C4 Trust Tag 接纳客户端 VLAN**：AP 上线的客户端 DHCP 流量带 SSID 对应 VLAN tag → 交换机信任该标签并匹配本地 VLAN → 无则自动创建 → MVRP 向邻居分发 <<<PAGE 21>>>
- **C5 漫游判定操作矩阵**：新 AP 无客户端上下文→按新客户端处理；有上下文且 WLAN 服务/ARP 与 VLAN 映射一致→L2 漫游；有上下文但 VLAN 不匹配→L3 漫游（L2GRE 隧道回家乡 AP）<<<PAGE 26>>>
- **C6 L2GRE 隧道建立流程**：隧道接入交换机与汇聚交换机各配端点 → UNP 口收到的流量按 L2/L3 方法分类进 UNP 画像 → 画像映射 L2 GRE 服务 → GRE 封装送到汇聚交换机 → 解封装后进 VLAN 域上 perimeter/Internet <<<PAGE 17>>>
- **C7 mDNS 网关模式部署**：边缘交换机把 mDNS/SSDP 流量转发到网关交换机 → 网关按预配置 VLAN 共享列表在所有 VLAN 复制转发 <<<PAGE 33>>>
- **C8 mDNS Responder 模式部署**：核心交换机跑 Responder → 边缘交换机配 standard 型 L2GRE 隧道指向 Responder → 独立建 server policy 与 client policy → service rule 关联两者决定"哪些服务共享给哪些请求" <<<PAGE 33>>>
- **C9 RAP 远程接入流程**：AP 启动连 OmniVista Cirrus 按 MAC 识别 → 下发 VPN 服务器公网 IP、VPN 客户端 IP、SSID/射频参数与 OmniVista Enterprise 地址 → 双 VPN 建立后 OmniVista 2500 下发完整配置 → 远端用户连 SSID 经隧道入公司网，可拆分隧道直上互联网 <<<PAGE 31>>>
- **C10 OmniVista HA 部署选型**：Standalone 单机无故障切换；L2 HA 双 VM 同子网 + 虚拟 Cluster IP（原单机 IP 可复用）；L3 HA 双节点跨子网各持 IP，设备需同时配置双节点地址，Preferred Node 须在 CLI admin 菜单设置 <<<PAGE 35>>>
- **C11 AP Onboarding 流程**：AP 初联自动回连 Cirrus Activation Server → 序列号对 Device Catalog 校验 → 发证书建 VPN → 注册/授权/按 AP 组模板自动下发配置 <<<PAGE 36>>>
- **C12 WCF 配置三步**：建 WCF Profile（可含多条过滤条件）→ 给 ARP 或 SSID 挂 WCF Profile → 将 ARP/SSID 应用到 AP <<<PAGE 41>>>
- **C13 Mesh 建网约束**：有线上联者为 mesh root、无线上联者为 pure mesh；每 AP 最多 5 SSID + 5 条点对多点连接；全网最多 16 台 AP、任一链路最深 8 跳 <<<PAGE 29>>>
- **C14 访客认证四方式部署**：嵌入式 Captive Portal 自注册 / 社交登录（Facebook、Google、Rainbow、微信）/ 员工或访客操作员赞助审批 / SMS（Plivo）取凭证；默认记录保留一个月，可外接日志服务器延长 <<<PAGE 39>>>
- **C15 BYOD 注册管控**：用户经 UPAM Captive Portal 声明设备 → 挂符合安全策略的 ARP → 施加时限、会话超时、每人 1–10 台限制；认证源可选本地库/AD(LDAP)/代理外部 RADIUS <<<PAGE 40>>>
