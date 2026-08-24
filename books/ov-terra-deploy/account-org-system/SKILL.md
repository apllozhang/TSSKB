---
name: 账号与组织体系
description: 当需要创建 Cirrus 账号（Partner/Customer）、创建组织、配置用户权限，或管理组织在 MSP 间的迁移/脱离时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 首次接入 Cirrus，需要注册账号并创建组织
- 需要给客户或团队成员分配 Admin/Viewer/Limited 权限（单个或批量邀请）
- 组织需要更换 MSP 或脱离当前 MSP

## I（核心理念）
Cirrus 是三级账号体系：Partner 账号创建后即为 MSP 级用户，可创建/配置组织并邀请用户；Customer 账号挂接组织但不关联 MSP；组织是管理租户单元（一家企业或实体，含多个站点）。一个邮箱在 OVC 10.4.3 中只能绑定一个 MSP 门户，多 MSP 访问要用子地址技巧。

## A1（行动框架）
1. **创建账号（选区域 URL）**：
   - 访问 https://eu.manage.ovcirrus.com/ 或 https://us.manage.ovcirrus.com/，选 Americas / Asia Pacific / EMEA
   - 填 First/Last Name、E-mail、Country，创建 Customer 或 Partner 账号（<<<PAGE 33>>><<<PAGE 34>>><<<PAGE 35>>>）
2. **密码与激活**：按安全要求定义密码（可自动生成强密码），创建后经激活邮件激活（<<<PAGE 38>>><<<PAGE 40>>>）。
3. **Partner 账号 MSP 关联三选一**：不挂 MSP / 加入既有 MSP / 自建 MSP（<<<PAGE 39>>>）。
4. **Customer 账号两种交付**：邀请 Partner 邮箱访问组织，或直接创建客户凭据（开箱即用账号）（<<<PAGE 43>>><<<PAGE 45>>>）。
5. **创建组织**："Click here to create your organization"，填 Organization Name、Security Policy（推荐强密码）、Country and timezone（<<<PAGE 51>>><<<PAGE 52>>>）。
6. **邀请用户**：组织级用户权限可 Globally 或 Per organization 设置（Admin/Viewer/Limited），支持批量邀请用户列表（<<<PAGE 131>>><<<PAGE 132>>><<<PAGE 133>>><<<PAGE 134>>><<<PAGE 135>>>）。
7. **组织迁移 MSP**：Actions > Change MSP，输入目标 MSP 管理员邮箱（<<<PAGE 60>>>）。

## A2（进阶应用）
- MSP 级用户权限同样是 Admin/Viewer/Limited 三档（<<<PAGE 50>>>）。
- 多 MSP 访问用子地址：MyMail+sub@MyCompany.com；注意激活链接仍发到原始邮箱（<<<PAGE 49>>>）。

## E（实证案例）
- **案例 1**：某伙伴同时服务两个客户 MSP，用同一邮箱注册第二个门户被拒——OVC 10.4.3 一个邮箱只能绑一个 MSP 门户，改用子地址 MyMail+sub@MyCompany.com 解决（<<<PAGE 49>>>）。
- **案例 2**：客户组织从伙伴 MSP 脱离（Actions > Disassociate）后，该 MSP 内所有用户立即失去对组织的访问（<<<PAGE 59>>>）。

## B（边界与陷阱）
- **单邮箱单 MSP**：需多 MSP 访问必须用不同邮箱或子地址（<<<PAGE 49>>>）。
- **脱离 MSP 不可逆的访问损失**：MSP 内所有用户立即失去访问，操作前必须确认（<<<PAGE 59>>>）。

## 来源
- frameworks·三级账号体系 Partner/MSP/Customer（<<<PAGE 50>>>）
- frameworks·Partner 账号 MSP 挂接三选项（<<<PAGE 39>>>）
- frameworks·Customer 账号两种交付方式（<<<PAGE 43>>><<<PAGE 45>>>）
- frameworks·组织在 MSP 间迁移与脱离（<<<PAGE 59>>><<<PAGE 60>>>）
- cases·Cirrus 账号创建（<<<PAGE 33>>><<<PAGE 34>>><<<PAGE 35>>>）
- cases·邀请组织级用户（<<<PAGE 131>>><<<PAGE 132>>><<<PAGE 133>>><<<PAGE 134>>><<<PAGE 135>>>）
- counter-examples·一个邮箱只能绑定一个 MSP 门户（<<<PAGE 49>>>）
- counter-examples·组织脱离 MSP 后 MSP 用户立即失去访问（<<<PAGE 59>>>）
- principles·MSP 级用户三种权限（<<<PAGE 50>>><<<PAGE 130>>>）
