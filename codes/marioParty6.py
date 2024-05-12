# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Blue Spaces Give {amountDec} Coins
0415F1E8 3880{amount}
'''

def getRedSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Red Spaces Take Away {amountDec} Coins
0415F278 3880{amount}
'''

def getMinigameCodeSix(amount, amountDec):
    return f'''
MP6 - Minigames Award {amountDec} Coins
2A265BA8 00000015
2A265BA8 00000016
2A265BA8 00000029
2A265BA8 0000002D
2A265BA8 0000002E
2A265BA8 00000030
2A265BA8 0000003F
2A265BA8 0000004F
2A265BA8 00000050
28265778 0000000A
02265778 0000{amount}
E2000001 80008000
2A265BA8 00000015
2A265BA8 00000016
2A265BA8 00000029
2A265BA8 0000002D
2A265BA8 0000002E
2A265BA8 00000030
2A265BA8 0000003F
2A265BA8 0000004F
2A265BA8 00000050
28265988 0000000A
02265988 0000{amount}
E2000001 80008000
2A265BA8 00000015
2A265BA8 00000016
2A265BA8 00000029
2A265BA8 0000002D
2A265BA8 0000002E
2A265BA8 00000030
2A265BA8 0000003F
2A265BA8 0000004F
2A265BA8 00000050
28265A90 0000000A
02265A90 0000{amount}
E2000001 80008000
2A265BA8 00000015
2A265BA8 00000016
2A265BA8 00000029
2A265BA8 0000002D
2A265BA8 0000002E
2A265BA8 00000030
2A265BA8 0000003F
2A265BA8 0000004F
2A265BA8 00000050
28265880 0000000A
02265880 0000{amount}
E2000001 80008000
'''

def getCharacterSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Character Spaces Give {amountDec} Coins
0415F230 3880{amount}
'''

def getStarSpaceCodeSix(amount, negAmount, amountDec):
    return f'''
MP6 - Stars Cost {amountDec} Coins
0418333C 2C03{amount}
0418342C 2C03{amount}
041834C4 2C03{amount}
0415F668 2C03{amount}
0415FA18 3880{negAmount}
0416068C 2C00{amount}
04160D0C 3880{negAmount}    
C2183590 00000002
3880{amount} 7C8400D0
60000000 00000000
28265B8A 00000014
00265B8B 0000{amount}
E2000001 80008000
204F0E28 2C030014
044F0E28 2C03{amount}
E2000001 80008000
204F0F38 3880FFEC
044F0F38 3880{negAmount}
E2000001 80008000
C2184538 00000001
2C14{amount} 00000000
C2184544 00000001
3880{negAmount} 00000000
'''

def getFaireSquareStarCodeSix(one, two, three, four):
    return f'''
MP6 - Stars Can Cost SIXONE, SIXTWO, SIXTHREE, or SIXFOUR During Faire Square's Nightime
04248064 0000{one}
04248068 0000{two}
04248070 0000{three}
04248074 0000{four}
04248D3C 0000{one}
04248D40 0000{two}
04248D48 0000{three}
04248D4C 0000{four}
204DDF60 465F6C00
044DDF74 0000{one}
044DDF78 0000{two}
044DDF80 0000{three}
044DDF84 0000{four}
E2000001 80008000
'''

def getPinkBooSpaceCodeSix(amount, negAmount, amountDec):
    return f'''
MP6 - Stars Cost {amountDec} Coins when stealing with Pink Boo
C21B1FB4 00000001
2C04{amount} 00000000
C21B2634 00000001
3880{negAmount} 00000000
'''

def getPinkBooCoinsSpaceCodeSix(amount, negAmount, amountDec):
    return f'''
MP6 - Coins Cost {amountDec} Coins when stealing with Pink Boo
C21B1F28 00000001
2C03{amount} 00000000
C21B2626 00000001
3880{negAmount} 00000000
'''

def getMinigameReplacement6(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP6 - Minigame Replacement: {gameUno} ➜ {gameDos}
28265BA8 000000{hexUno}
02265BA8 000000{hexDos}
E2000001 80008000
'''

def getOrbModsSix(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW):
    return f'''
MP6 - Orb Modifier
042BD220 00050505
042BD224 {oneW}{oneW}{oneW}{oneW}
042BD228 {oneW}{oneW}{oneW}{oneW}
042BD22C {oneW}{oneW}{oneW}{oneW}
042BD230 01{twoP}{twoP}{twoP}
042BD234 {twoW}{twoW}{twoW}{twoW}
042BD238 {twoW}{twoW}{twoW}{twoW}
042BD23C {twoW}{twoW}{twoW}{twoW}
042BD240 02{threeP}{threeP}{threeP}
042BD244 {threeW}{threeW}{threeW}{threeW}
042BD248 {threeW}{threeW}{threeW}{threeW}
042BD24C {threeW}{threeW}{threeW}{threeW}
042BD250 03{fourP}{fourP}{fourP}
042BD254 {fourW}{fourW}{fourW}{fourW}
042BD258 {fourW}{fourW}{fourW}{fourW}
042BD25C {fourW}{fourW}{fourW}{fourW}
042BD260 04{fiveP}{fiveP}{fiveP}
042BD264 {fiveW}{fiveW}{fiveW}{fiveW}
042BD268 {fiveW}{fiveW}{fiveW}{fiveW}
042BD26C {fiveW}{fiveW}{fiveW}{fiveW}
042BD270 05{sixP}{sixP}{sixP}
042BD274 {sixW}{sixW}{sixW}{sixW}
042BD278 {sixW}{sixW}{sixW}{sixW}
042BD27C {sixW}{sixW}{sixW}{sixW}
042BD280 06{sevenP}{sevenP}{sevenP}
042BD284 {sevenW}{sevenW}{sevenW}{sevenW}
042BD288 {sevenW}{sevenW}{sevenW}{sevenW}
042BD28C {sevenW}{sevenW}{sevenW}{sevenW}
042BD290 07{eightP}{eightP}{eightP}
042BD294 {eightW}{eightW}{eightW}{eightW}
042BD298 {eightW}{eightW}{eightW}{eightW}
042BD29C {eightW}{eightW}{eightW}{eightW}
042BD2A0 0A{nineP}{nineP}{nineP}
042BD2A4 {nineW}{nineW}{nineW}{nineW}
042BD2A8 {nineW}{nineW}{nineW}{nineW}
042BD2AC {nineW}{nineW}{nineW}{nineW}
042BD2B0 0B{tenP}{tenP}{tenP}
042BD2B4 {tenW}{tenW}{tenW}{tenW}
042BD2B8 {tenW}{tenW}{tenW}{tenW}
042BD2BC {tenW}{tenW}{tenW}{tenW}
042BD2C0 0C{elevenP}{elevenP}{elevenP}
042BD2C4 {elevenW}{elevenW}{elevenW}{elevenW}
042BD2C8 {elevenW}{elevenW}{elevenW}{elevenW}
042BD2CC {elevenW}{elevenW}{elevenW}{elevenW}
042BD2D0 0D{twelveP}{twelveP}{twelveP}
042BD2D4 {twelveW}{twelveW}{twelveW}{twelveW}
042BD2D8 {twelveW}{twelveW}{twelveW}{twelveW}
042BD2DC {twelveW}{twelveW}{twelveW}{twelveW}
042BD2E0 0F{thirteenP}{thirteenP}{thirteenP}
042BD2E4 {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042BD2E8 {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042BD2EC {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042BD2F0 10{fourteenP}{fourteenP}{fourteenP}
042BD2F4 {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042BD2F8 {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042BD2FC {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042BD300 11{fifteenP}{fifteenP}{fifteenP}
042BD304 {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042BD308 {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042BD30C {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042BD310 14{sixteenP}{sixteenP}{sixteenP}
042BD314 {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042BD318 {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042BD31C {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042BD320 15{seventeenP}{seventeenP}{seventeenP}
042BD324 {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042BD328 {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042BD32C {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042BD330 16{eighteenP}{eighteenP}{eighteenP}
042BD334 {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042BD338 {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042BD33C {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042BD340 17{ninteenP}{ninteenP}{ninteenP}
042BD344 {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042BD348 {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042BD34C {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042BD350 18{twentyP}{twentyP}{twentyP}
042BD354 {twentyW}{twentyW}{twentyW}{twentyW}
042BD358 {twentyW}{twentyW}{twentyW}{twentyW}
042BD35C {twentyW}{twentyW}{twentyW}{twentyW}
042BD360 19{twentyOneP}{twentyOneP}{twentyOneP}
042BD364 {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042BD368 {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042BD36C {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042BD370 1E{twentyTwoP}{twentyTwoP}{twentyTwoP}
042BD374 {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042BD378 {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042BD37C {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042BD380 1F{twentyThreeP}{twentyThreeP}{twentyThreeP}
042BD384 {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042BD388 {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042BD38C {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042BD390 2E{twentyFourP}{twentyFourP}{twentyFourP}
042BD394 {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042BD398 {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042BD39C {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042BD3A0 2A{twentyFiveP}{twentyFiveP}{twentyFiveP}
042BD3A4 {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042BD3A8 {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042BD3AC {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042BD3B0 2B{twentySixP}{twentySixP}{twentySixP}
042BD3B4 {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042BD3B8 {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042BD3BC {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042BD3C0 2C{twentySevenP}{twentySevenP}{twentySevenP}
042BD3C4 {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042BD3C8 {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042BD3CC {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042BD3D0 29{twentyEightP}{twentyEightP}{twentyEightP}
042BD3D4 {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042BD3D8 {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042BD3DC {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042BD3E0 FF000000
042BD3E4 00000000
042BD3E8 00000000
042BD3EC 00000000
'''

def getInitialItemsSix(one, two, three, oneItem, twoItem, threeItem):
    return f'''
MP6 - Start with {oneItem}, {twoItem}, and {threeItem}
06003620 00000028
3D808000 618C363C
1C1F0003 7C00E214
7CAC00AE 98A30005
48150114 {one}{two}{three}{one}
{two}{three}{one}{two} {three}{one}{two}{three}
04153748 4BEAFED8
'''

def getCoinStealBaseSix(value, amountDec):
    return f'''
MP6 - Steal SIXBOOMIN Coins Minimum from Pink Boo
C21B3498 00000002
3884{value} 9081002C
60000000 00000000
'''

def getSpaceReplaceSix1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP6 - Replace {spaceName} with {spaceName2} (Slot A)
C217590C 00000005
A01F0030 280000{spaceHex1}
40820018 A09F0032
2804FFFF 4082000C
380000{spaceHex2} B01F0030
88030000 00000000
'''

def getSpaceReplaceSix2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP6 - Replace {spaceName} with {spaceName2} (Slot B)
C2175910 00000005
5418CFFE A01F0030
280000{spaceHex1} 40820018
A09F0032 2804FFFF
4082000C 380000{spaceHex2}
B01F0030 00000000
'''

def getOtherCodesSix(code):
    if code == "30Hz":
        return '''
042C0038 40000000
042C003C 00000002
040440F0 38600001
C2005AB0 00000009
3C808000 6084E37C
7C8903A6 4E800421
3C808000 60845D90
7C8903A6 4E800421
38800000 908D8900
908D8904 38600001
3C808000 6084E37C
7C8903A6 4E800421
60000000 00000000
C2049194 00000002
7C9F2378 7CA50E70
60000000 00000000'''
    if code == "BattleMinigame":
        return '''
204cddc8 b003001e
044cddc4 60000000
e2000001 80008000'''
    if code == "CoinStar":
        return '''
204ecf4c a8c70034
044ecf4c a8c70022
e2000001 00000000
204ed07c a8e30034
044ed07c a8e30022
e2000001 00000000
2053109c 54686973
0453109c 54686973
045310a0 10697310
045310a4 796f7572
045310a8 106d6178
045310ac 10636f69
045310b0 6e731063
045310b4 6f6c6c65
045310b8 63746564
045310bc 85000000
e2000001 00000000'''
    if code == "PermaPaths":
        return '''
F6000001 80008180
41820118 2C170000
14000000 60000000
E0000000 80008000'''
    if code == "RandomMusic":
        return '''
C214427C 00000004
7C7D1B78 3860006E
3C808003 6084FCD4
7C8903A6 4E800421
7C7D1B78 00000000'''
    if code == "AdvanceText":
        return '''
F6000002 80008180
A81F01A0 7C001838
28000000 41820128
1400000C 60000000
E0000000 80008000'''
    if code == "DisableAdv":
        return '''
20503FB0 41820054
04503FB0 48000054
E2000001 80008000'''
    if code == "ChangeTurnCount":
        return '''
06005100 00000064
3C60802C A083FFD0
A0630008 3CA08026
88C55B75 546005EF
41820044 54800673
4182000C 38C6FFFF
48000010 548006B5
4182002C 38C60001
28060063 40810008
38C00063 88055B74
7C060040 40800008
7C060378 98C55B75
4818CE5C 806D9808
4818CE38 00000000
04191F94 4BE7316C'''
    if code == "DisableMus":
        return '''
042c02a4 00000001'''
    if code == "Boot":
        return '''
204cdc74 386003e8
044cdc34 48000038
044cdc4c 48000020
e2000001 80008000
204cc980 41820078
044cc980 60000000
e2000001 80008000
204CCE7C 3BDE0001
044CCE7C 3BC00DB6
E2000001 80008000'''
    if code == "BSpeed":
        return '''
041556d4 7d170e70
042c31b4 41f00000
041b02ac 60000000
04161758 38030002
04161764 38030002
204cdb1c 281e0018
044cdb18 3bde0002
e2000001 80008000
042c3e94 42200000
c21c28bc 00000002
801f0020 38800002
7c0027d6 00000000
c21c245c 00000002
801f0020 38800002
7c0027d6 00000000'''
    if code == "TSpam":
        return '''
0420526c 60000000
0420518c 60000000
0420516c 60000000'''
    if code == "OThrow":
        return '''
c21c28bc 00000002
801f0020 38800002
7c0027d6 00000000
c21c245c 00000002
801f0020 38800002
7c0027d6 00000000'''
    if code == "TxtDisplay":
        return '''
0404f51c 38000000'''
    if code == "ShowCtrl":
        return '''
C20456D4 00000002
807F0050 906D0000
38600000 00000000
C203E1FC 0000000C
3860012C 3880000A
38A0002D 38C00028
38E000FF 90ED0004
38ED0004 3D008000
6108C4B0 7D0903A6
4E800421 3860012C
3880000A 3CA08023
38A5ABEF 80CD0000
38C60001 C0228350
3CE08000 60E7C354
7CE903A6 4E800421
57A0083C 00000000
C2192B1C 00000006
38DD0001 C02280E0
38600138 38800010
3CA08022 60A5ABEF
3CE08000 60E7C354
7CE903A6 4E800421
57A0083C 00000000'''
    if code == "UnlockAll":
        return '''
F6000001 80008180
80A405A8 38800001
14000000 38A0FFFF
E0000000 80008000
F6000001 80008180
80A405A0 38800001
14000000 38A0FFFF
E0000000 80008000
F6000002 80008180
5460D808 54640FFE
7C040050 5400283E
14000020 3C80FFFF
14000024 6084FFFF
E0000000 80008000'''
    if code == "ZtarC":
        return '''
C21843D8 00000002
38600000 2C030001
60000000 00000000'''
    if code == "FaireHappening":
        return '''
282C0256 0000007D
044d3c70 60000000
044d4e3C 60000000
044d3c70 60000000
E2000001 80008000'''
    if code == "LakeRoll":
        return '''
204cc818 4bcbbacd
c24cc810 00000005
3b200007 3c608026
88635b80 5463d7fe
28030000 4182000c
1f3d0003 3b390003
60000000 00000000
e2000001 80008000'''
    if code == "LakeSellStar":
        return '''
0418040c 480000f0
204cadfc 48001595
48000000 802c0364
de000000 80008180
14014f64 7834300a
e2000001 80008000
204cadfc 48001595
c24cc390 00000021
9421ffe0 7c0802a6
90010024 93e10008
93c1000c 93a10018
7c7f1b78 3fc08015
63decd40 7fc903a6
4e800421 2c030028
418000b4 1c7f0108
3c808026 7c632214
88635750 70630020
40820050 38600001
3c800027 38840003
38a00006 38c00000
3fc08016 63debce8
7fc903a6 4e800421
3fc08016 63decda8
7fc903a6 4e800421
3fc08016 63decafc
7fc903a6 4e800421
2c030000 40820050
7fe3fb78 3880ffd8
3fc08017 63dee824
7fc903a6 4e800421
7fe3fb78 38800000
38a00001 38c00001
3fc08017 63defef0
7fc903a6 4e800421
38600014 3fc08016
63deec68 7fc903a6
4e800421 83a10018
83c1000c 83e10008
80010024 7c0803a6
38210020 4e800020
60000000 00000000
044cb09c 480000a0
e2000001 80008000'''
    if code == "LakeRollPlus5":
        return '''
204CC814 7FE3FB78
C24CC810 00000003
2C030005 40800008
38600005 7C791B78
60000000 00000000
E2000001 80008000'''
    if code == "AlwaysSneeze":
        return '''
202c0254 0000007b
044fde9c 60000000
044fde84 60000000
e2000001 80008000'''
    if code == "DoubleTurns":
        return '''
C214C75C 00000004
2C000032 4182000C
7C000214 48000008
38000063 98030005
60000000 00000000'''
    if code == "LakeStart3":
        return '''
204cb0dc 389b0005
044cb0dc 389b0003
e2000001 80008000'''
    if code == "ForceL5":
        return '''
F6000001 80008180
7C040040 4080041C
14000004 60000000
E0000000 80008000'''
    if code == "PPAll":
        return '''
C21A4BC8 00000001
38630000 00000000
C21A4BD4 00000001
7C7B1B78 00000000'''
    if code == "3Jump":
        return '''
202c0254 00000025
0408074c 60fb0003
e2000001 80008000
222c0254 00000025
0408074c 7cfb3b78
e2000001 80008000'''
    if code == "DizzyR":
        return '''
204F3F84 38800708
044F3F84 388004B0
E2000001 80008000'''
    if code == "SameSpaceAlways":
        return '''
04154348 60000000'''
    if code == "SameSpaceNever":
        return '''
04154348 48000048'''
    if code == "Insectiride":
        return '''
202c0254 00000034
204a176c c48d4000
044a176c c49c4000
e2000002 80008000
202c0254 00000034
204de52c c48d4000
044de52c c49c4000
e2000002 80008000
202c0254 00000034
204a183c 3f800000
044a183c 3fc00000
e2000002 80008000
202c0254 00000034
204d670c 40555555
044d670c 4079999a
e2000002 80008000'''
    if code == "QuickFinish":
        return '''
202c0254 0000003d
20538c60 3f800000
04538c60 4400c000
e2000002 80008000
202c0254 0000003d
20538ce0 3f800000
04538ce0 4400c000
e2000002 80008000'''
    if code == "TiesAreTies":
        return '''
204cf648 4082005c
044cf648 4800005c
e2000001 80008000'''
    if code == "PermDeath":
        return '''
202c0254 00000007
204d0530 b0a30052
044d0530 60000000
e2000002 80008000'''
    if code == "SlowerLazer":
        return '''
202c0254 00000026
044d2cfc 41a00000
e2000001 80008000'''
    if code == "StageFright":
        return '''
202c0254 00000023
204ebe52 00000708
044ebe52 000005dc
e2000002 80008000'''
    if code == "NoTrail":
        return '''
20474A04 38030001
04474A04 3800003C
E2000001 80008000'''
    if code == "HalvedTime":
        return '''
202c0254 00000011
204d6a0f 00000000
044d699f 0000003f
e2000002 80008000'''
    if code == "TankAir":
        return '''
202c0254 0000001e
204cf0b4 38030005
044cf0b4 38030003
044cf1a4 3803fffe
e2000002 80008000'''
    if code == "DisableLast5":
        return '''
0408D1F4 41800048'''
    if code == "ForceLast5":
        return '''
2080CB88 3F800000
0480CB88 2C040001
0408CB8C 41800048
E2000001 80008000'''
    if code == "x3 Coins":
        return '''
040FB87C 38A00000
040FB8EC 3A600000'''
    if code == "5 Star Spaces":
        return '''
040FB87C 38A00003
040FB8EC 3A600003'''
    if code == "Capsule Sapces on Every Space":
        return '''
040FB87C 38A00001
040FB8EC 3A600001'''
    if code == "Red Spaces are Bowser Spaces":
        return '''
040FB87C 38A00002
040FB8EC 3A600002'''