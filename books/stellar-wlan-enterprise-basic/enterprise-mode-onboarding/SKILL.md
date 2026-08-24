---
name: enterprise-mode-onboarding
description: 何时用：Stellar AP 以 Enterprise 模式开局——网络要求、DHCP option 138、OV2500 许可与发现、AP 注册入组、交换机 UNP 纳管。
source_book: DT00XTE368EN Stellar WLAN Enterprise Basic
---

# Enterprise 模式开局（OV2500 发现与 AP 纳管）

## R · 原文引用

> "1. AP is connected to the network and powered on. AP sends a DHCP request. 2. AP determines IP of OV2500 if option 138 is returned by DHCP server. AP is set in Enterprise mode. 3. AP contacts OV2500 for registration. 4. OV2500 assigns an AP Group to the AP. OV2500 applies the configuration to the AP." (p242)

> "AP is managed when Registration succeeds: AP is Trusted; AP is Licensed; Country Code matches RF profile CC. AP is unmanaged when Registration fails... Configuration not applied & All Radios are off." (p243)

> "1. AP sends LLDP. 2. AP classified in defaultWLANProfile -> VLAN 125 assigned. 3. AP sends untagged DHCP, get IP on vlan 125. 4. Switch sends LLDP with Port LAN ID and AP Location." (p236-237)

> "Management Plane: AP management traffic is always untagged... Wireless traffic always tagged on the AP uplink. No tunnel mode to OV... Data Plane is only L2." (p159-163)

## I · 方法论骨架

1. **模式选型**：Express（自组集群，PVM 选举，上限 255）/ Enterprise（OV2500 本地管，上限 4000）/ Cloud（Cirrus）；本 skill 主线为 Enterprise。
2. **四件套最低要求**：AP（出厂净化态）+ PoE 交换机（管理 VLAN + dhcp-relay）+ DHCP 服务器（管理 VLAN 作用域带 option 138 + 业务 VLAN 地址池）+ OV2500（IP 配置 + 许可）。
3. **上线四步**：上电 LLDP 选管理 VLAN → DHCP option 138 切 Enterprise → 向 OV2500 注册 → 分配 AP Group 下发配置。
4. **受管三条件**：Trusted + Licensed + 国家码匹配 RF Profile；任一失败即 Unmanaged、配置不下发、射频全关。
5. **三平面规则**（排障抓包必背）：管理流量不打标、业务流量在 AP 上联口打标、无隧道模式、数据面纯 L2。
6. **配置模型**：一切以 AP Group 为单位；UNP 让接入口免预配置（LLDP 分类→分管理 VLAN→上报位置）。

## A1 · 书中案例（Lab 精要）

- c02：OV2500 首登（admin/switch 改密），lds.al-enterprise.com 生成 EVAL 许可（Customer ID 99999 / evaluation / omnivista），文件与 key 两种装法二选一。
- c03：三台 OmniSwitch SNMPv3 发现——`user snmpuserv3 read-write all password "Superuser=1" sha+des` + `snmp station <OV IP> 162 snmpuserv3 v3 enable`，OV 侧超时 5000ms/重试 3/SHA+DES，Discover Now。
- c04：建管理 VLAN 40，AP 端口 enable + `lanpower` 重启 PoE，dhcp relay 回 option 138，国家码选 FR-France（实验室禁选 USA/日本/以色列），Unmanaged→Change to Trust Status，入组 APGX。串口排障链：`getmode`/`getovinfo`/`ssudo ifconfig br-wan`/`tcpdump` 抓 DHCP Offer。

## A2 · 触发场景（含与相邻 skill 的区分）

- AP 上线/注册/纳管/许可/HA/拓扑位置类问题——用本 skill。
- AP 已受管，接下来建 SSID、接 AD、配访客——转 employee-ssid-8021x / upam-guest-access。
- 远程站点经互联网接回总部——转 rap-remote-deployment。

## E · 可执行步骤

1. 核对四件套与最低配置清单（p16 条目：PoE/管理 VLAN/ip dhcp-relay/option 138/地址池/OV 许可）。
2. DHCP 配 option 138=OV2500 IP：isc-dhcp 先 `option ovwma code 138 = ip-address;`（vendor-class 以 "HAP." 开头可分类）；OmniSwitch 直接 `option 138 x.x.x.x`；Windows Server 走预定义选项 Code 138。
3. 导入 OV2500 许可：AP 许可数 > 待部署 AP 总数；HA 每对服务器一枚；WCF 按 1:10 AP。
4. 交换机侧（可选 UNP 自动化）：接入口配 UNP port-type bridge、关 trust-tag、建 LLDP 分类规则映射管理 VLAN。
5. AP 上电后按四步链路验证；注册失败查三条件（Trust/License/国家码）。
6. AP Location 语义化：接入口配 port alias > system location > system name > 默认机箱 MAC:端口。
7. HA 规划：主备 OV 经二层（或 VxLAN/SPB）互联，设备对虚拟 IP 通信。

## B · 边界与陷阱

- Express 切 Enterprise 不迁移配置，集群配置全丢——变更窗口预留重建时间。
- AP 不出现的五查：Managed 页→option 138（缺失/填错）→网络侧（管理 VLAN/L3 路由/dhcp-relay）→OV2500 Watchdog 服务状态。
- 国家码不匹配=射频全关；实验室必须选 FR。
- AP Group 属性里的 SSH Login 不要启用。
- 许可 key 只贴 key 本身不贴整行；文件与 key 二选一，不可都做。
- RADIUS 通信仍走 IPv4，纯 IPv6 管理网要留 IPv4 通路。

---
来源条目: f06, f07, f08, f16, p16, p17, p18, p19, p20, p21, p22, p23, p24, p36, p37, p38, ce06, ce07, ce08, ce09, ce10, c01, c02, c03, c04, g32, g33, g34
