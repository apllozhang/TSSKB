---
name: AOS 8 平台三梯队选型与规格解读法（Specifications Guide 导读）
description: 需要按 MAC/路由/聚合/接口规模为 OmniSwitch 选型或核对平台档位、理解 VC 规格的"整机上限"语义、或按文档地图找到正确的配置手册时使用。
source_book: OmniSwitch AOS Release 8 Specifications Guide (8.10R4)
---

## R（触发场景）
- 新建/扩容网络选 OmniSwitch 平台，要按规模定档（接入/汇聚/核心）
- 看规格表时不确定某个 maximum 是单机还是整 VC
- 只知道特性名，要找到该去哪本手册查配置
- 核对管理面资源（会话数/内存/Flash/USB 救援/镜像文件名）

## I（核心理念）
平台规模三梯队选型框架（F2，<<<PAGE 30>>>/<<<PAGE 42>>>）：接入级（6360/6465/6560：MAC 16K、路由 32-2K、聚合 32 组）→ 汇聚级（6570M/6575/6860 系：MAC 32-64K、路由 12-13K、聚合 128）→ 核心/数据中心级（6870/6900/6920/9900：MAC 104-228K、路由 113-384K、聚合 252+）；同级内再看 SM/RM/ER 转发 profile 二次放大。规划口诀：先选梯队、再选 profile、最后对 TCAM 档位。VC 规格解读框架（F4，<<<PAGE 12>>>/<<<PAGE 23-24>>>）：文档中的 maximum 默认作用于整 VC 而非单机（P13），三类例外要辨明——按机箱×成员数扩的、VC 封顶不随成员增加的（X35）、仅单机的（1588v2 VC-of-1）。文档地图四阶段法（F1，<<<PAGE 8-9>>>）：本手册只答"能到多少"不答"怎么配"，配置去 Network Config / Advanced Routing / Data Center Switching，命令查 CLI Reference。

## A1（决策框架）
1. **先定梯队**：按 MAC 表/路由表/聚合组三指标对号三梯队（F2）
2. **再定 profile**：SM/RM/ER 三态放大转发规模（如 6900-X RM 312K IPv4 路由、ER 更大 MAC 需重启生效）
3. **VC 场景辨语义**：默认整 VC 上限；UNP 用户看平台脚注 1（×成员数）或脚注 2（VC 封顶）；6900 VC 的 ARP=最低能力模块的值（X6，<<<PAGE 42>>>）
4. **混搭先查白名单**：6900 系内（V72/C32(E)/X48C6/T48C6/V48C8/X24C2/T24C2，最多 6；X48C4E 需 mixed VFL 模式）、6860+6865、6465 系内（用 1G SFP）、6360 10 口型仅 4 成员；**6860N 与 686x 禁止混 VC**（X2，<<<PAGE 24>>>）
5. **管理面核对**：Telnet 6 / SSH 8 / HTTP 4 全平台一致（P2）；内存/Flash 按 P4 矩阵

## A2（操作步骤）
- **镜像与救援文件名核对**（P1/P5，<<<PAGE 14>>>/<<<PAGE 17>>>）：6360=Nosa.img、6465/6560=Nos.img、6570M=Wos.img、6575=Dos.img、6860/6865=Uos.img、6860N=Uosn.img、6870=Kaos.img、6900=Yos.img、6920=Ypos.img、9900=Mhost.img+Mos.img+Meni.img；USB 救援用对应 rescue 镜像，ALE 认证 U 盘 FAT32、目录名小写
- **VC 成员数核对**（P11，<<<PAGE 23>>>）：6360 24/48 口=8（10 口=4）、6465=4、6560/6570M/6860/6865/6870=8、6575=4、6900-X=6、9907=2、9912/6920 不支持
- **VFL 规格核对**（P12，<<<PAGE 23>>>）：多数平台每机箱 2 peer、每 VFL 8 成员口、VFL id 0-1；6900 每 5 peer、16 成员口、VFL id 0-4
- **帧长核对**（P14，<<<PAGE 29>>>）：10/100M 口 1553 字节、1G+ 口 9216 字节
- **路由软超载预判**（P16，<<<PAGE 43>>>）：硬件路由超限时旧的不常用路由移入软件、活跃路由保硬件，超出即部分流量走软件路由
- **聚合规模梯度**（P17，<<<PAGE 35-36>>>）：6360/6465/6560=32 组×8 口；6570M 静态 32/LACP 96；6860 系=128×16；6870=252 组；6920=253 组×16；9900 ID 0/126/127 保留不可用（X48）

## E（实证案例）
- 本书为纯规格手册，无配置流程案例（原书自述 "designed to provide feature specification information only"）；"场景"即选型核对：按 F1 文档地图定位到对应配置手册后再动手配置

## B（反例/坑）
- 6920 与 OS9912 机箱完全不支持 VC；OS9907 仅 VC-of-2 且依赖 CMM/CFM 组合（X1，<<<PAGE 23-24>>>）
- OS6860N 与 OS686x 禁止混 VC（X2，<<<PAGE 24>>>）
- MAC Learning Mode 在 OS6900 VC 上不支持（X3，<<<PAGE 24>>>）
- VFL 在 4X25G splitter 口上必须两侧 inter-frame gap=13，否则 CRC（X4，<<<PAGE 24>>>）
- 1588v2 只支持 VC-of-1；6570M/6860/6865/6870 不支持 10/100 半双工（X5，<<<PAGE 29>>>）
- 作运行目录时文件/目录名上限 30 字符（普通场景 255）（glossary，<<<PAGE 15>>>）
- RCD 限制：ISSU 与 IPv6 不支持；uboot/miniboot/FPGA 升级不支持；FTP/SFTP 用户名 15 字符（X42，<<<PAGE 25>>>）
- OpenFlow 仅 6860 支持：Normal/Hybrid 模式、1.0/1.3.1、每逻辑交换机 3 控制器（最多 3 个、Hybrid 1）（P9，<<<PAGE 22>>>）

## 来源
OmniSwitch AOS Release 8 Specifications Guide 前言（<<<PAGE 7-11>>>）、Ch1 Switch Management（<<<PAGE 12-26>>>）、Ch2 平台规模部分（<<<PAGE 27-46>>>）。条目来源：principles P1/P2/P4/P5/P9/P11-P17；counter-examples X1-X6/X42/X48；frameworks F1/F2/F4。
