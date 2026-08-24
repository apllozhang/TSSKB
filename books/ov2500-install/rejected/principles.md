# rejected · principles（阶段 1.5 淘汰）

> 候选 31 条，通过 30 条，淘汰 1 条。

- id: p08
  title: 首次部署 VA 时不要提前添加新磁盘
  type: principle
  source_chapter: "p10"
  source_quote: |
    "When deploying the OmniVista VA for the first time, do not add the new disks in the hypervisor until after OmniVista is configured and rebooted."
  summary: |
    首次部署 OmniVista VA 时，扩展用的新磁盘必须等 OmniVista 完成初始配置并重启之后再从 Hypervisor 添加，否则可能影响初始安装流程。
  tags: [deployment, disk, first-install]

  reject_reason: V3 独特性不通过
  reject_detail: 与 ce18 逐字同源：同一引文（'When deploying the OmniVista VA for the first time, do not add the new disks...'，均在 p10）、同一规则（首次部署不得提前加盘）、tags 重合（deployment/disk/first-install）。两条规定同一行为，入库会造成知识库重复条目。按流水线规则保留反例框架的 ce18（其 summary 另含三平台先配 NIC 再继续的补充，p18/p24/p34），淘汰本条。V1/V2 本身通过（引文真实、内容可操作）。
