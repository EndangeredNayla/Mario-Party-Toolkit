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

def itemsEvent_mp4CustomItemSpace(miniMushroomPrice1 = "0", miniMushroomPrice2 = "0", miniMushroomPrice34 = "0", miniMushroomShopOdds12 = "0", miniMushroomShopOdds34 = "0", miniMushroomSpaceOdds1 = "0", miniMushroomSpaceOdds2 = "0", miniMushroomSpaceOdds34 = "0", megaMushroomPrice1 = "0", megaMushroomPrice2 = "0", megaMushroomPrice34 = "0", megaMushroomShopOdds12 = "0", megaMushroomShopOdds34 = "0", megaMushroomSpaceOdds1 = "0", megaMushroomSpaceOdds2 = "0", megaMushroomSpaceOdds34 = "0", superMiniMushroomPrice1 = "0", superMiniMushroomPrice2 = "0", superMiniMushroomPrice34 = "0", superMiniMushroomShopOdds12 = "0", superMiniMushroomShopOdds34 = "0", superMiniMushroomSpaceOdds1 = "0", superMiniMushroomSpaceOdds2 = "0", superMiniMushroomSpaceOdds34 = "0", superMegaMushroomPrice1 = "0", superMegaMushroomPrice2 = "0", superMegaMushroomPrice34 = "0", superMegaMushroomShopOdds12 = "0", superMegaMushroomShopOdds34 = "0", superMegaMushroomSpaceOdds1 = "0", superMegaMushroomSpaceOdds2 = "0", superMegaMushroomSpaceOdds34 = "0", miniMegaHammerPrice1 = "0", miniMegaHammerPrice2 = "0", miniMegaHammerPrice34 = "0", miniMegaHammerShopOdds12 = "0", miniMegaHammerShopOdds34 = "0", miniMegaHammerSpaceOdds1 = "0", miniMegaHammerSpaceOdds2 = "0", miniMegaHammerSpaceOdds34 = "0", warpPipePrice1 = "0", warpPipePrice2 = "0", warpPipePrice34 = "0", warpPipeShopOdds12 = "0", warpPipeShopOdds34 = "0", warpPipeSpaceOdds1 = "0", warpPipeSpaceOdds2 = "0", warpPipeSpaceOdds34 = "0", swapCardPrice1 = "0", swapCardPrice2 = "0", swapCardPrice34 = "0", swapCardShopOdds12 = "0", swapCardShopOdds34 = "0", swapCardSpaceOdds1 = "0", swapCardSpaceOdds2 = "0", swapCardSpaceOdds34 = "0", sparkyStickerPrice1 = "0", sparkyStickerPrice2 = "0", sparkyStickerPrice34 = "0", sparkyStickerShopOdds12 = "0", sparkyStickerShopOdds34 = "0", sparkyStickerSpaceOdds1 = "0", sparkyStickerSpaceOdds2 = "0", sparkyStickerSpaceOdds34 = "0", gaddlightPrice1 = "0", gaddlightPrice2 = "0", gaddlightPrice34 = "0", gaddlightShopOdds12 = "0", gaddlightShopOdds34 = "0", gaddlightSpaceOdds1 = "0", gaddlightSpaceOdds2 = "0", gaddlightSpaceOdds34 = "0", chompCallPrice1 = "0", chompCallPrice2 = "0", chompCallPrice34 = "0", chompCallShopOdds12 = "0", chompCallShopOdds34 = "0", chompCallSpaceOdds1 = "0", chompCallSpaceOdds2 = "0", chompCallSpaceOdds34 = "0", bowserSuitPrice1 = "0", bowserSuitPrice2 = "0", bowserSuitPrice34 = "0", bowserSuitShopOdds12 = "0", bowserSuitShopOdds34 = "0", bowserSuitSpaceOdds1 = "0", bowserSuitSpaceOdds2 = "0", bowserSuitSpaceOdds34 = "0", crystalBallPrice1 = "0", crystalBallPrice2 = "0", crystalBallPrice34 = "0", crystalBallShopOdds12 = "0", crystalBallShopOdds34 = "0", crystalBallSpaceOdds1 = "0", crystalBallSpaceOdds2 = "0", crystalBallSpaceOdds34 = "0", magicLampPrice1 = "0", magicLampPrice2 = "0", magicLampPrice34 = "0", magicLampShopOdds12 = "0", magicLampShopOdds34 = "0", magicLampSpaceOdds1 = "0", magicLampSpaceOdds2 = "0", magicLampSpaceOdds34 = "0", itemBagPrice1 = "0", itemBagPrice2 = "0", itemBagPrice34 = "0", itemBagShopOdds12 = "0", itemBagShopOdds34 = "0", itemBagSpaceOdds1 = "0", itemBagSpaceOdds2 = "0", itemBagSpaceOdds34 = "0", mushroomPrice1 = "0", mushroomPrice2 = "0", mushroomPrice34 = "0", mushroomShopOdds12 = "0", mushroomShopOdds34 = "0", mushroomSpaceOdds1 = "0", mushroomSpaceOdds2 = "0", mushroomSpaceOdds34 = "0", goldenMushroomPrice1 = "0", goldenMushroomPrice2 = "0", goldenMushroomPrice34 = "0", goldenMushroomShopOdds12 = "0", goldenMushroomShopOdds34 = "0", goldenMushroomSpaceOdds1 = "0", goldenMushroomSpaceOdds2 = "0", goldenMushroomSpaceOdds34 = "0", reverseMushroomPrice1 = "0", reverseMushroomPrice2 = "0", reverseMushroomPrice34 = "0", reverseMushroomShopOdds12 = "0", reverseMushroomShopOdds34 = "0", reverseMushroomSpaceOdds1 = "0", reverseMushroomSpaceOdds2 = "0", reverseMushroomSpaceOdds34 = "0", poisonMushroomPrice1 = "0", poisonMushroomPrice2 = "0", poisonMushroomPrice34 = "0", poisonMushroomShopOdds12 = "0", poisonMushroomShopOdds34 = "0", poisonMushroomSpaceOdds1 = "0", poisonMushroomSpaceOdds2 = "0", poisonMushroomSpaceOdds34 = "0", triplePoisonMushroomPrice1 = "0", triplePoisonMushroomPrice2 = "0", triplePoisonMushroomPrice34 = "0", triplePoisonMushroomShopOdds12 = "0", triplePoisonMushroomShopOdds34 = "0", triplePoisonMushroomSpaceOdds1 = "0", triplePoisonMushroomSpaceOdds2 = "0", triplePoisonMushroomSpaceOdds34 = "0", celluarShopperPrice1 = "0", celluarShopperPrice2 = "0", celluarShopperPrice34 = "0", celluarShopperShopOdds12 = "0", celluarShopperShopOdds34 = "0", celluarShopperSpaceOdds1 = "0", celluarShopperSpaceOdds2 = "0", celluarShopperSpaceOdds34 = "0", skeletonKeyPrice1 = "0", skeletonKeyPrice2 = "0", skeletonKeyPrice34 = "0", skeletonKeyShopOdds12 = "0", skeletonKeyShopOdds34 = "0", skeletonKeySpaceOdds1 = "0", skeletonKeySpaceOdds2 = "0", skeletonKeySpaceOdds34 = "0", plunderChestPrice1 = "0", plunderChestPrice2 = "0", plunderChestPrice34 = "0", plunderChestShopOdds12 = "0", plunderChestShopOdds34 = "0", plunderChestSpaceOdds1 = "0", plunderChestSpaceOdds2 = "0", plunderChestSpaceOdds34 = "0", gaddbrushPrice1 = "0", gaddbrushPrice2 = "0", gaddbrushPrice34 = "0", gaddbrushShopOdds12 = "0", gaddbrushShopOdds34 = "0", gaddbrushSpaceOdds1 = "0", gaddbrushSpaceOdds2 = "0", gaddbrushSpaceOdds34 = "0", warpBlockPrice1 = "0", warpBlockPrice2 = "0", warpBlockPrice34 = "0", warpBlockShopOdds12 = "0", warpBlockShopOdds34 = "0", warpBlockSpaceOdds1 = "0", warpBlockSpaceOdds2 = "0", warpBlockSpaceOdds34 = "0", flyGuyPrice1 = "0", flyGuyPrice2 = "0", flyGuyPrice34 = "0", flyGuyShopOdds12 = "0", flyGuyShopOdds34 = "0", flyGuySpaceOdds1 = "0", flyGuySpaceOdds2 = "0", flyGuySpaceOdds34 = "0", plusBlockPrice1 = "0", plusBlockPrice2 = "0", plusBlockPrice34 = "0", plusBlockShopOdds12 = "0", plusBlockShopOdds34 = "0", plusBlockSpaceOdds1 = "0", plusBlockSpaceOdds2 = "0", plusBlockSpaceOdds34 = "0", minusBlockPrice1 = "0", minusBlockPrice2 = "0", minusBlockPrice34 = "0", minusBlockShopOdds12 = "0", minusBlockShopOdds34 = "0", minusBlockSpaceOdds1 = "0", minusBlockSpaceOdds2 = "0", minusBlockSpaceOdds34 = "0", speedBlockPrice1 = "0", speedBlockPrice2 = "0", speedBlockPrice34 = "0", speedBlockShopOdds12 = "0", speedBlockShopOdds34 = "0", speedBlockSpaceOdds1 = "0", speedBlockSpaceOdds2 = "0", speedBlockSpaceOdds34 = "0", slowBlockPrice1 = "0", slowBlockPrice2 = "0", slowBlockPrice34 = "0", slowBlockShopOdds12 = "0", slowBlockShopOdds34 = "0", slowBlockSpaceOdds1 = "0", slowBlockSpaceOdds2 = "0", slowBlockSpaceOdds34 = "0", bowserPhonePrice1 = "0", bowserPhonePrice2 = "0", bowserPhonePrice34 = "0", bowserPhoneShopOdds12 = "0", bowserPhoneShopOdds34 = "0", bowserPhoneSpaceOdds1 = "0", bowserPhoneSpaceOdds2 = "0", bowserPhoneSpaceOdds34 = "0", doubleDipPrice1 = "0", doubleDipPrice2 = "0", doubleDipPrice34 = "0", doubleDipShopOdds12 = "0", doubleDipShopOdds34 = "0", doubleDipSpaceOdds1 = "0", doubleDipSpaceOdds2 = "0", doubleDipSpaceOdds34 = "0", hiddenBlockCardPrice1 = "0", hiddenBlockCardPrice2 = "0", hiddenBlockCardPrice34 = "0", hiddenBlockCardShopOdds12 = "0", hiddenBlockCardShopOdds34 = "0", hiddenBlockCardSpaceOdds1 = "0", hiddenBlockCardSpaceOdds2 = "0", hiddenBlockCardSpaceOdds34 = "0", barterBoxPrice1 = "0", barterBoxPrice2 = "0", barterBoxPrice34 = "0", barterBoxShopOdds12 = "0", barterBoxShopOdds34 = "0", barterBoxSpaceOdds1 = "0", barterBoxSpaceOdds2 = "0", barterBoxSpaceOdds34 = "0", superWarpPipePrice1 = "0", superWarpPipePrice2 = "0", superWarpPipePrice34 = "0", superWarpPipeShopOdds12 = "0", superWarpPipeShopOdds34 = "0", superWarpPipeSpaceOdds1 = "0", superWarpPipeSpaceOdds2 = "0", superWarpPipeSpaceOdds34 = "0", chanceTimeCharmPrice1 = "0", chanceTimeCharmPrice2 = "0", chanceTimeCharmPrice34 = "0", chanceTimeCharmShopOdds12 = "0", chanceTimeCharmShopOdds34 = "0", chanceTimeCharmSpaceOdds1 = "0", chanceTimeCharmSpaceOdds2 = "0", chanceTimeCharmSpaceOdds34 = "0", wackyWatchPrice1 = "0", wackyWatchPrice2 = "0", wackyWatchPrice34 = "0", wackyWatchShopOdds12 = "0", wackyWatchShopOdds34 = "0", wackyWatchSpaceOdds1 = "0", wackyWatchSpaceOdds2 = "0", wackyWatchSpaceOdds34 = "0"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    miniMushroomPrice1 = get_capsule_value(miniMushroomPrice1) or "0"
    miniMushroomPrice2 = get_capsule_value(miniMushroomPrice2) or "0"
    miniMushroomPrice34 = get_capsule_value(miniMushroomPrice34) or "0"
    miniMushroomShopOdds12 = get_capsule_value(miniMushroomShopOdds12) or "0"
    miniMushroomShopOdds34 = get_capsule_value(miniMushroomShopOdds34) or "0"
    miniMushroomSpaceOdds1 = get_capsule_value(miniMushroomSpaceOdds1) or "0"
    miniMushroomSpaceOdds2 = get_capsule_value(miniMushroomSpaceOdds2) or "0"
    miniMushroomSpaceOdds34 = get_capsule_value(miniMushroomSpaceOdds34) or "0"
    megaMushroomPrice1 = get_capsule_value(megaMushroomPrice1) or "0"
    megaMushroomPrice2 = get_capsule_value(megaMushroomPrice2) or "0"
    megaMushroomPrice34 = get_capsule_value(megaMushroomPrice34) or "0"
    megaMushroomShopOdds12 = get_capsule_value(megaMushroomShopOdds12) or "0"
    megaMushroomShopOdds34 = get_capsule_value(megaMushroomShopOdds34) or "0"
    megaMushroomSpaceOdds1 = get_capsule_value(megaMushroomSpaceOdds1) or "0"
    megaMushroomSpaceOdds2 = get_capsule_value(megaMushroomSpaceOdds2) or "0"
    megaMushroomSpaceOdds34 = get_capsule_value(megaMushroomSpaceOdds34) or "0"
    superMiniMushroomPrice1 = get_capsule_value(superMiniMushroomPrice1) or "0"
    superMiniMushroomPrice2 = get_capsule_value(superMiniMushroomPrice2) or "0"
    superMiniMushroomPrice34 = get_capsule_value(superMiniMushroomPrice34) or "0"
    superMiniMushroomShopOdds12 = get_capsule_value(superMiniMushroomShopOdds12) or "0"
    superMiniMushroomShopOdds34 = get_capsule_value(superMiniMushroomShopOdds34) or "0"
    superMiniMushroomSpaceOdds1 = get_capsule_value(superMiniMushroomSpaceOdds1) or "0"
    superMiniMushroomSpaceOdds2 = get_capsule_value(superMiniMushroomSpaceOdds2) or "0"
    superMiniMushroomSpaceOdds34 = get_capsule_value(superMiniMushroomSpaceOdds34) or "0"
    superMegaMushroomPrice1 = get_capsule_value(superMegaMushroomPrice1) or "0"
    superMegaMushroomPrice2 = get_capsule_value(superMegaMushroomPrice2) or "0"
    superMegaMushroomPrice34 = get_capsule_value(superMegaMushroomPrice34) or "0"
    superMegaMushroomShopOdds12 = get_capsule_value(superMegaMushroomShopOdds12) or "0"
    superMegaMushroomShopOdds34 = get_capsule_value(superMegaMushroomShopOdds34) or "0"
    superMegaMushroomSpaceOdds1 = get_capsule_value(superMegaMushroomSpaceOdds1) or "0"
    superMegaMushroomSpaceOdds2 = get_capsule_value(superMegaMushroomSpaceOdds2) or "0"
    superMegaMushroomSpaceOdds34 = get_capsule_value(superMegaMushroomSpaceOdds34) or "0"
    miniMegaHammerPrice1 = get_capsule_value(miniMegaHammerPrice1) or "0"
    miniMegaHammerPrice2 = get_capsule_value(miniMegaHammerPrice2) or "0"
    miniMegaHammerPrice34 = get_capsule_value(miniMegaHammerPrice34) or "0"
    miniMegaHammerShopOdds12 = get_capsule_value(miniMegaHammerShopOdds12) or "0"
    miniMegaHammerShopOdds34 = get_capsule_value(miniMegaHammerShopOdds34) or "0"
    miniMegaHammerSpaceOdds1 = get_capsule_value(miniMegaHammerSpaceOdds1) or "0"
    miniMegaHammerSpaceOdds2 = get_capsule_value(miniMegaHammerSpaceOdds2) or "0"
    miniMegaHammerSpaceOdds34 = get_capsule_value(miniMegaHammerSpaceOdds34) or "0"
    warpPipePrice1 = get_capsule_value(warpPipePrice1) or "0"
    warpPipePrice2 = get_capsule_value(warpPipePrice2) or "0"
    warpPipePrice34 = get_capsule_value(warpPipePrice34) or "0"
    warpPipeShopOdds12 = get_capsule_value(warpPipeShopOdds12) or "0"
    warpPipeShopOdds34 = get_capsule_value(warpPipeShopOdds34) or "0"
    warpPipeSpaceOdds1 = get_capsule_value(warpPipeSpaceOdds1) or "0"
    warpPipeSpaceOdds2 = get_capsule_value(warpPipeSpaceOdds2) or "0"
    warpPipeSpaceOdds34 = get_capsule_value(warpPipeSpaceOdds34) or "0"
    swapCardPrice1 = get_capsule_value(swapCardPrice1) or "0"
    swapCardPrice2 = get_capsule_value(swapCardPrice2) or "0"
    swapCardPrice34 = get_capsule_value(swapCardPrice34) or "0"
    swapCardShopOdds12 = get_capsule_value(swapCardShopOdds12) or "0"
    swapCardShopOdds34 = get_capsule_value(swapCardShopOdds34) or "0"
    swapCardSpaceOdds1 = get_capsule_value(swapCardSpaceOdds1) or "0"
    swapCardSpaceOdds2 = get_capsule_value(swapCardSpaceOdds2) or "0"
    swapCardSpaceOdds34 = get_capsule_value(swapCardSpaceOdds34) or "0"
    sparkyStickerPrice1 = get_capsule_value(sparkyStickerPrice1) or "0"
    sparkyStickerPrice2 = get_capsule_value(sparkyStickerPrice2) or "0"
    sparkyStickerPrice34 = get_capsule_value(sparkyStickerPrice34) or "0"
    sparkyStickerShopOdds12 = get_capsule_value(sparkyStickerShopOdds12) or "0"
    sparkyStickerShopOdds34 = get_capsule_value(sparkyStickerShopOdds34) or "0"
    sparkyStickerSpaceOdds1 = get_capsule_value(sparkyStickerSpaceOdds1) or "0"
    sparkyStickerSpaceOdds2 = get_capsule_value(sparkyStickerSpaceOdds2) or "0"
    sparkyStickerSpaceOdds34 = get_capsule_value(sparkyStickerSpaceOdds34) or "0"
    gaddlightPrice1 = get_capsule_value(gaddlightPrice1) or "0"    
    gaddlightPrice2 = get_capsule_value(gaddlightPrice2) or "0"
    gaddlightPrice34 = get_capsule_value(gaddlightPrice2) or "0"    
    gaddlightShopOdds12 = get_capsule_value(gaddlightShopOdds12) or "0"
    gaddlightShopOdds34 = get_capsule_value(gaddlightShopOdds34) or "0"
    gaddlightSpaceOdds1 = get_capsule_value(gaddlightSpaceOdds1) or "0"
    gaddlightSpaceOdds2 = get_capsule_value(gaddlightSpaceOdds2) or "0"
    gaddlightSpaceOdds34 = get_capsule_value(gaddlightSpaceOdds34) or "0"
    chompCallPrice1 = get_capsule_value(chompCallPrice1) or "0"
    chompCallPrice2 = get_capsule_value(chompCallPrice2) or "0" 
    chompCallPrice34 = get_capsule_value(chompCallPrice34) or "0"
    chompCallShopOdds12 = get_capsule_value(chompCallShopOdds12) or "0"
    chompCallShopOdds34 = get_capsule_value(chompCallShopOdds34) or "0"
    chompCallSpaceOdds1 = get_capsule_value(chompCallSpaceOdds1) or "0"
    chompCallSpaceOdds2 = get_capsule_value(chompCallSpaceOdds2) or "0"
    chompCallSpaceOdds34 = get_capsule_value(chompCallSpaceOdds34) or "0"
    bowserSuitPrice1 = get_capsule_value(bowserSuitPrice1) or "0"
    bowserSuitPrice2 = get_capsule_value(bowserSuitPrice2) or "0"
    bowserSuitPrice34 = get_capsule_value(bowserSuitPrice34) or "0"
    bowserSuitShopOdds12 = get_capsule_value(bowserSuitShopOdds12) or "0"
    bowserSuitShopOdds34 = get_capsule_value(bowserSuitShopOdds34) or "0"
    bowserSuitSpaceOdds1 = get_capsule_value(bowserSuitSpaceOdds1) or "0"
    bowserSuitSpaceOdds2 = get_capsule_value(bowserSuitSpaceOdds2) or "0"
    bowserSuitSpaceOdds34 = get_capsule_value(bowserSuitSpaceOdds34) or "0"
    crystalBallPrice1 = get_capsule_value(crystalBallPrice1) or "0"
    crystalBallPrice2 = get_capsule_value(crystalBallPrice2) or "0"
    crystalBallPrice34 = get_capsule_value(crystalBallPrice34) or "0"
    crystalBallShopOdds12 = get_capsule_value(crystalBallShopOdds12) or "0"
    crystalBallShopOdds34 = get_capsule_value(crystalBallShopOdds34) or "0"
    crystalBallSpaceOdds1 = get_capsule_value(crystalBallSpaceOdds1) or "0"
    crystalBallSpaceOdds2 = get_capsule_value(crystalBallSpaceOdds2) or "0"
    crystalBallSpaceOdds34 = get_capsule_value(crystalBallSpaceOdds34) or "0"
    magicLampPrice1 = get_capsule_value(magicLampPrice1) or "0"
    magicLampPrice2 = get_capsule_value(magicLampPrice2) or "0"
    magicLampPrice34 = get_capsule_value(magicLampPrice34) or "0"
    magicLampShopOdds12 = get_capsule_value(magicLampShopOdds12) or "0"
    magicLampShopOdds34 = get_capsule_value(magicLampShopOdds34) or "0"
    magicLampSpaceOdds1 = get_capsule_value(magicLampSpaceOdds1) or "0"
    magicLampSpaceOdds2 = get_capsule_value(magicLampSpaceOdds2) or "0"
    magicLampSpaceOdds34 = get_capsule_value(magicLampSpaceOdds34) or "0"
    itemBagPrice1 = get_capsule_value(itemBagPrice1) or "0"
    itemBagPrice2 = get_capsule_value(itemBagPrice2) or "0"
    itemBagPrice34 = get_capsule_value(itemBagPrice34) or "0"
    itemBagShopOdds12 = get_capsule_value(itemBagShopOdds12) or "0"
    itemBagShopOdds34 = get_capsule_value(itemBagShopOdds34) or "0"
    itemBagSpaceOdds1 = get_capsule_value(itemBagSpaceOdds1) or "0"
    itemBagSpaceOdds2 = get_capsule_value(itemBagSpaceOdds2) or "0"
    itemBagSpaceOdds34 = get_capsule_value(itemBagSpaceOdds34) or "0"
    mushroomPrice1 = get_capsule_value(mushroomPrice1) or "0"
    mushroomPrice2 = get_capsule_value(mushroomPrice2) or "0"
    mushroomPrice34 = get_capsule_value(mushroomPrice34) or "0"
    mushroomShopOdds12 = get_capsule_value(mushroomShopOdds12) or "0"
    mushroomShopOdds34 = get_capsule_value(mushroomShopOdds34) or "0"
    mushroomSpaceOdds1 = get_capsule_value(mushroomSpaceOdds1) or "0"
    mushroomSpaceOdds2 = get_capsule_value(mushroomSpaceOdds2) or "0"
    mushroomSpaceOdds34 = get_capsule_value(mushroomSpaceOdds34) or "0"
    goldenMushroomPrice1 = get_capsule_value(goldenMushroomPrice1) or "0"
    goldenMushroomPrice2 = get_capsule_value(goldenMushroomPrice2) or "0"
    goldenMushroomPrice34 = get_capsule_value(goldenMushroomPrice34) or "0"
    goldenMushroomShopOdds12 = get_capsule_value(goldenMushroomShopOdds12) or "0"
    goldenMushroomShopOdds34 = get_capsule_value(goldenMushroomShopOdds34) or "0"
    goldenMushroomSpaceOdds1 = get_capsule_value(goldenMushroomSpaceOdds1) or "0"
    goldenMushroomSpaceOdds2 = get_capsule_value(goldenMushroomSpaceOdds2) or "0"
    goldenMushroomSpaceOdds34 = get_capsule_value(goldenMushroomSpaceOdds34) or "0"
    reverseMushroomPrice1 = get_capsule_value(reverseMushroomPrice1) or "0"
    reverseMushroomPrice2 = get_capsule_value(reverseMushroomPrice2) or "0"
    reverseMushroomPrice34 = get_capsule_value(reverseMushroomPrice34) or "0"
    reverseMushroomShopOdds12 = get_capsule_value(reverseMushroomShopOdds12) or "0"
    reverseMushroomShopOdds34 = get_capsule_value(reverseMushroomShopOdds34) or "0"
    reverseMushroomSpaceOdds1 = get_capsule_value(reverseMushroomSpaceOdds1) or "0"
    reverseMushroomSpaceOdds2 = get_capsule_value(reverseMushroomSpaceOdds2) or "0"
    reverseMushroomSpaceOdds34 = get_capsule_value(reverseMushroomSpaceOdds34) or "0"
    poisonMushroomPrice1 = get_capsule_value(poisonMushroomPrice1) or "0"
    poisonMushroomPrice2 = get_capsule_value(poisonMushroomPrice2) or "0"
    poisonMushroomPrice34 = get_capsule_value(poisonMushroomPrice34) or "0"
    poisonMushroomShopOdds12 = get_capsule_value(poisonMushroomShopOdds12) or "0"
    poisonMushroomShopOdds34 = get_capsule_value(poisonMushroomShopOdds34) or "0"
    poisonMushroomSpaceOdds1 = get_capsule_value(poisonMushroomSpaceOdds1) or "0"
    poisonMushroomSpaceOdds2 = get_capsule_value(poisonMushroomSpaceOdds2) or "0"
    poisonMushroomSpaceOdds34 = get_capsule_value(poisonMushroomSpaceOdds34) or "0"
    triplePoisonMushroomPrice1 = get_capsule_value(triplePoisonMushroomPrice1) or "0"
    triplePoisonMushroomPrice2 = get_capsule_value(triplePoisonMushroomPrice2) or "0"
    triplePoisonMushroomPrice34 = get_capsule_value(triplePoisonMushroomPrice34) or "0"
    triplePoisonMushroomShopOdds12 = get_capsule_value(triplePoisonMushroomShopOdds12) or "0"
    triplePoisonMushroomShopOdds34 = get_capsule_value(triplePoisonMushroomShopOdds34) or "0"
    triplePoisonMushroomSpaceOdds1 = get_capsule_value(triplePoisonMushroomSpaceOdds1) or "0"
    triplePoisonMushroomSpaceOdds2 = get_capsule_value(triplePoisonMushroomSpaceOdds2) or "0"
    triplePoisonMushroomSpaceOdds34 = get_capsule_value(triplePoisonMushroomSpaceOdds34) or "0"
    celluarShopperPrice1 = get_capsule_value(celluarShopperPrice1) or "0"
    celluarShopperPrice2 = get_capsule_value(celluarShopperPrice2) or "0"
    celluarShopperPrice34 = get_capsule_value(celluarShopperPrice34) or "0"
    celluarShopperShopOdds12 = get_capsule_value(celluarShopperShopOdds12) or "0"
    celluarShopperShopOdds34 = get_capsule_value(celluarShopperShopOdds34) or "0"
    celluarShopperSpaceOdds1 = get_capsule_value(celluarShopperSpaceOdds1) or "0"
    celluarShopperSpaceOdds2 = get_capsule_value(celluarShopperSpaceOdds2) or "0"
    celluarShopperSpaceOdds34 = get_capsule_value(celluarShopperSpaceOdds34) or "0"
    skeletonKeyPrice1 = get_capsule_value(skeletonKeyPrice1) or "0"
    skeletonKeyPrice2 = get_capsule_value(skeletonKeyPrice2) or "0"
    skeletonKeyPrice34 = get_capsule_value(skeletonKeyPrice34) or "0"
    skeletonKeyShopOdds12 = get_capsule_value(skeletonKeyShopOdds12) or "0"
    skeletonKeyShopOdds34 = get_capsule_value(skeletonKeyShopOdds34) or "0"
    skeletonKeySpaceOdds1 = get_capsule_value(skeletonKeySpaceOdds1) or "0"
    skeletonKeySpaceOdds2 = get_capsule_value(skeletonKeySpaceOdds2) or "0"
    skeletonKeySpaceOdds34 = get_capsule_value(skeletonKeySpaceOdds34) or "0"
    plunderChestPrice1 = get_capsule_value(plunderChestPrice1) or "0"
    plunderChestPrice2 = get_capsule_value(plunderChestPrice2) or "0"
    plunderChestPrice34 = get_capsule_value(plunderChestPrice34) or "0"
    plunderChestShopOdds12 = get_capsule_value(plunderChestShopOdds12) or "0"
    plunderChestShopOdds34 = get_capsule_value(plunderChestShopOdds34) or "0"
    plunderChestSpaceOdds1 = get_capsule_value(plunderChestSpaceOdds1) or "0"
    plunderChestSpaceOdds2 = get_capsule_value(plunderChestSpaceOdds2) or "0"
    plunderChestSpaceOdds34 = get_capsule_value(plunderChestSpaceOdds34) or "0"
    gaddbrushPrice1 = get_capsule_value(gaddbrushPrice1) or "0"
    gaddbrushPrice2 = get_capsule_value(gaddbrushPrice2) or "0"
    gaddbrushPrice34 = get_capsule_value(gaddbrushPrice34) or "0"
    gaddbrushShopOdds12 = get_capsule_value(gaddbrushShopOdds12) or "0"
    gaddbrushShopOdds34 = get_capsule_value(gaddbrushShopOdds34) or "0"
    gaddbrushSpaceOdds1 = get_capsule_value(gaddbrushSpaceOdds1) or "0"
    gaddbrushSpaceOdds2 = get_capsule_value(gaddbrushSpaceOdds2) or "0"
    gaddbrushSpaceOdds34 = get_capsule_value(gaddbrushSpaceOdds34) or "0"
    warpBlockPrice1 = get_capsule_value(warpBlockPrice1) or "0"
    warpBlockPrice2 = get_capsule_value(warpBlockPrice2) or "0"
    warpBlockPrice34 = get_capsule_value(warpBlockPrice34) or "0"
    warpBlockShopOdds12 = get_capsule_value(warpBlockShopOdds12) or "0"
    warpBlockShopOdds34 = get_capsule_value(warpBlockShopOdds34) or "0"
    warpBlockSpaceOdds1 = get_capsule_value(warpBlockSpaceOdds1) or "0"
    warpBlockSpaceOdds2 = get_capsule_value(warpBlockSpaceOdds2) or "0"
    warpBlockSpaceOdds34 = get_capsule_value(warpBlockSpaceOdds34) or "0"
    flyGuyPrice1 = get_capsule_value(flyGuyPrice1) or "0"
    flyGuyPrice2 = get_capsule_value(flyGuyPrice2) or "0"
    flyGuyPrice34 = get_capsule_value(flyGuyPrice34) or "0"
    flyGuyShopOdds12 = get_capsule_value(flyGuyShopOdds12) or "0"
    flyGuyShopOdds34 = get_capsule_value(flyGuyShopOdds34) or "0"
    flyGuySpaceOdds1 = get_capsule_value(flyGuySpaceOdds1) or "0"
    flyGuySpaceOdds2 = get_capsule_value(flyGuySpaceOdds2) or "0"
    flyGuySpaceOdds34 = get_capsule_value(flyGuySpaceOdds34) or "0"
    plusBlockPrice1 = get_capsule_value(plusBlockPrice1) or "0"
    plusBlockPrice2 = get_capsule_value(plusBlockPrice2) or "0"
    plusBlockPrice34 = get_capsule_value(plusBlockPrice34) or "0"
    plusBlockShopOdds12 = get_capsule_value(plusBlockShopOdds12) or "0"
    plusBlockShopOdds34 = get_capsule_value(plusBlockShopOdds34) or "0"
    plusBlockSpaceOdds1 = get_capsule_value(plusBlockSpaceOdds1) or "0"
    plusBlockSpaceOdds2 = get_capsule_value(plusBlockSpaceOdds2) or "0"
    plusBlockSpaceOdds34 = get_capsule_value(plusBlockSpaceOdds34) or "0"
    minusBlockPrice1 = get_capsule_value(minusBlockPrice1) or "0"
    minusBlockPrice2 = get_capsule_value(minusBlockPrice2) or "0"
    minusBlockPrice34 = get_capsule_value(minusBlockPrice34) or "0"
    minusBlockShopOdds12 = get_capsule_value(minusBlockShopOdds12) or "0"
    minusBlockShopOdds34 = get_capsule_value(minusBlockShopOdds34) or "0"
    minusBlockSpaceOdds1 = get_capsule_value(minusBlockSpaceOdds1) or "0"
    minusBlockSpaceOdds2 = get_capsule_value(minusBlockSpaceOdds2) or "0"
    minusBlockSpaceOdds34 = get_capsule_value(minusBlockSpaceOdds34) or "0"
    speedBlockPrice1 = get_capsule_value(speedBlockPrice1) or "0"
    speedBlockPrice2 = get_capsule_value(speedBlockPrice2) or "0"
    speedBlockPrice34 = get_capsule_value(speedBlockPrice34) or "0"
    speedBlockShopOdds12 = get_capsule_value(speedBlockShopOdds12) or "0"
    speedBlockShopOdds34 = get_capsule_value(speedBlockShopOdds34) or "0"
    speedBlockSpaceOdds1 = get_capsule_value(speedBlockSpaceOdds1) or "0"
    speedBlockSpaceOdds2 = get_capsule_value(speedBlockSpaceOdds2) or "0"
    speedBlockSpaceOdds34 = get_capsule_value(speedBlockSpaceOdds34) or "0"
    slowBlockPrice1 = get_capsule_value(slowBlockPrice1) or "0"
    slowBlockPrice2 = get_capsule_value(slowBlockPrice2) or "0"
    slowBlockPrice34 = get_capsule_value(slowBlockPrice34) or "0"
    slowBlockShopOdds12 = get_capsule_value(slowBlockShopOdds12) or "0"
    slowBlockShopOdds34 = get_capsule_value(slowBlockShopOdds34) or "0"
    slowBlockSpaceOdds1 = get_capsule_value(slowBlockSpaceOdds1) or "0"
    slowBlockSpaceOdds2 = get_capsule_value(slowBlockSpaceOdds2) or "0"
    slowBlockSpaceOdds34 = get_capsule_value(slowBlockSpaceOdds34) or "0"
    bowserPhonePrice1 = get_capsule_value(bowserPhonePrice1) or "0"
    bowserPhonePrice2 = get_capsule_value(bowserPhonePrice2) or "0"
    bowserPhonePrice34 = get_capsule_value(bowserPhonePrice34) or "0"
    bowserPhoneShopOdds12 = get_capsule_value(bowserPhoneShopOdds12) or "0"
    bowserPhoneShopOdds34 = get_capsule_value(bowserPhoneShopOdds34) or "0"
    bowserPhoneSpaceOdds1 = get_capsule_value(bowserPhoneSpaceOdds1) or "0"
    bowserPhoneSpaceOdds2 = get_capsule_value(bowserPhoneSpaceOdds2) or "0"
    bowserPhoneSpaceOdds34 = get_capsule_value(bowserPhoneSpaceOdds34) or "0"
    doubleDipPrice1 = get_capsule_value(doubleDipPrice1) or "0"
    doubleDipPrice2 = get_capsule_value(doubleDipPrice2) or "0"
    doubleDipPrice34 = get_capsule_value(doubleDipPrice34) or "0"
    doubleDipShopOdds12 = get_capsule_value(doubleDipShopOdds12) or "0"
    doubleDipShopOdds34 = get_capsule_value(doubleDipShopOdds34) or "0"
    doubleDipSpaceOdds1 = get_capsule_value(doubleDipSpaceOdds1) or "0"
    doubleDipSpaceOdds2 = get_capsule_value(doubleDipSpaceOdds2) or "0"
    doubleDipSpaceOdds34 = get_capsule_value(doubleDipSpaceOdds34) or "0"
    hiddenBlockCardPrice1 = get_capsule_value(hiddenBlockCardPrice1) or "0"
    hiddenBlockCardPrice2 = get_capsule_value(hiddenBlockCardPrice2) or "0"
    hiddenBlockCardPrice34 = get_capsule_value(hiddenBlockCardPrice34) or "0"
    hiddenBlockCardShopOdds12 = get_capsule_value(hiddenBlockCardShopOdds12) or "0"
    hiddenBlockCardShopOdds34 = get_capsule_value(hiddenBlockCardShopOdds34) or "0"
    hiddenBlockCardSpaceOdds1 = get_capsule_value(hiddenBlockCardSpaceOdds1) or "0"
    hiddenBlockCardSpaceOdds2 = get_capsule_value(hiddenBlockCardSpaceOdds2) or "0"
    hiddenBlockCardSpaceOdds34 = get_capsule_value(hiddenBlockCardSpaceOdds34) or "0"
    barterBoxPrice1 = get_capsule_value(barterBoxPrice1) or "0"
    barterBoxPrice2 = get_capsule_value(barterBoxPrice2) or "0"
    barterBoxPrice34 = get_capsule_value(barterBoxPrice34) or "0"
    barterBoxShopOdds12 = get_capsule_value(barterBoxShopOdds12) or "0"
    barterBoxShopOdds34 = get_capsule_value(barterBoxShopOdds34) or "0"
    barterBoxSpaceOdds1 = get_capsule_value(barterBoxSpaceOdds1) or "0"
    barterBoxSpaceOdds2 = get_capsule_value(barterBoxSpaceOdds2) or "0"
    barterBoxSpaceOdds34 = get_capsule_value(barterBoxSpaceOdds34) or "0"
    superWarpPipePrice1 = get_capsule_value(superWarpPipePrice1) or "0"
    superWarpPipePrice2 = get_capsule_value(superWarpPipePrice2) or "0"
    superWarpPipePrice34 = get_capsule_value(superWarpPipePrice34) or "0"
    superWarpPipeShopOdds12 = get_capsule_value(superWarpPipeShopOdds12) or "0"
    superWarpPipeShopOdds34 = get_capsule_value(superWarpPipeShopOdds34) or "0"
    superWarpPipeSpaceOdds1 = get_capsule_value(superWarpPipeSpaceOdds1) or "0"
    superWarpPipeSpaceOdds2 = get_capsule_value(superWarpPipeSpaceOdds2) or "0"
    superWarpPipeSpaceOdds34 = get_capsule_value(superWarpPipeSpaceOdds34) or "0"
    chanceTimeCharmPrice1 = get_capsule_value(chanceTimeCharmPrice1) or "0"
    chanceTimeCharmPrice2 = get_capsule_value(chanceTimeCharmPrice2) or "0"
    chanceTimeCharmPrice34 = get_capsule_value(chanceTimeCharmPrice34) or "0"
    chanceTimeCharmShopOdds12 = get_capsule_value(chanceTimeCharmShopOdds12) or "0"
    chanceTimeCharmShopOdds34 = get_capsule_value(chanceTimeCharmShopOdds34) or "0"
    chanceTimeCharmSpaceOdds1 = get_capsule_value(chanceTimeCharmSpaceOdds1) or "0"
    chanceTimeCharmSpaceOdds2 = get_capsule_value(chanceTimeCharmSpaceOdds2) or "0"
    chanceTimeCharmSpaceOdds34 = get_capsule_value(chanceTimeCharmSpaceOdds34) or "0"
    wackyWatchPrice1 = get_capsule_value(wackyWatchPrice1) or "0"
    wackyWatchPrice2 = get_capsule_value(wackyWatchPrice2) or "0"
    wackyWatchPrice34 = get_capsule_value(wackyWatchPrice34) or "0"
    wackyWatchShopOdds12 = get_capsule_value(wackyWatchShopOdds12) or "0"
    wackyWatchShopOdds34 = get_capsule_value(wackyWatchShopOdds34) or "0"
    wackyWatchSpaceOdds1 = get_capsule_value(wackyWatchSpaceOdds1) or "0"
    wackyWatchSpaceOdds2 = get_capsule_value(wackyWatchSpaceOdds2) or "0"
    wackyWatchSpaceOdds34 = get_capsule_value(wackyWatchSpaceOdds34) or "0"

    # Weights lists
    shopOdds12 = [
        miniMushroomShopOdds12,
        megaMushroomShopOdds12,
        superMiniMushroomShopOdds12,
        superMegaMushroomShopOdds12,
        miniMegaHammerShopOdds12,
        warpPipeShopOdds12,
        swapCardShopOdds12,
        sparkyStickerShopOdds12,
        gaddlightShopOdds12,
        chompCallShopOdds12,
        bowserSuitShopOdds12,
        crystalBallShopOdds12,
        magicLampShopOdds12,
        itemBagShopOdds12,
        mushroomShopOdds12,
        goldenMushroomShopOdds12,
        reverseMushroomShopOdds12,
        poisonMushroomShopOdds12,
        triplePoisonMushroomShopOdds12,
        celluarShopperShopOdds12,
        skeletonKeyShopOdds12,
        plunderChestShopOdds12,
        gaddbrushShopOdds12,
        warpBlockShopOdds12,
        flyGuyShopOdds12,
        plusBlockShopOdds12,
        minusBlockShopOdds12,
        speedBlockShopOdds12,
        slowBlockShopOdds12,
        bowserPhoneShopOdds12,
        doubleDipShopOdds12,
        hiddenBlockCardShopOdds12,
        barterBoxShopOdds12,
        superWarpPipeShopOdds12,
        chanceTimeCharmShopOdds12,
        wackyWatchShopOdds12,
    ]

    shopOdds34 = [
        miniMushroomShopOdds34,
        megaMushroomShopOdds34,
        superMiniMushroomShopOdds34,
        superMegaMushroomShopOdds34,
        miniMegaHammerShopOdds34,
        warpPipeShopOdds34,
        swapCardShopOdds34,
        sparkyStickerShopOdds34,
        gaddlightShopOdds34,
        chompCallShopOdds34,
        bowserSuitShopOdds34,
        crystalBallShopOdds34,
        magicLampShopOdds34,
        itemBagShopOdds34,
        mushroomShopOdds34,
        goldenMushroomShopOdds34,
        reverseMushroomShopOdds34,
        poisonMushroomShopOdds34,
        triplePoisonMushroomShopOdds34,
        celluarShopperShopOdds34,
        skeletonKeyShopOdds34,
        plunderChestShopOdds34,
        gaddbrushShopOdds34,
        warpBlockShopOdds34,
        flyGuyShopOdds34,
        plusBlockShopOdds34,
        minusBlockShopOdds34,
        speedBlockShopOdds34,
        slowBlockShopOdds34,
        bowserPhoneShopOdds34,
        doubleDipShopOdds34,
        hiddenBlockCardShopOdds34,
        barterBoxShopOdds34,
        superWarpPipeShopOdds34,
        chanceTimeCharmShopOdds34,
        wackyWatchShopOdds34,
    ]

    spaceOdds1 = [
        miniMushroomSpaceOdds1,
        megaMushroomSpaceOdds1,
        superMiniMushroomSpaceOdds1,
        superMegaMushroomSpaceOdds1,
        miniMegaHammerSpaceOdds1,
        warpPipeSpaceOdds1,
        swapCardSpaceOdds1,
        sparkyStickerSpaceOdds1,
        gaddlightSpaceOdds1,
        chompCallSpaceOdds1,
        bowserSuitSpaceOdds1,
        crystalBallSpaceOdds1,
        magicLampSpaceOdds1,
        itemBagSpaceOdds1,
        mushroomSpaceOdds1,
        goldenMushroomSpaceOdds1,
        reverseMushroomSpaceOdds1,
        poisonMushroomSpaceOdds1,
        triplePoisonMushroomSpaceOdds1,
        celluarShopperSpaceOdds1,
        skeletonKeySpaceOdds1,
        plunderChestSpaceOdds1,
        gaddbrushSpaceOdds1,
        warpBlockSpaceOdds1,
        flyGuySpaceOdds1,
        plusBlockSpaceOdds1,
        minusBlockSpaceOdds1,
        speedBlockSpaceOdds1,
        slowBlockSpaceOdds1,
        bowserPhoneSpaceOdds1,
        doubleDipSpaceOdds1,
        hiddenBlockCardSpaceOdds1,
        barterBoxSpaceOdds1,
        superWarpPipeSpaceOdds1,
        chanceTimeCharmSpaceOdds1,
        wackyWatchSpaceOdds1,
    ]

    spaceOdds2 = [
        miniMushroomSpaceOdds2,
        megaMushroomSpaceOdds2,
        superMiniMushroomSpaceOdds2,
        superMegaMushroomSpaceOdds2,
        miniMegaHammerSpaceOdds2,
        warpPipeSpaceOdds2,
        swapCardSpaceOdds2,
        sparkyStickerSpaceOdds2,
        gaddlightSpaceOdds2,
        chompCallSpaceOdds2,
        bowserSuitSpaceOdds2,
        crystalBallSpaceOdds2,
        magicLampSpaceOdds2,
        itemBagSpaceOdds2,
        mushroomSpaceOdds2,
        goldenMushroomSpaceOdds2,
        reverseMushroomSpaceOdds2,
        poisonMushroomSpaceOdds2,
        triplePoisonMushroomSpaceOdds2,
        celluarShopperSpaceOdds2,
        skeletonKeySpaceOdds2,
        plunderChestSpaceOdds2,
        gaddbrushSpaceOdds2,
        warpBlockSpaceOdds2,
        flyGuySpaceOdds2,
        plusBlockSpaceOdds2,
        minusBlockSpaceOdds2,
        speedBlockSpaceOdds2,
        slowBlockSpaceOdds2,
        bowserPhoneSpaceOdds2,
        doubleDipSpaceOdds2,
        hiddenBlockCardSpaceOdds2,
        barterBoxSpaceOdds2,
        superWarpPipeSpaceOdds2,
        chanceTimeCharmSpaceOdds2,
        wackyWatchSpaceOdds2,
    ]

    spaceOdds34 = [
        miniMushroomSpaceOdds34,
        megaMushroomSpaceOdds34,
        superMiniMushroomSpaceOdds34,
        superMegaMushroomSpaceOdds34,
        miniMegaHammerSpaceOdds34,
        warpPipeSpaceOdds34,
        swapCardSpaceOdds34,
        sparkyStickerSpaceOdds34,
        gaddlightSpaceOdds34,
        chompCallSpaceOdds34,
        bowserSuitSpaceOdds34,
        crystalBallSpaceOdds34,
        magicLampSpaceOdds34,
        itemBagSpaceOdds34,
        mushroomSpaceOdds34,
        goldenMushroomSpaceOdds34,
        reverseMushroomSpaceOdds34,
        poisonMushroomSpaceOdds34,
        triplePoisonMushroomSpaceOdds34,
        celluarShopperSpaceOdds34,
        skeletonKeySpaceOdds34,
        plunderChestSpaceOdds34,
        gaddbrushSpaceOdds34,
        warpBlockSpaceOdds34,
        flyGuySpaceOdds34,
        plusBlockSpaceOdds34,
        minusBlockSpaceOdds34,
        speedBlockSpaceOdds34,
        slowBlockSpaceOdds34,
        bowserPhoneSpaceOdds34,
        doubleDipSpaceOdds34,
        hiddenBlockCardSpaceOdds34,
        barterBoxSpaceOdds34,
        superWarpPipeSpaceOdds34,
        chanceTimeCharmSpaceOdds34,
        wackyWatchSpaceOdds34,
    ]

    shopOdds12Weights = sum(int(weight) if weight else 0 for weight in shopOdds12)
    shopOdds34Weights = sum(int(weight) if weight else 0 for weight in shopOdds34)
    spaceOdds1Weights = sum(int(weight) if weight else 0 for weight in spaceOdds1)
    spaceOdds2Weights = sum(int(weight) if weight else 0 for weight in spaceOdds2)
    spaceOdds34Weights = sum(int(weight) if weight else 0 for weight in spaceOdds34)

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

    # Calculate weights for shop odds 34
    miniMushroomSpaceOdds34 = calculateWeight(miniMushroomSpaceOdds34, shopOdds34Weights)
    megaMushroomSpaceOdds34 = calculateWeight(megaMushroomSpaceOdds34, shopOdds34Weights)
    superMiniMushroomSpaceOdds34 = calculateWeight(superMiniMushroomSpaceOdds34, shopOdds34Weights)
    superMegaMushroomSpaceOdds34 = calculateWeight(superMegaMushroomSpaceOdds34, shopOdds34Weights)
    miniMegaHammerSpaceOdds34 = calculateWeight(miniMegaHammerSpaceOdds34, shopOdds34Weights)
    warpPipeSpaceOdds34 = calculateWeight(warpPipeSpaceOdds34, shopOdds34Weights)
    swapCardSpaceOdds34 = calculateWeight(swapCardSpaceOdds34, shopOdds34Weights)
    sparkyStickerSpaceOdds34 = calculateWeight(sparkyStickerSpaceOdds34, shopOdds34Weights)
    gaddlightSpaceOdds34 = calculateWeight(gaddlightSpaceOdds34, shopOdds34Weights)
    chompCallSpaceOdds34 = calculateWeight(chompCallSpaceOdds34, shopOdds34Weights)
    bowserSuitSpaceOdds34 = calculateWeight(bowserSuitSpaceOdds34, shopOdds34Weights)
    crystalBallSpaceOdds34 = calculateWeight(crystalBallSpaceOdds34, shopOdds34Weights)
    magicLampSpaceOdds34 = calculateWeight(magicLampSpaceOdds34, shopOdds34Weights)
    itemBagSpaceOdds34 = calculateWeight(itemBagSpaceOdds34, shopOdds34Weights)
    mushroomSpaceOdds34 = calculateWeight(mushroomSpaceOdds34, shopOdds34Weights)
    goldenMushroomSpaceOdds34 = calculateWeight(goldenMushroomSpaceOdds34, shopOdds34Weights)
    reverseMushroomSpaceOdds34 = calculateWeight(reverseMushroomSpaceOdds34, shopOdds34Weights)
    poisonMushroomSpaceOdds34 = calculateWeight(poisonMushroomSpaceOdds34, shopOdds34Weights)
    triplePoisonMushroomSpaceOdds34 = calculateWeight(triplePoisonMushroomSpaceOdds34, shopOdds34Weights)
    celluarShopperSpaceOdds34 = calculateWeight(celluarShopperSpaceOdds34, shopOdds34Weights)
    skeletonKeySpaceOdds34 = calculateWeight(skeletonKeySpaceOdds34, shopOdds34Weights)
    plunderChestSpaceOdds34 = calculateWeight(plunderChestSpaceOdds34, shopOdds34Weights)
    gaddbrushSpaceOdds34 = calculateWeight(gaddbrushSpaceOdds34, shopOdds34Weights)
    warpBlockSpaceOdds34 = calculateWeight(warpBlockSpaceOdds34, shopOdds34Weights)
    flyGuySpaceOdds34 = calculateWeight(flyGuySpaceOdds34, shopOdds34Weights)
    plusBlockSpaceOdds34 = calculateWeight(plusBlockSpaceOdds34, shopOdds34Weights)
    minusBlockSpaceOdds34 = calculateWeight(minusBlockSpaceOdds34, shopOdds34Weights)
    speedBlockSpaceOdds34 = calculateWeight(speedBlockSpaceOdds34, shopOdds34Weights)
    slowBlockSpaceOdds34 = calculateWeight(slowBlockSpaceOdds34, shopOdds34Weights)
    bowserPhoneSpaceOdds34 = calculateWeight(bowserPhoneSpaceOdds34, shopOdds34Weights)
    doubleDipSpaceOdds34 = calculateWeight(doubleDipSpaceOdds34, shopOdds34Weights)
    hiddenBlockCardSpaceOdds34 = calculateWeight(hiddenBlockCardSpaceOdds34, shopOdds34Weights)
    barterBoxSpaceOdds34 = calculateWeight(barterBoxSpaceOdds34, shopOdds34Weights)
    superWarpPipeSpaceOdds34 = calculateWeight(superWarpPipeSpaceOdds34, shopOdds34Weights)
    chanceTimeCharmSpaceOdds34 = calculateWeight(chanceTimeCharmSpaceOdds34, shopOdds34Weights)
    wackyWatchSpaceOdds34 = calculateWeight(wackyWatchSpaceOdds34, shopOdds34Weights)

    # Calculate weights for shop odds 12
    miniMushroomShopOdds12 = calculateWeight(miniMushroomShopOdds12, shopOdds12Weights)
    megaMushroomShopOdds12 = calculateWeight(megaMushroomShopOdds12, shopOdds12Weights)
    superMiniMushroomShopOdds12 = calculateWeight(superMiniMushroomShopOdds12, shopOdds12Weights)
    superMegaMushroomShopOdds12 = calculateWeight(superMegaMushroomShopOdds12, shopOdds12Weights)
    miniMegaHammerShopOdds12 = calculateWeight(miniMegaHammerShopOdds12, shopOdds12Weights)
    warpPipeShopOdds12 = calculateWeight(warpPipeShopOdds12, shopOdds12Weights)
    swapCardShopOdds12 = calculateWeight(swapCardShopOdds12, shopOdds12Weights)
    sparkyStickerShopOdds12 = calculateWeight(sparkyStickerShopOdds12, shopOdds12Weights)
    gaddlightShopOdds12 = calculateWeight(gaddlightShopOdds12, shopOdds12Weights)
    chompCallShopOdds12 = calculateWeight(chompCallShopOdds12, shopOdds12Weights)
    bowserSuitShopOdds12 = calculateWeight(bowserSuitShopOdds12, shopOdds12Weights)
    crystalBallShopOdds12 = calculateWeight(crystalBallShopOdds12, shopOdds12Weights)
    magicLampShopOdds12 = calculateWeight(magicLampShopOdds12, shopOdds12Weights)
    itemBagShopOdds12 = calculateWeight(itemBagShopOdds12, shopOdds12Weights)
    mushroomShopOdds12 = calculateWeight(mushroomShopOdds12, shopOdds12Weights)
    goldenMushroomShopOdds12 = calculateWeight(goldenMushroomShopOdds12, shopOdds12Weights)
    reverseMushroomShopOdds12 = calculateWeight(reverseMushroomShopOdds12, shopOdds12Weights)
    poisonMushroomShopOdds12 = calculateWeight(poisonMushroomShopOdds12, shopOdds12Weights)
    triplePoisonMushroomShopOdds12 = calculateWeight(triplePoisonMushroomShopOdds12, shopOdds12Weights)
    celluarShopperShopOdds12 = calculateWeight(celluarShopperShopOdds12, shopOdds12Weights)
    skeletonKeyShopOdds12 = calculateWeight(skeletonKeyShopOdds12, shopOdds12Weights)
    plunderChestShopOdds12 = calculateWeight(plunderChestShopOdds12, shopOdds12Weights)
    gaddbrushShopOdds12 = calculateWeight(gaddbrushShopOdds12, shopOdds12Weights)
    warpBlockShopOdds12 = calculateWeight(warpBlockShopOdds12, shopOdds12Weights)
    flyGuyShopOdds12 = calculateWeight(flyGuyShopOdds12, shopOdds12Weights)
    plusBlockShopOdds12 = calculateWeight(plusBlockShopOdds12, shopOdds12Weights)
    minusBlockShopOdds12 = calculateWeight(minusBlockShopOdds12, shopOdds12Weights)
    speedBlockShopOdds12 = calculateWeight(speedBlockShopOdds12, shopOdds12Weights)
    slowBlockShopOdds12 = calculateWeight(slowBlockShopOdds12, shopOdds12Weights)
    bowserPhoneShopOdds12 = calculateWeight(bowserPhoneShopOdds12, shopOdds12Weights)
    doubleDipShopOdds12 = calculateWeight(doubleDipShopOdds12, shopOdds12Weights)
    hiddenBlockCardShopOdds12 = calculateWeight(hiddenBlockCardShopOdds12, shopOdds12Weights)
    barterBoxShopOdds12 = calculateWeight(barterBoxShopOdds12, shopOdds12Weights)
    superWarpPipeShopOdds12 = calculateWeight(superWarpPipeShopOdds12, shopOdds12Weights)
    chanceTimeCharmShopOdds12 = calculateWeight(chanceTimeCharmShopOdds12, shopOdds12Weights)
    wackyWatchShopOdds12 = calculateWeight(wackyWatchShopOdds12, shopOdds12Weights)

   # Calculate weights for space odds 1
    miniMushroomSpaceOdds1 = calculateWeight(miniMushroomSpaceOdds1, spaceOdds1Weights)
    megaMushroomSpaceOdds1 = calculateWeight(megaMushroomSpaceOdds1, spaceOdds1Weights)
    superMiniMushroomSpaceOdds1 = calculateWeight(superMiniMushroomSpaceOdds1, spaceOdds1Weights)
    superMegaMushroomSpaceOdds1 = calculateWeight(superMegaMushroomSpaceOdds1, spaceOdds1Weights)
    miniMegaHammerSpaceOdds1 = calculateWeight(miniMegaHammerSpaceOdds1, spaceOdds1Weights)
    warpPipeSpaceOdds1 = calculateWeight(warpPipeSpaceOdds1, spaceOdds1Weights)
    swapCardSpaceOdds1 = calculateWeight(swapCardSpaceOdds1, spaceOdds1Weights)
    sparkyStickerSpaceOdds1 = calculateWeight(sparkyStickerSpaceOdds1, spaceOdds1Weights)
    gaddlightSpaceOdds1 = calculateWeight(gaddlightSpaceOdds1, spaceOdds1Weights)
    chompCallSpaceOdds1 = calculateWeight(chompCallSpaceOdds1, spaceOdds1Weights)
    bowserSuitSpaceOdds1 = calculateWeight(bowserSuitSpaceOdds1, spaceOdds1Weights)
    crystalBallSpaceOdds1 = calculateWeight(crystalBallSpaceOdds1, spaceOdds1Weights)
    magicLampSpaceOdds1 = calculateWeight(magicLampSpaceOdds1, spaceOdds1Weights)
    itemBagSpaceOdds1 = calculateWeight(itemBagSpaceOdds1, spaceOdds1Weights)
    mushroomSpaceOdds1 = calculateWeight(mushroomSpaceOdds1, spaceOdds1Weights)
    goldenMushroomSpaceOdds1 = calculateWeight(goldenMushroomSpaceOdds1, spaceOdds1Weights)
    reverseMushroomSpaceOdds1 = calculateWeight(reverseMushroomSpaceOdds1, spaceOdds1Weights)
    poisonMushroomSpaceOdds1 = calculateWeight(poisonMushroomSpaceOdds1, spaceOdds1Weights)
    triplePoisonMushroomSpaceOdds1 = calculateWeight(triplePoisonMushroomSpaceOdds1, spaceOdds1Weights)
    celluarShopperSpaceOdds1 = calculateWeight(celluarShopperSpaceOdds1, spaceOdds1Weights)
    skeletonKeySpaceOdds1 = calculateWeight(skeletonKeySpaceOdds1, spaceOdds1Weights)
    plunderChestSpaceOdds1 = calculateWeight(plunderChestSpaceOdds1, spaceOdds1Weights)
    gaddbrushSpaceOdds1 = calculateWeight(gaddbrushSpaceOdds1, spaceOdds1Weights)
    warpBlockSpaceOdds1 = calculateWeight(warpBlockSpaceOdds1, spaceOdds1Weights)
    flyGuySpaceOdds1 = calculateWeight(flyGuySpaceOdds1, spaceOdds1Weights)
    plusBlockSpaceOdds1 = calculateWeight(plusBlockSpaceOdds1, spaceOdds1Weights)
    minusBlockSpaceOdds1 = calculateWeight(minusBlockSpaceOdds1, spaceOdds1Weights)
    speedBlockSpaceOdds1 = calculateWeight(speedBlockSpaceOdds1, spaceOdds1Weights)
    slowBlockSpaceOdds1 = calculateWeight(slowBlockSpaceOdds1, spaceOdds1Weights)
    bowserPhoneSpaceOdds1 = calculateWeight(bowserPhoneSpaceOdds1, spaceOdds1Weights)
    doubleDipSpaceOdds1 = calculateWeight(doubleDipSpaceOdds1, spaceOdds1Weights)
    hiddenBlockCardSpaceOdds1 = calculateWeight(hiddenBlockCardSpaceOdds1, spaceOdds1Weights)
    barterBoxSpaceOdds1 = calculateWeight(barterBoxSpaceOdds1, spaceOdds1Weights)
    superWarpPipeSpaceOdds1 = calculateWeight(superWarpPipeSpaceOdds1, spaceOdds1Weights)
    chanceTimeCharmSpaceOdds1 = calculateWeight(chanceTimeCharmSpaceOdds1, spaceOdds1Weights)

    # Calculate weights for space odds 2
    miniMushroomSpaceOdds2 = calculateWeight(miniMushroomSpaceOdds2, spaceOdds2Weights)
    megaMushroomSpaceOdds2 = calculateWeight(megaMushroomSpaceOdds2, spaceOdds2Weights)
    superMiniMushroomSpaceOdds2 = calculateWeight(superMiniMushroomSpaceOdds2, spaceOdds2Weights)
    superMegaMushroomSpaceOdds2 = calculateWeight(superMegaMushroomSpaceOdds2, spaceOdds2Weights)
    miniMegaHammerSpaceOdds2 = calculateWeight(miniMegaHammerSpaceOdds2, spaceOdds2Weights)
    warpPipeSpaceOdds2 = calculateWeight(warpPipeSpaceOdds2, spaceOdds2Weights)
    swapCardSpaceOdds2 = calculateWeight(swapCardSpaceOdds2, spaceOdds2Weights)
    sparkyStickerSpaceOdds2 = calculateWeight(sparkyStickerSpaceOdds2, spaceOdds2Weights)
    gaddlightSpaceOdds2 = calculateWeight(gaddlightSpaceOdds2, spaceOdds2Weights)
    chompCallSpaceOdds2 = calculateWeight(chompCallSpaceOdds2, spaceOdds2Weights)
    bowserSuitSpaceOdds2 = calculateWeight(bowserSuitSpaceOdds2, spaceOdds2Weights)
    crystalBallSpaceOdds2 = calculateWeight(crystalBallSpaceOdds2, spaceOdds2Weights)
    magicLampSpaceOdds2 = calculateWeight(magicLampSpaceOdds2, spaceOdds2Weights)
    itemBagSpaceOdds2 = calculateWeight(itemBagSpaceOdds2, spaceOdds2Weights)
    mushroomSpaceOdds2 = calculateWeight(mushroomSpaceOdds2, spaceOdds2Weights)
    reverseMushroomSpaceOdds2 = calculateWeight(reverseMushroomSpaceOdds2, spaceOdds2Weights)
    poisonMushroomSpaceOdds2 = calculateWeight(poisonMushroomSpaceOdds2, spaceOdds2Weights)
    triplePoisonMushroomSpaceOdds2 = calculateWeight(triplePoisonMushroomSpaceOdds2, spaceOdds2Weights)
    celluarShopperSpaceOdds2 = calculateWeight(celluarShopperSpaceOdds2, spaceOdds2Weights)
    skeletonKeySpaceOdds2 = calculateWeight(skeletonKeySpaceOdds2, spaceOdds2Weights)
    plunderChestSpaceOdds2 = calculateWeight(plunderChestSpaceOdds2, spaceOdds2Weights)
    gaddbrushSpaceOdds2 = calculateWeight(gaddbrushSpaceOdds2, spaceOdds2Weights)
    warpBlockSpaceOdds2 = calculateWeight(warpBlockSpaceOdds2, spaceOdds2Weights)
    flyGuySpaceOdds2 = calculateWeight(flyGuySpaceOdds2, spaceOdds2Weights)
    plusBlockSpaceOdds2 = calculateWeight(plusBlockSpaceOdds2, spaceOdds2Weights)
    minusBlockSpaceOdds2 = calculateWeight(minusBlockSpaceOdds2, spaceOdds2Weights)
    speedBlockSpaceOdds2 = calculateWeight(speedBlockSpaceOdds2, spaceOdds2Weights)
    slowBlockSpaceOdds2 = calculateWeight(slowBlockSpaceOdds2, spaceOdds2Weights)
    bowserPhoneSpaceOdds2 = calculateWeight(bowserPhoneSpaceOdds2, spaceOdds2Weights)
    doubleDipSpaceOdds2 = calculateWeight(doubleDipSpaceOdds2, spaceOdds2Weights)
    hiddenBlockCardSpaceOdds2 = calculateWeight(hiddenBlockCardSpaceOdds2, spaceOdds2Weights)
    barterBoxSpaceOdds2 = calculateWeight(barterBoxSpaceOdds2, spaceOdds2Weights)
    superWarpPipeSpaceOdds2 = calculateWeight(superWarpPipeSpaceOdds2, spaceOdds2Weights)
    chanceTimeCharmSpaceOdds2 = calculateWeight(chanceTimeCharmSpaceOdds2, spaceOdds2Weights)
    wackyWatchSpaceOdds2 = calculateWeight(wackyWatchSpaceOdds2, spaceOdds2Weights)

    # Calculate weights for space odds 34
    miniMushroomSpaceOdds34 = calculateWeight(miniMushroomSpaceOdds34, spaceOdds34Weights)
    megaMushroomSpaceOdds34 = calculateWeight(megaMushroomSpaceOdds34, spaceOdds34Weights)
    superMiniMushroomSpaceOdds34 = calculateWeight(superMiniMushroomSpaceOdds34, spaceOdds34Weights)
    superMegaMushroomSpaceOdds34 = calculateWeight(superMegaMushroomSpaceOdds34, spaceOdds34Weights)
    miniMegaHammerSpaceOdds34 = calculateWeight(miniMegaHammerSpaceOdds34, spaceOdds34Weights)
    warpPipeSpaceOdds34 = calculateWeight(warpPipeSpaceOdds34, spaceOdds34Weights)
    swapCardSpaceOdds34 = calculateWeight(swapCardSpaceOdds34, spaceOdds34Weights)
    sparkyStickerSpaceOdds34 = calculateWeight(sparkyStickerSpaceOdds34, spaceOdds34Weights)
    gaddlightSpaceOdds34 = calculateWeight(gaddlightSpaceOdds34, spaceOdds34Weights)
    chompCallSpaceOdds34 = calculateWeight(chompCallSpaceOdds34, spaceOdds34Weights)
    bowserSuitSpaceOdds34 = calculateWeight(bowserSuitSpaceOdds34, spaceOdds34Weights)
    crystalBallSpaceOdds34 = calculateWeight(crystalBallSpaceOdds34, spaceOdds34Weights)
    magicLampSpaceOdds34 = calculateWeight(magicLampSpaceOdds34, spaceOdds34Weights)
    itemBagSpaceOdds34 = calculateWeight(itemBagSpaceOdds34, spaceOdds34Weights)
    mushroomSpaceOdds34 = calculateWeight(mushroomSpaceOdds34, spaceOdds34Weights)
    goldenMushroomSpaceOdds34 = calculateWeight(goldenMushroomSpaceOdds34, spaceOdds34Weights)
    reverseMushroomSpaceOdds34 = calculateWeight(reverseMushroomSpaceOdds34, spaceOdds34Weights)
    poisonMushroomSpaceOdds34 = calculateWeight(poisonMushroomSpaceOdds34, spaceOdds34Weights)
    triplePoisonMushroomSpaceOdds34 = calculateWeight(triplePoisonMushroomSpaceOdds34, spaceOdds34Weights)
    celluarShopperSpaceOdds34 = calculateWeight(celluarShopperSpaceOdds34, spaceOdds34Weights)
    skeletonKeySpaceOdds34 = calculateWeight(skeletonKeySpaceOdds34, spaceOdds34Weights)
    plunderChestSpaceOdds34 = calculateWeight(plunderChestSpaceOdds34, spaceOdds34Weights)
    gaddbrushSpaceOdds34 = calculateWeight(gaddbrushSpaceOdds34, spaceOdds34Weights)
    warpBlockSpaceOdds34 = calculateWeight(warpBlockSpaceOdds34, spaceOdds34Weights)
    flyGuySpaceOdds34 = calculateWeight(flyGuySpaceOdds34, spaceOdds34Weights)
    plusBlockSpaceOdds34 = calculateWeight(plusBlockSpaceOdds34, spaceOdds34Weights)
    minusBlockSpaceOdds34 = calculateWeight(minusBlockSpaceOdds34, spaceOdds34Weights)
    speedBlockSpaceOdds34 = calculateWeight(speedBlockSpaceOdds34, spaceOdds34Weights)
    slowBlockSpaceOdds34 = calculateWeight(slowBlockSpaceOdds34, spaceOdds34Weights)
    bowserPhoneSpaceOdds34 = calculateWeight(bowserPhoneSpaceOdds34, spaceOdds34Weights)
    doubleDipSpaceOdds34 = calculateWeight(doubleDipSpaceOdds34, spaceOdds34Weights)
    hiddenBlockCardSpaceOdds34 = calculateWeight(hiddenBlockCardSpaceOdds34, spaceOdds34Weights)
    barterBoxSpaceOdds34 = calculateWeight(barterBoxSpaceOdds34, spaceOdds34Weights)
    superWarpPipeSpaceOdds34 = calculateWeight(superWarpPipeSpaceOdds34, spaceOdds34Weights)
    chanceTimeCharmSpaceOdds34 = calculateWeight(chanceTimeCharmSpaceOdds34, spaceOdds34Weights)
    wackyWatchSpaceOdds34 = calculateWeight(wackyWatchSpaceOdds34, spaceOdds34Weights)

    # Redefine Weights lists
    shopOdds12 = [
        miniMushroomShopOdds12,
        megaMushroomShopOdds12,
        superMiniMushroomShopOdds12,
        superMegaMushroomShopOdds12,
        miniMegaHammerShopOdds12,
        warpPipeShopOdds12,
        swapCardShopOdds12,
        sparkyStickerShopOdds12,
        gaddlightShopOdds12,
        chompCallShopOdds12,
        bowserSuitShopOdds12,
        crystalBallShopOdds12,
        magicLampShopOdds12,
        itemBagShopOdds12,
        mushroomShopOdds12,
        goldenMushroomShopOdds12,
        reverseMushroomShopOdds12,
        poisonMushroomShopOdds12,
        triplePoisonMushroomShopOdds12,
        celluarShopperShopOdds12,
        skeletonKeyShopOdds12,
        plunderChestShopOdds12,
        gaddbrushShopOdds12,
        warpBlockShopOdds12,
        flyGuyShopOdds12,
        plusBlockShopOdds12,
        minusBlockShopOdds12,
        speedBlockShopOdds12,
        slowBlockShopOdds12,
        bowserPhoneShopOdds12,
        doubleDipShopOdds12,
        hiddenBlockCardShopOdds12,
        barterBoxShopOdds12,
        superWarpPipeShopOdds12,
        chanceTimeCharmShopOdds12,
        wackyWatchShopOdds12,
    ]

    shopOdds34 = [
        miniMushroomShopOdds34,
        megaMushroomShopOdds34,
        superMiniMushroomShopOdds34,
        superMegaMushroomShopOdds34,
        miniMegaHammerShopOdds34,
        warpPipeShopOdds34,
        swapCardShopOdds34,
        sparkyStickerShopOdds34,
        gaddlightShopOdds34,
        chompCallShopOdds34,
        bowserSuitShopOdds34,
        crystalBallShopOdds34,
        magicLampShopOdds34,
        itemBagShopOdds34,
        mushroomShopOdds34,
        goldenMushroomShopOdds34,
        reverseMushroomShopOdds34,
        poisonMushroomShopOdds34,
        triplePoisonMushroomShopOdds34,
        celluarShopperShopOdds34,
        skeletonKeyShopOdds34,
        plunderChestShopOdds34,
        gaddbrushShopOdds34,
        warpBlockShopOdds34,
        flyGuyShopOdds34,
        plusBlockShopOdds34,
        minusBlockShopOdds34,
        speedBlockShopOdds34,
        slowBlockShopOdds34,
        bowserPhoneShopOdds34,
        doubleDipShopOdds34,
        hiddenBlockCardShopOdds34,
        barterBoxShopOdds34,
        superWarpPipeShopOdds34,
        chanceTimeCharmShopOdds34,
        wackyWatchShopOdds34,
    ]

    spaceOdds1 = [
        miniMushroomSpaceOdds1,
        megaMushroomSpaceOdds1,
        superMiniMushroomSpaceOdds1,
        superMegaMushroomSpaceOdds1,
        miniMegaHammerSpaceOdds1,
        warpPipeSpaceOdds1,
        swapCardSpaceOdds1,
        sparkyStickerSpaceOdds1,
        gaddlightSpaceOdds1,
        chompCallSpaceOdds1,
        bowserSuitSpaceOdds1,
        crystalBallSpaceOdds1,
        magicLampSpaceOdds1,
        itemBagSpaceOdds1,
        mushroomSpaceOdds1,
        goldenMushroomSpaceOdds1,
        reverseMushroomSpaceOdds1,
        poisonMushroomSpaceOdds1,
        triplePoisonMushroomSpaceOdds1,
        celluarShopperSpaceOdds1,
        skeletonKeySpaceOdds1,
        plunderChestSpaceOdds1,
        gaddbrushSpaceOdds1,
        warpBlockSpaceOdds1,
        flyGuySpaceOdds1,
        plusBlockSpaceOdds1,
        minusBlockSpaceOdds1,
        speedBlockSpaceOdds1,
        slowBlockSpaceOdds1,
        bowserPhoneSpaceOdds1,
        doubleDipSpaceOdds1,
        hiddenBlockCardSpaceOdds1,
        barterBoxSpaceOdds1,
        superWarpPipeSpaceOdds1,
        chanceTimeCharmSpaceOdds1,
        wackyWatchSpaceOdds1,
    ]

    spaceOdds2 = [
        miniMushroomSpaceOdds2,
        megaMushroomSpaceOdds2,
        superMiniMushroomSpaceOdds2,
        superMegaMushroomSpaceOdds2,
        miniMegaHammerSpaceOdds2,
        warpPipeSpaceOdds2,
        swapCardSpaceOdds2,
        sparkyStickerSpaceOdds2,
        gaddlightSpaceOdds2,
        chompCallSpaceOdds2,
        bowserSuitSpaceOdds2,
        crystalBallSpaceOdds2,
        magicLampSpaceOdds2,
        itemBagSpaceOdds2,
        mushroomSpaceOdds2,
        goldenMushroomSpaceOdds2,
        reverseMushroomSpaceOdds2,
        poisonMushroomSpaceOdds2,
        triplePoisonMushroomSpaceOdds2,
        celluarShopperSpaceOdds2,
        skeletonKeySpaceOdds2,
        plunderChestSpaceOdds2,
        gaddbrushSpaceOdds2,
        warpBlockSpaceOdds2,
        flyGuySpaceOdds2,
        plusBlockSpaceOdds2,
        minusBlockSpaceOdds2,
        speedBlockSpaceOdds2,
        slowBlockSpaceOdds2,
        bowserPhoneSpaceOdds2,
        doubleDipSpaceOdds2,
        hiddenBlockCardSpaceOdds2,
        barterBoxSpaceOdds2,
        superWarpPipeSpaceOdds2,
        chanceTimeCharmSpaceOdds2,
        wackyWatchSpaceOdds2,
    ]

    spaceOdds34 = [
        miniMushroomSpaceOdds34,
        megaMushroomSpaceOdds34,
        superMiniMushroomSpaceOdds34,
        superMegaMushroomSpaceOdds34,
        miniMegaHammerSpaceOdds34,
        warpPipeSpaceOdds34,
        swapCardSpaceOdds34,
        sparkyStickerSpaceOdds34,
        gaddlightSpaceOdds34,
        chompCallSpaceOdds34,
        bowserSuitSpaceOdds34,
        crystalBallSpaceOdds34,
        magicLampSpaceOdds34,
        itemBagSpaceOdds34,
        mushroomSpaceOdds34,
        goldenMushroomSpaceOdds34,
        reverseMushroomSpaceOdds34,
        poisonMushroomSpaceOdds34,
        triplePoisonMushroomSpaceOdds34,
        celluarShopperSpaceOdds34,
        skeletonKeySpaceOdds34,
        plunderChestSpaceOdds34,
        gaddbrushSpaceOdds34,
        warpBlockSpaceOdds34,
        flyGuySpaceOdds34,
        plusBlockSpaceOdds34,
        minusBlockSpaceOdds34,
        speedBlockSpaceOdds34,
        slowBlockSpaceOdds34,
        bowserPhoneSpaceOdds34,
        doubleDipSpaceOdds34,
        hiddenBlockCardSpaceOdds34,
        barterBoxSpaceOdds34,
        superWarpPipeSpaceOdds34,
        chanceTimeCharmSpaceOdds34,
        wackyWatchSpaceOdds34,
    ]

    shopOdds12Weights = sum(int(weight) for weight in shopOdds12 if weight)
    shopOdds34Weights = sum(int(weight) for weight in shopOdds34 if weight)
    spaceOdds1Weights = sum(int(weight) for weight in spaceOdds1 if weight)
    spaceOdds2Weights = sum(int(weight) for weight in spaceOdds2 if weight)
    spaceOdds34Weights = sum(int(weight) for weight in spaceOdds34 if weight)

    if int(spaceOdds1Weights) < 101:
        spaceOdds1Max = max(zip(spaceOdds1, spaceOdds1), key=lambda tuple: int(tuple[1]))[0]

    if int(spaceOdds34Weights) < 101:
        spaceOdds34Max = max(zip(spaceOdds34, spaceOdds34), key=lambda tuple: int(tuple[1]))[0]

    if int(shopOdds12Weights) < 101:
        shopOdds12Max = max(zip(shopOdds12, shopOdds12), key=lambda tuple: int(tuple[1]))[0]

    if int(spaceOdds2Weights) < 101:
        spaceOdds2Max = max(zip(spaceOdds2, spaceOdds2), key=lambda tuple: int(tuple[1]))[0]

    if int(shopOdds34Weights) < 101:
        shopOdds34Max = max(zip(shopOdds34, shopOdds34), key=lambda tuple: int(tuple[1]))[0]

    if shopOdds12Max == 'miniMushroomShopOdds12':
        miniMushroomShopOdds12 += (100 - miniMushroomShopOdds12)

    if shopOdds12Max == 'megaMushroomShopOdds12':
        megaMushroomShopOdds12 += (100 - megaMushroomShopOdds12)

    if shopOdds12Max == 'superMiniMushroomShopOdds12':
        superMiniMushroomShopOdds12 += (100 - superMiniMushroomShopOdds12)

    if shopOdds12Max == 'superMegaMushroomShopOdds12':
        superMegaMushroomShopOdds12 += (100 - superMegaMushroomShopOdds12)

    if shopOdds12Max == 'miniMegaHammerShopOdds12':
        miniMegaHammerShopOdds12 += (100 - miniMegaHammerShopOdds12)

    if shopOdds12Max == 'warpPipeShopOdds12':
        warpPipeShopOdds12 += (100 - warpPipeShopOdds12)

    if shopOdds12Max == 'swapCardShopOdds12':
        swapCardShopOdds12 += (100 - swapCardShopOdds12)

    if shopOdds12Max == 'sparkyStickerShopOdds12':
        sparkyStickerShopOdds12 += (100 - sparkyStickerShopOdds12)

    if shopOdds12Max == 'gaddlightShopOdds12':
        gaddlightShopOdds12 += (100 - gaddlightShopOdds12)

    if shopOdds12Max == 'chompCallShopOdds12':
        chompCallShopOdds12 += (100 - chompCallShopOdds12)

    if shopOdds12Max == 'bowserSuitShopOdds12':
        bowserSuitShopOdds12 += (100 - bowserSuitShopOdds12)

    if shopOdds12Max == 'crystalBallShopOdds12':
        crystalBallShopOdds12 += (100 - crystalBallShopOdds12)

    if shopOdds12Max == 'magicLampShopOdds12':
        magicLampShopOdds12 += (100 - magicLampShopOdds12)

    if shopOdds12Max == 'itemBagShopOdds12':
        itemBagShopOdds12 += (100 - itemBagShopOdds12)

    if shopOdds12Max == 'mushroomShopOdds12':
        mushroomShopOdds12 += (100 - mushroomShopOdds12)

    if shopOdds12Max == 'goldenMushroomShopOdds12':
        goldenMushroomShopOdds12 += (100 - goldenMushroomShopOdds12)

    if shopOdds12Max == 'reverseMushroomShopOdds12':
        reverseMushroomShopOdds12 += (100 - reverseMushroomShopOdds12)

    if shopOdds12Max == 'poisonMushroomShopOdds12':
        poisonMushroomShopOdds12 += (100 - poisonMushroomShopOdds12)

    if shopOdds12Max == 'triplePoisonMushroomShopOdds12':
        triplePoisonMushroomShopOdds12 += (100 - triplePoisonMushroomShopOdds12)

    if shopOdds12Max == 'celluarShopperShopOdds12':
        celluarShopperShopOdds12 += (100 - celluarShopperShopOdds12)

    if shopOdds12Max == 'skeletonKeyShopOdds12':
        skeletonKeyShopOdds12 += (100 - skeletonKeyShopOdds12)

    if shopOdds12Max == 'plunderChestShopOdds12':
        plunderChestShopOdds12 += (100 - plunderChestShopOdds12)

    if shopOdds12Max == 'gaddbrushShopOdds12':
        gaddbrushShopOdds12 += (100 - gaddbrushShopOdds12)

    if shopOdds12Max == 'warpBlockShopOdds12':
        warpBlockShopOdds12 += (100 - warpBlockShopOdds12)

    if shopOdds12Max == 'flyGuyShopOdds12':
        flyGuyShopOdds12 += (100 - flyGuyShopOdds12)

    if shopOdds12Max == 'plusBlockShopOdds12':
        plusBlockShopOdds12 += (100 - plusBlockShopOdds12)

    if shopOdds12Max == 'minusBlockShopOdds12':
        minusBlockShopOdds12 += (100 - minusBlockShopOdds12)

    if shopOdds12Max == 'speedBlockShopOdds12':
        speedBlockShopOdds12 += (100 - speedBlockShopOdds12)

    if shopOdds12Max == 'slowBlockShopOdds12':
        slowBlockShopOdds12 += (100 - slowBlockShopOdds12)

    if shopOdds12Max == 'bowserPhoneShopOdds12':
        bowserPhoneShopOdds12 += (100 - bowserPhoneShopOdds12)

    if shopOdds12Max == 'doubleDipShopOdds12':
        doubleDipShopOdds12 += (100 - doubleDipShopOdds12)

    if shopOdds12Max == 'hiddenBlockCardShopOdds12':
        hiddenBlockCardShopOdds12 += (100 - hiddenBlockCardShopOdds12)

    if shopOdds12Max == 'barterBoxShopOdds12':
        barterBoxShopOdds12 += (100 - barterBoxShopOdds12)

    if shopOdds12Max == 'superWarpPipeShopOdds12':
        superWarpPipeShopOdds12 += (100 - superWarpPipeShopOdds12)

    if shopOdds12Max == 'chanceTimeCharmShopOdds12':
        chanceTimeCharmShopOdds12 += (100 - chanceTimeCharmShopOdds12)

    if shopOdds12Max == 'wackyWatchShopOdds12':
        wackyWatchShopOdds12 += (100 - wackyWatchShopOdds12)

    if shopOdds34Max == 'miniMushroomShopOdds34':
        miniMushroomShopOdds34 += (100 - miniMushroomShopOdds34)

    if shopOdds34Max == 'megaMushroomShopOdds34':
        megaMushroomShopOdds34 += (100 - megaMushroomShopOdds34)

    if shopOdds34Max == 'superMiniMushroomShopOdds34':
        superMiniMushroomShopOdds34 += (100 - superMiniMushroomShopOdds34)

    if shopOdds34Max == 'superMegaMushroomShopOdds34':
        superMegaMushroomShopOdds34 += (100 - superMegaMushroomShopOdds34)

    if shopOdds34Max == 'miniMegaHammerShopOdds34':
        miniMegaHammerShopOdds34 += (100 - miniMegaHammerShopOdds34)

    if shopOdds34Max == 'warpPipeShopOdds34':
        warpPipeShopOdds34 += (100 - warpPipeShopOdds34)

    if shopOdds34Max == 'swapCardShopOdds34':
        swapCardShopOdds34 += (100 - swapCardShopOdds34)

    if shopOdds34Max == 'sparkyStickerShopOdds34':
        sparkyStickerShopOdds34 += (100 - sparkyStickerShopOdds34)

    if shopOdds34Max == 'gaddlightShopOdds34':
        gaddlightShopOdds34 += (100 - gaddlightShopOdds34)

    if shopOdds34Max == 'chompCallShopOdds34':
        chompCallShopOdds34 += (100 - chompCallShopOdds34)

    if shopOdds34Max == 'bowserSuitShopOdds34':
        bowserSuitShopOdds34 += (100 - bowserSuitShopOdds34)

    if shopOdds34Max == 'crystalBallShopOdds34':
        crystalBallShopOdds34 += (100 - crystalBallShopOdds34)

    if shopOdds34Max == 'magicLampShopOdds34':
        magicLampShopOdds34 += (100 - magicLampShopOdds34)

    if shopOdds34Max == 'itemBagShopOdds34':
        itemBagShopOdds34 += (100 - itemBagShopOdds34)

    if shopOdds34Max == 'mushroomShopOdds34':
        mushroomShopOdds34 += (100 - mushroomShopOdds34)

    if shopOdds34Max == 'goldenMushroomShopOdds34':
        goldenMushroomShopOdds34 += (100 - goldenMushroomShopOdds34)

    if shopOdds34Max == 'reverseMushroomShopOdds34':
        reverseMushroomShopOdds34 += (100 - reverseMushroomShopOdds34)

    if shopOdds34Max == 'poisonMushroomShopOdds34':
        poisonMushroomShopOdds34 += (100 - poisonMushroomShopOdds34)

    if shopOdds34Max == 'triplePoisonMushroomShopOdds34':
        triplePoisonMushroomShopOdds34 += (100 - triplePoisonMushroomShopOdds34)

    if shopOdds34Max == 'celluarShopperShopOdds34':
        celluarShopperShopOdds34 += (100 - celluarShopperShopOdds34)

    if shopOdds34Max == 'skeletonKeyShopOdds34':
        skeletonKeyShopOdds34 += (100 - skeletonKeyShopOdds34)

    if shopOdds34Max == 'plunderChestShopOdds34':
        plunderChestShopOdds34 += (100 - plunderChestShopOdds34)

    if shopOdds34Max == 'gaddbrushShopOdds34':
        gaddbrushShopOdds34 += (100 - gaddbrushShopOdds34)

    if shopOdds34Max == 'warpBlockShopOdds34':
        warpBlockShopOdds34 += (100 - warpBlockShopOdds34)

    if shopOdds34Max == 'flyGuyShopOdds34':
        flyGuyShopOdds34 += (100 - flyGuyShopOdds34)

    if shopOdds34Max == 'plusBlockShopOdds34':
        plusBlockShopOdds34 += (100 - plusBlockShopOdds34)

    if shopOdds34Max == 'minusBlockShopOdds34':
        minusBlockShopOdds34 += (100 - minusBlockShopOdds34)

    if shopOdds34Max == 'speedBlockShopOdds34':
        speedBlockShopOdds34 += (100 - speedBlockShopOdds34)

    if shopOdds34Max == 'slowBlockShopOdds34':
        slowBlockShopOdds34 += (100 - slowBlockShopOdds34)

    if shopOdds34Max == 'bowserPhoneShopOdds34':
        bowserPhoneShopOdds34 += (100 - bowserPhoneShopOdds34)

    if shopOdds34Max == 'doubleDipShopOdds34':
        doubleDipShopOdds34 += (100 - doubleDipShopOdds34)

    if shopOdds34Max == 'hiddenBlockCardShopOdds34':
        hiddenBlockCardShopOdds34 += (100 - hiddenBlockCardShopOdds34)

    if shopOdds34Max == 'barterBoxShopOdds34':
        barterBoxShopOdds34 += (100 - barterBoxShopOdds34)

    if shopOdds34Max == 'superWarpPipeShopOdds34':
        superWarpPipeShopOdds34 += (100 - superWarpPipeShopOdds34)

    if shopOdds34Max == 'chanceTimeCharmShopOdds34':
        chanceTimeCharmShopOdds34 += (100 - chanceTimeCharmShopOdds34)

    if shopOdds34Max == 'wackyWatchShopOdds34':
        wackyWatchShopOdds34 += (100 - wackyWatchShopOdds34)

    if spaceOdds1Max == 'miniMushroomSpaceOdds1':
        miniMushroomSpaceOdds1 += (100 - miniMushroomSpaceOdds1)

    if spaceOdds1Max == 'megaMushroomSpaceOdds1':
        megaMushroomSpaceOdds1 += (100 - megaMushroomSpaceOdds1)

    if spaceOdds1Max == 'superMiniMushroomSpaceOdds1':
        superMiniMushroomSpaceOdds1 += (100 - superMiniMushroomSpaceOdds1)

    if spaceOdds1Max == 'superMegaMushroomSpaceOdds1':
        superMegaMushroomSpaceOdds1 += (100 - superMegaMushroomSpaceOdds1)

    if spaceOdds1Max == 'miniMegaHammerSpaceOdds1':
        miniMegaHammerSpaceOdds1 += (100 - miniMegaHammerSpaceOdds1)

    if spaceOdds1Max == 'warpPipeSpaceOdds1':
        warpPipeSpaceOdds1 += (100 - warpPipeSpaceOdds1)

    if spaceOdds1Max == 'swapCardSpaceOdds1':
        swapCardSpaceOdds1 += (100 - swapCardSpaceOdds1)

    if spaceOdds1Max == 'sparkyStickerSpaceOdds1':
        sparkyStickerSpaceOdds1 += (100 - sparkyStickerSpaceOdds1)

    if spaceOdds1Max == 'gaddlightSpaceOdds1':
        gaddlightSpaceOdds1 += (100 - gaddlightSpaceOdds1)

    if spaceOdds1Max == 'chompCallSpaceOdds1':
        chompCallSpaceOdds1 += (100 - chompCallSpaceOdds1)

    if spaceOdds1Max == 'bowserSuitSpaceOdds1':
        bowserSuitSpaceOdds1 += (100 - bowserSuitSpaceOdds1)

    if spaceOdds1Max == 'crystalBallSpaceOdds1':
        crystalBallSpaceOdds1 += (100 - crystalBallSpaceOdds1)

    if spaceOdds1Max == 'magicLampSpaceOdds1':
        magicLampSpaceOdds1 += (100 - magicLampSpaceOdds1)

    if spaceOdds1Max == 'itemBagSpaceOdds1':
        itemBagSpaceOdds1 += (100 - itemBagSpaceOdds1)

    if spaceOdds1Max == 'mushroomSpaceOdds1':
        mushroomSpaceOdds1 += (100 - mushroomSpaceOdds1)

    if spaceOdds1Max == 'goldenMushroomSpaceOdds1':
        goldenMushroomSpaceOdds1 += (100 - goldenMushroomSpaceOdds1)

    if spaceOdds1Max == 'reverseMushroomSpaceOdds1':
        reverseMushroomSpaceOdds1 += (100 - reverseMushroomSpaceOdds1)

    if spaceOdds1Max == 'poisonMushroomSpaceOdds1':
        poisonMushroomSpaceOdds1 += (100 - poisonMushroomSpaceOdds1)

    if spaceOdds1Max == 'triplePoisonMushroomSpaceOdds1':
        triplePoisonMushroomSpaceOdds1 += (100 - triplePoisonMushroomSpaceOdds1)

    if spaceOdds1Max == 'celluarShopperSpaceOdds1':
        celluarShopperSpaceOdds1 += (100 - celluarShopperSpaceOdds1)

    if spaceOdds1Max == 'skeletonKeySpaceOdds1':
        skeletonKeySpaceOdds1 += (100 - skeletonKeySpaceOdds1)

    if spaceOdds1Max == 'plunderChestSpaceOdds1':
        plunderChestSpaceOdds1 += (100 - plunderChestSpaceOdds1)

    if spaceOdds1Max == 'gaddbrushSpaceOdds1':
        gaddbrushSpaceOdds1 += (100 - gaddbrushSpaceOdds1)

    if spaceOdds1Max == 'warpBlockSpaceOdds1':
        warpBlockSpaceOdds1 += (100 - warpBlockSpaceOdds1)

    if spaceOdds1Max == 'flyGuySpaceOdds1':
        flyGuySpaceOdds1 += (100 - flyGuySpaceOdds1)

    if spaceOdds1Max == 'plusBlockSpaceOdds1':
        plusBlockSpaceOdds1 += (100 - plusBlockSpaceOdds1)

    if spaceOdds1Max == 'minusBlockSpaceOdds1':
        minusBlockSpaceOdds1 += (100 - minusBlockSpaceOdds1)

    if spaceOdds1Max == 'speedBlockSpaceOdds1':
        speedBlockSpaceOdds1 += (100 - speedBlockSpaceOdds1)

    if spaceOdds1Max == 'slowBlockSpaceOdds1':
        slowBlockSpaceOdds1 += (100 - slowBlockSpaceOdds1)

    if spaceOdds1Max == 'bowserPhoneSpaceOdds1':
        bowserPhoneSpaceOdds1 += (100 - bowserPhoneSpaceOdds1)

    if spaceOdds1Max == 'doubleDipSpaceOdds1':
        doubleDipSpaceOdds1 += (100 - doubleDipSpaceOdds1)

    if spaceOdds1Max == 'hiddenBlockCardSpaceOdds1':
        hiddenBlockCardSpaceOdds1 += (100 - hiddenBlockCardSpaceOdds1)

    if spaceOdds1Max == 'barterBoxSpaceOdds1':
        barterBoxSpaceOdds1 += (100 - barterBoxSpaceOdds1)

    if spaceOdds1Max == 'superWarpPipeSpaceOdds1':
        superWarpPipeSpaceOdds1 += (100 - superWarpPipeSpaceOdds1)

    if spaceOdds1Max == 'chanceTimeCharmSpaceOdds1':
        chanceTimeCharmSpaceOdds1 += (100 - chanceTimeCharmSpaceOdds1)

    if spaceOdds1Max == 'wackyWatchSpaceOdds1':
        wackyWatchSpaceOdds1 += (100 - wackyWatchSpaceOdds1)

    if spaceOdds2Max == 'miniMushroomSpaceOdds2':
        miniMushroomSpaceOdds2 += (100 - miniMushroomSpaceOdds2)

    if spaceOdds2Max == 'megaMushroomSpaceOdds2':
        megaMushroomSpaceOdds2 += (100 - megaMushroomSpaceOdds2)

    if spaceOdds2Max == 'superMiniMushroomSpaceOdds2':
        superMiniMushroomSpaceOdds2 += (100 - superMiniMushroomSpaceOdds2)

    if spaceOdds2Max == 'superMegaMushroomSpaceOdds2':
        superMegaMushroomSpaceOdds2 += (100 - superMegaMushroomSpaceOdds2)

    if spaceOdds2Max == 'miniMegaHammerSpaceOdds2':
        miniMegaHammerSpaceOdds2 += (100 - miniMegaHammerSpaceOdds2)

    if spaceOdds2Max == 'warpPipeSpaceOdds2':
        warpPipeSpaceOdds2 += (100 - warpPipeSpaceOdds2)

    if spaceOdds2Max == 'swapCardSpaceOdds2':
        swapCardSpaceOdds2 += (100 - swapCardSpaceOdds2)

    if spaceOdds2Max == 'sparkyStickerSpaceOdds2':
        sparkyStickerSpaceOdds2 += (100 - sparkyStickerSpaceOdds2)

    if spaceOdds2Max == 'gaddlightSpaceOdds2':
        gaddlightSpaceOdds2 += (100 - gaddlightSpaceOdds2)

    if spaceOdds2Max == 'chompCallSpaceOdds2':
        chompCallSpaceOdds2 += (100 - chompCallSpaceOdds2)

    if spaceOdds2Max == 'bowserSuitSpaceOdds2':
        bowserSuitSpaceOdds2 += (100 - bowserSuitSpaceOdds2)

    if spaceOdds2Max == 'crystalBallSpaceOdds2':
        crystalBallSpaceOdds2 += (100 - crystalBallSpaceOdds2)

    if spaceOdds2Max == 'magicLampSpaceOdds2':
        magicLampSpaceOdds2 += (100 - magicLampSpaceOdds2)

    if spaceOdds2Max == 'itemBagSpaceOdds2':
        itemBagSpaceOdds2 += (100 - itemBagSpaceOdds2)

    if spaceOdds2Max == 'mushroomSpaceOdds2':
        mushroomSpaceOdds2 += (100 - mushroomSpaceOdds2)

    if spaceOdds2Max == 'goldenMushroomSpaceOdds2':
        goldenMushroomSpaceOdds2 += (100 - goldenMushroomSpaceOdds2)

    if spaceOdds2Max == 'reverseMushroomSpaceOdds2':
        reverseMushroomSpaceOdds2 += (100 - reverseMushroomSpaceOdds2)

    if spaceOdds2Max == 'poisonMushroomSpaceOdds2':
        poisonMushroomSpaceOdds2 += (100 - poisonMushroomSpaceOdds2)

    if spaceOdds2Max == 'triplePoisonMushroomSpaceOdds2':
        triplePoisonMushroomSpaceOdds2 += (100 - triplePoisonMushroomSpaceOdds2)

    if spaceOdds2Max == 'celluarShopperSpaceOdds2':
        celluarShopperSpaceOdds2 += (100 - celluarShopperSpaceOdds2)

    if spaceOdds2Max == 'skeletonKeySpaceOdds2':
        skeletonKeySpaceOdds2 += (100 - skeletonKeySpaceOdds2)

    if spaceOdds2Max == 'plunderChestSpaceOdds2':
        plunderChestSpaceOdds2 += (100 - plunderChestSpaceOdds2)

    if spaceOdds2Max == 'gaddbrushSpaceOdds2':
        gaddbrushSpaceOdds2 += (100 - gaddbrushSpaceOdds2)

    if spaceOdds2Max == 'warpBlockSpaceOdds2':
        warpBlockSpaceOdds2 += (100 - warpBlockSpaceOdds2)

    if spaceOdds2Max == 'flyGuySpaceOdds2':
        flyGuySpaceOdds2 += (100 - flyGuySpaceOdds2)

    if spaceOdds2Max == 'plusBlockSpaceOdds2':
        plusBlockSpaceOdds2 += (100 - plusBlockSpaceOdds2)

    if spaceOdds2Max == 'minusBlockSpaceOdds2':
        minusBlockSpaceOdds2 += (100 - minusBlockSpaceOdds2)

    if spaceOdds2Max == 'speedBlockSpaceOdds2':
        speedBlockSpaceOdds2 += (100 - speedBlockSpaceOdds2)

    if spaceOdds2Max == 'slowBlockSpaceOdds2':
        slowBlockSpaceOdds2 += (100 - slowBlockSpaceOdds2)

    if spaceOdds2Max == 'bowserPhoneSpaceOdds2':
        bowserPhoneSpaceOdds2 += (100 - bowserPhoneSpaceOdds2)

    if spaceOdds2Max == 'doubleDipSpaceOdds2':
        doubleDipSpaceOdds2 += (100 - doubleDipSpaceOdds2)

    if spaceOdds2Max == 'hiddenBlockCardSpaceOdds2':
        hiddenBlockCardSpaceOdds2 += (100 - hiddenBlockCardSpaceOdds2)

    if spaceOdds2Max == 'barterBoxSpaceOdds2':
        barterBoxSpaceOdds2 += (100 - barterBoxSpaceOdds2)

    if spaceOdds2Max == 'superWarpPipeSpaceOdds2':
        superWarpPipeSpaceOdds2 += (100 - superWarpPipeSpaceOdds2)

    if spaceOdds2Max == 'chanceTimeCharmSpaceOdds2':
        chanceTimeCharmSpaceOdds2 += (100 - chanceTimeCharmSpaceOdds2)

    if spaceOdds2Max == 'wackyWatchSpaceOdds2':
        wackyWatchSpaceOdds2 += (100 - wackyWatchSpaceOdds2)

    if spaceOdds34Max == 'miniMushroomSpaceOdds34':
        miniMushroomSpaceOdds34 += (100 - miniMushroomSpaceOdds34)

    if spaceOdds34Max == 'megaMushroomSpaceOdds34':
        megaMushroomSpaceOdds34 += (100 - megaMushroomSpaceOdds34)

    if spaceOdds34Max == 'superMiniMushroomSpaceOdds34':
        superMiniMushroomSpaceOdds34 += (100 - superMiniMushroomSpaceOdds34)

    if spaceOdds34Max == 'superMegaMushroomSpaceOdds34':
        superMegaMushroomSpaceOdds34 += (100 - superMegaMushroomSpaceOdds34)

    if spaceOdds34Max == 'miniMegaHammerSpaceOdds34':
        miniMegaHammerSpaceOdds34 += (100 - miniMegaHammerSpaceOdds34)

    if spaceOdds34Max == 'warpPipeSpaceOdds34':
        warpPipeSpaceOdds34 += (100 - warpPipeSpaceOdds34)

    if spaceOdds34Max == 'swapCardSpaceOdds34':
        swapCardSpaceOdds34 += (100 - swapCardSpaceOdds34)

    if spaceOdds34Max == 'sparkyStickerSpaceOdds34':
        sparkyStickerSpaceOdds34 += (100 - sparkyStickerSpaceOdds34)

    if spaceOdds34Max == 'gaddlightSpaceOdds34':
        gaddlightSpaceOdds34 += (100 - gaddlightSpaceOdds34)

    if spaceOdds34Max == 'chompCallSpaceOdds34':
        chompCallSpaceOdds34 += (100 - chompCallSpaceOdds34)

    if spaceOdds34Max == 'bowserSuitSpaceOdds34':
        bowserSuitSpaceOdds34 += (100 - bowserSuitSpaceOdds34)

    if spaceOdds34Max == 'crystalBallSpaceOdds34':
        crystalBallSpaceOdds34 += (100 - crystalBallSpaceOdds34)

    if spaceOdds34Max == 'magicLampSpaceOdds34':
        magicLampSpaceOdds34 += (100 - magicLampSpaceOdds34)

    if spaceOdds34Max == 'itemBagSpaceOdds34':
        itemBagSpaceOdds34 += (100 - itemBagSpaceOdds34)

    if spaceOdds34Max == 'mushroomSpaceOdds34':
        mushroomSpaceOdds34 += (100 - mushroomSpaceOdds34)

    if spaceOdds34Max == 'goldenMushroomSpaceOdds34':
        goldenMushroomSpaceOdds34 += (100 - goldenMushroomSpaceOdds34)

    if spaceOdds34Max == 'reverseMushroomSpaceOdds34':
        reverseMushroomSpaceOdds34 += (100 - reverseMushroomSpaceOdds34)

    if spaceOdds34Max == 'poisonMushroomSpaceOdds34':
        poisonMushroomSpaceOdds34 += (100 - poisonMushroomSpaceOdds34)

    if spaceOdds34Max == 'triplePoisonMushroomSpaceOdds34':
        triplePoisonMushroomSpaceOdds34 += (100 - triplePoisonMushroomSpaceOdds34)

    if spaceOdds34Max == 'celluarShopperSpaceOdds34':
        celluarShopperSpaceOdds34 += (100 - celluarShopperSpaceOdds34)

    if spaceOdds34Max == 'skeletonKeySpaceOdds34':
        skeletonKeySpaceOdds34 += (100 - skeletonKeySpaceOdds34)

    if spaceOdds34Max == 'plunderChestSpaceOdds34':
        plunderChestSpaceOdds34 += (100 - plunderChestSpaceOdds34)

    if spaceOdds34Max == 'gaddbrushSpaceOdds34':
        gaddbrushSpaceOdds34 += (100 - gaddbrushSpaceOdds34)

    if spaceOdds34Max == 'warpBlockSpaceOdds34':
        warpBlockSpaceOdds34 += (100 - warpBlockSpaceOdds34)

    if spaceOdds34Max == 'flyGuySpaceOdds34':
        flyGuySpaceOdds34 += (100 - flyGuySpaceOdds34)

    if spaceOdds34Max == 'plusBlockSpaceOdds34':
        plusBlockSpaceOdds34 += (100 - plusBlockSpaceOdds34)

    if spaceOdds34Max == 'minusBlockSpaceOdds34':
        minusBlockSpaceOdds34 += (100 - minusBlockSpaceOdds34)

    if spaceOdds34Max == 'speedBlockSpaceOdds34':
        speedBlockSpaceOdds34 += (100 - speedBlockSpaceOdds34)

    if spaceOdds34Max == 'slowBlockSpaceOdds34':
        slowBlockSpaceOdds34 += (100 - slowBlockSpaceOdds34)

    if spaceOdds34Max == 'bowserPhoneSpaceOdds34':
        bowserPhoneSpaceOdds34 += (100 - bowserPhoneSpaceOdds34)

    if spaceOdds34Max == 'doubleDipSpaceOdds34':
        doubleDipSpaceOdds34 += (100 - doubleDipSpaceOdds34)

    if spaceOdds34Max == 'hiddenBlockCardSpaceOdds34':
        hiddenBlockCardSpaceOdds34 += (100 - hiddenBlockCardSpaceOdds34)

    if spaceOdds34Max == 'barterBoxSpaceOdds34':
        barterBoxSpaceOdds34 += (100 - barterBoxSpaceOdds34)

    if spaceOdds34Max == 'superWarpPipeSpaceOdds34':
        superWarpPipeSpaceOdds34 += (100 - superWarpPipeSpaceOdds34)

    if spaceOdds34Max == 'chanceTimeCharmSpaceOdds34':
        chanceTimeCharmSpaceOdds34 += (100 - chanceTimeCharmSpaceOdds34)

    if spaceOdds34Max == 'wackyWatchSpaceOdds34':
        wackyWatchSpaceOdds34 += (100 - wackyWatchSpaceOdds34)

    miniMushroomSpaceOdds34 = str(miniMushroomSpaceOdds34)
    megaMushroomSpaceOdds34 = str(megaMushroomSpaceOdds34)
    superMiniMushroomSpaceOdds34 = str(superMiniMushroomSpaceOdds34)
    superMegaMushroomSpaceOdds34 = str(superMegaMushroomSpaceOdds34)
    miniMegaHammerSpaceOdds34 = str(miniMegaHammerSpaceOdds34)
    warpPipeSpaceOdds34 = str(warpPipeSpaceOdds34)
    swapCardSpaceOdds34 = str(swapCardSpaceOdds34)
    sparkyStickerSpaceOdds34 = str(sparkyStickerSpaceOdds34)
    gaddlightSpaceOdds34 = str(gaddlightSpaceOdds34)
    chompCallSpaceOdds34 = str(chompCallSpaceOdds34)
    bowserSuitSpaceOdds34 = str(bowserSuitSpaceOdds34)
    crystalBallSpaceOdds34 = str(crystalBallSpaceOdds34)
    magicLampSpaceOdds34 = str(magicLampSpaceOdds34)
    itemBagSpaceOdds34 = str(itemBagSpaceOdds34)
    mushroomSpaceOdds34 = str(mushroomSpaceOdds34)
    goldenMushroomSpaceOdds34 = str(goldenMushroomSpaceOdds34)
    reverseMushroomSpaceOdds34 = str(reverseMushroomSpaceOdds34)
    poisonMushroomSpaceOdds34 = str(poisonMushroomSpaceOdds34)
    triplePoisonMushroomSpaceOdds34 = str(triplePoisonMushroomSpaceOdds34)
    celluarShopperSpaceOdds34 = str(celluarShopperSpaceOdds34)
    skeletonKeySpaceOdds34 = str(skeletonKeySpaceOdds34)
    plunderChestSpaceOdds34 = str(plunderChestSpaceOdds34)
    gaddbrushSpaceOdds34 = str(gaddbrushSpaceOdds34)
    warpBlockSpaceOdds34 = str(warpBlockSpaceOdds34)
    flyGuySpaceOdds34 = str(flyGuySpaceOdds34)
    plusBlockSpaceOdds34 = str(plusBlockSpaceOdds34)
    minusBlockSpaceOdds34 = str(minusBlockSpaceOdds34)
    speedBlockSpaceOdds34 = str(speedBlockSpaceOdds34)
    slowBlockSpaceOdds34 = str(slowBlockSpaceOdds34)
    bowserPhoneSpaceOdds34 = str(bowserPhoneSpaceOdds34)
    doubleDipSpaceOdds34 = str(doubleDipSpaceOdds34)
    hiddenBlockCardSpaceOdds34 = str(hiddenBlockCardSpaceOdds34)
    barterBoxSpaceOdds34 = str(barterBoxSpaceOdds34)
    superWarpPipeSpaceOdds34 = str(superWarpPipeSpaceOdds34)
    chanceTimeCharmSpaceOdds34 = str(chanceTimeCharmSpaceOdds34)
    wackyWatchSpaceOdds34 = str(wackyWatchSpaceOdds34)
    miniMushroomShopOdds12 = str(miniMushroomShopOdds12)
    megaMushroomShopOdds12 = str(megaMushroomShopOdds12)
    superMiniMushroomShopOdds12 = str(superMiniMushroomShopOdds12)
    superMegaMushroomShopOdds12 = str(superMegaMushroomShopOdds12)
    miniMegaHammerShopOdds12 = str(miniMegaHammerShopOdds12)
    warpPipeShopOdds12 = str(warpPipeShopOdds12)
    swapCardShopOdds12 = str(swapCardShopOdds12)
    sparkyStickerShopOdds12 = str(sparkyStickerShopOdds12)
    gaddlightShopOdds12 = str(gaddlightShopOdds12)
    chompCallShopOdds12 = str(chompCallShopOdds12)
    bowserSuitShopOdds12 = str(bowserSuitShopOdds12)
    crystalBallShopOdds12 = str(crystalBallShopOdds12)
    magicLampShopOdds12 = str(magicLampShopOdds12)
    itemBagShopOdds12 = str(itemBagShopOdds12)
    mushroomShopOdds12 = str(mushroomShopOdds12)
    goldenMushroomShopOdds12 = str(goldenMushroomShopOdds12)
    reverseMushroomShopOdds12 = str(reverseMushroomShopOdds12)
    poisonMushroomShopOdds12 = str(poisonMushroomShopOdds12)
    triplePoisonMushroomShopOdds12 = str(triplePoisonMushroomShopOdds12)
    celluarShopperShopOdds12 = str(celluarShopperShopOdds12)
    skeletonKeyShopOdds12 = str(skeletonKeyShopOdds12)
    plunderChestShopOdds12 = str(plunderChestShopOdds12)
    gaddbrushShopOdds12 = str(gaddbrushShopOdds12)
    warpBlockShopOdds12 = str(warpBlockShopOdds12)
    flyGuyShopOdds12 = str(flyGuyShopOdds12)
    plusBlockShopOdds12 = str(plusBlockShopOdds12)
    minusBlockShopOdds12 = str(minusBlockShopOdds12)
    speedBlockShopOdds12 = str(speedBlockShopOdds12)
    slowBlockShopOdds12 = str(slowBlockShopOdds12)
    bowserPhoneShopOdds12 = str(bowserPhoneShopOdds12)
    doubleDipShopOdds12 = str(doubleDipShopOdds12)
    hiddenBlockCardShopOdds12 = str(hiddenBlockCardShopOdds12)
    barterBoxShopOdds12 = str(barterBoxShopOdds12)
    superWarpPipeShopOdds12 = str(superWarpPipeShopOdds12)
    chanceTimeCharmShopOdds12 = str(chanceTimeCharmShopOdds12)
    wackyWatchShopOdds12 = str(wackyWatchShopOdds12)
    miniMushroomSpaceOdds1 = str(miniMushroomSpaceOdds1)
    megaMushroomSpaceOdds1 = str(megaMushroomSpaceOdds1)
    superMiniMushroomSpaceOdds1 = str(superMiniMushroomSpaceOdds1)
    superMegaMushroomSpaceOdds1 = str(superMegaMushroomSpaceOdds1)
    miniMegaHammerSpaceOdds1 = str(miniMegaHammerSpaceOdds1)
    warpPipeSpaceOdds1 = str(warpPipeSpaceOdds1)
    swapCardSpaceOdds1 = str(swapCardSpaceOdds1)
    sparkyStickerSpaceOdds1 = str(sparkyStickerSpaceOdds1)
    gaddlightSpaceOdds1 = str(gaddlightSpaceOdds1)
    chompCallSpaceOdds1 = str(chompCallSpaceOdds1)
    bowserSuitSpaceOdds1 = str(bowserSuitSpaceOdds1)
    crystalBallSpaceOdds1 = str(crystalBallSpaceOdds1)
    magicLampSpaceOdds1 = str(magicLampSpaceOdds1)
    itemBagSpaceOdds1 = str(itemBagSpaceOdds1)
    mushroomSpaceOdds1 = str(mushroomSpaceOdds1)
    goldenMushroomSpaceOdds1 = str(goldenMushroomSpaceOdds1)
    reverseMushroomSpaceOdds1 = str(reverseMushroomSpaceOdds1)
    poisonMushroomSpaceOdds1 = str(poisonMushroomSpaceOdds1)
    triplePoisonMushroomSpaceOdds1 = str(triplePoisonMushroomSpaceOdds1)
    celluarShopperSpaceOdds1 = str(celluarShopperSpaceOdds1)
    skeletonKeySpaceOdds1 = str(skeletonKeySpaceOdds1)
    plunderChestSpaceOdds1 = str(plunderChestSpaceOdds1)
    gaddbrushSpaceOdds1 = str(gaddbrushSpaceOdds1)
    warpBlockSpaceOdds1 = str(warpBlockSpaceOdds1)
    flyGuySpaceOdds1 = str(flyGuySpaceOdds1)
    plusBlockSpaceOdds1 = str(plusBlockSpaceOdds1)
    minusBlockSpaceOdds1 = str(minusBlockSpaceOdds1)
    speedBlockSpaceOdds1 = str(speedBlockSpaceOdds1)
    slowBlockSpaceOdds1 = str(slowBlockSpaceOdds1)
    bowserPhoneSpaceOdds1 = str(bowserPhoneSpaceOdds1)
    doubleDipSpaceOdds1 = str(doubleDipSpaceOdds1)
    hiddenBlockCardSpaceOdds1 = str(hiddenBlockCardSpaceOdds1)
    barterBoxSpaceOdds1 = str(barterBoxSpaceOdds1)
    superWarpPipeSpaceOdds1 = str(superWarpPipeSpaceOdds1)
    chanceTimeCharmSpaceOdds1 = str(chanceTimeCharmSpaceOdds1)
    miniMushroomSpaceOdds2 = str(miniMushroomSpaceOdds2)
    megaMushroomSpaceOdds2 = str(megaMushroomSpaceOdds2)
    superMiniMushroomSpaceOdds2 = str(superMiniMushroomSpaceOdds2)
    superMegaMushroomSpaceOdds2 = str(superMegaMushroomSpaceOdds2)
    miniMegaHammerSpaceOdds2 = str(miniMegaHammerSpaceOdds2)
    warpPipeSpaceOdds2 = str(warpPipeSpaceOdds2)
    swapCardSpaceOdds2 = str(swapCardSpaceOdds2)
    sparkyStickerSpaceOdds2 = str(sparkyStickerSpaceOdds2)
    gaddlightSpaceOdds2 = str(gaddlightSpaceOdds2)
    chompCallSpaceOdds2 = str(chompCallSpaceOdds2)
    bowserSuitSpaceOdds2 = str(bowserSuitSpaceOdds2)
    crystalBallSpaceOdds2 = str(crystalBallSpaceOdds2)
    magicLampSpaceOdds2 = str(magicLampSpaceOdds2)
    itemBagSpaceOdds2 = str(itemBagSpaceOdds2)
    mushroomSpaceOdds2 = str(mushroomSpaceOdds2)
    goldenMushroomSpaceOdds2 = str(goldenMushroomSpaceOdds2)
    reverseMushroomSpaceOdds2 = str(reverseMushroomSpaceOdds2)
    poisonMushroomSpaceOdds2 = str(poisonMushroomSpaceOdds2)
    triplePoisonMushroomSpaceOdds2 = str(triplePoisonMushroomSpaceOdds2)
    celluarShopperSpaceOdds2 = str(celluarShopperSpaceOdds2)
    skeletonKeySpaceOdds2 = str(skeletonKeySpaceOdds2)
    plunderChestSpaceOdds2 = str(plunderChestSpaceOdds2)
    gaddbrushSpaceOdds2 = str(gaddbrushSpaceOdds2)
    warpBlockSpaceOdds2 = str(warpBlockSpaceOdds2)
    flyGuySpaceOdds2 = str(flyGuySpaceOdds2)
    plusBlockSpaceOdds2 = str(plusBlockSpaceOdds2)
    minusBlockSpaceOdds2 = str(minusBlockSpaceOdds2)
    speedBlockSpaceOdds2 = str(speedBlockSpaceOdds2)
    slowBlockSpaceOdds2 = str(slowBlockSpaceOdds2)
    bowserPhoneSpaceOdds2 = str(bowserPhoneSpaceOdds2)
    doubleDipSpaceOdds2 = str(doubleDipSpaceOdds2)
    hiddenBlockCardSpaceOdds2 = str(hiddenBlockCardSpaceOdds2)
    barterBoxSpaceOdds2 = str(barterBoxSpaceOdds2)
    superWarpPipeSpaceOdds2 = str(superWarpPipeSpaceOdds2)
    chanceTimeCharmSpaceOdds2 = str(chanceTimeCharmSpaceOdds2)
    wackyWatchSpaceOdds2 = str(wackyWatchSpaceOdds2)
    miniMushroomSpaceOdds34 = str(miniMushroomSpaceOdds34)
    megaMushroomSpaceOdds34 = str(megaMushroomSpaceOdds34)
    superMiniMushroomSpaceOdds34 = str(superMiniMushroomSpaceOdds34)
    superMegaMushroomSpaceOdds34 = str(superMegaMushroomSpaceOdds34)
    miniMegaHammerSpaceOdds34 = str(miniMegaHammerSpaceOdds34)
    warpPipeSpaceOdds34 = str(warpPipeSpaceOdds34)
    swapCardSpaceOdds34 = str(swapCardSpaceOdds34)
    sparkyStickerSpaceOdds34 = str(sparkyStickerSpaceOdds34)
    gaddlightSpaceOdds34 = str(gaddlightSpaceOdds34)
    chompCallSpaceOdds34 = str(chompCallSpaceOdds34)
    bowserSuitSpaceOdds34 = str(bowserSuitSpaceOdds34)
    crystalBallSpaceOdds34 = str(crystalBallSpaceOdds34)
    magicLampSpaceOdds34 = str(magicLampSpaceOdds34)
    itemBagSpaceOdds34 = str(itemBagSpaceOdds34)
    mushroomSpaceOdds34 = str(mushroomSpaceOdds34)
    goldenMushroomSpaceOdds34 = str(goldenMushroomSpaceOdds34)
    reverseMushroomSpaceOdds34 = str(reverseMushroomSpaceOdds34)
    poisonMushroomSpaceOdds34 = str(poisonMushroomSpaceOdds34)
    triplePoisonMushroomSpaceOdds34 = str(triplePoisonMushroomSpaceOdds34)
    celluarShopperSpaceOdds34 = str(celluarShopperSpaceOdds34)
    skeletonKeySpaceOdds34 = str(skeletonKeySpaceOdds34)
    plunderChestSpaceOdds34 = str(plunderChestSpaceOdds34)
    gaddbrushSpaceOdds34 = str(gaddbrushSpaceOdds34)
    warpBlockSpaceOdds34 = str(warpBlockSpaceOdds34)
    flyGuySpaceOdds34 = str(flyGuySpaceOdds34)
    plusBlockSpaceOdds34 = str(plusBlockSpaceOdds34)
    minusBlockSpaceOdds34 = str(minusBlockSpaceOdds34)
    speedBlockSpaceOdds34 = str(speedBlockSpaceOdds34)
    slowBlockSpaceOdds34 = str(slowBlockSpaceOdds34)
    bowserPhoneSpaceOdds34 = str(bowserPhoneSpaceOdds34)
    doubleDipSpaceOdds34 = str(doubleDipSpaceOdds34)
    hiddenBlockCardSpaceOdds34 = str(hiddenBlockCardSpaceOdds34)
    barterBoxSpaceOdds34 = str(barterBoxSpaceOdds34)
    superWarpPipeSpaceOdds34 = str(superWarpPipeSpaceOdds34)
    chanceTimeCharmSpaceOdds34 = str(chanceTimeCharmSpaceOdds34)
    wackyWatchSpaceOdds34 = str(wackyWatchSpaceOdds34)

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

    # Usage
    miniMushroomPrice1 = convert_to_hex_weight(miniMushroomPrice1)
    miniMushroomPrice2 = convert_to_hex_weight(miniMushroomPrice2)
    miniMushroomPrice34 = convert_to_hex_weight(miniMushroomPrice34)
    miniMushroomShopOdds12 = convert_to_hex_weight(miniMushroomShopOdds12)
    miniMushroomShopOdds34 = convert_to_hex_weight(miniMushroomShopOdds34)
    miniMushroomSpaceOdds1 = convert_to_hex_weight(miniMushroomSpaceOdds1)
    miniMushroomSpaceOdds2 = convert_to_hex_weight(miniMushroomSpaceOdds2)
    miniMushroomSpaceOdds34 = convert_to_hex_weight(miniMushroomSpaceOdds34)
    megaMushroomPrice1 = convert_to_hex_weight(megaMushroomPrice1)
    megaMushroomPrice2 = convert_to_hex_weight(megaMushroomPrice2)
    megaMushroomPrice34 = convert_to_hex_weight(megaMushroomPrice34)
    megaMushroomShopOdds12 = convert_to_hex_weight(megaMushroomShopOdds12)
    megaMushroomShopOdds34 = convert_to_hex_weight(megaMushroomShopOdds34)
    megaMushroomSpaceOdds1 = convert_to_hex_weight(megaMushroomSpaceOdds1)
    megaMushroomSpaceOdds2 = convert_to_hex_weight(megaMushroomSpaceOdds2)
    megaMushroomSpaceOdds34 = convert_to_hex_weight(megaMushroomSpaceOdds34)
    superMiniMushroomPrice1 = convert_to_hex_weight(superMiniMushroomPrice1)
    superMiniMushroomPrice2 = convert_to_hex_weight(superMiniMushroomPrice2)
    superMiniMushroomPrice34 = convert_to_hex_weight(superMiniMushroomPrice34)
    superMiniMushroomShopOdds12 = convert_to_hex_weight(superMiniMushroomShopOdds12)
    superMiniMushroomShopOdds34 = convert_to_hex_weight(superMiniMushroomShopOdds34)
    superMiniMushroomSpaceOdds1 = convert_to_hex_weight(superMiniMushroomSpaceOdds1)
    superMiniMushroomSpaceOdds2 = convert_to_hex_weight(superMiniMushroomSpaceOdds2)
    superMiniMushroomSpaceOdds34 = convert_to_hex_weight(superMiniMushroomSpaceOdds34)
    superMegaMushroomPrice1 = convert_to_hex_weight(superMegaMushroomPrice1)
    superMegaMushroomPrice2 = convert_to_hex_weight(superMegaMushroomPrice2)
    superMegaMushroomPrice34 = convert_to_hex_weight(superMegaMushroomPrice34)
    superMegaMushroomShopOdds12 = convert_to_hex_weight(superMegaMushroomShopOdds12)
    superMegaMushroomShopOdds34 = convert_to_hex_weight(superMegaMushroomShopOdds34)
    superMegaMushroomSpaceOdds1 = convert_to_hex_weight(superMegaMushroomSpaceOdds1)
    superMegaMushroomSpaceOdds2 = convert_to_hex_weight(superMegaMushroomSpaceOdds2)
    superMegaMushroomSpaceOdds34 = convert_to_hex_weight(superMegaMushroomSpaceOdds34)
    miniMegaHammerPrice1 = convert_to_hex_weight(miniMegaHammerPrice1)
    miniMegaHammerPrice2 = convert_to_hex_weight(miniMegaHammerPrice2)
    miniMegaHammerPrice34 = convert_to_hex_weight(miniMegaHammerPrice34)
    miniMegaHammerShopOdds12 = convert_to_hex_weight(miniMegaHammerShopOdds12)
    miniMegaHammerShopOdds34 = convert_to_hex_weight(miniMegaHammerShopOdds34)
    miniMegaHammerSpaceOdds1 = convert_to_hex_weight(miniMegaHammerSpaceOdds1)
    miniMegaHammerSpaceOdds2 = convert_to_hex_weight(miniMegaHammerSpaceOdds2)
    miniMegaHammerSpaceOdds34 = convert_to_hex_weight(miniMegaHammerSpaceOdds34)
    warpPipePrice1 = convert_to_hex_weight(warpPipePrice1)
    warpPipePrice2 = convert_to_hex_weight(warpPipePrice2)
    warpPipePrice34 = convert_to_hex_weight(warpPipePrice34)
    warpPipeShopOdds12 = convert_to_hex_weight(warpPipeShopOdds12)
    warpPipeShopOdds34 = convert_to_hex_weight(warpPipeShopOdds34)
    warpPipeSpaceOdds1 = convert_to_hex_weight(warpPipeSpaceOdds1)
    warpPipeSpaceOdds2 = convert_to_hex_weight(warpPipeSpaceOdds2)
    warpPipeSpaceOdds34 = convert_to_hex_weight(warpPipeSpaceOdds34)
    swapCardPrice1 = convert_to_hex_weight(swapCardPrice1)
    swapCardPrice2 = convert_to_hex_weight(swapCardPrice2)
    swapCardPrice34 = convert_to_hex_weight(swapCardPrice34)
    swapCardShopOdds12 = convert_to_hex_weight(swapCardShopOdds12)
    swapCardShopOdds34 = convert_to_hex_weight(swapCardShopOdds34)
    swapCardSpaceOdds1 = convert_to_hex_weight(swapCardSpaceOdds1)
    swapCardSpaceOdds2 = convert_to_hex_weight(swapCardSpaceOdds2)
    swapCardSpaceOdds34 = convert_to_hex_weight(swapCardSpaceOdds34)
    sparkyStickerPrice1 = convert_to_hex_weight(sparkyStickerPrice1)
    sparkyStickerPrice2 = convert_to_hex_weight(sparkyStickerPrice2)
    sparkyStickerPrice34 = convert_to_hex_weight(sparkyStickerPrice34)
    sparkyStickerShopOdds12 = convert_to_hex_weight(sparkyStickerShopOdds12)
    sparkyStickerShopOdds34 = convert_to_hex_weight(sparkyStickerShopOdds34)
    sparkyStickerSpaceOdds1 = convert_to_hex_weight(sparkyStickerSpaceOdds1)
    sparkyStickerSpaceOdds2 = convert_to_hex_weight(sparkyStickerSpaceOdds2)
    sparkyStickerSpaceOdds34 = convert_to_hex_weight(sparkyStickerSpaceOdds34)
    gaddlightPrice1 = convert_to_hex_weight(gaddlightPrice1)
    gaddlightPrice2 = convert_to_hex_weight(gaddlightPrice2)
    gaddlightPrice34 = convert_to_hex_weight(gaddlightPrice34)
    gaddlightShopOdds12 = convert_to_hex_weight(gaddlightShopOdds12)
    gaddlightShopOdds34 = convert_to_hex_weight(gaddlightShopOdds34)
    gaddlightSpaceOdds1 = convert_to_hex_weight(gaddlightSpaceOdds1)
    gaddlightSpaceOdds2 = convert_to_hex_weight(gaddlightSpaceOdds2)
    gaddlightSpaceOdds34 = convert_to_hex_weight(gaddlightSpaceOdds34)
    chompCallPrice1 = convert_to_hex_weight(chompCallPrice1)
    chompCallPrice2 = convert_to_hex_weight(chompCallPrice2)
    chompCallPrice34 = convert_to_hex_weight(chompCallPrice34)
    chompCallShopOdds12 = convert_to_hex_weight(chompCallShopOdds12)
    chompCallShopOdds34 = convert_to_hex_weight(chompCallShopOdds34)
    chompCallSpaceOdds1 = convert_to_hex_weight(chompCallSpaceOdds1)
    chompCallSpaceOdds2 = convert_to_hex_weight(chompCallSpaceOdds2)
    chompCallSpaceOdds34 = convert_to_hex_weight(chompCallSpaceOdds34)
    bowserSuitPrice1 = convert_to_hex_weight(bowserSuitPrice1)
    bowserSuitPrice2 = convert_to_hex_weight(bowserSuitPrice2)
    bowserSuitPrice34 = convert_to_hex_weight(bowserSuitPrice34)
    bowserSuitShopOdds12 = convert_to_hex_weight(bowserSuitShopOdds12)
    bowserSuitShopOdds34 = convert_to_hex_weight(bowserSuitShopOdds34)
    bowserSuitSpaceOdds1 = convert_to_hex_weight(bowserSuitSpaceOdds1)
    bowserSuitSpaceOdds2 = convert_to_hex_weight(bowserSuitSpaceOdds2)
    bowserSuitSpaceOdds34 = convert_to_hex_weight(bowserSuitSpaceOdds34)
    crystalBallPrice1 = convert_to_hex_weight(crystalBallPrice1)
    crystalBallPrice2 = convert_to_hex_weight(crystalBallPrice2)
    crystalBallPrice34 = convert_to_hex_weight(crystalBallPrice34)
    crystalBallShopOdds12 = convert_to_hex_weight(crystalBallShopOdds12)
    crystalBallShopOdds34 = convert_to_hex_weight(crystalBallShopOdds34)
    crystalBallSpaceOdds1 = convert_to_hex_weight(crystalBallSpaceOdds1)
    crystalBallSpaceOdds2 = convert_to_hex_weight(crystalBallSpaceOdds2)
    crystalBallSpaceOdds34 = convert_to_hex_weight(crystalBallSpaceOdds34)
    magicLampPrice1 = convert_to_hex_weight(magicLampPrice1)
    magicLampPrice2 = convert_to_hex_weight(magicLampPrice2)
    magicLampPrice34 = convert_to_hex_weight(magicLampPrice34)
    magicLampShopOdds12 = convert_to_hex_weight(magicLampShopOdds12)
    magicLampShopOdds34 = convert_to_hex_weight(magicLampShopOdds34)
    magicLampSpaceOdds1 = convert_to_hex_weight(magicLampSpaceOdds1)
    magicLampSpaceOdds2 = convert_to_hex_weight(magicLampSpaceOdds2)
    magicLampSpaceOdds34 = convert_to_hex_weight(magicLampSpaceOdds34)
    itemBagPrice1 = convert_to_hex_weight(itemBagPrice1)
    itemBagPrice2 = convert_to_hex_weight(itemBagPrice2)
    itemBagPrice34 = convert_to_hex_weight(itemBagPrice34)
    itemBagShopOdds12 = convert_to_hex_weight(itemBagShopOdds12)
    itemBagShopOdds34 = convert_to_hex_weight(itemBagShopOdds34)
    itemBagSpaceOdds1 = convert_to_hex_weight(itemBagSpaceOdds1)
    itemBagSpaceOdds2 = convert_to_hex_weight(itemBagSpaceOdds2)
    itemBagSpaceOdds34 = convert_to_hex_weight(itemBagSpaceOdds34)
    mushroomPrice1 = convert_to_hex_weight(mushroomPrice1)
    mushroomPrice2 = convert_to_hex_weight(mushroomPrice2)
    mushroomPrice34 = convert_to_hex_weight(mushroomPrice34)
    mushroomShopOdds12 = convert_to_hex_weight(mushroomShopOdds12)
    mushroomShopOdds34 = convert_to_hex_weight(mushroomShopOdds34)
    mushroomSpaceOdds1 = convert_to_hex_weight(mushroomSpaceOdds1)
    mushroomSpaceOdds2 = convert_to_hex_weight(mushroomSpaceOdds2)
    mushroomSpaceOdds34 = convert_to_hex_weight(mushroomSpaceOdds34)
    goldenMushroomPrice1 = convert_to_hex_weight(goldenMushroomPrice1)
    goldenMushroomPrice2 = convert_to_hex_weight(goldenMushroomPrice2)
    goldenMushroomPrice34 = convert_to_hex_weight(goldenMushroomPrice34)
    goldenMushroomShopOdds12 = convert_to_hex_weight(goldenMushroomShopOdds12)
    goldenMushroomShopOdds34 = convert_to_hex_weight(goldenMushroomShopOdds34)
    goldenMushroomSpaceOdds1 = convert_to_hex_weight(goldenMushroomSpaceOdds1)
    goldenMushroomSpaceOdds2 = convert_to_hex_weight(goldenMushroomSpaceOdds2)
    goldenMushroomSpaceOdds34 = convert_to_hex_weight(goldenMushroomSpaceOdds34)
    reverseMushroomPrice1 = convert_to_hex_weight(reverseMushroomPrice1)
    reverseMushroomPrice2 = convert_to_hex_weight(reverseMushroomPrice2)
    reverseMushroomPrice34 = convert_to_hex_weight(reverseMushroomPrice34)
    reverseMushroomShopOdds12 = convert_to_hex_weight(reverseMushroomShopOdds12)
    reverseMushroomShopOdds34 = convert_to_hex_weight(reverseMushroomShopOdds34)
    reverseMushroomSpaceOdds1 = convert_to_hex_weight(reverseMushroomSpaceOdds1)
    reverseMushroomSpaceOdds2 = convert_to_hex_weight(reverseMushroomSpaceOdds2)
    reverseMushroomSpaceOdds34 = convert_to_hex_weight(reverseMushroomSpaceOdds34)
    poisonMushroomPrice1 = convert_to_hex_weight(poisonMushroomPrice1)
    poisonMushroomPrice2 = convert_to_hex_weight(poisonMushroomPrice2)
    poisonMushroomPrice34 = convert_to_hex_weight(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = convert_to_hex_weight(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = convert_to_hex_weight(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds1 = convert_to_hex_weight(poisonMushroomSpaceOdds1)
    poisonMushroomSpaceOdds2 = convert_to_hex_weight(poisonMushroomSpaceOdds2)
    poisonMushroomSpaceOdds34 = convert_to_hex_weight(poisonMushroomSpaceOdds34)
    triplePoisonMushroomPrice1 = convert_to_hex_weight(triplePoisonMushroomPrice1)
    triplePoisonMushroomPrice2 = convert_to_hex_weight(triplePoisonMushroomPrice2)
    triplePoisonMushroomPrice34 = convert_to_hex_weight(triplePoisonMushroomPrice34)
    triplePoisonMushroomShopOdds12 = convert_to_hex_weight(triplePoisonMushroomShopOdds12)
    triplePoisonMushroomShopOdds34 = convert_to_hex_weight(triplePoisonMushroomShopOdds34)
    triplePoisonMushroomSpaceOdds1 = convert_to_hex_weight(triplePoisonMushroomSpaceOdds1)
    triplePoisonMushroomSpaceOdds2 = convert_to_hex_weight(triplePoisonMushroomSpaceOdds2)
    triplePoisonMushroomSpaceOdds34 = convert_to_hex_weight(triplePoisonMushroomSpaceOdds34)
    celluarShopperPrice1 = convert_to_hex_weight(celluarShopperPrice1)
    celluarShopperPrice2 = convert_to_hex_weight(celluarShopperPrice2)
    celluarShopperPrice34 = convert_to_hex_weight(celluarShopperPrice34)
    celluarShopperShopOdds12 = convert_to_hex_weight(celluarShopperShopOdds12)
    celluarShopperShopOdds34 = convert_to_hex_weight(celluarShopperShopOdds34)
    celluarShopperSpaceOdds1 = convert_to_hex_weight(celluarShopperSpaceOdds1)
    celluarShopperSpaceOdds2 = convert_to_hex_weight(celluarShopperSpaceOdds2)
    celluarShopperSpaceOdds34 = convert_to_hex_weight(celluarShopperSpaceOdds34)
    skeletonKeyPrice1 = convert_to_hex_weight(skeletonKeyPrice1)
    skeletonKeyPrice2 = convert_to_hex_weight(skeletonKeyPrice2)
    skeletonKeyPrice34 = convert_to_hex_weight(skeletonKeyPrice34)
    skeletonKeyShopOdds12 = convert_to_hex_weight(skeletonKeyShopOdds12)
    skeletonKeyShopOdds34 = convert_to_hex_weight(skeletonKeyShopOdds34)
    skeletonKeySpaceOdds1 = convert_to_hex_weight(skeletonKeySpaceOdds1)
    skeletonKeySpaceOdds2 = convert_to_hex_weight(skeletonKeySpaceOdds2)
    skeletonKeySpaceOdds34 = convert_to_hex_weight(skeletonKeySpaceOdds34)
    plunderChestPrice1 = convert_to_hex_weight(plunderChestPrice1)
    plunderChestPrice2 = convert_to_hex_weight(plunderChestPrice2)
    plunderChestPrice34 = convert_to_hex_weight(plunderChestPrice34)
    plunderChestShopOdds12 = convert_to_hex_weight(plunderChestShopOdds12)
    plunderChestShopOdds34 = convert_to_hex_weight(plunderChestShopOdds34)
    plunderChestSpaceOdds1 = convert_to_hex_weight(plunderChestSpaceOdds1)
    plunderChestSpaceOdds2 = convert_to_hex_weight(plunderChestSpaceOdds2)
    plunderChestSpaceOdds34 = convert_to_hex_weight(plunderChestSpaceOdds34)
    gaddbrushPrice1 = convert_to_hex_weight(gaddbrushPrice1)
    gaddbrushPrice2 = convert_to_hex_weight(gaddbrushPrice2)
    gaddbrushPrice34 = convert_to_hex_weight(gaddbrushPrice34)
    gaddbrushShopOdds12 = convert_to_hex_weight(gaddbrushShopOdds12)
    gaddbrushShopOdds34 = convert_to_hex_weight(gaddbrushShopOdds34)
    gaddbrushSpaceOdds1 = convert_to_hex_weight(gaddbrushSpaceOdds1)
    gaddbrushSpaceOdds2 = convert_to_hex_weight(gaddbrushSpaceOdds2)
    gaddbrushSpaceOdds34 = convert_to_hex_weight(gaddbrushSpaceOdds34)
    warpBlockPrice1 = convert_to_hex_weight(warpBlockPrice1)
    warpBlockPrice2 = convert_to_hex_weight(warpBlockPrice2)
    warpBlockPrice34 = convert_to_hex_weight(warpBlockPrice34)
    warpBlockShopOdds12 = convert_to_hex_weight(warpBlockShopOdds12)
    warpBlockShopOdds34 = convert_to_hex_weight(warpBlockShopOdds34)
    warpBlockSpaceOdds1 = convert_to_hex_weight(warpBlockSpaceOdds1)
    warpBlockSpaceOdds2 = convert_to_hex_weight(warpBlockSpaceOdds2)
    warpBlockSpaceOdds34 = convert_to_hex_weight(warpBlockSpaceOdds34)
    flyGuyPrice1 = convert_to_hex_weight(flyGuyPrice1)
    flyGuyPrice2 = convert_to_hex_weight(flyGuyPrice2)
    flyGuyPrice34 = convert_to_hex_weight(flyGuyPrice34)
    flyGuyShopOdds12 = convert_to_hex_weight(flyGuyShopOdds12)
    flyGuyShopOdds34 = convert_to_hex_weight(flyGuyShopOdds34)
    flyGuySpaceOdds1 = convert_to_hex_weight(flyGuySpaceOdds1)
    flyGuySpaceOdds2 = convert_to_hex_weight(flyGuySpaceOdds2)
    flyGuySpaceOdds34 = convert_to_hex_weight(flyGuySpaceOdds34)
    plusBlockPrice1 = convert_to_hex_weight(plusBlockPrice1)
    plusBlockPrice2 = convert_to_hex_weight(plusBlockPrice2)
    plusBlockPrice34 = convert_to_hex_weight(plusBlockPrice34)
    plusBlockShopOdds12 = convert_to_hex_weight(plusBlockShopOdds12)
    plusBlockShopOdds34 = convert_to_hex_weight(plusBlockShopOdds34)
    plusBlockSpaceOdds1 = convert_to_hex_weight(plusBlockSpaceOdds1)
    plusBlockSpaceOdds2 = convert_to_hex_weight(plusBlockSpaceOdds2)
    plusBlockSpaceOdds34 = convert_to_hex_weight(plusBlockSpaceOdds34)
    minusBlockPrice1 = convert_to_hex_weight(minusBlockPrice1)
    minusBlockPrice2 = convert_to_hex_weight(minusBlockPrice2)
    minusBlockPrice34 = convert_to_hex_weight(minusBlockPrice34)
    minusBlockShopOdds12 = convert_to_hex_weight(minusBlockShopOdds12)
    minusBlockShopOdds34 = convert_to_hex_weight(minusBlockShopOdds34)
    minusBlockSpaceOdds1 = convert_to_hex_weight(minusBlockSpaceOdds1)
    minusBlockSpaceOdds2 = convert_to_hex_weight(minusBlockSpaceOdds2)
    minusBlockSpaceOdds34 = convert_to_hex_weight(minusBlockSpaceOdds34)
    speedBlockPrice1 = convert_to_hex_weight(speedBlockPrice1)
    speedBlockPrice2 = convert_to_hex_weight(speedBlockPrice2)
    speedBlockPrice34 = convert_to_hex_weight(speedBlockPrice34)
    speedBlockShopOdds12 = convert_to_hex_weight(speedBlockShopOdds12)
    speedBlockShopOdds34 = convert_to_hex_weight(speedBlockShopOdds34)
    speedBlockSpaceOdds1 = convert_to_hex_weight(speedBlockSpaceOdds1)
    speedBlockSpaceOdds2 = convert_to_hex_weight(speedBlockSpaceOdds2)
    speedBlockSpaceOdds34 = convert_to_hex_weight(speedBlockSpaceOdds34)
    slowBlockPrice1 = convert_to_hex_weight(slowBlockPrice1)
    slowBlockPrice2 = convert_to_hex_weight(slowBlockPrice2)
    slowBlockPrice34 = convert_to_hex_weight(slowBlockPrice34)
    slowBlockShopOdds12 = convert_to_hex_weight(slowBlockShopOdds12)
    slowBlockShopOdds34 = convert_to_hex_weight(slowBlockShopOdds34)
    slowBlockSpaceOdds1 = convert_to_hex_weight(slowBlockSpaceOdds1)
    slowBlockSpaceOdds2 = convert_to_hex_weight(slowBlockSpaceOdds2)
    slowBlockSpaceOdds34 = convert_to_hex_weight(slowBlockSpaceOdds34)
    bowserPhonePrice1 = convert_to_hex_weight(bowserPhonePrice1)
    bowserPhonePrice2 = convert_to_hex_weight(bowserPhonePrice2)
    bowserPhonePrice34 = convert_to_hex_weight(bowserPhonePrice34)
    bowserPhoneShopOdds12 = convert_to_hex_weight(bowserPhoneShopOdds12)
    bowserPhoneShopOdds34 = convert_to_hex_weight(bowserPhoneShopOdds34)
    bowserPhoneSpaceOdds1 = convert_to_hex_weight(bowserPhoneSpaceOdds1)
    bowserPhoneSpaceOdds2 = convert_to_hex_weight(bowserPhoneSpaceOdds2)
    bowserPhoneSpaceOdds34 = convert_to_hex_weight(bowserPhoneSpaceOdds34)
    doubleDipPrice1 = convert_to_hex_weight(doubleDipPrice1)
    doubleDipPrice2 = convert_to_hex_weight(doubleDipPrice2)
    doubleDipPrice34 = convert_to_hex_weight(doubleDipPrice34)
    doubleDipShopOdds12 = convert_to_hex_weight(doubleDipShopOdds12)
    doubleDipShopOdds34 = convert_to_hex_weight(doubleDipShopOdds34)
    doubleDipSpaceOdds1 = convert_to_hex_weight(doubleDipSpaceOdds1)
    doubleDipSpaceOdds2 = convert_to_hex_weight(doubleDipSpaceOdds2)
    doubleDipSpaceOdds34 = convert_to_hex_weight(doubleDipSpaceOdds34)
    hiddenBlockCardPrice1 = convert_to_hex_weight(hiddenBlockCardPrice1)
    hiddenBlockCardPrice2 = convert_to_hex_weight(hiddenBlockCardPrice2)
    hiddenBlockCardPrice34 = convert_to_hex_weight(hiddenBlockCardPrice34)
    hiddenBlockCardShopOdds12 = convert_to_hex_weight(hiddenBlockCardShopOdds12)
    hiddenBlockCardShopOdds34 = convert_to_hex_weight(hiddenBlockCardShopOdds34)
    hiddenBlockCardSpaceOdds1 = convert_to_hex_weight(hiddenBlockCardSpaceOdds1)
    hiddenBlockCardSpaceOdds2 = convert_to_hex_weight(hiddenBlockCardSpaceOdds2)
    hiddenBlockCardSpaceOdds34 = convert_to_hex_weight(hiddenBlockCardSpaceOdds34)
    barterBoxPrice1 = convert_to_hex_weight(barterBoxPrice1)
    barterBoxPrice2 = convert_to_hex_weight(barterBoxPrice2)
    barterBoxPrice34 = convert_to_hex_weight(barterBoxPrice34)
    barterBoxShopOdds12 = convert_to_hex_weight(barterBoxShopOdds12)
    barterBoxShopOdds34 = convert_to_hex_weight(barterBoxShopOdds34)
    barterBoxSpaceOdds1 = convert_to_hex_weight(barterBoxSpaceOdds1)
    barterBoxSpaceOdds2 = convert_to_hex_weight(barterBoxSpaceOdds2)
    barterBoxSpaceOdds34 = convert_to_hex_weight(barterBoxSpaceOdds34)
    superWarpPipePrice1 = convert_to_hex_weight(superWarpPipePrice1)
    superWarpPipePrice2 = convert_to_hex_weight(superWarpPipePrice2)
    superWarpPipePrice34 = convert_to_hex_weight(superWarpPipePrice34)
    superWarpPipeShopOdds12 = convert_to_hex_weight(superWarpPipeShopOdds12)
    superWarpPipeShopOdds34 = convert_to_hex_weight(superWarpPipeShopOdds34)
    superWarpPipeSpaceOdds1 = convert_to_hex_weight(superWarpPipeSpaceOdds1)
    superWarpPipeSpaceOdds2 = convert_to_hex_weight(superWarpPipeSpaceOdds2)
    superWarpPipeSpaceOdds34 = convert_to_hex_weight(superWarpPipeSpaceOdds34)
    chanceTimeCharmPrice1 = convert_to_hex_weight(chanceTimeCharmPrice1)
    chanceTimeCharmPrice2 = convert_to_hex_weight(chanceTimeCharmPrice2)
    chanceTimeCharmPrice34 = convert_to_hex_weight(chanceTimeCharmPrice34)
    chanceTimeCharmShopOdds12 = convert_to_hex_weight(chanceTimeCharmShopOdds12)
    chanceTimeCharmShopOdds34 = convert_to_hex_weight(chanceTimeCharmShopOdds34)
    chanceTimeCharmSpaceOdds1 = convert_to_hex_weight(chanceTimeCharmSpaceOdds1)
    chanceTimeCharmSpaceOdds2 = convert_to_hex_weight(chanceTimeCharmSpaceOdds2)
    chanceTimeCharmSpaceOdds34 = convert_to_hex_weight(chanceTimeCharmSpaceOdds34)
    wackyWatchPrice1 = convert_to_hex_weight(wackyWatchPrice1)
    wackyWatchPrice2 = convert_to_hex_weight(wackyWatchPrice2)
    wackyWatchPrice34 = convert_to_hex_weight(wackyWatchPrice34)
    wackyWatchShopOdds12 = convert_to_hex_weight(wackyWatchShopOdds12)
    wackyWatchShopOdds34 = convert_to_hex_weight(wackyWatchShopOdds34)
    wackyWatchSpaceOdds1 = convert_to_hex_weight(wackyWatchSpaceOdds1)
    wackyWatchSpaceOdds2 = convert_to_hex_weight(wackyWatchSpaceOdds2)
    wackyWatchSpaceOdds34 = convert_to_hex_weight(wackyWatchSpaceOdds34)


    generatedCode = getItemModsFourDXItemSpace(miniMushroomPrice1, miniMushroomPrice2, miniMushroomPrice34, miniMushroomShopOdds12, miniMushroomShopOdds34, miniMushroomSpaceOdds1, miniMushroomSpaceOdds2, miniMushroomSpaceOdds34, megaMushroomPrice1, megaMushroomPrice2, megaMushroomPrice34, megaMushroomShopOdds12, megaMushroomShopOdds34, megaMushroomSpaceOdds1, megaMushroomSpaceOdds2, megaMushroomSpaceOdds34, superMiniMushroomPrice1, superMiniMushroomPrice2, superMiniMushroomPrice34, superMiniMushroomShopOdds12, superMiniMushroomShopOdds34, superMiniMushroomSpaceOdds1, superMiniMushroomSpaceOdds2, superMiniMushroomSpaceOdds34, superMegaMushroomPrice1, superMegaMushroomPrice2, superMegaMushroomPrice34, superMegaMushroomShopOdds12, superMegaMushroomShopOdds34, superMegaMushroomSpaceOdds1, superMegaMushroomSpaceOdds2, superMegaMushroomSpaceOdds34, miniMegaHammerPrice1, miniMegaHammerPrice2, miniMegaHammerPrice34, miniMegaHammerShopOdds12, miniMegaHammerShopOdds34, miniMegaHammerSpaceOdds1, miniMegaHammerSpaceOdds2, miniMegaHammerSpaceOdds34, warpPipePrice1, warpPipePrice2, warpPipePrice34, warpPipeShopOdds12, warpPipeShopOdds34, warpPipeSpaceOdds1, warpPipeSpaceOdds2, warpPipeSpaceOdds34, swapCardPrice1, swapCardPrice2, swapCardPrice34, swapCardShopOdds12, swapCardShopOdds34, swapCardSpaceOdds1, swapCardSpaceOdds2, swapCardSpaceOdds34, sparkyStickerPrice1, sparkyStickerPrice2, sparkyStickerPrice34, sparkyStickerShopOdds12, sparkyStickerShopOdds34, sparkyStickerSpaceOdds1, sparkyStickerSpaceOdds2, sparkyStickerSpaceOdds34, gaddlightPrice1, gaddlightPrice2, gaddlightPrice34, gaddlightShopOdds12, gaddlightShopOdds34, gaddlightSpaceOdds1, gaddlightSpaceOdds2, gaddlightSpaceOdds34, chompCallPrice1, chompCallPrice2, chompCallPrice34, chompCallShopOdds12, chompCallShopOdds34, chompCallSpaceOdds1, chompCallSpaceOdds2, chompCallSpaceOdds34, bowserSuitPrice1, bowserSuitPrice2, bowserSuitPrice34, bowserSuitShopOdds12, bowserSuitShopOdds34, bowserSuitSpaceOdds1, bowserSuitSpaceOdds2, bowserSuitSpaceOdds34, crystalBallPrice1, crystalBallPrice2, crystalBallPrice34, crystalBallShopOdds12, crystalBallShopOdds34, crystalBallSpaceOdds1, crystalBallSpaceOdds2, crystalBallSpaceOdds34, magicLampPrice1, magicLampPrice2, magicLampPrice34, magicLampShopOdds12, magicLampShopOdds34, magicLampSpaceOdds1, magicLampSpaceOdds2, magicLampSpaceOdds34, itemBagPrice1, itemBagPrice2, itemBagPrice34, itemBagShopOdds12, itemBagShopOdds34, itemBagSpaceOdds1, itemBagSpaceOdds2, itemBagSpaceOdds34, mushroomPrice1, mushroomPrice2, mushroomPrice34, mushroomShopOdds12, mushroomShopOdds34, mushroomSpaceOdds1, mushroomSpaceOdds2, mushroomSpaceOdds34, goldenMushroomPrice1, goldenMushroomPrice2, goldenMushroomPrice34, goldenMushroomShopOdds12, goldenMushroomShopOdds34, goldenMushroomSpaceOdds1, goldenMushroomSpaceOdds2, goldenMushroomSpaceOdds34, reverseMushroomPrice1, reverseMushroomPrice2, reverseMushroomPrice34, reverseMushroomShopOdds12, reverseMushroomShopOdds34, reverseMushroomSpaceOdds1, reverseMushroomSpaceOdds2, reverseMushroomSpaceOdds34, poisonMushroomPrice1, poisonMushroomPrice2, poisonMushroomPrice34, poisonMushroomShopOdds12, poisonMushroomShopOdds34, poisonMushroomSpaceOdds1, poisonMushroomSpaceOdds2, poisonMushroomSpaceOdds34, triplePoisonMushroomPrice1, triplePoisonMushroomPrice2, triplePoisonMushroomPrice34, triplePoisonMushroomShopOdds12, triplePoisonMushroomShopOdds34, triplePoisonMushroomSpaceOdds1, triplePoisonMushroomSpaceOdds2, triplePoisonMushroomSpaceOdds34, celluarShopperPrice1, celluarShopperPrice2, celluarShopperPrice34, celluarShopperShopOdds12, celluarShopperShopOdds34, celluarShopperSpaceOdds1, celluarShopperSpaceOdds2, celluarShopperSpaceOdds34, skeletonKeyPrice1, skeletonKeyPrice2, skeletonKeyPrice34, skeletonKeyShopOdds12, skeletonKeyShopOdds34, skeletonKeySpaceOdds1, skeletonKeySpaceOdds2, skeletonKeySpaceOdds34, plunderChestPrice1, plunderChestPrice2, plunderChestPrice34, plunderChestShopOdds12, plunderChestShopOdds34, plunderChestSpaceOdds1, plunderChestSpaceOdds2, plunderChestSpaceOdds34, gaddbrushPrice1, gaddbrushPrice2, gaddbrushPrice34, gaddbrushShopOdds12, gaddbrushShopOdds34, gaddbrushSpaceOdds1, gaddbrushSpaceOdds2, gaddbrushSpaceOdds34, warpBlockPrice1, warpBlockPrice2, warpBlockPrice34, warpBlockShopOdds12, warpBlockShopOdds34, warpBlockSpaceOdds1, warpBlockSpaceOdds2, warpBlockSpaceOdds34, flyGuyPrice1, flyGuyPrice2, flyGuyPrice34, flyGuyShopOdds12, flyGuyShopOdds34, flyGuySpaceOdds1, flyGuySpaceOdds2, flyGuySpaceOdds34, plusBlockPrice1, plusBlockPrice2, plusBlockPrice34, plusBlockShopOdds12, plusBlockShopOdds34, plusBlockSpaceOdds1, plusBlockSpaceOdds2, plusBlockSpaceOdds34, minusBlockPrice1, minusBlockPrice2, minusBlockPrice34, minusBlockShopOdds12, minusBlockShopOdds34, minusBlockSpaceOdds1, minusBlockSpaceOdds2, minusBlockSpaceOdds34, speedBlockPrice1, speedBlockPrice2, speedBlockPrice34, speedBlockShopOdds12, speedBlockShopOdds34, speedBlockSpaceOdds1, speedBlockSpaceOdds2, speedBlockSpaceOdds34, slowBlockPrice1, slowBlockPrice2, slowBlockPrice34, slowBlockShopOdds12, slowBlockShopOdds34, slowBlockSpaceOdds1, slowBlockSpaceOdds2, slowBlockSpaceOdds34, bowserPhonePrice1, bowserPhonePrice2, bowserPhonePrice34, bowserPhoneShopOdds12, bowserPhoneShopOdds34, bowserPhoneSpaceOdds1, bowserPhoneSpaceOdds2, bowserPhoneSpaceOdds34, doubleDipPrice1, doubleDipPrice2, doubleDipPrice34, doubleDipShopOdds12, doubleDipShopOdds34, doubleDipSpaceOdds1, doubleDipSpaceOdds2, doubleDipSpaceOdds34, hiddenBlockCardPrice1, hiddenBlockCardPrice2, hiddenBlockCardPrice34, hiddenBlockCardShopOdds12, hiddenBlockCardShopOdds34, hiddenBlockCardSpaceOdds1, hiddenBlockCardSpaceOdds2, hiddenBlockCardSpaceOdds34, barterBoxPrice1, barterBoxPrice2, barterBoxPrice34, barterBoxShopOdds12, barterBoxShopOdds34, barterBoxSpaceOdds1, barterBoxSpaceOdds2, barterBoxSpaceOdds34, superWarpPipePrice1, superWarpPipePrice2, superWarpPipePrice34, superWarpPipeShopOdds12, superWarpPipeShopOdds34, superWarpPipeSpaceOdds1, superWarpPipeSpaceOdds2, superWarpPipeSpaceOdds34, chanceTimeCharmPrice1, chanceTimeCharmPrice2, chanceTimeCharmPrice34, chanceTimeCharmShopOdds12, chanceTimeCharmShopOdds34, chanceTimeCharmSpaceOdds1, chanceTimeCharmSpaceOdds2, chanceTimeCharmSpaceOdds34, wackyWatchPrice1, wackyWatchPrice2, wackyWatchPrice34, wackyWatchShopOdds12, wackyWatchShopOdds34, wackyWatchSpaceOdds1, wackyWatchSpaceOdds2, wackyWatchSpaceOdds34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def itemsEvent_mp4ItemSpace(miniMushroomPrice1 = "0", miniMushroomPrice2 = "0", miniMushroomPrice34 = "0", miniMushroomShopOdds12 = "0", miniMushroomShopOdds34 = "0", miniMushroomSpaceOdds1 = "0", miniMushroomSpaceOdds2 = "0", miniMushroomSpaceOdds34 = "0", megaMushroomPrice1 = "0", megaMushroomPrice2 = "0", megaMushroomPrice34 = "0", megaMushroomShopOdds12 = "0", megaMushroomShopOdds34 = "0", megaMushroomSpaceOdds1 = "0", megaMushroomSpaceOdds2 = "0", megaMushroomSpaceOdds34 = "0", superMiniMushroomPrice1 = "0", superMiniMushroomPrice2 = "0", superMiniMushroomPrice34 = "0", superMiniMushroomShopOdds12 = "0", superMiniMushroomShopOdds34 = "0", superMiniMushroomSpaceOdds1 = "0", superMiniMushroomSpaceOdds2 = "0", superMiniMushroomSpaceOdds34 = "0", superMegaMushroomPrice1 = "0", superMegaMushroomPrice2 = "0", superMegaMushroomPrice34 = "0", superMegaMushroomShopOdds12 = "0", superMegaMushroomShopOdds34 = "0", superMegaMushroomSpaceOdds1 = "0", superMegaMushroomSpaceOdds2 = "0", superMegaMushroomSpaceOdds34 = "0", miniMegaHammerPrice1 = "0", miniMegaHammerPrice2 = "0", miniMegaHammerPrice34 = "0", miniMegaHammerShopOdds12 = "0", miniMegaHammerShopOdds34 = "0", miniMegaHammerSpaceOdds1 = "0", miniMegaHammerSpaceOdds2 = "0", miniMegaHammerSpaceOdds34 = "0", warpPipePrice1 = "0", warpPipePrice2 = "0", warpPipePrice34 = "0", warpPipeShopOdds12 = "0", warpPipeShopOdds34 = "0", warpPipeSpaceOdds1 = "0", warpPipeSpaceOdds2 = "0", warpPipeSpaceOdds34 = "0", swapCardPrice1 = "0", swapCardPrice2 = "0", swapCardPrice34 = "0", swapCardShopOdds12 = "0", swapCardShopOdds34 = "0", swapCardSpaceOdds1 = "0", swapCardSpaceOdds2 = "0", swapCardSpaceOdds34 = "0", sparkyStickerPrice1 = "0", sparkyStickerPrice2 = "0", sparkyStickerPrice34 = "0", sparkyStickerShopOdds12 = "0", sparkyStickerShopOdds34 = "0", sparkyStickerSpaceOdds1 = "0", sparkyStickerSpaceOdds2 = "0", sparkyStickerSpaceOdds34 = "0", gaddlightPrice1 = "0", gaddlightPrice2 = "0", gaddlightPrice34 = "0", gaddlightShopOdds12 = "0", gaddlightShopOdds34 = "0", gaddlightSpaceOdds1 = "0", gaddlightSpaceOdds2 = "0", gaddlightSpaceOdds34 = "0", chompCallPrice1 = "0", chompCallPrice2 = "0", chompCallPrice34 = "0", chompCallShopOdds12 = "0", chompCallShopOdds34 = "0", chompCallSpaceOdds1 = "0", chompCallSpaceOdds2 = "0", chompCallSpaceOdds34 = "0", bowserSuitPrice1 = "0", bowserSuitPrice2 = "0", bowserSuitPrice34 = "0", bowserSuitShopOdds12 = "0", bowserSuitShopOdds34 = "0", bowserSuitSpaceOdds1 = "0", bowserSuitSpaceOdds2 = "0", bowserSuitSpaceOdds34 = "0", crystalBallPrice1 = "0", crystalBallPrice2 = "0", crystalBallPrice34 = "0", crystalBallShopOdds12 = "0", crystalBallShopOdds34 = "0", crystalBallSpaceOdds1 = "0", crystalBallSpaceOdds2 = "0", crystalBallSpaceOdds34 = "0", magicLampPrice1 = "0", magicLampPrice2 = "0", magicLampPrice34 = "0", magicLampShopOdds12 = "0", magicLampShopOdds34 = "0", magicLampSpaceOdds1 = "0", magicLampSpaceOdds2 = "0", magicLampSpaceOdds34 = "0", itemBagPrice1 = "0", itemBagPrice2 = "0", itemBagPrice34 = "0", itemBagShopOdds12 = "0", itemBagShopOdds34 = "0", itemBagSpaceOdds1 = "0", itemBagSpaceOdds2 = "0", itemBagSpaceOdds34 = "0"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    miniMushroomPrice1 = get_capsule_value(miniMushroomPrice1) or "0"
    miniMushroomPrice2 = get_capsule_value(miniMushroomPrice2) or "0"
    miniMushroomPrice34 = get_capsule_value(miniMushroomPrice34) or "0"
    miniMushroomShopOdds12 = get_capsule_value(miniMushroomShopOdds12) or "0"
    miniMushroomShopOdds34 = get_capsule_value(miniMushroomShopOdds34) or "0"
    miniMushroomSpaceOdds1 = get_capsule_value(miniMushroomSpaceOdds1) or "0"
    miniMushroomSpaceOdds2 = get_capsule_value(miniMushroomSpaceOdds2) or "0"
    miniMushroomSpaceOdds34 = get_capsule_value(miniMushroomSpaceOdds34) or "0"
    megaMushroomPrice1 = get_capsule_value(megaMushroomPrice1) or "0"
    megaMushroomPrice2 = get_capsule_value(megaMushroomPrice2) or "0"
    megaMushroomPrice34 = get_capsule_value(megaMushroomPrice34) or "0"
    megaMushroomShopOdds12 = get_capsule_value(megaMushroomShopOdds12) or "0"
    megaMushroomShopOdds34 = get_capsule_value(megaMushroomShopOdds34) or "0"
    megaMushroomSpaceOdds1 = get_capsule_value(megaMushroomSpaceOdds1) or "0"
    megaMushroomSpaceOdds2 = get_capsule_value(megaMushroomSpaceOdds2) or "0"
    megaMushroomSpaceOdds34 = get_capsule_value(megaMushroomSpaceOdds34) or "0"
    superMiniMushroomPrice1 = get_capsule_value(superMiniMushroomPrice1) or "0"
    superMiniMushroomPrice2 = get_capsule_value(superMiniMushroomPrice2) or "0"
    superMiniMushroomPrice34 = get_capsule_value(superMiniMushroomPrice34) or "0"
    superMiniMushroomShopOdds12 = get_capsule_value(superMiniMushroomShopOdds12) or "0"
    superMiniMushroomShopOdds34 = get_capsule_value(superMiniMushroomShopOdds34) or "0"
    superMiniMushroomSpaceOdds1 = get_capsule_value(superMiniMushroomSpaceOdds1) or "0"
    superMiniMushroomSpaceOdds2 = get_capsule_value(superMiniMushroomSpaceOdds2) or "0"
    superMiniMushroomSpaceOdds34 = get_capsule_value(superMiniMushroomSpaceOdds34) or "0"
    superMegaMushroomPrice1 = get_capsule_value(superMegaMushroomPrice1) or "0"
    superMegaMushroomPrice2 = get_capsule_value(superMegaMushroomPrice2) or "0"
    superMegaMushroomPrice34 = get_capsule_value(superMegaMushroomPrice34) or "0"
    superMegaMushroomShopOdds12 = get_capsule_value(superMegaMushroomShopOdds12) or "0"
    superMegaMushroomShopOdds34 = get_capsule_value(superMegaMushroomShopOdds34) or "0"
    superMegaMushroomSpaceOdds1 = get_capsule_value(superMegaMushroomSpaceOdds1) or "0"
    superMegaMushroomSpaceOdds2 = get_capsule_value(superMegaMushroomSpaceOdds2) or "0"
    superMegaMushroomSpaceOdds34 = get_capsule_value(superMegaMushroomSpaceOdds34) or "0"
    miniMegaHammerPrice1 = get_capsule_value(miniMegaHammerPrice1) or "0"
    miniMegaHammerPrice2 = get_capsule_value(miniMegaHammerPrice2) or "0"
    miniMegaHammerPrice34 = get_capsule_value(miniMegaHammerPrice34) or "0"
    miniMegaHammerShopOdds12 = get_capsule_value(miniMegaHammerShopOdds12) or "0"
    miniMegaHammerShopOdds34 = get_capsule_value(miniMegaHammerShopOdds34) or "0"
    miniMegaHammerSpaceOdds1 = get_capsule_value(miniMegaHammerSpaceOdds1) or "0"
    miniMegaHammerSpaceOdds2 = get_capsule_value(miniMegaHammerSpaceOdds2) or "0"
    miniMegaHammerSpaceOdds34 = get_capsule_value(miniMegaHammerSpaceOdds34) or "0"
    warpPipePrice1 = get_capsule_value(warpPipePrice1) or "0"
    warpPipePrice2 = get_capsule_value(warpPipePrice2) or "0"
    warpPipePrice34 = get_capsule_value(warpPipePrice34) or "0"
    warpPipeShopOdds12 = get_capsule_value(warpPipeShopOdds12) or "0"
    warpPipeShopOdds34 = get_capsule_value(warpPipeShopOdds34) or "0"
    warpPipeSpaceOdds1 = get_capsule_value(warpPipeSpaceOdds1) or "0"
    warpPipeSpaceOdds2 = get_capsule_value(warpPipeSpaceOdds2) or "0"
    warpPipeSpaceOdds34 = get_capsule_value(warpPipeSpaceOdds34) or "0"
    swapCardPrice1 = get_capsule_value(swapCardPrice1) or "0"
    swapCardPrice2 = get_capsule_value(swapCardPrice2) or "0"
    swapCardPrice34 = get_capsule_value(swapCardPrice34) or "0"
    swapCardShopOdds12 = get_capsule_value(swapCardShopOdds12) or "0"
    swapCardShopOdds34 = get_capsule_value(swapCardShopOdds34) or "0"
    swapCardSpaceOdds1 = get_capsule_value(swapCardSpaceOdds1) or "0"
    swapCardSpaceOdds2 = get_capsule_value(swapCardSpaceOdds2) or "0"
    swapCardSpaceOdds34 = get_capsule_value(swapCardSpaceOdds34) or "0"
    sparkyStickerPrice1 = get_capsule_value(sparkyStickerPrice1) or "0"
    sparkyStickerPrice2 = get_capsule_value(sparkyStickerPrice2) or "0"
    sparkyStickerPrice34 = get_capsule_value(sparkyStickerPrice34) or "0"
    sparkyStickerShopOdds12 = get_capsule_value(sparkyStickerShopOdds12) or "0"
    sparkyStickerShopOdds34 = get_capsule_value(sparkyStickerShopOdds34) or "0"
    sparkyStickerSpaceOdds1 = get_capsule_value(sparkyStickerSpaceOdds1) or "0"
    sparkyStickerSpaceOdds2 = get_capsule_value(sparkyStickerSpaceOdds2) or "0"
    sparkyStickerSpaceOdds34 = get_capsule_value(sparkyStickerSpaceOdds34) or "0"
    gaddlightPrice1 = get_capsule_value(gaddlightPrice1) or "0"    
    gaddlightPrice2 = get_capsule_value(gaddlightPrice2) or "0"
    gaddlightPrice34 = get_capsule_value(gaddlightPrice2) or "0"    
    gaddlightShopOdds12 = get_capsule_value(gaddlightShopOdds12) or "0"
    gaddlightShopOdds34 = get_capsule_value(gaddlightShopOdds34) or "0"
    gaddlightSpaceOdds1 = get_capsule_value(gaddlightSpaceOdds1) or "0"
    gaddlightSpaceOdds2 = get_capsule_value(gaddlightSpaceOdds2) or "0"
    gaddlightSpaceOdds34 = get_capsule_value(gaddlightSpaceOdds34) or "0"
    chompCallPrice1 = get_capsule_value(chompCallPrice1) or "0"
    chompCallPrice2 = get_capsule_value(chompCallPrice2) or "0" 
    chompCallPrice34 = get_capsule_value(chompCallPrice34) or "0"
    chompCallShopOdds12 = get_capsule_value(chompCallShopOdds12) or "0"
    chompCallShopOdds34 = get_capsule_value(chompCallShopOdds34) or "0"
    chompCallSpaceOdds1 = get_capsule_value(chompCallSpaceOdds1) or "0"
    chompCallSpaceOdds2 = get_capsule_value(chompCallSpaceOdds2) or "0"
    chompCallSpaceOdds34 = get_capsule_value(chompCallSpaceOdds34) or "0"
    bowserSuitPrice1 = get_capsule_value(bowserSuitPrice1) or "0"
    bowserSuitPrice2 = get_capsule_value(bowserSuitPrice2) or "0"
    bowserSuitPrice34 = get_capsule_value(bowserSuitPrice34) or "0"
    bowserSuitShopOdds12 = get_capsule_value(bowserSuitShopOdds12) or "0"
    bowserSuitShopOdds34 = get_capsule_value(bowserSuitShopOdds34) or "0"
    bowserSuitSpaceOdds1 = get_capsule_value(bowserSuitSpaceOdds1) or "0"
    bowserSuitSpaceOdds2 = get_capsule_value(bowserSuitSpaceOdds2) or "0"
    bowserSuitSpaceOdds34 = get_capsule_value(bowserSuitSpaceOdds34) or "0"
    crystalBallPrice1 = get_capsule_value(crystalBallPrice1) or "0"
    crystalBallPrice2 = get_capsule_value(crystalBallPrice2) or "0"
    crystalBallPrice34 = get_capsule_value(crystalBallPrice34) or "0"
    crystalBallShopOdds12 = get_capsule_value(crystalBallShopOdds12) or "0"
    crystalBallShopOdds34 = get_capsule_value(crystalBallShopOdds34) or "0"
    crystalBallSpaceOdds1 = get_capsule_value(crystalBallSpaceOdds1) or "0"
    crystalBallSpaceOdds2 = get_capsule_value(crystalBallSpaceOdds2) or "0"
    crystalBallSpaceOdds34 = get_capsule_value(crystalBallSpaceOdds34) or "0"
    magicLampPrice1 = get_capsule_value(magicLampPrice1) or "0"
    magicLampPrice2 = get_capsule_value(magicLampPrice2) or "0"
    magicLampPrice34 = get_capsule_value(magicLampPrice34) or "0"
    magicLampShopOdds12 = get_capsule_value(magicLampShopOdds12) or "0"
    magicLampShopOdds34 = get_capsule_value(magicLampShopOdds34) or "0"
    magicLampSpaceOdds1 = get_capsule_value(magicLampSpaceOdds1) or "0"
    magicLampSpaceOdds2 = get_capsule_value(magicLampSpaceOdds2) or "0"
    magicLampSpaceOdds34 = get_capsule_value(magicLampSpaceOdds34) or "0"
    itemBagPrice1 = get_capsule_value(itemBagPrice1) or "0"
    itemBagPrice2 = get_capsule_value(itemBagPrice2) or "0"
    itemBagPrice34 = get_capsule_value(itemBagPrice34) or "0"
    itemBagShopOdds12 = get_capsule_value(itemBagShopOdds12) or "0"
    itemBagShopOdds34 = get_capsule_value(itemBagShopOdds34) or "0"
    itemBagSpaceOdds1 = get_capsule_value(itemBagSpaceOdds1) or "0"
    itemBagSpaceOdds2 = get_capsule_value(itemBagSpaceOdds2) or "0"
    itemBagSpaceOdds34 = get_capsule_value(itemBagSpaceOdds34) or "0"

    # Weights lists
    shopOdds12 = [
        miniMushroomShopOdds12,
        megaMushroomShopOdds12,
        superMiniMushroomShopOdds12,
        superMegaMushroomShopOdds12,
        miniMegaHammerShopOdds12,
        warpPipeShopOdds12,
        swapCardShopOdds12,
        sparkyStickerShopOdds12,
        gaddlightShopOdds12,
        chompCallShopOdds12,
        bowserSuitShopOdds12,
        crystalBallShopOdds12,
        magicLampShopOdds12,
        itemBagShopOdds12,
    ]

    shopOdds34 = [
        miniMushroomShopOdds34,
        megaMushroomShopOdds34,
        superMiniMushroomShopOdds34,
        superMegaMushroomShopOdds34,
        miniMegaHammerShopOdds34,
        warpPipeShopOdds34,
        swapCardShopOdds34,
        sparkyStickerShopOdds34,
        gaddlightShopOdds34,
        chompCallShopOdds34,
        bowserSuitShopOdds34,
        crystalBallShopOdds34,
        magicLampShopOdds34,
        itemBagShopOdds34,
    ]

    spaceOdds1 = [
        miniMushroomSpaceOdds1,
        megaMushroomSpaceOdds1,
        superMiniMushroomSpaceOdds1,
        superMegaMushroomSpaceOdds1,
        miniMegaHammerSpaceOdds1,
        warpPipeSpaceOdds1,
        swapCardSpaceOdds1,
        sparkyStickerSpaceOdds1,
        gaddlightSpaceOdds1,
        chompCallSpaceOdds1,
        bowserSuitSpaceOdds1,
        crystalBallSpaceOdds1,
        magicLampSpaceOdds1,
        itemBagSpaceOdds1,
    ]

    spaceOdds2 = [
        miniMushroomSpaceOdds2,
        megaMushroomSpaceOdds2,
        superMiniMushroomSpaceOdds2,
        superMegaMushroomSpaceOdds2,
        miniMegaHammerSpaceOdds2,
        warpPipeSpaceOdds2,
        swapCardSpaceOdds2,
        sparkyStickerSpaceOdds2,
        gaddlightSpaceOdds2,
        chompCallSpaceOdds2,
        bowserSuitSpaceOdds2,
        crystalBallSpaceOdds2,
        magicLampSpaceOdds2,
        itemBagSpaceOdds2,
    ]

    spaceOdds34 = [
        miniMushroomSpaceOdds34,
        megaMushroomSpaceOdds34,
        superMiniMushroomSpaceOdds34,
        superMegaMushroomSpaceOdds34,
        miniMegaHammerSpaceOdds34,
        warpPipeSpaceOdds34,
        swapCardSpaceOdds34,
        sparkyStickerSpaceOdds34,
        gaddlightSpaceOdds34,
        chompCallSpaceOdds34,
        bowserSuitSpaceOdds34,
        crystalBallSpaceOdds34,
        magicLampSpaceOdds34,
        itemBagSpaceOdds34,
    ]

    shopOdds12Weights = sum(int(weight) if weight else 0 for weight in shopOdds12)
    shopOdds34Weights = sum(int(weight) if weight else 0 for weight in shopOdds34)
    spaceOdds1Weights = sum(int(weight) if weight else 0 for weight in spaceOdds1)
    spaceOdds2Weights = sum(int(weight) if weight else 0 for weight in spaceOdds2)
    spaceOdds34Weights = sum(int(weight) if weight else 0 for weight in spaceOdds34)

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

    # Calculate weights for shop odds 34
    miniMushroomSpaceOdds34 = calculateWeight(miniMushroomSpaceOdds34, shopOdds34Weights)
    megaMushroomSpaceOdds34 = calculateWeight(megaMushroomSpaceOdds34, shopOdds34Weights)
    superMiniMushroomSpaceOdds34 = calculateWeight(superMiniMushroomSpaceOdds34, shopOdds34Weights)
    superMegaMushroomSpaceOdds34 = calculateWeight(superMegaMushroomSpaceOdds34, shopOdds34Weights)
    miniMegaHammerSpaceOdds34 = calculateWeight(miniMegaHammerSpaceOdds34, shopOdds34Weights)
    warpPipeSpaceOdds34 = calculateWeight(warpPipeSpaceOdds34, shopOdds34Weights)
    swapCardSpaceOdds34 = calculateWeight(swapCardSpaceOdds34, shopOdds34Weights)
    sparkyStickerSpaceOdds34 = calculateWeight(sparkyStickerSpaceOdds34, shopOdds34Weights)
    gaddlightSpaceOdds34 = calculateWeight(gaddlightSpaceOdds34, shopOdds34Weights)
    chompCallSpaceOdds34 = calculateWeight(chompCallSpaceOdds34, shopOdds34Weights)
    bowserSuitSpaceOdds34 = calculateWeight(bowserSuitSpaceOdds34, shopOdds34Weights)
    crystalBallSpaceOdds34 = calculateWeight(crystalBallSpaceOdds34, shopOdds34Weights)
    magicLampSpaceOdds34 = calculateWeight(magicLampSpaceOdds34, shopOdds34Weights)
    itemBagSpaceOdds34 = calculateWeight(itemBagSpaceOdds34, shopOdds34Weights)

    # Calculate weights for shop odds 12
    miniMushroomShopOdds12 = calculateWeight(miniMushroomShopOdds12, shopOdds12Weights)
    megaMushroomShopOdds12 = calculateWeight(megaMushroomShopOdds12, shopOdds12Weights)
    superMiniMushroomShopOdds12 = calculateWeight(superMiniMushroomShopOdds12, shopOdds12Weights)
    superMegaMushroomShopOdds12 = calculateWeight(superMegaMushroomShopOdds12, shopOdds12Weights)
    miniMegaHammerShopOdds12 = calculateWeight(miniMegaHammerShopOdds12, shopOdds12Weights)
    warpPipeShopOdds12 = calculateWeight(warpPipeShopOdds12, shopOdds12Weights)
    swapCardShopOdds12 = calculateWeight(swapCardShopOdds12, shopOdds12Weights)
    sparkyStickerShopOdds12 = calculateWeight(sparkyStickerShopOdds12, shopOdds12Weights)
    gaddlightShopOdds12 = calculateWeight(gaddlightShopOdds12, shopOdds12Weights)
    chompCallShopOdds12 = calculateWeight(chompCallShopOdds12, shopOdds12Weights)
    bowserSuitShopOdds12 = calculateWeight(bowserSuitShopOdds12, shopOdds12Weights)
    crystalBallShopOdds12 = calculateWeight(crystalBallShopOdds12, shopOdds12Weights)
    magicLampShopOdds12 = calculateWeight(magicLampShopOdds12, shopOdds12Weights)
    itemBagShopOdds12 = calculateWeight(itemBagShopOdds12, shopOdds12Weights)

   # Calculate weights for space odds 1
    miniMushroomSpaceOdds1 = calculateWeight(miniMushroomSpaceOdds1, spaceOdds1Weights)
    megaMushroomSpaceOdds1 = calculateWeight(megaMushroomSpaceOdds1, spaceOdds1Weights)
    superMiniMushroomSpaceOdds1 = calculateWeight(superMiniMushroomSpaceOdds1, spaceOdds1Weights)
    superMegaMushroomSpaceOdds1 = calculateWeight(superMegaMushroomSpaceOdds1, spaceOdds1Weights)
    miniMegaHammerSpaceOdds1 = calculateWeight(miniMegaHammerSpaceOdds1, spaceOdds1Weights)
    warpPipeSpaceOdds1 = calculateWeight(warpPipeSpaceOdds1, spaceOdds1Weights)
    swapCardSpaceOdds1 = calculateWeight(swapCardSpaceOdds1, spaceOdds1Weights)
    sparkyStickerSpaceOdds1 = calculateWeight(sparkyStickerSpaceOdds1, spaceOdds1Weights)
    gaddlightSpaceOdds1 = calculateWeight(gaddlightSpaceOdds1, spaceOdds1Weights)
    chompCallSpaceOdds1 = calculateWeight(chompCallSpaceOdds1, spaceOdds1Weights)
    bowserSuitSpaceOdds1 = calculateWeight(bowserSuitSpaceOdds1, spaceOdds1Weights)
    crystalBallSpaceOdds1 = calculateWeight(crystalBallSpaceOdds1, spaceOdds1Weights)
    magicLampSpaceOdds1 = calculateWeight(magicLampSpaceOdds1, spaceOdds1Weights)
    itemBagSpaceOdds1 = calculateWeight(itemBagSpaceOdds1, spaceOdds1Weights)


    # Calculate weights for space odds 2
    miniMushroomSpaceOdds2 = calculateWeight(miniMushroomSpaceOdds2, spaceOdds2Weights)
    megaMushroomSpaceOdds2 = calculateWeight(megaMushroomSpaceOdds2, spaceOdds2Weights)
    superMiniMushroomSpaceOdds2 = calculateWeight(superMiniMushroomSpaceOdds2, spaceOdds2Weights)
    superMegaMushroomSpaceOdds2 = calculateWeight(superMegaMushroomSpaceOdds2, spaceOdds2Weights)
    miniMegaHammerSpaceOdds2 = calculateWeight(miniMegaHammerSpaceOdds2, spaceOdds2Weights)
    warpPipeSpaceOdds2 = calculateWeight(warpPipeSpaceOdds2, spaceOdds2Weights)
    swapCardSpaceOdds2 = calculateWeight(swapCardSpaceOdds2, spaceOdds2Weights)
    sparkyStickerSpaceOdds2 = calculateWeight(sparkyStickerSpaceOdds2, spaceOdds2Weights)
    gaddlightSpaceOdds2 = calculateWeight(gaddlightSpaceOdds2, spaceOdds2Weights)
    chompCallSpaceOdds2 = calculateWeight(chompCallSpaceOdds2, spaceOdds2Weights)
    bowserSuitSpaceOdds2 = calculateWeight(bowserSuitSpaceOdds2, spaceOdds2Weights)
    crystalBallSpaceOdds2 = calculateWeight(crystalBallSpaceOdds2, spaceOdds2Weights)
    magicLampSpaceOdds2 = calculateWeight(magicLampSpaceOdds2, spaceOdds2Weights)
    itemBagSpaceOdds2 = calculateWeight(itemBagSpaceOdds2, spaceOdds2Weights)

    # Calculate weights for space odds 34
    miniMushroomSpaceOdds34 = calculateWeight(miniMushroomSpaceOdds34, spaceOdds34Weights)
    megaMushroomSpaceOdds34 = calculateWeight(megaMushroomSpaceOdds34, spaceOdds34Weights)
    superMiniMushroomSpaceOdds34 = calculateWeight(superMiniMushroomSpaceOdds34, spaceOdds34Weights)
    superMegaMushroomSpaceOdds34 = calculateWeight(superMegaMushroomSpaceOdds34, spaceOdds34Weights)
    miniMegaHammerSpaceOdds34 = calculateWeight(miniMegaHammerSpaceOdds34, spaceOdds34Weights)
    warpPipeSpaceOdds34 = calculateWeight(warpPipeSpaceOdds34, spaceOdds34Weights)
    swapCardSpaceOdds34 = calculateWeight(swapCardSpaceOdds34, spaceOdds34Weights)
    sparkyStickerSpaceOdds34 = calculateWeight(sparkyStickerSpaceOdds34, spaceOdds34Weights)
    gaddlightSpaceOdds34 = calculateWeight(gaddlightSpaceOdds34, spaceOdds34Weights)
    chompCallSpaceOdds34 = calculateWeight(chompCallSpaceOdds34, spaceOdds34Weights)
    bowserSuitSpaceOdds34 = calculateWeight(bowserSuitSpaceOdds34, spaceOdds34Weights)
    crystalBallSpaceOdds34 = calculateWeight(crystalBallSpaceOdds34, spaceOdds34Weights)
    magicLampSpaceOdds34 = calculateWeight(magicLampSpaceOdds34, spaceOdds34Weights)
    itemBagSpaceOdds34 = calculateWeight(itemBagSpaceOdds34, spaceOdds34Weights)

    # Redefine Weights lists
    shopOdds12 = [
        miniMushroomShopOdds12,
        megaMushroomShopOdds12,
        superMiniMushroomShopOdds12,
        superMegaMushroomShopOdds12,
        miniMegaHammerShopOdds12,
        warpPipeShopOdds12,
        swapCardShopOdds12,
        sparkyStickerShopOdds12,
        gaddlightShopOdds12,
        chompCallShopOdds12,
        bowserSuitShopOdds12,
        crystalBallShopOdds12,
        magicLampShopOdds12,
        itemBagShopOdds12,
    ]

    shopOdds34 = [
        miniMushroomShopOdds34,
        megaMushroomShopOdds34,
        superMiniMushroomShopOdds34,
        superMegaMushroomShopOdds34,
        miniMegaHammerShopOdds34,
        warpPipeShopOdds34,
        swapCardShopOdds34,
        sparkyStickerShopOdds34,
        gaddlightShopOdds34,
        chompCallShopOdds34,
        bowserSuitShopOdds34,
        crystalBallShopOdds34,
        magicLampShopOdds34,
        itemBagShopOdds34,
    ]

    spaceOdds1 = [
        miniMushroomSpaceOdds1,
        megaMushroomSpaceOdds1,
        superMiniMushroomSpaceOdds1,
        superMegaMushroomSpaceOdds1,
        miniMegaHammerSpaceOdds1,
        warpPipeSpaceOdds1,
        swapCardSpaceOdds1,
        sparkyStickerSpaceOdds1,
        gaddlightSpaceOdds1,
        chompCallSpaceOdds1,
        bowserSuitSpaceOdds1,
        crystalBallSpaceOdds1,
        magicLampSpaceOdds1,
        itemBagSpaceOdds1,
    ]

    spaceOdds2 = [
        miniMushroomSpaceOdds2,
        megaMushroomSpaceOdds2,
        superMiniMushroomSpaceOdds2,
        superMegaMushroomSpaceOdds2,
        miniMegaHammerSpaceOdds2,
        warpPipeSpaceOdds2,
        swapCardSpaceOdds2,
        sparkyStickerSpaceOdds2,
        gaddlightSpaceOdds2,
        chompCallSpaceOdds2,
        bowserSuitSpaceOdds2,
        crystalBallSpaceOdds2,
        magicLampSpaceOdds2,
        itemBagSpaceOdds2,
    ]

    spaceOdds34 = [
        miniMushroomSpaceOdds34,
        megaMushroomSpaceOdds34,
        superMiniMushroomSpaceOdds34,
        superMegaMushroomSpaceOdds34,
        miniMegaHammerSpaceOdds34,
        warpPipeSpaceOdds34,
        swapCardSpaceOdds34,
        sparkyStickerSpaceOdds34,
        gaddlightSpaceOdds34,
        chompCallSpaceOdds34,
        bowserSuitSpaceOdds34,
        crystalBallSpaceOdds34,
        magicLampSpaceOdds34,
        itemBagSpaceOdds34,
    ]

    shopOdds12Weights = sum(int(weight) for weight in shopOdds12 if weight)
    shopOdds34Weights = sum(int(weight) for weight in shopOdds34 if weight)
    spaceOdds1Weights = sum(int(weight) for weight in spaceOdds1 if weight)
    spaceOdds2Weights = sum(int(weight) for weight in spaceOdds2 if weight)
    spaceOdds34Weights = sum(int(weight) for weight in spaceOdds34 if weight)

    if int(spaceOdds1Weights) < 101:
        spaceOdds1Max = max(zip(spaceOdds1, spaceOdds1), key=lambda tuple: int(tuple[1]))[0]

    if int(spaceOdds34Weights) < 101:
        spaceOdds34Max = max(zip(spaceOdds34, spaceOdds34), key=lambda tuple: int(tuple[1]))[0]

    if int(shopOdds12Weights) < 101:
        shopOdds12Max = max(zip(shopOdds12, shopOdds12), key=lambda tuple: int(tuple[1]))[0]

    if int(spaceOdds2Weights) < 101:
        spaceOdds2Max = max(zip(spaceOdds2, spaceOdds2), key=lambda tuple: int(tuple[1]))[0]

    if int(shopOdds34Weights) < 101:
        shopOdds34Max = max(zip(shopOdds34, shopOdds34), key=lambda tuple: int(tuple[1]))[0]

    if shopOdds12Max == 'miniMushroomShopOdds12':
        miniMushroomShopOdds12 += (100 - miniMushroomShopOdds12)

    if shopOdds12Max == 'megaMushroomShopOdds12':
        megaMushroomShopOdds12 += (100 - megaMushroomShopOdds12)

    if shopOdds12Max == 'superMiniMushroomShopOdds12':
        superMiniMushroomShopOdds12 += (100 - superMiniMushroomShopOdds12)

    if shopOdds12Max == 'superMegaMushroomShopOdds12':
        superMegaMushroomShopOdds12 += (100 - superMegaMushroomShopOdds12)

    if shopOdds12Max == 'miniMegaHammerShopOdds12':
        miniMegaHammerShopOdds12 += (100 - miniMegaHammerShopOdds12)

    if shopOdds12Max == 'warpPipeShopOdds12':
        warpPipeShopOdds12 += (100 - warpPipeShopOdds12)

    if shopOdds12Max == 'swapCardShopOdds12':
        swapCardShopOdds12 += (100 - swapCardShopOdds12)

    if shopOdds12Max == 'sparkyStickerShopOdds12':
        sparkyStickerShopOdds12 += (100 - sparkyStickerShopOdds12)

    if shopOdds12Max == 'gaddlightShopOdds12':
        gaddlightShopOdds12 += (100 - gaddlightShopOdds12)

    if shopOdds12Max == 'chompCallShopOdds12':
        chompCallShopOdds12 += (100 - chompCallShopOdds12)

    if shopOdds12Max == 'bowserSuitShopOdds12':
        bowserSuitShopOdds12 += (100 - bowserSuitShopOdds12)

    if shopOdds12Max == 'crystalBallShopOdds12':
        crystalBallShopOdds12 += (100 - crystalBallShopOdds12)

    if shopOdds12Max == 'magicLampShopOdds12':
        magicLampShopOdds12 += (100 - magicLampShopOdds12)

    if shopOdds12Max == 'itemBagShopOdds12':
        itemBagShopOdds12 += (100 - itemBagShopOdds12)

    if shopOdds34Max == 'miniMushroomShopOdds34':
        miniMushroomShopOdds34 += (100 - miniMushroomShopOdds34)

    if shopOdds34Max == 'megaMushroomShopOdds34':
        megaMushroomShopOdds34 += (100 - megaMushroomShopOdds34)

    if shopOdds34Max == 'superMiniMushroomShopOdds34':
        superMiniMushroomShopOdds34 += (100 - superMiniMushroomShopOdds34)

    if shopOdds34Max == 'superMegaMushroomShopOdds34':
        superMegaMushroomShopOdds34 += (100 - superMegaMushroomShopOdds34)

    if shopOdds34Max == 'miniMegaHammerShopOdds34':
        miniMegaHammerShopOdds34 += (100 - miniMegaHammerShopOdds34)

    if shopOdds34Max == 'warpPipeShopOdds34':
        warpPipeShopOdds34 += (100 - warpPipeShopOdds34)

    if shopOdds34Max == 'swapCardShopOdds34':
        swapCardShopOdds34 += (100 - swapCardShopOdds34)

    if shopOdds34Max == 'sparkyStickerShopOdds34':
        sparkyStickerShopOdds34 += (100 - sparkyStickerShopOdds34)

    if shopOdds34Max == 'gaddlightShopOdds34':
        gaddlightShopOdds34 += (100 - gaddlightShopOdds34)

    if shopOdds34Max == 'chompCallShopOdds34':
        chompCallShopOdds34 += (100 - chompCallShopOdds34)

    if shopOdds34Max == 'bowserSuitShopOdds34':
        bowserSuitShopOdds34 += (100 - bowserSuitShopOdds34)

    if shopOdds34Max == 'crystalBallShopOdds34':
        crystalBallShopOdds34 += (100 - crystalBallShopOdds34)

    if shopOdds34Max == 'magicLampShopOdds34':
        magicLampShopOdds34 += (100 - magicLampShopOdds34)

    if shopOdds34Max == 'itemBagShopOdds34':
        itemBagShopOdds34 += (100 - itemBagShopOdds34)

    if spaceOdds1Max == 'miniMushroomSpaceOdds1':
        miniMushroomSpaceOdds1 += (100 - miniMushroomSpaceOdds1)

    if spaceOdds1Max == 'megaMushroomSpaceOdds1':
        megaMushroomSpaceOdds1 += (100 - megaMushroomSpaceOdds1)

    if spaceOdds1Max == 'superMiniMushroomSpaceOdds1':
        superMiniMushroomSpaceOdds1 += (100 - superMiniMushroomSpaceOdds1)

    if spaceOdds1Max == 'superMegaMushroomSpaceOdds1':
        superMegaMushroomSpaceOdds1 += (100 - superMegaMushroomSpaceOdds1)

    if spaceOdds1Max == 'miniMegaHammerSpaceOdds1':
        miniMegaHammerSpaceOdds1 += (100 - miniMegaHammerSpaceOdds1)

    if spaceOdds1Max == 'warpPipeSpaceOdds1':
        warpPipeSpaceOdds1 += (100 - warpPipeSpaceOdds1)

    if spaceOdds1Max == 'swapCardSpaceOdds1':
        swapCardSpaceOdds1 += (100 - swapCardSpaceOdds1)

    if spaceOdds1Max == 'sparkyStickerSpaceOdds1':
        sparkyStickerSpaceOdds1 += (100 - sparkyStickerSpaceOdds1)

    if spaceOdds1Max == 'gaddlightSpaceOdds1':
        gaddlightSpaceOdds1 += (100 - gaddlightSpaceOdds1)

    if spaceOdds1Max == 'chompCallSpaceOdds1':
        chompCallSpaceOdds1 += (100 - chompCallSpaceOdds1)

    if spaceOdds1Max == 'bowserSuitSpaceOdds1':
        bowserSuitSpaceOdds1 += (100 - bowserSuitSpaceOdds1)

    if spaceOdds1Max == 'crystalBallSpaceOdds1':
        crystalBallSpaceOdds1 += (100 - crystalBallSpaceOdds1)

    if spaceOdds1Max == 'magicLampSpaceOdds1':
        magicLampSpaceOdds1 += (100 - magicLampSpaceOdds1)

    if spaceOdds1Max == 'itemBagSpaceOdds1':
        itemBagSpaceOdds1 += (100 - itemBagSpaceOdds1)

    if spaceOdds2Max == 'miniMushroomSpaceOdds2':
        miniMushroomSpaceOdds2 += (100 - miniMushroomSpaceOdds2)

    if spaceOdds2Max == 'megaMushroomSpaceOdds2':
        megaMushroomSpaceOdds2 += (100 - megaMushroomSpaceOdds2)

    if spaceOdds2Max == 'superMiniMushroomSpaceOdds2':
        superMiniMushroomSpaceOdds2 += (100 - superMiniMushroomSpaceOdds2)

    if spaceOdds2Max == 'superMegaMushroomSpaceOdds2':
        superMegaMushroomSpaceOdds2 += (100 - superMegaMushroomSpaceOdds2)

    if spaceOdds2Max == 'miniMegaHammerSpaceOdds2':
        miniMegaHammerSpaceOdds2 += (100 - miniMegaHammerSpaceOdds2)

    if spaceOdds2Max == 'warpPipeSpaceOdds2':
        warpPipeSpaceOdds2 += (100 - warpPipeSpaceOdds2)

    if spaceOdds2Max == 'swapCardSpaceOdds2':
        swapCardSpaceOdds2 += (100 - swapCardSpaceOdds2)

    if spaceOdds2Max == 'sparkyStickerSpaceOdds2':
        sparkyStickerSpaceOdds2 += (100 - sparkyStickerSpaceOdds2)

    if spaceOdds2Max == 'gaddlightSpaceOdds2':
        gaddlightSpaceOdds2 += (100 - gaddlightSpaceOdds2)

    if spaceOdds2Max == 'chompCallSpaceOdds2':
        chompCallSpaceOdds2 += (100 - chompCallSpaceOdds2)

    if spaceOdds2Max == 'bowserSuitSpaceOdds2':
        bowserSuitSpaceOdds2 += (100 - bowserSuitSpaceOdds2)

    if spaceOdds2Max == 'crystalBallSpaceOdds2':
        crystalBallSpaceOdds2 += (100 - crystalBallSpaceOdds2)

    if spaceOdds2Max == 'magicLampSpaceOdds2':
        magicLampSpaceOdds2 += (100 - magicLampSpaceOdds2)

    if spaceOdds2Max == 'itemBagSpaceOdds2':
        itemBagSpaceOdds2 += (100 - itemBagSpaceOdds2)

    if spaceOdds34Max == 'miniMushroomSpaceOdds34':
        miniMushroomSpaceOdds34 += (100 - miniMushroomSpaceOdds34)

    if spaceOdds34Max == 'megaMushroomSpaceOdds34':
        megaMushroomSpaceOdds34 += (100 - megaMushroomSpaceOdds34)

    if spaceOdds34Max == 'superMiniMushroomSpaceOdds34':
        superMiniMushroomSpaceOdds34 += (100 - superMiniMushroomSpaceOdds34)

    if spaceOdds34Max == 'superMegaMushroomSpaceOdds34':
        superMegaMushroomSpaceOdds34 += (100 - superMegaMushroomSpaceOdds34)

    if spaceOdds34Max == 'miniMegaHammerSpaceOdds34':
        miniMegaHammerSpaceOdds34 += (100 - miniMegaHammerSpaceOdds34)

    if spaceOdds34Max == 'warpPipeSpaceOdds34':
        warpPipeSpaceOdds34 += (100 - warpPipeSpaceOdds34)

    if spaceOdds34Max == 'swapCardSpaceOdds34':
        swapCardSpaceOdds34 += (100 - swapCardSpaceOdds34)

    if spaceOdds34Max == 'sparkyStickerSpaceOdds34':
        sparkyStickerSpaceOdds34 += (100 - sparkyStickerSpaceOdds34)

    if spaceOdds34Max == 'gaddlightSpaceOdds34':
        gaddlightSpaceOdds34 += (100 - gaddlightSpaceOdds34)

    if spaceOdds34Max == 'chompCallSpaceOdds34':
        chompCallSpaceOdds34 += (100 - chompCallSpaceOdds34)

    if spaceOdds34Max == 'bowserSuitSpaceOdds34':
        bowserSuitSpaceOdds34 += (100 - bowserSuitSpaceOdds34)

    if spaceOdds34Max == 'crystalBallSpaceOdds34':
        crystalBallSpaceOdds34 += (100 - crystalBallSpaceOdds34)

    if spaceOdds34Max == 'magicLampSpaceOdds34':
        magicLampSpaceOdds34 += (100 - magicLampSpaceOdds34)

    if spaceOdds34Max == 'itemBagSpaceOdds34':
        itemBagSpaceOdds34 += (100 - itemBagSpaceOdds34)

    miniMushroomSpaceOdds34 = str(miniMushroomSpaceOdds34)
    megaMushroomSpaceOdds34 = str(megaMushroomSpaceOdds34)
    superMiniMushroomSpaceOdds34 = str(superMiniMushroomSpaceOdds34)
    superMegaMushroomSpaceOdds34 = str(superMegaMushroomSpaceOdds34)
    miniMegaHammerSpaceOdds34 = str(miniMegaHammerSpaceOdds34)
    warpPipeSpaceOdds34 = str(warpPipeSpaceOdds34)
    swapCardSpaceOdds34 = str(swapCardSpaceOdds34)
    sparkyStickerSpaceOdds34 = str(sparkyStickerSpaceOdds34)
    gaddlightSpaceOdds34 = str(gaddlightSpaceOdds34)
    chompCallSpaceOdds34 = str(chompCallSpaceOdds34)
    bowserSuitSpaceOdds34 = str(bowserSuitSpaceOdds34)
    crystalBallSpaceOdds34 = str(crystalBallSpaceOdds34)
    magicLampSpaceOdds34 = str(magicLampSpaceOdds34)
    itemBagSpaceOdds34 = str(itemBagSpaceOdds34)
    miniMushroomShopOdds12 = str(miniMushroomShopOdds12)
    megaMushroomShopOdds12 = str(megaMushroomShopOdds12)
    superMiniMushroomShopOdds12 = str(superMiniMushroomShopOdds12)
    superMegaMushroomShopOdds12 = str(superMegaMushroomShopOdds12)
    miniMegaHammerShopOdds12 = str(miniMegaHammerShopOdds12)
    warpPipeShopOdds12 = str(warpPipeShopOdds12)
    swapCardShopOdds12 = str(swapCardShopOdds12)
    sparkyStickerShopOdds12 = str(sparkyStickerShopOdds12)
    gaddlightShopOdds12 = str(gaddlightShopOdds12)
    chompCallShopOdds12 = str(chompCallShopOdds12)
    bowserSuitShopOdds12 = str(bowserSuitShopOdds12)
    crystalBallShopOdds12 = str(crystalBallShopOdds12)
    magicLampShopOdds12 = str(magicLampShopOdds12)
    itemBagShopOdds12 = str(itemBagShopOdds12)
    miniMushroomSpaceOdds1 = str(miniMushroomSpaceOdds1)
    megaMushroomSpaceOdds1 = str(megaMushroomSpaceOdds1)
    superMiniMushroomSpaceOdds1 = str(superMiniMushroomSpaceOdds1)
    superMegaMushroomSpaceOdds1 = str(superMegaMushroomSpaceOdds1)
    miniMegaHammerSpaceOdds1 = str(miniMegaHammerSpaceOdds1)
    warpPipeSpaceOdds1 = str(warpPipeSpaceOdds1)
    swapCardSpaceOdds1 = str(swapCardSpaceOdds1)
    sparkyStickerSpaceOdds1 = str(sparkyStickerSpaceOdds1)
    gaddlightSpaceOdds1 = str(gaddlightSpaceOdds1)
    chompCallSpaceOdds1 = str(chompCallSpaceOdds1)
    bowserSuitSpaceOdds1 = str(bowserSuitSpaceOdds1)
    crystalBallSpaceOdds1 = str(crystalBallSpaceOdds1)
    magicLampSpaceOdds1 = str(magicLampSpaceOdds1)
    itemBagSpaceOdds1 = str(itemBagSpaceOdds1)
    miniMushroomSpaceOdds2 = str(miniMushroomSpaceOdds2)
    megaMushroomSpaceOdds2 = str(megaMushroomSpaceOdds2)
    superMiniMushroomSpaceOdds2 = str(superMiniMushroomSpaceOdds2)
    superMegaMushroomSpaceOdds2 = str(superMegaMushroomSpaceOdds2)
    miniMegaHammerSpaceOdds2 = str(miniMegaHammerSpaceOdds2)
    warpPipeSpaceOdds2 = str(warpPipeSpaceOdds2)
    swapCardSpaceOdds2 = str(swapCardSpaceOdds2)
    sparkyStickerSpaceOdds2 = str(sparkyStickerSpaceOdds2)
    gaddlightSpaceOdds2 = str(gaddlightSpaceOdds2)
    chompCallSpaceOdds2 = str(chompCallSpaceOdds2)
    bowserSuitSpaceOdds2 = str(bowserSuitSpaceOdds2)
    crystalBallSpaceOdds2 = str(crystalBallSpaceOdds2)
    magicLampSpaceOdds2 = str(magicLampSpaceOdds2)
    itemBagSpaceOdds2 = str(itemBagSpaceOdds2)
    miniMushroomSpaceOdds34 = str(miniMushroomSpaceOdds34)
    megaMushroomSpaceOdds34 = str(megaMushroomSpaceOdds34)
    superMiniMushroomSpaceOdds34 = str(superMiniMushroomSpaceOdds34)
    superMegaMushroomSpaceOdds34 = str(superMegaMushroomSpaceOdds34)
    miniMegaHammerSpaceOdds34 = str(miniMegaHammerSpaceOdds34)
    warpPipeSpaceOdds34 = str(warpPipeSpaceOdds34)
    swapCardSpaceOdds34 = str(swapCardSpaceOdds34)
    sparkyStickerSpaceOdds34 = str(sparkyStickerSpaceOdds34)
    gaddlightSpaceOdds34 = str(gaddlightSpaceOdds34)
    chompCallSpaceOdds34 = str(chompCallSpaceOdds34)
    bowserSuitSpaceOdds34 = str(bowserSuitSpaceOdds34)
    crystalBallSpaceOdds34 = str(crystalBallSpaceOdds34)
    magicLampSpaceOdds34 = str(magicLampSpaceOdds34)
    itemBagSpaceOdds34 = str(itemBagSpaceOdds34)

    minimumPrice = find_lowest_integer(*[int(miniMushroomPrice1), int(miniMushroomPrice2), int(miniMushroomPrice34), 
                                          int(megaMushroomPrice1), int(megaMushroomPrice2), int(megaMushroomPrice34), 
                                          int(superMiniMushroomPrice1), int(superMiniMushroomPrice2), int(superMiniMushroomPrice34), 
                                          int(superMegaMushroomPrice1), int(superMegaMushroomPrice2), int(superMegaMushroomPrice34), 
                                          int(miniMegaHammerPrice1), int(miniMegaHammerPrice2), int(miniMegaHammerPrice34), 
                                          int(warpPipePrice1), int(warpPipePrice2), int(warpPipePrice34), 
                                          int(swapCardPrice1), int(swapCardPrice2), int(swapCardPrice34), 
                                          int(sparkyStickerPrice1), int(sparkyStickerPrice2), int(sparkyStickerPrice34), 
                                          int(gaddlightPrice1), int(gaddlightPrice2), int(gaddlightPrice34), 
                                          int(chompCallPrice1), int(chompCallPrice2), int(chompCallPrice34), 
                                          int(bowserSuitPrice1), int(bowserSuitPrice2), int(bowserSuitPrice34), 
                                          int(crystalBallPrice1), int(crystalBallPrice2), int(crystalBallPrice34), 
                                          int(magicLampPrice1), int(magicLampPrice2), int(magicLampPrice34), 
                                          int(itemBagPrice1), int(itemBagPrice2), int(itemBagPrice34)])

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

    # Usage
    miniMushroomPrice1 = convert_to_hex_weight(miniMushroomPrice1)
    miniMushroomPrice2 = convert_to_hex_weight(miniMushroomPrice2)
    miniMushroomPrice34 = convert_to_hex_weight(miniMushroomPrice34)
    miniMushroomShopOdds12 = convert_to_hex_weight(miniMushroomShopOdds12)
    miniMushroomShopOdds34 = convert_to_hex_weight(miniMushroomShopOdds34)
    miniMushroomSpaceOdds1 = convert_to_hex_weight(miniMushroomSpaceOdds1)
    miniMushroomSpaceOdds2 = convert_to_hex_weight(miniMushroomSpaceOdds2)
    miniMushroomSpaceOdds34 = convert_to_hex_weight(miniMushroomSpaceOdds34)
    megaMushroomPrice1 = convert_to_hex_weight(megaMushroomPrice1)
    megaMushroomPrice2 = convert_to_hex_weight(megaMushroomPrice2)
    megaMushroomPrice34 = convert_to_hex_weight(megaMushroomPrice34)
    megaMushroomShopOdds12 = convert_to_hex_weight(megaMushroomShopOdds12)
    megaMushroomShopOdds34 = convert_to_hex_weight(megaMushroomShopOdds34)
    megaMushroomSpaceOdds1 = convert_to_hex_weight(megaMushroomSpaceOdds1)
    megaMushroomSpaceOdds2 = convert_to_hex_weight(megaMushroomSpaceOdds2)
    megaMushroomSpaceOdds34 = convert_to_hex_weight(megaMushroomSpaceOdds34)
    superMiniMushroomPrice1 = convert_to_hex_weight(superMiniMushroomPrice1)
    superMiniMushroomPrice2 = convert_to_hex_weight(superMiniMushroomPrice2)
    superMiniMushroomPrice34 = convert_to_hex_weight(superMiniMushroomPrice34)
    superMiniMushroomShopOdds12 = convert_to_hex_weight(superMiniMushroomShopOdds12)
    superMiniMushroomShopOdds34 = convert_to_hex_weight(superMiniMushroomShopOdds34)
    superMiniMushroomSpaceOdds1 = convert_to_hex_weight(superMiniMushroomSpaceOdds1)
    superMiniMushroomSpaceOdds2 = convert_to_hex_weight(superMiniMushroomSpaceOdds2)
    superMiniMushroomSpaceOdds34 = convert_to_hex_weight(superMiniMushroomSpaceOdds34)
    superMegaMushroomPrice1 = convert_to_hex_weight(superMegaMushroomPrice1)
    superMegaMushroomPrice2 = convert_to_hex_weight(superMegaMushroomPrice2)
    superMegaMushroomPrice34 = convert_to_hex_weight(superMegaMushroomPrice34)
    superMegaMushroomShopOdds12 = convert_to_hex_weight(superMegaMushroomShopOdds12)
    superMegaMushroomShopOdds34 = convert_to_hex_weight(superMegaMushroomShopOdds34)
    superMegaMushroomSpaceOdds1 = convert_to_hex_weight(superMegaMushroomSpaceOdds1)
    superMegaMushroomSpaceOdds2 = convert_to_hex_weight(superMegaMushroomSpaceOdds2)
    superMegaMushroomSpaceOdds34 = convert_to_hex_weight(superMegaMushroomSpaceOdds34)
    miniMegaHammerPrice1 = convert_to_hex_weight(miniMegaHammerPrice1)
    miniMegaHammerPrice2 = convert_to_hex_weight(miniMegaHammerPrice2)
    miniMegaHammerPrice34 = convert_to_hex_weight(miniMegaHammerPrice34)
    miniMegaHammerShopOdds12 = convert_to_hex_weight(miniMegaHammerShopOdds12)
    miniMegaHammerShopOdds34 = convert_to_hex_weight(miniMegaHammerShopOdds34)
    miniMegaHammerSpaceOdds1 = convert_to_hex_weight(miniMegaHammerSpaceOdds1)
    miniMegaHammerSpaceOdds2 = convert_to_hex_weight(miniMegaHammerSpaceOdds2)
    miniMegaHammerSpaceOdds34 = convert_to_hex_weight(miniMegaHammerSpaceOdds34)
    warpPipePrice1 = convert_to_hex_weight(warpPipePrice1)
    warpPipePrice2 = convert_to_hex_weight(warpPipePrice2)
    warpPipePrice34 = convert_to_hex_weight(warpPipePrice34)
    warpPipeShopOdds12 = convert_to_hex_weight(warpPipeShopOdds12)
    warpPipeShopOdds34 = convert_to_hex_weight(warpPipeShopOdds34)
    warpPipeSpaceOdds1 = convert_to_hex_weight(warpPipeSpaceOdds1)
    warpPipeSpaceOdds2 = convert_to_hex_weight(warpPipeSpaceOdds2)
    warpPipeSpaceOdds34 = convert_to_hex_weight(warpPipeSpaceOdds34)
    swapCardPrice1 = convert_to_hex_weight(swapCardPrice1)
    swapCardPrice2 = convert_to_hex_weight(swapCardPrice2)
    swapCardPrice34 = convert_to_hex_weight(swapCardPrice34)
    swapCardShopOdds12 = convert_to_hex_weight(swapCardShopOdds12)
    swapCardShopOdds34 = convert_to_hex_weight(swapCardShopOdds34)
    swapCardSpaceOdds1 = convert_to_hex_weight(swapCardSpaceOdds1)
    swapCardSpaceOdds2 = convert_to_hex_weight(swapCardSpaceOdds2)
    swapCardSpaceOdds34 = convert_to_hex_weight(swapCardSpaceOdds34)
    sparkyStickerPrice1 = convert_to_hex_weight(sparkyStickerPrice1)
    sparkyStickerPrice2 = convert_to_hex_weight(sparkyStickerPrice2)
    sparkyStickerPrice34 = convert_to_hex_weight(sparkyStickerPrice34)
    sparkyStickerShopOdds12 = convert_to_hex_weight(sparkyStickerShopOdds12)
    sparkyStickerShopOdds34 = convert_to_hex_weight(sparkyStickerShopOdds34)
    sparkyStickerSpaceOdds1 = convert_to_hex_weight(sparkyStickerSpaceOdds1)
    sparkyStickerSpaceOdds2 = convert_to_hex_weight(sparkyStickerSpaceOdds2)
    sparkyStickerSpaceOdds34 = convert_to_hex_weight(sparkyStickerSpaceOdds34)
    gaddlightPrice1 = convert_to_hex_weight(gaddlightPrice1)
    gaddlightPrice2 = convert_to_hex_weight(gaddlightPrice2)
    gaddlightPrice34 = convert_to_hex_weight(gaddlightPrice34)
    gaddlightShopOdds12 = convert_to_hex_weight(gaddlightShopOdds12)
    gaddlightShopOdds34 = convert_to_hex_weight(gaddlightShopOdds34)
    gaddlightSpaceOdds1 = convert_to_hex_weight(gaddlightSpaceOdds1)
    gaddlightSpaceOdds2 = convert_to_hex_weight(gaddlightSpaceOdds2)
    gaddlightSpaceOdds34 = convert_to_hex_weight(gaddlightSpaceOdds34)
    chompCallPrice1 = convert_to_hex_weight(chompCallPrice1)
    chompCallPrice2 = convert_to_hex_weight(chompCallPrice2)
    chompCallPrice34 = convert_to_hex_weight(chompCallPrice34)
    chompCallShopOdds12 = convert_to_hex_weight(chompCallShopOdds12)
    chompCallShopOdds34 = convert_to_hex_weight(chompCallShopOdds34)
    chompCallSpaceOdds1 = convert_to_hex_weight(chompCallSpaceOdds1)
    chompCallSpaceOdds2 = convert_to_hex_weight(chompCallSpaceOdds2)
    chompCallSpaceOdds34 = convert_to_hex_weight(chompCallSpaceOdds34)
    bowserSuitPrice1 = convert_to_hex_weight(bowserSuitPrice1)
    bowserSuitPrice2 = convert_to_hex_weight(bowserSuitPrice2)
    bowserSuitPrice34 = convert_to_hex_weight(bowserSuitPrice34)
    bowserSuitShopOdds12 = convert_to_hex_weight(bowserSuitShopOdds12)
    bowserSuitShopOdds34 = convert_to_hex_weight(bowserSuitShopOdds34)
    bowserSuitSpaceOdds1 = convert_to_hex_weight(bowserSuitSpaceOdds1)
    bowserSuitSpaceOdds2 = convert_to_hex_weight(bowserSuitSpaceOdds2)
    bowserSuitSpaceOdds34 = convert_to_hex_weight(bowserSuitSpaceOdds34)
    crystalBallPrice1 = convert_to_hex_weight(crystalBallPrice1)
    crystalBallPrice2 = convert_to_hex_weight(crystalBallPrice2)
    crystalBallPrice34 = convert_to_hex_weight(crystalBallPrice34)
    crystalBallShopOdds12 = convert_to_hex_weight(crystalBallShopOdds12)
    crystalBallShopOdds34 = convert_to_hex_weight(crystalBallShopOdds34)
    crystalBallSpaceOdds1 = convert_to_hex_weight(crystalBallSpaceOdds1)
    crystalBallSpaceOdds2 = convert_to_hex_weight(crystalBallSpaceOdds2)
    crystalBallSpaceOdds34 = convert_to_hex_weight(crystalBallSpaceOdds34)
    magicLampPrice1 = convert_to_hex_weight(magicLampPrice1)
    magicLampPrice2 = convert_to_hex_weight(magicLampPrice2)
    magicLampPrice34 = convert_to_hex_weight(magicLampPrice34)
    magicLampShopOdds12 = convert_to_hex_weight(magicLampShopOdds12)
    magicLampShopOdds34 = convert_to_hex_weight(magicLampShopOdds34)
    magicLampSpaceOdds1 = convert_to_hex_weight(magicLampSpaceOdds1)
    magicLampSpaceOdds2 = convert_to_hex_weight(magicLampSpaceOdds2)
    magicLampSpaceOdds34 = convert_to_hex_weight(magicLampSpaceOdds34)
    itemBagPrice1 = convert_to_hex_weight(itemBagPrice1)
    itemBagPrice2 = convert_to_hex_weight(itemBagPrice2)
    itemBagPrice34 = convert_to_hex_weight(itemBagPrice34)
    itemBagShopOdds12 = convert_to_hex_weight(itemBagShopOdds12)
    itemBagShopOdds34 = convert_to_hex_weight(itemBagShopOdds34)
    itemBagSpaceOdds1 = convert_to_hex_weight(itemBagSpaceOdds1)
    itemBagSpaceOdds2 = convert_to_hex_weight(itemBagSpaceOdds2)
    itemBagSpaceOdds34 = convert_to_hex_weight(itemBagSpaceOdds34)

    minimumPrice = convert_to_hex_weight(minimumPrice)

    generatedCode = getItemModsFourItemSpace(minimumPrice)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)