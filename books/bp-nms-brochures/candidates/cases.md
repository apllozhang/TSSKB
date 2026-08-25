# cases — bp-nms-brochures（选型决策案例）

- **C1 MSP 管理多家客户网络：选 Cirrus 而非 Terra**
  场景：托管服务商要集中管理多个客户组织。决策依据 <<<PAGE 15>>>："Multi-tenancy services - Allow Managed Service Providers (MSP) and large organizations to effectively manage and monitor multiple associated customers"；而 <<<PAGE 10>>> 明确 "Multi-tenancy: OmniVista Cirrus" 仅云版支持。Terra 只有 Multi-sites（单组织多站点）。

- **C2 数据主权严格（政务/受监管行业）：选 Terra 而非 Cirrus**
  决策依据 <<<PAGE 9>>>："OmniVista Terra – On-Premises: addresses stringent requirements for local infrastructure management, data sovereignty, and advanced security compliance." 客户要求数据不出境时选本地部署 Terra。

- **C3 大型本地网络（≤5000 设备）：Terra 规格规划**
  场景： campus 全本地管理约 4000 台 AP+交换机。决策依据 <<<PAGE 15>>>："up to 5,000 devices... Scales from one to three virtual machines" — 按设备数规划 1-3 台虚机（每台 8vCPU/32GB/3TB 数据盘），超 5000 设备需评估拆分或多实例。

- **C4 老平台（OV2500/Cirrus 4）客户升级谈判**
  场景：客户担心换新平台要重配全部设备。话术依据 <<<PAGE 10>>>："Minimal device reconfiguration when migrating from OmniVista Cirrus 4 or OmniVista 2500... to the new platform" + 标准包自带迁移工具（"Migration Tool Availability - Included as part of the standard package"）。

- **C5 只想买网管软件、硬件已有维保：选 Base 档**
  场景：客户设备已购硬件维保，只要云网管。决策依据 <<<PAGE 17>>>：Base 档 "Base Support (Excluding device hardware maintenance and node support access) - Includes OVC Updates & Cloud Support access"。要硬件维保打包则升 Business（Partner Plus + AVR），最终客户要直享 ALE 支持则 Premium（<<<PAGE 16>>> "End Customer Access support"）。

- **C6 混合 ALE+第三方设备网络加 AI 运维：Network Advisor**
  场景：客户已有一批第三方交换机，想上异常检测。决策依据 <<<PAGE 1>>> "It can also interface with 3rd party devices able to send syslog" + <<<PAGE 3>>> 第三方设备走 "Syslog Server support, with manual customization for anomalies and remediation rules"，按 NETAD-TP-* 订阅（<<<PAGE 4>>>）。前提：自备虚拟机（ALE 不卖，见 X1）。

- **C7 视频监控行业客户：Milestone Plugin 优先于通用网管做摄像机运维**
  场景：安防集成商，摄像机频繁掉线需派人现场重启。决策依据 <<<PAGE 7>>>："eliminates the need for expensive on-site visits and vendor calls when camera problems arise" + "Faster resolution for more than 90% of camera issues"；且 <<<PAGE 8>>> 可按端口看 PoE 消耗并设摄像机 PoE 优先级。条件：客户用 Milestone VMS + OmniSwitch。

- **C8 OT 现场无云连接、装维外包：Smart Tool 而非 Cirrus**
  场景：工厂/交通现场，云不可达，装维人员非网络专业。决策依据 <<<PAGE 22>>>："Limited or restricted cloud connectivity in OT environments" → OST 是 "standalone, cloud-independent field utility"；差异化能力 <<<PAGE 23>>> PoE 向导 60 秒修复 + TDR 线缆测试。

- **C9 预算有限客户的零成本切入：Fleet Supervision 先行**
  场景：先给客户免费价值再谈付费网管。依据 <<<PAGE 5>>>："Free of charge online tool - Self signup approach"，先盘点资产/生命周期/支持合规（NIS2，<<<PAGE 6>>>），再据盘点结果推动软件升级与换新预算。

- **C10 OPEX 预算客户：Cirrus Flexible Pay**
  场景：客户拒绝一次性预付、要按月支出。依据 <<<PAGE 16>>>："Flexible Pay with variable durations and payment terms is available only for OmniVista Cirrus" + <<<PAGE 19>>> OVC-C-ESS-M / OVC-C-ADV-M 按月定价、12-60 月期限、月/季/年/预付四种付款节奏。注意 Essential/Advanced 设备分档对应关系。
