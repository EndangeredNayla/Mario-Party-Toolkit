# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/15/2024
# License: MIT
# ============================================

def getBlueSpaceCodeOne(amount, switch):
    return f'''
MP1 - Blue Spaces Give ONEBLUE Coins: ONEBLUESWITCH
81057D80 3408
81057D82 000{switch}
81057D84 1100
81057D86 0003
81057D88 3410
81057D8A {amount}
81057D8C 5440
81057D8E 0001
81057D90 0010
81057D92 8040
0407FBE0 3BC0
'''

def getRedSpaceCodeOne(amount, switch):
    return f'''
MP1 - Red Spaces Take Away ONERED Coins: ONEREDSWITCH
81057DD8 3408
81057DDA 000{switch}
81057DDC 1100
81057DDE 0003
81057DE0 3410
81057DE2 {amount}
81057DE4 5440
81057DE6 0001
81057DE8 0010
81057DEA 8040
'''

def getMinigameReplacement1(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP1 - Minigame Replacement: {gameUno} -> {gameDos}
D10ED5DE 00{hexUno}
810ED5DE 00{hexDos}		
'''

def getBlueSpaceCodeTwo(amount, switch):
    return f'''
MP2 - Blue Spaces Give TWOBLUE Coins: TWOBLUESWITCH
81066300 3408
81066302 000{switch}
81066304 1100
81066306 0003
81066308 3410
8106630A {amount}
8106630C 5440
8106630E 0001
81066310 0010
81066312 8040
'''

def getRedSpaceCodeTwo(amount, switch):
    return f'''
MP2 - Red Spaces Take Away TWORED Coins: TWOREDSWITCH
8106634C 3408
8106634E 000{switch}
81066350 1100
81066352 0003
81066354 3410
81066356 {amount}
81066358 5440
8106635A 0001
8106635C 0010
8106635E 8040
'''

def getMinigameReplacement2(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP2 - Minigame Replacement: {gameUno} -> {gameDos}
D00F93C9 00{hexUno}
800F93C9 00{hexDos}		
'''

def getBlueSpaceCodeThree(amount, switch):
    return f'''
MP3 - Blue Spaces Give THREEBLUE Coins: THREEBLUESWITCH
810FE284 3408
810FE286 000{switch}
810FE288 1100
810FE28A 0003
810FE28C 3410
810FE28E {amount}
810FE290 5440
810FE292 0001
810FE294 0010
810FE296 8040
'''

def getRedSpaceCodeThree(amount, switch):
    return f'''
MP3 - Red Spaces Take Away THREERED Coins: THREEREDSWITCH
810FE2C0 3408
810FE2C2 000{switch}
810FE2C4 1100
810FE2C6 0003
810FE2C8 3410
810FE2CA {amount}
810FE2CC 5440
810FE2CE 0001
810FE2D0 0010
810FE2D2 8040
'''

def getStarSpaceCodeThree(amount, negAmount):
    return f'''
MP3 - Stars Cost THREESTAR Coins
D10CE202 0048
8110A61A {amount}
D10CE202 0048
8110A6BE {negAmount}
D10CE202 0048
8110A6CA {negAmount}
D10CE202 0049
8110A17E {amount}
D10CE202 0049
8110A222 {negAmount}
D10CE202 0049
8110A22E {negAmount}
D10CE202 004A
8110AF16 {amount}
D10CE202 004A
8110A4F2 {negAmount}
D10CE202 004A
8110A4FE {negAmount}
D10CE202 004B
8110A1BA {amount}
D10CE202 004B
8110A25E {negAmount}
D10CE202 004B
8110A26A {negAmount}
D10CE202 004C
81109BC2 {amount}
D10CE202 004C
81109C66 {negAmount}
D10CE202 004C
81109C72 {negAmount}
D10CE202 004D
8110B9AA {amount}
D10CE202 004D
8110BA4E {negAmount}
D10CE202 004D
8110BA5A {negAmount}
'''

def getKoopaBankCodeThree(amount, negAmount):
    return f'''
MP3 - Koopa Bank Deposits are THREEKOOPA Coins
D10CE202 0048
8110AE3E {amount}
D10CE202 0048
8110AFB6 {amount}
D10CE202 0048
8110AFE6 {amount}
D10CE202 0048
8110AFFA {negAmount}
D10CE202 0048
8110B002 {negAmount}
D10CE202 0049
8110A9AA {amount}
D10CE202 0049
8110AB22 {amount}
D10CE202 0049
8110AB52 {amount}
D10CE202 0049
8110AB66 {negAmount}
D10CE202 0049
8110AB6E {negAmount}
D10CE202 004A
8110AF16 {amount}
D10CE202 004A
8110B08E {amount}
D10CE202 004A
8110B0BE {amount}
D10CE202 004A
8110B0D2 {negAmount}
D10CE202 004A
8110B0DA {negAmount}
D10CE202 004B
8110A9DE {amount}
D10CE202 004B
8110AB56 {amount}
D10CE202 004B
8110AB86 {amount}
D10CE202 004B
8110AB9A {negAmount}
D10CE202 004B
8110ABA2 {negAmount}
D10CE202 004C
8110A3EE {amount}
D10CE202 004C
8110A566 {amount}
D10CE202 004C
8110A596 {amount}
D10CE202 004C
8110A5AA {negAmount}
D10CE202 004C
8110A5B2 {negAmount}
D10CE202 004D
8110C1CE {amount}
D10CE202 004D
8110C346 {amount}
D10CE202 004D
8110C376 {amount}
D10CE202 004D
8110C38A {negAmount}
D10CE202 004D
8110C392 {negAmount}
'''

def getMinigameReplacement3(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP3 - Minigame Replacement: {gameUno} -> {gameDos}
D00CD068 00{hexUno}
800CD068 00{hexDos}			
'''

def getRedSpaceCodeFour(amount):
    return f'''
MP4 - Red Spaces Take Away FOURRED Coins
0407FD74 60000000
0407FD78 3BC0{amount}
'''

def getBlueSpaceCodeFour(amount):
    return f'''
MP4 - Blue Spaces Give FOURBLUE Coins
0407FBDC 60000000
0407FBE0 3BC0{amount}
'''

def getMinigameCodeFour(amount):
    return f'''
MP4 - Minigames Award FOURMINIGAME Coins
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FC60 0000000A
0218FC60 0000{amount}
E2000001 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FC90 0000000A
0218FC90 0000{amount}
E2000001 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FCC0 0000000A
0218FCC0 0000{amount}
E2000001 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FCF0 0000000A
0218FCF0 0000{amount}
E2000001 80008000
'''

def getBooSpaceCodeFour(amount):
    return f'''
MP4 - Stars Cost FOURBOOSTARS Coins when stealing at the Boo House
040A5F30 2C1E{amount}
'''

def getBooSpaceCoinsCodeFour(amount):
    return f'''
MP4 - Coins Cost FOURBOOCOINS Coins when stealing at the Boo House
040A61DC 2C1E{amount}
040A517C 2C03{amount}
'''

def getStarSpaceCodeFour(amount):
    return f'''
MP4 - Stars Cost FOURSTAR Coins
040843CC 2C03{amount}
04084590 2C03{amount}
040845CC 2C03{amount}
0408473C 2C1C{amount}
'''

def getSquishCodeFour(amount):
    return f'''
MP4 - Mega Mushroom Steals FOURSQUISH Coins
0406BE70 3860{amount}
0406BEAC 3860{amount}
0406BE1C 3860{amount}
'''

def getLotterySpaceCodeFour(amount):
    return f'''
MP4 - Lottery Costs FOURLOTTERY Coins
0407BD20 2C1E{amount}
'''

def getMinigameReplacement4(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP4 - Minigame Replacement: {gameUno} ➜ {gameDos}
2818FD2C 000000{hexUno}
0218FD2C 000000{hexDos}
E2000001 80008000
'''

def getBlueSpaceCodeFive(amount):
    return f'''
MP5 - Blue Spaces Give FIVEBLUE Coins
040A9F5C 3880{amount}
'''

def getRedSpaceCodeFive(amount):
    return f'''
MP5 - Red Spaces Take Away FIVERED Coins
040AA160 3880{amount}
'''

def getMinigameCodeFive(amount):
    return f'''
MP5 - Minigames Award FIVEMINIGAME Coins
2A22A4C4 0000000F
2A22A4C4 00000017
2A22A4C4 00000022
2A22A4C4 00000023
2A22A4C4 00000024
2A22A4C4 00000025
2A22A4C4 00000026
2A22A4C4 00000027
2A22A4C4 00000044
2A22A4C4 0000004A
2822A09C 0000000A
0222A09C 0000{amount}
E2000001 80008000
2A22A4C4 0000000F
2A22A4C4 00000017
2A22A4C4 00000022
2A22A4C4 00000023
2A22A4C4 00000024
2A22A4C4 00000025
2A22A4C4 00000026
2A22A4C4 00000027
2A22A4C4 00000044
2A22A4C4 0000004A
2822A1A4 0000000A
0222A1A4 0000{amount}
E2000001 80008000
2A22A4C4 0000000F
2A22A4C4 00000017
2A22A4C4 00000022
2A22A4C4 00000023
2A22A4C4 00000024
2A22A4C4 00000025
2A22A4C4 00000026
2A22A4C4 00000027
2A22A4C4 00000044
2A22A4C4 0000004A
2822A2AC 0000000A
0222A2AC 0000{amount}
E2000001 80008000
2A22A4C4 0000000F
2A22A4C4 00000017
2A22A4C4 00000022
2A22A4C4 00000023
2A22A4C4 00000024
2A22A4C4 00000025
2A22A4C4 00000026
2A22A4C4 00000027
2A22A4C4 00000044
2A22A4C4 0000004A
2822A3B4 0000000A
0222A3B4 0000{amount}
E2000001 80008000
'''

def getStarSpaceCodeFive(amount, negAmount):
    return f'''
MP5 - Stars Cost FIVESTAR Coins
C20AFDB0 00000001
2C03{amount} 00000000
C20AFF9C 00000001
3880{negAmount} 00000000
'''


def getWigglerSpaceCodeFive(amount, negAmount):
    return f'''
MP5 - Stars Cost FIVEWIGGLER Coins from Wiggler
C20DB528 00000001
2C03{amount} 00000000
C20DBB40 00000001
3880{negAmount} 00000000
'''

def getChompSpaceCodeFive(amount, negAmount):
    return f'''
MP5 - Stars Cost FIVECHOMP Coins when stealing with Chain Chomp
C20F5F34 00000001
2C03{amount} 00000000
C20F630C 00000001
3880{negAmount} 00000000
'''

def getMinigameReplacement5(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP5 - Minigame Replacement: {gameUno} ➜ {gameDos}
2822A4C4 000000{hexUno}
0222A4C4 000000{hexDos}
E2000001 80008000
'''

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
2C04{amount} 00000000
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

def getBlueSpaceCodeEight(amount):
    return f'''
MP8 - Blue Spaces Give EIGHTBLUE Coins
2046CB88 38A00003
0446CB88 38A0{amount}
E0000000 80008000
2046CB8C 38C00003
0446CB8C 38C0{amount}
E0000000 80008000
20477C9C 38A00003
04477C9C 38A0{amount}
E0000000 80008000
20477CA0 38C00003
04477CA0 38C0{amount}
E0000000 80008000
204715CC 38A00003
044715CC 38A0{amount}
E0000000 80008000
204715D0 38C00003
044715D0 38C0{amount}
E0000000 80008000
204940A8 38A00003
044940A8 38A0{amount}
E0000000 80008000
204940AC 38C00003
044940AC 38C0{amount}
E0000000 80008000
2046F030 38A00003
0446F030 38A0{amount}
E0000000 80008000
2046F034 38C00003
0446F034 38C0{amount}
E0000000 80008000
20474964 38A00003
04474964 38A0{amount}
E0000000 80008000
20474968 38C00003
04474968 38C0{amount}
E0000000 80008000
'''

def getRedSpaceCodeEight(amount):
    return f'''
MP8 - Red Spaces Take Away EIGHTRED Coins
2046CEC4 38A0FFFD
0446CEC4 38A0{amount}
E0000000 80008000
2046CEC8 38C0FFFD
0446CEC8 38C0{amount}
E0000000 80008000
20477FD8 38A0FFFD
04477FD8 38A0{amount}
E0000000 80008000
20477FDC 38C0FFFD
04477FDC 38C0{amount}
E0000000 80008000
20471908 38A0FFFD
04471908 38A0{amount}
E0000000 80008000
2047190C 38C0FFFD
0447190C 38C0{amount}
E0000000 80008000
204943E4 38A0FFFD
044943E4 38A0{amount}
E0000000 80008000
204943E8 38C0FFFD
044943E8 38C0{amount}
E0000000 80008000
2046F36C 38A0FFFD
0446F36C 38A0{amount}
E0000000 80008000
2046F370 38C0FFFD
0446F370 38C0{amount}
E0000000 80008000
20474CA0 38A0FFFD
04474CA0 38A0{amount}
E0000000 80008000
20474CA4 38C0FFFD
04474CA4 38C0{amount}
E0000000 80008000
'''

def getBlueSpaceCodeEightGC(amount):
    return f'''
MP8 - Blue Spaces Give EIGHTBLUEGC Coins
2045ADE8 38A00003
0445ADE8 38A0{amount}
E0000000 80008000
2045ADEC 38C00003
0445ADEC 38C0{amount}
E0000000 80008000
20465EFC 38A00003
04465EFC 38A0{amount}
E0000000 80008000
20465F00 38C00003
04465F00 38C0{amount}
E0000000 80008000
2045F82C 38A00003
0445F82C 38A0{amount}
E0000000 80008000
2045F830 38C00003
0445F830 38C0{amount}
E0000000 80008000
20482308 38A00003
04482308 38A0{amount}
E0000000 80008000
204940AC 38C00003
044940AC 38C0{amount}
E0000000 80008000
2045D290 38A00003
0445D290 38A0{amount}
E0000000 80008000
2045D294 38C00003
0445D294 38C0{amount}
E0000000 80008000
20462BC4 38A00003
04462BC4 38A0{amount}
E0000000 80008000
20462BC8 38C00003
04462BC8 38C0{amount}
E0000000 80008000
'''

def getRedSpaceCodeEightGC(amount):
    return f'''
MP8 - Red Spaces Take Away EIGHTREDGC Coins
2045B124 38A0FFFD
0445B124 38A0{amount}
E0000000 80008000
2045B128 38C0FFFD
0445B128 38C0{amount}
E0000000 80008000
20477FD8 38A0FFFD
04477FD8 38A0{amount}
E0000000 80008000
20477FDC 38C0FFFD
04477FDC 38C0{amount}
E0000000 80008000
2045FB68 38A0FFFD
0445FB68 38A0{amount}
E0000000 80008000
2045FB6C 38C0FFFD
0445FB6C 38C0{amount}
E0000000 80008000
20482644 38A0FFFD
04482644 38A0{amount}
E0000000 80008000
20482648 38C0FFFD
04482648 38C0{amount}
E0000000 80008000
2045D5CC 38A0FFFD
0445D5CC 38A0{amount}
E0000000 80008000
2045D5D0 38C0FFFD
0445D5D0 38C0{amount}
E0000000 80008000
20462F00 38A0FFFD
04462F00 38A0{amount}
E0000000 80008000
20462F04 38C0FFFD
04462F04 38C0{amount}
E0000000 80008000
'''

def getMinigameCodeEight2(amount):
    return f'''
MP8 - Minigames Award EIGHTMINIGAMEGC Coins
2A2287CC 00000002
2A2287CC 0000000Dß
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
2822832A 0000000A
0222832A 0000{amount}
E2000001 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228443 0000000A
02228443 0000{amount}
E2000001 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
2822855B 0000000A
0222855B 0000{amount}
E2000001 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228673 0000000A
02228673 0000{amount}
E2000001 80008000
2A2287CC 00000002
2A2287CC 0000000D
2A2287CC 00000010
2A2287CC 0000001B
2A2287CC 00000024
2A2287CC 00000025
2A2287CC 00000026
2A2287CC 00000027
28228526 0000000A
02228526 0000{amount}
E2000001 80008000
'''

def getStarSpaceCodeEight(amount, negAmount):
    return f'''
MP8 - Stars Cost EIGHTSTAR Coins
203D7120 38600014
043D7120 3860{amount}
E0000000 80008000
20404B58 2C03000A
04404B58 2C03{amount}
E0000000 80008000
20404C64 38A0FFF6
04404C64 38A0{negAmount}
E0000000 80008000
203E320C 38A0FFEC
043E320C 38A0{negAmount}
E0000000 80008000
203E3210 38C0FFEC
043E3210 38C0{negAmount}
E0000000 80008000
203E3108 2C030014
043E3108 2C03{amount}
E0000000 80008000
'''

def getStarSpaceCodeEightGC(amount, negAmount):
    return f'''
MP8 - Stars Cost EIGHTSTARGC Coins
203C5380 38600014
043C5380 3860{amount}
E0000000 80008000
203F2DB8 2C03000A
043F2DB8 2C03{amount}
E0000000 80008000
203F2EC4 38A0FFF6
043F2EC4 38A0{negAmount}
E0000000 80008000
203D146C 38A0FFEC
043D146C 38A0{negAmount}
E0000000 80008000
203D1470 38C0FFEC
043D1470 38C0{negAmount}
E0000000 80008000
203D1368 2C030014
043D1368 2C03{amount}
E0000000 80008000
'''

def getItemModsFour(oneP, oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, minCoins):
    return f'''
MP4 - Item Modifer
C2083878 0000001E
48000045 60000000
00{oneW}0000 00{twoW}0001  
00{threeW}0002 00{fourW}0003
00{fiveW}0004 00{sixW}0005
00{sevenW}0006 00{eightW}0007
00{nineW}0008 00{tenW}0009
00{elevenW}000A 00{twelveW}000B
00{thirteenW}000C 00{fourteenW}000D
00000000 7CE802A6
38E70004 38600000
38800000 2C030038
41820014 7CA71A2E
7C842A14 38630004
4BFFFFEC 3CA08005
60A5FB40 7CA903A6
7C832378 4E800421
38800000 38A00000
2C050034 41820024
7CC72A2E 7C661850
2C030000 40A00008
48000010 38840001
38A50004 4BFFFFDC
1C840004 38840002
7C87222E 3CA0817F
60A5FFF0 90850000
2C040008 41800008
38840001 3CA00007
60A5006D 7C642A14
38800000 38A00000
38A00000 00000000
C2083028 00000041
480001B1 0B596F75
10676F74 1061101E
054D696E 69104D75
7368726F 6F6D1E08
85FF000B 596F7510
676F7410 61101E05
4D656761 104D7573
68726F6F 6D1E0885
FF000B59 6F751067
6F741061 101E0553
75706572 104D696E
69104D75 7368726F
6F6D1E08 85FF000B
596F7510 676F7410
61101E05 53757065
72104D65 6761104D
75736872 6F6F6D1E
0885FF00 0B596F75
10676F74 1061101E
054D696E 69104D65
67611048 616D6D65
721E0885 FF000B59
6F751067 6F741061
101E0557 61727010
50697065 1E0885FF
000B596F 7510676F
74106110 1E055377
61701043 6172641E
0885FF00 0B596F75
10676F74 1061101E
05537061 726B7910
53746963 6B65721E
0885FF00 0B596F75
10676F74 1061101E
05476164 646C6967
68741E08 85FF000B
596F7510 676F7410
61101E05 43686F6D
70104361 6C6C1E08
85FF000B 596F7510
676F7410 61101E05
426F7773 65721053
7569741E 0885FF00
0B596F75 10676F74
1061101E 04437279
7374616C 1042616C
6C1E0885 FF000B59
6F751067 6F741061
101E074D 61676963
104C616D 701E0885
FF000B59 6F751067
6F741061 6E101E07
4974656D 10426167
1E0885FF 00000000
7C6802A6 3C80817F
6084FFF0 80840000
38A00000 38C00000
7CE518AE 2C070000
40A20020 7C062000
41820020 7C632A14
38630001 38C60001
38A00000 4BFFFFDC
38A50001 4BFFFFD4
7C641B78 38600000
60000000 00000000
C2083CF0 00000002
3C80817F 6084FFF0
80840000 00000000
00139D2C 000000{oneP} 
00139D2D 000000{twoP} 
00139D2E 000000{threeP} 
00139D2F 000000{fourP}
00139D30 000000{fiveP} 
00139D31 000000{sixP} 
00139D32 000000{sevenP} 
00139D33 000000{eightP} 
00139D34 000000{nineP} 
00139D35 000000{tenP} 
00139D36 000000{elevenP} 
00139D37 000000{twelveP} 
00139D38 000000{thirteenP}
00139D39 000000{fourteenP}
02139DB2 0000{oneW}{twoW}
02139DB4 0000{threeW}{fourW}
02139DB6 0000{fiveW}{sixW}
02139DB8 0000{sevenW}{eightW}
02139DBA 0000{nineW}{tenW}
02139DBC 0000{elevenW}{twelveW}
02139DBE 0000{thirteenW}{fourteenW}
02139DC0 0000{oneW}{twoW}
02139DC2 0000{threeW}{fourW}
02139DC4 0000{fiveW}{sixW}
02139DC6 0000{sevenW}{eightW}
02139DC8 0000{nineW}{tenW}
02139DCA 0000{elevenW}{twelveW}
02139DCC 0000{thirteenW}{fourteenW}
02139DCE 0000{oneW}{twoW}
02139DD0 0000{threeW}{fourW}
02139DD2 0000{fiveW}{sixW}
02139DD4 0000{sevenW}{eightW}
02139DD6 0000{nineW}{tenW}
02139DD8 0000{elevenW}{twelveW}
02139DDA 0000{thirteenW}{fourteenW}
02139DDC 0000{oneW}{twoW}
02139DDE 0000{threeW}{fourW} 
02139DE0 0000{fiveW}{sixW}
02139DE2 0000{sevenW}{eightW} 
02139DE4 0000{nineW}{tenW}
02139DE6 0000{elevenW}{twelveW}
02139DE8 0000{thirteenW}{fourteenW}
02139DEA 0000{oneW}{twoW}
02139DEC 0000{threeW}{fourW}
02139DEE 0000{fiveW}{sixW} 
02139DF0 0000{sevenW}{eightW}
02139DF2 0000{nineW}{tenW}
02139DF4 0000{elevenW}{twelveW}
02139DF6 0000{thirteenW}{fourteenW}
02139DF8 0000{oneW}{twoW}
02139DFA 0000{threeW}{fourW}
02139DFC 0000{fiveW}{sixW}
02139DFE 0000{sevenW}{eightW}
02139E00 0000{nineW}{tenW}
02139E02 0000{elevenW}{twelveW}
02139E04 0000{thirteenW}{fourteenW}
02139E06 0000{oneW}{twoW}
02139E08 0000{threeW}{fourW}
02139E0A 0000{fiveW}{sixW}
02139E0c 0000{sevenW}{eightW}
02139E0E 0000{nineW}{tenW}
02139E10 0000{elevenW}{twelveW}
02139E12 0000{thirteenW}{fourteenW}
02139E14 0000{oneW}{twoW}
02139E16 0000{threeW}{fourW}
02139E18 0000{fiveW}{sixW}
02139E1A 0000{sevenW}{eightW}
02139E1C 0000{nineW}{tenW}
02139E1E 0000{elevenW}{twelveW}
02139E20 0000{thirteenW}{fourteenW}
02139E22 0000{oneW}{twoW}
02139E24 0000{threeW}{fourW}
02139E26 0000{fiveW}{sixW}
02139E28 0000{sevenW}{eightW}
02139E2A 0000{nineW}{tenW}
02139E2C 0000{elevenW}{twelveW}
02139E2E 0000{thirteenW}{fourteenW}
02139E30 0000{oneW}{twoW}
02139E32 0000{threeW}{fourW}
02139E34 0000{fiveW}{sixW}
02139E36 0000{sevenW}{eightW}
02139E38 0000{nineW}{tenW}
02139E3A 0000{elevenW}{twelveW}
02139E3C 0000{thirteenW}{fourteenW}
C2077D84 00000001
2C03{minCoins} 00000000
'''

def getCapsuleModsFive(oneP, oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW, twentyNineP, twentyNineW):
    return f'''
C20C8FA0 00000024
9421FFF0 7C0802A6
90010014 93E10000
48000081 60000000
00{oneW}0005 00{twoW}0100
00{threeW}0200 00{fourW}0300
00{fiveW}0400 00{sixW}0500
00{sevenW}0605 00{eightW}0A00
00{nineW}0B00 00{tenW}0C00
00{elevenW}0D00 00{twelveW}0E00
00{thirteenW}0F00 00{fourteenW}1000
00{fifteenW}1100 00{sixteenW}1400
00{seventeenW}1500 00{eighteenW}1600
00{ninteenW}1700 00{twentyW}1800
00{twentyOneW}1900 00{twentyTwoW}1E00
00{twentyThreeW}1F00 00{twentyFourW}2000
00{twentyFiveW}2100 00{twentySixW}2200
00{twentySevenW}2300 00{twentyEightW}2400
00{twentyNineW}2500 00000000
7CE802A6 38E70004
38600000 38800000
2C030074 41820014
7CA71A2E 7C842A14
38630004 4BFFFFEC
3CA08003 60A5B0F4
7CA903A6 7C832378
4E800421 38800000
38A00000 2C050074
41820024 7CC72A2E
7C661850 2C030000
40A00008 48000010
38840001 38A50004
4BFFFFDC 1C840004
38840002 7C6720AE
83E10000 80010014
7C0803A6 38210010
4E800020 00000000
001CA233 000000{oneP}
001CA249 000000{twoP}
001CA26B 000000{threeP}
001CA287 000000{fourP}
001CA2A3 000000{fiveP}
001CA2CF 000000{sixP}
001CA2DB 000000{sevenP}
001CA34B 000000{eightP}
001CA367 000000{nineP}
001CA383 000000{tenP}
001CA39F 000000{elevenP}
001CA3BB 000000{twelveP}
001CA3D7 000000{thirteenP}
001CA3F3 000000{fourteenP}
001CA40F 000000{fifteenP}
001CA463 000000{sixteenP}
001CA47F 000000{seventeenP}
001CA49B 000000{eighteenP}
001CA4B7 000000{ninteenP}
001CA4D3 000000{twentyP}
001CA4EF 000000{twentyOneP}
001CA57B 000000{twentyTwoP}
001CA597 000000{twentyThreeP}
001CA5B3 000000{twentyFourP}
001CA5CF 000000{twentyFiveP}
001CA5EB 000000{twentySixP}
001CA607 000000{twentySevenP}
001CA623 000000{twentyEightP}
001CA63F 000000{twentyNineP}
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

def getOrbModsSeven(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW, twentyNineP, twentyNineW):
    return f'''
MP7 - Orb Modifer
042EF588 00050505
042EF58C 05{oneW}{oneW}{oneW}
042EF590 {oneW}{oneW}{oneW}{oneW}
042EF594 {oneW}{oneW}0000
042EF598 01{twoP}{twoP}{twoP}
042EF59C {twoP}{twoW}{twoW}{twoW}
042EF5A0 {twoW}{twoW}{twoW}{twoW}
042EF5A4 {twoW}{twoW}0000
042EF5A8 02{threeP}{threeP}{threeP}
042EF5AC {threeP}{threeW}{threeW}{threeW}
042EF5B0 {threeW}{threeW}{threeW}{threeW}
042EF5B4 {threeW}{threeW}0000
042EF5B8 03{fourP}{fourP}{fourP}
042EF5BC {fourP}{fourW}{fourW}{fourW}
042EF5C0 {fourW}{fourW}{fourW}{fourW}
042EF5C4 {fourW}{fourW}0000
042EF5C8 04{fiveP}{fiveP}{fiveP}
042EF5CC {fiveP}{fiveW}{fiveW}{fiveW}
042EF5D0 {fiveW}{fiveW}{fiveW}{fiveW}
042EF5D4 {fiveW}{fiveW}0000
042EF5D8 05{sixP}{sixP}{sixP}
042EF5DC {sixP}{sixW}{sixW}{sixW}
042EF5E0 {sixW}{sixW}{sixW}{sixW}
042EF5E4 {sixW}{sixW}0000
042EF5E8 06{sevenP}{sevenP}{sevenP}
042EF5EC {sevenP}{sevenW}{sevenW}{sevenW}
042EF5F0 {sevenW}{sevenW}{sevenW}{sevenW}
042EF5F4 {sevenW}{sevenW}0000
042EF5F8 07{eightP}{eightP}{eightP}
042EF5FC {eightP}{eightW}{eightW}{eightW}
042EF600 {eightW}{eightW}{eightW}{eightW}
042EF604 {eightW}{eightW}0000
042EF608 0A{nineP}{nineP}{nineP}
042EF60C {nineP}{nineW}{nineW}{nineW}
042EF610 {nineW}{nineW}{nineW}{nineW}
042EF614 {nineW}{nineW}0000
042EF618 0B{tenP}{tenP}{tenP}
042EF61C {tenP}{tenW}{tenW}{tenW}
042EF620 {tenW}{tenW}{tenW}{tenW}
042EF624 {tenW}{tenW}0000
042EF628 0C{elevenP}{elevenP}{elevenP}
042EF62C {elevenP}{elevenW}{elevenW}{elevenW}
042EF630 {elevenW}{elevenW}{elevenW}{elevenW}
042EF634 {elevenW}{elevenW}0000
042EF638 0D{twelveP}{twelveP}{twelveP}
042EF63C {twelveP}{twelveW}{twelveW}{twelveW}
042EF640 {twelveW}{twelveW}{twelveW}{twelveW}
042EF644 {twelveW}{twelveW}0000
042EF648 0E{thirteenP}{thirteenP}{thirteenP}
042EF64C {thirteenP}{thirteenW}{thirteenW}{thirteenW}
042EF650 {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042EF654 {thirteenW}{thirteenW}0000
042EF658 0F{fourteenP}{fourteenP}{fourteenP}
042EF65C {fourteenP}{fourteenW}{fourteenW}{fourteenW}
042EF660 {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042EF664 {fourteenW}{fourteenW}0000
042EF668 10{fifteenP}{fifteenP}{fifteenP}
042EF66C {fifteenP}{fifteenW}{fifteenW}{fifteenW}
042EF670 {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042EF674 {fifteenW}{fifteenW}0000
042EF678 11{sixteenP}{sixteenP}{sixteenP}
042EF67C {sixteenP}{sixteenW}{sixteenW}{sixteenW}
042EF680 {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042EF684 {sixteenW}{sixteenW}0000
042EF688 14{seventeenP}{seventeenP}{seventeenP}
042EF68C {seventeenP}{seventeenW}{seventeenW}{seventeenW}
042EF690 {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042EF694 {seventeenW}{seventeenW}0000
042EF698 15{eighteenP}{eighteenP}{eighteenP}
042EF69C {eighteenP}{eighteenW}{eighteenW}{eighteenW}
042EF6A0 {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042EF6A4 {eighteenW}{eighteenW}0000
042EF6A8 16{ninteenP}{ninteenP}{ninteenP}
042EF6AC {ninteenP}{ninteenW}{ninteenW}{ninteenW}
042EF6B0 {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042EF6B4 {ninteenW}{ninteenW}0000
042EF6B8 17{twentyP}{twentyP}{twentyP}
042EF6BC {twentyP}{twentyW}{twentyW}{twentyW}
042EF6C0 {twentyW}{twentyW}{twentyW}{twentyW}
042EF6C4 {twentyW}{twentyW}0000
042EF6C8 18{twentyOneP}{twentyOneP}{twentyOneP}
042EF6CC {twentyOneP}{twentyOneW}{twentyOneW}{twentyOneW}
042EF6D0 {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042EF6D4 {twentyOneW}{twentyOneW}0000
042EF6D8 19{twentyTwoP}{twentyTwoP}{twentyTwoP}
042EF6DC {twentyTwoP}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042EF6E0 {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042EF6E4 {twentyTwoW}{twentyTwoW}0000
042EF6E8 1E{twentyThreeP}{twentyThreeP}{twentyThreeP}
042EF6EC {twentyThreeP}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042EF6F0 {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042EF6F4 {twentyThreeW}{twentyThreeW}0000
042EF6F8 1F{twentyFourP}{twentyFourP}{twentyFourP}
042EF6FC {twentyFourP}{twentyFourW}{twentyFourW}{twentyFourW}
042EF700 {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042EF704 {twentyFourW}{twentyFourW}0000
042EF708 20{twentyFiveP}{twentyFiveP}{twentyFiveP}
042EF70C {twentyFiveP}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042EF710 {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042EF714 {twentyFiveW}{twentyFiveW}0000
042EF718 21{twentySixP}{twentySixP}{twentySixP}
042EF71C {twentySixP}{twentySixW}{twentySixW}{twentySixW}
042EF720 {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042EF724 {twentySixW}{twentySixW}0000
042EF728 22{twentySevenP}{twentySevenP}{twentySevenP}
042EF72C {twentySevenP}{twentySevenW}{twentySevenW}{twentySevenW}
042EF730 {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042EF734 {twentySevenW}{twentySevenW}0000
042EF738 23{twentyEightP}{twentyEightP}{twentyEightP}
042EF73C {twentyEightP}{twentyEightW}{twentyEightW}{twentyEightW}
042EF740 {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042EF744 {twentyEightW}{twentyEightW}0000
042EF748 28{twentyNineP}{twentyNineP}{twentyNineP}
042EF74C {twentyNineP}{twentyNineW}{twentyNineW}{twentyNineW}
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

def getBattleAmountFour(one, two, three, four, five):
    return f'''
MP4 - Give FOURBATTLE1, FOURBATTLE2, FOURBATTLE3, FOURBATTLE4, or FOURBATTLE5 coins in Battle Minigames
201D5DE0 050A141E
041D5DE0 {one}{two}{three}{four}
041D5DE4 {five}000000
'''

def getMinigameReplacement82(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP8 - Minigame Replacement: {gameUno} ➜ {gameDos}
282287CC 000000{hexUno}
022287CC 000000{hexDos}
E2000001 80008000
'''