# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/7/2024
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import csv
import pyperclip

def itemsEvent_mp4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4):
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
    orbWeightTotal = int(miniWeight4) + int(megaWeight4) + int(superMiniWeight4) + int(superMegaWeight4) + int(miniMegaHammerWeight4) + int(warpPipeWeight4) + int(swapCardWeight4) + int(sparkyStickerWeight4) + int(gaddlightWeight4) + int(chompCallWeight4) + int(bowserSuitWeight4) + int(crystalBallWeight4) + int(magicLampWeight4) + int(itemBagWeight4)
    orbPriceMin = find_lowest_integer(*[int(miniPrice4), int(megaPrice4), int(superMiniPrice4), int(superMegaPrice4), int(miniMegaHammerPrice4), int(warpPipePrice4), int(swapCardPrice4), int(sparkyStickerPrice4), int(gaddlightPrice4), int(chompCallPrice4), int(bowserSuitPrice4), int(crystalBallPrice4), int(magicLampPrice4), int(itemBagPrice4)])
    miniWeight4 = (int(miniWeight4) / orbWeightTotal) * 100
    megaWeight4 = (int(megaWeight4) / orbWeightTotal) * 100
    superMegaWeight4 = (int(superMegaWeight4) / orbWeightTotal) * 100
    superMiniWeight4 = (int(superMiniWeight4) / orbWeightTotal) * 100
    miniMegaHammerWeight4 = (int(miniMegaHammerWeight4) / orbWeightTotal) * 100
    warpPipeWeight4 = (int(warpPipeWeight4) / orbWeightTotal) * 100
    swapCardWeight4 = (int(swapCardWeight4) / orbWeightTotal) * 100
    sparkyStickerWeight4 = (int(sparkyStickerWeight4) / orbWeightTotal) * 100
    gaddlightWeight4 = (int(gaddlightWeight4) / orbWeightTotal) * 100
    chompCallWeight4 = (int(chompCallWeight4) / orbWeightTotal) * 100
    bowserSuitWeight4 = (int(bowserSuitWeight4) / orbWeightTotal) * 100
    crystalBallWeight4 = (int(crystalBallWeight4) / orbWeightTotal) * 100
    magicLampWeight4 = (int(magicLampWeight4) / orbWeightTotal) * 100
    itemBagWeight4 = (int(itemBagWeight4) / orbWeightTotal) * 100
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
    orbPriceMin = hex(int(orbPriceMin))
    if len(orbPriceMin) == 4:
        orbPriceMin = "00" + orbPriceMin[2:]
    elif len(orbPriceMin) == 3:
        orbPriceMin = "000" + orbPriceMin[2:]
    generatedCode = getItemModsFour(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, sparkyStickerPrice4, sparkyStickerWeight4, gaddlightPrice4, gaddlightWeight4, chompCallPrice4, chompCallWeight4, bowserSuitPrice4, bowserSuitWeight4, crystalBallPrice4, crystalBallWeight4, magicLampPrice4, magicLampWeight4, itemBagPrice4, itemBagWeight4, orbPriceMin)
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