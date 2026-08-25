---
name: 园区 NMS 体系与安全（OmniVista HA/UPAM 统一接入/角色化策略/wIDS-wIPS）
description: 需要规划 OmniVista NMS 高可用（Standalone/L2 HA/L3 HA）、AP call-home onboarding、UPAM 统一有线无线认证（IoT 指纹/802.1x/访客四式/BYOD）、角色化安全（UNP/ARP/Quarantine/WCF/流氓 AP 遏制）时使用。
source_book: ALE Mobile Campus Architecture Guide（sol-campus-architecture DOC1）
---

## R（触发场景）
- 选型 OmniVista 部署形态与高可用（单机/L2 HA/L3 HA 功能取舍）
- 规划统一接入安全：员工 802.1x、IoT 指纹、访客认证、BYOD 管控
- 设计角色化策略（安全跟人走而非绑端口）与隔离处置闭环
- 无线安全：wIDS/wIPS、流氓 AP 判定与遏制、WCF 内容过滤

## I（核心理念）
统一接入安全框架（F5，<<<PAGE 36>>>）：UPAM 中央 RADIUS+captive portal → 认证谱系 → 角色（UNP/ARP）定 VLAN+ACL+QoS → 事后处置（Quarantine+QMR/WCF/wIDS/wIPS），安全贯穿"接入-授权-运行-处置"全生命周期。安全内建于网络并按角色动态施加，而非静态绑端口（P52，<<<PAGE 36>>>）；UNP/ARP 内嵌于交换机/AP 保证有线无线策略一致（P53，<<<PAGE 36>>>）。NMS 选型：L2 HA 复用原 IP 零改造（P49，<<<PAGE 35>>>）；L3 HA 跨子网但 sFlow/策略执行等功能受限（P50/X14，<<<PAGE 36>>>）。

## A1（行动框架）
1. NMS 部署选型（C10，<<<PAGE 35>>>）：单机无切换；L2 HA 双 VM 同子网+虚拟 Cluster IP（原单机 IP 可复用）；L3 HA 双节点跨子网各持 IP、设备配双地址、Preferred Node 须 CLI admin 菜单设置
2. AP onboarding（C11/P51，<<<PAGE 36>>>）：初联自动回连 Cirrus Activation Server→序列号对 Device Catalog 校验→发证书建 VPN→按 AP 组模板下发配置
3. 认证谱系选型（P54-P57，<<<PAGE 37-39>>>）：IoT 指纹（行为特征免手工）；员工 802.1x（AD/LDAP/外部 RADIUS，可代理 ClearPass/ISE）；访客四式（自注册/社交登录/员工赞助/SMS-Plivo）+Enhanced Open 免密场景；WPA3 优先兼顾存量 WPA2
4. 分段与管控：SSID 即分段（不同 SSID 对应安全设置/VLAN/访问控制，P58，<<<PAGE 40>>>）；BYOD 公司设备预置画像、外部设备声明注册+时限/会话/1-10 台限制（P59/C15，<<<PAGE 40>>>）
5. 处置闭环（P60/P61，<<<PAGE 40-42>>>）：syslog/SNMP trap 触发 Quarantine Manager 隔离或 Candidate List，QMR 补救；流氓 AP（接有线或仿冒 SSID）才遏制——DEAUTH 帧，默认关闭

## A2（操作步骤）
- **访客认证四方式部署**（C14，<<<PAGE 39>>>）：嵌入式 Captive Portal 自注册/社交登录（Facebook、Google、Rainbow、微信）/赞助审批/SMS（Plivo）取凭证；默认记录留一个月，可外接日志服务器
- **BYOD 注册管控**（C15，<<<PAGE 40>>>）：UPAM Captive Portal 声明设备→挂安全策略 ARP→时限、会话超时、每人 1-10 台
- **WCF 配置三步**（C12，<<<PAGE 41>>>）：建 WCF Profile（多条过滤条件）→给 ARP 或 SSID 挂 Profile→应用到 AP
- **安全动态施加**（X16，<<<PAGE 37>>>）：网络边缘安全按预定义角色随用户/设备动态应用，与端口解耦

## E（实证案例）
- OmniVista HA 三形态部署对比与 L3 HA 的 Preferred Node CLI 设置（C10/X15，<<<PAGE 35-36>>>）
- AP onboarding 全流程：call-home→序列号校验→证书→组模板（C11，<<<PAGE 36>>>）
- mDNS 网关/Responder 两模式实现跨网段服务共享并由防火墙审查（C7/C8，<<<PAGE 33>>>）

## B（反例与坑）
- L3 HA 不支持 sFlow、策略执行与部分设备管理功能；Preferred Node 不能走界面只能 CLI（X14/X15，<<<PAGE 36>>>）
- 未注册设备不得入网——onboarding 按序列号白名单（X17，<<<PAGE 36>>>）
- mDNS 传统同网段模式有安全风险（含访客/BYOD 威胁）（X11，<<<PAGE 32>>>）
- 干扰 AP 只造成 RF 干扰、不是直接安全威胁，勿与流氓 AP 混淆（X18，<<<PAGE 41>>>）
- 流氓 AP 遏制默认关闭，开启后检测 AP 才发 DEAUTH（X19，<<<PAGE 42>>>）
- 传统资产盘点靠用户反馈与猜测，易少买/多买——BLE 资产追踪替代（X20，<<<PAGE 34>>>）

来源：ALE Mobile Campus Architecture Guide（sol-campus-architecture DOC1，p33-42）
