import pyirk as p
import sympy as sp

from ipydex import IPS, activate_ips_on_exception  # noqa

ct = p.irkloader.load_mod_from_path(r"C:\Users\Julius Fiedler\Documents\Code\irk\irk-data\ocse\control_theory1.py", prefix="ct")
ma = ct.ma
ag = ma.ag

__URI__ = "irk:/ocse/0.2/auto_import_empty"

keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)

# these entities are declared here all at once in order to avoid referencing issues when setting relations.
# the relations of these entities are set below with the update method. This update method is called exactly once.
I39529 = p.create_item(R1__has_label="European Commission")
I74938 = p.create_item(R1__has_label="publication: Harnessing the economic benefi")
I85012 = p.create_item(R1__has_label="Rattani, A.")
I99712 = p.create_item(R1__has_label="Reddy, N.")
I94362 = p.create_item(R1__has_label="Derakhshani, R.")
I85528 = p.create_item(R1__has_label="publication: Multi-biometric Convolutional ")
I2855 = p.create_item(R1__has_label="BBVA")
I46793 = p.create_item(R1__has_label="publication: Biometrics and machine learnin")
I90963 = p.create_item(R1__has_label="Amerini, I.")
I54975 = p.create_item(R1__has_label="Li, C.-T.")
I72751 = p.create_item(R1__has_label="Caldelli, R.")
I80078 = p.create_item(R1__has_label="publication: Social network identification ")
I5210 = p.create_item(R1__has_label="Ingle P. Y.")
I32782 = p.create_item(R1__has_label="Kim, Y. G.")
I91760 = p.create_item(R1__has_label="publication: Real-time abnormal object dete")
I91215 = p.create_item(R1__has_label="Tan, X.")
I81970 = p.create_item(R1__has_label="Qin, T.")
I68229 = p.create_item(R1__has_label="F. Soong")
I64747 = p.create_item(R1__has_label="T.-Y. Liu")
I39757 = p.create_item(R1__has_label="publication: A survey on neural speech synt")
I30227 = p.create_item(R1__has_label="publication: ChatGPT: Optimizing language m")
I24132 = p.create_item(R1__has_label="Hong, T.")
I14404 = p.create_item(R1__has_label="Choi, J. A.")
I65317 = p.create_item(R1__has_label="Lim, K.")
I25665 = p.create_item(R1__has_label="Kim, P.")
I85099 = p.create_item(R1__has_label="publication: Enhancing personalized ads usi")
I97353 = p.create_item(R1__has_label="McKee, S. A.")
I47693 = p.create_item(R1__has_label="publication: Reflections on the memory wall")
I17571 = p.create_item(R1__has_label="Mehonic, A.")
I63422 = p.create_item(R1__has_label="Kenyon, A. J.")
I91057 = p.create_item(R1__has_label="publication: Brain-inspired computing needs")
I86040 = p.create_item(R1__has_label="Zhang, C.")
I60665 = p.create_item(R1__has_label="et al.")
I36571 = p.create_item(R1__has_label="publication: IMLBench: A machine learning b")
I76227 = p.create_item(R1__has_label="Li, F.")
I68467 = p.create_item(R1__has_label="Ye, Y.")
I11040 = p.create_item(R1__has_label="Tian, Z.")
I40507 = p.create_item(R1__has_label="Zhang, X.")
I46602 = p.create_item(R1__has_label="publication: CPU versus GPU: which can perf")
I75913 = p.create_item(R1__has_label="Farabet, C.")
I32043 = p.create_item(R1__has_label="Poulet, C.")
I45775 = p.create_item(R1__has_label="Han, J. Y.")
I88802 = p.create_item(R1__has_label="LeCun, Y.")
I89671 = p.create_item(R1__has_label="publication: CNP: An FPGA-based processor f")
I5377 = p.create_item(R1__has_label="publication: NeuFlow: A runtime reconfigura")
I79564 = p.create_item(R1__has_label="publication: Optimizing FPGA-based accelera")
I67803 = p.create_item(R1__has_label="Chakradhar, S.")
I37074 = p.create_item(R1__has_label="Sankaradas, M.")
I34513 = p.create_item(R1__has_label="Jakkula, V.")
I4484 = p.create_item(R1__has_label="Cadambi, S.")
I93059 = p.create_item(R1__has_label="publication: A dynamically configurable cop")
I89877 = p.create_item(R1__has_label="Wei X.")
I48946 = p.create_item(R1__has_label="publication: Automated systolic array archi")
I44836 = p.create_item(R1__has_label="Guo, K.")
I63006 = p.create_item(R1__has_label="publication: Neural Network Accelerator Com")
I99459 = p.create_item(R1__has_label="Jouppi, N. P.")
I48965 = p.create_item(R1__has_label="publication: In-datacenter performance anal")
I85347 = p.create_item(R1__has_label="publication: AI Chip Amazon Inferentia AWS")
I45993 = p.create_item(R1__has_label="Talpes, E.")
I24141 = p.create_item(R1__has_label="publication: Compute solution for Tesla's f")
I35428 = p.create_item(R1__has_label="Reuther, A.")
I10778 = p.create_item(R1__has_label="et al")
I69974 = p.create_item(R1__has_label="publication: AI and ML Accelerator Survey a")
I70494 = p.create_item(R1__has_label="Fick, L.")
I87242 = p.create_item(R1__has_label="Skrzyniarz, S.")
I93860 = p.create_item(R1__has_label="Parikh, M.")
I78857 = p.create_item(R1__has_label="Henry, M. B.")
I94601 = p.create_item(R1__has_label="Fick, D.")
I52917 = p.create_item(R1__has_label="publication: Analog matrix processor for ed")
I86787 = p.create_item(R1__has_label="publication: Gyrfalcon Unveils Fourth AI Ac")
I21123 = p.create_item(R1__has_label="Sebastian, A.")
I39708 = p.create_item(R1__has_label="Le Gallo, M.")
I93276 = p.create_item(R1__has_label="Khaddam-Aljameh, R.")
I53205 = p.create_item(R1__has_label="Eleftheriou, E.")
I87136 = p.create_item(R1__has_label="publication: Memory devices and application")
I41902 = p.create_item(R1__has_label="Zheng, N.")
I85417 = p.create_item(R1__has_label="Mazumder, P.")
I97657 = p.create_item(R1__has_label="publication: Learning in energy-efficient n")
I29872 = p.create_item(R1__has_label="Orchard, G.")
I21621 = p.create_item(R1__has_label="publication: Efficient Neuromorphic Signal ")
I87604 = p.create_item(R1__has_label="publication: Microchips that mimic the huma")
I58690 = p.create_item(R1__has_label="Davies, M.")
I7533 = p.create_item(R1__has_label="publication: Advancing neuromorphic computi")
I28840 = p.create_item(R1__has_label="Barnell, M.")
I49189 = p.create_item(R1__has_label="Raymond, C.")
I8849 = p.create_item(R1__has_label="Wilson, M.")
I74720 = p.create_item(R1__has_label="Isereau, D.")
I95219 = p.create_item(R1__has_label="Cicotta, C.")
I45292 = p.create_item(R1__has_label="publication: Target classification in synth")
I90863 = p.create_item(R1__has_label="Viale, A.")
I66609 = p.create_item(R1__has_label="Marchisio, A.")
I26240 = p.create_item(R1__has_label="Martina, M.")
I16712 = p.create_item(R1__has_label="Masera, G.")
I26637 = p.create_item(R1__has_label="Shafique, M.")
I73173 = p.create_item(R1__has_label="publication: CarSNN: An efficient spiking n")
I77352 = p.create_item(R1__has_label="publication: Innatera Unveils Neuromorphic ")
I12092 = p.create_item(R1__has_label="Pei, J.")
I95662 = p.create_item(R1__has_label="publication: Towards artificial general int")
I50118 = p.create_item(R1__has_label="Merolla, P. A.")
I52771 = p.create_item(R1__has_label="publication: A million spiking-neuron integ")
I38213 = p.create_item(R1__has_label="Adam, G. C.")
I9385 = p.create_item(R1__has_label="Khiat, A.")
I34131 = p.create_item(R1__has_label="Prodromakis, T.")
I47402 = p.create_item(R1__has_label="publication: Challenges hindering memristiv")
I8777 = p.create_item(R1__has_label="Sung, C.")
I61519 = p.create_item(R1__has_label="Hwang, H.")
I89808 = p.create_item(R1__has_label="Yoo, I. K.")
I73802 = p.create_item(R1__has_label="publication: Perspective: A review on memri")
I63079 = p.create_item(R1__has_label="Deng, L.")
I92934 = p.create_item(R1__has_label="publication: Energy consumption analysis fo")
I97154 = p.create_item(R1__has_label="Yu, S.")
I84376 = p.create_item(R1__has_label="Wu, Y.")
I72298 = p.create_item(R1__has_label="Jeyasingh, R.")
I34559 = p.create_item(R1__has_label="Kuzum, D.")
I83048 = p.create_item(R1__has_label="Wong, H. S. P.")
I71732 = p.create_item(R1__has_label="publication: An electronic synapse device b")
I16765 = p.create_item(R1__has_label="Shulaker, M. M.")
I18578 = p.create_item(R1__has_label="publication: Three-dimensional integration ")
I87992 = p.create_item(R1__has_label="Li, C.")
I44440 = p.create_item(R1__has_label="publication: Three-dimensional crossbar arr")
I58468 = p.create_item(R1__has_label="Yoon, J. H.")
I47470 = p.create_item(R1__has_label="publication: Truly electroforming-free and ")
I82062 = p.create_item(R1__has_label="Choi, B. J.")
I58157 = p.create_item(R1__has_label="publication: High-speed and low-energy nitr")
I27966 = p.create_item(R1__has_label="Strukov, D. B.")
I21352 = p.create_item(R1__has_label="Snider, G. S.")
I46285 = p.create_item(R1__has_label="Stewart, D. R.")
I6912 = p.create_item(R1__has_label="Williams, R. S.")
I26347 = p.create_item(R1__has_label="publication: The missing memristor found")
I24977 = p.create_item(R1__has_label="publication: FUJITSU SEMICONDUCTOR MEMORY S")
I9309 = p.create_item(R1__has_label="publication: Everspin | The MRAM Company")
I93983 = p.create_item(R1__has_label="Yole Group")
I18158 = p.create_item(R1__has_label="Stathopoulos, S.")
I63066 = p.create_item(R1__has_label="publication: Multibit memory operation of m")
I55774 = p.create_item(R1__has_label="Wu, W.")
I3236 = p.create_item(R1__has_label="publication: Demonstration of a multi-level")
I95705 = p.create_item(R1__has_label="Yang, J.")
I78145 = p.create_item(R1__has_label="publication: Thousands of conductance level")
I93419 = p.create_item(R1__has_label="Goux, L.")
I98801 = p.create_item(R1__has_label="publication: Ultralow sub-500nA operating c")
I11520 = p.create_item(R1__has_label="Li, H.")
I47520 = p.create_item(R1__has_label="publication: Memristive crossbar arrays for")
I59694 = p.create_item(R1__has_label="Lin, P.")
I79160 = p.create_item(R1__has_label="publication: Three-dimensional memristor ci")
I56829 = p.create_item(R1__has_label="Ishii, M.")
I10094 = p.create_item(R1__has_label="publication: On-Chip Trainable 1.4M 6T2R PC")
I33159 = p.create_item(R1__has_label="publication: Efficient and self-adaptive in")
I42033 = p.create_item(R1__has_label="Yao, P.")
I92000 = p.create_item(R1__has_label="publication: Fully hardware-implemented mem")
I7940 = p.create_item(R1__has_label="Correll, J. M.")
I69530 = p.create_item(R1__has_label="publication: An 8-bit 20.7 TOPS/W Multi-Lev")
I68259 = p.create_item(R1__has_label="Cai, F.")
I29098 = p.create_item(R1__has_label="publication: A fully integrated reprogramma")
I82346 = p.create_item(R1__has_label="Hung, J.-M.")
I90071 = p.create_item(R1__has_label="publication: An 8-Mb DC-Current-Free Binary")
I88962 = p.create_item(R1__has_label="Xue, C.-X.")
I12398 = p.create_item(R1__has_label="publication: 15.4 A 22nm 2Mb ReRAM Compute-")
I33364 = p.create_item(R1__has_label="Wan, W.")
I8173 = p.create_item(R1__has_label="publication: A compute-in-memory chip based")
I98878 = p.create_item(R1__has_label="Yin, S.")
I76458 = p.create_item(R1__has_label="Sun, X.")
I23249 = p.create_item(R1__has_label="Seo, J. S.")
I38620 = p.create_item(R1__has_label="publication: High-throughput in-memory comp")
I76087 = p.create_item(R1__has_label="Yan, X.")
I48237 = p.create_item(R1__has_label="publication: Robust Ag/ZrO2/WS2/Pt Memristo")
I61398 = p.create_item(R1__has_label="Chen, Q.")
I99103 = p.create_item(R1__has_label="publication: Improving the recognition accu")
I28976 = p.create_item(R1__has_label="Wang, Y.")
I66639 = p.create_item(R1__has_label="publication: High on/off ratio black phosph")
I34380 = p.create_item(R1__has_label="Xue, F.")
I37464 = p.create_item(R1__has_label="publication: Giant ferroelectric resistance")
I11681 = p.create_item(R1__has_label="Pan, W.-Q.")
I41069 = p.create_item(R1__has_label="publication: Strategies to improve the accu")
I5868 = p.create_item(R1__has_label="Seo, S.")
I61689 = p.create_item(R1__has_label="publication: Artificial optic-neural synaps")
I37167 = p.create_item(R1__has_label="Chandrasekaran, S.")
I12287 = p.create_item(R1__has_label="Simanjuntak, F. M.")
I86221 = p.create_item(R1__has_label="Saminathan, R.")
I47202 = p.create_item(R1__has_label="Panda, D.")
I29376 = p.create_item(R1__has_label="Tseng, T. Y.")
I69517 = p.create_item(R1__has_label="publication: Improving linearity by introdu")
I1362 = p.create_item(R1__has_label="Zhang, B.")
I57709 = p.create_item(R1__has_label="publication: 90% yield production of polyme")
I73000 = p.create_item(R1__has_label="Feng, X.")
I49887 = p.create_item(R1__has_label="publication: Self-selective multi-terminal ")
I67827 = p.create_item(R1__has_label="publication: HERMES-Core-A 1.59-TOPS/mm2PCM")
I22963 = p.create_item(R1__has_label="Narayanan, P.")
I17132 = p.create_item(R1__has_label="publication: Fully on-chip MAC at 14 nm ena")
I74155 = p.create_item(R1__has_label="publication: A 64-core mixed-signal in-memo")
I18985 = p.create_item(R1__has_label="Murmann, B.")
I87613 = p.create_item(R1__has_label="publication: Mixed-signal computing for dee")
I95725 = p.create_item(R1__has_label="Jiang, Z.")
I64045 = p.create_item(R1__has_label="Seok, M.")
I79243 = p.create_item(R1__has_label="publication: XNOR-SRAM: In-memory computing")
I52752 = p.create_item(R1__has_label="Biswas, A.")
I49299 = p.create_item(R1__has_label="Chandrakasan, A. P.")
I51187 = p.create_item(R1__has_label="publication: CONV-SRAM: An energy-efficient")
I59886 = p.create_item(R1__has_label="Valavi, H.")
I75602 = p.create_item(R1__has_label="Ramadge, P. J.")
I26646 = p.create_item(R1__has_label="Nestler, E.")
I22852 = p.create_item(R1__has_label="Verma, N.")
I77881 = p.create_item(R1__has_label="publication: A 64-Tile 2.4-Mb In-memory-com")
I49586 = p.create_item(R1__has_label="Khwa, W. S.")
I55924 = p.create_item(R1__has_label="publication: A 65nm 4Kb algorithm-dependent")
I97111 = p.create_item(R1__has_label="publication: In-memory computing: advances ")
I13415 = p.create_item(R1__has_label="Diorio, C.")
I84363 = p.create_item(R1__has_label="Hasler, P.")
I51358 = p.create_item(R1__has_label="Minch, A.")
I61262 = p.create_item(R1__has_label="Mead, C. A.")
I69614 = p.create_item(R1__has_label="publication: A single-transistor silicon sy")
I91097 = p.create_item(R1__has_label="Merrikh-Bayat, F.")
I84267 = p.create_item(R1__has_label="publication: High-performance mixed-signal ")
I32602 = p.create_item(R1__has_label="Wang, P.")
I91573 = p.create_item(R1__has_label="publication: Three-dimensional NAND flash f")
I60259 = p.create_item(R1__has_label="Bavandpour, M.")
I73590 = p.create_item(R1__has_label="Sahay, S.")
I74604 = p.create_item(R1__has_label="Mahmoodi, M. R.")
I66704 = p.create_item(R1__has_label="publication: 3DaCortex: an ultra-compact en")
I59620 = p.create_item(R1__has_label="Chu, M.")
I38907 = p.create_item(R1__has_label="publication: Neuromorphic hardware system f")
I72736 = p.create_item(R1__has_label="Yeo, I.")
I31938 = p.create_item(R1__has_label="Gi, S. G.")
I15972 = p.create_item(R1__has_label="Lee, B. G.")
I70751 = p.create_item(R1__has_label="publication: Stuck-at-fault tolerant scheme")
I86194 = p.create_item(R1__has_label="Cortes, C.")
I72160 = p.create_item(R1__has_label="Burges, C. J. C.")
I43694 = p.create_item(R1__has_label="publication: MNIST handwritten digit databa")
I77914 = p.create_item(R1__has_label="Krizhevsky, A.")
I10506 = p.create_item(R1__has_label="Nair, V.")
I67834 = p.create_item(R1__has_label="Hinton, G.")
I8593 = p.create_item(R1__has_label="publication: The CIFAR-10 dataset.")
I85158 = p.create_item(R1__has_label="Deng, J.")
I36804 = p.create_item(R1__has_label="publication: ImageNet: A large-scale hierar")
I65099 = p.create_item(R1__has_label="Simonyan, K.")
I16673 = p.create_item(R1__has_label="Zisserman, A.")
I33540 = p.create_item(R1__has_label="publication: Very deep convolutional networ")
I10736 = p.create_item(R1__has_label="He, K.")
I36840 = p.create_item(R1__has_label="Ren, S.")
I81192 = p.create_item(R1__has_label="Sun, J.")
I10867 = p.create_item(R1__has_label="publication: Deep Residual Learning for Ima")
I4130 = p.create_item(R1__has_label="Chen, P. Y.")
I52096 = p.create_item(R1__has_label="Peng, X.")
I63907 = p.create_item(R1__has_label="publication: NeuroSim: A circuit-level macr")
I28196 = p.create_item(R1__has_label="Wang, Q.")
I3591 = p.create_item(R1__has_label="Wang, X.")
I59167 = p.create_item(R1__has_label="Lee, S. H.")
I79716 = p.create_item(R1__has_label="Meng, F.-H.")
I88339 = p.create_item(R1__has_label="Lu W. D.")
I21466 = p.create_item(R1__has_label="publication: A Deep Neural Network Accelera")
I96420 = p.create_item(R1__has_label="Kim, H.")
I18805 = p.create_item(R1__has_label="Nili, H.")
I2133 = p.create_item(R1__has_label="publication: 4K-memristor analog-grade pass")
I32206 = p.create_item(R1__has_label="Inc. The Mathworks")
I64611 = p.create_item(R1__has_label="publication: MATLAB")
I83149 = p.create_item(R1__has_label="Amirsoleimani, A.")
I43547 = p.create_item(R1__has_label="publication: In-memory vector-matrix multip")
I98535 = p.create_item(R1__has_label="Chakraborty, I.")
I94285 = p.create_item(R1__has_label="publication: Resistive crossbars as approxi")
I15284 = p.create_item(R1__has_label="Jain, S.")
I68828 = p.create_item(R1__has_label="publication: Neural network accelerator des")
I60267 = p.create_item(R1__has_label="Ankit, A.")
I46809 = p.create_item(R1__has_label="publication: PANTHER: A Programmable Archit")
I25926 = p.create_item(R1__has_label="Mochida, R.")
I34829 = p.create_item(R1__has_label="publication: A 4M synapses integrated analo")
I78886 = p.create_item(R1__has_label="Su, F.")
I25994 = p.create_item(R1__has_label="publication: A 462GOPs/J RRAM-based nonvola")
I30847 = p.create_item(R1__has_label="Han J.")
I94613 = p.create_item(R1__has_label="Orshansky, M.")
I79574 = p.create_item(R1__has_label="publication: Approximate computing: An emer")
I47369 = p.create_item(R1__has_label="Kiani, F.")
I12147 = p.create_item(R1__has_label="Yin, J.")
I84254 = p.create_item(R1__has_label="Wang, Z.")
I1837 = p.create_item(R1__has_label="Joshua Yang, J.")
I56976 = p.create_item(R1__has_label="Xia, Q.")
I51104 = p.create_item(R1__has_label="publication: A fully hardware-based memrist")
I13464 = p.create_item(R1__has_label="Gokmen, T.")
I36870 = p.create_item(R1__has_label="Vlasov, Y.")
I58774 = p.create_item(R1__has_label="publication: Acceleration of deep neural ne")
I88474 = p.create_item(R1__has_label="Fouda, M. E.")
I66600 = p.create_item(R1__has_label="Lee, S.")
I75844 = p.create_item(R1__has_label="Lee, J.")
I73963 = p.create_item(R1__has_label="Eltawil, A.")
I41910 = p.create_item(R1__has_label="Kurdahi, F.")
I79146 = p.create_item(R1__has_label="publication: Mask technique for fast and ef")
I73731 = p.create_item(R1__has_label="Prezioso, M.")
I78650 = p.create_item(R1__has_label="publication: Training and operation of an i")
I15050 = p.create_item(R1__has_label="Hu, M.")
I10578 = p.create_item(R1__has_label="publication: Memristor crossbar-based neuro")
I8748 = p.create_item(R1__has_label="publication: Dot-product engine for neuromo")
I45648 = p.create_item(R1__has_label="Liu, C.")
I66282 = p.create_item(R1__has_label="Strachan, J. P.")
I71268 = p.create_item(R1__has_label="Li, H. H.")
I56031 = p.create_item(R1__has_label="publication: Rescuing memristorbased neurom")
I21727 = p.create_item(R1__has_label="Romero-Zaliz, R.")
I49840 = p.create_item(R1__has_label="Pérez, E.")
I6297 = p.create_item(R1__has_label="Jiménez-Molinos, F.")
I39887 = p.create_item(R1__has_label="Wenger, C.")
I85070 = p.create_item(R1__has_label="Roldán, J. B.")
I55806 = p.create_item(R1__has_label="publication: Study of quantized hardware de")
I43511 = p.create_item(R1__has_label="publication: Advanced temperature dependent")
I22386 = p.create_item(R1__has_label="Pérez-Bosch Quesada, E.")
I67258 = p.create_item(R1__has_label="publication: Toward reliable compact modeli")
I97751 = p.create_item(R1__has_label="Xia, L.")
I82053 = p.create_item(R1__has_label="publication: Stuck-at Fault Tolerance in RR")
I67957 = p.create_item(R1__has_label="publication: CMOS-integrated nanoscale memr")
I95101 = p.create_item(R1__has_label="Pedretti, G.")
I30784 = p.create_item(R1__has_label="publication: Redundancy and analog slicing ")
I74053 = p.create_item(R1__has_label="publication: Redundancy and analog slicing 2")
I60580 = p.create_item(R1__has_label="publication: Fully memristive neural networ")
I88740 = p.create_item(R1__has_label="T. Rabuske")
I11114 = p.create_item(R1__has_label="J. Fernandes")
I13786 = p.create_item(R1__has_label="publication: Charge-Sharing SAR ADCs for lo")
I22195 = p.create_item(R1__has_label="Kumar, P.")
I93525 = p.create_item(R1__has_label="publication: Hybrid architecture based on t")
I18596 = p.create_item(R1__has_label="Krestinskaya, O.")
I53810 = p.create_item(R1__has_label="Salama, K. N.")
I15074 = p.create_item(R1__has_label="James, A. P.")
I64389 = p.create_item(R1__has_label="publication: Learning in memristive neural ")
I62101 = p.create_item(R1__has_label="Chua, L. O.")
I3120 = p.create_item(R1__has_label="Tetzlaff, R.")
I98516 = p.create_item(R1__has_label="Slavova, A.")
I32025 = p.create_item(R1__has_label="publication: Memristor Computing Systems")
I9682 = p.create_item(R1__has_label="Oh, S.")
I22597 = p.create_item(R1__has_label="publication: Energy-efficient Mott activati")
I2571 = p.create_item(R1__has_label="Ambrogio, S.")
I44753 = p.create_item(R1__has_label="publication: Equivalent-accuracy accelerate")
I96741 = p.create_item(R1__has_label="Bocquet, M.")
I88080 = p.create_item(R1__has_label="publication: In-memory and error-immune dif")
I26547 = p.create_item(R1__has_label="Cheng, M.")
I48203 = p.create_item(R1__has_label="publication: TIME: A Training-in-memory arc")
I32397 = p.create_item(R1__has_label="Chi, P.")
I89377 = p.create_item(R1__has_label="publication: PRIME: A novel processing-in-m")
I53917 = p.create_item(R1__has_label="Choubey, B.")
I4628 = p.create_item(R1__has_label="publication: Memristive GAN in Analog")
I22186 = p.create_item(R1__has_label="Li, G. H. Y.")
I62904 = p.create_item(R1__has_label="publication: All-optical ultrafast ReLU fun")
I98627 = p.create_item(R1__has_label="Ando, K.")
I73752 = p.create_item(R1__has_label="publication: BRein memory: a single-chip bi")
I77303 = p.create_item(R1__has_label="Price, M.")
I14787 = p.create_item(R1__has_label="Glass, J.")
I95781 = p.create_item(R1__has_label="publication: A scalable speech recognizer w")
I98271 = p.create_item(R1__has_label="publication: A 1.06-to-5.09 TOPS/W reconfig")
I91887 = p.create_item(R1__has_label="Chen, Y. H.")
I80011 = p.create_item(R1__has_label="Krishna, T.")
I97489 = p.create_item(R1__has_label="Emer, J. S.")
I77461 = p.create_item(R1__has_label="Sze, V.")
I32449 = p.create_item(R1__has_label="publication: Eyeriss: An energy-efficient r")
I82221 = p.create_item(R1__has_label="Lazzaro, J.")
I23208 = p.create_item(R1__has_label="Ryckebusch, S. M.")
I81899 = p.create_item(R1__has_label="Mahowald, A.")
I12477 = p.create_item(R1__has_label="publication: Winner-Take-All Networks of O(")
I43845 = p.create_item(R1__has_label="Andreou, A. G.")
I27217 = p.create_item(R1__has_label="publication: Current-mode subthreshold MOS ")
I42841 = p.create_item(R1__has_label="Pouliquen, P. O.")
I40548 = p.create_item(R1__has_label="Strohbehn, K.")
I94901 = p.create_item(R1__has_label="Jenkins, R. E.")
I95801 = p.create_item(R1__has_label="publication: Associative memory integrated ")
I62543 = p.create_item(R1__has_label="Starzyk, J. A.")
I62880 = p.create_item(R1__has_label="Fang, X.")
I11307 = p.create_item(R1__has_label="publication: CMOS current mode winner-take-")
I72302 = p.create_item(R1__has_label="DeWeerth, S. P.")
I78560 = p.create_item(R1__has_label="Morris, T. G.")
I52910 = p.create_item(R1__has_label="publication: CMOS current mode winner-takea")
I6510 = p.create_item(R1__has_label="Indiveri, G.")
I59370 = p.create_item(R1__has_label="publication: A current-mode hysteretic winn")
I43562 = p.create_item(R1__has_label="Tan, B. P.")
I99776 = p.create_item(R1__has_label="Wilson, D. M.")
I36552 = p.create_item(R1__has_label="publication: Semiparallel rank order filter")
I86940 = p.create_item(R1__has_label="Serrano, T.")
I84649 = p.create_item(R1__has_label="Linares-Barranco, B.")
I11737 = p.create_item(R1__has_label="publication: Modular current-mode highpreci")
I4937 = p.create_item(R1__has_label="Meador, J. L.")
I32825 = p.create_item(R1__has_label="Hylander, P. D.")
I77144 = p.create_item(R1__has_label="publication: Pulse Coded Winner-Take-All Ne")
I46246 = p.create_item(R1__has_label="El-Masry, E. I.")
I33641 = p.create_item(R1__has_label="Yang, H. K.")
I32743 = p.create_item(R1__has_label="Yakout, M. A.")
I26808 = p.create_item(R1__has_label="publication: Implementations of artificial ")
I86409 = p.create_item(R1__has_label="Choi, J.")
I44397 = p.create_item(R1__has_label="Sheu, B. J.")
I53384 = p.create_item(R1__has_label="publication: A high-precision vlsi winner-t")
I84035 = p.create_item(R1__has_label="Yu, H.")
I89773 = p.create_item(R1__has_label="Miyaoka, R. S.")
I54780 = p.create_item(R1__has_label="publication: A High-Speed and High-Precisio")
I31896 = p.create_item(R1__has_label="Lau, K. T.")
I66327 = p.create_item(R1__has_label="Lee, S. T.")
I63400 = p.create_item(R1__has_label="publication: A CMOS winner-takes-all circui")
I36418 = p.create_item(R1__has_label="He, Y.")
I68779 = p.create_item(R1__has_label="Sánchez-Sinencio, E.")
I11624 = p.create_item(R1__has_label="publication: Min-net winner-take-all CMOS i")
I91103 = p.create_item(R1__has_label="Demosthenous, A.")
I98003 = p.create_item(R1__has_label="Smedley, S.")
I76493 = p.create_item(R1__has_label="Taylor, J.")
I65504 = p.create_item(R1__has_label="publication: A CMOS analog winner-take-all ")
I56660 = p.create_item(R1__has_label="publication: Winner-Takes-All associative m")
I15377 = p.create_item(R1__has_label="Fish, A.")
I61179 = p.create_item(R1__has_label="Milrud, V.")
I31858 = p.create_item(R1__has_label="Yadid-Pecht, O.")
I82458 = p.create_item(R1__has_label="publication: High-speed and high-precision ")
I30242 = p.create_item(R1__has_label="Ohnhäuser, F.")
I13701 = p.create_item(R1__has_label="publication: Analog-Digital Converters for ")
I68953 = p.create_item(R1__has_label="Pavan, S.")
I38138 = p.create_item(R1__has_label="Schreier, R.")
I36635 = p.create_item(R1__has_label="Temes, G. C.")
I80819 = p.create_item(R1__has_label="publication: Understanding Delta-Sigma Data")
I26114 = p.create_item(R1__has_label="Walden, R. H.")
I17993 = p.create_item(R1__has_label="publication: Analog-to-digital converter su")
I39688 = p.create_item(R1__has_label="Harpe, P.")
I87435 = p.create_item(R1__has_label="Gao, H.")
I63949 = p.create_item(R1__has_label="Van Dommele, R.")
I59350 = p.create_item(R1__has_label="Cantatore, E.")
I93987 = p.create_item(R1__has_label="Van Roermund, A. H. M.")
I36907 = p.create_item(R1__has_label="publication: A 0.20 mm2 3 nW signal acquisi")
I22322 = p.create_item(R1__has_label="publication: ADC Performance Survey 1997-20")
I13679 = p.create_item(R1__has_label="publication: PUMA: A Programmable Ultra-eff")
I28334 = p.create_item(R1__has_label="Ni, L.")
I66551 = p.create_item(R1__has_label="publication: An energy-efficient matrix mul")
I36221 = p.create_item(R1__has_label="Lu, W. D.")
I6152 = p.create_item(R1__has_label="publication: RRAM-enabled AI Accelerator Ar")
I15365 = p.create_item(R1__has_label="Xiao, T. P.")
I75041 = p.create_item(R1__has_label="publication: On the Accuracy of Analog Neur")
I43110 = p.create_item(R1__has_label="publication: XNOR-RRAM: A scalable and para")
I3393 = p.create_item(R1__has_label="Zhang, W.")
I32055 = p.create_item(R1__has_label="publication: Neuro-inspired computing chips")
I99575 = p.create_item(R1__has_label="Shafiee, A.")
I80100 = p.create_item(R1__has_label="publication: ISAAC: A Convolutional Neural ")
I47541 = p.create_item(R1__has_label="Fujiki, D.")
I46178 = p.create_item(R1__has_label="Mahlke, S.")
I58992 = p.create_item(R1__has_label="Das, R.")
I97679 = p.create_item(R1__has_label="publication: In-memory data parallel proces")
I67161 = p.create_item(R1__has_label="Nourazar, M.")
I5530 = p.create_item(R1__has_label="Rashtchi, V.")
I15538 = p.create_item(R1__has_label="Azarpeyvand, A.")
I15436 = p.create_item(R1__has_label="publication: Memristor-based approximate ma")
I85361 = p.create_item(R1__has_label="Saberi, M.")
I68019 = p.create_item(R1__has_label="Lotfi, R.")
I3925 = p.create_item(R1__has_label="Mafinezhad, K.")
I9150 = p.create_item(R1__has_label="Serdijn, W. A.")
I29966 = p.create_item(R1__has_label="publication: Analysis of power consumption ")
I55344 = p.create_item(R1__has_label="Kull, L.")
I93933 = p.create_item(R1__has_label="publication: A 3.1 mW 8b 1.2 GS/s single-Ch")
I31314 = p.create_item(R1__has_label="Hagan, M.")
I94653 = p.create_item(R1__has_label="Demuth, H.")
I37296 = p.create_item(R1__has_label="Beale, M.")
I78153 = p.create_item(R1__has_label="De Jesús, O.")
I81477 = p.create_item(R1__has_label="publication: Neural Network Design")
I97169 = p.create_item(R1__has_label="Choi, S.")
I80229 = p.create_item(R1__has_label="Sheridan, P.")
I12368 = p.create_item(R1__has_label="publication: Data clustering using memristo")
I54164 = p.create_item(R1__has_label="publication: HERMES Core: A 14nm CMOS and P")
I48329 = p.create_item(R1__has_label="Kennedy, J.")
I10466 = p.create_item(R1__has_label="Eberhart, R.")
I85491 = p.create_item(R1__has_label="publication: Particle swarm optimization")
I87251 = p.create_item(R1__has_label="Goldberg, D. E.")
I1064 = p.create_item(R1__has_label="Holland, J. H.")
I82112 = p.create_item(R1__has_label="publication: Genetic Algorithms and machine")
I79938 = p.create_item(R1__has_label="Kirkpatrick, S.")
I30361 = p.create_item(R1__has_label="Gelatt, C. D.")
I18375 = p.create_item(R1__has_label="Vecchi, M. P.")
I45745 = p.create_item(R1__has_label="publication: Optimization by simulated anne")
I44585 = p.create_item(R1__has_label="Rumelhart, D. E.")
I82729 = p.create_item(R1__has_label="Hinton, G. E.")
I33331 = p.create_item(R1__has_label="Williams, R. J.")
I21301 = p.create_item(R1__has_label="publication: Learning representations by ba")
I40424 = p.create_item(R1__has_label="Dennis, J. E.")
I75542 = p.create_item(R1__has_label="Schnabel, R. B.")
I93813 = p.create_item(R1__has_label="publication: Numerical Methods for Unconstr")
I69907 = p.create_item(R1__has_label="Møller, M. F.")
I64828 = p.create_item(R1__has_label="publication: A scaled conjugate gradient al")
I78457 = p.create_item(R1__has_label="Powell, M. J. D.")
I97315 = p.create_item(R1__has_label="publication: Restart procedures for the con")
I71929 = p.create_item(R1__has_label="Fletcher, R.")
I89265 = p.create_item(R1__has_label="publication: Function minimization by conju")
I17113 = p.create_item(R1__has_label="Marquardt, D. W.")
I23478 = p.create_item(R1__has_label="publication: An algorithm for least-squares")
I39360 = p.create_item(R1__has_label="Riedmiller, M.")
I79037 = p.create_item(R1__has_label="Braun, H.")
I94678 = p.create_item(R1__has_label="publication: Direct adaptive method for fas")
I37221 = p.create_item(R1__has_label="Battiti, R.")
I11187 = p.create_item(R1__has_label="publication: First- and second-order method")
I9576 = p.create_item(R1__has_label="Bottou, L.")
I13450 = p.create_item(R1__has_label="publication: Stochastic gradient descent tr")
I72065 = p.create_item(R1__has_label="Li, M.")
I53665 = p.create_item(R1__has_label="Zhang, T.")
I75737 = p.create_item(R1__has_label="Chen, Y.")
I12456 = p.create_item(R1__has_label="Smola, A. J.")
I23048 = p.create_item(R1__has_label="publication: Efficient mini-batch training ")
I66505 = p.create_item(R1__has_label="Zamanidoost, E.")
I62828 = p.create_item(R1__has_label="Bayat, F. M.")
I31085 = p.create_item(R1__has_label="Strukov, D.")
I22251 = p.create_item(R1__has_label="Kataeva, I.")
I52492 = p.create_item(R1__has_label="publication: Manhattan rule training for me")
I5558 = p.create_item(R1__has_label="Duchi, J.")
I84355 = p.create_item(R1__has_label="Hazan, E.")
I43372 = p.create_item(R1__has_label="Singer, Y.")
I77183 = p.create_item(R1__has_label="publication: Adaptive subgradient methods f")
I82881 = p.create_item(R1__has_label="Geoffrey Hinton")
I79664 = p.create_item(R1__has_label="publication: Neural Networks for Machine Le")
I81700 = p.create_item(R1__has_label="Kingma, D. P.")
I51455 = p.create_item(R1__has_label="Ba, J. L.")
I24925 = p.create_item(R1__has_label="publication: Adam: A Method for Stochastic ")
I31684 = p.create_item(R1__has_label="Zeiler, M. D.")
I99538 = p.create_item(R1__has_label="publication: ADADELTA: An adaptive learning")
I33941 = p.create_item(R1__has_label="Xiong, X.")
I45772 = p.create_item(R1__has_label="publication: Reconfigurable logic-in-memory")
I95251 = p.create_item(R1__has_label="Zoppo, G.")
I64422 = p.create_item(R1__has_label="Marrone, F.")
I78497 = p.create_item(R1__has_label="Corinto, F.")
I13328 = p.create_item(R1__has_label="publication: Equilibrium propagation for me")
I35141 = p.create_item(R1__has_label="Alibart, F.")
I92353 = p.create_item(R1__has_label="publication: Pattern classification by memr")
I2008 = p.create_item(R1__has_label="Joshi, V.")
I42437 = p.create_item(R1__has_label="publication: Accurate deep neural network i")
I6968 = p.create_item(R1__has_label="Rasch, M. J.")
I36817 = p.create_item(R1__has_label="publication: Hardware-aware training for la")
I10063 = p.create_item(R1__has_label="Huang, H.-M.")
I65484 = p.create_item(R1__has_label="Wang, T.")
I55500 = p.create_item(R1__has_label="Xiao, Y.")
I33489 = p.create_item(R1__has_label="Guo, X.")
I67348 = p.create_item(R1__has_label="publication: Artificial neural networks bas")
I17979 = p.create_item(R1__has_label="Nandakumar, S. R.")
I26369 = p.create_item(R1__has_label="publication: Mixed-precision deep learning ")
I88187 = p.create_item(R1__has_label="publication: Mixed-precision in-memory comp")
I28475 = p.create_item(R1__has_label="publication: Face classification using elec")
I60983 = p.create_item(R1__has_label="Papandreou, N.")
I28936 = p.create_item(R1__has_label="publication: Programming algorithms for mul")
I38939 = p.create_item(R1__has_label="Milo, V.")
I76769 = p.create_item(R1__has_label="publication: Multilevel HfO2-based RRAM dev")
I42158 = p.create_item(R1__has_label="publication: Scaling-up resistive synaptic ")
I18444 = p.create_item(R1__has_label="Woo, J.")
I16220 = p.create_item(R1__has_label="publication: Improved synaptic behavior und")
I39094 = p.create_item(R1__has_label="Xiao, S.")
I96930 = p.create_item(R1__has_label="publication: GST-memristor-based online lea")
I76222 = p.create_item(R1__has_label="Tian, H.")
I59925 = p.create_item(R1__has_label="publication: A novel artificial synapse wit")
I7333 = p.create_item(R1__has_label="Shi, T.")
I28608 = p.create_item(R1__has_label="Yin, X. B.")
I24546 = p.create_item(R1__has_label="Yang, R.")
I58871 = p.create_item(R1__has_label="publication: Pt/WO3/FTO memristive devices ")
I41422 = p.create_item(R1__has_label="Menzel, S.")
I14175 = p.create_item(R1__has_label="publication: Origin of the ultra-nonlinear ")
I40099 = p.create_item(R1__has_label="Buscarino, A.")
I60522 = p.create_item(R1__has_label="Fortuna, L.")
I53325 = p.create_item(R1__has_label="Frasca, M.")
I72877 = p.create_item(R1__has_label="Gambuzza, L. V.")
I67121 = p.create_item(R1__has_label="Sciuto, G.")
I35151 = p.create_item(R1__has_label="publication: Memristive chaotic circuits ba")
I79603 = p.create_item(R1__has_label="Li, Y.")
I23744 = p.create_item(R1__has_label="Ang, K.-W.")
I34521 = p.create_item(R1__has_label="publication: Hardware implementation of neu")
I24214 = p.create_item(R1__has_label="Zhu, J.")
I99392 = p.create_item(R1__has_label="Yang, Y.")
I82361 = p.create_item(R1__has_label="Huang, R.")
I15303 = p.create_item(R1__has_label="publication: A comprehensive review on emer")
I80771 = p.create_item(R1__has_label="publication: Engineering incremental resist")
I46726 = p.create_item(R1__has_label="Park, S. M.")
I34860 = p.create_item(R1__has_label="publication: Improvement of conductance mod")
I11959 = p.create_item(R1__has_label="Slesazeck, S.")
I4382 = p.create_item(R1__has_label="Mikolajick, T.")
I14309 = p.create_item(R1__has_label="publication: Nanoscale resistive switching ")
I54143 = p.create_item(R1__has_label="Waser, R.")
I90495 = p.create_item(R1__has_label="Dittmann, R.")
I50839 = p.create_item(R1__has_label="Staikov, C.")
I76881 = p.create_item(R1__has_label="Szot, K.")
I62042 = p.create_item(R1__has_label="publication: Redox-based resistive switchin")
I3498 = p.create_item(R1__has_label="Ielmini, D.")
I10110 = p.create_item(R1__has_label="publication: Resistive Switching")
I45564 = p.create_item(R1__has_label="Wouters, D. J.")
I83292 = p.create_item(R1__has_label="Wuttig, M.")
I72286 = p.create_item(R1__has_label="publication: Phase-change and redoxbased re")
I32305 = p.create_item(R1__has_label="Pan, F.")
I6649 = p.create_item(R1__has_label="Gao, S.")
I93204 = p.create_item(R1__has_label="Chen, C.")
I41659 = p.create_item(R1__has_label="Song, C.")
I26548 = p.create_item(R1__has_label="Zeng, F.")
I58101 = p.create_item(R1__has_label="publication: Recent progress in resistive r")
I49776 = p.create_item(R1__has_label="Kim, S.")
I31658 = p.create_item(R1__has_label="publication: Analog synaptic behavior of a ")
I15725 = p.create_item(R1__has_label="Li, W.")
I59746 = p.create_item(R1__has_label="Huang, S.")
I95140 = p.create_item(R1__has_label="Jiang, H.")
I96333 = p.create_item(R1__has_label="publication: A 40-nm MLC-RRAM compute-in-me")
I98017 = p.create_item(R1__has_label="Buchel, J.")
I2969 = p.create_item(R1__has_label="publication: Gradient descent-based program")
I53524 = p.create_item(R1__has_label="publication: Spike-timing-dependent plastic")
I14604 = p.create_item(R1__has_label="Park, S.")
I78668 = p.create_item(R1__has_label="publication: Electronic system with memrist")
I55153 = p.create_item(R1__has_label="publication: Binary neural network with 16 ")
I76191 = p.create_item(R1__has_label="Chen, W. H.")
I22564 = p.create_item(R1__has_label="publication: CMOS-integrated memristive non")
I9645 = p.create_item(R1__has_label="publication: A 16Mb dual-mode ReRAM macro w")
I65696 = p.create_item(R1__has_label="publication: Memristor-based analog computa")
I50193 = p.create_item(R1__has_label="publication: Analogue signal and image proc")
I50890 = p.create_item(R1__has_label="Paszke A.")
I54273 = p.create_item(R1__has_label="publication: Automatic differentiation in P")
I50771 = p.create_item(R1__has_label="Abadi, M.")
I18159 = p.create_item(R1__has_label="publication: TensorFlow: Large-Scale Machin")
I2373 = p.create_item(R1__has_label="Stimberg, M.")
I77558 = p.create_item(R1__has_label="Brette, R.")
I82721 = p.create_item(R1__has_label="Goodman, D. F. M.")
I67271 = p.create_item(R1__has_label="publication: Brian 2, an intuitive and effi")
I62511 = p.create_item(R1__has_label="Spreizer, S.")
I88085 = p.create_item(R1__has_label="publication: NEST 3.3")
I90843 = p.create_item(R1__has_label="Hazan, H.")
I27535 = p.create_item(R1__has_label="publication: BindsNET: A machine learning-o")
I49566 = p.create_item(R1__has_label="M. Y. Lin")
I63567 = p.create_item(R1__has_label="publication: DL-RSIM: A simulation framewor")
I83247 = p.create_item(R1__has_label="publication: Impact of non-ideal characteri")
I23927 = p.create_item(R1__has_label="Ma, X.")
I1444 = p.create_item(R1__has_label="publication: Tiny but Accurate: A Pruned, Q")
I91883 = p.create_item(R1__has_label="Yuan, G.")
I76611 = p.create_item(R1__has_label="publication: An Ultra-Efficient Memristor-B")
I41680 = p.create_item(R1__has_label="publication: A flexible and fast PyTorch to")
I32004 = p.create_item(R1__has_label="Grötker, T.")
I48787 = p.create_item(R1__has_label="publication: System design with SystemC")
I94376 = p.create_item(R1__has_label="Gajski, D. D.")
I23668 = p.create_item(R1__has_label="publication: SpecC: specification language ")
I30731 = p.create_item(R1__has_label="Lee, M. K. F.")
I68433 = p.create_item(R1__has_label="publication: A system-level simulator for R")
I5936 = p.create_item(R1__has_label="BanaGozar, A.")
I75090 = p.create_item(R1__has_label="publication: System simulation of memristor")
I58366 = p.create_item(R1__has_label="Gai, L.")
I96129 = p.create_item(R1__has_label="Gajski, D.")
I11593 = p.create_item(R1__has_label="publication: Transaction level modeling: an")
I51750 = p.create_item(R1__has_label="Poremba, M.")
I99505 = p.create_item(R1__has_label="Xie, Y.")
I25420 = p.create_item(R1__has_label="publication: NVMain: An architectural-level")
I63440 = p.create_item(R1__has_label="publication: NVMain 2.0: A user-friendly me")
I64964 = p.create_item(R1__has_label="publication: MNSIM: Simulation platform for")
I90249 = p.create_item(R1__has_label="Zhu, Z.")
I55106 = p.create_item(R1__has_label="publication: MNSIM 2.0: A behavior-level mo")
I43024 = p.create_item(R1__has_label="Banagozar, A.")
I30610 = p.create_item(R1__has_label="publication: CIM-SIM: Computation in Memory")
I31482 = p.create_item(R1__has_label="Fei, X.")
I39247 = p.create_item(R1__has_label="Zhang, Y.")
I80994 = p.create_item(R1__has_label="Zheng, W.")
I82827 = p.create_item(R1__has_label="publication: XB-SIM: A simulation framework")
I12179 = p.create_item(R1__has_label="Zahedi, M.")
I2757 = p.create_item(R1__has_label="publication: MNEMOSENE: Tile architecture a")
I48354 = p.create_item(R1__has_label="Dong, X.")
I19072 = p.create_item(R1__has_label="Xu, C.")
I65244 = p.create_item(R1__has_label="publication: NVSim: A circuit-level perform")
I25815 = p.create_item(R1__has_label="Song, L.")
I54870 = p.create_item(R1__has_label="Qian, X.")
I95320 = p.create_item(R1__has_label="publication: PipeLayer: A Pipelined ReRAM-b")
I9600 = p.create_item(R1__has_label="Imani, M.")
I78217 = p.create_item(R1__has_label="publication: RAPIDNN: In-Memory Deep Neural")
I25979 = p.create_item(R1__has_label="Chen, A.")
I21111 = p.create_item(R1__has_label="publication: A comprehensive crossbar array")
I2344 = p.create_item(R1__has_label="Aguirre, F. L.")
I36246 = p.create_item(R1__has_label="publication: Line resistance impact in memr")
I67547 = p.create_item(R1__has_label="publication: Minimization of the line resis")
I19609 = p.create_item(R1__has_label="Lee, Y. K.")
I99881 = p.create_item(R1__has_label="publication: Matrix mapping on crossbar mem")
I67187 = p.create_item(R1__has_label="Fei, W.")
I55919 = p.create_item(R1__has_label="Yeo, K. S.")
I66683 = p.create_item(R1__has_label="publication: Design exploration of hybrid C")
I76006 = p.create_item(R1__has_label="Pazos, S. M.")
I85036 = p.create_item(R1__has_label="Palumbo, F.")
I34338 = p.create_item(R1__has_label="Suñé, J.")
I87407 = p.create_item(R1__has_label="Miranda, E.")
I77671 = p.create_item(R1__has_label="publication: Application of the quasi-stati")
I15029 = p.create_item(R1__has_label="publication: SPICE simulation of RRAM-based")
I82314 = p.create_item(R1__has_label="publication: Assessment and improvement of ")
I89234 = p.create_item(R1__has_label="Fritscher, M.")
I2124 = p.create_item(R1__has_label="Knodtel, J.")
I45121 = p.create_item(R1__has_label="Reichenbach, M.")
I56268 = p.create_item(R1__has_label="Fey, D.")
I6786 = p.create_item(R1__has_label="publication: Simulating memristive systems ")
I72270 = p.create_item(R1__has_label="Applied Materials")
I86571 = p.create_item(R1__has_label="publication: GinestraTM")
I90436 = p.create_item(R1__has_label="publication: TCAD Technology Computer Aided")
I4223 = p.create_item(R1__has_label="publication: Automating analogue AI chip de")
I36839 = p.create_item(R1__has_label="Salama, K.")
I5809 = p.create_item(R1__has_label="publication: Towards hardware optimal neura")
I90927 = p.create_item(R1__has_label="Guan, Z.")
I98188 = p.create_item(R1__has_label="publication: A hardware-aware neural archit")
I5750 = p.create_item(R1__has_label="Li, G.")
I6757 = p.create_item(R1__has_label="Mandal, S. K.")
I73193 = p.create_item(R1__has_label="Ogras, U. Y.")
I70920 = p.create_item(R1__has_label="Marculescu, R.")
I55764 = p.create_item(R1__has_label="publication: FLASH: Fast neural architectur")
I60336 = p.create_item(R1__has_label="Yuan, Z.")
I67013 = p.create_item(R1__has_label="publication: NAS4RRAM: neural network archi")
I11166 = p.create_item(R1__has_label="Yan, Z.")
I7393 = p.create_item(R1__has_label="Juan, D.-C.")
I1623 = p.create_item(R1__has_label="Hu, X. S.")
I86037 = p.create_item(R1__has_label="Shi, Y.")
I98213 = p.create_item(R1__has_label="publication: Uncertainty modeling of emergi")
I9301 = p.create_item(R1__has_label="Sun H.")
I68330 = p.create_item(R1__has_label="publication: Gibbon: Efficient co-explorati")
I12749 = p.create_item(R1__has_label="Jiang, W.")
I38831 = p.create_item(R1__has_label="publication: Device-circuit-architecture co")
I45494 = p.create_item(R1__has_label="Burr, G. W.")
I47996 = p.create_item(R1__has_label="publication: Experimental demonstration and")
I52583 = p.create_item(R1__has_label="Dong, Z.")
I35079 = p.create_item(R1__has_label="publication: Convolutional neural networks ")
I10148 = p.create_item(R1__has_label="Querlioz, D.")
I35068 = p.create_item(R1__has_label="Bichler, O.")
I60959 = p.create_item(R1__has_label="Dollfus, P.")
I42597 = p.create_item(R1__has_label="Gamrat, C.")
I81302 = p.create_item(R1__has_label="publication: Immunity to device variations ")
I11032 = p.create_item(R1__has_label="Guan, X.")
I61436 = p.create_item(R1__has_label="publication: A SPICE compact model of metal")
I18300 = p.create_item(R1__has_label="Liang, J.")
I35023 = p.create_item(R1__has_label="Yeh, S.")
I95103 = p.create_item(R1__has_label="Simon Wong, S.")
I67772 = p.create_item(R1__has_label="Philip Wong, H. S.")
I66816 = p.create_item(R1__has_label="publication: Effect of wordline/bitline sca")
I89938 = p.create_item(R1__has_label="Hirtzlin, T.")
I71699 = p.create_item(R1__has_label="publication: Digital biologically plausible")
I4407 = p.create_item(R1__has_label="Xue, C. X.")
I94278 = p.create_item(R1__has_label="publication: A 1Mb Multibit ReRAM computing")
I81075 = p.create_item(R1__has_label="Wu, T. F.")
I17336 = p.create_item(R1__has_label="publication: A 43pJ/Cycle Non-Volatile Micr")
I3089 = p.create_item(R1__has_label="Liu, Q.")
I95679 = p.create_item(R1__has_label="publication: A Fully Integrated Analog ReRA")
I22719 = p.create_item(R1__has_label="Bennett, C. H.")
I36951 = p.create_item(R1__has_label="Feinberg, B.")
I31551 = p.create_item(R1__has_label="Agarwal, S.")
I70878 = p.create_item(R1__has_label="Marinella, M. J.")
I9426 = p.create_item(R1__has_label="publication: Analog architectures for neura")
I94216 = p.create_item(R1__has_label="publication: NVIDIA Data Center Deep Learni")
I43418 = p.create_item(R1__has_label="Habana L.")
I78330 = p.create_item(R1__has_label="publication: GoyaTM Inference Platform Whit")
I84818 = p.create_item(R1__has_label="Chen Y.")
I31142 = p.create_item(R1__has_label="publication: DaDianNao: A Machine-Learning ")
I74019 = p.create_item(R1__has_label="publication: UNPU: An energy-efficient deep")
I83705 = p.create_item(R1__has_label="Bankman, D.")
I19231 = p.create_item(R1__has_label="Yang, L.")
I72904 = p.create_item(R1__has_label="Moons, B.")
I26214 = p.create_item(R1__has_label="Verhelst, M.")
I56137 = p.create_item(R1__has_label="publication: An always-on 3.8μJ/86% CIFAR-1")
I15966 = p.create_item(R1__has_label="Nag, A.")
I42377 = p.create_item(R1__has_label="publication: Newton: Gravitating towards th")
I88305 = p.create_item(R1__has_label="Bojnordi M. N.")
I41974 = p.create_item(R1__has_label="Ipek, E.")
I75108 = p.create_item(R1__has_label="publication: Memristive Boltzmann machine: ")
I18859 = p.create_item(R1__has_label="publication: A heterogeneous and programmab")
I80129 = p.create_item(R1__has_label="Carnevale N. T.")
I55623 = p.create_item(R1__has_label="Hines, M. L.")
I27380 = p.create_item(R1__has_label="publication: The NEURON book")
I6779 = p.create_item(R1__has_label="Lammie, C.")
I89114 = p.create_item(R1__has_label="Xiang, W.")
I85415 = p.create_item(R1__has_label="Azghadi, M. R.")
I71318 = p.create_item(R1__has_label="publication: MemTorch: An Open-source Simul")
I40045 = p.create_item(R1__has_label="publication: CrossSim: accuracy simulation ")
I78072 = p.create_item(R1__has_label="Joksas, D.")
I17406 = p.create_item(R1__has_label="Ng, W. H.")
I70034 = p.create_item(R1__has_label="Buckwell, M.")
I82691 = p.create_item(R1__has_label="publication: Simulation of inference accura")
I67208 = p.create_item(R1__has_label="Zhang, Q.")
I29245 = p.create_item(R1__has_label="publication: Sign backpropagation: An on-ch")
I84274 = p.create_item(R1__has_label="Yamaoka, M.")
I97898 = p.create_item(R1__has_label="publication: Low-power SRAM")
I55841 = p.create_item(R1__has_label="Jan, Y. W.")
I63187 = p.create_item(R1__has_label="publication: Voltage based winner takes all")


########################################################################################################################
# content:
########################################################################################################################

# 2024_bib.md 
I39529["European Commission"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="European Commission",
    
)


# 2024_bib.md 
I74938["publication: Harnessing the economic benefi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I39529["European Commission"],
    R8434__has_title="Harnessing the economic benefits of Artificial Intelligence",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I85012["Rattani, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Rattani, A.",
    
)


# 2024_bib.md 
I99712["Reddy, N."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Reddy, N.",
    
)


# 2024_bib.md 
I94362["Derakhshani, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Derakhshani, R.",
    
)


# 2024_bib.md 
I85528["publication: Multi-biometric Convolutional "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I85012["Rattani, A."], I99712["Reddy, N."], I94362["Derakhshani, R."]],
    R8434__has_title="Multi-biometric Convolutional Neural Networks for Mobile User Authentication",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I2855["BBVA"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="BBVA",
    
)


# 2024_bib.md 
I46793["publication: Biometrics and machine learnin"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I2855["BBVA"],
    R8434__has_title="Biometrics and machine learning: the accurate, secure way to access your bank",
    R8435__has_year=2024,
    
)


# 2024_bib.md 
I90963["Amerini, I."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Amerini, I.",
    
)


# 2024_bib.md 
I54975["Li, C.-T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, C.-T.",
    
)


# 2024_bib.md 
I72751["Caldelli, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Caldelli, R.",
    
)


# 2024_bib.md 
I80078["publication: Social network identification "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I90963["Amerini, I."], I54975["Li, C.-T."], I72751["Caldelli, R."]],
    R8434__has_title="Social network identification through image classification with CNN",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I5210["Ingle P. Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ingle P. Y.",
    
)


# 2024_bib.md 
I32782["Kim, Y. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kim, Y. G.",
    
)


# 2024_bib.md 
I91760["publication: Real-time abnormal object dete"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I5210["Ingle P. Y."], I32782["Kim, Y. G."]],
    R8434__has_title="Real-time abnormal object detection for video surveillance in smart cities",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I91215["Tan, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Tan, X.",
    
)


# 2024_bib.md 
I81970["Qin, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Qin, T.",
    
)


# 2024_bib.md 
I68229["F. Soong"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="F. Soong",
    
)


# 2024_bib.md 
I64747["T.-Y. Liu"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="T.-Y. Liu",
    
)


# 2024_bib.md 
I39757["publication: A survey on neural speech synt"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I91215["Tan, X."], I81970["Qin, T."], I68229["F. Soong"], I64747["T.-Y. Liu"]],
    R8434__has_title="A survey on neural speech synthesis",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I30227["publication: ChatGPT: Optimizing language m"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="ChatGPT: Optimizing language models for dialogue",
    
)


# 2024_bib.md 
I24132["Hong, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hong, T.",
    
)


# 2024_bib.md 
I14404["Choi, J. A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Choi, J. A.",
    
)


# 2024_bib.md 
I65317["Lim, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lim, K.",
    
)


# 2024_bib.md 
I25665["Kim, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kim, P.",
    
)


# 2024_bib.md 
I85099["publication: Enhancing personalized ads usi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I24132["Hong, T."], I14404["Choi, J. A."], I65317["Lim, K."], I25665["Kim, P."]],
    R8434__has_title="Enhancing personalized ads using interest category classification of SNS users based on deep neural networks",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I97353["McKee, S. A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="McKee, S. A.",
    
)


# 2024_bib.md 
I47693["publication: Reflections on the memory wall"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I97353["McKee, S. A."],
    R8434__has_title="Reflections on the memory wall",
    R8435__has_year=2004,
    
)


# 2024_bib.md 
I17571["Mehonic, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mehonic, A.",
    
)


# 2024_bib.md 
I63422["Kenyon, A. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kenyon, A. J.",
    
)


# 2024_bib.md 
I91057["publication: Brain-inspired computing needs"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I17571["Mehonic, A."], I63422["Kenyon, A. J."]],
    R8434__has_title="Brain-inspired computing needs a master plan",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I86040["Zhang, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhang, C.",
    
)


# 2024_bib.md 
I60665["et al."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="et al.",
    
)


# 2024_bib.md 
I36571["publication: IMLBench: A machine learning b"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I86040["Zhang, C."], I60665["et al."]],
    R8434__has_title="IMLBench: A machine learning benchmark suite for CPU-GPU integrated architectures",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I76227["Li, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, F.",
    
)


# 2024_bib.md 
I68467["Ye, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ye, Y.",
    
)


# 2024_bib.md 
I11040["Tian, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Tian, Z.",
    
)


# 2024_bib.md 
I40507["Zhang, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhang, X.",
    
)


# 2024_bib.md 
I46602["publication: CPU versus GPU: which can perf"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I76227["Li, F."], I68467["Ye, Y."], I11040["Tian, Z."], I40507["Zhang, X."]],
    R8434__has_title="CPU versus GPU: which can perform matrix computation faster—performance comparison for basic linear algebra subprograms",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I75913["Farabet, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Farabet, C.",
    
)


# 2024_bib.md 
I32043["Poulet, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Poulet, C.",
    
)


# 2024_bib.md 
I45775["Han, J. Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Han, J. Y.",
    
)


# 2024_bib.md 
I88802["LeCun, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="LeCun, Y.",
    
)


# 2024_bib.md 
I89671["publication: CNP: An FPGA-based processor f"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I75913["Farabet, C."], I32043["Poulet, C."], I45775["Han, J. Y."], I88802["LeCun, Y."]],
    R8434__has_title="CNP: An FPGA-based processor for Convolutional Networks",
    R8435__has_year=2009,
    
)


# 2024_bib.md 
I5377["publication: NeuFlow: A runtime reconfigura"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I75913["Farabet, C."], I60665["et al."]],
    R8434__has_title="NeuFlow: A runtime reconfigurable dataflow processor for vision",
    
)


# 2024_bib.md 
I79564["publication: Optimizing FPGA-based accelera"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I86040["Zhang, C."], I60665["et al."]],
    R8434__has_title="Optimizing FPGA-based accelerator design for deep convolutional neural networks",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I67803["Chakradhar, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chakradhar, S.",
    
)


# 2024_bib.md 
I37074["Sankaradas, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sankaradas, M.",
    
)


# 2024_bib.md 
I34513["Jakkula, V."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jakkula, V.",
    
)


# 2024_bib.md 
I4484["Cadambi, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Cadambi, S.",
    
)


# 2024_bib.md 
I93059["publication: A dynamically configurable cop"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I67803["Chakradhar, S."], I37074["Sankaradas, M."], I34513["Jakkula, V."], I4484["Cadambi, S."]],
    R8434__has_title="A dynamically configurable coprocessor for convolutional neural networks",
    R8435__has_year=2010,
    
)


# 2024_bib.md 
I89877["Wei X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wei X.",
    
)


# 2024_bib.md 
I48946["publication: Automated systolic array archi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I89877["Wei X."],
    R8434__has_title="Automated systolic array architecture synthesis for high throughput CNN Inference on FPGAs",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I44836["Guo, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Guo, K.",
    
)


# 2024_bib.md 
I63006["publication: Neural Network Accelerator Com"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I44836["Guo, K."], I60665["et al."]],
    R8434__has_title="Neural Network Accelerator Comparison",
    
)


# 2024_bib.md 
I99459["Jouppi, N. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jouppi, N. P.",
    
)


# 2024_bib.md 
I48965["publication: In-datacenter performance anal"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I99459["Jouppi, N. P."], I60665["et al."]],
    R8434__has_title="In-datacenter performance analysis of a tensor processing unit",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I85347["publication: AI Chip Amazon Inferentia AWS"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="AI Chip Amazon Inferentia AWS",
    
)


# 2024_bib.md 
I45993["Talpes, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Talpes, E.",
    
)


# 2024_bib.md 
I24141["publication: Compute solution for Tesla's f"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I45993["Talpes, E."], I60665["et al."]],
    R8434__has_title="Compute solution for Tesla's full self-driving computer",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I35428["Reuther, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Reuther, A.",
    
)


# 2024_bib.md 
I10778["et al"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="et al",
    
)


# 2024_bib.md 
I69974["publication: AI and ML Accelerator Survey a"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I35428["Reuther, A."], I10778["et al"]],
    R8434__has_title="AI and ML Accelerator Survey and Trends",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I70494["Fick, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fick, L.",
    
)


# 2024_bib.md 
I87242["Skrzyniarz, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Skrzyniarz, S.",
    
)


# 2024_bib.md 
I93860["Parikh, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Parikh, M.",
    
)


# 2024_bib.md 
I78857["Henry, M. B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Henry, M. B.",
    
)


# 2024_bib.md 
I94601["Fick, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fick, D.",
    
)


# 2024_bib.md 
I52917["publication: Analog matrix processor for ed"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I70494["Fick, L."], I87242["Skrzyniarz, S."], I93860["Parikh, M."], I78857["Henry, M. B."], I94601["Fick, D."]],
    R8434__has_title="Analog matrix processor for edge AI real-time video analytics",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I86787["publication: Gyrfalcon Unveils Fourth AI Ac"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="Gyrfalcon Unveils Fourth AI Accelerator Chip",
    
)


# 2024_bib.md 
I21123["Sebastian, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sebastian, A.",
    
)


# 2024_bib.md 
I39708["Le Gallo, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Le Gallo, M.",
    
)


# 2024_bib.md 
I93276["Khaddam-Aljameh, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Khaddam-Aljameh, R.",
    
)


# 2024_bib.md 
I53205["Eleftheriou, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Eleftheriou, E.",
    
)


# 2024_bib.md 
I87136["publication: Memory devices and application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I21123["Sebastian, A."], I39708["Le Gallo, M."], I93276["Khaddam-Aljameh, R."], I53205["Eleftheriou, E."]],
    R8434__has_title="Memory devices and applications for in-memory computing",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I41902["Zheng, N."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zheng, N.",
    
)


# 2024_bib.md 
I85417["Mazumder, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mazumder, P.",
    
)


# 2024_bib.md 
I97657["publication: Learning in energy-efficient n"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I41902["Zheng, N."], I85417["Mazumder, P."]],
    R8434__has_title="Learning in energy-efficient neuromorphic computing: algorithm and architecture co-design",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I29872["Orchard, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Orchard, G.",
    
)


# 2024_bib.md 
I21621["publication: Efficient Neuromorphic Signal "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I29872["Orchard, G."], I60665["et al."]],
    R8434__has_title="Efficient Neuromorphic Signal Processing with Loihi 2",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I87604["publication: Microchips that mimic the huma"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="Microchips that mimic the human brain could make AI far more energy efficient",
    
)


# 2024_bib.md 
I58690["Davies, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Davies, M.",
    
)


# 2024_bib.md 
I7533["publication: Advancing neuromorphic computi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I58690["Davies, M."], I60665["et al."]],
    R8434__has_title="Advancing neuromorphic computing with Loihi: A survey of results and outlook",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I28840["Barnell, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Barnell, M.",
    
)


# 2024_bib.md 
I49189["Raymond, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Raymond, C.",
    
)


# 2024_bib.md 
I8849["Wilson, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wilson, M.",
    
)


# 2024_bib.md 
I74720["Isereau, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Isereau, D.",
    
)


# 2024_bib.md 
I95219["Cicotta, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Cicotta, C.",
    
)


# 2024_bib.md 
I45292["publication: Target classification in synth"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I28840["Barnell, M."], I49189["Raymond, C."], I8849["Wilson, M."], I74720["Isereau, D."], I95219["Cicotta, C."]],
    R8434__has_title="Target classification in synthetic aperture radar and optical imagery using loihi neuromorphic hardware",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I90863["Viale, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Viale, A.",
    
)


# 2024_bib.md 
I66609["Marchisio, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Marchisio, A.",
    
)


# 2024_bib.md 
I26240["Martina, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Martina, M.",
    
)


# 2024_bib.md 
I16712["Masera, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Masera, G.",
    
)


# 2024_bib.md 
I26637["Shafique, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Shafique, M.",
    
)


# 2024_bib.md 
I73173["publication: CarSNN: An efficient spiking n"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I90863["Viale, A."], I66609["Marchisio, A."], I26240["Martina, M."], I16712["Masera, G."], I26637["Shafique, M."]],
    R8434__has_title="CarSNN: An efficient spiking neural network for event-based autonomous cars on the Loihi Neuromorphic Research Processor",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I77352["publication: Innatera Unveils Neuromorphic "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="Innatera Unveils Neuromorphic AI Chip to Accelerate Spiking Networks - EE Times",
    
)


# 2024_bib.md 
I12092["Pei, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pei, J.",
    
)


# 2024_bib.md 
I95662["publication: Towards artificial general int"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I12092["Pei, J."], I60665["et al."]],
    R8434__has_title="Towards artificial general intelligence with hybrid Tianjic chip architecture",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I50118["Merolla, P. A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Merolla, P. A.",
    
)


# 2024_bib.md 
I52771["publication: A million spiking-neuron integ"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I50118["Merolla, P. A."], I60665["et al."]],
    R8434__has_title="A million spiking-neuron integrated circuit with a scalable communication network and interface",
    R8435__has_year=2014,
    
)


# 2024_bib.md 
I38213["Adam, G. C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Adam, G. C.",
    
)


# 2024_bib.md 
I9385["Khiat, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Khiat, A.",
    
)


# 2024_bib.md 
I34131["Prodromakis, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Prodromakis, T.",
    
)


# 2024_bib.md 
I47402["publication: Challenges hindering memristiv"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I38213["Adam, G. C."], I9385["Khiat, A."], I34131["Prodromakis, T."]],
    R8434__has_title="Challenges hindering memristive neuromorphic hardware from going mainstream",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I8777["Sung, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sung, C.",
    
)


# 2024_bib.md 
I61519["Hwang, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hwang, H.",
    
)


# 2024_bib.md 
I89808["Yoo, I. K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yoo, I. K.",
    
)


# 2024_bib.md 
I73802["publication: Perspective: A review on memri"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I8777["Sung, C."], I61519["Hwang, H."], I89808["Yoo, I. K."]],
    R8434__has_title="Perspective: A review on memristive hardware for neuromorphic computation",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I63079["Deng, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Deng, L.",
    
)


# 2024_bib.md 
I92934["publication: Energy consumption analysis fo"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I63079["Deng, L."], I60665["et al."]],
    R8434__has_title="Energy consumption analysis for various memristive networks under different learning strategies",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I97154["Yu, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yu, S.",
    
)


# 2024_bib.md 
I84376["Wu, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wu, Y.",
    
)


# 2024_bib.md 
I72298["Jeyasingh, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jeyasingh, R.",
    
)


# 2024_bib.md 
I34559["Kuzum, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kuzum, D.",
    
)


# 2024_bib.md 
I83048["Wong, H. S. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wong, H. S. P.",
    
)


# 2024_bib.md 
I71732["publication: An electronic synapse device b"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I97154["Yu, S."], I84376["Wu, Y."], I72298["Jeyasingh, R."], I34559["Kuzum, D."], I83048["Wong, H. S. P."]],
    R8434__has_title="An electronic synapse device based on metal oxide resistive switching memory for neuromorphic computation",
    R8435__has_year=2011,
    
)


# 2024_bib.md 
I16765["Shulaker, M. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Shulaker, M. M.",
    
)


# 2024_bib.md 
I18578["publication: Three-dimensional integration "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I16765["Shulaker, M. M."], I60665["et al."]],
    R8434__has_title="Three-dimensional integration of nanotechnologies for computing and data storage on a single chip",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I87992["Li, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, C.",
    
)


# 2024_bib.md 
I44440["publication: Three-dimensional crossbar arr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I87992["Li, C."], I60665["et al."]],
    R8434__has_title="Three-dimensional crossbar arrays of self-rectifying Si/ SiO2/Si memristors",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I58468["Yoon, J. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yoon, J. H.",
    
)


# 2024_bib.md 
I47470["publication: Truly electroforming-free and "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I58468["Yoon, J. H."],
    R8434__has_title="Truly electroforming-free and low-energy memristors with preconditioned conductive tunneling paths",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I82062["Choi, B. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Choi, B. J.",
    
)


# 2024_bib.md 
I58157["publication: High-speed and low-energy nitr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I82062["Choi, B. J."], I60665["et al."]],
    R8434__has_title="High-speed and low-energy nitride memristors",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I27966["Strukov, D. B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Strukov, D. B.",
    
)


# 2024_bib.md 
I21352["Snider, G. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Snider, G. S.",
    
)


# 2024_bib.md 
I46285["Stewart, D. R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Stewart, D. R.",
    
)


# 2024_bib.md 
I6912["Williams, R. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Williams, R. S.",
    
)


# 2024_bib.md 
I26347["publication: The missing memristor found"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I27966["Strukov, D. B."], I21352["Snider, G. S."], I46285["Stewart, D. R."], I6912["Williams, R. S."]],
    R8434__has_title="The missing memristor found",
    
)


# 2024_bib.md 
I24977["publication: FUJITSU SEMICONDUCTOR MEMORY S"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="FUJITSU SEMICONDUCTOR MEMORY SOLUTION",
    
)


# 2024_bib.md 
I9309["publication: Everspin | The MRAM Company"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="Everspin | The MRAM Company",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I93983["Yole Group"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yole Group",
    
)


# 2024_bib.md 
I18158["Stathopoulos, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Stathopoulos, S.",
    
)


# 2024_bib.md 
I63066["publication: Multibit memory operation of m"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I18158["Stathopoulos, S."], I10778["et al"]],
    R8434__has_title="Multibit memory operation of metal-oxide Bi-layer memristors",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I55774["Wu, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wu, W.",
    
)


# 2024_bib.md 
I3236["publication: Demonstration of a multi-level"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I55774["Wu, W."], I60665["et al."]],
    R8434__has_title="Demonstration of a multi-level μA-range bulk switching ReRAM and its application for keyword spotting",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I95705["Yang, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yang, J.",
    
)


# 2024_bib.md 
I78145["publication: Thousands of conductance level"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I95705["Yang, J."], I60665["et al."]],
    R8434__has_title="Thousands of conductance levels in memristors monolithically integrated on CMOS",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I93419["Goux, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Goux, L.",
    
)


# 2024_bib.md 
I98801["publication: Ultralow sub-500nA operating c"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I93419["Goux, L."], I60665["et al."]],
    R8434__has_title="Ultralow sub-500nA operating current highperformance TiN\Al 2O 3\HfO 2\Hf\TiN bipolar RRAM achieved through understanding-based stack-engineering",
    R8435__has_year=2012,
    
)


# 2024_bib.md 
I11520["Li, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, H.",
    
)


# 2024_bib.md 
I47520["publication: Memristive crossbar arrays for"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I11520["Li, H."], I60665["et al."]],
    R8434__has_title="Memristive crossbar arrays for storage and computing applications",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I59694["Lin, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lin, P.",
    
)


# 2024_bib.md 
I79160["publication: Three-dimensional memristor ci"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I59694["Lin, P."], I60665["et al."]],
    R8434__has_title="Three-dimensional memristor circuits as complex neural networks",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I56829["Ishii, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ishii, M.",
    
)


# 2024_bib.md 
I10094["publication: On-Chip Trainable 1.4M 6T2R PC"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I56829["Ishii, M."], I60665["et al."]],
    R8434__has_title="On-Chip Trainable 1.4M 6T2R PCM synaptic array with 1.6K Stochastic LIF neurons for spiking RBM",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I33159["publication: Efficient and self-adaptive in"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I87992["Li, C."], I60665["et al."]],
    R8434__has_title="Efficient and self-adaptive in-situ learning in multilayer memristor neural networks",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I42033["Yao, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yao, P.",
    
)


# 2024_bib.md 
I92000["publication: Fully hardware-implemented mem"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I42033["Yao, P."], I60665["et al."]],
    R8434__has_title="Fully hardware-implemented memristor convolutional neural network",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I7940["Correll, J. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Correll, J. M.",
    
)


# 2024_bib.md 
I69530["publication: An 8-bit 20.7 TOPS/W Multi-Lev"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I7940["Correll, J. M."], I60665["et al."]],
    R8434__has_title="An 8-bit 20.7 TOPS/W Multi-Level Cell ReRAMbased Compute Engine",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I68259["Cai, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Cai, F.",
    
)


# 2024_bib.md 
I29098["publication: A fully integrated reprogramma"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I68259["Cai, F."], I60665["et al."]],
    R8434__has_title="A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I82346["Hung, J.-M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hung, J.-M.",
    
)


# 2024_bib.md 
I90071["publication: An 8-Mb DC-Current-Free Binary"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I82346["Hung, J.-M."],
    R8434__has_title="An 8-Mb DC-Current-Free Binary-to-8b Precision ReRAM Nonvolatile Computing-in-Memory Macro using Time-Space-Readout with 1286.4-21.6TOPS/W for Edge-AI Devices",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I88962["Xue, C.-X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xue, C.-X.",
    
)


# 2024_bib.md 
I12398["publication: 15.4 A 22nm 2Mb ReRAM Compute-"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I88962["Xue, C.-X."],
    R8434__has_title="15.4 A 22nm 2Mb ReRAM Compute-in-Memory Macro with 121-28TOPS/W for Multibit MAC Computing for Tiny AI Edge Devices",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I33364["Wan, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wan, W.",
    
)


# 2024_bib.md 
I8173["publication: A compute-in-memory chip based"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I33364["Wan, W."], I60665["et al."]],
    R8434__has_title="A compute-in-memory chip based on resistive random-access memory",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I98878["Yin, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yin, S.",
    
)


# 2024_bib.md 
I76458["Sun, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sun, X.",
    
)


# 2024_bib.md 
I23249["Seo, J. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Seo, J. S.",
    
)


# 2024_bib.md 
I38620["publication: High-throughput in-memory comp"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I98878["Yin, S."], I76458["Sun, X."], I97154["Yu, S."], I23249["Seo, J. S."]],
    R8434__has_title="High-throughput in-memory computing for binary deep neural networks with monolithically integrated RRAM and 90-nm CMOS",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I76087["Yan, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yan, X.",
    
)


# 2024_bib.md 
I48237["publication: Robust Ag/ZrO2/WS2/Pt Memristo"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I76087["Yan, X."], I60665["et al."]],
    R8434__has_title="Robust Ag/ZrO2/WS2/Pt Memristor for Neuromorphic Computing",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I61398["Chen, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chen, Q.",
    
)


# 2024_bib.md 
I99103["publication: Improving the recognition accu"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I61398["Chen, Q."], I10778["et al"]],
    R8434__has_title="Improving the recognition accuracy of memristive neural networks via homogenized analog type conductance quantization",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I28976["Wang, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wang, Y.",
    
)


# 2024_bib.md 
I66639["publication: High on/off ratio black phosph"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I28976["Wang, Y."],
    R8434__has_title="High on/off ratio black phosphorus based memristor with ultra-thin phosphorus oxide layer",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I34380["Xue, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xue, F.",
    
)


# 2024_bib.md 
I37464["publication: Giant ferroelectric resistance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I34380["Xue, F."], I10778["et al"]],
    R8434__has_title="Giant ferroelectric resistance switching controlled by a modulatory terminal for low-power neuromorphic in-memory computing",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I11681["Pan, W.-Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pan, W.-Q.",
    
)


# 2024_bib.md 
I41069["publication: Strategies to improve the accu"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I11681["Pan, W.-Q."], I60665["et al."]],
    R8434__has_title="Strategies to improve the accuracy of memristorbased convolutional neural networks",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I5868["Seo, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Seo, S.",
    
)


# 2024_bib.md 
I61689["publication: Artificial optic-neural synaps"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I5868["Seo, S."], I60665["et al."]],
    R8434__has_title="Artificial optic-neural synapse for colored and colormixed pattern recognition",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I37167["Chandrasekaran, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chandrasekaran, S.",
    
)


# 2024_bib.md 
I12287["Simanjuntak, F. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Simanjuntak, F. M.",
    
)


# 2024_bib.md 
I86221["Saminathan, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Saminathan, R.",
    
)


# 2024_bib.md 
I47202["Panda, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Panda, D.",
    
)


# 2024_bib.md 
I29376["Tseng, T. Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Tseng, T. Y.",
    
)


# 2024_bib.md 
I69517["publication: Improving linearity by introdu"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I37167["Chandrasekaran, S."], I12287["Simanjuntak, F. M."], I86221["Saminathan, R."], I47202["Panda, D."], I29376["Tseng, T. Y."]],
    R8434__has_title="Improving linearity by introducing Al in HfO2 as a memristor synapse device",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I1362["Zhang, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhang, B.",
    
)


# 2024_bib.md 
I57709["publication: 90% yield production of polyme"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I1362["Zhang, B."], I60665["et al."]],
    R8434__has_title="90% yield production of polymer nano-memristor for in-memory computing",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I73000["Feng, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Feng, X.",
    
)


# 2024_bib.md 
I49887["publication: Self-selective multi-terminal "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I73000["Feng, X."], I60665["et al."]],
    R8434__has_title="Self-selective multi-terminal memtransistor crossbar array for in-memory computing",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I67827["publication: HERMES-Core-A 1.59-TOPS/mm2PCM"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I93276["Khaddam-Aljameh, R."], I60665["et al."]],
    R8434__has_title="HERMES-Core-A 1.59-TOPS/mm2PCM on 14-nm CMOS in-memory compute core using 300-ps/LSB linearized CCO-based ADCs",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I22963["Narayanan, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Narayanan, P.",
    
)


# 2024_bib.md 
I17132["publication: Fully on-chip MAC at 14 nm ena"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I22963["Narayanan, P."], I60665["et al."]],
    R8434__has_title="Fully on-chip MAC at 14 nm enabled by accurate row-wise programming of PCM-based weights and parallel vector-transport in duration-format",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I74155["publication: A 64-core mixed-signal in-memo"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I39708["Le Gallo, M."], I60665["et al."]],
    R8434__has_title="A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I18985["Murmann, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Murmann, B.",
    
)


# 2024_bib.md 
I87613["publication: Mixed-signal computing for dee"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I18985["Murmann, B."],
    R8434__has_title="Mixed-signal computing for deep neural network inference",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I95725["Jiang, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jiang, Z.",
    
)


# 2024_bib.md 
I64045["Seok, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Seok, M.",
    
)


# 2024_bib.md 
I79243["publication: XNOR-SRAM: In-memory computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I98878["Yin, S."], I95725["Jiang, Z."], I23249["Seo, J. S."], I64045["Seok, M."]],
    R8434__has_title="XNOR-SRAM: In-memory computing SRAM macro for binary/ternary deep neural networks",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I52752["Biswas, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Biswas, A.",
    
)


# 2024_bib.md 
I49299["Chandrakasan, A. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chandrakasan, A. P.",
    
)


# 2024_bib.md 
I51187["publication: CONV-SRAM: An energy-efficient"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I52752["Biswas, A."], I49299["Chandrakasan, A. P."]],
    R8434__has_title="CONV-SRAM: An energy-efficient SRAM with in-memory dot-product computation for low-power convolutional neural networks",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I59886["Valavi, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Valavi, H.",
    
)


# 2024_bib.md 
I75602["Ramadge, P. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ramadge, P. J.",
    
)


# 2024_bib.md 
I26646["Nestler, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Nestler, E.",
    
)


# 2024_bib.md 
I22852["Verma, N."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Verma, N.",
    
)


# 2024_bib.md 
I77881["publication: A 64-Tile 2.4-Mb In-memory-com"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I59886["Valavi, H."], I75602["Ramadge, P. J."], I26646["Nestler, E."], I22852["Verma, N."]],
    R8434__has_title="A 64-Tile 2.4-Mb In-memory-computing CNN accelerator employing chargedomain compute",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I49586["Khwa, W. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Khwa, W. S.",
    
)


# 2024_bib.md 
I55924["publication: A 65nm 4Kb algorithm-dependent"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I49586["Khwa, W. S."], I60665["et al."]],
    R8434__has_title="A 65nm 4Kb algorithm-dependent computing-in-memory SRAM unit-macro with 2.3ns and 55.8TOPS/W fully parallel product-sum operation for binary DNN edge processors",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I97111["publication: In-memory computing: advances "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I22852["Verma, N."], I60665["et al."]],
    R8434__has_title="In-memory computing: advances and prospects",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I13415["Diorio, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Diorio, C.",
    
)


# 2024_bib.md 
I84363["Hasler, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hasler, P.",
    
)


# 2024_bib.md 
I51358["Minch, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Minch, A.",
    
)


# 2024_bib.md 
I61262["Mead, C. A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mead, C. A.",
    
)


# 2024_bib.md 
I69614["publication: A single-transistor silicon sy"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I13415["Diorio, C."], I84363["Hasler, P."], I51358["Minch, A."], I61262["Mead, C. A."]],
    R8434__has_title="A single-transistor silicon synapse",
    R8435__has_year=1996,
    
)


# 2024_bib.md 
I91097["Merrikh-Bayat, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Merrikh-Bayat, F.",
    
)


# 2024_bib.md 
I84267["publication: High-performance mixed-signal "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I91097["Merrikh-Bayat, F."], I60665["et al."]],
    R8434__has_title="High-performance mixed-signal neurocomputing with nanoscale floating-gate memory cell arrays",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I32602["Wang, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wang, P.",
    
)


# 2024_bib.md 
I91573["publication: Three-dimensional NAND flash f"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I32602["Wang, P."], I60665["et al."]],
    R8434__has_title="Three-dimensional NAND flash for vector-matrix multiplication",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I60259["Bavandpour, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Bavandpour, M.",
    
)


# 2024_bib.md 
I73590["Sahay, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sahay, S.",
    
)


# 2024_bib.md 
I74604["Mahmoodi, M. R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mahmoodi, M. R.",
    
)


# 2024_bib.md 
I66704["publication: 3DaCortex: an ultra-compact en"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I60259["Bavandpour, M."], I73590["Sahay, S."], I74604["Mahmoodi, M. R."], I27966["Strukov, D. B."]],
    R8434__has_title="3DaCortex: an ultra-compact energy-efficient neurocomputing platform based on commercial 3D-NAND flash memories",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I59620["Chu, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chu, M.",
    
)


# 2024_bib.md 
I38907["publication: Neuromorphic hardware system f"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I59620["Chu, M."], I60665["et al."]],
    R8434__has_title="Neuromorphic hardware system for visual pattern recognition with memristor array and CMOS neuron",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I72736["Yeo, I."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yeo, I.",
    
)


# 2024_bib.md 
I31938["Gi, S. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gi, S. G.",
    
)


# 2024_bib.md 
I15972["Lee, B. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lee, B. G.",
    
)


# 2024_bib.md 
I70751["publication: Stuck-at-fault tolerant scheme"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I72736["Yeo, I."], I59620["Chu, M."], I31938["Gi, S. G."], I61519["Hwang, H."], I15972["Lee, B. G."]],
    R8434__has_title="Stuck-at-fault tolerant schemes for memristor crossbar array-based neural networks",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I86194["Cortes, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Cortes, C.",
    
)


# 2024_bib.md 
I72160["Burges, C. J. C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Burges, C. J. C.",
    
)


# 2024_bib.md 
I43694["publication: MNIST handwritten digit databa"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I88802["LeCun, Y."], I86194["Cortes, C."], I72160["Burges, C. J. C."]],
    R8434__has_title="MNIST handwritten digit database of handwritten digits",
    
)


# 2024_bib.md 
I77914["Krizhevsky, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Krizhevsky, A.",
    
)


# 2024_bib.md 
I10506["Nair, V."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Nair, V.",
    
)


# 2024_bib.md 
I67834["Hinton, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hinton, G.",
    
)


# 2024_bib.md 
I8593["publication: The CIFAR-10 dataset."].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I77914["Krizhevsky, A."], I10506["Nair, V."], I67834["Hinton, G."]],
    R8434__has_title="The CIFAR-10 dataset.",
    
)


# 2024_bib.md 
I85158["Deng, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Deng, J.",
    
)


# 2024_bib.md 
I36804["publication: ImageNet: A large-scale hierar"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I85158["Deng, J."], I60665["et al."]],
    R8434__has_title="ImageNet: A large-scale hierarchical image database",
    R8435__has_year=2009,
    
)


# 2024_bib.md 
I65099["Simonyan, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Simonyan, K.",
    
)


# 2024_bib.md 
I16673["Zisserman, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zisserman, A.",
    
)


# 2024_bib.md 
I33540["publication: Very deep convolutional networ"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I65099["Simonyan, K."], I16673["Zisserman, A."]],
    R8434__has_title="Very deep convolutional networks for large-scale image recognition",
    R8435__has_year=2014,
    
)


# 2024_bib.md 
I10736["He, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="He, K.",
    
)


# 2024_bib.md 
I36840["Ren, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ren, S.",
    
)


# 2024_bib.md 
I81192["Sun, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sun, J.",
    
)


# 2024_bib.md 
I10867["publication: Deep Residual Learning for Ima"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I10736["He, K."], I40507["Zhang, X."], I36840["Ren, S."], I81192["Sun, J."]],
    R8434__has_title="Deep Residual Learning for Image Recognition",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I4130["Chen, P. Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chen, P. Y.",
    
)


# 2024_bib.md 
I52096["Peng, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Peng, X.",
    
)


# 2024_bib.md 
I63907["publication: NeuroSim: A circuit-level macr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I4130["Chen, P. Y."], I52096["Peng, X."], I97154["Yu, S."]],
    R8434__has_title="NeuroSim: A circuit-level macro model for benchmarking neuro-inspired architectures in online learning",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I28196["Wang, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wang, Q.",
    
)


# 2024_bib.md 
I3591["Wang, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wang, X.",
    
)


# 2024_bib.md 
I59167["Lee, S. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lee, S. H.",
    
)


# 2024_bib.md 
I79716["Meng, F.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Meng, F.-H.",
    
)


# 2024_bib.md 
I88339["Lu W. D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lu W. D.",
    
)


# 2024_bib.md 
I21466["publication: A Deep Neural Network Accelera"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I28196["Wang, Q."], I3591["Wang, X."], I59167["Lee, S. H."], I79716["Meng, F.-H."], I88339["Lu W. D."]],
    R8434__has_title="A Deep Neural Network Accelerator Based on Tiled RRAM Architecture",
    
)


# 2024_bib.md 
I96420["Kim, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kim, H.",
    
)


# 2024_bib.md 
I18805["Nili, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Nili, H.",
    
)


# 2024_bib.md 
I2133["publication: 4K-memristor analog-grade pass"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I96420["Kim, H."], I74604["Mahmoodi, M. R."], I18805["Nili, H."], I27966["Strukov, D. B."]],
    R8434__has_title="4K-memristor analog-grade passive crossbar circuit",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I32206["Inc. The Mathworks"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Inc. The Mathworks",
    
)


# 2024_bib.md 
I64611["publication: MATLAB"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I32206["Inc. The Mathworks"],
    R8434__has_title="MATLAB",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I83149["Amirsoleimani, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Amirsoleimani, A.",
    
)


# 2024_bib.md 
I43547["publication: In-memory vector-matrix multip"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I83149["Amirsoleimani, A."], I60665["et al."]],
    R8434__has_title="In-memory vector-matrix multiplication in monolithic complementary metal–oxide–semiconductor-memristor integrated circuits: design choices, challenges, and perspectives",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I98535["Chakraborty, I."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chakraborty, I.",
    
)


# 2024_bib.md 
I94285["publication: Resistive crossbars as approxi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I98535["Chakraborty, I."], I60665["et al."]],
    R8434__has_title="Resistive crossbars as approximate hardware building blocks for machine learning: opportunities and challenges",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I15284["Jain, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jain, S.",
    
)


# 2024_bib.md 
I68828["publication: Neural network accelerator des"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15284["Jain, S."], I60665["et al."]],
    R8434__has_title="Neural network accelerator design with resistive crossbars: Opportunities and challenges",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I60267["Ankit, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ankit, A.",
    
)


# 2024_bib.md 
I46809["publication: PANTHER: A Programmable Archit"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I60267["Ankit, A."], I60665["et al."]],
    R8434__has_title="PANTHER: A Programmable Architecture for Neural Network Training Harnessing Energy-Efficient ReRAM",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I25926["Mochida, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mochida, R.",
    
)


# 2024_bib.md 
I34829["publication: A 4M synapses integrated analo"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I25926["Mochida, R."], I60665["et al."]],
    R8434__has_title="A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I78886["Su, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Su, F.",
    
)


# 2024_bib.md 
I25994["publication: A 462GOPs/J RRAM-based nonvola"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I78886["Su, F."], I60665["et al."]],
    R8434__has_title="A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I30847["Han J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Han J.",
    
)


# 2024_bib.md 
I94613["Orshansky, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Orshansky, M.",
    
)


# 2024_bib.md 
I79574["publication: Approximate computing: An emer"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I30847["Han J."], I94613["Orshansky, M."]],
    R8434__has_title="Approximate computing: An emerging paradigm for energy-efficient design",
    R8435__has_year=2013,
    
)


# 2024_bib.md 
I47369["Kiani, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kiani, F.",
    
)


# 2024_bib.md 
I12147["Yin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yin, J.",
    
)


# 2024_bib.md 
I84254["Wang, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wang, Z.",
    
)


# 2024_bib.md 
I1837["Joshua Yang, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Joshua Yang, J.",
    
)


# 2024_bib.md 
I56976["Xia, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xia, Q.",
    
)


# 2024_bib.md 
I51104["publication: A fully hardware-based memrist"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I47369["Kiani, F."], I12147["Yin, J."], I84254["Wang, Z."], I1837["Joshua Yang, J."], I56976["Xia, Q."]],
    R8434__has_title="A fully hardware-based memristive multilayer neural network",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I13464["Gokmen, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gokmen, T.",
    
)


# 2024_bib.md 
I36870["Vlasov, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Vlasov, Y.",
    
)


# 2024_bib.md 
I58774["publication: Acceleration of deep neural ne"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I13464["Gokmen, T."], I36870["Vlasov, Y."]],
    R8434__has_title="Acceleration of deep neural network training with resistive cross-point devices: Design considerations",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I88474["Fouda, M. E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fouda, M. E.",
    
)


# 2024_bib.md 
I66600["Lee, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lee, S.",
    
)


# 2024_bib.md 
I75844["Lee, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lee, J.",
    
)


# 2024_bib.md 
I73963["Eltawil, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Eltawil, A.",
    
)


# 2024_bib.md 
I41910["Kurdahi, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kurdahi, F.",
    
)


# 2024_bib.md 
I79146["publication: Mask technique for fast and ef"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I88474["Fouda, M. E."], I66600["Lee, S."], I75844["Lee, J."], I73963["Eltawil, A."], I41910["Kurdahi, F."]],
    R8434__has_title="Mask technique for fast and efficient training of binary resistive crossbar arrays",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I73731["Prezioso, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Prezioso, M.",
    
)


# 2024_bib.md 
I78650["publication: Training and operation of an i"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I73731["Prezioso, M."], I60665["et al."]],
    R8434__has_title="Training and operation of an integrated neuromorphic network based on metal-oxide memristors",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I15050["Hu, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hu, M.",
    
)


# 2024_bib.md 
I10578["publication: Memristor crossbar-based neuro"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15050["Hu, M."], I60665["et al."]],
    R8434__has_title="Memristor crossbar-based neuromorphic computing system: A case study",
    R8435__has_year=2014,
    
)


# 2024_bib.md 
I8748["publication: Dot-product engine for neuromo"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15050["Hu, M."], I60665["et al."]],
    R8434__has_title="Dot-product engine for neuromorphic computing",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I45648["Liu, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Liu, C.",
    
)


# 2024_bib.md 
I66282["Strachan, J. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Strachan, J. P.",
    
)


# 2024_bib.md 
I71268["Li, H. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, H. H.",
    
)


# 2024_bib.md 
I56031["publication: Rescuing memristorbased neurom"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I45648["Liu, C."], I15050["Hu, M."], I66282["Strachan, J. P."], I71268["Li, H. H."]],
    R8434__has_title="Rescuing memristorbased neuromorphic design with high defects",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I21727["Romero-Zaliz, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Romero-Zaliz, R.",
    
)


# 2024_bib.md 
I49840["Pérez, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pérez, E.",
    
)


# 2024_bib.md 
I6297["Jiménez-Molinos, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jiménez-Molinos, F.",
    
)


# 2024_bib.md 
I39887["Wenger, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wenger, C.",
    
)


# 2024_bib.md 
I85070["Roldán, J. B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Roldán, J. B.",
    
)


# 2024_bib.md 
I55806["publication: Study of quantized hardware de"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I21727["Romero-Zaliz, R."], I49840["Pérez, E."], I6297["Jiménez-Molinos, F."], I39887["Wenger, C."], I85070["Roldán, J. B."]],
    R8434__has_title="Study of quantized hardware deep neural networks based on resistive switching devices, conventional versus convolutional approaches",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I43511["publication: Advanced temperature dependent"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I49840["Pérez, E."], I60665["et al."]],
    R8434__has_title="Advanced temperature dependent statistical analysis of forming voltage distributions for three different HfO2-",
    
)


# 2024_bib.md 
I22386["Pérez-Bosch Quesada, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pérez-Bosch Quesada, E.",
    
)


# 2024_bib.md 
I67258["publication: Toward reliable compact modeli"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I22386["Pérez-Bosch Quesada, E."], I60665["et al."]],
    R8434__has_title="Toward reliable compact modeling of multilevel 1T-1R RRAM devices for neuromorphic systems",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I97751["Xia, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xia, L.",
    
)


# 2024_bib.md 
I82053["publication: Stuck-at Fault Tolerance in RR"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I97751["Xia, L."], I60665["et al."]],
    R8434__has_title="Stuck-at Fault Tolerance in RRAM Computing Systems",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I67957["publication: CMOS-integrated nanoscale memr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I87992["Li, C."], I60665["et al."]],
    R8434__has_title="CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I95101["Pedretti, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pedretti, G.",
    
)


# 2024_bib.md 
I30784["publication: Redundancy and analog slicing "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I95101["Pedretti, G."], I60665["et al."]],
    R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I74053["publication: Redundancy and analog slicing 2"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I95101["Pedretti, G."], I60665["et al."]],
    R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I60580["publication: Fully memristive neural networ"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I84254["Wang, Z."], I60665["et al."]],
    R8434__has_title="Fully memristive neural networks for pattern classification with unsupervised learning",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I88740["T. Rabuske"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="T. Rabuske",
    
)


# 2024_bib.md 
I11114["J. Fernandes"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="J. Fernandes",
    
)


# 2024_bib.md 
I13786["publication: Charge-Sharing SAR ADCs for lo"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I88740["T. Rabuske"], I11114["J. Fernandes"]],
    R8434__has_title="Charge-Sharing SAR ADCs for lowvoltage low-power applications",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I22195["Kumar, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kumar, P.",
    
)


# 2024_bib.md 
I93525["publication: Hybrid architecture based on t"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I22195["Kumar, P."], I60665["et al."]],
    R8434__has_title="Hybrid architecture based on two-dimensional memristor crossbar array and CMOS integrated circuit for edge computing",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I18596["Krestinskaya, O."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Krestinskaya, O.",
    
)


# 2024_bib.md 
I53810["Salama, K. N."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Salama, K. N.",
    
)


# 2024_bib.md 
I15074["James, A. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="James, A. P.",
    
)


# 2024_bib.md 
I64389["publication: Learning in memristive neural "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I18596["Krestinskaya, O."], I53810["Salama, K. N."], I15074["James, A. P."]],
    R8434__has_title="Learning in memristive neural network architectures using analog backpropagation circuits",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I62101["Chua, L. O."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chua, L. O.",
    
)


# 2024_bib.md 
I3120["Tetzlaff, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Tetzlaff, R.",
    
)


# 2024_bib.md 
I98516["Slavova, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Slavova, A.",
    
)


# 2024_bib.md 
I32025["publication: Memristor Computing Systems"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I62101["Chua, L. O."], I3120["Tetzlaff, R."], I98516["Slavova, A."]],
    R8434__has_title="Memristor Computing Systems",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I9682["Oh, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Oh, S.",
    
)


# 2024_bib.md 
I22597["publication: Energy-efficient Mott activati"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I9682["Oh, S."], I60665["et al."]],
    R8434__has_title="Energy-efficient Mott activation neuron for fullhardware implementation of neural networks",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I2571["Ambrogio, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ambrogio, S.",
    
)


# 2024_bib.md 
I44753["publication: Equivalent-accuracy accelerate"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I2571["Ambrogio, S."], I60665["et al."]],
    R8434__has_title="Equivalent-accuracy accelerated neural network training using analogue memory",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I96741["Bocquet, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Bocquet, M.",
    
)


# 2024_bib.md 
I88080["publication: In-memory and error-immune dif"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I96741["Bocquet, M."], I60665["et al."]],
    R8434__has_title="In-memory and error-immune differential RRAM implementation of binarized deep neural networks",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I26547["Cheng, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Cheng, M.",
    
)


# 2024_bib.md 
I48203["publication: TIME: A Training-in-memory arc"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I26547["Cheng, M."], I60665["et al."]],
    R8434__has_title="TIME: A Training-in-memory architecture for Memristor-based deep neural networks",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I32397["Chi, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chi, P.",
    
)


# 2024_bib.md 
I89377["publication: PRIME: A novel processing-in-m"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I32397["Chi, P."], I60665["et al."]],
    R8434__has_title="PRIME: A novel processing-in-memory architecture for neural network computation in ReRAM-based main memory",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I53917["Choubey, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Choubey, B.",
    
)


# 2024_bib.md 
I4628["publication: Memristive GAN in Analog"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I18596["Krestinskaya, O."], I53917["Choubey, B."], I15074["James, A. P."]],
    R8434__has_title="Memristive GAN in Analog",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I22186["Li, G. H. Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, G. H. Y.",
    
)


# 2024_bib.md 
I62904["publication: All-optical ultrafast ReLU fun"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I22186["Li, G. H. Y."], I60665["et al."]],
    R8434__has_title="All-optical ultrafast ReLU function for energy-efficient nanophotonic deep learning",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I98627["Ando, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ando, K.",
    
)


# 2024_bib.md 
I73752["publication: BRein memory: a single-chip bi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I98627["Ando, K."], I60665["et al."]],
    R8434__has_title="BRein memory: a single-chip binary/ternary reconfigurable in-memory deep neural network accelerator achieving 1.4 TOPS at 0.6 W",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I77303["Price, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Price, M.",
    
)


# 2024_bib.md 
I14787["Glass, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Glass, J.",
    
)


# 2024_bib.md 
I95781["publication: A scalable speech recognizer w"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I77303["Price, M."], I14787["Glass, J."], I49299["Chandrakasan, A. P."]],
    R8434__has_title="A scalable speech recognizer with deep-neural-network acoustic models and voice-",
    
)


# 2024_bib.md 
I98271["publication: A 1.06-to-5.09 TOPS/W reconfig"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I98878["Yin, S."], I60665["et al."]],
    R8434__has_title="A 1.06-to-5.09 TOPS/W reconfigurable hybrid neural-network processor for deep learning applications",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I91887["Chen, Y. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chen, Y. H.",
    
)


# 2024_bib.md 
I80011["Krishna, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Krishna, T.",
    
)


# 2024_bib.md 
I97489["Emer, J. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Emer, J. S.",
    
)


# 2024_bib.md 
I77461["Sze, V."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sze, V.",
    
)


# 2024_bib.md 
I32449["publication: Eyeriss: An energy-efficient r"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I91887["Chen, Y. H."], I80011["Krishna, T."], I97489["Emer, J. S."], I77461["Sze, V."]],
    R8434__has_title="Eyeriss: An energy-efficient reconfigurable accelerator for deep convolutional neural networks",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I82221["Lazzaro, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lazzaro, J.",
    
)


# 2024_bib.md 
I23208["Ryckebusch, S. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ryckebusch, S. M.",
    
)


# 2024_bib.md 
I81899["Mahowald, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mahowald, A.",
    
)


# 2024_bib.md 
I12477["publication: Winner-Take-All Networks of O("].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I82221["Lazzaro, J."], I23208["Ryckebusch, S. M."], I81899["Mahowald, A."], I61262["Mead, C. A."]],
    R8434__has_title="Winner-Take-All Networks of O(N) Complexity",
    R8435__has_year=1988,
    
)


# 2024_bib.md 
I43845["Andreou, A. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Andreou, A. G.",
    
)


# 2024_bib.md 
I27217["publication: Current-mode subthreshold MOS "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I43845["Andreou, A. G."],
    R8434__has_title="Current-mode subthreshold MOS circuits for analog VLSI neural systems",
    R8435__has_year=1991,
    
)


# 2024_bib.md 
I42841["Pouliquen, P. O."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pouliquen, P. O.",
    
)


# 2024_bib.md 
I40548["Strohbehn, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Strohbehn, K.",
    
)


# 2024_bib.md 
I94901["Jenkins, R. E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jenkins, R. E.",
    
)


# 2024_bib.md 
I95801["publication: Associative memory integrated "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I42841["Pouliquen, P. O."], I43845["Andreou, A. G."], I40548["Strohbehn, K."], I94901["Jenkins, R. E."]],
    R8434__has_title="Associative memory integrated system for character recognition",
    R8435__has_year=1993,
    
)


# 2024_bib.md 
I62543["Starzyk, J. A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Starzyk, J. A.",
    
)


# 2024_bib.md 
I62880["Fang, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fang, X.",
    
)


# 2024_bib.md 
I11307["publication: CMOS current mode winner-take-"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I62543["Starzyk, J. A."], I62880["Fang, X."]],
    R8434__has_title="CMOS current mode winner-take-all circuit with both excitatory and inhibitory feedback",
    R8435__has_year=1993,
    
)


# 2024_bib.md 
I72302["DeWeerth, S. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="DeWeerth, S. P.",
    
)


# 2024_bib.md 
I78560["Morris, T. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Morris, T. G.",
    
)


# 2024_bib.md 
I52910["publication: CMOS current mode winner-takea"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I72302["DeWeerth, S. P."], I78560["Morris, T. G."]],
    R8434__has_title="CMOS current mode winner-takeall circuit with distributed hysteresis",
    R8435__has_year=1995,
    
)


# 2024_bib.md 
I6510["Indiveri, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Indiveri, G.",
    
)


# 2024_bib.md 
I59370["publication: A current-mode hysteretic winn"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I6510["Indiveri, G."],
    R8434__has_title="A current-mode hysteretic winner-take-all network, with excitatory and inhibitory coupling",
    R8435__has_year=2001,
    
)


# 2024_bib.md 
I43562["Tan, B. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Tan, B. P.",
    
)


# 2024_bib.md 
I99776["Wilson, D. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wilson, D. M.",
    
)


# 2024_bib.md 
I36552["publication: Semiparallel rank order filter"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I43562["Tan, B. P."], I99776["Wilson, D. M."]],
    R8434__has_title="Semiparallel rank order filtering in analog VLSI",
    R8435__has_year=2001,
    
)


# 2024_bib.md 
I86940["Serrano, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Serrano, T.",
    
)


# 2024_bib.md 
I84649["Linares-Barranco, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Linares-Barranco, B.",
    
)


# 2024_bib.md 
I11737["publication: Modular current-mode highpreci"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I86940["Serrano, T."], I84649["Linares-Barranco, B."]],
    R8434__has_title="Modular current-mode highprecision winner-take-all circuit",
    R8435__has_year=1994,
    
)


# 2024_bib.md 
I4937["Meador, J. L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Meador, J. L.",
    
)


# 2024_bib.md 
I32825["Hylander, P. D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hylander, P. D.",
    
)


# 2024_bib.md 
I77144["publication: Pulse Coded Winner-Take-All Ne"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I4937["Meador, J. L."], I32825["Hylander, P. D."]],
    R8434__has_title="Pulse Coded Winner-Take-All Networks",
    R8435__has_year=1994,
    
)


# 2024_bib.md 
I46246["El-Masry, E. I."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="El-Masry, E. I.",
    
)


# 2024_bib.md 
I33641["Yang, H. K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yang, H. K.",
    
)


# 2024_bib.md 
I32743["Yakout, M. A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yakout, M. A.",
    
)


# 2024_bib.md 
I26808["publication: Implementations of artificial "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I46246["El-Masry, E. I."], I33641["Yang, H. K."], I32743["Yakout, M. A."]],
    R8434__has_title="Implementations of artificial neural networks using current-mode pulse width modulation technique",
    R8435__has_year=1997,
    
)


# 2024_bib.md 
I86409["Choi, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Choi, J.",
    
)


# 2024_bib.md 
I44397["Sheu, B. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sheu, B. J.",
    
)


# 2024_bib.md 
I53384["publication: A high-precision vlsi winner-t"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I86409["Choi, J."], I44397["Sheu, B. J."]],
    R8434__has_title="A high-precision vlsi winner-take-all circuit for self-organizing neural networks",
    R8435__has_year=1993,
    
)


# 2024_bib.md 
I84035["Yu, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yu, H.",
    
)


# 2024_bib.md 
I89773["Miyaoka, R. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Miyaoka, R. S.",
    
)


# 2024_bib.md 
I54780["publication: A High-Speed and High-Precisio"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I84035["Yu, H."], I89773["Miyaoka, R. S."]],
    R8434__has_title="A High-Speed and High-Precision Winner-Select-Output (WSO) ASIC",
    R8435__has_year=1998,
    
)


# 2024_bib.md 
I31896["Lau, K. T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lau, K. T.",
    
)


# 2024_bib.md 
I66327["Lee, S. T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lee, S. T.",
    
)


# 2024_bib.md 
I63400["publication: A CMOS winner-takes-all circui"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I31896["Lau, K. T."], I66327["Lee, S. T."]],
    R8434__has_title="A CMOS winner-takes-all circuit for self-organizing neural networks",
    R8435__has_year=2010,
    
)


# 2024_bib.md 
I36418["He, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="He, Y.",
    
)


# 2024_bib.md 
I68779["Sánchez-Sinencio, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sánchez-Sinencio, E.",
    
)


# 2024_bib.md 
I11624["publication: Min-net winner-take-all CMOS i"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I36418["He, Y."], I68779["Sánchez-Sinencio, E."]],
    R8434__has_title="Min-net winner-take-all CMOS implementation",
    R8435__has_year=1993,
    
)


# 2024_bib.md 
I91103["Demosthenous, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Demosthenous, A.",
    
)


# 2024_bib.md 
I98003["Smedley, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Smedley, S.",
    
)


# 2024_bib.md 
I76493["Taylor, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Taylor, J.",
    
)


# 2024_bib.md 
I65504["publication: A CMOS analog winner-take-all "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I91103["Demosthenous, A."], I98003["Smedley, S."], I76493["Taylor, J."]],
    R8434__has_title="A CMOS analog winner-take-all network for large-scale applications",
    R8435__has_year=1998,
    
)


# 2024_bib.md 
I56660["publication: Winner-Takes-All associative m"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I42841["Pouliquen, P. O."], I43845["Andreou, A. G."], I40548["Strohbehn, K."]],
    R8434__has_title="Winner-Takes-All associative memory: A hamming distance vector quantizer",
    R8435__has_year=1997,
    
)


# 2024_bib.md 
I15377["Fish, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fish, A.",
    
)


# 2024_bib.md 
I61179["Milrud, V."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Milrud, V.",
    
)


# 2024_bib.md 
I31858["Yadid-Pecht, O."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yadid-Pecht, O.",
    
)


# 2024_bib.md 
I82458["publication: High-speed and high-precision "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15377["Fish, A."], I61179["Milrud, V."], I31858["Yadid-Pecht, O."]],
    R8434__has_title="High-speed and high-precision current winner-take-all circuit",
    R8435__has_year=2005,
    
)


# 2024_bib.md 
I30242["Ohnhäuser, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ohnhäuser, F.",
    
)


# 2024_bib.md 
I13701["publication: Analog-Digital Converters for "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I30242["Ohnhäuser, F."],
    R8434__has_title="Analog-Digital Converters for Industrial Applications Including an Introduction to Digital-Analog Converters",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I68953["Pavan, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pavan, S.",
    
)


# 2024_bib.md 
I38138["Schreier, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Schreier, R.",
    
)


# 2024_bib.md 
I36635["Temes, G. C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Temes, G. C.",
    
)


# 2024_bib.md 
I80819["publication: Understanding Delta-Sigma Data"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I68953["Pavan, S."], I38138["Schreier, R."], I36635["Temes, G. C."]],
    R8434__has_title="Understanding Delta-Sigma Data Converters.",
    
)


# 2024_bib.md 
I26114["Walden, R. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Walden, R. H.",
    
)


# 2024_bib.md 
I17993["publication: Analog-to-digital converter su"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I26114["Walden, R. H."],
    R8434__has_title="Analog-to-digital converter survey and analysis",
    R8435__has_year=1999,
    
)


# 2024_bib.md 
I39688["Harpe, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Harpe, P.",
    
)


# 2024_bib.md 
I87435["Gao, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gao, H.",
    
)


# 2024_bib.md 
I63949["Van Dommele, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Van Dommele, R.",
    
)


# 2024_bib.md 
I59350["Cantatore, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Cantatore, E.",
    
)


# 2024_bib.md 
I93987["Van Roermund, A. H. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Van Roermund, A. H. M.",
    
)


# 2024_bib.md 
I36907["publication: A 0.20 mm2 3 nW signal acquisi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I39688["Harpe, P."], I87435["Gao, H."], I63949["Van Dommele, R."], I59350["Cantatore, E."], I93987["Van Roermund, A. H. M."]],
    R8434__has_title="A 0.20 mm2 3 nW signal acquisition IC for miniature sensor nodes in 65 nm CMOS",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I22322["publication: ADC Performance Survey 1997-20"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I18985["Murmann, B."],
    R8434__has_title="ADC Performance Survey 1997-2022",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I13679["publication: PUMA: A Programmable Ultra-eff"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I60267["Ankit, A."], I60665["et al."]],
    R8434__has_title="PUMA: A Programmable Ultra-efficient Memristor-based Accelerator for Machine Learning Inference",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I28334["Ni, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ni, L.",
    
)


# 2024_bib.md 
I66551["publication: An energy-efficient matrix mul"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I28334["Ni, L."], I60665["et al."]],
    R8434__has_title="An energy-efficient matrix multiplication accelerator by distributed in-memory computing on binary RRAM crossbar",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I36221["Lu, W. D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lu, W. D.",
    
)


# 2024_bib.md 
I6152["publication: RRAM-enabled AI Accelerator Ar"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I3591["Wang, X."], I84376["Wu, Y."], I36221["Lu, W. D."]],
    R8434__has_title="RRAM-enabled AI Accelerator Architecture",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I15365["Xiao, T. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xiao, T. P.",
    
)


# 2024_bib.md 
I75041["publication: On the Accuracy of Analog Neur"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15365["Xiao, T. P."], I60665["et al."]],
    R8434__has_title="On the Accuracy of Analog Neural Network Inference Accelerators",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I43110["publication: XNOR-RRAM: A scalable and para"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I76458["Sun, X."], I10778["et al"]],
    R8434__has_title="XNOR-RRAM: A scalable and parallel resistive synaptic architecture for binary neural networks",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I3393["Zhang, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhang, W.",
    
)


# 2024_bib.md 
I32055["publication: Neuro-inspired computing chips"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I3393["Zhang, W."], I60665["et al."]],
    R8434__has_title="Neuro-inspired computing chips",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I99575["Shafiee, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Shafiee, A.",
    
)


# 2024_bib.md 
I80100["publication: ISAAC: A Convolutional Neural "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I99575["Shafiee, A."], I60665["et al."]],
    R8434__has_title="ISAAC: A Convolutional Neural Network Accelerator with In-Situ Analog Arithmetic in Crossbars",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I47541["Fujiki, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fujiki, D.",
    
)


# 2024_bib.md 
I46178["Mahlke, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mahlke, S.",
    
)


# 2024_bib.md 
I58992["Das, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Das, R.",
    
)


# 2024_bib.md 
I97679["publication: In-memory data parallel proces"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I47541["Fujiki, D."], I46178["Mahlke, S."], I58992["Das, R."]],
    R8434__has_title="In-memory data parallel processor",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I67161["Nourazar, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Nourazar, M.",
    
)


# 2024_bib.md 
I5530["Rashtchi, V."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Rashtchi, V.",
    
)


# 2024_bib.md 
I15538["Azarpeyvand, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Azarpeyvand, A.",
    
)


# 2024_bib.md 
I15436["publication: Memristor-based approximate ma"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I67161["Nourazar, M."], I5530["Rashtchi, V."], I15538["Azarpeyvand, A."], I91097["Merrikh-Bayat, F."]],
    R8434__has_title="Memristor-based approximate matrix multiplier",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I85361["Saberi, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Saberi, M.",
    
)


# 2024_bib.md 
I68019["Lotfi, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lotfi, R.",
    
)


# 2024_bib.md 
I3925["Mafinezhad, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mafinezhad, K.",
    
)


# 2024_bib.md 
I9150["Serdijn, W. A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Serdijn, W. A.",
    
)


# 2024_bib.md 
I29966["publication: Analysis of power consumption "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I85361["Saberi, M."], I68019["Lotfi, R."], I3925["Mafinezhad, K."], I9150["Serdijn, W. A."]],
    R8434__has_title="Analysis of power consumption and linearity in capacitive digital-to-analog converters used in successive approximation ADCs",
    R8435__has_year=2011,
    
)


# 2024_bib.md 
I55344["Kull, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kull, L.",
    
)


# 2024_bib.md 
I93933["publication: A 3.1 mW 8b 1.2 GS/s single-Ch"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I55344["Kull, L."], I60665["et al."]],
    R8434__has_title="A 3.1 mW 8b 1.2 GS/s single-Channel asynchronous SAR ADC with alternate comparators for enhanced speed in 32 nm digital SOI CMOS",
    R8435__has_year=2013,
    
)


# 2024_bib.md 
I31314["Hagan, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hagan, M.",
    
)


# 2024_bib.md 
I94653["Demuth, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Demuth, H.",
    
)


# 2024_bib.md 
I37296["Beale, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Beale, M.",
    
)


# 2024_bib.md 
I78153["De Jesús, O."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="De Jesús, O.",
    
)


# 2024_bib.md 
I81477["publication: Neural Network Design"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I31314["Hagan, M."], I94653["Demuth, H."], I37296["Beale, M."], I78153["De Jesús, O."]],
    R8434__has_title="Neural Network Design",
    R8435__has_year=2014,
    
)


# 2024_bib.md 
I97169["Choi, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Choi, S.",
    
)


# 2024_bib.md 
I80229["Sheridan, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sheridan, P.",
    
)


# 2024_bib.md 
I12368["publication: Data clustering using memristo"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I97169["Choi, S."], I80229["Sheridan, P."], I36221["Lu, W. D."]],
    R8434__has_title="Data clustering using memristor networks",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I54164["publication: HERMES Core: A 14nm CMOS and P"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I93276["Khaddam-Aljameh, R."], I60665["et al."]],
    R8434__has_title="HERMES Core: A 14nm CMOS and PCM-based In-Memory Compute Core using an array of 300ps/ LSB Linearized CCO-based ADCs and local digital processing",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I48329["Kennedy, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kennedy, J.",
    
)


# 2024_bib.md 
I10466["Eberhart, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Eberhart, R.",
    
)


# 2024_bib.md 
I85491["publication: Particle swarm optimization"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I48329["Kennedy, J."], I10466["Eberhart, R."]],
    R8434__has_title="Particle swarm optimization",
    R8435__has_year=1995,
    
)


# 2024_bib.md 
I87251["Goldberg, D. E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Goldberg, D. E.",
    
)


# 2024_bib.md 
I1064["Holland, J. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Holland, J. H.",
    
)


# 2024_bib.md 
I82112["publication: Genetic Algorithms and machine"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I87251["Goldberg, D. E."], I1064["Holland, J. H."]],
    R8434__has_title="Genetic Algorithms and machine learning",
    R8435__has_year=1988,
    
)


# 2024_bib.md 
I79938["Kirkpatrick, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kirkpatrick, S.",
    
)


# 2024_bib.md 
I30361["Gelatt, C. D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gelatt, C. D.",
    
)


# 2024_bib.md 
I18375["Vecchi, M. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Vecchi, M. P.",
    
)


# 2024_bib.md 
I45745["publication: Optimization by simulated anne"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I79938["Kirkpatrick, S."], I30361["Gelatt, C. D."], I18375["Vecchi, M. P."]],
    R8434__has_title="Optimization by simulated annealing",
    R8435__has_year=1983,
    
)


# 2024_bib.md 
I44585["Rumelhart, D. E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Rumelhart, D. E.",
    
)


# 2024_bib.md 
I82729["Hinton, G. E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hinton, G. E.",
    
)


# 2024_bib.md 
I33331["Williams, R. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Williams, R. J.",
    
)


# 2024_bib.md 
I21301["publication: Learning representations by ba"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I44585["Rumelhart, D. E."], I82729["Hinton, G. E."], I33331["Williams, R. J."]],
    R8434__has_title="Learning representations by back-propagating errors",
    R8435__has_year=1986,
    
)


# 2024_bib.md 
I40424["Dennis, J. E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Dennis, J. E.",
    
)


# 2024_bib.md 
I75542["Schnabel, R. B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Schnabel, R. B.",
    
)


# 2024_bib.md 
I93813["publication: Numerical Methods for Unconstr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I40424["Dennis, J. E."], I75542["Schnabel, R. B."]],
    R8434__has_title="Numerical Methods for Unconstrained Optimization and Nonlinear Equations",
    R8435__has_year=1996,
    
)


# 2024_bib.md 
I69907["Møller, M. F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Møller, M. F.",
    
)


# 2024_bib.md 
I64828["publication: A scaled conjugate gradient al"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I69907["Møller, M. F."],
    R8434__has_title="A scaled conjugate gradient algorithm for fast supervised learning",
    R8435__has_year=1993,
    
)


# 2024_bib.md 
I78457["Powell, M. J. D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Powell, M. J. D.",
    
)


# 2024_bib.md 
I97315["publication: Restart procedures for the con"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I78457["Powell, M. J. D."],
    R8434__has_title="Restart procedures for the conjugate gradient method",
    R8435__has_year=1977,
    
)


# 2024_bib.md 
I71929["Fletcher, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fletcher, R.",
    
)


# 2024_bib.md 
I89265["publication: Function minimization by conju"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I71929["Fletcher, R."],
    R8434__has_title="Function minimization by conjugate gradients",
    R8435__has_year=1964,
    
)


# 2024_bib.md 
I17113["Marquardt, D. W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Marquardt, D. W.",
    
)


# 2024_bib.md 
I23478["publication: An algorithm for least-squares"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I17113["Marquardt, D. W."],
    R8434__has_title="An algorithm for least-squares estimation of nonlinear parameters",
    R8435__has_year=1963,
    
)


# 2024_bib.md 
I39360["Riedmiller, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Riedmiller, M.",
    
)


# 2024_bib.md 
I79037["Braun, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Braun, H.",
    
)


# 2024_bib.md 
I94678["publication: Direct adaptive method for fas"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I39360["Riedmiller, M."], I79037["Braun, H."]],
    R8434__has_title="Direct adaptive method for faster backpropagation learning: The RPROP algorithm",
    R8435__has_year=1993,
    
)


# 2024_bib.md 
I37221["Battiti, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Battiti, R.",
    
)


# 2024_bib.md 
I11187["publication: First- and second-order method"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I37221["Battiti, R."],
    R8434__has_title="First- and second-order methods for learning: between steepest descent and Newton's Method",
    R8435__has_year=1992,
    
)


# 2024_bib.md 
I9576["Bottou, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Bottou, L.",
    
)


# 2024_bib.md 
I13450["publication: Stochastic gradient descent tr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I9576["Bottou, L."],
    R8434__has_title="Stochastic gradient descent tricks",
    R8435__has_year=2012,
    
)


# 2024_bib.md 
I72065["Li, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, M.",
    
)


# 2024_bib.md 
I53665["Zhang, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhang, T.",
    
)


# 2024_bib.md 
I75737["Chen, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chen, Y.",
    
)


# 2024_bib.md 
I12456["Smola, A. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Smola, A. J.",
    
)


# 2024_bib.md 
I23048["publication: Efficient mini-batch training "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I72065["Li, M."], I53665["Zhang, T."], I75737["Chen, Y."], I12456["Smola, A. J."]],
    R8434__has_title="Efficient mini-batch training for stochastic optimization",
    R8435__has_year=2014,
    
)


# 2024_bib.md 
I66505["Zamanidoost, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zamanidoost, E.",
    
)


# 2024_bib.md 
I62828["Bayat, F. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Bayat, F. M.",
    
)


# 2024_bib.md 
I31085["Strukov, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Strukov, D.",
    
)


# 2024_bib.md 
I22251["Kataeva, I."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kataeva, I.",
    
)


# 2024_bib.md 
I52492["publication: Manhattan rule training for me"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I66505["Zamanidoost, E."], I62828["Bayat, F. M."], I31085["Strukov, D."], I22251["Kataeva, I."]],
    R8434__has_title="Manhattan rule training for memristive crossbar circuit pattern classifiers",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I5558["Duchi, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Duchi, J.",
    
)


# 2024_bib.md 
I84355["Hazan, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hazan, E.",
    
)


# 2024_bib.md 
I43372["Singer, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Singer, Y.",
    
)


# 2024_bib.md 
I77183["publication: Adaptive subgradient methods f"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I5558["Duchi, J."], I84355["Hazan, E."], I43372["Singer, Y."]],
    R8434__has_title="Adaptive subgradient methods for online learning and stochastic optimization",
    R8435__has_year=2011,
    
)


# 2024_bib.md 
I82881["Geoffrey Hinton"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Geoffrey Hinton",
    
)


# 2024_bib.md 
I79664["publication: Neural Networks for Machine Le"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I82881["Geoffrey Hinton"],
    R8434__has_title="Neural Networks for Machine Learning",
    
)


# 2024_bib.md 
I81700["Kingma, D. P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kingma, D. P.",
    
)


# 2024_bib.md 
I51455["Ba, J. L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ba, J. L.",
    
)


# 2024_bib.md 
I24925["publication: Adam: A Method for Stochastic "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I81700["Kingma, D. P."], I51455["Ba, J. L."]],
    R8434__has_title="Adam: A Method for Stochastic Optimization",
    R8435__has_year=2014,
    
)


# 2024_bib.md 
I31684["Zeiler, M. D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zeiler, M. D.",
    
)


# 2024_bib.md 
I99538["publication: ADADELTA: An adaptive learning"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I31684["Zeiler, M. D."],
    R8434__has_title="ADADELTA: An adaptive learning rate method",
    R8435__has_year=2012,
    
)


# 2024_bib.md 
I33941["Xiong, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xiong, X.",
    
)


# 2024_bib.md 
I45772["publication: Reconfigurable logic-in-memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I33941["Xiong, X."], I60665["et al."]],
    R8434__has_title="Reconfigurable logic-in-memory and multilingual artificial synapses based on 2D heterostructures",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I95251["Zoppo, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zoppo, G.",
    
)


# 2024_bib.md 
I64422["Marrone, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Marrone, F.",
    
)


# 2024_bib.md 
I78497["Corinto, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Corinto, F.",
    
)


# 2024_bib.md 
I13328["publication: Equilibrium propagation for me"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I95251["Zoppo, G."], I64422["Marrone, F."], I78497["Corinto, F."]],
    R8434__has_title="Equilibrium propagation for memristor-based recurrent neural networks",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I35141["Alibart, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Alibart, F.",
    
)


# 2024_bib.md 
I92353["publication: Pattern classification by memr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I35141["Alibart, F."], I66505["Zamanidoost, E."], I27966["Strukov, D. B."]],
    R8434__has_title="Pattern classification by memristive crossbar circuits using ex situ and in situ training",
    R8435__has_year=2013,
    
)


# 2024_bib.md 
I2008["Joshi, V."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Joshi, V.",
    
)


# 2024_bib.md 
I42437["publication: Accurate deep neural network i"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I2008["Joshi, V."], I60665["et al."]],
    R8434__has_title="Accurate deep neural network inference using computational phase-change memory",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I6968["Rasch, M. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Rasch, M. J.",
    
)


# 2024_bib.md 
I36817["publication: Hardware-aware training for la"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I6968["Rasch, M. J."], I60665["et al."]],
    R8434__has_title="Hardware-aware training for large-scale and diverse deep learning inference workloads using in-memory computing-based accelerators",
    R8435__has_year=2023,
    
)


# 2024_bib.md 
I10063["Huang, H.-M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Huang, H.-M.",
    
)


# 2024_bib.md 
I65484["Wang, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wang, T.",
    
)


# 2024_bib.md 
I55500["Xiao, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xiao, Y.",
    
)


# 2024_bib.md 
I33489["Guo, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Guo, X.",
    
)


# 2024_bib.md 
I67348["publication: Artificial neural networks bas"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I10063["Huang, H.-M."], I84254["Wang, Z."], I65484["Wang, T."], I55500["Xiao, Y."], I33489["Guo, X."]],
    R8434__has_title="Artificial neural networks based on memristive devices: from device to system",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I17979["Nandakumar, S. R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Nandakumar, S. R.",
    
)


# 2024_bib.md 
I26369["publication: Mixed-precision deep learning "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I17979["Nandakumar, S. R."], I60665["et al."]],
    R8434__has_title="Mixed-precision deep learning based on computational memory",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I88187["publication: Mixed-precision in-memory comp"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I39708["Le Gallo, M."], I60665["et al."]],
    R8434__has_title="Mixed-precision in-memory computing",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I28475["publication: Face classification using elec"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I42033["Yao, P."], I60665["et al."]],
    R8434__has_title="Face classification using electronic synapses",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I60983["Papandreou, N."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Papandreou, N.",
    
)


# 2024_bib.md 
I28936["publication: Programming algorithms for mul"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I60983["Papandreou, N."], I60665["et al."]],
    R8434__has_title="Programming algorithms for multilevel phase-change memory",
    R8435__has_year=2011,
    
)


# 2024_bib.md 
I38939["Milo, V."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Milo, V.",
    
)


# 2024_bib.md 
I76769["publication: Multilevel HfO2-based RRAM dev"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I38939["Milo, V."], I60665["et al."]],
    R8434__has_title="Multilevel HfO2-based RRAM devices for lowpower neuromorphic networks",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I42158["publication: Scaling-up resistive synaptic "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I97154["Yu, S."], I60665["et al."]],
    R8434__has_title="Scaling-up resistive synaptic arrays for neuroinspired architecture: Challenges and prospect",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I18444["Woo, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Woo, J.",
    
)


# 2024_bib.md 
I16220["publication: Improved synaptic behavior und"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I18444["Woo, J."], I60665["et al."]],
    R8434__has_title="Improved synaptic behavior under identical pulses using AlOx/HfO2 bilayer RRAM array for neuromorphic systems",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I39094["Xiao, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xiao, S.",
    
)


# 2024_bib.md 
I96930["publication: GST-memristor-based online lea"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I39094["Xiao, S."], I60665["et al."]],
    R8434__has_title="GST-memristor-based online learning neural networks",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I76222["Tian, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Tian, H.",
    
)


# 2024_bib.md 
I59925["publication: A novel artificial synapse wit"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I76222["Tian, H."], I10778["et al"]],
    R8434__has_title="A novel artificial synapse with dual modes using bilayer graphene as the bottom electrode",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I7333["Shi, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Shi, T.",
    
)


# 2024_bib.md 
I28608["Yin, X. B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yin, X. B.",
    
)


# 2024_bib.md 
I24546["Yang, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yang, R.",
    
)


# 2024_bib.md 
I58871["publication: Pt/WO3/FTO memristive devices "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I7333["Shi, T."], I28608["Yin, X. B."], I24546["Yang, R."], I33489["Guo, X."]],
    R8434__has_title="Pt/WO3/FTO memristive devices with recoverable pseudo-electroforming for time-delay switches in neuromorphic computing",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I41422["Menzel, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Menzel, S.",
    
)


# 2024_bib.md 
I14175["publication: Origin of the ultra-nonlinear "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I41422["Menzel, S."], I60665["et al."]],
    R8434__has_title="Origin of the ultra-nonlinear switching kinetics in oxide-based resistive switches",
    R8435__has_year=2011,
    
)


# 2024_bib.md 
I40099["Buscarino, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Buscarino, A.",
    
)


# 2024_bib.md 
I60522["Fortuna, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fortuna, L.",
    
)


# 2024_bib.md 
I53325["Frasca, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Frasca, M.",
    
)


# 2024_bib.md 
I72877["Gambuzza, L. V."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gambuzza, L. V.",
    
)


# 2024_bib.md 
I67121["Sciuto, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sciuto, G.",
    
)


# 2024_bib.md 
I35151["publication: Memristive chaotic circuits ba"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I40099["Buscarino, A."], I60522["Fortuna, L."], I53325["Frasca, M."], I72877["Gambuzza, L. V."], I67121["Sciuto, G."]],
    R8434__has_title="Memristive chaotic circuits based on cellular nonlinear networks",
    R8435__has_year=2012,
    
)


# 2024_bib.md 
I79603["Li, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, Y.",
    
)


# 2024_bib.md 
I23744["Ang, K.-W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ang, K.-W.",
    
)


# 2024_bib.md 
I34521["publication: Hardware implementation of neu"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I79603["Li, Y."], I23744["Ang, K.-W."]],
    R8434__has_title="Hardware implementation of neuromorphic computing using large-scale memristor crossbar arrays",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I24214["Zhu, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhu, J.",
    
)


# 2024_bib.md 
I99392["Yang, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yang, Y.",
    
)


# 2024_bib.md 
I82361["Huang, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Huang, R.",
    
)


# 2024_bib.md 
I15303["publication: A comprehensive review on emer"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I24214["Zhu, J."], I53665["Zhang, T."], I99392["Yang, Y."], I82361["Huang, R."]],
    R8434__has_title="A comprehensive review on emerging artificial neuromorphic devices",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I80771["publication: Engineering incremental resist"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I84254["Wang, Z."], I60665["et al."]],
    R8434__has_title="Engineering incremental resistive switching in TaOx based memristors for brain-inspired computing",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I46726["Park, S. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Park, S. M.",
    
)


# 2024_bib.md 
I34860["publication: Improvement of conductance mod"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I46726["Park, S. M."], I60665["et al."]],
    R8434__has_title="Improvement of conductance modulation linearity in a Cu2+-Doped KNbO3 memristor through the increase of the number of oxygen vacancies",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I11959["Slesazeck, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Slesazeck, S.",
    
)


# 2024_bib.md 
I4382["Mikolajick, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mikolajick, T.",
    
)


# 2024_bib.md 
I14309["publication: Nanoscale resistive switching "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I11959["Slesazeck, S."], I4382["Mikolajick, T."]],
    R8434__has_title="Nanoscale resistive switching memory devices: a review",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I54143["Waser, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Waser, R.",
    
)


# 2024_bib.md 
I90495["Dittmann, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Dittmann, R.",
    
)


# 2024_bib.md 
I50839["Staikov, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Staikov, C.",
    
)


# 2024_bib.md 
I76881["Szot, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Szot, K.",
    
)


# 2024_bib.md 
I62042["publication: Redox-based resistive switchin"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I54143["Waser, R."], I90495["Dittmann, R."], I50839["Staikov, C."], I76881["Szot, K."]],
    R8434__has_title="Redox-based resistive switching memories nanoionic mechanisms, prospects, and challenges",
    R8435__has_year=2009,
    
)


# 2024_bib.md 
I3498["Ielmini, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ielmini, D.",
    
)


# 2024_bib.md 
I10110["publication: Resistive Switching"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I3498["Ielmini, D."], I54143["Waser, R."]],
    R8434__has_title="Resistive Switching",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I45564["Wouters, D. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wouters, D. J.",
    
)


# 2024_bib.md 
I83292["Wuttig, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wuttig, M.",
    
)


# 2024_bib.md 
I72286["publication: Phase-change and redoxbased re"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I45564["Wouters, D. J."], I54143["Waser, R."], I83292["Wuttig, M."]],
    R8434__has_title="Phase-change and redoxbased resistive switching memories",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I32305["Pan, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pan, F.",
    
)


# 2024_bib.md 
I6649["Gao, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gao, S.",
    
)


# 2024_bib.md 
I93204["Chen, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chen, C.",
    
)


# 2024_bib.md 
I41659["Song, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Song, C.",
    
)


# 2024_bib.md 
I26548["Zeng, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zeng, F.",
    
)


# 2024_bib.md 
I58101["publication: Recent progress in resistive r"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I32305["Pan, F."], I6649["Gao, S."], I93204["Chen, C."], I41659["Song, C."], I26548["Zeng, F."]],
    R8434__has_title="Recent progress in resistive random access memories: Materials, switching mechanisms, and performance",
    R8435__has_year=2014,
    
)


# 2024_bib.md 
I49776["Kim, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Kim, S.",
    
)


# 2024_bib.md 
I31658["publication: Analog synaptic behavior of a "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I49776["Kim, S."], I60665["et al."]],
    R8434__has_title="Analog synaptic behavior of a silicon nitride memristor",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I15725["Li, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, W.",
    
)


# 2024_bib.md 
I59746["Huang, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Huang, S.",
    
)


# 2024_bib.md 
I95140["Jiang, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jiang, H.",
    
)


# 2024_bib.md 
I96333["publication: A 40-nm MLC-RRAM compute-in-me"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15725["Li, W."], I76458["Sun, X."], I59746["Huang, S."], I95140["Jiang, H."], I97154["Yu, S."]],
    R8434__has_title="A 40-nm MLC-RRAM compute-in-memory macro with sparsity control, On-Chip Writeverify, and temperature-independent ADC references",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I98017["Buchel, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Buchel, J.",
    
)


# 2024_bib.md 
I2969["publication: Gradient descent-based program"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I98017["Buchel, J."], I60665["et al."]],
    R8434__has_title="Gradient descent-based programming of analog in-memory computing cores",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I53524["publication: Spike-timing-dependent plastic"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I73731["Prezioso, M."], I60665["et al."]],
    R8434__has_title="Spike-timing-dependent plasticity learning of coincidence detection with passively integrated memristive circuits",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I14604["Park, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Park, S.",
    
)


# 2024_bib.md 
I78668["publication: Electronic system with memrist"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I14604["Park, S."], I60665["et al."]],
    R8434__has_title="Electronic system with memristive synapses for pattern recognition",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I55153["publication: Binary neural network with 16 "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I97154["Yu, S."], I60665["et al."]],
    R8434__has_title="Binary neural network with 16 Mb RRAM macro chip for classification and online training",
    R8435__has_year=2017,
    
)


# 2024_bib.md 
I76191["Chen, W. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chen, W. H.",
    
)


# 2024_bib.md 
I22564["publication: CMOS-integrated memristive non"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I76191["Chen, W. H."], I60665["et al."]],
    R8434__has_title="CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I9645["publication: A 16Mb dual-mode ReRAM macro w"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I76191["Chen, W. H."], I60665["et al."]],
    R8434__has_title="A 16Mb dual-mode ReRAM macro with sub-14ns computing-in-memory and memory functions enabled by self-write termination scheme",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I65696["publication: Memristor-based analog computa"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15050["Hu, M."], I60665["et al."]],
    R8434__has_title="Memristor-based analog computation and neural network classification with a dot product engine",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I50193["publication: Analogue signal and image proc"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I87992["Li, C."], I60665["et al."]],
    R8434__has_title="Analogue signal and image processing with large memristor crossbars",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I50890["Paszke A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Paszke A.",
    
)


# 2024_bib.md 
I54273["publication: Automatic differentiation in P"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I50890["Paszke A."], I60665["et al."]],
    R8434__has_title="Automatic differentiation in PyTorch",
    
)


# 2024_bib.md 
I50771["Abadi, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Abadi, M.",
    
)


# 2024_bib.md 
I18159["publication: TensorFlow: Large-Scale Machin"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I50771["Abadi, M."], I60665["et al."]],
    R8434__has_title="TensorFlow: Large-Scale Machine Learning on Heterogeneous Systems",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I2373["Stimberg, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Stimberg, M.",
    
)


# 2024_bib.md 
I77558["Brette, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Brette, R.",
    
)


# 2024_bib.md 
I82721["Goodman, D. F. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Goodman, D. F. M.",
    
)


# 2024_bib.md 
I67271["publication: Brian 2, an intuitive and effi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I2373["Stimberg, M."], I77558["Brette, R."], I82721["Goodman, D. F. M."]],
    R8434__has_title="Brian 2, an intuitive and efficient neural simulator",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I62511["Spreizer, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Spreizer, S.",
    
)


# 2024_bib.md 
I88085["publication: NEST 3.3"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I62511["Spreizer, S."], I60665["et al."]],
    R8434__has_title="NEST 3.3",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I90843["Hazan, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hazan, H.",
    
)


# 2024_bib.md 
I27535["publication: BindsNET: A machine learning-o"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I90843["Hazan, H."], I60665["et al."]],
    R8434__has_title="BindsNET: A machine learning-oriented spiking neural networks library in python",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I49566["M. Y. Lin"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="M. Y. Lin",
    
)


# 2024_bib.md 
I63567["publication: DL-RSIM: A simulation framewor"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I49566["M. Y. Lin"], I60665["et al."]],
    R8434__has_title="DL-RSIM: A simulation framework to enable reliable ReRAM-based accelerators for deep learning",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I83247["publication: Impact of non-ideal characteri"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I76458["Sun, X."], I97154["Yu, S."]],
    R8434__has_title="Impact of non-ideal characteristics of resistive synaptic devices on implementing convolutional neural networks",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I23927["Ma, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ma, X.",
    
)


# 2024_bib.md 
I1444["publication: Tiny but Accurate: A Pruned, Q"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I23927["Ma, X."], I60665["et al."]],
    R8434__has_title="Tiny but Accurate: A Pruned, Quantized and Optimized Memristor Crossbar Framework for Ultra Efficient DNN Implementation",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I91883["Yuan, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yuan, G.",
    
)


# 2024_bib.md 
I76611["publication: An Ultra-Efficient Memristor-B"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I91883["Yuan, G."], I60665["et al."]],
    R8434__has_title="An Ultra-Efficient Memristor-Based DNN Framework with Structured Weight Pruning and Quantization Using ADMM",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I41680["publication: A flexible and fast PyTorch to"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I6968["Rasch, M. J."], I60665["et al."]],
    R8434__has_title="A flexible and fast PyTorch toolkit for simulating training and inference on analog crossbar arrays",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I32004["Grötker, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Grötker, T.",
    
)


# 2024_bib.md 
I48787["publication: System design with SystemC"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I32004["Grötker, T."],
    R8434__has_title="System design with SystemC",
    R8435__has_year=2002,
    
)


# 2024_bib.md 
I94376["Gajski, D. D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gajski, D. D.",
    
)


# 2024_bib.md 
I23668["publication: SpecC: specification language "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I94376["Gajski, D. D."],
    R8434__has_title="SpecC: specification language and methodology",
    R8435__has_year=2000,
    
)


# 2024_bib.md 
I30731["Lee, M. K. F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lee, M. K. F.",
    
)


# 2024_bib.md 
I68433["publication: A system-level simulator for R"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I30731["Lee, M. K. F."], I60665["et al."]],
    R8434__has_title="A system-level simulator for RRAM-based neuromorphic computing chips",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I5936["BanaGozar, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="BanaGozar, A.",
    
)


# 2024_bib.md 
I75090["publication: System simulation of memristor"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I5936["BanaGozar, A."], I60665["et al."]],
    R8434__has_title="System simulation of memristor based computation in memory platforms",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I58366["Gai, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gai, L.",
    
)


# 2024_bib.md 
I96129["Gajski, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gajski, D.",
    
)


# 2024_bib.md 
I11593["publication: Transaction level modeling: an"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I58366["Gai, L."], I96129["Gajski, D."]],
    R8434__has_title="Transaction level modeling: an overview",
    R8435__has_year=2003,
    
)


# 2024_bib.md 
I51750["Poremba, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Poremba, M.",
    
)


# 2024_bib.md 
I99505["Xie, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xie, Y.",
    
)


# 2024_bib.md 
I25420["publication: NVMain: An architectural-level"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I51750["Poremba, M."], I99505["Xie, Y."]],
    R8434__has_title="NVMain: An architectural-level main memory simulator for emerging non-volatile memories",
    R8435__has_year=2012,
    
)


# 2024_bib.md 
I63440["publication: NVMain 2.0: A user-friendly me"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I51750["Poremba, M."], I53665["Zhang, T."], I99505["Xie, Y."]],
    R8434__has_title="NVMain 2.0: A user-friendly memory simulator to model (non-)volatile memory systems",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I64964["publication: MNSIM: Simulation platform for"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I97751["Xia, L."], I60665["et al."]],
    R8434__has_title="MNSIM: Simulation platform for memristor-based neuromorphic computing system",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I90249["Zhu, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhu, Z.",
    
)


# 2024_bib.md 
I55106["publication: MNSIM 2.0: A behavior-level mo"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I90249["Zhu, Z."], I60665["et al."]],
    R8434__has_title="MNSIM 2.0: A behavior-level modeling tool for memristor-based neuromorphic computing systems",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I43024["Banagozar, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Banagozar, A.",
    
)


# 2024_bib.md 
I30610["publication: CIM-SIM: Computation in Memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I43024["Banagozar, A."], I60665["et al."]],
    R8434__has_title="CIM-SIM: Computation in Memory SIMuIator",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I31482["Fei, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fei, X.",
    
)


# 2024_bib.md 
I39247["Zhang, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhang, Y.",
    
)


# 2024_bib.md 
I80994["Zheng, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zheng, W.",
    
)


# 2024_bib.md 
I82827["publication: XB-SIM: A simulation framework"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I31482["Fei, X."], I39247["Zhang, Y."], I80994["Zheng, W."]],
    R8434__has_title="XB-SIM: A simulation framework for modeling and exploration of ReRAM-based CNN acceleration design",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I12179["Zahedi, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zahedi, M.",
    
)


# 2024_bib.md 
I2757["publication: MNEMOSENE: Tile architecture a"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I12179["Zahedi, M."], I60665["et al."]],
    R8434__has_title="MNEMOSENE: Tile architecture and simulator for memristor-based computation-in-memory",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I48354["Dong, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Dong, X.",
    
)


# 2024_bib.md 
I19072["Xu, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xu, C.",
    
)


# 2024_bib.md 
I65244["publication: NVSim: A circuit-level perform"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I48354["Dong, X."], I19072["Xu, C."], I99505["Xie, Y."], I99459["Jouppi, N. P."]],
    R8434__has_title="NVSim: A circuit-level performance, energy, and area model for emerging nonvolatile memory",
    R8435__has_year=2012,
    
)


# 2024_bib.md 
I25815["Song, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Song, L.",
    
)


# 2024_bib.md 
I54870["Qian, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Qian, X.",
    
)


# 2024_bib.md 
I95320["publication: PipeLayer: A Pipelined ReRAM-b"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I25815["Song, L."], I54870["Qian, X."], I11520["Li, H."], I75737["Chen, Y."]],
    R8434__has_title="PipeLayer: A Pipelined ReRAM-based accelerator for deep learning",
    
)


# 2024_bib.md 
I9600["Imani, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Imani, M.",
    
)


# 2024_bib.md 
I78217["publication: RAPIDNN: In-Memory Deep Neural"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I9600["Imani, M."], I60665["et al."]],
    R8434__has_title="RAPIDNN: In-Memory Deep Neural Network Acceleration Framework",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I25979["Chen, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chen, A.",
    
)


# 2024_bib.md 
I21111["publication: A comprehensive crossbar array"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I25979["Chen, A."],
    R8434__has_title="A comprehensive crossbar array model with solutions for line resistance and nonlinear device characteristics",
    R8435__has_year=2013,
    
)


# 2024_bib.md 
I2344["Aguirre, F. L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Aguirre, F. L.",
    
)


# 2024_bib.md 
I36246["publication: Line resistance impact in memr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I2344["Aguirre, F. L."], I60665["et al."]],
    R8434__has_title="Line resistance impact in memristor-based multi layer perceptron for pattern recognition",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I67547["publication: Minimization of the line resis"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I2344["Aguirre, F. L."], I10778["et al"]],
    R8434__has_title="Minimization of the line resistance impact on memdiode-based simulations of multilayer perceptron arrays applied to pattern recognition",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I19609["Lee, Y. K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lee, Y. K.",
    
)


# 2024_bib.md 
I99881["publication: Matrix mapping on crossbar mem"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I19609["Lee, Y. K."], I60665["et al."]],
    R8434__has_title="Matrix mapping on crossbar memory arrays with resistive interconnects and its use in in-memory compression of biosignals",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I67187["Fei, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fei, W.",
    
)


# 2024_bib.md 
I55919["Yeo, K. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yeo, K. S.",
    
)


# 2024_bib.md 
I66683["publication: Design exploration of hybrid C"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I67187["Fei, W."], I84035["Yu, H."], I3393["Zhang, W."], I55919["Yeo, K. S."]],
    R8434__has_title="Design exploration of hybrid CMOS and memristor circuit by new modified nodal analysis",
    R8435__has_year=2012,
    
)


# 2024_bib.md 
I76006["Pazos, S. M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Pazos, S. M.",
    
)


# 2024_bib.md 
I85036["Palumbo, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Palumbo, F.",
    
)


# 2024_bib.md 
I34338["Suñé, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Suñé, J.",
    
)


# 2024_bib.md 
I87407["Miranda, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Miranda, E.",
    
)


# 2024_bib.md 
I77671["publication: Application of the quasi-stati"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I2344["Aguirre, F. L."], I76006["Pazos, S. M."], I85036["Palumbo, F."], I34338["Suñé, J."], I87407["Miranda, E."]],
    R8434__has_title="Application of the quasi-static memdiode model in cross-point arrays for large dataset pattern recognition",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I15029["publication: SPICE simulation of RRAM-based"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I2344["Aguirre, F. L."], I76006["Pazos, S. M."], I85036["Palumbo, F."], I34338["Suñé, J."], I87407["Miranda, E."]],
    R8434__has_title="SPICE simulation of RRAM-based crosspoint arrays using the dynamic memdiode model",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I82314["publication: Assessment and improvement of "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I2344["Aguirre, F. L."], I60665["et al."]],
    R8434__has_title="Assessment and improvement of the pattern recognition performance of memdiode-based cross-point arrays with randomly distributed stuck-at-faults",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I89234["Fritscher, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fritscher, M.",
    
)


# 2024_bib.md 
I2124["Knodtel, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Knodtel, J.",
    
)


# 2024_bib.md 
I45121["Reichenbach, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Reichenbach, M.",
    
)


# 2024_bib.md 
I56268["Fey, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Fey, D.",
    
)


# 2024_bib.md 
I6786["publication: Simulating memristive systems "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I89234["Fritscher, M."], I2124["Knodtel, J."], I45121["Reichenbach, M."], I56268["Fey, D."]],
    R8434__has_title="Simulating memristive systems in mixed-signal mode using commercial design tools",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I72270["Applied Materials"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Applied Materials",
    
)


# 2024_bib.md 
I86571["publication: GinestraTM"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I72270["Applied Materials"],
    R8434__has_title="GinestraTM",
    
)


# 2024_bib.md 
I90436["publication: TCAD Technology Computer Aided"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="TCAD Technology Computer Aided Design (TCAD) | Synopsys",
    
)


# 2024_bib.md 
I4223["publication: Automating analogue AI chip de"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I18596["Krestinskaya, O."], I53810["Salama, K. N."], I15074["James, A. P."]],
    R8434__has_title="Automating analogue AI chip design with genetic search",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I36839["Salama, K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Salama, K.",
    
)


# 2024_bib.md 
I5809["publication: Towards hardware optimal neura"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I18596["Krestinskaya, O."], I36839["Salama, K."], I15074["James, A. P."]],
    R8434__has_title="Towards hardware optimal neural network selection with multi-objective genetic search",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I90927["Guan, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Guan, Z.",
    
)


# 2024_bib.md 
I98188["publication: A hardware-aware neural archit"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I90927["Guan, Z."], I60665["et al."]],
    R8434__has_title="A hardware-aware neural architecture search pareto front exploration for in-memory computing",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I5750["Li, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Li, G.",
    
)


# 2024_bib.md 
I6757["Mandal, S. K."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Mandal, S. K.",
    
)


# 2024_bib.md 
I73193["Ogras, U. Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ogras, U. Y.",
    
)


# 2024_bib.md 
I70920["Marculescu, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Marculescu, R.",
    
)


# 2024_bib.md 
I55764["publication: FLASH: Fast neural architectur"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I5750["Li, G."], I6757["Mandal, S. K."], I73193["Ogras, U. Y."], I70920["Marculescu, R."]],
    R8434__has_title="FLASH: Fast neural architecture search with hardware optimization",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I60336["Yuan, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yuan, Z.",
    
)


# 2024_bib.md 
I67013["publication: NAS4RRAM: neural network archi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I60336["Yuan, Z."], I60665["et al."]],
    R8434__has_title="NAS4RRAM: neural network architecture search for inference on RRAM-based accelerators",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I11166["Yan, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yan, Z.",
    
)


# 2024_bib.md 
I7393["Juan, D.-C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Juan, D.-C.",
    
)


# 2024_bib.md 
I1623["Hu, X. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hu, X. S.",
    
)


# 2024_bib.md 
I86037["Shi, Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Shi, Y.",
    
)


# 2024_bib.md 
I98213["publication: Uncertainty modeling of emergi"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I11166["Yan, Z."], I7393["Juan, D.-C."], I1623["Hu, X. S."], I86037["Shi, Y."]],
    R8434__has_title="Uncertainty modeling of emerging device based computing-in-memory neural accelerators with application to neural architecture search",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I9301["Sun H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Sun H.",
    
)


# 2024_bib.md 
I68330["publication: Gibbon: Efficient co-explorati"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I9301["Sun H."], I60665["et al."]],
    R8434__has_title="Gibbon: Efficient co-exploration of NN model and processing-in-memory architecture",
    R8435__has_year=2022,
    
)


# 2024_bib.md 
I12749["Jiang, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jiang, W.",
    
)


# 2024_bib.md 
I38831["publication: Device-circuit-architecture co"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I12749["Jiang, W."], I60665["et al."]],
    R8434__has_title="Device-circuit-architecture co-exploration for computing-in-memory neural accelerators",
    R8435__has_year=2021,
    
)


# 2024_bib.md 
I45494["Burr, G. W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Burr, G. W.",
    
)


# 2024_bib.md 
I47996["publication: Experimental demonstration and"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I45494["Burr, G. W."], I60665["et al."]],
    R8434__has_title="Experimental demonstration and tolerancing of a large-scale neural network (165 000 Synapses) using phasechange memory as the synaptic weight element",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I52583["Dong, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Dong, Z.",
    
)


# 2024_bib.md 
I35079["publication: Convolutional neural networks "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I52583["Dong, Z."], I60665["et al."]],
    R8434__has_title="Convolutional neural networks based on RRAM devices for image recognition and online learning tasks",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I10148["Querlioz, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Querlioz, D.",
    
)


# 2024_bib.md 
I35068["Bichler, O."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Bichler, O.",
    
)


# 2024_bib.md 
I60959["Dollfus, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Dollfus, P.",
    
)


# 2024_bib.md 
I42597["Gamrat, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Gamrat, C.",
    
)


# 2024_bib.md 
I81302["publication: Immunity to device variations "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I10148["Querlioz, D."], I35068["Bichler, O."], I60959["Dollfus, P."], I42597["Gamrat, C."]],
    R8434__has_title="Immunity to device variations in a spiking neural network with memristive nanodevices",
    R8435__has_year=2013,
    
)


# 2024_bib.md 
I11032["Guan, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Guan, X.",
    
)


# 2024_bib.md 
I61436["publication: A SPICE compact model of metal"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I11032["Guan, X."], I97154["Yu, S."], I83048["Wong, H. S. P."]],
    R8434__has_title="A SPICE compact model of metal oxide resistive switching memory with variations",
    R8435__has_year=2012,
    
)


# 2024_bib.md 
I18300["Liang, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Liang, J.",
    
)


# 2024_bib.md 
I35023["Yeh, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yeh, S.",
    
)


# 2024_bib.md 
I95103["Simon Wong, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Simon Wong, S.",
    
)


# 2024_bib.md 
I67772["Philip Wong, H. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Philip Wong, H. S.",
    
)


# 2024_bib.md 
I66816["publication: Effect of wordline/bitline sca"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I18300["Liang, J."], I35023["Yeh, S."], I95103["Simon Wong, S."], I67772["Philip Wong, H. S."]],
    R8434__has_title="Effect of wordline/bitline scaling on the performance, energy consumption, and reliability of cross-point memory array",
    R8435__has_year=2013,
    
)


# 2024_bib.md 
I89938["Hirtzlin, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hirtzlin, T.",
    
)


# 2024_bib.md 
I71699["publication: Digital biologically plausible"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I89938["Hirtzlin, T."], I60665["et al."]],
    R8434__has_title="Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I4407["Xue, C. X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xue, C. X.",
    
)


# 2024_bib.md 
I94278["publication: A 1Mb Multibit ReRAM computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I4407["Xue, C. X."], I60665["et al."]],
    R8434__has_title="A 1Mb Multibit ReRAM computing-in-memory macro with 14.6ns Parallel MAC computing time for CNN based AI Edge processors",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I81075["Wu, T. F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Wu, T. F.",
    
)


# 2024_bib.md 
I17336["publication: A 43pJ/Cycle Non-Volatile Micr"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I81075["Wu, T. F."], I60665["et al."]],
    R8434__has_title="A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I3089["Liu, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Liu, Q.",
    
)


# 2024_bib.md 
I95679["publication: A Fully Integrated Analog ReRA"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I3089["Liu, Q."], I60665["et al."]],
    R8434__has_title="A Fully Integrated Analog ReRAM based 78.4TOPS/ W compute-in-memory chip with fully parallel MAC computing",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I22719["Bennett, C. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Bennett, C. H.",
    
)


# 2024_bib.md 
I36951["Feinberg, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Feinberg, B.",
    
)


# 2024_bib.md 
I31551["Agarwal, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Agarwal, S.",
    
)


# 2024_bib.md 
I70878["Marinella, M. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Marinella, M. J.",
    
)


# 2024_bib.md 
I9426["publication: Analog architectures for neura"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15365["Xiao, T. P."], I22719["Bennett, C. H."], I36951["Feinberg, B."], I31551["Agarwal, S."], I70878["Marinella, M. J."]],
    R8434__has_title="Analog architectures for neural network acceleration based on non-volatile memory",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I94216["publication: NVIDIA Data Center Deep Learni"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8434__has_title="NVIDIA Data Center Deep Learning Product Performance",
    
)


# 2024_bib.md 
I43418["Habana L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Habana L.",
    
)


# 2024_bib.md 
I78330["publication: GoyaTM Inference Platform Whit"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I43418["Habana L."],
    R8434__has_title="GoyaTM Inference Platform White Paper",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I84818["Chen Y."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Chen Y.",
    
)


# 2024_bib.md 
I31142["publication: DaDianNao: A Machine-Learning "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I84818["Chen Y."],
    R8434__has_title="DaDianNao: A Machine-Learning Supercomputer",
    R8435__has_year=2015,
    
)


# 2024_bib.md 
I74019["publication: UNPU: An energy-efficient deep"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I75844["Lee, J."], I60665["et al."]],
    R8434__has_title="UNPU: An energy-efficient deep neural network accelerator with fully variable weight bit precision",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I83705["Bankman, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Bankman, D.",
    
)


# 2024_bib.md 
I19231["Yang, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yang, L.",
    
)


# 2024_bib.md 
I72904["Moons, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Moons, B.",
    
)


# 2024_bib.md 
I26214["Verhelst, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Verhelst, M.",
    
)


# 2024_bib.md 
I56137["publication: An always-on 3.8μJ/86% CIFAR-1"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I83705["Bankman, D."], I19231["Yang, L."], I72904["Moons, B."], I26214["Verhelst, M."], I18985["Murmann, B."]],
    R8434__has_title="An always-on 3.8μJ/86% CIFAR-10 mixed-signal binary CNN processor with all memory on chip in 28nm CMOS",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I15966["Nag, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Nag, A.",
    
)


# 2024_bib.md 
I42377["publication: Newton: Gravitating towards th"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15966["Nag, A."], I60665["et al."]],
    R8434__has_title="Newton: Gravitating towards the physical limits of crossbar acceleration",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I88305["Bojnordi M. N."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Bojnordi M. N.",
    
)


# 2024_bib.md 
I41974["Ipek, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ipek, E.",
    
)


# 2024_bib.md 
I75108["publication: Memristive Boltzmann machine: "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I88305["Bojnordi M. N."], I41974["Ipek, E."]],
    R8434__has_title="Memristive Boltzmann machine: A hardware accelerator for combinatorial optimization and deep learning",
    R8435__has_year=2016,
    
)


# 2024_bib.md 
I18859["publication: A heterogeneous and programmab"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15284["Jain, S."], I60665["et al."]],
    R8434__has_title="A heterogeneous and programmable compute-in-memory accelerator architecture for analog-AI using dense 2-D Mesh",
    R8435__has_year=2023,
    
)


# 2024_bib.md 
I80129["Carnevale N. T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Carnevale N. T.",
    
)


# 2024_bib.md 
I55623["Hines, M. L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Hines, M. L.",
    
)


# 2024_bib.md 
I27380["publication: The NEURON book"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I80129["Carnevale N. T."], I55623["Hines, M. L."]],
    R8434__has_title="The NEURON book",
    R8435__has_year=2006,
    
)


# 2024_bib.md 
I6779["Lammie, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Lammie, C.",
    
)


# 2024_bib.md 
I89114["Xiang, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Xiang, W.",
    
)


# 2024_bib.md 
I85415["Azghadi, M. R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Azghadi, M. R.",
    
)


# 2024_bib.md 
I71318["publication: MemTorch: An Open-source Simul"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I6779["Lammie, C."], I89114["Xiang, W."], I84649["Linares-Barranco, B."], I85415["Azghadi, M. R."]],
    R8434__has_title="MemTorch: An Open-source Simulation Framework for Memristive Deep Learning Systems",
    R8435__has_year=2020,
    
)


# 2024_bib.md 
I40045["publication: CrossSim: accuracy simulation "].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I15365["Xiao, T. P."], I22719["Bennett, C. H."], I36951["Feinberg, B."], I70878["Marinella, M. J."], I31551["Agarwal, S."]],
    R8434__has_title="CrossSim: accuracy simulation of analog in-memory computing",
    
)


# 2024_bib.md 
I78072["Joksas, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Joksas, D.",
    
)


# 2024_bib.md 
I17406["Ng, W. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Ng, W. H.",
    
)


# 2024_bib.md 
I70034["Buckwell, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Buckwell, M.",
    
)


# 2024_bib.md 
I82691["publication: Simulation of inference accura"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I17571["Mehonic, A."], I78072["Joksas, D."], I17406["Ng, W. H."], I70034["Buckwell, M."], I63422["Kenyon, A. J."]],
    R8434__has_title="Simulation of inference accuracy using realistic rram devices",
    R8435__has_year=2019,
    
)


# 2024_bib.md 
I67208["Zhang, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Zhang, Q.",
    
)


# 2024_bib.md 
I29245["publication: Sign backpropagation: An on-ch"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I67208["Zhang, Q."], I60665["et al."]],
    R8434__has_title="Sign backpropagation: An on-chip learning algorithm for analog RRAM neuromorphic computing systems",
    R8435__has_year=2018,
    
)


# 2024_bib.md 
I84274["Yamaoka, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Yamaoka, M.",
    
)


# 2024_bib.md 
I97898["publication: Low-power SRAM"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=I84274["Yamaoka, M."],
    R8434__has_title="Low-power SRAM",
    R8435__has_year=2013,
    
)


# 2024_bib.md 
I55841["Jan, Y. W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    R7781__has_family_name="Jan, Y. W.",
    
)


# 2024_bib.md 
I63187["publication: Voltage based winner takes all"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    R8433__has_authors=[I62543["Starzyk, J. A."], I55841["Jan, Y. W."]],
    R8434__has_title="Voltage based winner takes all circuit for analog neural networks",
    R8435__has_year=1996,
    
)




p.end_mod()