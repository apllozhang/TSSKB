---
name: 设备准入与管理面防护（默认口令/SSH PKA/IP 锁定/AAA/SNMPv3/PKI/CC-JITC-FIPS 安全模式）
description: 需要加固交换机与网管平台的管理面时使用：U-boot 口令与镜像校验、带外/管理 VRF、管理站白名单、SSH 强加密与公钥认证、IP 锁定、AAA/RADIUS over TLS、SNMPv3（USM/TSM）、PKI 证书校验、ASA enhanced/CC/JITC/FIPS 四种安全模式、OmniVista 2FA 与 API 安全。
source_book: Network Security Guidelines
---

## R（触发场景）
- 首次开机安全基线：改默认口令、限制控制台、关多余服务
- 规划管理通道：带外 EMP vs 管理 VRF vs 数据 VRF 关管理口
- 部署 SSH PKA、IP 锁定、AAA 集中化与 RADIUS over TLS
- SNMPv3 三模型选择、PKI/SSL cipher、Captive Portal 证书
- 按合规要求选择 CC/JITC/FIPS/ASA enhanced 安全模式
- 加固 OmniVista：2FA、Network ID、REST API 凭据管理

## I（核心理念）
管理面三道闸（F2，<<<PAGE 9-30>>>）：物理/引导层（U-boot 口令+镜像校验）→ 通道层（OOB 优先、管理 VRF 隔离、白名单）→ 认证层（强加密 SSH+PKA+AAA+MFA）。密码认证固有弱点（可预测、重用、共享、钓鱼、暴力破解、长期有效，X5，<<<PAGE 16>>>）——公钥+多因素是出路（P22/P27）。安全模式是成套收紧：CC 仅 console+SSH、JITC 军规、FIPS 强算法，互斥选用。

## A1（行动框架）
1. 管理通道选型：专用物理 OOB（最优，P14）→ 不行则带内专用 VLAN/VRF（次优）→ 数据 VRF 内逐项关闭管理服务兜底（P15/C5，<<<PAGE 10>>>）
2. 认证体系递进：改默认口令（P17）→ 强口令策略（P45）→ SSH 强加密+PKA（P21/P22）→ IP 锁定+限登录次数（P23/P25）→ AAA 集中化+MFA（P27/P28）→ RADIUS over TLS（P29）
3. 安全模式选择：常规 ASA enhanced（P43）→ 合规 CC（默认 admin 仅装机用，X14）→ 军用 JITC → 密码合规 FIPS；互斥不可叠加（<<<PAGE 24-28>>>）
4. 网管平台（OmniVista）加固：2FA 全用户（P74）→ 停用未用服务（P75）→ Network ID 安全上线（P76）→ API 凭据不入代码+专用账户+最小权限（P80）

## A2（操作步骤）
- **首开基线**：改 admin 默认口令 "switch"（X1/P17）；secureadmin 首登强制改密并可校验镜像完整性（C4，<<<PAGE 11>>>）；U-boot/ONIE 设口令（P12）
- **管理 VRF 收敛攻击面**（C5，<<<PAGE 10>>>）：`vrf data ssh admin-state disable` / `vrf data telnet admin-state disable` / `vrf data webview server disable`
- **管理站白名单**：仅预定义 IP 可管理，上限 64 个（P16，<<<PAGE 11>>>）
- **SSH PKA 七步**（C6，<<<PAGE 14>>>）：ssh-keygen 生成对→保存私钥→scp 公钥上机→建用户→installsshkey→公钥登录→`ssh enforce-pubkey-auth`
- **暴力破解防护**：限登录尝试次数（P23）+ 收敛 login-grace-time（默认 120s）与会话超时（P24）+ IP 锁定阈值（认证失败达阈值永久封禁，清单上限 128 IP）（C7/P25，<<<PAGE 14-15>>>）
- **AAA 回退链**（C8，<<<PAGE 16>>>）：`aaa authentication ssh rad1 ldap2 local`——顺序可用性回退，rad1 挂走 ldap2，再挂走本地库；RADIUS over TLS 消除 MD5 风险（P29，<<<PAGE 17>>>）；按命令域/族做 RBAC（P30，<<<PAGE 17-18>>>）并开记账与 command.log（P31/P32，<<<PAGE 18-19>>>）
- **SNMPv3**：VACM 视图访问 + USM 用户安全 + TSM（over TLS/DTLS，已有 PKI 则用 TSM，否则 USM）；SNMP 专用账户禁 SSH；开认证陷阱（P33-P36，<<<PAGE 19-20>>>）；TSM 需 `snmp tsm-map remote-identity manager.crt user ...` 证书映射（C9，<<<PAGE 20>>>）
- **PKI/SSL**：三模式 No Validation（默认，不校验）/Server Cert Validation/Mutual Auth（P38，<<<PAGE 21>>>）；cipher 设 high（CC 模式强制 high）；WebView 换自定义证书勿依赖自签默认（P39/P40/X11，<<<PAGE 22-23>>>）；OCSP/CRL 校验失败即断 TLS（<<<PAGE 22>>>）
- **JITC 细则**（C13，<<<PAGE 27>>>）：口令≥15 字符；SSH 每 GB 或每 60 分钟 rekey；升级前必须验签
- **日志**：集中 syslog + TLS 加密 + 第二服务器冗余（P37，<<<PAGE 21>>>）
- **OmniVista**：MSP/Organization 两级用户均开 2FA（P74，<<<PAGE 72>>>）；DHCP Option 43 Sub-Option 133 下发 Network ID，Strict Mode 拒绝无 ID 设备（P76，<<<PAGE 75-76>>>）；API 凭据用第三方保管、专用账户、最小权限、勿暴露公网（P80/X23/X24，<<<PAGE 84>>>）

## E（实证案例）
- secureadmin 特权账户首登强制改密与自检（C4，<<<PAGE 11>>>）
- SSH PKA 部署七步（C6，<<<PAGE 14>>>）
- IP 锁定与封禁清单（上限 128 IP）（C7，<<<PAGE 15>>>）
- RADIUS 服务器排序回退链（rad1→ldap2→local）（C8，<<<PAGE 16>>>）
- SNMP over TLS（TSM）证书身份映射（C9，<<<PAGE 20>>>）
- JITC 模式强制安全细则（C13，<<<PAGE 27>>>）

## B（反例与坑）
- 默认口令 "switch"：admin 与 secureadmin 首开同密码（X1，<<<PAGE 11>>>）
- 控制台直连可重置管理员口令——控制台也要管起来（X2/P18，<<<PAGE 11>>>）
- U-boot 口令丢失且 flash 损坏时只能返厂（C3，<<<PAGE 9>>>）
- 工厂默认口令策略弱（无大小写要求数）、默认无用户锁定——必须手工收紧（X12/X13，<<<PAGE 25>>>）
- 默认 PKI 模式 No Validation 不校验证书（X10，<<<PAGE 21>>>）
- 自签默认证书触发浏览器告警且不可依赖（X11，<<<PAGE 23>>>）
- CC 模式下日常管理用默认 admin 是反模式（X14，<<<PAGE 26>>>）
- API 凭据硬编码、API 暴露公网（X23/X24，<<<PAGE 84>>>）
- 不用的 WebView 应整服务关闭而非仅改口（P26，<<<PAGE 15>>>）

来源：Network Security Guidelines（Management Plane 章 + OmniVista 章，p9-30、71-85）
