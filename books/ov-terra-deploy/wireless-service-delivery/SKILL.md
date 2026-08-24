---
name: 无线业务下发
description: 当需要创建站点/楼层、AP Group 与 Provisioning Configuration、配置 SSID（Employee 802.1X / Guest / PSK 多种认证）、Guest 门户与 Captive Portal 定制时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 无线项目开局：建站点楼层、AP Group、Provisioning Configuration
- 需要下发 Employee / Guest / BYOD SSID
- 需要定制访客门户、配置访客账号运营（Guest Operator）与配额策略

## I（核心理念）
无线配置的承载模型是"AP Group + Provisioning Configuration"：所有 AP 从其所属 AP Group 绑定的 Provisioning Configuration 取配置，SSID/RF Profile/模板均按 AP Group 管理而非物理网络。SSID 创建是向导式的，先选 Usage 预设模板（Guest/Employee/BYOD），再走认证策略 → Access Role → 网络分配。认证安全等级从 Open+CP 到 802.1X 递增，PSK 体系（DSPSK/PPSK/Dynamic PGPSK）是中间档的精细化工具。

## A1（行动框架）
1. **建站点与楼层**：创建 Site → Configure buildings and floors → 楼层平面图校准（Scale up/down / Rotate / Move / Move and calibrate the plan）（<<<PAGE 124>>><<<PAGE 125>>><<<PAGE 126>>><<<PAGE 127>>><<<PAGE 128>>>）。
2. **建 AP Group + Provisioning Configuration**：
   - 创建 AP Group（与物理网络无关，每组最多 20000 AP，可混型号）（<<<PAGE 152>>>）
   - 创建 Provisioning Configuration：必填 Name / Site / RF Profile / Timezone；另含 SSH Login、AP Web、证书、SNMP、IoT Radio、Syslog（最多4）等分节（<<<PAGE 153>>><<<PAGE 154>>><<<PAGE 155>>><<<PAGE 156>>>）
3. **Employee SSID（802.1X 示例）**：Usage 选 "Enterprise Network for Employee" → Encryption → Authentication Strategy 用 UPAMRadiusServer + 内部库建 Employee → Configure Access Role Attributes（VLAN ID: Employee(20)，可加 ACL/QoS 如 Full-Access、10Mbit/s）→ Network Assignment 选 Site + AP Group(s) → Schedule / VLAN Mapping 加 VLAN 完成（<<<PAGE 225>>><<<PAGE 226>>><<<PAGE 227>>><<<PAGE 228>>>）。
4. **Guest SSID + UPAM Guest 策略**：Usage "Guest Network" → 激活 Captive Portal 选项 → Authentication Strategy 选 RADIUS server → 用 UPAM 内部 RADIUS 则创建 Guest account → Guest Access Strategy 定义登录方式与 Post Portal enforcement → 给 Guest SSID 分配 VLAN（<<<PAGE 249>>>）。
5. **Captive Portal 定制**：可定制 Background Image、Login Background Color、Image Logo、Login Button 以贴合公司品牌；完成后点 apply the changes to the Devices（<<<PAGE 258>>><<<PAGE 259>>>）。
6. **访客运营**：Guest Operator 门户账号可创建访客账号、审批自注册请求；门户内 Manage Guests / Create Guest Account/Access Code / Import from XLSX or CSV / 审批自注册（<<<PAGE 287>>><<<PAGE 288>>>）。

## A2（进阶应用）
- **认证安全等级模型**：Open+CP（无安全）→ MAC 认证（可伪造、无加密）→ WPA2/WPA3 Personal PSK（共享密钥）→ WPA2/WPA3 Enterprise 802.1X（最强）（<<<PAGE 215>>>）。
- **PSK 体系三件套**（<<<PAGE 231>>><<<PAGE 233>>><<<PAGE 234>>><<<PAGE 235>>>）：
  - DSPSK：公司属性数据库按 MAC 分配专属 passphrase（Force/Prefer 两档）
  - PPSK：多个 passphrase 各绑一个 ARP
  - Dynamic Private Group PSK：条目同时绑 VLAN ID 与 ARP，免为每个 VLAN 建 ARP
- **VLAN Pooling**：一个 SSID 分配最多 256 个 VLAN，避免单一大广播域（<<<PAGE 224>>>）。
- **Guest Tunneling**：按 ARP 从 AP 到交换机/路由器建 L2 GRE 隧道（跨 L2/L3 网络），OmniSwitch 自动向 AP IP 建隧道简化部署，可加 GRE Backup tunnel 冗余（<<<PAGE 256>>>）。
- **带宽控制三层模型**：SSID 级（per SSID per AP 共享）→ ARP 级（per user）→ Policy List ACL/QoS 规则级；判定顺序：匹配 ACL 按规则限速，否则按 ARP，再否则按 SSID；Policy List 双向执行（<<<PAGE 268>>><<<PAGE 269>>><<<PAGE 264>>>）。
- **访客配额**：Service Level 绑定 ARP+Policy List+注册 Profile+有效期+删除策略（最多 5 个）；Registration Profile 定义 Data Quota（MB）与 Time Quota（小时/天），耗尽处理为 Block for remaining Duration（可加重定向 URL）或降速（kB/s）（<<<PAGE 282>>><<<PAGE 283>>><<<PAGE 284>>>）。

## E（实证案例）
- **案例 1**：企业员工网：SSID 用 Enterprise Usage + UPAMRadiusServer 内部库，Access Role Attributes 里 VLAN ID=Employee(20)，叠加 Full-Access ACL 与 10Mbit/s 限速，Network Assignment 指定 Site 与 AP Group（<<<PAGE 225>>><<<PAGE 226>>><<<PAGE 227>>><<<PAGE 228>>>）。
- **案例 2**：前台自助发访客账号：给前台开 Guest Operator 账号，其经 Guest Operator Login URL 登录门户，Create Guest Account/Access Code 或批量 Import from XLSX/CSV，并审批访客自注册（<<<PAGE 287>>><<<PAGE 288>>>）。
- **案例 3**：访客流量与企业流量隔离：Guest SSID 按 ARP 建 L2 GRE 隧道引到出口交换机，另加备份隧道保冗余（<<<PAGE 256>>>）。

## B（边界与陷阱）
- **DSPSK 加密限制**：AUTO_WPA_WPA2 加密不支持 DSPSK；PSK/PassPhrase 仅在 'Prefer Device Specific PSK' 时激活，需 Device Specific PSK: Enabled（<<<PAGE 232>>>）。
- **Provisioning Configuration 四必填**：Name / Site / RF Profile / Timezone 缺一不可（<<<PAGE 154>>>）。

## 来源
- cases·创建站点与楼层（<<<PAGE 124>>>~<<<PAGE 128>>>）
- cases·创建 AP Group 与 Provisioning Configuration（<<<PAGE 153>>><<<PAGE 155>>><<<PAGE 156>>>）
- cases·802.1X SSID 配置示例（<<<PAGE 225>>><<<PAGE 226>>><<<PAGE 227>>><<<PAGE 228>>>）
- cases·Guest SSID + UPAM Guest 策略配置（<<<PAGE 249>>>）
- cases·Captive Portal 定制（<<<PAGE 258>>><<<PAGE 259>>>）
- cases·Guest Operator 门户操作（<<<PAGE 287>>><<<PAGE 288>>>）
- frameworks·AP Group + Provisioning Configuration 配置下发模型（<<<PAGE 152>>><<<PAGE 153>>><<<PAGE 154>>>）
- principles·AP Group 概念与规模（<<<PAGE 152>>>）
- principles·Provisioning Configuration 必填四要素（<<<PAGE 154>>>）
- principles·SSID Usage 预定义模板模型（<<<PAGE 214>>><<<PAGE 218>>>）
- principles·认证安全等级模型（<<<PAGE 215>>>）
- principles·DSPSK/PPSK/Dynamic PGPSK 原理（<<<PAGE 231>>><<<PAGE 233>>><<<PAGE 234>>><<<PAGE 235>>>）
- principles·Guest Tunneling L2 GRE（<<<PAGE 256>>>）
- principles·带宽控制三层模型（<<<PAGE 268>>><<<PAGE 269>>>）
- principles·Policy List 双向执行（<<<PAGE 264>>>）
- principles·Registration Profile 配额与耗尽处理（<<<PAGE 283>>><<<PAGE 284>>>）
- principles·VLAN Pooling 原理（<<<PAGE 224>>>）
- counter-examples·DSPSK 不支持 AUTO_WPA_WPA2（<<<PAGE 232>>>）
