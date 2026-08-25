---
name: SSIDs 一步式配置与 WLAN 高级特性
description: 需要在 SSIDs 应用一步式创建无线网络（五种 Usage 预设）、配置 WPA3/Enhanced Open/6GHz、Private Group PSK (PPSK)、Device Specific PSK、VLAN 池限制、WLAN Service (Expert) 高级参数时使用。
source_book: OmniVista 2500 NMS 4.9R2 User Guide
---

## R（触发场景）
- 新建员工/访客 Wi-Fi，想一步生成认证、策略、Portal 全套配置
- 上 Wi-Fi 6E/7：6GHz 频段的 OWE、Transition Mode 兼容
- 不同部门共享 SSID 但口令与权限隔离（PPSK）
- 每台设备派发独立 PSK（Device Specific PSK）

## I（核心理念）
SSIDs 应用是一步式配置模型：创建 SSID 时自动派生并联动创建 Access Role Profile/Access Policy/Authentication Strategy/Guest/BYOD Access Strategy/AAA Server Profile/Tunnel Profile/Global Configuration（以 SSID 派生名命名）。五种 Usage 预设决定认证形态；SSID 也可在 WLAN Service (Expert) 里配，两种入口的编辑权随 Origin 而定。

## A1（行动框架）
Usage 预设选型（principles·P195，<<<PAGE 861-863>>>）：
1. **Guest Network**：Open + Captive Portal（CP 二选 OV-UPAM / External）
2. **Employee BYOD**：MAC + BYOD Portal
3. **Enterprise 802.1X**：企业认证
4. **Protected Network**：PSK + 可选 CP
5. **Protected Network for Employees**：PSK + BYOD Portal
约束：SSID ≤31 字符；一屏最多 15 个 SSID；Usage 与 Authentication Strategy 不匹配的 SSID 不能编辑。

## A2（操作步骤）
- **安全等级矩阵**（principles·P175，<<<PAGE 649-655>>>）：Open / Enhanced Open（OWE；Transition Mode 双 BSSID 兼容旧客户端，仅 AWOS 4.0.8+）/ Enterprise（DYNAMIC_WEP~WPA3_AES256 六种）/ Personal（STATIC_WEP~WPA3_PSK_SAE_AES 七种）；PMF 三态 Disabled/Optional/Required；Hotspot 2.0 仅 Enterprise WPA2_AES/WPA3_AES256
- **6GHz 规则**：Enhanced Open 在 6GHz 强制启用且不可关；6GHz SSID 的 2.4/5G 自动继承 WPA3_SAE_AES，开 Backward Compatibility 后用混合 WPA3_PSK_SAE_AES（MLO 含 6GHz 时自动禁用）（principles·P175/P196，<<<PAGE 649-655, 864-874>>>）
- **WPA3 兼容回退**：WPA3_AES256 不支持的 AP 自动回退 WPA2_AES（AP1101 全频段、AP1201H 2.4G 不支持）；AUTO_WPA_WPA2 混合模式两谱系均可用（principles·P196，<<<PAGE 864-874>>>）
- **Device Specific PSK**：每台设备按 MAC 派发不同 PSK，须同时在 SSIDs/WLAN Service (Expert) 与设备上启用；仅配 UPAM RADIUS：Prefer（无 AES-CBC-128 属性时用 SSID key）/Force（恒用 AAA 返回值，隐藏 Private Group PSK 配置）；可打印 PSK 或二维码（principles·P179/P196，<<<PAGE 697-702, 864-874>>>）
- **Private Group PSK (PPSK)**：按不同口令分组建组入不同 Access Role Profile；每 SSID ≤16 条 Entry，单 AP 全部 SSID 合计 ≤64 条；Entry 名与口令均不可重复（principles·P196，<<<PAGE 864-874>>>）
- **WLAN Service 无线参数默认值**：Max Clients Per Band 1-128 默认 64；最小客户端速率建议 2.4G=12、5G=24；Broadcast Key Rotation 默认 15 分钟；802.1p/DSCP 映射（Voice 上行 6/下行 6,7、Video 上 4/下 4,5）（principles·P165，<<<PAGE 603-606>>>）
- **TLS RADIUS**：选 TLS 服务器的 SSID 生成 AAA 仅含 802.1X 主服务器；TLS 服务器不支持 CP/MAC 认证；自动生成的 AAA Profile 与 SSID 同名——要换 RADIUS 应改 SSID 而非直接改该 Profile（principles·P196）

## E（实证案例）
- SSID 一步式创建：选 Usage → 自动派生八个配置对象（principles·P195，<<<PAGE 861-863>>>）
- PPSK 分组建组入不同 Access Role Profile（principles·P196，<<<PAGE 864-874>>>）
- SSID 也可在 WLAN Service (Expert) 配置，WLAN Name/WLAN Service Name 即 SSID Service Name（principles·P195）

## B（反例/坑）
- Usage 与 Authentication Strategy 不匹配的 SSID 不能编辑（如 Guest CP 用途却配了 Local DB+无 Web 认证）（principles·P195，<<<PAGE 861-863>>>）
- Transition Mode 需 AWOS 4.0.8+，旧版本重启后 SSID 退化为 open（principles·P196，<<<PAGE 864-874>>>）
- Stellar AP VLAN 池按机型限 WLAN 数：AP1301H=2、AP1311/1301/1431/1411=4、AP1320/1331/1351/1451=7（各 256 VLAN/WLAN）（principles·P196，<<<PAGE 864-874>>>）
- 事后把 TLS-disabled 服务器改开 TLS 会失败（principles·P196）
- WCF 首访放行陷阱：AP 对首次访问的 URL 先放行再判定，DNS 缓存过期后首个访客不受过滤（principles·P196，<<<PAGE 864-874>>>）
- Origin=SSIDs 的 WLAN Service 只能在 SSIDs 应用编辑/删除；Device Config 改动只影响所选设备不回写模板（principles·P175，<<<PAGE 649-655>>>）
- Hide SSID 几乎无安全价值（principles·P164，<<<PAGE 602-603>>>）
- MLO 频段取自 Allowed Band 且依赖 radio+EHT 开启；仅 Wi-Fi 7 AP（principles·P164/P44）

## 来源
OmniVista 2500 NMS 4.9R2 User Guide SSIDs 应用（<<<PAGE 861-874>>>）、WLAN Service (Device Config)（<<<PAGE 649-655>>>）、WLAN Service 无线参数（<<<PAGE 601-606>>>）。条目来源：principles P164/P165/P175/P179/P195/P196。
