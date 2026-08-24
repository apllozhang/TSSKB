---
name: Wi-Fi Express 模式日常操作
description: 当需要在 Express 模式下通过 AP Web 界面完成首次向导、建员工/访客 SSID、配内置 DHCP、访客账号与行为日志时使用。
source_book: DT00XTE310 OmniSwitch LAN Access & OmniAccess Stellar WLAN Express
---

## R（触发场景）
- 新 AP 首次上线，要改密码、改默认 SSID、配静态 IP
- 要给员工建 WPA2 SSID、给访客建 Captive Portal SSID 并分发账号
- 小站点没有外部 DHCP/RADIUS，需要 AP 内置 DHCP 服务器或本地认证

## I（核心理念）
Express 模式下所有管理动作集中在 AP（PVM）Web 界面：WLAN、Network、Access > Authentication 三大菜单覆盖 SSID、IP/DHCP、账号三类配置。访客场景的套路是 Open SSID + Captive Portal + 账号认证，员工场景是 WPA2/Enterprise + VLAN 映射。

## A1（行动框架）
1. **首次向导**：浏览器访问 `192.168.1.254:8080` → admin/admin → Wizard 改 superuser 密码 → 国家/时区 → 建 SSID（替换默认 mywifi-XXXX）→ AP > IP Mode > Edit 改静态 IP 与网关（<<<PAGE 117>>>-<<<PAGE 121>>>）。
2. **员工 SSID**：WLAN > New → 名称/Personal/密码 → Advanced 里 VLAN ID 20 → 客户端连接验证拿到对应网段地址（如 192.168.20.7x）（<<<PAGE 224>>>-<<<PAGE 231>>>）。
3. **访客 SSID**：Open + Captive Portal:Yes + VLAN 30 → Access > Authentication 选 Account 模式建 Guest 账号（密码区分大小写）→ 客户端浏览器访问任一 http URL 跳转 Portal（<<<PAGE 224>>>-<<<PAGE 231>>>）。
4. **内置 DHCP**：Network > AP Networks > vlan10 Manage 配 IP → Service > DHCP Create（Pool、Range、DNS）→ Action > Bind Network（<<<PAGE 232>>>-<<<PAGE 236>>>）。
5. **行为日志**：Access > Authentication > Client Behavior Tracking，日志行含 Event date / client MAC / IP / AP MAC / SSID / ONLINE-OFFLINE（<<<PAGE 236>>>-<<<PAGE 237>>>）。

## A2（进阶应用）
- **GuestOperator 前台账号**：System > General > Account Management > Operator: Enable + 密码，用 GuestOperator 登录仅可管理访客账号（<<<PAGE 237>>>）。
- **外部 RADIUS 员工 SSID**：Create WLAN → Security: Enterprise → AuthServer IP + AuthSecret → Advanced VLAN ID（<<<PAGE 238>>>）。
- **DHCP 池容量意识**：Range 40 个地址即 40 台并发设备上限（<<<PAGE 232>>>-<<<PAGE 236>>>）。

## E（实证案例）
- 员工+访客 SSID 创建：EmployeesX（WPA2+VLAN 20）验证拿 192.168.20.7x；Guests（Open+Portal+VLAN 30）经 Account 账号认证（<<<PAGE 224>>>-<<<PAGE 231>>>）。
- AP 内置 DHCP：Pool Employees，Range 192.168.10.10-50，DNS 指向自身，Bind 到 vlan10（<<<PAGE 232>>>-<<<PAGE 236>>>）。

## B（边界与陷阱）
- **默认口令基线**：admin/switch（交换机侧为 admin/switch，AP 侧 admin/admin）；8.10R3 起告警催改默认密码，8.10R4 起强制修改（<<<PAGE 64>>>-<<<PAGE 65>>>）——上线第一步就改密。
- Guest 账号密码区分大小写（<<<PAGE 224>>>-<<<PAGE 231>>>）。
- 内置 DHCP 的 Range 长度就是并发设备上限（<<<PAGE 232>>>-<<<PAGE 236>>>）。
- 访客 Portal 依赖 DNS 正常（排障前置检查 `cat /etc/resolv.conf`，<<<PAGE 444>>>-<<<PAGE 448>>>）。

## 来源
- cases·C4 Stellar AP 首次向导配置（<<<PAGE 117>>>-<<<PAGE 121>>>）
- cases·C11 员工/访客 SSID 创建（<<<PAGE 224>>>-<<<PAGE 231>>>）
- cases·C12 AP 内置 DHCP（<<<PAGE 232>>>-<<<PAGE 236>>>）
- cases·C13 用户行为日志（<<<PAGE 236>>>-<<<PAGE 237>>>）
- cases·C14 GuestOperator（<<<PAGE 237>>>）
- cases·C15 外部 RADIUS 员工 SSID（<<<PAGE 238>>>）
- counter-examples·X6 默认口令安全基线（<<<PAGE 64>>>-<<<PAGE 65>>>）
