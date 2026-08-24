# BOOK_OVERVIEW — DT00XTE317 · OmniVista Cirrus / Terra Deployment and Configuration (Edition 10)

## 基本信息与定位
- **课程编号**：DT00XTE317（Participant's Guide，478 页）
- **受众**：部署和配置 OmniVista Cirrus（云 SaaS）与 OmniVista Terra（本地部署版）网管平台的工程师
- **技术栈**：OV Cirrus 云平台 + OV Terra（3-VM Kubernetes 集群形态）+ Stellar AP + OmniSwitch

## 全书结构（章节地图）
| 页码范围 | 章节 | 核心内容 |
|---|---|---|
| p1-10 | Cirrus 概览 | 云管平台定位、有线无线特性清单、网络前置条件（防火墙端口/域名白名单） |
| p11-19 | Terra 概览 | 本地部署 NMS 定位、高层架构、网络前置条件 |
| p20-29 | Licenses & Subscription（Cirrus） | License 订购与下发流程 |
| p30-71 | Account & Organization | 账号创建激活、Partner/MSP/Customer 三级账号体系、组织创建、Trial 试用期申请与转正、MSP Dashboard、组织迁移、License 导入 |
| p72-92 | Terra 服务器安装 | VM 部署要求、安装步骤、WebAdmin 登录、Admin 账号、集群设置、IP/SMTP、Build 部署（K8s Nodes/Pods 状态）、DNS 配置、初始登录 |
| p93-119 | Terra License 与组织 | Terra 侧 License 导入与验证、组织创建 |
| p120-136 | Sites and Users | 站点创建、楼宇/楼层配置、组织级用户邀请（单个/批量） |
| p137-157 | Stellar AP Onboarding | 前置条件、Device Catalog、激活状态与日志、设备定位、AP Group、Provisioning Configuration |
| p158-176 | OmniSwitch Onboarding | 交换机激活流程、Device Catalog Inventory |
| p177-478 | 后半部：SSID/交换机配置管理/监控告警/运维 | 无线业务下发、有线配置、监控与告警、运维（对应站内 v1 课程后段） |

## 关键技术主题（提取器重点关照）
1. **Cirrus vs Terra 双形态**：同一平台的云/本地两种部署，功能与前置条件差异
2. **三级账号体系**：Partner/MSP/Customer 的权限与组织挂接、组织在 MSP 间迁移
3. **Terra 3-VM K8s 部署链**：VM 要求→安装→集群设置→Build 部署→DNS→初始登录全序列
4. **Trial 试用转正流程** 与 License 导入验证
5. **Device Catalog 激活状态机**（AP 与交换机 onboarding 排障入口）
6. **AP Group + Provisioning Configuration** 配置下发模型
7. **网络前置条件清单**（防火墙放行，部署失败的常见根因）

## 原文风格与引用注意
- 幻灯片短句 + 大量 Web UI 截图（314 张图）
- 与站内 v1 旧课（postsales/ov-terra，10 单元）同源——本次为新流水线重跑版，产出将替换旧课

## 与站内其他书的关系
- acfe-wlan（T360）覆盖 Cirrus 云管交付（AP 生命周期），本书更全面（含 Terra 本地部署与账号组织体系）
- ov2500-nms-admin 是另一条本地 NMS 产品线（OV2500），架构不同
