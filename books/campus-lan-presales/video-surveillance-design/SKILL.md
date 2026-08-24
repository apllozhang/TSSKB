---
name: video-surveillance-design
description: 安防弱电项目用视频监控概念模板（前端/承载/后端/DMZ）+ Milestone 插件能力与支持机型清单出方案。
source_book: DT00XPS281EN Campus LAN Presales
---

# 视频监控网络方案（Milestone VMS + 插件）

## R · 原文引用

> "SURVEILLANCE NETWORK CONCEPTUAL DESIGN — IP CAMERAS / PAN TILT ZOOM CAMERAS / DETECTORS / EDGE STORAGE / 360 CAMERAS / AUDIO … SMART WALL / SMART CLIENT OPERATIONS / DMZ / FIREWALL / WEB CLIENT / USERS … MILESTONE VMS & PLUGINS — STORAGE / EVENT / NETWORK MANAGEMENT / SQL SERVERS — SPB" (p465)

> "Add an OmniSwitch to the Management client … Port – reset, power reset, LPS lock-unlock, PoE priority. Test camera status and reset if needed with one click. Set PoE priority on a per camera basis ensuring critical devices remain powered if the power budget is exceeded" (p463-464)

> "SWITCHES SUPPORTED — OS6360-P10/A, OS6360-P24 PH/X, OS6360-P48 PH/X, OS6465-P6 P12 H-P12, OS6465-P28, OS6465T-P12, OS6560-P24 X4/Z8/Z24, OS6560-P48 X4/Z16, OS6860E P24/P48/Z8, OS6860N P24/P48 Z/M, OS6865-P16X" (p466)

## I · 方法论骨架

**概念模板四段分层**（画图底稿）：

| 段 | 组成 |
|---|---|
| 前端 | IP/PTZ/360 摄像机、探测器、边缘存储、音频 |
| 承载 | 交换机接入 + SPB 分段隔离骨干 |
| 后端 | Milestone VMS：Management Client（管理）+ Smart Client（操作）+ Event/SQL/存储服务器 + Smart Wall 电视墙 |
| 边界 | DMZ + 防火墙，Web Client 远程访问 |

**插件双端能力**：
- Management Client（管理员侧）：交换机增删、端口信息查询、端口/电源复位、LPS 端口锁定、PoE 优先级。
- Smart Client（值班操作员侧）：端口表看摄像头上下线与 PoE 消耗、一键测试/复位摄像头、逐摄像头设 PoE 优先级（预算超限时保关键设备供电）、查交换机型号/版本/IP/位置/温度。
- 价值主张：交换机 + 摄像机管理一家集成，不在两套系统间切换——把网络从"哑管道"提升为 VMS 内可运维组件。

**支持机型清单（11 个 PoE 机型合规对照）**：OS6360-P10/A、P24/P48 PH/X；OS6465-P6/P12/H-P12/P28、6465T-P12；OS6560-P24 X4/Z8/Z24、P48 X4/Z16；OS6860E P24/P48/Z8；OS6860N P24/P48 Z/M；OS6865-P16X（坚固型）。方案由 ALE（交换机+插件软件）与 Milestone 两部分组成。

## A1 · 书中案例

c16（p465）完整概念设计图；c17（p463-464）插件功能实例；c18（p466）支持机型清单——三页合起来即一个可投标的安防网络分册骨架。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：接安防/弱电集成项目，需画监控网络图、选接入交换机、演示 VMS 内管交换机。
- 区分：本 skill 管**视频监控垂直方案**；通用准入安全（摄像头作为哑终端的画像治理）在 `security-unified-access`；骨干用 SPB 的机制设计在 `spb-vxlan-core-fabric`；PoE 预算常数在 `omniswitch-model-selection`。

## E · 可执行步骤

1. 盘前端：摄像机类型/数量/码率，估带宽与 PoE 预算。
2. 按支持机型清单选接入交换机（全部须为清单内 PoE 机型），核对 PoE 预算。
3. 按四段模板画图：前端→SPB 承载→Milestone 后端→DMZ 远程访问。
4. 配置逐摄像头 PoE 优先级策略，关键点位设高优先级。
5. 演示脚本：Smart Client 内一键复位摄像头 + 端口锁定，展示与竞品"两套系统"的差异。

## B · 边界与陷阱

- 教材视频监控章节较薄（p457-473）：无与 Genetec 等其他物理安防平台对接细节，ONVIF 相关口径书中未展开（g30 为待确认项），投标前以 ALE 视频监控方案页核实。
- 插件只支持清单内 11 个机型——选型越界即合规失败。
- 组播优化依托 SPB（IP Multicast Optimization），承载网设计须先满足 SPB 机型门槛。

---
来源条目: f29, c16, c17, c18, g21, g26, g30, g46
