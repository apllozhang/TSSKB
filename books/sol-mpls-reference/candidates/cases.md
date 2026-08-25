# cases — sol-mpls-reference（作者亲自演练的案例，页码为真实标记）

- **C1 MPLS 五收益论证案例**：BGP-free core、简单查找、自愈、流量工程、统一基础设施逐条展开。<<<PAGE 5-6>>>
- **C2 双标签封装-解封端到端流程**："The iLER binds the customer's traffic from the SAP... by 'pushing' the Service Label... Then another Transport label is added... Once the packet reaches the eLER, the top label (transport label) is 'popped' and the Service Label is processed and also 'popped'." <<<PAGE 20-21>>>
- **C3 LDP 邻居发现与会话建立流程**："LSRs start sending UDP-based LDP Hello messages on all links... After Hello messages are exchanged... they attempt to establish an LDP session between them using TCP-based messages... negotiate LDP session parameters by exchanging LDP Initialization messages." <<<PAGE 12>>>
- **C4 T-LDP 与直连 LDP 的场景对比**：远端 LER 间服务标签交换、链路故障时会话保持。"T-LDP, as can be observed from the name 'targeted', uses unicast UDP communication for discovery and unicast TCP to establish the session." <<<PAGE 15>>>
- **C5 push/swap/pop 三操作数据面走包**："the iLER inserts or 'push' a label... it 'swaps' or changes the top label... all labels are 'popped' or removed before the packet is switched out." <<<PAGE 16>>>
- **C6 PHP 与 explicit NULL 的 QoS 保留对比案例**："When the last LSR removes the top label, the EXP bits are also removed... The explicit NULL... will preserve the EXP bits in the explicit NULL label." <<<PAGE 16-17>>>
- **C7 QoS uniform/pipe 双模式行为**："In uniform mode, the IP precedence value... is copied to the EXP bits... In pipe mode, the EXP value is set according to the Service Provider's policy." <<<PAGE 18>>>
- **C8 TTL uniform/pipe 双模式（L3VPN 减 2、L2VPN 不变）**："In case of a Layer 3 VPN, the TTL is decremented by 1 at the iLER and again at the eLER, while for Layer 2 VPN, the TTL is not changed." <<<PAGE 19>>>
- **C9 LSP ping 实测案例**："mpls ping ldp 1.1.1.4/32" 5 发 5 中，min/avg/max = 0.67/1.30/1.94 ms。<<<PAGE 44>>>
- **C10 LSP traceroute 实测案例**："mpls trace ldp 1.1.1.4/32" 逐跳 TTL 递增发现 "0 20.2.1.2 [Labels: implicit-null]"。<<<PAGE 44>>>
- **C11 MPLS backbone 五步配置案例（R1 视角）**：接口 → 单区域 OSPF（p2p+BFD+SPF delay 0）→ 安装 uosn-mpls-v1.deb 包 → mpls interface → mpls ldp interface。<<<PAGE 29-31>>>
- **C12 LDP-VPLS 五步配置案例**：access port → SDP（far-end）→ service vpls vplsid + signaling ldp → SAP port 1/1/4:0 → bind-sdp 102 103（mesh，R1/R6/R7）。<<<PAGE 33-34>>>
- **C13 BGP-VPLS 四步配置案例**："ip bgp address-family l2vpn-vpls" + neighbor activate l2vpn-vpls + "service 2 vpls vplsid 11 signaling bgp ve-id 1" + SAP。<<<PAGE 34-35>>>
- **C14 VPWS 四步配置案例**：service vpws vcid 100 → SDP far-end → bind-sdp 20 spoke → 两端 SAP port 1/1/1:0、1/1/2:0，"The above configuration will setup a virtual bridge between port 1/1/1 on PE1 and port 1/1/2 on PE2." <<<PAGE 41-42>>>
- **C15 验证命令族全景案例**：show mpls / ftn-table / ilm-table / forwarding-table / ldp [neighbor|session]；show service [vpls|vpws|bind-sdp|mesh-sdp]；show ip bgp l2vpn-vpls [path]；show mac-learning domain vpls。<<<PAGE 31-44>>>
- **C16 FTN/ILM 表项解读案例**："FTN Code: B - BGP, L - LDP; OpCode: 1 = PUSH, 2 = POP, 3 = SWAP" 配真实表项输出。<<<PAGE 32>>>
- **C17 LDP 会话协商结果案例**："Advertisement mode = Downstream Unsolicited, Label retention mode = Liberal, Graceful restart = Enabled, Restarting mode = Helper." <<<PAGE 33>>>
- **C18 BGP VPLS 自动发现结果案例**："show ip bgp l2vpn-vpls path 50" 展示 VPLS-ID 50、VE Block Offset 1、Label Base 53122、Ext Community RT+MTU:9194。<<<PAGE 38-39>>>
