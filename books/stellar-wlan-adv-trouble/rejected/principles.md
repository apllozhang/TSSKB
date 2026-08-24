# 淘汰条目 · principles（原则/参数）

> 阶段 1.5 三重验证结果：候选 26 条（p01-p26），**通过 26 条，淘汰 0 条**。
> 已通过的条目及理由见 verified.md 第二节。

## 淘汰清单

无。

## 曾重点评估的边界条目（最终保留，理由备案）

- **p22 网络连通性四命令**（ifconfig/route/ping/traceroute）：V3 曾存疑（单项命令属通用 Linux 网工知识）。保留理由：命令组合嵌在 Stellar 语境中（ssudo 前缀、br-wan 有线桥接口、"逐个测网关/NTP/DHCP/DNS/防火墙/OmniVista"），是教材网络层排障的标准路径，未达"重启试试"级常识线。
- **p10 CPU/内存/进程诊断**（R/S/X/Z）：V3 曾存疑（进程状态判定属 Linux 通用知识）。保留理由：判据作用于 Stellar AP 的 top/ps 输出并规定"开票附进程列表"的上报动作；另注意与 ce17/ce18 重叠，阶段 2 合并即可（见 verified.md 附注 B）。
- **p07 support 账号 aos2016**：V3 曾存疑（默认密码仅适用于训练/实验室环境，生产多为自定义）。保留理由：教材明示 Enterprise 模式需在 AP Group 激活 SSH 并自定义密码，条目同时覆盖了该生产路径，登录入口信息（support 账号）本身稳定有效。
