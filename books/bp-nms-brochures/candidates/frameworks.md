# frameworks — bp-nms-brochures（产品线定位矩阵/代际演进）

- **F1 OmniVista 管理产品代际与形态矩阵** <<<PAGE 9>>> / <<<PAGE 10>>>
  ```
                云端 SaaS                 本地 On-Prem
  上一代     OmniVista Cirrus 4        OmniVista 2500
  新一代     OmniVista Cirrus          OmniVista Terra
             （微服务/多租户/MSP）      （≤5000 设备/Active-Active L2/数据主权）
  伴随层     OmniVista Network Advisor（AI/ML 异常检测+修复，混合架构，p1）
  ```
  依据摘录 <<<PAGE 10>>>："migrating from OmniVista Cirrus 4 or OmniVista 2500... to the new platform"；<<<PAGE 9>>>："OmniVista Cirrus – Cloud-based... OmniVista Terra – On-Premises"。

- **F2 管理深度光谱：从免费盘点到 AI 自愈** <<<PAGE 5>>> / <<<PAGE 1>>> / <<<PAGE 9>>>
  ```
  免费资产可见 → 网管平台（配置/监控/NAC）→ AI 运维伴随 → 现场独立工具
  Fleet Supervision   OmniVista C/T        Network Advisor    Smart Tool
  （零成本,自助注册）  （订阅制全功能）      （异常检测/自动修复） （免云免CLI,OT专用）
  ```
  选型第一问：客户痛点在"看不见资产"、"管不住配置"、"修不过来告警"还是"现场没人会装"。

- **F3 订阅分档三轴模型（Cirrus/Terra 订购决策树）** <<<PAGE 16>>> / <<<PAGE 17>>> / <<<PAGE 19>>>
  ```
  轴1 形态：云 Cirrus（可 Flexible Pay）/ 本地 Terra（仅预付，多 7 年期选项）
  轴2 服务档：Base（软件支持）→ Business（+设备硬件维保 AVR）→ Premium（+最终客户直享支持）
  轴3 设备档：AP 分 APL（x0x/x1x/x2x）/ APH（x3x 及以上）；交换机按系列 63/64/65/68/69/99；
             Flexible Pay 分 Essential（AP+OS63/64/65） / Advanced（OS68 及以上）
  ```

- **F4 运维工具按"谁在用/在哪用"定位** <<<PAGE 2>>> / <<<PAGE 22>>> / <<<PAGE 7>>>
  ```
  IT 网络团队日常运维 → OmniVista 平台 + Network Advisor（Rainbow/Teams 伴随）
  安防/视频运维人员   → Milestone Plugin（在 VMS 界面内复位摄像机）
  OT 现场装维外包人员 → Smart Tool（手机/PC 直连交换机，免 CLI 免云）
  资产/合规经理       → Fleet Supervision（Web 仪表盘）
  ```
  同一网络可同时部署多工具，互不替代。

- **F5 ALE"订阅+设备合同"总拥有成本检查清单** <<<PAGE 16>>> / <<<PAGE 4>>> / <<<PAGE 3>>>
  ```
  1. 网管订阅本体（OVCX/OVTX 或 NETAD SKU）
  2. 设备级支持合同（Base 档与 Flexible Pay 均不含，需另购）
  3. 自备资源（NetAdvisor 虚拟机 8GB+/Terra 虚机 8vCPU/3TB）
  4. 版本升级预算（交换机 AOS 8.9R1+、AP AWOS 5.0.1MR+ 前置）
  5. 老设备淘汰（AP1101/AP1201H 不支持新平台）
  ```
