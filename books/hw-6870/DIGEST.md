# DIGEST — OmniSwitch 6870 Hardware Users Guide 精华

本书是 ALE 千兆/多千兆接入交换机 OS6870 家族的硬件手册（85 页，9 个 1U 机型）。核心卖点：上行覆盖 SFP28(25G)/QSFP28(100G)/QSFP56(200G) 三档；M 系列模块化（95W bt 多千兆 + Uplink Module Slot 后配上行）；6 型电源（250W-2000W）支持不同瓦数混插扩容；PoE 802.3af/at/bt 至 Class 8（90-99W/口）。全书沿"选型→安装→上电→PoE→监控"生命周期展开。

## 一、知识地图（三技能单元）

1. **机型与端口体系**（os6870-model-ports）：九机型三分类、QSFP56 200G、M/Z/V/CNI/LNI 命名、四色 RJ45 速率 LED（Ch1/Ch3，p12-39）。
2. **安装与供电**（os6870-install-power）：弹簧夹法兰机架、六型电源与混插扩容、PoE 预算四变量、DC 三线（Ch2-Ch4，p14-71）。
3. **运维与排障**（os6870-ops-troubleshoot）：lanpower+4pair/bt 使能、温度双阈值、DG 三通道、上电入网七步（Ch2-Ch4，p14-71）。

## 二、三单元要点串讲

### 1. 机型与端口：九机型三分类
命名（<<<PAGE 12>>>）：`P`=PoE；`M`=Modular（上行模块槽+95W bt+QSFP56 200G）；`Z`=固定多千兆 60W bt；`V12`=全光；CNI-U2/LNI-U6=上行扩展机箱。三分类（P1）：非 PoE 固定（-24/-48）→P*M 模块化（P24M 至 10G/P48M 至 5G，均 95W bt）→P*Z 固定（至 2.5G，60W bt）。上行阶梯（P2）：SFP28 1/10/25G（25G 推荐 VFL）→QSFP28 40/100G→QSFP56 40/100/200G。RJ45 四色速率 LED：绿=10/100/1000、蓝=2.5G、品红=5G、琥珀=10G（<<<PAGE 39>>>）。功耗梯度：-24=71W→P48M=251.8W。

### 2. 安装与供电：混插扩容与四变量预算
双电源负载分担+热插拔，且**支持不同瓦数混插**（<<<PAGE 47>>>/<<<PAGE 51>>>）——扩容可先混后替（F4：600W→1200W→2000W 平滑升级），与 6860 wattage 禁混相反。2000W 仅 P24M/P48M（Z 系列标 N/A，<<<PAGE 47>>>）。PoE 预算四变量（F2，<<<PAGE 63>>>）：机型×电源瓦数×单双×电压档（双值条目=低压/高压输入；1200W/2000W 需 190-240VAC 才得高 PoE 功率，<<<PAGE 52>>>/<<<PAGE 53>>>）；P48M 双 2000W 最高 3309W。多电源数秒内相继插电（<<<PAGE 18>>>）。DC 三线：绿黄=地/黑=return/红=-48V（<<<PAGE 54>>>）。

### 3. 运维与排障：bt 全栈与双阈值
两级使能（<<<PAGE 65>>>）：`lanpower 4pair`（60/75/95W，at 4 对+PoH）→`lanpower 8023bt`（bt Type3/4 Class 5-8，90-99W）。首次激活必须 `lanpower slot service start`（<<<PAGE 65>>>）。Guard Band：剩余预算<口上限/类最大值即拒载，调低口上限放行；不作用已在电 PD（<<<PAGE 67>>>/<<<PAGE 68>>>）。Priority Disconnect：**端口号 1 最高→48 最低**（<<<PAGE 68>>>/<<<PAGE 69>>>）。温度双阈值：Warning 可配发 trap，Danger 固化关机须手动启动（<<<PAGE 58>>>/<<<PAGE 59>>>）。DG 三通道（<<<PAGE 59>>>/<<<PAGE 60>>>）：SNMP 前 3 站+Syslog 前 3 服务器+4×802.3ah PDU（上联口优先）。console 全系 115200-8N1 rollover 线。

## 三、本书在知识库中的位置

6870 定位多千兆 bt 高端接入/楼宇汇聚，上行 25G-200G 覆盖，与 hw-6860（VC 千兆中坚）、hw-6560（多千兆办公）构成接入高、中、办公三线，上接 hw-6900v2 核心。跨书易混点：①Priority Disconnect 口号 1 高 48 低，与 6860 反向；②6870 允许混插电源，6860 禁混；③console 波特率全系 115200，与 6360/6865（9600）、6860（9600/仅 N 型 115200）不同；④6870 SFP28 口组无 6860 N 型"禁混速"限制。

## 来源
OmniSwitch 6870 Hardware Users Guide（Part No. 060931-00, Rev. D, 2025-12）。verified.md：cases C1-C27；principles P1-P40；counter-examples X1-X45；frameworks F1-F4；glossary 约 55 条。
