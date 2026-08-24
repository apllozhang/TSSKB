# frameworks 候选 — DT00XTE311 OmniVista 2500 NMS Administration R4

1. Unified Access 三层策略模型（AAA Server Profile → Access Role Profile → Access Auth Profile → Unified Policy）
   - <<<PAGE 235>>>：Unified Profile Templates 定义各对象："Access Role Profiles. Contains the various UNP properties (e.g., QoS Policy List attached to the UNP, Access Policies, Captive Portal Authentication)"、"AAA Server Profile. Defines specific AAA parameters that can be used in an Access Auth Profile or a Captive Portal Profile"、"Access Auth Profile. Enables the assignment of a pre-defined UNP port configuration to an edge port"。
   - <<<PAGE 246>>>："Unified policies are part of the Access Role Profile configuration."（QoS 策略最终挂在 Access Role Profile 下）。
   - 实操链路证据：<<<PAGE 259-265>>>（先建 RADIUS Server → AAA Server Profile（AAA_RADIUS）→ Access Role Profile（UNP-employee）→ Access Auth Profile（UNP_template）→ Apply to Devices/Port）。

2. 用户角色导向访问策略（User Role Oriented Access Policy：Employee/Guest Profile 分别映射 VLAN/带宽/优先级）
   - <<<PAGE 231>>>：图示 "Employee Profile → VLAN 20, Employee Resources, Higher Bandwidth, Higher Priority"；"Guest Profile → VLAN 30, Internet Only, Lower Bandwidth, Lower Priority"，由 "OV 2500 / UPAM" 下发 "Employee/Guest Access Profile (ARP/UNP)"。

3. PolicyView QoS 规则配置四步法（Condition → Action → Rule → Apply）
   - <<<PAGE 275>>>："QOS RULE CONFIGURATION STEPS：Create a Policy Condition / Create a Policy Action / Create a Policy Rule / Apply the Policy"。
   - Expert Mode 向导五步：<<<PAGE 279-284>>>：Create Policy（名称/Precedence/高级选项）→ Device Selection → Set Condition（L2 MAC/L3 IP/DSCP/L4/L7）→ Set Action（QoS/Disposition/TCM）→ Validity Period and Review。

4. PolicyView 双模式框架（OneTouch vs Expert Mode）
   - <<<PAGE 273>>>："Operation modes: OneTouch for Voice, Data & ACL … Expert Mode. Advanced QoS controls for complex policies (including validation scheme)"；OneTouch "Sets parameters once, Distributed to devices at the same time"。
   - OneTouch 三子模式：Voice（<<<PAGE 276>>>）、Data（Platinum/Gold/Silver/Bronze 优先级，<<<PAGE 277>>>）、ACL（Accept/Drop，<<<PAGE 278>>>）。

5. Policy Flow（LDAP 策略仓库驱动的策略下发流程）
   - <<<PAGE 272>>>："Policies stored in LDAP server configured as part of OmniVista installation. Switches notified to retrieve new policies from this server."
   - <<<PAGE 286>>>：流程图：用户在 PolicyView 创建策略(1) → 存入 Policy Directory Server(2) → Policy Enabled(3) → Switches 从 LDAP 拉取(4)。

6. Discovery 配置流程（Profile 三段式 + IP 范围 + Discover Now）
   - <<<PAGE 110-112>>>：Discovery Profile 三段：General（Name/CLI-FTP 用户密码）、SNMP（版本/Timeout 默认 5000ms/v3 用户与 Auth-Priv）、Advanced（Trap Station User/Discover Link/Shell Preference Telnet 或 SSH/Use Get Bulk/Max Repetitions）。
   - <<<PAGE 113-114>>>：先定义 IP 地址范围并关联 SNMP 设置，再 "click on the Discover Now button"。
   - 实操：<<<PAGE 170-172>>>（Network → Discovery → Discovery Profiles → + → 填三段参数 → Managed Devices → Discover New Devices → Start/End IP → Discover Now → Finish）。

7. OV2500 容量规划（Sizing）决策框架：Network Size 四档
   - <<<PAGE 45>>>："PLATFORM AND SIZING REQUIREMENTS … OmniVista allocates memory based on the network size selected during installation"；"If there are 4,000 Stellar AP in a 'High' network size, up to 500 AOS switches can be supported. If there are 4,000 Stellar APs in a 'Very High' network size, up to 1,000 AOS switches can be supported."
   - <<<PAGE 58>>>：Network Size 分档表：Low <500 / Medium 500-2000 / High 2000-5000 / Very High 5000-10000 台设备。
   - <<<PAGE 44>>>：容量上限：10000 devices、4000 Stellar APs、5000 VMs。

8. Virtual Appliance 安装部署序列框架
   - <<<PAGE 55-60>>>：Deploy VA（从 BPWS 下载）→ Power on → Hypervisor Console 依次填 Initial Settings（键盘/cliadmin 密码）→ IP Settings（OV IP/HTTP-HTTPS 端口/Captive Portal/Additional OV Web）→ Network Size → Additional Options（Hostname/DNS/NTP/Timezone/Routes）→ Exit & Reboot。
   - <<<PAGE 54>>>：vSphere OVF 部署向导步骤（"Disk formatting (Thin or Thick Provision). (Thick provision is recommended.)"）。

9. License 类型决策框架（Device License vs Service License；Starter/Evaluation/Production）
   - <<<PAGE 46-49>>>：两类许可（Device/Service）；Device 三型：Starter Pack（免费 30 台：10 AOS+10 三方+10 Stellar）、Evaluation（90 天 60 台）、Production（最多 10000 台）；Service：VM/Guest/On-Boarding/HA/Web Content Filtering。
   - <<<PAGE 50-51>>>：HA 许可自 4.3R1 起，"you don't have to double the licenses on the redundant system"；节点计数规则：VC 内每台物理设备 1 license（"VC of 2 = 2 license units"）。

10. Quarantine Manager 攻击检测与遏制框架（Detection → Rules → Enforcement → Responder）
    - <<<PAGE 303-307>>>：检测（AOS AlaDosTrap/Syslog 事件）→ 规则（内置+自定义：名称/描述/触发表达式/提取表达式/动作）→ 执行（Quarantine VLAN (vlan 999 <mac>) / ACL / Port shutdown / 黑名单）。
    - <<<PAGE 304>>>："By Default all of the rules are disabled"。
    - <<<PAGE 308-310>>>：三列表决策模型：Candidates（等待管理员决策）/ Banned（隔离直至手动释放）/ Never Banned（OV 自身与已发现交换机隐式加入）。

11. Template Based Provisioning 部署场景决策框架（4 场景矩阵）
    - <<<PAGE 418/451>>>：场景表：①Mobile App 离线+可选 Basic DHCP（无 3G/4G 远程站点）②Mobile App 在线（有电话网络）③Advanced DHCP+RCL（企业/园区）④仅 Advanced DHCP（企业/园区）。
    - <<<PAGE 414>>>：三阶段状态模型：Factory-default（隔离不可用）→ Bootstrapped（有限连通，待 Provisioning）→ Provisioned（完全受管）。

12. 动态模板 + 值映射（Value Mapping）实例化框架
    - <<<PAGE 463-464>>>：模板可为 Static（无变量）或 Dynamic（带 $VLAN/$PORTS 变量）；动态模板必须创建 Value Mappings，模板+变量值表推导出实际下发给交换机的配置。

13. Application Visibility 四步配置框架（Signature File → Signature Profile → Apply to Devices → 报表/强制）
    - <<<PAGE 373-375>>>：向导步骤：创建 Profile 名 → 选择 Signature File → Monitor Flow Count 组（建 App Group）→ Bandwidth Usage and Enforcement 组（配 ACL/QoS：Disposition DROP）→ Create Profile → Apply to Devices 选端口。
    - <<<PAGE 365-366>>>：策略归一化："The Policy has to be included in a Policy List. Then, the Policy List is included as part of the Access Role Profile configuration."

14. Analytics 报表体系框架（Visibility vs Availability；Profile 先行）
    - <<<PAGE 317-318>>>：两类报表（Visibility：Top N Apps/Clients/Ports/POE；Availability：设备状态/Alarms）；"To generate an Analytics Report for any of the 'Visibility' Reports, you must first create an Analytics Profile"。
    - <<<PAGE 321>>>：KPI-机制-结果对应表：Top N Apps ← sFlow sampling + TCP/UDP 端口识别；Top N Switches ← CPU/内存/温度派生指数；Top N Port ← SNMP MIB Polling。

15. Access Classification 回退分类规则框架（认证不可用时按规则定 Profile）
    - <<<PAGE 243>>>："If authentication is not available or does not return a profile name for whatever reason, Access Classification rules are applied to determine the profile assignment."
    - <<<PAGE 244>>>：有线规则类型（Port/MAC/MAC OUI/MAC+Port/MAC+IP+Port/LLDP/认证类型/IP+Port）；无线规则类型（MAC/BSSID/ESSID/DHCP Option/DHCP Option 77/加密类型/位置）。
