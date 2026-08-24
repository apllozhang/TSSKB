---
name: rap-vpn-troubleshooting
description: 何时用：RAP 管理隧道/数据隧道 down、AP 不注册、客户端拿不到 DHCP 或上不了 LAN 时的分层排障决策树。
source_book: OV2500 4.9R2 RAP and VPN VA Installation
---

# RAP 隧道排障决策树

## R · 原文引用

> "If the AP Management VPN Tunnel is down: Check if tunnel interface was created using command "wg" on VPN VA ... Verify that the AP's IP Address is present in the VPN.conf file ... Verify that the firewall is not blocking traffic in both ways (from outside company, from VPN-VA)." (p81)

> "If both tunnels are UP but client does not get DHCP lease: Check if the client is present in the AP association list with command "ssudo sta_list"" (p81，原文命令拼写即 ssudo)

> "Client is not able to ping any device or gateway within same subnet. Make sure that Promiscuous Mode is enabled and set to "Accept" on the vswitch (by default this is set to reject). ... Promiscuous Mode is enabled but it is not working. Check if the Override checkbox is disabled." (p81)

## I · 方法论骨架

按"隧道状态 → 注册状态 → DHCP → LAN 可达"四层逐层下钻，先看隧道再查之上业务：

1. **管理隧道 down**：wg 查接口 → 查 AP IP 是否在导入的 VPN.conf → 防火墙双向放行。
2. **管理隧道 up 但 AP 未注册到 OV**：OV ping AP → OV 上配到 AP wg0 子网的静态路由。
3. **数据隧道 down**：两侧 wg → 配置是否推到 AP 的 /tmp/config/datavpn.conf → Data VPN Server 是否绑了 AP Group → ifconfig wg1 是否有 IP、该 IP 是否在 Data-VPN.conf → 防火墙双向。
4. **双隧道 up 但客户端无 DHCP**：sta_list 查关联与 TUNNELID/FARENDIP → brctl show 查桥接（ath0x 应关联 br-g1）→ 接入交换机是否学到客户端 MAC → DHCP relay（ip helper、dhcp-snooping）。
5. **客户端上不了 LAN**：vSwitch 混杂模式默认 Reject 改 Accept；Override 勾选时三项全 Accept。

## A1 · 书中案例

- wg show 输出基线（p81-82）：对端 endpoint 198.206.185.132:9093、persistent keepalive 每 5 秒；检查公钥/监听端口/allowed ips/握手时间/收发增量。
- ip -d link 基线：gre0=1476、gretap0=1462、wg0=1420，均须低于 1500。
- 配置核对路径：管理配置 `cat /etc/config/rap.conf`，数据配置 `cat /var/config/datavpn.conf`。
- 日志收集：VPN VA 日志走 VA 菜单；RAP 日志经 OV（OVE/OVC）→Administration→Audit→Collect Support Info。

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：交付后或变更后出现"AP 离线""隧道起不来""无线连上但拿不到 IP / 上不了内网"，需要按层定位。
- 与 `vpn-va-deploy-capacity` 的区分：部署期的导入/网卡错误在那边（如混杂模式的三项 Accept 配法两边都引用，本 skill 把"混杂模式默认 Reject"作为故障第一嫌疑）。
- 与 `rap-data-tunnel-config` 的区分：那边是正向配置（设置文件、AP Group 绑定）；本 skill 假设配置已做完，定位哪一环失效——很多故障根因正是那边 B 节列的陷阱（文件没重传、AP Group 没绑）。
- 与升级割接相关：若故障发生在 VA 升级后（约 5 分钟窗口），先确认第 4-7 步是否已完成、profile 是否已回导。

## E · 可执行步骤

1. 先定层：wg 查管理隧道接口在不在。不在 → 走第 2 步；在 → 跳第 3 步。
2. 管理隧道 down：确认在 VPN VA 上执行（RAP 不可达时不在此执行）；grep AP 的 IP 是否在导入的 VPN.conf；核对防火墙双向（企业外部↔VPN-VA）。
3. 隧道 up 但 OV 里没 AP：从 OV ping AP 地址；检查 OV 到 AP wg0 子网的静态路由。
4. 数据隧道 down：两侧 wg 查接口；AP 上 cat /tmp/config/datavpn.conf 看配置是否推送；确认 Data VPN Server 已绑 AP Group；ifconfig wg1 看 IP 且核对在导入的 Data-VPN.conf 中；防火墙双向。
5. 双隧道 up、客户端无 DHCP：AP 上 sta_list 查关联与 TUNNELID/FARENDIP；brctl show 确认 ath0x 关联 br-g1；查企业接入交换机 MAC 表；查 DHCP relay（ip helper、dhcp-snooping）。
6. 客户端不通同网段设备/网关：vSwitch/端口组混杂模式改 Accept；勾了 Override 则 Promiscuous Mode、MAC address changes、Forged transmits 三项全 Accept；端口组继承时确认 vSwitch0。
7. 仍不明：wg show 对基线（endpoint/keepalive/握手/收发增量）；ip -d link 对 MTU 基线；收集 VA 菜单日志 + OV→Administration→Audit→Collect Support Info 的 RAP 日志。

## B · 边界与陷阱

- **混杂模式默认 Reject 是"客户端不通 LAN"的头号原因**——双隧道全 up 也照样不通；第二层坑是 Override 勾了但三项没全 Accept，或端口组继承了 Reject 的 vSwitch0（ce06，p20/p81 两处强调）。
- wg 相关命令要在**有隧道上下文的一侧**执行：RAP 不可达时不在 RAP 上执行 wg 定位管理隧道。
- MTU 基线数值（1476/1462/1420）为书中实测样例，环境不同会略有差异，核对"低于 1500"这一性质即可。
- 排障前先问"最近改过什么"：加了 AP 没重传设置文件、改了 VPN 配置没重新导出、升级后 profile 没回导，都是高发根因（见 `rap-data-tunnel-config` 的 B 节）。
- DS-Lite ISP 环境下隧道慢/断，先按 TCPMSS/MTU 参数表核对（1352/1300/1376 一组），参数入口见 `rap-data-tunnel-config` 第 8 步。

---
来源条目: p20, ce06（交叉引用）, p19（升级窗口交叉引用）
