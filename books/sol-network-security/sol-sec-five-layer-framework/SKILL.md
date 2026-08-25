---
name: ALE 五层集成安全框架与三平面加固体系
description: 需要对企业网络做整体安全规划或安全审计时使用：ALE 五层集成安全框架（用户/设备/应用/网络/IoT）、管理面/控制面/数据面三平面加固清单、Secure By Design 认证体系（CC/FIPS/JITC）、PSIRT 漏洞响应与物理访问边界。
source_book: Network Security Guidelines + Maximizing Security and Performance Whitepaper
---

## R（触发场景）
- 制定全网安全加固方案，需要分层分平面的系统化清单
- 安全审计：按管理面/控制面/数据面逐面核查 OmniSwitch/Stellar/OmniVista
- 对客户讲解 ALE 安全理念（Secure By Design、五层框架、认证资质）
- 建立漏洞响应与补丁管理流程

## I（核心理念）
安全是过程而非产品（P1，<<<PAGE 5>>>）：不可购买，是组织的持续保护方法。多层纵深防御（P2/P4，<<<PAGE 5>>>）：ALE 五层框架自用户/设备/应用/网络到 IoT 容器隔离逐层设防。三平面加固是全册主结构（F2，<<<PAGE 9-47>>>）：管理面（访问/AAA/证书/SNMP/日志/安全模式）、控制面（路由/发现/网管协议认证）、数据面（MACsec/地址防护/端口安全）。Secure By Design + 默认安全（P6，<<<PAGE 6>>>）：签名镜像、ASLR、默认 DoS 过滤、CC EAL2/NDcPP/FIPS/TAA 认证背书。安全对终端用户透明（P3，<<<PAGE 5>>>）。

## A1（行动框架）
1. ALE 五层集成安全框架（F1/P4，<<<PAGE 5-6>>>）：用户级（画像/AAA）→ 设备级（认证+合规预检）→ 应用级（按应用规则：阻断/限速/身份限定）→ 网络级（智能分析可见性 + DPI 识别异常）→ IoT 级（虚拟容器隔离，单点失陷不扩散，P5）
2. 三平面安全加固框架（F2，<<<PAGE 9-47>>>）：管理面 → 控制面 → 数据面逐面过清单（详见各专项技能：sol-sec-device-access 管理面、sol-sec-protocol-hardening 控制面+数据面）
3. 认证与响应基线：及时打补丁（P7）+ 订阅 ALE 安全通告（P8）+ PSIRT/CVE 流程（C2）+ 物理访问边界（P9）+ 人员意识培训（P10）

## A2（操作步骤）
- **供应链完整性**：AOS 镜像 RSA-4096+SHA-256 签名，重载时验签；U-boot ≥8.9.70.R04 仅支持签名镜像（C1，<<<PAGE 6>>>）；升级前 `image integrity-check` 手工校验（P13，<<<PAGE 9-10>>>）
- **漏洞响应**：PSIRT 与 CERT-IST/NVD/US-CERT 协作，报告带唯一 CVE 号，确认后发 Security Advisory（C2/P7/P8，<<<PAGE 7>>>）
- **物理层**：关键交换机上锁机房、限制进入；监控 coldStart/warmStart trap 检测设备被重启（P9/P11，<<<PAGE 8>>>）
- **合规认证引用**：Common Criteria EAL2/NDcPP、FIPS 140-2、TAA、IV&V 源码测试、ASLR（<<<PAGE 6>>>）
- **物理安全依赖网络安全**：看门的摄像头被远程禁用即物理失守（P88，<<<PAGE 99>>>）

## E（实证案例）
- 签名镜像验证供应链完整（RSA-4096/SHA-256，U-boot 8.9.70.R04+）（C1，<<<PAGE 6>>>）
- PSIRT 漏洞响应流程与第三方协作（C2，<<<PAGE 7>>>）
- 网络插孔直通防火墙内网（X8，<<<PAGE 8>>>）
- 未培训员工无意暴露（X9，<<<PAGE 8>>>）

## B（反例与坑）
- 公开漏洞即攻击武器，补丁拖延=开门揖盗（X7/P7，<<<PAGE 7>>>）
- 物理访问是安全边界：控制台直连可重置管理员口令、U-boot 可改系统参数（X2/X6/P9，<<<PAGE 9-11>>>）
- 单层防御不可靠，必须多层层深（P2，<<<PAGE 5>>>）
- 入门级交换机不满足 AI 系统需求（P83，<<<PAGE 91>>>）
- 网络保险与合规倒逼：视频监控系统须过网络安全标准（P89，<<<PAGE 99>>>）

来源：Network Security Guidelines（Intro/Secure By Design/Physical Security，p5-10）+ 白皮书（p91、99）
