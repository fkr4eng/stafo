import pyirk as p
import sympy as sp

from ipydex import IPS, activate_ips_on_exception  # noqa




ag = p.irkloader.load_mod_from_path(r"C:\Users\Julius Fiedler\Documents\Code\irk\irk-data\ocse\agents1.py", prefix="ag")


__URI__ = "irk:/ocse/0.2/auto_import_formalized_statements"

keymanager = p.KeyManager()
p.register_mod(__URI__, keymanager)
p.start_mod(__URI__)

# these entities are declared here all at once in order to avoid referencing issues when setting relations.
# the relations of these entities are set below with the update method. This update method is called exactly once.
I39529 = p.create_item(R1__has_label="memristor stack")
I74938 = p.create_item(R1__has_label="stack component")
R62251 = p.create_relation(R1__has_label="has stack component")
R68123 = p.create_relation(R1__has_label="has memristor stack")
I85012 = p.create_item(R1__has_label="publication: Memristive crossbar arrays for brain-inspired computing")
I99712 = p.create_item(R1__has_label="Wang, Z.")
I94362 = p.create_item(R1__has_label="publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing")
I85528 = p.create_item(R1__has_label="Li, C.")
I2855 = p.create_item(R1__has_label="publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors")
I46793 = p.create_item(R1__has_label="Midya, R.")
I90963 = p.create_item(R1__has_label="publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity")
I54975 = p.create_item(R1__has_label="Srinivasan, V. S. S.")
I72751 = p.create_item(R1__has_label="publication: Punchthrough-diode-based bipolar RRAM selector by Si epitaxy")
I80078 = p.create_item(R1__has_label="Huang, J.-J.")
I5210 = p.create_item(R1__has_label="Tseng, Y.-M.")
I32782 = p.create_item(R1__has_label="Hsu, C.-W.")
I91760 = p.create_item(R1__has_label="Hou, T.-H.")
I91215 = p.create_item(R1__has_label="publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications")
I81970 = p.create_item(R1__has_label="Shin, J.")
I68229 = p.create_item(R1__has_label="publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application")
I64747 = p.create_item(R1__has_label="Govoreanu, B.")
I39757 = p.create_item(R1__has_label="publication: High-performance metal–insulator–metal tunnel diode selectors")
I30227 = p.create_item(R1__has_label="Woo, J.")
I24132 = p.create_item(R1__has_label="publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)")
I14404 = p.create_item(R1__has_label="Lee, W.")
I65317 = p.create_item(R1__has_label="publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays")
I25665 = p.create_item(R1__has_label="Choi, B. J.")
I85099 = p.create_item(R1__has_label="publication: Trilayer tunnel selectors for memristor memory cells")
I97353 = p.create_item(R1__has_label="Kawahara, A.")
I47693 = p.create_item(R1__has_label="publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput")
I17571 = p.create_item(R1__has_label="IBM")
I63422 = p.create_item(R1__has_label="publication: MIEC Access Device for 3D-Crosspoint Nonvolatile Memory Arrays")
I91057 = p.create_item(R1__has_label="publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance")
I86040 = p.create_item(R1__has_label="Yasuda, S.")
I60665 = p.create_item(R1__has_label="publication: A cross point Cu-ReRAM with a novel OTS selector for storage class memory applications")
I36571 = p.create_item(R1__has_label="Yang, H.")
I76227 = p.create_item(R1__has_label="publication: Novel selector for high density non-volatile memory with ultra-low holding voltage and 107 on/of ratio")
I68467 = p.create_item(R1__has_label="Kim, S. G.")
I11040 = p.create_item(R1__has_label="publication: Breakthrough of selector technology for cross-point 25-nm ReRAM")
I40507 = p.create_item(R1__has_label="Son, M.")
I46602 = p.create_item(R1__has_label="publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications")
I75913 = p.create_item(R1__has_label="Kim, W. G.")
I32043 = p.create_item(R1__has_label="publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application")
I45775 = p.create_item(R1__has_label="Cha, E.")
I88802 = p.create_item(R1__has_label="publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode")
I89671 = p.create_item(R1__has_label="Lee, M.-J.")
I5377 = p.create_item(R1__has_label="publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays")
I79564 = p.create_item(R1__has_label="Sun, J.")
I67803 = p.create_item(R1__has_label="publication: Physically transient threshold switching device based on magnesium oxide for security application")
I37074 = p.create_item(R1__has_label="Jo, S. H.")
I34513 = p.create_item(R1__has_label="Kumar, T.")
I4484 = p.create_item(R1__has_label="Narayanan, S.")
I93059 = p.create_item(R1__has_label="Lu, W. D.")
I89877 = p.create_item(R1__has_label="Nazarian, H.")
I48946 = p.create_item(R1__has_label="publication: 3D-stackable crossbar resistive memory based on feld assisted superlinear threshold (FAST) selector")
I44836 = p.create_item(R1__has_label="Ji, L.")
I63006 = p.create_item(R1__has_label="publication: Integrated one diode-one resistor architecture in nanopillar SiO*x* resistive switching memory by nanosphere lithography")
I99459 = p.create_item(R1__has_label="Wang, G.")
I48965 = p.create_item(R1__has_label="publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array")
I85347 = p.create_item(R1__has_label="publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell")
I45993 = p.create_item(R1__has_label="Song, M.")
I24141 = p.create_item(R1__has_label="publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications")
I35428 = p.create_item(R1__has_label="Lu, D.")
I10778 = p.create_item(R1__has_label="publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices")
I69974 = p.create_item(R1__has_label="Wang, M. J.")
I70494 = p.create_item(R1__has_label="Gao, S.")
I87242 = p.create_item(R1__has_label="Zeng, F.")
I93860 = p.create_item(R1__has_label="Song, C.")
I78857 = p.create_item(R1__has_label="Pan, F.")
I94601 = p.create_item(R1__has_label="publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices")
I52917 = p.create_item(R1__has_label="Kim, K.-H.")
I86787 = p.create_item(R1__has_label="Gaba, S.")
I21123 = p.create_item(R1__has_label="Lu, W.")
I39708 = p.create_item(R1__has_label="publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance")
I93276 = p.create_item(R1__has_label="Ni/TiO2/Ni")
I53205 = p.create_item(R1__has_label="Ni")
I87136 = p.create_item(R1__has_label="TiO2")
I85417 = p.create_item(R1__has_label="Pt/TiO2/TiN")
I97657 = p.create_item(R1__has_label="Pt")
I21621 = p.create_item(R1__has_label="TiN")
I87604 = p.create_item(R1__has_label="TiN/Ta2O5/TiN")
I7533 = p.create_item(R1__has_label="Ta2O5")
I49189 = p.create_item(R1__has_label="W/Ta2O5/TaOx/ TiO2/TiN")
I8849 = p.create_item(R1__has_label="W")
I95219 = p.create_item(R1__has_label="TaOx")
I45292 = p.create_item(R1__has_label=" TiO2")
I66609 = p.create_item(R1__has_label="Pt/TaOx/TiO2/TaOx/Pt")
I12092 = p.create_item(R1__has_label="Pt/TaN1+x/Ta2O5/TaN1+<br>x/Pt")
I50118 = p.create_item(R1__has_label="TaN1+x")
I38213 = p.create_item(R1__has_label="TaN1+<br>x")
I34131 = p.create_item(R1__has_label="TaN/SiNx/TaN")
I47402 = p.create_item(R1__has_label="TaN")
I8777 = p.create_item(R1__has_label="SiNx")
I89808 = p.create_item(R1__has_label="TE(Cu doped) /Cu8GeSe6/<br>BE(Cu doped)")
I73802 = p.create_item(R1__has_label="TE(Cu doped) ")
I63079 = p.create_item(R1__has_label="Cu8GeSe6")
I92934 = p.create_item(R1__has_label="<br>BE(Cu doped)")
I97154 = p.create_item(R1__has_label="TiN/GexSe1–x/TiN")
I72298 = p.create_item(R1__has_label="GexSe1–x")
I83048 = p.create_item(R1__has_label="TiN/As:SiO2/TiN")
I16765 = p.create_item(R1__has_label="As:SiO2")
I87992 = p.create_item(R1__has_label="Pt/VO2/Pt")
I58468 = p.create_item(R1__has_label="VO2")
I82062 = p.create_item(R1__has_label="TiN/NbO2/TiN")
I27966 = p.create_item(R1__has_label="NbO2")
I46285 = p.create_item(R1__has_label="TiN/NbO2/W")
I9309 = p.create_item(R1__has_label="TiN/AsTeGeSiN/TiN")
I18158 = p.create_item(R1__has_label="AsTeGeSiN")
I55774 = p.create_item(R1__has_label="W/Ag/MgO/Ag/W")
I95705 = p.create_item(R1__has_label="Ag")
I78145 = p.create_item(R1__has_label="MgO")
I11520 = p.create_item(R1__has_label="Pt/Ag:SiOxNy/Pt")
I59694 = p.create_item(R1__has_label="Ag:SiOxNy")
I56829 = p.create_item(R1__has_label="Pd/Ag/HfO2/Ag/Pd")
I10094 = p.create_item(R1__has_label="Pd")
I42033 = p.create_item(R1__has_label="HfO2")
I69530 = p.create_item(R1__has_label="P2+/N+/N2+ epitaxial Si")
I68259 = p.create_item(R1__has_label="P2+")
I29098 = p.create_item(R1__has_label="N+")
I82346 = p.create_item(R1__has_label="N2+ epitaxial Si")
I90071 = p.create_item(R1__has_label="TiN/Al2O3/TiO2/TiN")
I12398 = p.create_item(R1__has_label="Al2O3")
I98878 = p.create_item(R1__has_label="W/VOx/Pt")
I23249 = p.create_item(R1__has_label="VOx")
I76087 = p.create_item(R1__has_label="p-Si/SiO2/n-Si")
I48237 = p.create_item(R1__has_label="p-Si")
I61398 = p.create_item(R1__has_label="SiO2")
I99103 = p.create_item(R1__has_label="n-Si")
I28976 = p.create_item(R1__has_label="Ni/HfO2/n-Si")
I11681 = p.create_item(R1__has_label="Cu/HfO2/n-Si")
I41069 = p.create_item(R1__has_label="Cu")
I37167 = p.create_item(R1__has_label="Ag/a-Si/p-poly-Si")
I86221 = p.create_item(R1__has_label="a-Si")
I47202 = p.create_item(R1__has_label="p-poly-Si")
I29376 = p.create_item(R1__has_label="publication: Hardware implementation of memristorbased artificial neural networks")
I69517 = p.create_item(R1__has_label="Yao, P.")
I1362 = p.create_item(R1__has_label="publication: Fully hardware-implemented memristor convolutional neural network")
I57709 = p.create_item(R1__has_label="Cai, F.")
I73000 = p.create_item(R1__has_label="publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations")
I49887 = p.create_item(R1__has_label="Wan, W.")
I67827 = p.create_item(R1__has_label="publication: A compute-in-memory chip based on resistive random-access memory")
I22963 = p.create_item(R1__has_label="Yin, S.")
I17132 = p.create_item(R1__has_label="Sun, X.")
I74155 = p.create_item(R1__has_label="Yu, S.")
I18985 = p.create_item(R1__has_label="Seo, J. S.")
I87613 = p.create_item(R1__has_label="publication: High-throughput in-memory computing for binary deep neural networks with monolithically integrated RRAM and 90-nm CMOS")
I95725 = p.create_item(R1__has_label="Khaddam-Aljameh, R.")
I64045 = p.create_item(R1__has_label="publication: HERMES-Core-A 1.59-TOPS/mm2PCM on 14-nm CMOS in-memory compute core using 300-ps/LSB linearized CCO-based ADCs")
I79243 = p.create_item(R1__has_label="Narayanan, P.")
I52752 = p.create_item(R1__has_label="publication: Fully on-chip MAC at 14 nm enabled by accurate row-wise programming of PCM-based weights and parallel vector-transport in duration-format")
I49299 = p.create_item(R1__has_label="Le Gallo, M.")
I51187 = p.create_item(R1__has_label="publication: A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference")
I59886 = p.create_item(R1__has_label="Mochida, R.")
I75602 = p.create_item(R1__has_label="publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture")
I26646 = p.create_item(R1__has_label="Su, F.")
I22852 = p.create_item(R1__has_label="publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory")
I77881 = p.create_item(R1__has_label="Kiani, F.")
I49586 = p.create_item(R1__has_label="Yin, J.")
I55924 = p.create_item(R1__has_label="Joshua Yang, J.")
I97111 = p.create_item(R1__has_label="Xia, Q.")
I13415 = p.create_item(R1__has_label="publication: A fully hardware-based memristive multilayer neural network")
I84363 = p.create_item(R1__has_label="publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration")
I51358 = p.create_item(R1__has_label="Pedretti, G.")
I61262 = p.create_item(R1__has_label="publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques")
I69614 = p.create_item(R1__has_label="publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark")
I91097 = p.create_item(R1__has_label="publication: Fully memristive neural networks for pattern classification with unsupervised learning")
I84267 = p.create_item(R1__has_label="Ambrogio, S.")
I32602 = p.create_item(R1__has_label="publication: Equivalent-accuracy accelerated neural network training using analogue memory")
I91573 = p.create_item(R1__has_label="Bocquet, M.")
I60259 = p.create_item(R1__has_label="publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks")
I73590 = p.create_item(R1__has_label="Chen, W. H.")
I74604 = p.create_item(R1__has_label="publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors")
I66704 = p.create_item(R1__has_label="Hirtzlin, T.")
I59620 = p.create_item(R1__has_label="publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays")
I38907 = p.create_item(R1__has_label="Xue, C. X.")
I72736 = p.create_item(R1__has_label="publication: A 1Mb Multibit ReRAM computing-in-memory macro with 14.6ns Parallel MAC computing time for CNN based AI Edge processors")
I31938 = p.create_item(R1__has_label="Wu, T. F.")
I15972 = p.create_item(R1__has_label="publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques")
I70751 = p.create_item(R1__has_label="Liu, Q.")
I86194 = p.create_item(R1__has_label="publication: A Fully Integrated Analog ReRAM based 78.4TOPS/ W compute-in-memory chip with fully parallel MAC computing")
I72160 = p.create_item(R1__has_label="Au/Pd/WOX/Au")
I43694 = p.create_item(R1__has_label="Au")
I10506 = p.create_item(R1__has_label="WOX")
I8593 = p.create_item(R1__has_label="TiN/TaOx/HfO/TiNx")
I65099 = p.create_item(R1__has_label="HfO")
I16673 = p.create_item(R1__has_label="TiNx")
I33540 = p.create_item(R1__has_label="Pt/Ta/Ta2O5/Pt/Ti")
I36840 = p.create_item(R1__has_label="Ta")
I4130 = p.create_item(R1__has_label="Ti")
I52096 = p.create_item(R1__has_label="Ta/TaOx/Pt")
I59167 = p.create_item(R1__has_label="W/TiN/TiON")
I21466 = p.create_item(R1__has_label="TiON")
I96420 = p.create_item(R1__has_label="Pt/SiOxAg/Pt/Ti")
I2133 = p.create_item(R1__has_label="SiOxAg")
I83149 = p.create_item(R1__has_label=" Ta/Pd/HfO2/Pt/Ti")
I43547 = p.create_item(R1__has_label=" Ta")
I60267 = p.create_item(R1__has_label="TiN/HfO2/Ti/TiN")
I25994 = p.create_item(R1__has_label="W/Ta2O5/TaOx/W")
I12147 = p.create_item(R1__has_label="AlCu/TiN/Ti/HfO2/TiN")
I84254 = p.create_item(R1__has_label="AlCu")
I15050 = p.create_item(R1__has_label="-/HfO2/TaOX/-")
I10578 = p.create_item(R1__has_label="-")
I45648 = p.create_item(R1__has_label="TaOX")
I71268 = p.create_item(R1__has_label="TiN/HfO2/TaOX/TiN")


########################################################################################################################
# content:
########################################################################################################################






I39529["memristor stack"].update_relations(
    R4__is_instance_of=p.I2["Metaclass"],

)



I74938["stack component"].update_relations(
    R4__is_instance_of=p.I2["Metaclass"],

)



R62251["has stack component"].update_relations(
    R8__has_domain_of_argument_1=I39529["memristor stack"],
    R11__has_range_of_result=I74938["stack component"],

)



R68123["has memristor stack"].update_relations(
    R8__has_domain_of_argument_1=ag.I6591["source document"],
    R11__has_range_of_result=I39529["memristor stack"],

)


# 2019
I85012["publication: Memristive crossbar arrays for brain-inspired computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=["Qiangfei Xia", "J. Joshua Yang"],
    ag__R8434__has_title="Memristive crossbar arrays for brain-inspired computing",
    ag__R8435__has_year=2019,
    ag__R8440__cites=[I94362["publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing"], I2855["publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors"], I90963["publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity"], I72751["publication: Punchthrough-diode-based bipolar RRAM selector by Si epitaxy"], I91215["publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications"], I68229["publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application"], I39757["publication: High-performance metal–insulator–metal tunnel diode selectors"], I24132["publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)"], I65317["publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays"], I85099["publication: Trilayer tunnel selectors for memristor memory cells"], I47693["publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput"], I63422["publication: MIEC Access Device for 3D-Crosspoint Nonvolatile Memory Arrays"], I91057["publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance"], I60665["publication: A cross point Cu-ReRAM with a novel OTS selector for storage class memory applications"], I76227["publication: Novel selector for high density non-volatile memory with ultra-low holding voltage and 107 on/of ratio"], I11040["publication: Breakthrough of selector technology for cross-point 25-nm ReRAM"], I46602["publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications"], I32043["publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application"], I88802["publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode"], I5377["publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays"], I67803["publication: Physically transient threshold switching device based on magnesium oxide for security application"], I48946["publication: 3D-stackable crossbar resistive memory based on feld assisted superlinear threshold (FAST) selector"], I63006["publication: Integrated one diode-one resistor architecture in nanopillar SiO*x* resistive switching memory by nanosphere lithography"], I48965["publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array"], I85347["publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell"], I24141["publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications"], I10778["publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices"], I94601["publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices"], I39708["publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance"]],

)


# 2019
I99712["Wang, Z."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, Z.",

)


# 2019
I94362["publication: Memristors with difusive dynamics as synaptic emulators for neuromorphic computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I99712["Wang, Z."],
    ag__R8434__has_title="Memristors with difusive dynamics as synaptic emulators for neuromorphic computing",
    ag__R8435__has_year=2017,
    R68123__has_memristor_stack=I11520["Pt/Ag:SiOxNy/Pt"],

)


# 2019
I85528["Li, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Li, C.",

)


# 2019
I2855["publication: Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I85528["Li, C."],
    ag__R8434__has_title="Tree-dimensional crossbar arrays of self-rectifying Si/SiO2/Si memristors",
    ag__R8435__has_year=2017,
    R68123__has_memristor_stack=I76087["p-Si/SiO2/n-Si"],

)


# 2019
I46793["Midya, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Midya, R.",

)


# 2019
I90963["publication: Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I46793["Midya, R."],
    ag__R8434__has_title="Anatomy of Ag/Hafnia-based selectors with 1010 nonlinearity",
    ag__R8435__has_year=2017,
    R68123__has_memristor_stack=I56829["Pd/Ag/HfO2/Ag/Pd"],

)


# 2019
I54975["Srinivasan, V. S. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Srinivasan, V. S. S.",

)


# 2019
I72751["publication: Punchthrough-diode-based bipolar RRAM selector by Si epitaxy"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I54975["Srinivasan, V. S. S."],
    ag__R8434__has_title="Punchthrough-diode-based bipolar RRAM selector by Si epitaxy",
    ag__R8435__has_year=2012,

)


# 2019
I80078["Huang, J.-J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Huang, J.-J.",

)


# 2019
I5210["Tseng, Y.-M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Tseng, Y.-M.",

)


# 2019
I32782["Hsu, C.-W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hsu, C.-W.",

)


# 2019
I91760["Hou, T.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hou, T.-H.",

)


# 2019
I91215["publication: Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I80078["Huang, J.-J."], I5210["Tseng, Y.-M."], I32782["Hsu, C.-W."], I91760["Hou, T.-H."]],
    ag__R8434__has_title="Bipolar nonlinear Ni/ TiO2/Ni selector for 1S1R crossbar array applications",
    ag__R8435__has_year=2011,
    R68123__has_memristor_stack=I93276["Ni/TiO2/Ni"],

)


# 2019
I81970["Shin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Shin, J.",

)


# 2019
I68229["publication: TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I81970["Shin, J."],
    ag__R8434__has_title="TiO2-based metal–insulator–metal selection device for bipolar resistive random access memory cross-point application",
    ag__R8435__has_year=2011,
    R68123__has_memristor_stack=I85417["Pt/TiO2/TiN"],

)


# 2019
I64747["Govoreanu, B."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Govoreanu, B.",

)


# 2019
I39757["publication: High-performance metal–insulator–metal tunnel diode selectors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I64747["Govoreanu, B."],
    ag__R8434__has_title="High-performance metal–insulator–metal tunnel diode selectors",
    ag__R8435__has_year=2014,
    R68123__has_memristor_stack=I87604["TiN/Ta2O5/TiN"],

)


# 2019
I30227["Woo, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Woo, J.",

)


# 2019
I24132["publication: Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I30227["Woo, J."],
    ag__R8434__has_title="Electrical and reliability characteristics of a scaled (∼30nm) tunnel barrier selector (W/Ta2O5/TaOx/TiO2/TiN) with excellent performance (JMAX>107A/cm2)",
    ag__R8435__has_year=2014,
    R68123__has_memristor_stack=I49189["W/Ta2O5/TaOx/ TiO2/TiN"],

)


# 2019
I14404["Lee, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lee, W.",

)


# 2019
I65317["publication: Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I14404["Lee, W."],
    ag__R8434__has_title="Varistor-type bidirectional switch (JMAX>107A/cm2 , selectivity ∼104 ) for 3D bipolar resistive memory arrays",
    ag__R8435__has_year=2012,
    R68123__has_memristor_stack=I66609["Pt/TaOx/TiO2/TaOx/Pt"],

)


# 2019
I25665["Choi, B. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Choi, B. J.",

)


# 2019
I85099["publication: Trilayer tunnel selectors for memristor memory cells"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I25665["Choi, B. J."],
    ag__R8434__has_title="Trilayer tunnel selectors for memristor memory cells",
    ag__R8435__has_year=2016,
    R68123__has_memristor_stack=I12092["Pt/TaN1+x/Ta2O5/TaN1+<br>x/Pt"],

)


# 2019
I97353["Kawahara, A."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kawahara, A.",

)


# 2019
I47693["publication: An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I97353["Kawahara, A."],
    ag__R8434__has_title="An 8 Mb multi-layered cross-point ReRAM macro with 443 MB/s write throughput",
    ag__R8435__has_year=2013,
    R68123__has_memristor_stack=I34131["TaN/SiNx/TaN"],

)


# 2019
I17571["IBM"].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="IBM",

)


# 2019
I63422["publication: MIEC Access Device for 3D-Crosspoint Nonvolatile Memory Arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I17571["IBM"],
    ag__R8434__has_title="MIEC Access Device for 3D-Crosspoint Nonvolatile Memory Arrays",
    ag__R8435__has_year=2013,
    R68123__has_memristor_stack=I89808["TE(Cu doped) /Cu8GeSe6/<br>BE(Cu doped)"],

)


# 2019
I91057["publication: Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I64747["Govoreanu, B."],
    ag__R8434__has_title="Termally stable integrated Se-based OTS selectors with >20MA/cm2 current drive, >3.103 half-bias nonlinearity, tunable threshold voltage and excellent endurance",
    ag__R8435__has_year=2017,
    R68123__has_memristor_stack=I97154["TiN/GexSe1–x/TiN"],

)


# 2019
I86040["Yasuda, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yasuda, S.",

)


# 2019
I60665["publication: A cross point Cu-ReRAM with a novel OTS selector for storage class memory applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I86040["Yasuda, S."],
    ag__R8434__has_title="A cross point Cu-ReRAM with a novel OTS selector for storage class memory applications",
    ag__R8435__has_year=2017,

)


# 2019
I36571["Yang, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yang, H.",

)


# 2019
I76227["publication: Novel selector for high density non-volatile memory with ultra-low holding voltage and 107 on/of ratio"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I36571["Yang, H."],
    ag__R8434__has_title="Novel selector for high density non-volatile memory with ultra-low holding voltage and 107 on/of ratio",
    ag__R8435__has_year=2015,

)


# 2019
I68467["Kim, S. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, S. G.",

)


# 2019
I11040["publication: Breakthrough of selector technology for cross-point 25-nm ReRAM"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I68467["Kim, S. G."],
    ag__R8434__has_title="Breakthrough of selector technology for cross-point 25-nm ReRAM",
    ag__R8435__has_year=2017,
    R68123__has_memristor_stack=I83048["TiN/As:SiO2/TiN"],

)


# 2019
I40507["Son, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Son, M.",

)


# 2019
I46602["publication: Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I40507["Son, M."],
    ag__R8434__has_title="Excellent selector characteristics of nanoscale VO2 for high-density bipolar ReRAM applications",
    ag__R8435__has_year=2011,
    R68123__has_memristor_stack=I87992["Pt/VO2/Pt"],

)


# 2019
I75913["Kim, W. G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, W. G.",

)


# 2019
I32043["publication: NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I75913["Kim, W. G."],
    ag__R8434__has_title="NbO2-based low power and cost efective 1S1R switching for high density cross point ReRAM application",
    ag__R8435__has_year=2014,
    R68123__has_memristor_stack=I82062["TiN/NbO2/TiN"],

)


# 2019
I45775["Cha, E."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Cha, E.",

)


# 2019
I88802["publication: Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I45775["Cha, E."],
    ag__R8434__has_title="Nanoscale (∼10nm) 3D vertical ReRAM and NbO2 threshold selector with TiN electrode",
    ag__R8435__has_year=2013,
    R68123__has_memristor_stack=I46285["TiN/NbO2/W"],

)


# 2019
I89671["Lee, M.-J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lee, M.-J.",

)


# 2019
I5377["publication: Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I89671["Lee, M.-J."],
    ag__R8434__has_title="Highly-scalable threshold switching select device based on chalcogenide glasses for 3D nanoscaled memory arrays",
    ag__R8435__has_year=2012,
    R68123__has_memristor_stack=I9309["TiN/AsTeGeSiN/TiN"],

)


# 2019
I79564["Sun, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Sun, J.",

)


# 2019
I67803["publication: Physically transient threshold switching device based on magnesium oxide for security application"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I79564["Sun, J."],
    ag__R8434__has_title="Physically transient threshold switching device based on magnesium oxide for security application",
    ag__R8435__has_year=2018,
    R68123__has_memristor_stack=I55774["W/Ag/MgO/Ag/W"],

)


# 2019
I37074["Jo, S. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Jo, S. H.",

)


# 2019
I34513["Kumar, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kumar, T.",

)


# 2019
I4484["Narayanan, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Narayanan, S.",

)


# 2019
I93059["Lu, W. D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, W. D.",

)


# 2019
I89877["Nazarian, H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Nazarian, H.",

)


# 2019
I48946["publication: 3D-stackable crossbar resistive memory based on feld assisted superlinear threshold (FAST) selector"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I37074["Jo, S. H."], I34513["Kumar, T."], I4484["Narayanan, S."], I93059["Lu, W. D."], I89877["Nazarian, H."]],
    ag__R8434__has_title="3D-stackable crossbar resistive memory based on feld assisted superlinear threshold (FAST) selector",
    ag__R8435__has_year=2014,

)


# 2019
I44836["Ji, L."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Ji, L.",

)


# 2019
I63006["publication: Integrated one diode-one resistor architecture in nanopillar SiO*x* resistive switching memory by nanosphere lithography"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I44836["Ji, L."],
    ag__R8434__has_title="Integrated one diode-one resistor architecture in nanopillar SiO*x* resistive switching memory by nanosphere lithography",
    ag__R8435__has_year=2014,
    R68123__has_memristor_stack=I69530["P2+/N+/N2+ epitaxial Si"],

)


# 2019
I99459["Wang, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, G.",

)


# 2019
I48965["publication: High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I99459["Wang, G."],
    ag__R8434__has_title="High‐performance and low‐power rewritable SiO*x* 1 kbit one diode–one resistor crossbar memory array",
    ag__R8435__has_year=2013,

)


# 2019
I85347["publication: Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I64747["Govoreanu, B."],
    ag__R8434__has_title="Vacancy-modulated conductive oxide resistive RAM (VMCO-RRAM): an area-scalable switching current, self-compliant, highly nonlinear and wide on/of-window resistive switching cell",
    ag__R8435__has_year=2013,
    R68123__has_memristor_stack=I90071["TiN/Al2O3/TiO2/TiN"],

)


# 2019
I45993["Song, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Song, M.",

)


# 2019
I24141["publication: Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I45993["Song, M."],
    ag__R8434__has_title="Self-selective characteristics of nanoscale VOx devices for high-density ReRAM applications",
    ag__R8435__has_year=2012,
    R68123__has_memristor_stack=I98878["W/VOx/Pt"],

)


# 2019
I35428["Lu, D."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, D.",

)


# 2019
I10778["publication: Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I35428["Lu, D."],
    ag__R8434__has_title="Investigations of conduction mechanisms of the self-rectifying n<sup>+</sup>Si-HfO2-Ni RRAM devices",
    ag__R8435__has_year=2014,
    R68123__has_memristor_stack=I28976["Ni/HfO2/n-Si"],

)


# 2019
I69974["Wang, M. J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wang, M. J.",

)


# 2019
I70494["Gao, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gao, S.",

)


# 2019
I87242["Zeng, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Zeng, F.",

)


# 2019
I93860["Song, C."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Song, C.",

)


# 2019
I78857["Pan, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Pan, F.",

)


# 2019
I94601["publication: Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I69974["Wang, M. J."], I70494["Gao, S."], I87242["Zeng, F."], I93860["Song, C."], I78857["Pan, F."]],
    ag__R8434__has_title="Unipolar resistive switching with forming-free and self-rectifying efects in Cu/HfO2/n-Si devices",
    ag__R8435__has_year=2016,
    R68123__has_memristor_stack=I11681["Cu/HfO2/n-Si"],

)


# 2019
I52917["Kim, K.-H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kim, K.-H.",

)


# 2019
I86787["Gaba, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Gaba, S.",

)


# 2019
I21123["Lu, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Lu, W.",

)


# 2019
I39708["publication: Nanoscale resistive memory with intrinsic diode characteristics and long endurance"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I52917["Kim, K.-H."], I37074["Jo, S. H."], I86787["Gaba, S."], I21123["Lu, W."]],
    ag__R8434__has_title="Nanoscale resistive memory with intrinsic diode characteristics and long endurance",
    ag__R8435__has_year=2010,
    R68123__has_memristor_stack=I37167["Ag/a-Si/p-poly-Si"],

)


# 2019
I93276["Ni/TiO2/Ni"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I53205["Ni"], I87136["TiO2"], I53205["Ni"]],

)


# 2019
I53205["Ni"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I87136["TiO2"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I85417["Pt/TiO2/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I97657["Pt"], I87136["TiO2"], I21621["TiN"]],

)


# 2019
I97657["Pt"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I21621["TiN"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I87604["TiN/Ta2O5/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I7533["Ta2O5"], I21621["TiN"]],

)


# 2019
I7533["Ta2O5"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I49189["W/Ta2O5/TaOx/ TiO2/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I8849["W"], I7533["Ta2O5"], I95219["TaOx"], I45292[" TiO2"], I21621["TiN"]],

)


# 2019
I8849["W"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I95219["TaOx"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I45292[" TiO2"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I66609["Pt/TaOx/TiO2/TaOx/Pt"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I97657["Pt"], I95219["TaOx"], I87136["TiO2"], I95219["TaOx"], I97657["Pt"]],

)


# 2019
I12092["Pt/TaN1+x/Ta2O5/TaN1+<br>x/Pt"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I97657["Pt"], I50118["TaN1+x"], I7533["Ta2O5"], I38213["TaN1+<br>x"], I97657["Pt"]],

)


# 2019
I50118["TaN1+x"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I38213["TaN1+<br>x"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I34131["TaN/SiNx/TaN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I47402["TaN"], I8777["SiNx"], I47402["TaN"]],

)


# 2019
I47402["TaN"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I8777["SiNx"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I89808["TE(Cu doped) /Cu8GeSe6/<br>BE(Cu doped)"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I73802["TE(Cu doped) "], I63079["Cu8GeSe6"], I92934["<br>BE(Cu doped)"]],

)


# 2019
I73802["TE(Cu doped) "].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I63079["Cu8GeSe6"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I92934["<br>BE(Cu doped)"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I97154["TiN/GexSe1–x/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I72298["GexSe1–x"], I21621["TiN"]],

)


# 2019
I72298["GexSe1–x"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I83048["TiN/As:SiO2/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I16765["As:SiO2"], I21621["TiN"]],

)


# 2019
I16765["As:SiO2"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I87992["Pt/VO2/Pt"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I97657["Pt"], I58468["VO2"], I97657["Pt"]],

)


# 2019
I58468["VO2"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I82062["TiN/NbO2/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I27966["NbO2"], I21621["TiN"]],

)


# 2019
I27966["NbO2"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I46285["TiN/NbO2/W"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I27966["NbO2"], I8849["W"]],

)


# 2019
I9309["TiN/AsTeGeSiN/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I18158["AsTeGeSiN"], I21621["TiN"]],

)


# 2019
I18158["AsTeGeSiN"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I55774["W/Ag/MgO/Ag/W"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I8849["W"], I95705["Ag"], I78145["MgO"], I95705["Ag"], I8849["W"]],

)


# 2019
I95705["Ag"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I78145["MgO"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I11520["Pt/Ag:SiOxNy/Pt"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I97657["Pt"], I59694["Ag:SiOxNy"], I97657["Pt"]],

)


# 2019
I59694["Ag:SiOxNy"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I56829["Pd/Ag/HfO2/Ag/Pd"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I10094["Pd"], I95705["Ag"], I42033["HfO2"], I95705["Ag"], I10094["Pd"]],

)


# 2019
I10094["Pd"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I42033["HfO2"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I69530["P2+/N+/N2+ epitaxial Si"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I68259["P2+"], I29098["N+"], I82346["N2+ epitaxial Si"]],

)


# 2019
I68259["P2+"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I29098["N+"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I82346["N2+ epitaxial Si"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I90071["TiN/Al2O3/TiO2/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I12398["Al2O3"], I87136["TiO2"], I21621["TiN"]],

)


# 2019
I12398["Al2O3"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I98878["W/VOx/Pt"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I8849["W"], I23249["VOx"], I97657["Pt"]],

)


# 2019
I23249["VOx"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I76087["p-Si/SiO2/n-Si"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I48237["p-Si"], I61398["SiO2"], I99103["n-Si"]],

)


# 2019
I48237["p-Si"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I61398["SiO2"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I99103["n-Si"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I28976["Ni/HfO2/n-Si"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I53205["Ni"], I42033["HfO2"], I99103["n-Si"]],

)


# 2019
I11681["Cu/HfO2/n-Si"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I41069["Cu"], I42033["HfO2"], I99103["n-Si"]],

)


# 2019
I41069["Cu"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I37167["Ag/a-Si/p-poly-Si"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I95705["Ag"], I86221["a-Si"], I47202["p-poly-Si"]],

)


# 2019
I86221["a-Si"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2019
I47202["p-poly-Si"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I29376["publication: Hardware implementation of memristorbased artificial neural networks"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=["Fernando Aguirre", "Abu Sebastian"],
    ag__R8434__has_title="Hardware implementation of memristorbased artificial neural networks",
    ag__R8435__has_year=2024,
    ag__R8440__cites=[I1362["publication: Fully hardware-implemented memristor convolutional neural network"], I73000["publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations"], I67827["publication: A compute-in-memory chip based on resistive random-access memory"], I87613["publication: High-throughput in-memory computing for binary deep neural networks with monolithically integrated RRAM and 90-nm CMOS"], I64045["publication: HERMES-Core-A 1.59-TOPS/mm2PCM on 14-nm CMOS in-memory compute core using 300-ps/LSB linearized CCO-based ADCs"], I52752["publication: Fully on-chip MAC at 14 nm enabled by accurate row-wise programming of PCM-based weights and parallel vector-transport in duration-format"], I51187["publication: A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference"], I75602["publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture"], I22852["publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory"], I13415["publication: A fully hardware-based memristive multilayer neural network"], I84363["publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration"], I61262["publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques"], I69614["publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark"], I91097["publication: Fully memristive neural networks for pattern classification with unsupervised learning"], I32602["publication: Equivalent-accuracy accelerated neural network training using analogue memory"], I60259["publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks"], I74604["publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors"], I59620["publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays"], I72736["publication: A 1Mb Multibit ReRAM computing-in-memory macro with 14.6ns Parallel MAC computing time for CNN based AI Edge processors"], I15972["publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques"], I86194["publication: A Fully Integrated Analog ReRAM based 78.4TOPS/ W compute-in-memory chip with fully parallel MAC computing"]],

)


# 2024
I69517["Yao, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yao, P.",

)


# 2024
I1362["publication: Fully hardware-implemented memristor convolutional neural network"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I69517["Yao, P."],
    ag__R8434__has_title="Fully hardware-implemented memristor convolutional neural network",
    ag__R8435__has_year=2020,
    R68123__has_memristor_stack=I8593["TiN/TaOx/HfO/TiNx"],

)


# 2024
I57709["Cai, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Cai, F.",

)


# 2024
I73000["publication: A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I57709["Cai, F."],
    ag__R8434__has_title="A fully integrated reprogrammable memristor-CMOS system for efficient multiply-accumulate operations",
    ag__R8435__has_year=2019,
    R68123__has_memristor_stack=I72160["Au/Pd/WOX/Au"],

)


# 2024
I49887["Wan, W."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wan, W.",

)


# 2024
I67827["publication: A compute-in-memory chip based on resistive random-access memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I49887["Wan, W."],
    ag__R8434__has_title="A compute-in-memory chip based on resistive random-access memory",
    ag__R8435__has_year=2022,
    R68123__has_memristor_stack=I71268["TiN/HfO2/TaOX/TiN"],

)


# 2024
I22963["Yin, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yin, S.",

)


# 2024
I17132["Sun, X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Sun, X.",

)


# 2024
I74155["Yu, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yu, S.",

)


# 2024
I18985["Seo, J. S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Seo, J. S.",

)


# 2024
I87613["publication: High-throughput in-memory computing for binary deep neural networks with monolithically integrated RRAM and 90-nm CMOS"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I22963["Yin, S."], I17132["Sun, X."], I74155["Yu, S."], I18985["Seo, J. S."]],
    ag__R8434__has_title="High-throughput in-memory computing for binary deep neural networks with monolithically integrated RRAM and 90-nm CMOS",
    ag__R8435__has_year=2020,

)


# 2024
I95725["Khaddam-Aljameh, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Khaddam-Aljameh, R.",

)


# 2024
I64045["publication: HERMES-Core-A 1.59-TOPS/mm2PCM on 14-nm CMOS in-memory compute core using 300-ps/LSB linearized CCO-based ADCs"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I95725["Khaddam-Aljameh, R."],
    ag__R8434__has_title="HERMES-Core-A 1.59-TOPS/mm2PCM on 14-nm CMOS in-memory compute core using 300-ps/LSB linearized CCO-based ADCs",
    ag__R8435__has_year=2022,

)


# 2024
I79243["Narayanan, P."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Narayanan, P.",

)


# 2024
I52752["publication: Fully on-chip MAC at 14 nm enabled by accurate row-wise programming of PCM-based weights and parallel vector-transport in duration-format"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I79243["Narayanan, P."],
    ag__R8434__has_title="Fully on-chip MAC at 14 nm enabled by accurate row-wise programming of PCM-based weights and parallel vector-transport in duration-format",
    ag__R8435__has_year=2021,

)


# 2024
I49299["Le Gallo, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Le Gallo, M.",

)


# 2024
I51187["publication: A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I49299["Le Gallo, M."],
    ag__R8434__has_title="A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference",
    ag__R8435__has_year=2022,

)


# 2024
I59886["Mochida, R."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Mochida, R.",

)


# 2024
I75602["publication: A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I59886["Mochida, R."],
    ag__R8434__has_title="A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture",
    ag__R8435__has_year=2018,
    R68123__has_memristor_stack=I25994["W/Ta2O5/TaOx/W"],

)


# 2024
I26646["Su, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Su, F.",

)


# 2024
I22852["publication: A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I26646["Su, F."],
    ag__R8434__has_title="A 462GOPs/J RRAM-based nonvolatile intelligent processor for energy harvesting IoE system featuring nonvolatile logics and processing-in-memory",
    ag__R8435__has_year=2017,
    R68123__has_memristor_stack=I12147["AlCu/TiN/Ti/HfO2/TiN"],

)


# 2024
I77881["Kiani, F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Kiani, F.",

)


# 2024
I49586["Yin, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Yin, J.",

)


# 2024
I55924["Joshua Yang, J."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Joshua Yang, J.",

)


# 2024
I97111["Xia, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Xia, Q.",

)


# 2024
I13415["publication: A fully hardware-based memristive multilayer neural network"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=[I77881["Kiani, F."], I49586["Yin, J."], I99712["Wang, Z."], I55924["Joshua Yang, J."], I97111["Xia, Q."]],
    ag__R8434__has_title="A fully hardware-based memristive multilayer neural network",
    ag__R8435__has_year=2021,
    R68123__has_memristor_stack=I33540["Pt/Ta/Ta2O5/Pt/Ti"],

)


# 2024
I84363["publication: CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I85528["Li, C."],
    ag__R8434__has_title="CMOS-integrated nanoscale memristive crossbars for CNN and optimization acceleration",
    ag__R8435__has_year=2020,
    R68123__has_memristor_stack=I52096["Ta/TaOx/Pt"],

)


# 2024
I51358["Pedretti, G."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Pedretti, G.",

)


# 2024
I61262["publication: Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I51358["Pedretti, G."],
    ag__R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part I: Programming techniques",
    ag__R8435__has_year=2021,

)


# 2024
I69614["publication: Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I51358["Pedretti, G."],
    ag__R8434__has_title="Redundancy and analog slicing for precise inmemory machine learning - Part II: Applications and benchmark",
    ag__R8435__has_year=2021,

)


# 2024
I91097["publication: Fully memristive neural networks for pattern classification with unsupervised learning"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I99712["Wang, Z."],
    ag__R8434__has_title="Fully memristive neural networks for pattern classification with unsupervised learning",
    ag__R8435__has_year=2018,
    R68123__has_memristor_stack=[I96420["Pt/SiOxAg/Pt/Ti"], I83149[" Ta/Pd/HfO2/Pt/Ti"]],

)


# 2024
I84267["Ambrogio, S."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Ambrogio, S.",

)


# 2024
I32602["publication: Equivalent-accuracy accelerated neural network training using analogue memory"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I84267["Ambrogio, S."],
    ag__R8434__has_title="Equivalent-accuracy accelerated neural network training using analogue memory",
    ag__R8435__has_year=2018,

)


# 2024
I91573["Bocquet, M."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Bocquet, M.",

)


# 2024
I60259["publication: In-memory and error-immune differential RRAM implementation of binarized deep neural networks"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I91573["Bocquet, M."],
    ag__R8434__has_title="In-memory and error-immune differential RRAM implementation of binarized deep neural networks",
    ag__R8435__has_year=2018,
    R68123__has_memristor_stack=I60267["TiN/HfO2/Ti/TiN"],

)


# 2024
I73590["Chen, W. H."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Chen, W. H.",

)


# 2024
I74604["publication: CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I73590["Chen, W. H."],
    ag__R8434__has_title="CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors",
    ag__R8435__has_year=2019,
    R68123__has_memristor_stack=I59167["W/TiN/TiON"],

)


# 2024
I66704["Hirtzlin, T."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Hirtzlin, T.",

)


# 2024
I59620["publication: Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I66704["Hirtzlin, T."],
    ag__R8434__has_title="Digital biologically plausible implementation of binarized neural networks with differential hafnium oxide resistive memory arrays",
    ag__R8435__has_year=2020,
    R68123__has_memristor_stack=I60267["TiN/HfO2/Ti/TiN"],

)


# 2024
I38907["Xue, C. X."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Xue, C. X.",

)


# 2024
I72736["publication: A 1Mb Multibit ReRAM computing-in-memory macro with 14.6ns Parallel MAC computing time for CNN based AI Edge processors"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I38907["Xue, C. X."],
    ag__R8434__has_title="A 1Mb Multibit ReRAM computing-in-memory macro with 14.6ns Parallel MAC computing time for CNN based AI Edge processors",
    ag__R8435__has_year=2019,

)


# 2024
I31938["Wu, T. F."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Wu, T. F.",

)


# 2024
I15972["publication: A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I31938["Wu, T. F."],
    ag__R8434__has_title="A 43pJ/Cycle Non-Volatile Microcontroller with 4.7μs Shutdown/Wake-up Integrating 2.3-bit/Cell Resistive RAM and Resilience Techniques",
    ag__R8435__has_year=2019,
    R68123__has_memristor_stack=I60267["TiN/HfO2/Ti/TiN"],

)


# 2024
I70751["Liu, Q."].update_relations(
    R4__is_instance_of=ag.I7435["human"],
    ag__R7781__has_family_name="Liu, Q.",

)


# 2024
I86194["publication: A Fully Integrated Analog ReRAM based 78.4TOPS/ W compute-in-memory chip with fully parallel MAC computing"].update_relations(
    R4__is_instance_of=ag.I6591["source document"],
    ag__R8433__has_authors=I70751["Liu, Q."],
    ag__R8434__has_title="A Fully Integrated Analog ReRAM based 78.4TOPS/ W compute-in-memory chip with fully parallel MAC computing",
    ag__R8435__has_year=2020,
    R68123__has_memristor_stack=I15050["-/HfO2/TaOX/-"],

)


# 2024
I72160["Au/Pd/WOX/Au"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I43694["Au"], I10094["Pd"], I10506["WOX"], I43694["Au"]],

)


# 2024
I43694["Au"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I10506["WOX"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I8593["TiN/TaOx/HfO/TiNx"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I95219["TaOx"], I65099["HfO"], I16673["TiNx"]],

)


# 2024
I65099["HfO"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I16673["TiNx"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I33540["Pt/Ta/Ta2O5/Pt/Ti"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I97657["Pt"], I36840["Ta"], I7533["Ta2O5"], I97657["Pt"], I4130["Ti"]],

)


# 2024
I36840["Ta"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I4130["Ti"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I52096["Ta/TaOx/Pt"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I36840["Ta"], I95219["TaOx"], I97657["Pt"]],

)


# 2024
I59167["W/TiN/TiON"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I8849["W"], I21621["TiN"], I21466["TiON"]],

)


# 2024
I21466["TiON"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I96420["Pt/SiOxAg/Pt/Ti"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I97657["Pt"], I2133["SiOxAg"], I97657["Pt"], I4130["Ti"]],

)


# 2024
I2133["SiOxAg"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I83149[" Ta/Pd/HfO2/Pt/Ti"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I43547[" Ta"], I10094["Pd"], I42033["HfO2"], I97657["Pt"], I4130["Ti"]],

)


# 2024
I43547[" Ta"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I60267["TiN/HfO2/Ti/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I42033["HfO2"], I4130["Ti"], I21621["TiN"], I21621["TiN"], I42033["HfO2"], I4130["Ti"], I21621["TiN"], I21621["TiN"], I42033["HfO2"], I4130["Ti"], I21621["TiN"]],

)


# 2024
I25994["W/Ta2O5/TaOx/W"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I8849["W"], I7533["Ta2O5"], I95219["TaOx"], I8849["W"]],

)


# 2024
I12147["AlCu/TiN/Ti/HfO2/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I84254["AlCu"], I21621["TiN"], I4130["Ti"], I42033["HfO2"], I21621["TiN"]],

)


# 2024
I84254["AlCu"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I15050["-/HfO2/TaOX/-"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I10578["-"], I42033["HfO2"], I45648["TaOX"], I10578["-"]],

)


# 2024
I10578["-"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I45648["TaOX"].update_relations(
    R4__is_instance_of=I74938["stack component"],

)


# 2024
I71268["TiN/HfO2/TaOX/TiN"].update_relations(
    R4__is_instance_of=I39529["memristor stack"],
    R62251__has_stack_component=[I21621["TiN"], I42033["HfO2"], I45648["TaOX"], I21621["TiN"]],

)




p.end_mod()