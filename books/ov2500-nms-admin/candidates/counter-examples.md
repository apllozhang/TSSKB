# counter-examples 候选 — DT00XTE311 OmniVista 2500 NMS Administration R4

1. 许可安装二选一陷阱：License 文件与 License Keys 不可同时使用
   - <<<PAGE 104>>>："There are 2 different ways to install the evaluation license: By inserting directly the license file … OR by typing the license keys. **Don't do both!**"

2. License Key 粘贴整行的反例（会把许可名一起粘进去）
   - <<<PAGE 104>>> Warning："COPY AND PASTE ONLY THE LICENSE KEYS AND NOT THE ENTIRE LINES!（示例行 'EVAL-NM-EX-20-N, KEQWEXRH-…'，只取逗号后的 key 部分）"；且 "remove the license name before inserting them"。

3. 默认状态下交换机不能被 OV 管理（必须先配 SNMP）
   - <<<PAGE 97>>>："By default, an OmniSwitch cannot be managed by Omnivista. The switch must be modified to allow SNMP access."
   - <<<PAGE 164>>>："SNMP users and community strings need to be configured on devices before they can be managed by OmniVista."

4. 路由表缺 Loopback0 → 实验环境直接失败（需联系培训师）
   - <<<PAGE 90>>> Attention："IF THE ROUTING TABLE DOES NOT CONTAIN LOOPBACK0 ADDRESSES, PLEASE CONTACT THE TRAINER!"

5. 无可用快照 → 无法恢复 OV 初始配置
   - <<<PAGE 100>>>："IF NO SNAPSHOT IS AVAILABLE, PLEASE CONTACT YOUR TRAINER."（快照含 OV 的 IP、网关、network size 初始参数）。

6. 默认密码未改即无法继续 / 装完许可文件未删的隐患
   - <<<PAGE 101-102>>>：首登强制改默认密码（admin/switch → Training123#）才能进系统。
   - <<<PAGE 105>>>："Once the license file correctly inserted, please delete the file ('EVAL…') from the computer."

7. 误勾 Enable Fleet Supervision
   - <<<PAGE 104>>>：接受 EULA 时明确指示 "Check OK (don't check Enable Fleet Supervision)"，后面再次强调 "do not select the Enable Fleet Supervision option"。

8. HA 缺失时的业务中断反例（UPAM 认证停摆）
   - <<<PAGE 18>>>："If using UPAM, no new additional clients would be able to authenticate"（Main OV 失效且无 HA 时）。

9. 容量规划反例：High 档带 4000 AP 时交换机上限骤降
   - <<<PAGE 45>>>："**If there are 4,000 Stellar AP in a 'High' network size, up to 500 AOS switches can be supported. If there are 4,000 Stellar APs in a 'Very High' network size, up to 1,000 AOS switches can be supported."（选错 Network Size 会限制可管理规模）。

10. Trap 邮件Responder 不含 Normal 级别的配置注意点
    - <<<PAGE 192>>>："In the Trap Type section, disable the Normal trap so only the other severity levels are included in the mail."（不禁用会涌入正常事件）。
    - 前置条件：收 link trap 需交换机启用 `interfaces <slot>[/port] link-trap enable`（<<<PAGE 192>>> Note）。

11. VLAN 802.1X 客户端认证页签不可见的排查反例
    - <<<PAGE 266>>>："If Authentication tab is not available, click on the Start button, Run…, type services.msc … Look for Wired AutoConfig service and start it."
    - <<<PAGE 267-268>>>：必须取消 "Cache user information"、取消 "Automatically use my windows logon name and password"、取消 "Validate server certificate"，否则测试不成立。

12. 重新认证前未清 UNP 用户状态 → 残留会话干扰结果
    - <<<PAGE 268>>>："To ensure a clean status of the user ports on the 6860 … type: `-> unp user flush port 1/1/1`"，再禁用/启用网卡触发弹窗。
    - 同页 Note："You may see a second entry with a different MAC address. This is the link to the physical NIC associated with the client VM."（勿误判为异常）。

13. Client 拿不到 DHCP 地址的排障边界
    - <<<PAGE 290>>>："If Client07 does not get an IP address, then make sure that the AAA Training Server PodX VM is powered on. If this does not solve the issue, then assign a static IP address in the 192.168.80.X subnet with the default gateway set to 192.168.80.8"（IP helper 依赖 DHCP 服务器 VM）。

14. UNP 命名不一致 → RADIUS 返回值匹配失败
    - <<<PAGE 263>>> Notes："Type the UNP name as shown as it is the value returned from the RADIUS server"（Access Role Profile 名必须与 Filter-ID 完全一致，否则用户落不到 profile）。

15. 签名 Profile / 统计 Profile 的"一机一档"限制
    - <<<PAGE 342>>>："Note: A switch can only be in one profile of a particular Profile Type."（Analytics Profile）。
    - <<<PAGE 372>>>："A switch can be assigned only to one Signature Profile."（AppVis）。
    - <<<PAGE 391>>>："If you create a new profile, you will first have to unassign the 'Default Profile' from the desired switches."（统计采集）。

16. "NO DATA AVAILABLE" 并非故障——数据生成时延
    - <<<PAGE 380>>>："you should see a 'NO DATA AVAILABLE' warning. The main reason is that no traffic has been already generated from the client 8 … 'App Discovery' will only display the traffic captured after the generation of the internet traffic."
    - <<<PAGE 382>>>："Wait for 15-20 minutes before the applications are displayed in the OV widgets."

17. 自定义数据 3 个月上限与滚动覆盖
    - <<<PAGE 324>>>："You can display up to 3 months of data. When data reaches the 3-month maximum, it is overwritten with new data."

18. 应用端口映射导入会覆盖现有映射
    - <<<PAGE 351>>>："An existing application ports mapping file (.json file) can be imported … Note that this new mapping will override the existing mapping."
    - 未映射端口显示为 "Unknown"（<<<PAGE 350>>>）。

19. QM 内置规则默认全部禁用（以为开了其实没开）
    - <<<PAGE 304>>>："By Default all of the rules are disabled."

20. Candidates List 设备流量不被阻断的语义陷阱
    - <<<PAGE 308>>>："If a device is placed on the Candidates List, traffic to and from that device will continue until the Network Administrator decides what action should take place."（误以为进候选名单即隔离）。

21. Control Panel 误停服务的课堂警告
    - <<<PAGE 221>>>："(DO NOT modify or stop any process unless directed by your instructor!)"。

22. 镜像升级实验的环境约束与升级后手动动作
    - <<<PAGE 203>>>："DO NOT perform this section unless directed by your instructor."（镜像升级节）。
    - <<<PAGE 206>>>：升级完成信息须仔细读并照做：需 SSH 到交换机从 working 目录 reload，重启后执行 Copy Working Certified——漏做则升级不生效。

23. Thin Client 模式下直接改交换机配置的反例
    - <<<PAGE 75>>>："All configuration changes should be done in OV 2500."（thin-client 模式交换机本地不留 running 配置，本地改动无意义/会被覆盖）。
    - 版本边界："Thin Client is supported only on switches running AOS Release 8.8R1 (or higher)."

24. IoT 仅 IPv4 限制
    - <<<PAGE 404>>>："Note: IoT is supported on IPv4 devices only."

25. Mobile App 场景的连通性前提（未来版本功能边界）
    - <<<PAGE 415/451>>>："Mobile App: … Available in future release"——四个部署场景中的场景 1/2 依赖该未发布功能，当前不可实施。

26. 备份交换机 FTP 凭据缺失会中断备份向导
    - <<<PAGE 198>>>："Your switch may not have the FTP authentication credentials. Click on Add FTP Authentication if prompted."（须补 admin/switch 后数据库才同步）。

27. Check Service Stats 警告弹窗的处理
    - <<<PAGE 376>>>："A Check Service Stats warning message may appear. Click Ok if prompted."（AppVis Profile 应用时的已知提示）。

28. 远程实验室音频/剪贴板限制
    - <<<PAGE 195>>>："Due to the Remote lab Setup an audio device is not available to listen the notification sounds."
    - <<<PAGE 81>>>：Firefox 复制粘贴问题与 workaround 链接。

29. OVNA 设备不出现的排障边界
    - <<<PAGE 433-434>>>：需等待下次同步（每小时）；"Switches / APs need to be configured including managment IP, syslog configuration and make sure that OVNA is reachable from these devices"。

30. Sizing 环境变量影响实际容量
    - <<<PAGE 45>>>："Specific configurations may vary depending on the network, number of wired/wireless clients, number of VLANs, open applications, etc."（标称容量非保证值）。
