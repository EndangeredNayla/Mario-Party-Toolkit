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
MP4 - Stars Cost {amountDec} Coins when stealing at the Boo House
040A5F30 2C1E{amount}
'''

def getBooSpaceCoinsFour(amount, amountDec):
    return f'''
MP4 - Coins Cost {amountDec} Coins when stealing at the Boo House
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
0406C790 38000005
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