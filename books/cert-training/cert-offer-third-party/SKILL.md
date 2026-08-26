---
name: 第三方与转售认证路径（Celona 5G/Versa SD-WAN/HPE Aruba/Nokia POL-IP-OPTICS 与 ALE 互认）
description: 需要处理 ALE 生态第三方产品培训与认证时使用：Celona Private 5G、Versa SD-WAN、HPE Aruba 转售后的认证替代、Nokia POL/OPTICS EPON/IP Networks 培训入口及 Nokia↔ALE 认证映射与互认申请流程。
source_book: Training offer for Network, Cloud and Industries (June 2026)（p10-11、p17-18、p28-31、p51-67）
---

## R（触发场景）
- 合作伙伴要销售/实施 Celona Private 5G、Versa SD-WAN、Nokia POL/IP/OPTICS 等 ALE 转售产品
- 2025 年 2 月起 Aruba 转售调整后，原 Aruba 培训需求如何满足、证书如何被 ALE 认可
- 持有 Nokia 证书的工程师想把证书映射为 ALE 认证以满足专业化资质
- 确认第三方培训的准入前提（协议签署）与费用

## I（核心理念）
四家第三方各有通道：Celona 与 Versa 培训完全托管在对方门户（需签 Celona Addendum / Versa Resell Agreement），ALE 侧只提供入门 WSA/WPS 课；Aruba 自 2025-02-01 起整体转回 HPE Aruba 教育服务，其指定认证被 ALE 认可用于支持工单路由；Nokia 的 POL/OPTICS EPON/IP Networks 由 Nokia Learning Store 直接培训认证，证书按等级映射为 ALE 的 ACSR/ACPS/ACFE/ACSE 并在 360PartnerExperience 中可验证 Nokia 专业化（P63）。互认需填表 + 证书副本邮件申请（P67）。

## A1（决策要点）
1. **先查准入协议**：Celona 要签 Addendum、Versa 要签 Resell Agreement、Nokia 要接受 NIRA，否则进不了对方培训门户（P10/P11/P55）
2. **ALE 侧入门课先行**：Private 5G（DT00WSA037）、Versa SD-WAN（DT00WSA038/WPS295）、HPOL（DT00WSA026）都在 Knowledge Hub 提供，免费
3. **Aruba 场景**：走 HPE Aruba 官方认证（ACP/ACX Campus Access、ClearPass、Airwave 管理课），2025-02 后取得的证书 ALE 认可（P30）
4. **Nokia 证书互认**：按 P64-66 三张映射表对号，再按 P67 流程提交申请

## A2（细节速查）
### 第三方培训入口一览
| 厂商 | ALE 侧课程 | 对方门户 | 准入条件 | 页码 |
|---|---|---|---|---|
| Celona Private 5G | DT00WSA037（I 58min/46min） | partners.celona.io/training-certification | 签 Celona Addendum；FREE、MCQ | P10/P17/P28 |
| Versa SD-WAN | DT00WSA038（Sales 36min）、DT00WPS295（Presales 36min） | academy.versa-networks.com | 签 Versa Resell Agreement | P11/P18 |
| Versa 售后路径 | —（全在 Versa Academy） | Versa Essentials→SD-WAN Basics/Policy→VNX100 认证 | Individual Learning 免费，讲师引导收费 | P29 |
| HPE Aruba | 无 ALE 课程 | HPE Aruba Education Services / ATC | 2025-02-01 起调整 | P30 |
| Nokia（HPOL 除外） | 仅 HPOL 见 cert-offer-network | Nokia Learning Store | 接受 NIRA + 建账号 | P55 |

### HPE Aruba 认可认证（P30-31）
| 认证 | 方向 |
|---|---|
| ACP Campus Access | 校园接入（Professional 级） |
| ACX Campus Access Mobility | 校园接入移动性（Expert 级） |
| ACP Network Security (ClearPass) | 网络安全 |
| ACX Network Security (ClearPass) | 网络安全（Expert 级） |
| Airwave 管理平台课程 | 网管 |

### Nokia→ALE 认证映射（P64-66）
| Nokia 证书（GPP 编号系） | ALE 对应认证 | 页码 |
|---|---|---|
| POL Sales Specialist（GPP31341K/31361K） | ACSR POL | P64 |
| POL Sales Engineer Specialist（GPP32341K/32361K） | ACPS POL | P64 |
| POL Field Technician / Technical Support L1（GPP3334xK/3336xK） | ACFE POL | P64 |
| POL Network Integration / Technical Support L2（GPP33342K/33364K 等） | ACSE POL | P64 |
| IP Sales Specialist（GPP10010K） | ACSR IP Network | P65 |
| IP Sales Engineer Specialist（GPP10011K） | ACPS IP Network | P65 |
| IP Field Technician / Technical Support L1（GPP13505K/10017K/10018K） | ACFE IP Network | P65 |
| IP Network Integration Specialist / Tech Support L2（GPP10023K/13511K/10019K/10020K）；SRC/NRS II 亦可认 ACSE | ACSE IP Network | P65 |
| OPTICS EPON Sales→Integration 全序列（GPPA13xxK） | ACSR/ACPS/ACFE/ACSE OPTICS EPON | P66 |

### Nokia 专业化（Networking+Nokia）认证要求（P63）
| 级别 | Postsales | Presales | Sales |
|---|---|---|---|
| Basic | 1 ACFE HPOL（DT00CTE/VTE342）或 ACFE POL/OPTICS EPON/IP Network | 1 ACPS HPOL（DT00WCE208）或 ACPS POL/OPTICS EPON/IP Network | 1 ACSR HPOL（DT00WSA026）或 ACSR POL/OPTICS EPON/IP Network |
| Upper | 1 ACFE HPOL 或 ACSE POL/OPTICS EPON/IP Network | 同 Basic | 2 ACSR（同源） |

### 互认申请流程（P67）
1. 填写指定表单；2. 准备 Nokia 官方证书副本；3. 发送至 Training.services@al-enterprise.com

### Nokia 侧下单注意（P54）
- Individual Learning 模块在 Nokia Learning Store 免费，可自注册
- 面授/虚拟讲师课收费，收到采购订单后注册；报价联系四大区域 education-services 邮箱
- HPOL 培训在 ALE Knowledge Hub，按普通 ALE 课程报名

## E（场景案例）
- 伙伴要交付 Hybrid POL：ALE 侧完成 DT00WSA026/DT00WPS301/DT00CTE342 取 ACSR+ACPS+ACFE；再按建议补 Nokia POL Field Technician（P32/P58）
- 已持 Nokia IP Network Integration Specialist（GPP10023K）的工程师：按 P65 映射为 ACSE IP Network，走 P67 流程提交即可满足 Nokia 专业化上门框
- 伙伴原来靠 Aruba 证书提供 WLAN 支持：2025-02 后改考 HPE Aruba ACP Campus Access，ALE 认可用于 Welcome Center 工单路由（P30）
- 销售 Private 5G：先在 Knowledge Hub 看 DT00WSA037（58 分钟），进阶内容到 Celona 门户学 Sales Freq（P10）

## B（限制与注意）
- Celona/Versa 的培训排期、报名、费用全由对方管理，ALE 文档不保证其内容时效（P10/P11）
- Versa 售后内容 Individual Learning 免费，需要讲师引导则向 Versa Academy 付费（P29）
- Aruba 认可仅限 2025 年 2 月 1 日之后在 HPE Aruba 取得的证书（P30）
- VSR 不在 Nokia 伙伴计划内，其部署课程偏技术、未必适合销售（P62）
- Nokia 互认表格必须附官方证书副本，否则不被受理（P67）

来源：Training offer for Network, Cloud and Industries（P10-11、P17-18、P28-31、P51-67）
