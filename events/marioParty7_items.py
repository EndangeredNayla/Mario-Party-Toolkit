# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

from codes.marioParty7 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp7(mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, posionMushroomWeight7, posionMushroomPrice7, dkCapsuleWeight7, dkCapsulePrice7, orbBagCapsuleWeight7, orbBagCapsulePrice7, duelCapsuleWeight7, duelCapsulePrice7, mysteryCapsuleWeight7, mysteryCapsulePrice7):
    if not mushroomCapsuleWeight7.get() or not goldenMushroomCapsulePrice7.get() or not goldenMushroomCapsuleWeight7.get() or not slowMushroomCapsulePrice7.get() or not slowMushroomCapsuleWeight7.get() or not metalMushroomCapsulePrice7.get() or not metalMushroomCapsuleWeight7.get() or not flutterCapsulePrice7.get() or not flutterCapsuleWeight7.get() or not cannonCapsulePrice7.get() or not cannonCapsuleWeight7.get() or not snackCapsulePrice7.get() or not snackCapsuleWeight7.get() or not lakituCapsulePrice7.get() or not lakituCapsuleWeight7.get() or not hammerBroCapsuleWeight7.get() or not hammerBroCapsulePrice7.get() or not plantCapsulePrice7.get() or not plantCapsuleWeight7.get() or not spearCapsuleWeight7.get() or not spearCapsulePrice7.get() or not kamekCapsuleWeight7.get() or not kamekCapsulePrice7.get() or not toadyCapsuleWeight7.get() or not toadyCapsulePrice7.get() or not blizzardCapsuleWeight7.get() or not blizzardCapsulePrice7.get() or not banditCapsulePrice7.get() or not banditCapsuleWeight7.get() or not pinkBooCapsuleWeight7.get() or not pinkBooCapsulePrice7.get() or not spinyCapsulePrice7.get() or not spinyCapsuleWeight7.get() or not zapCapsulePrice7.get() or not zapCapsuleWeight7.get() or not tweesterCapsulePrice7.get() or not tweesterCapsuleWeight7.get() or not thwompCapsulePrice7.get() or not thwompCapsuleWeight7.get() or not warpCapsulePrice7.get() or not warpCapsuleWeight7.get() or not bombCapsulePrice7.get() or not bombCapsuleWeight7.get() or not fireballCapsulePrice7.get() or not fireballCapsuleWeight7.get() or not eggCapsulePrice7.get() or not eggCapsuleWeight7.get() or not flowerCapsulePrice7.get() or not flowerCapsuleWeight7.get() or not vacuumCapsulePrice7.get() or not vacuumCapsuleWeight7.get() or not magicCapsulePrice7.get() or not magicCapsuleWeight7.get() or not tripleCapsulePrice7.get() or not tripleCapsuleWeight7.get() or not koopaCapsulePrice7.get() or not koopaCapsuleWeight7.get():
        if sys.platform == "darwin":
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        else:
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    
    mushroomCapsuleWeight7 = mushroomCapsuleWeight7.get()
    
    goldenMushroomCapsulePrice7 = goldenMushroomCapsulePrice7.get()
    goldenMushroomCapsuleWeight7 = goldenMushroomCapsuleWeight7.get()

    slowMushroomCapsulePrice7 = slowMushroomCapsulePrice7.get()
    slowMushroomCapsuleWeight7 = slowMushroomCapsuleWeight7.get()

    metalMushroomCapsulePrice7 = metalMushroomCapsulePrice7.get()
    metalMushroomCapsuleWeight7 = metalMushroomCapsuleWeight7.get()

    flutterCapsulePrice7 = flutterCapsulePrice7.get()
    flutterCapsuleWeight7 = flutterCapsuleWeight7.get()

    cannonCapsulePrice7 = cannonCapsulePrice7.get()
    cannonCapsuleWeight7 = cannonCapsuleWeight7.get()

    snackCapsulePrice7 = snackCapsulePrice7.get()
    snackCapsuleWeight7 = snackCapsuleWeight7.get()

    lakituCapsulePrice7 = lakituCapsulePrice7.get()
    lakituCapsuleWeight7 = lakituCapsuleWeight7.get()

    hammerBroCapsulePrice7 = hammerBroCapsulePrice7.get()
    hammerBroCapsuleWeight7 = hammerBroCapsuleWeight7.get()

    plantCapsulePrice7 = plantCapsulePrice7.get()
    plantCapsuleWeight7 = plantCapsuleWeight7.get()

    spearCapsulePrice7 = spearCapsulePrice7.get()
    spearCapsuleWeight7 = spearCapsuleWeight7.get()

    kamekCapsulePrice7 = kamekCapsulePrice7.get()
    kamekCapsuleWeight7 = kamekCapsuleWeight7.get()

    toadyCapsulePrice7 = toadyCapsulePrice7.get()
    toadyCapsuleWeight7 = toadyCapsuleWeight7.get()

    blizzardCapsulePrice7 = blizzardCapsulePrice7.get()
    blizzardCapsuleWeight7 = blizzardCapsuleWeight7.get()

    banditCapsulePrice7 = banditCapsulePrice7.get()
    banditCapsuleWeight7 = banditCapsuleWeight7.get()

    pinkBooCapsulePrice7 = pinkBooCapsulePrice7.get()
    pinkBooCapsuleWeight7 = pinkBooCapsuleWeight7.get()

    spinyCapsulePrice7 = spinyCapsulePrice7.get()
    spinyCapsuleWeight7 = spinyCapsuleWeight7.get()

    zapCapsulePrice7 = zapCapsulePrice7.get()
    zapCapsuleWeight7 = zapCapsuleWeight7.get()

    tweesterCapsulePrice7 = tweesterCapsulePrice7.get()
    tweesterCapsuleWeight7 = tweesterCapsuleWeight7.get()

    thwompCapsulePrice7 = thwompCapsulePrice7.get()
    thwompCapsuleWeight7 = thwompCapsuleWeight7.get()

    warpCapsulePrice7 = warpCapsulePrice7.get()
    warpCapsuleWeight7 = warpCapsuleWeight7.get()

    bombCapsulePrice7 = bombCapsulePrice7.get()
    bombCapsuleWeight7 = bombCapsuleWeight7.get()

    fireballCapsulePrice7 = fireballCapsulePrice7.get()
    fireballCapsuleWeight7 = fireballCapsuleWeight7.get()

    flowerCapsulePrice7 = flowerCapsulePrice7.get()
    flowerCapsuleWeight7 = flowerCapsuleWeight7.get()

    eggCapsulePrice7 = eggCapsulePrice7.get()
    eggCapsuleWeight7 = eggCapsuleWeight7.get()

    vacuumCapsulePrice7 = vacuumCapsulePrice7.get()
    vacuumCapsuleWeight7 = vacuumCapsuleWeight7.get()

    magicCapsulePrice7 = magicCapsulePrice7.get()
    magicCapsuleWeight7 = magicCapsuleWeight7.get()

    tripleCapsulePrice7 = tripleCapsulePrice7.get()
    tripleCapsuleWeight7 = tripleCapsuleWeight7.get()

    koopaCapsulePrice7 = koopaCapsulePrice7.get()
    koopaCapsuleWeight7 = koopaCapsuleWeight7.get()

    try:
        orbBagCapsulePrice7 = orbBagCapsulePrice7.get()
    except:
        orbBagCapsulePrice7 = 00

    try:
        orbBagCapsuleWeight7 = orbBagCapsuleWeight7.get()
    except:
        orbBagCapsuleWeight7 = 00

    try:
        dkCapsulePrice7 = dkCapsulePrice7.get()
    except:
        dkCapsulePrice7 = 00

    try:
        dkCapsuleWeight7 = dkCapsuleWeight7.get()
    except:
        dkCapsuleWeight7 = 00

    try:
        posionMushroomPrice7 = posionMushroomPrice7.get()
    except:
        posionMushroomPrice7 = 00

    try:
        posionMushroomWeight7 = posionMushroomWeight7.get()
    except:
        posionMushroomWeight7 = 00

    try:
        duelCapsulePrice7 = duelCapsulePrice7.get()
    except:
        duelCapsulePrice7 = 00

    try:
        duelCapsuleWeight7 = duelCapsuleWeight7.get()
    except:
        duelCapsuleWeight7 = 00

    try:
        mysteryCapsulePrice7 = mysteryCapsulePrice7.get()
    except:
        mysteryCapsulePrice7 = 00

    try:
        mysteryCapsuleWeight7 = mysteryCapsuleWeight7.get()
    except:
        mysteryCapsuleWeight7 = 00
    
    orbWeightTotal = int(mushroomCapsuleWeight7) + int(goldenMushroomCapsuleWeight7) + int(metalMushroomCapsuleWeight7) + int(slowMushroomCapsuleWeight7) + int(flutterCapsuleWeight7) + int(cannonCapsuleWeight7) + int(snackCapsuleWeight7) + int(lakituCapsuleWeight7) + int(hammerBroCapsuleWeight7) + int(plantCapsuleWeight7) + int(spearCapsuleWeight7) + int(kamekCapsuleWeight7) + int(toadyCapsuleWeight7) + int(blizzardCapsuleWeight7) + int(banditCapsuleWeight7) + int(pinkBooCapsuleWeight7) + int(spinyCapsuleWeight7) + int(zapCapsuleWeight7) + int(tweesterCapsuleWeight7) + int(thwompCapsuleWeight7) + int(warpCapsuleWeight7) + int(bombCapsuleWeight7) + int(fireballCapsuleWeight7) + int(flowerCapsuleWeight7) + int(eggCapsuleWeight7) + int(vacuumCapsuleWeight7) + int(magicCapsuleWeight7) + int(tripleCapsuleWeight7) + int(koopaCapsuleWeight7) + int(mysteryCapsuleWeight7) + int(duelCapsuleWeight7) + int(dkCapsuleWeight7) + int(mysteryCapsuleWeight7) + int(orbBagCapsuleWeight7)

    def calculateWeight(weight):
        if orbWeightTotal < 100:
            percentage = int(weight)
            return percentage
        else:
            percentage = (int(weight) / orbWeightTotal) * 100
            if 0< percentage < 1:
                return math.ceil(percentage)
            return round(percentage)
        
    mushroomCapsuleWeight7 = calculateWeight(mushroomCapsuleWeight7)
    goldenMushroomCapsuleWeight7 = calculateWeight(goldenMushroomCapsuleWeight7)
    metalMushroomCapsuleWeight7 = calculateWeight(metalMushroomCapsuleWeight7)
    slowMushroomCapsuleWeight7 = calculateWeight(slowMushroomCapsuleWeight7)
    flutterCapsuleWeight7 = calculateWeight(flutterCapsuleWeight7)
    cannonCapsuleWeight7 = calculateWeight(cannonCapsuleWeight7)
    snackCapsuleWeight7 = calculateWeight(snackCapsuleWeight7)
    lakituCapsuleWeight7 = calculateWeight(lakituCapsuleWeight7)
    hammerBroCapsuleWeight7 = calculateWeight(hammerBroCapsuleWeight7)
    plantCapsuleWeight7 = calculateWeight(plantCapsuleWeight7)
    spearCapsuleWeight7 = calculateWeight(spearCapsuleWeight7)
    kamekCapsuleWeight7 = calculateWeight(kamekCapsuleWeight7)
    toadyCapsuleWeight7 = calculateWeight(toadyCapsuleWeight7)
    blizzardCapsuleWeight7 = calculateWeight(blizzardCapsuleWeight7)
    banditCapsuleWeight7 = calculateWeight(banditCapsuleWeight7)
    pinkBooCapsuleWeight7 = calculateWeight(pinkBooCapsuleWeight7)
    spinyCapsuleWeight7 = calculateWeight(spinyCapsuleWeight7)
    zapCapsuleWeight7 = calculateWeight(zapCapsuleWeight7)
    tweesterCapsuleWeight7 = calculateWeight(tweesterCapsuleWeight7)
    thwompCapsuleWeight7 = calculateWeight(thwompCapsuleWeight7)
    warpCapsuleWeight7 = calculateWeight(warpCapsuleWeight7)
    bombCapsuleWeight7 = calculateWeight(bombCapsuleWeight7)
    fireballCapsuleWeight7 = calculateWeight(fireballCapsuleWeight7)
    flowerCapsuleWeight7 = calculateWeight(flowerCapsuleWeight7)
    eggCapsuleWeight7 = calculateWeight(eggCapsuleWeight7)
    vacuumCapsuleWeight7 = calculateWeight(vacuumCapsuleWeight7)
    magicCapsuleWeight7 = calculateWeight(magicCapsuleWeight7)
    tripleCapsuleWeight7 = calculateWeight(tripleCapsuleWeight7)
    orbBagCapsuleWeight7 = calculateWeight(orbBagCapsuleWeight7)
    posionMushroomWeight7 = calculateWeight(posionMushroomWeight7)
    dkCapsuleWeight7 = calculateWeight(dkCapsuleWeight7)
    duelCapsuleWeight7 = calculateWeight(duelCapsuleWeight7)
    mysteryCapsuleWeight7 = calculateWeight(mysteryCapsuleWeight7)
    koopaCapsuleWeight7 = calculateWeight(koopaCapsuleWeight7)

    orbWeightTotal = mushroomCapsuleWeight7 + goldenMushroomCapsuleWeight7 + metalMushroomCapsuleWeight7 + slowMushroomCapsuleWeight7 + flutterCapsuleWeight7 + cannonCapsuleWeight7 + snackCapsuleWeight7 + lakituCapsuleWeight7 + hammerBroCapsuleWeight7 + plantCapsuleWeight7 + spearCapsuleWeight7 + kamekCapsuleWeight7 + toadyCapsuleWeight7 + blizzardCapsuleWeight7 + banditCapsuleWeight7 + pinkBooCapsuleWeight7 + spinyCapsuleWeight7 + zapCapsuleWeight7 + tweesterCapsuleWeight7 + thwompCapsuleWeight7 + warpCapsuleWeight7 + bombCapsuleWeight7 + fireballCapsuleWeight7 + flowerCapsuleWeight7 + eggCapsuleWeight7 + vacuumCapsuleWeight7 + magicCapsuleWeight7 + tripleCapsuleWeight7 + koopaCapsuleWeight7 + mysteryCapsuleWeight7 + duelCapsuleWeight7 + dkCapsuleWeight7 + orbBagCapsuleWeight7 + posionMushroomWeight7
    
    if orbWeightTotal < 100:
        var_names = ['mushroomCapsuleWeight7', 'goldenMushroomCapsuleWeight7', 'metalMushroomCapsuleWeight7', 'slowMushroomCapsuleWeight7', 'flutterCapsuleWeight7', 'cannonCapsuleWeight7', 'snackCapsuleWeight7', 'lakituCapsuleWeight7', 'hammerBroCapsuleWeight7', 'plantCapsuleWeight7', 'spearCapsuleWeight7', 'kamekCapsuleWeight7', 'toadyCapsuleWeight7', 'blizzardCapsuleWeight7', 'banditCapsuleWeight7', 'pinkBooCapsuleWeight7', 'spinyCapsuleWeight7', 'zapCapsuleWeight7', 'tweesterCapsuleWeight7', 'thwompCapsuleWeight7', 'warpCapsuleWeight7', 'bombCapsuleWeight7', 'fireballCapsuleWeight7', 'flowerCapsuleWeight7', 'eggCapsuleWeight7', 'vacuumCapsuleWeight7', 'magicCapsuleWeight7', 'tripleCapsuleWeight7', 'koopaCapsuleWeight7', 'mysteryCapsuleWeight7', 'duelCapsuleWeight7', 'dkCapsuleWeight7', 'orbBagCapsuleWeight7', 'posionMushroomWeight7']
        max_var = max(zip(var_names, (map(eval, var_names))), key=lambda tuple: tuple[1])[0]

        if max_var == 'mushroomCapsuleWeight7':
            mushroomCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'goldenMushroomCapsuleWeight7':
            goldenMushroomCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'metalMushroomCapsuleWeight7':
            metalMushroomCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'slowMushroomCapsuleWeight7':
            slowMushroomCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'flutterCapsuleWeight7':
            flutterCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'cannonCapsuleWeight7':
            cannonCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'snackCapsuleWeight7':
            snackCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'lakituCapsuleWeight7':
            lakituCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'hammerBroCapsuleWeight7':
            hammerBroCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'plantCapsuleWeight7':
            plantCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'spearCapsuleWeight7':
            spearCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'kamekCapsuleWeight7':
            kamekCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'toadyCapsuleWeight7':
            toadyCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'blizzardCapsuleWeight7':
            blizzardCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'banditCapsuleWeight7':
            banditCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'pinkBooCapsuleWeight7':
            pinkBooCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'spinyCapsuleWeight7':
            spinyCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'zapCapsuleWeight7':
            zapCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'tweesterCapsuleWeight7':
            tweesterCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'thwompCapsuleWeight7':
            thwompCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'warpCapsuleWeight7':
            warpCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'bombCapsuleWeight7':
            bombCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'fireballCapsuleWeight7':
            fireballCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'flowerCapsuleWeight7':
            flowerCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'eggCapsuleWeight7':
            eggCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'vacuumCapsuleWeight7':
            vacuumCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'magicCapsuleWeight7':
            magicCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'tripleCapsuleWeight7':
            tripleCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'koopaCapsuleWeight7':
            koopaCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'duelCapsuleWeight7':
            duelCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'dkCapsuleWeight7':
            dkCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'posionMushroomWeight7':
            posionMushroomWeight7 += (100 - orbWeightTotal)

        if max_var == 'mysteryCapsuleWeight7':
            mysteryCapsuleWeight7 += (100 - orbWeightTotal)

        if max_var == 'orbBagCapsuleWeight7':
            orbBagCapsuleWeight7 += (100 - orbWeightTotal)

    mushroomCapsuleWeight7 = str(mushroomCapsuleWeight7)
    goldenMushroomCapsuleWeight7 = str(goldenMushroomCapsuleWeight7)
    metalMushroomCapsuleWeight7 = str(metalMushroomCapsuleWeight7)
    slowMushroomCapsuleWeight7 = str(slowMushroomCapsuleWeight7)
    flutterCapsuleWeight7 = str(flutterCapsuleWeight7)
    cannonCapsuleWeight7 = str(cannonCapsuleWeight7)
    snackCapsuleWeight7 = str(snackCapsuleWeight7)
    lakituCapsuleWeight7 = str(lakituCapsuleWeight7)
    hammerBroCapsuleWeight7 = str(hammerBroCapsuleWeight7)
    plantCapsuleWeight7 = str(plantCapsuleWeight7)
    spearCapsuleWeight7 = str(spearCapsuleWeight7)
    kamekCapsuleWeight7 = str(kamekCapsuleWeight7)
    toadyCapsuleWeight7 = str(toadyCapsuleWeight7)
    blizzardCapsuleWeight7 = str(blizzardCapsuleWeight7)
    banditCapsuleWeight7 = str(banditCapsuleWeight7)
    pinkBooCapsuleWeight7 = str(pinkBooCapsuleWeight7)
    spinyCapsuleWeight7 = str(spinyCapsuleWeight7)
    zapCapsuleWeight7 = str(zapCapsuleWeight7)
    tweesterCapsuleWeight7 = str(tweesterCapsuleWeight7)
    thwompCapsuleWeight7 = str(thwompCapsuleWeight7)
    warpCapsuleWeight7 = str(warpCapsuleWeight7)
    bombCapsuleWeight7 = str(bombCapsuleWeight7)
    fireballCapsuleWeight7 = str(fireballCapsuleWeight7)
    flowerCapsuleWeight7 = str(flowerCapsuleWeight7)
    eggCapsuleWeight7 = str(eggCapsuleWeight7)
    vacuumCapsuleWeight7 = str(vacuumCapsuleWeight7)
    magicCapsuleWeight7 = str(magicCapsuleWeight7)
    tripleCapsuleWeight7 = str(tripleCapsuleWeight7)
    koopaCapsuleWeight7 = str(koopaCapsuleWeight7)
    duelCapsuleWeight7 = str(duelCapsuleWeight7)
    dkCapsuleWeight7 = str(dkCapsuleWeight7)
    posionMushroomWeight7 = str(posionMushroomWeight7)
    mysteryCapsuleWeight7 = str(mysteryCapsuleWeight7)
    orbBagCapsuleWeight7 = str(orbBagCapsuleWeight7)

    try:
        mushroomCapsuleWeight7 = hex(int(mushroomCapsuleWeight7))
        if len(mushroomCapsuleWeight7) == 4:
            mushroomCapsuleWeight7 = mushroomCapsuleWeight7[2:]
        elif len(mushroomCapsuleWeight7) == 3:
            mushroomCapsuleWeight7 = "0" + mushroomCapsuleWeight7[2:]
    except:
        mushroomCapsuleWeight7 = "00"

    try:
        goldenMushroomCapsuleWeight7 = hex(int(goldenMushroomCapsuleWeight7))
        if len(goldenMushroomCapsuleWeight7) == 4:
            goldenMushroomCapsuleWeight7 = goldenMushroomCapsuleWeight7[2:]
        elif len(goldenMushroomCapsuleWeight7) == 3:
            goldenMushroomCapsuleWeight7 = "0" + goldenMushroomCapsuleWeight7[2:]
    except:
        goldenMushroomCapsuleWeight7 = "00"

    try:
        goldenMushroomCapsulePrice7 = hex(int(goldenMushroomCapsulePrice7))
        if len(goldenMushroomCapsulePrice7) == 4:
            goldenMushroomCapsulePrice7 = goldenMushroomCapsulePrice7[2:]
        elif len(goldenMushroomCapsulePrice7) == 3:
            goldenMushroomCapsulePrice7 = "0" + goldenMushroomCapsulePrice7[2:]
    except:
        goldenMushroomCapsulePrice7 = "00"
    
    try:
        slowMushroomCapsuleWeight7 = hex(int(slowMushroomCapsuleWeight7))
        if len(slowMushroomCapsuleWeight7) == 4:
            slowMushroomCapsuleWeight7 = slowMushroomCapsuleWeight7[2:]
        elif len(slowMushroomCapsuleWeight7) == 3:
            slowMushroomCapsuleWeight7 = "0" + slowMushroomCapsuleWeight7[2:]
    except:
        slowMushroomCapsuleWeight7 = "00"

    try:
        slowMushroomCapsulePrice7 = hex(int(slowMushroomCapsulePrice7))
        if len(slowMushroomCapsulePrice7) == 4:
            slowMushroomCapsulePrice7 = slowMushroomCapsulePrice7[2:]
        elif len(slowMushroomCapsulePrice7) == 3:
            slowMushroomCapsulePrice7 = "0" + slowMushroomCapsulePrice7[2:]
    except:
        slowMushroomCapsulePrice7 = "00"

    try:
        metalMushroomCapsuleWeight7 = hex(int(metalMushroomCapsuleWeight7))
        if len(metalMushroomCapsuleWeight7) == 4:
            metalMushroomCapsuleWeight7 = metalMushroomCapsuleWeight7[2:]
        elif len(metalMushroomCapsuleWeight7) == 3:
            metalMushroomCapsuleWeight7 = "0" + metalMushroomCapsuleWeight7[2:]
    except:
        metalMushroomCapsuleWeight7 = "00"

    try:
        metalMushroomCapsulePrice7 = hex(int(metalMushroomCapsulePrice7))
        if len(metalMushroomCapsulePrice7) == 4:
            metalMushroomCapsulePrice7 = metalMushroomCapsulePrice7[2:]
        elif len(metalMushroomCapsulePrice7) == 3:
            metalMushroomCapsulePrice7 = "0" + metalMushroomCapsulePrice7[2:]
    except:
        metalMushroomCapsulePrice7 = "00"

    try:
        flutterCapsuleWeight7 = hex(int(flutterCapsuleWeight7))
        if len(flutterCapsuleWeight7) == 4:
            flutterCapsuleWeight7 = flutterCapsuleWeight7[2:]
        elif len(flutterCapsuleWeight7) == 3:
            flutterCapsuleWeight7 = "0" + flutterCapsuleWeight7[2:]
    except:
        flutterCapsuleWeight7 = "00"

    try:
        flutterCapsulePrice7 = hex(int(flutterCapsulePrice7))
        if len(flutterCapsulePrice7) == 4:
            flutterCapsulePrice7 = flutterCapsulePrice7[2:]
        elif len(flutterCapsulePrice7) == 3:
            flutterCapsulePrice7 = "0" + flutterCapsulePrice7[2:]
    except:
        flutterCapsulePrice7 = "00"

    try:
        cannonCapsuleWeight7 = hex(int(cannonCapsuleWeight7))
        if len(cannonCapsuleWeight7) == 4:
            cannonCapsuleWeight7 = cannonCapsuleWeight7[2:]
        elif len(cannonCapsuleWeight7) == 3:
            cannonCapsuleWeight7 = "0" + cannonCapsuleWeight7[2:]
    except:
        cannonCapsuleWeight7 = "00"

    try:
        cannonCapsulePrice7 = hex(int(cannonCapsulePrice7))
        if len(cannonCapsulePrice7) == 4:
            cannonCapsulePrice7 = cannonCapsulePrice7[2:]
        elif len(cannonCapsulePrice7) == 3:
            cannonCapsulePrice7 = "0" + cannonCapsulePrice7[2:]
    except:
        cannonCapsulePrice7 = "00"

    try:
        snackCapsuleWeight7 = hex(int(snackCapsuleWeight7))
        if len(snackCapsuleWeight7) == 4:
            snackCapsuleWeight7 = snackCapsuleWeight7[2:]
        elif len(snackCapsuleWeight7) == 3:
            snackCapsuleWeight7 = "0" + snackCapsuleWeight7[2:]
    except:
        snackCapsuleWeight7 = "00"

    try:
        snackCapsulePrice7 = hex(int(snackCapsulePrice7))
        if len(snackCapsulePrice7) == 4:
            snackCapsulePrice7 = snackCapsulePrice7[2:]
        elif len(snackCapsulePrice7) == 3:
            snackCapsulePrice7 = "0" + snackCapsulePrice7[2:]
    except:
        snackCapsulePrice7 = "00"

    try:
        lakituCapsuleWeight7 = hex(int(lakituCapsuleWeight7))
        if len(lakituCapsuleWeight7) == 4:
            lakituCapsuleWeight7 = lakituCapsuleWeight7[2:]
        elif len(lakituCapsuleWeight7) == 3:
            lakituCapsuleWeight7 = "0" + lakituCapsuleWeight7[2:]
    except:
        lakituCapsuleWeight7 = "00"

    try:
        lakituCapsulePrice7 = hex(int(lakituCapsulePrice7))
        if len(lakituCapsulePrice7) == 4:
            lakituCapsulePrice7 = lakituCapsulePrice7[2:]
        elif len(lakituCapsulePrice7) == 3:
            lakituCapsulePrice7 = "0" + lakituCapsulePrice7[2:]
    except:
        lakituCapsulePrice7 = "00"

    try:
        hammerBroCapsuleWeight7 = hex(int(hammerBroCapsuleWeight7))
        if len(hammerBroCapsuleWeight7) == 4:
            hammerBroCapsuleWeight7 = hammerBroCapsuleWeight7[2:]
        elif len(hammerBroCapsuleWeight7) == 3:
            hammerBroCapsuleWeight7 = "0" + hammerBroCapsuleWeight7[2:]
    except:
        hammerBroCapsuleWeight7 = "00"

    try:
        hammerBroCapsulePrice7 = hex(int(hammerBroCapsulePrice7))
        if len(hammerBroCapsulePrice7) == 4:
            hammerBroCapsulePrice7 = hammerBroCapsulePrice7[2:]
        elif len(hammerBroCapsulePrice7) == 3:
            hammerBroCapsulePrice7 = "0" + hammerBroCapsulePrice7[2:]
    except:
        hammerBroCapsulePrice7 = "00"

    try:
        plantCapsuleWeight7 = hex(int(plantCapsuleWeight7))
        if len(plantCapsuleWeight7) == 4:
            plantCapsuleWeight7 = plantCapsuleWeight7[2:]
        elif len(plantCapsuleWeight7) == 3:
            plantCapsuleWeight7 = "0" + plantCapsuleWeight7[2:]
    except:
        plantCapsuleWeight7 = "00"

    try:
        plantCapsulePrice7 = hex(int(plantCapsulePrice7))
        if len(plantCapsulePrice7) == 4:
            plantCapsulePrice7 = plantCapsulePrice7[2:]
        elif len(plantCapsulePrice7) == 3:
            plantCapsulePrice7 = "0" + plantCapsulePrice7[2:]
    except:
        plantCapsulePrice7 = "00"

    try:
        spearCapsuleWeight7 = hex(int(spearCapsuleWeight7))
        if len(spearCapsuleWeight7) == 4:
            spearCapsuleWeight7 = spearCapsuleWeight7[2:]
        elif len(spearCapsuleWeight7) == 3:
            spearCapsuleWeight7 = "0" + spearCapsuleWeight7[2:]
    except:
        spearCapsuleWeight7 = "00"

    try:
        spearCapsulePrice7 = hex(int(spearCapsulePrice7))
        if len(spearCapsulePrice7) == 4:
            spearCapsulePrice7 = spearCapsulePrice7[2:]
        elif len(spearCapsulePrice7) == 3:
            spearCapsulePrice7 = "0" + spearCapsulePrice7[2:]
    except:
        spearCapsulePrice7 = "00"

    try:
        kamekCapsuleWeight7 = hex(int(kamekCapsuleWeight7))
        if len(kamekCapsuleWeight7) == 4:
            kamekCapsuleWeight7 = kamekCapsuleWeight7[2:]
        elif len(kamekCapsuleWeight7) == 3:
            kamekCapsuleWeight7 = "0" + kamekCapsuleWeight7[2:]
    except:
        kamekCapsuleWeight7 = "00"

    try:
        kamekCapsulePrice7 = hex(int(kamekCapsulePrice7))
        if len(kamekCapsulePrice7) == 4:
            kamekCapsulePrice7 = kamekCapsulePrice7[2:]
        elif len(kamekCapsulePrice7) == 3:
            kamekCapsulePrice7 = "0" + kamekCapsulePrice7[2:]
    except:
        kamekCapsulePrice7 = "00"

    try:
        toadyCapsuleWeight7 = hex(int(toadyCapsuleWeight7))
        if len(toadyCapsuleWeight7) == 4:
            toadyCapsuleWeight7 = toadyCapsuleWeight7[2:]
        elif len(toadyCapsuleWeight7) == 3:
            toadyCapsuleWeight7 = "0" + toadyCapsuleWeight7[2:]
    except:
        toadyCapsuleWeight7 = "00"

    try:
        toadyCapsulePrice7 = hex(int(toadyCapsulePrice7))
        if len(toadyCapsulePrice7) == 4:
            toadyCapsulePrice7 = toadyCapsulePrice7[2:]
        elif len(toadyCapsulePrice7) == 3:
            toadyCapsulePrice7 = "0" + toadyCapsulePrice7[2:]
    except:
        toadyCapsulePrice7 = "00"

    try:
        blizzardCapsuleWeight7 = hex(int(blizzardCapsuleWeight7))
        if len(blizzardCapsuleWeight7) == 4:
            blizzardCapsuleWeight7 = blizzardCapsuleWeight7[2:]
        elif len(blizzardCapsuleWeight7) == 3:
            blizzardCapsuleWeight7 = "0" + blizzardCapsuleWeight7[2:]
    except:
        blizzardCapsuleWeight7 = "00"

    try:
        blizzardCapsulePrice7 = hex(int(blizzardCapsulePrice7))
        if len(blizzardCapsulePrice7) == 4:
            blizzardCapsulePrice7 = blizzardCapsulePrice7[2:]
        elif len(blizzardCapsulePrice7) == 3:
            blizzardCapsulePrice7 = "0" + blizzardCapsulePrice7[2:]
    except:
        blizzardCapsulePrice7 = "00"

    try:
        banditCapsuleWeight7 = hex(int(banditCapsuleWeight7))
        if len(banditCapsuleWeight7) == 4:
            banditCapsuleWeight7 = banditCapsuleWeight7[2:]
        elif len(banditCapsuleWeight7) == 3:
            banditCapsuleWeight7 = "0" + banditCapsuleWeight7[2:]
    except:
        banditCapsuleWeight7 = "00"

    try:
        banditCapsulePrice7 = hex(int(banditCapsulePrice7))
        if len(banditCapsulePrice7) == 4:
            banditCapsulePrice7 = banditCapsulePrice7[2:]
        elif len(banditCapsulePrice7) == 3:
            banditCapsulePrice7 = "0" + banditCapsulePrice7[2:]
    except:
        banditCapsulePrice7 = "00"

    try:
        pinkBooCapsuleWeight7 = hex(int(pinkBooCapsuleWeight7))
        if len(pinkBooCapsuleWeight7) == 4:
            pinkBooCapsuleWeight7 = pinkBooCapsuleWeight7[2:]
        elif len(pinkBooCapsuleWeight7) == 3:
            pinkBooCapsuleWeight7 = "0" + pinkBooCapsuleWeight7[2:]
    except:
        pinkBooCapsuleWeight7 = "00"

    try:
        pinkBooCapsulePrice7 = hex(int(pinkBooCapsulePrice7))
        if len(pinkBooCapsulePrice7) == 4:
            pinkBooCapsulePrice7 = pinkBooCapsulePrice7[2:]
        elif len(pinkBooCapsulePrice7) == 3:
            pinkBooCapsulePrice7 = "0" + pinkBooCapsulePrice7[2:]
    except:
        pinkBooCapsulePrice7 = "00"

    try:
        spinyCapsuleWeight7 = hex(int(spinyCapsuleWeight7))
        if len(spinyCapsuleWeight7) == 4:
            spinyCapsuleWeight7 = spinyCapsuleWeight7[2:]
        elif len(spinyCapsuleWeight7) == 3:
            spinyCapsuleWeight7 = "0" + spinyCapsuleWeight7[2:]
    except:
        spinyCapsuleWeight7 = "00"

    try:
        spinyCapsulePrice7 = hex(int(spinyCapsulePrice7))
        if len(spinyCapsulePrice7) == 4:
            spinyCapsulePrice7 = spinyCapsulePrice7[2:]
        elif len(spinyCapsulePrice7) == 3:
            spinyCapsulePrice7 = "0" + spinyCapsulePrice7[2:]
    except:
        spinyCapsulePrice7 = "00"

    try:
        zapCapsuleWeight7 = hex(int(zapCapsuleWeight7))
        if len(zapCapsuleWeight7) == 4:
            zapCapsuleWeight7 = zapCapsuleWeight7[2:]
        elif len(zapCapsuleWeight7) == 3:
            zapCapsuleWeight7 = "0" + zapCapsuleWeight7[2:]
    except:
        zapCapsuleWeight7 = "00"

    try:
        zapCapsulePrice7 = hex(int(zapCapsulePrice7))
        if len(zapCapsulePrice7) == 4:
            zapCapsulePrice7 = zapCapsulePrice7[2:]
        elif len(zapCapsulePrice7) == 3:
            zapCapsulePrice7 = "0" + zapCapsulePrice7[2:]
    except:
        zapCapsulePrice7 = "00"

    try:
        tweesterCapsuleWeight7 = hex(int(tweesterCapsuleWeight7))
        if len(tweesterCapsuleWeight7) == 4:
            tweesterCapsuleWeight7 = tweesterCapsuleWeight7[2:]
        elif len(tweesterCapsuleWeight7) == 3:
            tweesterCapsuleWeight7 = "0" + tweesterCapsuleWeight7[2:]
    except:
        tweesterCapsuleWeight7 = "00"

    try:
        tweesterCapsulePrice7 = hex(int(tweesterCapsulePrice7))
        if len(tweesterCapsulePrice7) == 4:
            tweesterCapsulePrice7 = tweesterCapsulePrice7[2:]
        elif len(tweesterCapsulePrice7) == 3:
            tweesterCapsulePrice7 = "0" + tweesterCapsulePrice7[2:]
    except:
        tweesterCapsulePrice7 = "00"

    try:
        thwompCapsuleWeight7 = hex(int(thwompCapsuleWeight7))
        if len(thwompCapsuleWeight7) == 4:
            thwompCapsuleWeight7 = thwompCapsuleWeight7[2:]
        elif len(thwompCapsuleWeight7) == 3:
            thwompCapsuleWeight7 = "0" + thwompCapsuleWeight7[2:]
    except:
        thwompCapsuleWeight7 = "00"

    try:
        thwompCapsulePrice7 = hex(int(thwompCapsulePrice7))
        if len(thwompCapsulePrice7) == 4:
            thwompCapsulePrice7 = thwompCapsulePrice7[2:]
        elif len(thwompCapsulePrice7) == 3:
            thwompCapsulePrice7 = "0" + thwompCapsulePrice7[2:]
    except:
        thwompCapsulePrice7 = "00"


    try:
        warpCapsuleWeight7 = hex(int(warpCapsuleWeight7))
        if len(warpCapsuleWeight7) == 4:
            warpCapsuleWeight7 = warpCapsuleWeight7[2:]
        elif len(warpCapsuleWeight7) == 3:
            warpCapsuleWeight7 = "0" + warpCapsuleWeight7[2:]
    except:
        warpCapsuleWeight7 = "00"

    try:
        warpCapsulePrice7 = hex(int(warpCapsulePrice7))
        if len(warpCapsulePrice7) == 4:
            warpCapsulePrice7 = warpCapsulePrice7[2:]
        elif len(warpCapsulePrice7) == 3:
            warpCapsulePrice7 = "0" + warpCapsulePrice7[2:]
    except:
        warpCapsulePrice7 = "00"

    try:
        bombCapsuleWeight7 = hex(int(bombCapsuleWeight7))
        if len(bombCapsuleWeight7) == 4:
            bombCapsuleWeight7 = bombCapsuleWeight7[2:]
        elif len(bombCapsuleWeight7) == 3:
            bombCapsuleWeight7 = "0" + bombCapsuleWeight7[2:]
    except:
        bombCapsuleWeight7 = "00"

    try:
        bombCapsulePrice7 = hex(int(bombCapsulePrice7))
        if len(bombCapsulePrice7) == 4:
            bombCapsulePrice7 = bombCapsulePrice7[2:]
        elif len(bombCapsulePrice7) == 3:
            bombCapsulePrice7 = "0" + bombCapsulePrice7[2:]
    except:
        bombCapsulePrice7 = "00"

    try:
        fireballCapsuleWeight7 = hex(int(fireballCapsuleWeight7))
        if len(fireballCapsuleWeight7) == 4:
            fireballCapsuleWeight7 = fireballCapsuleWeight7[2:]
        elif len(fireballCapsuleWeight7) == 3:
            fireballCapsuleWeight7 = "0" + fireballCapsuleWeight7[2:]
    except:
        fireballCapsuleWeight7 = "00"

    try:
        fireballCapsulePrice7 = hex(int(fireballCapsulePrice7))
        if len(fireballCapsulePrice7) == 4:
            fireballCapsulePrice7 = fireballCapsulePrice7[2:]
        elif len(fireballCapsulePrice7) == 3:
            fireballCapsulePrice7 = "0" + fireballCapsulePrice7[2:]
    except:
        fireballCapsulePrice7 = "00"

    try:
        flowerCapsuleWeight7 = hex(int(flowerCapsuleWeight7))
        if len(flowerCapsuleWeight7) == 4:
            flowerCapsuleWeight7 = flowerCapsuleWeight7[2:]
        elif len(flowerCapsuleWeight7) == 3:
            flowerCapsuleWeight7 = "0" + flowerCapsuleWeight7[2:]
    except:
        flowerCapsuleWeight7 = "00"

    try:
        flowerCapsulePrice7 = hex(int(flowerCapsulePrice7))
        if len(flowerCapsulePrice7) == 4:
            flowerCapsulePrice7 = flowerCapsulePrice7[2:]
        elif len(flowerCapsulePrice7) == 3:
            flowerCapsulePrice7 = "0" + flowerCapsulePrice7[2:]
    except:
        flowerCapsulePrice7 = "00"

    try:
        eggCapsuleWeight7 = hex(int(eggCapsuleWeight7))
        if len(eggCapsuleWeight7) == 4:
            eggCapsuleWeight7 = eggCapsuleWeight7[2:]
        elif len(eggCapsuleWeight7) == 3:
            eggCapsuleWeight7 = "0" + eggCapsuleWeight7[2:]
    except:
        eggCapsuleWeight7 = "00"

    try:
        eggCapsulePrice7 = hex(int(eggCapsulePrice7))
        if len(eggCapsulePrice7) == 4:
            eggCapsulePrice7 = eggCapsulePrice7[2:]
        elif len(eggCapsulePrice7) == 3:
            eggCapsulePrice7 = "0" + eggCapsulePrice7[2:]
    except:
        eggCapsulePrice7 = "00"

    try:
        vacuumCapsuleWeight7 = hex(int(vacuumCapsuleWeight7))
        if len(vacuumCapsuleWeight7) == 4:
            vacuumCapsuleWeight7 = vacuumCapsuleWeight7[2:]
        elif len(vacuumCapsuleWeight7) == 3:
            vacuumCapsuleWeight7 = "0" + vacuumCapsuleWeight7[2:]
    except:
        vacuumCapsuleWeight7 = "00"

    try:
        vacuumCapsulePrice7 = hex(int(vacuumCapsulePrice7))
        if len(vacuumCapsulePrice7) == 4:
            vacuumCapsulePrice7 = vacuumCapsulePrice7[2:]
        elif len(vacuumCapsulePrice7) == 3:
            vacuumCapsulePrice7 = "0" + vacuumCapsulePrice7[2:]
    except:
        vacuumCapsulePrice7 = "00"

    try:
        magicCapsuleWeight7 = hex(int(magicCapsuleWeight7))
        if len(magicCapsuleWeight7) == 4:
            magicCapsuleWeight7 = magicCapsuleWeight7[2:]
        elif len(magicCapsuleWeight7) == 3:
            magicCapsuleWeight7 = "0" + magicCapsuleWeight7[2:]
    except:
        magicCapsuleWeight7 = "00"

    try:
        magicCapsulePrice7 = hex(int(magicCapsulePrice7))
        if len(magicCapsulePrice7) == 4:
            magicCapsulePrice7 = magicCapsulePrice7[2:]
        elif len(magicCapsulePrice7) == 3:
            magicCapsulePrice7 = "0" + magicCapsulePrice7[2:]
    except:
        magicCapsulePrice7 = "00"
    
    try:
        tripleCapsuleWeight7 = hex(int(tripleCapsuleWeight7))
        if len(tripleCapsuleWeight7) == 4:
            tripleCapsuleWeight7 = tripleCapsuleWeight7[2:]
        elif len(tripleCapsuleWeight7) == 3:
            tripleCapsuleWeight7 = "0" + tripleCapsuleWeight7[2:]
    except:
        tripleCapsuleWeight7 = "00"

    try:
        tripleCapsulePrice7 = hex(int(tripleCapsulePrice7))
        if len(tripleCapsulePrice7) == 4:
            tripleCapsulePrice7 = tripleCapsulePrice7[2:]
        elif len(tripleCapsulePrice7) == 3:
            tripleCapsulePrice7 = "0" + tripleCapsulePrice7[2:]
    except:
        tripleCapsulePrice7 = "00"

    try:
        koopaCapsuleWeight7 = hex(int(koopaCapsuleWeight7))
        if len(koopaCapsuleWeight7) == 4:
            koopaCapsuleWeight7 = koopaCapsuleWeight7[2:]
        elif len(koopaCapsuleWeight7) == 3:
            koopaCapsuleWeight7 = "0" + koopaCapsuleWeight7[2:]
    except:
        koopaCapsuleWeight7 = "00"

    try:
        koopaCapsulePrice7 = hex(int(koopaCapsulePrice7))
        if len(koopaCapsulePrice7) == 4:
            koopaCapsulePrice7 = koopaCapsulePrice7[2:]
        elif len(koopaCapsulePrice7) == 3:
            koopaCapsulePrice7 = "0" + koopaCapsulePrice7[2:]
    except:
        koopaCapsulePrice7 = "00"

    try:
        dkCapsuleWeight7 = hex(int(dkCapsuleWeight7))
        if len(dkCapsuleWeight7) == 4:
            dkCapsuleWeight7 = dkCapsuleWeight7[2:]
        elif len(dkCapsuleWeight7) == 3:
            dkCapsuleWeight7 = "0" + dkCapsuleWeight7[2:]
    except:
        dkCapsuleWeight7 = "00"

    try:
        dkCapsulePrice7 = hex(int(dkCapsulePrice7))
        if len(dkCapsulePrice7) == 4:
            dkCapsulePrice7 = dkCapsulePrice7[2:]
        elif len(dkCapsulePrice7) == 3:
            dkCapsulePrice7 = "0" + dkCapsulePrice7[2:]
    except:
        dkCapsulePrice7 = "00"

    try:
        duelCapsuleWeight7 = hex(int(duelCapsuleWeight7))
        if len(duelCapsuleWeight7) == 4:
            duelCapsuleWeight7 = duelCapsuleWeight7[2:]
        elif len(duelCapsuleWeight7) == 3:
            duelCapsuleWeight7 = "0" + duelCapsuleWeight7[2:]
    except:
        duelCapsuleWeight7 = "00"
    try:
        duelCapsulePrice7 = hex(int(duelCapsulePrice7))
        if len(duelCapsulePrice7) == 4:
            duelCapsulePrice7 = duelCapsulePrice7[2:]
        elif len(duelCapsulePrice7) == 3:
            duelCapsulePrice7 = "0" + duelCapsulePrice7[2:]
    except:
        duelCapsulePrice7 = "00"

    try:
        orbBagCapsuleWeight7 = hex(int(orbBagCapsuleWeight7))
        if len(orbBagCapsuleWeight7) == 4:
            orbBagCapsuleWeight7 = orbBagCapsuleWeight7[2:]
        elif len(orbBagCapsuleWeight7) == 3:
            orbBagCapsuleWeight7 = "0" + orbBagCapsuleWeight7[2:]
    except:
        orbBagCapsuleWeight7 = "00"

    try:
        orbBagCapsulePrice7 = hex(int(orbBagCapsulePrice7))
        if len(orbBagCapsulePrice7) == 4:
            orbBagCapsulePrice7 = orbBagCapsulePrice7[2:]
        elif len(orbBagCapsulePrice7) == 3:
            orbBagCapsulePrice7 = "0" + orbBagCapsulePrice7[2:]
    except:
        orbBagCapsulePrice7 = "00"

    try:
        mysteryCapsuleWeight7 = hex(int(mysteryCapsuleWeight7))
        if len(mysteryCapsuleWeight7) == 4:
            mysteryCapsuleWeight7 = mysteryCapsuleWeight7[2:]
        elif len(mysteryCapsuleWeight7) == 3:
            mysteryCapsuleWeight7 = "0" + mysteryCapsuleWeight7[2:]
    except:
        mysteryCapsuleWeight7 = "00"
    try:
        mysteryCapsulePrice7 = hex(int(mysteryCapsulePrice7))
        if len(mysteryCapsulePrice7) == 4:
            mysteryCapsulePrice7 = mysteryCapsulePrice7[2:]
        elif len(mysteryCapsulePrice7) == 3:
            mysteryCapsulePrice7 = "0" + mysteryCapsulePrice7[2:]
    except:
        mysteryCapsulePrice7 = "00"

    try:
        posionMushroomWeight7 = hex(int(posionMushroomWeight7))
        if len(posionMushroomWeight7) == 4:
            posionMushroomWeight7 = posionMushroomWeight7[2:]
        elif len(posionMushroomWeight7) == 3:
            posionMushroomWeight7 = "0" + posionMushroomWeight7[2:]
    except:
        posionMushroomWeight7 = "00"
    try:
        posionMushroomPrice7 = hex(int(posionMushroomPrice7))
        if len(posionMushroomPrice7) == 4:
            posionMushroomPrice7 = posionMushroomPrice7[2:]
        elif len(posionMushroomPrice7) == 3:
            posionMushroomPrice7 = "0" + posionMushroomPrice7[2:]
    except:
        posionMushroomPrice7 = "00"

    generatedCode = getOrbModsSeven(mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, orbBagCapsulePrice7, orbBagCapsuleWeight7, dkCapsulePrice7, dkCapsuleWeight7, duelCapsulePrice7, duelCapsuleWeight7, mysteryCapsulePrice7, mysteryCapsuleWeight7, posionMushroomPrice7, posionMushroomWeight7)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def savePresetItems7(mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, posionMushroomWeight7, posionMushroomPrice7, dkCapsuleWeight7, dkCapsulePrice7, orbBagCapsuleWeight7, orbBagCapsulePrice7, duelCapsuleWeight7, duelCapsulePrice7, mysteryCapsuleWeight7, mysteryCapsulePrice7):
    if not mushroomCapsuleWeight7.get() or not goldenMushroomCapsulePrice7.get() or not goldenMushroomCapsuleWeight7.get() or not slowMushroomCapsulePrice7.get() or not slowMushroomCapsuleWeight7.get() or not metalMushroomCapsulePrice7.get() or not metalMushroomCapsuleWeight7.get() or not flutterCapsulePrice7.get() or not flutterCapsuleWeight7.get() or not cannonCapsulePrice7.get() or not cannonCapsuleWeight7.get() or not snackCapsulePrice7.get() or not snackCapsuleWeight7.get() or not lakituCapsulePrice7.get() or not lakituCapsuleWeight7.get() or not hammerBroCapsuleWeight7.get() or not hammerBroCapsulePrice7.get() or not plantCapsulePrice7.get() or not plantCapsuleWeight7.get() or not spearCapsuleWeight7.get() or not spearCapsulePrice7.get() or not kamekCapsuleWeight7.get() or not kamekCapsulePrice7.get() or not toadyCapsuleWeight7.get() or not toadyCapsulePrice7.get() or not blizzardCapsuleWeight7.get() or not blizzardCapsulePrice7.get() or not banditCapsulePrice7.get() or not banditCapsuleWeight7.get() or not pinkBooCapsuleWeight7.get() or not pinkBooCapsulePrice7.get() or not spinyCapsulePrice7.get() or not spinyCapsuleWeight7.get() or not zapCapsulePrice7.get() or not zapCapsuleWeight7.get() or not tweesterCapsulePrice7.get() or not tweesterCapsuleWeight7.get() or not thwompCapsulePrice7.get() or not thwompCapsuleWeight7.get() or not warpCapsulePrice7.get() or not warpCapsuleWeight7.get() or not bombCapsulePrice7.get() or not bombCapsuleWeight7.get() or not fireballCapsulePrice7.get() or not fireballCapsuleWeight7.get() or not eggCapsulePrice7.get() or not eggCapsuleWeight7.get() or not flowerCapsulePrice7.get() or not flowerCapsuleWeight7.get() or not vacuumCapsulePrice7.get() or not vacuumCapsuleWeight7.get() or not magicCapsulePrice7.get() or not magicCapsuleWeight7.get() or not tripleCapsulePrice7.get() or not tripleCapsuleWeight7.get() or not koopaCapsulePrice7.get() or not koopaCapsuleWeight7.get():
        if sys.platform == "darwin":
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        else:
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    
    mushroomCapsuleWeight7 = mushroomCapsuleWeight7.get()
    
    goldenMushroomCapsulePrice7 = goldenMushroomCapsulePrice7.get()
    goldenMushroomCapsuleWeight7 = goldenMushroomCapsuleWeight7.get()
    slowMushroomCapsulePrice7 = slowMushroomCapsulePrice7.get()
    slowMushroomCapsuleWeight7 = slowMushroomCapsuleWeight7.get()
    metalMushroomCapsulePrice7 = metalMushroomCapsulePrice7.get()
    metalMushroomCapsuleWeight7 = metalMushroomCapsuleWeight7.get()
    flutterCapsulePrice7 = flutterCapsulePrice7.get()
    flutterCapsuleWeight7 = flutterCapsuleWeight7.get()
    cannonCapsulePrice7 = cannonCapsulePrice7.get()
    cannonCapsuleWeight7 = cannonCapsuleWeight7.get()
    snackCapsulePrice7 = snackCapsulePrice7.get()
    snackCapsuleWeight7 = snackCapsuleWeight7.get()
    lakituCapsulePrice7 = lakituCapsulePrice7.get()
    lakituCapsuleWeight7 = lakituCapsuleWeight7.get()
    hammerBroCapsulePrice7 = hammerBroCapsulePrice7.get()
    hammerBroCapsuleWeight7 = hammerBroCapsuleWeight7.get()
    plantCapsulePrice7 = plantCapsulePrice7.get()
    plantCapsuleWeight7 = plantCapsuleWeight7.get()
    spearCapsulePrice7 = spearCapsulePrice7.get()
    spearCapsuleWeight7 = spearCapsuleWeight7.get()
    kamekCapsulePrice7 = kamekCapsulePrice7.get()
    kamekCapsuleWeight7 = kamekCapsuleWeight7.get()
    toadyCapsulePrice7 = toadyCapsulePrice7.get()
    toadyCapsuleWeight7 = toadyCapsuleWeight7.get()
    blizzardCapsulePrice7 = blizzardCapsulePrice7.get()
    blizzardCapsuleWeight7 = blizzardCapsuleWeight7.get()
    banditCapsulePrice7 = banditCapsulePrice7.get()
    banditCapsuleWeight7 = banditCapsuleWeight7.get()
    pinkBooCapsulePrice7 = pinkBooCapsulePrice7.get()
    pinkBooCapsuleWeight7 = pinkBooCapsuleWeight7.get()
    spinyCapsulePrice7 = spinyCapsulePrice7.get()
    spinyCapsuleWeight7 = spinyCapsuleWeight7.get()
    zapCapsulePrice7 = zapCapsulePrice7.get()
    zapCapsuleWeight7 = zapCapsuleWeight7.get()
    tweesterCapsulePrice7 = tweesterCapsulePrice7.get()
    tweesterCapsuleWeight7 = tweesterCapsuleWeight7.get()
    thwompCapsulePrice7 = thwompCapsulePrice7.get()
    thwompCapsuleWeight7 = thwompCapsuleWeight7.get()
    warpCapsulePrice7 = warpCapsulePrice7.get()
    warpCapsuleWeight7 = warpCapsuleWeight7.get()
    bombCapsulePrice7 = bombCapsulePrice7.get()
    bombCapsuleWeight7 = bombCapsuleWeight7.get()
    fireballCapsulePrice7 = fireballCapsulePrice7.get()
    fireballCapsuleWeight7 = fireballCapsuleWeight7.get()
    flowerCapsulePrice7 = flowerCapsulePrice7.get()
    flowerCapsuleWeight7 = flowerCapsuleWeight7.get()
    eggCapsulePrice7 = eggCapsulePrice7.get()
    eggCapsuleWeight7 = eggCapsuleWeight7.get()
    vacuumCapsulePrice7 = vacuumCapsulePrice7.get()
    vacuumCapsuleWeight7 = vacuumCapsuleWeight7.get()
    magicCapsulePrice7 = magicCapsulePrice7.get()
    magicCapsuleWeight7 = magicCapsuleWeight7.get()
    tripleCapsulePrice7 = tripleCapsulePrice7.get()
    tripleCapsuleWeight7 = tripleCapsuleWeight7.get()
    koopaCapsulePrice7 = koopaCapsulePrice7.get()
    koopaCapsuleWeight7 = koopaCapsuleWeight7.get()
    
    try:
        dkCapsulePrice7 = dkCapsulePrice7.get()
    except:
        dkCapsulePrice7 = 0

    try:
        dkCapsuleWeight7 = dkCapsuleWeight7.get()
    except:
        dkCapsuleWeight7 = 0

    try:
        posionMushroomPrice7 = posionMushroomPrice7.get()
    except:
        posionMushroomPrice7 = 0

    try:
        posionMushroomWeight7 = posionMushroomWeight7.get()
    except:
        posionMushroomWeight7 = 0

    try:
        duelCapsulePrice7 = duelCapsulePrice7.get()
    except:
        duelCapsulePrice7 = 0

    try:
        duelCapsuleWeight7 = duelCapsuleWeight7.get()
    except:
        duelCapsuleWeight7 = 0

    try:
        mysteryCapsulePrice7 = mysteryCapsulePrice7.get()
    except:
        mysteryCapsulePrice7 = 0

    try:
        mysteryCapsuleWeight7 = mysteryCapsuleWeight7.get()
    except:
        mysteryCapsuleWeight7 = 0
    
    try:
        orbBagCapsulePrice7 = orbBagCapsulePrice7.get()
    except:
        orbBagCapsulePrice7 = 0

    try:
        orbBagCapsuleWeight7 = orbBagCapsuleWeight7.get()
    except:
        orbBagCapsuleWeight7 = 0

    prices7 = ["5", goldenMushroomCapsulePrice7, slowMushroomCapsulePrice7, metalMushroomCapsulePrice7, flutterCapsulePrice7, cannonCapsulePrice7, snackCapsulePrice7, lakituCapsulePrice7, hammerBroCapsulePrice7, plantCapsulePrice7, spearCapsulePrice7, kamekCapsulePrice7, toadyCapsulePrice7, blizzardCapsulePrice7, banditCapsulePrice7, pinkBooCapsulePrice7, spinyCapsulePrice7, zapCapsulePrice7, tweesterCapsulePrice7, thwompCapsulePrice7, warpCapsulePrice7, bombCapsulePrice7, fireballCapsulePrice7, flowerCapsulePrice7, eggCapsulePrice7, vacuumCapsulePrice7, magicCapsulePrice7, tripleCapsulePrice7, koopaCapsulePrice7, dkCapsulePrice7, posionMushroomPrice7, duelCapsulePrice7, mysteryCapsulePrice7, orbBagCapsulePrice7]
    weights7 = [mushroomCapsuleWeight7, goldenMushroomCapsuleWeight7, slowMushroomCapsuleWeight7, metalMushroomCapsuleWeight7, flutterCapsuleWeight7, cannonCapsuleWeight7, snackCapsuleWeight7, lakituCapsuleWeight7, hammerBroCapsuleWeight7, plantCapsuleWeight7, spearCapsuleWeight7, kamekCapsuleWeight7, toadyCapsuleWeight7, blizzardCapsuleWeight7, banditCapsuleWeight7, pinkBooCapsuleWeight7, spinyCapsuleWeight7, zapCapsuleWeight7, tweesterCapsuleWeight7, thwompCapsuleWeight7, warpCapsuleWeight7, bombCapsuleWeight7, fireballCapsuleWeight7, flowerCapsuleWeight7, eggCapsuleWeight7, vacuumCapsuleWeight7, magicCapsuleWeight7, tripleCapsuleWeight7, koopaCapsuleWeight7, dkCapsuleWeight7, posionMushroomWeight7, duelCapsuleWeight7, mysteryCapsuleWeight7, orbBagCapsuleWeight7]
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prices', 'Weights'])
            for price, weight in zip(prices7, weights7):
                writer.writerow([price, weight])
        print("MPT file saved successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def loadPresetItems7(hide_custom, mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, posionMushroomPrice7, posionMushroomWeight7, dkCapsulePrice7, dkCapsuleWeight7, orbBagCapsulePrice7, orbBagCapsuleWeight7, duelCapsulePrice7, duelCapsuleWeight7, mysteryCapsulePrice7, mysteryCapsuleWeight7):
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        prices7In = []
        weights7In = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                prices7In.append(float(row[0]))
                weights7In.append(float(row[1]))
        
        testVar = ""
        # Define a list of Entry widget attributes
        
        pricesNames7 = [testVar, goldenMushroomCapsulePrice7, slowMushroomCapsulePrice7, metalMushroomCapsulePrice7, flutterCapsulePrice7, cannonCapsulePrice7, snackCapsulePrice7, lakituCapsulePrice7, hammerBroCapsulePrice7, plantCapsulePrice7, spearCapsulePrice7, kamekCapsulePrice7, toadyCapsulePrice7, blizzardCapsulePrice7, banditCapsulePrice7, pinkBooCapsulePrice7, spinyCapsulePrice7, zapCapsulePrice7, tweesterCapsulePrice7, thwompCapsulePrice7, warpCapsulePrice7, bombCapsulePrice7, fireballCapsulePrice7, flowerCapsulePrice7, eggCapsulePrice7, vacuumCapsulePrice7, magicCapsulePrice7, tripleCapsulePrice7, koopaCapsulePrice7]
        weightsNames7 = [mushroomCapsuleWeight7, goldenMushroomCapsuleWeight7, slowMushroomCapsuleWeight7, metalMushroomCapsuleWeight7, flutterCapsuleWeight7, cannonCapsuleWeight7, snackCapsuleWeight7, lakituCapsuleWeight7, hammerBroCapsuleWeight7, plantCapsuleWeight7, spearCapsuleWeight7, kamekCapsuleWeight7, toadyCapsuleWeight7, blizzardCapsuleWeight7, banditCapsuleWeight7, pinkBooCapsuleWeight7, spinyCapsuleWeight7, zapCapsuleWeight7, tweesterCapsuleWeight7, thwompCapsuleWeight7, warpCapsuleWeight7, bombCapsuleWeight7, fireballCapsuleWeight7, flowerCapsuleWeight7, eggCapsuleWeight7, vacuumCapsuleWeight7, magicCapsuleWeight7, tripleCapsuleWeight7, koopaCapsuleWeight7]
        
        if not hide_custom:
            pricesNames7.extend([dkCapsulePrice7, posionMushroomPrice7, duelCapsulePrice7, mysteryCapsulePrice7, orbBagCapsulePrice7])
            weightsNames7.extend([dkCapsuleWeight7, posionMushroomWeight7, duelCapsuleWeight7, mysteryCapsuleWeight7, orbBagCapsuleWeight7])
        
        # Update widgets with loaded values
        for index, widget in enumerate(pricesNames7):
            if widget and index < len(prices7In):
                widget.delete(0, 'end')
                widget.insert(0, int(prices7In[index]))
        for index, widget in enumerate(weightsNames7):
            if widget and index < len(weights7In):
                widget.delete(0, 'end')
                widget.insert(0, int(weights7In[index]))
        print("MPT file laoded successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def fillViaCode7(hide_custom, top, codeText, mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, posionMushroomPrice7, posionMushroomWeight7, dkCapsulePrice7, dkCapsuleWeight7, orbBagCapsulePrice7, orbBagCapsuleWeight7, duelCapsulePrice7, duelCapsuleWeight7, mysteryCapsulePrice7, mysteryCapsuleWeight7):
    code7 = []
    code_single7 = []
    weight_code7 = []
    price_code7 = []
    weights7 = []
    weights7In = []
    prices7 = []
    prices7In = []
    names = ['Mushroom Orb', "Super Mushroom Orb", "Slow 'Shroom Orb", "Metal Mushroom Orb", "Flutter Orb", "Cannon Orb", "Snack Orb", "Lakitu Orb", "Hammer Bro Orb", "Piranha Plant Orb", "Spear Guy Orb", "Kamek Orb", "Toady Orb", "Mr. Blizzard Orb", "Bandit Orb", "Pink Boo Orb", "Spiny Orb", "Zap Orb", "Tweester Orb", "Thwomp Orb", "Warp Pipe Orb", "Bob-omb Orb", "Fireball Orb", "Flower Orb", "Egg Orb", "Vacuum Orb", "Surprise Orb", "Triple 'Shroom Orb", "Koopa Kid Orb"]
    current_line7 = ""

    code7.append(codeText.get("1.0", "end"))
    
    try:
        for i in range(0, 17):
            current_line7 = current_line7 + code7[0][i]

        if current_line7 == "MP7 - Orb Modifer":
            current_line7 = ""
            
            for i in range(18, 2538):
                if code7[0][i] != " " and code7[0][i] != "\n":
                    current_line7 = current_line7 + code7[0][i]
                else:
                    code_single7.append(current_line7)
                    current_line7 = ""
        else:
            current_line7 = ""
            
            for i in range(0, 2520):
                if code7[0][i] != " " and code7[0][i] != "\n":
                    current_line7 = current_line7 + code7[0][i]
                else:
                    code_single7.append(current_line7)
                    current_line7 = ""
    except IndexError:
        createDialog("Error", "error", "Invalid Code", None)
        return
    
    del code_single7[0:3]
    del code_single7[269::]

    for i in range(1, 135):
        del code_single7[i] 

    x = 1
    
    for i in range(34):
        for n in range(2):
            del code_single7[x]
        x += 2
    
    code_single7.insert(0, "00000005")
    
    x = 1

    for i in range(34):
        weight_code7.append(code_single7[x])
        x += 2
    
    x = 0

    for i in range(34):
        price_code7.append(code_single7[x])
        x += 2

    for line in weight_code7:
        weights7.append(line[6:8])
    
    for line in price_code7:
        prices7.append(line[6:8])
    
    for weight in weights7:
        weights7In.append(int(weight, 16))
    
    for price in prices7:
        prices7In.append(int(price, 16))

    print(prices7In)
    print(weights7In)
    
    prices7In.insert(31, prices7In.pop(32))
    weights7In.insert(31, prices7In.pop(32))
    
    testVar = ""
    
    # Define a list of Entry widget attributes
    pricesNames7 = [testVar, goldenMushroomCapsulePrice7, slowMushroomCapsulePrice7, metalMushroomCapsulePrice7, flutterCapsulePrice7, cannonCapsulePrice7, snackCapsulePrice7, lakituCapsulePrice7, hammerBroCapsulePrice7, plantCapsulePrice7, spearCapsulePrice7, kamekCapsulePrice7, toadyCapsulePrice7, blizzardCapsulePrice7, banditCapsulePrice7, pinkBooCapsulePrice7, spinyCapsulePrice7, zapCapsulePrice7, tweesterCapsulePrice7, thwompCapsulePrice7, warpCapsulePrice7, bombCapsulePrice7, fireballCapsulePrice7, flowerCapsulePrice7, eggCapsulePrice7, vacuumCapsulePrice7, magicCapsulePrice7, tripleCapsulePrice7, koopaCapsulePrice7]
    weightsNames7 = [mushroomCapsuleWeight7, goldenMushroomCapsuleWeight7, slowMushroomCapsuleWeight7, metalMushroomCapsuleWeight7, flutterCapsuleWeight7, cannonCapsuleWeight7, snackCapsuleWeight7, lakituCapsuleWeight7, hammerBroCapsuleWeight7, plantCapsuleWeight7, spearCapsuleWeight7, kamekCapsuleWeight7, toadyCapsuleWeight7, blizzardCapsuleWeight7, banditCapsuleWeight7, pinkBooCapsuleWeight7, spinyCapsuleWeight7, zapCapsuleWeight7, tweesterCapsuleWeight7, thwompCapsuleWeight7, warpCapsuleWeight7, bombCapsuleWeight7, fireballCapsuleWeight7, flowerCapsuleWeight7, eggCapsuleWeight7, vacuumCapsuleWeight7, magicCapsuleWeight7, tripleCapsuleWeight7, koopaCapsuleWeight7]
    
    if not hide_custom:
        pricesNames7.extend([dkCapsulePrice7, posionMushroomPrice7, duelCapsulePrice7, mysteryCapsulePrice7, orbBagCapsulePrice7])
        weightsNames7.extend([dkCapsuleWeight7, posionMushroomWeight7, duelCapsuleWeight7, mysteryCapsuleWeight7, orbBagCapsuleWeight7])

    # Update widgets with loaded values
    for index, widget in enumerate(pricesNames7):
        if widget and index < len(prices7In):
            widget.delete(0, 'end')
            widget.insert(0, int(prices7In[index]))
    for index, widget in enumerate(weightsNames7):
        if widget and index < len(weights7In):
            widget.delete(0, 'end')
            widget.insert(0, int(weights7In[index]))
    print("Code loaded successfully!")
    
    top.destroy()

    createDialog("Operation Sucessful", "success", "Code loaded successfully!.", None)