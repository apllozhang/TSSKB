---
name: 访客网络与 Captive Portal 设计
description: 当需要为 SMB 设计访客 Wi-Fi（门户模板、访客账号/接入码、Walled Garden、行为审计、访客自助管理）时使用本技能。
source_book: DT00XTE301 LAN & WLAN Installation & Configuration for SMB
---

## R（触发场景）
- 企业/酒店要给访客开放 Wi-Fi，要求门户认证 + 有效期控制
- 访客认证前需要放行部分白名单站点（Walled Garden）
- 前台需要自助开访客账号、或需要审计访客在线行为

## I（核心理念）
访客网络的标准形态是：Open SSID + Captive Portal + 独立 VLAN + 仅 internet 访问 + 低优先级。认证方式三选一（账号 / 接入码 / 使用条款），账号可设起止日期形成自然过期。UPAM 内嵌的 Captive Portal 支持 Social Login（如 Rainbow），并可用 GuestOperator 受限账号把开号工作交给前台。

## A1（行动框架）
1. Express 版访客 SSID：WLAN > New > Security Open + Captive Portal Yes + VLAN 30 > Access > Authentication 选 Account > Add 建账号（如 Guest/superuser）并设起止日期 > 客户端访问 non-https URL 触发门户 > 登录后取 192.168.30.x（C12，<<<PAGE 225>>>–<<<PAGE 228>>>）。
2. 访客行为审计：Access > Authentication > Client Behavior Tracking 启用，Log To 选 TFTP/SFTP/Syslog 并填服务器 IP 与周期；日志行含事件时间、客户端 MAC/IP、AP MAC、SSID、ONLINE/OFFLINE（C14，<<<PAGE 233>>>）。
3. 前台自助管理：System > General > Account Management > Operator Enable + 设密码 > 重新登录选 GuestOperator，仅见访客账号管理界面（C15，<<<PAGE 234>>>）。
4. Cirrus 版（C21，<<<PAGE 418>>>–<<<PAGE 425>>>）：VLAN 30（云侧 + 接入交换机手工）> Create SSID：Usage = Guest Network、Captive Portal = YES（OV-UPAM）> 建 Guest 账号 > Create Guest Access Strategy + Captive Portal Template（Login By Username & Password）> 绑 My-AP-Group/VLAN 30 > 客户端 non-https URL 触发门户；踢人：Network > Analytics > Clients > Actions > Kick Off。

## A2（进阶应用）
- 三种认证方式（P39，<<<PAGE 226>>>）：account（账号密码）、access code（接入码）、terms of use（使用条款）；账号字段区分大小写，可设有效期。
- Walled Garden（P49，<<<PAGE 235>>>、<<<PAGE 410>>>）：认证前白名单放行预设站点（如酒店官网），提升访客体验。
- 门户能力面：账号/接入码/条款/社交登录（Rainbow）/自助注册（glossary·<<<PAGE 213>>>、<<<PAGE 409>>>）。
- 访客策略三维基线：仅 internet、常规带宽、低优先级（P38，<<<PAGE 217>>>）。
- Guest 场景的 SSID 向导比员工版多一步 Guest Access Strategy（门户定制 + 登录方式）（F05，<<<PAGE 405>>>、<<<PAGE 413>>>）。

## E（实证案例）
- Express 访客门户：GuestX SSID + 账号 Guest/superuser，http://2.2.2.2 触发重定向，登录后取 192.168.30.x（C12，<<<PAGE 225>>>–<<<PAGE 228>>>）。
- Cirrus 访客门户：Guest Access Strategy + 门户模板 + VLAN30 绑定，Analytics 里 Kick Off 踢出用户（C21，<<<PAGE 418>>>–<<<PAGE 425>>>）。
- 行为日志外发 Syslog，含 MAC/IP/SSID/在线状态（C14，<<<PAGE 233>>>）。

## B（边界与陷阱）
- 门户重定向只对 non-https URL 生效，Debian 树莓派不会自动弹门户，须手动开 http 站点（CE11，<<<PAGE 422>>>）。
- 账号区分大小写：'Guest' 与 'guest' 是两个账号，登录失败先查大小写（CE12，<<<PAGE 226>>>）。
- 访客 SSID 必须绑独立 VLAN（如 VLAN30），与员工网段隔离（C12/C21）。

## 来源
- case·Guests SSID + 内置 Captive Portal + 访客账号（<<<PAGE 225>>>–<<<PAGE 228>>>）
- case·访客行为日志（<<<PAGE 233>>>）
- case·GuestOperator 受限管理账号（<<<PAGE 234>>>）
- case·Cirrus Guests SSID + 踢出客户端（<<<PAGE 418>>>–<<<PAGE 425>>>）
- principle·Captive Portal 三种认证方式（<<<PAGE 226>>>）
- principle·Walled Garden 特性（<<<PAGE 235>>>、<<<PAGE 410>>>）
- principle·AP 内置 QoS/ACL 三角色用例（<<<PAGE 217>>>）
- counter·non-https 才触发重定向（<<<PAGE 422>>>）
- counter·账号字段区分大小写（<<<PAGE 226>>>）
