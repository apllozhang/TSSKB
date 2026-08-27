# 故障处理运行手册

## 首页不可用

1. 从其他内网节点请求 `/healthz` 和 `/`，区分主机/Nginx与网络故障；
2. 查看 Nginx error log 和最近 `current` 指向；
3. 如果故障紧随发布，立即回滚上一 release；
4. 若上一 release 也失败，检查 Nginx root、磁盘、权限和网络；
5. 恢复后记录时间线、影响范围、恢复时长和防复发行动。

## 搜索不可用但页面正常

1. 请求 `/search/manifest.json` 和 manifest 中最大分片；
2. 检查 Content-Type、缓存和 CSP worker-src；
3. 浏览器控制台确认 Worker/JSON 错误；
4. 若新 release 引入问题，回滚；
5. 在 CI 增加能够复现该错误的测试。

## 单页或图片 404

1. 在 `_meta/manifest.json` 确认文件是否属于 release；
2. 本地运行 `tsskb validate --site dist/site --strict`；
3. 历史链接改名时增加 `content/redirects.json`，不要静默删除；
4. 图片应来自 `static/assets` 或对应 book 的 `images` 目录。

## 磁盘空间

发布主流程不删除历史版本。磁盘告警时先列出 release ID、日期、当前/上一版本和大小；保留当前与至少一个已知健康版本。历史清理必须独立审批并记录精确目标。
