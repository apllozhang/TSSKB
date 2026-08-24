# 反例提取 · Campus LAN Presales Ed29（失败模式 / 警告 / 局限 / 陷阱）

> 来源：DT00XPS281EN Edition 29（480 页）。每条含页码、原文引用（≤100 英文词）、踩坑场景与规避方法。

```yaml
- id: ce01
  title: VC 脑裂（Split Chassis）：VFL 断链导致 MAC/IP 双主，必须预部署 RCD 或 VCSP 保护
  type: counter-example
  source_chapter: "p71-74, p76-77"
  source_quote: |
    "Failures on VFL links cause potential MAC/IP duplication. 2 mechanisms: Out of Band: EMP Remote Chassis Detection (RCD); In Band: VC Split Protocol. ... Other Sub-VC goes into Protection mode automatically, shuts off all user ports (LAG and VFL ports are up)."
  summary: |
    场景：虚拟机箱（VC）的 VFL 堆叠链路全部断开（光纤被挖断、误拔线），两台成员交换机各自认为自己是 Master。
    后果：同一 MAC/IP 在两处重复出现，造成 IP 冲突、流量黑洞和网络震荡；这是 VC 方案最大的单点风险。
    避开：方案设计时必须二选一预部署保护机制——(1) 带外：管理网（EMP 口）上跑 RCD 协议，交换机重启并关闭所有业务口；(2) 带内：VCSP（VC Split Protocol），借助上/下游 helper 交换机的 LAG 检测分裂，非 Master 子 VC 进入 Protection 模式、关闭全部用户端口（仅保留 LAG 和 VFL 口）。建议每个 VC 成员都有一条链路加入通往 helper 交换机的 VCSP LAG。另外 OS9900 的 chassis-id 必须静态配置（vcsetup.cfg，强制），混 EMP/非 EMP 机型组 VC 要指定专门管理 VLAN。
  tags: [vc, split-chassis, rcd, vcsp, risk, resilience]

- id: ce02
  title: 无 EMP 端口机型做 RCD 防脑裂，必须自购 USB 转以太网适配器
  type: counter-example
  source_chapter: "p72, p77"
  source_quote: |
    "On OS6360/OS6560/E, EMP port must be added through USB to Ethernet adapter to support RCD. ... On models without EMP port, you must add a dedicated USB to Ethernet converter, supported models are ASIX 8817 interface and RealTek RTL8153."
  summary: |
    场景：用 OS6360、OS6560/E 等没有 EMP 管理口的机型组 VC，且只部署了带外 RCD 防脑裂（没部署 VCSP）。
    后果：RCD 协议没有承载通道，脑裂检测形同虚设，VFL 断链时双主风险裸奔。
    避开：BOM 里给每台无 EMP 机型加一个 USB 转 Ethernet 适配器，且只支持两个型号：ASIX 8817 和 RealTek RTL8153——买错型号 RCD 不工作。或者改用带内 VCSP 方案绕开 EMP 依赖。这是售前报价时最容易漏配的小物件。
  tags: [vc, rcd, emp, bom, hardware]

- id: ce03
  title: DHL 双归属环路风险：上联误接非核心设备会成环，接入侧必须配防环三件套
  type: counter-example
  source_chapter: "p56"
  source_quote: |
    "Link between uplink device other than core network is not advisable as it will create loop. Solution on Access switches: LPS, Loop Guard, BPDU Shutdown."
  summary: |
    场景：DHL（双归属激活/激活）只在"接入交换机→核心"这条路径上改 VLAN 转发状态防环；如果现场把两台接入交换机的 DHL 上联口之间又互连了一段（或上联到核心以外的设备），DHL 的防环逻辑不覆盖这段链路。
    后果：二层环路，广播风暴打瘫全网。
    避开：接入交换机上强制开启防环三件套——LPS（Learned Port Security）、Loop Guard、BPDU Shutdown；施工规范里禁止把 DHL 链路接到核心以外的设备。另外注意 DHL 只管理接入交换机、每台交换机只允许一个 DHL session（p54-55），别拿它做核心间互联。
  tags: [dhl, loop, lps, loop-guard, bpdu-shutdown, access]

- id: ce04
  title: DHL 机型支持范围：教材自相矛盾——p54 称"除 9900 全支持"，p301 矩阵 6900/9900 均标 No
  type: counter-example
  source_chapter: "p54, p301"
  source_quote: |
    "Available on all OmniSwitch models, except OmniSwitch 9900. (p54) ... DHL Active-Active: ... OS6900 No, OS9900 No. (p301 matrix)"
  summary: |
    场景：售前按 p54 的说法给客户承诺"全系列都支持 DHL 双活"，选型时用了 OS6900 做双归属接入或 OS6570M 做 DHL。
    后果：p301 机型矩阵里 DHL Active-Active 一行 OS6900、OS9900 均为 No（6570M 一列也无 Yes 标记），到货后发现特性不可用，方案返工。
    避开：DHL 卖点只在接入/汇聚层兑现（6360/6465/6560/6860N/6870 等），核心层（6900/9900）改用 LAG/VC/SPB 做冗余。教材 p54 的"除 9900 外全支持"与 p301 矩阵冲突，投标前必须以机型矩阵 + 最新 release notes 复核。
  tags: [dhl, model-matrix, contradiction, presales]

- id: ce05
  title: VFL 堆叠链路硬限制：速率不能混跑、6860N 与 6870 不能混插 VC、6860N 100G VFL 必须用暗光纤
  type: counter-example
  source_chapter: "p60-61, p70"
  source_quote: |
    "VFL trunk are comprised of up to 16 member ports according to the model. VFL link speeds MAY not be mixed. ... No mix between 6860N and 6870. ... You must use a 'dark fiber' as multiple wavelengths are used for 100G connectivity."
  summary: |
    场景：三个常见踩坑——(1) 同一条 VFL trunk 里混用 10G 和 25G/40G/100G 成员口；(2) 远程堆叠想省钱，把 OS6860N 和 OS6870 混在一个 VC 里；(3) OS6860N 两台楼间 100G 远程堆叠直接租了波分/单波长专线。
    后果：(1) VFL 不成立或带宽异常；(2) VC 无法组建（两者虽同代但协议/硬件族不兼容；可混的是 6860/6860E/6865）；(3) 100G 用多波长传输，走波分设备会不通。
    避开：VFL trunk 内所有成员口同速率；跨楼远程堆叠按家族选型（6860N×N 或 6870×N，不跨族）；6860N 的 QSFP28 VFL 100G 远程互联必须用暗光纤（dark fiber），并查 transceiver guide 选对模块。另注意各机型 VC 台数上限：6465/6575 最多 4 台、6900 最多 6 台、9907 最多 2 台（p59）。
  tags: [vc, vfl, remote-stacking, dark-fiber, limitation]

- id: ce06
  title: auto-fabric 从 8.10R2 起改为 opt-in：新出厂默认不再自动组网，老版本默认开启曾致误组网
  type: counter-example
  source_chapter: "p36, p137, p140"
  source_quote: |
    "Prompt to disable auto-fabric during the boot sequence giving user 10s to decide. Auto-VC, RCL and auto-fabric are enabled (input Y default). Starting with 8.10R2 auto-fabric is opt-in !!"
  summary: |
    场景：(1) 8.10R2 之前的版本，交换机开箱首次启动默认启用 Auto-VC/auto-fabric，boot 过程只给 10 秒按 Y/N 的窗口——新设备插进现网，可能自动和邻居建 VC、自动起 SPB 织构；(2) 8.10R2 起默认关闭（opt-in），工程师按老习惯以为开箱即自动组网，结果 VC 一直建不起来。
    后果：老版本误组网造成配置漂移、意外 VC 合并；新版本按旧文档施工则自动化不生效、开通延迟。
    避开：按版本区分施工手册——8.10R2 前注意 boot 10 秒提示窗口（插电前想清楚）；8.10R2 起需显式启用 auto-fabric。另注意 auto-VFL 会征用特定端口：6900 是"每台最后 5 个端口（含扩展槽，无论有没有插模块）"，6560 是 24 口型的 29/30、48 口型的 53/54，6360 是 11/12、27/28 或 51/52——这些端口若已被规划为业务上联会冲突。
  tags: [auto-fabric, ifab, auto-vc, vfl-ports, release-behavior]

- id: ce07
  title: SPB 收敛约 300ms：达不到电信级 50ms，时敏场景要靠 ERPv2，且 50ms 本身有前提条件
  type: counter-example
  source_chapter: "p85, p103, p122, p125"
  source_quote: |
    "100's ms convergence times. (p85) Fast reconvergence (~300ms). (p103) ... enables 50 ms convergence time upon a link or node failure. (p122) ... with less than 1200 km of ring fiber circumference, and fewer than 16 Ethernet Ring Nodes, the switch completion time ... shall be less than 50 ms. (G.8032 quote, p125)"
  summary: |
    场景：客户招标书里写"故障倒换 ≤50ms"（电力、轨道交通、运营商级 SLA），售前拿 SPB 的"快收敛"去应标。
    后果：SPB 实测收敛量级约 300ms（书里两处自述：p85 "100's ms"、p103 "~300ms"），达不到 50ms，测试验收不过。
    避开：50ms 级保护用 ERPv2（G.8032 环网）兑现，但要同时满足书里引用的前提：环周长 <1200km、环上节点 <16（推荐值）、无拥塞、节点处于 idle 态；环规模设计还要守住 4094 个受保护 VLAN、单机最多 64 个 ERP 环（p122/p128）。园区大网用 SPB 换带宽利用率和可扩展性（1000 节点），时敏链路局部叠 ERP，两者不矛盾。
  tags: [spb, erp, convergence, sla, limitation]

- id: ce08
  title: 机型功能矩阵的 No 项：SPB/MPLS/ISSU/VC/用户接入按机型裁剪，选型照表不照宣传
  type: counter-example
  source_chapter: "p300-301"
  source_quote: |
    "MPLS: ... OS6860N Yes**, OS6870 Yes**, OS6900 Yes**, OS9900 No. ... SPB: OS2260 No, OS2360 No, OS6360 No, OS6465 No, OS6560/E Yes**, OS6570M Yes** ... ISSU: OS2260 No, OS2360 No, OS6465 No, OS6560/E No ... User Access: OS6900 No. (matrix excerpts)"
  summary: |
    场景：凭产品线宣传"全家族支持 XX"去做选型，典型错误：给低端接入（6360/6465）承诺 SPB；给 2260/2360/6465/6560 承诺 ISSU 不中断升级；把 OS6900 放到用户接入层；给 OS2260 上堆叠。
    后果：p301 矩阵明确这些组合是 No——到货装不了或特性缺失，投标技术偏离。
    避开：所有选型先过 p300（层级定位表：6360/6465 不能做汇聚/核心，6560/6570M 不能做核心，6900 不做用户接入）+ p301（功能矩阵）。注意矩阵里打 ** 的项是"license 解锁"（如 6560 的 SPB/MPLS、6860N 的 MPLS），BOM 忘加 license 等于不支持；VC 在 6860N/6870 是 Yes，但 MPLS 在 6575/6570M 低配型号上还要看 PRM license（p334）。
  tags: [model-matrix, spb, mpls, issu, vc, selection, license]

- id: ce09
  title: 教材自相矛盾：p301 矩阵 OS9900 MPLS 标 No，p443/444 又写 9907/9912 "MPLS support"
  type: counter-example
  source_chapter: "p301 vs p443-444"
  source_quote: |
    "MPLS: ... OS9900 No. (p301, footnote: * Roadmap) ... MACsec, 1588v2 & MPLS support. (OMNISWITCH 9907, p443; same wording for 9912, p444)"
  summary: |
    场景：客户要在园区核心跑 MPLS（如 VPLS/EVPN 承载），售前查 p301 矩阵看到 9900 MPLS=No，直接把 9900 排除、改推 6900。
    后果：p443/p444 的 9907/9912 产品页明确写着 "MACsec, 1588v2 & MPLS support"，两处冲突（p301 该行很可能标注的是 Ed29 时点的 roadmap 状态，表脚注即 "* Roadmap"）。若客户核心要求机箱形态，误排除 9900 会直接输给竞品。
    避开：遇到书中前后冲突的数据，以最新 AOS release notes / 官方 datasheet 为准，投标前向 ALE 产品线确认 9900 的 MPLS 交付状态与所需 license。这条同时提醒：Ed29 教材任何"某机型支持某特性"的结论都有时效性。
  tags: [contradiction, mpls, os9900, roadmap, data-freshness]

- id: ce10
  title: MACsec 端口限制按型号裁剪：多数机型仅上联/特定口支持，6560 的 25-30/53-54 口干脆不支持
  type: counter-example
  source_chapter: "p178-180, p424"
  source_quote: |
    "OS6860N-U28: All ports except VFL. OS6860N-P48Z: SFP28 ports. OS6870: All ports, all models, except VFL ports on 6870-24/48. ... OS6560-P24X4: Ports 25-30 SFP(+) uplink ports (Not Supported). OS6560E-P48Z16: Ports 53-54 QSFP+ ports (Not Supported)."
  summary: |
    场景：客户要求"全网二层链路加密"，售前按"6860N/6870/9900 支持 MACsec"全端口承诺。
    后果：实际支持范围按型号大打折扣——6860N-P48Z/P24Z 只有 SFP28 上联口支持；6860N-U28/6870-24/48 排除 VFL 口（想加密堆叠链路不行）；6570M-12 不支持 Static 模式；6900-X48E 只有 1G/10G SFP+ 和 2 个 QSFP28 口；6560 系列 24 口型的 25-30 口、48 口型的 53-54 口（QSFP+）、X10 的 9-10 口明确不支持。
    避开：售前按 p178-180 的端口表逐口核对加密需求，加密只承诺在支持端口之间建立；堆叠/VFL 链路的 MACsec 用 6870 的 24Z/48Z/M/V 型号（p424：这几型 All ports）。
  tags: [macsec, port-limitation, security, model-matrix]

- id: ce11
  title: MACsec 从 8.6R1 起要 site license：升级 AOS 后功能会被禁用，直到装上（免费但必须下单）
  type: counter-example
  source_chapter: "p177, p340"
  source_quote: |
    "Beginning in 8.6R1 the MACsec feature requires a site license. After upgrading, the feature will be disabled until a license is installed. There is no reboot required after applying the license. ... OS-SW-MACSEC: One license per customer at no cost."
  summary: |
    场景：客户现网 MACsec 已在跑，运维直接升级到 8.6R1 及以后版本；或新项目 BOM 里漏了 MACsec license 行项。
    后果：升级完成后 MACsec 被自动禁用，加密链路中断（业务受影响）；新项目则开箱用不了。
    避开：MACsec license（OS-SW-MACSEC）每个客户一份、零费用，但必须显式下单并安装——6900 订购指引原话是 "no cost, must be included"（p340）。升级窗口里把 license 安装排进升级步骤（装完不用重启即生效）。
  tags: [macsec, license, upgrade, bom]

- id: ce12
  title: Demo License 只有一次、30 天、一激活就倒计时：MPLS 试点最容易翻车
  type: counter-example
  source_chapter: "p346"
  source_quote: |
    "Demo License: Available once for MPLS (can be used one time and not more); Valid for 30 days total; Activated as soon as MPLS is run on a node. Permanent License (for MPLS, Metro Ethernet, Advanced routing, 10G): Each one is unique (serialized), valid for a specific set of feature and platform."
  summary: |
    场景：POC/试点阶段为了赶进度，在客户设备上激活 MPLS demo license"先用着"；或实验室验证时顺手跑了 MPLS 命令。
    后果：demo license 每节点只有一次机会，只要节点上一跑 MPLS 就立即激活并开始 30 天倒计时——等正式项目要再试用时发现额度已耗尽；30 天一到特性失效，承载的业务中断。
    避开：把 demo license 当一次性火柴——只在真正的验收窗口激活，并提前把永久 license 采购流程（序列化、绑定特性+平台，纸质/电子交付）排进项目计划，30 天内完成切换。Metro Ethernet / Advanced Routing / 10G 升级同理走永久 license。
  tags: [license, mpls, demo, poc, quotation]

- id: ce13
  title: 商务坑：WWPL 升级件不打折、价格随时可变、供货分级（Standard 2 周/Extended 4 周/Contact 无期）
  type: counter-example
  source_chapter: "p324, p326"
  source_quote: |
    "The products and prices are subject to change without notice. No discount is offered on upgrades. ... Standard: ARO within two (2) weeks. Extended: Four (4) weeks. Contact: Product is announced but not released; availability information can only be given by contacting your Alcatel-Lucent representative."
  summary: |
    场景：(1) 报价时把升级 SKU（UPG/U 类）按新品折扣率算成本；(2) 用半年前的 WWPL 价目表投标；(3) 给客户承诺统一交货期，但 BOM 里混入了 Extended/Contact 分级的产品。
    后果：(1) 升级件无折扣，成本测算偏低、毛利被吃掉；(2) WWPL 明确声明价格随时变动且不另行通知，旧表报价可能直接废标或亏本；(3) Contact 类产品"已宣布未发布"，交期只能问 ALE 代表，承诺落空。
    避开：升级件按无折扣计价；每次报价前拉当月 WWPL（myportal.al-enterprise.com）；逐项核对 Sales/Service Category 与 Availability 分级，Contact 项在标书里写明"交期待确认"。
  tags: [wwpl, pricing, discount, aro, quotation, bom]

- id: ce14
  title: Roadmap 陷阱：OS6870 的 MPLS/SPB-MS/50G 只是"硬件就绪、软件未交付"，OS9912 的 VC 同样在 roadmap
  type: counter-example
  source_chapter: "p13, p413-422, p444"
  source_quote: |
    "Ready for SPB-MS and MPLS* ... * Future release – hardware ready. (OS6870 pages) ... * 50G available in future with license. ... OS9912 will support virtual chassis technology in future release. (p13) Virtual Chassis support (roadmap). (p444)"
  summary: |
    场景：客户现在就要 MPLS 接入网或 50G 上联，售前看 OS6870 宣传页写着 "MPLS*" 就按已交付特性应标；或客户要机箱双机虚拟化，售前推了两台 OS9912 组 VC。
    后果：OS6870 的 MPLS、SPB-MS、50G 在 Ed29 时点均为 "Future release – hardware ready"——硬件具备、软件未发，承诺即跳票；OS9912 的 VC 仅在 roadmap，只有 OS9907 支持双机 VC（p59：2 x OS9907）。
    避开：凡是带星号/roadmap 脚注的特性，标书里要么不承诺，要么写明"依赖 AOS 后续版本，交付时间以 roadmap 为准"。现在就要 MPLS 的接入场景选 6860N（加 MPLS license）；现在就要机箱 VC 的场景选 9907×2 或改用 6900×6 的 VC 方案。
  tags: [roadmap, os6870, os9912, mpls, vc, presales-risk]

- id: ce15
  title: 网管 License 不吃 VC 的账：虚拟机箱里每台成员交换机都要单独占一个 license
  type: counter-example
  source_chapter: "p199-200"
  source_quote: |
    "OS9900 in VC – All units need to be licensed. A VC of 2 = 2 license units. OS6900 or OS6860N in VC: All units need to be licensed, i.e. VC of 4 = 4 license counts. ... Paid Upgrades – based on UPG & U SKU from WWPL ... Different license keys across releases."
  summary: |
    场景：售前话术"VC 八台合一、只当一个管理点"，于是 OV2500 网管 license 只按 1 台买。
    后果：网管侧 license 按物理台数计——VC of 4 就是 4 个 license，license 不足则部分成员失管。另外 OV2500 跨大版本升级是付费升级（UPG/U SKU），且不同版本 license key 不通用，升级前还要做备份保住拓扑/Locator 等数据。
    避开：网管 license 数量按物理台数（含 VC 成员）算，第三方设备按管理 IP 数算；OV2500 升级项目单独列 license 换购与数据备份工作量。容量红线：单套 OV2500 最多 10000 设备 / 4000 Stellar AP / 5000 VM（p191）。
  tags: [ov2500, license, vc, capacity, upgrade]

- id: ce16
  title: OS2260/2360 不在美国销售；VXLAN Head-End 复制模式下远端 VTEP 未登记就收不到流量
  type: counter-example
  source_chapter: "p11, p24-25, p117"
  source_quote: |
    "*except in the USA. (OS2x60, p11) NOTE: Not sold in the USA. (p24/p25) ... Head end replication: Requires that the VTEP know of all the IPs of the remote VTEPs participating in a VNI, or they will not receive any traffic. (p117)"
  summary: |
    两个易踩的小坑：(1) OS2260/2360（SMB WebSmart 系列）在美国市场不销售（p11/p24/p25 三处标注 except in the USA）——美国客户的 SMB 项目不能报 2x60，要换成 6360 等替代；(2) VXLAN BUM 流量用 Head-End 复制时，本端 VTEP 必须知道同一 VNI 内所有远端 VTEP 的 IP（静态配置或动态学习），漏登记任何一台，那台就静默收不到广播/未知单播流量，故障表现是"部分站点 ARP 学不到、时通时断"，难排查。
    避开：美国项目 BOM 屏蔽 2x60 家族；VXLAN 网状设计时逐台核对 VNI 内 VTEP IP 清单，或改用 Tandem 组播模式（需 PIM-BIDIR）规避全量登记问题。
  tags: [os2260, os2360, region, vxlan, head-end-replication, vtep]
```
