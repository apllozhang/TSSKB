---
name: AOS 8 机箱冗余与虚拟机箱（CMM 主备/VC/VFL/分裂保护）
description: 需要在 OmniSwitch AOS 8 上管理双 CMM 冗余（flash-synchro/takeover）、组建 Virtual Chassis（手工/Auto-VFL/自动 Chassis ID）、配置 VFL/控制 VLAN、部署 VCSP/RCD 分裂保护、排查 VC 混合机型与参数限制时使用。
source_book: OmniSwitch AOS Release 8.10R4 Switch Management Guide
---

## R（触发场景）
- 双 CMM 机箱要做 certified 同步（flash-synchro）或计划内接管（takeover）
- 要把多台交换机组成 Virtual Chassis 单 IP 管理：手工组 VC 或 Auto-VFL 零接触建组
- 要配置 VFL 聚合链路、控制 VLAN、Master 选举优先级
- 要部署分裂保护（RCD 带外检测 / VCSP+helper）并演练分裂恢复
- VC 加新成员、混合机型入组、重复 chassis ID 排障

## I（核心理念）
VC 框架（F7，<<<PAGE 305-343>>>）：vcsetup.cfg（单机入组设置：Chassis ID/Group/priority/VFL）+ vcboot.cfg（VC 整体配置）双文件体系；Master/Slave 选举五准则（现任→priority→uptime→最小 ID→最小 MAC，P130）；VFL（10/40/100G 聚合、16 字节封装头）+ 控制 VLAN（默认 4094）+ IS-IS VC 专有协议维持拓扑。分裂双保险：RCD（EMP 带外周期通告，VFL 全断时 former Slave 关全部面板口防双 IP/MAC，P134）与 VCSP（经 helper 邻机专用 linkagg 转 PDU，master MAC 不匹配即进 protection state，P135/P136）。CMM 冗余（P85-P87）：running 配置自动同步，certified 需手动 flash-synchro；takeover 断开旧主管理会话。

## A1（决策框架）
1. **双 CMM 日常**：certify + 同步一步 `copy running certified flash-synchro`；计划内切换 `takeover`（先同步）（C23）
2. **组 VC 选路径**：默认 auto-VFL 端口直连即成（C47）；无默认端口机型 `auto-vf-link-port` 指定；手工模式走 configured-chassis-id + vf-link + convert-configuration（C46）
3. **VFL 设计**：仅 10/40/100G、同速不混、10GBase-T 不可入 VFL（X77）；线速场景注意 16 字节头开销可能丢包（X78/P141）
4. **分裂保护选型**：标准 VC 用 RCD（EMP 互连）；VFL 需经第三方链路时用 VCSP+helper（VC 与 helper 不能同机，X81）
5. **混合机型**：OS6900-X48C4E 入组需 `capability vfl-type mixed` 并重启 VC（X70）

## A2（操作步骤）
- **CMM 同步与接管**：`copy running certified flash-synchro`（或单独 `copy flash-synchro`）；`takeover`（C23，<<<PAGE 110-111>>>）
- **手工组 VC**：双侧 `virtual-chassis configured-chassis-id 1|2` → `virtual-chassis vf-link 0 create` + member-port → `ip interface local emp ...` → `write memory` → `convert-configuration to vc_dir` → `reload from vc_dir no rollback-timeout`；Master 上配 `ip interface master emp address 10.255.100.100`（C46，<<<PAGE 307, 328>>>）
- **Auto-VFL**：默认端口直连即成；`virtual-chassis auto-vf-link-port 1/1/25`；验证 `show virtual-chassis topology|consistency|vf-link member-port`（C47，<<<PAGE 304, 339>>>）
- **VCSP**：VC 侧 `virtual-chassis split-protection admin-state enable` + `split-protection linkagg`；helper 侧 `split-protection helper admin-state enable` + helper linkagg；guard-timer 控自动恢复（C48，<<<PAGE 341>>>）
- **受控下架成员**：`virtual-chassis shutdown`；跨机箱访问 `ssh-chassis`（<<<PAGE 327>>>）
- **write memory 拓扑确认**：拓扑元素缺失时确认 possible configuration purge（P140，<<<PAGE 313>>>）

## E（实证案例）
- CMM 同步与接管（C23，<<<PAGE 110-111>>>）
- 两台交换机手工组 VC 全流程（C46，<<<PAGE 307, 328>>>）
- Auto-VFL 快速组 VC 与验证（C47，<<<PAGE 304, 339>>>）
- VCSP 双侧配置（C48，<<<PAGE 341>>>）

## B（反例/坑）
- VC 不能混不同家族机型（OS6900 与 OS6860 不可同 VC）（X73）；混合机型需切 mixed 模式（X70）；部分 VC 参数运行时改不生效须重启（chassis ID/priority/控制 VLAN/hello interval）（X71）（<<<PAGE 319>>>）
- 新单元加入 VC 与现有目录/镜像/vcboot.cfg 不一致时可能重启两次（X72，<<<PAGE 319>>>）
- 重复 chassis ID 会被自动改号到 101-102，需经 EMP 本地修复（X74，<<<PAGE 324>>>）
- 组 ID 冲突不自检也不纠正，影响 RCD（X75，<<<PAGE 322>>>）
- VFL 上禁配 SFlow/ERP/UDLD/LLDP（X76）；VFL 限 10/40/100G 不混速、10GBase-T 不可入（X77）；线速可能丢包（X78）（<<<PAGE 322>>>）
- hello 间隔不匹配会降级为 Inconsistent/Misconfigured-Hello-Interval（X79，<<<PAGE 324>>>）
- EMP 直连不是推荐的分裂检测法（X80，<<<PAGE 312>>>）
- VCSP 与 helper 不能同机、helper 与 VC 不能同 Group ID（X81，<<<PAGE 340>>>）
- VC 分裂后配置改动不生效直到重启（X82，<<<PAGE 317>>>）
- takeover 断开旧主上的管理会话，需重连新主（X27，<<<PAGE 47>>>）
- Master 与 Slave 的 vcboot.cfg/镜像不一致时 Master 覆盖 Slave 并令其自动重启（P131，<<<PAGE 307>>>）

## 来源
OmniSwitch AOS 8.10R4 Switch Management Guide 第 4 章 CMM 冗余（<<<PAGE 99-111>>>）、第 13 章 Virtual Chassis（<<<PAGE 300-343>>>）。条目来源：cases C23/C46/C47/C48；principles P85-P92/P128-P141；counter-examples X27/X70-X82；frameworks F7。
