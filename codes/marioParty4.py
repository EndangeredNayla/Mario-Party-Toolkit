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


def getItemModsFourDXItemSpace(minCoins, miniMushroomPrice1, miniMushroomPrice2, miniMushroomPrice34, miniMushroomShopOdds12, miniMushroomShopOdds34, miniMushroomSpaceOdds1, miniMushroomSpaceOdds2, miniMushroomSpaceOdds34, megaMushroomPrice1, megaMushroomPrice2, megaMushroomPrice34, megaMushroomShopOdds12, megaMushroomShopOdds34, megaMushroomSpaceOdds1, megaMushroomSpaceOdds2, megaMushroomSpaceOdds34, superMiniMushroomPrice1, superMiniMushroomPrice2, superMiniMushroomPrice34, superMiniMushroomShopOdds12, superMiniMushroomShopOdds34, superMiniMushroomSpaceOdds1, superMiniMushroomSpaceOdds2, superMiniMushroomSpaceOdds34, superMegaMushroomPrice1, superMegaMushroomPrice2, superMegaMushroomPrice34, superMegaMushroomShopOdds12, superMegaMushroomShopOdds34, superMegaMushroomSpaceOdds1, superMegaMushroomSpaceOdds2, superMegaMushroomSpaceOdds34, miniMegaHammerPrice1, miniMegaHammerPrice2, miniMegaHammerPrice34, miniMegaHammerShopOdds12, miniMegaHammerShopOdds34, miniMegaHammerSpaceOdds1, miniMegaHammerSpaceOdds2, miniMegaHammerSpaceOdds34, warpPipePrice1, warpPipePrice2, warpPipePrice34, warpPipeShopOdds12, warpPipeShopOdds34, warpPipeSpaceOdds1, warpPipeSpaceOdds2, warpPipeSpaceOdds34, swapCardPrice1, swapCardPrice2, swapCardPrice34, swapCardShopOdds12, swapCardShopOdds34, swapCardSpaceOdds1, swapCardSpaceOdds2, swapCardSpaceOdds34, sparkyStickerPrice1, sparkyStickerPrice2, sparkyStickerPrice34, sparkyStickerShopOdds12, sparkyStickerShopOdds34, sparkyStickerSpaceOdds1, sparkyStickerSpaceOdds2, sparkyStickerSpaceOdds34, gaddlightPrice1, gaddlightPrice2, gaddlightPrice34, gaddlightShopOdds12, gaddlightShopOdds34, gaddlightSpaceOdds1, gaddlightSpaceOdds2, gaddlightSpaceOdds34, chompCallPrice1, chompCallPrice2, chompCallPrice34, chompCallShopOdds12, chompCallShopOdds34, chompCallSpaceOdds1, chompCallSpaceOdds2, chompCallSpaceOdds34, bowserSuitPrice1, bowserSuitPrice2, bowserSuitPrice34, bowserSuitShopOdds12, bowserSuitShopOdds34, bowserSuitSpaceOdds1, bowserSuitSpaceOdds2, bowserSuitSpaceOdds34, crystalBallPrice1, crystalBallPrice2, crystalBallPrice34, crystalBallShopOdds12, crystalBallShopOdds34, crystalBallSpaceOdds1, crystalBallSpaceOdds2, crystalBallSpaceOdds34, magicLampPrice1, magicLampPrice2, magicLampPrice34, magicLampShopOdds12, magicLampShopOdds34, magicLampSpaceOdds1, magicLampSpaceOdds2, magicLampSpaceOdds34, itemBagPrice1, itemBagPrice2, itemBagPrice34, itemBagShopOdds12, itemBagShopOdds34, itemBagSpaceOdds1, itemBagSpaceOdds2, itemBagSpaceOdds34, mushroomPrice1, mushroomPrice2, mushroomPrice34, mushroomShopOdds12, mushroomShopOdds34, mushroomSpaceOdds1, mushroomSpaceOdds2, mushroomSpaceOdds34, goldenMushroomPrice1, goldenMushroomPrice2, goldenMushroomPrice34, goldenMushroomShopOdds12, goldenMushroomShopOdds34, goldenMushroomSpaceOdds1, goldenMushroomSpaceOdds2, goldenMushroomSpaceOdds34, reverseMushroomPrice1, reverseMushroomPrice2, reverseMushroomPrice34, reverseMushroomShopOdds12, reverseMushroomShopOdds34, reverseMushroomSpaceOdds1, reverseMushroomSpaceOdds2, reverseMushroomSpaceOdds34, poisonMushroomPrice1, poisonMushroomPrice2, poisonMushroomPrice34, poisonMushroomShopOdds12, poisonMushroomShopOdds34, poisonMushroomSpaceOdds1, poisonMushroomSpaceOdds2, poisonMushroomSpaceOdds34, triplePoisonMushroomPrice1, triplePoisonMushroomPrice2, triplePoisonMushroomPrice34, triplePoisonMushroomShopOdds12, triplePoisonMushroomShopOdds34, triplePoisonMushroomSpaceOdds1, triplePoisonMushroomSpaceOdds2, triplePoisonMushroomSpaceOdds34, celluarShopperPrice1, celluarShopperPrice2, celluarShopperPrice34, celluarShopperShopOdds12, celluarShopperShopOdds34, celluarShopperSpaceOdds1, celluarShopperSpaceOdds2, celluarShopperSpaceOdds34, skeletonKeyPrice1, skeletonKeyPrice2, skeletonKeyPrice34, skeletonKeyShopOdds12, skeletonKeyShopOdds34, skeletonKeySpaceOdds1, skeletonKeySpaceOdds2, skeletonKeySpaceOdds34, plunderChestPrice1, plunderChestPrice2, plunderChestPrice34, plunderChestShopOdds12, plunderChestShopOdds34, plunderChestSpaceOdds1, plunderChestSpaceOdds2, plunderChestSpaceOdds34, gaddbrushPrice1, gaddbrushPrice2, gaddbrushPrice34, gaddbrushShopOdds12, gaddbrushShopOdds34, gaddbrushSpaceOdds1, gaddbrushSpaceOdds2, gaddbrushSpaceOdds34, warpBlockPrice1, warpBlockPrice2, warpBlockPrice34, warpBlockShopOdds12, warpBlockShopOdds34, warpBlockSpaceOdds1, warpBlockSpaceOdds2, warpBlockSpaceOdds34, flyGuyPrice1, flyGuyPrice2, flyGuyPrice34, flyGuyShopOdds12, flyGuyShopOdds34, flyGuySpaceOdds1, flyGuySpaceOdds2, flyGuySpaceOdds34, plusBlockPrice1, plusBlockPrice2, plusBlockPrice34, plusBlockShopOdds12, plusBlockShopOdds34, plusBlockSpaceOdds1, plusBlockSpaceOdds2, plusBlockSpaceOdds34, minusBlockPrice1, minusBlockPrice2, minusBlockPrice34, minusBlockShopOdds12, minusBlockShopOdds34, minusBlockSpaceOdds1, minusBlockSpaceOdds2, minusBlockSpaceOdds34, speedBlockPrice1, speedBlockPrice2, speedBlockPrice34, speedBlockShopOdds12, speedBlockShopOdds34, speedBlockSpaceOdds1, speedBlockSpaceOdds2, speedBlockSpaceOdds34, slowBlockPrice1, slowBlockPrice2, slowBlockPrice34, slowBlockShopOdds12, slowBlockShopOdds34, slowBlockSpaceOdds1, slowBlockSpaceOdds2, slowBlockSpaceOdds34, bowserPhonePrice1, bowserPhonePrice2, bowserPhonePrice34, bowserPhoneShopOdds12, bowserPhoneShopOdds34, bowserPhoneSpaceOdds1, bowserPhoneSpaceOdds2, bowserPhoneSpaceOdds34, doubleDipPrice1, doubleDipPrice2, doubleDipPrice34, doubleDipShopOdds12, doubleDipShopOdds34, doubleDipSpaceOdds1, doubleDipSpaceOdds2, doubleDipSpaceOdds34, hiddenBlockCardPrice1, hiddenBlockCardPrice2, hiddenBlockCardPrice34, hiddenBlockCardShopOdds12, hiddenBlockCardShopOdds34, hiddenBlockCardSpaceOdds1, hiddenBlockCardSpaceOdds2, hiddenBlockCardSpaceOdds34, barterBoxPrice1, barterBoxPrice2, barterBoxPrice34, barterBoxShopOdds12, barterBoxShopOdds34, barterBoxSpaceOdds1, barterBoxSpaceOdds2, barterBoxSpaceOdds34, superWarpPipePrice1, superWarpPipePrice2, superWarpPipePrice34, superWarpPipeShopOdds12, superWarpPipeShopOdds34, superWarpPipeSpaceOdds1, superWarpPipeSpaceOdds2, superWarpPipeSpaceOdds34, chanceTimeCharmPrice1, chanceTimeCharmPrice2, chanceTimeCharmPrice34, chanceTimeCharmShopOdds12, chanceTimeCharmShopOdds34, chanceTimeCharmSpaceOdds1, chanceTimeCharmSpaceOdds2, chanceTimeCharmSpaceOdds34, wackyWatchPrice1, wackyWatchPrice2, wackyWatchPrice34, wackyWatchShopOdds12, wackyWatchShopOdds34, wackyWatchSpaceOdds1, wackyWatchSpaceOdds2, wackyWatchSpaceOdds34):
    return f'''
MP4 - Item Modifer
C2077D84 00000001
2C0300{minCoins} 00000000
2818FD02 000000FF
2814C5C2 00000000
66200009 00000000
E2000001 00000000
2814C5C2 00000001
66200009 00000000
E2000001 00000000
2C14C5C2 00000001
66200009 00000000
E0000000 00000000
2818FD02 000001FF
2814C5C2 00000000
66200009 00000000
E2000001 00000000
2814C5C2 00000001
66200009 00000000
E0000000 00000000
2C14C5C2 00000001
66200009 00000000
E0000000 00000000
2818FD02 000002FF
2814C5C2 00000000
66200009 00000000
E2000001 00000000
2814C5C2 00000001
66200009 00000000
E2000001 00000000
2C14C5C2 00000001
66200009 00000000
E0000000 00000000
2818FD02 000003FF
2814C5C2 00000000
66200007 00000000
E2000001 00000000
2814C5C2 00000001
66200018 00000000
E0000000 00000000
2C14C5C2 00000001
66200029 00000000
E0000000 00000000
04071F08 {miniMushroomPrice1}{megaMushroomPrice1}{superMiniMushroomPrice1}{superMegaMushroomPrice1}
04071F0C {miniMegaHammerPrice1}{warpPipePrice1}{swapCardPrice1}{sparkyStickerPrice1}
04071F10 {gaddlightPrice1}{chompCallPrice1}{bowserSuitPrice1}{crystalBallPrice1}
04071F14 {magicLampPrice1}{itemBagPrice1}{bowserPhonePrice1}{mushroomPrice1}
04071F18 {goldenMushroomPrice1}{hiddenBlockCardPrice1}{celluarShopperPrice1}{barterBoxPrice1}
04071F1C {superWarpPipePrice1}{chanceTimeCharmPrice1}{wackyWatchPrice1}{plunderChestPrice1}
04071F20 {gaddbrushPrice1}{skeletonKeyPrice1}{warpBlockPrice1}{flyGuyPrice1}
04071F24 {plusBlockPrice1}{minusBlockPrice1}{speedBlockPrice1}{slowBlockPrice1}
04071F28 {poisonMushroomPrice1}{triplePoisonMushroomPrice1}{doubleDipPrice1}{reverseMushroomPrice1}
02071C42 0000{miniMushroomSpaceOdds1}{megaMushroomSpaceOdds1}
04071C44 {superMiniMushroomSpaceOdds1}{superMegaMushroomSpaceOdds1}{miniMegaHammerSpaceOdds1}{warpPipeSpaceOdds1}
04071C48 {swapCardSpaceOdds1}{sparkyStickerSpaceOdds1}{gaddlightSpaceOdds1}{chompCallSpaceOdds1}
04071C4C {bowserSuitSpaceOdds1}{crystalBallSpaceOdds1}{magicLampSpaceOdds1}{itemBagSpaceOdds1}
04071C50 {bowserPhoneSpaceOdds1}{mushroomSpaceOdds1}{goldenMushroomSpaceOdds1}{hiddenBlockCardSpaceOdds1}
04071C54 {celluarShopperSpaceOdds1}{barterBoxSpaceOdds1}{superWarpPipeSpaceOdds1}{chanceTimeCharmSpaceOdds1}
04071C58 {wackyWatchSpaceOdds1}{plunderChestSpaceOdds1}{gaddbrushSpaceOdds1}{skeletonKeySpaceOdds1}
04071C5C {flyGuySpaceOdds1}{warpBlockSpaceOdds1}{plusBlockSpaceOdds1}{minusBlockSpaceOdds1}
04071C60 {speedBlockSpaceOdds1}{slowBlockSpaceOdds1}{poisonMushroomSpaceOdds1}{triplePoisonMushroomSpaceOdds1}
04071C64 {doubleDipSpaceOdds1}{reverseMushroomSpaceOdds1}0000  
66200014 00000000
04071F08 {miniMushroomPrice2}{megaMushroomPrice2}{superMiniMushroomPrice2}{superMegaMushroomPrice2}
04071F0C {miniMegaHammerPrice2}{warpPipePrice2}{swapCardPrice2}{sparkyStickerPrice2}
04071F10 {gaddlightPrice2}{chompCallPrice2}{bowserSuitPrice2}{crystalBallPrice2}
04071F14 {magicLampPrice2}{itemBagPrice2}{bowserPhonePrice2}{mushroomPrice2}
04071F18 {goldenMushroomPrice2}{hiddenBlockCardPrice2}{celluarShopperPrice2}{barterBoxPrice2}
04071F1C {superWarpPipePrice2}{chanceTimeCharmPrice2}{wackyWatchPrice2}{plunderChestPrice2}
04071F20 {gaddbrushPrice2}{skeletonKeyPrice2}{warpBlockPrice2}{flyGuyPrice2}
04071F24 {plusBlockPrice2}{minusBlockPrice2}{speedBlockPrice2}{slowBlockPrice2}
04071F28 {poisonMushroomPrice2}{triplePoisonMushroomPrice2}{doubleDipPrice2}{reverseMushroomPrice2}
02071C42 0000{miniMushroomSpaceOdds2}{megaMushroomSpaceOdds2}
04071C44 {superMiniMushroomSpaceOdds2}{superMegaMushroomSpaceOdds2}{miniMegaHammerSpaceOdds2}{warpPipeSpaceOdds2}
04071C48 {swapCardSpaceOdds2}{sparkyStickerSpaceOdds2}{gaddlightSpaceOdds2}{chompCallSpaceOdds2}
04071C4C {bowserSuitSpaceOdds2}{crystalBallSpaceOdds2}{magicLampSpaceOdds2}{itemBagSpaceOdds2}
04071C50 {bowserPhoneSpaceOdds2}{mushroomSpaceOdds2}{goldenMushroomSpaceOdds2}{hiddenBlockCardSpaceOdds2}
04071C54 {celluarShopperSpaceOdds2}{barterBoxSpaceOdds2}{superWarpPipeSpaceOdds2}{chanceTimeCharmSpaceOdds2}
04071C58 {wackyWatchSpaceOdds2}{plunderChestSpaceOdds2}{gaddbrushSpaceOdds2}{skeletonKeySpaceOdds2}
04071C5C {flyGuySpaceOdds2}{warpBlockSpaceOdds2}{plusBlockSpaceOdds2}{minusBlockSpaceOdds2}
04071C60 {speedBlockSpaceOdds2}{slowBlockSpaceOdds2}{poisonMushroomSpaceOdds2}{triplePoisonMushroomSpaceOdds2}
04071C64 {doubleDipSpaceOdds2}{reverseMushroomSpaceOdds2}0000
66200014 00000000
04071F08 {miniMushroomPrice34}{megaMushroomPrice34}{superMiniMushroomPrice34}{superMegaMushroomPrice34}
04071F0C {miniMegaHammerPrice34}{warpPipePrice34}{swapCardPrice34}{sparkyStickerPrice34}
04071F10 {gaddlightPrice34}{chompCallPrice34}{bowserSuitPrice34}{crystalBallPrice34}
04071F14 {magicLampPrice34}{itemBagPrice34}{bowserPhonePrice34}{mushroomPrice34}
04071F18 {goldenMushroomPrice34}{hiddenBlockCardPrice34}{celluarShopperPrice34}{barterBoxPrice34}
04071F1C {superWarpPipePrice34}{chanceTimeCharmPrice34}{wackyWatchPrice34}{plunderChestPrice34}
04071F20 {gaddbrushPrice34}{skeletonKeyPrice34}{warpBlockPrice34}{flyGuyPrice34}
04071F24 {plusBlockPrice34}{minusBlockPrice34}{speedBlockPrice34}{slowBlockPrice34}
04071F28 {poisonMushroomPrice34}{triplePoisonMushroomPrice34}{doubleDipPrice34}{reverseMushroomPrice34}
02071C42 0000{miniMushroomSpaceOdds34}{megaMushroomSpaceOdds34}
04071C44 {superMiniMushroomSpaceOdds34}{superMegaMushroomSpaceOdds34}{miniMegaHammerSpaceOdds34}{warpPipeSpaceOdds34}
04071C48 {swapCardSpaceOdds34}{sparkyStickerSpaceOdds34}{gaddlightSpaceOdds34}{chompCallSpaceOdds34}
04071C4C {bowserSuitSpaceOdds34}{crystalBallSpaceOdds34}{magicLampSpaceOdds34}{itemBagSpaceOdds34}
04071C50 {bowserPhoneSpaceOdds34}{mushroomSpaceOdds34}{goldenMushroomSpaceOdds34}{hiddenBlockCardSpaceOdds34}
04071C54 {celluarShopperSpaceOdds34}{barterBoxSpaceOdds34}{superWarpPipeSpaceOdds34}{chanceTimeCharmSpaceOdds34}
04071C58 {wackyWatchSpaceOdds34}{plunderChestSpaceOdds34}{gaddbrushSpaceOdds34}{skeletonKeySpaceOdds34}
04071C5C {flyGuySpaceOdds34}{warpBlockSpaceOdds34}{plusBlockSpaceOdds34}{minusBlockSpaceOdds34}
04071C60 {speedBlockSpaceOdds34}{slowBlockSpaceOdds34}{poisonMushroomSpaceOdds34}{triplePoisonMushroomSpaceOdds34}
04071C64 {doubleDipSpaceOdds34}{reverseMushroomSpaceOdds34}0000
E0000000 00000000
04071f30 {miniMushroomShopOdds12}{megaMushroomShopOdds12}{superMiniMushroomShopOdds12}{superMegaMushroomShopOdds12}
04071f34 {miniMegaHammerShopOdds12}{warpPipeShopOdds12}{swapCardShopOdds12}{sparkyStickerShopOdds12}
04071f38 {gaddlightShopOdds12}{chompCallShopOdds12}{bowserSuitShopOdds12}{crystalBallShopOdds12}
04071f3C {magicLampShopOdds12}{itemBagShopOdds12}{bowserPhoneShopOdds12}{mushroomShopOdds12}
04071f40 {goldenMushroomShopOdds12}{hiddenBlockCardShopOdds12}{celluarShopperShopOdds12}{barterBoxShopOdds12}
04071f44 {superWarpPipeShopOdds12}{chanceTimeCharmShopOdds12}{wackyWatchShopOdds12}{plunderChestShopOdds12}
04071f48 {gaddbrushShopOdds12}{skeletonKeyShopOdds12}{warpBlockShopOdds12}{flyGuyShopOdds12}
04071f4C {plusBlockShopOdds12}{minusBlockShopOdds12}{speedBlockShopOdds12}{slowBlockShopOdds12}
04071f50 {poisonMushroomShopOdds12}{triplePoisonMushroomShopOdds12}{doubleDipShopOdds12}{reverseMushroomShopOdds12}
02071f62 0000{miniMushroomShopOdds12}{megaMushroomShopOdds12}
04071f64 {superMegaMushroomShopOdds12}{superMegaMushroomShopOdds12}{miniMegaHammerShopOdds12}{superWarpPipeShopOdds12}
04071f68 {swapCardShopOdds12}{sparkyStickerShopOdds12}{gaddlightShopOdds12}{chompCallShopOdds12}
04071f6C {bowserSuitShopOdds12}{crystalBallShopOdds12}{magicLampShopOdds12}{itemBagShopOdds12}
04071f70 {bowserPhoneShopOdds12}{mushroomShopOdds12}{goldenMushroomShopOdds12}{hiddenBlockCardShopOdds12}
04071f74 {celluarShopperShopOdds12}{barterBoxShopOdds12}{superWarpPipeShopOdds12}{chanceTimeCharmShopOdds12}
04071f78 {wackyWatchShopOdds12}{plunderChestShopOdds12}{gaddbrushShopOdds12}{skeletonKeyShopOdds12}
04071f7C {warpBlockShopOdds12}{flyGuyShopOdds12}{plusBlockShopOdds12}{minusBlockShopOdds12}
04071f80 {speedBlockShopOdds12}{slowBlockShopOdds12}{poisonMushroomShopOdds12}{triplePoisonMushroomShopOdds12}
04071f84 {doubleDipShopOdds12}{reverseMushroomShopOdds12}0000
04071F94 {miniMushroomShopOdds12}{megaMushroomShopOdds12}{superMiniMushroomShopOdds12}{superMegaMushroomShopOdds12}
04071f98 {miniMegaHammerShopOdds12}{warpPipeShopOdds12}{swapCardShopOdds12}{sparkyStickerShopOdds12}
04071f9C {gaddlightShopOdds12}{chompCallShopOdds12}{bowserSuitShopOdds12}{crystalBallShopOdds12}
04071fA0 {magicLampShopOdds12}{itemBagShopOdds12}{bowserPhoneShopOdds12}{mushroomShopOdds12}
04071fA4 {goldenMushroomShopOdds12}{hiddenBlockCardShopOdds12}{celluarShopperShopOdds12}{barterBoxShopOdds12}
04071fA8 {superWarpPipeShopOdds12}{chanceTimeCharmShopOdds12}{wackyWatchShopOdds12}{plunderChestShopOdds12}
04071fAC {gaddbrushShopOdds12}{skeletonKeyShopOdds12}{warpBlockShopOdds12}{flyGuyShopOdds12}
04071fB0 {plusBlockShopOdds12}{minusBlockShopOdds12}{speedBlockShopOdds12}{slowBlockShopOdds12}
04071fB4 {poisonMushroomShopOdds12}{triplePoisonMushroomShopOdds12}{doubleDipShopOdds12}{reverseMushroomShopOdds12}
02071FC6 0000{miniMushroomShopOdds12}{megaMushroomShopOdds12}
04071fC8 {superMegaMushroomShopOdds12}{superMegaMushroomShopOdds12}{miniMegaHammerShopOdds12}{superWarpPipeShopOdds12}
04071fCC {swapCardShopOdds12}{sparkyStickerShopOdds12}{gaddlightShopOdds12}{chompCallShopOdds12}
04071fD0 {bowserSuitShopOdds12}{crystalBallShopOdds12}{magicLampShopOdds12}{itemBagShopOdds12}
04071fD4 {bowserPhoneShopOdds12}{mushroomShopOdds12}{goldenMushroomShopOdds12}{hiddenBlockCardShopOdds12}
04071fD8 {celluarShopperShopOdds12}{barterBoxShopOdds12}{superWarpPipeShopOdds12}{chanceTimeCharmShopOdds12}
04071fDC {wackyWatchShopOdds12}{plunderChestShopOdds12}{gaddbrushShopOdds12}{skeletonKeyShopOdds12}
04071fE0 {warpBlockShopOdds12}{flyGuyShopOdds12}{plusBlockShopOdds12}{minusBlockShopOdds12}
04071fE4 {speedBlockShopOdds12}{slowBlockShopOdds12}{poisonMushroomShopOdds12}{triplePoisonMushroomShopOdds12}
04071fE8 {doubleDipShopOdds12}{reverseMushroomShopOdds12}0000
04071Ff8 {miniMushroomShopOdds12}{megaMushroomShopOdds12}{superMiniMushroomShopOdds12}{superMegaMushroomShopOdds12}
04071ffc {miniMegaHammerShopOdds12}{warpPipeShopOdds12}{swapCardShopOdds12}{sparkyStickerShopOdds12}
04072000 {gaddlightShopOdds12}{chompCallShopOdds12}{bowserSuitShopOdds12}{crystalBallShopOdds12}
04072004 {magicLampShopOdds12}{itemBagShopOdds12}{bowserPhoneShopOdds12}{mushroomShopOdds12}
04072008 {goldenMushroomShopOdds12}{hiddenBlockCardShopOdds12}{celluarShopperShopOdds12}{barterBoxShopOdds12}
0407200c {superWarpPipeShopOdds12}{chanceTimeCharmShopOdds12}{wackyWatchShopOdds12}{plunderChestShopOdds12}
04072010 {gaddbrushShopOdds12}{skeletonKeyShopOdds12}{warpBlockShopOdds12}{flyGuyShopOdds12}
04072014 {plusBlockShopOdds12}{minusBlockShopOdds12}{speedBlockShopOdds12}{slowBlockShopOdds12}
04072018 {poisonMushroomShopOdds12}{triplePoisonMushroomShopOdds12}{doubleDipShopOdds12}{reverseMushroomShopOdds12}
0207202A 0000{miniMushroomShopOdds34}{megaMushroomShopOdds34}
0407202C {superMegaMushroomShopOdds34}{superMegaMushroomShopOdds34}{miniMegaHammerShopOdds34}{superWarpPipeShopOdds34}
04072030 {swapCardShopOdds34}{sparkyStickerShopOdds34}{gaddlightShopOdds34}{chompCallShopOdds34}
04072034 {bowserSuitShopOdds34}{crystalBallShopOdds34}{magicLampShopOdds34}{itemBagShopOdds34}
04072038 {bowserPhoneShopOdds34}{mushroomShopOdds34}{goldenMushroomShopOdds34}{hiddenBlockCardShopOdds34}
0407203C {celluarShopperShopOdds34}{barterBoxShopOdds34}{superWarpPipeShopOdds34}{chanceTimeCharmShopOdds34}
04072040 {wackyWatchShopOdds34}{plunderChestShopOdds34}{gaddbrushShopOdds34}{skeletonKeyShopOdds34}
04072044 {warpBlockShopOdds34}{flyGuyShopOdds34}{plusBlockShopOdds34}{minusBlockShopOdds34}
04072048 {speedBlockShopOdds34}{slowBlockShopOdds34}{poisonMushroomShopOdds34}{triplePoisonMushroomShopOdds34}
0407204C {doubleDipShopOdds34}{reverseMushroomShopOdds34}0000
0407205C {miniMushroomShopOdds34}{megaMushroomShopOdds34}{superMiniMushroomShopOdds34}{superMegaMushroomShopOdds34}
04072060 {miniMegaHammerShopOdds34}{warpPipeShopOdds34}{swapCardShopOdds34}{sparkyStickerShopOdds34}
04072064 {gaddlightShopOdds34}{chompCallShopOdds34}{bowserSuitShopOdds34}{crystalBallShopOdds34}
04072068 {magicLampShopOdds34}{itemBagShopOdds34}{bowserPhoneShopOdds34}{mushroomShopOdds34}
0407206C {goldenMushroomShopOdds34}{hiddenBlockCardShopOdds34}{celluarShopperShopOdds34}{barterBoxShopOdds34}
04072070 {superWarpPipeShopOdds34}{chanceTimeCharmShopOdds34}{wackyWatchShopOdds34}{plunderChestShopOdds34}
04072074 {gaddbrushShopOdds34}{skeletonKeyShopOdds34}{warpBlockShopOdds34}{flyGuyShopOdds34}
04072078 {plusBlockShopOdds34}{minusBlockShopOdds34}{speedBlockShopOdds34}{slowBlockShopOdds34}
0407207C {poisonMushroomShopOdds34}{triplePoisonMushroomShopOdds34}{doubleDipShopOdds34}{reverseMushroomShopOdds34}
0207208E 0000{miniMushroomShopOdds34}{megaMushroomShopOdds34}
04072090 {superMegaMushroomShopOdds34}{superMegaMushroomShopOdds34}{miniMegaHammerShopOdds34}{superWarpPipeShopOdds34}
04072094 {swapCardShopOdds34}{sparkyStickerShopOdds34}{gaddlightShopOdds34}{chompCallShopOdds34}
04072098 {bowserSuitShopOdds34}{crystalBallShopOdds34}{magicLampShopOdds34}{itemBagShopOdds34}
0407209C {bowserPhoneShopOdds34}{mushroomShopOdds34}{goldenMushroomShopOdds34}{hiddenBlockCardShopOdds34}
040720A0 {celluarShopperShopOdds34}{barterBoxShopOdds34}{superWarpPipeShopOdds34}{chanceTimeCharmShopOdds34}
040720A4 {wackyWatchShopOdds34}{plunderChestShopOdds34}{gaddbrushShopOdds34}{skeletonKeyShopOdds34}
040720A8 {warpBlockShopOdds34}{flyGuyShopOdds34}{plusBlockShopOdds34}{minusBlockShopOdds34}
040720AC {speedBlockShopOdds34}{slowBlockShopOdds34}{poisonMushroomShopOdds34}{triplePoisonMushroomShopOdds34}
040720B0 {doubleDipShopOdds34}{reverseMushroomShopOdds34}0000
040720C0 {miniMushroomShopOdds34}{megaMushroomShopOdds34}{superMiniMushroomShopOdds34}{superMegaMushroomShopOdds34}
040720C4 {miniMegaHammerShopOdds34}{warpPipeShopOdds34}{swapCardShopOdds34}{sparkyStickerShopOdds34}
040720C8 {gaddlightShopOdds34}{chompCallShopOdds34}{bowserSuitShopOdds34}{crystalBallShopOdds34}
040720CC {magicLampShopOdds34}{itemBagShopOdds34}{bowserPhoneShopOdds34}{mushroomShopOdds34}
040720D0 {goldenMushroomShopOdds34}{hiddenBlockCardShopOdds34}{celluarShopperShopOdds34}{barterBoxShopOdds34}
040720D4 {superWarpPipeShopOdds34}{chanceTimeCharmShopOdds34}{wackyWatchShopOdds34}{plunderChestShopOdds34}
040720D8 {gaddbrushShopOdds34}{skeletonKeyShopOdds34}{warpBlockShopOdds34}{flyGuyShopOdds34}
040720DC {plusBlockShopOdds34}{minusBlockShopOdds34}{speedBlockShopOdds34}{slowBlockShopOdds34}
040720E0 {poisonMushroomShopOdds34}{triplePoisonMushroomShopOdds34}{doubleDipShopOdds34}{reverseMushroomShopOdds34}
'''