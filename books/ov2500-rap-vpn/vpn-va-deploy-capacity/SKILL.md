---
name: vpn-va-deploy-capacity
description: 何时用：在 VMware/Hyper-V/KVM 上部署 RAP VPN VA 虚拟机时做容量分档、三网卡配置、导入与初装，含升级割接。
source_book: OV2500 4.9R2 RAP and VPN VA Installation
---

# VPN VA 部署与容量规划（三平台）

## R · 原文引用

> "1 - 100 APs - 4 vCPUs, 2GB RAM; 100 - 250 APs - 6 vCPUs, 4GB RAM; 250 - 500 APs - 8 vCPUs, 8GB RAM; 500 - 1,000 APs - 12 vCPUs, 16GB RAM. ... For deployments with more than 250 RAPs, it is recommended that you deploy a second VPN VA Server." (p13)

> "Configure VLAN 0 if you want Untagged VLAN traffic to be tunneled through VPN tunnels. Configure VLAN 4095 if you want Tagged VLAN traffic to be tunneled through VPN tunnels. On the ESXi VM, enable Promiscuous Mode for the above NIC. If the "Override" checkbox is enabled, make sure Promiscuous Mode, MAC address changes, and Forged transmits are set to "Accept"." (p20)

> "Use Eth0 for the public interface, Eth1 for the private interface, and Eth2 for the bridge interface. ... Set-VMNetworkAdaptervlan -VMName OmniVista-VPN-4.9.2 -VMNetworkAdapterName "Eth2" -Trunk -AllowedVlanIdList "201,202" -NativeVlanId 0" (p29, p32)

> "To set up a Data Tunnel, you use the third NIC on the VA. You must not configure an IP address for this NIC because it will be a Layer 2 Tunnel. You also need to enable "Promiscuous Mode" for this NIC in your Hypervisor." (p55)

## I · 方法论骨架

1. **容量先分档**：按 RAP 数量选 4 档规格；超 250 台加第二台 VPN VA 分担（产品不支持冗余，不能按 HA 设计）。
2. **吞吐定网卡**：每 RAP 吞吐 10-20 Mbps（Local Breakout 全兜底）或 20-100 Mbps（全隧道）；500 台以上标配 10G，更高用双 10G Teaming。
3. **三平台共同骨架**：OVF/qcow2 导入（VMware/Hyper-V 必删 *.mf）→ 三网卡（公网/私网/桥接，桥接网卡无 IP + 开混杂模式）→ 控制台初装（E1000 默认、Admin 密码）→ NIC1 公网 IP、NIC2 私网 IP、配 SSH、回程路由。
4. **平台专属项**：VMware=端口组 VLAN 0/4095 与三项 Accept；Hyper-V=PowerShell 建网卡 + Trunk + Teaming 兼容矩阵；KVM=3 网卡 Macvtap + 双盘 Discard unmap。
5. **升级七步**：备份 vpn_profile → 新 VA disconnected 部署 → 旧 VA 跑到第 4 步才关 → 停机约 5 分钟。

## A1 · 书中案例

- 容量样例：100 台以下 4 vCPU/2GB；500-1000 台 12 vCPU/16GB；251 台起规划第二台。
- Hyper-V 网卡样例：Eth0 映射公网 VLAN 70、Eth1 映射私网 VLAN 1000、Eth2 开 MAC 地址欺骗后配 Trunk（AllowedVlanIdList "201,202"、NativeVlanId 0），Get-VMNetworkAdapterVlan 验证。
- NIC Teaming 实测矩阵：Switch Independent 下仅 Address Hash 可用；Linkagg static / LACP 下三种负载均衡全通过。
- KVM 样例：Ubuntu 22.04 装 qemu-kvm/libvirt/virtinst/bridge-utils，两块 qcow2、OS 选 Generic Linux 2022，安装前对两块 VirtIO 盘把 Discard Mode 设 unmap。
- 升级样例：旧 VA 4.9.1 Build 3 一直运行到第 4 步才关停，RAP 断连集中在第 4-7 步，约 5 分钟；新 VA 4.9.2 默认硬盘 8GB。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：模式已定（见 `rap-vpn-mode-registration`），开始动手装 VPN VA：选 vCPU/内存档位、ESXi/Hyper-V/KVM 导入 OVF、配网卡、初装控制台，或版本升级割接。
- 与 `rap-vpn-mode-registration` 的区分：那边管选型和 Device Catalog 注册；本 skill 从"拿到 OVF 包"开始。
- 与 `rap-data-tunnel-config` 的区分：本 skill 终点是 VA 网络就绪（三网卡 IP、SSH、回程路由）；VPN 设置文件导入、Data VPN Server、SSID 配置不在此处。
- 与 `rap-vpn-troubleshooting` 的区分：升级流程在本 skill（变更操作）；运行期故障定位转排障 skill。

## E · 可执行步骤

1. 按台数定规格：1-100→4C2G；100-250→6C4G；250-500→8C8G；500-1000→12C16G；>250 台规划第二台。500 台以上上 10G 网卡。
2. 导入：解压包后只留 OVF + 两块 VMDK/qcow2，**先删 *.mf**；VMware 磁盘置备选 Thin；Hyper-V 导入类型选 Copy the Virtual Machine；KVM 勾 Customize configuration before install。
3. VMware 桥接网卡端口组：untagged 流量配 VLAN 0，tagged 配 VLAN 4095；混杂模式必开，勾 Override 时 Promiscuous Mode / MAC address changes / Forged transmits 三项全部 Accept；端口组继承 vSwitch 时确认 vSwitch0 三项为 Accept。
4. Hyper-V：删原网卡，PowerShell 循环 Add-VMNetworkAdapter 建 Eth0/Eth1/Eth2 + External 交换机；Eth0/Eth1 配 VLAN 识别，Eth2 开 MAC 地址欺骗并 Set-VMNetworkAdapterVlan 配 Trunk，验证后开机。
5. KVM：3 块网卡统一 Network Source=Macvtap device、Device name=宿主机网卡名、Device model=default；Begin Installation 前对两块 VirtIO 盘设 Discard Mode=unmap。
6. 初装：保留 OVF 默认 E1000；接受协议、设 Admin 密码；NIC1 配公网 IP（例 10.255.222.97/24）、NIC2 配连 OVE 的接口 IP、第三网卡**禁配 IP**；配 SSH（SFTP 用）、每步 Apply。
7. 回程路由：VA 菜单 2→8→3 加路由让 OmniVista 可达 VA 企业网卡段（如 10.255.255.0/24），菜单 2 核对。
8. 升级：备份 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile → 新 VA 三网卡同端口组但 disconnected → 配好除 VPN Endpoints 外全部项 → 关旧 VA → 网卡改 connected → 导入备份 profile → 按旧配置设 VPN Endpoints（停机约 5 分钟，VMware/Hyper-V 通用）。

## B · 边界与陷阱

- **不支持冗余**（Known Limitations，p14）：不能做双机热备；SLA 与割接窗口按单点评估（ce03）。
- ***.mf 未删**：VMware/Hyper-V 两条路径都会卡在导入步骤（ce02；"导入失败"为推断，原文未明说后果）。
- **第三网卡误配 IP**：数据隧道是 L2 桥接，配 IP 即不通；hypervisor 侧还要开混杂模式（ce05）。
- **vSwitch 混杂模式默认 Reject**：双隧道全 up、客户端仍 ping 不通同网段任何设备；Override 勾了但三项没全 Accept、或端口组继承的 vSwitch0 仍是 Reject，同样失效（ce06）。
- **Hyper-V Teaming 选错组合**：Switch Independent 下选 Hyper-V Port 或 Dynamic 实测不通过，只有 Address Hash 可用（ce08）。
- **KVM 漏设 unmap**：Begin Installation 点完就无法回头补，只能重部署（ce09；"只能重部署"为推断）。
- 虚拟网卡数量仅受 hypervisor 限制，VA 自身不设限。

---
来源条目: p05, p06, p07, p08, p09, p10, p11, p19, ce02, ce03, ce05, ce06, ce08, ce09, g04, g16, g17
