# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

from codes.marioParty3 import *
from functions import *

import pyperclip


def itemsEvent_mp3(mushroom3, skeletonKey3, poisonMushroom3, reverseMushroom3, goldenMushroom3, magicLamp3, warpBlock3, celluarShopper3, bowserPhone3, duelingGlove3, luckyLamp3, bowserSuit3, plunderChest3, booBell3, booRepellant3, itemBag3):
    if not bowserPhone3.get() or not mushroom3.get() or not skeletonKey3.get() or not plunderChest3.get() or not duelingGlove3.get() or not warpBlock3.get() or not goldenMushroom3.get() or not magicLamp3.get() or not celluarShopper3.get() or not itemBag3.get() or not poisonMushroom3.get() or not reverseMushroom3.get() or not booBell3.get() or not booRepellant3.get() or not luckyLamp3.get():
        if sys.platform == "darwin":
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        else:
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        return

    mushroom3 = mushroom3.get()
    skeletonKey3 = skeletonKey3.get()
    plunderChest3 = plunderChest3.get()
    duelingGlove3 = duelingGlove3.get()
    warpBlock3 = warpBlock3.get()
    goldenMushroom3 = goldenMushroom3.get()
    magicLamp3 = magicLamp3.get()
    celluarShopper3 = celluarShopper3.get()
    itemBag3 = itemBag3.get()
    poisonMushroom3 = poisonMushroom3.get()
    reverseMushroom3 = reverseMushroom3.get()
    booBell3 = booBell3.get()
    booRepellant3 = booRepellant3.get()
    luckyLamp3 = luckyLamp3.get()
    bowserPhone3 = bowserPhone3.get()

    orbPriceMin = find_lowest_integer_with_zero(*[int(mushroom3), int(skeletonKey3), int(plunderChest3), int(duelingGlove3), int(warpBlock3), int(goldenMushroom3), int(magicLamp3), int(celluarShopper3), int(itemBag3), int(poisonMushroom3), int(reverseMushroom3), int(booBell3), int(booRepellant3), int(luckyLamp3), int(bowserPhone3)])

    try:
        mushroom3 = hex(int(mushroom3))
        if len(mushroom3) == 4:
            mushroom3 = mushroom3[2:]
        elif len(mushroom3) == 3:
            mushroom3 = "0" + mushroom3[2:]
    except:
        mushroom3 = "00"

    try:
        skeletonKey3 = hex(int(skeletonKey3))
        if len(skeletonKey3) == 4:
            skeletonKey3 = skeletonKey3[2:]
        elif len(skeletonKey3) == 3:
            skeletonKey3 = "0" + skeletonKey3[2:]
    except:
        skeletonKey3 = "00"

    try:
        plunderChest3 = hex(int(plunderChest3))
        if len(plunderChest3) == 4:
            plunderChest3 = plunderChest3[2:]
        elif len(plunderChest3) == 3:
            plunderChest3 = "0" + plunderChest3[2:]
    except:
        plunderChest3 = "00"

    try:
        duelingGlove3 = hex(int(duelingGlove3))
        if len(duelingGlove3) == 4:
            duelingGlove3 = duelingGlove3[2:]
        elif len(duelingGlove3) == 3:
            duelingGlove3 = "0" + duelingGlove3[2:]
    except:
        duelingGlove3 = "00"

    try:
        warpBlock3 = hex(int(warpBlock3))
        if len(warpBlock3) == 4:
            warpBlock3 = warpBlock3[2:]
        elif len(warpBlock3) == 3:
            warpBlock3 = "0" + warpBlock3[2:]
    except:
        warpBlock3 = "00"

    try:
        goldenMushroom3 = hex(int(goldenMushroom3))
        if len(goldenMushroom3) == 4:
            goldenMushroom3 = goldenMushroom3[2:]
        elif len(goldenMushroom3) == 3:
            goldenMushroom3 = "0" + goldenMushroom3[2:]
    except:
        goldenMushroom3 = "00"

    try:
        celluarShopper3 = hex(int(celluarShopper3))
        if len(celluarShopper3) == 4:
            celluarShopper3 = celluarShopper3[2:]
        elif len(celluarShopper3) == 3:
            celluarShopper3 = "0" + celluarShopper3[2:]
    except:
        celluarShopper3 = "00"

    try:
        magicLamp3 = hex(int(magicLamp3))
        if len(magicLamp3) == 4:
            magicLamp3 = magicLamp3[2:]
        elif len(magicLamp3) == 3:
            magicLamp3 = "0" + magicLamp3[2:]
    except:
        magicLamp3 = "00"

    try:
        poisonMushroom3 = hex(int(poisonMushroom3))
        if len(poisonMushroom3) == 4:
            poisonMushroom3 = poisonMushroom3[2:]
        elif len(poisonMushroom3) == 3:
            poisonMushroom3 = "0" + poisonMushroom3[2:]
    except:
        poisonMushroom3 = "00"

    try:
        reverseMushroom3 = hex(int(reverseMushroom3))
        if len(reverseMushroom3) == 4:
            reverseMushroom3 = reverseMushroom3[2:]
        elif len(reverseMushroom3) == 3:
            reverseMushroom3 = "0" + reverseMushroom3[2:]
    except:
        reverseMushroom3 = "00"

    try:
        booBell3 = hex(int(booBell3))
        if len(booBell3) == 4:
            booBell3 = booBell3[2:]
        elif len(booBell3) == 3:
            booBell3 = "0" + booBell3[2:]
    except:
        booBell3 = "00"

    try:
        booRepellant3 = hex(int(booRepellant3))
        if len(booRepellant3) == 4:
            booRepellant3 = booRepellant3[2:]
        elif len(booRepellant3) == 3:
            booRepellant3 = "0" + booRepellant3[2:]
    except:
        booRepellant3 = "00"

    try:
        luckyLamp3 = hex(int(luckyLamp3))
        if len(luckyLamp3) == 4:
            luckyLamp3 = luckyLamp3[2:]
        elif len(luckyLamp3) == 3:
            luckyLamp3 = "0" + luckyLamp3[2:]
    except:
        luckyLamp3 = "00"

    try:
        itemBag3 = hex(int(itemBag3))
        if len(itemBag3) == 4:
            itemBag3 = itemBag3[2:]
        elif len(itemBag3) == 3:
            itemBag3 = "0" + itemBag3[2:]
    except:
        itemBag3 = "00"

    try:
        bowserPhone3 = hex(int(bowserPhone3))
        if len(bowserPhone3) == 4:
            bowserPhone3 = bowserPhone3[2:]
        elif len(bowserPhone3) == 3:
            bowserPhone3 = "0" + bowserPhone3[2:]
    except:
        bowserPhone3 = "00"

    
    orbPriceMin = hex(int(orbPriceMin))
    if len(orbPriceMin) == 4:
        orbPriceMin = orbPriceMin[2:]
    elif len(orbPriceMin) == 3:
        orbPriceMin = "0" + orbPriceMin[2:]
    code = getItems3(mushroom3, skeletonKey3, plunderChest3, duelingGlove3, warpBlock3, goldenMushroom3, magicLamp3, celluarShopper3, poisonMushroom3, reverseMushroom3, booBell3, booRepellant3, luckyLamp3, bowserPhone3, itemBag3, bowserPhone3, orbPriceMin).upper()
    code = code.strip()
    pyperclip.copy(code)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)