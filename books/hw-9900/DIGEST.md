# DIGEST — OmniSwitch 9900 Series Hardware Users Guide 精华

本书是 ALE 核心/园区骨干模块化机箱 OS9900 系列的硬件手册（74 页，两款机箱）。核心卖点：CMM/CFM/NI 全模块化架构 + 4 电源 N+1 负载分担 + VC-of-2 双机箱虚拟化 + PoE（HPoE 75W）。全书沿"机箱架构→安装上电→PoE→组件拆除"生命周期展开。

## 一、知识地图（三技能单元）

1. **机箱与模块体系**（os9900-chassis-modules）：9907/9912 选型矩阵、CMM/CFM 兼容组合决策表、slot2 双角色权衡、11 种 NI 谱系、VC-of-2（Ch1，p5-31）。
2. **安装与供电**（os9900-install-power）：组件安装标准序列、功率预算三步法（Power Left）、电源三不混、DC 75A/10AWG 接线（Ch1/Ch2，p28-49）。
3. **运维与排障**（os9900-ops-troubleshoot）：热插拔节律（拆 30s/插 5min）、CFM 120 秒窗口、NI 同类替换、CMM LED 诊断、lanpower 与 Priority Disconnect（Ch3/Ch4，p50-63）。

## 二、三单元要点串讲

### 1. 机箱与模块：兼容矩阵是生命线
9907=11RU 七槽（2 CMM+5 NI，32.83kg）；9912=17RU 十二槽（2 CMM+10 NI，64.36kg）；均 23" 深、仅前→后气流、CFM3/4 预留未激活（<<<PAGE 5>>>-<<<PAGE 15>>>）。CMM/CFM 只有三种同箱组合支持（旧体系/CMM+CFM2/CMM2+CFM2 对称），一切新旧混插 Not Supported；CMM2 需 AOS ≥8.10R2、CFM2 需 ≥8.9R1（<<<PAGE 17>>>/<<<PAGE 20>>>/<<<PAGE 22>>>）。9907 slot2 双角色：装 NI 只活前 8 口且失 CMM 冗余。9912 不支持 XNI-P48Z16/P24Z8/UP24Q2/U12Q 四种 NI。VC-of-2 双机箱仅三种对称组合。

### 2. 安装与供电：功率预算先行
组件插入中板功率需求即刻生效，预算不足则新组件不上电甚至中断数据流——变更前必查 `show chassis` Power Left（<<<PAGE 49>>>）。电源 OS99-PS-A（AC 1200/3000W 两档）/OS99-PS-D（DC 2500W）三不混：AC/DC 不可混、Hi(240V)/Lo(110V) 不可混（与 6900 家族相反）。DC 接线 75A 过流+双 10AWG+FCI PWRBLADE 连接器（<<<PAGE 30>>>/<<<PAGE 31>>>）。安装序列：空箱就位（禁满载搬运）→ CFM（先拆风扇托盘）→ NI → CMM → 核预算 → 电源 → 主 CMM 四绿判据（<<<PAGE 36-45>>>）。

### 3. 运维与排障：机箱级热插拔节律
拆件间隔 30 秒、插件间隔 5 分钟+LED 无错（<<<PAGE 63>>>）；单 CMM/CFM/电源不可热拆；CFM 热换 120 秒窗口且一次一块；NI 只能同类替换。LED 诊断：PRI/FAB 编码+五灯同闪=全部 CFM PCIe 失效（<<<PAGE 18>>>）。PoE：默认 operational disabled；lanpower slot service 是首次激活唯一途径；Priority Disconnect 端口优先 48 高→1 低（与接入系列相反）（<<<PAGE 52>>>/<<<PAGE 55>>>）。

## 三、本书在知识库中的位置

与 hw-6900v2（1U 汇聚/ToR）构成"盒式 vs 机箱"两级硬件线。跨书易混点：9900 电源 AC/DC 不可混而 6900 可混；9900 仅前→后气流而 6900 双向；Priority Disconnect 端口方向 9900 为 48 高 1 低、接入系列为 1 高 48 低。

## 来源
OmniSwitch 9900 Series Hardware Users Guide（Rev. S, 2025-12）。verified.md：cases C2-C27；principles P1-P40；counter-examples X1-X51；frameworks F1-F4；glossary 约 60 条。
