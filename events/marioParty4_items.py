# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/7/2024
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4, mushroomPrice4, mushroomWeight4, goldenMushroomPrice4, goldenMushroomWeight4, bowserPhonePrice4, bowserPhoneWeight4, cellularShopperPrice4, cellularShopperWeight4, hiddenBlockCardPrice4, hiddenBlockCardWeight4):
    if not miniPrice4.get() or not miniWeight4.get() or not megaPrice4.get() or not megaWeight4.get() or not superMegaPrice4.get() or not superMegaWeight4.get() or not superMiniPrice4.get() or not superMiniWeight4.get() or not miniMegaHammerPrice4.get() or not miniMegaHammerWeight4.get() or not warpPipePrice4.get() or not warpPipeWeight4.get() or not swapCardPrice4.get() or not swapCardWeight4.get() or not sparkyStickerPrice4.get() or not sparkyStickerWeight4.get() or not bowserSuitPrice4.get() or not bowserSuitWeight4.get() or not gaddlightPrice4.get() or not gaddlightWeight4.get() or not chompCallPrice4.get() or not chompCallWeight4.get() or not crystalBallPrice4.get() or not crystalBallWeight4.get() or not magicLampPrice4.get() or not magicLampWeight4.get() or not itemBagPrice4.get()  or not itemBagWeight4.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    miniPrice4 = miniPrice4.get()
    miniWeight4 = miniWeight4.get()
    megaPrice4 = megaPrice4.get()
    megaWeight4 = megaWeight4.get()
    superMiniPrice4 = superMiniPrice4.get()
    superMiniWeight4 = superMiniWeight4.get()
    superMegaPrice4 = superMegaPrice4.get()
    superMegaWeight4 = superMegaWeight4.get()
    miniMegaHammerPrice4 = miniMegaHammerPrice4.get()
    miniMegaHammerWeight4 = miniMegaHammerWeight4.get()
    warpPipePrice4 = warpPipePrice4.get()
    warpPipeWeight4 = warpPipeWeight4.get()
    swapCardPrice4 = swapCardPrice4.get()
    swapCardWeight4 = swapCardWeight4.get()
    sparkyStickerPrice4 = sparkyStickerPrice4.get()
    sparkyStickerWeight4 = sparkyStickerWeight4.get()
    gaddlightPrice4 = gaddlightPrice4.get()
    gaddlightWeight4 = gaddlightWeight4.get()
    chompCallPrice4 = chompCallPrice4.get()
    chompCallWeight4 = chompCallWeight4.get()
    bowserSuitPrice4 = bowserSuitPrice4.get()
    bowserSuitWeight4 = bowserSuitWeight4.get()
    crystalBallPrice4 = crystalBallPrice4.get()
    crystalBallWeight4 = crystalBallWeight4.get()
    magicLampPrice4 = magicLampPrice4.get()
    magicLampWeight4 = magicLampWeight4.get()
    itemBagPrice4 = itemBagPrice4.get()
    itemBagWeight4 = itemBagWeight4.get()

    try:
        mushroomWeight4 = mushroomWeight4.get()
    except:
        mushroomWeight4 = 0

    try:
        mushroomPrice4 = mushroomPrice4.get()
    except:
        mushroomPrice4 = 0

    try:
        goldenMushroomWeight4 = goldenMushroomWeight4.get()
    except:
        goldenMushroomWeight4 = 0

    try:
        goldenMushroomPrice4 = goldenMushroomPrice4.get()
    except:
        goldenMushroomPrice4 = 0

    try:
        cellularShopperWeight4 = cellularShopperWeight4.get()
    except:
        cellularShopperWeight4 = 0

    try:
        cellularShopperPrice4 = cellularShopperPrice4.get()
    except:
        cellularShopperPrice4 = 0

    try:
        bowserPhoneWeight4 = bowserPhoneWeight4.get()
    except:
        bowserPhoneWeight4 = 0

    try:
        bowserPhonePrice4 = bowserPhonePrice4.get()
    except:
        bowserPhonePrice4 = 0

    try:
        hiddenBlockCardWeight4 = hiddenBlockCardWeight4.get()
    except:
        hiddenBlockCardWeight4 = 0

    try:
        hiddenBlockCardPrice4 = hiddenBlockCardPrice4.get()
    except:
        hiddenBlockCardPrice4 = 0

    orbWeightTotal = int(miniWeight4) + int(megaWeight4) + int(superMiniWeight4) + int(superMegaWeight4) + int(miniMegaHammerWeight4) + int(warpPipeWeight4) + int(swapCardWeight4) + int(sparkyStickerWeight4) + int(gaddlightWeight4) + int(chompCallWeight4) + int(bowserSuitWeight4) + int(crystalBallWeight4) + int(magicLampWeight4) + int(itemBagWeight4) + int(mushroomWeight4) + int(goldenMushroomWeight4) + int(cellularShopperWeight4) + int(bowserPhoneWeight4) + int(hiddenBlockCardWeight4)

    orbPriceMin = find_lowest_integer(*[int(miniPrice4), int(megaPrice4), int(superMiniPrice4), int(superMegaPrice4), int(miniMegaHammerPrice4), int(warpPipePrice4), int(swapCardPrice4), int(sparkyStickerPrice4), int(gaddlightPrice4), int(chompCallPrice4), int(bowserSuitPrice4), int(crystalBallPrice4), int(magicLampPrice4), int(itemBagPrice4), int(mushroomPrice4), int(goldenMushroomPrice4), int(cellularShopperPrice4), int(bowserPhonePrice4), int(hiddenBlockCardPrice4)])
    
    def calculateWeight(weight):
        if orbWeightTotal < 100:
            percentage = int(weight)
            return percentage
        else:
            percentage = (int(weight) / orbWeightTotal) * 100
            if 0< percentage < 1:
                return math.ceil(percentage)
            return round(percentage)

    miniWeight4 = calculateWeight(miniWeight4)
    megaWeight4 = calculateWeight(megaWeight4)
    superMegaWeight4 = calculateWeight(superMegaWeight4)
    superMiniWeight4 = calculateWeight(superMiniWeight4)
    miniMegaHammerWeight4 = calculateWeight(miniMegaHammerWeight4)
    warpPipeWeight4 = calculateWeight(warpPipeWeight4)
    swapCardWeight4 = calculateWeight(swapCardWeight4)
    sparkyStickerWeight4 = calculateWeight(sparkyStickerWeight4)
    gaddlightWeight4 = calculateWeight(gaddlightWeight4)
    chompCallWeight4 = calculateWeight(chompCallWeight4)
    bowserSuitWeight4 = calculateWeight(bowserSuitWeight4)
    crystalBallWeight4 = calculateWeight(crystalBallWeight4)
    magicLampWeight4 = calculateWeight(magicLampWeight4)
    itemBagWeight4 = calculateWeight(itemBagWeight4)
    mushroomWeight4 = calculateWeight(mushroomWeight4)
    goldenMushroomWeight4 = calculateWeight(goldenMushroomWeight4)
    cellularShopperWeight4 = calculateWeight(cellularShopperWeight4)
    bowserPhoneWeight4 = calculateWeight(bowserPhoneWeight4)
    hiddenBlockCardWeight4 = calculateWeight(hiddenBlockCardWeight4)
    
    orbWeightTotal = miniWeight4 + megaWeight4 + superMiniWeight4 + superMegaWeight4 + miniMegaHammerWeight4 + warpPipeWeight4 + swapCardWeight4 + sparkyStickerWeight4 + gaddlightWeight4 + chompCallWeight4 + bowserSuitWeight4 + crystalBallWeight4 + magicLampWeight4 + itemBagWeight4 + mushroomWeight4 + goldenMushroomWeight4 + cellularShopperWeight4 + bowserPhoneWeight4 + hiddenBlockCardWeight4
    
    if orbWeightTotal < 100:
        var_names = ['miniWeight4', 'megaWeight4', 'superMegaWeight4', 'superMiniWeight4', 'miniMegaHammerWeight4', 'warpPipeWeight4', 'swapCardWeight4', 'sparkyStickerWeight4', 'gaddlightWeight4', 'chompCallWeight4', 'bowserSuitWeight4', 'crystalBallWeight4', 'magicLampWeight4', 'itemBagWeight4', 'mushroomWeight4', 'goldenMushroomWeight4', 'cellularShopperWeight4', 'bowserPhoneWeight4', 'hiddenBlockCardWeight4']
        max_var = max(zip(var_names, (map(eval, var_names))), key=lambda tuple: tuple[1])[0]
    
        if max_var == 'miniWeight4':
            miniWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'megaWeight4':
            megaWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'superMegaWeight4':
            superMegaWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'superMiniWeight4':
            superMiniWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'miniMegaHammerWeight4':
            miniMegaHammerWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'warpPipeWeight4':
            warpPipeWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'swapCardWeight4':
            swapCardWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'sparkyStickerWeight4':
            sparkyStickerWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'gaddlightWeight4':
            gaddlightWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'chompCallWeight4':
            chompCallWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bowserSuitWeight4':
            bowserSuitWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'crystalBallWeight4':
            crystalBallWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'magicLampWeight4':
            magicLampWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'itemBagWeight4':
            itemBagWeight4 += (100 - orbWeightTotal)
    
        # New items adjustments
        if max_var == 'mushroomWeight4':
            mushroomWeight4 += (100 - orbWeightTotal)
    
        if max_var == 'goldenMushroomWeight4':
            goldenMushroomWeight4 += (100 - orbWeightTotal)
    
        if max_var == 'cellularShopperWeight4':
            cellularShopperWeight4 += (100 - orbWeightTotal)
    
        if max_var == 'bowserPhoneWeight4':
            bowserPhoneWeight4 += (100 - orbWeightTotal)
    
        if max_var == 'hiddenBlockCardWeight4':
            hiddenBlockCardWeight4 += (100 - orbWeightTotal)
    
    miniWeight4 = str(miniWeight4)
    megaWeight4 = str(megaWeight4)
    superMegaWeight4 = str(superMegaWeight4)
    superMiniWeight4 = str(superMiniWeight4)
    miniMegaHammerWeight4 = str(miniMegaHammerWeight4)
    warpPipeWeight4 = str(warpPipeWeight4)
    swapCardWeight4 = str(swapCardWeight4)
    sparkyStickerWeight4 = str(sparkyStickerWeight4)
    gaddlightWeight4 = str(gaddlightWeight4)
    chompCallWeight4 = str(chompCallWeight4)
    bowserSuitWeight4 = str(bowserSuitWeight4)
    crystalBallWeight4 = str(crystalBallWeight4)
    magicLampWeight4 = str(magicLampWeight4)
    itemBagWeight4 = str(itemBagWeight4)
    mushroomWeight4 = str(mushroomWeight4)
    goldenMushroomWeight4 = str(goldenMushroomWeight4)
    cellularShopperWeight4 = str(cellularShopperWeight4)
    bowserPhoneWeight4 = str(bowserPhoneWeight4)
    hiddenBlockCardWeight4 = str(hiddenBlockCardWeight4)
    
    try:
        miniWeight4 = hex(int(miniWeight4))
        if len(miniWeight4) == 4:
            miniWeight4 = miniWeight4[2:]
        elif len(miniWeight4) == 3:
            miniWeight4 = "0" + miniWeight4[2:]
    except:
        miniWeight4 = "00"
    try:
        miniPrice4 = hex(int(miniPrice4))
        if len(miniPrice4) == 4:
            miniPrice4 = miniPrice4[2:]
        elif len(miniPrice4) == 3:
            miniPrice4 = "0" + miniPrice4[2:]
    except:
        miniPrice4 = "00"        
    try:
        megaWeight4 = hex(int(megaWeight4))
        if len(megaWeight4) == 4:
            megaWeight4 = megaWeight4[2:]
        elif len(megaWeight4) == 3:
            megaWeight4 = "0" + megaWeight4[2:]
    except:
        megaWeight4 = "00"
    try:
        megaPrice4 = hex(int(megaPrice4))
        if len(megaPrice4) == 4:
            megaPrice4 = megaPrice4[2:]
        elif len(megaPrice4) == 3:
            megaPrice4 = "0" + megaPrice4[2:]
    except:
        megaPrice4 = "00"
    try:
        superMiniWeight4 = hex(int(superMiniWeight4))
        if len(superMiniWeight4) == 4:
            superMiniWeight4 = superMiniWeight4[2:]
        elif len(superMiniWeight4) == 3:
            superMiniWeight4 = "0" + superMiniWeight4[2:]
    except:
        superMiniWeight4 = "00"
    try:
        superMiniPrice4 = hex(int(superMiniPrice4))
        if len(superMiniPrice4) == 4:
            superMiniPrice4 = superMiniPrice4[2:]
        elif len(superMiniPrice4) == 3:
            superMiniPrice4 = "0" + superMiniPrice4[2:]
    except:
        superMiniPrice4 = "00"
    try:
        superMegaWeight4 = hex(int(superMegaWeight4))
        if len(superMegaWeight4) == 4:
            superMegaWeight4 = superMegaWeight4[2:]
        elif len(superMegaWeight4) == 3:
            superMegaWeight4 = "0" + superMegaWeight4[2:]
    except:
        superMegaWeight4 = "00"
    try:
        superMegaPrice4 = hex(int(superMegaPrice4))
        if len(superMegaPrice4) == 4:
            superMegaPrice4 = superMegaPrice4[2:]
        elif len(superMegaPrice4) == 3:
            superMegaPrice4 = "0" + superMegaPrice4[2:]
    except:
        superMegaPrice4 = "00"
    try:
        miniMegaHammerWeight4 = hex(int(miniMegaHammerWeight4))
        if len(miniMegaHammerWeight4) == 4:
            miniMegaHammerWeight4 = miniMegaHammerWeight4[2:]
        elif len(miniMegaHammerWeight4) == 3:
            miniMegaHammerWeight4 = "0" + miniMegaHammerWeight4[2:]
    except:
        miniMegaHammerWeight4 = "00"
    try:
        miniMegaHammerPrice4 = hex(int(miniMegaHammerPrice4))
        if len(miniMegaHammerPrice4) == 4:
            miniMegaHammerPrice4 = miniMegaHammerPrice4[2:]
        elif len(miniMegaHammerPrice4) == 3:
            miniMegaHammerPrice4 = "0" + miniMegaHammerPrice4[2:]
    except:
        miniMegaHammerPrice4 = "00"
    try:
        warpPipeWeight4 = hex(int(warpPipeWeight4))
        if len(warpPipeWeight4) == 4:
            warpPipeWeight4 = warpPipeWeight4[2:]
        elif len(warpPipeWeight4) == 3:
            warpPipeWeight4 = "0" + warpPipeWeight4[2:]
    except:
        warpPipeWeight4 = "00"
    try:
        warpPipePrice4 = hex(int(warpPipePrice4))
        if len(warpPipePrice4) == 4:
            warpPipePrice4 = warpPipePrice4[2:]
        elif len(warpPipePrice4) == 3:
            warpPipePrice4 = "0" + warpPipePrice4[2:]
    except:
        warpPipePrice4 = "00"
    try:
        swapCardWeight4 = hex(int(swapCardWeight4))
        if len(swapCardWeight4) == 4:
            swapCardWeight4 = swapCardWeight4[2:]
        elif len(swapCardWeight4) == 3:
            swapCardWeight4 = "0" + swapCardWeight4[2:]
    except:
        swapCardWeight4 = "00"
    try:
        swapCardPrice4 = hex(int(swapCardPrice4))
        if len(swapCardPrice4) == 4:
            swapCardPrice4 = swapCardPrice4[2:]
        elif len(swapCardPrice4) == 3:
            swapCardPrice4 = "0" + swapCardPrice4[2:]
    except:
        swapCardPrice4 = "00"
    try:
        sparkyStickerWeight4 = hex(int(sparkyStickerWeight4))
        if len(sparkyStickerWeight4) == 4:
            sparkyStickerWeight4 = sparkyStickerWeight4[2:]
        elif len(sparkyStickerWeight4) == 3:
            sparkyStickerWeight4 = "0" + sparkyStickerWeight4[2:]
    except:
        sparkyStickerWeight4 = "00"
    try:
        sparkyStickerPrice4 = hex(int(sparkyStickerPrice4))
        if len(sparkyStickerPrice4) == 4:
            sparkyStickerPrice4 = sparkyStickerPrice4[2:]
        elif len(sparkyStickerPrice4) == 3:
            sparkyStickerPrice4 = "0" + sparkyStickerPrice4[2:]
    except:
        sparkyStickerPrice4 = "00"
    try:
        gaddlightWeight4 = hex(int(gaddlightWeight4))
        if len(gaddlightWeight4) == 4:
            gaddlightWeight4 = gaddlightWeight4[2:]
        elif len(gaddlightWeight4) == 3:
            gaddlightWeight4 = "0" + gaddlightWeight4[2:]
    except:
        gaddlightWeight4 = "00"
    try:
        gaddlightPrice4 = hex(int(gaddlightPrice4))
        if len(gaddlightPrice4) == 4:
            gaddlightPrice4 = gaddlightPrice4[2:]
        elif len(gaddlightPrice4) == 3:
            gaddlightPrice4 = "0" + gaddlightPrice4[2:]
    except:
        gaddlightPrice4 = "00"
    try:
        chompCallWeight4 = hex(int(chompCallWeight4))
        if len(chompCallWeight4) == 4:
            chompCallWeight4 = chompCallWeight4[2:]
        elif len(chompCallWeight4) == 3:
            chompCallWeight4 = "0" + chompCallWeight4[2:]
    except:
        chompCallWeight4 = "00"
    try:
        chompCallPrice4 = hex(int(chompCallPrice4))
        if len(chompCallPrice4) == 4:
            chompCallPrice4 = chompCallPrice4[2:]
        elif len(chompCallPrice4) == 3:
            chompCallPrice4 = "0" + chompCallPrice4[2:]
    except:
        chompCallPrice4 = "00"
    try:
        bowserSuitWeight4 = hex(int(bowserSuitWeight4))
        if len(bowserSuitWeight4) == 4:
            bowserSuitWeight4 = bowserSuitWeight4[2:]
        elif len(bowserSuitWeight4) == 3:
            bowserSuitWeight4 = "0" + bowserSuitWeight4[2:]
    except:
        bowserSuitWeight4 = "00"
    try:
        bowserSuitPrice4 = hex(int(bowserSuitPrice4))
        if len(bowserSuitPrice4) == 4:
            bowserSuitPrice4 = bowserSuitPrice4[2:]
        elif len(bowserSuitPrice4) == 3:
            bowserSuitPrice4 = "0" + bowserSuitPrice4[2:]
    except:
        bowserSuitPrice4 = "00"
    try:
        crystalBallWeight4 = hex(int(crystalBallWeight4))
        if len(crystalBallWeight4) == 4:
            crystalBallWeight4 = crystalBallWeight4[2:]
        elif len(crystalBallWeight4) == 3:
            crystalBallWeight4 = "0" + crystalBallWeight4[2:]
    except:
        crystalBallWeight4 = "00"
    try:
        crystalBallPrice4 = hex(int(crystalBallPrice4))
        if len(crystalBallPrice4) == 4:
            crystalBallPrice4 = crystalBallPrice4[2:]
        elif len(crystalBallPrice4) == 3:
            crystalBallPrice4 = "0" + crystalBallPrice4[2:]
    except:
        crystalBallPrice4 = "00"
    try:
        magicLampWeight4 = hex(int(magicLampWeight4))
        if len(magicLampWeight4) == 4:
            magicLampWeight4 = magicLampWeight4[2:]
        elif len(magicLampWeight4) == 3:
            magicLampWeight4 = "0" + magicLampWeight4[2:]
    except:
        magicLampWeight4 = "00"
    try:
        magicLampPrice4 = hex(int(magicLampPrice4))
        if len(magicLampPrice4) == 4:
            magicLampPrice4 = magicLampPrice4[2:]
        elif len(magicLampPrice4) == 3:
            magicLampPrice4 = "0" + magicLampPrice4[2:]
    except:
        magicLampPrice4 = "00"
    try:
        itemBagWeight4 = hex(int(itemBagWeight4))
        if len(itemBagWeight4) == 4:
            itemBagWeight4 = itemBagWeight4[2:]
        elif len(itemBagWeight4) == 3:
            itemBagWeight4 = "0" + itemBagWeight4[2:]
    except:
        itemBagWeight4 = "00"
    try:
        itemBagPrice4 = hex(int(itemBagPrice4))
        if len(itemBagPrice4) == 4:
            itemBagPrice4 = itemBagPrice4[2:]
        elif len(itemBagPrice4) == 3:
            itemBagPrice4 = "0" + itemBagPrice4[2:]
    except:
        itemBagPrice4 = "00"

    try:
        itemBagPrice4 = hex(int(itemBagPrice4))
        if len(itemBagPrice4) == 4:
            itemBagPrice4 = itemBagPrice4[2:]
        elif len(itemBagPrice4) == 3:
            itemBagPrice4 = "0" + itemBagPrice4[2:]
    except:
        itemBagPrice4 = "00"

    # New items price conversion
    try:
        mushroomPrice4 = hex(int(mushroomPrice4))
        if len(mushroomPrice4) == 4:
            mushroomPrice4 = mushroomPrice4[2:]
        elif len(mushroomPrice4) == 3:
            mushroomPrice4 = "0" + mushroomPrice4[2:]
    except:
        mushroomPrice4 = "00"

    try:
        goldenMushroomPrice4 = hex(int(goldenMushroomPrice4))
        if len(goldenMushroomPrice4) == 4:
            goldenMushroomPrice4 = goldenMushroomPrice4[2:]
        elif len(goldenMushroomPrice4) == 3:
            goldenMushroomPrice4 = "0" + goldenMushroomPrice4[2:]
    except:
        goldenMushroomPrice4 = "00"

    try:
        cellularShopperPrice4 = hex(int(cellularShopperPrice4))
        if len(cellularShopperPrice4) == 4:
            cellularShopperPrice4 = cellularShopperPrice4[2:]
        elif len(cellularShopperPrice4) == 3:
            cellularShopperPrice4 = "0" + cellularShopperPrice4[2:]
    except:
        cellularShopperPrice4 = "00"

    try:
        bowserPhonePrice4 = hex(int(bowserPhonePrice4))
        if len(bowserPhonePrice4) == 4:
            bowserPhonePrice4 = bowserPhonePrice4[2:]
        elif len(bowserPhonePrice4) == 3:
            bowserPhonePrice4 = "0" + bowserPhonePrice4[2:]
    except:
        bowserPhonePrice4 = "00"

    try:
        hiddenBlockCardPrice4 = hex(int(hiddenBlockCardPrice4))
        if len(hiddenBlockCardPrice4) == 4:
            hiddenBlockCardPrice4 = hiddenBlockCardPrice4[2:]
        elif len(hiddenBlockCardPrice4) == 3:
            hiddenBlockCardPrice4 = "0" + hiddenBlockCardPrice4[2:]
    except:
        hiddenBlockCardPrice4 = "00"

    orbPriceMin = hex(int(orbPriceMin))
    if len(orbPriceMin) == 4:
        orbPriceMin = "00" + orbPriceMin[2:]
    elif len(orbPriceMin) == 3:
        orbPriceMin = "000" + orbPriceMin[2:]
    generatedCode = getItemModsFour(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, sparkyStickerPrice4, sparkyStickerWeight4, gaddlightPrice4, gaddlightWeight4, chompCallPrice4, chompCallWeight4, bowserSuitPrice4, bowserSuitWeight4, crystalBallPrice4, crystalBallWeight4, magicLampPrice4, magicLampWeight4, itemBagPrice4, itemBagWeight4, orbPriceMin, mushroomPrice4, mushroomWeight4, goldenMushroomPrice4, goldenMushroomWeight4, cellularShopperPrice4, cellularShopperWeight4, bowserPhonePrice4, bowserPhoneWeight4, hiddenBlockCardPrice4, hiddenBlockCardWeight4)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def savePresetItems4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4, mushroomPrice4, mushroomWeight4, goldenMushroomPrice4, goldenMushroomWeight4, cellularShopperPrice4, cellularShopperWeight4, bowserPhonePrice4, bowserPhoneWeight4, hiddenBlockCardPrice4, hiddenBlockCardWeight4):
    if not miniPrice4.get() or not miniWeight4.get() or not megaPrice4.get() or not megaWeight4.get() or not superMegaPrice4.get() or not superMegaWeight4.get() or not superMiniPrice4.get() or not superMiniWeight4.get() or not miniMegaHammerPrice4.get() or not miniMegaHammerWeight4.get() or not warpPipePrice4.get() or not warpPipeWeight4.get() or not swapCardPrice4.get() or not swapCardWeight4.get() or not sparkyStickerPrice4.get() or not sparkyStickerWeight4.get() or not bowserSuitPrice4.get() or not bowserSuitWeight4.get() or not gaddlightPrice4.get() or not gaddlightWeight4.get() or not chompCallPrice4.get() or not chompCallWeight4.get() or not crystalBallPrice4.get() or not crystalBallWeight4.get() or not magicLampPrice4.get() or not magicLampWeight4.get() or not itemBagPrice4.get() or not itemBagWeight4.get() or not mushroomPrice4.get() or not mushroomWeight4.get() or not goldenMushroomPrice4.get() or not goldenMushroomWeight4.get() or not cellularShopperPrice4.get() or not cellularShopperWeight4.get() or not bowserPhonePrice4.get() or not bowserPhoneWeight4.get() or not hiddenBlockCardPrice4.get() or not hiddenBlockCardWeight4.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return

    miniPrice4 = miniPrice4.get()
    miniWeight4 = miniWeight4.get()
    megaPrice4 = megaPrice4.get()
    megaWeight4 = megaWeight4.get()
    superMiniPrice4 = superMiniPrice4.get()
    superMiniWeight4 = superMiniWeight4.get()
    superMegaPrice4 = superMegaPrice4.get()
    superMegaWeight4 = superMegaWeight4.get()
    miniMegaHammerPrice4 = miniMegaHammerPrice4.get()
    miniMegaHammerWeight4 = miniMegaHammerWeight4.get()
    warpPipePrice4 = warpPipePrice4.get()
    warpPipeWeight4 = warpPipeWeight4.get()
    swapCardPrice4 = swapCardPrice4.get()
    swapCardWeight4 = swapCardWeight4.get()
    sparkyStickerPrice4 = sparkyStickerPrice4.get()
    sparkyStickerWeight4 = sparkyStickerWeight4.get()
    gaddlightPrice4 = gaddlightPrice4.get()
    gaddlightWeight4 = gaddlightWeight4.get()
    chompCallPrice4 = chompCallPrice4.get()
    chompCallWeight4 = chompCallWeight4.get()
    bowserSuitPrice4 = bowserSuitPrice4.get()
    bowserSuitWeight4 = bowserSuitWeight4.get()
    crystalBallPrice4 = crystalBallPrice4.get()
    crystalBallWeight4 = crystalBallWeight4.get()
    magicLampPrice4 = magicLampPrice4.get()
    magicLampWeight4 = magicLampWeight4.get()
    itemBagPrice4 = itemBagPrice4.get()
    itemBagWeight4 = itemBagWeight4.get()
    
    # New items
    mushroomPrice4 = mushroomPrice4.get()
    mushroomWeight4 = mushroomWeight4.get()
    goldenMushroomPrice4 = goldenMushroomPrice4.get()
    goldenMushroomWeight4 = goldenMushroomWeight4.get()
    cellularShopperPrice4 = cellularShopperPrice4.get()
    cellularShopperWeight4 = cellularShopperWeight4.get()
    bowserPhonePrice4 = bowserPhonePrice4.get()
    bowserPhoneWeight4 = bowserPhoneWeight4.get()
    hiddenBlockCardPrice4 = hiddenBlockCardPrice4.get()
    hiddenBlockCardWeight4 = hiddenBlockCardWeight4.get()

    prices4 = [miniPrice4, megaPrice4, superMiniPrice4, superMegaPrice4, miniMegaHammerPrice4, warpPipePrice4, swapCardPrice4, sparkyStickerPrice4, gaddlightPrice4, chompCallPrice4, bowserSuitPrice4, crystalBallPrice4, magicLampPrice4, itemBagPrice4, mushroomPrice4, goldenMushroomPrice4, cellularShopperPrice4, bowserPhonePrice4, hiddenBlockCardPrice4]
    weights4 = [miniWeight4, megaWeight4, superMiniWeight4, superMegaWeight4, miniMegaHammerWeight4, warpPipeWeight4, swapCardWeight4, sparkyStickerWeight4, gaddlightWeight4, chompCallWeight4, bowserSuitWeight4, crystalBallWeight4, magicLampWeight4, itemBagWeight4, mushroomWeight4, goldenMushroomWeight4, cellularShopperWeight4, bowserPhoneWeight4, hiddenBlockCardWeight4]

    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prices', 'Weights'])
            for price, weight in zip(prices4, weights4):
                writer.writerow([price, weight])
        print("MPT file saved successfully!")
        createDialog("Operation Successful", "success", "Presets file saved successfully!.", None)

def loadPresetItems4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4):
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        prices4In = []
        weights4In = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                prices4In.append(float(row[0]))
                weights4In.append(float(row[1]))
        # Define a list of Entry widget attributes
        pricesNames4 = [miniPrice4, megaPrice4, superMiniPrice4, superMegaPrice4, miniMegaHammerPrice4, warpPipePrice4, swapCardPrice4, sparkyStickerPrice4, gaddlightPrice4, chompCallPrice4, bowserSuitPrice4, crystalBallPrice4, magicLampPrice4, itemBagPrice4]
        weightsNames4 = [miniWeight4, megaWeight4, superMiniWeight4, superMegaWeight4, miniMegaHammerWeight4, warpPipeWeight4, swapCardWeight4, sparkyStickerWeight4, gaddlightWeight4, chompCallWeight4, bowserSuitWeight4, crystalBallWeight4, magicLampWeight4, itemBagWeight4]
        # Update widgets with loaded values
        for index, widget in enumerate(pricesNames4):
            if widget and index < len(prices4In):
                widget.delete(0, 'end')
                widget.insert(0, int(prices4In[index]))
        for index, widget in enumerate(weightsNames4):
            if widget and index < len(weights4In):
                widget.delete(0, 'end')
                widget.insert(0, int(weights4In[index]))
        print("MPT file laoded successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def fillViaCode4(hide_custom, top, codeText, miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4):
    code4 = []
    code_single4 = []
    weight_code4 = []
    price_code4 = []
    weights4 = []
    weights4In = []
    prices4 = []
    prices4In = []
    current_line4 = ""

    code4.append(codeText.get("1.0", "end"))
    
    try:
        for i in range(0, 18):
            current_line4 = current_line4 + code4[0][i]

        if current_line4 == "MP4 - Item Modifer":
            current_line4 = ""
            
            for i in range(19, 3367):
                if code4[0][i] != " " and code4[0][i] != "\n":
                    current_line4 = current_line4 + code4[0][i]
                else:
                    code_single4.append(current_line4)
                    current_line4 = ""
        else:
            current_line4 = ""
            
            for i in range(0, 3348):
                if code4[0][i] != " " and code4[0][i] != "\n":
                    current_line4 = current_line4 + code4[0][i]
                else:
                    code_single4.append(current_line4)
                    current_line4 = ""
    except IndexError:
        createDialog("Error", "error", "Invalid Code", None)
        return
    
    del code_single4[0:4]
    del code_single4[14:196]
    del code_single4[42::]

    for i in range(14, 28):
        del code_single4[i]
    
    for i in range(14):
        weight_code4.append(code_single4[i])
    
    for i in range(14):
        price_code4.append(code_single4[i + 14])

    for line in weight_code4:
        weights4.append(line[2:4])
    
    for line in price_code4:
        prices4.append(line[6:8])
    
    for weight in weights4:
        weights4In.append(int(weight, 16))
    
    for price in prices4:
        prices4In.append(int(price, 16))
        
    # Define a list of Entry widget attributes
    pricesNames4 = [miniPrice4, megaPrice4, superMiniPrice4, superMegaPrice4, miniMegaHammerPrice4, warpPipePrice4, swapCardPrice4, sparkyStickerPrice4, gaddlightPrice4, chompCallPrice4, bowserSuitPrice4, crystalBallPrice4, magicLampPrice4, itemBagPrice4]
    weightsNames4 = [miniWeight4, megaWeight4, superMiniWeight4, superMegaWeight4, miniMegaHammerWeight4, warpPipeWeight4, swapCardWeight4, sparkyStickerWeight4, gaddlightWeight4, chompCallWeight4, bowserSuitWeight4, crystalBallWeight4, magicLampWeight4, itemBagWeight4]
    
    if not hide_custom:
        pricesNames4.extend([mushroomPrice4, goldenMushroomPrice4, celluarShopperPrice4, bowserPhonePrice4, hiddenBlockCardPrice4])
        weightsNames4.extend([mushroomWeight4, goldenMushroomWeight4, celluarShopperWeight4, bowserPhoneWeight4, hiddenBlockCardWeight4])

    # Update widgets with loaded values
    for index, widget in enumerate(pricesNames4):
        if widget and index < len(prices4In):
            widget.delete(0, 'end')
            widget.insert(0, int(prices4In[index]))
    for index, widget in enumerate(weightsNames4):
        if widget and index < len(weights4In):
            widget.delete(0, 'end')
            widget.insert(0, int(weights4In[index]))
    print("Code loaded successfully!")
    
    top.destroy()

    createDialog("Operation Sucessful", "success", "Code loaded successfully!.", None)