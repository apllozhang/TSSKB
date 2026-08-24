---
name: OV2500 虚机部署与许可管理
description: 需要在 vSphere/Hyper-V/KVM 上全新部署 OmniVista 2500 虚拟机、做容量分档（Network Size）选型、或生成/安装 Evaluation/Production License 时使用。
source_book: DT00XTE311 OmniVista 2500 NMS Administration R4
---

## R（触发场景）
- 新建 OV2500 管理平台，需要从 OVF 模板部署 Virtual Appliance 并完成控制台初始化
- 不确定选 Low/Medium/High/Very High 哪个 Network Size，或带大量 Stellar AP 时交换机规模受限
- 需要申请、安装、更换 Evaluation 或 Production License

## I（核心理念）
OV2500 是纯虚拟机形态（Virtual Appliance = Linux OS + OV 应用打包在一起，无独立安装器），平台规模在安装时通过 Network Size 一次性锁定，系统按所选档位分配内存。License 分 Device License（Starter/Evaluation/Production）与 Service License（VM/Guest/On-Boarding/HA/Web Content Filtering）两条线，安装方式文件与密钥二选一。

## A1（行动框架）
1. **容量选型**：按设备数定档——Low <500 / Medium 500-2000 / High 2000-5000 / Very High 5000-10000 台；上限 10000 devices、4000 Stellar APs、5000 VMs（<<<PAGE 45/58/44>>>）
2. **部署 OVF**：vCenter → vSphere Client → File > Deploy OVF Template；Disk Formatting 选 Thick Provision（推荐）；部署完成后如未自动开机则手动 Power on（<<<PAGE 54>>>）
3. **控制台初始化**：Hypervisor Console 依次填——cliadmin 密码 → IP Settings（OV IP、HTTP/HTTPS 端口、Captive Portal IP/端口、Additional OV Web）→ Network Size → Hostname/DNS/NTP/Timezone/Routes → Exit & Reboot（<<<PAGE 56-60>>>）
4. **首登与改密**：浏览器访问 `https://<IP>`，首次登录强制修改默认密码（admin/switch），否则无法进入系统（<<<PAGE 61/101-102>>>）
5. **申请 EVAL License**：https://lds.al-enterprise.com/ → OmniVista 2500 NMS → Customer ID 99999 / Order Number "evaluation" → License Type EVAL-OV2500-ALL-TYPE_1 / Passcode omnivista → Generate License 保存文件（<<<PAGE 103-104>>>）
6. **安装 License**：Add License → Browse 上传文件，**或**手输 License Keys（二选一）；EULA 勾 OK、**不勾** Enable Fleet Supervision；装好后删除本地 EVAL 许可文件（<<<PAGE 104-105>>>）

## A2（进阶应用）
- HA 场景许可：自 4.3R1 起 "you don't have to double the licenses on the redundant system"；节点计数规则：VC 内每台物理设备占 1 个 license（"VC of 2 = 2 license units"）（<<<PAGE 50-51>>>）
- 带 4000 Stellar AP 时：High 档仅支持到 500 台 AOS 交换机，Very High 档到 1000 台——AP 多的无线重环境要升档（<<<PAGE 45>>>）
- 标称容量受环境变量影响（VLAN 数、客户端数、开放的应用数等），"Specific configurations may vary"（<<<PAGE 45>>>）

## E（实证案例）
- 部署 Virtual Appliance（vSphere OVF 全流程，Thick Provision 推荐）——cases·OVF 部署（<<<PAGE 54>>>）
- 安装序列：控制台初始化 → 重启 → 首登改密 → License 弹窗——cases·安装序列（<<<PAGE 56-60/61/101-102>>>）
- 生成并安装 Evaluation License 全流程——cases·EVAL 许可（<<<PAGE 103-105>>>）

## B（边界与陷阱）
- License 文件与 License Keys 不可同时安装："Don't do both!"（<<<PAGE 104>>>）
- 粘贴 Key 时只取逗号后的 key 部分，整行粘贴会把许可名带进去（<<<PAGE 104>>>）
- 接受 EULA 时不要勾 Enable Fleet Supervision，书中两次强调（<<<PAGE 104>>>）
- 装完许可务必删除本地 EVAL 文件，防止外泄（<<<PAGE 105>>>）
- 无可用快照时无法恢复 OV 初始配置（快照含 IP/网关/network size），只能联系培训师/支持（<<<PAGE 100>>>）

## 来源
- frameworks·Sizing 四档决策（<<<PAGE 45/58/44>>>）、VA 部署序列（<<<PAGE 55-60/54>>>）、License 类型决策（<<<PAGE 46-51>>>）
- principles·纯虚机形态（<<<PAGE 25/44>>>）
- cases·OVF 部署/安装序列/EVAL 许可（<<<PAGE 54/56-61/97/101-105>>>）
- counter-examples·许可二选一/粘贴反例/Fleet Supervision/快照缺失/容量骤降（<<<PAGE 100-105/45>>>）
