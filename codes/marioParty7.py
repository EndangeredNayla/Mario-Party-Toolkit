# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Blue Spaces Give {amountDec} Coins
04168578 60000000
0416857C 3880{amount}
'''

def getRedSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Red Spaces Take Away {amountDec} Coins
04168600 60000000
04168604 3880{amount}
'''

def getCharacterSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Character Spaces Give {amountDec} Coins
C21685B8 00000001
3880{amount} 00000000
'''

def getMinigameCodeSeven(amount, amountDec):
    return f'''
MP7 - Minigames Award {amountDec} Coins
C20098A4 00000012
3DC08029 61CE1559
89EE0000 2C0F0004
41820068 2C0F001A
41820060 2C0F002B
41820058 2C0F002F
41820050 2C0F0030
41820048 2C0F0031
41820040 2C0F0037
41820038 2C0F0038
41820030 3DC08029
61CE0CCA A1EE0000
2C0F0000 4182000C
39E0{amount} B1EE0000
39CE0110 3A100001
2C100003 4081FFE0
3800FFFF 39C00000
39E00000 3A000000
60000000 00000000
'''

def getStarSpaceCodeSeven(amount, amountDec, x2, x3, x4):
    return f'''
MP7 - Stars Cost {amountDec} Coins
04188774 3B80{amount}
204E0640 38030001
044E0644 1C00000A
044E0574 3800{amount} 
044E08D8 3800{amount}
044E09B8 1C00000A
044E0BAC 38A0{amount}
044E0C8C 1C60000A
E2000001 80008000
204F92AC 804F929D
044F9268 0000{amount}
044F926C 0000{x2}
044F9270 0000{x3}
044F9274 0000{x4}
E2000001 80008000
'''

def getStarSpaceCodeSevenLastFive(amount, amountDec):
    return f'''
MP7 - Stars Cost {amountDec} Coins During the Last 5 Turns Event
0418876C 3B80{amount}
'''

def getHammerBroSpaceCodeSeven(amount, negAmount, halfAmount, amountDec):
    return f'''
MP7 - Hammer Bro Takes {amountDec} Coins
041A902C 3AC0{amount}
041A9A28 38A0{negAmount}
041A973C 38000000
041A9744 3800{halfAmount}
041A974C 38000000
041A9754 3800{halfAmount}
'''

def getZapSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Zap Takes {amountDec} Coins
C21B652C 00000001
3880{amount} 00000000
'''

def getFlowerSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Flower Gives {amountDec} Coins Per Space
041C4F24 3B40{amount}
'''

def getVacuumSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Vaccum Always Steals {amountDec} Coins
041C8A34 3860{amount}
'''

def getFireballSpaceCodeSeven(amount, negAmount, amountDec):
    return f'''
MP7 - Fireball Takes {amountDec} Coins
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

def getOrbModsSeven(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW, twentyNineP, twentyNineW, thirtyP, thirtyW, thirtyOneP, thirtyOneW, thirtyTwoP, thirtyTwoW, thirtyThreeP, thirtyThreeW, thirtyFourP, thirtyFourW):
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
042EF758 32{thirtyFourP}{thirtyFourP}{thirtyFourP}
042EF75C {thirtyFourW}{thirtyFourW}{thirtyFourW}{thirtyFourW}
042EF760 {thirtyFourW}{thirtyFourW}{thirtyFourW}{thirtyFourW}
042EF764 {thirtyFourW}{thirtyFourW}0000
042EF768 08{thirtyTwoP}{thirtyTwoP}{thirtyTwoP}
042EF76C {thirtyTwoW}{thirtyTwoW}{thirtyTwoW}{thirtyTwoW}
042EF770 {thirtyTwoW}{thirtyTwoW}{thirtyTwoW}{thirtyTwoW}
042EF774 {thirtyTwoW}{thirtyTwoW}0000
042EF778 09{thirtyOneP}{thirtyOneP}{thirtyOneP}
042EF78C {thirtyOneW}{thirtyOneW}{thirtyOneW}{thirtyOneW}
042EF790 {thirtyOneW}{thirtyOneW}{thirtyOneW}{thirtyOneW}
042EF794 {thirtyOneW}{thirtyOneW}0000
042EF798 33{thirtyP}{thirtyP}{thirtyP}
042EF79C {thirtyW}{thirtyW}{thirtyW}{thirtyW}
042EF7A0 {thirtyW}{thirtyW}{thirtyW}{thirtyW}
042EF7A4 {thirtyW}{thirtyW}0000
042EF7A8 35{thirtyThreeP}{thirtyThreeP}{thirtyThreeP}
042EF7AC {thirtyThreeW}{thirtyThreeW}{thirtyThreeW}{thirtyThreeW}
042EF7B0 {thirtyThreeW}{thirtyThreeW}{thirtyThreeW}{thirtyThreeW}
042EF7B4 {thirtyThreeW}{thirtyThreeW}0000
042EF7B8 FF000000
042EF7BC 00000000
042EF7C0 00000000
042EF7C4 00000000
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

def getWindmillMaxSeven(amount, amountDec):
    return f'''
MP7 - Windmillville: Invest Up To {amountDec}
204E4C7C 2C040064
044E4C7C 2C04{amount}
E2000001 80008000
204E4CCC 2C040064
044E4CCC 2C04{amount}
E2000001 80008000
'''

def getStarHandicap(p1, p2, p3, p4):
    return f'''
MP7 - Star Handicap
20290CC4 00000000
02290CD0 0000{p1}
02290DE0 0000{p2}
02290EF0 0000{p3}
02291000 0000{p4}
E2000001 80008000
'''

def getSpinxEvent(a, b):
    return f'''
MP7 - Pyramid Park: Spinx Event is Always {b}
282F2F3E 0000007C
28290CA8 0000004D
28291522 00000023
0052449F 000000{a}
E2000002 80008000
28290DB8 0000004D
28291522 00000123
0052449F 000000{a}
E2000002 80008000
28290EC8 0000004D
28291522 00000223
0052449F 000000{a}
E2000002 80008000
28290FD8 0000004D
28291522 00000323
0052449F 000000{a}
E2000003 80008000
'''

def getGliderEvent(a, b):
    return f'''
MP7 - Windmillvlle: Flower Glider Always Goes To
282F2F3E 0000007E
28290CA8 00000031
28291522 0000001A
026370B2 000000{a}
E2000002 80008000
28290DB8 00000031
28291522 0000011A
026370B2 000000{a}
E2000002 80008000
28290EC8 00000031
28291522 0000021A
026370B2 000000{a}
E2000002 80008000
28290FD8 00000031
28291522 0000031A
026370B2 000000{a}
E2000003 80008000
'''

def getGliderCostEvent(a, b, c):
    return f'''
MP7 - Windmillville: Flower Glider Costs {c}
282F2F3E 0000007E
284E73AE 0000000A
024E73AE 0000{a}
E2000001 80008000
284E7D12 0000FFF6
024E7D12 0000{b}
E2000002 80008000
'''

def getBlackChomp(a, b):
    return f'''
MP7 - Pyramid Park: Standard Chomp Costs {b}
282F2F3E 0000007C
28511722 0000000A
02511722 0000{a}
E2000002 80008000
'''

def getRedChomp(a, b):
    return f'''
MP7 - Pyramid Park: Red Chomp Costs {b}
282F2F3E 0000007C
28511726 0000000A
02511726 0000{a}
E2000002 80008000
'''

def initialCoinsMod7(hex, hexDec):
    return f'''
MP7 - Gain {hexDec} Coins at the Start of the Game
02196D12 0000{hex}
02151DEB 0000{hex}
'''
