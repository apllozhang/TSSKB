# TSSKB — ALE Networking 技术培训知识库

Technical Support Knowledge Base：ALE 售后培训教材蒸馏学习站。

## 内容

- `site/` — 静态学习门户（可直接部署任意 HTTP 服务器）
  - 门户封面：按 售前/售后/WLAN/LAN/管理/安全/认证 分类
  - 课程子站：
    - DT00XTE317 · OmniVista Cirrus / Terra 部署与配置（10 知识单元）
    - DT00XTE220 · OmniSwitch LAN R8 Bootcamp Ed23（12 知识单元）
    - DT00XTE216 · OmniSwitch LAN R8 Core Switching Ed15（11 知识单元）
  - 每单元含：原文引用 / 方法论骨架 / 案例 / 触发场景 / 可执行步骤 / 边界陷阱
- `build_site.py` — 门户构建脚本（新增课程只需在 COURSES 列表加一条）
- `deploy.py` — 部署脚本（示例：SSH/SFTP 到内网服务器）

## 本地运行

```bash
cd site && python -m http.server 8000
```

## 生产部署

任意静态服务器托管 `site/` 目录即可（示例：`python3 -m http.server 8899 --bind 0.0.0.0`）。

## 内容生成方式

由 cangjie-skill 流水线从 ALE 官方培训教材蒸馏生成，仅供内部学习使用；教材版权归 ALE Training Services 所有，请勿外传或用于商业用途。
