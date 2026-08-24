---
name: device-cloud-onboarding
description: 何时用：把 OmniSwitch/Stellar AP 上线到 Cirrus 云管——Onboarding 双方法选型、激活状态机、AP Group/Provisioning 配置与"不上云"排障。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# 设备云管 Onboarding 与激活排障

## R · 原文引用

> "METHOD 1 > MANUAL CLASSIFICATION: Create a VLAN that will serve as the management VLAN ... manually configured as default/untagged VLAN on all ports where an AP is connected. METHOD 2 > ON BOARDING WITH UNP: 'defaultWLANProfile' UNP ... Automatically assigned to a built-in UNP LLDP classification rule that recognize and classify AP devices" (p284)

> "Intermediate Status: Registered / Obtaining Certificate / Upgrade / Upgrading / Assigned / VPN Configuring / Connected to OV. Expected Activation Status: Up to 5 minutes. Activation Status failures: Failed To Get Certificate / Upgrade Failed / Configuring VPN Failed / Provisioning Failed / Device Validation Failed / Factory Reset Required" (p261)

> "The Stellar AP is not authenticated with 802.1x. If 802.1x is enabled on the port ... and the Stellar AP fails 802.1x authentication, the VLAN-tagged client traffic is trusted and forwarded on the UNP port" (p291)

## I · 方法论骨架

**1. 交换机侧 Onboarding 方法选型**

| | 方法一：手动 VLAN 分类 | 方法二：UNP 自动分类 |
|---|---|---|
| 机制 | 每 AP 口手工配管理 VLAN untagged + SSID VLAN tagged | 端口设 UNP 口，LLDP-MED 自动识别 AP 归入内置 defaultWLANProfile，回发 Port VLAN ID |
| 优点 | 端口控制明确 | 新增 AP 免配置，扩展性好 |
| 代价 | 每台新 AP 都要逐口补 VLAN，漏配即不通且故障隐蔽 | 不做 802.1X——未认证 AP 的 tagged 流量仍被转发（rogue 风险） |
| 适用 | 安全要求高的端口 | 大规模/频繁扩容部署（配 >999 Dummy VLAN） |

**2. 激活状态机（卡住即对照定位）**
```
Waiting for validation → Waiting for first contact → Obtaining Certificate → Registered
→ Upgrade → Assigned → VPN Configuring → Connected to OV → Provisioning → OV Managed
```
- 每个中间态正常 ≤5 分钟
- 失败态映射：Failed To Get Certificate（证书服务/时间）| Upgrade Failed | Configuring VPN Failed | Provisioning Failed | Device Validation Failed | Factory Reset Required（VPN profile 变更过，唯一解是现场恢复出厂）
- 设备靠周期性 Call Home 联系云：交换机 `cloud-agent admin-state restart`（约 2 分钟）、AP 重启/firstboot 强制立即呼叫

**3. AP Group / Provisioning Configuration**
- Cirrus 以 AP Group 为单位管理（SSID/RF Profile 挂组）；组内可混型号，上限 2000，不依赖物理网络
- Provisioning 四必填：Name / Site / RF Profile / Timezone
- 可选项：SSH Login、AP Web、Client Behavior Tracking、证书、SNMP、IoT Radio、Data VPN、Syslog（≤4 台）
- BLE 信标按 AP Group 配置（默认关，默认 iBeacon 模式；可调功率/周期/UUID/Major/Minor），用于资产定位（p12）

**4. "不上云"三层排障链（全书复用骨架）**
1. L2：`show interfaces`（线缆/链路 up）→ `show vlan members port`（VLAN 正确）→ AP 另查 `show lanpower`（PoE）
2. AP 侧：恢复出厂（Reset 6 秒 LED 闪红 / `ssudo firstboot`）→ `getmode` 必须 OVNG → `cat /etc/config/network` 确认 proto dhcp → `ssudo ifconfig br-wan` 看 IP → `getovinfo` 看激活服务器
3. L3：`show ip interface` UP → ping eu.activation.ovng.myovcloud.com（同时验 DNS）→ Device Catalog > Action > View Activation Log

**5. AP 排障 CLI 工具箱（串口 115200-8-N-1，support/aos2016）**
`showsysinfo`（序列号/MAC/固件，云登记必用）、`ocloud_show`（VPN Status、下次 Call Home 倒计时）、交换机侧 `show cloud-agent status`（应 completeOK / DeviceManaged）。

## A1 · 书中案例（Lab 步骤精要）
- **c11/p241-253**：建 Site/Building/Floor（导入平面图、勾勒周界）→ Device Catalog +Create Device 选 OmniSwitch，控制台 `show chassis` 取序列号 → 分配站点、Do Not Upgrade → `cloud-agent admin-state restart` 强制激活 → 约 2 分钟到 OV Managed。
- **c12/p293-306**：OS-6360 预配 `vlan 10 members port 1/1/6 untagged` + 上联 tagged → AP `showsysinfo` 取 SN（SSZ231200742）→ 建 My-AP-Group + My-Provisioning-Config（Site/Default RF Profile/Europe-Paris）→ AP firstboot+reboot → `ocloud_show` 验证 VPN Status=connected。
- **c10/p238-240**：进入 Cirrus 系列实验前跑 reset_PODX 加载预配置，重启期间严禁按键（防 Miniboot）。

## A2 · 触发场景（含与相邻 skill 的区分）
- 设备要首次纳入 Cirrus 管理、换新设备重新上云、或"Device Catalog 里不出现/停在中间态"排障时用。
- **区分**：模式为什么落错（option 138/未登记）→ `express-mode-bootstrap`；许可/组织没开通 → `cirrus-license-org-lifecycle`；本 skill 从交换机侧准备一路管到 OV Managed 状态。

## E · 可执行步骤
1. 交换机侧选方法：安全敏感端口手动分类（管理 VLAN untagged + SSID VLAN tagged）；规模部署用 UNP（建管理 VLAN、端口设 UNP、映射到 defaultWLANProfile、配 Dummy VLAN >999）。
2. 控制台取序列号（交换机 `show chassis`；AP `showsysinfo`）。
3. Cirrus 建 AP Group 与 Provisioning Configuration（四必填字段），设备声明时分配 Site。
4. 等 Call Home 或强制（交换机 cloud-agent restart / AP 重启），每个中间态 ≤5 分钟。
5. 验证：状态 OV Managed；`show cloud-agent status` / `ocloud_show`。
6. 卡住按三层排障链走，最后看 Activation Log 反推失败态。

## B · 边界与陷阱
- UNP 安全盲区：AP 不过 802.1X，仿冒 AP 的 tagged 流量照样进内网 VLAN；高安全环境补 ACL/WIPS（ce17）。
- 手动分类漏配 VLAN 故障隐蔽（其他 SSID 正常），新 AP 上线用固定检查单核对（ce18）。
- 管理 VLAN 没 untagged 到 AP 口是最常见根因（ce16）。
- Call Home 间隔可到 30 分钟量级，等太久≠故障，用强制手段（ce15）。
- "Factory Reset Required" 表示 VPN profile 变更过，须现场恢复出厂，提前排窗口（ce14）。
- AOS release 5 交换机（如 OS2360）不被 Cirrus 支持，只能本地手管，规划前盘点版本避免"半纳管"（ce19）。
- AP1101/AP1201L/H/HL 不被 Cirrus 支持。

---
来源条目: f06, f07, f08, p12, p27, p28, p29, p30, p31, c10, c11, c12, ce14, ce15, ce16, ce17, ce18, ce19 · 术语锚点: g34, g12, g07, g41
