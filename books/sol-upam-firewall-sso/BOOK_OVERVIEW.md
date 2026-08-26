# OmniVista UPAM 防火墙 SSO 集成课程书

## 定位

本书由两份 ALE 应用笔记蒸馏而成，覆盖 OmniVista UPAM 与第三方下一代防火墙的单点登录（SSO）集成：

| 源文档 | 篇幅 | 集成对象 | 推送机制 |
|---|---|---|---|
| OmniVista 2500 UPAM and Fortinet Single Sign-On Application Note（2021-03） | 17 页 | Fortinet FortiGate / FortiAuthenticator（FSSO/RSSO） | RADIUS Accounting（UDP 1813，网络设备直发） |
| OmniVista UPAM and Palo Alto Networks User-ID Integration Guide（2020-07） | 15 页 | Palo Alto PAN 防火墙（User-ID） | Syslog（UDP 514，UPAM 发送） |

两份笔记共享同一套叙事骨架（零信任动因 → UPAM 简介 → AD 路线 vs BYOD/IoT 路线 → 机制 → 两侧分步配置 → 验证 → 结论），区别只在防火墙侧的身份推送通道与配置细节，适合对照学习。

## 单元导航

| 单元 | 内容 | 主要来源与页码 |
|---|---|---|
| [upamfw-sso-overview](skills/upamfw-sso-overview.html) | SSO 机制总览：零信任动因、UPAM 能力、AD 路线与 BYOD/IoT 路线分界、两种推送机制对比 | 两份笔记 p3-5 |
| [upamfw-fortinet-arch](skills/upamfw-fortinet-arch.html) | Fortinet 集成架构：RADIUS Accounting 直发、FortiAuthenticator 汇聚、interim interval、任务清单 | Fortinet 笔记 p4-7、p13 |
| [upamfw-fortinet-config](skills/upamfw-fortinet-config.html) | Fortinet 集成配置：OV 侧 4 步 + FortiGate 侧 7 步全菜单路径与验证命令 | Fortinet 笔记 p5-16 |
| [upamfw-pan-arch](skills/upamfw-pan-arch.html) | PAN 集成架构：User-ID、syslog 字段解析、Accounting-only 过滤与 45 分钟登出局限 | PAN 笔记 p3-6、p12 |
| [upamfw-pan-config](skills/upamfw-pan-config.html) | PAN 集成配置：OV 侧 4 步 + PAN 侧 7 步全菜单路径与验证命令 | PAN 笔记 p6-14 |

## 建议学习路径

1. 先读 upamfw-sso-overview 建立全局图景与路线判断
2. 按目标防火墙二选一：Fortinet → arch → config；PAN → arch → config
3. 动手前通读对应 config 单元的 B（限制与坑）一节
