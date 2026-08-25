# GLOSSARY · OmniSwitch 6560 Hardware Users Guide

> 页码为原书 `<<<PAGE N>>>` 标记。按机型/电源/安装/面板/温度/PoE/CLI/法规分组。

- **OS6560-P24Z8**：16 口 at + 8 口 2.5G bt PoE + 2×SFP+，待机 67W <<<PAGE 12>>>/<<<PAGE 25>>>
- **OS6560E-P24Z8**：16 at + 4×2.5G bt（17-20）+ 4×2.5G/5G bt（21-24）+ 2×SFP+ 的 E 增强版，不支持 BP-P 电源 <<<PAGE 12>>>/<<<PAGE 26>>>/<<<PAGE 60>>>
- **OS6560-P24Z24**：24 口全 2.5G bt PoE + 4×SFP+ + 2×20G QSFP+ VFL，待机 116W <<<PAGE 12>>>/<<<PAGE 28>>>
- **OS6560-P48Z16**：32 at + 16 口 2.5G bt + 4×SFP+ + 2×QSFP+ VFL；有 903954-90（老版）与其余 PN（新版）两版 <<<PAGE 12>>>/<<<PAGE 34>>>
- **OS6560E-P48Z16**：32 at + 4×2.5G/5G bt（33-36）+ 12×2.5G bt（37-48）+ 4×SFP+ + 2×QSFP+ VFL，待机 119W <<<PAGE 12>>>/<<<PAGE 36>>>
- **OS6560-24Z8**：16 千兆 + 8×2.5G 非 PoE + 2×SFP+ <<<PAGE 12>>>/<<<PAGE 38>>>
- **OS6560-24Z24**：24×2.5G 非 PoE + 4×SFP+ + 2×QSFP+ VFL <<<PAGE 12>>>/<<<PAGE 40>>>
- **OS6560-24X4**：24 千兆非 PoE + 2×SFP(+)（10G 需许可）+ 4×SFP+；内置电源+BPS 槽 <<<PAGE 13>>>/<<<PAGE 42>>>
- **OS6560-P24X4**：24 口 at PoE + 2×SFP(+)（10G 需许可）+ 4×SFP+ <<<PAGE 13>>>/<<<PAGE 30>>>
- **OS6560-48X4**：48 千兆 + 2×SFP(+)（10G 需许可）+ 2×SFP+ + 2×纯 10G SFP+；内置电源+BPS 槽 <<<PAGE 13>>>/<<<PAGE 44>>>
- **OS6560-P48X4**：48 口 at PoE 版 48X4，双 PX 电源 PoE 预算最高 1440W <<<PAGE 13>>>/<<<PAGE 32>>>/<<<PAGE 87>>>
- **OS6560-X10**：8×SFP+ 1G/10G + 2×20G QSFP+ VFL 纯上联机型，内置 65W+模块化电源 <<<PAGE 13>>>/<<<PAGE 46>>>
- **Z 口（多千兆口）**：100/1000/2.5G（E 版至 5G）802.3bt PoE 口，Speed+PoE 双 LED <<<PAGE 12>>>/<<<PAGE 49>>>
- **10G 许可口**：SFP(+) 1G/10G 口位，10G 速率需软件许可（49-50 口）<<<PAGE 30>>>等

## 电源体系（Ch3）
- **OS6560-BP-P**：300W AC PoE 电源（PS-300W-AC-P），54.5V/5.5A，系统 110W 封顶；不配 E 机型与新 PN 的 P48Z16 <<<PAGE 61>>>/<<<PAGE 60>>>
- **OS6560-BP-PH**：600W AC PoE 电源（PS-600W-AC-P），54.5V/11A；PN 903852-90/904071-90/904072-90 三版，904072-90 需 ≥8.8R1 <<<PAGE 62>>>
- **OS6560-BP-PX**：920W AC PoE 电源（PS-920W-AC-P），54.5V/16.88A；903853-90/904073-90 两版，904073-90 需 ≥8.8R1 <<<PAGE 63>>>
- **OS6560-BP**：150W AC 电源（PS-150W-AC），配非 PoE 机型/BPS；可与 BP-D 混插 <<<PAGE 64>>>
- **OS6560-BP-D**：150W DC 电源（PS-150W-DC），-36~-72V 输入，配非 PoE 机型 <<<PAGE 65>>>
- **内置 AC 电源（65W）**：24X4/48X4/X10 的内置 12V/5.42A 系统电源 <<<PAGE 66>>>
- **BPS（Backup Power Supply Slot）**：非 PoE 机型后部模块化备份电源槽（标"BPS"）<<<PAGE 42>>>/<<<PAGE 44>>>/<<<PAGE 46>>>
- **锁扣（Lock Tab）**：可插拔电源的锁定片（插入 click 锁定/按住中心抽出）<<<PAGE 70>>>/<<<PAGE 72>>>
- **AC OK / DC OK LED**：PoE 电源双指示灯（绿/红）<<<PAGE 61>>>
- **BP/BP-D 单 LED 六态**：稳绿/闪绿待机/闪红无 AC/闪绿红告警/稳红故障/灭全停 <<<PAGE 64>>>/<<<PAGE 65>>>
- **负载分担（Load Sharing）**：双 PoE 电源共同分担供电（"the two power supplies will load share"）<<<PAGE 60>>>
- **DC 线束**：三芯 12AWG（绿黄=地/黑=return/红=-48VDC），15A 过流、SELV、DC-1 隔离回流 <<<PAGE 68>>>/<<<PAGE 69>>>

## 安装部件（Ch3）
- **Rack Mount Flange**：免工具卡扣机架法兰（out/in 位+CLICK）<<<PAGE 54>>>
- **OS-DNV-MNT**：P48X4/X10 船用安装套件（侧轨+前后托架）<<<PAGE 58>>>
- **OS-DNV-FILTER**：DNV EMC 滤波器——滤除 10kHz-150kHz 传导发射，串接电源与机箱之间；C14 入/C15 出 <<<PAGE 58>>>/<<<PAGE 67>>>
- **Blank Cover Panel**：空槽盲板（箭头朝上常装）<<<PAGE 52>>>
- **Virtual Chassis ID LED**：前面板 VC 标识灯 <<<PAGE 24>>>等

## 面板与 LED（Ch3）
- **OK LED**：绿=启动 OK、闪绿=进行中、琥珀=启动失败 <<<PAGE 48>>>
- **VC LED**：稳绿=master、稳琥珀=slave、灭=关机或非 VC <<<PAGE 48>>>
- **PWR LED**：绿=双电/单电正常、琥珀=一或双故障、灭=无电源 <<<PAGE 48>>>
- **2.5G 口双 LED**：Speed LED（绿=2.5G/琥珀=100-1000）+PoE LED（琥珀=PoE 开）<<<PAGE 49>>>

## 温度与 DG（Ch3）
- **Warning Threshold（可配）**：6560 温度告警阈值用户可配（"user-configurable warning threshold"），超限发 trap 不停机 <<<PAGE 76>>>
- **Danger Threshold**：危险阈值出厂固化，超限关机需手动重启 <<<PAGE 76>>>
- **Dying Gasp**：失电残电通告——SNMP trap（前 3 站）+Syslog（前 3 服务器）+4 个 802.3ah OAM PDU（上联口优先）<<<PAGE 78>>>-<<<PAGE 82>>>
- **efm-oam propagate-events dying-gasp**：使能 DG 经 OAM PDU 通告 <<<PAGE 82>>>
- **CBN（Common Bonding Network）**：共模接地网（DC 安装要求）<<<PAGE 68>>>

## PoE 体系（Ch4）
- **802.3bt 口功率范围**：3000-95000mW（at 口 3000-30000mW）<<<PAGE 85>>>
- **PoE 预算表**：机型×电源×数量三要素查表（如 P48X4 双 PX=1440W）<<<PAGE 87>>>
- **lanpower slot service / port admin-state**：slot 启停 / 端口复活（不能首启）<<<PAGE 89>>>
- **lanpower power / slot maxpower**：端口/槽上限（不预留）<<<PAGE 90>>>
- **lanpower priority**：low/high/critical 三级 <<<PAGE 90>>>
- **lanpower 4pair / 8023bt**：开 60/75/95W PoH / 开 bt Class 5-8 <<<PAGE 89>>>
- **Guard Band**：余量低于口上限即拒新 PD <<<PAGE 92>>>
- **Priority Disconnect**：优先级+物理口号（1 高 48 低）裁决新 PD <<<PAGE 93>>>/<<<PAGE 94>>>
- **BPS power 显示**：show lanpower 输出的备份电源状态行 <<<PAGE 88>>>

## CLI 与管理（Ch2-Ch4）
- **show module / long / temperature / powersupply / lanpower**：硬件巡检命令族 <<<PAGE 75>>>/<<<PAGE 87>>>/<<<PAGE 96>>>
- **WebView**：内嵌 Web 管理界面（OmniVista 或浏览器启动），可管 PoE 等硬件特性 <<<PAGE 84>>>
- **aaa authentication / password / system * / write memory**：首次登录六步命令 <<<PAGE 20>>>-<<<PAGE 22>>>
- **snmp station / swlog output socket**：DG trap/Syslog 接收站配置 <<<PAGE 80>>>/<<<PAGE 81>>>

## 安全与法规（附录 A）
- **CDE（Cable Discharge Event）**：线缆静电放电（Cat5e/6/6a 接前先接地）<<<PAGE 16>>>
- **ESD/Wrist Strap**：静电防护腕带 <<<PAGE 108>>>
- **Class 1M Laser**：开盖激光勿直视 <<<PAGE 24>>>等/<<<PAGE 105>>>
- **Restricted Access Location**：受限访问场所 <<<PAGE 108>>>
- **WEEE/RoHS/Prop 65**：回收/有害物/加州铅警告 <<<PAGE 97>>>-<<<PAGE 100>>>
- **Hi-Pot Test**：以太网口 2250V DC 耐压测试 <<<PAGE 102>>>
- **ETS 300 019**：环境标准（存储 1.1/运输 2.3/固定使用 3.1）<<<PAGE 103>>>
- **Class A 设备**：商用限制（住宅禁用）<<<PAGE 104>>>
- **Tmra**：最大额定环境温度（全家族 0-45°C）<<<PAGE 25>>>等
- **Chassis vs Ambient Temperature**：机箱传感器温度恒高于室温 <<<PAGE 25>>>等

---
合计：约 60 条。
