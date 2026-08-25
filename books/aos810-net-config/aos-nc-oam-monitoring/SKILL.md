---
name: AOS 8 OAM 与运维监测（CFM/EFM/健康监测/日志/SAA/PPPoE-IA）
description: 需要在 OmniSwitch AOS 8 上配置 Service OAM/CFM（MD/MA/MEP、loopback/linktrace、帧时延）、EFM LINK OAM（发现/链路监控/远端环回）、Switch Health 资源阈值、日志输出、SAA 服务保障测量、PPPoE Intermediate Agent 时使用。
source_book: OmniSwitch AOS Release 8.10R4 Network Configuration Guide
---

## R（触发场景）
- 端到端以太业务要连续性检查与故障定位：CFM CC/loopback/linktrace
- 单条链路质量劣化要监控告警：EFM errored-frame 窗口阈值
- 要测帧时延/抖动：Y.1731 帧时延测量
- 交换机 CPU/内存资源要阈值监控：Switch Health
- 要调日志级别/输出设备/格式，或做 SPB 服务保障测量（SAA）
- 宽带接入要在 PPPoE 报文插用户线路标识：PPPoE-IA

## I（核心理念）
OAM 分层框架（F14，<<<PAGE 1655>>>）：LINK OAM(802.3ah，单链路发现/监控/环回) 与 Service OAM(802.1ag/Y.1731，MD/MA/MEP 层级+CC/LB/LT+时延测量) 互补，CFM MD 分层 0-7 对应运营商/客户组织边界。MD 分级：5-7 客户、3-4 运营商、0-2 操作员；MEP 发起 OAM 命令防域间泄漏，MIP 被动应答（P196，<<<PAGE 1655>>>）。EFM 用慢协议 OAMPDU 承载控制与状态，单链路传递不被网桥转发；发现阶段双方能力匹配才建立 OAM 连接，5 秒无 OAMPDU 即失联（P198/P199，<<<PAGE 1673-1674>>>）。

## A1（决策框架）
1. **定位故障先分层**：单链路问题用 LINK OAM（发现/三窗口链路监控/远端故障/远端环回，P200，<<<PAGE 1673>>>）；业务端到端问题用 Service OAM（P195，<<<PAGE 1655>>>）
2. **MD 级别按组织边界规划**：运营商侧低级别（0-4）、客户侧高级别（5-7），避免 MEP 命令跨域泄漏
3. **链路劣化监控选 EFM 窗口**：errored-frame / errored-frame-seconds / errored-frame-seconds-summary 三窗口阈值+notify
4. **资源与运维面**：Switch Health 资源阈值+采样间隔（P190，<<<PAGE 1566>>>）；日志=级别筛选+输出设备+文件大小+格式+存储上限（P194，<<<PAGE 1580>>>）
5. **测量类**：帧时延测量（Y.1731）、SAA 以 SPB 会话做服务保障测量并可生成 XML 历史（P204，<<<PAGE 1700>>>）

## A2（操作步骤）
- **Service OAM**：`cfm domain`→MA→MEP/虚拟 MEP→loopback/linktrace/帧时延测量（cases·C62，<<<PAGE 1650>>>）；RFP 把连通故障事件传播到 MEP 所在接口（P197，<<<PAGE 1655>>>）
- **EFM LINK OAM**：`efm-oam enable`→端口使能→errored-frame(-seconds-summary) 窗口/阈值/notify（样例 `efm-oam port 1/1/1 errored-frame window 32 threshold 10 notify enable`）→远端环回；验证 show efm-oam（cases·C63，<<<PAGE 1672>>>）
- **Switch Health**：资源阈值+采样间隔监控 CPU/内存等并出统计（P190，<<<PAGE 1566>>>）
- **日志**：级别筛选+输出设备（console/memory/remote 等）+文件大小+格式+存储上限（P194，<<<PAGE 1580>>>）
- **SAA**：以 SPB 会话做测量，可生成 XML 历史文件（P204，<<<PAGE 1700>>>）
- **PPPoE-IA**：`pppoe-ia enable`→（可选）`pppoe-ia ignore-slot`（AOS6 格式 Circuit-ID）→`pppoe-ia port 1/1/1 enable`→trust/client 口→access-node-id/circuit-id/remote-id；验证 show pppoe-ia（cases·C64，<<<PAGE 1715>>>）

## E（实证案例）
- Service OAM domain→MA→MEP→测量（C62，<<<PAGE 1650>>>）
- EFM LINK OAM 窗口阈值与远端环回（C63，<<<PAGE 1672>>>）
- PPPoE-IA trust/client 口与线路标识（C64，<<<PAGE 1715>>>）

## B（反例/坑）
- LINK OAM 5 秒收不到 OAMPDU 邻接即丢，keepalive 间隔配置不当会频繁掉 OAM 会话（X72/P199，<<<PAGE 1674>>>）
- PPPoE-IA 不支持镜像目的口；全局+端口两级必须同时使能否则不生效（X73/P203，<<<PAGE 1715>>>）
- PPPoE access loop 标识：直连用户=chassis/slot/port，多用户共享口=端口+CVLAN 组合（P202，<<<PAGE 1714>>>）
- MD Level 分层对应组织边界，跨层规划会导致 OAM 命令泄漏或测量失效（P196，<<<PAGE 1655>>>）
- 虚拟 MEP 是虚拟端口上的 UP MEP，用于没有物理口的场景（<<<PAGE 1655>>>）

## 来源
OmniSwitch AOS 8.10R4 Network Configuration Guide 第 41 章 Switch Health（<<<PAGE 1566>>>）、第 43 章 Switch Logging（<<<PAGE 1580>>>）、第 44 章 Service OAM/CFM（<<<PAGE 1650-1665>>>）、第 45 章 EFM LINK OAM（<<<PAGE 1672-1674>>>）、第 47 章 PPPoE-IA（<<<PAGE 1714-1715>>>）、第 48 章 SAA（<<<PAGE 1700>>>）。条目来源：cases C62-C64；principles P190/P194-P204；counter-examples X72/X73；frameworks F14。
