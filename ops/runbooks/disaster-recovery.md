# 灾难恢复基线

## 可恢复对象

- Git 仓库：内容、模板、静态资源、配置、代码和运行手册；
- CI artifact：通过质量门禁的完整 `dist/site`；
- 服务器 release 目录：最近多个不可变版本；
- Nginx/systemd 配置：位于 `ops/`，由基础设施流程安装。

## 主机重建

1. 准备受支持的 Linux 主机与 Nginx；
2. 安装 `ops/nginx/tsskb.conf` 并先执行 `nginx -t`；
3. 创建 remote root 与 release 操作账号，按最小权限授权；
4. 从 CI 下载最后一个已知健康 artifact；
5. 上传为新的不可变 release，核验 manifest；
6. 创建 `current` 软链接并启动 Nginx；
7. 执行标准四项健康检查；
8. 恢复探针和日志采集。

## RPO / RTO 建议

- 内容 RPO：0（以已合并 Git 提交为准）；
- Release RPO：最后一个通过 CI 的 artifact；
- 单主机重建 RTO：目标 60 分钟，需通过季度演练验证；
- 单次错误发布恢复：目标 5 分钟内，原子回滚通常应在秒级完成。

这些是设计目标，未完成真实演练前不能声明已经达到。
