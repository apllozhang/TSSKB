# BOOK_OVERVIEW — DT00XTE216 · OmniSwitch LAN Core Switching (Edition 15)

## 基本信息与定位
- **课程编号**：DT00XTE216EN（Participant's Guide，724 页）
- **受众**：负责园区核心/汇聚层的网络工程师（核心交换专题，接入层内容见 T215）
- **技术栈**：OmniSwitch AOS R8 核心特性 + 路由协议

## 全书结构（章节地图）
| 页码范围 | 章节 | 核心内容 |
|---|---|---|
| p1-21 | Introduction + R-Lab | 课程组织、远程实验连接 |
| p22-34 | Portfolio | OmniSwitch 家族与 Stellar AP 产品线速览 |
| p35-64 | Ethernet Ring Protocol (ERP) | 环网协议概念、稳态/故障/恢复状态机、配置序列 |
| p65-95 | MACsec | 二层加密概述（802.3br/preMACsec）、密钥管理、配置与监控、Security Admin |
| p96-112 | Private VLAN | Primary/Isolated/Community VLAN 类型、Promiscuous/Host 端口类型、配置 |
| p113-149 | MSTP | 多生成树：Region、实例、域内/域间、配置与监控、完整示例 |
| p150-164 | MVRP | 多 VLAN 注册协议、动态 VLAN 成员传播、CLI 配置与监控 |
| p165-210 | Consistent AOS Network Security | DoS 保护/过滤、UDP Relay、认证 Trap、ARP 防御（ARP 欺骗检测/本地代理 ARP/ARP 过滤）、Port Mapping、MAC 强制转发、Storm Control、Learned Port Security |
| p211-235 | IP 接口与静态/RIP 路由 | IP 接口、静态路由（含递归）、RIP 规格/命令/定时器、EMP 端口 ACL |
| p236-295 | OSPF 基础+进阶 | 邻居/DR-BDR、Router 类型（BB/IR/ABR/ASBR）、LSA 类型、Area 类型（Standard/Stub/Totally Stubby/NSSA）、路由重分发、ECMP、汇总、接口认证、Virtual Link、监控 |
| p296-724 | 后半部 | Route Map/路由重分发、BGP、组播、QoS、VPN、IPv6、VxLAN 等进阶专题与综合 Lab |

## 关键技术主题（提取器重点关照）
1. **ERP 环网状态机**：RPL owner/blocking、稳态-故障-恢复转换与收敛时序
2. **MACsec 全链**：preMACsec/802.3br、密钥协商、配置与监控命令、Security Admin 区别
3. **Private VLAN 模型**：三类 VLAN + 两类端口的矩阵及配置陷阱
4. **MSTP Region 与实例设计**：域边界、实例到 VLAN 映射、监控命令
5. **ARP 防御武器库**：欺骗检测/代理 ARP 过滤/MFF 的适用场景对比
6. **Learned Port Security**：学习端口安全的配置与违例处理
7. **OSPF 四 Area 类型的边界**（Stub/Totally Stubby/NSSA 的 LSA 差异）
8. **路由重分发与 Route Map** 语义

## 原文风格与引用注意
- 幻灯片短句 + CLI 命令块（`>>>` 提示符）+ 拓扑图
- 与站内 v1 旧课（11 单元 core switching）同源——本次为新流水线重跑版，产出将替换旧课
- 与 os-lan-access-switching（T215）互补：T215 讲接入基础，本书讲核心特性与路由

## 与站内其他书的关系
- MSTP/安全特性与 os-lan-access-switching 部分重叠，但本书深度更高（Area 类型、MACsec、ERP）
