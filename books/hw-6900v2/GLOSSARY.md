# GLOSSARY · OmniSwitch 6900 Hardware Users Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按机型/接口/电源/风扇气流/LED 监控/管理口/法规分组，精选 52 条。

## 机型（Ch1/Ch3）
- **OS6900-V72**：48×SFP28(10/25G)+6×QSFP28 机型，深度 51.5cm，188/400W <<<PAGE 12>>>/<<<PAGE 28>>>/<<<PAGE 29>>>
- **OS6900-C32**：32×QSFP28(100G) 机型，145/543W <<<PAGE 12>>>/<<<PAGE 30>>>/<<<PAGE 31>>>
- **OS6900-C32E**：32×QSFP28+2×SFP+（33/34 口未启用），175/510W <<<PAGE 12>>>/<<<PAGE 32>>>
- **OS6900-T48C6**：48×1G/10GBaseT+6×QSFP28；52/53 口 DAC 与 QSFP 不可混插 <<<PAGE 12>>>/<<<PAGE 34>>>
- **OS6900-X48C6**：48×SFP+ +6×QSFP28 机型，114/392W <<<PAGE 12>>>/<<<PAGE 36>>>
- **OS6900-X48C4E**：40×SFP+ +8×SFP28+6×QSFP28，端口组 41-48 分 2 组锁速 <<<PAGE 12>>>/<<<PAGE 38>>>
- **OS6900-V48C8**：48×SFP28+8×QSFP28+2×SFP+（57/58 未启用），226/532W，端口组编号非连续 <<<PAGE 12>>>/<<<PAGE 40>>>
- **OS6900-T24C2**：24×10GBaseT+2×SFP+ +2×QSFP28，91/209W <<<PAGE 12>>>/<<<PAGE 42>>>
- **OS6900-X24C2**：24×SFP+ +2×SFP+ +2×QSFP28，75/197W <<<PAGE 12>>>/<<<PAGE 44>>>
- **OS6920-D32**：32×QSFP-DD(400G)+1×SFP+（未启用），深 59cm，最高 1400W；后→前气流限 35°C <<<PAGE 12>>>/<<<PAGE 46>>>/<<<PAGE 47>>>
- **ToR（Top-of-Rack）**：数据中心机柜顶部署模式，6900 家族第二定位 <<<PAGE 12>>>
- **机箱深度三档**：47.3cm（T/X 小型）→51.5-53.6cm（V/C 系）→59cm（OS6920），决定后支撑需求 <<<PAGE 29>>>等/<<<PAGE 35>>>等/<<<PAGE 47>>>

## 接口与端口约束
- **QSFP-DD**：400G 双密度四模块接口（400G/2X200G/4X100G，向下兼容 QSFP56/28/+）<<<PAGE 46>>>
- **QSFP28**：100G 光模块口（4X10G/40G/4X25G/100G）<<<PAGE 28>>>等
- **SFP28**：25G 光模块口（1G/10G/25G）<<<PAGE 28>>>等
- **端口组（Port Group）**：4 口一组速率锁定单元，组内 10G 与 25G 不可混（1G+10G 可混）<<<PAGE 28>>>/<<<PAGE 38>>>/<<<PAGE 40>>>
- **DAC（Direct-attached Cable）**：直连铜缆；T48C6/X48C6 52/53 口与 QSFP 不可混插 <<<PAGE 34>>>等
- **Splitter 功能**：T48C6/X48C6 51/54 口一拆四分支 <<<PAGE 34>>>/<<<PAGE 36>>>
- **Not currently functional 口**：预留未激活口（C32E 33/34、V48C8 57/58、OS6920 33），不可当可用口规划 <<<PAGE 32>>>/<<<PAGE 40>>>/<<<PAGE 46>>>

## 电源体系（Ch3）
- **OS6900C-BP-F / -R**：650W AC 电源（12V/52.9A），V 系用 <<<PAGE 60>>>
- **OS6900X-BP-F / -R**：400W AC 电源（12V/33.34A），X 系用 <<<PAGE 61>>>
- **OS6900C-BPD-F / -R**：650W DC 电源（36-72VDC），V 系用 <<<PAGE 62>>>
- **OS6900X-BPD-F / -R**：200/400W DC 电源（-20~-75VDC），X 系用 <<<PAGE 63>>>
- **OS6920-BP-F / -R**：1500W AC 电源（100-127V/12A 或 220-240V/8A；hold time <20ms）<<<PAGE 64>>>
- **OS6920-BPD-F / -R**：1600W DC 电源（-40~-75V/50A，6AWG）<<<PAGE 65>>>
- **两代电源阵营**：V 系 650W 与 X 系 400W 互不兼容，同箱混插禁止 <<<PAGE 60>>>-<<<PAGE 65>>>
- **AC+DC 混插**：同阵营同箱允许（与 9900 相反）<<<PAGE 60>>>等
- **1+1 冗余**：双电源热插拔冗余，第二电源 standby <<<PAGE 12>>>/<<<PAGE 59>>>
- **Lock Tab（锁片）**：电源"咔哒"锁定/按压释放机构 <<<PAGE 67>>>等
- **5VSB**：电源待机 5V 输出 <<<PAGE 60>>>等
- **环形端子（Ring Terminal）**：OS6920 DC 接线端子（电源 8AWG/接地 6AWG）<<<PAGE 67>>>
- **OS-DNV-DC-PWR**：IEC 60945 认证 DC 线缆（双磁环），船用认证场景必备 <<<PAGE 63>>>
- **无电源开关语义**：接电即开机，断全部电源线即关机 <<<PAGE 59>>>

## 风扇与气流
- **风扇托盘（Fan Tray）**：机箱后部 5/6 个热插拔托盘，主温控部件；必装件 <<<PAGE 28>>>等/<<<PAGE 70>>>
- **风扇托盘型号**：OS6900V-FT / T48C6-FT / V48C8-FT / OS6920-FT 各分 F/R 版，随机型专用 <<<PAGE 70>>>/<<<PAGE 71>>>
- **前→后气流（F）**：顶部前进风、后部排风；部件标准色 <<<PAGE 51>>>/<<<PAGE 52>>>
- **后→前气流（R）**：后部进风、前顶排风；部件紫色标识 <<<PAGE 51>>>/<<<PAGE 52>>>
- **气流失配（Airflow Mismatch）**：电源与风扇方向不一致→trap→循环重启/Danger 重启 <<<PAGE 50>>>/<<<PAGE 52>>>
- **紫色编码**：后→前部件的防差错颜色 <<<PAGE 52>>>
- **滑入式支撑（Slide-in Braces）**：深机箱机架安装强制后支撑件 <<<PAGE 54>>>/<<<PAGE 55>>>
- **中装法兰（Mid-Mount Flanges）**：机箱中部螺纹孔替代安装方式 <<<PAGE 56>>>
- **60 秒风扇更换窗口**：无风扇托盘运行不得超过 60 秒 <<<PAGE 72>>>

## LED 与监控
- **PS1/PS2 LED**：绿=正常、琥珀=错误、灭=不在位 <<<PAGE 48>>>
- **Diag LED**：绿=正常、琥珀=自检故障 <<<PAGE 48>>>
- **Fan LED**：绿=正常、琥珀=错误（任一风扇停转即转琥珀+trap）<<<PAGE 48>>>/<<<PAGE 75>>>
- **LOC LED**：闪琥珀=远程定位激活 <<<PAGE 48>>>
- **QSFP-DD 十二态色表**：青=400G、紫=200G、蓝=100G、橙=40G、红=端口故障等 <<<PAGE 48>>>
- **show module / show module long**：槽位基本/详细信息 <<<PAGE 74>>>
- **show temperature**：温度与 Warning/Danger 阈值状态 <<<PAGE 74>>>
- **show fan**：风扇托盘状态 <<<PAGE 75>>>
- **Warning 阈值**：可配告警阈值，超限发 trap 业务继续 <<<PAGE 75>>>
- **Danger 阈值**：出厂固化，超限自动关机须手动启动 <<<PAGE 75>>>

## 管理口与登录
- **EMP（Ethernet Management Port）**：RJ45 10/100/1000 带外管理口，默认 192.168.1.1/24 <<<PAGE 12>>>/<<<PAGE 18>>>/<<<PAGE 22>>>
- **EMP 线缆规则**：接交换机用直通线、接计算机用交叉线 <<<PAGE 18>>>
- **ip interface emp**：改 EMP IP 命令（须 console 先行）<<<PAGE 22>>>
- **admin/switch**：出厂默认账号/密码 <<<PAGE 21>>>
- **aaa authentication**：解锁会话类型命令族（解锁前 EMP 不能远程访问）<<<PAGE 22>>>/<<<PAGE 23>>>
- **115200-8N1 + rollover**：console 默认参数与线缆类型（软件流控 XON/XOFF）<<<PAGE 18>>>/<<<PAGE 76>>>

## 安全与法规（附录 A）
- **Class 1M Laser**：1M 级激光，勿用光学仪器直视 <<<PAGE 84>>>
- **CR1220**：机箱 RTC 锂电池型号 <<<PAGE 81>>>
- **UN3091**：设备内含锂金属电池运输分类 <<<PAGE 80>>>
- **CDE（Cable Discharge Event）**：线缆静电放电，接线前对地放电 <<<PAGE 15>>>/<<<PAGE 16>>>
- **受限场所（Restricted Access Location）**：DC 源安装要求 <<<PAGE 66>>>/<<<PAGE 88>>>
- **Tmra**：最大额定环境温度（OS6920 后→前气流降额 35°C）<<<PAGE 49>>>/<<<PAGE 47>>>

---
合计：52 条。
