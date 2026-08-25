# DIGEST — Network Security Guidelines + 视频监控白皮书 精华

本书册由两份文档构成（页码连续）：DOC1 为 ALE 全栈安全加固技术简报（p1-86，OmniSwitch/Stellar WLAN/OmniVista，按管理面/控制面/数据面三平面 × 三产品域组织）；DOC2 为视频监控网络全生命周期白皮书（p87-100，NLM 7 阶段方法论）。版本基线 AOS 8.10R2 / AWOS 5.0.1 / OV2500 R4.9.1 / Cirrus R10.4.3。

## 一、知识地图（四技能单元）

1. **五层框架与三平面体系**（sol-sec-five-layer-framework）：安全是过程、五层集成框架、Secure By Design 认证、PSIRT/补丁、物理边界（p5-10）。
2. **协议加固与替换表**（sol-sec-protocol-hardening）：路由/keychain 认证、STP/ARP/DHCP/IPv6 防护、MACsec/LPS、不安全协议替换决策表（p12、30-47）。
3. **设备准入与管理面防护**（sol-sec-device-access）：默认口令、OOB/管理 VRF、SSH PKA、IP 锁定、AAA/SNMPv3/PKI、CC/JITC/FIPS 模式、OmniVista 2FA/API（p9-30、71-85）。
4. **NLM 生命周期**（sol-sec-nlm-lifecycle）：视频监控 7 阶段、Five S's、Lightning Config、wIPS/WPA3 无线配套、冗余升级、退役擦除（p47-100）。

## 二、四单元要点串讲

### 1. 框架层：安全是过程
"Security is not a tangible product"——多层纵深防御是唯一正道（<<<PAGE 5>>>）。ALE 五层框架从用户/设备/应用/网络到 IoT 容器隔离；Secure By Design 背书：签名镜像（RSA-4096/SHA-256）、ASLR、默认 DoS 过滤、CC EAL2/FIPS/TAA（<<<PAGE 6>>>）。补丁与物理访问是两条底线：公开漏洞即攻击武器（<<<PAGE 7>>>）；控制台直连可重置口令、插孔直通防火墙内网（<<<PAGE 8-11>>>）。

### 2. 协议加固：控制面+数据面清单化
开机默认全开服务端口是攻击面——先全关再按需开（<<<PAGE 12>>>）。替换表：Telnet→SSH、FTP/TFTP→SFTP/SCP、SNMPv1/2c→v3、HTTP→HTTPS。控制面：OSPF keychain 轮换（最安全）、Root Guard/TCN/BPDU 三防、LLDP Agent Security 防 rogue、ARP/GARP 防欺骗、DHCP Snooping+DAI、IPv6 三件套、NTP 认证、ICMP 裁剪。数据面：MACsec/MKA 链路加密、禁定向广播、IPv6 邻居缓存限额、边缘 LPS（<<<PAGE 30-47>>>）。

### 3. 管理面：三道闸与四种安全模式
物理/引导层（U-boot 口令+镜像校验）→ 通道层（OOB 优先→管理 VRF→白名单 64 IP）→ 认证层（强口令→SSH 强加密+PKA→IP 锁定 128 IP→AAA/RADIUS over TLS→MFA）。SNMPv3 按有无 PKI 选 TSM/USM。安全模式互斥四选：ASA enhanced（常规）、CC（默认 admin 仅装机）、JITC（军规：口令≥15、SSH 每小时/GB rekey）、FIPS。OmniVista：全用户 2FA、Network ID 上线、API 凭据不入代码（<<<PAGE 9-30、71-85>>>）。

### 4. NLM：7 阶段全程管理
"装完就不管"不成立。规划用 Five S's（Software/Surveillance IoT/Servers-Storage/Switches/Services-Support）→ 部署用 Lightning Config（50 分钟培训→5 分钟装机）与 UNP → 运营用 Milestone VMS 插件/Z-Score 异常检测/Quarantine Manager 联动 IPS 隔离 → 维护靠冗余零停机升级 → 升级引入 AI Network Advisor → 合规对接网络保险 → 退役按隐私法擦除。无线配套：wIPS rogue 治理组合拳、WPA3/SAE、OWE、客户端隔离（<<<PAGE 47-100>>>）。

## 三、本书在知识库中的位置
本书册是 ALE 安全域的"总纲"：交换机细节配 hw-* 与 aos810-switch-mgmt，无线细节配 stellar-wlan-adv-deploy / bp-stellar-ap-datasheets，网管配 ov2500-*。独特价值是三平面审计清单与 NLM 方法论，可直接当加固基线模板用。跨书易混点：CC/JITC/FIPS 三模式互斥且收紧力度递进；DHCP Option-82 与 Snooping 互斥。

## 来源
DOC1 network-infrasctructure-solution-security-tech-brief-en.pdf（p1-86）；DOC2 maximizing-security-and-performance-whitepaper-en.pdf（p87-100）。verified.md：cases C1-C20；principles P1-P92；counter-examples X1-X27；frameworks F1-F4；glossary 89 条。
