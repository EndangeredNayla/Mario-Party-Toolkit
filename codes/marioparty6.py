# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/15/2024
# License: MIT
# ============================================

def getBlueSpaceCodeSix(amount):
    return f'''
MP6 - Blue Spaces Give SIXBLUE Coins
0415F1E8 3880{amount}
'''

def getRedSpaceCodeSix(amount):
    return f'''
MP6 - Red Spaces Take Away SIXRED Coins
0415F278 3880{amount}
'''

def getMinigameCodeSix(amount):
    return f'''
MP6 - Minigames Award SIXMINIGAME Coins
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

def getCharacterSpaceCodeSix(amount):
    return f'''
MP6 - Character Spaces Give SIXCHARACTER Coins
0415F230 3880{amount}
'''

def getStarSpaceCodeSix(amount, negAmount):
    return f'''
MP6 - Stars Cost SIXSTAR Coins
0418333C 2C03{amount}
0418342C 2C03{amount}
041834C4 2C03{amount}
0415F668 2C03{amount}
0415FA18 3880{negAmount}
0416068C 2C00{amount}
04160D0C 3880{negAmount}    
C2183590 00000002
3880{negAmount} 7C8400D0
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

def getPinkBooSpaceCodeSix(amount, negAmount):
    return f'''
MP6 - Stars Cost SIXBOOSTARS Coins when stealing with Pink Boo
C21B1FB4 00000001
2C04{amount} 00000000
C21B2634 00000001
3880{negAmount} 00000000
'''

def getPinkBooCoinsSpaceCodeSix(amount, negAmount):
    return f'''
MP6 - Coins Cost SIXBOOCOINS Coins when stealing with Pink Boo
C21B1F28 00000001
2C03{amount} 00000000
C21B2626 00000001
3880{negAmount} 00000000
'''

def getMinigameReplacement6(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP6 - Minigame Replacement: {gameUno} ➜ {gameDos}
28265BA8 000000{hexUno}
0222A4C4 000000{hexDos}
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