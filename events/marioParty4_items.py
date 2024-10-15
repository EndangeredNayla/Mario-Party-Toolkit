# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 10/14/2024
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp4ShopDXPrices(miniMushroomEarlyPrice1 = "5", miniMushroomEarlyPrice2 = "5", miniMushroomEarlyPrice34 = "5", miniMushroomMidPrice1 = "5", miniMushroomMidPrice2 = "5", miniMushroomMidPrice34 = "5", miniMushroomLatePrice1 = "5", miniMushroomLatePrice2 = "5", miniMushroomLatePrice34 = "5", megaMushroomEarlyPrice1 = "5", megaMushroomEarlyPrice2 = "5", megaMushroomEarlyPrice34 = "5", megaMushroomMidPrice1 = "5", megaMushroomMidPrice2 = "5", megaMushroomMidPrice34 = "5", megaMushroomLatePrice1 = "5", megaMushroomLatePrice2 = "5", megaMushroomLatePrice34 = "5", superMiniMushroomEarlyPrice1 = "10", superMiniMushroomEarlyPrice2 = "10", superMiniMushroomEarlyPrice34 = "10", superMiniMushroomMidPrice1 = "10", superMiniMushroomMidPrice2 = "10", superMiniMushroomMidPrice34 = "10", superMiniMushroomLatePrice1 = "10", superMiniMushroomLatePrice2 = "10", superMiniMushroomLatePrice34 = "10", superMegaMushroomEarlyPrice1 = "15", superMegaMushroomEarlyPrice2 = "15", superMegaMushroomEarlyPrice34 = "15", superMegaMushroomMidPrice1 = "15", superMegaMushroomMidPrice2 = "15", superMegaMushroomMidPrice34 = "15", superMegaMushroomLatePrice1 = "15", superMegaMushroomLatePrice2 = "15", superMegaMushroomLatePrice34 = "15", miniMegaHammerEarlyPrice1 = "10", miniMegaHammerEarlyPrice2 = "10", miniMegaHammerEarlyPrice34 = "10", miniMegaHammerMidPrice1 = "10", miniMegaHammerMidPrice2 = "10", miniMegaHammerMidPrice34 = "10", miniMegaHammerLatePrice1 = "10", miniMegaHammerLatePrice2 = "10", miniMegaHammerLatePrice34 = "10", warpPipeEarlyPrice1 = "10", warpPipeEarlyPrice2 = "10", warpPipeEarlyPrice34 = "10", warpPipeMidPrice1 = "10", warpPipeMidPrice2 = "10", warpPipeMidPrice34 = "10", warpPipeLatePrice1 = "10", warpPipeLatePrice2 = "10", warpPipeLatePrice34 = "10", swapCardEarlyPrice1 = "15", swapCardEarlyPrice2 = "15", swapCardEarlyPrice34 = "15", swapCardMidPrice1 = "15", swapCardMidPrice2 = "15", swapCardMidPrice34 = "15", swapCardLatePrice1 = "15", swapCardLatePrice2 = "15", swapCardLatePrice34 = "15", sparkyStickerEarlyPrice1 = "5", sparkyStickerEarlyPrice2 = "5", sparkyStickerEarlyPrice34 = "5", sparkyStickerMidPrice1 = "5", sparkyStickerMidPrice2 = "5", sparkyStickerMidPrice34 = "5", sparkyStickerLatePrice1 = "5", sparkyStickerLatePrice2 = "5", sparkyStickerLatePrice34 = "5", gaddlightEarlyPrice1 = "15", gaddlightEarlyPrice2 = "15", gaddlightEarlyPrice34 = "15", gaddlightMidPrice1 = "15", gaddlightMidPrice2 = "15", gaddlightMidPrice34 = "15", gaddlightLatePrice1 = "15", gaddlightLatePrice2 = "15", gaddlightLatePrice34 = "10", chompCallEarlyPrice1 = "10", chompCallEarlyPrice2 = "10", chompCallEarlyPrice34 = "10", chompCallMidPrice1 = "10", chompCallMidPrice2 = "10", chompCallMidPrice34 = "10", chompCallLatePrice1 = "10", chompCallLatePrice2 = "10", chompCallLatePrice34 = "10", bowserSuitEarlyPrice1 = "12", bowserSuitEarlyPrice2 = "12", bowserSuitEarlyPrice34 = "12", bowserSuitMidPrice1 = "12", bowserSuitMidPrice2 = "12", bowserSuitMidPrice34 = "12", bowserSuitLatePrice1 = "12", bowserSuitLatePrice2 = "12", bowserSuitLatePrice34 = "12", crystalBallEarlyPrice1 = "25", crystalBallEarlyPrice2 = "25", crystalBallEarlyPrice34 = "25", crystalBallMidPrice1 = "25", crystalBallMidPrice2 = "25", crystalBallMidPrice34 = "25", crystalBallLatePrice1 = "25", crystalBallLatePrice2 = "25", crystalBallLatePrice34 = "25", magicLampEarlyPrice1 = "30", magicLampEarlyPrice2 = "30", magicLampEarlyPrice34 = "30", magicLampMidPrice1 = "30", magicLampMidPrice2 = "30", magicLampMidPrice34 = "30", magicLampLatePrice1 = "30", magicLampLatePrice2 = "30", magicLampLatePrice34 = "30", itemBagEarlyPrice1 = "30", itemBagEarlyPrice2 = "30", itemBagEarlyPrice34 = "30", itemBagMidPrice1 = "30", itemBagMidPrice2 = "30", itemBagMidPrice34 = "30", itemBagLatePrice1 = "30", itemBagLatePrice2 = "30", itemBagLatePrice34 = "30", mushroomEarlyPrice1 = "5", mushroomEarlyPrice2 = "5", mushroomEarlyPrice34 = "5", mushroomMidPrice1 = "5", mushroomMidPrice2 = "5", mushroomMidPrice34 = "5", mushroomLatePrice1 = "5", mushroomLatePrice2 = "5", mushroomLatePrice34 = "5", goldenMushroomEarlyPrice1 = "10", goldenMushroomEarlyPrice2 = "10", goldenMushroomEarlyPrice34 = "10", goldenMushroomMidPrice1 = "10", goldenMushroomMidPrice2 = "10", goldenMushroomMidPrice34 = "10", goldenMushroomLatePrice1 = "10", goldenMushroomLatePrice2 = "10", goldenMushroomLatePrice34 = "10", reverseMushroomEarlyPrice1 = "10", reverseMushroomEarlyPrice2 = "10", reverseMushroomEarlyPrice34 = "10", reverseMushroomMidPrice1 = "10", reverseMushroomMidPrice2 = "10", reverseMushroomMidPrice34 = "10", reverseMushroomLatePrice1 = "10", reverseMushroomLatePrice2 = "10", reverseMushroomLatePrice34 = "5", poisonMushroomEarlyPrice1 = "5", poisonMushroomEarlyPrice2 = "5", poisonMushroomEarlyPrice34 = "5", poisonMushroomMidPrice1 = "5", poisonMushroomMidPrice2 = "5", poisonMushroomMidPrice34 = "5", poisonMushroomLatePrice1 = "5", poisonMushroomLatePrice2 = "5", poisonMushroomLatePrice34 = "5", triplePoisonMushroomEarlyPrice1 = "15", triplePoisonMushroomEarlyPrice2 = "15", triplePoisonMushroomEarlyPrice34 = "15", triplePoisonMushroomMidPrice1 = "15", triplePoisonMushroomMidPrice2 = "15", triplePoisonMushroomMidPrice34 = "15", triplePoisonMushroomLatePrice1 = "15", triplePoisonMushroomLatePrice2 = "15", triplePoisonMushroomLatePrice34 = "15", celluarShopperEarlyPrice1 = "5", celluarShopperEarlyPrice2 = "5", celluarShopperEarlyPrice34 = "5", celluarShopperMidPrice1 = "5", celluarShopperMidPrice2 = "5", celluarShopperMidPrice34 = "5", celluarShopperLatePrice1 = "5", celluarShopperLatePrice2 = "5", celluarShopperLatePrice34 = "5", skeletonKeyEarlyPrice1 = "5", skeletonKeyEarlyPrice2 = "5", skeletonKeyEarlyPrice34 = "5", skeletonKeyMidPrice1 = "5", skeletonKeyMidPrice2 = "5", skeletonKeyMidPrice34 = "5", skeletonKeyLatePrice1 = "5", skeletonKeyLatePrice2 = "5", skeletonKeyLatePrice34 = "5", plunderChestEarlyPrice1 = "15", plunderChestEarlyPrice2 = "15", plunderChestEarlyPrice34 = "15", plunderChestMidPrice1 = "15", plunderChestMidPrice2 = "15", plunderChestMidPrice34 = "15", plunderChestLatePrice1 = "15", plunderChestLatePrice2 = "15", plunderChestLatePrice34 = "15", gaddbrushEarlyPrice1 = "15", gaddbrushEarlyPrice2 = "15", gaddbrushEarlyPrice34 = "15", gaddbrushMidPrice1 = "15", gaddbrushMidPrice2 = "15", gaddbrushMidPrice34 = "15", gaddbrushLatePrice1 = "15", gaddbrushLatePrice2 = "15", gaddbrushLatePrice34 = "15", warpBlockEarlyPrice1 = "5", warpBlockEarlyPrice2 = "5", warpBlockEarlyPrice34 = "5", warpBlockMidPrice1 = "5", warpBlockMidPrice2 = "5", warpBlockMidPrice34 = "5", warpBlockLatePrice1 = "5", warpBlockLatePrice2 = "5", warpBlockLatePrice34 = "5", flyGuyEarlyPrice1 = "12", flyGuyEarlyPrice2 = "12", flyGuyEarlyPrice34 = "12", flyGuyMidPrice1 = "12", flyGuyMidPrice2 = "12", flyGuyMidPrice34 = "12", flyGuyLatePrice1 = "12", flyGuyLatePrice2 = "12", flyGuyLatePrice34 = "12", plusBlockEarlyPrice1 = "10", plusBlockEarlyPrice2 = "10", plusBlockEarlyPrice34 = "10", plusBlockMidPrice1 = "10", plusBlockMidPrice2 = "10", plusBlockMidPrice34 = "10", plusBlockLatePrice1 = "10", plusBlockLatePrice2 = "10", plusBlockLatePrice34 = "10", minusBlockEarlyPrice1 = "10", minusBlockEarlyPrice2 = "10", minusBlockEarlyPrice34 = "10", minusBlockMidPrice1 = "10", minusBlockMidPrice2 = "10", minusBlockMidPrice34 = "10", minusBlockLatePrice1 = "10", minusBlockLatePrice2 = "10", minusBlockLatePrice34 = "10", speedBlockEarlyPrice1 = "12", speedBlockEarlyPrice2 = "12", speedBlockEarlyPrice34 = "12", speedBlockMidPrice1 = "12", speedBlockMidPrice2 = "12", speedBlockMidPrice34 = "12", speedBlockLatePrice1 = "12", speedBlockLatePrice2 = "12", speedBlockLatePrice34 = "12", slowBlockEarlyPrice1 = "12", slowBlockEarlyPrice2 = "12", slowBlockEarlyPrice34 = "12", slowBlockMidPrice1 = "12", slowBlockMidPrice2 = "12", slowBlockMidPrice34 = "12", slowBlockLatePrice1 = "12", slowBlockLatePrice2 = "12", slowBlockLatePrice34 = "12", bowserPhoneEarlyPrice1 = "10", bowserPhoneEarlyPrice2 = "10", bowserPhoneEarlyPrice34 = "10", bowserPhoneMidPrice1 = "10", bowserPhoneMidPrice2 = "10", bowserPhoneMidPrice34 = "10", bowserPhoneLatePrice1 = "10", bowserPhoneLatePrice2 = "10", bowserPhoneLatePrice34 = "10", doubleDipEarlyPrice1 = "12", doubleDipEarlyPrice2 = "12", doubleDipEarlyPrice34 = "12", doubleDipMidPrice1 = "12", doubleDipMidPrice2 = "12", doubleDipMidPrice34 = "12", doubleDipLatePrice1 = "12", doubleDipLatePrice2 = "12", doubleDipLatePrice34 = "12", hiddenBlockCardEarlyPrice1 = "40", hiddenBlockCardEarlyPrice2 = "40", hiddenBlockCardEarlyPrice34 = "40", hiddenBlockCardMidPrice1 = "40", hiddenBlockCardMidPrice2 = "40", hiddenBlockCardMidPrice34 = "40", hiddenBlockCardLatePrice1 = "40", hiddenBlockCardLatePrice2 = "40", hiddenBlockCardLatePrice34 = "40", barterBoxEarlyPrice1 = "40", barterBoxEarlyPrice2 = "40", barterBoxEarlyPrice34 = "40", barterBoxMidPrice1 = "40", barterBoxMidPrice2 = "40", barterBoxMidPrice34 = "40", barterBoxLatePrice1 = "40", barterBoxLatePrice2 = "40", barterBoxLatePrice34 = "40", superWarpPipeEarlyPrice1 = "40", superWarpPipeEarlyPrice2 = "40", superWarpPipeEarlyPrice34 = "40", superWarpPipeMidPrice1 = "40", superWarpPipeMidPrice2 = "40", superWarpPipeMidPrice34 = "40", superWarpPipeLatePrice1 = "40", superWarpPipeLatePrice2 = "40", superWarpPipeLatePrice34 = "40", chanceTimeCharmEarlyPrice1 = "40", chanceTimeCharmEarlyPrice2 = "40", chanceTimeCharmEarlyPrice34 = "40", chanceTimeCharmMidPrice1 = "40", chanceTimeCharmMidPrice2 = "40", chanceTimeCharmMidPrice34 = "40", chanceTimeCharmLatePrice1 = "40", chanceTimeCharmLatePrice2 = "40", chanceTimeCharmLatePrice34 = "40", wackyWatchEarlyPrice1 = "100", wackyWatchEarlyPrice2 = "100", wackyWatchEarlyPrice34 = "100", wackyWatchMidPrice1 = "100", wackyWatchMidPrice2 = "100", wackyWatchMidPrice34 = "100", wackyWatchLatePrice1 = "100", wackyWatchLatePrice2 = "100", wackyWatchLatePrice34 = "100"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    # Mini Mushroom
    miniMushroomEarlyPrice1 = get_capsule_value(miniMushroomEarlyPrice1) or "5"
    miniMushroomEarlyPrice2 = get_capsule_value(miniMushroomEarlyPrice2) or "5"
    miniMushroomEarlyPrice34 = get_capsule_value(miniMushroomEarlyPrice34) or "5"
    miniMushroomMidPrice1 = get_capsule_value(miniMushroomMidPrice1) or "5"
    miniMushroomMidPrice2 = get_capsule_value(miniMushroomMidPrice2) or "5"
    miniMushroomMidPrice34 = get_capsule_value(miniMushroomMidPrice34) or "5"
    miniMushroomLatePrice1 = get_capsule_value(miniMushroomLatePrice1) or "5"
    miniMushroomLatePrice2 = get_capsule_value(miniMushroomLatePrice2) or "5"
    miniMushroomLatePrice34 = get_capsule_value(miniMushroomLatePrice34) or "5"
    
    # Mega Mushroom
    megaMushroomEarlyPrice1 = get_capsule_value(megaMushroomEarlyPrice1) or "5"
    megaMushroomEarlyPrice2 = get_capsule_value(megaMushroomEarlyPrice2) or "5"
    megaMushroomEarlyPrice34 = get_capsule_value(megaMushroomEarlyPrice34) or "5"
    megaMushroomMidPrice1 = get_capsule_value(megaMushroomMidPrice1) or "5"
    megaMushroomMidPrice2 = get_capsule_value(megaMushroomMidPrice2) or "5"
    megaMushroomMidPrice34 = get_capsule_value(megaMushroomMidPrice34) or "5"
    megaMushroomLatePrice1 = get_capsule_value(megaMushroomLatePrice1) or "5"
    megaMushroomLatePrice2 = get_capsule_value(megaMushroomLatePrice2) or "5"
    megaMushroomLatePrice34 = get_capsule_value(megaMushroomLatePrice34) or "5"

    # Super Mini Mushroom
    superMiniMushroomEarlyPrice1 = get_capsule_value(superMiniMushroomEarlyPrice1) or "10"
    superMiniMushroomEarlyPrice2 = get_capsule_value(superMiniMushroomEarlyPrice2) or "10"
    superMiniMushroomEarlyPrice34 = get_capsule_value(superMiniMushroomEarlyPrice34) or "10"
    superMiniMushroomMidPrice1 = get_capsule_value(superMiniMushroomMidPrice1) or "10"
    superMiniMushroomMidPrice2 = get_capsule_value(superMiniMushroomMidPrice2) or "10"
    superMiniMushroomMidPrice34 = get_capsule_value(superMiniMushroomMidPrice34) or "10"
    superMiniMushroomLatePrice1 = get_capsule_value(superMiniMushroomLatePrice1) or "10"
    superMiniMushroomLatePrice2 = get_capsule_value(superMiniMushroomLatePrice2) or "10"
    superMiniMushroomLatePrice34 = get_capsule_value(superMiniMushroomLatePrice34) or "10"

    # Super Mega Mushroom
    superMegaMushroomEarlyPrice1 = get_capsule_value(superMegaMushroomEarlyPrice1) or "15"
    superMegaMushroomEarlyPrice2 = get_capsule_value(superMegaMushroomEarlyPrice2) or "15"
    superMegaMushroomEarlyPrice34 = get_capsule_value(superMegaMushroomEarlyPrice34) or "15"
    superMegaMushroomMidPrice1 = get_capsule_value(superMegaMushroomMidPrice1) or "15"
    superMegaMushroomMidPrice2 = get_capsule_value(superMegaMushroomMidPrice2) or "15"
    superMegaMushroomMidPrice34 = get_capsule_value(superMegaMushroomMidPrice34) or "15"
    superMegaMushroomLatePrice1 = get_capsule_value(superMegaMushroomLatePrice1) or "15"
    superMegaMushroomLatePrice2 = get_capsule_value(superMegaMushroomLatePrice2) or "15"
    superMegaMushroomLatePrice34 = get_capsule_value(superMegaMushroomLatePrice34) or "15"

    # Mini Mega Hammer
    miniMegaHammerEarlyPrice1 = get_capsule_value(miniMegaHammerEarlyPrice1) or "10"
    miniMegaHammerEarlyPrice2 = get_capsule_value(miniMegaHammerEarlyPrice2) or "10"
    miniMegaHammerEarlyPrice34 = get_capsule_value(miniMegaHammerEarlyPrice34) or "10"
    miniMegaHammerMidPrice1 = get_capsule_value(miniMegaHammerMidPrice1) or "10"
    miniMegaHammerMidPrice2 = get_capsule_value(miniMegaHammerMidPrice2) or "10"
    miniMegaHammerMidPrice34 = get_capsule_value(miniMegaHammerMidPrice34) or "10"
    miniMegaHammerLatePrice1 = get_capsule_value(miniMegaHammerLatePrice1) or "10"
    miniMegaHammerLatePrice2 = get_capsule_value(miniMegaHammerLatePrice2) or "10"
    miniMegaHammerLatePrice34 = get_capsule_value(miniMegaHammerLatePrice34) or "10"

    # Warp Pipe
    warpPipeEarlyPrice1 = get_capsule_value(warpPipeEarlyPrice1) or "10"
    warpPipeEarlyPrice2 = get_capsule_value(warpPipeEarlyPrice2) or "10"
    warpPipeEarlyPrice34 = get_capsule_value(warpPipeEarlyPrice34) or "10"
    warpPipeMidPrice1 = get_capsule_value(warpPipeMidPrice1) or "10"
    warpPipeMidPrice2 = get_capsule_value(warpPipeMidPrice2) or "10"
    warpPipeMidPrice34 = get_capsule_value(warpPipeMidPrice34) or "10"
    warpPipeLatePrice1 = get_capsule_value(warpPipeLatePrice1) or "10"
    warpPipeLatePrice2 = get_capsule_value(warpPipeLatePrice2) or "10"
    warpPipeLatePrice34 = get_capsule_value(warpPipeLatePrice34) or "10"

    # Swap Card
    swapCardEarlyPrice1 = get_capsule_value(swapCardEarlyPrice1) or "15"
    swapCardEarlyPrice2 = get_capsule_value(swapCardEarlyPrice2) or "15"
    swapCardEarlyPrice34 = get_capsule_value(swapCardEarlyPrice34) or "15"
    swapCardMidPrice1 = get_capsule_value(swapCardMidPrice1) or "15"
    swapCardMidPrice2 = get_capsule_value(swapCardMidPrice2) or "15"
    swapCardMidPrice34 = get_capsule_value(swapCardMidPrice34) or "15"
    swapCardLatePrice1 = get_capsule_value(swapCardLatePrice1) or "15"
    swapCardLatePrice2 = get_capsule_value(swapCardLatePrice2) or "15"
    swapCardLatePrice34 = get_capsule_value(swapCardLatePrice34) or "15"

    # Sparky Sticker
    sparkyStickerEarlyPrice1 = get_capsule_value(sparkyStickerEarlyPrice1) or "5"
    sparkyStickerEarlyPrice2 = get_capsule_value(sparkyStickerEarlyPrice2) or "5"
    sparkyStickerEarlyPrice34 = get_capsule_value(sparkyStickerEarlyPrice34) or "5"
    sparkyStickerMidPrice1 = get_capsule_value(sparkyStickerMidPrice1) or "5"
    sparkyStickerMidPrice2 = get_capsule_value(sparkyStickerMidPrice2) or "5"
    sparkyStickerMidPrice34 = get_capsule_value(sparkyStickerMidPrice34) or "5"
    sparkyStickerLatePrice1 = get_capsule_value(sparkyStickerLatePrice1) or "5"
    sparkyStickerLatePrice2 = get_capsule_value(sparkyStickerLatePrice2) or "5"
    sparkyStickerLatePrice34 = get_capsule_value(sparkyStickerLatePrice34) or "5"

    # Gaddlight
    gaddlightEarlyPrice1 = get_capsule_value(gaddlightEarlyPrice1) or "15"
    gaddlightEarlyPrice2 = get_capsule_value(gaddlightEarlyPrice2) or "15"
    gaddlightEarlyPrice34 = get_capsule_value(gaddlightEarlyPrice34) or "15"
    gaddlightMidPrice1 = get_capsule_value(gaddlightMidPrice1) or "15"
    gaddlightMidPrice2 = get_capsule_value(gaddlightMidPrice2) or "15"
    gaddlightMidPrice34 = get_capsule_value(gaddlightMidPrice34) or "15"
    gaddlightLatePrice1 = get_capsule_value(gaddlightLatePrice1) or "15"
    gaddlightLatePrice2 = get_capsule_value(gaddlightLatePrice2) or "15"
    gaddlightLatePrice34 = get_capsule_value(gaddlightLatePrice34) or "15"

    # Chomp Call
    chompCallEarlyPrice1 = get_capsule_value(chompCallEarlyPrice1) or "10"
    chompCallEarlyPrice2 = get_capsule_value(chompCallEarlyPrice2) or "10"
    chompCallEarlyPrice34 = get_capsule_value(chompCallEarlyPrice34) or "10"
    chompCallMidPrice1 = get_capsule_value(chompCallMidPrice1) or "10"
    chompCallMidPrice2 = get_capsule_value(chompCallMidPrice2) or "10"
    chompCallMidPrice34 = get_capsule_value(chompCallMidPrice34) or "10"
    chompCallLatePrice1 = get_capsule_value(chompCallLatePrice1) or "10"
    chompCallLatePrice2 = get_capsule_value(chompCallLatePrice2) or "10"
    chompCallLatePrice34 = get_capsule_value(chompCallLatePrice34) or "10"

    # Bowser Suit
    bowserSuitEarlyPrice1 = get_capsule_value(bowserSuitEarlyPrice1) or "12"
    bowserSuitEarlyPrice2 = get_capsule_value(bowserSuitEarlyPrice2) or "12"
    bowserSuitEarlyPrice34 = get_capsule_value(bowserSuitEarlyPrice34) or "12"
    bowserSuitMidPrice1 = get_capsule_value(bowserSuitMidPrice1) or "12"
    bowserSuitMidPrice2 = get_capsule_value(bowserSuitMidPrice2) or "12"
    bowserSuitMidPrice34 = get_capsule_value(bowserSuitMidPrice34) or "12"
    bowserSuitLatePrice1 = get_capsule_value(bowserSuitLatePrice1) or "12"
    bowserSuitLatePrice2 = get_capsule_value(bowserSuitLatePrice2) or "12"
    bowserSuitLatePrice34 = get_capsule_value(bowserSuitLatePrice34) or "12"

    # Crystal Ball
    crystalBallEarlyPrice1 = get_capsule_value(crystalBallEarlyPrice1) or "25"
    crystalBallEarlyPrice2 = get_capsule_value(crystalBallEarlyPrice2) or "25"
    crystalBallEarlyPrice34 = get_capsule_value(crystalBallEarlyPrice34) or "25"
    crystalBallMidPrice1 = get_capsule_value(crystalBallMidPrice1) or "25"
    crystalBallMidPrice2 = get_capsule_value(crystalBallMidPrice2) or "25"
    crystalBallMidPrice34 = get_capsule_value(crystalBallMidPrice34) or "25"
    crystalBallLatePrice1 = get_capsule_value(crystalBallLatePrice1) or "25"
    crystalBallLatePrice2 = get_capsule_value(crystalBallLatePrice2) or "25"
    crystalBallLatePrice34 = get_capsule_value(crystalBallLatePrice34) or "25"

    # Magic Lamp
    magicLampEarlyPrice1 = get_capsule_value(magicLampEarlyPrice1) or "30"
    magicLampEarlyPrice2 = get_capsule_value(magicLampEarlyPrice2) or "30"
    magicLampEarlyPrice34 = get_capsule_value(magicLampEarlyPrice34) or "30"
    magicLampMidPrice1 = get_capsule_value(magicLampMidPrice1) or "30"
    magicLampMidPrice2 = get_capsule_value(magicLampMidPrice2) or "30"
    magicLampMidPrice34 = get_capsule_value(magicLampMidPrice34) or "30"
    magicLampLatePrice1 = get_capsule_value(magicLampLatePrice1) or "30"
    magicLampLatePrice2 = get_capsule_value(magicLampLatePrice2) or "30"
    magicLampLatePrice34 = get_capsule_value(magicLampLatePrice34) or "30"

    # Item Bag
    itemBagEarlyPrice1 = get_capsule_value(itemBagEarlyPrice1) or "30"
    itemBagEarlyPrice2 = get_capsule_value(itemBagEarlyPrice2) or "30"
    itemBagEarlyPrice34 = get_capsule_value(itemBagEarlyPrice34) or "30"
    itemBagMidPrice1 = get_capsule_value(itemBagMidPrice1) or "30"
    itemBagMidPrice2 = get_capsule_value(itemBagMidPrice2) or "30"
    itemBagMidPrice34 = get_capsule_value(itemBagMidPrice34) or "30"
    itemBagLatePrice1 = get_capsule_value(itemBagLatePrice1) or "30"
    itemBagLatePrice2 = get_capsule_value(itemBagLatePrice2) or "30"
    itemBagLatePrice34 = get_capsule_value(itemBagLatePrice34) or "30"

    # Mushroom: DX
    mushroomEarlyPrice1 = get_capsule_value(mushroomEarlyPrice1) or "5"
    mushroomEarlyPrice2 = get_capsule_value(mushroomEarlyPrice2) or "5"
    mushroomEarlyPrice34 = get_capsule_value(mushroomEarlyPrice34) or "5"
    mushroomMidPrice1 = get_capsule_value(mushroomMidPrice1) or "5"
    mushroomMidPrice2 = get_capsule_value(mushroomMidPrice2) or "5"
    mushroomMidPrice34 = get_capsule_value(mushroomMidPrice34) or "5"
    mushroomLatePrice1 = get_capsule_value(mushroomLatePrice1) or "5"
    mushroomLatePrice2 = get_capsule_value(mushroomLatePrice2) or "5"
    mushroomLatePrice34 = get_capsule_value(mushroomLatePrice34) or "5"

    # Golden Mushroom: DX
    goldenMushroomEarlyPrice1 = get_capsule_value(goldenMushroomEarlyPrice1) or "10"
    goldenMushroomEarlyPrice2 = get_capsule_value(goldenMushroomEarlyPrice2) or "10"
    goldenMushroomEarlyPrice34 = get_capsule_value(goldenMushroomEarlyPrice34) or "10"
    goldenMushroomMidPrice1 = get_capsule_value(goldenMushroomMidPrice1) or "10"
    goldenMushroomMidPrice2 = get_capsule_value(goldenMushroomMidPrice2) or "10"
    goldenMushroomMidPrice34 = get_capsule_value(goldenMushroomMidPrice34) or "10"
    goldenMushroomLatePrice1 = get_capsule_value(goldenMushroomLatePrice1) or "10"
    goldenMushroomLatePrice2 = get_capsule_value(goldenMushroomLatePrice2) or "10"
    goldenMushroomLatePrice34 = get_capsule_value(goldenMushroomLatePrice34) or "10"

    # Reverse Mushroom: DX
    reverseMushroomEarlyPrice1 = get_capsule_value(reverseMushroomEarlyPrice1) or "15"
    reverseMushroomEarlyPrice2 = get_capsule_value(reverseMushroomEarlyPrice2) or "15"
    reverseMushroomEarlyPrice34 = get_capsule_value(reverseMushroomEarlyPrice34) or "15"
    reverseMushroomMidPrice1 = get_capsule_value(reverseMushroomMidPrice1) or "15"
    reverseMushroomMidPrice2 = get_capsule_value(reverseMushroomMidPrice2) or "15"
    reverseMushroomMidPrice34 = get_capsule_value(reverseMushroomMidPrice34) or "15"
    reverseMushroomLatePrice1 = get_capsule_value(reverseMushroomLatePrice1) or "15"
    reverseMushroomLatePrice2 = get_capsule_value(reverseMushroomLatePrice2) or "15"
    reverseMushroomLatePrice34 = get_capsule_value(reverseMushroomLatePrice34) or "15"

    # Poison Mushroom: DX
    poisonMushroomEarlyPrice1 = get_capsule_value(poisonMushroomEarlyPrice1) or "5"
    poisonMushroomEarlyPrice2 = get_capsule_value(poisonMushroomEarlyPrice2) or "5"
    poisonMushroomEarlyPrice34 = get_capsule_value(poisonMushroomEarlyPrice34) or "5"
    poisonMushroomMidPrice1 = get_capsule_value(poisonMushroomMidPrice1) or "5"
    poisonMushroomMidPrice2 = get_capsule_value(poisonMushroomMidPrice2) or "5"
    poisonMushroomMidPrice34 = get_capsule_value(poisonMushroomMidPrice34) or "5"
    poisonMushroomLatePrice1 = get_capsule_value(poisonMushroomLatePrice1) or "5"
    poisonMushroomLatePrice2 = get_capsule_value(poisonMushroomLatePrice2) or "5"
    poisonMushroomLatePrice34 = get_capsule_value(poisonMushroomLatePrice34) or "5"
    
    # Bowser Phone: DX
    bowserPhoneEarlyPrice1 = get_capsule_value(bowserPhoneEarlyPrice1) or "10"
    bowserPhoneEarlyPrice2 = get_capsule_value(bowserPhoneEarlyPrice2) or "10"
    bowserPhoneEarlyPrice34 = get_capsule_value(bowserPhoneEarlyPrice34) or "10"
    bowserPhoneMidPrice1 = get_capsule_value(bowserPhoneMidPrice1) or "10"
    bowserPhoneMidPrice2 = get_capsule_value(bowserPhoneMidPrice2) or "10"
    bowserPhoneMidPrice34 = get_capsule_value(bowserPhoneMidPrice34) or "10"
    bowserPhoneLatePrice1 = get_capsule_value(bowserPhoneLatePrice1) or "10"
    bowserPhoneLatePrice2 = get_capsule_value(bowserPhoneLatePrice2) or "10"
    bowserPhoneLatePrice34 = get_capsule_value(bowserPhoneLatePrice34) or "10"

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyPrice1 = get_capsule_value(triplePoisonMushroomEarlyPrice1) or "15"
    triplePoisonMushroomEarlyPrice2 = get_capsule_value(triplePoisonMushroomEarlyPrice2) or "15"
    triplePoisonMushroomEarlyPrice34 = get_capsule_value(triplePoisonMushroomEarlyPrice34) or "15"
    triplePoisonMushroomMidPrice1 = get_capsule_value(triplePoisonMushroomMidPrice1) or "15"
    triplePoisonMushroomMidPrice2 = get_capsule_value(triplePoisonMushroomMidPrice2) or "15"
    triplePoisonMushroomMidPrice34 = get_capsule_value(triplePoisonMushroomMidPrice34) or "15"
    triplePoisonMushroomLatePrice1 = get_capsule_value(triplePoisonMushroomLatePrice1) or "15"
    triplePoisonMushroomLatePrice2 = get_capsule_value(triplePoisonMushroomLatePrice2) or "15"
    triplePoisonMushroomLatePrice34 = get_capsule_value(triplePoisonMushroomLatePrice34) or "15"

    # Celluar Shopper: DX
    celluarShopperEarlyPrice1 = get_capsule_value(celluarShopperEarlyPrice1) or "5"
    celluarShopperEarlyPrice2 = get_capsule_value(celluarShopperEarlyPrice2) or "5"
    celluarShopperEarlyPrice34 = get_capsule_value(celluarShopperEarlyPrice34) or "5"
    celluarShopperMidPrice1 = get_capsule_value(celluarShopperMidPrice1) or "5"
    celluarShopperMidPrice2 = get_capsule_value(celluarShopperMidPrice2) or "5"
    celluarShopperMidPrice34 = get_capsule_value(celluarShopperMidPrice34) or "5"
    celluarShopperLatePrice1 = get_capsule_value(celluarShopperLatePrice1) or "5"
    celluarShopperLatePrice2 = get_capsule_value(celluarShopperLatePrice2) or "5"
    celluarShopperLatePrice34 = get_capsule_value(celluarShopperLatePrice34) or "5"

    # Skeleton Key: DX
    skeletonKeyEarlyPrice1 = get_capsule_value(skeletonKeyEarlyPrice1) or "5"
    skeletonKeyEarlyPrice2 = get_capsule_value(skeletonKeyEarlyPrice2) or "5"
    skeletonKeyEarlyPrice34 = get_capsule_value(skeletonKeyEarlyPrice34) or "5"
    skeletonKeyMidPrice1 = get_capsule_value(skeletonKeyMidPrice1) or "5"
    skeletonKeyMidPrice2 = get_capsule_value(skeletonKeyMidPrice2) or "5"
    skeletonKeyMidPrice34 = get_capsule_value(skeletonKeyMidPrice34) or "5"
    skeletonKeyLatePrice1 = get_capsule_value(skeletonKeyLatePrice1) or "5"
    skeletonKeyLatePrice2 = get_capsule_value(skeletonKeyLatePrice2) or "5"
    skeletonKeyLatePrice34 = get_capsule_value(skeletonKeyLatePrice34) or "5"

    # Plunder Chest: DX
    plunderChestEarlyPrice1 = get_capsule_value(plunderChestEarlyPrice1) or "15"
    plunderChestEarlyPrice2 = get_capsule_value(plunderChestEarlyPrice2) or "15"
    plunderChestEarlyPrice34 = get_capsule_value(plunderChestEarlyPrice34) or "15"
    plunderChestMidPrice1 = get_capsule_value(plunderChestMidPrice1) or "15"
    plunderChestMidPrice2 = get_capsule_value(plunderChestMidPrice2) or "15"
    plunderChestMidPrice34 = get_capsule_value(plunderChestMidPrice34) or "15"
    plunderChestLatePrice1 = get_capsule_value(plunderChestLatePrice1) or "15"
    plunderChestLatePrice2 = get_capsule_value(plunderChestLatePrice2) or "15"
    plunderChestLatePrice34 = get_capsule_value(plunderChestLatePrice34) or "15"

    # Gaddbrush: DX
    gaddbrushEarlyPrice1 = get_capsule_value(gaddbrushEarlyPrice1) or "15"
    gaddbrushEarlyPrice2 = get_capsule_value(gaddbrushEarlyPrice2) or "15"
    gaddbrushEarlyPrice34 = get_capsule_value(gaddbrushEarlyPrice34) or "15"
    gaddbrushMidPrice1 = get_capsule_value(gaddbrushMidPrice1) or "15"
    gaddbrushMidPrice2 = get_capsule_value(gaddbrushMidPrice2) or "15"
    gaddbrushMidPrice34 = get_capsule_value(gaddbrushMidPrice34) or "15"
    gaddbrushLatePrice1 = get_capsule_value(gaddbrushLatePrice1) or "15"
    gaddbrushLatePrice2 = get_capsule_value(gaddbrushLatePrice2) or "15"
    gaddbrushLatePrice34 = get_capsule_value(gaddbrushLatePrice34) or "15"

    # Warp Block: DX
    warpBlockEarlyPrice1 = get_capsule_value(warpBlockEarlyPrice1) or "5"
    warpBlockEarlyPrice2 = get_capsule_value(warpBlockEarlyPrice2) or "5"
    warpBlockEarlyPrice34 = get_capsule_value(warpBlockEarlyPrice34) or "5"
    warpBlockMidPrice1 = get_capsule_value(warpBlockMidPrice1) or "5"
    warpBlockMidPrice2 = get_capsule_value(warpBlockMidPrice2) or "5"
    warpBlockMidPrice34 = get_capsule_value(warpBlockMidPrice34) or "5"
    warpBlockLatePrice1 = get_capsule_value(warpBlockLatePrice1) or "5"
    warpBlockLatePrice2 = get_capsule_value(warpBlockLatePrice2) or "5"
    warpBlockLatePrice34 = get_capsule_value(warpBlockLatePrice34) or "5"

    # Fly Guy: DX
    flyGuyEarlyPrice1 = get_capsule_value(flyGuyEarlyPrice1) or "12"
    flyGuyEarlyPrice2 = get_capsule_value(flyGuyEarlyPrice2) or "12"
    flyGuyEarlyPrice34 = get_capsule_value(flyGuyEarlyPrice34) or "12"
    flyGuyMidPrice1 = get_capsule_value(flyGuyMidPrice1) or "12"
    flyGuyMidPrice2 = get_capsule_value(flyGuyMidPrice2) or "12"
    flyGuyMidPrice34 = get_capsule_value(flyGuyMidPrice34) or "12"
    flyGuyLatePrice1 = get_capsule_value(flyGuyLatePrice1) or "12"
    flyGuyLatePrice2 = get_capsule_value(flyGuyLatePrice2) or "12"
    flyGuyLatePrice34 = get_capsule_value(flyGuyLatePrice34) or "12"

    # Plus Block: DX
    plusBlockEarlyPrice1 = get_capsule_value(plusBlockEarlyPrice1) or "10"
    plusBlockEarlyPrice2 = get_capsule_value(plusBlockEarlyPrice2) or "10"
    plusBlockEarlyPrice34 = get_capsule_value(plusBlockEarlyPrice34) or "10"
    plusBlockMidPrice1 = get_capsule_value(plusBlockMidPrice1) or "10"
    plusBlockMidPrice2 = get_capsule_value(plusBlockMidPrice2) or "10"
    plusBlockMidPrice34 = get_capsule_value(plusBlockMidPrice34) or "10"
    plusBlockLatePrice1 = get_capsule_value(plusBlockLatePrice1) or "10"
    plusBlockLatePrice2 = get_capsule_value(plusBlockLatePrice2) or "10"
    plusBlockLatePrice34 = get_capsule_value(plusBlockLatePrice34) or "10"

    # Minus Block: DX
    minusBlockEarlyPrice1 = get_capsule_value(minusBlockEarlyPrice1) or "10"
    minusBlockEarlyPrice2 = get_capsule_value(minusBlockEarlyPrice2) or "10"
    minusBlockEarlyPrice34 = get_capsule_value(minusBlockEarlyPrice34) or "10"
    minusBlockMidPrice1 = get_capsule_value(minusBlockMidPrice1) or "10"
    minusBlockMidPrice2 = get_capsule_value(minusBlockMidPrice2) or "10"
    minusBlockMidPrice34 = get_capsule_value(minusBlockMidPrice34) or "10"
    minusBlockLatePrice1 = get_capsule_value(minusBlockLatePrice1) or "10"
    minusBlockLatePrice2 = get_capsule_value(minusBlockLatePrice2) or "10"
    minusBlockLatePrice34 = get_capsule_value(minusBlockLatePrice34) or "10"

    # Speed Block: DX
    speedBlockEarlyPrice1 = get_capsule_value(speedBlockEarlyPrice1) or "12"
    speedBlockEarlyPrice2 = get_capsule_value(speedBlockEarlyPrice2) or "12"
    speedBlockEarlyPrice34 = get_capsule_value(speedBlockEarlyPrice34) or "12"
    speedBlockMidPrice1 = get_capsule_value(speedBlockMidPrice1) or "12"
    speedBlockMidPrice2 = get_capsule_value(speedBlockMidPrice2) or "12"
    speedBlockMidPrice34 = get_capsule_value(speedBlockMidPrice34) or "12"
    speedBlockLatePrice1 = get_capsule_value(speedBlockLatePrice1) or "12"
    speedBlockLatePrice2 = get_capsule_value(speedBlockLatePrice2) or "12"
    speedBlockLatePrice34 = get_capsule_value(speedBlockLatePrice34) or "12"

    # Slow Block: DX
    slowBlockEarlyPrice1 = get_capsule_value(slowBlockEarlyPrice1) or "12"
    slowBlockEarlyPrice2 = get_capsule_value(slowBlockEarlyPrice2) or "12"
    slowBlockEarlyPrice34 = get_capsule_value(slowBlockEarlyPrice34) or "12"
    slowBlockMidPrice1 = get_capsule_value(slowBlockMidPrice1) or "12"
    slowBlockMidPrice2 = get_capsule_value(slowBlockMidPrice2) or "12"
    slowBlockMidPrice34 = get_capsule_value(slowBlockMidPrice34) or "12"
    slowBlockLatePrice1 = get_capsule_value(slowBlockLatePrice1) or "12"
    slowBlockLatePrice2 = get_capsule_value(slowBlockLatePrice2) or "12"
    slowBlockLatePrice34 = get_capsule_value(slowBlockLatePrice34) or "12"

    # Hidden Block Card: DX
    hiddenBlockCardEarlyPrice1 = get_capsule_value(hiddenBlockCardEarlyPrice1) or "40"
    hiddenBlockCardEarlyPrice2 = get_capsule_value(hiddenBlockCardEarlyPrice2) or "40"
    hiddenBlockCardEarlyPrice34 = get_capsule_value(hiddenBlockCardEarlyPrice34) or "40"
    hiddenBlockCardMidPrice1 = get_capsule_value(hiddenBlockCardMidPrice1) or "40"
    hiddenBlockCardMidPrice2 = get_capsule_value(hiddenBlockCardMidPrice2) or "40"
    hiddenBlockCardMidPrice34 = get_capsule_value(hiddenBlockCardMidPrice34) or "40"
    hiddenBlockCardLatePrice1 = get_capsule_value(hiddenBlockCardLatePrice1) or "40"
    hiddenBlockCardLatePrice2 = get_capsule_value(hiddenBlockCardLatePrice2) or "40"
    hiddenBlockCardLatePrice34 = get_capsule_value(hiddenBlockCardLatePrice34) or "40"

    # Barter Box: DX
    barterBoxEarlyPrice1 = get_capsule_value(barterBoxEarlyPrice1) or "40"
    barterBoxEarlyPrice2 = get_capsule_value(barterBoxEarlyPrice2) or "40"
    barterBoxEarlyPrice34 = get_capsule_value(barterBoxEarlyPrice34) or "40"
    barterBoxMidPrice1 = get_capsule_value(barterBoxMidPrice1) or "40"
    barterBoxMidPrice2 = get_capsule_value(barterBoxMidPrice2) or "40"
    barterBoxMidPrice34 = get_capsule_value(barterBoxMidPrice34) or "40"
    barterBoxLatePrice1 = get_capsule_value(barterBoxLatePrice1) or "40"
    barterBoxLatePrice2 = get_capsule_value(barterBoxLatePrice2) or "40"
    barterBoxLatePrice34 = get_capsule_value(barterBoxLatePrice34) or "40"

    # Super Warp Pipe: DX
    superWarpPipeEarlyPrice1 = get_capsule_value(superWarpPipeEarlyPrice1) or "40"
    superWarpPipeEarlyPrice2 = get_capsule_value(superWarpPipeEarlyPrice2) or "40"
    superWarpPipeEarlyPrice34 = get_capsule_value(superWarpPipeEarlyPrice34) or "40"
    superWarpPipeMidPrice1 = get_capsule_value(superWarpPipeMidPrice1) or "40"
    superWarpPipeMidPrice2 = get_capsule_value(superWarpPipeMidPrice2) or "40"
    superWarpPipeMidPrice34 = get_capsule_value(superWarpPipeMidPrice34) or "40"
    superWarpPipeLatePrice1 = get_capsule_value(superWarpPipeLatePrice1) or "40"
    superWarpPipeLatePrice2 = get_capsule_value(superWarpPipeLatePrice2) or "40"
    superWarpPipeLatePrice34 = get_capsule_value(superWarpPipeLatePrice34) or "40"

    # Chance Time Charm: DX
    chanceTimeCharmEarlyPrice1 = get_capsule_value(chanceTimeCharmEarlyPrice1) or "40"
    chanceTimeCharmEarlyPrice2 = get_capsule_value(chanceTimeCharmEarlyPrice2) or "40"
    chanceTimeCharmEarlyPrice34 = get_capsule_value(chanceTimeCharmEarlyPrice34) or "40"
    chanceTimeCharmMidPrice1 = get_capsule_value(chanceTimeCharmMidPrice1) or "40"
    chanceTimeCharmMidPrice2 = get_capsule_value(chanceTimeCharmMidPrice2) or "40"
    chanceTimeCharmMidPrice34 = get_capsule_value(chanceTimeCharmMidPrice34) or "40"
    chanceTimeCharmLatePrice1 = get_capsule_value(chanceTimeCharmLatePrice1) or "40"
    chanceTimeCharmLatePrice2 = get_capsule_value(chanceTimeCharmLatePrice2) or "40"
    chanceTimeCharmLatePrice34 = get_capsule_value(chanceTimeCharmLatePrice34) or "40"

    # Wacky Watch: DX
    wackyWatchEarlyPrice1 = get_capsule_value(wackyWatchEarlyPrice1) or "100"
    wackyWatchEarlyPrice2 = get_capsule_value(wackyWatchEarlyPrice2) or "100"
    wackyWatchEarlyPrice34 = get_capsule_value(wackyWatchEarlyPrice34) or "100"
    wackyWatchMidPrice1 = get_capsule_value(wackyWatchMidPrice1) or "100"
    wackyWatchMidPrice2 = get_capsule_value(wackyWatchMidPrice2) or "100"
    wackyWatchMidPrice34 = get_capsule_value(wackyWatchMidPrice34) or "100"
    wackyWatchLatePrice1 = get_capsule_value(wackyWatchLatePrice1) or "100"
    wackyWatchLatePrice2 = get_capsule_value(wackyWatchLatePrice2) or "100"
    wackyWatchLatePrice34 = get_capsule_value(wackyWatchLatePrice34) or "100"
    
    minCoins = find_lowest_integer(*[
        int(miniMushroomEarlyPrice1), int(miniMushroomEarlyPrice2), int(miniMushroomEarlyPrice34), 
        int(miniMushroomMidPrice1), int(miniMushroomMidPrice2), int(miniMushroomMidPrice34),
        int(miniMushroomLatePrice1), int(miniMushroomLatePrice2), int(miniMushroomLatePrice34),
        int(megaMushroomEarlyPrice1), int(megaMushroomEarlyPrice2), int(megaMushroomEarlyPrice34), 
        int(megaMushroomMidPrice1), int(megaMushroomMidPrice2), int(megaMushroomMidPrice34),
        int(megaMushroomLatePrice1), int(megaMushroomLatePrice2), int(megaMushroomLatePrice34),
        int(superMiniMushroomEarlyPrice1), int(superMiniMushroomEarlyPrice2), int(superMiniMushroomEarlyPrice34),
        int(superMiniMushroomMidPrice1), int(superMiniMushroomMidPrice2), int(superMiniMushroomMidPrice34),
        int(superMiniMushroomLatePrice1), int(superMiniMushroomLatePrice2), int(superMiniMushroomLatePrice34),
        int(superMegaMushroomEarlyPrice1), int(superMegaMushroomEarlyPrice2), int(superMegaMushroomEarlyPrice34),
        int(superMegaMushroomMidPrice1), int(superMegaMushroomMidPrice2), int(superMegaMushroomMidPrice34),
        int(superMegaMushroomLatePrice1), int(superMegaMushroomLatePrice2), int(superMegaMushroomLatePrice34),
        int(miniMegaHammerEarlyPrice1), int(miniMegaHammerEarlyPrice2), int(miniMegaHammerEarlyPrice34),
        int(miniMegaHammerMidPrice1), int(miniMegaHammerMidPrice2), int(miniMegaHammerMidPrice34),
        int(miniMegaHammerLatePrice1), int(miniMegaHammerLatePrice2), int(miniMegaHammerLatePrice34),
        int(warpPipeEarlyPrice1), int(warpPipeEarlyPrice2), int(warpPipeEarlyPrice34),
        int(warpPipeMidPrice1), int(warpPipeMidPrice2), int(warpPipeMidPrice34),
        int(warpPipeLatePrice1), int(warpPipeLatePrice2), int(warpPipeLatePrice34),
        int(swapCardEarlyPrice1), int(swapCardEarlyPrice2), int(swapCardEarlyPrice34),
        int(swapCardMidPrice1), int(swapCardMidPrice2), int(swapCardMidPrice34),
        int(swapCardLatePrice1), int(swapCardLatePrice2), int(swapCardLatePrice34),
        int(sparkyStickerEarlyPrice1), int(sparkyStickerEarlyPrice2), int(sparkyStickerEarlyPrice34),
        int(sparkyStickerMidPrice1), int(sparkyStickerMidPrice2), int(sparkyStickerMidPrice34),
        int(sparkyStickerLatePrice1), int(sparkyStickerLatePrice2), int(sparkyStickerLatePrice34),
        int(gaddlightEarlyPrice1), int(gaddlightEarlyPrice2), int(gaddlightEarlyPrice34),
        int(gaddlightMidPrice1), int(gaddlightMidPrice2), int(gaddlightMidPrice34),
        int(gaddlightLatePrice1), int(gaddlightLatePrice2), int(gaddlightLatePrice34),
        int(chompCallEarlyPrice1), int(chompCallEarlyPrice2), int(chompCallEarlyPrice34),
        int(chompCallMidPrice1), int(chompCallMidPrice2), int(chompCallMidPrice34),
        int(chompCallLatePrice1), int(chompCallLatePrice2), int(chompCallLatePrice34),
        int(bowserSuitEarlyPrice1), int(bowserSuitEarlyPrice2), int(bowserSuitEarlyPrice34),
        int(bowserSuitMidPrice1), int(bowserSuitMidPrice2), int(bowserSuitMidPrice34),
        int(bowserSuitLatePrice1), int(bowserSuitLatePrice2), int(bowserSuitLatePrice34),
        int(crystalBallEarlyPrice1), int(crystalBallEarlyPrice2), int(crystalBallEarlyPrice34),
        int(crystalBallMidPrice1), int(crystalBallMidPrice2), int(crystalBallMidPrice34),
        int(crystalBallLatePrice1), int(crystalBallLatePrice2), int(crystalBallLatePrice34),
        int(magicLampEarlyPrice1), int(magicLampEarlyPrice2), int(magicLampEarlyPrice34),
        int(magicLampMidPrice1), int(magicLampMidPrice2), int(magicLampMidPrice34),
        int(magicLampLatePrice1), int(magicLampLatePrice2), int(magicLampLatePrice34),
        int(itemBagEarlyPrice1), int(itemBagEarlyPrice2), int(itemBagEarlyPrice34),
        int(itemBagMidPrice1), int(itemBagMidPrice2), int(itemBagMidPrice34),
        int(itemBagLatePrice1), int(itemBagLatePrice2), int(itemBagLatePrice34),
        int(mushroomEarlyPrice1), int(mushroomEarlyPrice2), int(mushroomEarlyPrice34),
        int(mushroomMidPrice1), int(mushroomMidPrice2), int(mushroomMidPrice34),
        int(mushroomLatePrice1), int(mushroomLatePrice2), int(mushroomLatePrice34),
        int(goldenMushroomEarlyPrice1), int(goldenMushroomEarlyPrice2), int(goldenMushroomEarlyPrice34),
        int(goldenMushroomMidPrice1), int(goldenMushroomMidPrice2), int(goldenMushroomMidPrice34),
        int(goldenMushroomLatePrice1), int(goldenMushroomLatePrice2), int(goldenMushroomLatePrice34),
        int(reverseMushroomEarlyPrice1), int(reverseMushroomEarlyPrice2), int(reverseMushroomEarlyPrice34),
        int(reverseMushroomMidPrice1), int(reverseMushroomMidPrice2), int(reverseMushroomMidPrice34),
        int(reverseMushroomLatePrice1), int(reverseMushroomLatePrice2), int(reverseMushroomLatePrice34),
        int(poisonMushroomEarlyPrice1), int(poisonMushroomEarlyPrice2), int(poisonMushroomEarlyPrice34),
        int(poisonMushroomMidPrice1), int(poisonMushroomMidPrice2), int(poisonMushroomMidPrice34),
        int(poisonMushroomLatePrice1), int(poisonMushroomLatePrice2), int(poisonMushroomLatePrice34),
        int(bowserPhoneEarlyPrice1), int(bowserPhoneEarlyPrice2), int(bowserPhoneEarlyPrice34),
        int(bowserPhoneMidPrice1), int(bowserPhoneMidPrice2), int(bowserPhoneMidPrice34),
        int(bowserPhoneLatePrice1), int(bowserPhoneLatePrice2), int(bowserPhoneLatePrice34),
        int(triplePoisonMushroomEarlyPrice1), int(triplePoisonMushroomEarlyPrice2), int(triplePoisonMushroomEarlyPrice34),
        int(triplePoisonMushroomMidPrice1), int(triplePoisonMushroomMidPrice2), int(triplePoisonMushroomMidPrice34),
        int(triplePoisonMushroomLatePrice1), int(triplePoisonMushroomLatePrice2), int(triplePoisonMushroomLatePrice34),
        int(celluarShopperEarlyPrice1), int(celluarShopperEarlyPrice2), int(celluarShopperEarlyPrice34),
        int(celluarShopperMidPrice1), int(celluarShopperMidPrice2), int(celluarShopperMidPrice34),
        int(celluarShopperLatePrice1), int(celluarShopperLatePrice2), int(celluarShopperLatePrice34),
        int(skeletonKeyEarlyPrice1), int(skeletonKeyEarlyPrice2), int(skeletonKeyEarlyPrice34),
        int(skeletonKeyMidPrice1), int(skeletonKeyMidPrice2), int(skeletonKeyMidPrice34),
        int(skeletonKeyLatePrice1), int(skeletonKeyLatePrice2), int(skeletonKeyLatePrice34),
        int(plunderChestEarlyPrice1), int(plunderChestEarlyPrice2), int(plunderChestEarlyPrice34),
        int(plunderChestMidPrice1), int(plunderChestMidPrice2), int(plunderChestMidPrice34),
        int(plunderChestLatePrice1), int(plunderChestLatePrice2), int(plunderChestLatePrice34),
        int(gaddbrushEarlyPrice1), int(gaddbrushEarlyPrice2), int(gaddbrushEarlyPrice34),
        int(gaddbrushMidPrice1), int(gaddbrushMidPrice2), int(gaddbrushMidPrice34),
        int(gaddbrushLatePrice1), int(gaddbrushLatePrice2), int(gaddbrushLatePrice34),
        int(warpBlockEarlyPrice1), int(warpBlockEarlyPrice2), int(warpBlockEarlyPrice34),
        int(warpBlockMidPrice1), int(warpBlockMidPrice2), int(warpBlockMidPrice34),
        int(warpBlockLatePrice1), int(warpBlockLatePrice2), int(warpBlockLatePrice34),
        int(flyGuyEarlyPrice1), int(flyGuyEarlyPrice2), int(flyGuyEarlyPrice34),
        int(flyGuyMidPrice1), int(flyGuyMidPrice2), int(flyGuyMidPrice34),
        int(flyGuyLatePrice1), int(flyGuyLatePrice2), int(flyGuyLatePrice34),
        int(plusBlockEarlyPrice1), int(plusBlockEarlyPrice2), int(plusBlockEarlyPrice34),
        int(plusBlockMidPrice1), int(plusBlockMidPrice2), int(plusBlockMidPrice34),
        int(plusBlockLatePrice1), int(plusBlockLatePrice2), int(plusBlockLatePrice34),
        int(minusBlockEarlyPrice1), int(minusBlockEarlyPrice2), int(minusBlockEarlyPrice34),
        int(minusBlockMidPrice1), int(minusBlockMidPrice2), int(minusBlockMidPrice34),
        int(minusBlockLatePrice1), int(minusBlockLatePrice2), int(minusBlockLatePrice34),
        int(speedBlockEarlyPrice1), int(speedBlockEarlyPrice2), int(speedBlockEarlyPrice34),
        int(speedBlockMidPrice1), int(speedBlockMidPrice2), int(speedBlockMidPrice34),
        int(speedBlockLatePrice1), int(speedBlockLatePrice2), int(speedBlockLatePrice34),
        int(slowBlockEarlyPrice1), int(slowBlockEarlyPrice2), int(slowBlockEarlyPrice34),
        int(slowBlockMidPrice1), int(slowBlockMidPrice2), int(slowBlockMidPrice34),
        int(slowBlockLatePrice1), int(slowBlockLatePrice2), int(slowBlockLatePrice34),
        int(hiddenBlockCardEarlyPrice1), int(hiddenBlockCardEarlyPrice2), int(hiddenBlockCardEarlyPrice34),
        int(hiddenBlockCardMidPrice1), int(hiddenBlockCardMidPrice2), int(hiddenBlockCardMidPrice34),
        int(hiddenBlockCardLatePrice1), int(hiddenBlockCardLatePrice2), int(hiddenBlockCardLatePrice34),
        int(barterBoxEarlyPrice1), int(barterBoxEarlyPrice2), int(barterBoxEarlyPrice34),
        int(barterBoxMidPrice1), int(barterBoxMidPrice2), int(barterBoxMidPrice34),
        int(barterBoxLatePrice1), int(barterBoxLatePrice2), int(barterBoxLatePrice34),
        int(superWarpPipeEarlyPrice1), int(superWarpPipeEarlyPrice2), int(superWarpPipeEarlyPrice34),
        int(superWarpPipeMidPrice1), int(superWarpPipeMidPrice2), int(superWarpPipeMidPrice34),
        int(superWarpPipeLatePrice1), int(superWarpPipeLatePrice2), int(superWarpPipeLatePrice34),
        int(chanceTimeCharmEarlyPrice1), int(chanceTimeCharmEarlyPrice2), int(chanceTimeCharmEarlyPrice34),
        int(chanceTimeCharmMidPrice1), int(chanceTimeCharmMidPrice2), int(chanceTimeCharmMidPrice34),
        int(chanceTimeCharmLatePrice1), int(chanceTimeCharmLatePrice2), int(chanceTimeCharmLatePrice34),
        int(wackyWatchEarlyPrice1), int(wackyWatchEarlyPrice2), int(wackyWatchEarlyPrice34),
        int(wackyWatchMidPrice1), int(wackyWatchMidPrice2), int(wackyWatchMidPrice34),
        int(wackyWatchLatePrice1), int(wackyWatchLatePrice2), int(wackyWatchLatePrice34)
    ])


    def convert_to_hex_weight(weight):
        try:
            weight_hex = hex(int(weight))
            if len(weight_hex) == 4:
                return weight_hex[2:]  # Remove '0x' prefix
            elif len(weight_hex) == 3:
                return "0" + weight_hex[2:]  # Add leading zero
            return weight_hex[2:]  # Return as is for other lengths
        except:
            return "00"  # Return default value on error


    # Mini Mushroom
    miniMushroomEarlyPrice1 = convert_to_hex_weight(miniMushroomEarlyPrice1)
    miniMushroomEarlyPrice2 = convert_to_hex_weight(miniMushroomEarlyPrice2)
    miniMushroomEarlyPrice34 = convert_to_hex_weight(miniMushroomEarlyPrice34)
    miniMushroomMidPrice1 = convert_to_hex_weight(miniMushroomMidPrice1)
    miniMushroomMidPrice2 = convert_to_hex_weight(miniMushroomMidPrice2)
    miniMushroomMidPrice34 = convert_to_hex_weight(miniMushroomMidPrice34)
    miniMushroomLatePrice1 = convert_to_hex_weight(miniMushroomLatePrice1)
    miniMushroomLatePrice2 = convert_to_hex_weight(miniMushroomLatePrice2)
    miniMushroomLatePrice34 = convert_to_hex_weight(miniMushroomLatePrice34)
    
    # Mega Mushroom
    megaMushroomEarlyPrice1 = convert_to_hex_weight(megaMushroomEarlyPrice1)
    megaMushroomEarlyPrice2 = convert_to_hex_weight(megaMushroomEarlyPrice2)
    megaMushroomEarlyPrice34 = convert_to_hex_weight(megaMushroomEarlyPrice34)
    megaMushroomMidPrice1 = convert_to_hex_weight(megaMushroomMidPrice1)
    megaMushroomMidPrice2 = convert_to_hex_weight(megaMushroomMidPrice2)
    megaMushroomMidPrice34 = convert_to_hex_weight(megaMushroomMidPrice34)
    megaMushroomLatePrice1 = convert_to_hex_weight(megaMushroomLatePrice1)
    megaMushroomLatePrice2 = convert_to_hex_weight(megaMushroomLatePrice2)
    megaMushroomLatePrice34 = convert_to_hex_weight(megaMushroomLatePrice34)

    # Super Mini Mushroom
    superMiniMushroomEarlyPrice1 = convert_to_hex_weight(superMiniMushroomEarlyPrice1)
    superMiniMushroomEarlyPrice2 = convert_to_hex_weight(superMiniMushroomEarlyPrice2)
    superMiniMushroomEarlyPrice34 = convert_to_hex_weight(superMiniMushroomEarlyPrice34)
    superMiniMushroomMidPrice1 = convert_to_hex_weight(superMiniMushroomMidPrice1)
    superMiniMushroomMidPrice2 = convert_to_hex_weight(superMiniMushroomMidPrice2)
    superMiniMushroomMidPrice34 = convert_to_hex_weight(superMiniMushroomMidPrice34)
    superMiniMushroomLatePrice1 = convert_to_hex_weight(superMiniMushroomLatePrice1)
    superMiniMushroomLatePrice2 = convert_to_hex_weight(superMiniMushroomLatePrice2)
    superMiniMushroomLatePrice34 = convert_to_hex_weight(superMiniMushroomLatePrice34)

    # Super Mega Mushroom
    superMegaMushroomEarlyPrice1 = convert_to_hex_weight(superMegaMushroomEarlyPrice1)
    superMegaMushroomEarlyPrice2 = convert_to_hex_weight(superMegaMushroomEarlyPrice2)
    superMegaMushroomEarlyPrice34 = convert_to_hex_weight(superMegaMushroomEarlyPrice34)
    superMegaMushroomMidPrice1 = convert_to_hex_weight(superMegaMushroomMidPrice1)
    superMegaMushroomMidPrice2 = convert_to_hex_weight(superMegaMushroomMidPrice2)
    superMegaMushroomMidPrice34 = convert_to_hex_weight(superMegaMushroomMidPrice34)
    superMegaMushroomLatePrice1 = convert_to_hex_weight(superMegaMushroomLatePrice1)
    superMegaMushroomLatePrice2 = convert_to_hex_weight(superMegaMushroomLatePrice2)
    superMegaMushroomLatePrice34 = convert_to_hex_weight(superMegaMushroomLatePrice34)

    # Mini Mega Hammer
    miniMegaHammerEarlyPrice1 = convert_to_hex_weight(miniMegaHammerEarlyPrice1)
    miniMegaHammerEarlyPrice2 = convert_to_hex_weight(miniMegaHammerEarlyPrice2)
    miniMegaHammerEarlyPrice34 = convert_to_hex_weight(miniMegaHammerEarlyPrice34)
    miniMegaHammerMidPrice1 = convert_to_hex_weight(miniMegaHammerMidPrice1)
    miniMegaHammerMidPrice2 = convert_to_hex_weight(miniMegaHammerMidPrice2)
    miniMegaHammerMidPrice34 = convert_to_hex_weight(miniMegaHammerMidPrice34)
    miniMegaHammerLatePrice1 = convert_to_hex_weight(miniMegaHammerLatePrice1)
    miniMegaHammerLatePrice2 = convert_to_hex_weight(miniMegaHammerLatePrice2)
    miniMegaHammerLatePrice34 = convert_to_hex_weight(miniMegaHammerLatePrice34)

    # Warp Pipe
    warpPipeEarlyPrice1 = convert_to_hex_weight(warpPipeEarlyPrice1)
    warpPipeEarlyPrice2 = convert_to_hex_weight(warpPipeEarlyPrice2)
    warpPipeEarlyPrice34 = convert_to_hex_weight(warpPipeEarlyPrice34)
    warpPipeMidPrice1 = convert_to_hex_weight(warpPipeMidPrice1)
    warpPipeMidPrice2 = convert_to_hex_weight(warpPipeMidPrice2)
    warpPipeMidPrice34 = convert_to_hex_weight(warpPipeMidPrice34)
    warpPipeLatePrice1 = convert_to_hex_weight(warpPipeLatePrice1)
    warpPipeLatePrice2 = convert_to_hex_weight(warpPipeLatePrice2)
    warpPipeLatePrice34 = convert_to_hex_weight(warpPipeLatePrice34)

    # Swap Card
    swapCardEarlyPrice1 = convert_to_hex_weight(swapCardEarlyPrice1)
    swapCardEarlyPrice2 = convert_to_hex_weight(swapCardEarlyPrice2)
    swapCardEarlyPrice34 = convert_to_hex_weight(swapCardEarlyPrice34)
    swapCardMidPrice1 = convert_to_hex_weight(swapCardMidPrice1)
    swapCardMidPrice2 = convert_to_hex_weight(swapCardMidPrice2)
    swapCardMidPrice34 = convert_to_hex_weight(swapCardMidPrice34)
    swapCardLatePrice1 = convert_to_hex_weight(swapCardLatePrice1)
    swapCardLatePrice2 = convert_to_hex_weight(swapCardLatePrice2)
    swapCardLatePrice34 = convert_to_hex_weight(swapCardLatePrice34)

    # Sparky Sticker
    sparkyStickerEarlyPrice1 = convert_to_hex_weight(sparkyStickerEarlyPrice1)
    sparkyStickerEarlyPrice2 = convert_to_hex_weight(sparkyStickerEarlyPrice2)
    sparkyStickerEarlyPrice34 = convert_to_hex_weight(sparkyStickerEarlyPrice34)
    sparkyStickerMidPrice1 = convert_to_hex_weight(sparkyStickerMidPrice1)
    sparkyStickerMidPrice2 = convert_to_hex_weight(sparkyStickerMidPrice2)
    sparkyStickerMidPrice34 = convert_to_hex_weight(sparkyStickerMidPrice34)
    sparkyStickerLatePrice1 = convert_to_hex_weight(sparkyStickerLatePrice1)
    sparkyStickerLatePrice2 = convert_to_hex_weight(sparkyStickerLatePrice2)
    sparkyStickerLatePrice34 = convert_to_hex_weight(sparkyStickerLatePrice34)

    # Gaddlight
    gaddlightEarlyPrice1 = convert_to_hex_weight(gaddlightEarlyPrice1)
    gaddlightEarlyPrice2 = convert_to_hex_weight(gaddlightEarlyPrice2)
    gaddlightEarlyPrice34 = convert_to_hex_weight(gaddlightEarlyPrice34)
    gaddlightMidPrice1 = convert_to_hex_weight(gaddlightMidPrice1)
    gaddlightMidPrice2 = convert_to_hex_weight(gaddlightMidPrice2)
    gaddlightMidPrice34 = convert_to_hex_weight(gaddlightMidPrice34)
    gaddlightLatePrice1 = convert_to_hex_weight(gaddlightLatePrice1)
    gaddlightLatePrice2 = convert_to_hex_weight(gaddlightLatePrice2)
    gaddlightLatePrice34 = convert_to_hex_weight(gaddlightLatePrice34)

    # Chomp Call
    chompCallEarlyPrice1 = convert_to_hex_weight(chompCallEarlyPrice1)
    chompCallEarlyPrice2 = convert_to_hex_weight(chompCallEarlyPrice2)
    chompCallEarlyPrice34 = convert_to_hex_weight(chompCallEarlyPrice34)
    chompCallMidPrice1 = convert_to_hex_weight(chompCallMidPrice1)
    chompCallMidPrice2 = convert_to_hex_weight(chompCallMidPrice2)
    chompCallMidPrice34 = convert_to_hex_weight(chompCallMidPrice34)
    chompCallLatePrice1 = convert_to_hex_weight(chompCallLatePrice1)
    chompCallLatePrice2 = convert_to_hex_weight(chompCallLatePrice2)
    chompCallLatePrice34 = convert_to_hex_weight(chompCallLatePrice34)

    # Bowser Suit
    bowserSuitEarlyPrice1 = convert_to_hex_weight(bowserSuitEarlyPrice1)
    bowserSuitEarlyPrice2 = convert_to_hex_weight(bowserSuitEarlyPrice2)
    bowserSuitEarlyPrice34 = convert_to_hex_weight(bowserSuitEarlyPrice34)
    bowserSuitMidPrice1 = convert_to_hex_weight(bowserSuitMidPrice1)
    bowserSuitMidPrice2 = convert_to_hex_weight(bowserSuitMidPrice2)
    bowserSuitMidPrice34 = convert_to_hex_weight(bowserSuitMidPrice34)
    bowserSuitLatePrice1 = convert_to_hex_weight(bowserSuitLatePrice1)
    bowserSuitLatePrice2 = convert_to_hex_weight(bowserSuitLatePrice2)
    bowserSuitLatePrice34 = convert_to_hex_weight(bowserSuitLatePrice34)

    # Crystal Ball
    crystalBallEarlyPrice1 = convert_to_hex_weight(crystalBallEarlyPrice1)
    crystalBallEarlyPrice2 = convert_to_hex_weight(crystalBallEarlyPrice2)
    crystalBallEarlyPrice34 = convert_to_hex_weight(crystalBallEarlyPrice34)
    crystalBallMidPrice1 = convert_to_hex_weight(crystalBallMidPrice1)
    crystalBallMidPrice2 = convert_to_hex_weight(crystalBallMidPrice2)
    crystalBallMidPrice34 = convert_to_hex_weight(crystalBallMidPrice34)
    crystalBallLatePrice1 = convert_to_hex_weight(crystalBallLatePrice1)
    crystalBallLatePrice2 = convert_to_hex_weight(crystalBallLatePrice2)
    crystalBallLatePrice34 = convert_to_hex_weight(crystalBallLatePrice34)

    # Magic Lamp
    magicLampEarlyPrice1 = convert_to_hex_weight(magicLampEarlyPrice1)
    magicLampEarlyPrice2 = convert_to_hex_weight(magicLampEarlyPrice2)
    magicLampEarlyPrice34 = convert_to_hex_weight(magicLampEarlyPrice34)
    magicLampMidPrice1 = convert_to_hex_weight(magicLampMidPrice1)
    magicLampMidPrice2 = convert_to_hex_weight(magicLampMidPrice2)
    magicLampMidPrice34 = convert_to_hex_weight(magicLampMidPrice34)
    magicLampLatePrice1 = convert_to_hex_weight(magicLampLatePrice1)
    magicLampLatePrice2 = convert_to_hex_weight(magicLampLatePrice2)
    magicLampLatePrice34 = convert_to_hex_weight(magicLampLatePrice34)

    # Item Bag
    itemBagEarlyPrice1 = convert_to_hex_weight(itemBagEarlyPrice1)
    itemBagEarlyPrice2 = convert_to_hex_weight(itemBagEarlyPrice2)
    itemBagEarlyPrice34 = convert_to_hex_weight(itemBagEarlyPrice34)
    itemBagMidPrice1 = convert_to_hex_weight(itemBagMidPrice1)
    itemBagMidPrice2 = convert_to_hex_weight(itemBagMidPrice2)
    itemBagMidPrice34 = convert_to_hex_weight(itemBagMidPrice34)
    itemBagLatePrice1 = convert_to_hex_weight(itemBagLatePrice1)
    itemBagLatePrice2 = convert_to_hex_weight(itemBagLatePrice2)
    itemBagLatePrice34 = convert_to_hex_weight(itemBagLatePrice34)

    # Mushroom: DX
    mushroomEarlyPrice1 = convert_to_hex_weight(mushroomEarlyPrice1)
    mushroomEarlyPrice2 = convert_to_hex_weight(mushroomEarlyPrice2)
    mushroomEarlyPrice34 = convert_to_hex_weight(mushroomEarlyPrice34)
    mushroomMidPrice1 = convert_to_hex_weight(mushroomMidPrice1)
    mushroomMidPrice2 = convert_to_hex_weight(mushroomMidPrice2)
    mushroomMidPrice34 = convert_to_hex_weight(mushroomMidPrice34)
    mushroomLatePrice1 = convert_to_hex_weight(mushroomLatePrice1)
    mushroomLatePrice2 = convert_to_hex_weight(mushroomLatePrice2)
    mushroomLatePrice34 = convert_to_hex_weight(mushroomLatePrice34)

    # Golden Mushroom: DX
    goldenMushroomEarlyPrice1 = convert_to_hex_weight(goldenMushroomEarlyPrice1)
    goldenMushroomEarlyPrice2 = convert_to_hex_weight(goldenMushroomEarlyPrice2)
    goldenMushroomEarlyPrice34 = convert_to_hex_weight(goldenMushroomEarlyPrice34)
    goldenMushroomMidPrice1 = convert_to_hex_weight(goldenMushroomMidPrice1)
    goldenMushroomMidPrice2 = convert_to_hex_weight(goldenMushroomMidPrice2)
    goldenMushroomMidPrice34 = convert_to_hex_weight(goldenMushroomMidPrice34)
    goldenMushroomLatePrice1 = convert_to_hex_weight(goldenMushroomLatePrice1)
    goldenMushroomLatePrice2 = convert_to_hex_weight(goldenMushroomLatePrice2)
    goldenMushroomLatePrice34 = convert_to_hex_weight(goldenMushroomLatePrice34)

    # Reverse Mushroom: DX
    reverseMushroomEarlyPrice1 = convert_to_hex_weight(reverseMushroomEarlyPrice1)
    reverseMushroomEarlyPrice2 = convert_to_hex_weight(reverseMushroomEarlyPrice2)
    reverseMushroomEarlyPrice34 = convert_to_hex_weight(reverseMushroomEarlyPrice34)
    reverseMushroomMidPrice1 = convert_to_hex_weight(reverseMushroomMidPrice1)
    reverseMushroomMidPrice2 = convert_to_hex_weight(reverseMushroomMidPrice2)
    reverseMushroomMidPrice34 = convert_to_hex_weight(reverseMushroomMidPrice34)
    reverseMushroomLatePrice1 = convert_to_hex_weight(reverseMushroomLatePrice1)
    reverseMushroomLatePrice2 = convert_to_hex_weight(reverseMushroomLatePrice2)
    reverseMushroomLatePrice34 = convert_to_hex_weight(reverseMushroomLatePrice34)

    # Poison Mushroom: DX
    poisonMushroomEarlyPrice1 = convert_to_hex_weight(poisonMushroomEarlyPrice1)
    poisonMushroomEarlyPrice2 = convert_to_hex_weight(poisonMushroomEarlyPrice2)
    poisonMushroomEarlyPrice34 = convert_to_hex_weight(poisonMushroomEarlyPrice34)
    poisonMushroomMidPrice1 = convert_to_hex_weight(poisonMushroomMidPrice1)
    poisonMushroomMidPrice2 = convert_to_hex_weight(poisonMushroomMidPrice2)
    poisonMushroomMidPrice34 = convert_to_hex_weight(poisonMushroomMidPrice34)
    poisonMushroomLatePrice1 = convert_to_hex_weight(poisonMushroomLatePrice1)
    poisonMushroomLatePrice2 = convert_to_hex_weight(poisonMushroomLatePrice2)
    poisonMushroomLatePrice34 = convert_to_hex_weight(poisonMushroomLatePrice34)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyPrice1 = convert_to_hex_weight(triplePoisonMushroomEarlyPrice1)
    triplePoisonMushroomEarlyPrice2 = convert_to_hex_weight(triplePoisonMushroomEarlyPrice2)
    triplePoisonMushroomEarlyPrice34 = convert_to_hex_weight(triplePoisonMushroomEarlyPrice34)
    triplePoisonMushroomMidPrice1 = convert_to_hex_weight(triplePoisonMushroomMidPrice1)
    triplePoisonMushroomMidPrice2 = convert_to_hex_weight(triplePoisonMushroomMidPrice2)
    triplePoisonMushroomMidPrice34 = convert_to_hex_weight(triplePoisonMushroomMidPrice34)
    triplePoisonMushroomLatePrice1 = convert_to_hex_weight(triplePoisonMushroomLatePrice1)
    triplePoisonMushroomLatePrice2 = convert_to_hex_weight(triplePoisonMushroomLatePrice2)
    triplePoisonMushroomLatePrice34 = convert_to_hex_weight(triplePoisonMushroomLatePrice34)

    # Celluar Shopper: DX
    celluarShopperEarlyPrice1 = convert_to_hex_weight(celluarShopperEarlyPrice1)
    celluarShopperEarlyPrice2 = convert_to_hex_weight(celluarShopperEarlyPrice2)
    celluarShopperEarlyPrice34 = convert_to_hex_weight(celluarShopperEarlyPrice34)
    celluarShopperMidPrice1 = convert_to_hex_weight(celluarShopperMidPrice1)
    celluarShopperMidPrice2 = convert_to_hex_weight(celluarShopperMidPrice2)
    celluarShopperMidPrice34 = convert_to_hex_weight(celluarShopperMidPrice34)
    celluarShopperLatePrice1 = convert_to_hex_weight(celluarShopperLatePrice1)
    celluarShopperLatePrice2 = convert_to_hex_weight(celluarShopperLatePrice2)
    celluarShopperLatePrice34 = convert_to_hex_weight(celluarShopperLatePrice34)

    # Skeleton Key: DX
    skeletonKeyEarlyPrice1 = convert_to_hex_weight(skeletonKeyEarlyPrice1)
    skeletonKeyEarlyPrice2 = convert_to_hex_weight(skeletonKeyEarlyPrice2)
    skeletonKeyEarlyPrice34 = convert_to_hex_weight(skeletonKeyEarlyPrice34)
    skeletonKeyMidPrice1 = convert_to_hex_weight(skeletonKeyMidPrice1)
    skeletonKeyMidPrice2 = convert_to_hex_weight(skeletonKeyMidPrice2)
    skeletonKeyMidPrice34 = convert_to_hex_weight(skeletonKeyMidPrice34)
    skeletonKeyLatePrice1 = convert_to_hex_weight(skeletonKeyLatePrice1)
    skeletonKeyLatePrice2 = convert_to_hex_weight(skeletonKeyLatePrice2)
    skeletonKeyLatePrice34 = convert_to_hex_weight(skeletonKeyLatePrice34)

    # Plunder Chest: DX
    plunderChestEarlyPrice1 = convert_to_hex_weight(plunderChestEarlyPrice1)
    plunderChestEarlyPrice2 = convert_to_hex_weight(plunderChestEarlyPrice2)
    plunderChestEarlyPrice34 = convert_to_hex_weight(plunderChestEarlyPrice34)
    plunderChestMidPrice1 = convert_to_hex_weight(plunderChestMidPrice1)
    plunderChestMidPrice2 = convert_to_hex_weight(plunderChestMidPrice2)
    plunderChestMidPrice34 = convert_to_hex_weight(plunderChestMidPrice34)
    plunderChestLatePrice1 = convert_to_hex_weight(plunderChestLatePrice1)
    plunderChestLatePrice2 = convert_to_hex_weight(plunderChestLatePrice2)
    plunderChestLatePrice34 = convert_to_hex_weight(plunderChestLatePrice34)

    # Gaddbrush: DX
    gaddbrushEarlyPrice1 = convert_to_hex_weight(gaddbrushEarlyPrice1)
    gaddbrushEarlyPrice2 = convert_to_hex_weight(gaddbrushEarlyPrice2)
    gaddbrushEarlyPrice34 = convert_to_hex_weight(gaddbrushEarlyPrice34)
    gaddbrushMidPrice1 = convert_to_hex_weight(gaddbrushMidPrice1)
    gaddbrushMidPrice2 = convert_to_hex_weight(gaddbrushMidPrice2)
    gaddbrushMidPrice34 = convert_to_hex_weight(gaddbrushMidPrice34)
    gaddbrushLatePrice1 = convert_to_hex_weight(gaddbrushLatePrice1)
    gaddbrushLatePrice2 = convert_to_hex_weight(gaddbrushLatePrice2)
    gaddbrushLatePrice34 = convert_to_hex_weight(gaddbrushLatePrice34)

    # Warp Block: DX
    warpBlockEarlyPrice1 = convert_to_hex_weight(warpBlockEarlyPrice1)
    warpBlockEarlyPrice2 = convert_to_hex_weight(warpBlockEarlyPrice2)
    warpBlockEarlyPrice34 = convert_to_hex_weight(warpBlockEarlyPrice34)
    warpBlockMidPrice1 = convert_to_hex_weight(warpBlockMidPrice1)
    warpBlockMidPrice2 = convert_to_hex_weight(warpBlockMidPrice2)
    warpBlockMidPrice34 = convert_to_hex_weight(warpBlockMidPrice34)
    warpBlockLatePrice1 = convert_to_hex_weight(warpBlockLatePrice1)
    warpBlockLatePrice2 = convert_to_hex_weight(warpBlockLatePrice2)
    warpBlockLatePrice34 = convert_to_hex_weight(warpBlockLatePrice34)

    # Fly Guy: DX
    flyGuyEarlyPrice1 = convert_to_hex_weight(flyGuyEarlyPrice1)
    flyGuyEarlyPrice2 = convert_to_hex_weight(flyGuyEarlyPrice2)
    flyGuyEarlyPrice34 = convert_to_hex_weight(flyGuyEarlyPrice34)
    flyGuyMidPrice1 = convert_to_hex_weight(flyGuyMidPrice1)
    flyGuyMidPrice2 = convert_to_hex_weight(flyGuyMidPrice2)
    flyGuyMidPrice34 = convert_to_hex_weight(flyGuyMidPrice34)
    flyGuyLatePrice1 = convert_to_hex_weight(flyGuyLatePrice1)
    flyGuyLatePrice2 = convert_to_hex_weight(flyGuyLatePrice2)
    flyGuyLatePrice34 = convert_to_hex_weight(flyGuyLatePrice34)

    # Plus Block: DX
    plusBlockEarlyPrice1 = convert_to_hex_weight(plusBlockEarlyPrice1)
    plusBlockEarlyPrice2 = convert_to_hex_weight(plusBlockEarlyPrice2)
    plusBlockEarlyPrice34 = convert_to_hex_weight(plusBlockEarlyPrice34)
    plusBlockMidPrice1 = convert_to_hex_weight(plusBlockMidPrice1)
    plusBlockMidPrice2 = convert_to_hex_weight(plusBlockMidPrice2)
    plusBlockMidPrice34 = convert_to_hex_weight(plusBlockMidPrice34)
    plusBlockLatePrice1 = convert_to_hex_weight(plusBlockLatePrice1)
    plusBlockLatePrice2 = convert_to_hex_weight(plusBlockLatePrice2)
    plusBlockLatePrice34 = convert_to_hex_weight(plusBlockLatePrice34)

    # Minus Block: DX
    minusBlockEarlyPrice1 = convert_to_hex_weight(minusBlockEarlyPrice1)
    minusBlockEarlyPrice2 = convert_to_hex_weight(minusBlockEarlyPrice2)
    minusBlockEarlyPrice34 = convert_to_hex_weight(minusBlockEarlyPrice34)
    minusBlockMidPrice1 = convert_to_hex_weight(minusBlockMidPrice1)
    minusBlockMidPrice2 = convert_to_hex_weight(minusBlockMidPrice2)
    minusBlockMidPrice34 = convert_to_hex_weight(minusBlockMidPrice34)
    minusBlockLatePrice1 = convert_to_hex_weight(minusBlockLatePrice1)
    minusBlockLatePrice2 = convert_to_hex_weight(minusBlockLatePrice2)
    minusBlockLatePrice34 = convert_to_hex_weight(minusBlockLatePrice34)

    # Speed Block: DX
    speedBlockEarlyPrice1 = convert_to_hex_weight(speedBlockEarlyPrice1)
    speedBlockEarlyPrice2 = convert_to_hex_weight(speedBlockEarlyPrice2)
    speedBlockEarlyPrice34 = convert_to_hex_weight(speedBlockEarlyPrice34)
    speedBlockMidPrice1 = convert_to_hex_weight(speedBlockMidPrice1)
    speedBlockMidPrice2 = convert_to_hex_weight(speedBlockMidPrice2)
    speedBlockMidPrice34 = convert_to_hex_weight(speedBlockMidPrice34)
    speedBlockLatePrice1 = convert_to_hex_weight(speedBlockLatePrice1)
    speedBlockLatePrice2 = convert_to_hex_weight(speedBlockLatePrice2)
    speedBlockLatePrice34 = convert_to_hex_weight(speedBlockLatePrice34)

    # Slow Block: DX
    slowBlockEarlyPrice1 = convert_to_hex_weight(slowBlockEarlyPrice1)
    slowBlockEarlyPrice2 = convert_to_hex_weight(slowBlockEarlyPrice2)
    slowBlockEarlyPrice34 = convert_to_hex_weight(slowBlockEarlyPrice34)
    slowBlockMidPrice1 = convert_to_hex_weight(slowBlockMidPrice1)
    slowBlockMidPrice2 = convert_to_hex_weight(slowBlockMidPrice2)
    slowBlockMidPrice34 = convert_to_hex_weight(slowBlockMidPrice34)
    slowBlockLatePrice1 = convert_to_hex_weight(slowBlockLatePrice1)
    slowBlockLatePrice2 = convert_to_hex_weight(slowBlockLatePrice2)
    slowBlockLatePrice34 = convert_to_hex_weight(slowBlockLatePrice34)

    # Hidden Block Card: DX
    hiddenBlockCardEarlyPrice1 = convert_to_hex_weight(hiddenBlockCardEarlyPrice1)
    hiddenBlockCardEarlyPrice2 = convert_to_hex_weight(hiddenBlockCardEarlyPrice2)
    hiddenBlockCardEarlyPrice34 = convert_to_hex_weight(hiddenBlockCardEarlyPrice34)
    hiddenBlockCardMidPrice1 = convert_to_hex_weight(hiddenBlockCardMidPrice1)
    hiddenBlockCardMidPrice2 = convert_to_hex_weight(hiddenBlockCardMidPrice2)
    hiddenBlockCardMidPrice34 = convert_to_hex_weight(hiddenBlockCardMidPrice34)
    hiddenBlockCardLatePrice1 = convert_to_hex_weight(hiddenBlockCardLatePrice1)
    hiddenBlockCardLatePrice2 = convert_to_hex_weight(hiddenBlockCardLatePrice2)
    hiddenBlockCardLatePrice34 = convert_to_hex_weight(hiddenBlockCardLatePrice34)

    # Barter Box: DX
    barterBoxEarlyPrice1 = convert_to_hex_weight(barterBoxEarlyPrice1)
    barterBoxEarlyPrice2 = convert_to_hex_weight(barterBoxEarlyPrice2)
    barterBoxEarlyPrice34 = convert_to_hex_weight(barterBoxEarlyPrice34)
    barterBoxMidPrice1 = convert_to_hex_weight(barterBoxMidPrice1)
    barterBoxMidPrice2 = convert_to_hex_weight(barterBoxMidPrice2)
    barterBoxMidPrice34 = convert_to_hex_weight(barterBoxMidPrice34)
    barterBoxLatePrice1 = convert_to_hex_weight(barterBoxLatePrice1)
    barterBoxLatePrice2 = convert_to_hex_weight(barterBoxLatePrice2)
    barterBoxLatePrice34 = convert_to_hex_weight(barterBoxLatePrice34)

    # Super Warp Pipe: DX
    superWarpPipeEarlyPrice1 = convert_to_hex_weight(superWarpPipeEarlyPrice1)
    superWarpPipeEarlyPrice2 = convert_to_hex_weight(superWarpPipeEarlyPrice2)
    superWarpPipeEarlyPrice34 = convert_to_hex_weight(superWarpPipeEarlyPrice34)
    superWarpPipeMidPrice1 = convert_to_hex_weight(superWarpPipeMidPrice1)
    superWarpPipeMidPrice2 = convert_to_hex_weight(superWarpPipeMidPrice2)
    superWarpPipeMidPrice34 = convert_to_hex_weight(superWarpPipeMidPrice34)
    superWarpPipeLatePrice1 = convert_to_hex_weight(superWarpPipeLatePrice1)
    superWarpPipeLatePrice2 = convert_to_hex_weight(superWarpPipeLatePrice2)
    superWarpPipeLatePrice34 = convert_to_hex_weight(superWarpPipeLatePrice34)

    # Chance Time Charm: DX
    chanceTimeCharmEarlyPrice1 = convert_to_hex_weight(chanceTimeCharmEarlyPrice1)
    chanceTimeCharmEarlyPrice2 = convert_to_hex_weight(chanceTimeCharmEarlyPrice2)
    chanceTimeCharmEarlyPrice34 = convert_to_hex_weight(chanceTimeCharmEarlyPrice34)
    chanceTimeCharmMidPrice1 = convert_to_hex_weight(chanceTimeCharmMidPrice1)
    chanceTimeCharmMidPrice2 = convert_to_hex_weight(chanceTimeCharmMidPrice2)
    chanceTimeCharmMidPrice34 = convert_to_hex_weight(chanceTimeCharmMidPrice34)
    chanceTimeCharmLatePrice1 = convert_to_hex_weight(chanceTimeCharmLatePrice1)
    chanceTimeCharmLatePrice2 = convert_to_hex_weight(chanceTimeCharmLatePrice2)
    chanceTimeCharmLatePrice34 = convert_to_hex_weight(chanceTimeCharmLatePrice34)

    # Wacky Watch: DX
    wackyWatchEarlyPrice1 = convert_to_hex_weight(wackyWatchEarlyPrice1)
    wackyWatchEarlyPrice2 = convert_to_hex_weight(wackyWatchEarlyPrice2)
    wackyWatchEarlyPrice34 = convert_to_hex_weight(wackyWatchEarlyPrice34)
    wackyWatchMidPrice1 = convert_to_hex_weight(wackyWatchMidPrice1)
    wackyWatchMidPrice2 = convert_to_hex_weight(wackyWatchMidPrice2)
    wackyWatchMidPrice34 = convert_to_hex_weight(wackyWatchMidPrice34)
    wackyWatchLatePrice1 = convert_to_hex_weight(wackyWatchLatePrice1)
    wackyWatchLatePrice2 = convert_to_hex_weight(wackyWatchLatePrice2)
    wackyWatchLatePrice34 = convert_to_hex_weight(wackyWatchLatePrice34)

    # Bowser Phone: DX
    bowserPhoneEarlyPrice1 = convert_to_hex_weight(bowserPhoneEarlyPrice1)
    bowserPhoneEarlyPrice2 = convert_to_hex_weight(bowserPhoneEarlyPrice2)
    bowserPhoneEarlyPrice34 = convert_to_hex_weight(bowserPhoneEarlyPrice34)
    bowserPhoneMidPrice1 = convert_to_hex_weight(bowserPhoneMidPrice1)
    bowserPhoneMidPrice2 = convert_to_hex_weight(bowserPhoneMidPrice2)
    bowserPhoneMidPrice34 = convert_to_hex_weight(bowserPhoneMidPrice34)
    bowserPhoneLatePrice1 = convert_to_hex_weight(bowserPhoneLatePrice1)
    bowserPhoneLatePrice2 = convert_to_hex_weight(bowserPhoneLatePrice2)
    bowserPhoneLatePrice34 = convert_to_hex_weight(bowserPhoneLatePrice34)

    minCoins = convert_to_hex_weight(minCoins)

    generatedCode = getItemShopPricesFourDX(minCoins, miniMushroomEarlyPrice1, miniMushroomEarlyPrice2, miniMushroomEarlyPrice34, miniMushroomMidPrice1, miniMushroomMidPrice2, miniMushroomMidPrice34, miniMushroomLatePrice1, miniMushroomLatePrice2, miniMushroomLatePrice34, megaMushroomEarlyPrice1, megaMushroomEarlyPrice2, megaMushroomEarlyPrice34, megaMushroomMidPrice1, megaMushroomMidPrice2, megaMushroomMidPrice34, megaMushroomLatePrice1, megaMushroomLatePrice2, megaMushroomLatePrice34, superMiniMushroomEarlyPrice1, superMiniMushroomEarlyPrice2, superMiniMushroomEarlyPrice34, superMiniMushroomMidPrice1, superMiniMushroomMidPrice2, superMiniMushroomMidPrice34, superMiniMushroomLatePrice1, superMiniMushroomLatePrice2, superMiniMushroomLatePrice34, superMegaMushroomEarlyPrice1, superMegaMushroomEarlyPrice2, superMegaMushroomEarlyPrice34, superMegaMushroomMidPrice1, superMegaMushroomMidPrice2, superMegaMushroomMidPrice34, superMegaMushroomLatePrice1, superMegaMushroomLatePrice2, superMegaMushroomLatePrice34, miniMegaHammerEarlyPrice1, miniMegaHammerEarlyPrice2, miniMegaHammerEarlyPrice34, miniMegaHammerMidPrice1, miniMegaHammerMidPrice2, miniMegaHammerMidPrice34, miniMegaHammerLatePrice1, miniMegaHammerLatePrice2, miniMegaHammerLatePrice34, warpPipeEarlyPrice1, warpPipeEarlyPrice2, warpPipeEarlyPrice34, warpPipeMidPrice1, warpPipeMidPrice2, warpPipeMidPrice34, warpPipeLatePrice1, warpPipeLatePrice2, warpPipeLatePrice34, swapCardEarlyPrice1, swapCardEarlyPrice2, swapCardEarlyPrice34, swapCardMidPrice1, swapCardMidPrice2, swapCardMidPrice34, swapCardLatePrice1, swapCardLatePrice2, swapCardLatePrice34, sparkyStickerEarlyPrice1, sparkyStickerEarlyPrice2, sparkyStickerEarlyPrice34, sparkyStickerMidPrice1, sparkyStickerMidPrice2, sparkyStickerMidPrice34, sparkyStickerLatePrice1, sparkyStickerLatePrice2, sparkyStickerLatePrice34, gaddlightEarlyPrice1, gaddlightEarlyPrice2, gaddlightEarlyPrice34, gaddlightMidPrice1, gaddlightMidPrice2, gaddlightMidPrice34, gaddlightLatePrice1, gaddlightLatePrice2, gaddlightLatePrice34, chompCallEarlyPrice1, chompCallEarlyPrice2, chompCallEarlyPrice34, chompCallMidPrice1, chompCallMidPrice2, chompCallMidPrice34, chompCallLatePrice1, chompCallLatePrice2, chompCallLatePrice34, bowserSuitEarlyPrice1, bowserSuitEarlyPrice2, bowserSuitEarlyPrice34, bowserSuitMidPrice1, bowserSuitMidPrice2, bowserSuitMidPrice34, bowserSuitLatePrice1, bowserSuitLatePrice2, bowserSuitLatePrice34, crystalBallEarlyPrice1, crystalBallEarlyPrice2, crystalBallEarlyPrice34, crystalBallMidPrice1, crystalBallMidPrice2, crystalBallMidPrice34, crystalBallLatePrice1, crystalBallLatePrice2, crystalBallLatePrice34, magicLampEarlyPrice1, magicLampEarlyPrice2, magicLampEarlyPrice34, magicLampMidPrice1, magicLampMidPrice2, magicLampMidPrice34, magicLampLatePrice1, magicLampLatePrice2, magicLampLatePrice34, itemBagEarlyPrice1, itemBagEarlyPrice2, itemBagEarlyPrice34, itemBagMidPrice1, itemBagMidPrice2, itemBagMidPrice34, itemBagLatePrice1, itemBagLatePrice2, itemBagLatePrice34, mushroomEarlyPrice1, mushroomEarlyPrice2, mushroomEarlyPrice34, mushroomMidPrice1, mushroomMidPrice2, mushroomMidPrice34, mushroomLatePrice1, mushroomLatePrice2, mushroomLatePrice34, goldenMushroomEarlyPrice1, goldenMushroomEarlyPrice2, goldenMushroomEarlyPrice34, goldenMushroomMidPrice1, goldenMushroomMidPrice2, goldenMushroomMidPrice34, goldenMushroomLatePrice1, goldenMushroomLatePrice2, goldenMushroomLatePrice34, reverseMushroomEarlyPrice1, reverseMushroomEarlyPrice2, reverseMushroomEarlyPrice34, reverseMushroomMidPrice1, reverseMushroomMidPrice2, reverseMushroomMidPrice34, reverseMushroomLatePrice1, reverseMushroomLatePrice2, reverseMushroomLatePrice34, poisonMushroomEarlyPrice1, poisonMushroomEarlyPrice2, poisonMushroomEarlyPrice34, poisonMushroomMidPrice1, poisonMushroomMidPrice2, poisonMushroomMidPrice34, poisonMushroomLatePrice1, poisonMushroomLatePrice2, poisonMushroomLatePrice34, triplePoisonMushroomEarlyPrice1, triplePoisonMushroomEarlyPrice2, triplePoisonMushroomEarlyPrice34, triplePoisonMushroomMidPrice1, triplePoisonMushroomMidPrice2, triplePoisonMushroomMidPrice34, triplePoisonMushroomLatePrice1, triplePoisonMushroomLatePrice2, triplePoisonMushroomLatePrice34, celluarShopperEarlyPrice1, celluarShopperEarlyPrice2, celluarShopperEarlyPrice34, celluarShopperMidPrice1, celluarShopperMidPrice2, celluarShopperMidPrice34, celluarShopperLatePrice1, celluarShopperLatePrice2, celluarShopperLatePrice34, skeletonKeyEarlyPrice1, skeletonKeyEarlyPrice2, skeletonKeyEarlyPrice34, skeletonKeyMidPrice1, skeletonKeyMidPrice2, skeletonKeyMidPrice34, skeletonKeyLatePrice1, skeletonKeyLatePrice2, skeletonKeyLatePrice34, plunderChestEarlyPrice1, plunderChestEarlyPrice2, plunderChestEarlyPrice34, plunderChestMidPrice1, plunderChestMidPrice2, plunderChestMidPrice34, plunderChestLatePrice1, plunderChestLatePrice2, plunderChestLatePrice34, gaddbrushEarlyPrice1, gaddbrushEarlyPrice2, gaddbrushEarlyPrice34, gaddbrushMidPrice1, gaddbrushMidPrice2, gaddbrushMidPrice34, gaddbrushLatePrice1, gaddbrushLatePrice2, gaddbrushLatePrice34, warpBlockEarlyPrice1, warpBlockEarlyPrice2, warpBlockEarlyPrice34, warpBlockMidPrice1, warpBlockMidPrice2, warpBlockMidPrice34, warpBlockLatePrice1, warpBlockLatePrice2, warpBlockLatePrice34, flyGuyEarlyPrice1, flyGuyEarlyPrice2, flyGuyEarlyPrice34, flyGuyMidPrice1, flyGuyMidPrice2, flyGuyMidPrice34, flyGuyLatePrice1, flyGuyLatePrice2, flyGuyLatePrice34, plusBlockEarlyPrice1, plusBlockEarlyPrice2, plusBlockEarlyPrice34, plusBlockMidPrice1, plusBlockMidPrice2, plusBlockMidPrice34, plusBlockLatePrice1, plusBlockLatePrice2, plusBlockLatePrice34, minusBlockEarlyPrice1, minusBlockEarlyPrice2, minusBlockEarlyPrice34, minusBlockMidPrice1, minusBlockMidPrice2, minusBlockMidPrice34, minusBlockLatePrice1, minusBlockLatePrice2, minusBlockLatePrice34, speedBlockEarlyPrice1, speedBlockEarlyPrice2, speedBlockEarlyPrice34, speedBlockMidPrice1, speedBlockMidPrice2, speedBlockMidPrice34, speedBlockLatePrice1, speedBlockLatePrice2, speedBlockLatePrice34, slowBlockEarlyPrice1, slowBlockEarlyPrice2, slowBlockEarlyPrice34, slowBlockMidPrice1, slowBlockMidPrice2, slowBlockMidPrice34, slowBlockLatePrice1, slowBlockLatePrice2, slowBlockLatePrice34, bowserPhoneEarlyPrice1, bowserPhoneEarlyPrice2, bowserPhoneEarlyPrice34, bowserPhoneMidPrice1, bowserPhoneMidPrice2, bowserPhoneMidPrice34, bowserPhoneLatePrice1, bowserPhoneLatePrice2, bowserPhoneLatePrice34, doubleDipEarlyPrice1, doubleDipEarlyPrice2, doubleDipEarlyPrice34, doubleDipMidPrice1, doubleDipMidPrice2, doubleDipMidPrice34, doubleDipLatePrice1, doubleDipLatePrice2, doubleDipLatePrice34, hiddenBlockCardEarlyPrice1, hiddenBlockCardEarlyPrice2, hiddenBlockCardEarlyPrice34, hiddenBlockCardMidPrice1, hiddenBlockCardMidPrice2, hiddenBlockCardMidPrice34, hiddenBlockCardLatePrice1, hiddenBlockCardLatePrice2, hiddenBlockCardLatePrice34, barterBoxEarlyPrice1, barterBoxEarlyPrice2, barterBoxEarlyPrice34, barterBoxMidPrice1, barterBoxMidPrice2, barterBoxMidPrice34, barterBoxLatePrice1, barterBoxLatePrice2, barterBoxLatePrice34, superWarpPipeEarlyPrice1, superWarpPipeEarlyPrice2, superWarpPipeEarlyPrice34, superWarpPipeMidPrice1, superWarpPipeMidPrice2, superWarpPipeMidPrice34, superWarpPipeLatePrice1, superWarpPipeLatePrice2, superWarpPipeLatePrice34, chanceTimeCharmEarlyPrice1, chanceTimeCharmEarlyPrice2, chanceTimeCharmEarlyPrice34, chanceTimeCharmMidPrice1, chanceTimeCharmMidPrice2, chanceTimeCharmMidPrice34, chanceTimeCharmLatePrice1, chanceTimeCharmLatePrice2, chanceTimeCharmLatePrice34, wackyWatchEarlyPrice1, wackyWatchEarlyPrice2, wackyWatchEarlyPrice34, wackyWatchMidPrice1, wackyWatchMidPrice2, wackyWatchMidPrice34, wackyWatchLatePrice1, wackyWatchLatePrice2, wackyWatchLatePrice34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def itemsEvent_mp4ShopPrices(miniMushroomEarlyPrice1 = "5", miniMushroomEarlyPrice2 = "5", miniMushroomEarlyPrice34 = "5", miniMushroomMidPrice1 = "5", miniMushroomMidPrice2 = "5", miniMushroomMidPrice34 = "5", miniMushroomLatePrice1 = "5", miniMushroomLatePrice2 = "5", miniMushroomLatePrice34 = "5", megaMushroomEarlyPrice1 = "5", megaMushroomEarlyPrice2 = "5", megaMushroomEarlyPrice34 = "5", megaMushroomMidPrice1 = "5", megaMushroomMidPrice2 = "5", megaMushroomMidPrice34 = "5", megaMushroomLatePrice1 = "5", megaMushroomLatePrice2 = "5", megaMushroomLatePrice34 = "5", superMiniMushroomEarlyPrice1 = "15", superMiniMushroomEarlyPrice2 = "15", superMiniMushroomEarlyPrice34 = "15", superMiniMushroomMidPrice1 = "15", superMiniMushroomMidPrice2 = "10", superMiniMushroomMidPrice34 = "15", superMiniMushroomLatePrice1 = "15", superMiniMushroomLatePrice2 = "15", superMiniMushroomLatePrice34 = "15", superMegaMushroomEarlyPrice1 = "15", superMegaMushroomEarlyPrice2 = "15", superMegaMushroomEarlyPrice34 = "15", superMegaMushroomMidPrice1 = "15", superMegaMushroomMidPrice2 = "15", superMegaMushroomMidPrice34 = "15", superMegaMushroomLatePrice1 = "15", superMegaMushroomLatePrice2 = "15", superMegaMushroomLatePrice34 = "15", miniMegaHammerEarlyPrice1 = "10", miniMegaHammerEarlyPrice2 = "10", miniMegaHammerEarlyPrice34 = "10", miniMegaHammerMidPrice1 = "10", miniMegaHammerMidPrice2 = "10", miniMegaHammerMidPrice34 = "10", miniMegaHammerLatePrice1 = "10", miniMegaHammerLatePrice2 = "10", miniMegaHammerLatePrice34 = "10", warpPipeEarlyPrice1 = "10", warpPipeEarlyPrice2 = "10", warpPipeEarlyPrice34 = "10", warpPipeMidPrice1 = "10", warpPipeMidPrice2 = "10", warpPipeMidPrice34 = "10", warpPipeLatePrice1 = "10", warpPipeLatePrice2 = "10", warpPipeLatePrice34 = "10", swapCardEarlyPrice1 = "15", swapCardEarlyPrice2 = "15", swapCardEarlyPrice34 = "15", swapCardMidPrice1 = "15", swapCardMidPrice2 = "15", swapCardMidPrice34 = "15", swapCardLatePrice1 = "15", swapCardLatePrice2 = "15", swapCardLatePrice34 = "15", sparkyStickerEarlyPrice1 = "15", sparkyStickerEarlyPrice2 = "15", sparkyStickerEarlyPrice34 = "15", sparkyStickerMidPrice1 = "15", sparkyStickerMidPrice2 = "15", sparkyStickerMidPrice34 = "5", sparkyStickerLatePrice1 = "15", sparkyStickerLatePrice2 = "15", sparkyStickerLatePrice34 = "15", gaddlightEarlyPrice1 = "15", gaddlightEarlyPrice2 = "15", gaddlightEarlyPrice34 = "15", gaddlightMidPrice1 = "15", gaddlightMidPrice2 = "15", gaddlightMidPrice34 = "15", gaddlightLatePrice1 = "15", gaddlightLatePrice2 = "15", gaddlightLatePrice34 = "10", chompCallEarlyPrice1 = "15", chompCallEarlyPrice2 = "15", chompCallEarlyPrice34 = "15", chompCallMidPrice1 = "15", chompCallMidPrice2 = "10", chompCallMidPrice34 = "15", chompCallLatePrice1 = "10", chompCallLatePrice2 = "15", chompCallLatePrice34 = "15", bowserSuitEarlyPrice1 = "0", bowserSuitEarlyPrice2 = "0", bowserSuitEarlyPrice34 = "0", bowserSuitMidPrice1 = "0", bowserSuitMidPrice2 = "0", bowserSuitMidPrice34 = "0", bowserSuitLatePrice1 = "0", bowserSuitLatePrice2 = "0", bowserSuitLatePrice34 = "12", crystalBallEarlyPrice1 = "25", crystalBallEarlyPrice2 = "25", crystalBallEarlyPrice34 = "25", crystalBallMidPrice1 = "25", crystalBallMidPrice2 = "25", crystalBallMidPrice34 = "25", crystalBallLatePrice1 = "25", crystalBallLatePrice2 = "25", crystalBallLatePrice34 = "25", magicLampEarlyPrice1 = "30", magicLampEarlyPrice2 = "30", magicLampEarlyPrice34 = "30", magicLampMidPrice1 = "30", magicLampMidPrice2 = "30", magicLampMidPrice34 = "30", magicLampLatePrice1 = "30", magicLampLatePrice2 = "30", magicLampLatePrice34 = "30", itemBagEarlyPrice1 = "30", itemBagEarlyPrice2 = "30", itemBagEarlyPrice34 = "30", itemBagMidPrice1 = "30", itemBagMidPrice2 = "30", itemBagMidPrice34 = "30", itemBagLatePrice1 = "30", itemBagLatePrice2 = "30", itemBagLatePrice34 = "30"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    # Mini Mushroom
    miniMushroomEarlyPrice1 = get_capsule_value(miniMushroomEarlyPrice1) or "5"
    miniMushroomEarlyPrice2 = get_capsule_value(miniMushroomEarlyPrice2) or "5"
    miniMushroomEarlyPrice34 = get_capsule_value(miniMushroomEarlyPrice34) or "5"
    miniMushroomMidPrice1 = get_capsule_value(miniMushroomMidPrice1) or "5"
    miniMushroomMidPrice2 = get_capsule_value(miniMushroomMidPrice2) or "5"
    miniMushroomMidPrice34 = get_capsule_value(miniMushroomMidPrice34) or "5"
    miniMushroomLatePrice1 = get_capsule_value(miniMushroomLatePrice1) or "5"
    miniMushroomLatePrice2 = get_capsule_value(miniMushroomLatePrice2) or "5"
    miniMushroomLatePrice34 = get_capsule_value(miniMushroomLatePrice34) or "5"
    
    # Mega Mushroom
    megaMushroomEarlyPrice1 = get_capsule_value(megaMushroomEarlyPrice1) or "5"
    megaMushroomEarlyPrice2 = get_capsule_value(megaMushroomEarlyPrice2) or "5"
    megaMushroomEarlyPrice34 = get_capsule_value(megaMushroomEarlyPrice34) or "5"
    megaMushroomMidPrice1 = get_capsule_value(megaMushroomMidPrice1) or "5"
    megaMushroomMidPrice2 = get_capsule_value(megaMushroomMidPrice2) or "5"
    megaMushroomMidPrice34 = get_capsule_value(megaMushroomMidPrice34) or "5"
    megaMushroomLatePrice1 = get_capsule_value(megaMushroomLatePrice1) or "5"
    megaMushroomLatePrice2 = get_capsule_value(megaMushroomLatePrice2) or "5"
    megaMushroomLatePrice34 = get_capsule_value(megaMushroomLatePrice34) or "5"

    # Super Mini Mushroom
    superMiniMushroomEarlyPrice1 = get_capsule_value(superMiniMushroomEarlyPrice1) or "15"
    superMiniMushroomEarlyPrice2 = get_capsule_value(superMiniMushroomEarlyPrice2) or "15"
    superMiniMushroomEarlyPrice34 = get_capsule_value(superMiniMushroomEarlyPrice34) or "15"
    superMiniMushroomMidPrice1 = get_capsule_value(superMiniMushroomMidPrice1) or "15"
    superMiniMushroomMidPrice2 = get_capsule_value(superMiniMushroomMidPrice2) or "15"
    superMiniMushroomMidPrice34 = get_capsule_value(superMiniMushroomMidPrice34) or "15"
    superMiniMushroomLatePrice1 = get_capsule_value(superMiniMushroomLatePrice1) or "15"
    superMiniMushroomLatePrice2 = get_capsule_value(superMiniMushroomLatePrice2) or "15"
    superMiniMushroomLatePrice34 = get_capsule_value(superMiniMushroomLatePrice34) or "15"

    # Super Mega Mushroom
    superMegaMushroomEarlyPrice1 = get_capsule_value(superMegaMushroomEarlyPrice1) or "15"
    superMegaMushroomEarlyPrice2 = get_capsule_value(superMegaMushroomEarlyPrice2) or "15"
    superMegaMushroomEarlyPrice34 = get_capsule_value(superMegaMushroomEarlyPrice34) or "15"
    superMegaMushroomMidPrice1 = get_capsule_value(superMegaMushroomMidPrice1) or "15"
    superMegaMushroomMidPrice2 = get_capsule_value(superMegaMushroomMidPrice2) or "15"
    superMegaMushroomMidPrice34 = get_capsule_value(superMegaMushroomMidPrice34) or "15"
    superMegaMushroomLatePrice1 = get_capsule_value(superMegaMushroomLatePrice1) or "15"
    superMegaMushroomLatePrice2 = get_capsule_value(superMegaMushroomLatePrice2) or "15"
    superMegaMushroomLatePrice34 = get_capsule_value(superMegaMushroomLatePrice34) or "15"

    # Mini Mega Hammer
    miniMegaHammerEarlyPrice1 = get_capsule_value(miniMegaHammerEarlyPrice1) or "10"
    miniMegaHammerEarlyPrice2 = get_capsule_value(miniMegaHammerEarlyPrice2) or "10"
    miniMegaHammerEarlyPrice34 = get_capsule_value(miniMegaHammerEarlyPrice34) or "10"
    miniMegaHammerMidPrice1 = get_capsule_value(miniMegaHammerMidPrice1) or "10"
    miniMegaHammerMidPrice2 = get_capsule_value(miniMegaHammerMidPrice2) or "10"
    miniMegaHammerMidPrice34 = get_capsule_value(miniMegaHammerMidPrice34) or "10"
    miniMegaHammerLatePrice1 = get_capsule_value(miniMegaHammerLatePrice1) or "10"
    miniMegaHammerLatePrice2 = get_capsule_value(miniMegaHammerLatePrice2) or "10"
    miniMegaHammerLatePrice34 = get_capsule_value(miniMegaHammerLatePrice34) or "10"

    # Warp Pipe
    warpPipeEarlyPrice1 = get_capsule_value(warpPipeEarlyPrice1) or "10"
    warpPipeEarlyPrice2 = get_capsule_value(warpPipeEarlyPrice2) or "10"
    warpPipeEarlyPrice34 = get_capsule_value(warpPipeEarlyPrice34) or "10"
    warpPipeMidPrice1 = get_capsule_value(warpPipeMidPrice1) or "10"
    warpPipeMidPrice2 = get_capsule_value(warpPipeMidPrice2) or "10"
    warpPipeMidPrice34 = get_capsule_value(warpPipeMidPrice34) or "10"
    warpPipeLatePrice1 = get_capsule_value(warpPipeLatePrice1) or "10"
    warpPipeLatePrice2 = get_capsule_value(warpPipeLatePrice2) or "10"
    warpPipeLatePrice34 = get_capsule_value(warpPipeLatePrice34) or "10"

    # Swap Card
    swapCardEarlyPrice1 = get_capsule_value(swapCardEarlyPrice1) or "15"
    swapCardEarlyPrice2 = get_capsule_value(swapCardEarlyPrice2) or "15"
    swapCardEarlyPrice34 = get_capsule_value(swapCardEarlyPrice34) or "15"
    swapCardMidPrice1 = get_capsule_value(swapCardMidPrice1) or "15"
    swapCardMidPrice2 = get_capsule_value(swapCardMidPrice2) or "15"
    swapCardMidPrice34 = get_capsule_value(swapCardMidPrice34) or "15"
    swapCardLatePrice1 = get_capsule_value(swapCardLatePrice1) or "15"
    swapCardLatePrice2 = get_capsule_value(swapCardLatePrice2) or "15"
    swapCardLatePrice34 = get_capsule_value(swapCardLatePrice34) or "15"

    # Sparky Sticker
    sparkyStickerEarlyPrice1 = get_capsule_value(sparkyStickerEarlyPrice1) or "15"
    sparkyStickerEarlyPrice2 = get_capsule_value(sparkyStickerEarlyPrice2) or "15"
    sparkyStickerEarlyPrice34 = get_capsule_value(sparkyStickerEarlyPrice34) or "15"
    sparkyStickerMidPrice1 = get_capsule_value(sparkyStickerMidPrice1) or "15"
    sparkyStickerMidPrice2 = get_capsule_value(sparkyStickerMidPrice2) or "15"
    sparkyStickerMidPrice34 = get_capsule_value(sparkyStickerMidPrice34) or "15"
    sparkyStickerLatePrice1 = get_capsule_value(sparkyStickerLatePrice1) or "15"
    sparkyStickerLatePrice2 = get_capsule_value(sparkyStickerLatePrice2) or "15"
    sparkyStickerLatePrice34 = get_capsule_value(sparkyStickerLatePrice34) or "15"

    # Gaddlight
    gaddlightEarlyPrice1 = get_capsule_value(gaddlightEarlyPrice1) or "15"
    gaddlightEarlyPrice2 = get_capsule_value(gaddlightEarlyPrice2) or "15"
    gaddlightEarlyPrice34 = get_capsule_value(gaddlightEarlyPrice34) or "15"
    gaddlightMidPrice1 = get_capsule_value(gaddlightMidPrice1) or "15"
    gaddlightMidPrice2 = get_capsule_value(gaddlightMidPrice2) or "15"
    gaddlightMidPrice34 = get_capsule_value(gaddlightMidPrice34) or "15"
    gaddlightLatePrice1 = get_capsule_value(gaddlightLatePrice1) or "15"
    gaddlightLatePrice2 = get_capsule_value(gaddlightLatePrice2) or "15"
    gaddlightLatePrice34 = get_capsule_value(gaddlightLatePrice34) or "15"

    # Chomp Call
    chompCallEarlyPrice1 = get_capsule_value(chompCallEarlyPrice1) or "15"
    chompCallEarlyPrice2 = get_capsule_value(chompCallEarlyPrice2) or "15"
    chompCallEarlyPrice34 = get_capsule_value(chompCallEarlyPrice34) or "15"
    chompCallMidPrice1 = get_capsule_value(chompCallMidPrice1) or "15"
    chompCallMidPrice2 = get_capsule_value(chompCallMidPrice2) or "15"
    chompCallMidPrice34 = get_capsule_value(chompCallMidPrice34) or "15"
    chompCallLatePrice1 = get_capsule_value(chompCallLatePrice1) or "15"
    chompCallLatePrice2 = get_capsule_value(chompCallLatePrice2) or "15"
    chompCallLatePrice34 = get_capsule_value(chompCallLatePrice34) or "15"

    # Bowser Suit
    bowserSuitEarlyPrice1 = get_capsule_value(bowserSuitEarlyPrice1) or "0"
    bowserSuitEarlyPrice2 = get_capsule_value(bowserSuitEarlyPrice2) or "0"
    bowserSuitEarlyPrice34 = get_capsule_value(bowserSuitEarlyPrice34) or "0"
    bowserSuitMidPrice1 = get_capsule_value(bowserSuitMidPrice1) or "0"
    bowserSuitMidPrice2 = get_capsule_value(bowserSuitMidPrice2) or "0"
    bowserSuitMidPrice34 = get_capsule_value(bowserSuitMidPrice34) or "0"
    bowserSuitLatePrice1 = get_capsule_value(bowserSuitLatePrice1) or "0"
    bowserSuitLatePrice2 = get_capsule_value(bowserSuitLatePrice2) or "0"
    bowserSuitLatePrice34 = get_capsule_value(bowserSuitLatePrice34) or "0"

    # Crystal Ball
    crystalBallEarlyPrice1 = get_capsule_value(crystalBallEarlyPrice1) or "25"
    crystalBallEarlyPrice2 = get_capsule_value(crystalBallEarlyPrice2) or "25"
    crystalBallEarlyPrice34 = get_capsule_value(crystalBallEarlyPrice34) or "25"
    crystalBallMidPrice1 = get_capsule_value(crystalBallMidPrice1) or "25"
    crystalBallMidPrice2 = get_capsule_value(crystalBallMidPrice2) or "25"
    crystalBallMidPrice34 = get_capsule_value(crystalBallMidPrice34) or "25"
    crystalBallLatePrice1 = get_capsule_value(crystalBallLatePrice1) or "25"
    crystalBallLatePrice2 = get_capsule_value(crystalBallLatePrice2) or "25"
    crystalBallLatePrice34 = get_capsule_value(crystalBallLatePrice34) or "25"

    # Magic Lamp
    magicLampEarlyPrice1 = get_capsule_value(magicLampEarlyPrice1) or "30"
    magicLampEarlyPrice2 = get_capsule_value(magicLampEarlyPrice2) or "30"
    magicLampEarlyPrice34 = get_capsule_value(magicLampEarlyPrice34) or "30"
    magicLampMidPrice1 = get_capsule_value(magicLampMidPrice1) or "30"
    magicLampMidPrice2 = get_capsule_value(magicLampMidPrice2) or "30"
    magicLampMidPrice34 = get_capsule_value(magicLampMidPrice34) or "30"
    magicLampLatePrice1 = get_capsule_value(magicLampLatePrice1) or "30"
    magicLampLatePrice2 = get_capsule_value(magicLampLatePrice2) or "30"
    magicLampLatePrice34 = get_capsule_value(magicLampLatePrice34) or "30"

    # Item Bag
    itemBagEarlyPrice1 = get_capsule_value(itemBagEarlyPrice1) or "30"
    itemBagEarlyPrice2 = get_capsule_value(itemBagEarlyPrice2) or "30"
    itemBagEarlyPrice34 = get_capsule_value(itemBagEarlyPrice34) or "30"
    itemBagMidPrice1 = get_capsule_value(itemBagMidPrice1) or "30"
    itemBagMidPrice2 = get_capsule_value(itemBagMidPrice2) or "30"
    itemBagMidPrice34 = get_capsule_value(itemBagMidPrice34) or "30"
    itemBagLatePrice1 = get_capsule_value(itemBagLatePrice1) or "30"
    itemBagLatePrice2 = get_capsule_value(itemBagLatePrice2) or "30"
    itemBagLatePrice34 = get_capsule_value(itemBagLatePrice34) or "30"
    
    minCoins = find_lowest_integer(*[
        int(miniMushroomEarlyPrice1), int(miniMushroomEarlyPrice2), int(miniMushroomEarlyPrice34), 
        int(miniMushroomMidPrice1), int(miniMushroomMidPrice2), int(miniMushroomMidPrice34),
        int(miniMushroomLatePrice1), int(miniMushroomLatePrice2), int(miniMushroomLatePrice34),
        int(megaMushroomEarlyPrice1), int(megaMushroomEarlyPrice2), int(megaMushroomEarlyPrice34), 
        int(megaMushroomMidPrice1), int(megaMushroomMidPrice2), int(megaMushroomMidPrice34),
        int(megaMushroomLatePrice1), int(megaMushroomLatePrice2), int(megaMushroomLatePrice34),
        int(superMiniMushroomEarlyPrice1), int(superMiniMushroomEarlyPrice2), int(superMiniMushroomEarlyPrice34),
        int(superMiniMushroomMidPrice1), int(superMiniMushroomMidPrice2), int(superMiniMushroomMidPrice34),
        int(superMiniMushroomLatePrice1), int(superMiniMushroomLatePrice2), int(superMiniMushroomLatePrice34),
        int(superMegaMushroomEarlyPrice1), int(superMegaMushroomEarlyPrice2), int(superMegaMushroomEarlyPrice34),
        int(superMegaMushroomMidPrice1), int(superMegaMushroomMidPrice2), int(superMegaMushroomMidPrice34),
        int(superMegaMushroomLatePrice1), int(superMegaMushroomLatePrice2), int(superMegaMushroomLatePrice34),
        int(miniMegaHammerEarlyPrice1), int(miniMegaHammerEarlyPrice2), int(miniMegaHammerEarlyPrice34),
        int(miniMegaHammerMidPrice1), int(miniMegaHammerMidPrice2), int(miniMegaHammerMidPrice34),
        int(miniMegaHammerLatePrice1), int(miniMegaHammerLatePrice2), int(miniMegaHammerLatePrice34),
        int(warpPipeEarlyPrice1), int(warpPipeEarlyPrice2), int(warpPipeEarlyPrice34),
        int(warpPipeMidPrice1), int(warpPipeMidPrice2), int(warpPipeMidPrice34),
        int(warpPipeLatePrice1), int(warpPipeLatePrice2), int(warpPipeLatePrice34),
        int(swapCardEarlyPrice1), int(swapCardEarlyPrice2), int(swapCardEarlyPrice34),
        int(swapCardMidPrice1), int(swapCardMidPrice2), int(swapCardMidPrice34),
        int(swapCardLatePrice1), int(swapCardLatePrice2), int(swapCardLatePrice34),
        int(sparkyStickerEarlyPrice1), int(sparkyStickerEarlyPrice2), int(sparkyStickerEarlyPrice34),
        int(sparkyStickerMidPrice1), int(sparkyStickerMidPrice2), int(sparkyStickerMidPrice34),
        int(sparkyStickerLatePrice1), int(sparkyStickerLatePrice2), int(sparkyStickerLatePrice34),
        int(gaddlightEarlyPrice1), int(gaddlightEarlyPrice2), int(gaddlightEarlyPrice34),
        int(gaddlightMidPrice1), int(gaddlightMidPrice2), int(gaddlightMidPrice34),
        int(gaddlightLatePrice1), int(gaddlightLatePrice2), int(gaddlightLatePrice34),
        int(chompCallEarlyPrice1), int(chompCallEarlyPrice2), int(chompCallEarlyPrice34),
        int(chompCallMidPrice1), int(chompCallMidPrice2), int(chompCallMidPrice34),
        int(chompCallLatePrice1), int(chompCallLatePrice2), int(chompCallLatePrice34),
        int(bowserSuitEarlyPrice1), int(bowserSuitEarlyPrice2), int(bowserSuitEarlyPrice34),
        int(bowserSuitMidPrice1), int(bowserSuitMidPrice2), int(bowserSuitMidPrice34),
        int(bowserSuitLatePrice1), int(bowserSuitLatePrice2), int(bowserSuitLatePrice34),
        int(crystalBallEarlyPrice1), int(crystalBallEarlyPrice2), int(crystalBallEarlyPrice34),
        int(crystalBallMidPrice1), int(crystalBallMidPrice2), int(crystalBallMidPrice34),
        int(crystalBallLatePrice1), int(crystalBallLatePrice2), int(crystalBallLatePrice34),
        int(magicLampEarlyPrice1), int(magicLampEarlyPrice2), int(magicLampEarlyPrice34),
        int(magicLampMidPrice1), int(magicLampMidPrice2), int(magicLampMidPrice34),
        int(magicLampLatePrice1), int(magicLampLatePrice2), int(magicLampLatePrice34),
        int(itemBagEarlyPrice1), int(itemBagEarlyPrice2), int(itemBagEarlyPrice34),
        int(itemBagMidPrice1), int(itemBagMidPrice2), int(itemBagMidPrice34),
        int(itemBagLatePrice1), int(itemBagLatePrice2), int(itemBagLatePrice34)
    ])


    def convert_to_hex_weight(weight):
        try:
            weight_hex = hex(int(weight))
            if len(weight_hex) == 4:
                return weight_hex[2:]  # Remove '0x' prefix
            elif len(weight_hex) == 3:
                return "0" + weight_hex[2:]  # Add leading zero
            return weight_hex[2:]  # Return as is for other lengths
        except:
            return "00"  # Return default value on error


    # Mini Mushroom
    miniMushroomEarlyPrice1 = convert_to_hex_weight(miniMushroomEarlyPrice1)
    miniMushroomEarlyPrice2 = convert_to_hex_weight(miniMushroomEarlyPrice2)
    miniMushroomEarlyPrice34 = convert_to_hex_weight(miniMushroomEarlyPrice34)
    miniMushroomMidPrice1 = convert_to_hex_weight(miniMushroomMidPrice1)
    miniMushroomMidPrice2 = convert_to_hex_weight(miniMushroomMidPrice2)
    miniMushroomMidPrice34 = convert_to_hex_weight(miniMushroomMidPrice34)
    miniMushroomLatePrice1 = convert_to_hex_weight(miniMushroomLatePrice1)
    miniMushroomLatePrice2 = convert_to_hex_weight(miniMushroomLatePrice2)
    miniMushroomLatePrice34 = convert_to_hex_weight(miniMushroomLatePrice34)
    
    # Mega Mushroom
    megaMushroomEarlyPrice1 = convert_to_hex_weight(megaMushroomEarlyPrice1)
    megaMushroomEarlyPrice2 = convert_to_hex_weight(megaMushroomEarlyPrice2)
    megaMushroomEarlyPrice34 = convert_to_hex_weight(megaMushroomEarlyPrice34)
    megaMushroomMidPrice1 = convert_to_hex_weight(megaMushroomMidPrice1)
    megaMushroomMidPrice2 = convert_to_hex_weight(megaMushroomMidPrice2)
    megaMushroomMidPrice34 = convert_to_hex_weight(megaMushroomMidPrice34)
    megaMushroomLatePrice1 = convert_to_hex_weight(megaMushroomLatePrice1)
    megaMushroomLatePrice2 = convert_to_hex_weight(megaMushroomLatePrice2)
    megaMushroomLatePrice34 = convert_to_hex_weight(megaMushroomLatePrice34)

    # Super Mini Mushroom
    superMiniMushroomEarlyPrice1 = convert_to_hex_weight(superMiniMushroomEarlyPrice1)
    superMiniMushroomEarlyPrice2 = convert_to_hex_weight(superMiniMushroomEarlyPrice2)
    superMiniMushroomEarlyPrice34 = convert_to_hex_weight(superMiniMushroomEarlyPrice34)
    superMiniMushroomMidPrice1 = convert_to_hex_weight(superMiniMushroomMidPrice1)
    superMiniMushroomMidPrice2 = convert_to_hex_weight(superMiniMushroomMidPrice2)
    superMiniMushroomMidPrice34 = convert_to_hex_weight(superMiniMushroomMidPrice34)
    superMiniMushroomLatePrice1 = convert_to_hex_weight(superMiniMushroomLatePrice1)
    superMiniMushroomLatePrice2 = convert_to_hex_weight(superMiniMushroomLatePrice2)
    superMiniMushroomLatePrice34 = convert_to_hex_weight(superMiniMushroomLatePrice34)

    # Super Mega Mushroom
    superMegaMushroomEarlyPrice1 = convert_to_hex_weight(superMegaMushroomEarlyPrice1)
    superMegaMushroomEarlyPrice2 = convert_to_hex_weight(superMegaMushroomEarlyPrice2)
    superMegaMushroomEarlyPrice34 = convert_to_hex_weight(superMegaMushroomEarlyPrice34)
    superMegaMushroomMidPrice1 = convert_to_hex_weight(superMegaMushroomMidPrice1)
    superMegaMushroomMidPrice2 = convert_to_hex_weight(superMegaMushroomMidPrice2)
    superMegaMushroomMidPrice34 = convert_to_hex_weight(superMegaMushroomMidPrice34)
    superMegaMushroomLatePrice1 = convert_to_hex_weight(superMegaMushroomLatePrice1)
    superMegaMushroomLatePrice2 = convert_to_hex_weight(superMegaMushroomLatePrice2)
    superMegaMushroomLatePrice34 = convert_to_hex_weight(superMegaMushroomLatePrice34)

    # Mini Mega Hammer
    miniMegaHammerEarlyPrice1 = convert_to_hex_weight(miniMegaHammerEarlyPrice1)
    miniMegaHammerEarlyPrice2 = convert_to_hex_weight(miniMegaHammerEarlyPrice2)
    miniMegaHammerEarlyPrice34 = convert_to_hex_weight(miniMegaHammerEarlyPrice34)
    miniMegaHammerMidPrice1 = convert_to_hex_weight(miniMegaHammerMidPrice1)
    miniMegaHammerMidPrice2 = convert_to_hex_weight(miniMegaHammerMidPrice2)
    miniMegaHammerMidPrice34 = convert_to_hex_weight(miniMegaHammerMidPrice34)
    miniMegaHammerLatePrice1 = convert_to_hex_weight(miniMegaHammerLatePrice1)
    miniMegaHammerLatePrice2 = convert_to_hex_weight(miniMegaHammerLatePrice2)
    miniMegaHammerLatePrice34 = convert_to_hex_weight(miniMegaHammerLatePrice34)

    # Warp Pipe
    warpPipeEarlyPrice1 = convert_to_hex_weight(warpPipeEarlyPrice1)
    warpPipeEarlyPrice2 = convert_to_hex_weight(warpPipeEarlyPrice2)
    warpPipeEarlyPrice34 = convert_to_hex_weight(warpPipeEarlyPrice34)
    warpPipeMidPrice1 = convert_to_hex_weight(warpPipeMidPrice1)
    warpPipeMidPrice2 = convert_to_hex_weight(warpPipeMidPrice2)
    warpPipeMidPrice34 = convert_to_hex_weight(warpPipeMidPrice34)
    warpPipeLatePrice1 = convert_to_hex_weight(warpPipeLatePrice1)
    warpPipeLatePrice2 = convert_to_hex_weight(warpPipeLatePrice2)
    warpPipeLatePrice34 = convert_to_hex_weight(warpPipeLatePrice34)

    # Swap Card
    swapCardEarlyPrice1 = convert_to_hex_weight(swapCardEarlyPrice1)
    swapCardEarlyPrice2 = convert_to_hex_weight(swapCardEarlyPrice2)
    swapCardEarlyPrice34 = convert_to_hex_weight(swapCardEarlyPrice34)
    swapCardMidPrice1 = convert_to_hex_weight(swapCardMidPrice1)
    swapCardMidPrice2 = convert_to_hex_weight(swapCardMidPrice2)
    swapCardMidPrice34 = convert_to_hex_weight(swapCardMidPrice34)
    swapCardLatePrice1 = convert_to_hex_weight(swapCardLatePrice1)
    swapCardLatePrice2 = convert_to_hex_weight(swapCardLatePrice2)
    swapCardLatePrice34 = convert_to_hex_weight(swapCardLatePrice34)

    # Sparky Sticker
    sparkyStickerEarlyPrice1 = convert_to_hex_weight(sparkyStickerEarlyPrice1)
    sparkyStickerEarlyPrice2 = convert_to_hex_weight(sparkyStickerEarlyPrice2)
    sparkyStickerEarlyPrice34 = convert_to_hex_weight(sparkyStickerEarlyPrice34)
    sparkyStickerMidPrice1 = convert_to_hex_weight(sparkyStickerMidPrice1)
    sparkyStickerMidPrice2 = convert_to_hex_weight(sparkyStickerMidPrice2)
    sparkyStickerMidPrice34 = convert_to_hex_weight(sparkyStickerMidPrice34)
    sparkyStickerLatePrice1 = convert_to_hex_weight(sparkyStickerLatePrice1)
    sparkyStickerLatePrice2 = convert_to_hex_weight(sparkyStickerLatePrice2)
    sparkyStickerLatePrice34 = convert_to_hex_weight(sparkyStickerLatePrice34)

    # Gaddlight
    gaddlightEarlyPrice1 = convert_to_hex_weight(gaddlightEarlyPrice1)
    gaddlightEarlyPrice2 = convert_to_hex_weight(gaddlightEarlyPrice2)
    gaddlightEarlyPrice34 = convert_to_hex_weight(gaddlightEarlyPrice34)
    gaddlightMidPrice1 = convert_to_hex_weight(gaddlightMidPrice1)
    gaddlightMidPrice2 = convert_to_hex_weight(gaddlightMidPrice2)
    gaddlightMidPrice34 = convert_to_hex_weight(gaddlightMidPrice34)
    gaddlightLatePrice1 = convert_to_hex_weight(gaddlightLatePrice1)
    gaddlightLatePrice2 = convert_to_hex_weight(gaddlightLatePrice2)
    gaddlightLatePrice34 = convert_to_hex_weight(gaddlightLatePrice34)

    # Chomp Call
    chompCallEarlyPrice1 = convert_to_hex_weight(chompCallEarlyPrice1)
    chompCallEarlyPrice2 = convert_to_hex_weight(chompCallEarlyPrice2)
    chompCallEarlyPrice34 = convert_to_hex_weight(chompCallEarlyPrice34)
    chompCallMidPrice1 = convert_to_hex_weight(chompCallMidPrice1)
    chompCallMidPrice2 = convert_to_hex_weight(chompCallMidPrice2)
    chompCallMidPrice34 = convert_to_hex_weight(chompCallMidPrice34)
    chompCallLatePrice1 = convert_to_hex_weight(chompCallLatePrice1)
    chompCallLatePrice2 = convert_to_hex_weight(chompCallLatePrice2)
    chompCallLatePrice34 = convert_to_hex_weight(chompCallLatePrice34)

    # Bowser Suit
    bowserSuitEarlyPrice1 = convert_to_hex_weight(bowserSuitEarlyPrice1)
    bowserSuitEarlyPrice2 = convert_to_hex_weight(bowserSuitEarlyPrice2)
    bowserSuitEarlyPrice34 = convert_to_hex_weight(bowserSuitEarlyPrice34)
    bowserSuitMidPrice1 = convert_to_hex_weight(bowserSuitMidPrice1)
    bowserSuitMidPrice2 = convert_to_hex_weight(bowserSuitMidPrice2)
    bowserSuitMidPrice34 = convert_to_hex_weight(bowserSuitMidPrice34)
    bowserSuitLatePrice1 = convert_to_hex_weight(bowserSuitLatePrice1)
    bowserSuitLatePrice2 = convert_to_hex_weight(bowserSuitLatePrice2)
    bowserSuitLatePrice34 = convert_to_hex_weight(bowserSuitLatePrice34)

    # Crystal Ball
    crystalBallEarlyPrice1 = convert_to_hex_weight(crystalBallEarlyPrice1)
    crystalBallEarlyPrice2 = convert_to_hex_weight(crystalBallEarlyPrice2)
    crystalBallEarlyPrice34 = convert_to_hex_weight(crystalBallEarlyPrice34)
    crystalBallMidPrice1 = convert_to_hex_weight(crystalBallMidPrice1)
    crystalBallMidPrice2 = convert_to_hex_weight(crystalBallMidPrice2)
    crystalBallMidPrice34 = convert_to_hex_weight(crystalBallMidPrice34)
    crystalBallLatePrice1 = convert_to_hex_weight(crystalBallLatePrice1)
    crystalBallLatePrice2 = convert_to_hex_weight(crystalBallLatePrice2)
    crystalBallLatePrice34 = convert_to_hex_weight(crystalBallLatePrice34)

    # Magic Lamp
    magicLampEarlyPrice1 = convert_to_hex_weight(magicLampEarlyPrice1)
    magicLampEarlyPrice2 = convert_to_hex_weight(magicLampEarlyPrice2)
    magicLampEarlyPrice34 = convert_to_hex_weight(magicLampEarlyPrice34)
    magicLampMidPrice1 = convert_to_hex_weight(magicLampMidPrice1)
    magicLampMidPrice2 = convert_to_hex_weight(magicLampMidPrice2)
    magicLampMidPrice34 = convert_to_hex_weight(magicLampMidPrice34)
    magicLampLatePrice1 = convert_to_hex_weight(magicLampLatePrice1)
    magicLampLatePrice2 = convert_to_hex_weight(magicLampLatePrice2)
    magicLampLatePrice34 = convert_to_hex_weight(magicLampLatePrice34)

    # Item Bag
    itemBagEarlyPrice1 = convert_to_hex_weight(itemBagEarlyPrice1)
    itemBagEarlyPrice2 = convert_to_hex_weight(itemBagEarlyPrice2)
    itemBagEarlyPrice34 = convert_to_hex_weight(itemBagEarlyPrice34)
    itemBagMidPrice1 = convert_to_hex_weight(itemBagMidPrice1)
    itemBagMidPrice2 = convert_to_hex_weight(itemBagMidPrice2)
    itemBagMidPrice34 = convert_to_hex_weight(itemBagMidPrice34)
    itemBagLatePrice1 = convert_to_hex_weight(itemBagLatePrice1)
    itemBagLatePrice2 = convert_to_hex_weight(itemBagLatePrice2)
    itemBagLatePrice34 = convert_to_hex_weight(itemBagLatePrice34)

    minCoins = convert_to_hex_weight(minCoins)

    generatedCode = getItemShopPricesFour(minCoins, miniMushroomEarlyPrice1, miniMushroomEarlyPrice2, miniMushroomEarlyPrice34, miniMushroomMidPrice1, miniMushroomMidPrice2, miniMushroomMidPrice34, miniMushroomLatePrice1, miniMushroomLatePrice2, miniMushroomLatePrice34, megaMushroomEarlyPrice1, megaMushroomEarlyPrice2, megaMushroomEarlyPrice34, megaMushroomMidPrice1, megaMushroomMidPrice2, megaMushroomMidPrice34, megaMushroomLatePrice1, megaMushroomLatePrice2, megaMushroomLatePrice34, superMiniMushroomEarlyPrice1, superMiniMushroomEarlyPrice2, superMiniMushroomEarlyPrice34, superMiniMushroomMidPrice1, superMiniMushroomMidPrice2, superMiniMushroomMidPrice34, superMiniMushroomLatePrice1, superMiniMushroomLatePrice2, superMiniMushroomLatePrice34, superMegaMushroomEarlyPrice1, superMegaMushroomEarlyPrice2, superMegaMushroomEarlyPrice34, superMegaMushroomMidPrice1, superMegaMushroomMidPrice2, superMegaMushroomMidPrice34, superMegaMushroomLatePrice1, superMegaMushroomLatePrice2, superMegaMushroomLatePrice34, miniMegaHammerEarlyPrice1, miniMegaHammerEarlyPrice2, miniMegaHammerEarlyPrice34, miniMegaHammerMidPrice1, miniMegaHammerMidPrice2, miniMegaHammerMidPrice34, miniMegaHammerLatePrice1, miniMegaHammerLatePrice2, miniMegaHammerLatePrice34, warpPipeEarlyPrice1, warpPipeEarlyPrice2, warpPipeEarlyPrice34, warpPipeMidPrice1, warpPipeMidPrice2, warpPipeMidPrice34, warpPipeLatePrice1, warpPipeLatePrice2, warpPipeLatePrice34, swapCardEarlyPrice1, swapCardEarlyPrice2, swapCardEarlyPrice34, swapCardMidPrice1, swapCardMidPrice2, swapCardMidPrice34, swapCardLatePrice1, swapCardLatePrice2, swapCardLatePrice34, sparkyStickerEarlyPrice1, sparkyStickerEarlyPrice2, sparkyStickerEarlyPrice34, sparkyStickerMidPrice1, sparkyStickerMidPrice2, sparkyStickerMidPrice34, sparkyStickerLatePrice1, sparkyStickerLatePrice2, sparkyStickerLatePrice34, gaddlightEarlyPrice1, gaddlightEarlyPrice2, gaddlightEarlyPrice34, gaddlightMidPrice1, gaddlightMidPrice2, gaddlightMidPrice34, gaddlightLatePrice1, gaddlightLatePrice2, gaddlightLatePrice34, chompCallEarlyPrice1, chompCallEarlyPrice2, chompCallEarlyPrice34, chompCallMidPrice1, chompCallMidPrice2, chompCallMidPrice34, chompCallLatePrice1, chompCallLatePrice2, chompCallLatePrice34, bowserSuitEarlyPrice1, bowserSuitEarlyPrice2, bowserSuitEarlyPrice34, bowserSuitMidPrice1, bowserSuitMidPrice2, bowserSuitMidPrice34, bowserSuitLatePrice1, bowserSuitLatePrice2, bowserSuitLatePrice34, crystalBallEarlyPrice1, crystalBallEarlyPrice2, crystalBallEarlyPrice34, crystalBallMidPrice1, crystalBallMidPrice2, crystalBallMidPrice34, crystalBallLatePrice1, crystalBallLatePrice2, crystalBallLatePrice34, magicLampEarlyPrice1, magicLampEarlyPrice2, magicLampEarlyPrice34, magicLampMidPrice1, magicLampMidPrice2, magicLampMidPrice34, magicLampLatePrice1, magicLampLatePrice2, magicLampLatePrice34, itemBagEarlyPrice1, itemBagEarlyPrice2, itemBagEarlyPrice34, itemBagMidPrice1, itemBagMidPrice2, itemBagMidPrice34, itemBagLatePrice1, itemBagLatePrice2, itemBagLatePrice34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def itemsEvent_mp4ShopOdds(miniMushroomEarlyOdds1, miniMushroomEarlyOdds2, miniMushroomEarlyOdds34, miniMushroomMidOdds1, miniMushroomMidOdds2, miniMushroomMidOdds34, miniMushroomLateOdds1, miniMushroomLateOdds2, miniMushroomLateOdds34, megaMushroomEarlyOdds1, megaMushroomEarlyOdds2, megaMushroomEarlyOdds34, megaMushroomMidOdds1, megaMushroomMidOdds2, megaMushroomMidOdds34, megaMushroomLateOdds1, megaMushroomLateOdds2, megaMushroomLateOdds34, superMiniMushroomEarlyOdds1, superMiniMushroomEarlyOdds2, superMiniMushroomEarlyOdds34, superMiniMushroomMidOdds1, superMiniMushroomMidOdds2, superMiniMushroomMidOdds34, superMiniMushroomLateOdds1, superMiniMushroomLateOdds2, superMiniMushroomLateOdds34, superMegaMushroomEarlyOdds1, superMegaMushroomEarlyOdds2, superMegaMushroomEarlyOdds34, superMegaMushroomMidOdds1, superMegaMushroomMidOdds2, superMegaMushroomMidOdds34, superMegaMushroomLateOdds1, superMegaMushroomLateOdds2, superMegaMushroomLateOdds34, miniMegaHammerEarlyOdds1, miniMegaHammerEarlyOdds2, miniMegaHammerEarlyOdds34, miniMegaHammerMidOdds1, miniMegaHammerMidOdds2, miniMegaHammerMidOdds34, miniMegaHammerLateOdds1, miniMegaHammerLateOdds2, miniMegaHammerLateOdds34, warpPipeEarlyOdds1, warpPipeEarlyOdds2, warpPipeEarlyOdds34, warpPipeMidOdds1, warpPipeMidOdds2, warpPipeMidOdds34, warpPipeLateOdds1, warpPipeLateOdds2, warpPipeLateOdds34, swapCardEarlyOdds1, swapCardEarlyOdds2, swapCardEarlyOdds34, swapCardMidOdds1, swapCardMidOdds2, swapCardMidOdds34, swapCardLateOdds1, swapCardLateOdds2, swapCardLateOdds34, sparkyStickerEarlyOdds1, sparkyStickerEarlyOdds2, sparkyStickerEarlyOdds34, sparkyStickerMidOdds1, sparkyStickerMidOdds2, sparkyStickerMidOdds34, sparkyStickerLateOdds1, sparkyStickerLateOdds2, sparkyStickerLateOdds34, gaddlightEarlyOdds1, gaddlightEarlyOdds2, gaddlightEarlyOdds34, gaddlightMidOdds1, gaddlightMidOdds2, gaddlightMidOdds34, gaddlightLateOdds1, gaddlightLateOdds2, gaddlightLateOdds34, chompCallEarlyOdds1, chompCallEarlyOdds2, chompCallEarlyOdds34, chompCallMidOdds1, chompCallMidOdds2, chompCallMidOdds34, chompCallLateOdds1, chompCallLateOdds2, chompCallLateOdds34, bowserSuitEarlyOdds1, bowserSuitEarlyOdds2, bowserSuitEarlyOdds34, bowserSuitMidOdds1, bowserSuitMidOdds2, bowserSuitMidOdds34, bowserSuitLateOdds1, bowserSuitLateOdds2, bowserSuitLateOdds34, crystalBallEarlyOdds1, crystalBallEarlyOdds2, crystalBallEarlyOdds34, crystalBallMidOdds1, crystalBallMidOdds2, crystalBallMidOdds34, crystalBallLateOdds1, crystalBallLateOdds2, crystalBallLateOdds34, magicLampEarlyOdds1, magicLampEarlyOdds2, magicLampEarlyOdds34, magicLampMidOdds1, magicLampMidOdds2, magicLampMidOdds34, magicLampLateOdds1, magicLampLateOdds2, magicLampLateOdds34, itemBagEarlyOdds1, itemBagEarlyOdds2, itemBagEarlyOdds34, itemBagMidOdds1, itemBagMidOdds2, itemBagMidOdds34, itemBagLateOdds1, itemBagLateOdds2, itemBagLateOdds34):
    pass

def itemsEvent_mp4ShopOddsDX(miniMushroomEarlyOdds1, miniMushroomEarlyOdds2, miniMushroomEarlyOdds34, miniMushroomMidOdds1, miniMushroomMidOdds2, miniMushroomMidOdds34, miniMushroomLateOdds1, miniMushroomLateOdds2, miniMushroomLateOdds34, megaMushroomEarlyOdds1, megaMushroomEarlyOdds2, megaMushroomEarlyOdds34, megaMushroomMidOdds1, megaMushroomMidOdds2, megaMushroomMidOdds34, megaMushroomLateOdds1, megaMushroomLateOdds2, megaMushroomLateOdds34, superMiniMushroomEarlyOdds1, superMiniMushroomEarlyOdds2, superMiniMushroomEarlyOdds34, superMiniMushroomMidOdds1, superMiniMushroomMidOdds2, superMiniMushroomMidOdds34, superMiniMushroomLateOdds1, superMiniMushroomLateOdds2, superMiniMushroomLateOdds34, superMegaMushroomEarlyOdds1, superMegaMushroomEarlyOdds2, superMegaMushroomEarlyOdds34, superMegaMushroomMidOdds1, superMegaMushroomMidOdds2, superMegaMushroomMidOdds34, superMegaMushroomLateOdds1, superMegaMushroomLateOdds2, superMegaMushroomLateOdds34, miniMegaHammerEarlyOdds1, miniMegaHammerEarlyOdds2, miniMegaHammerEarlyOdds34, miniMegaHammerMidOdds1, miniMegaHammerMidOdds2, miniMegaHammerMidOdds34, miniMegaHammerLateOdds1, miniMegaHammerLateOdds2, miniMegaHammerLateOdds34, warpPipeEarlyOdds1, warpPipeEarlyOdds2, warpPipeEarlyOdds34, warpPipeMidOdds1, warpPipeMidOdds2, warpPipeMidOdds34, warpPipeLateOdds1, warpPipeLateOdds2, warpPipeLateOdds34, swapCardEarlyOdds1, swapCardEarlyOdds2, swapCardEarlyOdds34, swapCardMidOdds1, swapCardMidOdds2, swapCardMidOdds34, swapCardLateOdds1, swapCardLateOdds2, swapCardLateOdds34, sparkyStickerEarlyOdds1, sparkyStickerEarlyOdds2, sparkyStickerEarlyOdds34, sparkyStickerMidOdds1, sparkyStickerMidOdds2, sparkyStickerMidOdds34, sparkyStickerLateOdds1, sparkyStickerLateOdds2, sparkyStickerLateOdds34, gaddlightEarlyOdds1, gaddlightEarlyOdds2, gaddlightEarlyOdds34, gaddlightMidOdds1, gaddlightMidOdds2, gaddlightMidOdds34, gaddlightLateOdds1, gaddlightLateOdds2, gaddlightLateOdds34, chompCallEarlyOdds1, chompCallEarlyOdds2, chompCallEarlyOdds34, chompCallMidOdds1, chompCallMidOdds2, chompCallMidOdds34, chompCallLateOdds1, chompCallLateOdds2, chompCallLateOdds34, bowserSuitEarlyOdds1, bowserSuitEarlyOdds2, bowserSuitEarlyOdds34, bowserSuitMidOdds1, bowserSuitMidOdds2, bowserSuitMidOdds34, bowserSuitLateOdds1, bowserSuitLateOdds2, bowserSuitLateOdds34, crystalBallEarlyOdds1, crystalBallEarlyOdds2, crystalBallEarlyOdds34, crystalBallMidOdds1, crystalBallMidOdds2, crystalBallMidOdds34, crystalBallLateOdds1, crystalBallLateOdds2, crystalBallLateOdds34, magicLampEarlyOdds1, magicLampEarlyOdds2, magicLampEarlyOdds34, magicLampMidOdds1, magicLampMidOdds2, magicLampMidOdds34, magicLampLateOdds1, magicLampLateOdds2, magicLampLateOdds34, itemBagEarlyOdds1, itemBagEarlyOdds2, itemBagEarlyOdds34, itemBagMidOdds1, itemBagMidOdds2, itemBagMidOdds34, itemBagLateOdds1, itemBagLateOdds2, itemBagLateOdds34, mushroomEarlyOdds1, mushroomEarlyOdds2, mushroomEarlyOdds34, mushroomMidOdds1, mushroomMidOdds2, mushroomMidOdds34, mushroomLateOdds1, mushroomLateOdds2, mushroomLateOdds34, goldenMushroomEarlyOdds1, goldenMushroomEarlyOdds2, goldenMushroomEarlyOdds34, goldenMushroomMidOdds1, goldenMushroomMidOdds2, goldenMushroomMidOdds34, goldenMushroomLateOdds1, goldenMushroomLateOdds2, goldenMushroomLateOdds34, reverseMushroomEarlyOdds1, reverseMushroomEarlyOdds2, reverseMushroomEarlyOdds34, reverseMushroomMidOdds1, reverseMushroomMidOdds2, reverseMushroomMidOdds34, reverseMushroomLateOdds1, reverseMushroomLateOdds2, reverseMushroomLateOdds34, poisonMushroomEarlyOdds1, poisonMushroomEarlyOdds2, poisonMushroomEarlyOdds34, poisonMushroomMidOdds1, poisonMushroomMidOdds2, poisonMushroomMidOdds34, poisonMushroomLateOdds1, poisonMushroomLateOdds2, poisonMushroomLateOdds34, triplePoisonMushroomEarlyOdds1, triplePoisonMushroomEarlyOdds2, triplePoisonMushroomEarlyOdds34, triplePoisonMushroomMidOdds1, triplePoisonMushroomMidOdds2, triplePoisonMushroomMidOdds34, triplePoisonMushroomLateOdds1, triplePoisonMushroomLateOdds2, triplePoisonMushroomLateOdds34, celluarShopperEarlyOdds1, celluarShopperEarlyOdds2, celluarShopperEarlyOdds34, celluarShopperMidOdds1, celluarShopperMidOdds2, celluarShopperMidOdds34, celluarShopperLateOdds1, celluarShopperLateOdds2, celluarShopperLateOdds34, skeletonKeyEarlyOdds1, skeletonKeyEarlyOdds2, skeletonKeyEarlyOdds34, skeletonKeyMidOdds1, skeletonKeyMidOdds2, skeletonKeyMidOdds34, skeletonKeyLateOdds1, skeletonKeyLateOdds2, skeletonKeyLateOdds34, plunderChestEarlyOdds1, plunderChestEarlyOdds2, plunderChestEarlyOdds34, plunderChestMidOdds1, plunderChestMidOdds2, plunderChestMidOdds34, plunderChestLateOdds1, plunderChestLateOdds2, plunderChestLateOdds34, gaddbrushEarlyOdds1, gaddbrushEarlyOdds2, gaddbrushEarlyOdds34, gaddbrushMidOdds1, gaddbrushMidOdds2, gaddbrushMidOdds34, gaddbrushLateOdds1, gaddbrushLateOdds2, gaddbrushLateOdds34, warpBlockEarlyOdds1, warpBlockEarlyOdds2, warpBlockEarlyOdds34, warpBlockMidOdds1, warpBlockMidOdds2, warpBlockMidOdds34, warpBlockLateOdds1, warpBlockLateOdds2, warpBlockLateOdds34, flyGuyEarlyOdds1, flyGuyEarlyOdds2, flyGuyEarlyOdds34, flyGuyMidOdds1, flyGuyMidOdds2, flyGuyMidOdds34, flyGuyLateOdds1, flyGuyLateOdds2, flyGuyLateOdds34, plusBlockEarlyOdds1, plusBlockEarlyOdds2, plusBlockEarlyOdds34, plusBlockMidOdds1, plusBlockMidOdds2, plusBlockMidOdds34, plusBlockLateOdds1, plusBlockLateOdds2, plusBlockLateOdds34, minusBlockEarlyOdds1, minusBlockEarlyOdds2, minusBlockEarlyOdds34, minusBlockMidOdds1, minusBlockMidOdds2, minusBlockMidOdds34, minusBlockLateOdds1, minusBlockLateOdds2, minusBlockLateOdds34, speedBlockEarlyOdds1, speedBlockEarlyOdds2, speedBlockEarlyOdds34, speedBlockMidOdds1, speedBlockMidOdds2, speedBlockMidOdds34, speedBlockLateOdds1, speedBlockLateOdds2, speedBlockLateOdds34, slowBlockEarlyOdds1, slowBlockEarlyOdds2, slowBlockEarlyOdds34, slowBlockMidOdds1, slowBlockMidOdds2, slowBlockMidOdds34, slowBlockLateOdds1, slowBlockLateOdds2, slowBlockLateOdds34, bowserPhoneEarlyOdds1, bowserPhoneEarlyOdds2, bowserPhoneEarlyOdds34, bowserPhoneMidOdds1, bowserPhoneMidOdds2, bowserPhoneMidOdds34, bowserPhoneLateOdds1, bowserPhoneLateOdds2, bowserPhoneLateOdds34, doubleDipEarlyOdds1, doubleDipEarlyOdds2, doubleDipEarlyOdds34, doubleDipMidOdds1, doubleDipMidOdds2, doubleDipMidOdds34, doubleDipLateOdds1, doubleDipLateOdds2, doubleDipLateOdds34, hiddenBlockCardEarlyOdds1, hiddenBlockCardEarlyOdds2, hiddenBlockCardEarlyOdds34, hiddenBlockCardMidOdds1, hiddenBlockCardMidOdds2, hiddenBlockCardMidOdds34, hiddenBlockCardLateOdds1, hiddenBlockCardLateOdds2, hiddenBlockCardLateOdds34, barterBoxEarlyOdds1, barterBoxEarlyOdds2, barterBoxEarlyOdds34, barterBoxMidOdds1, barterBoxMidOdds2, barterBoxMidOdds34, barterBoxLateOdds1, barterBoxLateOdds2, barterBoxLateOdds34, superWarpPipeEarlyOdds1, superWarpPipeEarlyOdds2, superWarpPipeEarlyOdds34, superWarpPipeMidOdds1, superWarpPipeMidOdds2, superWarpPipeMidOdds34, superWarpPipeLateOdds1, superWarpPipeLateOdds2, superWarpPipeLateOdds34, chanceTimeCharmEarlyOdds1, chanceTimeCharmEarlyOdds2, chanceTimeCharmEarlyOdds34, chanceTimeCharmMidOdds1, chanceTimeCharmMidOdds2, chanceTimeCharmMidOdds34, chanceTimeCharmLateOdds1, chanceTimeCharmLateOdds2, chanceTimeCharmLateOdds34, wackyWatchEarlyOdds1, wackyWatchEarlyOdds2, wackyWatchEarlyOdds34, wackyWatchMidOdds1, wackyWatchMidOdds2, wackyWatchMidOdds34, wackyWatchLateOdds1, wackyWatchLateOdds2, wackyWatchLateOdds34):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    # Mini Mushroom
    miniMushroomEarlyOdds1 = get_capsule_value(miniMushroomEarlyOdds1) or "5"
    miniMushroomEarlyOdds2 = get_capsule_value(miniMushroomEarlyOdds2) or "5"
    miniMushroomEarlyOdds34 = get_capsule_value(miniMushroomEarlyOdds34) or "5"
    miniMushroomMidOdds1 = get_capsule_value(miniMushroomMidOdds1) or "5"
    miniMushroomMidOdds2 = get_capsule_value(miniMushroomMidOdds2) or "5"
    miniMushroomMidOdds34 = get_capsule_value(miniMushroomMidOdds34) or "5"
    miniMushroomLateOdds1 = get_capsule_value(miniMushroomLateOdds1) or "5"
    miniMushroomLateOdds2 = get_capsule_value(miniMushroomLateOdds2) or "5"
    miniMushroomLateOdds34 = get_capsule_value(miniMushroomLateOdds34) or "5"
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = get_capsule_value(megaMushroomEarlyOdds1) or "5"
    megaMushroomEarlyOdds2 = get_capsule_value(megaMushroomEarlyOdds2) or "5"
    megaMushroomEarlyOdds34 = get_capsule_value(megaMushroomEarlyOdds34) or "5"
    megaMushroomMidOdds1 = get_capsule_value(megaMushroomMidOdds1) or "5"
    megaMushroomMidOdds2 = get_capsule_value(megaMushroomMidOdds2) or "5"
    megaMushroomMidOdds34 = get_capsule_value(megaMushroomMidOdds34) or "5"
    megaMushroomLateOdds1 = get_capsule_value(megaMushroomLateOdds1) or "5"
    megaMushroomLateOdds2 = get_capsule_value(megaMushroomLateOdds2) or "5"
    megaMushroomLateOdds34 = get_capsule_value(megaMushroomLateOdds34) or "5"

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = get_capsule_value(superMiniMushroomEarlyOdds1) or "10"
    superMiniMushroomEarlyOdds2 = get_capsule_value(superMiniMushroomEarlyOdds2) or "10"
    superMiniMushroomEarlyOdds34 = get_capsule_value(superMiniMushroomEarlyOdds34) or "10"
    superMiniMushroomMidOdds1 = get_capsule_value(superMiniMushroomMidOdds1) or "10"
    superMiniMushroomMidOdds2 = get_capsule_value(superMiniMushroomMidOdds2) or "10"
    superMiniMushroomMidOdds34 = get_capsule_value(superMiniMushroomMidOdds34) or "10"
    superMiniMushroomLateOdds1 = get_capsule_value(superMiniMushroomLateOdds1) or "10"
    superMiniMushroomLateOdds2 = get_capsule_value(superMiniMushroomLateOdds2) or "10"
    superMiniMushroomLateOdds34 = get_capsule_value(superMiniMushroomLateOdds34) or "10"

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = get_capsule_value(superMegaMushroomEarlyOdds1) or "15"
    superMegaMushroomEarlyOdds2 = get_capsule_value(superMegaMushroomEarlyOdds2) or "15"
    superMegaMushroomEarlyOdds34 = get_capsule_value(superMegaMushroomEarlyOdds34) or "15"
    superMegaMushroomMidOdds1 = get_capsule_value(superMegaMushroomMidOdds1) or "15"
    superMegaMushroomMidOdds2 = get_capsule_value(superMegaMushroomMidOdds2) or "15"
    superMegaMushroomMidOdds34 = get_capsule_value(superMegaMushroomMidOdds34) or "15"
    superMegaMushroomLateOdds1 = get_capsule_value(superMegaMushroomLateOdds1) or "15"
    superMegaMushroomLateOdds2 = get_capsule_value(superMegaMushroomLateOdds2) or "15"
    superMegaMushroomLateOdds34 = get_capsule_value(superMegaMushroomLateOdds34) or "15"

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = get_capsule_value(miniMegaHammerEarlyOdds1) or "10"
    miniMegaHammerEarlyOdds2 = get_capsule_value(miniMegaHammerEarlyOdds2) or "10"
    miniMegaHammerEarlyOdds34 = get_capsule_value(miniMegaHammerEarlyOdds34) or "10"
    miniMegaHammerMidOdds1 = get_capsule_value(miniMegaHammerMidOdds1) or "10"
    miniMegaHammerMidOdds2 = get_capsule_value(miniMegaHammerMidOdds2) or "10"
    miniMegaHammerMidOdds34 = get_capsule_value(miniMegaHammerMidOdds34) or "10"
    miniMegaHammerLateOdds1 = get_capsule_value(miniMegaHammerLateOdds1) or "10"
    miniMegaHammerLateOdds2 = get_capsule_value(miniMegaHammerLateOdds2) or "10"
    miniMegaHammerLateOdds34 = get_capsule_value(miniMegaHammerLateOdds34) or "10"

    # Warp Pipe
    warpPipeEarlyOdds1 = get_capsule_value(warpPipeEarlyOdds1) or "10"
    warpPipeEarlyOdds2 = get_capsule_value(warpPipeEarlyOdds2) or "10"
    warpPipeEarlyOdds34 = get_capsule_value(warpPipeEarlyOdds34) or "10"
    warpPipeMidOdds1 = get_capsule_value(warpPipeMidOdds1) or "10"
    warpPipeMidOdds2 = get_capsule_value(warpPipeMidOdds2) or "10"
    warpPipeMidOdds34 = get_capsule_value(warpPipeMidOdds34) or "10"
    warpPipeLateOdds1 = get_capsule_value(warpPipeLateOdds1) or "10"
    warpPipeLateOdds2 = get_capsule_value(warpPipeLateOdds2) or "10"
    warpPipeLateOdds34 = get_capsule_value(warpPipeLateOdds34) or "10"

    # Swap Card
    swapCardEarlyOdds1 = get_capsule_value(swapCardEarlyOdds1) or "15"
    swapCardEarlyOdds2 = get_capsule_value(swapCardEarlyOdds2) or "15"
    swapCardEarlyOdds34 = get_capsule_value(swapCardEarlyOdds34) or "15"
    swapCardMidOdds1 = get_capsule_value(swapCardMidOdds1) or "15"
    swapCardMidOdds2 = get_capsule_value(swapCardMidOdds2) or "15"
    swapCardMidOdds34 = get_capsule_value(swapCardMidOdds34) or "15"
    swapCardLateOdds1 = get_capsule_value(swapCardLateOdds1) or "15"
    swapCardLateOdds2 = get_capsule_value(swapCardLateOdds2) or "15"
    swapCardLateOdds34 = get_capsule_value(swapCardLateOdds34) or "15"

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = get_capsule_value(sparkyStickerEarlyOdds1) or "5"
    sparkyStickerEarlyOdds2 = get_capsule_value(sparkyStickerEarlyOdds2) or "5"
    sparkyStickerEarlyOdds34 = get_capsule_value(sparkyStickerEarlyOdds34) or "5"
    sparkyStickerMidOdds1 = get_capsule_value(sparkyStickerMidOdds1) or "5"
    sparkyStickerMidOdds2 = get_capsule_value(sparkyStickerMidOdds2) or "5"
    sparkyStickerMidOdds34 = get_capsule_value(sparkyStickerMidOdds34) or "5"
    sparkyStickerLateOdds1 = get_capsule_value(sparkyStickerLateOdds1) or "5"
    sparkyStickerLateOdds2 = get_capsule_value(sparkyStickerLateOdds2) or "5"
    sparkyStickerLateOdds34 = get_capsule_value(sparkyStickerLateOdds34) or "5"

    # Gaddlight
    gaddlightEarlyOdds1 = get_capsule_value(gaddlightEarlyOdds1) or "15"
    gaddlightEarlyOdds2 = get_capsule_value(gaddlightEarlyOdds2) or "15"
    gaddlightEarlyOdds34 = get_capsule_value(gaddlightEarlyOdds34) or "15"
    gaddlightMidOdds1 = get_capsule_value(gaddlightMidOdds1) or "15"
    gaddlightMidOdds2 = get_capsule_value(gaddlightMidOdds2) or "15"
    gaddlightMidOdds34 = get_capsule_value(gaddlightMidOdds34) or "15"
    gaddlightLateOdds1 = get_capsule_value(gaddlightLateOdds1) or "15"
    gaddlightLateOdds2 = get_capsule_value(gaddlightLateOdds2) or "15"
    gaddlightLateOdds34 = get_capsule_value(gaddlightLateOdds34) or "15"

    # Chomp Call
    chompCallEarlyOdds1 = get_capsule_value(chompCallEarlyOdds1) or "10"
    chompCallEarlyOdds2 = get_capsule_value(chompCallEarlyOdds2) or "10"
    chompCallEarlyOdds34 = get_capsule_value(chompCallEarlyOdds34) or "10"
    chompCallMidOdds1 = get_capsule_value(chompCallMidOdds1) or "10"
    chompCallMidOdds2 = get_capsule_value(chompCallMidOdds2) or "10"
    chompCallMidOdds34 = get_capsule_value(chompCallMidOdds34) or "10"
    chompCallLateOdds1 = get_capsule_value(chompCallLateOdds1) or "10"
    chompCallLateOdds2 = get_capsule_value(chompCallLateOdds2) or "10"
    chompCallLateOdds34 = get_capsule_value(chompCallLateOdds34) or "10"

    # Bowser Suit
    bowserSuitEarlyOdds1 = get_capsule_value(bowserSuitEarlyOdds1) or "12"
    bowserSuitEarlyOdds2 = get_capsule_value(bowserSuitEarlyOdds2) or "12"
    bowserSuitEarlyOdds34 = get_capsule_value(bowserSuitEarlyOdds34) or "12"
    bowserSuitMidOdds1 = get_capsule_value(bowserSuitMidOdds1) or "12"
    bowserSuitMidOdds2 = get_capsule_value(bowserSuitMidOdds2) or "12"
    bowserSuitMidOdds34 = get_capsule_value(bowserSuitMidOdds34) or "12"
    bowserSuitLateOdds1 = get_capsule_value(bowserSuitLateOdds1) or "12"
    bowserSuitLateOdds2 = get_capsule_value(bowserSuitLateOdds2) or "12"
    bowserSuitLateOdds34 = get_capsule_value(bowserSuitLateOdds34) or "12"

    # Crystal Ball
    crystalBallEarlyOdds1 = get_capsule_value(crystalBallEarlyOdds1) or "25"
    crystalBallEarlyOdds2 = get_capsule_value(crystalBallEarlyOdds2) or "25"
    crystalBallEarlyOdds34 = get_capsule_value(crystalBallEarlyOdds34) or "25"
    crystalBallMidOdds1 = get_capsule_value(crystalBallMidOdds1) or "25"
    crystalBallMidOdds2 = get_capsule_value(crystalBallMidOdds2) or "25"
    crystalBallMidOdds34 = get_capsule_value(crystalBallMidOdds34) or "25"
    crystalBallLateOdds1 = get_capsule_value(crystalBallLateOdds1) or "25"
    crystalBallLateOdds2 = get_capsule_value(crystalBallLateOdds2) or "25"
    crystalBallLateOdds34 = get_capsule_value(crystalBallLateOdds34) or "25"

    # Magic Lamp
    magicLampEarlyOdds1 = get_capsule_value(magicLampEarlyOdds1) or "30"
    magicLampEarlyOdds2 = get_capsule_value(magicLampEarlyOdds2) or "30"
    magicLampEarlyOdds34 = get_capsule_value(magicLampEarlyOdds34) or "30"
    magicLampMidOdds1 = get_capsule_value(magicLampMidOdds1) or "30"
    magicLampMidOdds2 = get_capsule_value(magicLampMidOdds2) or "30"
    magicLampMidOdds34 = get_capsule_value(magicLampMidOdds34) or "30"
    magicLampLateOdds1 = get_capsule_value(magicLampLateOdds1) or "30"
    magicLampLateOdds2 = get_capsule_value(magicLampLateOdds2) or "30"
    magicLampLateOdds34 = get_capsule_value(magicLampLateOdds34) or "30"

    # Item Bag
    itemBagEarlyOdds1 = get_capsule_value(itemBagEarlyOdds1) or "30"
    itemBagEarlyOdds2 = get_capsule_value(itemBagEarlyOdds2) or "30"
    itemBagEarlyOdds34 = get_capsule_value(itemBagEarlyOdds34) or "30"
    itemBagMidOdds1 = get_capsule_value(itemBagMidOdds1) or "30"
    itemBagMidOdds2 = get_capsule_value(itemBagMidOdds2) or "30"
    itemBagMidOdds34 = get_capsule_value(itemBagMidOdds34) or "30"
    itemBagLateOdds1 = get_capsule_value(itemBagLateOdds1) or "30"
    itemBagLateOdds2 = get_capsule_value(itemBagLateOdds2) or "30"
    itemBagLateOdds34 = get_capsule_value(itemBagLateOdds34) or "30"

    # Mushroom: DX
    mushroomEarlyOdds1 = get_capsule_value(mushroomEarlyOdds1) or "5"
    mushroomEarlyOdds2 = get_capsule_value(mushroomEarlyOdds2) or "5"
    mushroomEarlyOdds34 = get_capsule_value(mushroomEarlyOdds34) or "5"
    mushroomMidOdds1 = get_capsule_value(mushroomMidOdds1) or "5"
    mushroomMidOdds2 = get_capsule_value(mushroomMidOdds2) or "5"
    mushroomMidOdds34 = get_capsule_value(mushroomMidOdds34) or "5"
    mushroomLateOdds1 = get_capsule_value(mushroomLateOdds1) or "5"
    mushroomLateOdds2 = get_capsule_value(mushroomLateOdds2) or "5"
    mushroomLateOdds34 = get_capsule_value(mushroomLateOdds34) or "5"

    # Golden Mushroom: DX
    goldenMushroomEarlyOdds1 = get_capsule_value(goldenMushroomEarlyOdds1) or "10"
    goldenMushroomEarlyOdds2 = get_capsule_value(goldenMushroomEarlyOdds2) or "10"
    goldenMushroomEarlyOdds34 = get_capsule_value(goldenMushroomEarlyOdds34) or "10"
    goldenMushroomMidOdds1 = get_capsule_value(goldenMushroomMidOdds1) or "10"
    goldenMushroomMidOdds2 = get_capsule_value(goldenMushroomMidOdds2) or "10"
    goldenMushroomMidOdds34 = get_capsule_value(goldenMushroomMidOdds34) or "10"
    goldenMushroomLateOdds1 = get_capsule_value(goldenMushroomLateOdds1) or "10"
    goldenMushroomLateOdds2 = get_capsule_value(goldenMushroomLateOdds2) or "10"
    goldenMushroomLateOdds34 = get_capsule_value(goldenMushroomLateOdds34) or "10"

    # Reverse Mushroom: DX
    reverseMushroomEarlyOdds1 = get_capsule_value(reverseMushroomEarlyOdds1) or "15"
    reverseMushroomEarlyOdds2 = get_capsule_value(reverseMushroomEarlyOdds2) or "15"
    reverseMushroomEarlyOdds34 = get_capsule_value(reverseMushroomEarlyOdds34) or "15"
    reverseMushroomMidOdds1 = get_capsule_value(reverseMushroomMidOdds1) or "15"
    reverseMushroomMidOdds2 = get_capsule_value(reverseMushroomMidOdds2) or "15"
    reverseMushroomMidOdds34 = get_capsule_value(reverseMushroomMidOdds34) or "15"
    reverseMushroomLateOdds1 = get_capsule_value(reverseMushroomLateOdds1) or "15"
    reverseMushroomLateOdds2 = get_capsule_value(reverseMushroomLateOdds2) or "15"
    reverseMushroomLateOdds34 = get_capsule_value(reverseMushroomLateOdds34) or "15"

    # Poison Mushroom: DX
    poisonMushroomEarlyOdds1 = get_capsule_value(poisonMushroomEarlyOdds1) or "5"
    poisonMushroomEarlyOdds2 = get_capsule_value(poisonMushroomEarlyOdds2) or "5"
    poisonMushroomEarlyOdds34 = get_capsule_value(poisonMushroomEarlyOdds34) or "5"
    poisonMushroomMidOdds1 = get_capsule_value(poisonMushroomMidOdds1) or "5"
    poisonMushroomMidOdds2 = get_capsule_value(poisonMushroomMidOdds2) or "5"
    poisonMushroomMidOdds34 = get_capsule_value(poisonMushroomMidOdds34) or "5"
    poisonMushroomLateOdds1 = get_capsule_value(poisonMushroomLateOdds1) or "5"
    poisonMushroomLateOdds2 = get_capsule_value(poisonMushroomLateOdds2) or "5"
    poisonMushroomLateOdds34 = get_capsule_value(poisonMushroomLateOdds34) or "5"
    
    # Bowser Phone: DX
    bowserPhoneEarlyOdds1 = get_capsule_value(bowserPhoneEarlyOdds1) or "10"
    bowserPhoneEarlyOdds2 = get_capsule_value(bowserPhoneEarlyOdds2) or "10"
    bowserPhoneEarlyOdds34 = get_capsule_value(bowserPhoneEarlyOdds34) or "10"
    bowserPhoneMidOdds1 = get_capsule_value(bowserPhoneMidOdds1) or "10"
    bowserPhoneMidOdds2 = get_capsule_value(bowserPhoneMidOdds2) or "10"
    bowserPhoneMidOdds34 = get_capsule_value(bowserPhoneMidOdds34) or "10"
    bowserPhoneLateOdds1 = get_capsule_value(bowserPhoneLateOdds1) or "10"
    bowserPhoneLateOdds2 = get_capsule_value(bowserPhoneLateOdds2) or "10"
    bowserPhoneLateOdds34 = get_capsule_value(bowserPhoneLateOdds34) or "10"

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyOdds1 = get_capsule_value(triplePoisonMushroomEarlyOdds1) or "15"
    triplePoisonMushroomEarlyOdds2 = get_capsule_value(triplePoisonMushroomEarlyOdds2) or "15"
    triplePoisonMushroomEarlyOdds34 = get_capsule_value(triplePoisonMushroomEarlyOdds34) or "15"
    triplePoisonMushroomMidOdds1 = get_capsule_value(triplePoisonMushroomMidOdds1) or "15"
    triplePoisonMushroomMidOdds2 = get_capsule_value(triplePoisonMushroomMidOdds2) or "15"
    triplePoisonMushroomMidOdds34 = get_capsule_value(triplePoisonMushroomMidOdds34) or "15"
    triplePoisonMushroomLateOdds1 = get_capsule_value(triplePoisonMushroomLateOdds1) or "15"
    triplePoisonMushroomLateOdds2 = get_capsule_value(triplePoisonMushroomLateOdds2) or "15"
    triplePoisonMushroomLateOdds34 = get_capsule_value(triplePoisonMushroomLateOdds34) or "15"

    # Celluar Shopper: DX
    celluarShopperEarlyOdds1 = get_capsule_value(celluarShopperEarlyOdds1) or "5"
    celluarShopperEarlyOdds2 = get_capsule_value(celluarShopperEarlyOdds2) or "5"
    celluarShopperEarlyOdds34 = get_capsule_value(celluarShopperEarlyOdds34) or "5"
    celluarShopperMidOdds1 = get_capsule_value(celluarShopperMidOdds1) or "5"
    celluarShopperMidOdds2 = get_capsule_value(celluarShopperMidOdds2) or "5"
    celluarShopperMidOdds34 = get_capsule_value(celluarShopperMidOdds34) or "5"
    celluarShopperLateOdds1 = get_capsule_value(celluarShopperLateOdds1) or "5"
    celluarShopperLateOdds2 = get_capsule_value(celluarShopperLateOdds2) or "5"
    celluarShopperLateOdds34 = get_capsule_value(celluarShopperLateOdds34) or "5"

    # Skeleton Key: DX
    skeletonKeyEarlyOdds1 = get_capsule_value(skeletonKeyEarlyOdds1) or "5"
    skeletonKeyEarlyOdds2 = get_capsule_value(skeletonKeyEarlyOdds2) or "5"
    skeletonKeyEarlyOdds34 = get_capsule_value(skeletonKeyEarlyOdds34) or "5"
    skeletonKeyMidOdds1 = get_capsule_value(skeletonKeyMidOdds1) or "5"
    skeletonKeyMidOdds2 = get_capsule_value(skeletonKeyMidOdds2) or "5"
    skeletonKeyMidOdds34 = get_capsule_value(skeletonKeyMidOdds34) or "5"
    skeletonKeyLateOdds1 = get_capsule_value(skeletonKeyLateOdds1) or "5"
    skeletonKeyLateOdds2 = get_capsule_value(skeletonKeyLateOdds2) or "5"
    skeletonKeyLateOdds34 = get_capsule_value(skeletonKeyLateOdds34) or "5"

    # Plunder Chest: DX
    plunderChestEarlyOdds1 = get_capsule_value(plunderChestEarlyOdds1) or "15"
    plunderChestEarlyOdds2 = get_capsule_value(plunderChestEarlyOdds2) or "15"
    plunderChestEarlyOdds34 = get_capsule_value(plunderChestEarlyOdds34) or "15"
    plunderChestMidOdds1 = get_capsule_value(plunderChestMidOdds1) or "15"
    plunderChestMidOdds2 = get_capsule_value(plunderChestMidOdds2) or "15"
    plunderChestMidOdds34 = get_capsule_value(plunderChestMidOdds34) or "15"
    plunderChestLateOdds1 = get_capsule_value(plunderChestLateOdds1) or "15"
    plunderChestLateOdds2 = get_capsule_value(plunderChestLateOdds2) or "15"
    plunderChestLateOdds34 = get_capsule_value(plunderChestLateOdds34) or "15"

    # Gaddbrush: DX
    gaddbrushEarlyOdds1 = get_capsule_value(gaddbrushEarlyOdds1) or "15"
    gaddbrushEarlyOdds2 = get_capsule_value(gaddbrushEarlyOdds2) or "15"
    gaddbrushEarlyOdds34 = get_capsule_value(gaddbrushEarlyOdds34) or "15"
    gaddbrushMidOdds1 = get_capsule_value(gaddbrushMidOdds1) or "15"
    gaddbrushMidOdds2 = get_capsule_value(gaddbrushMidOdds2) or "15"
    gaddbrushMidOdds34 = get_capsule_value(gaddbrushMidOdds34) or "15"
    gaddbrushLateOdds1 = get_capsule_value(gaddbrushLateOdds1) or "15"
    gaddbrushLateOdds2 = get_capsule_value(gaddbrushLateOdds2) or "15"
    gaddbrushLateOdds34 = get_capsule_value(gaddbrushLateOdds34) or "15"

    # Warp Block: DX
    warpBlockEarlyOdds1 = get_capsule_value(warpBlockEarlyOdds1) or "5"
    warpBlockEarlyOdds2 = get_capsule_value(warpBlockEarlyOdds2) or "5"
    warpBlockEarlyOdds34 = get_capsule_value(warpBlockEarlyOdds34) or "5"
    warpBlockMidOdds1 = get_capsule_value(warpBlockMidOdds1) or "5"
    warpBlockMidOdds2 = get_capsule_value(warpBlockMidOdds2) or "5"
    warpBlockMidOdds34 = get_capsule_value(warpBlockMidOdds34) or "5"
    warpBlockLateOdds1 = get_capsule_value(warpBlockLateOdds1) or "5"
    warpBlockLateOdds2 = get_capsule_value(warpBlockLateOdds2) or "5"
    warpBlockLateOdds34 = get_capsule_value(warpBlockLateOdds34) or "5"

    # Fly Guy: DX
    flyGuyEarlyOdds1 = get_capsule_value(flyGuyEarlyOdds1) or "12"
    flyGuyEarlyOdds2 = get_capsule_value(flyGuyEarlyOdds2) or "12"
    flyGuyEarlyOdds34 = get_capsule_value(flyGuyEarlyOdds34) or "12"
    flyGuyMidOdds1 = get_capsule_value(flyGuyMidOdds1) or "12"
    flyGuyMidOdds2 = get_capsule_value(flyGuyMidOdds2) or "12"
    flyGuyMidOdds34 = get_capsule_value(flyGuyMidOdds34) or "12"
    flyGuyLateOdds1 = get_capsule_value(flyGuyLateOdds1) or "12"
    flyGuyLateOdds2 = get_capsule_value(flyGuyLateOdds2) or "12"
    flyGuyLateOdds34 = get_capsule_value(flyGuyLateOdds34) or "12"

    # Plus Block: DX
    plusBlockEarlyOdds1 = get_capsule_value(plusBlockEarlyOdds1) or "10"
    plusBlockEarlyOdds2 = get_capsule_value(plusBlockEarlyOdds2) or "10"
    plusBlockEarlyOdds34 = get_capsule_value(plusBlockEarlyOdds34) or "10"
    plusBlockMidOdds1 = get_capsule_value(plusBlockMidOdds1) or "10"
    plusBlockMidOdds2 = get_capsule_value(plusBlockMidOdds2) or "10"
    plusBlockMidOdds34 = get_capsule_value(plusBlockMidOdds34) or "10"
    plusBlockLateOdds1 = get_capsule_value(plusBlockLateOdds1) or "10"
    plusBlockLateOdds2 = get_capsule_value(plusBlockLateOdds2) or "10"
    plusBlockLateOdds34 = get_capsule_value(plusBlockLateOdds34) or "10"

    # Minus Block: DX
    minusBlockEarlyOdds1 = get_capsule_value(minusBlockEarlyOdds1) or "10"
    minusBlockEarlyOdds2 = get_capsule_value(minusBlockEarlyOdds2) or "10"
    minusBlockEarlyOdds34 = get_capsule_value(minusBlockEarlyOdds34) or "10"
    minusBlockMidOdds1 = get_capsule_value(minusBlockMidOdds1) or "10"
    minusBlockMidOdds2 = get_capsule_value(minusBlockMidOdds2) or "10"
    minusBlockMidOdds34 = get_capsule_value(minusBlockMidOdds34) or "10"
    minusBlockLateOdds1 = get_capsule_value(minusBlockLateOdds1) or "10"
    minusBlockLateOdds2 = get_capsule_value(minusBlockLateOdds2) or "10"
    minusBlockLateOdds34 = get_capsule_value(minusBlockLateOdds34) or "10"

    # Speed Block: DX
    speedBlockEarlyOdds1 = get_capsule_value(speedBlockEarlyOdds1) or "12"
    speedBlockEarlyOdds2 = get_capsule_value(speedBlockEarlyOdds2) or "12"
    speedBlockEarlyOdds34 = get_capsule_value(speedBlockEarlyOdds34) or "12"
    speedBlockMidOdds1 = get_capsule_value(speedBlockMidOdds1) or "12"
    speedBlockMidOdds2 = get_capsule_value(speedBlockMidOdds2) or "12"
    speedBlockMidOdds34 = get_capsule_value(speedBlockMidOdds34) or "12"
    speedBlockLateOdds1 = get_capsule_value(speedBlockLateOdds1) or "12"
    speedBlockLateOdds2 = get_capsule_value(speedBlockLateOdds2) or "12"
    speedBlockLateOdds34 = get_capsule_value(speedBlockLateOdds34) or "12"

    # Slow Block: DX
    slowBlockEarlyOdds1 = get_capsule_value(slowBlockEarlyOdds1) or "12"
    slowBlockEarlyOdds2 = get_capsule_value(slowBlockEarlyOdds2) or "12"
    slowBlockEarlyOdds34 = get_capsule_value(slowBlockEarlyOdds34) or "12"
    slowBlockMidOdds1 = get_capsule_value(slowBlockMidOdds1) or "12"
    slowBlockMidOdds2 = get_capsule_value(slowBlockMidOdds2) or "12"
    slowBlockMidOdds34 = get_capsule_value(slowBlockMidOdds34) or "12"
    slowBlockLateOdds1 = get_capsule_value(slowBlockLateOdds1) or "12"
    slowBlockLateOdds2 = get_capsule_value(slowBlockLateOdds2) or "12"
    slowBlockLateOdds34 = get_capsule_value(slowBlockLateOdds34) or "12"

    # Hidden Block Card: DX
    hiddenBlockCardEarlyOdds1 = get_capsule_value(hiddenBlockCardEarlyOdds1) or "40"
    hiddenBlockCardEarlyOdds2 = get_capsule_value(hiddenBlockCardEarlyOdds2) or "40"
    hiddenBlockCardEarlyOdds34 = get_capsule_value(hiddenBlockCardEarlyOdds34) or "40"
    hiddenBlockCardMidOdds1 = get_capsule_value(hiddenBlockCardMidOdds1) or "40"
    hiddenBlockCardMidOdds2 = get_capsule_value(hiddenBlockCardMidOdds2) or "40"
    hiddenBlockCardMidOdds34 = get_capsule_value(hiddenBlockCardMidOdds34) or "40"
    hiddenBlockCardLateOdds1 = get_capsule_value(hiddenBlockCardLateOdds1) or "40"
    hiddenBlockCardLateOdds2 = get_capsule_value(hiddenBlockCardLateOdds2) or "40"
    hiddenBlockCardLateOdds34 = get_capsule_value(hiddenBlockCardLateOdds34) or "40"

    # Barter Box: DX
    barterBoxEarlyOdds1 = get_capsule_value(barterBoxEarlyOdds1) or "40"
    barterBoxEarlyOdds2 = get_capsule_value(barterBoxEarlyOdds2) or "40"
    barterBoxEarlyOdds34 = get_capsule_value(barterBoxEarlyOdds34) or "40"
    barterBoxMidOdds1 = get_capsule_value(barterBoxMidOdds1) or "40"
    barterBoxMidOdds2 = get_capsule_value(barterBoxMidOdds2) or "40"
    barterBoxMidOdds34 = get_capsule_value(barterBoxMidOdds34) or "40"
    barterBoxLateOdds1 = get_capsule_value(barterBoxLateOdds1) or "40"
    barterBoxLateOdds2 = get_capsule_value(barterBoxLateOdds2) or "40"
    barterBoxLateOdds34 = get_capsule_value(barterBoxLateOdds34) or "40"

    # Super Warp Pipe: DX
    superWarpPipeEarlyOdds1 = get_capsule_value(superWarpPipeEarlyOdds1) or "40"
    superWarpPipeEarlyOdds2 = get_capsule_value(superWarpPipeEarlyOdds2) or "40"
    superWarpPipeEarlyOdds34 = get_capsule_value(superWarpPipeEarlyOdds34) or "40"
    superWarpPipeMidOdds1 = get_capsule_value(superWarpPipeMidOdds1) or "40"
    superWarpPipeMidOdds2 = get_capsule_value(superWarpPipeMidOdds2) or "40"
    superWarpPipeMidOdds34 = get_capsule_value(superWarpPipeMidOdds34) or "40"
    superWarpPipeLateOdds1 = get_capsule_value(superWarpPipeLateOdds1) or "40"
    superWarpPipeLateOdds2 = get_capsule_value(superWarpPipeLateOdds2) or "40"
    superWarpPipeLateOdds34 = get_capsule_value(superWarpPipeLateOdds34) or "40"

    # Chance Time Charm: DX
    chanceTimeCharmEarlyOdds1 = get_capsule_value(chanceTimeCharmEarlyOdds1) or "40"
    chanceTimeCharmEarlyOdds2 = get_capsule_value(chanceTimeCharmEarlyOdds2) or "40"
    chanceTimeCharmEarlyOdds34 = get_capsule_value(chanceTimeCharmEarlyOdds34) or "40"
    chanceTimeCharmMidOdds1 = get_capsule_value(chanceTimeCharmMidOdds1) or "40"
    chanceTimeCharmMidOdds2 = get_capsule_value(chanceTimeCharmMidOdds2) or "40"
    chanceTimeCharmMidOdds34 = get_capsule_value(chanceTimeCharmMidOdds34) or "40"
    chanceTimeCharmLateOdds1 = get_capsule_value(chanceTimeCharmLateOdds1) or "40"
    chanceTimeCharmLateOdds2 = get_capsule_value(chanceTimeCharmLateOdds2) or "40"
    chanceTimeCharmLateOdds34 = get_capsule_value(chanceTimeCharmLateOdds34) or "40"

    # Wacky Watch: DX
    wackyWatchEarlyOdds1 = get_capsule_value(wackyWatchEarlyOdds1) or "100"
    wackyWatchEarlyOdds2 = get_capsule_value(wackyWatchEarlyOdds2) or "100"
    wackyWatchEarlyOdds34 = get_capsule_value(wackyWatchEarlyOdds34) or "100"
    wackyWatchMidOdds1 = get_capsule_value(wackyWatchMidOdds1) or "100"
    wackyWatchMidOdds2 = get_capsule_value(wackyWatchMidOdds2) or "100"
    wackyWatchMidOdds34 = get_capsule_value(wackyWatchMidOdds34) or "100"
    wackyWatchLateOdds1 = get_capsule_value(wackyWatchLateOdds1) or "100"
    wackyWatchLateOdds2 = get_capsule_value(wackyWatchLateOdds2) or "100"
    wackyWatchLateOdds34 = get_capsule_value(wackyWatchLateOdds34) or "100"

    earlyOdds1 = [
        miniMushroomEarlyOdds1,
        megaMushroomEarlyOdds1,
        superMiniMushroomEarlyOdds1,
        superMegaMushroomEarlyOdds1,
        miniMegaHammerEarlyOdds1,
        warpPipeEarlyOdds1,
        swapCardEarlyOdds1,
        sparkyStickerEarlyOdds1,
        gaddlightEarlyOdds1,
        chompCallEarlyOdds1,
        bowserSuitEarlyOdds1,
        crystalBallEarlyOdds1,
        magicLampEarlyOdds1,
        itemBagEarlyOdds1,
        mushroomEarlyOdds1,
        goldenMushroomEarlyOdds1,
        reverseMushroomEarlyOdds1,
        poisonMushroomEarlyOdds1,
        triplePoisonMushroomEarlyOdds1,
        celluarShopperEarlyOdds1,
        skeletonKeyEarlyOdds1,
        plunderChestEarlyOdds1,
        gaddbrushEarlyOdds1,
        warpBlockEarlyOdds1,
        flyGuyEarlyOdds1,
        plusBlockEarlyOdds1,
        minusBlockEarlyOdds1,
        speedBlockEarlyOdds1,
        slowBlockEarlyOdds1,
        bowserPhoneEarlyOdds1,
        doubleDipEarlyOdds1,
        hiddenBlockCardEarlyOdds1,
        barterBoxEarlyOdds1,
        superWarpPipeEarlyOdds1,
        chanceTimeCharmEarlyOdds1,
        wackyWatchEarlyOdds1,
    ]
    
    earlyOdds2 = [
        miniMushroomEarlyOdds2,
        megaMushroomEarlyOdds2,
        superMiniMushroomEarlyOdds2,
        superMegaMushroomEarlyOdds2,
        miniMegaHammerEarlyOdds2,
        warpPipeEarlyOdds2,
        swapCardEarlyOdds2,
        sparkyStickerEarlyOdds2,
        gaddlightEarlyOdds2,
        chompCallEarlyOdds2,
        bowserSuitEarlyOdds2,
        crystalBallEarlyOdds2,
        magicLampEarlyOdds2,
        itemBagEarlyOdds2,
        mushroomEarlyOdds2,
        goldenMushroomEarlyOdds2,
        reverseMushroomEarlyOdds2,
        poisonMushroomEarlyOdds2,
        triplePoisonMushroomEarlyOdds2,
        celluarShopperEarlyOdds2,
        skeletonKeyEarlyOdds2,
        plunderChestEarlyOdds2,
        gaddbrushEarlyOdds2,
        warpBlockEarlyOdds2,
        flyGuyEarlyOdds2,
        plusBlockEarlyOdds2,
        minusBlockEarlyOdds2,
        speedBlockEarlyOdds2,
        slowBlockEarlyOdds2,
        bowserPhoneEarlyOdds2,
        doubleDipEarlyOdds2,
        hiddenBlockCardEarlyOdds2,
        barterBoxEarlyOdds2,
        superWarpPipeEarlyOdds2,
        chanceTimeCharmEarlyOdds2,
        wackyWatchEarlyOdds2,
    ]

    earlyOdds34 = [
        miniMushroomEarlyOdds34,
        megaMushroomEarlyOdds34,
        superMiniMushroomEarlyOdds34,
        superMegaMushroomEarlyOdds34,
        miniMegaHammerEarlyOdds34,
        warpPipeEarlyOdds34,
        swapCardEarlyOdds34,
        sparkyStickerEarlyOdds34,
        gaddlightEarlyOdds34,
        chompCallEarlyOdds34,
        bowserSuitEarlyOdds34,
        crystalBallEarlyOdds34,
        magicLampEarlyOdds34,
        itemBagEarlyOdds34,
        mushroomEarlyOdds34,
        goldenMushroomEarlyOdds34,
        reverseMushroomEarlyOdds34,
        poisonMushroomEarlyOdds34,
        triplePoisonMushroomEarlyOdds34,
        celluarShopperEarlyOdds34,
        skeletonKeyEarlyOdds34,
        plunderChestEarlyOdds34,
        gaddbrushEarlyOdds34,
        warpBlockEarlyOdds34,
        flyGuyEarlyOdds34,
        plusBlockEarlyOdds34,
        minusBlockEarlyOdds34,
        speedBlockEarlyOdds34,
        slowBlockEarlyOdds34,
        bowserPhoneEarlyOdds34,
        doubleDipEarlyOdds34,
        hiddenBlockCardEarlyOdds34,
        barterBoxEarlyOdds34,
        superWarpPipeEarlyOdds34,
        chanceTimeCharmEarlyOdds34,
        wackyWatchEarlyOdds34,
    ]
    
    midOdds1 = [
        miniMushroomMidOdds1,
        megaMushroomMidOdds1,
        superMiniMushroomMidOdds1,
        superMegaMushroomMidOdds1,
        miniMegaHammerMidOdds1,
        warpPipeMidOdds1,
        swapCardMidOdds1,
        sparkyStickerMidOdds1,
        gaddlightMidOdds1,
        chompCallMidOdds1,
        bowserSuitMidOdds1,
        crystalBallMidOdds1,
        magicLampMidOdds1,
        itemBagMidOdds1,
        mushroomMidOdds1,
        goldenMushroomMidOdds1,
        reverseMushroomMidOdds1,
        poisonMushroomMidOdds1,
        triplePoisonMushroomMidOdds1,
        celluarShopperMidOdds1,
        skeletonKeyMidOdds1,
        plunderChestMidOdds1,
        gaddbrushMidOdds1,
        warpBlockMidOdds1,
        flyGuyMidOdds1,
        plusBlockMidOdds1,
        minusBlockMidOdds1,
        speedBlockMidOdds1,
        slowBlockMidOdds1,
        bowserPhoneMidOdds1,
        doubleDipMidOdds1,
        hiddenBlockCardMidOdds1,
        barterBoxMidOdds1,
        superWarpPipeMidOdds1,
        chanceTimeCharmMidOdds1,
        wackyWatchMidOdds1,
    ]

    midOdds2 = [
        miniMushroomMidOdds2,
        megaMushroomMidOdds2,
        superMiniMushroomMidOdds2,
        superMegaMushroomMidOdds2,
        miniMegaHammerMidOdds2,
        warpPipeMidOdds2,
        swapCardMidOdds2,
        sparkyStickerMidOdds2,
        gaddlightMidOdds2,
        chompCallMidOdds2,
        bowserSuitMidOdds2,
        crystalBallMidOdds2,
        magicLampMidOdds2,
        itemBagMidOdds2,
        mushroomMidOdds2,
        goldenMushroomMidOdds2,
        reverseMushroomMidOdds2,
        poisonMushroomMidOdds2,
        triplePoisonMushroomMidOdds2,
        celluarShopperMidOdds2,
        skeletonKeyMidOdds2,
        plunderChestMidOdds2,
        gaddbrushMidOdds2,
        warpBlockMidOdds2,
        flyGuyMidOdds2,
        plusBlockMidOdds2,
        minusBlockMidOdds2,
        speedBlockMidOdds2,
        slowBlockMidOdds2,
        bowserPhoneMidOdds2,
        doubleDipMidOdds2,
        hiddenBlockCardMidOdds2,
        barterBoxMidOdds2,
        superWarpPipeMidOdds2,
        chanceTimeCharmMidOdds2,
        wackyWatchMidOdds2,
    ]

    midOdds34 = [
        miniMushroomMidOdds34,
        megaMushroomMidOdds34,
        superMiniMushroomMidOdds34,
        superMegaMushroomMidOdds34,
        miniMegaHammerMidOdds34,
        warpPipeMidOdds34,
        swapCardMidOdds34,
        sparkyStickerMidOdds34,
        gaddlightMidOdds34,
        chompCallMidOdds34,
        bowserSuitMidOdds34,
        crystalBallMidOdds34,
        magicLampMidOdds34,
        itemBagMidOdds34,
        mushroomMidOdds34,
        goldenMushroomMidOdds34,
        reverseMushroomMidOdds34,
        poisonMushroomMidOdds34,
        triplePoisonMushroomMidOdds34,
        celluarShopperMidOdds34,
        skeletonKeyMidOdds34,
        plunderChestMidOdds34,
        gaddbrushMidOdds34,
        warpBlockMidOdds34,
        flyGuyMidOdds34,
        plusBlockMidOdds34,
        minusBlockMidOdds34,
        speedBlockMidOdds34,
        slowBlockMidOdds34,
        bowserPhoneMidOdds34,
        doubleDipMidOdds34,
        hiddenBlockCardMidOdds34,
        barterBoxMidOdds34,
        superWarpPipeMidOdds34,
        chanceTimeCharmMidOdds34,
        wackyWatchMidOdds34,
    ]

    lateOdds1 = [
        miniMushroomLateOdds1,
        megaMushroomLateOdds1,
        superMiniMushroomLateOdds1,
        superMegaMushroomLateOdds1,
        miniMegaHammerLateOdds1,
        warpPipeLateOdds1,
        swapCardLateOdds1,
        sparkyStickerLateOdds1,
        gaddlightLateOdds1,
        chompCallLateOdds1,
        bowserSuitLateOdds1,
        crystalBallLateOdds1,
        magicLampLateOdds1,
        itemBagLateOdds1,
        mushroomLateOdds1,
        goldenMushroomLateOdds1,
        reverseMushroomLateOdds1,
        poisonMushroomLateOdds1,
        triplePoisonMushroomLateOdds1,
        celluarShopperLateOdds1,
        skeletonKeyLateOdds1,
        plunderChestLateOdds1,
        gaddbrushLateOdds1,
        warpBlockLateOdds1,
        flyGuyLateOdds1,
        plusBlockLateOdds1,
        minusBlockLateOdds1,
        speedBlockLateOdds1,
        slowBlockLateOdds1,
        bowserPhoneLateOdds1,
        doubleDipLateOdds1,
        hiddenBlockCardLateOdds1,
        barterBoxLateOdds1,
        superWarpPipeLateOdds1,
        chanceTimeCharmLateOdds1,
        wackyWatchLateOdds1,
    ]

    lateOdds2 = [
        miniMushroomLateOdds2,
        megaMushroomLateOdds2,
        superMiniMushroomLateOdds2,
        superMegaMushroomLateOdds2,
        miniMegaHammerLateOdds2,
        warpPipeLateOdds2,
        swapCardLateOdds2,
        sparkyStickerLateOdds2,
        gaddlightLateOdds2,
        chompCallLateOdds2,
        bowserSuitLateOdds2,
        crystalBallLateOdds2,
        magicLampLateOdds2,
        itemBagLateOdds2,
        mushroomLateOdds2,
        goldenMushroomLateOdds2,
        reverseMushroomLateOdds2,
        poisonMushroomLateOdds2,
        triplePoisonMushroomLateOdds2,
        celluarShopperLateOdds2,
        skeletonKeyLateOdds2,
        plunderChestLateOdds2,
        gaddbrushLateOdds2,
        warpBlockLateOdds2,
        flyGuyLateOdds2,
        plusBlockLateOdds2,
        minusBlockLateOdds2,
        speedBlockLateOdds2,
        slowBlockLateOdds2,
        bowserPhoneLateOdds2,
        doubleDipLateOdds2,
        hiddenBlockCardLateOdds2,
        barterBoxLateOdds2,
        superWarpPipeLateOdds2,
        chanceTimeCharmLateOdds2,
        wackyWatchLateOdds2,
    ]

    lateOdds34 = [
        miniMushroomLateOdds34,
        megaMushroomLateOdds34,
        superMiniMushroomLateOdds34,
        superMegaMushroomLateOdds34,
        miniMegaHammerLateOdds34,
        warpPipeLateOdds34,
        swapCardLateOdds34,
        sparkyStickerLateOdds34,
        gaddlightLateOdds34,
        chompCallLateOdds34,
        bowserSuitLateOdds34,
        crystalBallLateOdds34,
        magicLampLateOdds34,
        itemBagLateOdds34,
        mushroomLateOdds34,
        goldenMushroomLateOdds34,
        reverseMushroomLateOdds34,
        poisonMushroomLateOdds34,
        triplePoisonMushroomLateOdds34,
        celluarShopperLateOdds34,
        skeletonKeyLateOdds34,
        plunderChestLateOdds34,
        gaddbrushLateOdds34,
        warpBlockLateOdds34,
        flyGuyLateOdds34,
        plusBlockLateOdds34,
        minusBlockLateOdds34,
        speedBlockLateOdds34,
        slowBlockLateOdds34,
        bowserPhoneLateOdds34,
        doubleDipLateOdds34,
        hiddenBlockCardLateOdds34,
        barterBoxLateOdds34,
        superWarpPipeLateOdds34,
        chanceTimeCharmLateOdds34,
        wackyWatchLateOdds34,
    ]

    earlyOdds1Weights = sum(int(weight) if weight else 0 for weight in earlyOdds1)
    earlyOdds2Weights = sum(int(weight) if weight else 0 for weight in earlyOdds2)
    earlyOdds34Weights = sum(int(weight) if weight else 0 for weight in earlyOdds34)
    midOdds1Weights = sum(int(weight) if weight else 0 for weight in midOdds1)
    midOdds2Weights = sum(int(weight) if weight else 0 for weight in midOdds2)
    midOdds34Weights = sum(int(weight) if weight else 0 for weight in midOdds34)
    lateOdds1Weights = sum(int(weight) if weight else 0 for weight in lateOdds1)
    lateOdds2Weights = sum(int(weight) if weight else 0 for weight in lateOdds2)
    lateOdds34Weights = sum(int(weight) if weight else 0 for weight in lateOdds34)

    def calculateWeight(weight, total):
        # Convert weight to int, default to 0 if empty or None
        weight = int(weight) if weight else 0
        # Check for total being zero to avoid division by zero
        if total <= 0:
            return 0  # Return 0 if total is zero or negative
        if total < 100:
            return weight  # Return the weight directly if total is less than 100
        else:
            percentage = (weight / total) * 100
            if 0 < percentage < 1:
                return math.ceil(percentage)
            return round(percentage)

    # Mini Mushroom
    miniMushroomEarlyOdds1 = calculateWeight(miniMushroomEarlyOdds1, earlyOdds1Weights)
    miniMushroomEarlyOdds2 = calculateWeight(miniMushroomEarlyOdds2, earlyOdds2Weights)
    miniMushroomEarlyOdds34 = calculateWeight(miniMushroomEarlyOdds34, earlyOdds34Weights)
    miniMushroomMidOdds1 = calculateWeight(miniMushroomMidOdds1, midOdds1Weights)
    miniMushroomMidOdds2 = calculateWeight(miniMushroomMidOdds2, midOdds2Weights)
    miniMushroomMidOdds34 = calculateWeight(miniMushroomMidOdds34, midOdds34Weights)
    miniMushroomLateOdds1 = calculateWeight(miniMushroomLateOdds1, lateOdds1Weights)
    miniMushroomLateOdds2 = calculateWeight(miniMushroomLateOdds2, lateOdds2Weights)
    miniMushroomLateOdds34 = calculateWeight(miniMushroomLateOdds34, lateOdds34Weights)

    # Mega Mushroom
    megaMushroomEarlyOdds1 = calculateWeight(megaMushroomEarlyOdds1, earlyOdds1Weights)
    megaMushroomEarlyOdds2 = calculateWeight(megaMushroomEarlyOdds2, earlyOdds2Weights)
    megaMushroomEarlyOdds34 = calculateWeight(megaMushroomEarlyOdds34, earlyOdds34Weights)
    megaMushroomMidOdds1 = calculateWeight(megaMushroomMidOdds1, midOdds1Weights)
    megaMushroomMidOdds2 = calculateWeight(megaMushroomMidOdds2, midOdds2Weights)
    megaMushroomMidOdds34 = calculateWeight(megaMushroomMidOdds34, midOdds34Weights)
    megaMushroomLateOdds1 = calculateWeight(megaMushroomLateOdds1, lateOdds1Weights)
    megaMushroomLateOdds2 = calculateWeight(megaMushroomLateOdds2, lateOdds2Weights)
    megaMushroomLateOdds34 = calculateWeight(megaMushroomLateOdds34, lateOdds34Weights)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = calculateWeight(superMiniMushroomEarlyOdds1, earlyOdds1Weights)
    superMiniMushroomEarlyOdds2 = calculateWeight(superMiniMushroomEarlyOdds2, earlyOdds2Weights)
    superMiniMushroomEarlyOdds34 = calculateWeight(superMiniMushroomEarlyOdds34, earlyOdds34Weights)
    superMiniMushroomMidOdds1 = calculateWeight(superMiniMushroomMidOdds1, midOdds1Weights)
    superMiniMushroomMidOdds2 = calculateWeight(superMiniMushroomMidOdds2, midOdds2Weights)
    superMiniMushroomMidOdds34 = calculateWeight(superMiniMushroomMidOdds34, midOdds34Weights)
    superMiniMushroomLateOdds1 = calculateWeight(superMiniMushroomLateOdds1, lateOdds1Weights)
    superMiniMushroomLateOdds2 = calculateWeight(superMiniMushroomLateOdds2, lateOdds2Weights)
    superMiniMushroomLateOdds34 = calculateWeight(superMiniMushroomLateOdds34, lateOdds34Weights)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = calculateWeight(superMegaMushroomEarlyOdds1, earlyOdds1Weights)
    superMegaMushroomEarlyOdds2 = calculateWeight(superMegaMushroomEarlyOdds2, earlyOdds2Weights)
    superMegaMushroomEarlyOdds34 = calculateWeight(superMegaMushroomEarlyOdds34, earlyOdds34Weights)
    superMegaMushroomMidOdds1 = calculateWeight(superMegaMushroomMidOdds1, midOdds1Weights)
    superMegaMushroomMidOdds2 = calculateWeight(superMegaMushroomMidOdds2, midOdds2Weights)
    superMegaMushroomMidOdds34 = calculateWeight(superMegaMushroomMidOdds34, midOdds34Weights)
    superMegaMushroomLateOdds1 = calculateWeight(superMegaMushroomLateOdds1, lateOdds1Weights)
    superMegaMushroomLateOdds2 = calculateWeight(superMegaMushroomLateOdds2, lateOdds2Weights)
    superMegaMushroomLateOdds34 = calculateWeight(superMegaMushroomLateOdds34, lateOdds34Weights)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = calculateWeight(miniMegaHammerEarlyOdds1, earlyOdds1Weights)
    miniMegaHammerEarlyOdds2 = calculateWeight(miniMegaHammerEarlyOdds2, earlyOdds2Weights)
    miniMegaHammerEarlyOdds34 = calculateWeight(miniMegaHammerEarlyOdds34, earlyOdds34Weights)
    miniMegaHammerMidOdds1 = calculateWeight(miniMegaHammerMidOdds1, midOdds1Weights)
    miniMegaHammerMidOdds2 = calculateWeight(miniMegaHammerMidOdds2, midOdds2Weights)
    miniMegaHammerMidOdds34 = calculateWeight(miniMegaHammerMidOdds34, midOdds34Weights)
    miniMegaHammerLateOdds1 = calculateWeight(miniMegaHammerLateOdds1, lateOdds1Weights)
    miniMegaHammerLateOdds2 = calculateWeight(miniMegaHammerLateOdds2, lateOdds2Weights)
    miniMegaHammerLateOdds34 = calculateWeight(miniMegaHammerLateOdds34, lateOdds34Weights)

    # Warp Pipe
    warpPipeEarlyOdds1 = calculateWeight(warpPipeEarlyOdds1, earlyOdds1Weights)
    warpPipeEarlyOdds2 = calculateWeight(warpPipeEarlyOdds2, earlyOdds2Weights)
    warpPipeEarlyOdds34 = calculateWeight(warpPipeEarlyOdds34, earlyOdds34Weights)
    warpPipeMidOdds1 = calculateWeight(warpPipeMidOdds1, midOdds1Weights)
    warpPipeMidOdds2 = calculateWeight(warpPipeMidOdds2, midOdds2Weights)
    warpPipeMidOdds34 = calculateWeight(warpPipeMidOdds34, midOdds34Weights)
    warpPipeLateOdds1 = calculateWeight(warpPipeLateOdds1, lateOdds1Weights)
    warpPipeLateOdds2 = calculateWeight(warpPipeLateOdds2, lateOdds2Weights)
    warpPipeLateOdds34 = calculateWeight(warpPipeLateOdds34, lateOdds34Weights)

    # Swap Card
    swapCardEarlyOdds1 = calculateWeight(swapCardEarlyOdds1, earlyOdds1Weights)
    swapCardEarlyOdds2 = calculateWeight(swapCardEarlyOdds2, earlyOdds2Weights)
    swapCardEarlyOdds34 = calculateWeight(swapCardEarlyOdds34, earlyOdds34Weights)
    swapCardMidOdds1 = calculateWeight(swapCardMidOdds1, midOdds1Weights)
    swapCardMidOdds2 = calculateWeight(swapCardMidOdds2, midOdds2Weights)
    swapCardMidOdds34 = calculateWeight(swapCardMidOdds34, midOdds34Weights)
    swapCardLateOdds1 = calculateWeight(swapCardLateOdds1, lateOdds1Weights)
    swapCardLateOdds2 = calculateWeight(swapCardLateOdds2, lateOdds2Weights)
    swapCardLateOdds34 = calculateWeight(swapCardLateOdds34, lateOdds34Weights)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = calculateWeight(sparkyStickerEarlyOdds1, earlyOdds1Weights)
    sparkyStickerEarlyOdds2 = calculateWeight(sparkyStickerEarlyOdds2, earlyOdds2Weights)
    sparkyStickerEarlyOdds34 = calculateWeight(sparkyStickerEarlyOdds34, earlyOdds34Weights)
    sparkyStickerMidOdds1 = calculateWeight(sparkyStickerMidOdds1, midOdds1Weights)
    sparkyStickerMidOdds2 = calculateWeight(sparkyStickerMidOdds2, midOdds2Weights)
    sparkyStickerMidOdds34 = calculateWeight(sparkyStickerMidOdds34, midOdds34Weights)
    sparkyStickerLateOdds1 = calculateWeight(sparkyStickerLateOdds1, lateOdds1Weights)
    sparkyStickerLateOdds2 = calculateWeight(sparkyStickerLateOdds2, lateOdds2Weights)
    sparkyStickerLateOdds34 = calculateWeight(sparkyStickerLateOdds34, lateOdds34Weights)

    # Gaddlight
    gaddlightEarlyOdds1 = calculateWeight(gaddlightEarlyOdds1, earlyOdds1Weights)
    gaddlightEarlyOdds2 = calculateWeight(gaddlightEarlyOdds2, earlyOdds2Weights)
    gaddlightEarlyOdds34 = calculateWeight(gaddlightEarlyOdds34, earlyOdds34Weights)
    gaddlightMidOdds1 = calculateWeight(gaddlightMidOdds1, midOdds1Weights)
    gaddlightMidOdds2 = calculateWeight(gaddlightMidOdds2, midOdds2Weights)
    gaddlightMidOdds34 = calculateWeight(gaddlightMidOdds34, midOdds34Weights)
    gaddlightLateOdds1 = calculateWeight(gaddlightLateOdds1, lateOdds1Weights)
    gaddlightLateOdds2 = calculateWeight(gaddlightLateOdds2, lateOdds2Weights)
    gaddlightLateOdds34 = calculateWeight(gaddlightLateOdds34, lateOdds34Weights)

    # Chomp Call
    chompCallEarlyOdds1 = calculateWeight(chompCallEarlyOdds1, earlyOdds1Weights)
    chompCallEarlyOdds2 = calculateWeight(chompCallEarlyOdds2, earlyOdds2Weights)
    chompCallEarlyOdds34 = calculateWeight(chompCallEarlyOdds34, earlyOdds34Weights)
    chompCallMidOdds1 = calculateWeight(chompCallMidOdds1, midOdds1Weights)
    chompCallMidOdds2 = calculateWeight(chompCallMidOdds2, midOdds2Weights)
    chompCallMidOdds34 = calculateWeight(chompCallMidOdds34, midOdds34Weights)
    chompCallLateOdds1 = calculateWeight(chompCallLateOdds1, lateOdds1Weights)
    chompCallLateOdds2 = calculateWeight(chompCallLateOdds2, lateOdds2Weights)
    chompCallLateOdds34 = calculateWeight(chompCallLateOdds34, lateOdds34Weights)

    # Bowser Suit
    bowserSuitEarlyOdds1 = calculateWeight(bowserSuitEarlyOdds1, earlyOdds1Weights)
    bowserSuitEarlyOdds2 = calculateWeight(bowserSuitEarlyOdds2, earlyOdds2Weights)
    bowserSuitEarlyOdds34 = calculateWeight(bowserSuitEarlyOdds34, earlyOdds34Weights)
    bowserSuitMidOdds1 = calculateWeight(bowserSuitMidOdds1, midOdds1Weights)
    bowserSuitMidOdds2 = calculateWeight(bowserSuitMidOdds2, midOdds2Weights)
    bowserSuitMidOdds34 = calculateWeight(bowserSuitMidOdds34, midOdds34Weights)
    bowserSuitLateOdds1 = calculateWeight(bowserSuitLateOdds1, lateOdds1Weights)
    bowserSuitLateOdds2 = calculateWeight(bowserSuitLateOdds2, lateOdds2Weights)
    bowserSuitLateOdds34 = calculateWeight(bowserSuitLateOdds34, lateOdds34Weights)

    # Crystal Ball
    crystalBallEarlyOdds1 = calculateWeight(crystalBallEarlyOdds1, earlyOdds1Weights)
    crystalBallEarlyOdds2 = calculateWeight(crystalBallEarlyOdds2, earlyOdds2Weights)
    crystalBallEarlyOdds34 = calculateWeight(crystalBallEarlyOdds34, earlyOdds34Weights)
    crystalBallMidOdds1 = calculateWeight(crystalBallMidOdds1, midOdds1Weights)
    crystalBallMidOdds2 = calculateWeight(crystalBallMidOdds2, midOdds2Weights)
    crystalBallMidOdds34 = calculateWeight(crystalBallMidOdds34, midOdds34Weights)
    crystalBallLateOdds1 = calculateWeight(crystalBallLateOdds1, lateOdds1Weights)
    crystalBallLateOdds2 = calculateWeight(crystalBallLateOdds2, lateOdds2Weights)
    crystalBallLateOdds34 = calculateWeight(crystalBallLateOdds34, lateOdds34Weights)

    # Magic Lamp
    magicLampEarlyOdds1 = calculateWeight(magicLampEarlyOdds1, earlyOdds1Weights)
    magicLampEarlyOdds2 = calculateWeight(magicLampEarlyOdds2, earlyOdds2Weights)
    magicLampEarlyOdds34 = calculateWeight(magicLampEarlyOdds34, earlyOdds34Weights)
    magicLampMidOdds1 = calculateWeight(magicLampMidOdds1, midOdds1Weights)
    magicLampMidOdds2 = calculateWeight(magicLampMidOdds2, midOdds2Weights)
    magicLampMidOdds34 = calculateWeight(magicLampMidOdds34, midOdds34Weights)
    magicLampLateOdds1 = calculateWeight(magicLampLateOdds1, lateOdds1Weights)
    magicLampLateOdds2 = calculateWeight(magicLampLateOdds2, lateOdds2Weights)
    magicLampLateOdds34 = calculateWeight(magicLampLateOdds34, lateOdds34Weights)

    # Item Bag
    itemBagEarlyOdds1 = calculateWeight(itemBagEarlyOdds1, earlyOdds1Weights)
    itemBagEarlyOdds2 = calculateWeight(itemBagEarlyOdds2, earlyOdds2Weights)
    itemBagEarlyOdds34 = calculateWeight(itemBagEarlyOdds34, earlyOdds34Weights)
    itemBagMidOdds1 = calculateWeight(itemBagMidOdds1, midOdds1Weights)
    itemBagMidOdds2 = calculateWeight(itemBagMidOdds2, midOdds2Weights)
    itemBagMidOdds34 = calculateWeight(itemBagMidOdds34, midOdds34Weights)
    itemBagLateOdds1 = calculateWeight(itemBagLateOdds1, lateOdds1Weights)
    itemBagLateOdds2 = calculateWeight(itemBagLateOdds2, lateOdds2Weights)
    itemBagLateOdds34 = calculateWeight(itemBagLateOdds34, lateOdds34Weights)

    # Mushroom: DX
    mushroomEarlyOdds1 = calculateWeight(mushroomEarlyOdds1, earlyOdds1Weights)
    mushroomEarlyOdds2 = calculateWeight(mushroomEarlyOdds2, earlyOdds2Weights)
    mushroomEarlyOdds34 = calculateWeight(mushroomEarlyOdds34, earlyOdds34Weights)
    mushroomMidOdds1 = calculateWeight(mushroomMidOdds1, midOdds1Weights)
    mushroomMidOdds2 = calculateWeight(mushroomMidOdds2, midOdds2Weights)
    mushroomMidOdds34 = calculateWeight(mushroomMidOdds34, midOdds34Weights)
    mushroomLateOdds1 = calculateWeight(mushroomLateOdds1, lateOdds1Weights)
    mushroomLateOdds2 = calculateWeight(mushroomLateOdds2, lateOdds2Weights)
    mushroomLateOdds34 = calculateWeight(mushroomLateOdds34, lateOdds34Weights)

    # Golden Mushroom: DX
    goldenMushroomEarlyOdds1 = calculateWeight(goldenMushroomEarlyOdds1, earlyOdds1Weights)
    goldenMushroomEarlyOdds2 = calculateWeight(goldenMushroomEarlyOdds2, earlyOdds2Weights)
    goldenMushroomEarlyOdds34 = calculateWeight(goldenMushroomEarlyOdds34, earlyOdds34Weights)
    goldenMushroomMidOdds1 = calculateWeight(goldenMushroomMidOdds1, midOdds1Weights)
    goldenMushroomMidOdds2 = calculateWeight(goldenMushroomMidOdds2, midOdds2Weights)
    goldenMushroomMidOdds34 = calculateWeight(goldenMushroomMidOdds34, midOdds34Weights)
    goldenMushroomLateOdds1 = calculateWeight(goldenMushroomLateOdds1, lateOdds1Weights)
    goldenMushroomLateOdds2 = calculateWeight(goldenMushroomLateOdds2, lateOdds2Weights)
    goldenMushroomLateOdds34 = calculateWeight(goldenMushroomLateOdds34, lateOdds34Weights)

    # Reverse Mushroom: DX
    reverseMushroomEarlyOdds1 = calculateWeight(reverseMushroomEarlyOdds1, earlyOdds1Weights)
    reverseMushroomEarlyOdds2 = calculateWeight(reverseMushroomEarlyOdds2, earlyOdds2Weights)
    reverseMushroomEarlyOdds34 = calculateWeight(reverseMushroomEarlyOdds34, earlyOdds34Weights)
    reverseMushroomMidOdds1 = calculateWeight(reverseMushroomMidOdds1, midOdds1Weights)
    reverseMushroomMidOdds2 = calculateWeight(reverseMushroomMidOdds2, midOdds2Weights)
    reverseMushroomMidOdds34 = calculateWeight(reverseMushroomMidOdds34, midOdds34Weights)
    reverseMushroomLateOdds1 = calculateWeight(reverseMushroomLateOdds1, lateOdds1Weights)
    reverseMushroomLateOdds2 = calculateWeight(reverseMushroomLateOdds2, lateOdds2Weights)
    reverseMushroomLateOdds34 = calculateWeight(reverseMushroomLateOdds34, lateOdds34Weights)

    # Poison Mushroom: DX
    poisonMushroomEarlyOdds1 = calculateWeight(poisonMushroomEarlyOdds1, earlyOdds1Weights)
    poisonMushroomEarlyOdds2 = calculateWeight(poisonMushroomEarlyOdds2, earlyOdds2Weights)
    poisonMushroomEarlyOdds34 = calculateWeight(poisonMushroomEarlyOdds34, earlyOdds34Weights)
    poisonMushroomMidOdds1 = calculateWeight(poisonMushroomMidOdds1, midOdds1Weights)
    poisonMushroomMidOdds2 = calculateWeight(poisonMushroomMidOdds2, midOdds2Weights)
    poisonMushroomMidOdds34 = calculateWeight(poisonMushroomMidOdds34, midOdds34Weights)
    poisonMushroomLateOdds1 = calculateWeight(poisonMushroomLateOdds1, lateOdds1Weights)
    poisonMushroomLateOdds2 = calculateWeight(poisonMushroomLateOdds2, lateOdds2Weights)
    poisonMushroomLateOdds34 = calculateWeight(poisonMushroomLateOdds34, lateOdds34Weights)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyOdds1 = calculateWeight(triplePoisonMushroomEarlyOdds1, earlyOdds1Weights)
    triplePoisonMushroomEarlyOdds2 = calculateWeight(triplePoisonMushroomEarlyOdds2, earlyOdds2Weights)
    triplePoisonMushroomEarlyOdds34 = calculateWeight(triplePoisonMushroomEarlyOdds34, earlyOdds34Weights)
    triplePoisonMushroomMidOdds1 = calculateWeight(triplePoisonMushroomMidOdds1, midOdds1Weights)
    triplePoisonMushroomMidOdds2 = calculateWeight(triplePoisonMushroomMidOdds2, midOdds2Weights)
    triplePoisonMushroomMidOdds34 = calculateWeight(triplePoisonMushroomMidOdds34, midOdds34Weights)
    triplePoisonMushroomLateOdds1 = calculateWeight(triplePoisonMushroomLateOdds1, lateOdds1Weights)
    triplePoisonMushroomLateOdds2 = calculateWeight(triplePoisonMushroomLateOdds2, lateOdds2Weights)
    triplePoisonMushroomLateOdds34 = calculateWeight(triplePoisonMushroomLateOdds34, lateOdds34Weights)

    # Celluar Shopper: DX
    celluarShopperEarlyOdds1 = calculateWeight(celluarShopperEarlyOdds1, earlyOdds1Weights)
    celluarShopperEarlyOdds2 = calculateWeight(celluarShopperEarlyOdds2, earlyOdds2Weights)
    celluarShopperEarlyOdds34 = calculateWeight(celluarShopperEarlyOdds34, earlyOdds34Weights)
    celluarShopperMidOdds1 = calculateWeight(celluarShopperMidOdds1, midOdds1Weights)
    celluarShopperMidOdds2 = calculateWeight(celluarShopperMidOdds2, midOdds2Weights)
    celluarShopperMidOdds34 = calculateWeight(celluarShopperMidOdds34, midOdds34Weights)
    celluarShopperLateOdds1 = calculateWeight(celluarShopperLateOdds1, lateOdds1Weights)
    celluarShopperLateOdds2 = calculateWeight(celluarShopperLateOdds2, lateOdds2Weights)
    celluarShopperLateOdds34 = calculateWeight(celluarShopperLateOdds34, lateOdds34Weights)

    # Skeleton Key: DX
    skeletonKeyEarlyOdds1 = calculateWeight(skeletonKeyEarlyOdds1, earlyOdds1Weights)
    skeletonKeyEarlyOdds2 = calculateWeight(skeletonKeyEarlyOdds2, earlyOdds2Weights)
    skeletonKeyEarlyOdds34 = calculateWeight(skeletonKeyEarlyOdds34, earlyOdds34Weights)
    skeletonKeyMidOdds1 = calculateWeight(skeletonKeyMidOdds1, midOdds1Weights)
    skeletonKeyMidOdds2 = calculateWeight(skeletonKeyMidOdds2, midOdds2Weights)
    skeletonKeyMidOdds34 = calculateWeight(skeletonKeyMidOdds34, midOdds34Weights)
    skeletonKeyLateOdds1 = calculateWeight(skeletonKeyLateOdds1, lateOdds1Weights)
    skeletonKeyLateOdds2 = calculateWeight(skeletonKeyLateOdds2, lateOdds2Weights)
    skeletonKeyLateOdds34 = calculateWeight(skeletonKeyLateOdds34, lateOdds34Weights)

    # Plunder Chest: DX
    plunderChestEarlyOdds1 = calculateWeight(plunderChestEarlyOdds1, earlyOdds1Weights)
    plunderChestEarlyOdds2 = calculateWeight(plunderChestEarlyOdds2, earlyOdds2Weights)
    plunderChestEarlyOdds34 = calculateWeight(plunderChestEarlyOdds34, earlyOdds34Weights)
    plunderChestMidOdds1 = calculateWeight(plunderChestMidOdds1, midOdds1Weights)
    plunderChestMidOdds2 = calculateWeight(plunderChestMidOdds2, midOdds2Weights)
    plunderChestMidOdds34 = calculateWeight(plunderChestMidOdds34, midOdds34Weights)
    plunderChestLateOdds1 = calculateWeight(plunderChestLateOdds1, lateOdds1Weights)
    plunderChestLateOdds2 = calculateWeight(plunderChestLateOdds2, lateOdds2Weights)
    plunderChestLateOdds34 = calculateWeight(plunderChestLateOdds34, lateOdds34Weights)

    # Gaddbrush: DX
    gaddbrushEarlyOdds1 = calculateWeight(gaddbrushEarlyOdds1, earlyOdds1Weights)
    gaddbrushEarlyOdds2 = calculateWeight(gaddbrushEarlyOdds2, earlyOdds2Weights)
    gaddbrushEarlyOdds34 = calculateWeight(gaddbrushEarlyOdds34, earlyOdds34Weights)
    gaddbrushMidOdds1 = calculateWeight(gaddbrushMidOdds1, midOdds1Weights)
    gaddbrushMidOdds2 = calculateWeight(gaddbrushMidOdds2, midOdds2Weights)
    gaddbrushMidOdds34 = calculateWeight(gaddbrushMidOdds34, midOdds34Weights)
    gaddbrushLateOdds1 = calculateWeight(gaddbrushLateOdds1, lateOdds1Weights)
    gaddbrushLateOdds2 = calculateWeight(gaddbrushLateOdds2, lateOdds2Weights)
    gaddbrushLateOdds34 = calculateWeight(gaddbrushLateOdds34, lateOdds34Weights)

    earlyOdds1 = [
        miniMushroomEarlyOdds1,
        megaMushroomEarlyOdds1,
        superMiniMushroomEarlyOdds1,
        superMegaMushroomEarlyOdds1,
        miniMegaHammerEarlyOdds1,
        warpPipeEarlyOdds1,
        swapCardEarlyOdds1,
        sparkyStickerEarlyOdds1,
        gaddlightEarlyOdds1,
        chompCallEarlyOdds1,
        bowserSuitEarlyOdds1,
        crystalBallEarlyOdds1,
        magicLampEarlyOdds1,
        itemBagEarlyOdds1,
        mushroomEarlyOdds1,
        goldenMushroomEarlyOdds1,
        reverseMushroomEarlyOdds1,
        poisonMushroomEarlyOdds1,
        triplePoisonMushroomEarlyOdds1,
        celluarShopperEarlyOdds1,
        skeletonKeyEarlyOdds1,
        plunderChestEarlyOdds1,
        gaddbrushEarlyOdds1,
        warpBlockEarlyOdds1,
        flyGuyEarlyOdds1,
        plusBlockEarlyOdds1,
        minusBlockEarlyOdds1,
        speedBlockEarlyOdds1,
        slowBlockEarlyOdds1,
        bowserPhoneEarlyOdds1,
        doubleDipEarlyOdds1,
        hiddenBlockCardEarlyOdds1,
        barterBoxEarlyOdds1,
        superWarpPipeEarlyOdds1,
        chanceTimeCharmEarlyOdds1,
        wackyWatchEarlyOdds1,
    ]
    
    earlyOdds2 = [
        miniMushroomEarlyOdds2,
        megaMushroomEarlyOdds2,
        superMiniMushroomEarlyOdds2,
        superMegaMushroomEarlyOdds2,
        miniMegaHammerEarlyOdds2,
        warpPipeEarlyOdds2,
        swapCardEarlyOdds2,
        sparkyStickerEarlyOdds2,
        gaddlightEarlyOdds2,
        chompCallEarlyOdds2,
        bowserSuitEarlyOdds2,
        crystalBallEarlyOdds2,
        magicLampEarlyOdds2,
        itemBagEarlyOdds2,
        mushroomEarlyOdds2,
        goldenMushroomEarlyOdds2,
        reverseMushroomEarlyOdds2,
        poisonMushroomEarlyOdds2,
        triplePoisonMushroomEarlyOdds2,
        celluarShopperEarlyOdds2,
        skeletonKeyEarlyOdds2,
        plunderChestEarlyOdds2,
        gaddbrushEarlyOdds2,
        warpBlockEarlyOdds2,
        flyGuyEarlyOdds2,
        plusBlockEarlyOdds2,
        minusBlockEarlyOdds2,
        speedBlockEarlyOdds2,
        slowBlockEarlyOdds2,
        bowserPhoneEarlyOdds2,
        doubleDipEarlyOdds2,
        hiddenBlockCardEarlyOdds2,
        barterBoxEarlyOdds2,
        superWarpPipeEarlyOdds2,
        chanceTimeCharmEarlyOdds2,
        wackyWatchEarlyOdds2,
    ]

    earlyOdds34 = [
        miniMushroomEarlyOdds34,
        megaMushroomEarlyOdds34,
        superMiniMushroomEarlyOdds34,
        superMegaMushroomEarlyOdds34,
        miniMegaHammerEarlyOdds34,
        warpPipeEarlyOdds34,
        swapCardEarlyOdds34,
        sparkyStickerEarlyOdds34,
        gaddlightEarlyOdds34,
        chompCallEarlyOdds34,
        bowserSuitEarlyOdds34,
        crystalBallEarlyOdds34,
        magicLampEarlyOdds34,
        itemBagEarlyOdds34,
        mushroomEarlyOdds34,
        goldenMushroomEarlyOdds34,
        reverseMushroomEarlyOdds34,
        poisonMushroomEarlyOdds34,
        triplePoisonMushroomEarlyOdds34,
        celluarShopperEarlyOdds34,
        skeletonKeyEarlyOdds34,
        plunderChestEarlyOdds34,
        gaddbrushEarlyOdds34,
        warpBlockEarlyOdds34,
        flyGuyEarlyOdds34,
        plusBlockEarlyOdds34,
        minusBlockEarlyOdds34,
        speedBlockEarlyOdds34,
        slowBlockEarlyOdds34,
        bowserPhoneEarlyOdds34,
        doubleDipEarlyOdds34,
        hiddenBlockCardEarlyOdds34,
        barterBoxEarlyOdds34,
        superWarpPipeEarlyOdds34,
        chanceTimeCharmEarlyOdds34,
        wackyWatchEarlyOdds34,
    ]
    
    midOdds1 = [
        miniMushroomMidOdds1,
        megaMushroomMidOdds1,
        superMiniMushroomMidOdds1,
        superMegaMushroomMidOdds1,
        miniMegaHammerMidOdds1,
        warpPipeMidOdds1,
        swapCardMidOdds1,
        sparkyStickerMidOdds1,
        gaddlightMidOdds1,
        chompCallMidOdds1,
        bowserSuitMidOdds1,
        crystalBallMidOdds1,
        magicLampMidOdds1,
        itemBagMidOdds1,
        mushroomMidOdds1,
        goldenMushroomMidOdds1,
        reverseMushroomMidOdds1,
        poisonMushroomMidOdds1,
        triplePoisonMushroomMidOdds1,
        celluarShopperMidOdds1,
        skeletonKeyMidOdds1,
        plunderChestMidOdds1,
        gaddbrushMidOdds1,
        warpBlockMidOdds1,
        flyGuyMidOdds1,
        plusBlockMidOdds1,
        minusBlockMidOdds1,
        speedBlockMidOdds1,
        slowBlockMidOdds1,
        bowserPhoneMidOdds1,
        doubleDipMidOdds1,
        hiddenBlockCardMidOdds1,
        barterBoxMidOdds1,
        superWarpPipeMidOdds1,
        chanceTimeCharmMidOdds1,
        wackyWatchMidOdds1,
    ]

    midOdds2 = [
        miniMushroomMidOdds2,
        megaMushroomMidOdds2,
        superMiniMushroomMidOdds2,
        superMegaMushroomMidOdds2,
        miniMegaHammerMidOdds2,
        warpPipeMidOdds2,
        swapCardMidOdds2,
        sparkyStickerMidOdds2,
        gaddlightMidOdds2,
        chompCallMidOdds2,
        bowserSuitMidOdds2,
        crystalBallMidOdds2,
        magicLampMidOdds2,
        itemBagMidOdds2,
        mushroomMidOdds2,
        goldenMushroomMidOdds2,
        reverseMushroomMidOdds2,
        poisonMushroomMidOdds2,
        triplePoisonMushroomMidOdds2,
        celluarShopperMidOdds2,
        skeletonKeyMidOdds2,
        plunderChestMidOdds2,
        gaddbrushMidOdds2,
        warpBlockMidOdds2,
        flyGuyMidOdds2,
        plusBlockMidOdds2,
        minusBlockMidOdds2,
        speedBlockMidOdds2,
        slowBlockMidOdds2,
        bowserPhoneMidOdds2,
        doubleDipMidOdds2,
        hiddenBlockCardMidOdds2,
        barterBoxMidOdds2,
        superWarpPipeMidOdds2,
        chanceTimeCharmMidOdds2,
        wackyWatchMidOdds2,
    ]

    midOdds34 = [
        miniMushroomMidOdds34,
        megaMushroomMidOdds34,
        superMiniMushroomMidOdds34,
        superMegaMushroomMidOdds34,
        miniMegaHammerMidOdds34,
        warpPipeMidOdds34,
        swapCardMidOdds34,
        sparkyStickerMidOdds34,
        gaddlightMidOdds34,
        chompCallMidOdds34,
        bowserSuitMidOdds34,
        crystalBallMidOdds34,
        magicLampMidOdds34,
        itemBagMidOdds34,
        mushroomMidOdds34,
        goldenMushroomMidOdds34,
        reverseMushroomMidOdds34,
        poisonMushroomMidOdds34,
        triplePoisonMushroomMidOdds34,
        celluarShopperMidOdds34,
        skeletonKeyMidOdds34,
        plunderChestMidOdds34,
        gaddbrushMidOdds34,
        warpBlockMidOdds34,
        flyGuyMidOdds34,
        plusBlockMidOdds34,
        minusBlockMidOdds34,
        speedBlockMidOdds34,
        slowBlockMidOdds34,
        bowserPhoneMidOdds34,
        doubleDipMidOdds34,
        hiddenBlockCardMidOdds34,
        barterBoxMidOdds34,
        superWarpPipeMidOdds34,
        chanceTimeCharmMidOdds34,
        wackyWatchMidOdds34,
    ]

    lateOdds1 = [
        miniMushroomLateOdds1,
        megaMushroomLateOdds1,
        superMiniMushroomLateOdds1,
        superMegaMushroomLateOdds1,
        miniMegaHammerLateOdds1,
        warpPipeLateOdds1,
        swapCardLateOdds1,
        sparkyStickerLateOdds1,
        gaddlightLateOdds1,
        chompCallLateOdds1,
        bowserSuitLateOdds1,
        crystalBallLateOdds1,
        magicLampLateOdds1,
        itemBagLateOdds1,
        mushroomLateOdds1,
        goldenMushroomLateOdds1,
        reverseMushroomLateOdds1,
        poisonMushroomLateOdds1,
        triplePoisonMushroomLateOdds1,
        celluarShopperLateOdds1,
        skeletonKeyLateOdds1,
        plunderChestLateOdds1,
        gaddbrushLateOdds1,
        warpBlockLateOdds1,
        flyGuyLateOdds1,
        plusBlockLateOdds1,
        minusBlockLateOdds1,
        speedBlockLateOdds1,
        slowBlockLateOdds1,
        bowserPhoneLateOdds1,
        doubleDipLateOdds1,
        hiddenBlockCardLateOdds1,
        barterBoxLateOdds1,
        superWarpPipeLateOdds1,
        chanceTimeCharmLateOdds1,
        wackyWatchLateOdds1,
    ]

    lateOdds2 = [
        miniMushroomLateOdds2,
        megaMushroomLateOdds2,
        superMiniMushroomLateOdds2,
        superMegaMushroomLateOdds2,
        miniMegaHammerLateOdds2,
        warpPipeLateOdds2,
        swapCardLateOdds2,
        sparkyStickerLateOdds2,
        gaddlightLateOdds2,
        chompCallLateOdds2,
        bowserSuitLateOdds2,
        crystalBallLateOdds2,
        magicLampLateOdds2,
        itemBagLateOdds2,
        mushroomLateOdds2,
        goldenMushroomLateOdds2,
        reverseMushroomLateOdds2,
        poisonMushroomLateOdds2,
        triplePoisonMushroomLateOdds2,
        celluarShopperLateOdds2,
        skeletonKeyLateOdds2,
        plunderChestLateOdds2,
        gaddbrushLateOdds2,
        warpBlockLateOdds2,
        flyGuyLateOdds2,
        plusBlockLateOdds2,
        minusBlockLateOdds2,
        speedBlockLateOdds2,
        slowBlockLateOdds2,
        bowserPhoneLateOdds2,
        doubleDipLateOdds2,
        hiddenBlockCardLateOdds2,
        barterBoxLateOdds2,
        superWarpPipeLateOdds2,
        chanceTimeCharmLateOdds2,
        wackyWatchLateOdds2,
    ]

    lateOdds34 = [
        miniMushroomLateOdds34,
        megaMushroomLateOdds34,
        superMiniMushroomLateOdds34,
        superMegaMushroomLateOdds34,
        miniMegaHammerLateOdds34,
        warpPipeLateOdds34,
        swapCardLateOdds34,
        sparkyStickerLateOdds34,
        gaddlightLateOdds34,
        chompCallLateOdds34,
        bowserSuitLateOdds34,
        crystalBallLateOdds34,
        magicLampLateOdds34,
        itemBagLateOdds34,
        mushroomLateOdds34,
        goldenMushroomLateOdds34,
        reverseMushroomLateOdds34,
        poisonMushroomLateOdds34,
        triplePoisonMushroomLateOdds34,
        celluarShopperLateOdds34,
        skeletonKeyLateOdds34,
        plunderChestLateOdds34,
        gaddbrushLateOdds34,
        warpBlockLateOdds34,
        flyGuyLateOdds34,
        plusBlockLateOdds34,
        minusBlockLateOdds34,
        speedBlockLateOdds34,
        slowBlockLateOdds34,
        bowserPhoneLateOdds34,
        doubleDipLateOdds34,
        hiddenBlockCardLateOdds34,
        barterBoxLateOdds34,
        superWarpPipeLateOdds34,
        chanceTimeCharmLateOdds34,
        wackyWatchLateOdds34,
    ]

    earlyOdds1Weights = sum(int(weight) for weight in earlyOdds1 if weight)
    earlyOdds2Weights = sum(int(weight) for weight in earlyOdds2 if weight)
    earlyOdds34Weights = sum(int(weight) for weight in earlyOdds34 if weight)
    midOdds1Weights = sum(int(weight) for weight in midOdds1 if weight)
    midOdds2Weights = sum(int(weight) for weight in midOdds2 if weight)
    midOdds34Weights = sum(int(weight) for weight in midOdds34 if weight)
    lateOdds1Weights = sum(int(weight) for weight in lateOdds1 if weight)
    lateOdds2Weights = sum(int(weight) for weight in lateOdds2 if weight)
    lateOdds34Weights = sum(int(weight) for weight in lateOdds34 if weight)

    if int(earlyOdds1Weights) < 101:
        earlyOdds1Max = max(zip(earlyOdds1, earlyOdds1), key=lambda tuple: int(tuple[1]))[0]

    if int(earlyOdds2Weights) < 101:
        earlyOdds2Max = max(zip(earlyOdds2, earlyOdds2), key=lambda tuple: int(tuple[1]))[0]

    if int(earlyOdds34Weights) < 101:
        earlyOdds34Max = max(zip(earlyOdds34, earlyOdds34), key=lambda tuple: int(tuple[1]))[0]

    if int(midOdds1Weights) < 101:
        midOdds1Max = max(zip(midOdds1, midOdds1), key=lambda tuple: int(tuple[1]))[0]

    if int(midOdds2Weights) < 101:
        midOdds2Max = max(zip(midOdds2, midOdds2), key=lambda tuple: int(tuple[1]))[0]

    if int(midOdds34Weights) < 101:
        midOdds34Max = max(zip(midOdds34, midOdds34), key=lambda tuple: int(tuple[1]))[0]

    if int(lateOdds1Weights) < 101:
        lateOdds1Max = max(zip(lateOdds1, lateOdds1), key=lambda tuple: int(tuple[1]))[0]

    if int(lateOdds2Weights) < 101:
        lateOdds2Max = max(zip(lateOdds2, lateOdds2), key=lambda tuple: int(tuple[1]))[0]

    if int(lateOdds34Weights) < 101:
        lateOdds34Max = max(zip(lateOdds34, lateOdds34), key=lambda tuple: int(tuple[1]))[0]

    # Mini Mushroom
    if earlyOdds1Max == 'miniMushroomEarlyOdds1':
        miniMushroomEarlyOdds1 += (100 - miniMushroomEarlyOdds1)
    if earlyOdds2Max == 'miniMushroomEarlyOdds2':
        miniMushroomEarlyOdds2 += (100 - miniMushroomEarlyOdds2)
    if earlyOdds34Max == 'miniMushroomEarlyOdds34':
        miniMushroomEarlyOdds34 += (100 - miniMushroomEarlyOdds34)
    if midOdds1Max == 'miniMushroomMidOdds1':
        miniMushroomMidOdds1 += (100 - miniMushroomMidOdds1)
    if midOdds2Max == 'miniMushroomMidOdds2':
        miniMushroomMidOdds2 += (100 - miniMushroomMidOdds2)
    if midOdds34Max == 'miniMushroomMidOdds34':
        miniMushroomMidOdds34 += (100 - miniMushroomMidOdds34)
    if lateOdds1Max == 'miniMushroomLateOdds1':
        miniMushroomLateOdds1 += (100 - miniMushroomLateOdds1)
    if lateOdds2Max == 'miniMushroomLateOdds2':
        miniMushroomLateOdds2 += (100 - miniMushroomLateOdds2)
    if lateOdds34Max == 'miniMushroomLateOdds34':
        miniMushroomLateOdds34 += (100 - miniMushroomLateOdds34)

    # Mega Mushroom
    if earlyOdds1Max == 'megaMushroomEarlyOdds1':
        megaMushroomEarlyOdds1 += (100 - megaMushroomEarlyOdds1)
    if earlyOdds2Max == 'megaMushroomEarlyOdds2':
        megaMushroomEarlyOdds2 += (100 - megaMushroomEarlyOdds2)
    if earlyOdds34Max == 'megaMushroomEarlyOdds34':
        megaMushroomEarlyOdds34 += (100 - megaMushroomEarlyOdds34)
    if midOdds1Max == 'megaMushroomMidOdds1':
        megaMushroomMidOdds1 += (100 - megaMushroomMidOdds1)
    if midOdds2Max == 'megaMushroomMidOdds2':
        megaMushroomMidOdds2 += (100 - megaMushroomMidOdds2)
    if midOdds34Max == 'megaMushroomMidOdds34':
        megaMushroomMidOdds34 += (100 - megaMushroomMidOdds34)
    if lateOdds1Max == 'megaMushroomLateOdds1':
        megaMushroomLateOdds1 += (100 - megaMushroomLateOdds1)
    if lateOdds2Max == 'megaMushroomLateOdds2':
        megaMushroomLateOdds2 += (100 - megaMushroomLateOdds2)
    if lateOdds34Max == 'megaMushroomLateOdds34':
        megaMushroomLateOdds34 += (100 - megaMushroomLateOdds34)

    # Super Mini Mushroom
    if earlyOdds1Max == 'superMiniMushroomEarlyOdds1':
        superMiniMushroomEarlyOdds1 += (100 - superMiniMushroomEarlyOdds1)
    if earlyOdds2Max == 'superMiniMushroomEarlyOdds2':
        superMiniMushroomEarlyOdds2 += (100 - superMiniMushroomEarlyOdds2)
    if earlyOdds34Max == 'superMiniMushroomEarlyOdds34':
        superMiniMushroomEarlyOdds34 += (100 - superMiniMushroomEarlyOdds34)
    if midOdds1Max == 'superMiniMushroomMidOdds1':
        superMiniMushroomMidOdds1 += (100 - superMiniMushroomMidOdds1)
    if midOdds2Max == 'superMiniMushroomMidOdds2':
        superMiniMushroomMidOdds2 += (100 - superMiniMushroomMidOdds2)
    if midOdds34Max == 'superMiniMushroomMidOdds34':
        superMiniMushroomMidOdds34 += (100 - superMiniMushroomMidOdds34)
    if lateOdds1Max == 'superMiniMushroomLateOdds1':
        superMiniMushroomLateOdds1 += (100 - superMiniMushroomLateOdds1)
    if lateOdds2Max == 'superMiniMushroomLateOdds2':
        superMiniMushroomLateOdds2 += (100 - superMiniMushroomLateOdds2)
    if lateOdds34Max == 'superMiniMushroomLateOdds34':
        superMiniMushroomLateOdds34 += (100 - superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    if earlyOdds1Max == 'superMegaMushroomEarlyOdds1':
        superMegaMushroomEarlyOdds1 += (100 - superMegaMushroomEarlyOdds1)
    if earlyOdds2Max == 'superMegaMushroomEarlyOdds2':
        superMegaMushroomEarlyOdds2 += (100 - superMegaMushroomEarlyOdds2)
    if earlyOdds34Max == 'superMegaMushroomEarlyOdds34':
        superMegaMushroomEarlyOdds34 += (100 - superMegaMushroomEarlyOdds34)
    if midOdds1Max == 'superMegaMushroomMidOdds1':
        superMegaMushroomMidOdds1 += (100 - superMegaMushroomMidOdds1)
    if midOdds2Max == 'superMegaMushroomMidOdds2':
        superMegaMushroomMidOdds2 += (100 - superMegaMushroomMidOdds2)
    if midOdds34Max == 'superMegaMushroomMidOdds34':
        superMegaMushroomMidOdds34 += (100 - superMegaMushroomMidOdds34)
    if lateOdds1Max == 'superMegaMushroomLateOdds1':
        superMegaMushroomLateOdds1 += (100 - superMegaMushroomLateOdds1)
    if lateOdds2Max == 'superMegaMushroomLateOdds2':
        superMegaMushroomLateOdds2 += (100 - superMegaMushroomLateOdds2)
    if lateOdds34Max == 'superMegaMushroomLateOdds34':
        superMegaMushroomLateOdds34 += (100 - superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    if earlyOdds1Max == 'miniMegaHammerEarlyOdds1':
        miniMegaHammerEarlyOdds1 += (100 - miniMegaHammerEarlyOdds1)
    if earlyOdds2Max == 'miniMegaHammerEarlyOdds2':
        miniMegaHammerEarlyOdds2 += (100 - miniMegaHammerEarlyOdds2)
    if earlyOdds34Max == 'miniMegaHammerEarlyOdds34':
        miniMegaHammerEarlyOdds34 += (100 - miniMegaHammerEarlyOdds34)
    if midOdds1Max == 'miniMegaHammerMidOdds1':
        miniMegaHammerMidOdds1 += (100 - miniMegaHammerMidOdds1)
    if midOdds2Max == 'miniMegaHammerMidOdds2':
        miniMegaHammerMidOdds2 += (100 - miniMegaHammerMidOdds2)
    if midOdds34Max == 'miniMegaHammerMidOdds34':
        miniMegaHammerMidOdds34 += (100 - miniMegaHammerMidOdds34)
    if lateOdds1Max == 'miniMegaHammerLateOdds1':
        miniMegaHammerLateOdds1 += (100 - miniMegaHammerLateOdds1)
    if lateOdds2Max == 'miniMegaHammerLateOdds2':
        miniMegaHammerLateOdds2 += (100 - miniMegaHammerLateOdds2)
    if lateOdds34Max == 'miniMegaHammerLateOdds34':
        miniMegaHammerLateOdds34 += (100 - miniMegaHammerLateOdds34)

    # Warp Pipe
    if earlyOdds1Max == 'warpPipeEarlyOdds1':
        warpPipeEarlyOdds1 += (100 - warpPipeEarlyOdds1)
    if earlyOdds2Max == 'warpPipeEarlyOdds2':
        warpPipeEarlyOdds2 += (100 - warpPipeEarlyOdds2)
    if earlyOdds34Max == 'warpPipeEarlyOdds34':
        warpPipeEarlyOdds34 += (100 - warpPipeEarlyOdds34)
    if midOdds1Max == 'warpPipeMidOdds1':
        warpPipeMidOdds1 += (100 - warpPipeMidOdds1)
    if midOdds2Max == 'warpPipeMidOdds2':
        warpPipeMidOdds2 += (100 - warpPipeMidOdds2)
    if midOdds34Max == 'warpPipeMidOdds34':
        warpPipeMidOdds34 += (100 - warpPipeMidOdds34)
    if lateOdds1Max == 'warpPipeLateOdds1':
        warpPipeLateOdds1 += (100 - warpPipeLateOdds1)
    if lateOdds2Max == 'warpPipeLateOdds2':
        warpPipeLateOdds2 += (100 - warpPipeLateOdds2)
    if lateOdds34Max == 'warpPipeLateOdds34':
        warpPipeLateOdds34 += (100 - warpPipeLateOdds34)

    # Swap Card
    if earlyOdds1Max == 'swapCardEarlyOdds1':
        swapCardEarlyOdds1 += (100 - swapCardEarlyOdds1)
    if earlyOdds2Max == 'swapCardEarlyOdds2':
        swapCardEarlyOdds2 += (100 - swapCardEarlyOdds2)
    if earlyOdds34Max == 'swapCardEarlyOdds34':
        swapCardEarlyOdds34 += (100 - swapCardEarlyOdds34)
    if midOdds1Max == 'swapCardMidOdds1':
        swapCardMidOdds1 += (100 - swapCardMidOdds1)
    if midOdds2Max == 'swapCardMidOdds2':
        swapCardMidOdds2 += (100 - swapCardMidOdds2)
    if midOdds34Max == 'swapCardMidOdds34':
        swapCardMidOdds34 += (100 - swapCardMidOdds34)
    if lateOdds1Max == 'swapCardLateOdds1':
        swapCardLateOdds1 += (100 - swapCardLateOdds1)
    if lateOdds2Max == 'swapCardLateOdds2':
        swapCardLateOdds2 += (100 - swapCardLateOdds2)
    if lateOdds34Max == 'swapCardLateOdds34':
        swapCardLateOdds34 += (100 - swapCardLateOdds34)

    # Sparky Sticker
    if earlyOdds1Max == 'sparkyStickerEarlyOdds1':
        sparkyStickerEarlyOdds1 += (100 - sparkyStickerEarlyOdds1)
    if earlyOdds2Max == 'sparkyStickerEarlyOdds2':
        sparkyStickerEarlyOdds2 += (100 - sparkyStickerEarlyOdds2)
    if earlyOdds34Max == 'sparkyStickerEarlyOdds34':
        sparkyStickerEarlyOdds34 += (100 - sparkyStickerEarlyOdds34)
    if midOdds1Max == 'sparkyStickerMidOdds1':
        sparkyStickerMidOdds1 += (100 - sparkyStickerMidOdds1)
    if midOdds2Max == 'sparkyStickerMidOdds2':
        sparkyStickerMidOdds2 += (100 - sparkyStickerMidOdds2)
    if midOdds34Max == 'sparkyStickerMidOdds34':
        sparkyStickerMidOdds34 += (100 - sparkyStickerMidOdds34)
    if lateOdds1Max == 'sparkyStickerLateOdds1':
        sparkyStickerLateOdds1 += (100 - sparkyStickerLateOdds1)
    if lateOdds2Max == 'sparkyStickerLateOdds2':
        sparkyStickerLateOdds2 += (100 - sparkyStickerLateOdds2)
    if lateOdds34Max == 'sparkyStickerLateOdds34':
        sparkyStickerLateOdds34 += (100 - sparkyStickerLateOdds34)

    # Gaddlight
    if earlyOdds1Max == 'gaddlightEarlyOdds1':
        gaddlightEarlyOdds1 += (100 - gaddlightEarlyOdds1)
    if earlyOdds2Max == 'gaddlightEarlyOdds2':
        gaddlightEarlyOdds2 += (100 - gaddlightEarlyOdds2)
    if earlyOdds34Max == 'gaddlightEarlyOdds34':
        gaddlightEarlyOdds34 += (100 - gaddlightEarlyOdds34)
    if midOdds1Max == 'gaddlightMidOdds1':
        gaddlightMidOdds1 += (100 - gaddlightMidOdds1)
    if midOdds2Max == 'gaddlightMidOdds2':
        gaddlightMidOdds2 += (100 - gaddlightMidOdds2)
    if midOdds34Max == 'gaddlightMidOdds34':
        gaddlightMidOdds34 += (100 - gaddlightMidOdds34)
    if lateOdds1Max == 'gaddlightLateOdds1':
        gaddlightLateOdds1 += (100 - gaddlightLateOdds1)
    if lateOdds2Max == 'gaddlightLateOdds2':
        gaddlightLateOdds2 += (100 - gaddlightLateOdds2)
    if lateOdds34Max == 'gaddlightLateOdds34':
        gaddlightLateOdds34 += (100 - gaddlightLateOdds34)

    # Chomp Call
    if earlyOdds1Max == 'chompCallEarlyOdds1':
        chompCallEarlyOdds1 += (100 - chompCallEarlyOdds1)
    if earlyOdds2Max == 'chompCallEarlyOdds2':
        chompCallEarlyOdds2 += (100 - chompCallEarlyOdds2)
    if earlyOdds34Max == 'chompCallEarlyOdds34':
        chompCallEarlyOdds34 += (100 - chompCallEarlyOdds34)
    if midOdds1Max == 'chompCallMidOdds1':
        chompCallMidOdds1 += (100 - chompCallMidOdds1)
    if midOdds2Max == 'chompCallMidOdds2':
        chompCallMidOdds2 += (100 - chompCallMidOdds2)
    if midOdds34Max == 'chompCallMidOdds34':
        chompCallMidOdds34 += (100 - chompCallMidOdds34)
    if lateOdds1Max == 'chompCallLateOdds1':
        chompCallLateOdds1 += (100 - chompCallLateOdds1)
    if lateOdds2Max == 'chompCallLateOdds2':
        chompCallLateOdds2 += (100 - chompCallLateOdds2)
    if lateOdds34Max == 'chompCallLateOdds34':
        chompCallLateOdds34 += (100 - chompCallLateOdds34)

    # Bowser Suit
    if earlyOdds1Max == 'bowserSuitEarlyOdds1':
        bowserSuitEarlyOdds1 += (100 - bowserSuitEarlyOdds1)
    if earlyOdds2Max == 'bowserSuitEarlyOdds2':
        bowserSuitEarlyOdds2 += (100 - bowserSuitEarlyOdds2)
    if earlyOdds34Max == 'bowserSuitEarlyOdds34':
        bowserSuitEarlyOdds34 += (100 - bowserSuitEarlyOdds34)
    if midOdds1Max == 'bowserSuitMidOdds1':
        bowserSuitMidOdds1 += (100 - bowserSuitMidOdds1)
    if midOdds2Max == 'bowserSuitMidOdds2':
        bowserSuitMidOdds2 += (100 - bowserSuitMidOdds2)
    if midOdds34Max == 'bowserSuitMidOdds34':
        bowserSuitMidOdds34 += (100 - bowserSuitMidOdds34)
    if lateOdds1Max == 'bowserSuitLateOdds1':
        bowserSuitLateOdds1 += (100 - bowserSuitLateOdds1)
    if lateOdds2Max == 'bowserSuitLateOdds2':
        bowserSuitLateOdds2 += (100 - bowserSuitLateOdds2)
    if lateOdds34Max == 'bowserSuitLateOdds34':
        bowserSuitLateOdds34 += (100 - bowserSuitLateOdds34)

    # Crystal Ball
    if earlyOdds1Max == 'crystalBallEarlyOdds1':
        crystalBallEarlyOdds1 += (100 - crystalBallEarlyOdds1)
    if earlyOdds2Max == 'crystalBallEarlyOdds2':
        crystalBallEarlyOdds2 += (100 - crystalBallEarlyOdds2)
    if earlyOdds34Max == 'crystalBallEarlyOdds34':
        crystalBallEarlyOdds34 += (100 - crystalBallEarlyOdds34)
    if midOdds1Max == 'crystalBallMidOdds1':
        crystalBallMidOdds1 += (100 - crystalBallMidOdds1)
    if midOdds2Max == 'crystalBallMidOdds2':
        crystalBallMidOdds2 += (100 - crystalBallMidOdds2)
    if midOdds34Max == 'crystalBallMidOdds34':
        crystalBallMidOdds34 += (100 - crystalBallMidOdds34)
    if lateOdds1Max == 'crystalBallLateOdds1':
        crystalBallLateOdds1 += (100 - crystalBallLateOdds1)
    if lateOdds2Max == 'crystalBallLateOdds2':
        crystalBallLateOdds2 += (100 - crystalBallLateOdds2)
    if lateOdds34Max == 'crystalBallLateOdds34':
        crystalBallLateOdds34 += (100 - crystalBallLateOdds34)

    # Magic Lamp
    if earlyOdds1Max == 'magicLampEarlyOdds1':
        magicLampEarlyOdds1 += (100 - magicLampEarlyOdds1)
    if earlyOdds2Max == 'magicLampEarlyOdds2':
        magicLampEarlyOdds2 += (100 - magicLampEarlyOdds2)
    if earlyOdds34Max == 'magicLampEarlyOdds34':
        magicLampEarlyOdds34 += (100 - magicLampEarlyOdds34)
    if midOdds1Max == 'magicLampMidOdds1':
        magicLampMidOdds1 += (100 - magicLampMidOdds1)
    if midOdds2Max == 'magicLampMidOdds2':
        magicLampMidOdds2 += (100 - magicLampMidOdds2)
    if midOdds34Max == 'magicLampMidOdds34':
        magicLampMidOdds34 += (100 - magicLampMidOdds34)
    if lateOdds1Max == 'magicLampLateOdds1':
        magicLampLateOdds1 += (100 - magicLampLateOdds1)
    if lateOdds2Max == 'magicLampLateOdds2':
        magicLampLateOdds2 += (100 - magicLampLateOdds2)
    if lateOdds34Max == 'magicLampLateOdds34':
        magicLampLateOdds34 += (100 - magicLampLateOdds34)

    # Item Bag
    if earlyOdds1Max == 'itemBagEarlyOdds1':
        itemBagEarlyOdds1 += (100 - itemBagEarlyOdds1)
    if earlyOdds2Max == 'itemBagEarlyOdds2':
        itemBagEarlyOdds2 += (100 - itemBagEarlyOdds2)
    if earlyOdds34Max == 'itemBagEarlyOdds34':
        itemBagEarlyOdds34 += (100 - itemBagEarlyOdds34)
    if midOdds1Max == 'itemBagMidOdds1':
        itemBagMidOdds1 += (100 - itemBagMidOdds1)
    if midOdds2Max == 'itemBagMidOdds2':
        itemBagMidOdds2 += (100 - itemBagMidOdds2)
    if midOdds34Max == 'itemBagMidOdds34':
        itemBagMidOdds34 += (100 - itemBagMidOdds34)
    if lateOdds1Max == 'itemBagLateOdds1':
        itemBagLateOdds1 += (100 - itemBagLateOdds1)
    if lateOdds2Max == 'itemBagLateOdds2':
        itemBagLateOdds2 += (100 - itemBagLateOdds2)
    if lateOdds34Max == 'itemBagLateOdds34':
        itemBagLateOdds34 += (100 - itemBagLateOdds34)

    # Mushroom: DX
    if earlyOdds1Max == 'mushroomEarlyOdds1':
        mushroomEarlyOdds1 += (100 - mushroomEarlyOdds1)
    if earlyOdds2Max == 'mushroomEarlyOdds2':
        mushroomEarlyOdds2 += (100 - mushroomEarlyOdds2)
    if earlyOdds34Max == 'mushroomEarlyOdds34':
        mushroomEarlyOdds34 += (100 - mushroomEarlyOdds34)
    if midOdds1Max == 'mushroomMidOdds1':
        mushroomMidOdds1 += (100 - mushroomMidOdds1)
    if midOdds2Max == 'mushroomMidOdds2':
        mushroomMidOdds2 += (100 - mushroomMidOdds2)
    if midOdds34Max == 'mushroomMidOdds34':
        mushroomMidOdds34 += (100 - mushroomMidOdds34)
    if lateOdds1Max == 'mushroomLateOdds1':
        mushroomLateOdds1 += (100 - mushroomLateOdds1)
    if lateOdds2Max == 'mushroomLateOdds2':
        mushroomLateOdds2 += (100 - mushroomLateOdds2)
    if lateOdds34Max == 'mushroomLateOdds34':
        mushroomLateOdds34 += (100 - mushroomLateOdds34)

    # Golden Mushroom: DX
    if earlyOdds1Max == 'goldenMushroomEarlyOdds1':
        goldenMushroomEarlyOdds1 += (100 - goldenMushroomEarlyOdds1)
    if earlyOdds2Max == 'goldenMushroomEarlyOdds2':
        goldenMushroomEarlyOdds2 += (100 - goldenMushroomEarlyOdds2)
    if earlyOdds34Max == 'goldenMushroomEarlyOdds34':
        goldenMushroomEarlyOdds34 += (100 - goldenMushroomEarlyOdds34)
    if midOdds1Max == 'goldenMushroomMidOdds1':
        goldenMushroomMidOdds1 += (100 - goldenMushroomMidOdds1)
    if midOdds2Max == 'goldenMushroomMidOdds2':
        goldenMushroomMidOdds2 += (100 - goldenMushroomMidOdds2)
    if midOdds34Max == 'goldenMushroomMidOdds34':
        goldenMushroomMidOdds34 += (100 - goldenMushroomMidOdds34)
    if lateOdds1Max == 'goldenMushroomLateOdds1':
        goldenMushroomLateOdds1 += (100 - goldenMushroomLateOdds1)
    if lateOdds2Max == 'goldenMushroomLateOdds2':
        goldenMushroomLateOdds2 += (100 - goldenMushroomLateOdds2)
    if lateOdds34Max == 'goldenMushroomLateOdds34':
        goldenMushroomLateOdds34 += (100 - goldenMushroomLateOdds34)

    # Reverse Mushroom: DX
    if earlyOdds1Max == 'reverseMushroomEarlyOdds1':
        reverseMushroomEarlyOdds1 += (100 - reverseMushroomEarlyOdds1)
    if earlyOdds2Max == 'reverseMushroomEarlyOdds2':
        reverseMushroomEarlyOdds2 += (100 - reverseMushroomEarlyOdds2)
    if earlyOdds34Max == 'reverseMushroomEarlyOdds34':
        reverseMushroomEarlyOdds34 += (100 - reverseMushroomEarlyOdds34)
    if midOdds1Max == 'reverseMushroomMidOdds1':
        reverseMushroomMidOdds1 += (100 - reverseMushroomMidOdds1)
    if midOdds2Max == 'reverseMushroomMidOdds2':
        reverseMushroomMidOdds2 += (100 - reverseMushroomMidOdds2)
    if midOdds34Max == 'reverseMushroomMidOdds34':
        reverseMushroomMidOdds34 += (100 - reverseMushroomMidOdds34)
    if lateOdds1Max == 'reverseMushroomLateOdds1':
        reverseMushroomLateOdds1 += (100 - reverseMushroomLateOdds1)
    if lateOdds2Max == 'reverseMushroomLateOdds2':
        reverseMushroomLateOdds2 += (100 - reverseMushroomLateOdds2)
    if lateOdds34Max == 'reverseMushroomLateOdds34':
        reverseMushroomLateOdds34 += (100 - reverseMushroomLateOdds34)

    # Poison Mushroom: DX
    if earlyOdds1Max == 'poisonMushroomEarlyOdds1':
        poisonMushroomEarlyOdds1 += (100 - poisonMushroomEarlyOdds1)
    if earlyOdds2Max == 'poisonMushroomEarlyOdds2':
        poisonMushroomEarlyOdds2 += (100 - poisonMushroomEarlyOdds2)
    if earlyOdds34Max == 'poisonMushroomEarlyOdds34':
        poisonMushroomEarlyOdds34 += (100 - poisonMushroomEarlyOdds34)
    if midOdds1Max == 'poisonMushroomMidOdds1':
        poisonMushroomMidOdds1 += (100 - poisonMushroomMidOdds1)
    if midOdds2Max == 'poisonMushroomMidOdds2':
        poisonMushroomMidOdds2 += (100 - poisonMushroomMidOdds2)
    if midOdds34Max == 'poisonMushroomMidOdds34':
        poisonMushroomMidOdds34 += (100 - poisonMushroomMidOdds34)
    if lateOdds1Max == 'poisonMushroomLateOdds1':
        poisonMushroomLateOdds1 += (100 - poisonMushroomLateOdds1)
    if lateOdds2Max == 'poisonMushroomLateOdds2':
        poisonMushroomLateOdds2 += (100 - poisonMushroomLateOdds2)
    if lateOdds34Max == 'poisonMushroomLateOdds34':
        poisonMushroomLateOdds34 += (100 - poisonMushroomLateOdds34)

    # Triple Poison Mushroom: DX
    if earlyOdds1Max == 'triplePoisonMushroomEarlyOdds1':
        triplePoisonMushroomEarlyOdds1 += (100 - triplePoisonMushroomEarlyOdds1)
    if earlyOdds2Max == 'triplePoisonMushroomEarlyOdds2':
        triplePoisonMushroomEarlyOdds2 += (100 - triplePoisonMushroomEarlyOdds2)
    if earlyOdds34Max == 'triplePoisonMushroomEarlyOdds34':
        triplePoisonMushroomEarlyOdds34 += (100 - triplePoisonMushroomEarlyOdds34)
    if midOdds1Max == 'triplePoisonMushroomMidOdds1':
        triplePoisonMushroomMidOdds1 += (100 - triplePoisonMushroomMidOdds1)
    if midOdds2Max == 'triplePoisonMushroomMidOdds2':
        triplePoisonMushroomMidOdds2 += (100 - triplePoisonMushroomMidOdds2)
    if midOdds34Max == 'triplePoisonMushroomMidOdds34':
        triplePoisonMushroomMidOdds34 += (100 - triplePoisonMushroomMidOdds34)
    if lateOdds1Max == 'triplePoisonMushroomLateOdds1':
        triplePoisonMushroomLateOdds1 += (100 - triplePoisonMushroomLateOdds1)
    if lateOdds2Max == 'triplePoisonMushroomLateOdds2':
        triplePoisonMushroomLateOdds2 += (100 - triplePoisonMushroomLateOdds2)
    if lateOdds34Max == 'triplePoisonMushroomLateOdds34':
        triplePoisonMushroomLateOdds34 += (100 - triplePoisonMushroomLateOdds34)

    # Celluar Shopper: DX
    if earlyOdds1Max == 'celluarShopperEarlyOdds1':
        celluarShopperEarlyOdds1 += (100 - celluarShopperEarlyOdds1)
    if earlyOdds2Max == 'celluarShopperEarlyOdds2':
        celluarShopperEarlyOdds2 += (100 - celluarShopperEarlyOdds2)
    if earlyOdds34Max == 'celluarShopperEarlyOdds34':
        celluarShopperEarlyOdds34 += (100 - celluarShopperEarlyOdds34)
    if midOdds1Max == 'celluarShopperMidOdds1':
        celluarShopperMidOdds1 += (100 - celluarShopperMidOdds1)
    if midOdds2Max == 'celluarShopperMidOdds2':
        celluarShopperMidOdds2 += (100 - celluarShopperMidOdds2)
    if midOdds34Max == 'celluarShopperMidOdds34':
        celluarShopperMidOdds34 += (100 - celluarShopperMidOdds34)
    if lateOdds1Max == 'celluarShopperLateOdds1':
        celluarShopperLateOdds1 += (100 - celluarShopperLateOdds1)
    if lateOdds2Max == 'celluarShopperLateOdds2':
        celluarShopperLateOdds2 += (100 - celluarShopperLateOdds2)
    if lateOdds34Max == 'celluarShopperLateOdds34':
        celluarShopperLateOdds34 += (100 - celluarShopperLateOdds34)

    # Skeleton Key: DX
    if earlyOdds1Max == 'skeletonKeyEarlyOdds1':
        skeletonKeyEarlyOdds1 += (100 - skeletonKeyEarlyOdds1)
    if earlyOdds2Max == 'skeletonKeyEarlyOdds2':
        skeletonKeyEarlyOdds2 += (100 - skeletonKeyEarlyOdds2)
    if earlyOdds34Max == 'skeletonKeyEarlyOdds34':
        skeletonKeyEarlyOdds34 += (100 - skeletonKeyEarlyOdds34)
    if midOdds1Max == 'skeletonKeyMidOdds1':
        skeletonKeyMidOdds1 += (100 - skeletonKeyMidOdds1)
    if midOdds2Max == 'skeletonKeyMidOdds2':
        skeletonKeyMidOdds2 += (100 - skeletonKeyMidOdds2)
    if midOdds34Max == 'skeletonKeyMidOdds34':
        skeletonKeyMidOdds34 += (100 - skeletonKeyMidOdds34)
    if lateOdds1Max == 'skeletonKeyLateOdds1':
        skeletonKeyLateOdds1 += (100 - skeletonKeyLateOdds1)
    if lateOdds2Max == 'skeletonKeyLateOdds2':
        skeletonKeyLateOdds2 += (100 - skeletonKeyLateOdds2)
    if lateOdds34Max == 'skeletonKeyLateOdds34':
        skeletonKeyLateOdds34 += (100 - skeletonKeyLateOdds34)

    # Plunder Chest: DX
    if earlyOdds1Max == 'plunderChestEarlyOdds1':
        plunderChestEarlyOdds1 += (100 - plunderChestEarlyOdds1)
    if earlyOdds2Max == 'plunderChestEarlyOdds2':
        plunderChestEarlyOdds2 += (100 - plunderChestEarlyOdds2)
    if earlyOdds34Max == 'plunderChestEarlyOdds34':
        plunderChestEarlyOdds34 += (100 - plunderChestEarlyOdds34)
    if midOdds1Max == 'plunderChestMidOdds1':
        plunderChestMidOdds1 += (100 - plunderChestMidOdds1)
    if midOdds2Max == 'plunderChestMidOdds2':
        plunderChestMidOdds2 += (100 - plunderChestMidOdds2)
    if midOdds34Max == 'plunderChestMidOdds34':
        plunderChestMidOdds34 += (100 - plunderChestMidOdds34)
    if lateOdds1Max == 'plunderChestLateOdds1':
        plunderChestLateOdds1 += (100 - plunderChestLateOdds1)
    if lateOdds2Max == 'plunderChestLateOdds2':
        plunderChestLateOdds2 += (100 - plunderChestLateOdds2)
    if lateOdds34Max == 'plunderChestLateOdds34':
        plunderChestLateOdds34 += (100 - plunderChestLateOdds34)

    # Gaddbrush: DX
    if earlyOdds1Max == 'gaddbrushEarlyOdds1':
        gaddbrushEarlyOdds1 += (100 - gaddbrushEarlyOdds1)
    if earlyOdds2Max == 'gaddbrushEarlyOdds2':
        gaddbrushEarlyOdds2 += (100 - gaddbrushEarlyOdds2)
    if earlyOdds34Max == 'gaddbrushEarlyOdds34':
        gaddbrushEarlyOdds34 += (100 - gaddbrushEarlyOdds34)
    if midOdds1Max == 'gaddbrushMidOdds1':
        gaddbrushMidOdds1 += (100 - gaddbrushMidOdds1)
    if midOdds2Max == 'gaddbrushMidOdds2':
        gaddbrushMidOdds2 += (100 - gaddbrushMidOdds2)
    if midOdds34Max == 'gaddbrushMidOdds34':
        gaddbrushMidOdds34 += (100 - gaddbrushMidOdds34)
    if lateOdds1Max == 'gaddbrushLateOdds1':
        gaddbrushLateOdds1 += (100 - gaddbrushLateOdds1)
    if lateOdds2Max == 'gaddbrushLateOdds2':
        gaddbrushLateOdds2 += (100 - gaddbrushLateOdds2)
    if lateOdds34Max == 'gaddbrushLateOdds34':
        gaddbrushLateOdds34 += (100 - gaddbrushLateOdds34)

    # Warp Block: DX
    if earlyOdds1Max == 'warpBlockEarlyOdds1':
        warpBlockEarlyOdds1 += (100 - warpBlockEarlyOdds1)
    if earlyOdds2Max == 'warpBlockEarlyOdds2':
        warpBlockEarlyOdds2 += (100 - warpBlockEarlyOdds2)
    if earlyOdds34Max == 'warpBlockEarlyOdds34':
        warpBlockEarlyOdds34 += (100 - warpBlockEarlyOdds34)
    if midOdds1Max == 'warpBlockMidOdds1':
        warpBlockMidOdds1 += (100 - warpBlockMidOdds1)
    if midOdds2Max == 'warpBlockMidOdds2':
        warpBlockMidOdds2 += (100 - warpBlockMidOdds2)
    if midOdds34Max == 'warpBlockMidOdds34':
        warpBlockMidOdds34 += (100 - warpBlockMidOdds34)
    if lateOdds1Max == 'warpBlockLateOdds1':
        warpBlockLateOdds1 += (100 - warpBlockLateOdds1)
    if lateOdds2Max == 'warpBlockLateOdds2':
        warpBlockLateOdds2 += (100 - warpBlockLateOdds2)
    if lateOdds34Max == 'warpBlockLateOdds34':
        warpBlockLateOdds34 += (100 - warpBlockLateOdds34)

    # Fly Guy: DX
    if earlyOdds1Max == 'flyGuyEarlyOdds1':
        flyGuyEarlyOdds1 += (100 - flyGuyEarlyOdds1)
    if earlyOdds2Max == 'flyGuyEarlyOdds2':
        flyGuyEarlyOdds2 += (100 - flyGuyEarlyOdds2)
    if earlyOdds34Max == 'flyGuyEarlyOdds34':
        flyGuyEarlyOdds34 += (100 - flyGuyEarlyOdds34)
    if midOdds1Max == 'flyGuyMidOdds1':
        flyGuyMidOdds1 += (100 - flyGuyMidOdds1)
    if midOdds2Max == 'flyGuyMidOdds2':
        flyGuyMidOdds2 += (100 - flyGuyMidOdds2)
    if midOdds34Max == 'flyGuyMidOdds34':
        flyGuyMidOdds34 += (100 - flyGuyMidOdds34)
    if lateOdds1Max == 'flyGuyLateOdds1':
        flyGuyLateOdds1 += (100 - flyGuyLateOdds1)
    if lateOdds2Max == 'flyGuyLateOdds2':
        flyGuyLateOdds2 += (100 - flyGuyLateOdds2)
    if lateOdds34Max == 'flyGuyLateOdds34':
        flyGuyLateOdds34 += (100 - flyGuyLateOdds34)

    # Plus Block: DX
    if earlyOdds1Max == 'plusBlockEarlyOdds1':
        plusBlockEarlyOdds1 += (100 - plusBlockEarlyOdds1)
    if earlyOdds2Max == 'plusBlockEarlyOdds2':
        plusBlockEarlyOdds2 += (100 - plusBlockEarlyOdds2)
    if earlyOdds34Max == 'plusBlockEarlyOdds34':
        plusBlockEarlyOdds34 += (100 - plusBlockEarlyOdds34)
    if midOdds1Max == 'plusBlockMidOdds1':
        plusBlockMidOdds1 += (100 - plusBlockMidOdds1)
    if midOdds2Max == 'plusBlockMidOdds2':
        plusBlockMidOdds2 += (100 - plusBlockMidOdds2)
    if midOdds34Max == 'plusBlockMidOdds34':
        plusBlockMidOdds34 += (100 - plusBlockMidOdds34)
    if lateOdds1Max == 'plusBlockLateOdds1':
        plusBlockLateOdds1 += (100 - plusBlockLateOdds1)
    if lateOdds2Max == 'plusBlockLateOdds2':
        plusBlockLateOdds2 += (100 - plusBlockLateOdds2)
    if lateOdds34Max == 'plusBlockLateOdds34':
        plusBlockLateOdds34 += (100 - plusBlockLateOdds34)

    # Minus Block: DX
    if earlyOdds1Max == 'minusBlockEarlyOdds1':
        minusBlockEarlyOdds1 += (100 - minusBlockEarlyOdds1)
    if earlyOdds2Max == 'minusBlockEarlyOdds2':
        minusBlockEarlyOdds2 += (100 - minusBlockEarlyOdds2)
    if earlyOdds34Max == 'minusBlockEarlyOdds34':
        minusBlockEarlyOdds34 += (100 - minusBlockEarlyOdds34)
    if midOdds1Max == 'minusBlockMidOdds1':
        minusBlockMidOdds1 += (100 - minusBlockMidOdds1)
    if midOdds2Max == 'minusBlockMidOdds2':
        minusBlockMidOdds2 += (100 - minusBlockMidOdds2)
    if midOdds34Max == 'minusBlockMidOdds34':
        minusBlockMidOdds34 += (100 - minusBlockMidOdds34)
    if lateOdds1Max == 'minusBlockLateOdds1':
        minusBlockLateOdds1 += (100 - minusBlockLateOdds1)
    if lateOdds2Max == 'minusBlockLateOdds2':
        minusBlockLateOdds2 += (100 - minusBlockLateOdds2)
    if lateOdds34Max == 'minusBlockLateOdds34':
        minusBlockLateOdds34 += (100 - minusBlockLateOdds34)

    # Speed Block: DX
    if earlyOdds1Max == 'speedBlockEarlyOdds1':
        speedBlockEarlyOdds1 += (100 - speedBlockEarlyOdds1)
    if earlyOdds2Max == 'speedBlockEarlyOdds2':
        speedBlockEarlyOdds2 += (100 - speedBlockEarlyOdds2)
    if earlyOdds34Max == 'speedBlockEarlyOdds34':
        speedBlockEarlyOdds34 += (100 - speedBlockEarlyOdds34)
    if midOdds1Max == 'speedBlockMidOdds1':
        speedBlockMidOdds1 += (100 - speedBlockMidOdds1)
    if midOdds2Max == 'speedBlockMidOdds2':
        speedBlockMidOdds2 += (100 - speedBlockMidOdds2)
    if midOdds34Max == 'speedBlockMidOdds34':
        speedBlockMidOdds34 += (100 - speedBlockMidOdds34)
    if lateOdds1Max == 'speedBlockLateOdds1':
        speedBlockLateOdds1 += (100 - speedBlockLateOdds1)
    if lateOdds2Max == 'speedBlockLateOdds2':
        speedBlockLateOdds2 += (100 - speedBlockLateOdds2)
    if lateOdds34Max == 'speedBlockLateOdds34':
        speedBlockLateOdds34 += (100 - speedBlockLateOdds34)

    # Slow Block: DX
    if earlyOdds1Max == 'slowBlockEarlyOdds1':
        slowBlockEarlyOdds1 += (100 - slowBlockEarlyOdds1)
    if earlyOdds2Max == 'slowBlockEarlyOdds2':
        slowBlockEarlyOdds2 += (100 - slowBlockEarlyOdds2)
    if earlyOdds34Max == 'slowBlockEarlyOdds34':
        slowBlockEarlyOdds34 += (100 - slowBlockEarlyOdds34)
    if midOdds1Max == 'slowBlockMidOdds1':
        slowBlockMidOdds1 += (100 - slowBlockMidOdds1)
    if midOdds2Max == 'slowBlockMidOdds2':
        slowBlockMidOdds2 += (100 - slowBlockMidOdds2)
    if midOdds34Max == 'slowBlockMidOdds34':
        slowBlockMidOdds34 += (100 - slowBlockMidOdds34)
    if lateOdds1Max == 'slowBlockLateOdds1':
        slowBlockLateOdds1 += (100 - slowBlockLateOdds1)
    if lateOdds2Max == 'slowBlockLateOdds2':
        slowBlockLateOdds2 += (100 - slowBlockLateOdds2)
    if lateOdds34Max == 'slowBlockLateOdds34':
        slowBlockLateOdds34 += (100 - slowBlockLateOdds34)

    # Hidden Block Card: DX
    if earlyOdds1Max == 'hiddenBlockCardEarlyOdds1':
        hiddenBlockCardEarlyOdds1 += (100 - hiddenBlockCardEarlyOdds1)
    if earlyOdds2Max == 'hiddenBlockCardEarlyOdds2':
        hiddenBlockCardEarlyOdds2 += (100 - hiddenBlockCardEarlyOdds2)
    if earlyOdds34Max == 'hiddenBlockCardEarlyOdds34':
        hiddenBlockCardEarlyOdds34 += (100 - hiddenBlockCardEarlyOdds34)
    if midOdds1Max == 'hiddenBlockCardMidOdds1':
        hiddenBlockCardMidOdds1 += (100 - hiddenBlockCardMidOdds1)
    if midOdds2Max == 'hiddenBlockCardMidOdds2':
        hiddenBlockCardMidOdds2 += (100 - hiddenBlockCardMidOdds2)
    if midOdds34Max == 'hiddenBlockCardMidOdds34':
        hiddenBlockCardMidOdds34 += (100 - hiddenBlockCardMidOdds34)
    if lateOdds1Max == 'hiddenBlockCardLateOdds1':
        hiddenBlockCardLateOdds1 += (100 - hiddenBlockCardLateOdds1)
    if lateOdds2Max == 'hiddenBlockCardLateOdds2':
        hiddenBlockCardLateOdds2 += (100 - hiddenBlockCardLateOdds2)
    if lateOdds34Max == 'hiddenBlockCardLateOdds34':
        hiddenBlockCardLateOdds34 += (100 - hiddenBlockCardLateOdds34)

    # Barter Box: DX
    if earlyOdds1Max == 'barterBoxEarlyOdds1':
        barterBoxEarlyOdds1 += (100 - barterBoxEarlyOdds1)
    if earlyOdds2Max == 'barterBoxEarlyOdds2':
        barterBoxEarlyOdds2 += (100 - barterBoxEarlyOdds2)
    if earlyOdds34Max == 'barterBoxEarlyOdds34':
        barterBoxEarlyOdds34 += (100 - barterBoxEarlyOdds34)
    if midOdds1Max == 'barterBoxMidOdds1':
        barterBoxMidOdds1 += (100 - barterBoxMidOdds1)
    if midOdds2Max == 'barterBoxMidOdds2':
        barterBoxMidOdds2 += (100 - barterBoxMidOdds2)
    if midOdds34Max == 'barterBoxMidOdds34':
        barterBoxMidOdds34 += (100 - barterBoxMidOdds34)
    if lateOdds1Max == 'barterBoxLateOdds1':
        barterBoxLateOdds1 += (100 - barterBoxLateOdds1)
    if lateOdds2Max == 'barterBoxLateOdds2':
        barterBoxLateOdds2 += (100 - barterBoxLateOdds2)
    if lateOdds34Max == 'barterBoxLateOdds34':
        barterBoxLateOdds34 += (100 - barterBoxLateOdds34)

    # Super Warp Pipe: DX
    if earlyOdds1Max == 'superWarpPipeEarlyOdds1':
        superWarpPipeEarlyOdds1 += (100 - superWarpPipeEarlyOdds1)
    if earlyOdds2Max == 'superWarpPipeEarlyOdds2':
        superWarpPipeEarlyOdds2 += (100 - superWarpPipeEarlyOdds2)
    if earlyOdds34Max == 'superWarpPipeEarlyOdds34':
        superWarpPipeEarlyOdds34 += (100 - superWarpPipeEarlyOdds34)
    if midOdds1Max == 'superWarpPipeMidOdds1':
        superWarpPipeMidOdds1 += (100 - superWarpPipeMidOdds1)
    if midOdds2Max == 'superWarpPipeMidOdds2':
        superWarpPipeMidOdds2 += (100 - superWarpPipeMidOdds2)
    if midOdds34Max == 'superWarpPipeMidOdds34':
        superWarpPipeMidOdds34 += (100 - superWarpPipeMidOdds34)
    if lateOdds1Max == 'superWarpPipeLateOdds1':
        superWarpPipeLateOdds1 += (100 - superWarpPipeLateOdds1)
    if lateOdds2Max == 'superWarpPipeLateOdds2':
        superWarpPipeLateOdds2 += (100 - superWarpPipeLateOdds2)
    if lateOdds34Max == 'superWarpPipeLateOdds34':
        superWarpPipeLateOdds34 += (100 - superWarpPipeLateOdds34)

    # Chance Time Charm: DX
    if earlyOdds1Max == 'chanceTimeCharmEarlyOdds1':
        chanceTimeCharmEarlyOdds1 += (100 - chanceTimeCharmEarlyOdds1)
    if earlyOdds2Max == 'chanceTimeCharmEarlyOdds2':
        chanceTimeCharmEarlyOdds2 += (100 - chanceTimeCharmEarlyOdds2)
    if earlyOdds34Max == 'chanceTimeCharmEarlyOdds34':
        chanceTimeCharmEarlyOdds34 += (100 - chanceTimeCharmEarlyOdds34)
    if midOdds1Max == 'chanceTimeCharmMidOdds1':
        chanceTimeCharmMidOdds1 += (100 - chanceTimeCharmMidOdds1)
    if midOdds2Max == 'chanceTimeCharmMidOdds2':
        chanceTimeCharmMidOdds2 += (100 - chanceTimeCharmMidOdds2)
    if midOdds34Max == 'chanceTimeCharmMidOdds34':
        chanceTimeCharmMidOdds34 += (100 - chanceTimeCharmMidOdds34)
    if lateOdds1Max == 'chanceTimeCharmLateOdds1':
        chanceTimeCharmLateOdds1 += (100 - chanceTimeCharmLateOdds1)
    if lateOdds2Max == 'chanceTimeCharmLateOdds2':
        chanceTimeCharmLateOdds2 += (100 - chanceTimeCharmLateOdds2)
    if lateOdds34Max == 'chanceTimeCharmLateOdds34':
        chanceTimeCharmLateOdds34 += (100 - chanceTimeCharmLateOdds34)

    # Wacky Watch: DX
    if earlyOdds1Max == 'wackyWatchEarlyOdds1':
        wackyWatchEarlyOdds1 += (100 - wackyWatchEarlyOdds1)
    if earlyOdds2Max == 'wackyWatchEarlyOdds2':
        wackyWatchEarlyOdds2 += (100 - wackyWatchEarlyOdds2)
    if earlyOdds34Max == 'wackyWatchEarlyOdds34':
        wackyWatchEarlyOdds34 += (100 - wackyWatchEarlyOdds34)
    if midOdds1Max == 'wackyWatchMidOdds1':
        wackyWatchMidOdds1 += (100 - wackyWatchMidOdds1)
    if midOdds2Max == 'wackyWatchMidOdds2':
        wackyWatchMidOdds2 += (100 - wackyWatchMidOdds2)
    if midOdds34Max == 'wackyWatchMidOdds34':
        wackyWatchMidOdds34 += (100 - wackyWatchMidOdds34)
    if lateOdds1Max == 'wackyWatchLateOdds1':
        wackyWatchLateOdds1 += (100 - wackyWatchLateOdds1)
    if lateOdds2Max == 'wackyWatchLateOdds2':
        wackyWatchLateOdds2 += (100 - wackyWatchLateOdds2)
    if lateOdds34Max == 'wackyWatchLateOdds34':
        wackyWatchLateOdds34 += (100 - wackyWatchLateOdds34)
    
    # Mini Mushroom
    miniMushroomEarlyOdds1 = str(miniMushroomEarlyOdds1)
    miniMushroomEarlyOdds2 = str(miniMushroomEarlyOdds2)
    miniMushroomEarlyOdds34 = str(miniMushroomEarlyOdds34)
    miniMushroomMidOdds1 = str(miniMushroomMidOdds1)
    miniMushroomMidOdds2 = str(miniMushroomMidOdds2)
    miniMushroomMidOdds34 = str(miniMushroomMidOdds34)
    miniMushroomLateOdds1 = str(miniMushroomLateOdds1)
    miniMushroomLateOdds2 = str(miniMushroomLateOdds2)
    miniMushroomLateOdds34 = str(miniMushroomLateOdds34)
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = str(megaMushroomEarlyOdds1)
    megaMushroomEarlyOdds2 = str(megaMushroomEarlyOdds2)
    megaMushroomEarlyOdds34 = str(megaMushroomEarlyOdds34)
    megaMushroomMidOdds1 = str(megaMushroomMidOdds1)
    megaMushroomMidOdds2 = str(megaMushroomMidOdds2)
    megaMushroomMidOdds34 = str(megaMushroomMidOdds34)
    megaMushroomLateOdds1 = str(megaMushroomLateOdds1)
    megaMushroomLateOdds2 = str(megaMushroomLateOdds2)
    megaMushroomLateOdds34 = str(megaMushroomLateOdds34)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = str(superMiniMushroomEarlyOdds1)
    superMiniMushroomEarlyOdds2 = str(superMiniMushroomEarlyOdds2)
    superMiniMushroomEarlyOdds34 = str(superMiniMushroomEarlyOdds34)
    superMiniMushroomMidOdds1 = str(superMiniMushroomMidOdds1)
    superMiniMushroomMidOdds2 = str(superMiniMushroomMidOdds2)
    superMiniMushroomMidOdds34 = str(superMiniMushroomMidOdds34)
    superMiniMushroomLateOdds1 = str(superMiniMushroomLateOdds1)
    superMiniMushroomLateOdds2 = str(superMiniMushroomLateOdds2)
    superMiniMushroomLateOdds34 = str(superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = str(superMegaMushroomEarlyOdds1)
    superMegaMushroomEarlyOdds2 = str(superMegaMushroomEarlyOdds2)
    superMegaMushroomEarlyOdds34 = str(superMegaMushroomEarlyOdds34)
    superMegaMushroomMidOdds1 = str(superMegaMushroomMidOdds1)
    superMegaMushroomMidOdds2 = str(superMegaMushroomMidOdds2)
    superMegaMushroomMidOdds34 = str(superMegaMushroomMidOdds34)
    superMegaMushroomLateOdds1 = str(superMegaMushroomLateOdds1)
    superMegaMushroomLateOdds2 = str(superMegaMushroomLateOdds2)
    superMegaMushroomLateOdds34 = str(superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = str(miniMegaHammerEarlyOdds1)
    miniMegaHammerEarlyOdds2 = str(miniMegaHammerEarlyOdds2)
    miniMegaHammerEarlyOdds34 = str(miniMegaHammerEarlyOdds34)
    miniMegaHammerMidOdds1 = str(miniMegaHammerMidOdds1)
    miniMegaHammerMidOdds2 = str(miniMegaHammerMidOdds2)
    miniMegaHammerMidOdds34 = str(miniMegaHammerMidOdds34)
    miniMegaHammerLateOdds1 = str(miniMegaHammerLateOdds1)
    miniMegaHammerLateOdds2 = str(miniMegaHammerLateOdds2)
    miniMegaHammerLateOdds34 = str(miniMegaHammerLateOdds34)

    # Warp Pipe
    warpPipeEarlyOdds1 = str(warpPipeEarlyOdds1)
    warpPipeEarlyOdds2 = str(warpPipeEarlyOdds2)
    warpPipeEarlyOdds34 = str(warpPipeEarlyOdds34)
    warpPipeMidOdds1 = str(warpPipeMidOdds1)
    warpPipeMidOdds2 = str(warpPipeMidOdds2)
    warpPipeMidOdds34 = str(warpPipeMidOdds34)
    warpPipeLateOdds1 = str(warpPipeLateOdds1)
    warpPipeLateOdds2 = str(warpPipeLateOdds2)
    warpPipeLateOdds34 = str(warpPipeLateOdds34)

    # Swap Card
    swapCardEarlyOdds1 = str(swapCardEarlyOdds1)
    swapCardEarlyOdds2 = str(swapCardEarlyOdds2)
    swapCardEarlyOdds34 = str(swapCardEarlyOdds34)
    swapCardMidOdds1 = str(swapCardMidOdds1)
    swapCardMidOdds2 = str(swapCardMidOdds2)
    swapCardMidOdds34 = str(swapCardMidOdds34)
    swapCardLateOdds1 = str(swapCardLateOdds1)
    swapCardLateOdds2 = str(swapCardLateOdds2)
    swapCardLateOdds34 = str(swapCardLateOdds34)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = str(sparkyStickerEarlyOdds1)
    sparkyStickerEarlyOdds2 = str(sparkyStickerEarlyOdds2)
    sparkyStickerEarlyOdds34 = str(sparkyStickerEarlyOdds34)
    sparkyStickerMidOdds1 = str(sparkyStickerMidOdds1)
    sparkyStickerMidOdds2 = str(sparkyStickerMidOdds2)
    sparkyStickerMidOdds34 = str(sparkyStickerMidOdds34)
    sparkyStickerLateOdds1 = str(sparkyStickerLateOdds1)
    sparkyStickerLateOdds2 = str(sparkyStickerLateOdds2)
    sparkyStickerLateOdds34 = str(sparkyStickerLateOdds34)

    # Gaddlight
    gaddlightEarlyOdds1 = str(gaddlightEarlyOdds1)
    gaddlightEarlyOdds2 = str(gaddlightEarlyOdds2)
    gaddlightEarlyOdds34 = str(gaddlightEarlyOdds34)
    gaddlightMidOdds1 = str(gaddlightMidOdds1)
    gaddlightMidOdds2 = str(gaddlightMidOdds2)
    gaddlightMidOdds34 = str(gaddlightMidOdds34)
    gaddlightLateOdds1 = str(gaddlightLateOdds1)
    gaddlightLateOdds2 = str(gaddlightLateOdds2)
    gaddlightLateOdds34 = str(gaddlightLateOdds34)

    # Chomp Call
    chompCallEarlyOdds1 = str(chompCallEarlyOdds1)
    chompCallEarlyOdds2 = str(chompCallEarlyOdds2)
    chompCallEarlyOdds34 = str(chompCallEarlyOdds34)
    chompCallMidOdds1 = str(chompCallMidOdds1)
    chompCallMidOdds2 = str(chompCallMidOdds2)
    chompCallMidOdds34 = str(chompCallMidOdds34)
    chompCallLateOdds1 = str(chompCallLateOdds1)
    chompCallLateOdds2 = str(chompCallLateOdds2)
    chompCallLateOdds34 = str(chompCallLateOdds34)

    # Bowser Suit
    bowserSuitEarlyOdds1 = str(bowserSuitEarlyOdds1)
    bowserSuitEarlyOdds2 = str(bowserSuitEarlyOdds2)
    bowserSuitEarlyOdds34 = str(bowserSuitEarlyOdds34)
    bowserSuitMidOdds1 = str(bowserSuitMidOdds1)
    bowserSuitMidOdds2 = str(bowserSuitMidOdds2)
    bowserSuitMidOdds34 = str(bowserSuitMidOdds34)
    bowserSuitLateOdds1 = str(bowserSuitLateOdds1)
    bowserSuitLateOdds2 = str(bowserSuitLateOdds2)
    bowserSuitLateOdds34 = str(bowserSuitLateOdds34)

    # Crystal Ball
    crystalBallEarlyOdds1 = str(crystalBallEarlyOdds1)
    crystalBallEarlyOdds2 = str(crystalBallEarlyOdds2)
    crystalBallEarlyOdds34 = str(crystalBallEarlyOdds34)
    crystalBallMidOdds1 = str(crystalBallMidOdds1)
    crystalBallMidOdds2 = str(crystalBallMidOdds2)
    crystalBallMidOdds34 = str(crystalBallMidOdds34)
    crystalBallLateOdds1 = str(crystalBallLateOdds1)
    crystalBallLateOdds2 = str(crystalBallLateOdds2)
    crystalBallLateOdds34 = str(crystalBallLateOdds34)

    # Magic Lamp
    magicLampEarlyOdds1 = str(magicLampEarlyOdds1)
    magicLampEarlyOdds2 = str(magicLampEarlyOdds2)
    magicLampEarlyOdds34 = str(magicLampEarlyOdds34)
    magicLampMidOdds1 = str(magicLampMidOdds1)
    magicLampMidOdds2 = str(magicLampMidOdds2)
    magicLampMidOdds34 = str(magicLampMidOdds34)
    magicLampLateOdds1 = str(magicLampLateOdds1)
    magicLampLateOdds2 = str(magicLampLateOdds2)
    magicLampLateOdds34 = str(magicLampLateOdds34)

    # Item Bag
    itemBagEarlyOdds1 = str(itemBagEarlyOdds1)
    itemBagEarlyOdds2 = str(itemBagEarlyOdds2)
    itemBagEarlyOdds34 = str(itemBagEarlyOdds34)
    itemBagMidOdds1 = str(itemBagMidOdds1)
    itemBagMidOdds2 = str(itemBagMidOdds2)
    itemBagMidOdds34 = str(itemBagMidOdds34)
    itemBagLateOdds1 = str(itemBagLateOdds1)
    itemBagLateOdds2 = str(itemBagLateOdds2)
    itemBagLateOdds34 = str(itemBagLateOdds34)

    # Mushroom: DX
    mushroomEarlyOdds1 = str(mushroomEarlyOdds1)
    mushroomEarlyOdds2 = str(mushroomEarlyOdds2)
    mushroomEarlyOdds34 = str(mushroomEarlyOdds34)
    mushroomMidOdds1 = str(mushroomMidOdds1)
    mushroomMidOdds2 = str(mushroomMidOdds2)
    mushroomMidOdds34 = str(mushroomMidOdds34)
    mushroomLateOdds1 = str(mushroomLateOdds1)
    mushroomLateOdds2 = str(mushroomLateOdds2)
    mushroomLateOdds34 = str(mushroomLateOdds34)

    # Golden Mushroom: DX
    goldenMushroomEarlyOdds1 = str(goldenMushroomEarlyOdds1)
    goldenMushroomEarlyOdds2 = str(goldenMushroomEarlyOdds2)
    goldenMushroomEarlyOdds34 = str(goldenMushroomEarlyOdds34)
    goldenMushroomMidOdds1 = str(goldenMushroomMidOdds1)
    goldenMushroomMidOdds2 = str(goldenMushroomMidOdds2)
    goldenMushroomMidOdds34 = str(goldenMushroomMidOdds34)
    goldenMushroomLateOdds1 = str(goldenMushroomLateOdds1)
    goldenMushroomLateOdds2 = str(goldenMushroomLateOdds2)
    goldenMushroomLateOdds34 = str(goldenMushroomLateOdds34)

    # Reverse Mushroom: DX
    reverseMushroomEarlyOdds1 = str(reverseMushroomEarlyOdds1)
    reverseMushroomEarlyOdds2 = str(reverseMushroomEarlyOdds2)
    reverseMushroomEarlyOdds34 = str(reverseMushroomEarlyOdds34)
    reverseMushroomMidOdds1 = str(reverseMushroomMidOdds1)
    reverseMushroomMidOdds2 = str(reverseMushroomMidOdds2)
    reverseMushroomMidOdds34 = str(reverseMushroomMidOdds34)
    reverseMushroomLateOdds1 = str(reverseMushroomLateOdds1)
    reverseMushroomLateOdds2 = str(reverseMushroomLateOdds2)
    reverseMushroomLateOdds34 = str(reverseMushroomLateOdds34)

    # Poison Mushroom: DX
    poisonMushroomEarlyOdds1 = str(poisonMushroomEarlyOdds1)
    poisonMushroomEarlyOdds2 = str(poisonMushroomEarlyOdds2)
    poisonMushroomEarlyOdds34 = str(poisonMushroomEarlyOdds34)
    poisonMushroomMidOdds1 = str(poisonMushroomMidOdds1)
    poisonMushroomMidOdds2 = str(poisonMushroomMidOdds2)
    poisonMushroomMidOdds34 = str(poisonMushroomMidOdds34)
    poisonMushroomLateOdds1 = str(poisonMushroomLateOdds1)
    poisonMushroomLateOdds2 = str(poisonMushroomLateOdds2)
    poisonMushroomLateOdds34 = str(poisonMushroomLateOdds34)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyOdds1 = str(triplePoisonMushroomEarlyOdds1)
    triplePoisonMushroomEarlyOdds2 = str(triplePoisonMushroomEarlyOdds2)
    triplePoisonMushroomEarlyOdds34 = str(triplePoisonMushroomEarlyOdds34)
    triplePoisonMushroomMidOdds1 = str(triplePoisonMushroomMidOdds1)
    triplePoisonMushroomMidOdds2 = str(triplePoisonMushroomMidOdds2)
    triplePoisonMushroomMidOdds34 = str(triplePoisonMushroomMidOdds34)
    triplePoisonMushroomLateOdds1 = str(triplePoisonMushroomLateOdds1)
    triplePoisonMushroomLateOdds2 = str(triplePoisonMushroomLateOdds2)
    triplePoisonMushroomLateOdds34 = str(triplePoisonMushroomLateOdds34)

    # Celluar Shopper: DX
    celluarShopperEarlyOdds1 = str(celluarShopperEarlyOdds1)
    celluarShopperEarlyOdds2 = str(celluarShopperEarlyOdds2)
    celluarShopperEarlyOdds34 = str(celluarShopperEarlyOdds34)
    celluarShopperMidOdds1 = str(celluarShopperMidOdds1)
    celluarShopperMidOdds2 = str(celluarShopperMidOdds2)
    celluarShopperMidOdds34 = str(celluarShopperMidOdds34)
    celluarShopperLateOdds1 = str(celluarShopperLateOdds1)
    celluarShopperLateOdds2 = str(celluarShopperLateOdds2)
    celluarShopperLateOdds34 = str(celluarShopperLateOdds34)

    # Skeleton Key: DX
    skeletonKeyEarlyOdds1 = str(skeletonKeyEarlyOdds1)
    skeletonKeyEarlyOdds2 = str(skeletonKeyEarlyOdds2)
    skeletonKeyEarlyOdds34 = str(skeletonKeyEarlyOdds34)
    skeletonKeyMidOdds1 = str(skeletonKeyMidOdds1)
    skeletonKeyMidOdds2 = str(skeletonKeyMidOdds2)
    skeletonKeyMidOdds34 = str(skeletonKeyMidOdds34)
    skeletonKeyLateOdds1 = str(skeletonKeyLateOdds1)
    skeletonKeyLateOdds2 = str(skeletonKeyLateOdds2)
    skeletonKeyLateOdds34 = str(skeletonKeyLateOdds34)

    # Plunder Chest: DX
    plunderChestEarlyOdds1 = str(plunderChestEarlyOdds1)
    plunderChestEarlyOdds2 = str(plunderChestEarlyOdds2)
    plunderChestEarlyOdds34 = str(plunderChestEarlyOdds34)
    plunderChestMidOdds1 = str(plunderChestMidOdds1)
    plunderChestMidOdds2 = str(plunderChestMidOdds2)
    plunderChestMidOdds34 = str(plunderChestMidOdds34)
    plunderChestLateOdds1 = str(plunderChestLateOdds1)
    plunderChestLateOdds2 = str(plunderChestLateOdds2)
    plunderChestLateOdds34 = str(plunderChestLateOdds34)

    # Gaddbrush: DX
    gaddbrushEarlyOdds1 = str(gaddbrushEarlyOdds1)
    gaddbrushEarlyOdds2 = str(gaddbrushEarlyOdds2)
    gaddbrushEarlyOdds34 = str(gaddbrushEarlyOdds34)
    gaddbrushMidOdds1 = str(gaddbrushMidOdds1)
    gaddbrushMidOdds2 = str(gaddbrushMidOdds2)
    gaddbrushMidOdds34 = str(gaddbrushMidOdds34)
    gaddbrushLateOdds1 = str(gaddbrushLateOdds1)
    gaddbrushLateOdds2 = str(gaddbrushLateOdds2)
    gaddbrushLateOdds34 = str(gaddbrushLateOdds34)

    # Warp Block: DX
    warpBlockEarlyOdds1 = str(warpBlockEarlyOdds1)
    warpBlockEarlyOdds2 = str(warpBlockEarlyOdds2)
    warpBlockEarlyOdds34 = str(warpBlockEarlyOdds34)
    warpBlockMidOdds1 = str(warpBlockMidOdds1)
    warpBlockMidOdds2 = str(warpBlockMidOdds2)
    warpBlockMidOdds34 = str(warpBlockMidOdds34)
    warpBlockLateOdds1 = str(warpBlockLateOdds1)
    warpBlockLateOdds2 = str(warpBlockLateOdds2)
    warpBlockLateOdds34 = str(warpBlockLateOdds34)

    # Fly Guy: DX
    flyGuyEarlyOdds1 = str(flyGuyEarlyOdds1)
    flyGuyEarlyOdds2 = str(flyGuyEarlyOdds2)
    flyGuyEarlyOdds34 = str(flyGuyEarlyOdds34)
    flyGuyMidOdds1 = str(flyGuyMidOdds1)
    flyGuyMidOdds2 = str(flyGuyMidOdds2)
    flyGuyMidOdds34 = str(flyGuyMidOdds34)
    flyGuyLateOdds1 = str(flyGuyLateOdds1)
    flyGuyLateOdds2 = str(flyGuyLateOdds2)
    flyGuyLateOdds34 = str(flyGuyLateOdds34)

    # Plus Block: DX
    plusBlockEarlyOdds1 = str(plusBlockEarlyOdds1)
    plusBlockEarlyOdds2 = str(plusBlockEarlyOdds2)
    plusBlockEarlyOdds34 = str(plusBlockEarlyOdds34)
    plusBlockMidOdds1 = str(plusBlockMidOdds1)
    plusBlockMidOdds2 = str(plusBlockMidOdds2)
    plusBlockMidOdds34 = str(plusBlockMidOdds34)
    plusBlockLateOdds1 = str(plusBlockLateOdds1)
    plusBlockLateOdds2 = str(plusBlockLateOdds2)
    plusBlockLateOdds34 = str(plusBlockLateOdds34)

    # Minus Block: DX
    minusBlockEarlyOdds1 = str(minusBlockEarlyOdds1)
    minusBlockEarlyOdds2 = str(minusBlockEarlyOdds2)
    minusBlockEarlyOdds34 = str(minusBlockEarlyOdds34)
    minusBlockMidOdds1 = str(minusBlockMidOdds1)
    minusBlockMidOdds2 = str(minusBlockMidOdds2)
    minusBlockMidOdds34 = str(minusBlockMidOdds34)
    minusBlockLateOdds1 = str(minusBlockLateOdds1)
    minusBlockLateOdds2 = str(minusBlockLateOdds2)
    minusBlockLateOdds34 = str(minusBlockLateOdds34)

    # Speed Block: DX
    speedBlockEarlyOdds1 = str(speedBlockEarlyOdds1)
    speedBlockEarlyOdds2 = str(speedBlockEarlyOdds2)
    speedBlockEarlyOdds34 = str(speedBlockEarlyOdds34)
    speedBlockMidOdds1 = str(speedBlockMidOdds1)
    speedBlockMidOdds2 = str(speedBlockMidOdds2)
    speedBlockMidOdds34 = str(speedBlockMidOdds34)
    speedBlockLateOdds1 = str(speedBlockLateOdds1)
    speedBlockLateOdds2 = str(speedBlockLateOdds2)
    speedBlockLateOdds34 = str(speedBlockLateOdds34)

    # Slow Block: DX
    slowBlockEarlyOdds1 = str(slowBlockEarlyOdds1)
    slowBlockEarlyOdds2 = str(slowBlockEarlyOdds2)
    slowBlockEarlyOdds34 = str(slowBlockEarlyOdds34)
    slowBlockMidOdds1 = str(slowBlockMidOdds1)
    slowBlockMidOdds2 = str(slowBlockMidOdds2)
    slowBlockMidOdds34 = str(slowBlockMidOdds34)
    slowBlockLateOdds1 = str(slowBlockLateOdds1)
    slowBlockLateOdds2 = str(slowBlockLateOdds2)
    slowBlockLateOdds34 = str(slowBlockLateOdds34)

    # Hidden Block Card: DX
    hiddenBlockCardEarlyOdds1 = str(hiddenBlockCardEarlyOdds1)
    hiddenBlockCardEarlyOdds2 = str(hiddenBlockCardEarlyOdds2)
    hiddenBlockCardEarlyOdds34 = str(hiddenBlockCardEarlyOdds34)
    hiddenBlockCardMidOdds1 = str(hiddenBlockCardMidOdds1)
    hiddenBlockCardMidOdds2 = str(hiddenBlockCardMidOdds2)
    hiddenBlockCardMidOdds34 = str(hiddenBlockCardMidOdds34)
    hiddenBlockCardLateOdds1 = str(hiddenBlockCardLateOdds1)
    hiddenBlockCardLateOdds2 = str(hiddenBlockCardLateOdds2)
    hiddenBlockCardLateOdds34 = str(hiddenBlockCardLateOdds34)

    # Barter Box: DX
    barterBoxEarlyOdds1 = str(barterBoxEarlyOdds1)
    barterBoxEarlyOdds2 = str(barterBoxEarlyOdds2)
    barterBoxEarlyOdds34 = str(barterBoxEarlyOdds34)
    barterBoxMidOdds1 = str(barterBoxMidOdds1)
    barterBoxMidOdds2 = str(barterBoxMidOdds2)
    barterBoxMidOdds34 = str(barterBoxMidOdds34)
    barterBoxLateOdds1 = str(barterBoxLateOdds1)
    barterBoxLateOdds2 = str(barterBoxLateOdds2)
    barterBoxLateOdds34 = str(barterBoxLateOdds34)

    # Super Warp Pipe: DX
    superWarpPipeEarlyOdds1 = str(superWarpPipeEarlyOdds1)
    superWarpPipeEarlyOdds2 = str(superWarpPipeEarlyOdds2)
    superWarpPipeEarlyOdds34 = str(superWarpPipeEarlyOdds34)
    superWarpPipeMidOdds1 = str(superWarpPipeMidOdds1)
    superWarpPipeMidOdds2 = str(superWarpPipeMidOdds2)
    superWarpPipeMidOdds34 = str(superWarpPipeMidOdds34)
    superWarpPipeLateOdds1 = str(superWarpPipeLateOdds1)
    superWarpPipeLateOdds2 = str(superWarpPipeLateOdds2)
    superWarpPipeLateOdds34 = str(superWarpPipeLateOdds34)

    # Chance Time Charm: DX
    chanceTimeCharmEarlyOdds1 = str(chanceTimeCharmEarlyOdds1)
    chanceTimeCharmEarlyOdds2 = str(chanceTimeCharmEarlyOdds2)
    chanceTimeCharmEarlyOdds34 = str(chanceTimeCharmEarlyOdds34)
    chanceTimeCharmMidOdds1 = str(chanceTimeCharmMidOdds1)
    chanceTimeCharmMidOdds2 = str(chanceTimeCharmMidOdds2)
    chanceTimeCharmMidOdds34 = str(chanceTimeCharmMidOdds34)
    chanceTimeCharmLateOdds1 = str(chanceTimeCharmLateOdds1)
    chanceTimeCharmLateOdds2 = str(chanceTimeCharmLateOdds2)
    chanceTimeCharmLateOdds34 = str(chanceTimeCharmLateOdds34)

    # Wacky Watch: DX
    wackyWatchEarlyOdds1 = str(wackyWatchEarlyOdds1)
    wackyWatchEarlyOdds2 = str(wackyWatchEarlyOdds2)
    wackyWatchEarlyOdds34 = str(wackyWatchEarlyOdds34)
    wackyWatchMidOdds1 = str(wackyWatchMidOdds1)
    wackyWatchMidOdds2 = str(wackyWatchMidOdds2)
    wackyWatchMidOdds34 = str(wackyWatchMidOdds34)
    wackyWatchLateOdds1 = str(wackyWatchLateOdds1)
    wackyWatchLateOdds2 = str(wackyWatchLateOdds2)
    wackyWatchLateOdds34 = str(wackyWatchLateOdds34)

    # Bowser Phone: DX
    bowserPhoneEarlyOdds1 = str(bowserPhoneEarlyOdds1)
    bowserPhoneEarlyOdds2 = str(bowserPhoneEarlyOdds2)
    bowserPhoneEarlyOdds34 = str(bowserPhoneEarlyOdds34)
    bowserPhoneMidOdds1 = str(bowserPhoneMidOdds1)
    bowserPhoneMidOdds2 = str(bowserPhoneMidOdds2)
    bowserPhoneMidOdds34 = str(bowserPhoneMidOdds34)
    bowserPhoneLateOdds1 = str(bowserPhoneLateOdds1)
    bowserPhoneLateOdds2 = str(bowserPhoneLateOdds2)
    bowserPhoneLateOdds34 = str(bowserPhoneLateOdds34)


    def convert_to_hex_weight(weight):
        try:
            weight_hex = hex(int(weight))
            if len(weight_hex) == 4:
                return weight_hex[2:]  # Remove '0x' prefix
            elif len(weight_hex) == 3:
                return "0" + weight_hex[2:]  # Add leading zero
            return weight_hex[2:]  # Return as is for other lengths
        except:
            return "00"  # Return default value on error


    # Mini Mushroom
    miniMushroomEarlyOdds1 = convert_to_hex_weight(miniMushroomEarlyOdds1)
    miniMushroomEarlyOdds2 = convert_to_hex_weight(miniMushroomEarlyOdds2)
    miniMushroomEarlyOdds34 = convert_to_hex_weight(miniMushroomEarlyOdds34)
    miniMushroomMidOdds1 = convert_to_hex_weight(miniMushroomMidOdds1)
    miniMushroomMidOdds2 = convert_to_hex_weight(miniMushroomMidOdds2)
    miniMushroomMidOdds34 = convert_to_hex_weight(miniMushroomMidOdds34)
    miniMushroomLateOdds1 = convert_to_hex_weight(miniMushroomLateOdds1)
    miniMushroomLateOdds2 = convert_to_hex_weight(miniMushroomLateOdds2)
    miniMushroomLateOdds34 = convert_to_hex_weight(miniMushroomLateOdds34)
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = convert_to_hex_weight(megaMushroomEarlyOdds1)
    megaMushroomEarlyOdds2 = convert_to_hex_weight(megaMushroomEarlyOdds2)
    megaMushroomEarlyOdds34 = convert_to_hex_weight(megaMushroomEarlyOdds34)
    megaMushroomMidOdds1 = convert_to_hex_weight(megaMushroomMidOdds1)
    megaMushroomMidOdds2 = convert_to_hex_weight(megaMushroomMidOdds2)
    megaMushroomMidOdds34 = convert_to_hex_weight(megaMushroomMidOdds34)
    megaMushroomLateOdds1 = convert_to_hex_weight(megaMushroomLateOdds1)
    megaMushroomLateOdds2 = convert_to_hex_weight(megaMushroomLateOdds2)
    megaMushroomLateOdds34 = convert_to_hex_weight(megaMushroomLateOdds34)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = convert_to_hex_weight(superMiniMushroomEarlyOdds1)
    superMiniMushroomEarlyOdds2 = convert_to_hex_weight(superMiniMushroomEarlyOdds2)
    superMiniMushroomEarlyOdds34 = convert_to_hex_weight(superMiniMushroomEarlyOdds34)
    superMiniMushroomMidOdds1 = convert_to_hex_weight(superMiniMushroomMidOdds1)
    superMiniMushroomMidOdds2 = convert_to_hex_weight(superMiniMushroomMidOdds2)
    superMiniMushroomMidOdds34 = convert_to_hex_weight(superMiniMushroomMidOdds34)
    superMiniMushroomLateOdds1 = convert_to_hex_weight(superMiniMushroomLateOdds1)
    superMiniMushroomLateOdds2 = convert_to_hex_weight(superMiniMushroomLateOdds2)
    superMiniMushroomLateOdds34 = convert_to_hex_weight(superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = convert_to_hex_weight(superMegaMushroomEarlyOdds1)
    superMegaMushroomEarlyOdds2 = convert_to_hex_weight(superMegaMushroomEarlyOdds2)
    superMegaMushroomEarlyOdds34 = convert_to_hex_weight(superMegaMushroomEarlyOdds34)
    superMegaMushroomMidOdds1 = convert_to_hex_weight(superMegaMushroomMidOdds1)
    superMegaMushroomMidOdds2 = convert_to_hex_weight(superMegaMushroomMidOdds2)
    superMegaMushroomMidOdds34 = convert_to_hex_weight(superMegaMushroomMidOdds34)
    superMegaMushroomLateOdds1 = convert_to_hex_weight(superMegaMushroomLateOdds1)
    superMegaMushroomLateOdds2 = convert_to_hex_weight(superMegaMushroomLateOdds2)
    superMegaMushroomLateOdds34 = convert_to_hex_weight(superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = convert_to_hex_weight(miniMegaHammerEarlyOdds1)
    miniMegaHammerEarlyOdds2 = convert_to_hex_weight(miniMegaHammerEarlyOdds2)
    miniMegaHammerEarlyOdds34 = convert_to_hex_weight(miniMegaHammerEarlyOdds34)
    miniMegaHammerMidOdds1 = convert_to_hex_weight(miniMegaHammerMidOdds1)
    miniMegaHammerMidOdds2 = convert_to_hex_weight(miniMegaHammerMidOdds2)
    miniMegaHammerMidOdds34 = convert_to_hex_weight(miniMegaHammerMidOdds34)
    miniMegaHammerLateOdds1 = convert_to_hex_weight(miniMegaHammerLateOdds1)
    miniMegaHammerLateOdds2 = convert_to_hex_weight(miniMegaHammerLateOdds2)
    miniMegaHammerLateOdds34 = convert_to_hex_weight(miniMegaHammerLateOdds34)

    # Warp Pipe
    warpPipeEarlyOdds1 = convert_to_hex_weight(warpPipeEarlyOdds1)
    warpPipeEarlyOdds2 = convert_to_hex_weight(warpPipeEarlyOdds2)
    warpPipeEarlyOdds34 = convert_to_hex_weight(warpPipeEarlyOdds34)
    warpPipeMidOdds1 = convert_to_hex_weight(warpPipeMidOdds1)
    warpPipeMidOdds2 = convert_to_hex_weight(warpPipeMidOdds2)
    warpPipeMidOdds34 = convert_to_hex_weight(warpPipeMidOdds34)
    warpPipeLateOdds1 = convert_to_hex_weight(warpPipeLateOdds1)
    warpPipeLateOdds2 = convert_to_hex_weight(warpPipeLateOdds2)
    warpPipeLateOdds34 = convert_to_hex_weight(warpPipeLateOdds34)

    # Swap Card
    swapCardEarlyOdds1 = convert_to_hex_weight(swapCardEarlyOdds1)
    swapCardEarlyOdds2 = convert_to_hex_weight(swapCardEarlyOdds2)
    swapCardEarlyOdds34 = convert_to_hex_weight(swapCardEarlyOdds34)
    swapCardMidOdds1 = convert_to_hex_weight(swapCardMidOdds1)
    swapCardMidOdds2 = convert_to_hex_weight(swapCardMidOdds2)
    swapCardMidOdds34 = convert_to_hex_weight(swapCardMidOdds34)
    swapCardLateOdds1 = convert_to_hex_weight(swapCardLateOdds1)
    swapCardLateOdds2 = convert_to_hex_weight(swapCardLateOdds2)
    swapCardLateOdds34 = convert_to_hex_weight(swapCardLateOdds34)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = convert_to_hex_weight(sparkyStickerEarlyOdds1)
    sparkyStickerEarlyOdds2 = convert_to_hex_weight(sparkyStickerEarlyOdds2)
    sparkyStickerEarlyOdds34 = convert_to_hex_weight(sparkyStickerEarlyOdds34)
    sparkyStickerMidOdds1 = convert_to_hex_weight(sparkyStickerMidOdds1)
    sparkyStickerMidOdds2 = convert_to_hex_weight(sparkyStickerMidOdds2)
    sparkyStickerMidOdds34 = convert_to_hex_weight(sparkyStickerMidOdds34)
    sparkyStickerLateOdds1 = convert_to_hex_weight(sparkyStickerLateOdds1)
    sparkyStickerLateOdds2 = convert_to_hex_weight(sparkyStickerLateOdds2)
    sparkyStickerLateOdds34 = convert_to_hex_weight(sparkyStickerLateOdds34)

    # Gaddlight
    gaddlightEarlyOdds1 = convert_to_hex_weight(gaddlightEarlyOdds1)
    gaddlightEarlyOdds2 = convert_to_hex_weight(gaddlightEarlyOdds2)
    gaddlightEarlyOdds34 = convert_to_hex_weight(gaddlightEarlyOdds34)
    gaddlightMidOdds1 = convert_to_hex_weight(gaddlightMidOdds1)
    gaddlightMidOdds2 = convert_to_hex_weight(gaddlightMidOdds2)
    gaddlightMidOdds34 = convert_to_hex_weight(gaddlightMidOdds34)
    gaddlightLateOdds1 = convert_to_hex_weight(gaddlightLateOdds1)
    gaddlightLateOdds2 = convert_to_hex_weight(gaddlightLateOdds2)
    gaddlightLateOdds34 = convert_to_hex_weight(gaddlightLateOdds34)

    # Chomp Call
    chompCallEarlyOdds1 = convert_to_hex_weight(chompCallEarlyOdds1)
    chompCallEarlyOdds2 = convert_to_hex_weight(chompCallEarlyOdds2)
    chompCallEarlyOdds34 = convert_to_hex_weight(chompCallEarlyOdds34)
    chompCallMidOdds1 = convert_to_hex_weight(chompCallMidOdds1)
    chompCallMidOdds2 = convert_to_hex_weight(chompCallMidOdds2)
    chompCallMidOdds34 = convert_to_hex_weight(chompCallMidOdds34)
    chompCallLateOdds1 = convert_to_hex_weight(chompCallLateOdds1)
    chompCallLateOdds2 = convert_to_hex_weight(chompCallLateOdds2)
    chompCallLateOdds34 = convert_to_hex_weight(chompCallLateOdds34)

    # Bowser Suit
    bowserSuitEarlyOdds1 = convert_to_hex_weight(bowserSuitEarlyOdds1)
    bowserSuitEarlyOdds2 = convert_to_hex_weight(bowserSuitEarlyOdds2)
    bowserSuitEarlyOdds34 = convert_to_hex_weight(bowserSuitEarlyOdds34)
    bowserSuitMidOdds1 = convert_to_hex_weight(bowserSuitMidOdds1)
    bowserSuitMidOdds2 = convert_to_hex_weight(bowserSuitMidOdds2)
    bowserSuitMidOdds34 = convert_to_hex_weight(bowserSuitMidOdds34)
    bowserSuitLateOdds1 = convert_to_hex_weight(bowserSuitLateOdds1)
    bowserSuitLateOdds2 = convert_to_hex_weight(bowserSuitLateOdds2)
    bowserSuitLateOdds34 = convert_to_hex_weight(bowserSuitLateOdds34)

    # Crystal Ball
    crystalBallEarlyOdds1 = convert_to_hex_weight(crystalBallEarlyOdds1)
    crystalBallEarlyOdds2 = convert_to_hex_weight(crystalBallEarlyOdds2)
    crystalBallEarlyOdds34 = convert_to_hex_weight(crystalBallEarlyOdds34)
    crystalBallMidOdds1 = convert_to_hex_weight(crystalBallMidOdds1)
    crystalBallMidOdds2 = convert_to_hex_weight(crystalBallMidOdds2)
    crystalBallMidOdds34 = convert_to_hex_weight(crystalBallMidOdds34)
    crystalBallLateOdds1 = convert_to_hex_weight(crystalBallLateOdds1)
    crystalBallLateOdds2 = convert_to_hex_weight(crystalBallLateOdds2)
    crystalBallLateOdds34 = convert_to_hex_weight(crystalBallLateOdds34)

    # Magic Lamp
    magicLampEarlyOdds1 = convert_to_hex_weight(magicLampEarlyOdds1)
    magicLampEarlyOdds2 = convert_to_hex_weight(magicLampEarlyOdds2)
    magicLampEarlyOdds34 = convert_to_hex_weight(magicLampEarlyOdds34)
    magicLampMidOdds1 = convert_to_hex_weight(magicLampMidOdds1)
    magicLampMidOdds2 = convert_to_hex_weight(magicLampMidOdds2)
    magicLampMidOdds34 = convert_to_hex_weight(magicLampMidOdds34)
    magicLampLateOdds1 = convert_to_hex_weight(magicLampLateOdds1)
    magicLampLateOdds2 = convert_to_hex_weight(magicLampLateOdds2)
    magicLampLateOdds34 = convert_to_hex_weight(magicLampLateOdds34)

    # Item Bag
    itemBagEarlyOdds1 = convert_to_hex_weight(itemBagEarlyOdds1)
    itemBagEarlyOdds2 = convert_to_hex_weight(itemBagEarlyOdds2)
    itemBagEarlyOdds34 = convert_to_hex_weight(itemBagEarlyOdds34)
    itemBagMidOdds1 = convert_to_hex_weight(itemBagMidOdds1)
    itemBagMidOdds2 = convert_to_hex_weight(itemBagMidOdds2)
    itemBagMidOdds34 = convert_to_hex_weight(itemBagMidOdds34)
    itemBagLateOdds1 = convert_to_hex_weight(itemBagLateOdds1)
    itemBagLateOdds2 = convert_to_hex_weight(itemBagLateOdds2)
    itemBagLateOdds34 = convert_to_hex_weight(itemBagLateOdds34)

    # Mushroom: DX
    mushroomEarlyOdds1 = convert_to_hex_weight(mushroomEarlyOdds1)
    mushroomEarlyOdds2 = convert_to_hex_weight(mushroomEarlyOdds2)
    mushroomEarlyOdds34 = convert_to_hex_weight(mushroomEarlyOdds34)
    mushroomMidOdds1 = convert_to_hex_weight(mushroomMidOdds1)
    mushroomMidOdds2 = convert_to_hex_weight(mushroomMidOdds2)
    mushroomMidOdds34 = convert_to_hex_weight(mushroomMidOdds34)
    mushroomLateOdds1 = convert_to_hex_weight(mushroomLateOdds1)
    mushroomLateOdds2 = convert_to_hex_weight(mushroomLateOdds2)
    mushroomLateOdds34 = convert_to_hex_weight(mushroomLateOdds34)

    # Golden Mushroom: DX
    goldenMushroomEarlyOdds1 = convert_to_hex_weight(goldenMushroomEarlyOdds1)
    goldenMushroomEarlyOdds2 = convert_to_hex_weight(goldenMushroomEarlyOdds2)
    goldenMushroomEarlyOdds34 = convert_to_hex_weight(goldenMushroomEarlyOdds34)
    goldenMushroomMidOdds1 = convert_to_hex_weight(goldenMushroomMidOdds1)
    goldenMushroomMidOdds2 = convert_to_hex_weight(goldenMushroomMidOdds2)
    goldenMushroomMidOdds34 = convert_to_hex_weight(goldenMushroomMidOdds34)
    goldenMushroomLateOdds1 = convert_to_hex_weight(goldenMushroomLateOdds1)
    goldenMushroomLateOdds2 = convert_to_hex_weight(goldenMushroomLateOdds2)
    goldenMushroomLateOdds34 = convert_to_hex_weight(goldenMushroomLateOdds34)

    # Reverse Mushroom: DX
    reverseMushroomEarlyOdds1 = convert_to_hex_weight(reverseMushroomEarlyOdds1)
    reverseMushroomEarlyOdds2 = convert_to_hex_weight(reverseMushroomEarlyOdds2)
    reverseMushroomEarlyOdds34 = convert_to_hex_weight(reverseMushroomEarlyOdds34)
    reverseMushroomMidOdds1 = convert_to_hex_weight(reverseMushroomMidOdds1)
    reverseMushroomMidOdds2 = convert_to_hex_weight(reverseMushroomMidOdds2)
    reverseMushroomMidOdds34 = convert_to_hex_weight(reverseMushroomMidOdds34)
    reverseMushroomLateOdds1 = convert_to_hex_weight(reverseMushroomLateOdds1)
    reverseMushroomLateOdds2 = convert_to_hex_weight(reverseMushroomLateOdds2)
    reverseMushroomLateOdds34 = convert_to_hex_weight(reverseMushroomLateOdds34)

    # Poison Mushroom: DX
    poisonMushroomEarlyOdds1 = convert_to_hex_weight(poisonMushroomEarlyOdds1)
    poisonMushroomEarlyOdds2 = convert_to_hex_weight(poisonMushroomEarlyOdds2)
    poisonMushroomEarlyOdds34 = convert_to_hex_weight(poisonMushroomEarlyOdds34)
    poisonMushroomMidOdds1 = convert_to_hex_weight(poisonMushroomMidOdds1)
    poisonMushroomMidOdds2 = convert_to_hex_weight(poisonMushroomMidOdds2)
    poisonMushroomMidOdds34 = convert_to_hex_weight(poisonMushroomMidOdds34)
    poisonMushroomLateOdds1 = convert_to_hex_weight(poisonMushroomLateOdds1)
    poisonMushroomLateOdds2 = convert_to_hex_weight(poisonMushroomLateOdds2)
    poisonMushroomLateOdds34 = convert_to_hex_weight(poisonMushroomLateOdds34)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyOdds1 = convert_to_hex_weight(triplePoisonMushroomEarlyOdds1)
    triplePoisonMushroomEarlyOdds2 = convert_to_hex_weight(triplePoisonMushroomEarlyOdds2)
    triplePoisonMushroomEarlyOdds34 = convert_to_hex_weight(triplePoisonMushroomEarlyOdds34)
    triplePoisonMushroomMidOdds1 = convert_to_hex_weight(triplePoisonMushroomMidOdds1)
    triplePoisonMushroomMidOdds2 = convert_to_hex_weight(triplePoisonMushroomMidOdds2)
    triplePoisonMushroomMidOdds34 = convert_to_hex_weight(triplePoisonMushroomMidOdds34)
    triplePoisonMushroomLateOdds1 = convert_to_hex_weight(triplePoisonMushroomLateOdds1)
    triplePoisonMushroomLateOdds2 = convert_to_hex_weight(triplePoisonMushroomLateOdds2)
    triplePoisonMushroomLateOdds34 = convert_to_hex_weight(triplePoisonMushroomLateOdds34)

    # Celluar Shopper: DX
    celluarShopperEarlyOdds1 = convert_to_hex_weight(celluarShopperEarlyOdds1)
    celluarShopperEarlyOdds2 = convert_to_hex_weight(celluarShopperEarlyOdds2)
    celluarShopperEarlyOdds34 = convert_to_hex_weight(celluarShopperEarlyOdds34)
    celluarShopperMidOdds1 = convert_to_hex_weight(celluarShopperMidOdds1)
    celluarShopperMidOdds2 = convert_to_hex_weight(celluarShopperMidOdds2)
    celluarShopperMidOdds34 = convert_to_hex_weight(celluarShopperMidOdds34)
    celluarShopperLateOdds1 = convert_to_hex_weight(celluarShopperLateOdds1)
    celluarShopperLateOdds2 = convert_to_hex_weight(celluarShopperLateOdds2)
    celluarShopperLateOdds34 = convert_to_hex_weight(celluarShopperLateOdds34)

    # Skeleton Key: DX
    skeletonKeyEarlyOdds1 = convert_to_hex_weight(skeletonKeyEarlyOdds1)
    skeletonKeyEarlyOdds2 = convert_to_hex_weight(skeletonKeyEarlyOdds2)
    skeletonKeyEarlyOdds34 = convert_to_hex_weight(skeletonKeyEarlyOdds34)
    skeletonKeyMidOdds1 = convert_to_hex_weight(skeletonKeyMidOdds1)
    skeletonKeyMidOdds2 = convert_to_hex_weight(skeletonKeyMidOdds2)
    skeletonKeyMidOdds34 = convert_to_hex_weight(skeletonKeyMidOdds34)
    skeletonKeyLateOdds1 = convert_to_hex_weight(skeletonKeyLateOdds1)
    skeletonKeyLateOdds2 = convert_to_hex_weight(skeletonKeyLateOdds2)
    skeletonKeyLateOdds34 = convert_to_hex_weight(skeletonKeyLateOdds34)

    # Plunder Chest: DX
    plunderChestEarlyOdds1 = convert_to_hex_weight(plunderChestEarlyOdds1)
    plunderChestEarlyOdds2 = convert_to_hex_weight(plunderChestEarlyOdds2)
    plunderChestEarlyOdds34 = convert_to_hex_weight(plunderChestEarlyOdds34)
    plunderChestMidOdds1 = convert_to_hex_weight(plunderChestMidOdds1)
    plunderChestMidOdds2 = convert_to_hex_weight(plunderChestMidOdds2)
    plunderChestMidOdds34 = convert_to_hex_weight(plunderChestMidOdds34)
    plunderChestLateOdds1 = convert_to_hex_weight(plunderChestLateOdds1)
    plunderChestLateOdds2 = convert_to_hex_weight(plunderChestLateOdds2)
    plunderChestLateOdds34 = convert_to_hex_weight(plunderChestLateOdds34)

    # Gaddbrush: DX
    gaddbrushEarlyOdds1 = convert_to_hex_weight(gaddbrushEarlyOdds1)
    gaddbrushEarlyOdds2 = convert_to_hex_weight(gaddbrushEarlyOdds2)
    gaddbrushEarlyOdds34 = convert_to_hex_weight(gaddbrushEarlyOdds34)
    gaddbrushMidOdds1 = convert_to_hex_weight(gaddbrushMidOdds1)
    gaddbrushMidOdds2 = convert_to_hex_weight(gaddbrushMidOdds2)
    gaddbrushMidOdds34 = convert_to_hex_weight(gaddbrushMidOdds34)
    gaddbrushLateOdds1 = convert_to_hex_weight(gaddbrushLateOdds1)
    gaddbrushLateOdds2 = convert_to_hex_weight(gaddbrushLateOdds2)
    gaddbrushLateOdds34 = convert_to_hex_weight(gaddbrushLateOdds34)

    # Warp Block: DX
    warpBlockEarlyOdds1 = convert_to_hex_weight(warpBlockEarlyOdds1)
    warpBlockEarlyOdds2 = convert_to_hex_weight(warpBlockEarlyOdds2)
    warpBlockEarlyOdds34 = convert_to_hex_weight(warpBlockEarlyOdds34)
    warpBlockMidOdds1 = convert_to_hex_weight(warpBlockMidOdds1)
    warpBlockMidOdds2 = convert_to_hex_weight(warpBlockMidOdds2)
    warpBlockMidOdds34 = convert_to_hex_weight(warpBlockMidOdds34)
    warpBlockLateOdds1 = convert_to_hex_weight(warpBlockLateOdds1)
    warpBlockLateOdds2 = convert_to_hex_weight(warpBlockLateOdds2)
    warpBlockLateOdds34 = convert_to_hex_weight(warpBlockLateOdds34)

    # Fly Guy: DX
    flyGuyEarlyOdds1 = convert_to_hex_weight(flyGuyEarlyOdds1)
    flyGuyEarlyOdds2 = convert_to_hex_weight(flyGuyEarlyOdds2)
    flyGuyEarlyOdds34 = convert_to_hex_weight(flyGuyEarlyOdds34)
    flyGuyMidOdds1 = convert_to_hex_weight(flyGuyMidOdds1)
    flyGuyMidOdds2 = convert_to_hex_weight(flyGuyMidOdds2)
    flyGuyMidOdds34 = convert_to_hex_weight(flyGuyMidOdds34)
    flyGuyLateOdds1 = convert_to_hex_weight(flyGuyLateOdds1)
    flyGuyLateOdds2 = convert_to_hex_weight(flyGuyLateOdds2)
    flyGuyLateOdds34 = convert_to_hex_weight(flyGuyLateOdds34)

    # Plus Block: DX
    plusBlockEarlyOdds1 = convert_to_hex_weight(plusBlockEarlyOdds1)
    plusBlockEarlyOdds2 = convert_to_hex_weight(plusBlockEarlyOdds2)
    plusBlockEarlyOdds34 = convert_to_hex_weight(plusBlockEarlyOdds34)
    plusBlockMidOdds1 = convert_to_hex_weight(plusBlockMidOdds1)
    plusBlockMidOdds2 = convert_to_hex_weight(plusBlockMidOdds2)
    plusBlockMidOdds34 = convert_to_hex_weight(plusBlockMidOdds34)
    plusBlockLateOdds1 = convert_to_hex_weight(plusBlockLateOdds1)
    plusBlockLateOdds2 = convert_to_hex_weight(plusBlockLateOdds2)
    plusBlockLateOdds34 = convert_to_hex_weight(plusBlockLateOdds34)

    # Minus Block: DX
    minusBlockEarlyOdds1 = convert_to_hex_weight(minusBlockEarlyOdds1)
    minusBlockEarlyOdds2 = convert_to_hex_weight(minusBlockEarlyOdds2)
    minusBlockEarlyOdds34 = convert_to_hex_weight(minusBlockEarlyOdds34)
    minusBlockMidOdds1 = convert_to_hex_weight(minusBlockMidOdds1)
    minusBlockMidOdds2 = convert_to_hex_weight(minusBlockMidOdds2)
    minusBlockMidOdds34 = convert_to_hex_weight(minusBlockMidOdds34)
    minusBlockLateOdds1 = convert_to_hex_weight(minusBlockLateOdds1)
    minusBlockLateOdds2 = convert_to_hex_weight(minusBlockLateOdds2)
    minusBlockLateOdds34 = convert_to_hex_weight(minusBlockLateOdds34)

    # Speed Block: DX
    speedBlockEarlyOdds1 = convert_to_hex_weight(speedBlockEarlyOdds1)
    speedBlockEarlyOdds2 = convert_to_hex_weight(speedBlockEarlyOdds2)
    speedBlockEarlyOdds34 = convert_to_hex_weight(speedBlockEarlyOdds34)
    speedBlockMidOdds1 = convert_to_hex_weight(speedBlockMidOdds1)
    speedBlockMidOdds2 = convert_to_hex_weight(speedBlockMidOdds2)
    speedBlockMidOdds34 = convert_to_hex_weight(speedBlockMidOdds34)
    speedBlockLateOdds1 = convert_to_hex_weight(speedBlockLateOdds1)
    speedBlockLateOdds2 = convert_to_hex_weight(speedBlockLateOdds2)
    speedBlockLateOdds34 = convert_to_hex_weight(speedBlockLateOdds34)

    # Slow Block: DX
    slowBlockEarlyOdds1 = convert_to_hex_weight(slowBlockEarlyOdds1)
    slowBlockEarlyOdds2 = convert_to_hex_weight(slowBlockEarlyOdds2)
    slowBlockEarlyOdds34 = convert_to_hex_weight(slowBlockEarlyOdds34)
    slowBlockMidOdds1 = convert_to_hex_weight(slowBlockMidOdds1)
    slowBlockMidOdds2 = convert_to_hex_weight(slowBlockMidOdds2)
    slowBlockMidOdds34 = convert_to_hex_weight(slowBlockMidOdds34)
    slowBlockLateOdds1 = convert_to_hex_weight(slowBlockLateOdds1)
    slowBlockLateOdds2 = convert_to_hex_weight(slowBlockLateOdds2)
    slowBlockLateOdds34 = convert_to_hex_weight(slowBlockLateOdds34)

    # Hidden Block Card: DX
    hiddenBlockCardEarlyOdds1 = convert_to_hex_weight(hiddenBlockCardEarlyOdds1)
    hiddenBlockCardEarlyOdds2 = convert_to_hex_weight(hiddenBlockCardEarlyOdds2)
    hiddenBlockCardEarlyOdds34 = convert_to_hex_weight(hiddenBlockCardEarlyOdds34)
    hiddenBlockCardMidOdds1 = convert_to_hex_weight(hiddenBlockCardMidOdds1)
    hiddenBlockCardMidOdds2 = convert_to_hex_weight(hiddenBlockCardMidOdds2)
    hiddenBlockCardMidOdds34 = convert_to_hex_weight(hiddenBlockCardMidOdds34)
    hiddenBlockCardLateOdds1 = convert_to_hex_weight(hiddenBlockCardLateOdds1)
    hiddenBlockCardLateOdds2 = convert_to_hex_weight(hiddenBlockCardLateOdds2)
    hiddenBlockCardLateOdds34 = convert_to_hex_weight(hiddenBlockCardLateOdds34)

    # Barter Box: DX
    barterBoxEarlyOdds1 = convert_to_hex_weight(barterBoxEarlyOdds1)
    barterBoxEarlyOdds2 = convert_to_hex_weight(barterBoxEarlyOdds2)
    barterBoxEarlyOdds34 = convert_to_hex_weight(barterBoxEarlyOdds34)
    barterBoxMidOdds1 = convert_to_hex_weight(barterBoxMidOdds1)
    barterBoxMidOdds2 = convert_to_hex_weight(barterBoxMidOdds2)
    barterBoxMidOdds34 = convert_to_hex_weight(barterBoxMidOdds34)
    barterBoxLateOdds1 = convert_to_hex_weight(barterBoxLateOdds1)
    barterBoxLateOdds2 = convert_to_hex_weight(barterBoxLateOdds2)
    barterBoxLateOdds34 = convert_to_hex_weight(barterBoxLateOdds34)

    # Super Warp Pipe: DX
    superWarpPipeEarlyOdds1 = convert_to_hex_weight(superWarpPipeEarlyOdds1)
    superWarpPipeEarlyOdds2 = convert_to_hex_weight(superWarpPipeEarlyOdds2)
    superWarpPipeEarlyOdds34 = convert_to_hex_weight(superWarpPipeEarlyOdds34)
    superWarpPipeMidOdds1 = convert_to_hex_weight(superWarpPipeMidOdds1)
    superWarpPipeMidOdds2 = convert_to_hex_weight(superWarpPipeMidOdds2)
    superWarpPipeMidOdds34 = convert_to_hex_weight(superWarpPipeMidOdds34)
    superWarpPipeLateOdds1 = convert_to_hex_weight(superWarpPipeLateOdds1)
    superWarpPipeLateOdds2 = convert_to_hex_weight(superWarpPipeLateOdds2)
    superWarpPipeLateOdds34 = convert_to_hex_weight(superWarpPipeLateOdds34)

    # Chance Time Charm: DX
    chanceTimeCharmEarlyOdds1 = convert_to_hex_weight(chanceTimeCharmEarlyOdds1)
    chanceTimeCharmEarlyOdds2 = convert_to_hex_weight(chanceTimeCharmEarlyOdds2)
    chanceTimeCharmEarlyOdds34 = convert_to_hex_weight(chanceTimeCharmEarlyOdds34)
    chanceTimeCharmMidOdds1 = convert_to_hex_weight(chanceTimeCharmMidOdds1)
    chanceTimeCharmMidOdds2 = convert_to_hex_weight(chanceTimeCharmMidOdds2)
    chanceTimeCharmMidOdds34 = convert_to_hex_weight(chanceTimeCharmMidOdds34)
    chanceTimeCharmLateOdds1 = convert_to_hex_weight(chanceTimeCharmLateOdds1)
    chanceTimeCharmLateOdds2 = convert_to_hex_weight(chanceTimeCharmLateOdds2)
    chanceTimeCharmLateOdds34 = convert_to_hex_weight(chanceTimeCharmLateOdds34)

    # Wacky Watch: DX
    wackyWatchEarlyOdds1 = convert_to_hex_weight(wackyWatchEarlyOdds1)
    wackyWatchEarlyOdds2 = convert_to_hex_weight(wackyWatchEarlyOdds2)
    wackyWatchEarlyOdds34 = convert_to_hex_weight(wackyWatchEarlyOdds34)
    wackyWatchMidOdds1 = convert_to_hex_weight(wackyWatchMidOdds1)
    wackyWatchMidOdds2 = convert_to_hex_weight(wackyWatchMidOdds2)
    wackyWatchMidOdds34 = convert_to_hex_weight(wackyWatchMidOdds34)
    wackyWatchLateOdds1 = convert_to_hex_weight(wackyWatchLateOdds1)
    wackyWatchLateOdds2 = convert_to_hex_weight(wackyWatchLateOdds2)
    wackyWatchLateOdds34 = convert_to_hex_weight(wackyWatchLateOdds34)

    # Bowser Phone: DX
    bowserPhoneEarlyOdds1 = convert_to_hex_weight(bowserPhoneEarlyOdds1)
    bowserPhoneEarlyOdds2 = convert_to_hex_weight(bowserPhoneEarlyOdds2)
    bowserPhoneEarlyOdds34 = convert_to_hex_weight(bowserPhoneEarlyOdds34)
    bowserPhoneMidOdds1 = convert_to_hex_weight(bowserPhoneMidOdds1)
    bowserPhoneMidOdds2 = convert_to_hex_weight(bowserPhoneMidOdds2)
    bowserPhoneMidOdds34 = convert_to_hex_weight(bowserPhoneMidOdds34)
    bowserPhoneLateOdds1 = convert_to_hex_weight(bowserPhoneLateOdds1)
    bowserPhoneLateOdds2 = convert_to_hex_weight(bowserPhoneLateOdds2)
    bowserPhoneLateOdds34 = convert_to_hex_weight(bowserPhoneLateOdds34)

    generatedCode = getItemShopOddsFourDX(miniMushroomEarlyOdds1, miniMushroomEarlyOdds2, miniMushroomEarlyOdds34, miniMushroomMidOdds1, miniMushroomMidOdds2, miniMushroomMidOdds34, miniMushroomLateOdds1, miniMushroomLateOdds2, miniMushroomLateOdds34, megaMushroomEarlyOdds1, megaMushroomEarlyOdds2, megaMushroomEarlyOdds34, megaMushroomMidOdds1, megaMushroomMidOdds2, megaMushroomMidOdds34, megaMushroomLateOdds1, megaMushroomLateOdds2, megaMushroomLateOdds34, superMiniMushroomEarlyOdds1, superMiniMushroomEarlyOdds2, superMiniMushroomEarlyOdds34, superMiniMushroomMidOdds1, superMiniMushroomMidOdds2, superMiniMushroomMidOdds34, superMiniMushroomLateOdds1, superMiniMushroomLateOdds2, superMiniMushroomLateOdds34, superMegaMushroomEarlyOdds1, superMegaMushroomEarlyOdds2, superMegaMushroomEarlyOdds34, superMegaMushroomMidOdds1, superMegaMushroomMidOdds2, superMegaMushroomMidOdds34, superMegaMushroomLateOdds1, superMegaMushroomLateOdds2, superMegaMushroomLateOdds34, miniMegaHammerEarlyOdds1, miniMegaHammerEarlyOdds2, miniMegaHammerEarlyOdds34, miniMegaHammerMidOdds1, miniMegaHammerMidOdds2, miniMegaHammerMidOdds34, miniMegaHammerLateOdds1, miniMegaHammerLateOdds2, miniMegaHammerLateOdds34, warpPipeEarlyOdds1, warpPipeEarlyOdds2, warpPipeEarlyOdds34, warpPipeMidOdds1, warpPipeMidOdds2, warpPipeMidOdds34, warpPipeLateOdds1, warpPipeLateOdds2, warpPipeLateOdds34, swapCardEarlyOdds1, swapCardEarlyOdds2, swapCardEarlyOdds34, swapCardMidOdds1, swapCardMidOdds2, swapCardMidOdds34, swapCardLateOdds1, swapCardLateOdds2, swapCardLateOdds34, sparkyStickerEarlyOdds1, sparkyStickerEarlyOdds2, sparkyStickerEarlyOdds34, sparkyStickerMidOdds1, sparkyStickerMidOdds2, sparkyStickerMidOdds34, sparkyStickerLateOdds1, sparkyStickerLateOdds2, sparkyStickerLateOdds34, gaddlightEarlyOdds1, gaddlightEarlyOdds2, gaddlightEarlyOdds34, gaddlightMidOdds1, gaddlightMidOdds2, gaddlightMidOdds34, gaddlightLateOdds1, gaddlightLateOdds2, gaddlightLateOdds34, chompCallEarlyOdds1, chompCallEarlyOdds2, chompCallEarlyOdds34, chompCallMidOdds1, chompCallMidOdds2, chompCallMidOdds34, chompCallLateOdds1, chompCallLateOdds2, chompCallLateOdds34, bowserSuitEarlyOdds1, bowserSuitEarlyOdds2, bowserSuitEarlyOdds34, bowserSuitMidOdds1, bowserSuitMidOdds2, bowserSuitMidOdds34, bowserSuitLateOdds1, bowserSuitLateOdds2, bowserSuitLateOdds34, crystalBallEarlyOdds1, crystalBallEarlyOdds2, crystalBallEarlyOdds34, crystalBallMidOdds1, crystalBallMidOdds2, crystalBallMidOdds34, crystalBallLateOdds1, crystalBallLateOdds2, crystalBallLateOdds34, magicLampEarlyOdds1, magicLampEarlyOdds2, magicLampEarlyOdds34, magicLampMidOdds1, magicLampMidOdds2, magicLampMidOdds34, magicLampLateOdds1, magicLampLateOdds2, magicLampLateOdds34, itemBagEarlyOdds1, itemBagEarlyOdds2, itemBagEarlyOdds34, itemBagMidOdds1, itemBagMidOdds2, itemBagMidOdds34, itemBagLateOdds1, itemBagLateOdds2, itemBagLateOdds34, mushroomEarlyOdds1, mushroomEarlyOdds2, mushroomEarlyOdds34, mushroomMidOdds1, mushroomMidOdds2, mushroomMidOdds34, mushroomLateOdds1, mushroomLateOdds2, mushroomLateOdds34, goldenMushroomEarlyOdds1, goldenMushroomEarlyOdds2, goldenMushroomEarlyOdds34, goldenMushroomMidOdds1, goldenMushroomMidOdds2, goldenMushroomMidOdds34, goldenMushroomLateOdds1, goldenMushroomLateOdds2, goldenMushroomLateOdds34, reverseMushroomEarlyOdds1, reverseMushroomEarlyOdds2, reverseMushroomEarlyOdds34, reverseMushroomMidOdds1, reverseMushroomMidOdds2, reverseMushroomMidOdds34, reverseMushroomLateOdds1, reverseMushroomLateOdds2, reverseMushroomLateOdds34, poisonMushroomEarlyOdds1, poisonMushroomEarlyOdds2, poisonMushroomEarlyOdds34, poisonMushroomMidOdds1, poisonMushroomMidOdds2, poisonMushroomMidOdds34, poisonMushroomLateOdds1, poisonMushroomLateOdds2, poisonMushroomLateOdds34, triplePoisonMushroomEarlyOdds1, triplePoisonMushroomEarlyOdds2, triplePoisonMushroomEarlyOdds34, triplePoisonMushroomMidOdds1, triplePoisonMushroomMidOdds2, triplePoisonMushroomMidOdds34, triplePoisonMushroomLateOdds1, triplePoisonMushroomLateOdds2, triplePoisonMushroomLateOdds34, celluarShopperEarlyOdds1, celluarShopperEarlyOdds2, celluarShopperEarlyOdds34, celluarShopperMidOdds1, celluarShopperMidOdds2, celluarShopperMidOdds34, celluarShopperLateOdds1, celluarShopperLateOdds2, celluarShopperLateOdds34, skeletonKeyEarlyOdds1, skeletonKeyEarlyOdds2, skeletonKeyEarlyOdds34, skeletonKeyMidOdds1, skeletonKeyMidOdds2, skeletonKeyMidOdds34, skeletonKeyLateOdds1, skeletonKeyLateOdds2, skeletonKeyLateOdds34, plunderChestEarlyOdds1, plunderChestEarlyOdds2, plunderChestEarlyOdds34, plunderChestMidOdds1, plunderChestMidOdds2, plunderChestMidOdds34, plunderChestLateOdds1, plunderChestLateOdds2, plunderChestLateOdds34, gaddbrushEarlyOdds1, gaddbrushEarlyOdds2, gaddbrushEarlyOdds34, gaddbrushMidOdds1, gaddbrushMidOdds2, gaddbrushMidOdds34, gaddbrushLateOdds1, gaddbrushLateOdds2, gaddbrushLateOdds34, warpBlockEarlyOdds1, warpBlockEarlyOdds2, warpBlockEarlyOdds34, warpBlockMidOdds1, warpBlockMidOdds2, warpBlockMidOdds34, warpBlockLateOdds1, warpBlockLateOdds2, warpBlockLateOdds34, flyGuyEarlyOdds1, flyGuyEarlyOdds2, flyGuyEarlyOdds34, flyGuyMidOdds1, flyGuyMidOdds2, flyGuyMidOdds34, flyGuyLateOdds1, flyGuyLateOdds2, flyGuyLateOdds34, plusBlockEarlyOdds1, plusBlockEarlyOdds2, plusBlockEarlyOdds34, plusBlockMidOdds1, plusBlockMidOdds2, plusBlockMidOdds34, plusBlockLateOdds1, plusBlockLateOdds2, plusBlockLateOdds34, minusBlockEarlyOdds1, minusBlockEarlyOdds2, minusBlockEarlyOdds34, minusBlockMidOdds1, minusBlockMidOdds2, minusBlockMidOdds34, minusBlockLateOdds1, minusBlockLateOdds2, minusBlockLateOdds34, speedBlockEarlyOdds1, speedBlockEarlyOdds2, speedBlockEarlyOdds34, speedBlockMidOdds1, speedBlockMidOdds2, speedBlockMidOdds34, speedBlockLateOdds1, speedBlockLateOdds2, speedBlockLateOdds34, slowBlockEarlyOdds1, slowBlockEarlyOdds2, slowBlockEarlyOdds34, slowBlockMidOdds1, slowBlockMidOdds2, slowBlockMidOdds34, slowBlockLateOdds1, slowBlockLateOdds2, slowBlockLateOdds34, bowserPhoneEarlyOdds1, bowserPhoneEarlyOdds2, bowserPhoneEarlyOdds34, bowserPhoneMidOdds1, bowserPhoneMidOdds2, bowserPhoneMidOdds34, bowserPhoneLateOdds1, bowserPhoneLateOdds2, bowserPhoneLateOdds34, doubleDipEarlyOdds1, doubleDipEarlyOdds2, doubleDipEarlyOdds34, doubleDipMidOdds1, doubleDipMidOdds2, doubleDipMidOdds34, doubleDipLateOdds1, doubleDipLateOdds2, doubleDipLateOdds34, hiddenBlockCardEarlyOdds1, hiddenBlockCardEarlyOdds2, hiddenBlockCardEarlyOdds34, hiddenBlockCardMidOdds1, hiddenBlockCardMidOdds2, hiddenBlockCardMidOdds34, hiddenBlockCardLateOdds1, hiddenBlockCardLateOdds2, hiddenBlockCardLateOdds34, barterBoxEarlyOdds1, barterBoxEarlyOdds2, barterBoxEarlyOdds34, barterBoxMidOdds1, barterBoxMidOdds2, barterBoxMidOdds34, barterBoxLateOdds1, barterBoxLateOdds2, barterBoxLateOdds34, superWarpPipeEarlyOdds1, superWarpPipeEarlyOdds2, superWarpPipeEarlyOdds34, superWarpPipeMidOdds1, superWarpPipeMidOdds2, superWarpPipeMidOdds34, superWarpPipeLateOdds1, superWarpPipeLateOdds2, superWarpPipeLateOdds34, chanceTimeCharmEarlyOdds1, chanceTimeCharmEarlyOdds2, chanceTimeCharmEarlyOdds34, chanceTimeCharmMidOdds1, chanceTimeCharmMidOdds2, chanceTimeCharmMidOdds34, chanceTimeCharmLateOdds1, chanceTimeCharmLateOdds2, chanceTimeCharmLateOdds34, wackyWatchEarlyOdds1, wackyWatchEarlyOdds2, wackyWatchEarlyOdds34, wackyWatchMidOdds1, wackyWatchMidOdds2, wackyWatchMidOdds34, wackyWatchLateOdds1, wackyWatchLateOdds2, wackyWatchLateOdds34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
