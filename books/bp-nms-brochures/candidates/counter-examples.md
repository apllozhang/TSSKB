# counter-examples — bp-nms-brochures（限制/边界/订购注意）

- **X1 Network Advisor 虚拟机需自购，ALE 不卖** <<<PAGE 3>>>
  "Virtual Appliance to be acquired separately (not sold by ALE)"
  要点：NetAdvisor 本地组件的虚拟机要客户自备，报价时勿遗漏。

- **X2 NetAdvisor 不依赖 OmniVista Cirrus** <<<PAGE 3>>>
  "OmniVista Cirrus is not required"
  要点：买 NetAdvisor 不强制先买 Cirrus。

- **X3 NetAdvisor 用户必须有 Rainbow 账号** <<<PAGE 3>>>
  "OmniVista Network Advisor users must have an active Rainbow account"
  要点：交互全靠 Rainbow Bot/Bubble，无 Rainbow 无法用（p2 "Uses a dedicated Rainbow Bot and Bubble"）。

- **X4 NetAdvisor 第三方设备能力受限：仅 syslog + 手工定制** <<<PAGE 3>>>
  "Third-Party devices able to send syslogs (over Syslog Server support, with manual customization for anomalies and remediation rules)"
  要点：第三方设备无深度遥测，异常/修复规则要手工配。

- **X5 新 OmniVista 平台不支持 AP1101 / AP1201H** <<<PAGE 15>>>
  "(Access Points from AP 12xx, 13xx,14xx and 15xxSeries) - AP1101, AP1201H models not supported"
  要点：老 AP1101 与 AP1201H 被明确排除，存量客户需先换 AP。

- **X6 新 OmniVista 平台交换机门槛 AOS 8.9R1** <<<PAGE 15>>>
  "Devices with minimum AOS release 8.9R1"
  要点：比 NetAdvisor 的 8.7R2 更高；老版本交换机需先升级。

- **X7 Stellar AP 需 AWOS 5.0.1MR 起** <<<PAGE 15>>>
  "OmniAccess Stellar WLAN Access Points (Access Points 15xx series) with minimum AWOS release 5.0.1MR"
  要点：网管平台对接 AP 的最低固件，低于此版本纳管受限。

- **X8 Terra 仅支持 VMware/Hyper-V，ESXi 最低 8** <<<PAGE 15>>>
  "Supported virtualization platform: VMware and Hyper-V / Minimum ESXi version: 8 / AVX/AVX2 instructions must be supported / Disk must be SSD/NVMe with at least 50MB/s rate"
  要点：KVM/Nutanix 等不在列；老 ESXi 6.x/7.x 不支持；磁盘必须是 SSD/NVMe。

- **X9 Terra 无 Flexible Pay，只能预付** <<<PAGE 16>>>
  "Flexible Pay with variable durations and payment terms is available only for OmniVista Cirrus."
  要点：Terra 只有 PrePaid/Upfront；期限 1/3/5/7 年（Cirrus 1/3/5 年）。

- **X10 Base 档不含设备硬件维保与设备支持** <<<PAGE 17>>>
  "Base Support (Excluding device hardware maintenance and node support access)"
  要点：Base 只保 OmniVista 软件本身；设备维保需另购或升 Business/Premium。

- **X11 Terra 客户软件升级需自访问 ALE 仓库** <<<PAGE 16>>>
  "OmniVista Terra is deployed and managed on the customer's premises. Customers can access the ALE repository to upgrade to the latest device software and firmware version."
  要点：Terra 无云自动推送，升级由客户自己从仓库拉取执行。

- **X12 Flexible Pay 不含设备硬件维保** <<<PAGE 19>>>
  "Not included: Device hardware maintenance and Support access plans (sold separately)"
  要点：OPEX 月付模式仅含 SaaS+升级+支持入口，硬件维保单卖。

- **X13 Flexible Pay 最短 12 个月** <<<PAGE 19>>>
  "Require Subscription Configuration for duration (min 12-to-60-month max)"
  要点：不支持短于一年的订阅。

- **X14 迁移工具能力因源系统而异** <<<PAGE 10>>>
  "functionality may vary depending on source system and version"
  要点：OV2500/Cirrus4 迁移并非全自动等价迁移，需评估差异。

- **X15 Fleet Supervision 故障换新需有效最终客户支持合同** <<<PAGE 6>>>
  "For customers with an active end-customer support contract"（脚注 1，对应 "Request faulty device replacements directly to streamline operations"）
  要点：无支持合同不能在线发起换新。
