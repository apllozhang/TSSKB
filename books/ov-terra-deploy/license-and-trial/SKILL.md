---
name: License 与 Trial 转正
description: 当需要申请 Trial、eBuy 下单 License、Subscription Manager 创建订阅、或在 Cirrus/Terra 中导入订阅完成试用转正时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 新建组织没有 License，需要申请 Trial 试用期
- Trial 到期前需要转正式（paid mode）订阅
- eBuy 下单后 License 找不到，或需要导出/激活订阅

## I（核心理念）
License 链路是三段式：eBuy 下单 → Subscription Manager 建订阅 → OV 实例（Cirrus/Terra）导入。License SKU 编码自带等级/年限/品类信息。Terra 与 Cirrus 的导入差异在于 Terra 需额外下载 license 文件 (.json)。注意两个时间陷阱：eBuy 下单后订阅最长延迟 24 小时出现；勾选 "Activate subscription" 即开始订阅倒计时。

## A1（行动框架）
1. **申请 Trial**：建组织后点 "Request a trial period for this organization"（<<<PAGE 53>>>）；表单必填 ALE 销售/CSM/KAM 联系人，不知道则用通用值 "My-ALE-Contact / MyALEContact@al-enterprise.com"；Partner Name 与 CRD ID 从 eBuy 复制；预填的时长与设备数量无特殊原因不要改（<<<PAGE 54>>>）；审批通过后发起人收邮件通知，组织状态更新（<<<PAGE 55>>>）。Terra 组织则是自动激活 90 天 Trial（<<<PAGE 110>>>）。
2. **eBuy 下单**：https://ebuy.businesspartner.al-enterprise.com/（或 MyPortal: Other Quick Links > eBuy）→ 新建购物车选 "Other Services & Items Section" → 输入 license reference 与数量 → 填 Order Entry（PO、requested date）并 validate（<<<PAGE 25>>><<<PAGE 97>>>）。
   - SKU 编码：如 OVCX-68-BAS-3Y = 等级 BASE(BAS)/BUSINESS(BIZ)/PREMIUM(PRM) + 年限 1Y/3Y/5Y（Terra 另有 7Y）+ 品类（APL=低端 AP1x0x/1x1x/1x2x，或 APH/63/64/65/68/69/99）（<<<PAGE 23>>><<<PAGE 95>>>）
3. **Subscription Manager 建订阅**：MyPortal: Installed Base > eLicensing Management > OVC Subscription Manager → 选 offer → "Your purchased license" → Action "Create a subscription" → 选数量、填客户信息、同意条款 → 记录 Subscription reference；状态到 "Created / Pending activation from OVC UI" 后展开记录 Subscription 和 Order ID（<<<PAGE 26>>><<<PAGE 27>>><<<PAGE 28>>>）。
4. **Cirrus 导入（Trial 转正）**：License Management > import licenses > CAPEX Subscription → 输入 Subscription ID + Activation Code → 同意条款 → Import Subscription → 步骤2选自动/手动设备分配 → 步骤3 review + upgrade → Proceed 确认 paid mode → 验证 License mode / Duration / Type / 型号数量（<<<PAGE 62>>><<<PAGE 63>>><<<PAGE 64>>><<<PAGE 65>>><<<PAGE 66>>><<<PAGE 67>>>）。
5. **Terra 导入（多一步下载文件）**：Admin Center 右上角取 OmniVista ID → 在 Subscription Manager 选 "Download Licenses / Activate subscription"（同时下载 license 文件）→ 导入时输入 Subscription ID + Activation Code + License file (.json) → 同意条款 > Import > 选设备分配 > upgrade > Proceed → 验证同上（<<<PAGE 100>>><<<PAGE 101>>><<<PAGE 113>>><<<PAGE 114>>><<<PAGE 115>>><<<PAGE 116>>><<<PAGE 117>>>）。

## A2（进阶应用）
- Subscription Manager 支持续订、增购、延期、转移等订阅全生命周期管理（<<<PAGE 24>>><<<PAGE 26>>>）。
- Terra 场景利用自动 90 天 Trial 窗口完成部署验证，再导入正式订阅转 paid mode（<<<PAGE 110>>><<<PAGE 66>>>）。

## E（实证案例）
- **案例 1**：伙伴在 eBuy 下单后立刻到 Subscription Manager 建订阅，列表里空无一物——License 最长 24 小时后才出现，等待即可（<<<PAGE 26>>><<<PAGE 98>>>）。
- **案例 2**：Terra 管理员在导入前"顺手"勾了 Activate subscription，订阅期白白开始倒计时——应等真正上线再激活（<<<PAGE 101>>>）。

## B（边界与陷阱）
- **24 小时延迟**：eBuy 下单后订阅最长 24h 才出现在 Subscription Manager（<<<PAGE 26>>><<<PAGE 98>>>）。
- **激活即倒计时**：勾选 "Activate subscription" 立刻开始扣订阅期，不要提前激活（<<<PAGE 101>>>）。
- **Terra 别忘了 license 文件**：只有 ID+激活码不够，必须同时下载并导入 .json 文件（<<<PAGE 100>>><<<PAGE 114>>>）。

## 来源
- frameworks·组织创建与 Trial 试用期申请流程（<<<PAGE 51>>><<<PAGE 52>>><<<PAGE 53>>><<<PAGE 54>>><<<PAGE 55>>>）
- frameworks·Trial 转正（转订阅）流程（<<<PAGE 62>>>~<<<PAGE 67>>>）
- frameworks·License 订购→订阅生成→导入三段流程（<<<PAGE 24>>><<<PAGE 25>>><<<PAGE 26>>><<<PAGE 27>>><<<PAGE 28>>>）
- frameworks·Terra 侧 License 激活流程（<<<PAGE 100>>><<<PAGE 101>>><<<PAGE 114>>>）
- principles·License SKU 编码模型（<<<PAGE 23>>><<<PAGE 95>>>）
- principles·Terra 组织自动 90 天 Trial（<<<PAGE 110>>>）
- cases·Trial 申请表单填写（<<<PAGE 54>>>）
- cases·eBuy 下单 License（<<<PAGE 25>>><<<PAGE 97>>>）
- cases·Subscription Manager 创建订阅（<<<PAGE 26>>><<<PAGE 27>>><<<PAGE 28>>>）
- cases·Cirrus 导入订阅（<<<PAGE 62>>>~<<<PAGE 67>>>）
- cases·Terra License 下载与导入（<<<PAGE 101>>><<<PAGE 113>>><<<PAGE 114>>><<<PAGE 115>>><<<PAGE 116>>><<<PAGE 117>>>）
- counter-examples·eBuy 购买后订阅最长延迟 24 小时（<<<PAGE 26>>><<<PAGE 98>>>）
- counter-examples·Activate subscription 即开始倒计时（<<<PAGE 101>>>）
