---
name: AOS 8 CLI 会话与用户安全（登录/SSH PKA/密码策略/AAA/权限分区）
description: 需要在 OmniSwitch AOS 8 上配置控制台/EMP/Telnet/SSH 登录与会话参数、部署 SSH 公钥认证、创建用户并分配命令域/族权限、配置密码策略与锁定、部署 AAA（RADIUS/LDAP）认证链、增强/JITC 安全模式时使用。
source_book: OmniSwitch AOS Release 8.10R4 Switch Management Guide
---

## R（触发场景）
- 新交换机首次登录（console/EMP/USB dongle/蓝牙），或要解锁 Telnet/SSH/FTP/HTTP 管理访问
- 要部署 SSH 公钥认证（PKA）、登录横幅、会话超时/登录尝试限制
- 要建用户并按命令域/族分配读写权限（分区管理），或配置全局密码策略/锁定
- 要接 RADIUS/LDAP 外部认证并设计本地回退链，或部署 ASA 增强模式/JITC/FIPS

## I（核心理念）
ASA 安全框架（F3，<<<PAGE 167-186>>>）：管理接口（console/ftp/http/ssh/telnet/snmp）× 认证源（RADIUS/LDAP/local 链式故障切换）× 授权（命令域/族分区）× 计费四层，default/enhanced/JITC 三档安全模式递进。权限分区框架（F4）：命令域（domain-admin/system/network 等 12 个）下辖命令族，read-only/read-write/all/none/all-except 组合授权。默认管理面锁定（P34）：除 console 外一切管理接口需 `aaa authentication` 显式解锁；admin 恒可走 console 兜底（P36）。CLI 是单级命令体系，任意时刻可输任意命令（P46）。

## A1（决策框架）
1. **首次带外接入**：micro-USB/RJ-45 console（默认 9600-8-N-1）或 EMP/USB dongle/蓝牙；改串口参数走 `modify boot parameters`（C5-C7）
2. **远程管理选 SSH 弃 Telnet/FTP**（明文不安全，X3）：四阶段认证（P39），高安全场景上 PKA（P41）
3. **用户授权按域/族分区**：`user <name> read-write <域|族>` 精确授权，default 账户做新用户模板（P63/P67）
4. **外部认证设计回退链**：`aaa authentication <iface> rad1 ldap2 local`——顺序即故障切换序，local 必须最后（P70/P73）
5. **安全档位递进**：默认 → FIPS（加密合规，切换需重启）→ 增强模式（加盐/单会话/TLS1.2/镜像校验）→ JITC（军用，与增强互斥）（P44/P75-P81/X45）

## A2（操作步骤）
- **EMP/共享 IP**：`ip interface emp address 198.51.100.100 mask 255.255.0.0`；CMM 私有地址在控制台 `boot empipaddr/empmasklength` + `commit boot`（C7，<<<PAGE 35-36>>>）
- **SSH PKA**：`ssh-keygen -t rsa` → `scp *.pub admin@ip:/flash/system` → `installsshkey new_ssh_user /flash/system/*.pub` → 客户端公钥登录；撤销 `revokesshkey`（C8，<<<PAGE 41-42>>>）
- **登录横幅/会话**：`session {cli|ftp|http} banner /flash/switch/xxx.txt`（仅 ASCII .txt）；`session login-attempt 5`、`session cli timeout N`、`ssh login-grace-time 200`（C9/C10）
- **建用户授权**：`user thomas password techpubs` → `user thomas read-write domain-network ip-helper telnet` → `show user thomas`；密码策略 `user password-size min 10`、`user password-expiration 3`、`user password-history 2`（C30，<<<PAGE 149-155>>>）
- **锁定**：`user lockout-window 30` + `lockout-threshold 3` + `lockout-duration 60`；手工 `user j_smith lockout|unlock`（C31，<<<PAGE 157-158>>>）
- **AAA 快速部署**：`aaa radius-server rad1 host 10.10.1.2 timeout 3` → `aaa authentication telnet rad1 ldap2 local` → `aaa accounting session ldap2 local` → `show aaa authentication`（C32，<<<PAGE 171>>>）
- **增强模式**：`aaa switch-access mode enhanced`（保存并重启）+ `ip-lockout-threshold 2` + 管理站白名单 `aaa switch-access management stations 100.15.5.9`（C33，<<<PAGE 176-182>>>）
- **FIPS**：`system fips admin-state enable` → `reload from working no rollback-timeout` → `show system fips` → 手动禁 Telnet/FTP（C12，<<<PAGE 47-48>>>）
- **会话管理**：`who` / `whoami` / `kill <n>`；`session session-limit` 限并发（P84/P45）

## E（实证案例）
- console/蓝牙/EMP 三种带外接入定位与配置（C5-C7，<<<PAGE 33-36>>>）
- SSH PKA 部署与撤销（C8，<<<PAGE 41-42>>>）
- 创建用户 + 密码策略 + 锁定全套（C30/C31，<<<PAGE 149-158>>>）
- AAA 快速部署与增强模式（C32/C33，<<<PAGE 171-182>>>）
- JITC 模式启用与验证（C34，<<<PAGE 184>>>）

## B（反例/坑）
- Telnet/FTP 不加密，官方建议改用 SSH（X3，<<<PAGE 37-38>>>）
- `commit system` 只进运行系统不落非易失存储，重启丢失（X4，<<<PAGE 34, 36>>>）
- EMP 无独立路由表，与业务接口共用一张表（X5，<<<PAGE 35>>>）
- 密码策略命令不自动保存到配置（X31）；全星号密码被拒（X32）；密码过期用户需 admin 重置（X33）（<<<PAGE 151-154>>>）
- 锁定观察窗不应长于锁时长（X34，<<<PAGE 157>>>）
- SNMP 不能配 admin 用户（X35）；secondary CMM/Slave 不支持远端认证，只能 local（X37）；SNMP 仅支持 LDAP/local（X38）（<<<PAGE 161, 173-174>>>）
- 增强模式：非合规密码登录直接判认证失败（X39）、单用户单会话（X40）、仅 TLS1.2（X41）、新镜像必须同步更新 imgsha256sum 否则循环重启（X42）（<<<PAGE 177-178>>>）
- priv-mask 读写权限仅限 HTTP(S)，SSH/Telnet/Console 只能只读（X44，<<<PAGE 181>>>）
- JITC 与增强/CC 模式互斥（X45）；超级用户密码不可恢复，遗忘只能恢复出厂（X47）（<<<PAGE 184, 186>>>）
- secureadmin 用户不可用 Telnet/FTP，关键 CLI 仅 console 会话可执行（X101，<<<PAGE 146>>>）

## 来源
OmniSwitch AOS 8.10R4 Switch Management Guide 第 2 章 Logging In（<<<PAGE 29-48>>>）、第 5 章 Using the CLI（<<<PAGE 122-130>>>）、第 7 章 User Accounts（<<<PAGE 144-166>>>）、第 8 章 Switch Security（<<<PAGE 167-186>>>）。条目来源：cases C5-C12/C30-C34；principles P34-P51/P61-P84；counter-examples X3-X5/X31-X47/X101；frameworks F3/F4。
