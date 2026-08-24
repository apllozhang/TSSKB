---
name: site-survey-ekahau
description: 何时用：WLAN 项目需做预测/预部署/后部署勘测、画墙仿真、现场排障覆盖问题时，按此流程执行。
source_book: DT00XTE368EN Stellar WLAN Enterprise Basic
---

# 站点勘测方法（Ekahau 全流程）

## R · 原文引用

> "SITE SURVEY TASKS: PLAN > VALIDATE > MONITOR > TROUBLESHOOT. PLAN: PREPARATION & REQUIREMENTS, PREDICTIVE SITE SURVEY. VALIDATE: PRE-DEPLOYMENT SITE SURVEY, INSTALLATION AND CONFIGURATION, POST-DEPLOYMENT SITE SURVEY. MONITOR/TROUBLESHOOT: SPECTRUM ANALYSIS, PACKET ANALYSIS, PERIODIC CHECK-UPS, CONTINUOUS MONITORING." (p85)

> "Predictive Survey / Virtual Survey: Uses variables: Building materials, Square footage, Number of wireless users, Applications, Access point models..." (p110-121)

> "The site survey is a snapshot in time. The more snapshots you have the better you can understand the environment." (p133)

> "Metal absorb Wi-Fi signals. Elevators block Wi-Fi signals to a great extent... Tinted glass and window film have metal in them so expect a drop in signal strength." (p136)

## I · 方法论骨架

1. **四阶段任务地图**：PLAN（需求+预测勘测）→ VALIDATE（预部署勘测→安装配置→后部署勘测）→ MONITOR/TROUBLESHOOT（频谱/抓包/巡检/持续监控）。
2. **勘测五型选型**：预测（软件仿真，无需到场）/ 被动（只听不关联，测 RSSI/SNR/干扰）/ 主动（关联入网，测丢包/RTT/漫游）/ 吞吐（吞吐+抖动）/ 频谱（检测一切 RF 源与占空比）。
3. **预测七步**：导入楼层图→WOW 标比例画墙（赋 dB 衰减）→导入设置→Area 圈区设终端→Auto-Planner 自动摆 AP（可调型号/功率/信道带宽/双 5GHz/最低速率/频段引导等）→复核调参重跑→出报告。
4. **现场排障三步**：平面图定位（障碍/优先区/AP 落点）→实测五查（AP 型号、同频/邻频、覆盖空洞、功率、布放）→五类纠正（换型号/重做 RF/收窄信道/删低速率/改善布放）。

## A1 · 书中案例（Lab 精要）

- 预部署 Stop-and-Go（p126）：AP 装三脚架通电，Ekahau 走测点击采样，一个点位测完 Freeze 该 AP 再搬站，多点位拼整层热图。
- 后部署主动勘测（p127-128）：网内装 ePerf 吞吐服务器，Continuous Survey 匀速走测，采集认证/关联/丢包/RTT/吞吐，加注覆盖空洞与天线朝向后出报告，留作性能基线。

## A2 · 触发场景（含与相邻 skill 的区分）

- 新建/改造 WLAN 前做设计、部署后做验收、客户投诉"WiFi 差"——用本 skill。
- 纯理论解释（为什么 6 GHz 快）——转 wlan-theory-fundamentals；AP 已定位到注册/配置问题——转 enterprise-mode-onboarding；漫游类"固定区域掉线"——转 roaming-l2-l3。

## E · 可执行步骤

1. 按四阶段把项目工作项列表，确认不漏"后部署验证"与"持续监控"环节。
2. 预测勘测：按七步执行，画墙时用标准衰减值——砖墙 10 dB、混凝土 12 dB、石膏板 3 dB、室内窗 1 dB、钢质防火门 13/19 dB、卷帘门 11 dB（保守口径：门全关）。
3. AP 布放：天线初始垂直朝向；AP 与墙面等距、尽量居中、高于所有障碍物；长走廊用半定向；远离热源暴晒。
4. 现场干扰对照：2.4G 查微波炉/无绳电话/荧光灯/蓝牙；5G 查雷达/卫星/户外桥接；金属货架、电梯井、镀膜玻璃按屏蔽体处理（电梯覆盖放井顶/井底/轿厢内）。
5. 排障走三步法，五查先行再选五类纠正措施之一。
6. 交付勘测报告时写明"时间快照"局限性，建议周期性复测。

## B · 边界与陷阱

- 勘测预测不了未来的使用模式/扩容/外部干扰——别承诺"测一次管五年"。
- 无线网络禁止 Over provisioning：信道数是硬上限，堆 AP 会自干扰；容量不足重做 RF 设计。
- 勘测复现不了大规模并发负载，也建议不了天线朝向——天线方向图必须人工调试验证。
- "勘测全绿、用户吐槽"优先查并发负载与天线朝向两个盲区。

---
来源条目: f01, f02, f03, f04, f05, p13, p14, p15, p35, ce02, ce03, ce04, ce05, g19, g20
