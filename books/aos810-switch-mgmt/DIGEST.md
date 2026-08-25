# DIGEST — OmniSwitch AOS 8.10R4 Switch Management Guide 精华

本书是 ALE OmniSwitch AOS Release 8.10R4 的 511 页交换机管理指南（17 个功能章 + 附录），覆盖从首次上电登录、文件与配置管理、用户与 AAA 安全、SNMP/WebView/云纳管，到虚拟机箱与自动化部署的全套运维底座。全书主线可以概括为三条：**目录即安全网**（certified/working 双目录 + 回滚）、**默认即锁定**（管理面默认关闭、逐层解锁）、**自动化分层递进**（Auto VC → RCL → Auto Fabric → Lightning/Cirrus）。以下按六个技能单元摘要，页码均指原书。

## 一、知识地图（六技能单元）

1. **Flash 双目录与配置文件**（aos-sm-flash-config）：/flash 结构、certified/working/RUNNING 三层模型、reload 回滚、配置文件 apply/snapshot、恢复出厂（Ch3/4/6，p52-64、94-107、122-141）。
2. **代码升级与软件包**（aos-sm-software-upgrade）：标准 reload 升级、ISSU、签名镜像/Secure Boot、pkgmgr/appmgr、USB 升级与灾难恢复（Ch1/3/4，p21-24、62-92、113-118）。
3. **CLI 会话与用户安全**（aos-sm-cli-session-usermgmt）：console/EMP/SSH 登录、PKA、横幅、密码策略与锁定、权限分区、AAA、增强/JITC/FIPS 模式（Ch2/5/7/8，p29-48、122-130、144-186）。
4. **纳管服务**（aos-sm-mgmt-services）：SNMP v1/v2c/v3、WebView、REST/Python、Cirrus 云与 NaaS、DNS、NTP（Ch9-12/17，p190-278、406-417）。
5. **日志与健康监测**（aos-sm-logging-health）：command-log 审计、swlog、tech-support 基线、文件系统与镜像完整性自检、系统时钟（Ch1/3/5，p23、52-60、127-128）。
6. **机箱冗余与虚拟机箱**（aos-sm-chassis-cmm）：双 CMM 同步/接管、VC 组建（手工/Auto-VFL）、VFL/控制 VLAN、RCD/VCSP 分裂保护（Ch4/13，p99-111、300-343）。

## 二、六单元要点串讲

### 1. Flash 双目录：改动为什么会丢
certified 是已认证的可靠基线且**不可直接写**（<<<PAGE 94>>>）；working/用户目录是试验场；RUNNING CONFIGURATION 在 RAM（P3）。正常重启时 certified 与运行目录内容不同则从 certified 启动（P4），未保存的改动全部丢失（X2）。试验流程：`modify running-directory` 切用户目录 → `write memory` → 验证 → `copy running certified`（C20）；激进变更配 `reload from working rollback-timeout 5` 兜底（C21）。配置文件是纯 ASCII，`configuration syntax-check` 预检、`configuration apply` 支持 at/in 定时（但全网同时只允许一个定时会话，X30），`configuration snapshot` 导出非默认配置，`reset-to-factory` 三档清理（config/retain-vc/all，all 档连 license 一起清）。

### 2. 升级：两条路径一个安全链
标准升级 = 维护例行（`show system`、清旧文件、`show tech-support` 基线）→ 镜像进 Running 目录 → reload → 验证 → certify（C1/C3）；ISSU 按 chassis-id 从低到高逐台重启 Slave、最后 Master，结束后必须复位 NI（C2/P16）。软件安全链：ASLR → RSA-2048/SHA-256 签名镜像 → Secure Boot（P18-P20）；注意签名镜像机型降旧版须先降 u-boot（X9）。非 AOS 软件走 pkgmgr（verify→install→write memory，不保存则重启/takeover 丢失，X17），应用启停走 appmgr 免重启（C18）。USB：自动升级需 aossignature 空文件防误触发（P90）；灾难恢复传统用 Trescue.img + `run rescue`，ONIE 设备用 Onie Rescue + `onie-nos-install`（C25）。

### 3. 用户与 AAA：默认锁定 + 分区授权
管理面默认除 console 全锁（P34），admin 恒可 console 兜底（P36）。Telnet/FTP 明文，官方建议 SSH（X3）；高安全用 PKA（installsshkey/revokesshkey，C8）。授权按命令域/族两级分区（12 个域，F4），read-only/read-write 组合到 user 或 aaa priv-mask。密码策略成体系（长度/禁含用户名/过期/历史），但策略命令不自动保存（X31）；锁定三参数 window/threshold/duration 配合手工 lockout/unlock。AAA 认证链顺序即故障切换序，local 必须最后（P70）；secondary CMM/Slave 不支持远端认证（X37）。安全档位递进：FIPS（切换必重启，X25）→ 增强模式（加盐/单会话/TLS1.2/imgsha256sum 校验，X39-X42）→ JITC（与增强互斥，X45）。

### 4. 纳管服务：从 SNMP 轮询到云推送
SNMP：v3 用户配认证+加密组合（sha+aes），v1/v2c 靠 community-map 映射用户继承权限（P95）；trap 可按命令族或 trap ID 过滤、可重放、可吸收去重（P98/P99）。WebView 需 `aaa authentication http local` 解锁，自定义证书拼 web.pem 安装（C35）；改端口前必须断全部会话（X48）。REST 双域（mib/cli）+ JSON/XML，认证走 GET auth、配置走 PUT（C40）。Cirrus：新机无 boot.cfg 默认上云，存量机 `cloud-agent admin-state enable`（X54）；无 NTP 上不了云（X55）；NaaS license 状态机 Operational→Grace→Degraded，降级后只转发不管理（X57/X58）。NTP：minpoll/maxpoll 指数、burst/iburst 加速、MD5/SHA1 认证须 trusted key（P158-P161）。

### 5. 日志与健康：先有基线再谈排障
command-log 默认禁用，启用后自动建 /flash/command.log，记录命令/用户/IP/结果（C26）；启用期间文件不可删（X29）。升级/排障前必采 `show tech-support layer2|layer3|eng complete` 分层基线（C3）。文件系统 fsck 两档（no-repair/repair）、镜像 `image integrity check` SHA256 校验（P92）。时钟是日志与证书可信的前提，`system date/timezone`，DST 随时区自动（P163）。

### 6. 机箱与 VC：单 IP 管理与分裂双保险
双 CMM：running 自动同步，certified 需 `copy running certified flash-synchro`；takeover 前先同步，接管断旧主管理会话（C23/X27）。VC：vcsetup.cfg（入组）+ vcboot.cfg（整体）双文件；Master 选举五准则（P130）；Auto-VFL 直连即成（C47），手工路径走 convert-configuration + reload from vc_dir（C46）。限制清单长：不可混家族（X73）、VFL 限 10/40/100G 不混速（X77）、新成员可能双重启（X72）、分裂后配置不生效（X82）。分裂双保险：RCD（EMP 带外，VFL 全断时 former Slave 关面板口）与 VCSP（helper 专用 linkagg，master MAC 不匹配进 protection state，guard-timer 控恢复）。

## 三、高价值章节页码索引

| 主题 | 页码 |
|---|---|
| 自动管理特性总框架 | 21, 230 |
| 标准升级/ISSU/维护例行 | 22-24 |
| console/EMP/蓝牙接入 | 33-36 |
| SSH PKA/横幅/会话参数 | 38-45 |
| DNS/FIPS | 46-48 |
| /flash 结构与文件工具 | 52-64 |
| 签名镜像/Secure Boot | 65-66 |
| License（传统/SILOS） | 66-77 |
| 系统时钟/keychain | 78-84 |
| pkgmgr/appmgr | 85-90 |
| U-boot/ONIE 加固 | 91-92 |
| 双目录/回滚/certify | 94-107 |
| CMM 同步/takeover | 110-111 |
| USB 升级/灾备/镜像校验 | 113-118 |
| CLI 机制/命令日志 | 122-128 |
| 配置文件/快照/恢复出厂 | 133-141 |
| 用户/密码策略/锁定 | 145-158 |
| 权限域族/AAA | 159-175 |
| 增强模式/JITC | 176-186 |
| WebView | 190-199 |
| SNMP 全体系 | 203-220 |
| Cirrus/云纳管/NaaS | 222-241 |
| REST/Python/AMS | 246-278 |
| OpenFlow/Nutanix/PROFINET | 281-299 |
| VC 全体系/分裂保护 | 300-343 |
| RCL 自动远程配置 | 345-365 |
| Lightning/Auto Fabric | 373-404 |
| NTP | 406-417 |

## 四、一句话总纲

AOS 管理手册的底层逻辑是"改动永不直接进基线"：certified 保底、working 试验、reload 回滚兜底；管理面默认全锁、逐层解锁（aaa authentication → 用户分区 → 安全模式档位）；所有"配了没生效"先查三层——保存了吗（write memory）、认证链解锁了吗（aaa authentication）、是否踩了目录/模式/依赖限制（Limitations 反例）。
