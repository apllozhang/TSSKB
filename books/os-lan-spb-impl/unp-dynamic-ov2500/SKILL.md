---
name: unp-dynamic-ov2500
description: 何时用：终端动态归档建 SAP（UNP 分类/802.1x/静默设备/编号公式）或 OV2500 编排纳管 SPB 网时。
source_book: DT00XTE323EN SPB Concepts & Implementation
---

# UNP 动态服务与 OV2500 编排

## R · 原文引用

> "Traffic received on UNP access ports that is not assigned to a configured service profile is assigned to the System Default service profile. Default I-SID number Calculation: 10,000,000 + (Domain ID * 10,000) + (Vlan Tag % 512). Default SPB Service ID number Calculation: Service ID number: 32768 incremented by 1... Default BVLAN number to use: BVLAN index (Calculated I-SID number %8)" (p274/275)

> "UNP Port classification rule precedence 1. – MAC address + VLAN tag 2. – MAC address 3. – MAC address range + VLAN tag 4. – MAC address range 5. – IP address + VLAN tag 6. – IP address 7. – VLAN tag" (p267)

> "-> aaa authentication snmp local -> user snmpuser password "Superuser=1" read-write all no auth -> snmp security no-security -> snmp community-map public user snmpuser enable -> snmp station 192.168.100.107 snmpuser v2 enable" (p309；注：用户名禁用 admin/diag/user)

> "Use Case: Silent Device -> unp profile silent map service-type spb tag-value 100 isid 1004 bvlan 4002 -> unp port 5/1/1 profile silent -> unp profile silent mac-mobility. A persistent SAP does not age out ... Up to eight SPB service profiles per UNP port" (p272/273)

## I · 方法论骨架

1. **UNP 决策流**（f10）：UNP 口流量 → 分类规则命中 → 按 profile 建 SAP；未命中且开启动态服务 → 按 System Default 公式自动建 I-SID/Service/BVLAN。
2. **三个确定性公式**（p20）：I-SID = 10,000,000 + 域ID×10,000 + (VLAN tag mod 512)；Service ID 从 32768 递增；BVLAN = I-SID mod 8 做索引取已建 BVLAN。基数/模数可用 `unp system-default service-base/service-mod` 调。
3. **七级分类优先序**（p19）：MAC+VLAN > MAC > MAC段+VLAN > MAC段 > IP+VLAN > IP > VLAN tag。
4. **持久 SAP 保静默设备与 VRRP**（p22）：静态指派 profile 生成不老化 SAP（每口最多 8 个服务 profile）；mac-mobility 保 VRRP 主备通告不中断。
5. **OV2500 上线五步**（f11）：快照开机 → EVAL License → 交换机侧 SNMP → 按控制 BVLAN 网段发现 → 拓扑 Poll Latest Data。

## A1 · 书中案例（Lab 配置序列精要）

Lab8 UNP 三场景（c15，p279/281/286）：
```
! 场景1 动态服务
unp port 1/1/1 port-type access
unp system-default service-base 1000
! 场景2 802.1x
service 4005 spb isid 4005 bvlan 2002 description Training stats enable vlan-xlation enable
unp profile UNP-employee
unp profile UNP-employee map service-type static tag-value 0 service-id 4005
aaa radius-server AAA host 192.168.100.102 key alcatel-lucent
aaa device-authentication 802.1x AAA
! 场景3 静默设备（持久 SAP）
unp profile unp-profile-silent map service-type spb tag-value 90 isid 1111 bvlan 2007 vlan-xlation
unp port 1/1/4 profile unp-profile-silent
unp classification mac-address "@mac Silent-A" profile1 unp-profile-silent
```
Lab9 OV2500（c16，p304/306/309）：带内管理 `ip interface "spb-mgmt" address 172.30.1.x/24 vlan 2000` → SNMP 六条（见 R）→ OV 侧 OV-init 快照 + EVAL-OV2500 License（90 天）→ `Discover New Devices (172.30.1.1-8)` → `Topology → SPB Network → Poll Latest Data`。

## A2 · 触发场景（含与相邻 skill 的区分）

- 终端上线自动归服务、802.1x/MAC 认证分流、打印机类静默设备、VRRP 通告要过 UNP 口、网管要图形化开通/监控 SPB 时用本 skill。
- 与 `spb-l2-service` 的区分：静态 SAP 手工建归 L2 服务 skill，本 skill 是 profile 驱动的动态 SAP；与 `spb-hybrid-etree` 的区分：UNP profile 的 e-tree 选项是本 skill 的动态形态补充。
- OV2500 纳管前提是 `spb-backbone-deploy` 里的控制 BVLAN 带内管理已就绪。

## E · 可执行步骤

1. 规划编号：确定域 ID 与 VLAN tag 空间，用公式预演 I-SID/BVLAN（如 VLAN 412 → I-SID 10,000,412）；多租户冲突则调 service-base/service-mod。
2. 建服务 profile：`unp profile <name>` + `map service-type spb tag-value <t> isid <i> bvlan <b>`。
3. 声明 UNP 口：`unp port <p> port-type access`，按需加 `802.1x-authentication` 或静态 profile 指派。
4. 配分类规则（按七级优先序设计）：`unp classification {mac-address|mac-range|ip-address|vlan-tag} ... profile1 <name>`。
5. RADIUS 联动：`aaa radius-server` + `aaa device-authentication 802.1x AAA`，`aaa test-radius-server` 单测。
6. 静默/VRRP 场景：静态 profile + `unp profile <name> mac-mobility`（先全局 `unp mac-mobility`）。
7. OV2500：快照开机改密 → 生成导入 EVAL License → 交换机 SNMP 六条 → Range List 发现 → 拓扑轮询；验证 `show service spb`（Dynamic * 标记）、`show unp user [details]`。
8. 关闭自动建服务：`unp port <p> dynamic-service none`。

## B · 边界与陷阱

- **SNMP 用户名禁用 admin/diag/user**（ce12/p35）：建号失败先查保留字；`snmp community-map mode enable` 别漏。
- **UNP 隔离用户不能重定向补救**（ce13/p34）：NAC 合规整改设计要绕开 Quarantine Manager 重定向。
- **multi-untag-sap 平台限制**（p21）：仅 UNP 动态 SAP 且仅 6860N/6900 系列新平台支持。
- 每口最多 8 个 SPB 服务 profile（p22）；动态创建的服务默认 head-end 组播、vlan-xlation 使能（p20）。
- 分类优先序意味着 vlan-tag 兜底规则会吞掉所有未命中流量，精确规则要排在其语义之前生效（p19）。

---
来源条目: f10, f11, p19, p20, p21, p22, p34, p35, c15, c16, ce12, ce13, g12, g27, g29, g37
