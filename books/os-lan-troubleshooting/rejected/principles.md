# rejected/principles.md · 淘汰条目（1 条）

## p11 终端侧排障命令五件套（ipconfig / ping / arp -a / nslookup / route print）

- source_chapter: p123
- V1 原文真实性：**通过**——"On client side: ... arp -a ... nslookup ... route print" 在 fulltext 命中。
- V2 可操作价值：**边缘通过**——命令可用，但属 Windows 通用网维常识。
- V3 独特性：**不通过**——五个命令与"先排本机再怪网络"的顺序原则均为通用常识，无 AOS/ALE 特有增量；同类信息在 f07（二层排障配置错误小节）已作为流程一环覆盖，单独成条价值低。
- 处置：淘汰。若后续阶段需要客户端侧检查项，引用 f07 的 summary 即可。
