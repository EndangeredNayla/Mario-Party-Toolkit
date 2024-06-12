# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 6/10/2024
# License: MIT
# ============================================

from codes.marioParty8 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp8(board, twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4):
    if not twiceWeight4.get() or not thricePrice4.get() or not thriceWeight4.get() or not springoPrice4.get() or not springoWeight4.get() or not slowgoPrice4.get() or not slowgoWeight4.get() or not cashzapPrice4.get() or not cashzapWeight4.get() or not bitsizePrice4.get() or not bitsizeWeight4.get() or not blowayPrice4.get() or not blowayWeight4.get() or not vampirePrice4.get() or not vampireWeight4.get() or not bowloPrice4.get() or not bowloWeight4.get() or not weeglePrice4.get() or not weegleWeight4.get() or not bowserPrice4.get() or not bowserWeight4.get() or not bulletPrice4.get() or not bulletWeight4.get() or not thwompPrice4.get() or not thwompWeight4.get() or not dueloPrice4.get()  or not dueloWeight4.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    
    board = board.get()

    twiceWeight4 = twiceWeight4.get()
    thricePrice4 = thricePrice4.get()
    thriceWeight4 = thriceWeight4.get()
    slowgoPrice4 = slowgoPrice4.get()
    slowgoWeight4 = slowgoWeight4.get()
    springoPrice4 = springoPrice4.get()
    springoWeight4 = springoWeight4.get()
    cashzapPrice4 = cashzapPrice4.get()
    cashzapWeight4 = cashzapWeight4.get()
    bitsizePrice4 = bitsizePrice4.get()
    bitsizeWeight4 = bitsizeWeight4.get()
    blowayPrice4 = blowayPrice4.get()
    blowayWeight4 = blowayWeight4.get()
    vampirePrice4 = vampirePrice4.get()
    vampireWeight4 = vampireWeight4.get()
    weeglePrice4 = weeglePrice4.get()
    weegleWeight4 = weegleWeight4.get()
    bowserPrice4 = bowserPrice4.get()
    bowserWeight4 = bowserWeight4.get()
    bowloPrice4 = bowloPrice4.get()
    bowloWeight4 = bowloWeight4.get()
    bulletPrice4 = bulletPrice4.get()
    bulletWeight4 = bulletWeight4.get()
    thwompPrice4 = thwompPrice4.get()
    thwompWeight4 = thwompWeight4.get()
    dueloPrice4 = dueloPrice4.get()
    dueloWeight4 = dueloWeight4.get()
    
    orbWeightTotal = int(twiceWeight4) + int(thriceWeight4) + int(slowgoWeight4) + int(springoWeight4) + int(cashzapWeight4) + int(bitsizeWeight4) + int(blowayWeight4) + int(vampireWeight4) + int(weegleWeight4) + int(bowserWeight4) + int(bowloWeight4) + int(bulletWeight4) + int(thwompWeight4) + int(dueloWeight4)
    
    def calculateWeight(weight):
        if orbWeightTotal < 100:
            percentage = int(weight)
            return percentage
        else:
            percentage = (int(weight) / orbWeightTotal) * 100
            if 0< percentage < 1:
                return math.ceil(percentage)
            return round(percentage)

    twiceWeight4 = calculateWeight(twiceWeight4)
    thriceWeight4 = calculateWeight(thriceWeight4)
    slowgoWeight4 = calculateWeight(slowgoWeight4)
    springoWeight4 = calculateWeight(springoWeight4)
    cashzapWeight4 = calculateWeight(cashzapWeight4)
    bitsizeWeight4 = calculateWeight(bitsizeWeight4)
    blowayWeight4 = calculateWeight(blowayWeight4)
    vampireWeight4 = calculateWeight(vampireWeight4)
    weegleWeight4 = calculateWeight(weegleWeight4)
    bowserWeight4 = calculateWeight(bowserWeight4)
    bowloWeight4 = calculateWeight(bowloWeight4)
    bulletWeight4 = calculateWeight(bulletWeight4)
    thwompWeight4 = calculateWeight(thwompWeight4)
    dueloWeight4 = calculateWeight(dueloWeight4)

    orbWeightTotal = twiceWeight4 + thriceWeight4 + springoWeight4 + slowgoWeight4 + cashzapWeight4 + bitsizeWeight4 + blowayWeight4 + vampireWeight4 + weegleWeight4 + bowserWeight4 + bowloWeight4 + bulletWeight4 + thwompWeight4 + dueloWeight4

    if orbWeightTotal < 100:
        var_names = ['twiceWeight4', 'thriceWeight4', 'slowgoWeight4', 'springoWeight4', 'cashzapWeight4', 'bitsizeWeight4', 'blowayWeight4', 'vampireWeight4', 'weegleWeight4', 'bowserWeight4', 'bowloWeight4', 'bulletWeight4', 'thwompWeight4', 'dueloWeight4']
        max_var = max(zip(var_names, (map(eval, var_names))), key=lambda tuple: tuple[1])[0]

        if max_var == 'twiceWeight4':
            twiceWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'thriceWeight4':
            thriceWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'slowgoWeight4':
            slowgoWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'springoWeight4':
            springoWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'cashzapWeight4':
            cashzapWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bitsizeWeight4':
            bitsizeWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'blowayWeight4':
            blowayWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'vampireWeight4':
            vampireWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'weegleWeight4':
            weegleWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bowserWeight4':
            bowserWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bowloWeight4':
            bowloWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bulletWeight4':
            bulletWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'thwompWeight4':
            thwompWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'dueloWeight4':
            dueloWeight4 += (100 - orbWeightTotal)

    twiceWeight4 = str(twiceWeight4)
    thriceWeight4 = str(thriceWeight4)
    slowgoWeight4 = str(slowgoWeight4)
    springoWeight4 = str(springoWeight4)
    cashzapWeight4 = str(cashzapWeight4)
    bitsizeWeight4 = str(bitsizeWeight4)
    blowayWeight4 = str(blowayWeight4)
    vampireWeight4 = str(vampireWeight4)
    weegleWeight4 = str(weegleWeight4)
    bowserWeight4 = str(bowserWeight4)
    bowloWeight4 = str(bowloWeight4)
    bulletWeight4 = str(bulletWeight4)
    thwompWeight4 = str(thwompWeight4)
    dueloWeight4 = str(dueloWeight4)

    
    try:
        twiceWeight4 = hex(int(twiceWeight4))
        if len(twiceWeight4) == 4:
            twiceWeight4 = twiceWeight4[2:]
        elif len(twiceWeight4) == 3:
            twiceWeight4 = "0" + twiceWeight4[2:]
    except:
        twiceWeight4 = "00"
    try:
        miniPrice4 = hex(int(miniPrice4))
        if len(miniPrice4) == 4:
            miniPrice4 = miniPrice4[2:]
        elif len(miniPrice4) == 3:
            miniPrice4 = "0" + miniPrice4[2:]
    except:
        miniPrice4 = "00"        
    try:
        thriceWeight4 = hex(int(thriceWeight4))
        if len(thriceWeight4) == 4:
            thriceWeight4 = thriceWeight4[2:]
        elif len(thriceWeight4) == 3:
            thriceWeight4 = "0" + thriceWeight4[2:]
    except:
        thriceWeight4 = "00"
    try:
        megaPrice4 = hex(int(megaPrice4))
        if len(megaPrice4) == 4:
            megaPrice4 = megaPrice4[2:]
        elif len(megaPrice4) == 3:
            megaPrice4 = "0" + megaPrice4[2:]
    except:
        megaPrice4 = "00"
    try:
        springoWeight4 = hex(int(springoWeight4))
        if len(springoWeight4) == 4:
            springoWeight4 = springoWeight4[2:]
        elif len(springoWeight4) == 3:
            springoWeight4 = "0" + springoWeight4[2:]
    except:
        springoWeight4 = "00"
    try:
        superMiniPrice4 = hex(int(superMiniPrice4))
        if len(superMiniPrice4) == 4:
            superMiniPrice4 = superMiniPrice4[2:]
        elif len(superMiniPrice4) == 3:
            superMiniPrice4 = "0" + superMiniPrice4[2:]
    except:
        superMiniPrice4 = "00"
    try:
        slowgoWeight4 = hex(int(slowgoWeight4))
        if len(slowgoWeight4) == 4:
            slowgoWeight4 = slowgoWeight4[2:]
        elif len(slowgoWeight4) == 3:
            slowgoWeight4 = "0" + slowgoWeight4[2:]
    except:
        slowgoWeight4 = "00"
    try:
        superMegaPrice4 = hex(int(superMegaPrice4))
        if len(superMegaPrice4) == 4:
            superMegaPrice4 = superMegaPrice4[2:]
        elif len(superMegaPrice4) == 3:
            superMegaPrice4 = "0" + superMegaPrice4[2:]
    except:
        superMegaPrice4 = "00"
    try:
        cashzapWeight4 = hex(int(cashzapWeight4))
        if len(cashzapWeight4) == 4:
            cashzapWeight4 = cashzapWeight4[2:]
        elif len(cashzapWeight4) == 3:
            cashzapWeight4 = "0" + cashzapWeight4[2:]
    except:
        cashzapWeight4 = "00"
    try:
        miniMegaHammerPrice4 = hex(int(miniMegaHammerPrice4))
        if len(miniMegaHammerPrice4) == 4:
            miniMegaHammerPrice4 = miniMegaHammerPrice4[2:]
        elif len(miniMegaHammerPrice4) == 3:
            miniMegaHammerPrice4 = "0" + miniMegaHammerPrice4[2:]
    except:
        miniMegaHammerPrice4 = "00"
    try:
        bitsizeWeight4 = hex(int(bitsizeWeight4))
        if len(bitsizeWeight4) == 4:
            bitsizeWeight4 = bitsizeWeight4[2:]
        elif len(bitsizeWeight4) == 3:
            bitsizeWeight4 = "0" + bitsizeWeight4[2:]
    except:
        bitsizeWeight4 = "00"
    try:
        warpPipePrice4 = hex(int(warpPipePrice4))
        if len(warpPipePrice4) == 4:
            warpPipePrice4 = warpPipePrice4[2:]
        elif len(warpPipePrice4) == 3:
            warpPipePrice4 = "0" + warpPipePrice4[2:]
    except:
        warpPipePrice4 = "00"
    try:
        blowayWeight4 = hex(int(blowayWeight4))
        if len(blowayWeight4) == 4:
            blowayWeight4 = blowayWeight4[2:]
        elif len(blowayWeight4) == 3:
            blowayWeight4 = "0" + blowayWeight4[2:]
    except:
        blowayWeight4 = "00"
    try:
        swapCardPrice4 = hex(int(swapCardPrice4))
        if len(swapCardPrice4) == 4:
            swapCardPrice4 = swapCardPrice4[2:]
        elif len(swapCardPrice4) == 3:
            swapCardPrice4 = "0" + swapCardPrice4[2:]
    except:
        swapCardPrice4 = "00"
    try:
        vampireWeight4 = hex(int(vampireWeight4))
        if len(vampireWeight4) == 4:
            vampireWeight4 = vampireWeight4[2:]
        elif len(vampireWeight4) == 3:
            vampireWeight4 = "0" + vampireWeight4[2:]
    except:
        vampireWeight4 = "00"
    try:
        sparkyStickerPrice4 = hex(int(sparkyStickerPrice4))
        if len(sparkyStickerPrice4) == 4:
            sparkyStickerPrice4 = sparkyStickerPrice4[2:]
        elif len(sparkyStickerPrice4) == 3:
            sparkyStickerPrice4 = "0" + sparkyStickerPrice4[2:]
    except:
        sparkyStickerPrice4 = "00"
    try:
        weegleWeight4 = hex(int(weegleWeight4))
        if len(weegleWeight4) == 4:
            weegleWeight4 = weegleWeight4[2:]
        elif len(weegleWeight4) == 3:
            weegleWeight4 = "0" + weegleWeight4[2:]
    except:
        weegleWeight4 = "00"
    try:
        gaddlightPrice4 = hex(int(gaddlightPrice4))
        if len(gaddlightPrice4) == 4:
            gaddlightPrice4 = gaddlightPrice4[2:]
        elif len(gaddlightPrice4) == 3:
            gaddlightPrice4 = "0" + gaddlightPrice4[2:]
    except:
        gaddlightPrice4 = "00"
    try:
        bowserWeight4 = hex(int(bowserWeight4))
        if len(bowserWeight4) == 4:
            bowserWeight4 = bowserWeight4[2:]
        elif len(bowserWeight4) == 3:
            bowserWeight4 = "0" + bowserWeight4[2:]
    except:
        bowserWeight4 = "00"
    try:
        chompCallPrice4 = hex(int(chompCallPrice4))
        if len(chompCallPrice4) == 4:
            chompCallPrice4 = chompCallPrice4[2:]
        elif len(chompCallPrice4) == 3:
            chompCallPrice4 = "0" + chompCallPrice4[2:]
    except:
        chompCallPrice4 = "00"
    try:
        bowloWeight4 = hex(int(bowloWeight4))
        if len(bowloWeight4) == 4:
            bowloWeight4 = bowloWeight4[2:]
        elif len(bowloWeight4) == 3:
            bowloWeight4 = "0" + bowloWeight4[2:]
    except:
        bowloWeight4 = "00"
    try:
        bowserSuitPrice4 = hex(int(bowserSuitPrice4))
        if len(bowserSuitPrice4) == 4:
            bowserSuitPrice4 = bowserSuitPrice4[2:]
        elif len(bowserSuitPrice4) == 3:
            bowserSuitPrice4 = "0" + bowserSuitPrice4[2:]
    except:
        bowserSuitPrice4 = "00"
    try:
        bulletWeight4 = hex(int(bulletWeight4))
        if len(bulletWeight4) == 4:
            bulletWeight4 = bulletWeight4[2:]
        elif len(bulletWeight4) == 3:
            bulletWeight4 = "0" + bulletWeight4[2:]
    except:
        bulletWeight4 = "00"
    try:
        crystalBallPrice4 = hex(int(crystalBallPrice4))
        if len(crystalBallPrice4) == 4:
            crystalBallPrice4 = crystalBallPrice4[2:]
        elif len(crystalBallPrice4) == 3:
            crystalBallPrice4 = "0" + crystalBallPrice4[2:]
    except:
        crystalBallPrice4 = "00"
    try:
        thwompWeight4 = hex(int(thwompWeight4))
        if len(thwompWeight4) == 4:
            thwompWeight4 = thwompWeight4[2:]
        elif len(thwompWeight4) == 3:
            thwompWeight4 = "0" + thwompWeight4[2:]
    except:
        thwompWeight4 = "00"
    try:
        magicLampPrice4 = hex(int(magicLampPrice4))
        if len(magicLampPrice4) == 4:
            magicLampPrice4 = magicLampPrice4[2:]
        elif len(magicLampPrice4) == 3:
            magicLampPrice4 = "0" + magicLampPrice4[2:]
    except:
        magicLampPrice4 = "00"
    try:
        dueloWeight4 = hex(int(dueloWeight4))
        if len(dueloWeight4) == 4:
            dueloWeight4 = dueloWeight4[2:]
        elif len(dueloWeight4) == 3:
            dueloWeight4 = "0" + dueloWeight4[2:]
    except:
        dueloWeight4 = "00"
    try:
        itemBagPrice4 = hex(int(itemBagPrice4))
        if len(itemBagPrice4) == 4:
            itemBagPrice4 = itemBagPrice4[2:]
        elif len(itemBagPrice4) == 3:
            itemBagPrice4 = "0" + itemBagPrice4[2:]
    except:
        itemBagPrice4 = "00"
    orbPriceMin = hex(int(orbPriceMin))
    if len(orbPriceMin) == 4:
        orbPriceMin = "00" + orbPriceMin[2:]
    elif len(orbPriceMin) == 3:
        orbPriceMin = "000" + orbPriceMin[2:]
    if board == "DK's Treetop Temple":
        generatedCode = getCandyCodeDK(twiceWeight4, megaPrice4, thriceWeight4, superMiniPrice4, springoWeight4, superMegaPrice4, slowgoWeight4, miniMegaHammerPrice4, cashzapWeight4, warpPipePrice4, bitsizeWeight4, swapCardPrice4, blowayWeight4, sparkyStickerPrice4, vampireWeight4, gaddlightPrice4, weegleWeight4, chompCallPrice4, bowserWeight4, bowserSuitPrice4, bowloWeight4, crystalBallPrice4, bulletWeight4, magicLampPrice4, thwompWeight4, itemBagPrice4, dueloWeight4, orbPriceMin)
    elif board == "Goomba's Booty Boardwalk":
        generatedCode = getCandyCodeGoomba(twiceWeight4, megaPrice4, thriceWeight4, superMiniPrice4, springoWeight4, superMegaPrice4, slowgoWeight4, miniMegaHammerPrice4, cashzapWeight4, warpPipePrice4, bitsizeWeight4, swapCardPrice4, blowayWeight4, sparkyStickerPrice4, vampireWeight4, gaddlightPrice4, weegleWeight4, chompCallPrice4, bowserWeight4, bowserSuitPrice4, bowloWeight4, crystalBallPrice4, bulletWeight4, magicLampPrice4, thwompWeight4, itemBagPrice4, dueloWeight4, orbPriceMin)
    elif board == "King Boo's Haunted Hideaway":
        generatedCode = getCandyCodeBoo(twiceWeight4, megaPrice4, thriceWeight4, superMiniPrice4, springoWeight4, superMegaPrice4, slowgoWeight4, miniMegaHammerPrice4, cashzapWeight4, warpPipePrice4, bitsizeWeight4, swapCardPrice4, blowayWeight4, sparkyStickerPrice4, vampireWeight4, gaddlightPrice4, weegleWeight4, chompCallPrice4, bowserWeight4, bowserSuitPrice4, bowloWeight4, crystalBallPrice4, bulletWeight4, magicLampPrice4, thwompWeight4, itemBagPrice4, dueloWeight4, orbPriceMin)
    elif board == "Shy Guy's Perplex Express":
        generatedCode = getCandyCodeShyGuy(twiceWeight4, megaPrice4, thriceWeight4, superMiniPrice4, springoWeight4, superMegaPrice4, slowgoWeight4, miniMegaHammerPrice4, cashzapWeight4, warpPipePrice4, bitsizeWeight4, swapCardPrice4, blowayWeight4, sparkyStickerPrice4, vampireWeight4, gaddlightPrice4, weegleWeight4, chompCallPrice4, bowserWeight4, bowserSuitPrice4, bowloWeight4, crystalBallPrice4, bulletWeight4, magicLampPrice4, thwompWeight4, itemBagPrice4, dueloWeight4, orbPriceMin)
    elif board == "Koopa's Tycoon Town":
        generatedCode = getCandyCodeKoopa(twiceWeight4, megaPrice4, thriceWeight4, superMiniPrice4, springoWeight4, superMegaPrice4, slowgoWeight4, miniMegaHammerPrice4, cashzapWeight4, warpPipePrice4, bitsizeWeight4, swapCardPrice4, blowayWeight4, sparkyStickerPrice4, vampireWeight4, gaddlightPrice4, weegleWeight4, chompCallPrice4, bowserWeight4, bowserSuitPrice4, bowloWeight4, crystalBallPrice4, bulletWeight4, magicLampPrice4, thwompWeight4, itemBagPrice4, dueloWeight4, orbPriceMin)
    elif board == "Bowser's Warped Orbit":
        generatedCode = getCandyCodeBowser(twiceWeight4, megaPrice4, thriceWeight4, superMiniPrice4, springoWeight4, superMegaPrice4, slowgoWeight4, miniMegaHammerPrice4, cashzapWeight4, warpPipePrice4, bitsizeWeight4, swapCardPrice4, blowayWeight4, sparkyStickerPrice4, vampireWeight4, gaddlightPrice4, weegleWeight4, chompCallPrice4, bowserWeight4, bowserSuitPrice4, bowloWeight4, crystalBallPrice4, bulletWeight4, magicLampPrice4, thwompWeight4, itemBagPrice4, dueloWeight4, orbPriceMin)

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)


def savePresetItems4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4):
    if not miniPrice4.get() or not miniWeight4.get() or not megaPrice4.get() or not megaWeight4.get() or not superMegaPrice4.get() or not superMegaWeight4.get() or not superMiniPrice4.get() or not superMiniWeight4.get() or not miniMegaHammerPrice4.get() or not miniMegaHammerWeight4.get() or not warpPipePrice4.get() or not warpPipeWeight4.get() or not swapCardPrice4.get() or not swapCardWeight4.get() or not sparkyStickerPrice4.get() or not sparkyStickerWeight4.get() or not bowserSuitPrice4.get() or not bowserSuitWeight4.get() or not gaddlightPrice4.get() or not gaddlightWeight4.get() or not chompCallPrice4.get() or not chompCallWeight4.get() or not crystalBallPrice4.get() or not crystalBallWeight4.get() or not magicLampPrice4.get() or not magicLampWeight4.get() or not itemBagPrice4.get()  or not itemBagWeight4.get():
        if sys.platform == "darwin":
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        else:
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
    prices4 = [miniPrice4, megaPrice4, superMiniPrice4, superMegaPrice4, miniMegaHammerPrice4, warpPipePrice4, swapCardPrice4, sparkyStickerPrice4, gaddlightPrice4, chompCallPrice4, bowserSuitPrice4, crystalBallPrice4, magicLampPrice4, itemBagPrice4]
    weights4 = [miniWeight4, megaWeight4, superMiniWeight4, superMegaWeight4, miniMegaHammerWeight4, warpPipeWeight4, swapCardWeight4, sparkyStickerWeight4, gaddlightWeight4, chompCallWeight4, bowserSuitWeight4, crystalBallWeight4, magicLampWeight4, itemBagWeight4]
 
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prices', 'Weights'])
            for price, weight in zip(prices4, weights4):
                writer.writerow([price, weight])
        print("MPT file saved successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

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