# SLO、指标与告警基线

## 服务目标

| SLI | SLO | 测量方式 |
|---|---|---|
| 生产可用性 | 月度 ≥ 99.9% | Nginx access log + 外部 HTTP 探针 |
| 首页 TTFB | 内网 P95 < 500 ms | access log `$request_time` |
| 搜索查询 | 索引就绪后 P95 < 100 ms | 浏览器 Performance API / RUM 接入点 |
| 构建成功率 | 月度 ≥ 99% | CI workflow 结果 |
| 发布成功率 | 月度 ≥ 99% | `deploy.completed` / `deploy.*` 结构化事件 |
| 内容完整性 | 断链、缺图、失效锚点 = 0 | 每次严格构建的 SiteValidator |
| 回滚能力 | 失败发布 5 分钟内恢复 | 发布日志与演练记录 |

99.9% 月可用性约对应 43 分钟错误预算。静态站故障通常来自发布、Nginx/主机或网络，而不是应用代码；告警必须能够区分三者。

## 构建指标

`_meta/build-metrics.json` 和 JSON 日志至少包含 build ID、模式、耗时、变化课程数、页面数、引用数、总文件大小、搜索容量和异常类型。时间戳不进入确定性 manifest，避免破坏可复现比较。

## 发布指标

关键事件为 `deploy.upload.started`、`deploy.completed`、`deploy.auto_rollback` 和 `rollback.completed`。每个事件包含环境、release ID 和必要的前后版本，不包含密码、私钥或完整敏感命令。

## 告警分级

- P1：生产首页连续 5 分钟不可用，立即回滚/切流；
- P2：搜索 manifest 或代表性课程 5 分钟不可用，15 分钟内处理；
- P2：发布触发自动回滚；
- P3：CI 容量预算、断链或 schema 门禁失败；
- P3：TTFB P95 连续 30 分钟超过 500 ms。

## 演练

每季度至少执行：

1. staging 发布一个健康版本；
2. 人为让代表性健康检查失败；
3. 观察自动恢复上一 `current`；
4. 手工执行指定 release rollback；
5. 记录恢复时间、日志完整性和改进行动。

生产发布未启用时，只执行 dry-run 和本地 transport mock，不伪造线上演练结果。
