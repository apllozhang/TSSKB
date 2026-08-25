---
name: AOS 8 接入安全（Access Guardian/UNP/AAA/AppMon/AFP/LPS/镜像/sFlow）
description: 需要在 OmniSwitch AOS 8 上配置网络准入（802.1X/MAC 认证/UNP 分类/Captive Portal）、AAA 服务器（RADIUS/RADSEC/TACACS+/LDAP）、BYOD mDNS/SSDP、L2 GRE 隧道、应用监控 AppMon/DPI、应用指纹 AFP、Learned Port Security、端口镜像/sFlow/RMON 时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 边缘端口要认证准入：802.1X（supplicant）或 MAC 认证（打印机/IoT）
- 认证后按用户/设备给不同 VLAN 与 QoS：UNP profile+分类规则
- 访客 Web 认证：Captive Portal
- AAA 服务器选型与备份：RADIUS/RADSEC/TACACS+/LDAP
- BYOD/零配置发现：mDNS/SSDP relay；AP 流量回传：L2 GRE
- 要按应用（DPI/REGEX 指纹）识别并施策：AppMon/AFP
- 限制端口学习 MAC 数防私接：LPS
- 取证与流量分析：端口镜像/端口监控/sFlow/RMON

## I（核心理念）
网络准入框架（F9，<<<PAGE 1212>>>）：认证（802.1X/MAC/Captive Portal→RADIUS/UPAM/CPPM）→分类（UNP 规则/端口默认）→角色（profile：VLAN/service 映射+QoS 列表）→限制/隔离（QMR 隔离修复）；BYOD（mDNS/SSDP）与 IoT profiling 是外延。AAA 服务器选型矩阵（F10，<<<PAGE 1475>>>）：RADIUS（管理+准入）/TACACS+（管理含 SNMP）/LDAP（管理含 SNMP）。应用感知框架（F11，<<<PAGE 1431>>>/<<<PAGE 1457>>>）：AppMon（DPI 签名+应用列表+QoS 执行）与 AFP（REGEX 指纹+分类器库+trap/UNP 列表）互补。安全纵深四层（F18，<<<PAGE 83>>>/<<<PAGE 1536>>>/<<<PAGE 819>>>/<<<PAGE 1212>>>）：端口级（LPS/风暴控制）→链路级（MACsec）→网络级（IPsec/DoS）→身份级（AG/UNP）。

## A1（决策框架）
1. **准入路径**：supplicant 用 802.1X（EAP over RADIUS）；非 supplicant 用 MAC 认证（MAC 作 username/password）；无认证场景用 UNP 分类规则（源 MAC/IP/domain 等）（P167/P169，<<<PAGE 1213>>>）
2. **标准次序**：先配 RADIUS→profile→映射→分类规则→端口→认证/分类使能→默认 profile（P171，<<<PAGE 1211>>>）
3. **AAA 选型**：端口准入只认 RADIUS（TACACS+/LDAP 不支持，X71）；管理授权优先从服务器取，未配置回落本地用户库（P180）
4. **应用识别**：面向 OVNG DPI 生态选 AppMon；面向服务器侧端口行为选 AFP（F11）
5. **观测面选型**：抓包分析端口镜像/端口监控；采样统计 sFlow；SNMP 探针 RMON（F15）

## A2（操作步骤）
- **Access Guardian 十二步**：`aaa radius-server rad1_mac host 10.135.60.44 hash-key secret ...`→`aaa device-authentication mac rad1_mac`→`aaa mac session-timeout enable`→`unp profile na_employee`→`unp profile na_employee qos-policy-list naEmpList`→默认 profile `unp profile def_unp`→`unp profile map na_employee vlan 100`→`unp classification mac-range ... profile1 na_employee`→`unp port 1/1/20 port-type bridge`→`unp port 1/1/1 mac-authentication`→`unp port 1/1/1 classification`→端口默认 profile；验证 show unp 系列（cases·C55，<<<PAGE 1210>>>）
- **Captive Portal**：操作模式→配置 profile→替换证书→自定义 web 页→认证流程（cases·C56，<<<PAGE 1303>>>）
- **L2 GRE 隧道（BYOD/AP 流量）**：tunnel access switch 与 tunnel aggregation switch 两侧配置+外部环回 SAP+SDP 绑定（cases·C57，<<<PAGE 1353>>>）
- **mDNS/SSDP 零配置**：使能 relay→VLAN/service 域配置→（可选）filtering 规则（cases·C58，<<<PAGE 1400>>>）
- **AppMon**：签名 kit 文件→应用池→应用列表→应用组→QoS 策略；监控流程=端口采样→签名匹配→更新流数据库→应用记录，强制流程再叠加 QoS 执行（P174/P175，<<<PAGE 1431-1432>>>）
- **AFP**：REGEX 签名文件（/flash/app-signature/app-regex.txt）匹配采样 IP 包，命中生成分类器入库并联动 QoS/trap/UNP 列表；默认全局使能但所有端口禁用，端口使能才采样（P176/P177，<<<PAGE 1457>>>）
- **LPS**：学习窗口时长+最大 bridged/filtered 数量+授权 MAC 范围；违规处理三选一（阻断违规流量/停止学习/管理关闭端口）（P182/P183，<<<PAGE 1536>>>）
- **端口镜像**：`port-mirroring 6 source 1/2/3-9 destination 1/2/10 unblocked-vlan 7`；验证 `show port-mirroring status 6`（cases·C59，<<<PAGE 1558>>>）
- **sFlow 三段**：`sflow receiver 1 name Golden address 198.206.181.3`→`sflow sampler 1 port 2/1/1-5 receiver 1 rate 2048 sample-hdr-size 128`→`sflow poller 1 port 1/2/6-10 receiver 1 interval 30`；验证 `show sflow receiver`（cases·C60，<<<PAGE 1561>>>）

## E（实证案例）
- Access Guardian 十二步快配（C55，<<<PAGE 1210>>>）
- Captive Portal 五步（C56，<<<PAGE 1303>>>）
- sFlow 三段配置（C60，<<<PAGE 1561>>>）

## B（反例/坑）
- 认证服务器不逐台轮询：第一台可用服务器上找不到用户即判失败，不自动试下台（X70/P179，<<<PAGE 1475>>>）
- TACACS+/LDAP 不支持端口准入，Access Guardian 只认 RADIUS（X71，<<<PAGE 1475>>>）
- MAC 认证把 MAC 同时作用户名密码，服务器侧格式不匹配（大小写/分隔符）会全军覆没（X74，<<<PAGE 1214>>>）
- 认证失败或无 profile 返回时回落到 UNP 端口默认 profile 与分类规则（P168，<<<PAGE 1213>>>）；MAC 会话定时器默认 12 小时（P172，<<<PAGE 1210>>>）
- LPS 不支持 linkagg/聚合成员口；学习窗口全局生效不能按口调（X69/P184，<<<PAGE 1536>>>）；MAC 四类型中 bridged 满后新地址按 filtered 学（P185，<<<PAGE 1537>>>）
- sFlow 三件套默认 UDP 6343、datagram 1400 字节、版本 5；端口镜像加 unblocked-vlan 防 STP 变化中断镜像会话（P188/P187，<<<PAGE 1561, 1558>>>）
- 端口监控（port-monitoring）持久会话落盘数据文件默认 64K、可覆盖、capture brief（P189，<<<PAGE 1559>>>）
- 802.1Q tagged 口默认 untrusted，上联口标记不生效（X64，<<<PAGE 1134>>>，详见 aos-nc-qos-policy）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 35 章 Access Guardian（<<<PAGE 1210-1400>>>）、第 36 章 AppMon（<<<PAGE 1431-1449>>>）、第 37 章 AFP（<<<PAGE 1457-1458>>>）、第 38 章 Authentication Servers（<<<PAGE 1475-1525>>>）、第 40 章 LPS（<<<PAGE 1536-1542>>>）、第 41 章端口镜像/sFlow/RMON（<<<PAGE 1558-1567>>>）。条目来源：cases C55-C60；principles P167-P190；counter-examples X69-X71/X74；frameworks F9-F11/F15/F18。
