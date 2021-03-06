[diagram]
link=[N4] node=[U1:str_conc#Node#C2:str_conc]
link=[N3] node=[U2:outString#Node#U1:stringIn_0]
link=[N0] node=[U0:factorial#Node#C1:factorial]
link=[N5] node=[C0:inInt#Node#U3:inInt]
link=[N2] node=[U3:outIn#Node#U2:inInt]
link=[N1] node=[U3:outIn#Node#U0:enter_int]
block=[U1] category=[Tools.StringManipulation] class=[string_concatenat_dyn] valInputs=[(['stringIn', 'stringIn_0', 'stringIn_1'], ['', 'Node(N3)', '! = '], ['str_conc'], ['str'])] RectF=[(-5.1761399018933005, 75.84097419483666, 156.71875, 80.0)]
block=[U3] category=[Tools.Constants] class=[Constant_int_simple] valInputs=[(['inInt'], ['Node(N5)'], ['outIn'], ['int'])] RectF=[(-512.2978369359828, -15.232736488744223, 150.0, 80.0)]
block=[U2] category=[Tools.Conversion] class=[IntToString] valInputs=[(['inInt'], ['Node(N2)'], ['outString'], ['str'])] RectF=[(-215.30016207634336, 74.07504051908583, 150.0, 80.0)]
block=[U0] category=[C.Maths] class=[fact] valInputs=[(['enter_int'], ['Node(N1)'], ['factorial'], ['int'])] RectF=[(-224.0, -109.0, 150.0, 80.0)]
connt=[C2] name=[str_conc] type=[out] format=[str] RectF=[(206.60983267523218, 101.43238618751508, 70, 24)]
connt=[C1] name=[factorial] type=[out] format=[int] RectF=[(185.48008173203613, -88.50475819744327, 70, 24)]
connt=[C0] name=[inInt] type=[in] format=[int] valOut=[0] RectF=[(-692.7930787385395, 14.441215053785811, 70, 24)]
[execution]
['C0:inInt=']
['U3', 'ThreadOn', 'U2', 'U0', 'ThreadOff', 'U1']
{'U0': ('C.Maths', 'fact', "(['enter_int'], ['U3:outIn'], ['factorial'], ['int'])"), 'U2': ('Tools.Conversion', 'IntToString', "(['inInt'], ['U3:outIn'], ['outString'], ['str'])"), 'U3': ('Tools.Constants', 'Constant_int_simple', "(['inInt'], ['C0:inInt'], ['outIn'], ['int'])"), 'U1': ('Tools.StringManipulation', 'string_concatenat_dyn', "(['stringIn', 'stringIn_0', 'stringIn_1'], ['', 'U2:outString', '! = '], ['str_conc'], ['str'])")}
['U3:outIn', 'U3:outIn', 'C0:inInt', 'U0:factorial', 'U2:outString', 'U1:str_conc']
{}
['C1:factorial=U0:factorial', 'C2:str_conc=U1:str_conc']
