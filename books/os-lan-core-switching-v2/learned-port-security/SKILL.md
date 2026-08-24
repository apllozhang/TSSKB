---
name: Learned Port Security 端口安全
description: 需要限制接入端口的 MAC 学习数量并处置违例（过滤/关停/静态化锁定设备）时使用本技能。
source_book: DT00XTE216 OmniSwitch LAN Core Switching Ed15
---

## R（触发场景）
- 接入端口要锁定为"一台终端一个口"，防止私接交换机/AP
- 出现非授权 MAC 需要自动过滤或直接关闭端口
- 端口接了交换机导致 LPS 误过滤 LLDP/STP/IP 多 MAC，需要排查

## I（核心理念）
LPS 通过"限学多少 MAC（maximum）+ 学习窗口 + 违例动作（restrict 只拦违例源 / shutdown 整口）"三重控制接入安全，convert-to-static 把当前学到的 MAC 固化实现设备绑定。学习期被截获的报文由 pkt-relay 重注入，正常业务不中断；违例默认 300s 自动恢复、最多自动恢复 10 次。

## A1（行动框架）
1. 最小模板一次成型：`port-security port 1/1/1 admin-state enable / maximum 1 / violation shutdown / convert-to-static enable`（<<<PAGE 193>>>）
2. 验证：`show port-security`（默认 maximum 1、violation RESTRICT、max-filtering 5，最多可学 100 MAC/口）（<<<PAGE 207>>>）
3. 固化设备：先让流量把 MAC 学上来，再 `port-security port 1/1/8 convert-to-static`（<<<PAGE 208>>>）
4. 违例处置：`violation shutdown` + `max-filtering 0` → 再学即端口关闭；`show violation` 查看，`violation port 1/1/8 recovery-time 30` 修改恢复时间（默认 300），`clear violation port 1/1/8` 手工恢复（<<<PAGE 209>>>-<<<PAGE 210>>>）

## A2（进阶应用）
- 三阶段演进实验路径：限 1 MAC 观察 filtering → convert-to-static 固定 → shutdown+max-filtering 0 硬关（<<<PAGE 207>>>-<<<PAGE 210>>>）
- 对端是交换机时：LLDP/STP 用一个 MAC、L3 用另一个 MAC，多个源 MAC 会挤占学习额度导致误过滤——先关协议再 flush mac-learning 后重学（<<<PAGE 206>>>）
- 命令权限纳入 security 域管理（同 MACsec，见 p82）

## E（实证案例）
- C-16 三阶段实验：restrict 过滤 → convert-to-static 固化 → shutdown 关闭 + recovery-time 调整与 clear violation 手工恢复，含关 STP/LLDP 排除干扰（<<<PAGE 207>>>-<<<PAGE 210>>>）
- C-17 标准绑定模板（maximum 1 + shutdown + convert-to-static）（<<<PAGE 193>>>）

## B（边界与陷阱）
- LPS 不支持链路聚合端口（Not supported on Link Aggregate ports）（<<<PAGE 190>>>）
- convert-to-static 必须在设备 MAC 已学到之后执行，先发流量再固化（<<<PAGE 208>>>）
- 对端交换机自身多 MAC（LLDP/STP/L3 各一个）会触发 restrict 误过滤（<<<PAGE 206>>>-<<<PAGE 207>>>）

## 来源
- framework·F-09 LPS 配置四步法与违例决策（<<<PAGE 190>>>-<<<PAGE 193>>>）
- principle·P-32 学习控制与违例（<<<PAGE 190>>>、<<<PAGE 191>>>、<<<PAGE 207>>>）
- principle·P-33 自动恢复与 pkt-relay（<<<PAGE 196>>>、<<<PAGE 209>>>）
- case·C-16/C-17；counter·X-11/X-12
