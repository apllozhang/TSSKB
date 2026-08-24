---
name: ov2500-known-issues
description: 何时用：OV 2500 环境出现异常现象时，按模块与症状检索 4.9R2 官方已知问题与 workaround。
source_book: OV2500 4.9R2 Release Notes
---

# OV 2500 4.9R2 已知问题排障库（73 条）

## R · 原文引用

> "This document details known problems and limitations in OmniVista 2500 NMS 4.9R2 (OV 2500 NMS 4.9R2), and workarounds are included." (p5)

> "Performing a 'Save to Running' action on a large number of APs in the Discovery application takes a long time (it takes approximately 10 seconds for each AP). Workaround: No workaround at this time. PR# OVE-2264" (p24)

> "OmniVista became unavailable to web clients, displaying the following error message on the browser: 'OmniVista Error Fail to get current user'. Workaround: Restart ovclient or tomcat service. PR# OVE-2220" (p36)

> "UPAM authentication does not work if you are using an external LDAP with an Encryption Password (e.g., MD5, SHA) configured for the user. Workaround: ... use a plain text password. PR# OVE-818" (p29)

## I · 方法论骨架

排障检索法：先按"故障模块"定位分组，再按"症状关键词"查下表，命中后执行 workaround 或按"判读口径"做预期管理。每条含 PR 号，可回溯官方原文。

判读三原则：
1. **先查版本组合**：大量问题与 AOS/AWOS/OV 版本组合绑定（LLDP 链路不显示、IPv6 策略、DPI 报错）。
2. **区分 bug 与边界**：不少条目是功能边界（Locator 不支持 OS2200、门户不能 HTML 定制），改方案而非等修复。
3. **No workaround 也有价值**：用于变更窗口估算、监控告警降噪、报表数据预期。

## A1 · 书中案例（按模块 13 组全量索引）

**① AP 注册（p24）**
| 症状 | 处置 | id |
|---|---|---|
| IE11 打不开 AP Web 管理 | 换 Chrome/Firefox/Edge | ce01 |
| 同名 Key File 不能再上传 | 换文件名 | ce02 |

**② Discovery（p24）**
| AP 恢复 Up 后 Reason Down 字段不清空 | 判读口径：Status=Up 就忽略该字段 | ce03 |
| 大批 AP Save to Running 极慢（约 10 秒/台） | 无 workaround，变更窗口按此估算/分批 | ce04 |
| 配置/升级无理由失败 | 先查设备 NaaS 许可（降级模式不提示原因） | ce05 |

**③ Locator（p25）**：OS2200 上无法定位终端 = 功能边界，不规划该需求 (ce06)。

**④ mDNS（p25-26）**
| Chromecast 跨 VLAN 不可见 | 同 VLAN + mDNS Edge AP；AOS 8.7R2 修复 | ce07 |
| 用户先入网、后配 Responder/Edge，服务不共享 | 先配后放用户；错了让用户重新共享 | ce08 |
| 禁用 mDNS 后 AirPlay 仍续传 | 预期行为，验证禁用需客户端重连 | ce09 |
| AP1351/1301 仅 Eth1 不能跑 mDNS | 用 Eth0 或 Eth0+Eth1 聚合 | ce10 |

**⑤ PolicyView（p26）**
| OS6900-Q32 专家模式无 Port Type | 策略设计避开 | ce11 |
| Send Trap 属性策略推不下去（4.2.2 GA 升级遗留） | 新建策略列表替换 | ce12 |

**⑥ Resource Manager（p26-27）**
| OS6900 8.3.1 备份丢 SSH Key/用户表 | 恢复后手工补 | ce13 |
| U-Boot 文件名缺点号升级失败 | 改名 u-boot.5.2.R03.3.tar.gz | ce14 |
| OS9907/9912 U-Boot 升级"不工作" | Denverton（CMM2/CNI-U20）与 Rangeley（CMM1/其余 NI）分两次、各用对应文件 | ce15 |

**⑦ Topology（p27）**
| ERP-RPL 链路 AMAP 条目不显示 | ERPv2 场景改用 LLDP | ce16 |
| 多选 >2 台不显示 SPT 链路 | 一次只选两台 | ce17 |
| AOS 8.8R1 × AWOS 4.0.4 LLDP 链路不显示 | AOS 8.8R2 修复，先核版本组合 | ce18 |

**⑧ Unified Access（p28-29）**
| OS6900-Q32/X72 Device Config 显示错误 | 以设备 CLI 实际配置为准 | ce19 |
| AOS 8.2.1 看不到 Access Role Profile | 到设备侧查看 | ce20 |
| Reflexive 选项致 Drop 策略漏丢包 | 不要开 Reflexive（安全放行漏洞） | ce21 |
| OS6465/6560 策略列表不支持源 MAC 条件 | 规则里去掉源 MAC | ce22 |
| 认证失败后 ARP 授权残留 | AP 侧升 AWOS 5.0.1+；交换机无解（安全影响） | ce23 |
| 拆 VC 后策略选择器不显示设备 | 删 /flash/network/vcpolicy.cfg 并重启 | ce24 |

**⑨ UPAM（p29-31）**
| HSTS 站点二次访问不重定向到门户 | 预期行为；清缓存可恢复一次；Chrome 必现 | ce25 |
| 外部 LDAP 加密密码致认证失败 | LDAP 用户密码用明文 | ce26 |
| 门户页不支持完整 HTML 定制 | 方案阶段排除 | ce27 |
| 有线 CP 认证失败 | 客户网络需 DNS 且解析到 OV 辅助 IP（UPAM 地址）；无线无此要求 | ce28 |
| Windows LDAP 不支持 | 用 OpenLDAP 或 Windows Server AD | ce29 |
| LDAPS 停服带崩 freeradius 且无法重启 | 恢复 LDAP 或在 UPAM Settings 禁用 LDAP/AD | ce30 |
| Guest 账户过期仍显示 Enabled | 设过期删除策略（立即或 1-90 天） | ce31 |
| WiFi4EU 有效期 24h 合规 | 把门户有效期从默认 30 天改为 24 小时 | ce32 |
| TLS RADIUS 无端口字段 | TLS 端口填在 Authentication Port（默认 2083） | ce33 |

**⑩ VMM（p31-32）**
| VM 模板被当虚拟设备计数 | 设计使然，统计/许可核算时排除 | ce35 |
| 多网卡 VM 显示多行 | 许可按 UUID 只计一台，纯显示冗余 | ce36 |
| 删 LAG 默认 UNP 后 VLAN 通知延迟 | MAC 表回填慢，"短暂失联自愈"判读 | ce37 |

**⑪ WCF（p32-33）**
| 手机 App 流量绕过 WCF | 无解，方案须算 App 豁免 | ce38 |
| 代理上网使 WCF 失效 | 部署前提：客户端 DNS 直连 | ce39 |
| HA 升级+failover 后 WCF 失效 | 重启 WMA 服务 | ce40 |

**⑫ WLAN（p33-34）**
| GRE 隧道档案不生效 | 组合规则：合法=ID>0+Entropy 开、ID=0+关；非法=ID>0+关、ID=0+开 | ce41 |
| 2 万 rogue AP 页面超时 | WMA 查询 65s > 超时 50s，大规模下该页面不可靠 | ce42 |
| AP1201BG 不支持 RF Profile | BLE 网关，下发时排除 | ce43 |
| 备节点 WMA 显示 Not Responding | 无影响，转主自动恢复，勿误判 | ce44 |
| 无线客户端摘要信息不全 | 浏览器时区与服务器对齐 | ce45 |

**⑬ 其他/系统（p34-39）**
| OS6450 U-Boot 显示 NA | 硬件限制，盘点基线须知 | ce46 |
| Win2012R2 IE 按 IP 本地访问失败 | hosts 映射 localhost，用 localhost 访问 | ce47 |
| SNMP community 含撇号非法 | 凭据生成时过滤 ' | ce48 |
| 主机名上限 15 字符 | 命名规范约束 | ce49 |
| 添加 Hyper-V 报错 | 放通 VMM 端口（135+49152-65535）→ 仍失败按附录 A 启 DCOM | ce50 |
| 带口令私钥证书致 Nginx 不启动 | 证书 SOP：私钥不得加密，换证书重导并重启 | ce52 |
| 改系统端口后代理断网 | Preferences – System Settings – Proxy 改回代理端口 | ce53 |
| Web 报 Fail to get current user | 重启 ovclient 或 tomcat | ce54 |
| AOS 6.4.6 推不了 IPv6 策略 | 需 6.7.2R7+ 或 8.6R2+，先清点版本 | ce55 |
| Firefox 大列表卡顿 | 用 Chrome/Edge；Firefox 调 about:config（responseBodyLimit=0、max_script_run_time=20） | ce57 |
| DRBD stdin/stdout 警告 / cockpit.socket 提示 | 均可忽略，告警降噪 | ce58, ce59 |
| 8.10R3 下发 DPI 档案报错 | 存量档案升级后仍工作；新配置等修复 | ce68 |

（另见功能矩阵硬限制 ce70-73，归 `ov2500-49r2-features-compat`；高危项 ce51/ce63/ce65/ce66/ce67 归 `ov2500-danger-traps`。）

## A2 · 触发场景（含与相邻 skill 的区分）

- 触发：任一 OV 2500 环境故障工单、验收异常、监控误报判读、方案能力核查。
- 区分：升级方案规划（还没出故障）→ `ov2500-upgrade-deploy`；会造成停机/变砖/大面积锁死的风险 → 先查 `ov2500-danger-traps`；纯版本兼容问题 → `ov2500-49r2-features-compat`。

## E · 可执行步骤

1. 用一句话描述症状（模块 + 现象 + 版本），在上表分组内关键词检索。
2. 命中后按"处置"列执行；No workaround 条目转为预期管理（估算窗口/降噪/改方案）。
3. 处置前记录 PR 号，必要时用 PR 号向 ALE TAC 交叉确认修复版本。
4. 版本组合类问题（ce18/ce55/ce68）先做全网版本清点再动配置。
5. 未命中时按通用路径排：Watchdog 是否启动（p18）→ 浏览器是否受支持（p18）→ 时区/代理/DNS 等环境因素（ce45/ce39/ce28）。

## B · 边界与陷阱

- 本表基于 4.9R2 Release Notes；条目含更老版本遗留（ce12/ce34/ce47/ce56），在 4.7R1→4.9R2 升级路径内仍可命中。
- 多条"显示问题"实际是功能边界或设计行为（ce03/ce31/ce35/ce36），不要当 bug 反复报修。
- ce21（Reflexive 漏丢包）、ce23（授权残留）有安全影响，处置优先级高于普通显示类问题。

---
来源条目: ce01-ce62, ce68（共 63 条排障条目）；关联 ce34, ce70-73 详见 features-compat，ce51/ce63/ce65/ce66/ce67 详见 danger-traps；g06, g08, g12, g13, g15
