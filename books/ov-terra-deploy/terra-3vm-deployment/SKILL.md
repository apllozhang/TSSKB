---
name: Terra 3-VM 部署
description: 当需要从零部署 OmniVista Terra 本地集群（OVA 部署、控制台初始化、WebAdmin 首设、Build 部署、DNS 配置）时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 客户采购了 Terra，需要在其 VMware 环境部署 3-VM 集群
- 部署 build 后 Dashboard 上 Pod 状态异常，需要定位
- 部署前核对 ESXi/CPU/RAM/磁盘等硬件门槛

## I（核心理念）
Terra 是 3 台 VM 组成的 Kubernetes 集群（Active-Active 高可用），部署分四层：①虚拟化资源（硬性 CPU 指令集要求）→ ②OVA + 控制台网络初始化 → ③WebAdmin（端口 3000）首设与 build 上传 → ④DNS 四域名解析。每一步都有明确的验证命令和失败取证入口。

## A1（行动框架）
1. **硬件与环境核对**（<<<PAGE 75>>>）：
   - 3 台 VM；ESXi 最低 8.0；每台 8 vCPU @3GHz、RAM 32GB、SSD（≥50MB/s）、System Disk 200GB、Data Disk 3TB
   - CPU 必须支持 AVX/AVX2；vCenter 集群需开 EVC，基线推荐 Ice Lake，最低 Broadwell
2. **部署 OVA**：下载 OmniVista Terra OVA 与 build (.7z)，部署时输入 Name、选 NIC card，上电（<<<PAGE 76>>><<<PAGE 77>>>）。
3. **控制台初始化**（每节点）：键盘布局 → hostname（如 ovtx-100）→ IP/掩码/网关/主备 DNS（必须能解析 myovterra.myovcloud.com）→ ovtx 用户密码 → 应用配置重启 → `ip addr` 验证；第 2/3 节点换 hostname/IP 重复（<<<PAGE 78>>><<<PAGE 79>>><<<PAGE 80>>>）。
4. **WebAdmin 首次设置**：浏览器访问 `<Node_IP>:3000` → 创建 admin 账号 → General Info（Email/Company/Country/Timezone/预期 AP 与交换机数量）→ 输入第 2/3 节点 IP 并确认可达 → 定义 4 个 IP（Main / VPN / UPAM Captive Portal / UPAM Radius）→ SMTP（示例 smtp.gmail.com:465，TLS/StartTLS + SMTP 认证）（<<<PAGE 82>>><<<PAGE 83>>><<<PAGE 84>>><<<PAGE 85>>><<<PAGE 86>>>）。
5. **部署 Build**：选 build release file (.7z) 上传 → Done → Confirm the deployment；完成后刷新 admin center 看 Dashboard 的 Nodes 与 Pods 状态（<<<PAGE 87>>><<<PAGE 88>>><<<PAGE 89>>>）。
6. **配置 DNS 四域名**（在客户 DNS 服务器，如 Windows DNS）（<<<PAGE 90>>>）：
   - activation.myovterra.com / as.myovterra.com → Main IP（activation server）
   - vpn.myovterra.com → VPN IP
   - images.myovterra.com → Main IP（Image Server）
   - myovterra.myovcloud.com → Main IP（主 URL）
7. **首次登录**：以 myovterra.myovcloud.com 登录（<<<PAGE 91>>>）。

## A2（进阶应用）
- Terra 组织创建后自动激活 90 天 Trial（<<<PAGE 110>>>），可边试用边完成生产 License 导入。
- 高层架构：VMware 多服务器高可用（Active-Active L3）、Kubernetes 集群、VM×3、VPN Server/Load balancer、Kafka/MQTT、HTTPS（<<<PAGE 17>>>）。
- 部署失败时在 Install 菜单看状态（Success/Failure/In Progress），点 "Download the logs" 取安装日志（<<<PAGE 89>>>）。

## E（实证案例）
- **案例 1**：vCenter 集群 EVC 基线设为低于 Broadwell 的老基线，Terra 部署失败——CPU AVX/AVX2 指令集不满足；改基线为 Ice Lake（或最低 Broadwell）后成功（<<<PAGE 75>>>）。
- **案例 2**：节点 DNS 无法解析 myovterra.myovcloud.com，控制台配置卡住——配置 DNS 前必须确保解析可行（<<<PAGE 78>>>）。

## B（边界与陷阱）
- **EVC 基线禁区**：低于 Broadwell 的基线必失败（<<<PAGE 75>>>）。
- **不要靠猜排障**：部署失败先 Download the logs 取证，不要盲目重部署（<<<PAGE 89>>>）。

## 来源
- frameworks·Terra 3-VM 部署全流程（<<<PAGE 76>>><<<PAGE 77>>><<<PAGE 78>>><<<PAGE 79>>><<<PAGE 80>>><<<PAGE 82>>><<<PAGE 83>>><<<PAGE 84>>><<<PAGE 87>>><<<PAGE 90>>><<<PAGE 91>>>）
- principles·Terra 高层架构 3-VM Kubernetes（<<<PAGE 17>>><<<PAGE 75>>>）
- principles·Terra VM 硬件要求（<<<PAGE 75>>>）
- principles·Terra DNS 四域名映射（<<<PAGE 90>>>）
- cases·Terra 部署 VM OVA 与控制台初始化（<<<PAGE 76>>><<<PAGE 77>>><<<PAGE 78>>><<<PAGE 79>>><<<PAGE 80>>>）
- cases·WebAdmin 首次设置（<<<PAGE 82>>><<<PAGE 83>>><<<PAGE 84>>><<<PAGE 85>>><<<PAGE 86>>>）
- cases·Terra Build 部署与状态检查（<<<PAGE 87>>><<<PAGE 88>>><<<PAGE 89>>>）
- cases·Terra DNS 配置（<<<PAGE 90>>><<<PAGE 91>>>）
- counter-examples·CPU AVX/AVX2 与 EVC 基线陷阱（<<<PAGE 75>>>）
- counter-examples·部署失败时的取证路径（<<<PAGE 89>>>）
