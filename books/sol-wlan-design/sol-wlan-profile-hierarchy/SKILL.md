---
name: Stellar 三级配置体系与部署服务（RF Profile/AP Group/SSID/Enterprise-Express 模式/部署协助服务包）
description: 需要落地 Stellar WLAN 配置或订购 ALE 部署服务时使用：RF Profile（信道计划/功率/扫描）-AP Group（设备组管理）-SSID（认证/漫游/带宽合约/QoS 映射）三级配置体系、Enterprise vs Express 模式选型、访客与监控两套模板要点、部署协助服务（Ekahau 预测勘测/ACSE 认证/5 天交付）前置条件与订购。
source_book: OmniAccess Stellar HD Design Guide 附录 + Fine-Tuning 附录 + Deployment Assistance Datasheet
---

## R（触发场景）
- 把设计蓝图落成配置：按区域/设备组/业务三级组织参数
- 决定 AP 运营模式：Enterprise（OmniVista 集中）vs Express（集群自治）
- 查参数默认值与推荐值（信标间隔/DTIM/带宽合约/WMM 映射等）
- 订购或交付 ALE 部署协助专业服务

## I（核心理念）
三级配置体系各管一维（F4，<<<PAGE 27-38, 66-72>>>）：RF Profile 按区域差异化（频段/信道计划/功率/扫描）、AP Group 按设备组统一（SSH/SNMP/IGMP/日志）、SSID 按业务差异化（认证/漫游/带宽/QoS）。配置粒度对应管理责任：区域 RF 环境、设备组运维、业务体验。HD 指南附录给出访客与监控两套完整模板、微调简报附录给出默认值与推荐值对照表，照表落地即可。

## A1（行动框架）
1. 三级配置体系（F4）：
   - RF Profile：频段/信道计划（DRM/Channel List）/信道宽度/收发功率范围/信标间隔/扫描
   - AP Group：SSH/SNMP/IGMP Snooping/日志上送
   - SSID：认证方式/最低速率/漫游（11r/k/v/OKC/FDB）/带宽合约/广播组播优化/QoS 映射
2. 运营模式选型：Enterprise = OmniVista 集中管理（单机 4000 AP/组）；Express = 集群自治（256 AP/集群）（<<<PAGE 47>>>）；高密场馆用 Enterprise（P5）
3. 服务路径（<<<PAGE 73-75>>>）：自建（预测勘测 Ekahau Pro + 现场勘测）vs 订购部署协助服务（前置：ACFE 认证 + 一次办公部署经验 + HLD 已完成）

## A2（操作步骤）
- **RF Profile 参数基准**：信标间隔默认 100ms，极高负载可增至 150ms（<<<PAGE 29, 68>>>）；扫描间隔 <40s（X20，<<<PAGE 56>>>）
- **SSID 参数基准**：DTIM 间隔 Apple 互通建议 3（<<<PAGE 71>>>）；Bandwidth Contract 上/下行及突发 0-2621440 Kbps（<<<PAGE 32, 72>>>）；Client Isolation 与 PMF 按安全需要（<<<PAGE 70>>>）
- **QoS 映射**：WMM 四类（AC_BK/BE/VI/VO）↔ 802.1p/DSCP；Trust Original DSCP 信任上行原值（<<<PAGE 32, 63>>>）
- **模板套用**：访客 SSID=开放+Captive Portal+限速+客户端隔离；监控 SSID=802.1X+流速率限制（P17，<<<PAGE 9-10>>> + 附录）
- **部署协助服务交付**（C21，<<<PAGE 75>>>）：5 天交付包——项目启动会/数据分析/Ekahau 预测勘测/现场勘测/部署辅导/DT00WTE278 课程与 ACSE 认证；eBuy 订购号 PS-PAER-5-NET
- **运维监控配套**：QoE 评分驱动（P34，<<<PAGE 25>>>）；Custom Dashboard 为媒体包厢等专区聚合统计（C12，<<<PAGE 23>>>）；客户端密度图（Cirrus 10.4.1+，<<<PAGE 24>>>）

## E（实证案例）
- HD 附录访客与监控两套三级配置模板 + 454 AP 的 BOM（<<<PAGE 27-44>>>）
- 媒体包厢 Custom Dashboard 自定义仪表盘（C12，<<<PAGE 23>>>）
- 部署协助服务五天交付包全流程（C21，<<<PAGE 75>>>）

## B（反例与坑）
- 手工功率设置值超型号能力时按最大能力发射，设定失效（X18，<<<PAGE 67>>>）
- 关闭 High Efficiency 使 11ax AP 降级 VHT 模式（X19，<<<PAGE 68>>>）
- Beacon Interval 增大省空口但影响发现速度，仅极高负载调至 150ms（<<<PAGE 68>>>）
- 订购部署协助服务前必须满足三前置（ACFE/办公部署经验/HLD），缺一不接（<<<PAGE 75>>>）
- AP Group 与 RF Profile 混配错区会导致相邻区域信道计划冲突——按区域严格分 Profile（P14，<<<PAGE 8>>>）

来源：HD Design Guide 附录（p27-44）+ Fine-Tuning 附录（p66-72）+ Deployment Assistance Datasheet（p73-75）
