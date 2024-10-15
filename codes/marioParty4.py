# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/9/2024
# License: MIT
# ============================================

def getRedSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Red Spaces Take Away {amountDec} Coins
C207FD5C 00000001
3BC0{amount} 00000000
'''

def getBlueSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Blue Spaces Give {amountDec} Coins
C207FBC4 00000001
3BC0{amount} 00000000
'''

def getMinigameCodeFour(amount, amountDec):
    return f'''
MP4 - Minigames Award {amountDec} Coins
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
E0000000 80008000
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
E0000000 80008000
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
E0000000 80008000
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
E0000000 80008000
'''

def getBooSpaceStarFour(amount, amountDec):
    return f'''
MP4 - Star Stealing Costs {amountDec} at the Boo House.
040A5F30 2C1E{amount}
'''

def getBooSpaceCoinsFour(amount, amountDec):
    return f'''
MP4 - Coin Stealing Costs {amountDec} at the Boo House.
040A61DC 2C1E{amount}
040A517C 2C03{amount}
'''

def getStarSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Stars Cost {amountDec} Coins
040843CC 2C03{amount}
04084590 2C03{amount}
040845CC 2C03{amount}
0408473C 2C1C{amount}
'''

def getSquishCodeFour(amount, amountDec):
    return f'''
MP4 - Mega Mushroom Steals {amountDec} Coins
0406BE88 2C00{amount}
0406BE90 3800{amount}
'''

def getBowserSuitCodeFour(amount, amountDec):
    return f'''
MP4 - Bowser Suit Steals {amountDec} Coins
0406C788 2C00{amount}
0406C790 3800{amount}
'''

def getLotterySpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Lottery Costs {amountDec} Coins
0407BD20 2C1E{amount}
'''

def getMinigameReplacement4(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP4 - Minigame Replacement: {gameUno} ➜ {gameDos}
2818FD2C 000000{hexUno}
0218FD2C 000000{hexDos}
E2000001 80008000
'''

def getBooHouseMinimum(min, minDec):
    return f'''
MP4 - Steal Minimum of {minDec} Coins from Boo
C20A19CC 00000003
7C1D0000 4181000C
7C1D0378 3BBD0001
7C00E850 00000000
040A19B0 3BA0{min}
'''

def getInitialItemsFour(one, two, three, oneItem, twoItem, threeItem):
    return f'''
MP4 - Start with {oneItem}, {twoItem}, and {threeItem}
C2063AE0 00000013
7C83032E 2C040007
40820080 3DC08018
61CEFCFC 89CE0000
2C0E0001 4082006C
3DC08018 61CEFC3D
39E000{one} 99EE0000
39E000{two} 99EE0001
39E000{three} 99EE0002
39E000{one} 99EE0030
39E000{two} 99EE0031
39E000{three} 99EE0032
39E000{one} 99EE0060
39E000{two} 99EE0061
39E000{three} 99EE0062
39E000{one} 99EE0090
39E000{two} 99EE0091
39E000{three} 99EE0092
39C00000 39E00000
60000000 00000000
'''

def getSpaceReplaceFour1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP4 - Replace {spaceName} with {spaceName2} (Slot A)
C2076A08 00000003
A01F0028 280000{spaceHex1}
4082000C 380000{spaceHex2}
B01F0028 00000000
'''

def getSpaceReplaceFour2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP4 - Replace {spaceName} with {spaceName2} (Slot B)
C2076A0C 00000003
280000{spaceHex1} 4082000C
380000{spaceHex2} B01F0028
28000000 00000000
'''

def getLotteryRewards4(lotteryPrizeA, lotteryPrizeB, lotteryPrizeC, lotteryPrizeD, lotteryPrizeALabel, lotteryPrizeBLabel, lotteryPrizeCLabel, lotteryPrizeDLabel):
    return f'''
MP4 - Lottery 1st is {lotteryPrizeALabel} - 2nd is {lotteryPrizeBLabel} - 3rd is {lotteryPrizeCLabel} or {lotteryPrizeDLabel}
0407EA58 3B80{lotteryPrizeA}
0407EA60 3B80{lotteryPrizeB}
021D5678 0000{lotteryPrizeC}{lotteryPrizeD}
'''

def getStarHandicap(p1, p2, p3, p4):
    return f'''
MP4 - Star Handicap
C2063AE4 0000000B
7C83032E 2C040007
40820040 3DC08018
61CEFCFC 89CE0000
2C0E0001 4082002C
3DC08018 61CEFC63
39E0{p1} 99EE0000
39E0{p2} 99EE0030
39E0{p3} 99EE0060
39E0{p4} 99EE0090
39C00000 39E00000
60000000 00000000
'''

def initialCoinsMod4(hex, hexDec):
    return f'''
MP4 - Gain {hexDec} Coins at the Start of the Game
020A8F0E 0000{hex}
'''

def getBattleGame4(p1, p2, p3, p4, p5, s1, s2, s3, s4, s5):
    return f'''
MP4 - Battle Minigames Bounties are {s1}, {s2}, {s3}, {s4}, and {s5}
041D5DE0 {p1}{p2}{p3}{p4}
041D5DE4 {p5}000000
'''


def getItemModsFourDXItemSpace():
    return f'''
MP4DX - Item Modifer
'''

def getItemModsFourItemSpace(minCoins):
    return f'''
MP4 - Item Modifier
C2086480 00000008
80640000 3DE08018
61EFFD02 89EF0000
1DEF0030 3C808018
6084FC38 7C847A14
88840009 70840060
5484D97E 3DE08018
61EFFD88 B08F0000
38A00000 00000000
C2077D84 00000001
2C0300{minCoins} 00000000
'''