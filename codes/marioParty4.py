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


def getItemShopPricesFourDX(minCoins, miniMushroomEarlyPrice1, miniMushroomEarlyPrice2, miniMushroomEarlyPrice34, miniMushroomMidPrice1, miniMushroomMidPrice2, miniMushroomMidPrice34, miniMushroomLatePrice1, miniMushroomLatePrice2, miniMushroomLatePrice34, megaMushroomEarlyPrice1, megaMushroomEarlyPrice2, megaMushroomEarlyPrice34, megaMushroomMidPrice1, megaMushroomMidPrice2, megaMushroomMidPrice34, megaMushroomLatePrice1, megaMushroomLatePrice2, megaMushroomLatePrice34, superMiniMushroomEarlyPrice1, superMiniMushroomEarlyPrice2, superMiniMushroomEarlyPrice34, superMiniMushroomMidPrice1, superMiniMushroomMidPrice2, superMiniMushroomMidPrice34, superMiniMushroomLatePrice1, superMiniMushroomLatePrice2, superMiniMushroomLatePrice34, superMegaMushroomEarlyPrice1, superMegaMushroomEarlyPrice2, superMegaMushroomEarlyPrice34, superMegaMushroomMidPrice1, superMegaMushroomMidPrice2, superMegaMushroomMidPrice34, superMegaMushroomLatePrice1, superMegaMushroomLatePrice2, superMegaMushroomLatePrice34, miniMegaHammerEarlyPrice1, miniMegaHammerEarlyPrice2, miniMegaHammerEarlyPrice34, miniMegaHammerMidPrice1, miniMegaHammerMidPrice2, miniMegaHammerMidPrice34, miniMegaHammerLatePrice1, miniMegaHammerLatePrice2, miniMegaHammerLatePrice34, warpPipeEarlyPrice1, warpPipeEarlyPrice2, warpPipeEarlyPrice34, warpPipeMidPrice1, warpPipeMidPrice2, warpPipeMidPrice34, warpPipeLatePrice1, warpPipeLatePrice2, warpPipeLatePrice34, swapCardEarlyPrice1, swapCardEarlyPrice2, swapCardEarlyPrice34, swapCardMidPrice1, swapCardMidPrice2, swapCardMidPrice34, swapCardLatePrice1, swapCardLatePrice2, swapCardLatePrice34, sparkyStickerEarlyPrice1, sparkyStickerEarlyPrice2, sparkyStickerEarlyPrice34, sparkyStickerMidPrice1, sparkyStickerMidPrice2, sparkyStickerMidPrice34, sparkyStickerLatePrice1, sparkyStickerLatePrice2, sparkyStickerLatePrice34, gaddlightEarlyPrice1, gaddlightEarlyPrice2, gaddlightEarlyPrice34, gaddlightMidPrice1, gaddlightMidPrice2, gaddlightMidPrice34, gaddlightLatePrice1, gaddlightLatePrice2, gaddlightLatePrice34, chompCallEarlyPrice1, chompCallEarlyPrice2, chompCallEarlyPrice34, chompCallMidPrice1, chompCallMidPrice2, chompCallMidPrice34, chompCallLatePrice1, chompCallLatePrice2, chompCallLatePrice34, bowserSuitEarlyPrice1, bowserSuitEarlyPrice2, bowserSuitEarlyPrice34, bowserSuitMidPrice1, bowserSuitMidPrice2, bowserSuitMidPrice34, bowserSuitLatePrice1, bowserSuitLatePrice2, bowserSuitLatePrice34, crystalBallEarlyPrice1, crystalBallEarlyPrice2, crystalBallEarlyPrice34, crystalBallMidPrice1, crystalBallMidPrice2, crystalBallMidPrice34, crystalBallLatePrice1, crystalBallLatePrice2, crystalBallLatePrice34, magicLampEarlyPrice1, magicLampEarlyPrice2, magicLampEarlyPrice34, magicLampMidPrice1, magicLampMidPrice2, magicLampMidPrice34, magicLampLatePrice1, magicLampLatePrice2, magicLampLatePrice34, itemBagEarlyPrice1, itemBagEarlyPrice2, itemBagEarlyPrice34, itemBagMidPrice1, itemBagMidPrice2, itemBagMidPrice34, itemBagLatePrice1, itemBagLatePrice2, itemBagLatePrice34, mushroomEarlyPrice1, mushroomEarlyPrice2, mushroomEarlyPrice34, mushroomMidPrice1, mushroomMidPrice2, mushroomMidPrice34, mushroomLatePrice1, mushroomLatePrice2, mushroomLatePrice34, goldenMushroomEarlyPrice1, goldenMushroomEarlyPrice2, goldenMushroomEarlyPrice34, goldenMushroomMidPrice1, goldenMushroomMidPrice2, goldenMushroomMidPrice34, goldenMushroomLatePrice1, goldenMushroomLatePrice2, goldenMushroomLatePrice34, reverseMushroomEarlyPrice1, reverseMushroomEarlyPrice2, reverseMushroomEarlyPrice34, reverseMushroomMidPrice1, reverseMushroomMidPrice2, reverseMushroomMidPrice34, reverseMushroomLatePrice1, reverseMushroomLatePrice2, reverseMushroomLatePrice34, poisonMushroomEarlyPrice1, poisonMushroomEarlyPrice2, poisonMushroomEarlyPrice34, poisonMushroomMidPrice1, poisonMushroomMidPrice2, poisonMushroomMidPrice34, poisonMushroomLatePrice1, poisonMushroomLatePrice2, poisonMushroomLatePrice34, triplePoisonMushroomEarlyPrice1, triplePoisonMushroomEarlyPrice2, triplePoisonMushroomEarlyPrice34, triplePoisonMushroomMidPrice1, triplePoisonMushroomMidPrice2, triplePoisonMushroomMidPrice34, triplePoisonMushroomLatePrice1, triplePoisonMushroomLatePrice2, triplePoisonMushroomLatePrice34, celluarShopperEarlyPrice1, celluarShopperEarlyPrice2, celluarShopperEarlyPrice34, celluarShopperMidPrice1, celluarShopperMidPrice2, celluarShopperMidPrice34, celluarShopperLatePrice1, celluarShopperLatePrice2, celluarShopperLatePrice34, skeletonKeyEarlyPrice1, skeletonKeyEarlyPrice2, skeletonKeyEarlyPrice34, skeletonKeyMidPrice1, skeletonKeyMidPrice2, skeletonKeyMidPrice34, skeletonKeyLatePrice1, skeletonKeyLatePrice2, skeletonKeyLatePrice34, plunderChestEarlyPrice1, plunderChestEarlyPrice2, plunderChestEarlyPrice34, plunderChestMidPrice1, plunderChestMidPrice2, plunderChestMidPrice34, plunderChestLatePrice1, plunderChestLatePrice2, plunderChestLatePrice34, gaddbrushEarlyPrice1, gaddbrushEarlyPrice2, gaddbrushEarlyPrice34, gaddbrushMidPrice1, gaddbrushMidPrice2, gaddbrushMidPrice34, gaddbrushLatePrice1, gaddbrushLatePrice2, gaddbrushLatePrice34, warpBlockEarlyPrice1, warpBlockEarlyPrice2, warpBlockEarlyPrice34, warpBlockMidPrice1, warpBlockMidPrice2, warpBlockMidPrice34, warpBlockLatePrice1, warpBlockLatePrice2, warpBlockLatePrice34, flyGuyEarlyPrice1, flyGuyEarlyPrice2, flyGuyEarlyPrice34, flyGuyMidPrice1, flyGuyMidPrice2, flyGuyMidPrice34, flyGuyLatePrice1, flyGuyLatePrice2, flyGuyLatePrice34, plusBlockEarlyPrice1, plusBlockEarlyPrice2, plusBlockEarlyPrice34, plusBlockMidPrice1, plusBlockMidPrice2, plusBlockMidPrice34, plusBlockLatePrice1, plusBlockLatePrice2, plusBlockLatePrice34, minusBlockEarlyPrice1, minusBlockEarlyPrice2, minusBlockEarlyPrice34, minusBlockMidPrice1, minusBlockMidPrice2, minusBlockMidPrice34, minusBlockLatePrice1, minusBlockLatePrice2, minusBlockLatePrice34, speedBlockEarlyPrice1, speedBlockEarlyPrice2, speedBlockEarlyPrice34, speedBlockMidPrice1, speedBlockMidPrice2, speedBlockMidPrice34, speedBlockLatePrice1, speedBlockLatePrice2, speedBlockLatePrice34, slowBlockEarlyPrice1, slowBlockEarlyPrice2, slowBlockEarlyPrice34, slowBlockMidPrice1, slowBlockMidPrice2, slowBlockMidPrice34, slowBlockLatePrice1, slowBlockLatePrice2, slowBlockLatePrice34, bowserPhoneEarlyPrice1, bowserPhoneEarlyPrice2, bowserPhoneEarlyPrice34, bowserPhoneMidPrice1, bowserPhoneMidPrice2, bowserPhoneMidPrice34, bowserPhoneLatePrice1, bowserPhoneLatePrice2, bowserPhoneLatePrice34, doubleDipEarlyPrice1, doubleDipEarlyPrice2, doubleDipEarlyPrice34, doubleDipMidPrice1, doubleDipMidPrice2, doubleDipMidPrice34, doubleDipLatePrice1, doubleDipLatePrice2, doubleDipLatePrice34, hiddenBlockCardEarlyPrice1, hiddenBlockCardEarlyPrice2, hiddenBlockCardEarlyPrice34, hiddenBlockCardMidPrice1, hiddenBlockCardMidPrice2, hiddenBlockCardMidPrice34, hiddenBlockCardLatePrice1, hiddenBlockCardLatePrice2, hiddenBlockCardLatePrice34, barterBoxEarlyPrice1, barterBoxEarlyPrice2, barterBoxEarlyPrice34, barterBoxMidPrice1, barterBoxMidPrice2, barterBoxMidPrice34, barterBoxLatePrice1, barterBoxLatePrice2, barterBoxLatePrice34, superWarpPipeEarlyPrice1, superWarpPipeEarlyPrice2, superWarpPipeEarlyPrice34, superWarpPipeMidPrice1, superWarpPipeMidPrice2, superWarpPipeMidPrice34, superWarpPipeLatePrice1, superWarpPipeLatePrice2, superWarpPipeLatePrice34, chanceTimeCharmEarlyPrice1, chanceTimeCharmEarlyPrice2, chanceTimeCharmEarlyPrice34, chanceTimeCharmMidPrice1, chanceTimeCharmMidPrice2, chanceTimeCharmMidPrice34, chanceTimeCharmLatePrice1, chanceTimeCharmLatePrice2, chanceTimeCharmLatePrice34, wackyWatchEarlyPrice1, wackyWatchEarlyPrice2, wackyWatchEarlyPrice34, wackyWatchMidPrice1, wackyWatchMidPrice2, wackyWatchMidPrice34, wackyWatchLatePrice1, wackyWatchLatePrice2, wackyWatchLatePrice34):
    return f'''
MP4DX - Item Modifer
C2077D84 00000001
2C0300{minCoins} 00000000
20071C98 00000000
04071F08 {miniMushroomEarlyPrice1}{megaMushroomEarlyPrice1}{superMiniMushroomEarlyPrice1}{superMegaMushroomEarlyPrice1}
04071F0C {miniMegaHammerEarlyPrice1}{warpPipeEarlyPrice1}{swapCardEarlyPrice1}{sparkyStickerEarlyPrice1}
04071F10 {gaddlightEarlyPrice1}{chompCallEarlyPrice1}{bowserSuitEarlyPrice1}{crystalBallEarlyPrice1}
04071F14 {magicLampEarlyPrice1}{itemBagEarlyPrice1}{bowserPhoneEarlyPrice1}{mushroomEarlyPrice1}
04071F18 {goldenMushroomEarlyPrice1}{hiddenBlockCardEarlyPrice1}{celluarShopperEarlyPrice1}{barterBoxEarlyPrice1}
04071F1C {superWarpPipeEarlyPrice1}{chanceTimeCharmEarlyPrice1}{wackyWatchEarlyPrice1}{plunderChestEarlyPrice1}
04071F20 {gaddbrushEarlyPrice1}{skeletonKeyEarlyPrice1}{warpBlockEarlyPrice1}{flyGuyEarlyPrice1}
04071F24 {plusBlockEarlyPrice1}{minusBlockEarlyPrice1}{speedBlockEarlyPrice1}{slowBlockEarlyPrice1}
04071F28 {poisonMushroomEarlyPrice1}{triplePoisonMushroomEarlyPrice1}{doubleDipEarlyPrice1}{reverseMushroomEarlyPrice1}
E0000000 80008000
20071C98 00000001
04071F08 {miniMushroomEarlyPrice2}{megaMushroomEarlyPrice2}{superMiniMushroomEarlyPrice2}{superMegaMushroomEarlyPrice2}
04071F0C {miniMegaHammerEarlyPrice2}{warpPipeEarlyPrice2}{swapCardEarlyPrice2}{sparkyStickerEarlyPrice2}
04071F10 {gaddlightEarlyPrice2}{chompCallEarlyPrice2}{bowserSuitEarlyPrice2}{crystalBallEarlyPrice2}
04071F14 {magicLampEarlyPrice2}{itemBagEarlyPrice2}{bowserPhoneEarlyPrice2}{mushroomEarlyPrice2}
04071F18 {goldenMushroomEarlyPrice2}{hiddenBlockCardEarlyPrice2}{celluarShopperEarlyPrice2}{barterBoxEarlyPrice2}
04071F1C {superWarpPipeEarlyPrice2}{chanceTimeCharmEarlyPrice2}{wackyWatchEarlyPrice2}{plunderChestEarlyPrice2}
04071F20 {gaddbrushEarlyPrice2}{skeletonKeyEarlyPrice2}{warpBlockEarlyPrice2}{flyGuyEarlyPrice2}
04071F24 {plusBlockEarlyPrice2}{minusBlockEarlyPrice2}{speedBlockEarlyPrice2}{slowBlockEarlyPrice2}
04071F28 {poisonMushroomEarlyPrice2}{triplePoisonMushroomEarlyPrice2}{doubleDipEarlyPrice2}{reverseMushroomEarlyPrice2}
E0000000 80008000
20071C98 00000002
04071F08 {miniMushroomEarlyPrice34}{megaMushroomEarlyPrice34}{superMiniMushroomEarlyPrice34}{superMegaMushroomEarlyPrice34}
04071F0C {miniMegaHammerEarlyPrice34}{warpPipeEarlyPrice34}{swapCardEarlyPrice34}{sparkyStickerEarlyPrice34}
04071F10 {gaddlightEarlyPrice34}{chompCallEarlyPrice34}{bowserSuitEarlyPrice34}{crystalBallEarlyPrice34}
04071F14 {magicLampEarlyPrice34}{itemBagEarlyPrice34}{bowserPhoneEarlyPrice34}{mushroomEarlyPrice34}
04071F18 {goldenMushroomEarlyPrice34}{hiddenBlockCardEarlyPrice34}{celluarShopperEarlyPrice34}{barterBoxEarlyPrice34}
04071F1C {superWarpPipeEarlyPrice34}{chanceTimeCharmEarlyPrice34}{wackyWatchEarlyPrice34}{plunderChestEarlyPrice34}
04071F20 {gaddbrushEarlyPrice34}{skeletonKeyEarlyPrice34}{warpBlockEarlyPrice34}{flyGuyEarlyPrice34}
04071F24 {plusBlockEarlyPrice34}{minusBlockEarlyPrice34}{speedBlockEarlyPrice34}{slowBlockEarlyPrice34}
04071F28 {poisonMushroomEarlyPrice34}{triplePoisonMushroomEarlyPrice34}{doubleDipEarlyPrice34}{reverseMushroomEarlyPrice34}
E0000000 80008000
20071C98 00010000
04071F08 {miniMushroomMidPrice1}{megaMushroomMidPrice1}{superMiniMushroomMidPrice1}{superMegaMushroomMidPrice1}
04071F0C {miniMegaHammerMidPrice1}{warpPipeMidPrice1}{swapCardMidPrice1}{sparkyStickerMidPrice1}
04071F10 {gaddlightMidPrice1}{chompCallMidPrice1}{bowserSuitMidPrice1}{crystalBallMidPrice1}
04071F14 {magicLampMidPrice1}{itemBagMidPrice1}{bowserPhoneMidPrice1}{mushroomMidPrice1}
04071F18 {goldenMushroomMidPrice1}{hiddenBlockCardMidPrice1}{celluarShopperMidPrice1}{barterBoxMidPrice1}
04071F1C {superWarpPipeMidPrice1}{chanceTimeCharmMidPrice1}{wackyWatchMidPrice1}{plunderChestMidPrice1}
04071F20 {gaddbrushMidPrice1}{skeletonKeyMidPrice1}{warpBlockMidPrice1}{flyGuyMidPrice1}
04071F24 {plusBlockMidPrice1}{minusBlockMidPrice1}{speedBlockMidPrice1}{slowBlockMidPrice1}
04071F28 {poisonMushroomMidPrice1}{triplePoisonMushroomMidPrice1}{doubleDipMidPrice1}{reverseMushroomMidPrice1}
E0000000 80008000
20071C98 00010001
04071F08 {miniMushroomMidPrice2}{megaMushroomMidPrice2}{superMiniMushroomMidPrice2}{superMegaMushroomMidPrice2}
04071F0C {miniMegaHammerMidPrice2}{warpPipeMidPrice2}{swapCardMidPrice2}{sparkyStickerMidPrice2}
04071F10 {gaddlightMidPrice2}{chompCallMidPrice2}{bowserSuitMidPrice2}{crystalBallMidPrice2}
04071F14 {magicLampMidPrice2}{itemBagMidPrice2}{bowserPhoneMidPrice2}{mushroomMidPrice2}
04071F18 {goldenMushroomMidPrice2}{hiddenBlockCardMidPrice2}{celluarShopperMidPrice2}{barterBoxMidPrice2}
04071F1C {superWarpPipeMidPrice2}{chanceTimeCharmMidPrice2}{wackyWatchMidPrice2}{plunderChestMidPrice2}
04071F20 {gaddbrushMidPrice2}{skeletonKeyMidPrice2}{warpBlockMidPrice2}{flyGuyMidPrice2}
04071F24 {plusBlockMidPrice2}{minusBlockMidPrice2}{speedBlockMidPrice2}{slowBlockMidPrice2}
04071F28 {poisonMushroomMidPrice2}{triplePoisonMushroomMidPrice2}{doubleDipMidPrice2}{reverseMushroomMidPrice2}
E0000000 80008000
20071C98 00010002
04071F08 {miniMushroomMidPrice34}{megaMushroomMidPrice34}{superMiniMushroomMidPrice34}{superMegaMushroomMidPrice34}
04071F0C {miniMegaHammerMidPrice34}{warpPipeMidPrice34}{swapCardMidPrice34}{sparkyStickerMidPrice34}
04071F10 {gaddlightMidPrice34}{chompCallMidPrice34}{bowserSuitMidPrice34}{crystalBallMidPrice34}
04071F14 {magicLampMidPrice34}{itemBagMidPrice34}{bowserPhoneMidPrice34}{mushroomMidPrice34}
04071F18 {goldenMushroomMidPrice34}{hiddenBlockCardMidPrice34}{celluarShopperMidPrice34}{barterBoxMidPrice34}
04071F1C {superWarpPipeMidPrice34}{chanceTimeCharmMidPrice34}{wackyWatchMidPrice34}{plunderChestMidPrice34}
04071F20 {gaddbrushMidPrice34}{skeletonKeyMidPrice34}{warpBlockMidPrice34}{flyGuyMidPrice34}
04071F24 {plusBlockMidPrice34}{minusBlockMidPrice34}{speedBlockMidPrice34}{slowBlockMidPrice34}
04071F28 {poisonMushroomMidPrice34}{triplePoisonMushroomMidPrice34}{doubleDipMidPrice34}{reverseMushroomMidPrice34}
E0000000 80008000
2C071C98 00000002
28071C9A 00000000
04071F08 {miniMushroomLatePrice1}{megaMushroomLatePrice1}{superMiniMushroomLatePrice1}{superMegaMushroomLatePrice1}
04071F0C {miniMegaHammerLatePrice1}{warpPipeLatePrice1}{swapCardLatePrice1}{sparkyStickerLatePrice1}
04071F10 {gaddlightLatePrice1}{chompCallLatePrice1}{bowserSuitLatePrice1}{crystalBallLatePrice1}
04071F14 {magicLampLatePrice1}{itemBagLatePrice1}{bowserPhoneLatePrice1}{mushroomLatePrice1}
04071F18 {goldenMushroomLatePrice1}{hiddenBlockCardLatePrice1}{celluarShopperLatePrice1}{barterBoxLatePrice1}
04071F1C {superWarpPipeLatePrice1}{chanceTimeCharmLatePrice1}{wackyWatchLatePrice1}{plunderChestLatePrice1}
04071F20 {gaddbrushLatePrice1}{skeletonKeyLatePrice1}{warpBlockLatePrice1}{flyGuyLatePrice1}
04071F24 {plusBlockLatePrice1}{minusBlockLatePrice1}{speedBlockLatePrice1}{slowBlockLatePrice1}
04071F28 {poisonMushroomLatePrice1}{triplePoisonMushroomLatePrice1}{doubleDipLatePrice1}{reverseMushroomLatePrice1}
E2000001 80008000
28071C9A 00000001
04071F08 {miniMushroomLatePrice2}{megaMushroomLatePrice2}{superMiniMushroomLatePrice2}{superMegaMushroomLatePrice2}
04071F0C {miniMegaHammerLatePrice2}{warpPipeLatePrice2}{swapCardLatePrice2}{sparkyStickerLatePrice2}
04071F10 {gaddlightLatePrice2}{chompCallLatePrice2}{bowserSuitLatePrice2}{crystalBallLatePrice2}
04071F14 {magicLampLatePrice2}{itemBagLatePrice2}{bowserPhoneLatePrice2}{mushroomLatePrice2}
04071F18 {goldenMushroomLatePrice2}{hiddenBlockCardLatePrice2}{celluarShopperLatePrice2}{barterBoxLatePrice2}
04071F1C {superWarpPipeLatePrice2}{chanceTimeCharmLatePrice2}{wackyWatchLatePrice2}{plunderChestLatePrice2}
04071F20 {gaddbrushLatePrice2}{skeletonKeyLatePrice2}{warpBlockLatePrice2}{flyGuyLatePrice2}
04071F24 {plusBlockLatePrice2}{minusBlockLatePrice2}{speedBlockLatePrice2}{slowBlockLatePrice2}
04071F28 {poisonMushroomLatePrice2}{triplePoisonMushroomLatePrice2}{doubleDipLatePrice2}{reverseMushroomLatePrice2}
E2000001 80008000
28071C9A 00000002
04071F08 {miniMushroomLatePrice34}{megaMushroomLatePrice34}{superMiniMushroomLatePrice34}{superMegaMushroomLatePrice34}
04071F0C {miniMegaHammerLatePrice34}{warpPipeLatePrice34}{swapCardLatePrice34}{sparkyStickerLatePrice34}
04071F10 {gaddlightLatePrice34}{chompCallLatePrice34}{bowserSuitLatePrice34}{crystalBallLatePrice34}
04071F14 {magicLampLatePrice34}{itemBagLatePrice34}{bowserPhoneLatePrice34}{mushroomLatePrice34}
04071F18 {goldenMushroomLatePrice34}{hiddenBlockCardLatePrice34}{celluarShopperLatePrice34}{barterBoxLatePrice34}
04071F1C {superWarpPipeLatePrice34}{chanceTimeCharmLatePrice34}{wackyWatchLatePrice34}{plunderChestLatePrice34}
04071F20 {gaddbrushLatePrice34}{skeletonKeyLatePrice34}{warpBlockLatePrice34}{flyGuyLatePrice34}
04071F24 {plusBlockLatePrice34}{minusBlockLatePrice34}{speedBlockLatePrice34}{slowBlockLatePrice34}
04071F28 {poisonMushroomLatePrice34}{triplePoisonMushroomLatePrice34}{doubleDipLatePrice34}{reverseMushroomLatePrice34}
E0000000 80008000
'''

def getItemShopPricesFour(minCoins, miniMushroomEarlyPrice1, miniMushroomEarlyPrice2, miniMushroomEarlyPrice34, miniMushroomMidPrice1, miniMushroomMidPrice2, miniMushroomMidPrice34, miniMushroomLatePrice1, miniMushroomLatePrice2, miniMushroomLatePrice34, megaMushroomEarlyPrice1, megaMushroomEarlyPrice2, megaMushroomEarlyPrice34, megaMushroomMidPrice1, megaMushroomMidPrice2, megaMushroomMidPrice34, megaMushroomLatePrice1, megaMushroomLatePrice2, megaMushroomLatePrice34, superMiniMushroomEarlyPrice1, superMiniMushroomEarlyPrice2, superMiniMushroomEarlyPrice34, superMiniMushroomMidPrice1, superMiniMushroomMidPrice2, superMiniMushroomMidPrice34, superMiniMushroomLatePrice1, superMiniMushroomLatePrice2, superMiniMushroomLatePrice34, superMegaMushroomEarlyPrice1, superMegaMushroomEarlyPrice2, superMegaMushroomEarlyPrice34, superMegaMushroomMidPrice1, superMegaMushroomMidPrice2, superMegaMushroomMidPrice34, superMegaMushroomLatePrice1, superMegaMushroomLatePrice2, superMegaMushroomLatePrice34, miniMegaHammerEarlyPrice1, miniMegaHammerEarlyPrice2, miniMegaHammerEarlyPrice34, miniMegaHammerMidPrice1, miniMegaHammerMidPrice2, miniMegaHammerMidPrice34, miniMegaHammerLatePrice1, miniMegaHammerLatePrice2, miniMegaHammerLatePrice34, warpPipeEarlyPrice1, warpPipeEarlyPrice2, warpPipeEarlyPrice34, warpPipeMidPrice1, warpPipeMidPrice2, warpPipeMidPrice34, warpPipeLatePrice1, warpPipeLatePrice2, warpPipeLatePrice34, swapCardEarlyPrice1, swapCardEarlyPrice2, swapCardEarlyPrice34, swapCardMidPrice1, swapCardMidPrice2, swapCardMidPrice34, swapCardLatePrice1, swapCardLatePrice2, swapCardLatePrice34, sparkyStickerEarlyPrice1, sparkyStickerEarlyPrice2, sparkyStickerEarlyPrice34, sparkyStickerMidPrice1, sparkyStickerMidPrice2, sparkyStickerMidPrice34, sparkyStickerLatePrice1, sparkyStickerLatePrice2, sparkyStickerLatePrice34, gaddlightEarlyPrice1, gaddlightEarlyPrice2, gaddlightEarlyPrice34, gaddlightMidPrice1, gaddlightMidPrice2, gaddlightMidPrice34, gaddlightLatePrice1, gaddlightLatePrice2, gaddlightLatePrice34, chompCallEarlyPrice1, chompCallEarlyPrice2, chompCallEarlyPrice34, chompCallMidPrice1, chompCallMidPrice2, chompCallMidPrice34, chompCallLatePrice1, chompCallLatePrice2, chompCallLatePrice34, bowserSuitEarlyPrice1, bowserSuitEarlyPrice2, bowserSuitEarlyPrice34, bowserSuitMidPrice1, bowserSuitMidPrice2, bowserSuitMidPrice34, bowserSuitLatePrice1, bowserSuitLatePrice2, bowserSuitLatePrice34, crystalBallEarlyPrice1, crystalBallEarlyPrice2, crystalBallEarlyPrice34, crystalBallMidPrice1, crystalBallMidPrice2, crystalBallMidPrice34, crystalBallLatePrice1, crystalBallLatePrice2, crystalBallLatePrice34, magicLampEarlyPrice1, magicLampEarlyPrice2, magicLampEarlyPrice34, magicLampMidPrice1, magicLampMidPrice2, magicLampMidPrice34, magicLampLatePrice1, magicLampLatePrice2, magicLampLatePrice34, itemBagEarlyPrice1, itemBagEarlyPrice2, itemBagEarlyPrice34, itemBagMidPrice1, itemBagMidPrice2, itemBagMidPrice34, itemBagLatePrice1, itemBagLatePrice2, itemBagLatePrice34):
    return f'''
MP4 - Item Modifier
C2086480 00000013
80640000 3DE08018
61EFFD02 89EF0000
1DEF0030 3C808018
6084FC38 7C847A14
88840009 70840060
5484D97E 3DE08018
61EFFD62 B08F0000
3DC08018 61CEFCFC
888E0001 89CE0000
39C00003 7C8473D6
3DC08018 61CEFCFC
89CE0000 39E00000
7C0E2000 40810018
39E00001 1C840002
7C0E2000 40810008
39E00002 3C808018
6084FD72 B1E40000
39C00000 39E00000
60000000 00000000
C2077D84 00000001
2C0300{minCoins} 00000000
2818FD62 00000000
2818FD72 00000000
04139D2C {miniMushroomEarlyPrice1}{megaMushroomEarlyPrice1}{superMiniMushroomEarlyPrice1}{superMegaMushroomEarlyPrice1}
04139D30 {miniMegaHammerEarlyPrice1}{warpPipeEarlyPrice1}{swapCardEarlyPrice1}{sparkyStickerEarlyPrice1}
04139D34 {gaddlightEarlyPrice1}{chompCallEarlyPrice1}{bowserSuitEarlyPrice1}{crystalBallEarlyPrice1}
02139D38 0000{magicLampEarlyPrice1}{itemBagEarlyPrice1}
E2000001 80008000
2818FD72 00000001
04139D2C {miniMushroomEarlyPrice2}{megaMushroomEarlyPrice2}{superMiniMushroomEarlyPrice2}{superMegaMushroomEarlyPrice2}
04139D30 {miniMegaHammerEarlyPrice2}{warpPipeEarlyPrice2}{swapCardEarlyPrice2}{sparkyStickerEarlyPrice2}
04139D34 {gaddlightEarlyPrice2}{chompCallEarlyPrice2}{bowserSuitEarlyPrice2}{crystalBallEarlyPrice2}
02139D38 0000{magicLampEarlyPrice2}{itemBagEarlyPrice2}
E2000001 80008000
2818FD72 00000002
04139D2C {miniMushroomEarlyPrice34}{megaMushroomEarlyPrice34}{superMiniMushroomEarlyPrice34}{superMegaMushroomEarlyPrice34}
04139D30 {miniMegaHammerEarlyPrice34}{warpPipeEarlyPrice34}{swapCardEarlyPrice34}{sparkyStickerEarlyPrice34}
04139D34 {gaddlightEarlyPrice34}{chompCallEarlyPrice34}{bowserSuitEarlyPrice34}{crystalBallEarlyPrice34}
02139D38 0000{magicLampEarlyPrice34}{itemBagEarlyPrice34}
E0000000 80008000
2818FD62 00000001
2818FD72 00000000
04139D2C {miniMushroomMidPrice1}{megaMushroomMidPrice1}{superMiniMushroomMidPrice1}{superMegaMushroomMidPrice1}
04139D30 {miniMegaHammerMidPrice1}{warpPipeMidPrice1}{swapCardMidPrice1}{sparkyStickerMidPrice1}
04139D34 {gaddlightMidPrice1}{chompCallMidPrice1}{bowserSuitMidPrice1}{crystalBallMidPrice1}
02139D38 0000{magicLampMidPrice1}{itemBagMidPrice1}
E2000001 80008000
2818FD72 00000001
04139D2C {miniMushroomMidPrice2}{megaMushroomMidPrice2}{superMiniMushroomMidPrice2}{superMegaMushroomMidPrice2}
04139D30 {miniMegaHammerMidPrice2}{warpPipeMidPrice2}{swapCardMidPrice2}{sparkyStickerMidPrice2}
04139D34 {gaddlightMidPrice2}{chompCallMidPrice2}{bowserSuitMidPrice2}{crystalBallMidPrice2}
02139D38 0000{magicLampMidPrice2}{itemBagMidPrice2}
E2000001 80008000
2818FD72 00000001
04139D2C {miniMushroomMidPrice34}{megaMushroomMidPrice34}{superMiniMushroomMidPrice34}{superMegaMushroomMidPrice34}
04139D30 {miniMegaHammerMidPrice34}{warpPipeMidPrice34}{swapCardMidPrice34}{sparkyStickerMidPrice34}
04139D34 {gaddlightMidPrice34}{chompCallMidPrice34}{bowserSuitMidPrice34}{crystalBallMidPrice34}
02139D38 0000{magicLampMidPrice34}{itemBagMidPrice34}
E2000001 80008000
2C18FD62 00000002
2818FD72 00000000
04139D2C {miniMushroomLatePrice1}{megaMushroomLatePrice1}{superMiniMushroomLatePrice1}{superMegaMushroomLatePrice1}
04139D30 {miniMegaHammerLatePrice1}{warpPipeLatePrice1}{swapCardLatePrice1}{sparkyStickerLatePrice1}
04139D34 {gaddlightLatePrice1}{chompCallLatePrice1}{bowserSuitLatePrice1}{crystalBallLatePrice1}
02139D38 0000{magicLampLatePrice1}{itemBagLatePrice1}
2818FD72 00000001
04139D2C {miniMushroomLatePrice2}{megaMushroomLatePrice2}{superMiniMushroomLatePrice2}{superMegaMushroomLatePrice2}
04139D30 {miniMegaHammerLatePrice2}{warpPipeLatePrice2}{swapCardLatePrice2}{sparkyStickerLatePrice2}
04139D34 {gaddlightLatePrice2}{chompCallLatePrice2}{bowserSuitLatePrice2}{crystalBallLatePrice2}
02139D38 0000{magicLampLatePrice2}{itemBagLatePrice2}
E2000001 80008000
2818FD72 00000002
04139D2C {miniMushroomLatePrice34}{megaMushroomLatePrice34}{superMiniMushroomLatePrice34}{superMegaMushroomLatePrice34}
04139D30 {miniMegaHammerLatePrice34}{warpPipeLatePrice34}{swapCardLatePrice34}{sparkyStickerLatePrice34}
04139D34 {gaddlightLatePrice34}{chompCallLatePrice34}{bowserSuitLatePrice34}{crystalBallLatePrice34}
02139D38 0000{magicLampLatePrice34}{itemBagLatePrice34}
E0000000 80008000
'''

def getItemShopOddsFour():
    return f'''
C2077FF4 00000039
3C80801A 60844A60
386000FF 90640000
90640004 90640008
9064000C 90640010
3C608018 6063FCFC
88830001 88630000
38A00003 7C842BD6
38A00000 7C032000
40810048 38A0000E
1C840002 7C032000
40810008 38A00046
3C808019 6084FD02
88840000 1C840030
3C608018 6063FC38
7C832214 8C640009
70630060 5463D97E
1C63000E 7CA51A14
3CC08013 60C69DB2
7CC62A14 38600000
3A200000 7C8618AE
7E312214 38630001
2C03000E 40800008
4BFFFFEC 3C608005
6063FB40 7C6903A6
2C030000 418200DC
7E238B78 4E800421
7C651B78 38600000
39600000 7C8618AE
7D6B2214 7C0B2800
41810018 7C0B8800
41820010 38630001
4BFFFFE4 4BFFFFCC
3C80801A 60844A60
81640000 3AA00000
3A400000 7CA6A8AE
2C050000 41820008
3A520001 3AB50001
2C15000E 40800008
4BFFFFE4 3AA00000
3CA0801A 60A54A60
7CA5AA14 80A50000
2C0500FF 4182002C
3AB50001 2C150005
40800008 4BFFFFDC
7C0B1800 4182FF64
2C0B00FF 41820018
38840004 4BFFFF94
7C159000 4080FFEC
4BFFFFE0 90640000
3C80801A 60844A60
80840010 2C0400FF
4082002C 4BFFFF2C
3860000E 4E800421
3C80801A 60844A60
98640000 98640004
98640008 9864000C
98640010 00000000
'''

def getItemShopOddsFourDX():
    pass
