# counter-examples · 陷阱/警告（stellar-wlan-adv-deploy / DT00XTE361）

```yaml
- id: ce01
  title: 复位脚本运行中按任意键会掉进 Miniboot
  type: counter-example
  source_chapter: "p46"
  source_quote: |
    "In the OmniSwitch console window, DO NOT press any key during the reset process. Pressing Enter during the OmniSwitch reboot phase will lead you to the Miniboot of the switch and interrupt the reboot cycle."
  summary: |
    运行 reset_PODX 复位脚本时，交换机重启阶段绝不能按回车/任意键，否则进入 Miniboot 且重启中断，只能等几分钟让启动流程自然结束。
  tags: [陷阱, 复位, Miniboot, 操作禁忌]

- id: ce02
  title: 误删云管组织不可恢复
  type: counter-example
  source_chapter: "p47"
  source_quote: |
    "Warning: DO NOT use the action Delete on your Organization."
  summary: |
    在 OmniVista Cirrus MSP Portal 里对所在组织点 Delete 是毁灭性操作；实验/交付中组织只进不出，删组织会连带其下站点、设备与全部配置。
  tags: [陷阱, 云管, 删除组织]

- id: ce03
  title: 树莓派的有线网卡绝对不能动
  type: counter-example
  source_chapter: "p41"
  source_quote: |
    "Never touch the Ethernet card (configuration or disconnection), because it is from the wired network that you can join the raspberry pi desktop."
  summary: |
    无线测试客户端树莓派的远程桌面走有线网，改动配置或拔有线网口会立刻失联，只能靠讲师恢复。
  tags: [陷阱, 测试客户端, 树莓派]

- id: ce04
  title: 预置设备与服务器不得管理配置
  type: counter-example
  source_chapter: "p38, p291"
  source_quote: |
    "DO NOT MANAGE AND CONFIGURE the core switch OS6900... DO NOT MODIFY OR DELETE the default configuration loaded on the OS-6870 by the reset script."
  summary: |
    核心交换机 OS-6900、汇聚 OS-6870 的预置默认配置、DHCP/NAT 服务器都属于平台底座：L3 路由由脚本预置，改删会断开 POD 与 DHCP/外网/云管的连通。正确做法是"保留默认配置，在其上叠加实验所需配置"。
  tags: [陷阱, 预置配置, 变更边界]

- id: ce05
  title: untagged 与 tagged VLAN 之间不能漫游
  type: counter-example
  source_chapter: "p264"
  source_quote: |
    "No Roaming from an untagged VLAN to a tagged VLAN."
  summary: |
    同一 SSID 在两台 AP 上一个配成 untagged、一个配成 tagged 时客户端无法漫游——VLAN 封装方式不一致是漫游静默失败的常见根因，部署多 AP 同 SSID 时必须统一打标方式。
  tags: [陷阱, 漫游, VLAN]

- id: ce06
  title: RSSI 门限设得过高会主动踢客户端
  type: counter-example
  source_chapter: "p281"
  source_quote: |
    "High RSSI Threshold? Cause client to disconnect if their RSSI is below the Threshold. ... signalStrengthThreshold:70 ... Threshold too high. Decrease the value."
  summary: |
    RF Profile 的 signalStrengthThreshold（案例中被设为 70）会让低于门限的客户端被强制断开；"客户端频繁掉线"排查时除查发射功率外，必须检查该门限是否设得过激进，必要时下调。
  tags: [陷阱, 掉线, RSSI门限, RF-Profile]

- id: ce07
  title: AP 发射功率被压到最小导致弱信号掉线
  type: counter-example
  source_chapter: "p279-p280"
  source_quote: |
    "AP transmit power is too low? ... Current Tx-Power=3 dBm (1 mW) — Transmit power set to minimum value. ... Bad signal quality. High probability of disconnection."
  summary: |
    案例中客户端 RSSI 仅 16（约 -80dBm）、SNR 30：噪声虽大但根因是 AP 发射功率被设为最小值 3dBm。修复：在 RF Profile 调大功率。教训：低功率部署（如打印机场景）只适用于终端紧邻 AP 的特例，通用覆盖不能照搬。
  tags: [陷阱, 发射功率, 弱信号, 掉线]

- id: ce08
  title: 僵尸进程悄悄吃光内存
  type: counter-example
  source_chapter: "p217"
  source_quote: |
    "Issue: X (Dead) and Z (Zombie process). Too many Zombie processes will consume large portion of memory."
  summary: |
    ps 输出里出现 X（Dead）或 Z（Zombie）状态进程即为异常；僵尸进程累积会大量占用内存导致 AP 功能劣化。发现后收集进程清单开票给技术支持，不要只重启了事。
  tags: [陷阱, 进程, 内存, 系统诊断]

- id: ce09
  title: Captive Portal 客户端无 IP 时重定向必失败
  type: counter-example
  source_chapter: "p220"
  source_quote: |
    "Client first connection to the Captive Portal. Client IP address unknown. Redirection URL can not be sent."
  summary: |
    门户首连时客户端 IP 还是 0.0.0.0，AP 发不出重定向 URL 是正常时序而非故障；但若客户端始终拿不到 IP（DHCP 故障/VLAN 错/Final_role 过滤 DHCP），门户就会"永远打不开"。先查 IP 再查门户。
  tags: [陷阱, Captive-Portal, DHCP, 时序]

- id: ce10
  title: 老款 AP 桥接不支持 VLAN 打标
  type: counter-example
  source_chapter: "p113"
  source_quote: |
    "* AP1101, AP1201 & AP1201H are not compatible with VLAN tagging over a bridge."
  summary: |
    WiFi Bridge 宣称"可用 VLAN 分隔与保护桥上流量"，但 AP1101/AP1201/AP1201H 三款例外——桥接上不支持 VLAN 打标，选型时若需桥上多 VLAN 隔离必须避开这三款。
  tags: [陷阱, Bridge, VLAN, 选型限制]

- id: ce11
  title: 国家码不匹配导致客户端看不到 SSID
  type: counter-example
  source_chapter: "p276"
  source_quote: |
    "3) Country Code of the AP? Supported by the client? Wrong country code: Set manually a compatible channel on the AP in RF profile."
  summary: |
    AP 国家码决定了可用信道集，客户端不支持该国信道时就"看不见"SSID——现象像 SSID 没广播，实际是信道不兼容。规避：在 RF Profile 手工指定一个双方都兼容的信道。
  tags: [陷阱, 国家码, 信道, SSID不可见]

- id: ce12
  title: 训练环境里把"升级演示"当真执行会砸环境
  type: counter-example
  source_chapter: "p252"
  source_quote: |
    "THE STELLAR AP HAVE ALREADY THE DESIRED SOFTWARE VERSION. THIS SECTION EXPLAINS ONLY HOW TO SCHEDULE THE UPGRADE... DO NOT COMPLETE THIS SCHEDULE UPGRADE."
  summary: |
    升级计划向导走读止步于 Review 步点 Cancel：远程实验室版本是配好的，真建计划会触发重启、终端断线。推及生产：任何升级计划创建前都要确认目标版本确实需要、窗口已批准（参考 ce 配套原则 p17）。
  tags: [陷阱, 升级, 演练环境, 变更控制]

- id: ce13
  title: 云管删除有依赖顺序，硬删会报错
  type: counter-example
  source_chapter: "p316"
  source_quote: |
    "The AP Group can only be deleted if no custom provisioning configuration is assigned. ... If you get an error while trying to delete it, Edit this profile and set the RF profile parameter with 'Default RF Profile'."
  summary: |
    清理组织的典型报错：AP 组上还挂着自定义 Provisioning 配置时删不掉；删 Provisioning 配置又因其引用了自定义 RF Profile 而失败。必须先解除引用（改回 Default）再逐层删除，逆着创建顺序操作。
  tags: [陷阱, 清理, 依赖顺序, 云管]
```
