---
name: AOS 8 纳管服务（SNMP/WebView/Cirrus 云/REST/DNS/NTP）
description: 需要在 OmniSwitch AOS 8 上配置 SNMP v1/v2c/v3 管理站与 trap、WebView Web 管理与证书、OmniVista Cirrus 云纳管与 NaaS license、REST Web Services 自动化、DNS 解析器、NTP 时间同步时使用。
source_book: OmniSwitch AOS Release 8.10R4 Switch Management Guide
---

## R（触发场景）
- 要把交换机接入 NMS/OmniVista：配 SNMP station、community-map、v3 认证加密用户、trap 过滤/重放
- 要启用 WebView 或换 HTTPS 证书；要用 REST API / Python 自动化管理
- 要零接触接入 OmniVista Cirrus 云（DHCP Option 43、cloud-agent、NaaS license）
- 要让交换机解析域名（DNS resolver）或对时（NTP 客户端/服务器/广播/认证）

## I（核心理念）
纳管四条通道递进：SNMP（传统 NMS 轮询+trap，v1/v2c community 映射到用户、v3 USM/TSM 加密认证，P93-P100）→ WebView/REST（内嵌 Web 界面 + mib/cli 双域 RESTful API，P101/P113-P117）→ AMS 发布订阅（MQTT 替代 SNMP 轮询的局域微服务，P120-P123）→ OmniVista Cirrus 云管理（零接触 call-home + VPN 隧道 + NaaS 订阅状态机，F10）。时间同步框架（F12）：本地时钟/时区（DST 自动）→ NTP 分层 stratum 模型 → 云场景 NTP 池保障证书时间有效。DNS 三步启用：domain-name → domain-lookup → name-server（P43）。

## A1（决策框架）
1. **传统 NMS 纳管选 SNMP**：v3 加密认证（sha+aes）优先；v1/v2c 靠 community-map 映射到用户继承权限（P95）；安全等级链决定接受哪些请求（P94）
2. **Web/编程纳管**：WebView 需 `aaa authentication http local` 解锁（分区权限授权）；自动化走 REST（GET/PUT/POST/DELETE + JSON/XML）或 AOSAPI Python 库（P113-P117）
3. **云纳管选 Cirrus**：新机默认上云（无 vcboot.cfg 即启用 agent，P104）；存量机 `cloud-agent admin-state enable`；NaaS license 状态机 Operational→Grace→Degraded（P107/P108）
4. **对时选 NTP**：客户端/服务器/广播三模式；认证场景 ntp.keys + trusted key；不与 stratum 16 同步（P158-P161/X98）
5. **跨交换机事件联动选嵌入式 Python/AMS**：trap 绑定脚本须存 /flash/python（P119）；AMS 以 MQTT broker/topic 做配置同步（P120-P121）

## A2（操作步骤）
- **SNMP 管理站**：`user NMSuserV3MD5DES md5+des password ***` → `snmp station 199.199.100.200 8010 NMSuserV3MD5DES v3 enable` → `show snmp station`（C36，<<<PAGE 205>>>）
- **SNMP community/引擎/过滤**：`user community_user1 password *** no auth read-only all` → `snmp community-map comstring2 user community_user1 enable` → `snmp community-map mode enable`；engineid 可改 text/mac/ipv4；`snmp trap filter 210.1.2.1 0 1 2 3`（C37）
- **WebView**：`aaa authentication http local` → https://<ip>/new#/；自定义证书 `cat wv_server.key wv_server.crt > web.pem` → `aaa certificate install-certificate webview web.pem`（C35，<<<PAGE 192>>>）
- **Cirrus 接入**：DHCP 配 Option 43；`cloud-agent admin-state enable`、`cloud-agent discovery-interval 60` → `show cloud-agent status`（C38，<<<PAGE 224>>>）；NaaS：`naas license apply file licenseFile.v2c`（需重启）→ `show naas license`（C39）
- **REST**：`GET https://192.168.1.1/auth/?&username=admin&password=switch`；`PUT https://192.168.1.1/mib/vlanTable?mibObject0=vlanNumber:2&...`；`GET .../cli/aos?&cmd=show+vlan+5`（C40，<<<PAGE 249-259>>>）
- **DNS**：`ip domain-name mycompany1.com` → `ip domain-lookup` → `ip name-server <ip>`（C11，<<<PAGE 46>>>）
- **NTP**：`ntp server 198.206.181.139` → `ntp client admin-state enable` → `show ntp status`；广播 `ntp broadcast-client enable` + `broadcast-delay 1000`；认证 `ntp key load` → `ntp authentication enable` → `ntp server 1.1.1.1 key 2` → `ntp key 2 trusted`（C52，<<<PAGE 408-417>>>）
- **事件脚本**：`event-action trap linkDown script /flash/python/link_event.py` → `show event-action statistics`（C41，<<<PAGE 270-271>>>）

## E（实证案例）
- SNMP v3 管理站部署（C36，<<<PAGE 205>>>）与 community/引擎/过滤（C37，<<<PAGE 207-216>>>）
- WebView 启用与自定义证书（C35，<<<PAGE 192>>>）
- Cirrus 快速接入（C38，<<<PAGE 224>>>）与 NaaS 配置（C39，<<<PAGE 237>>>）
- REST 登录/建 VLAN/查询三例（C40，<<<PAGE 249-259>>>）
- NTP 客户端/广播/认证三套（C52，<<<PAGE 408-417>>>）

## B（反例/坑）
- WebView 改 http/https 端口前必须先断开所有 WebView 会话（X48，<<<PAGE 191>>>）
- TSM 启用后丢弃全部 v1/v2/v3 USM 请求与 trap，SNMP 仅走 IPv4（X49，<<<PAGE 209>>>）
- 证书更新须手工从 primary 拷到所有 secondary/slave 并重启（X50，<<<PAGE 210, 213>>>）
- 修改用户 SNMP 权限必须重输密码（哈希依赖认证等级）（X52，<<<PAGE 161>>>）
- 已有 (vc)boot.cfg 的存量交换机不会自动上云，需 CLI 手动启用 cloud-agent（X54，<<<PAGE 223>>>）
- 无 NTP 则设备无法连激活服务器入云（除非手工设对日期）（X55，<<<PAGE 228>>>）
- NaaS degraded 模式禁访 certified/running 目录、禁 show/监控命令（X57）；宽限/降级模式可登录但不能执行 CLI（X58）；NaaS license 需重启激活且宽限计时依赖 NTP（X59）（<<<PAGE 238-239>>>）
- Thin Switch 模式不落本地配置，由 OmniVista 下发才知道自己是瘦模式（X61，<<<PAGE 240>>>）
- REST 场景代理不遵守 Vary 头会出现 JSON/XML 串格式（X62，<<<PAGE 248>>>）
- 事件脚本单绑定（一事件一脚本），须存 /flash/python 且需 AAA 写权限（X63，<<<PAGE 270>>>）
- NTP 不支持 2035 年以后（X97）；不同步 stratum 16 未同步服务器（X98）；peer 关联只应建在同 stratum 层（X99）（<<<PAGE 413-414>>>）

## 来源
OmniSwitch AOS 8.10R4 Switch Management Guide 第 2 章 DNS（<<<PAGE 46>>>）、第 9 章 WebView（<<<PAGE 190-199>>>）、第 10 章 SNMP（<<<PAGE 203-220>>>）、第 11 章 OmniVista Cirrus（<<<PAGE 222-241>>>）、第 12 章 Web Services（<<<PAGE 246-278>>>）、第 17 章 NTP（<<<PAGE 406-417>>>）。条目来源：cases C11/C35-C41/C52；principles P43/P93-P123/P158-P163；counter-examples X48-X52/X54-X62/X97-X99；frameworks F9/F10/F12。
