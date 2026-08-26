# 全书精华串讲

## 一句话总纲

DAN 的主张：网络不再是复杂昂贵的底层设施，而是数字化转型的业务引擎——用自动化把"开通一个服务要几天"压缩到"几秒无错完成"，把海量不安全的 IoT 安全装进来，再把网络数据变成新营收（dan-overview p2；dan-wp-global p3）。

---

## 主线一：三支柱（技术叙事）

### 支柱 1：Autonomous Network（自主网络）——网的自动化

- **网络服务的新定义**：一个网络服务 = 从用户或物体到授权应用的自动安全连接（各文档反复出现）
- **核心组件**：
  - iFab（Intelligent Fabric）：自动部署网络、简化搬迁增改（MAC），基于 SPB（IEEE 802.1aq）充分利用全部物理链路
  - UnP（Universal network Profiles）：在接入层统一下发部门/应用/安全/QoS 策略，有线无线一致
  - 新一代 Wi-Fi：AP 内嵌控制、免物理集中控制器，分布式架构高性能高可用低 TCO
  - 单一 NMS：终结"有线一套系统、无线一套策略"的双头管理
- **技术彩蛋**：内嵌 L2-L7 DPI 应用可视，可按应用（Rainbow、WhatsApp、YouTube…）限速/阻断/优先级（dan-wp-global p6）
- **演进方向**：机器学习分析配置 + QoE + 已知问题，向管理员提变更建议（各版均标注为"未来"能力）

### 支柱 2：IoT onboarding——物的安全接入

统一的 IoT containment 三步法，所有行业彩页复用：

1. **Discover & classify**：29+ million 设备指纹库（2019 版为 17 million）自动识别、自动下发配置
2. **Virtual segmentation**：一张物理网切成虚拟容器，按设备要访问的应用自动分段
3. **Continuous monitoring**：全部授权设备入库存档（厂商/序列号/位置/状态），行为偏离（如突发大流量、大量 DNS 请求）即自动断开、告警或转容器核查

关键安全逻辑：**最大风险不在 IoT 设备本身，而在它被攻陷后打开的通往其他网段的门**（dan-wp-global p8）。

### 支柱 3：Business Innovation——流程的自动化与变现

- **位置服务双件套**：
  - OmniAccess Stellar Asset Tracking：Wi-Fi + Bluetooth 实时/历史定位，热点追踪、contact tracing、占用管理
  - OmniAccess Stellar LBS：wayfinding 室内导航 + geonotifications 位置推送，云端应用 + 分析仪表盘
- **Rainbow 工作流**：Location Services 数据接 Rainbow，用 triggers × rules → actions 把重复任务自动化
  - 全书最完整的编排实例（酒店）：会议排期为触发器 → 按起止时间配置会议室 AP → 自动建/删/启停 SSID、开关射频、密钥发组织者、通知网管（dan-hosp p7）
- **商业模式**：
  - NoD（Network on Demand）：CAPEX 转月度固定 OPEX 的"网络即服务"（dan-wp-global p11）
  - OmniVista Cirrus 云管：pay-as-you-go，内置访客接入、BYOD、分析（dan-wp-apac p10）

### 框架演变要点

- 2019 全球白皮书用"四趋势"框架：Connectivity / IoT / Augmented intelligence / Cloud economics
- 2022 APAC 白皮书起改用"三支柱"框架（与总彩页、行业彩页对齐），增强智能与云经济被吸收进 Autonomous Network 与 Business Innovation

---

## 主线二：六大行业（场景叙事）

行业彩页结构高度模板化（痛点 → 三支柱 → Location Services → Summary），差异点如下：

### 企业（dan-ent）
最"素"的一册：三支柱标准口径 + containment + Asset Tracking + 工作流，可作为无行业属性客户的默认模板。

### 教育（dan-edu）
- 多角色权限：学生（LMS/在线课程）、教师（成绩/科研）、行政（财务/安防）分权访问
- SPB 承载科研大流量（粒子加速、天文图像）与视频/AR 教学流量
- 特色主张：用网络数据（聚集、出勤、应用使用）辅助评估学生成功/流失风险——原文自认"还有长路要走"

### 政府/智慧城市（dan-gov）
- 独有论点：**智慧城市必须打破竖井**，水平参考架构 = 公共基础设施 + 服务层共享，避免每个垂直应用重复建网
- 智慧城市分层图：多制式接入（Wi-Fi/LPWAN/SCADA…）→ 服务层（分析/控制/定位/安全/数据代理）→ 用例（停车/照明/垃圾/监控）
- 独有能力：危机场景下优先保障一线响应人员通信与指定摄像头直播资源

### 医疗（dan-health）
- 核心概念：**融合但非合并（connected but not consolidated）**——多张科室网融进单一基础设施、保持虚拟隔离
- 三前提：医疗设备识别上线、4K 影像无损传输、EHR 随时随地低时延
- 特色能力：位置增强访问控制（人+设备+位置+应用组合策略）；标签按钮呼叫 + VNA 联动防警报疲劳；SD-WAN/SASE 承接养老照护远程站点

### 酒店（dan-hosp）
- 角色化接入：宾客/员工/IoT 不同 profile 不同权限
- 最完整的 IoT 多标准口径：Ethernet/Wi-Fi/BLE/Zigbee 原生 + IoT Hub 接第三方标准
- LBS 变现叙事最浓：位置促销、家庭组儿童看护、宾客车辆追踪、位置分析 × PMS/CRM 超个性化

### 交通（dan-trans）
- 全书最"硬"规格所在：WPA3、OS 加固交换机、单集群 4000 AP、室内外加固设备
- 轨交双网合一：关键任务网（信号/SCADA/安防）与业务网（售检票/零售 Wi-Fi）物理合一、逻辑隔离
- 机场多租户、智慧公路 ITS、港口 IoT 拓扑（双加密 + OXE 通信）各有专述

---

## 售前取用建议

- 给高层讲愿景 → dan-vision；给技术层讲架构 → dan-wp-enterprises；引用新口径与 APAC 案例 → dan-wp-apac
- 行业客户直接取对应行业单元的"痛点→组件"映射表（各单元 A2 段）
- 版本陷阱两处：设备库 17M（2019）vs 29+M（2022 起）；Gartner 预测多为 2018-2019 年发布
