# 术语词典

| 术语 | 含义 | 页码 |
|---|---|---|
| Bridging（桥接） | Point-to-Point 单链路 mesh 配置，延伸整个企业 LAN 到远端站点，不广播 SSID | <<<PAGE 6>>> |
| Multi-Point Meshing（多点网状） | 面向无法布线区域的多节点 mesh 配置，root 与各 mesh AP 可广播 WLAN 服务并带下联口 | <<<PAGE 6>>> |
| Root 角色 | mesh 集群中作为 LAN 网关的 AP，所有数据流量经其进出有线网 | <<<PAGE 5>>> |
| Mesh 角色 | mesh 集群中的无线节点 AP，逐跳转发数据 | <<<PAGE 5>>> |
| 双 root | 同一 AP group 配置两个 root AP，mesh AP 按最佳 RSSI 选接，提供网关冗余 | <<<PAGE 6>>> |
| Mesh backhaul（回程） | mesh AP 之间/到 root 的无线回传链路，与客户端业务共享带宽，可配 5GHz 或 2.4GHz | <<<PAGE 7>>> |
| Auto-Mesh | root 连 LAN 激活后，邻居空配置 AP 自动用默认 mesh 链路接入的开局特性 | <<<PAGE 7>>> |
| WDS（Wireless Distribution System） | AP 以 station 模式互连的透明以太桥接，用 802.11 四地址帧（普通客户端业务为三地址），统一广播域、承载多 VLAN | <<<PAGE 7>>> |
| 4 地址帧 | WDS 模式使用的 802.11 帧格式，携带两个 802.11 MAC 源/目的以实现透明桥接 | <<<PAGE 7>>> |
| 吞吐减半 | Multi-Point 模式下 mesh 节点同频同射频收发，需回传的数据吞吐每节点除以 2 | <<<PAGE 7>>> |
| ENET0/ENET1 | AP 的以太口；Bridge 默认经 ENET0 分发 VLAN，AP1361/1362/1361D 的 ENET1 支持 802.3af/at PSE PoE 输出 | <<<PAGE 8>>> |
| 下联口（downlink port） | mesh/bridge AP 上为远端有线客户端提供接入的以太口，透传 tagged/untagged VLAN | <<<PAGE 8>>> |
| ARP（Access Role Profile） | Enterprise 模式按 VLAN/端口定义角色（ACL、QoS）的配置档 | <<<PAGE 8>>> |
| LoS（Line of Sight） | 视距：天线主瓣互对、无遮挡的链路形态，bridge 典型要求 | <<<PAGE 9>>> |
| nLoS | 非视距配置；半定向天线波束边缘至少计 3dB 损耗 | <<<PAGE 11>>> |
| Fresnel 区净空 | 链路椭球区无遮挡比例，至少 60%；决定天线安装高度 | <<<PAGE 12>>> |
| RFPL（Free Space Path Loss） | 自由空间损耗，距离-吞吐性能表链路预算的计算项 | <<<PAGE 14>>> |
| SOM（System Margin） | 系统余量，默认 10dB，吸收风雨等外部条件引起的射频波动 | <<<PAGE 14>>> |
| MU-MIMO 天线 | 通常双斜 ±45°、垂直/水平极化，推荐用于 bridge/mesh AP 性能 | <<<PAGE 9>>> |
| TIA-6076B | 室外电气安装（防雷接地）最佳实践参考标准 | <<<PAGE 12>>> |
| IP67 | 室外防护等级；室外 AP（AP1361/1251 等）与室外 PoE 注入器的要求 | <<<PAGE 10>>> |
| Ekahau PRO | 站点勘测/规划工具（10.4 版内置 Stellar AP 与天线），仿真 mesh 链路传播与吞吐 | <<<PAGE 18>>> |
| OV2500（OmniVista 2500 / Cirrus） | Enterprise 模式统一管理平台：AP group、RF profile、SSID、mesh 角色、uNP、监控 | <<<PAGE 5>>> |
| Express 模式 | Wi-Fi Express 轻量管理模式，逐 AP 经 APUI（手机/平板）管理，家庭 mesh 场景使用 | <<<PAGE 16>>> |
| APUI | AP 自带 Web 管理界面，可设 mesh 角色（Backhaul0）与端口 VLAN（Enet0/1/2/3） | <<<PAGE 25>>> |
| uNP 认证配置（Access Auth Profile） | 管理 bridge 下联口的端口配置档：trust tag、bypass VLAN、端口认证参数 | <<<PAGE 24>>> |
| Trust tag / Bypass VLAN | uNP 按端口信任 tag 与放行的 VLAN 列表 | <<<PAGE 25>>> |
| rfprofile.conf | AP 本地 /tmp/config/ 下实际生效的 RF 配置文件，监控核对用 | <<<PAGE 27>>> |
| Link Quality | iwconfig 输出的链路健壮度指标（基于信号强度与 SNR），骤降提示距离/频率/安装/nLoS 问题 | <<<PAGE 30>>> |
| athap1 / ath01 / ath11 | AP 无线接口：athap1 为 mesh backhaul 接口，ath01/ath11 为 2.4G/5G 客户端 SSID 接口（书中示例） | <<<PAGE 30-31>>> |
| DRM（Dynamic Radio Management） | 动态射频管理；mesh SSID 上远端客户端的 DRM 只在 root AP 层处理 | <<<PAGE 29>>> |
| DFS（UNII-2 子带） | 动态频率选择子带，雷达检测告警直接显示在 AP 控制台 | <<<PAGE 30>>> |
| 802.11ax / Wi-Fi 6 | 第六代 Wi-Fi 标准；Extra Range、长保护间隔（long GI）、OFDMA、扩展 MU-MIMO 利用户外链路 | <<<PAGE 9>>> |
