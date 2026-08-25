# DIGEST — OmniSwitch 6860/6860E/6860N Hardware Users Guide 精华

本书是 ALE VC 堆叠接入交换机 OS6860 家族的硬件手册（115 页，15 个 1U 机型三代同堂：基础/E/N）。核心卖点：三代同包络演进——基础代 20G VC 口最省钱、E 代协处理器+EMP+私有 HPoE 60/75W、N 代 bt 95W+25G SFP28/QSFP28 VFL+M 型上联模块槽；7 款电源（150W-2000W）；Fast/Perpetual PoE。全书沿"选型→安装→上电→PoE→监控"生命周期展开。

## 一、知识地图（三技能单元）

1. **机型与端口体系**（os6860-model-ports）：三代命名解码、20G VC 口/QSFP28 VFL、SFP28 四口组限速、上联模块四款、五色端口 LED（Ch1/Ch3，p14-60）。
2. **安装与供电**（os6860-install-power）：机架法兰+N 型后支架、七款电源与混插规则、N 型 PoE 预算矩阵、DC 接线（Ch2-Ch4，p18-103）。
3. **运维与排障**（os6860-ops-troubleshoot）：lanpower 全族、DG 三通道与 PDU 挤占公式、温度双阈值、LED 诊断（Ch2-Ch4，p18-103）。

## 二、三单元要点串讲

### 1. 机型与端口：三代同堂矩阵
命名（<<<PAGE 14>>>/<<<PAGE 15>>>）：`P`=PoE；`E`=协处理器+EMP+HPoE；`N`=bt 95W+25G；`U28`=全光；`Z`=多千兆；`M`=上联模块槽。三代端口演化（F4）：基础=千兆铜+4×SFP+ +2×20G VC→E=+协处理器/OK2/HPoE 60-75W（非 bt 合规，<<<PAGE 43>>>/<<<PAGE 46>>>）→N=bt 95W 全面化+SFP28 25G（四口组 31-34 禁 1G/10G 与 25G 混跑，<<<PAGE 48>>>/<<<PAGE 53>>>）+QSFP28 VFL。N 型五色端口 LED：绿=千兆/琥珀=PoE/蓝=2.5G/蓝黄=5G/品红=10G（<<<PAGE 60>>>）。功耗从基础代 46W 到 N-P48M 260W 翻数番；N 型 M/Z 机箱 44cm 深需后支架（<<<PAGE 52>>>）。

### 2. 安装与供电：七款电源与预算矩阵
双舱 1+1 热插拔（<<<PAGE 15>>>）。七款电源（<<<PAGE 69>>>）：非 PoE=BP/BP-D 150W；PoE=BP-PH 600W/BP-PX 920W；N 专属=N-BPPH/N-BPPX/N-BPXL 2000W（仅 P48M/P24M）。混插铁律：wattage 禁混（发 trap 且不支持电源插入即禁全部业务口，<<<PAGE 69>>>）；BP+BP-D 唯一例外（<<<PAGE 71>>>）。2000W 电源 115V 输入仅 1000W，230V 才满额（<<<PAGE 77>>>）。N 型预算矩阵（<<<PAGE 93>>>）：P48M 双 2000W(230V)=3390W 最高；P48Z 双 920W=1500W。OS-BPS 槽已停支持（<<<PAGE 29>>>）。

### 3. 运维与排障：三层预算闸门与 DG 挤占公式
三层预算（F2）：物理矩阵→priority disconnect 上限（920W→780W/600W→450W 每电源，<<<PAGE 99>>>）→Guard Band（剩余<口上限即拒新 PD，<<<PAGE 102>>>）。**本机型 Priority Disconnect 端口号越大优先级越高（48 最高→1 最低，<<<PAGE 100>>>），与接入系列通用方向相反**。DG 三通道（<<<PAGE 69>>>/<<<PAGE 70>>>）：SNMP 前 3 站+Syslog 前 3 服务器+4×OAM PDU；同时发 PDU 口数=10−服务器数（本书独有公式）。温度双阈值：Warning 可配不停机，Danger 固化关机手动恢复；VC 堆叠内逐机箱阈值独立（<<<PAGE 87>>>）。Fast PoE 上电数秒供电（FPGA 固化）+Perpetual PoE 软重启不断电（MCU 升级例外）（<<<PAGE 96>>>）。

## 三、本书在知识库中的位置

6860 定位 VC 堆叠千兆/多千兆接入中坚，上承 6360/6560（接入基础与多千兆）、侧邻 6865（加固型）/6870（多千兆 25G-200G 上行）、上接 6900v2（核心）。跨书易混点：①Priority Disconnect 口号方向本机型反向（越大越高）；②6860 wattage 禁混，6870 反而允许混插扩容；③console 波特率 9600（N 型 115200）与 6870 全系 115200 不同。

## 来源
OmniSwitch 6860/6860E/6860N Hardware Users Guide（Part No. 060390-10, Rev. W, 2025-12）。verified.md：cases C1-C25；principles P1-P45；counter-examples X1-X39；frameworks F1-F4；glossary 约 60 条。
