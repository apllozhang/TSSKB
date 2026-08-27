# TSSKB 2.x — ALE 技术培训内容平台

TSSKB 把 ALE 官方培训教材、产品手册和内部整理的知识单元构建为可检索的静态门户。2.x 的重点不只是“生成网页”，而是建立一条可校验、可复现、可回滚、可观测的内容供应链。

## 为什么仍然使用静态站点

这是一个内部只读知识库：读取量远高于写入量，也没有登录、收藏或学习进度等在线状态。静态生成能减少运行组件、攻击面和维护成本。平台化能力放在内容契约、构建、测试、搜索、发布和治理层，不为展示技术而引入数据库或微服务。

## 快速开始

建议使用 Python 3.11–3.12：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev,deploy]"
tsskb validate --strict
tsskb build --output dist/site --full --strict
tsskb serve --site dist/site --port 8000
```

如果只需兼容旧命令，也可运行 `python build_site.py`。它调用同一条新流水线，产物位于 `dist/site`，不会覆盖仓库中的旧 `site/` 基线。

## 常用命令

```powershell
# 内容、来源目录和跨文件引用契约
tsskb validate --strict

# 完整构建；任何断链、缺图或搜索容量超限都会失败
tsskb build --output dist/site --full --strict

# 仅重新渲染输入摘要发生变化的课程
tsskb build --output dist/site --incremental --strict

# 查看页面、文件、站点大小和搜索容量
tsskb metrics --site dist/site --environment prod --enforce-budget

# 测试、代码规范和类型检查
pytest --cov=src/tsskb --cov-report=term-missing
ruff check .
mypy src

# 只展示发布/回滚动作，不连接服务器
tsskb deploy --environment staging --dry-run
tsskb rollback --environment staging --dry-run
```

## 目录说明

```text
content/       课程、分类、学习路径、重定向和环境配置
schemas/       与强类型模型同步的 JSON Schema
books/         Markdown 内容和课程图片来源
templates/     自动转义的 Jinja2 页面模板
static/        ALE 品牌 CSS、独立 JavaScript 和 PBG 场景素材
src/tsskb/     内容、构建、搜索、验证、发布和可观测性代码
tests/         单元、契约和集成测试
ops/           Nginx、健康检查和运行手册
docs/          架构、容量、SLO、ADR 和面试讲解
dist/site/     构建产物，不作为手写源码
site/          1.x 黄金基线；迁移验收期间保留
```

原来的单文件生成器保存在 `tools/legacy/build_site_v1.py`，只用于迁移审计，不进入 2.x 构建路径。

## 内容变更流程

1. 修改 `content/*.json` 或 `books/**`，不改 Python 课程清单。
2. 运行 `tsskb validate --strict`，先得到精确到文件和字段的错误。
3. 运行测试和完整构建。
4. 提交 Pull Request；CI 自动执行 lint、类型检查、测试、构建、断链、容量和可复现性检查。
5. 通过 staging 健康检查后再晋级生产。

历史 URL 不直接删除。合并或拆分内容时，先在 `content/redirects.json` 建立显式迁移关系。

## 发布安全边界

- `content/environments/*.json` 默认禁用远端发布。
- SSH 使用已知主机密钥，拒绝未知主机，不使用 `AutoAddPolicy`。
- 每次上传到新的 `releases/<release-id>`，核验 manifest 后原子切换 `current`。
- 健康检查失败时自动恢复上一版本。
- 发布密钥/密码只从 agent、密钥文件或环境变量读取，不写入仓库。
- 本仓库不执行任何数据库操作。

详细设计见 [架构](docs/architecture.md)、[容量模型](docs/capacity.md)、[SLO](docs/slo.md)、[发布运行手册](ops/runbooks/release.md) 和 [面试讲解](docs/interview-guide.md)。

> 内容仅供内部学习使用；教材版权归 ALE Training Services 所有，请勿外传或用于商业用途。
