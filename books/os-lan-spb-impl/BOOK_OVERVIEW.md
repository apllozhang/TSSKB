# BOOK_OVERVIEW · OmniSwitch LAN SPB Concepts & Implementation (DT00XTE323EN)

> 教材: ALE Training Services · 367 页 · 售后 Experienced 路径（3 天实操课）
> 定位: SPB 售前书的**实施版**——同一技术体系从"讲卖点"变为"配出来"：骨干部署→L2/L3 服务→高级特性→动态服务→OV2500 编排

## 一、结构

1. **DAY 1** (p3-151): OmniFabric/Why SPB 复习 → Mac-in-Mac/控制面/数据面 → **Lab：SPB-M 骨干部署、L2 服务、协议分析与保护** → BUM 流量与排障
2. **DAY 2** (p152-258): IP over SPB 三部曲（IP Routing 冗余 / VPN-Lite / L3-VPN，各配 Lab）→ **SPB 高级配置**（Lab）
3. **DAY 3** (p259-344): **动态服务**（UNP SPB Dynamic SAP，Lab）→ **OV2500 SPB 编排**（Lab）→ 混合接入与 E-Tree 服务（Lab）→ 成功案例
4. **附录**: 老硬件上的 SPB 路由概念

## 二、解释

课程主线 = SPB 交付生命周期：Day1 打骨干（BCB/BEB/BVLAN/IS-IS）、Day2 加路由（VPN-Lite/L3VPN 配置对拍）、Day3 上自动化（UNP 动态 SAP/OV2500 编排/E-Tree）。与售前书的章节一一对应但全部落到 AOS CLI 和 OV2500 操作。

## 三、批判

与售前 SPB 书理论重叠约 40%（实施视角增值在 Lab 步骤与配置细节）；3 天节奏紧凑、Lab 环境不可复现时价值减半。

## 四、应用

SPB 交付工程师的配置手册：从零搭 SPB 骨干到 L3VPN 到动态服务的全 CLI 流程；排障章（BUM/协议分析）独立可用。
