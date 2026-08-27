# ADR-005：迁移期保留旧产物，新产物不入库

- 状态：Accepted for migration
- 日期：2026-08-27

## 背景

仓库中的 `site/` 是 1.x 黄金基线，但生成脚本与产物曾不同步。直接删除会失去视觉/URL 对照证据。

## 决策

迁移期间不删除 `site/`；2.x 只写 `dist/site`，并由 CI 上传 artifact。原生成器移动到 `tools/legacy`。8 个历史 URL 通过显式重定向保留。

## 后果

- 可并行比较新旧页面，主分支历史不丢失；
- 仓库暂时保留一份旧生成产物；
- 完成 staging/production 验收后，再另开 ADR 决定是否停止跟踪 `site/`。
