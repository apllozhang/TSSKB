# 发布与回滚运行手册

## 前置条件

- CI 中测试、完整构建、断链和容量门禁全部通过；
- staging/prod 环境文件经评审后显式设置 `deploy.enabled=true`；
- 目标主机公钥已写入操作账号的 known_hosts；
- Nginx `root` 指向 `<remote_root>/current`；
- 凭据通过 SSH agent、`TSSKB_DEPLOY_KEY` 或 `TSSKB_DEPLOY_PASSWORD` 提供。

## 发布步骤

```powershell
tsskb build --output dist/site --environment staging --full --strict
tsskb deploy --site dist/site --environment staging --dry-run
tsskb deploy --site dist/site --environment staging
```

确认 staging 首页、搜索、代表课程、移动端和控制台无错误后，使用同一 CI artifact 晋级生产，禁止重新构建一个“看似相同”的产物。

```powershell
tsskb deploy --site dist/site --environment prod --dry-run
tsskb deploy --site dist/site --environment prod
```

## 自动回滚

切换后会检查：首页、`_meta/release-manifest.json` 中的目标 `release_id`、`search/manifest.json`、代表性课程和品牌 Logo。任何一步失败都会恢复 previous 软链接并记录 `deploy.auto_rollback`。

## 手工回滚

```powershell
tsskb rollback --environment prod --dry-run
tsskb rollback --environment prod

# 指定已知健康版本
tsskb rollback --environment prod --target <16位release-id>
```

回滚目标会执行与发布相同的健康检查；如果目标不健康，命令会恢复回滚前的 `current`，并记录 `rollback.compensated` 事件。

## 禁止事项

- 不在发布前 `rm -rf` 当前站点；
- 不直接修改 release 目录中的文件；
- 不使用 `AutoAddPolicy` 接受未知 SSH 主机；
- 不把生产密码、私钥或 known_hosts 提交到 Git；
- 不在未通过 staging 时跳过晋级流程。
