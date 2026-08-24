# OV2500 RAP 与 VPN VA 精华速读

> 目标读者：要做居家办公/分支 AP 回连交付的网络工程师。读完这篇，不翻原书也能把方案选型、部署主线、配置要点、排障路径和版本红线装进脑子。

## 一、一页看懂 RAP 方案

方案的第一道分岔在管理模式，不在产品型号（p4）：

- **OVE 全隧道模式（真 RAP）**：AP 由企业本地 OmniVista Enterprise（OVE，OmniVista 企业版）管理。开箱首连 OVC Device Registration Server 取回参数（含 OVE IP），密钥导出到总部 RAP VPN Server，先建 WireGuard 管理隧道接受 OVE 管理，再配数据隧道承载业务——两条隧道。
- **OVC 仅数据模式**：AP 由 OmniVista Cirrus（OVC，ALE 云管平台）管理，技术上不算 RAP。管理通道走 OVC 云内 OpenVPN，不配 Management VPN Server；只有数据流量要回传总部时，才对企业的 VPN Server 另建一条 Data VPN 隧道（p4）。

拓扑上抓住一个可达性判断：本地 AP 靠 DHCP option 138 直连 OV 就能管；远程站点 AP 对企业侧不可直达，连接与管理必须走 VPN 隧道（p4）。VPN VA 是专有隧道终结点，与 Cirrus/OV2500 打配合（p5）。

## 二、部署主线

顺序错一步，隧道就建不起来。主线五段：

1. **账号**：注册 registration.ovcirrus.com 建 Cirrus Freemium 账号（验证邮件来自 noreply@ovcirrus.com，正文含设备 OS 下载链接）（p6-7）。
2. **目录**：先定 VPN Server 四参数——Public IP、Port、VPN IP（私网地址，必须与客户端池同网段）、Client VPN IP Pool（p10-11）——再把 AP 加进 Device Catalog 并预置 Security Keys。首次 VPN Settings 用 Create New，后续 AP 用 Choose Existing 复用。CSV 批量导入时 RAP 列必须为 TRUE。
3. **VPN VA**：按 RAP 台数选容量档（p13）：

| RAP 数量 | vCPU | 内存 |
|---|---|---|
| 1-100 | 4 | 2GB |
| 100-250 | 6 | 4GB |
| 250-500 | 8 | 8GB |
| 500-1000 | 12 | 16GB |

   超 250 台建议部署第二台 VPN VA——产品**不支持冗余**（p14 Known Limitations），别按双机热备设计。吞吐参考：Local Breakout 兜底每 RAP 10-20 Mbps，全隧道 20-100 Mbps；500 台以上标配 10G 网卡（p13-14）。

4. **隧道**：导入 OVF/qcow2（先删 *.mf）→ 三网卡（Eth0 公网/Eth1 私网/Eth2 桥接，桥接网卡禁配 IP + 开混杂模式，p20/p55）→ 控制台初装、配 SSH、加回程路由。
5. **验证**：管理隧道和数据隧道分别用 wg / wg1 核对接口与握手，客户端能拿 DHCP、能通 LAN 才算收工。

## 三、配置文件与 Local Breakout 要点

**设置文件是这套方案的命门**（p62-63）：Device Catalog/Data VPN Server 界面导出（AP 入目录即可，无需等 Registered），SFTP 上传到 VA 的 /opt/OmniVista_2500_NMS/data/vpn_conf/vpn_profile 目录，**文件名不可改**；任何配置变更或新加 AP，都必须重走"导出→SFTP→VA 重配"全流程——旧文件里没有新 AP 的 WireGuard 公钥。

Data VPN 五步链：建 Data VPN Server → **绑 AP Group（p68 明确 mandatory，不绑隧道建不起来）** → 导出文件 → SFTP 上传 → 配 VPN Service 与 Endpoint（管理隧道接口选 None，数据隧道选无 IP 的 eth2）。隧道 SSID 参数块：Use Tunnel 勾选、Tunnel ID=0、选 Data VPN Server profile、WPA3_AES、Entropy 禁用（p71）。最终 RAP 与 VPN Server 间建 L2GRE 隧道（p67-68）。

Local Breakout 三条路由红线（p73-74）：只有 Tunnel ID=0 且隧道内单 VLAN 才能开；静态路由跨 SSID 累积（SSID1 配 A/B、SSID2 配 C/D，四条对两个 SSID 都生效），子网必须唯一；隧道 VLAN 网段禁手工配路由。DNS 故障统一解法是配正确的总部 DNS（p83-84）。DS-Lite 环境按参数表调 TCPMSS/MTU（1352/1300/1376 一组）。1201H 下行口认证仅限 Premium/Business 账号、仅 AP1201H/1201HL/AP1311、最多 Eth1-Eth3 三口（p75）。

## 四、排障决策树

按四层下钻，先看隧道再查其上的业务：

1. **隧道层**：wg 查接口在不在；管理隧道 down → grep AP IP 是否在 VPN.conf、防火墙双向放行；数据隧道 down → cat /tmp/config/datavpn.conf 看配置推没推、Data VPN Server 绑没绑 AP Group、ifconfig wg1 有没有 IP（p81）。
2. **注册层**：隧道 up 但 OV 里没 AP → OV ping AP，加 OV 到 AP wg0 子网的静态路由（p81）。
3. **DHCP 层**：双隧道 up 客户端拿不到 IP → AP 上 sta_list 查关联与 TUNNELID/FARENDIP，brctl show 确认 ath0x 桥到 br-g1，再查交换机 MAC 表与 DHCP relay（p81）。
4. **LAN 层**：客户端 ping 不通同网段设备/网关——**vSwitch 混杂模式默认 Reject 是头号原因**（p20/p81 两处强调）；勾了 Override 则 Promiscuous Mode、MAC address changes、Forged transmits 三项全 Accept，端口组继承时确认 vSwitch0。

排障前先问"最近改过什么"：加 AP 没重传设置文件、改配置没重新导出、VA 升级后 profile 没回导（升级停机约 5 分钟，p19），都是高发根因。

## 五、端口与版本红线清单

- **hypervisor**：ESXi 6.5/6.7/7.0.2/8.0，**5.5 明确不支持**；Hyper-V 2016/2019/2022；另支持 Ubuntu 22.04 LTS + KVM（p5）。
- **版本配套**：AWOS ≥5.0.2（文档三处口径打架：p7 邮件写 5.0.1、p71 写 4.0.1 疑笔误，按最严 5.0.2+ 核对）；VPN VA 4.9.2.2 配 OV2500 4.9R2 / OVC 4.9.2（p5）。
- **网卡与端口**：Eth0 公网口/Eth1 私网口/Eth2 桥接口（L2 隧道禁配 IP）；Hyper-V Teaming 仅 Switch Independent + Address Hash 实测可用（Switch Independent 下另两种不通过）；KVM 安装前必须对 VirtIO 盘设 Discard=unmap，点完 Begin Installation 就无法回头。
- **导入红线**：解压后先删 *.mf 再导 OVF，否则 VMware/Hyper-V 都会卡在导入步骤。
- **License 红线**：下行口认证需 Premium/Business 账号；CSV 的 RAP 列留空或 FALSE，导入看似成功但 AP 不带隧道配置。

---
由 cangjie-skill 流水线从 OV2500 4.9R2 RAP and VPN VA Installation 蒸馏生成。
