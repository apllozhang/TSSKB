---
name: rlab-lab-manual
description: 何时用：连接/重置 ALE Stellar 远程实验室（R-Lab）做本书实验，或把 15 个 Lab 当案例库检索对应实操流程。
source_book: DT00XTE360EN ACFE WLAN Basic Deployment
---

# R-Lab 实操手册与 Lab 案例库索引

## R · 原文引用

> "A web browser is required to connect to the Rlab ... Rlab access URL: https://rdp.al-mydemo.com/ ... Username: Refer to the table below to get the corresponding 'User Account' ... Password: unique per session - sent from our LMS to the Instructor" (p69)

> "Reset all the R-Lab's equipment by using the Reset_PodX script (X = R-Lab Number) ... The reinitialization process takes around 5 minutes (OmniSwitch) ... around 1min30 - 2min (OmniAccess Stellar Access Point)" (p77)

> "WARNING: THE OMNISWITCH SWITCHES DEFAULT CONFIGURATION IS NOT AN EMPTY CONFIGURATION! ... A SPECIFIC CONFIGURATION IS APPLIED TO THE SWITCHES; ALL THE INTERFACES ARE DISABLED. DURING THE NEXT LABS, IT WILL BE ASKED TO ENABLE THE INTERFACES THAT YOU WILL USE." (p80)

> "Never touch the Ethernet card (configuration or disconnection), because it is from the wired network that you can join the raspberry pi desktop." (p75)

## I · 方法论骨架

**1. 环境连接**
- 入口：https://rdp.al-mydemo.com/，账号形如 stellanpod25a（POD 25-32），密码每期由 LMS 发讲师
- 拓扑三层：接入 OS-2360/OS-6360（学员配置）→ 汇聚 OS-6870（保留预配置）→ 核心 OS-6900（不管理）；DHCP/AAA 服务器与 pfSense NAT 禁止改动
- 终端：桌面快捷方式 TeraTerm 开交换机控制台（"Hunting Group Busy"=被占用）；RealVNC 连树莓派 WifiClientX（user/superuser），实验前 "Clean Wireless Networks"；vSphere 开 client5 有线 VM

**2. 重置流程与常数**
- 桌面 DT00CTE210 目录双击 Reset_PodX（Cirrus 系列实验前另有 "OmniVista CIRRUS 10" 目录的 reset_PODX）
- 交换机约 5 分钟、AP 约 1.5-2 分钟；期间严禁对控制台按键
- 重置后"默认配置"非空：脚本灌特定预配置且**所有端口禁用**，每个 Lab 逐个 enable 要用的端口
- 树莓派重置：Clean Wireless Networks → Execute

**3. 实验网 IP/DHCP 常数（全部 Lab 的判定基准）**
VLAN10 管理 192.168.10.70-79 / VLAN20 Employees 192.168.20.70-79 / VLAN30 Guests 192.168.30.70-79；网关 6870 上 .7；DHCP/NAT 服务器 192.168.100.102 与核心 OS6900 不许改。

**4. Lab → skill 案例库索引**

| Lab | 页 | 内容 | 详细所在 skill |
|---|---|---|---|
| c03/c04 设备启动/PoE-VLAN-DHCP | p108-129 | 控制台+向导+端口 | express-mode-bootstrap |
| c05/c06/c07 Express SSID/内置 DHCP/日志 | p144-160 | SMB 无网管开局 | ssid-authentication-suite |
| c08 isc-dhcp option 138 | p33 | DHCP 样例 | express-mode-bootstrap |
| c09 许可订阅全流程 | p169-238 | eBuy→导入 | cirrus-license-org-lifecycle |
| c10 Cirrus 预配置重置 | p238-240 | 本 skill | — |
| c11 环境创建+交换机上云 | p241-253 | Site/激活 | device-cloud-onboarding |
| c12 AP 上云+Group | p293-306 | 声明/Provisioning | device-cloud-onboarding |
| c13 Employee SSID(802.1X) | p332-347 | 全链+排障 | ssid-authentication-suite |
| c14 PSK 四方案 | p324-330 | 逐屏样例 | ssid-authentication-suite |
| c15 Guest SSID+踢下线 | p372-388 | 门户+eag | ssid-authentication-suite |
| c16 BYOD SSID | p389-395 | 双 VLAN 切换 | ssid-authentication-suite |
| c17 Unified Policy | p411-416 | Block_SSH | upam-policy-bandwidth |
| c18 RF 管理 | p456-466 | RSSI 阈值实验 | rf-optimization-baseline |
| c19 WIPS | p521-525 | 分类+Friendly | wips-security-deployment |
| c20 组织清理 25 步 | p542-547 | 逆序拆除 | cirrus-license-org-lifecycle |
| c21 RAP 部署 | p549-572 | 双隧道全流程 | roaming-rap-design |
| c22 勘测方法论 | p526-540 | 三步法 | site-survey-troubleshooting |
| c23 账号与配额 | p417-434 | 配额触发 | upam-policy-bandwidth |

## A1 · 书中案例（Lab 步骤精要）
- **c01/p69-75**：浏览器连 RDP → POD 账号登录 → 认识拓扑与 TeraTerm/VNC/vSphere 三类入口。
- **c02/p77-80**：Reset_PodX 重置全设备（等待常数）→ 树莓派清网络 → 后续 Lab 逐口 enable。
- **c10/p238-240**：reset_PODX 后连通性验证——三台交换机 ping 192.168.100.102 与 www.google.com；AP1301 控制台 `ssudo ping` 同验；AP1321 此时 ping 不通属预期。

## A2 · 触发场景（含与相邻 skill 的区分）
- 要实际操练本书内容、连接或重置 R-Lab、或查找"某个 Lab 在书里哪几页/归哪个 skill"时用。
- **区分**：各 Lab 的技术内容本身已在对应业务 skill 的 A1 节精要化；本 skill 只管实验环境操作与索引。

## E · 可执行步骤
1. 拿到 POD 号与会话密码 → rdp.al-mydemo.com 登录。
2. 按实验阶段选对重置脚本（DT00CTE210 的 Reset_PodX / OmniVista CIRRUS 10 的 reset_PODX），跑完等足时长。
3. 重置后逐个启用要用的端口（1/1/6 AP 口、1/1/1 客户端口等）。
4. 树莓派 Clean Wireless Networks，保留以太网卡不动。
5. 实验判定一律对照 VLAN10/20/30 的 .70-.79 地址池。
6. 需要某 Lab 详细步骤时按索引表跳转对应 skill 的 A1 节。

## B · 边界与陷阱
- 重置脚本加载的默认配置非空且端口全禁——"设备不通"先查端口是否启用（ce09）。
- 重启阶段对控制台按一次回车就落 Miniboot，中断整个重置（ce10）。
- 不要对 R-Lab 交换机执行真恢复出厂（rm vcboot.cfg + reload）——会破坏 POD 专用预配置，后续实验全挂（ce11）。
- 树莓派以太网卡是 VNC 生命线，只动 wlan 接口（ce12）。
- 本书强依赖 R-Lab，无实验环境时 Lab 章节只能读；OV2500 本地管理 GUI 不在本书范围，与售前课（DT00XPS288）概念重叠但视角不同——引用时注意区分（ce40）。

---
来源条目: c01, c02, c10, p17, ce09, ce10, ce11, ce12, ce40 · 术语锚点: g51
