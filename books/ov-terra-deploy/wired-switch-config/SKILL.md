---
name: 有线业务配置下发
description: 当需要对已纳管交换机做 CLI 模板化配置（Initial/Incremental）、建 VLAN/IP Interface（L2/L3）、配置有线客户端 MAC 认证或 Golden Configuration 合规审计时使用。
source_book: DT00XTE317 OmniVista Cirrus/Terra Deployment and Configuration
---

## R（触发场景）
- 交换机批量上线，需要标准化初始配置（Initial 模板 + Value Mappings）
- 需要给特定站点/单机追加配置（Incremental 模板）
- 需要建 VLAN、IP Interface，或给有线客户端做 MAC 认证
- 需要交换机配置合规审计（Golden Configuration）

## I（核心理念）
有线配置下发有两条模型：①模板化——Initial 模板在设备变 managed 前应用，Incremental 模板对已纳管交换机增量应用，变量经 Value Mappings 映射；②对象化——VLAN Manager 管 L2、IP Interface 管 L3，均以"创建对象 + 选择交换机"的方式下发。Golden Configuration 提供基准备份与偏离审计。

## A1（行动框架）
1. **CLI 模板化配置**：
   - Initial 模板：在设备 onboarding 时的 "Initial Configuration" 应用（设备变 managed 前）（<<<PAGE 174>>>）
   - Value Mappings：将模板变量映射到值（<<<PAGE 175>>>）
   - Incremental 模板：Save and Assign 或 Actions > Assign → Step1 选站点/单机 → Step2 选 Value mapping（<<<PAGE 176>>><<<PAGE 177>>><<<PAGE 178>>><<<PAGE 179>>><<<PAGE 180>>>）
2. **L2：创建 VLAN**（VLAN Manager）：VLAN IDs、Default VLAN ID、Default Ports Template（VLAN 在默认端口 untagged）、Q Tagged Ports Template、Switch selection；可顺带配 Spanning Tree（Summary/Bridge/Port）与 IP Router（<<<PAGE 182>>><<<PAGE 183>>><<<PAGE 184>>>）
3. **L3：创建 IP Interface**：IP interface name、IP Address/Mask、Device type（Unbound/EMP/VLAN/Tunnel…）、VRF IP、Enable/Disable（Admin State、IP Forward、Local Proxy ARP、Primary Interface）、Switch selection（<<<PAGE 187>>><<<PAGE 188>>>）
4. **有线客户端 MAC 认证四步**（路径 Configure > Network Access > Unified Access / UPAM-NAC / Accounts）（<<<PAGE 451>>>~<<<PAGE 456>>>）：
   - [PRE] 预配 ARP_DEFAULT / ARP_PASS
   - ① AAA Server Profile（UPAMRadiusServer, MAC）
   - ② Access Auth Profile（MAC 方法 + AAA Profile + 默认 ARP + AP Group + 端口 Eth1）
   - ③ Access Policy（Auth Type=MAC, Local-Database, ARP_PASS，无重定向）
   - ④ 本地数据库建 MAC 条目（Company Property）
5. **Golden Configuration 合规审计**：以备份作为基准，交换机配置意外变更可用于恢复；Status 为 Compliant 表示无偏离；支持周期审计与即时审计（<<<PAGE 195>>><<<PAGE 196>>><<<PAGE 351>>>）

## A2（进阶应用）
- 模板 + Value Mappings 实现多站点差异化：一套模板，每站点一套映射值（<<<PAGE 175>>>）。
- IoT 设备识别（Device Profiling）：基于 MAC OUI 与 DHCP 指纹（option 55 参数请求列表 / option 60 厂商标识）分类，再按设备类别映射 ARP 执行 Enforcement（<<<PAGE 464>>><<<PAGE 465>>>）。
- UNP（Unified Network Policy）：OmniSwitch 上的统一网络策略，可在有线客户端/port 视图应用（<<<PAGE 193>>><<<PAGE 313>>>）。

## E（实证案例）
- **案例 1**：多站点 rollout，同一份 Initial 模板配多套 Value Mappings，onboarding 时自动注入站点差异参数（<<<PAGE 174>>><<<PAGE 175>>>）。
- **案例 2**：打印机等哑终端接交换机 Eth1 需要认证，走 UPAM 内置 MAC 认证服务器 + 本地 MAC 数据库（ARP_PASS），四步完成（<<<PAGE 451>>>~<<<PAGE 456>>>）。

## B（边界与陷阱）
- Initial 与 Incremental 应用时机不同：Initial 只在设备变 managed 前的 onboarding 环节生效，错过就要用 Incremental（<<<PAGE 174>>>）。
- 审计基准更新要及时：Golden Configuration 偏离即 Non-Compliant，计划内变更后需刷新基准（<<<PAGE 195>>><<<PAGE 196>>>）。

## 来源
- cases·CLI 模板化配置 Initial/Incremental（<<<PAGE 174>>>~<<<PAGE 180>>>）
- cases·VLAN Manager 创建 VLAN（<<<PAGE 182>>><<<PAGE 183>>><<<PAGE 184>>>）
- cases·创建 IP Interface（<<<PAGE 187>>><<<PAGE 188>>>）
- frameworks·有线客户端 MAC 认证四步配置流程（<<<PAGE 451>>>~<<<PAGE 456>>>）
- principles·Golden Configuration 合规检查（<<<PAGE 195>>><<<PAGE 196>>><<<PAGE 351>>>）
- principles·IoT 设备识别原理（<<<PAGE 464>>><<<PAGE 465>>>）
- glossary·UNP（<<<PAGE 193>>><<<PAGE 313>>>）
