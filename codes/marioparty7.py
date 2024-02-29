# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeSeven(amount):
    return f'''
MP7 - Blue Spaces Give SEVENBLUE Coins
04168578 60000000
0416857C 3880{amount}
'''

def getRedSpaceCodeSeven(amount):
    return f'''
MP7 - Red Spaces Take Away SEVENRED Coins
04168600 60000000
04168604 3880{amount}
'''

def getCharacterSpaceCodeSeven(amount):
    return f'''
MP7 - Character Spaces Give SEVENCHARACTER Coins
C21685B8 00000001
3880{amount} 00000000
'''

def getMinigameCodeSeven(amount):
    return f'''
MP7 - Minigames Award SEVENMINIGAME Coins
2A291558 00000004
2A291558 0000001A
2A291558 0000002B
2A291558 0000002F
2A291558 00000030
2A291558 00000031
2A291558 00000037
2A291558 00000038
28290CCA 0000000A
02290CCA 0000{amount}
E2000001 80008000
2A291558 00000004
2A291558 0000001A
2A291558 0000002B
2A291558 0000002F
2A291558 00000030
2A291558 00000031
2A291558 00000037
2A291558 00000038
28290DDA 0000000A
02290DDA 0000{amount}
E2000001 80008000
2A291558 00000004
2A291558 0000001A
2A291558 0000002B
2A291558 0000002F
2A291558 00000030
2A291558 00000031
2A291558 00000037
2A291558 00000038
28290EEA 0000000A
02290EEA 0000{amount}
E2000001 80008000
2A291558 00000004
2A291558 0000001A
2A291558 0000002B
2A291558 0000002F
2A291558 00000030
2A291558 00000031
2A291558 00000037
2A291558 00000038
28290FFA 0000000A
02290FFA 0000{amount}
E2000001 80008000
'''

def getStarSpaceCodeSeven(amount):
    return f'''
MP7 - Stars Cost SEVENSTAR Coins
04188774 3B80{amount}
204E0640 38030001
044E0644 1C00000A
044E0574 3800{amount} 
044E08D8 3800{amount}
044E09B8 1C00000A
044E0BAC 38A0{amount}
044E0C8C 1C60000A
E2000001 80008000
'''

def getStarSpaceCodeSevenLastFive(amount):
    return f'''
MP7 - Stars Cost SEVENSTLASTFIVE Coins During the Last 5 Turns Event
0418876C 3B80{amount}
'''

def getHammerBroSpaceCodeSeven(amount, negAmount, halfAmount):
    return f'''
MP7 - Hammer Bro Takes SEVENHAMMERBRO Coins
041A902C 3AC0{amount}
041A9A28 38A0{negAmount}
041A973C 38000000
041A9744 3800{halfAmount}
041A974C 38000000
041A9754 3800{halfAmount}
'''

def getZapSpaceCodeSeven(amount):
    return f'''
MP7 - Zap Takes SEVENZAP Coins
C21B652C 00000001
3880{amount} 00000000
'''

def getFlowerSpaceCodeSeven(amount):
    return f'''
MP7 - Flower Gives SEVENFLOWER Coins Per Space
041C4F24 3B40{amount}
'''

def getVacuumSpaceCodeSeven(amount):
    return f'''
MP7 - Vaccum Always Steals SEVENVACUUM Coins
041C8A34 3860{amount}
'''

def getFireballSpaceCodeSeven(amount, negAmount):
    return f'''
MP7 - Fireball Takes SEVENFIREBALL Coins
041C1464 3b80{amount}
041C148C 38A0{negAmount}
'''

def getMinigameReplacement7(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP7 - Minigame Replacement: {gameUno} ➜ {gameDos}
28291558 000000{hexUno}
02291558 000000{hexDos}
E2000001 80008000
'''

def getOrbModsSeven(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW, twentyNineP, twentyNineW):
    return f'''
MP7 - Orb Modifer
042EF588 00050505
042EF58C {oneW}{oneW}{oneW}{oneW}
042EF590 {oneW}{oneW}{oneW}{oneW}
042EF594 {oneW}{oneW}0000
042EF598 01{twoP}{twoP}{twoP}
042EF59C {twoW}{twoW}{twoW}{twoW}
042EF5A0 {twoW}{twoW}{twoW}{twoW}
042EF5A4 {twoW}{twoW}0000
042EF5A8 02{threeP}{threeP}{threeP}
042EF5AC {threeW}{threeW}{threeW}{threeW}
042EF5B0 {threeW}{threeW}{threeW}{threeW}
042EF5B4 {threeW}{threeW}0000
042EF5B8 03{fourP}{fourP}{fourP}
042EF5BC {fourW}{fourW}{fourW}{fourW}
042EF5C0 {fourW}{fourW}{fourW}{fourW}
042EF5C4 {fourW}{fourW}0000
042EF5C8 04{fiveP}{fiveP}{fiveP}
042EF5CC {fiveW}{fiveW}{fiveW}{fiveW}
042EF5D0 {fiveW}{fiveW}{fiveW}{fiveW}
042EF5D4 {fiveW}{fiveW}0000
042EF5D8 05{sixP}{sixP}{sixP}
042EF5DC {sixW}{sixW}{sixW}{sixW}
042EF5E0 {sixW}{sixW}{sixW}{sixW}
042EF5E4 {sixW}{sixW}0000
042EF5E8 06{sevenP}{sevenP}{sevenP}
042EF5EC {sevenW}{sevenW}{sevenW}{sevenW}
042EF5F0 {sevenW}{sevenW}{sevenW}{sevenW}
042EF5F4 {sevenW}{sevenW}0000
042EF5F8 07{eightP}{eightP}{eightP}
042EF5FC {eightW}{eightW}{eightW}{eightW}
042EF600 {eightW}{eightW}{eightW}{eightW}
042EF604 {eightW}{eightW}0000
042EF608 0A{nineP}{nineP}{nineP}
042EF60C {nineW}{nineW}{nineW}{nineW}
042EF610 {nineW}{nineW}{nineW}{nineW}
042EF614 {nineW}{nineW}0000
042EF618 0B{tenP}{tenP}{tenP}
042EF61C {tenW}{tenW}{tenW}{tenW}
042EF620 {tenW}{tenW}{tenW}{tenW}
042EF624 {tenW}{tenW}0000
042EF628 0C{elevenP}{elevenP}{elevenP}
042EF62C {elevenW}{elevenW}{elevenW}{elevenW}
042EF630 {elevenW}{elevenW}{elevenW}{elevenW}
042EF634 {elevenW}{elevenW}0000
042EF638 0D{twelveP}{twelveP}{twelveP}
042EF63C {twelveW}{twelveW}{twelveW}{twelveW}
042EF640 {twelveW}{twelveW}{twelveW}{twelveW}
042EF644 {twelveW}{twelveW}0000
042EF648 0E{thirteenP}{thirteenP}{thirteenP}
042EF64C {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042EF650 {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042EF654 {thirteenW}{thirteenW}0000
042EF658 0F{fourteenP}{fourteenP}{fourteenP}
042EF65C {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042EF660 {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042EF664 {fourteenW}{fourteenW}0000
042EF668 10{fifteenP}{fifteenP}{fifteenP}
042EF66C {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042EF670 {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042EF674 {fifteenW}{fifteenW}0000
042EF678 11{sixteenP}{sixteenP}{sixteenP}
042EF67C {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042EF680 {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042EF684 {sixteenW}{sixteenW}0000
042EF688 14{seventeenP}{seventeenP}{seventeenP}
042EF68C {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042EF690 {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042EF694 {seventeenW}{seventeenW}0000
042EF698 15{eighteenP}{eighteenP}{eighteenP}
042EF69C {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042EF6A0 {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042EF6A4 {eighteenW}{eighteenW}0000
042EF6A8 16{ninteenP}{ninteenP}{ninteenP}
042EF6AC {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042EF6B0 {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042EF6B4 {ninteenW}{ninteenW}0000
042EF6B8 17{twentyP}{twentyP}{twentyP}
042EF6BC {twentyW}{twentyW}{twentyW}{twentyW}
042EF6C0 {twentyW}{twentyW}{twentyW}{twentyW}
042EF6C4 {twentyW}{twentyW}0000
042EF6C8 18{twentyOneP}{twentyOneP}{twentyOneP}
042EF6CC {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042EF6D0 {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042EF6D4 {twentyOneW}{twentyOneW}0000
042EF6D8 19{twentyTwoP}{twentyTwoP}{twentyTwoP}
042EF6DC {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042EF6E0 {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042EF6E4 {twentyTwoW}{twentyTwoW}0000
042EF6E8 1E{twentyThreeP}{twentyThreeP}{twentyThreeP}
042EF6EC {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042EF6F0 {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042EF6F4 {twentyThreeW}{twentyThreeW}0000
042EF6F8 1F{twentyFourP}{twentyFourP}{twentyFourP}
042EF6FC {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042EF700 {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042EF704 {twentyFourW}{twentyFourW}0000
042EF708 20{twentyFiveP}{twentyFiveP}{twentyFiveP}
042EF70C {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042EF710 {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042EF714 {twentyFiveW}{twentyFiveW}0000
042EF718 21{twentySixP}{twentySixP}{twentySixP}
042EF71C {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042EF720 {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042EF724 {twentySixW}{twentySixW}0000
042EF728 22{twentySevenP}{twentySevenP}{twentySevenP}
042EF72C {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042EF730 {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042EF734 {twentySevenW}{twentySevenW}0000
042EF738 23{twentyEightP}{twentyEightP}{twentyEightP}
042EF73C {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042EF740 {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042EF744 {twentyEightW}{twentyEightW}0000
042EF748 28{twentyNineP}{twentyNineP}{twentyNineP}
042EF74C {twentyNineW}{twentyNineW}{twentyNineW}{twentyNineW}
042EF750 {twentyNineW}{twentyNineW}{twentyNineW}{twentyNineW}
042EF754 {twentyNineW}{twentyNineW}0000
042EF758 32000000
042EF75C 00000000
042EF760 00000000
042EF764 00000000
042EF768 33000000
042EF76C 00000000
042EF770 00000000
042EF774 00000000
042EF778 34000000
042EF77C 00000000
042EF780 00000000
042EF784 00000000
042EF788 35000000
042EF78C 00000000
042EF790 00000000
042EF794 00000000
042EF798 FF000000
042EF79C 00000000
042EF7A0 00000000
042EF7A4 00000000
'''

def getInitialItemsSeven(one, two, three, four, five, oneItem, twoItem, threeItem, fourItem, fiveItem):
    return f'''
MP7 - Start with {oneItem}, {twoItem}, and {threeItem}
06003620 00000030
3D808000 618C363C
1C060005 7C005A14
7C8C00AE 98830006
48164338 {one}{two}{three}{four}
{five}{one}{two}{three} {four}{five}{one}{two}
{three}{four}{five}{one} {two}{three}{four}{five}
0416796C 4BE9BCB4
'''

def getSpaceReplaceSeven1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP7 - Replace {spaceName} with {spaceName2} (Slot A)
C217942C 00000005
A01F0030 280000{spaceHex1}
40820018 A09F0032
2804FFFF 4082000C
380000{spaceHex2} B01F0030
60000000 00000000
'''

def getSpaceReplaceSeven2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP7 - Replace {spaceName} with {spaceName2} (Slot B)
C2179430 00000005
280000{spaceHex1} 40820018
A09F0032 2804FFFF
4082000C 380000{spaceHex2}
B01F0030 5404083C
60000000 00000000
'''

def getOtherCodesSeven(code):
    if code == "AdvTxt":
        return '''
04050ddc 60000000'''
    if code == "CtrlOpAlways":
        return '''
0422D890 4800000C'''
    if code == "DisableAdv":
        return '''
204DF310 41820050
044DF310 48000050
E2000001 80008000'''
    if code == "DisableCPU":
        return '''
0419336C 48000018'''
    if code == "Boot":
        return '''
204dd974 2c030000
044dd978 60000000
e2000001 80008000
204e17d0 41820014
044e17d0 60000000
e2000001 80008000
204dffcc 41820014
044dffcc 60000000
e2000001 80008000
204df868 3bde0001
044df868 3bc00db6
e2000001 80008000
204e879c 41820014
044e879c 60000000
e2000001 80008000'''
    if code == "BSpeed":
        return '''
04160ad8 38030002
041604b0 38c0000a
204e317c 281e000c
044e2f08 3bde0002
044e3178 3bde0002
044e31ec 3bde0002
044e344c 3bde0002
044e3844 3bde0002
e2000001 80008000'''
    if code == "OSpeed":
        return '''
041e3110 38030002'''
    if code == "Taunt":
        return '''
04235abc 60000000
04235b0c 60000000
04235b90 60000000'''
    if code == "TxtDisplay":
        return '''
04050a70 38800000'''
    if code == "ShowCtrl":
        return '''
c2047400 00000002
807f0050 906d0000
38600000 00000000
c20402fc 0000000c
3860012c 3880000a
38a0002d 38c00028
38e000ff 90ed0004
38ed0004 3d008000
6108ca28 7d0903a6
4e800421 3860012c
3880000a 3ca08025
38a548ef 80cd0000
38c60001 c0228388
3ce08000 60e7c8cc
7ce903a6 4e800421
57a0083c 00000000
C219965C 00000006
38DE0001 C02280E0
38600138 38800010
3CA08025 60A548EF
3CE08000 60E7C8CC
7CE903A6 4E800421
57C0083C 00000000'''
    if code == "UnlockAll":
        return '''
0403EDC0 38600001
82200001 802922F8
86200001 00000006
84200001 802922F8
82200001 802922F8
86200001 00000008
84200001 802922F8
82200001 802922F8
86200001 00000040
84200001 802922F8
82200001 802922FC
86200001 00040000
84200001 802922FC
204E1B7C 3C608051
044E1B88 38600001
044E1B8C 98640002
044E1B90 60000000
E2000001 80008000
204F6C64 4182001C
044F6C64 60000000
044E9AFC 60000000
E2000001 80008000
204E8A28 3CC08050
C24E8A34 00000002
38A00002 98A40000
88A40000 00000000
E2000001 80008000
204F0BC4 2C030000
044F0BC0 38600001
044F0C4C 38600001
044F0CD8 38600001
044F0CFC 38600001
044F0D18 38600001
E2000001 80008000
04235ABC 60000000
04235B0C 60000000
04235B90 60000000
022922F8 0003FFFF
04235B74 60000000'''
    