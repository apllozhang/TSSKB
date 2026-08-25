# glossary — OmniSwitch 6900 Hardware Users Guide（术语表候选）

格式：`- **术语**：解释 <<<PAGE N>>>`（页码为 fulltext.md 真实标记；按章分组）

## 机型（Ch1/Ch3）

- **OS6900-V72**：48×SFP28(10/25G)+6×QSFP28 机型，深度 51.5cm，188/400W <<<PAGE 12>>>/<<<PAGE 28>>>/<<<PAGE 29>>>
- **OS6900-C32**：32×QSFP28(100G) 机型，145/543W <<<PAGE 12>>>/<<<PAGE 30>>>/<<<PAGE 31>>>
- **OS6900-C32E**：32×QSFP28+2×SFP+（33/34 口 Not currently functional），175/510W <<<PAGE 12>>>/<<<PAGE 32>>>等
- **OS6900-T48C6**：48×1G/10GBaseT+6×QSFP28 机型；52/53 口 DAC 与 QSFP 不可混插 <<<PAGE 12>>>/<<<PAGE 34>>>等
- **OS6900-X48C6**：48×SFP+ +6×QSFP28 机型，114/392W <<<PAGE 12>>>/<<<PAGE 36>>>等
- **OS6900-X48C4E**：40×SFP+ +8×SFP28+6×QSFP28 机型，端口组 41-48 分 2 组锁速 <<<PAGE 12>>>/<<<PAGE 38>>>等
- **OS6900-V48C8**：48×SFP28+8×QSFP28+2×SFP+（57/58 未启用），226/532W，端口组编号非连续 <<<PAGE 12>>>/<<<PAGE 40>>>等
- **OS6900-T24C2**：24×10GBaseT+2×SFP+ +2×QSFP28 机型，91/209W <<<PAGE 12>>>/<<<PAGE 42>>>等
- **OS6900-X24C2**：24×SFP+ +2×SFP+ +2×QSFP28 机型，75/197W <<<PAGE 12>>>/<<<PAGE 44>>>等
- **OS6920-D32**：32×QSFP-DD(400G)+1×SFP+（未启用）机型，深 59cm，最高 1400W；后→前气流限 35°C <<<PAGE 12>>>/<<<PAGE 46>>>/<<<PAGE 47>>>
- **ToR（Top-of-Rack）**：数据中心机柜顶交换机部署模式，6900 家族第二定位 <<<PAGE 12>>>
- **QSFP-DD**：400G 双密度四通道光模块接口（支持 400G/2X200G/4X100G，向下兼容 QSFP56/28/+）<<<PAGE 46>>>
- **QSFP28**：100G 光模块口（4X10G/40G/4X25G/100G）<<<PAGE 28>>>等
- **SFP28**：25G 光模块口（1G/10G/25G）<<<PAGE 28>>>等
- **端口组（Port Group）**：4 口一组的速率锁定单元（V72/X48C4E/V48C8），组内 10G 与 25G 不可混 <<<PAGE 28>>>/<<<PAGE 38>>>/<<<PAGE 40>>>
- **Splitter 功能**：T48C6/X48C6 的 51/54 口支持分支（一拆四）功能 <<<PAGE 34>>>/<<<PAGE 36>>>
- **DAC（Direct-attached Cable）**：直连铜缆；T48C6/X48C6 52/53 口与 QSFP 光模块不可混插 <<<PAGE 34>>>等

## 电源（Ch3）

- **OS6900C-BP-F / -R**：650W AC 电源（12V/52.9A），V 系机型用，F=前→后/R=后→前 <<<PAGE 60>>>
- **OS6900X-BP-F / -R**：400W AC 电源（12V/33.34A），X 系机型用 <<<PAGE 61>>>
- **OS6900C-BPD-F / -R**：650W DC 电源（36-72VDC 输入），V 系用 <<<PAGE 62>>>
- **OS6900X-BPD-F / -R**：200/400W DC 电源（-20~-75VDC 两档输出），X 系用 <<<PAGE 63>>>
- **OS6920-BP-F / -R**：1500W AC 电源（100-127V/12A 或 220-240V/8A；hold time <20ms）<<<PAGE 64>>>
- **OS6920-BPD-F / -R**：1600W DC 电源（-40~-75V/50A，12V/133.33A），DC 端子+接地端子 <<<PAGE 65>>>
- **1+1 冗余（1+1 Redundant）**：双电源热插拔冗余，第二电源为 standby 角色 <<<PAGE 12>>>/<<<PAGE 59>>>
- **Lock Tab（锁片）**：电源就位"咔哒"锁定/按压释放机构 <<<PAGE 67>>>等
- **5VSB**：电源待机输出（5V standby）<<<PAGE 60>>>等
- **OS-DNV-DC-PWR**：IEC 60945 认证 DC 线缆（双磁环），X48C6+BPD-F 船用认证场景必备 <<<PAGE 63>>>
- **环形端子（Ring Terminal）**：OS6920 DC 电源接线端子（电源 8AWG/接地 6AWG，规格九项尺寸）<<<PAGE 67>>>
- **CBN / Isolated DC Return（DC-I）**：共同联结网络 / 隔离式 DC 回流 <<<PAGE 66>>>

## 风扇与气流（Ch3）

- **风扇托盘（Fan Tray）**：机箱后部 5/6 个独立热插拔风扇模块，主温控部件 <<<PAGE 28>>>等/<<<PAGE 70>>>
- **OS6900V-FT-F/R**：V72/C32/C32E/X48C4E 风扇托盘（F/R=气流方向）<<<PAGE 70>>>
- **OS6900-T48C6/X48C6-FT-F/R**：T/X 系风扇托盘（拇指螺丝在右上）<<<PAGE 70>>>
- **OS6900-V48C8-FT-F/R / OS6920-FT-F/R**：V48C8 / OS6920 专用风扇托盘 <<<PAGE 70>>>/<<<PAGE 71>>>
- **前→后气流（Front-to-Rear）**：顶部前进风、后部排风；部件标准色 <<<PAGE 51>>>/<<<PAGE 52>>>
- **后→前气流（Rear-to-Front）**：后部进风、前顶排风；部件紫色标识 <<<PAGE 51>>>/<<<PAGE 52>>>
- **气流失配（Airflow Mismatch）**：电源与风扇方向不一致引发的告警-重启机制 <<<PAGE 50>>>/<<<PAGE 52>>>
- **紫色编码（Purple Color Coding）**：后→前部件的防差错颜色标识 <<<PAGE 52>>>
- **滑入式支撑（Slide-in Braces）**：深机箱机架安装的强制后支撑件 <<<PAGE 54>>>/<<<PAGE 55>>>
- **中装法兰（Mid-Mount Flanges）**：装于机箱中部螺纹孔的替代安装方式 <<<PAGE 56>>>

## LED 与监控（Ch3）

- **PS1/PS2 LED**：绿=正常、琥珀=错误、灭=不在位 <<<PAGE 48>>>
- **Diag LED**：绿=正常、琥珀=自检故障 <<<PAGE 48>>>
- **Fan LED**：绿=正常、琥珀=错误（任一风扇意外停转即转琥珀并发 trap）<<<PAGE 48>>>/<<<PAGE 75>>>
- **LOC LED**：闪琥珀=远程定位激活 <<<PAGE 48>>>
- **QSFP-DD LED 色表**：青=400G、紫=200G、蓝=100G、橙=40G、红=端口故障等 12 态 <<<PAGE 48>>>
- **show module / show module long**：槽位基本/详细信息命令 <<<PAGE 74>>>
- **show temperature**：温度与 Warning/Danger 阈值状态命令 <<<PAGE 74>>>
- **show fan**：风扇托盘状态命令 <<<PAGE 75>>>
- **Warning 阈值**：可查/可配温度告警阈值，超限发 trap 业务继续 <<<PAGE 75>>>
- **Danger 阈值**：出厂固化，超限自动关机须手动启动 <<<PAGE 75>>>

## 管理口与登录（Ch2/Ch3）

- **EMP（Ethernet Management Port）**：RJ45 10/100/1000 带外管理口；默认 192.168.1.1/24 <<<PAGE 12>>>/<<<PAGE 18>>>/<<<PAGE 22>>>
- **EMP 线缆规则**：接交换机用直通线、接计算机用交叉线 <<<PAGE 18>>>
- **ip interface emp**：改 EMP IP 地址命令 <<<PAGE 22>>>
- **admin/switch**：出厂默认账号/密码 <<<PAGE 21>>>
- **aaa authentication**：解锁会话类型命令族 <<<PAGE 23>>>
- **115200-8N1 + rollover**：console 默认参数与线缆类型 <<<PAGE 18>>>
- **XON/XOFF**：软件流控（console 无 RTS/CTS 硬件握手）<<<PAGE 76>>>
- **Reset 按钮**：前面板系统重启按钮 <<<PAGE 28>>>等
- **RCL（Remote Configuration Load）**：远程配置加载（详见 Switch Management Guide）<<<PAGE 21>>>
- **show system / write memory**：查看系统信息 / 保存配置 <<<PAGE 25>>>
- **system location**：设置交换机物理位置 <<<PAGE 24>>>

## 标准与合规（附录 A）

- **UL 60950-1 / IEC 60950-1**：IT 设备安全标准（第二版）<<<PAGE 82>>>
- **EN 60825-1/-2**：激光产品安全标准 <<<PAGE 82>>>
- **FCC Part 15 Class A / CISPR 22**：Class A 电磁干扰限值 <<<PAGE 82>>>/<<<PAGE 84>>>
- **ETS 300 019**：环境试验标准（存储 1.1/运输 2.3/固定使用 3.1）<<<PAGE 83>>>
- **Class 1M Laser**：1M 级激光辐射、勿用光学仪器直视 <<<PAGE 84>>>
- **CR1220**：机箱 RTC 锂电池型号（X48C6/T48C6/X48C4E/V48C8）<<<PAGE 81>>>
- **UN3091**：设备内含锂金属电池的运输分类（不得入生活垃圾）<<<PAGE 80>>>
- **Prop 65 / WEEE / RoHS**：加州 65 号 / 欧盟回收 / 有害物质限制 <<<PAGE 78>>>-<<<PAGE 80>>>
- **CDE（Cable Discharge Event）**：线缆静电放电事件；接线前对地放电 <<<PAGE 15>>>
- **ESD 腕带**：防静电腕带，接触部件前消除静电 <<<PAGE 88>>>
- **受限场所（Restricted Access Location）**：仅持钥匙/安保措施的维护人员可进入 <<<PAGE 88>>>
- **Tmra**：最大额定环境温度（封闭机架内按此折减）<<<PAGE 49>>>
