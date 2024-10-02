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

def itemsEvent_mp7(mushroomCapsuleShopOdds12 = "0", mushroomCapsuleShopOdds34 = "0", mushroomCapsuleSpaceOdds12 = "0", mushroomCapsuleSpaceOdds34 = "0", goldenMushroomCapsulePrice12 = "0", goldenMushroomCapsulePrice34 = "0", goldenMushroomCapsuleShopOdds12 = "0", goldenMushroomCapsuleShopOdds34 = "0", goldenMushroomCapsuleSpaceOdds12 = "0", goldenMushroomCapsuleSpaceOdds34 = "0", slowMushroomCapsulePrice12 = "0", slowMushroomCapsulePrice34 = "0", slowMushroomCapsuleShopOdds12 = "0", slowMushroomCapsuleShopOdds34 = "0", slowMushroomCapsuleSpaceOdds12 = "0", slowMushroomCapsuleSpaceOdds34 = "0", metalMushroomCapsulePrice12 = "0", metalMushroomCapsulePrice34 = "0", metalMushroomCapsuleShopOdds12 = "0", metalMushroomCapsuleShopOdds34 = "0", metalMushroomCapsuleSpaceOdds12 = "0", metalMushroomCapsuleSpaceOdds34 = "0", flutterCapsulePrice12 = "0", flutterCapsulePrice34 = "0", flutterCapsuleShopOdds12 = "0", flutterCapsuleShopOdds34 = "0", flutterCapsuleSpaceOdds12 = "0", flutterCapsuleSpaceOdds34 = "0", cannonCapsulePrice12 = "0", cannonCapsulePrice34 = "0", cannonCapsuleShopOdds12 = "0", cannonCapsuleShopOdds34 = "0", cannonCapsuleSpaceOdds12 = "0", cannonCapsuleSpaceOdds34 = "0", snackCapsulePrice12 = "0", snackCapsulePrice34 = "0", snackCapsuleShopOdds12 = "0", snackCapsuleShopOdds34 = "0", snackCapsuleSpaceOdds12 = "0", snackCapsuleSpaceOdds34 = "0", lakituCapsulePrice12 = "0", lakituCapsulePrice34 = "0", lakituCapsuleShopOdds12 = "0", lakituCapsuleShopOdds34 = "0", lakituCapsuleSpaceOdds12 = "0", lakituCapsuleSpaceOdds34 = "0", hammerBroCapsulePrice12 = "0", hammerBroCapsulePrice34 = "0", hammerBroCapsuleShopOdds12 = "0", hammerBroCapsuleShopOdds34 = "0", hammerBroCapsuleSpaceOdds12 = "0", hammerBroCapsuleSpaceOdds34 = "0", piranhaPlantCapsulePrice12 = "0", piranhaPlantCapsulePrice34 = "0", piranhaPlantCapsuleShopOdds12 = "0", piranhaPlantCapsuleShopOdds34 = "0", piranhaPlantCapsuleSpaceOdds12 = "0", piranhaPlantCapsuleSpaceOdds34 = "0", spearGuyCapsulePrice12 = "0", spearGuyCapsulePrice34 = "0", spearGuyCapsuleShopOdds12 = "0", spearGuyCapsuleShopOdds34 = "0", spearGuyCapsuleSpaceOdds12 = "0", spearGuyCapsuleSpaceOdds34 = "0", kamekCapsulePrice12 = "0", kamekCapsulePrice34 = "0", kamekCapsuleShopOdds12 = "0", kamekCapsuleShopOdds34 = "0", kamekCapsuleSpaceOdds12 = "0", kamekCapsuleSpaceOdds34 = "0", toadyCapsulePrice12 = "0", toadyCapsulePrice34 = "0", toadyCapsuleShopOdds12 = "0", toadyCapsuleShopOdds34 = "0", toadyCapsuleSpaceOdds12 = "0", toadyCapsuleSpaceOdds34 = "0", mrBlizzardCapsulePrice12 = "0", mrBlizzardCapsulePrice34 = "0", mrBlizzardCapsuleShopOdds12 = "0", mrBlizzardCapsuleShopOdds34 = "0", mrBlizzardCapsuleSpaceOdds12 = "0", mrBlizzardCapsuleSpaceOdds34 = "0", banditCapsulePrice12 = "0", banditCapsulePrice34 = "0", banditCapsuleShopOdds12 = "0", banditCapsuleShopOdds34 = "0", banditCapsuleSpaceOdds12 = "0", banditCapsuleSpaceOdds34 = "0", pinkBooCapsulePrice12 = "0", pinkBooCapsulePrice34 = "0", pinkBooCapsuleShopOdds12 = "0", pinkBooCapsuleShopOdds34 = "0", pinkBooCapsuleSpaceOdds12 = "0", pinkBooCapsuleSpaceOdds34 = "0", spinyCapsulePrice12 = "0", spinyCapsulePrice34 = "0", spinyCapsuleShopOdds12 = "0", spinyCapsuleShopOdds34 = "0", spinyCapsuleSpaceOdds12 = "0", spinyCapsuleSpaceOdds34 = "0", zapCapsulePrice12 = "0", zapCapsulePrice34 = "0", zapCapsuleShopOdds12 = "0", zapCapsuleShopOdds34 = "0", zapCapsuleSpaceOdds12 = "0", zapCapsuleSpaceOdds34 = "0", tweesterCapsulePrice12 = "0", tweesterCapsulePrice34 = "0", tweesterCapsuleShopOdds12 = "0", tweesterCapsuleShopOdds34 = "0", tweesterCapsuleSpaceOdds12 = "0", tweesterCapsuleSpaceOdds34 = "0", thwompCapsulePrice12 = "0", thwompCapsulePrice34 = "0", thwompCapsuleShopOdds12 = "0", thwompCapsuleShopOdds34 = "0", thwompCapsuleSpaceOdds12 = "0", thwompCapsuleSpaceOdds34 = "0", warpCapsulePrice12 = "0", warpCapsulePrice34 = "0", warpCapsuleShopOdds12 = "0", warpCapsuleShopOdds34 = "0", warpCapsuleSpaceOdds12 = "0", warpCapsuleSpaceOdds34 = "0", bombCapsulePrice12 = "0", bombCapsulePrice34 = "0", bombCapsuleShopOdds12 = "0", bombCapsuleShopOdds34 = "0", bombCapsuleSpaceOdds12 = "0", bombCapsuleSpaceOdds34 = "0", fireballCapsulePrice12 = "0", fireballCapsulePrice34 = "0", fireballCapsuleShopOdds12 = "0", fireballCapsuleShopOdds34 = "0", fireballCapsuleSpaceOdds12 = "0", fireballCapsuleSpaceOdds34 = "0", flowerCapsulePrice12 = "0", flowerCapsulePrice34 = "0", flowerCapsuleShopOdds12 = "0", flowerCapsuleShopOdds34 = "0", flowerCapsuleSpaceOdds12 = "0", flowerCapsuleSpaceOdds34 = "0", eggCapsulePrice12 = "0", eggCapsulePrice34 = "0", eggCapsuleShopOdds12 = "0", eggCapsuleShopOdds34 = "0", eggCapsuleSpaceOdds12 = "0", eggCapsuleSpaceOdds34 = "0", vacuumCapsulePrice12 = "0", vacuumCapsulePrice34 = "0", vacuumCapsuleShopOdds12 = "0", vacuumCapsuleShopOdds34 = "0", vacuumCapsuleSpaceOdds12 = "0", vacuumCapsuleSpaceOdds34 = "0", magicCapsulePrice12 = "0", magicCapsulePrice34 = "0", magicCapsuleShopOdds12 = "0", magicCapsuleShopOdds34 = "0", magicCapsuleSpaceOdds12 = "0", magicCapsuleSpaceOdds34 = "0", tripleCapsulePrice12 = "0", tripleCapsulePrice34 = "0", tripleCapsuleShopOdds12 = "0", tripleCapsuleShopOdds34 = "0", tripleCapsuleSpaceOdds12 = "0", tripleCapsuleSpaceOdds34 = "0", koopaCapsulePrice12 = "0", koopaCapsulePrice34 = "0", koopaCapsuleShopOdds12 = "0", koopaCapsuleShopOdds34 = "0", koopaCapsuleSpaceOdds12 = "0", koopaCapsuleSpaceOdds34 = "0", poisonMushroomPrice34 = "0", poisonMushroomPrice12 = "0", poisonMushroomShopOdds12 = "0", poisonMushroomShopOdds34 = "0", poisonMushroomSpaceOdds12 = "0", poisonMushroomSpaceOdds34 = "0", orbBagCapsulePrice34 = "0", orbBagCapsulePrice12 = "0", orbBagCapsuleShopOdds12 = "0", orbBagCapsuleShopOdds34 = "0", orbBagCapsuleSpaceOdds12 = "0", orbBagCapsuleSpaceOdds34 = "0", mysteryCapsulePrice34 = "0", mysteryCapsulePrice12 = "0", mysteryCapsuleShopOdds12 = "0", mysteryCapsuleShopOdds34 = "0", mysteryCapsuleSpaceOdds12 = "0", mysteryCapsuleSpaceOdds34 = "0", dkCapsulePrice34 = "0", dkCapsulePrice12 = "0", dkCapsuleShopOdds12 = "0", dkCapsuleShopOdds34 = "0", dkCapsuleSpaceOdds12 = "0", dkCapsuleSpaceOdds34 = "0", duelCapsulePrice34 = "0", duelCapsulePrice12 = "0", duelCapsuleShopOdds12 = "0", duelCapsuleShopOdds34 = "0", duelCapsuleSpaceOdds12 = "0", duelCapsuleSpaceOdds34 = "0"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    mushroomCapsulePrice12 = "5"
    mushroomCapsulePrice34 = "5"
    mushroomCapsuleShopOdds12 = get_capsule_value(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = get_capsule_value(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds12 = get_capsule_value(mushroomCapsuleSpaceOdds12)
    mushroomCapsuleSpaceOdds34 = get_capsule_value(mushroomCapsuleSpaceOdds34)
    goldenMushroomCapsulePrice12 = get_capsule_value(goldenMushroomCapsulePrice12)
    goldenMushroomCapsulePrice34 = get_capsule_value(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = get_capsule_value(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = get_capsule_value(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds12 = get_capsule_value(goldenMushroomCapsuleSpaceOdds12)
    goldenMushroomCapsuleSpaceOdds34 = get_capsule_value(goldenMushroomCapsuleSpaceOdds34)
    slowMushroomCapsulePrice12 = get_capsule_value(slowMushroomCapsulePrice12)
    slowMushroomCapsulePrice34 = get_capsule_value(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = get_capsule_value(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = get_capsule_value(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds12 = get_capsule_value(slowMushroomCapsuleSpaceOdds12)
    slowMushroomCapsuleSpaceOdds34 = get_capsule_value(slowMushroomCapsuleSpaceOdds34)
    metalMushroomCapsulePrice12 = get_capsule_value(metalMushroomCapsulePrice12)
    metalMushroomCapsulePrice34 = get_capsule_value(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = get_capsule_value(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = get_capsule_value(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds12 = get_capsule_value(metalMushroomCapsuleSpaceOdds12)
    metalMushroomCapsuleSpaceOdds34 = get_capsule_value(metalMushroomCapsuleSpaceOdds34)
    flutterCapsulePrice12 = get_capsule_value(flutterCapsulePrice12)
    flutterCapsulePrice34 = get_capsule_value(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = get_capsule_value(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = get_capsule_value(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds12 = get_capsule_value(flutterCapsuleSpaceOdds12)
    flutterCapsuleSpaceOdds34 = get_capsule_value(flutterCapsuleSpaceOdds34)
    cannonCapsulePrice12 = get_capsule_value(cannonCapsulePrice12)
    cannonCapsulePrice34 = get_capsule_value(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = get_capsule_value(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = get_capsule_value(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds12 = get_capsule_value(cannonCapsuleSpaceOdds12)
    cannonCapsuleSpaceOdds34 = get_capsule_value(cannonCapsuleSpaceOdds34)
    snackCapsulePrice12 = get_capsule_value(snackCapsulePrice12)
    snackCapsulePrice34 = get_capsule_value(snackCapsulePrice34)
    snackCapsuleShopOdds12 = get_capsule_value(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = get_capsule_value(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds12 = get_capsule_value(snackCapsuleSpaceOdds12)
    snackCapsuleSpaceOdds34 = get_capsule_value(snackCapsuleSpaceOdds34)
    lakituCapsulePrice12 = get_capsule_value(lakituCapsulePrice12)
    lakituCapsulePrice34 = get_capsule_value(lakituCapsulePrice34)
    lakituCapsuleShopOdds12 = get_capsule_value(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = get_capsule_value(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds12 = get_capsule_value(lakituCapsuleSpaceOdds12)
    lakituCapsuleSpaceOdds34 = get_capsule_value(lakituCapsuleSpaceOdds34)
    hammerBroCapsulePrice12 = get_capsule_value(hammerBroCapsulePrice12)
    hammerBroCapsulePrice34 = get_capsule_value(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = get_capsule_value(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = get_capsule_value(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds12 = get_capsule_value(hammerBroCapsuleSpaceOdds12)
    hammerBroCapsuleSpaceOdds34 = get_capsule_value(hammerBroCapsuleSpaceOdds34)
    piranhaPlantCapsulePrice12 = get_capsule_value(piranhaPlantCapsulePrice12)
    piranhaPlantCapsulePrice34 = get_capsule_value(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = get_capsule_value(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = get_capsule_value(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds12 = get_capsule_value(piranhaPlantCapsuleSpaceOdds12)
    piranhaPlantCapsuleSpaceOdds34 = get_capsule_value(piranhaPlantCapsuleSpaceOdds34)
    spearGuyCapsulePrice12 = get_capsule_value(spearGuyCapsulePrice12)
    spearGuyCapsulePrice34 = get_capsule_value(spearGuyCapsulePrice34)
    spearGuyCapsuleShopOdds12 = get_capsule_value(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = get_capsule_value(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds12 = get_capsule_value(spearGuyCapsuleSpaceOdds12)
    spearGuyCapsuleSpaceOdds34 = get_capsule_value(spearGuyCapsuleSpaceOdds34)
    kamekCapsulePrice12 = get_capsule_value(kamekCapsulePrice12)
    kamekCapsulePrice34 = get_capsule_value(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = get_capsule_value(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = get_capsule_value(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds12 = get_capsule_value(kamekCapsuleSpaceOdds12)
    kamekCapsuleSpaceOdds34 = get_capsule_value(kamekCapsuleSpaceOdds34)
    toadyCapsulePrice12 = get_capsule_value(toadyCapsulePrice12)
    toadyCapsulePrice34 = get_capsule_value(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = get_capsule_value(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = get_capsule_value(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds12 = get_capsule_value(toadyCapsuleSpaceOdds12)
    toadyCapsuleSpaceOdds34 = get_capsule_value(toadyCapsuleSpaceOdds34)
    mrBlizzardCapsulePrice12 = get_capsule_value(mrBlizzardCapsulePrice12)
    mrBlizzardCapsulePrice34 = get_capsule_value(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = get_capsule_value(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = get_capsule_value(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds12 = get_capsule_value(mrBlizzardCapsuleSpaceOdds12)
    mrBlizzardCapsuleSpaceOdds34 = get_capsule_value(mrBlizzardCapsuleSpaceOdds34)
    banditCapsulePrice12 = get_capsule_value(banditCapsulePrice12)
    banditCapsulePrice34 = get_capsule_value(banditCapsulePrice34)
    banditCapsuleShopOdds12 = get_capsule_value(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = get_capsule_value(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds12 = get_capsule_value(banditCapsuleSpaceOdds12)
    banditCapsuleSpaceOdds34 = get_capsule_value(banditCapsuleSpaceOdds34)
    pinkBooCapsulePrice12 = get_capsule_value(pinkBooCapsulePrice12)
    pinkBooCapsulePrice34 = get_capsule_value(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = get_capsule_value(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = get_capsule_value(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds12 = get_capsule_value(pinkBooCapsuleSpaceOdds12)
    pinkBooCapsuleSpaceOdds34 = get_capsule_value(pinkBooCapsuleSpaceOdds34)
    spinyCapsulePrice12 = get_capsule_value(spinyCapsulePrice12)
    spinyCapsulePrice34 = get_capsule_value(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = get_capsule_value(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = get_capsule_value(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds12 = get_capsule_value(spinyCapsuleSpaceOdds12)
    spinyCapsuleSpaceOdds34 = get_capsule_value(spinyCapsuleSpaceOdds34)
    zapCapsulePrice12 = get_capsule_value(zapCapsulePrice12)
    zapCapsulePrice34 = get_capsule_value(zapCapsulePrice34)
    zapCapsuleShopOdds12 = get_capsule_value(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = get_capsule_value(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds12 = get_capsule_value(zapCapsuleSpaceOdds12)
    zapCapsuleSpaceOdds34 = get_capsule_value(zapCapsuleSpaceOdds34)
    tweesterCapsulePrice12 = get_capsule_value(tweesterCapsulePrice12)
    tweesterCapsulePrice34 = get_capsule_value(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = get_capsule_value(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = get_capsule_value(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds12 = get_capsule_value(tweesterCapsuleSpaceOdds12)
    tweesterCapsuleSpaceOdds34 = get_capsule_value(tweesterCapsuleSpaceOdds34)
    thwompCapsulePrice12 = get_capsule_value(thwompCapsulePrice12)
    thwompCapsulePrice34 = get_capsule_value(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = get_capsule_value(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = get_capsule_value(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds12 = get_capsule_value(thwompCapsuleSpaceOdds12)
    thwompCapsuleSpaceOdds34 = get_capsule_value(thwompCapsuleSpaceOdds34)
    warpCapsulePrice12 = get_capsule_value(warpCapsulePrice12)
    warpCapsulePrice34 = get_capsule_value(warpCapsulePrice34)
    warpCapsuleShopOdds12 = get_capsule_value(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = get_capsule_value(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds12 = get_capsule_value(warpCapsuleSpaceOdds12)
    warpCapsuleSpaceOdds34 = get_capsule_value(warpCapsuleSpaceOdds34)
    bombCapsulePrice12 = get_capsule_value(bombCapsulePrice12)
    bombCapsulePrice34 = get_capsule_value(bombCapsulePrice34)
    bombCapsuleShopOdds12 = get_capsule_value(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = get_capsule_value(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds12 = get_capsule_value(bombCapsuleSpaceOdds12)
    bombCapsuleSpaceOdds34 = get_capsule_value(bombCapsuleSpaceOdds34)
    fireballCapsulePrice12 = get_capsule_value(fireballCapsulePrice12)
    fireballCapsulePrice34 = get_capsule_value(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = get_capsule_value(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = get_capsule_value(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds12 = get_capsule_value(fireballCapsuleSpaceOdds12)
    fireballCapsuleSpaceOdds34 = get_capsule_value(fireballCapsuleSpaceOdds34)
    flowerCapsulePrice12 = get_capsule_value(flowerCapsulePrice12)
    flowerCapsulePrice34 = get_capsule_value(flowerCapsulePrice34)
    flowerCapsuleShopOdds12 = get_capsule_value(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = get_capsule_value(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds12 = get_capsule_value(flowerCapsuleSpaceOdds12)
    flowerCapsuleSpaceOdds34 = get_capsule_value(flowerCapsuleSpaceOdds34)
    eggCapsulePrice12 = get_capsule_value(eggCapsulePrice12)
    eggCapsulePrice34 = get_capsule_value(eggCapsulePrice34)
    eggCapsuleShopOdds12 = get_capsule_value(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = get_capsule_value(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds12 = get_capsule_value(eggCapsuleSpaceOdds12)
    eggCapsuleSpaceOdds34 = get_capsule_value(eggCapsuleSpaceOdds34)
    vacuumCapsulePrice12 = get_capsule_value(vacuumCapsulePrice12)
    vacuumCapsulePrice34 = get_capsule_value(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = get_capsule_value(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = get_capsule_value(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds12 = get_capsule_value(vacuumCapsuleSpaceOdds12)
    vacuumCapsuleSpaceOdds34 = get_capsule_value(vacuumCapsuleSpaceOdds34)
    magicCapsulePrice12 = get_capsule_value(magicCapsulePrice12)
    magicCapsulePrice34 = get_capsule_value(magicCapsulePrice34)
    magicCapsuleShopOdds12 = get_capsule_value(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = get_capsule_value(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds12 = get_capsule_value(magicCapsuleSpaceOdds12)
    magicCapsuleSpaceOdds34 = get_capsule_value(magicCapsuleSpaceOdds34)
    tripleCapsulePrice12 = get_capsule_value(tripleCapsulePrice12)
    tripleCapsulePrice34 = get_capsule_value(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = get_capsule_value(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = get_capsule_value(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds12 = get_capsule_value(tripleCapsuleSpaceOdds12)
    tripleCapsuleSpaceOdds34 = get_capsule_value(tripleCapsuleSpaceOdds34)
    koopaCapsulePrice12 = get_capsule_value(koopaCapsulePrice12)
    koopaCapsulePrice34 = get_capsule_value(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = get_capsule_value(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = get_capsule_value(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds12 = get_capsule_value(koopaCapsuleSpaceOdds12)
    koopaCapsuleSpaceOdds34 = get_capsule_value(koopaCapsuleSpaceOdds34)
    poisonMushroomPrice12 = get_capsule_value(poisonMushroomPrice12)
    poisonMushroomPrice34 = get_capsule_value(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = get_capsule_value(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = get_capsule_value(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds12 = get_capsule_value(poisonMushroomSpaceOdds12)
    poisonMushroomSpaceOdds34 = get_capsule_value(poisonMushroomSpaceOdds34)
    orbBagCapsulePrice12 = get_capsule_value(orbBagCapsulePrice12)
    orbBagCapsulePrice34 = get_capsule_value(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = get_capsule_value(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = get_capsule_value(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds12 = get_capsule_value(orbBagCapsuleSpaceOdds12)
    orbBagCapsuleSpaceOdds34 = get_capsule_value(orbBagCapsuleSpaceOdds34)
    mysteryCapsulePrice12 = get_capsule_value(mysteryCapsulePrice12)
    mysteryCapsulePrice34 = get_capsule_value(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = get_capsule_value(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = get_capsule_value(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds12 = get_capsule_value(mysteryCapsuleSpaceOdds12)
    mysteryCapsuleSpaceOdds34 = get_capsule_value(mysteryCapsuleSpaceOdds34)
    dkCapsulePrice12 = get_capsule_value(dkCapsulePrice12)
    dkCapsulePrice34 = get_capsule_value(dkCapsulePrice34)
    dkCapsuleShopOdds12 = get_capsule_value(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = get_capsule_value(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds12 = get_capsule_value(dkCapsuleSpaceOdds12)
    dkCapsuleSpaceOdds34 = get_capsule_value(dkCapsuleSpaceOdds34)
    duelCapsulePrice12 = get_capsule_value(duelCapsulePrice12)
    duelCapsulePrice34 = get_capsule_value(duelCapsulePrice34)
    duelCapsuleShopOdds12 = get_capsule_value(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = get_capsule_value(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds12 = get_capsule_value(duelCapsuleSpaceOdds12)
    duelCapsuleSpaceOdds34 = get_capsule_value(duelCapsuleSpaceOdds34)


    # Weights lists
    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, lakituCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, spearGuyCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, zapCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, flowerCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, lakituCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, spearGuyCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, zapCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, flowerCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
    ]

    spaceOdds12 = [
        mushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds12,
        slowMushroomCapsuleSpaceOdds12, flutterCapsuleSpaceOdds12, cannonCapsuleSpaceOdds12,
        snackCapsuleSpaceOdds12, lakituCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds12,
        piranhaPlantCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds12, kamekCapsuleSpaceOdds12,
        toadyCapsuleSpaceOdds12, mrBlizzardCapsuleSpaceOdds12, banditCapsuleSpaceOdds12,
        pinkBooCapsuleSpaceOdds12, spinyCapsuleSpaceOdds12, zapCapsuleSpaceOdds12,
        tweesterCapsuleSpaceOdds12, thwompCapsuleSpaceOdds12, warpCapsuleSpaceOdds12,
        bombCapsuleSpaceOdds12, fireballCapsuleSpaceOdds12, flowerCapsuleSpaceOdds12,
        eggCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds12, magicCapsuleSpaceOdds12,
        tripleCapsuleSpaceOdds12, koopaCapsuleSpaceOdds12, mysteryCapsuleSpaceOdds12,
        duelCapsuleSpaceOdds12, dkCapsuleSpaceOdds12, orbBagCapsuleSpaceOdds12
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, lakituCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, spearGuyCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, zapCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, flowerCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
    ]


    shopOdds12Weights = sum(int(weight) for weight in shopOdds12)
    shopOdds34Weights = sum(int(weight) for weight in shopOdds34)
    spaceOdds12Weights = sum(int(weight) for weight in spaceOdds12)
    spaceOdds34Weights = sum(int(weight) for weight in spaceOdds34)

    def calculateWeight(weight, total):
       if total < 100:
           percentage = int(weight)
           return percentage
       else:
           percentage = (int(weight) / total) * 100
           if 0< percentage < 1:
               return math.ceil(percentage)
           return round(percentage)
       
    # Calculate weights for shop odds 12
    mushroomCapsuleShopOdds12 = calculateWeight(mushroomCapsuleShopOdds12, shopOdds12Weights)
    goldenMushroomCapsuleShopOdds12 = calculateWeight(goldenMushroomCapsuleShopOdds12, shopOdds12Weights)
    metalMushroomCapsuleShopOdds12 = calculateWeight(metalMushroomCapsuleShopOdds12, shopOdds12Weights)
    slowMushroomCapsuleShopOdds12 = calculateWeight(slowMushroomCapsuleShopOdds12, shopOdds12Weights)
    flutterCapsuleShopOdds12 = calculateWeight(flutterCapsuleShopOdds12, shopOdds12Weights)
    cannonCapsuleShopOdds12 = calculateWeight(cannonCapsuleShopOdds12, shopOdds12Weights)
    snackCapsuleShopOdds12 = calculateWeight(snackCapsuleShopOdds12, shopOdds12Weights)
    lakituCapsuleShopOdds12 = calculateWeight(lakituCapsuleShopOdds12, shopOdds12Weights)
    hammerBroCapsuleShopOdds12 = calculateWeight(hammerBroCapsuleShopOdds12, shopOdds12Weights)
    piranhaPlantCapsuleShopOdds12 = calculateWeight(piranhaPlantCapsuleShopOdds12, shopOdds12Weights)
    spearGuyCapsuleShopOdds12 = calculateWeight(spearGuyCapsuleShopOdds12, shopOdds12Weights)
    kamekCapsuleShopOdds12 = calculateWeight(kamekCapsuleShopOdds12, shopOdds12Weights)
    toadyCapsuleShopOdds12 = calculateWeight(toadyCapsuleShopOdds12, shopOdds12Weights)
    mrBlizzardCapsuleShopOdds12 = calculateWeight(mrBlizzardCapsuleShopOdds12, shopOdds12Weights)
    banditCapsuleShopOdds12 = calculateWeight(banditCapsuleShopOdds12, shopOdds12Weights)
    pinkBooCapsuleShopOdds12 = calculateWeight(pinkBooCapsuleShopOdds12, shopOdds12Weights)
    spinyCapsuleShopOdds12 = calculateWeight(spinyCapsuleShopOdds12, shopOdds12Weights)
    zapCapsuleShopOdds12 = calculateWeight(zapCapsuleShopOdds12, shopOdds12Weights)
    tweesterCapsuleShopOdds12 = calculateWeight(tweesterCapsuleShopOdds12, shopOdds12Weights)
    thwompCapsuleShopOdds12 = calculateWeight(thwompCapsuleShopOdds12, shopOdds12Weights)
    warpCapsuleShopOdds12 = calculateWeight(warpCapsuleShopOdds12, shopOdds12Weights)
    bombCapsuleShopOdds12 = calculateWeight(bombCapsuleShopOdds12, shopOdds12Weights)
    fireballCapsuleShopOdds12 = calculateWeight(fireballCapsuleShopOdds12, shopOdds12Weights)
    flowerCapsuleShopOdds12 = calculateWeight(flowerCapsuleShopOdds12, shopOdds12Weights)
    eggCapsuleShopOdds12 = calculateWeight(eggCapsuleShopOdds12, shopOdds12Weights)
    vacuumCapsuleShopOdds12 = calculateWeight(vacuumCapsuleShopOdds12, shopOdds12Weights)
    magicCapsuleShopOdds12 = calculateWeight(magicCapsuleShopOdds12, shopOdds12Weights)
    tripleCapsuleShopOdds12 = calculateWeight(tripleCapsuleShopOdds12, shopOdds12Weights)
    koopaCapsuleShopOdds12 = calculateWeight(koopaCapsuleShopOdds12, shopOdds12Weights)
    mysteryCapsuleShopOdds12 = calculateWeight(mysteryCapsuleShopOdds12, shopOdds12Weights)
    duelCapsuleShopOdds12 = calculateWeight(duelCapsuleShopOdds12, shopOdds12Weights)
    dkCapsuleShopOdds12 = calculateWeight(dkCapsuleShopOdds12, shopOdds12Weights)
    orbBagCapsuleShopOdds12 = calculateWeight(orbBagCapsuleShopOdds12, shopOdds12Weights)

    # Calculate weights for shop odds 34
    mushroomCapsuleShopOdds34 = calculateWeight(mushroomCapsuleShopOdds34, shopOdds34Weights)
    goldenMushroomCapsuleShopOdds34 = calculateWeight(goldenMushroomCapsuleShopOdds34, shopOdds34Weights)
    metalMushroomCapsuleShopOdds34 = calculateWeight(metalMushroomCapsuleShopOdds34, shopOdds34Weights)
    slowMushroomCapsuleShopOdds34 = calculateWeight(slowMushroomCapsuleShopOdds34, shopOdds34Weights)
    flutterCapsuleShopOdds34 = calculateWeight(flutterCapsuleShopOdds34, shopOdds34Weights)
    cannonCapsuleShopOdds34 = calculateWeight(cannonCapsuleShopOdds34, shopOdds34Weights)
    snackCapsuleShopOdds34 = calculateWeight(snackCapsuleShopOdds34, shopOdds34Weights)
    lakituCapsuleShopOdds34 = calculateWeight(lakituCapsuleShopOdds34, shopOdds34Weights)
    hammerBroCapsuleShopOdds34 = calculateWeight(hammerBroCapsuleShopOdds34, shopOdds34Weights)
    piranhaPlantCapsuleShopOdds34 = calculateWeight(piranhaPlantCapsuleShopOdds34, shopOdds34Weights)
    spearGuyCapsuleShopOdds34 = calculateWeight(spearGuyCapsuleShopOdds34, shopOdds34Weights)
    kamekCapsuleShopOdds34 = calculateWeight(kamekCapsuleShopOdds34, shopOdds34Weights)
    toadyCapsuleShopOdds34 = calculateWeight(toadyCapsuleShopOdds34, shopOdds34Weights)
    mrBlizzardCapsuleShopOdds34 = calculateWeight(mrBlizzardCapsuleShopOdds34, shopOdds34Weights)
    banditCapsuleShopOdds34 = calculateWeight(banditCapsuleShopOdds34, shopOdds34Weights)
    pinkBooCapsuleShopOdds34 = calculateWeight(pinkBooCapsuleShopOdds34, shopOdds34Weights)
    spinyCapsuleShopOdds34 = calculateWeight(spinyCapsuleShopOdds34, shopOdds34Weights)
    zapCapsuleShopOdds34 = calculateWeight(zapCapsuleShopOdds34, shopOdds34Weights)
    tweesterCapsuleShopOdds34 = calculateWeight(tweesterCapsuleShopOdds34, shopOdds34Weights)
    thwompCapsuleShopOdds34 = calculateWeight(thwompCapsuleShopOdds34, shopOdds34Weights)
    warpCapsuleShopOdds34 = calculateWeight(warpCapsuleShopOdds34, shopOdds34Weights)
    bombCapsuleShopOdds34 = calculateWeight(bombCapsuleShopOdds34, shopOdds34Weights)
    fireballCapsuleShopOdds34 = calculateWeight(fireballCapsuleShopOdds34, shopOdds34Weights)
    flowerCapsuleShopOdds34 = calculateWeight(flowerCapsuleShopOdds34, shopOdds34Weights)
    eggCapsuleShopOdds34 = calculateWeight(eggCapsuleShopOdds34, shopOdds34Weights)
    vacuumCapsuleShopOdds34 = calculateWeight(vacuumCapsuleShopOdds34, shopOdds34Weights)
    magicCapsuleShopOdds34 = calculateWeight(magicCapsuleShopOdds34, shopOdds34Weights)
    tripleCapsuleShopOdds34 = calculateWeight(tripleCapsuleShopOdds34, shopOdds34Weights)
    koopaCapsuleShopOdds34 = calculateWeight(koopaCapsuleShopOdds34, shopOdds34Weights)
    mysteryCapsuleShopOdds34 = calculateWeight(mysteryCapsuleShopOdds34, shopOdds34Weights)
    duelCapsuleShopOdds34 = calculateWeight(duelCapsuleShopOdds34, shopOdds34Weights)
    dkCapsuleShopOdds34 = calculateWeight(dkCapsuleShopOdds34, shopOdds34Weights)
    orbBagCapsuleShopOdds34 = calculateWeight(orbBagCapsuleShopOdds34, shopOdds34Weights)

    # Calculate weights for space odds 12
    mushroomCapsuleSpaceOdds12 = calculateWeight(mushroomCapsuleSpaceOdds12, spaceOdds12Weights)
    goldenMushroomCapsuleSpaceOdds12 = calculateWeight(goldenMushroomCapsuleSpaceOdds12, spaceOdds12Weights)
    metalMushroomCapsuleSpaceOdds12 = calculateWeight(metalMushroomCapsuleSpaceOdds12, spaceOdds12Weights)
    slowMushroomCapsuleSpaceOdds12 = calculateWeight(slowMushroomCapsuleSpaceOdds12, spaceOdds12Weights)
    flutterCapsuleSpaceOdds12 = calculateWeight(flutterCapsuleSpaceOdds12, spaceOdds12Weights)
    cannonCapsuleSpaceOdds12 = calculateWeight(cannonCapsuleSpaceOdds12, spaceOdds12Weights)
    snackCapsuleSpaceOdds12 = calculateWeight(snackCapsuleSpaceOdds12, spaceOdds12Weights)
    lakituCapsuleSpaceOdds12 = calculateWeight(lakituCapsuleSpaceOdds12, spaceOdds12Weights)
    hammerBroCapsuleSpaceOdds12 = calculateWeight(hammerBroCapsuleSpaceOdds12, spaceOdds12Weights)
    piranhaPlantCapsuleSpaceOdds12 = calculateWeight(piranhaPlantCapsuleSpaceOdds12, spaceOdds12Weights)
    spearGuyCapsuleSpaceOdds12 = calculateWeight(spearGuyCapsuleSpaceOdds12, spaceOdds12Weights)
    kamekCapsuleSpaceOdds12 = calculateWeight(kamekCapsuleSpaceOdds12, spaceOdds12Weights)
    toadyCapsuleSpaceOdds12 = calculateWeight(toadyCapsuleSpaceOdds12, spaceOdds12Weights)
    mrBlizzardCapsuleSpaceOdds12 = calculateWeight(mrBlizzardCapsuleSpaceOdds12, spaceOdds12Weights)
    banditCapsuleSpaceOdds12 = calculateWeight(banditCapsuleSpaceOdds12, spaceOdds12Weights)
    pinkBooCapsuleSpaceOdds12 = calculateWeight(pinkBooCapsuleSpaceOdds12, spaceOdds12Weights)
    spinyCapsuleSpaceOdds12 = calculateWeight(spinyCapsuleSpaceOdds12, spaceOdds12Weights)
    zapCapsuleSpaceOdds12 = calculateWeight(zapCapsuleSpaceOdds12, spaceOdds12Weights)
    tweesterCapsuleSpaceOdds12 = calculateWeight(tweesterCapsuleSpaceOdds12, spaceOdds12Weights)
    thwompCapsuleSpaceOdds12 = calculateWeight(thwompCapsuleSpaceOdds12, spaceOdds12Weights)
    warpCapsuleSpaceOdds12 = calculateWeight(warpCapsuleSpaceOdds12, spaceOdds12Weights)
    bombCapsuleSpaceOdds12 = calculateWeight(bombCapsuleSpaceOdds12, spaceOdds12Weights)
    fireballCapsuleSpaceOdds12 = calculateWeight(fireballCapsuleSpaceOdds12, spaceOdds12Weights)
    flowerCapsuleSpaceOdds12 = calculateWeight(flowerCapsuleSpaceOdds12, spaceOdds12Weights)
    eggCapsuleSpaceOdds12 = calculateWeight(eggCapsuleSpaceOdds12, spaceOdds12Weights)
    vacuumCapsuleSpaceOdds12 = calculateWeight(vacuumCapsuleSpaceOdds12, spaceOdds12Weights)
    magicCapsuleSpaceOdds12 = calculateWeight(magicCapsuleSpaceOdds12, spaceOdds12Weights)
    tripleCapsuleSpaceOdds12 = calculateWeight(tripleCapsuleSpaceOdds12, spaceOdds12Weights)
    koopaCapsuleSpaceOdds12 = calculateWeight(koopaCapsuleSpaceOdds12, spaceOdds12Weights)
    mysteryCapsuleSpaceOdds12 = calculateWeight(mysteryCapsuleSpaceOdds12, spaceOdds12Weights)
    duelCapsuleSpaceOdds12 = calculateWeight(duelCapsuleSpaceOdds12, spaceOdds12Weights)
    dkCapsuleSpaceOdds12 = calculateWeight(dkCapsuleSpaceOdds12, spaceOdds12Weights)
    orbBagCapsuleSpaceOdds12 = calculateWeight(orbBagCapsuleSpaceOdds12, spaceOdds12Weights)

    # Calculate weights for space odds 34
    mushroomCapsuleSpaceOdds34 = calculateWeight(mushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    goldenMushroomCapsuleSpaceOdds34 = calculateWeight(goldenMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    metalMushroomCapsuleSpaceOdds34 = calculateWeight(metalMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    slowMushroomCapsuleSpaceOdds34 = calculateWeight(slowMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    flutterCapsuleSpaceOdds34 = calculateWeight(flutterCapsuleSpaceOdds34, spaceOdds34Weights)
    cannonCapsuleSpaceOdds34 = calculateWeight(cannonCapsuleSpaceOdds34, spaceOdds34Weights)
    snackCapsuleSpaceOdds34 = calculateWeight(snackCapsuleSpaceOdds34, spaceOdds34Weights)
    lakituCapsuleSpaceOdds34 = calculateWeight(lakituCapsuleSpaceOdds34, spaceOdds34Weights)
    hammerBroCapsuleSpaceOdds34 = calculateWeight(hammerBroCapsuleSpaceOdds34, spaceOdds34Weights)
    piranhaPlantCapsuleSpaceOdds34 = calculateWeight(piranhaPlantCapsuleSpaceOdds34, spaceOdds34Weights)
    spearGuyCapsuleSpaceOdds34 = calculateWeight(spearGuyCapsuleSpaceOdds34, spaceOdds34Weights)
    kamekCapsuleSpaceOdds34 = calculateWeight(kamekCapsuleSpaceOdds34, spaceOdds34Weights)
    toadyCapsuleSpaceOdds34 = calculateWeight(toadyCapsuleSpaceOdds34, spaceOdds34Weights)
    mrBlizzardCapsuleSpaceOdds34 = calculateWeight(mrBlizzardCapsuleSpaceOdds34, spaceOdds34Weights)
    banditCapsuleSpaceOdds34 = calculateWeight(banditCapsuleSpaceOdds34, spaceOdds34Weights)
    pinkBooCapsuleSpaceOdds34 = calculateWeight(pinkBooCapsuleSpaceOdds34, spaceOdds34Weights)
    spinyCapsuleSpaceOdds34 = calculateWeight(spinyCapsuleSpaceOdds34, spaceOdds34Weights)
    zapCapsuleSpaceOdds34 = calculateWeight(zapCapsuleSpaceOdds34, spaceOdds34Weights)
    tweesterCapsuleSpaceOdds34 = calculateWeight(tweesterCapsuleSpaceOdds34, spaceOdds34Weights)
    thwompCapsuleSpaceOdds34 = calculateWeight(thwompCapsuleSpaceOdds34, spaceOdds34Weights)
    warpCapsuleSpaceOdds34 = calculateWeight(warpCapsuleSpaceOdds34, spaceOdds34Weights)
    bombCapsuleSpaceOdds34 = calculateWeight(bombCapsuleSpaceOdds34, spaceOdds34Weights)
    fireballCapsuleSpaceOdds34 = calculateWeight(fireballCapsuleSpaceOdds34, spaceOdds34Weights)
    flowerCapsuleSpaceOdds34 = calculateWeight(flowerCapsuleSpaceOdds34, spaceOdds34Weights)
    eggCapsuleSpaceOdds34 = calculateWeight(eggCapsuleSpaceOdds34, spaceOdds34Weights)
    vacuumCapsuleSpaceOdds34 = calculateWeight(vacuumCapsuleSpaceOdds34, spaceOdds34Weights)
    magicCapsuleSpaceOdds34 = calculateWeight(magicCapsuleSpaceOdds34, spaceOdds34Weights)
    tripleCapsuleSpaceOdds34 = calculateWeight(tripleCapsuleSpaceOdds34, spaceOdds34Weights)
    koopaCapsuleSpaceOdds34 = calculateWeight(koopaCapsuleSpaceOdds34, spaceOdds34Weights)
    mysteryCapsuleSpaceOdds34 = calculateWeight(mysteryCapsuleSpaceOdds34, spaceOdds34Weights)
    duelCapsuleSpaceOdds34 = calculateWeight(duelCapsuleSpaceOdds34, spaceOdds34Weights)
    dkCapsuleSpaceOdds34 = calculateWeight(dkCapsuleSpaceOdds34, spaceOdds34Weights)
    orbBagCapsuleSpaceOdds34 = calculateWeight(orbBagCapsuleSpaceOdds34, spaceOdds34Weights)


    # Redefine Weights lists
    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, lakituCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, spearGuyCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, zapCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, flowerCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, lakituCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, spearGuyCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, zapCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, flowerCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
    ]

    spaceOdds12 = [
        mushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds12,
        slowMushroomCapsuleSpaceOdds12, flutterCapsuleSpaceOdds12, cannonCapsuleSpaceOdds12,
        snackCapsuleSpaceOdds12, lakituCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds12,
        piranhaPlantCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds12, kamekCapsuleSpaceOdds12,
        toadyCapsuleSpaceOdds12, mrBlizzardCapsuleSpaceOdds12, banditCapsuleSpaceOdds12,
        pinkBooCapsuleSpaceOdds12, spinyCapsuleSpaceOdds12, zapCapsuleSpaceOdds12,
        tweesterCapsuleSpaceOdds12, thwompCapsuleSpaceOdds12, warpCapsuleSpaceOdds12,
        bombCapsuleSpaceOdds12, fireballCapsuleSpaceOdds12, flowerCapsuleSpaceOdds12,
        eggCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds12, magicCapsuleSpaceOdds12,
        tripleCapsuleSpaceOdds12, koopaCapsuleSpaceOdds12, mysteryCapsuleSpaceOdds12,
        duelCapsuleSpaceOdds12, dkCapsuleSpaceOdds12, orbBagCapsuleSpaceOdds12
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, lakituCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, spearGuyCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, zapCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, flowerCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
    ]

    spaceOdds12Weights = sum(weight for weight in spaceOdds12)
    spaceOdds34Weights = sum(weight for weight in spaceOdds34)
    shopOdds12Weights = sum(weight for weight in shopOdds12)
    shopOdds34Weights = sum(weight for weight in shopOdds34)

    if spaceOdds12Weights < 100:
        spaceOdds12Max = max(zip(spaceOdds12, (map(eval, spaceOdds12))), key=lambda tuple: tuple[1])[0]

    if spaceOdds34Weights < 100:
        spaceOdds34Max = max(zip(spaceOdds34, (map(eval, spaceOdds34))), key=lambda tuple: tuple[1])[0]

    if shopOdds12Weights < 100:
        shopOdds12Max = max(zip(shopOdds12, (map(eval, shopOdds12))), key=lambda tuple: tuple[1])[0]

    if shopOdds34Weights < 100:
        shopOdds34Max = max(zip(shopOdds34, (map(eval, shopOdds34))), key=lambda tuple: tuple[1])[0]

    if shopOdds12Max == 'mushroomCapsuleShopOdds12':
        mushroomCapsuleShopOdds12 += (100 - mushroomCapsuleShopOdds12)

    if shopOdds12Max == 'goldenMushroomCapsuleShopOdds12':
        goldenMushroomCapsuleShopOdds12 += (100 - goldenMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'metalMushroomCapsuleShopOdds12':
        metalMushroomCapsuleShopOdds12 += (100 - metalMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'slowMushroomCapsuleShopOdds12':
        slowMushroomCapsuleShopOdds12 += (100 - slowMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'flutterCapsuleShopOdds12':
        flutterCapsuleShopOdds12 += (100 - flutterCapsuleShopOdds12)

    if shopOdds12Max == 'cannonCapsuleShopOdds12':
        cannonCapsuleShopOdds12 += (100 - cannonCapsuleShopOdds12)

    if shopOdds12Max == 'snackCapsuleShopOdds12':
        snackCapsuleShopOdds12 += (100 - snackCapsuleShopOdds12)

    if shopOdds12Max == 'lakituCapsuleShopOdds12':
        lakituCapsuleShopOdds12 += (100 - lakituCapsuleShopOdds12)

    if shopOdds12Max == 'hammerBroCapsuleShopOdds12':
        hammerBroCapsuleShopOdds12 += (100 - hammerBroCapsuleShopOdds12)

    if shopOdds12Max == 'piranhaPlantCapsuleShopOdds12':
        piranhaPlantCapsuleShopOdds12 += (100 - piranhaPlantCapsuleShopOdds12)

    if shopOdds12Max == 'spearGuyCapsuleShopOdds12':
        spearGuyCapsuleShopOdds12 += (100 - spearGuyCapsuleShopOdds12)

    if shopOdds12Max == 'kamekCapsuleShopOdds12':
        kamekCapsuleShopOdds12 += (100 - kamekCapsuleShopOdds12)

    if shopOdds12Max == 'toadyCapsuleShopOdds12':
        toadyCapsuleShopOdds12 += (100 - toadyCapsuleShopOdds12)

    if shopOdds12Max == 'mrBlizzardCapsuleShopOdds12':
        mrBlizzardCapsuleShopOdds12 += (100 - mrBlizzardCapsuleShopOdds12)

    if shopOdds12Max == 'banditCapsuleShopOdds12':
        banditCapsuleShopOdds12 += (100 - banditCapsuleShopOdds12)

    if shopOdds12Max == 'pinkBooCapsuleShopOdds12':
        pinkBooCapsuleShopOdds12 += (100 - pinkBooCapsuleShopOdds12)

    if shopOdds12Max == 'spinyCapsuleShopOdds12':
        spinyCapsuleShopOdds12 += (100 - spinyCapsuleShopOdds12)

    if shopOdds12Max == 'zapCapsuleShopOdds12':
        zapCapsuleShopOdds12 += (100 - zapCapsuleShopOdds12)

    if shopOdds12Max == 'tweesterCapsuleShopOdds12':
        tweesterCapsuleShopOdds12 += (100 - tweesterCapsuleShopOdds12)

    if shopOdds12Max == 'thwompCapsuleShopOdds12':
        thwompCapsuleShopOdds12 += (100 - thwompCapsuleShopOdds12)

    if shopOdds12Max == 'warpCapsuleShopOdds12':
        warpCapsuleShopOdds12 += (100 - warpCapsuleShopOdds12)

    if shopOdds12Max == 'bombCapsuleShopOdds12':
        bombCapsuleShopOdds12 += (100 - bombCapsuleShopOdds12)

    if shopOdds12Max == 'fireballCapsuleShopOdds12':
        fireballCapsuleShopOdds12 += (100 - fireballCapsuleShopOdds12)

    if shopOdds12Max == 'flowerCapsuleShopOdds12':
        flowerCapsuleShopOdds12 += (100 - flowerCapsuleShopOdds12)

    if shopOdds12Max == 'eggCapsuleShopOdds12':
        eggCapsuleShopOdds12 += (100 - eggCapsuleShopOdds12)

    if shopOdds12Max == 'vacuumCapsuleShopOdds12':
        vacuumCapsuleShopOdds12 += (100 - vacuumCapsuleShopOdds12)

    if shopOdds12Max == 'magicCapsuleShopOdds12':
        magicCapsuleShopOdds12 += (100 - magicCapsuleShopOdds12)

    if shopOdds12Max == 'tripleCapsuleShopOdds12':
        tripleCapsuleShopOdds12 += (100 - tripleCapsuleShopOdds12)

    if shopOdds12Max == 'koopaCapsuleShopOdds12':
        koopaCapsuleShopOdds12 += (100 - koopaCapsuleShopOdds12)

    if shopOdds12Max == 'mysteryCapsuleShopOdds12':
        mysteryCapsuleShopOdds12 += (100 - mysteryCapsuleShopOdds12)

    if shopOdds12Max == 'duelCapsuleShopOdds12':
        duelCapsuleShopOdds12 += (100 - duelCapsuleShopOdds12)

    if shopOdds12Max == 'dkCapsuleShopOdds12':
        dkCapsuleShopOdds12 += (100 - dkCapsuleShopOdds12)

    if shopOdds12Max == 'orbBagCapsuleShopOdds12':
        orbBagCapsuleShopOdds12 += (100 - orbBagCapsuleShopOdds12)

    if shopOdds34Max == 'mushroomCapsuleShopOdds34':
        mushroomCapsuleShopOdds34 += (100 - mushroomCapsuleShopOdds34)

    if shopOdds34Max == 'goldenMushroomCapsuleShopOdds34':
        goldenMushroomCapsuleShopOdds34 += (100 - goldenMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'metalMushroomCapsuleShopOdds34':
        metalMushroomCapsuleShopOdds34 += (100 - metalMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'slowMushroomCapsuleShopOdds34':
        slowMushroomCapsuleShopOdds34 += (100 - slowMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'flutterCapsuleShopOdds34':
        flutterCapsuleShopOdds34 += (100 - flutterCapsuleShopOdds34)

    if shopOdds34Max == 'cannonCapsuleShopOdds34':
        cannonCapsuleShopOdds34 += (100 - cannonCapsuleShopOdds34)

    if shopOdds34Max == 'snackCapsuleShopOdds34':
        snackCapsuleShopOdds34 += (100 - snackCapsuleShopOdds34)

    if shopOdds34Max == 'lakituCapsuleShopOdds34':
        lakituCapsuleShopOdds34 += (100 - lakituCapsuleShopOdds34)

    if shopOdds34Max == 'hammerBroCapsuleShopOdds34':
        hammerBroCapsuleShopOdds34 += (100 - hammerBroCapsuleShopOdds34)

    if shopOdds34Max == 'piranhaPlantCapsuleShopOdds34':
        piranhaPlantCapsuleShopOdds34 += (100 - piranhaPlantCapsuleShopOdds34)

    if shopOdds34Max == 'spearGuyCapsuleShopOdds34':
        spearGuyCapsuleShopOdds34 += (100 - spearGuyCapsuleShopOdds34)

    if shopOdds34Max == 'kamekCapsuleShopOdds34':
        kamekCapsuleShopOdds34 += (100 - kamekCapsuleShopOdds34)

    if shopOdds34Max == 'toadyCapsuleShopOdds34':
        toadyCapsuleShopOdds34 += (100 - toadyCapsuleShopOdds34)

    if shopOdds34Max == 'mrBlizzardCapsuleShopOdds34':
        mrBlizzardCapsuleShopOdds34 += (100 - mrBlizzardCapsuleShopOdds34)

    if shopOdds34Max == 'banditCapsuleShopOdds34':
        banditCapsuleShopOdds34 += (100 - banditCapsuleShopOdds34)

    if shopOdds34Max == 'pinkBooCapsuleShopOdds34':
        pinkBooCapsuleShopOdds34 += (100 - pinkBooCapsuleShopOdds34)

    if shopOdds34Max == 'spinyCapsuleShopOdds34':
        spinyCapsuleShopOdds34 += (100 - spinyCapsuleShopOdds34)

    if shopOdds34Max == 'zapCapsuleShopOdds34':
        zapCapsuleShopOdds34 += (100 - zapCapsuleShopOdds34)

    if shopOdds34Max == 'tweesterCapsuleShopOdds34':
        tweesterCapsuleShopOdds34 += (100 - tweesterCapsuleShopOdds34)

    if shopOdds34Max == 'thwompCapsuleShopOdds34':
        thwompCapsuleShopOdds34 += (100 - thwompCapsuleShopOdds34)

    if shopOdds34Max == 'warpCapsuleShopOdds34':
        warpCapsuleShopOdds34 += (100 - warpCapsuleShopOdds34)

    if shopOdds34Max == 'bombCapsuleShopOdds34':
        bombCapsuleShopOdds34 += (100 - bombCapsuleShopOdds34)

    if shopOdds34Max == 'fireballCapsuleShopOdds34':
        fireballCapsuleShopOdds34 += (100 - fireballCapsuleShopOdds34)

    if shopOdds34Max == 'flowerCapsuleShopOdds34':
        flowerCapsuleShopOdds34 += (100 - flowerCapsuleShopOdds34)

    if shopOdds34Max == 'eggCapsuleShopOdds34':
        eggCapsuleShopOdds34 += (100 - eggCapsuleShopOdds34)

    if shopOdds34Max == 'vacuumCapsuleShopOdds34':
        vacuumCapsuleShopOdds34 += (100 - vacuumCapsuleShopOdds34)

    if shopOdds34Max == 'magicCapsuleShopOdds34':
        magicCapsuleShopOdds34 += (100 - magicCapsuleShopOdds34)

    if shopOdds34Max == 'tripleCapsuleShopOdds34':
        tripleCapsuleShopOdds34 += (100 - tripleCapsuleShopOdds34)

    if shopOdds34Max == 'koopaCapsuleShopOdds34':
        koopaCapsuleShopOdds34 += (100 - koopaCapsuleShopOdds34)

    if shopOdds34Max == 'mysteryCapsuleShopOdds34':
        mysteryCapsuleShopOdds34 += (100 - mysteryCapsuleShopOdds34)

    if shopOdds34Max == 'duelCapsuleShopOdds34':
        duelCapsuleShopOdds34 += (100 - duelCapsuleShopOdds34)

    if shopOdds34Max == 'dkCapsuleShopOdds34':
        dkCapsuleShopOdds34 += (100 - dkCapsuleShopOdds34)

    if shopOdds34Max == 'orbBagCapsuleShopOdds34':
        orbBagCapsuleShopOdds34 += (100 - orbBagCapsuleShopOdds34)

    if spaceOdds12Max == 'mushroomCapsuleSpaceOdds12':
        mushroomCapsuleSpaceOdds12 += (100 - mushroomCapsuleSpaceOdds12)

    if spaceOdds12Max == 'goldenMushroomCapsuleSpaceOdds12':
        goldenMushroomCapsuleSpaceOdds12 += (100 - goldenMushroomCapsuleSpaceOdds12)

    if spaceOdds12Max == 'metalMushroomCapsuleSpaceOdds12':
        metalMushroomCapsuleSpaceOdds12 += (100 - metalMushroomCapsuleSpaceOdds12)

    if spaceOdds12Max == 'slowMushroomCapsuleSpaceOdds12':
        slowMushroomCapsuleSpaceOdds12 += (100 - slowMushroomCapsuleSpaceOdds12)

    if spaceOdds12Max == 'flutterCapsuleSpaceOdds12':
        flutterCapsuleSpaceOdds12 += (100 - flutterCapsuleSpaceOdds12)

    if spaceOdds12Max == 'cannonCapsuleSpaceOdds12':
        cannonCapsuleSpaceOdds12 += (100 - cannonCapsuleSpaceOdds12)

    if spaceOdds12Max == 'snackCapsuleSpaceOdds12':
        snackCapsuleSpaceOdds12 += (100 - snackCapsuleSpaceOdds12)

    if spaceOdds12Max == 'lakituCapsuleSpaceOdds12':
        lakituCapsuleSpaceOdds12 += (100 - lakituCapsuleSpaceOdds12)

    if spaceOdds12Max == 'hammerBroCapsuleSpaceOdds12':
        hammerBroCapsuleSpaceOdds12 += (100 - hammerBroCapsuleSpaceOdds12)

    if spaceOdds12Max == 'piranhaPlantCapsuleSpaceOdds12':
        piranhaPlantCapsuleSpaceOdds12 += (100 - piranhaPlantCapsuleSpaceOdds12)

    if spaceOdds12Max == 'spearGuyCapsuleSpaceOdds12':
        spearGuyCapsuleSpaceOdds12 += (100 - spearGuyCapsuleSpaceOdds12)

    if spaceOdds12Max == 'kamekCapsuleSpaceOdds12':
        kamekCapsuleSpaceOdds12 += (100 - kamekCapsuleSpaceOdds12)

    if spaceOdds12Max == 'toadyCapsuleSpaceOdds12':
        toadyCapsuleSpaceOdds12 += (100 - toadyCapsuleSpaceOdds12)

    if spaceOdds12Max == 'mrBlizzardCapsuleSpaceOdds12':
        mrBlizzardCapsuleSpaceOdds12 += (100 - mrBlizzardCapsuleSpaceOdds12)

    if spaceOdds12Max == 'banditCapsuleSpaceOdds12':
        banditCapsuleSpaceOdds12 += (100 - banditCapsuleSpaceOdds12)

    if spaceOdds12Max == 'pinkBooCapsuleSpaceOdds12':
        pinkBooCapsuleSpaceOdds12 += (100 - pinkBooCapsuleSpaceOdds12)

    if spaceOdds12Max == 'spinyCapsuleSpaceOdds12':
        spinyCapsuleSpaceOdds12 += (100 - spinyCapsuleSpaceOdds12)

    if spaceOdds12Max == 'zapCapsuleSpaceOdds12':
        zapCapsuleSpaceOdds12 += (100 - zapCapsuleSpaceOdds12)

    if spaceOdds12Max == 'tweesterCapsuleSpaceOdds12':
        tweesterCapsuleSpaceOdds12 += (100 - tweesterCapsuleSpaceOdds12)

    if spaceOdds12Max == 'thwompCapsuleSpaceOdds12':
        thwompCapsuleSpaceOdds12 += (100 - thwompCapsuleSpaceOdds12)

    if spaceOdds12Max == 'warpCapsuleSpaceOdds12':
        warpCapsuleSpaceOdds12 += (100 - warpCapsuleSpaceOdds12)

    if spaceOdds12Max == 'bombCapsuleSpaceOdds12':
        bombCapsuleSpaceOdds12 += (100 - bombCapsuleSpaceOdds12)

    if spaceOdds12Max == 'fireballCapsuleSpaceOdds12':
        fireballCapsuleSpaceOdds12 += (100 - fireballCapsuleSpaceOdds12)

    if spaceOdds12Max == 'flowerCapsuleSpaceOdds12':
        flowerCapsuleSpaceOdds12 += (100 - flowerCapsuleSpaceOdds12)

    if spaceOdds12Max == 'eggCapsuleSpaceOdds12':
        eggCapsuleSpaceOdds12 += (100 - eggCapsuleSpaceOdds12)

    if spaceOdds12Max == 'vacuumCapsuleSpaceOdds12':
        vacuumCapsuleSpaceOdds12 += (100 - vacuumCapsuleSpaceOdds12)

    if spaceOdds12Max == 'magicCapsuleSpaceOdds12':
        magicCapsuleSpaceOdds12 += (100 - magicCapsuleSpaceOdds12)

    if spaceOdds12Max == 'tripleCapsuleSpaceOdds12':
        tripleCapsuleSpaceOdds12 += (100 - tripleCapsuleSpaceOdds12)

    if spaceOdds12Max == 'koopaCapsuleSpaceOdds12':
        koopaCapsuleSpaceOdds12 += (100 - koopaCapsuleSpaceOdds12)

    if spaceOdds12Max == 'mysteryCapsuleSpaceOdds12':
        mysteryCapsuleSpaceOdds12 += (100 - mysteryCapsuleSpaceOdds12)

    if spaceOdds12Max == 'duelCapsuleSpaceOdds12':
        duelCapsuleSpaceOdds12 += (100 - duelCapsuleSpaceOdds12)

    if spaceOdds12Max == 'dkCapsuleSpaceOdds12':
        dkCapsuleSpaceOdds12 += (100 - dkCapsuleSpaceOdds12)

    if spaceOdds12Max == 'orbBagCapsuleSpaceOdds12':
        orbBagCapsuleSpaceOdds12 += (100 - orbBagCapsuleSpaceOdds12)

    if spaceOdds34Max == 'mushroomCapsuleSpaceOdds34':
        mushroomCapsuleSpaceOdds34 += (100 - mushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'goldenMushroomCapsuleSpaceOdds34':
        goldenMushroomCapsuleSpaceOdds34 += (100 - goldenMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'metalMushroomCapsuleSpaceOdds34':
        metalMushroomCapsuleSpaceOdds34 += (100 - metalMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'slowMushroomCapsuleSpaceOdds34':
        slowMushroomCapsuleSpaceOdds34 += (100 - slowMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'flutterCapsuleSpaceOdds34':
        flutterCapsuleSpaceOdds34 += (100 - flutterCapsuleSpaceOdds34)

    if spaceOdds34Max == 'cannonCapsuleSpaceOdds34':
        cannonCapsuleSpaceOdds34 += (100 - cannonCapsuleSpaceOdds34)

    if spaceOdds34Max == 'snackCapsuleSpaceOdds34':
        snackCapsuleSpaceOdds34 += (100 - snackCapsuleSpaceOdds34)

    if spaceOdds34Max == 'lakituCapsuleSpaceOdds34':
        lakituCapsuleSpaceOdds34 += (100 - lakituCapsuleSpaceOdds34)

    if spaceOdds34Max == 'hammerBroCapsuleSpaceOdds34':
        hammerBroCapsuleSpaceOdds34 += (100 - hammerBroCapsuleSpaceOdds34)

    if spaceOdds34Max == 'piranhaPlantCapsuleSpaceOdds34':
        piranhaPlantCapsuleSpaceOdds34 += (100 - piranhaPlantCapsuleSpaceOdds34)

    if spaceOdds34Max == 'spearGuyCapsuleSpaceOdds34':
        spearGuyCapsuleSpaceOdds34 += (100 - spearGuyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'kamekCapsuleSpaceOdds34':
        kamekCapsuleSpaceOdds34 += (100 - kamekCapsuleSpaceOdds34)

    if spaceOdds34Max == 'toadyCapsuleSpaceOdds34':
        toadyCapsuleSpaceOdds34 += (100 - toadyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'mrBlizzardCapsuleSpaceOdds34':
        mrBlizzardCapsuleSpaceOdds34 += (100 - mrBlizzardCapsuleSpaceOdds34)

    if spaceOdds34Max == 'banditCapsuleSpaceOdds34':
        banditCapsuleSpaceOdds34 += (100 - banditCapsuleSpaceOdds34)

    if spaceOdds34Max == 'pinkBooCapsuleSpaceOdds34':
        pinkBooCapsuleSpaceOdds34 += (100 - pinkBooCapsuleSpaceOdds34)

    if spaceOdds34Max == 'spinyCapsuleSpaceOdds34':
        spinyCapsuleSpaceOdds34 += (100 - spinyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'zapCapsuleSpaceOdds34':
        zapCapsuleSpaceOdds34 += (100 - zapCapsuleSpaceOdds34)

    if spaceOdds34Max == 'tweesterCapsuleSpaceOdds34':
        tweesterCapsuleSpaceOdds34 += (100 - tweesterCapsuleSpaceOdds34)

    if spaceOdds34Max == 'thwompCapsuleSpaceOdds34':
        thwompCapsuleSpaceOdds34 += (100 - thwompCapsuleSpaceOdds34)

    if spaceOdds34Max == 'warpCapsuleSpaceOdds34':
        warpCapsuleSpaceOdds34 += (100 - warpCapsuleSpaceOdds34)

    if spaceOdds34Max == 'bombCapsuleSpaceOdds34':
        bombCapsuleSpaceOdds34 += (100 - bombCapsuleSpaceOdds34)

    if spaceOdds34Max == 'fireballCapsuleSpaceOdds34':
        fireballCapsuleSpaceOdds34 += (100 - fireballCapsuleSpaceOdds34)

    if spaceOdds34Max == 'flowerCapsuleSpaceOdds34':
        flowerCapsuleSpaceOdds34 += (100 - flowerCapsuleSpaceOdds34)

    if spaceOdds34Max == 'eggCapsuleSpaceOdds34':
        eggCapsuleSpaceOdds34 += (100 - eggCapsuleSpaceOdds34)

    if spaceOdds34Max == 'vacuumCapsuleSpaceOdds34':
        vacuumCapsuleSpaceOdds34 += (100 - vacuumCapsuleSpaceOdds34)

    if spaceOdds34Max == 'magicCapsuleSpaceOdds34':
        magicCapsuleSpaceOdds34 += (100 - magicCapsuleSpaceOdds34)

    if spaceOdds34Max == 'tripleCapsuleSpaceOdds34':
        tripleCapsuleSpaceOdds34 += (100 - tripleCapsuleSpaceOdds34)

    if spaceOdds34Max == 'koopaCapsuleSpaceOdds34':
        koopaCapsuleSpaceOdds34 += (100 - koopaCapsuleSpaceOdds34)

    if spaceOdds34Max == 'mysteryCapsuleSpaceOdds34':
        mysteryCapsuleSpaceOdds34 += (100 - mysteryCapsuleSpaceOdds34)

    if spaceOdds34Max == 'duelCapsuleSpaceOdds34':
        duelCapsuleSpaceOdds34 += (100 - duelCapsuleSpaceOdds34)

    if spaceOdds34Max == 'dkCapsuleSpaceOdds34':
        dkCapsuleSpaceOdds34 += (100 - dkCapsuleSpaceOdds34)

    if spaceOdds34Max == 'orbBagCapsuleSpaceOdds34':
        orbBagCapsuleSpaceOdds34 += (100 - orbBagCapsuleSpaceOdds34)

    mushroomCapsuleShopOdds12 = str(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = str(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds12 = str(mushroomCapsuleSpaceOdds12)
    mushroomCapsuleSpaceOdds34 = str(mushroomCapsuleSpaceOdds34)
    goldenMushroomCapsuleShopOdds12 = str(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = str(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds12 = str(goldenMushroomCapsuleSpaceOdds12)
    goldenMushroomCapsuleSpaceOdds34 = str(goldenMushroomCapsuleSpaceOdds34)
    slowMushroomCapsuleShopOdds12 = str(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = str(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds12 = str(slowMushroomCapsuleSpaceOdds12)
    slowMushroomCapsuleSpaceOdds34 = str(slowMushroomCapsuleSpaceOdds34)
    metalMushroomCapsuleShopOdds12 = str(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = str(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds12 = str(metalMushroomCapsuleSpaceOdds12)
    metalMushroomCapsuleSpaceOdds34 = str(metalMushroomCapsuleSpaceOdds34)
    flutterCapsuleShopOdds12 = str(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = str(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds12 = str(flutterCapsuleSpaceOdds12)
    flutterCapsuleSpaceOdds34 = str(flutterCapsuleSpaceOdds34)
    cannonCapsuleShopOdds12 = str(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = str(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds12 = str(cannonCapsuleSpaceOdds12)
    cannonCapsuleSpaceOdds34 = str(cannonCapsuleSpaceOdds34)
    snackCapsuleShopOdds12 = str(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = str(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds12 = str(snackCapsuleSpaceOdds12)
    snackCapsuleSpaceOdds34 = str(snackCapsuleSpaceOdds34)
    lakituCapsuleShopOdds12 = str(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = str(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds12 = str(lakituCapsuleSpaceOdds12)
    lakituCapsuleSpaceOdds34 = str(lakituCapsuleSpaceOdds34)
    hammerBroCapsuleShopOdds12 = str(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = str(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds12 = str(hammerBroCapsuleSpaceOdds12)
    hammerBroCapsuleSpaceOdds34 = str(hammerBroCapsuleSpaceOdds34)
    piranhaPlantCapsuleShopOdds12 = str(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = str(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds12 = str(piranhaPlantCapsuleSpaceOdds12)
    piranhaPlantCapsuleSpaceOdds34 = str(piranhaPlantCapsuleSpaceOdds34)
    spearGuyCapsuleShopOdds12 = str(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = str(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds12 = str(spearGuyCapsuleSpaceOdds12)
    spearGuyCapsuleSpaceOdds34 = str(spearGuyCapsuleSpaceOdds34)
    kamekCapsuleShopOdds12 = str(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = str(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds12 = str(kamekCapsuleSpaceOdds12)
    kamekCapsuleSpaceOdds34 = str(kamekCapsuleSpaceOdds34)
    toadyCapsuleShopOdds12 = str(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = str(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds12 = str(toadyCapsuleSpaceOdds12)
    toadyCapsuleSpaceOdds34 = str(toadyCapsuleSpaceOdds34)
    mrBlizzardCapsuleShopOdds12 = str(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = str(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds12 = str(mrBlizzardCapsuleSpaceOdds12)
    mrBlizzardCapsuleSpaceOdds34 = str(mrBlizzardCapsuleSpaceOdds34)
    banditCapsuleShopOdds12 = str(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = str(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds12 = str(banditCapsuleSpaceOdds12)
    banditCapsuleSpaceOdds34 = str(banditCapsuleSpaceOdds34)
    pinkBooCapsuleShopOdds12 = str(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = str(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds12 = str(pinkBooCapsuleSpaceOdds12)
    pinkBooCapsuleSpaceOdds34 = str(pinkBooCapsuleSpaceOdds34)
    spinyCapsuleShopOdds12 = str(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = str(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds12 = str(spinyCapsuleSpaceOdds12)
    spinyCapsuleSpaceOdds34 = str(spinyCapsuleSpaceOdds34)
    zapCapsuleShopOdds12 = str(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = str(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds12 = str(zapCapsuleSpaceOdds12)
    zapCapsuleSpaceOdds34 = str(zapCapsuleSpaceOdds34)
    tweesterCapsuleShopOdds12 = str(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = str(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds12 = str(tweesterCapsuleSpaceOdds12)
    tweesterCapsuleSpaceOdds34 = str(tweesterCapsuleSpaceOdds34)
    thwompCapsuleShopOdds12 = str(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = str(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds12 = str(thwompCapsuleSpaceOdds12)
    thwompCapsuleSpaceOdds34 = str(thwompCapsuleSpaceOdds34)
    warpCapsuleShopOdds12 = str(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = str(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds12 = str(warpCapsuleSpaceOdds12)
    warpCapsuleSpaceOdds34 = str(warpCapsuleSpaceOdds34)
    bombCapsuleShopOdds12 = str(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = str(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds12 = str(bombCapsuleSpaceOdds12)
    bombCapsuleSpaceOdds34 = str(bombCapsuleSpaceOdds34)
    fireballCapsuleShopOdds12 = str(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = str(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds12 = str(fireballCapsuleSpaceOdds12)
    fireballCapsuleSpaceOdds34 = str(fireballCapsuleSpaceOdds34)
    flowerCapsuleShopOdds12 = str(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = str(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds12 = str(flowerCapsuleSpaceOdds12)
    flowerCapsuleSpaceOdds34 = str(flowerCapsuleSpaceOdds34)
    eggCapsuleShopOdds12 = str(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = str(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds12 = str(eggCapsuleSpaceOdds12)
    eggCapsuleSpaceOdds34 = str(eggCapsuleSpaceOdds34)
    vacuumCapsuleShopOdds12 = str(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = str(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds12 = str(vacuumCapsuleSpaceOdds12)
    vacuumCapsuleSpaceOdds34 = str(vacuumCapsuleSpaceOdds34)
    magicCapsuleShopOdds12 = str(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = str(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds12 = str(magicCapsuleSpaceOdds12)
    magicCapsuleSpaceOdds34 = str(magicCapsuleSpaceOdds34)
    tripleCapsuleShopOdds12 = str(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = str(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds12 = str(tripleCapsuleSpaceOdds12)
    tripleCapsuleSpaceOdds34 = str(tripleCapsuleSpaceOdds34)
    koopaCapsuleShopOdds12 = str(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = str(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds12 = str(koopaCapsuleSpaceOdds12)
    koopaCapsuleSpaceOdds34 = str(koopaCapsuleSpaceOdds34)
    poisonMushroomShopOdds12 = str(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = str(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds12 = str(poisonMushroomSpaceOdds12)
    poisonMushroomSpaceOdds34 = str(poisonMushroomSpaceOdds34)
    orbBagCapsuleShopOdds12 = str(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = str(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds12 = str(orbBagCapsuleSpaceOdds12)
    orbBagCapsuleSpaceOdds34 = str(orbBagCapsuleSpaceOdds34)
    mysteryCapsuleShopOdds12 = str(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = str(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds12 = str(mysteryCapsuleSpaceOdds12)
    mysteryCapsuleSpaceOdds34 = str(mysteryCapsuleSpaceOdds34)
    dkCapsuleShopOdds12 = str(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = str(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds12 = str(dkCapsuleSpaceOdds12)
    dkCapsuleSpaceOdds34 = str(dkCapsuleSpaceOdds34)
    duelCapsuleShopOdds12 = str(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = str(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds12 = str(duelCapsuleSpaceOdds12)
    duelCapsuleSpaceOdds34 = str(duelCapsuleSpaceOdds34)

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
    mushroomCapsuleShopOdds12 = convert_to_hex_weight(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = convert_to_hex_weight(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds12 = convert_to_hex_weight(mushroomCapsuleSpaceOdds12)
    mushroomCapsuleSpaceOdds34 = convert_to_hex_weight(mushroomCapsuleSpaceOdds34)
    goldenMushroomCapsulePrice12 = convert_to_hex_weight(goldenMushroomCapsulePrice12)
    goldenMushroomCapsulePrice34 = convert_to_hex_weight(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = convert_to_hex_weight(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = convert_to_hex_weight(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds12 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds12)
    goldenMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds34)
    slowMushroomCapsulePrice12 = convert_to_hex_weight(slowMushroomCapsulePrice12)
    slowMushroomCapsulePrice34 = convert_to_hex_weight(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = convert_to_hex_weight(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = convert_to_hex_weight(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds12 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds12)
    slowMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds34)
    metalMushroomCapsulePrice12 = convert_to_hex_weight(metalMushroomCapsulePrice12)
    metalMushroomCapsulePrice34 = convert_to_hex_weight(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = convert_to_hex_weight(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = convert_to_hex_weight(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds12 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds12)
    metalMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds34)
    flutterCapsulePrice12 = convert_to_hex_weight(flutterCapsulePrice12)
    flutterCapsulePrice34 = convert_to_hex_weight(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = convert_to_hex_weight(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = convert_to_hex_weight(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds12 = convert_to_hex_weight(flutterCapsuleSpaceOdds12)
    flutterCapsuleSpaceOdds34 = convert_to_hex_weight(flutterCapsuleSpaceOdds34)
    cannonCapsulePrice12 = convert_to_hex_weight(cannonCapsulePrice12)
    cannonCapsulePrice34 = convert_to_hex_weight(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = convert_to_hex_weight(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = convert_to_hex_weight(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds12 = convert_to_hex_weight(cannonCapsuleSpaceOdds12)
    cannonCapsuleSpaceOdds34 = convert_to_hex_weight(cannonCapsuleSpaceOdds34)
    snackCapsulePrice12 = convert_to_hex_weight(snackCapsulePrice12)
    snackCapsulePrice34 = convert_to_hex_weight(snackCapsulePrice34)
    snackCapsuleShopOdds12 = convert_to_hex_weight(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = convert_to_hex_weight(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds12 = convert_to_hex_weight(snackCapsuleSpaceOdds12)
    snackCapsuleSpaceOdds34 = convert_to_hex_weight(snackCapsuleSpaceOdds34)
    lakituCapsulePrice12 = convert_to_hex_weight(lakituCapsulePrice12)
    lakituCapsulePrice34 = convert_to_hex_weight(lakituCapsulePrice34)
    lakituCapsuleShopOdds12 = convert_to_hex_weight(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = convert_to_hex_weight(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds12 = convert_to_hex_weight(lakituCapsuleSpaceOdds12)
    lakituCapsuleSpaceOdds34 = convert_to_hex_weight(lakituCapsuleSpaceOdds34)
    hammerBroCapsulePrice12 = convert_to_hex_weight(hammerBroCapsulePrice12)
    hammerBroCapsulePrice34 = convert_to_hex_weight(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = convert_to_hex_weight(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = convert_to_hex_weight(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds12 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds12)
    hammerBroCapsuleSpaceOdds34 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds34)
    piranhaPlantCapsulePrice12 = convert_to_hex_weight(piranhaPlantCapsulePrice12)
    piranhaPlantCapsulePrice34 = convert_to_hex_weight(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = convert_to_hex_weight(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = convert_to_hex_weight(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds12 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds12)
    piranhaPlantCapsuleSpaceOdds34 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds34)
    spearGuyCapsulePrice12 = convert_to_hex_weight(spearGuyCapsulePrice12)
    spearGuyCapsulePrice34 = convert_to_hex_weight(spearGuyCapsulePrice34)
    spearGuyCapsuleShopOdds12 = convert_to_hex_weight(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = convert_to_hex_weight(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds12 = convert_to_hex_weight(spearGuyCapsuleSpaceOdds12)
    spearGuyCapsuleSpaceOdds34 = convert_to_hex_weight(spearGuyCapsuleSpaceOdds34)
    kamekCapsulePrice12 = convert_to_hex_weight(kamekCapsulePrice12)
    kamekCapsulePrice34 = convert_to_hex_weight(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = convert_to_hex_weight(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = convert_to_hex_weight(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds12 = convert_to_hex_weight(kamekCapsuleSpaceOdds12)
    kamekCapsuleSpaceOdds34 = convert_to_hex_weight(kamekCapsuleSpaceOdds34)
    toadyCapsulePrice12 = convert_to_hex_weight(toadyCapsulePrice12)
    toadyCapsulePrice34 = convert_to_hex_weight(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = convert_to_hex_weight(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = convert_to_hex_weight(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds12 = convert_to_hex_weight(toadyCapsuleSpaceOdds12)
    toadyCapsuleSpaceOdds34 = convert_to_hex_weight(toadyCapsuleSpaceOdds34)
    mrBlizzardCapsulePrice12 = convert_to_hex_weight(mrBlizzardCapsulePrice12)
    mrBlizzardCapsulePrice34 = convert_to_hex_weight(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = convert_to_hex_weight(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = convert_to_hex_weight(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds12 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds12)
    mrBlizzardCapsuleSpaceOdds34 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds34)
    banditCapsulePrice12 = convert_to_hex_weight(banditCapsulePrice12)
    banditCapsulePrice34 = convert_to_hex_weight(banditCapsulePrice34)
    banditCapsuleShopOdds12 = convert_to_hex_weight(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = convert_to_hex_weight(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds12 = convert_to_hex_weight(banditCapsuleSpaceOdds12)
    banditCapsuleSpaceOdds34 = convert_to_hex_weight(banditCapsuleSpaceOdds34)
    pinkBooCapsulePrice12 = convert_to_hex_weight(pinkBooCapsulePrice12)
    pinkBooCapsulePrice34 = convert_to_hex_weight(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = convert_to_hex_weight(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = convert_to_hex_weight(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds12 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds12)
    pinkBooCapsuleSpaceOdds34 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds34)
    spinyCapsulePrice12 = convert_to_hex_weight(spinyCapsulePrice12)
    spinyCapsulePrice34 = convert_to_hex_weight(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = convert_to_hex_weight(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = convert_to_hex_weight(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds12 = convert_to_hex_weight(spinyCapsuleSpaceOdds12)
    spinyCapsuleSpaceOdds34 = convert_to_hex_weight(spinyCapsuleSpaceOdds34)
    zapCapsulePrice12 = convert_to_hex_weight(zapCapsulePrice12)
    zapCapsulePrice34 = convert_to_hex_weight(zapCapsulePrice34)
    zapCapsuleShopOdds12 = convert_to_hex_weight(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = convert_to_hex_weight(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds12 = convert_to_hex_weight(zapCapsuleSpaceOdds12)
    zapCapsuleSpaceOdds34 = convert_to_hex_weight(zapCapsuleSpaceOdds34)
    tweesterCapsulePrice12 = convert_to_hex_weight(tweesterCapsulePrice12)
    tweesterCapsulePrice34 = convert_to_hex_weight(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = convert_to_hex_weight(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = convert_to_hex_weight(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds12 = convert_to_hex_weight(tweesterCapsuleSpaceOdds12)
    tweesterCapsuleSpaceOdds34 = convert_to_hex_weight(tweesterCapsuleSpaceOdds34)
    thwompCapsulePrice12 = convert_to_hex_weight(thwompCapsulePrice12)
    thwompCapsulePrice34 = convert_to_hex_weight(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = convert_to_hex_weight(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = convert_to_hex_weight(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds12 = convert_to_hex_weight(thwompCapsuleSpaceOdds12)
    thwompCapsuleSpaceOdds34 = convert_to_hex_weight(thwompCapsuleSpaceOdds34)
    warpCapsulePrice12 = convert_to_hex_weight(warpCapsulePrice12)
    warpCapsulePrice34 = convert_to_hex_weight(warpCapsulePrice34)
    warpCapsuleShopOdds12 = convert_to_hex_weight(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = convert_to_hex_weight(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds12 = convert_to_hex_weight(warpCapsuleSpaceOdds12)
    warpCapsuleSpaceOdds34 = convert_to_hex_weight(warpCapsuleSpaceOdds34)
    bombCapsulePrice12 = convert_to_hex_weight(bombCapsulePrice12)
    bombCapsulePrice34 = convert_to_hex_weight(bombCapsulePrice34)
    bombCapsuleShopOdds12 = convert_to_hex_weight(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = convert_to_hex_weight(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds12 = convert_to_hex_weight(bombCapsuleSpaceOdds12)
    bombCapsuleSpaceOdds34 = convert_to_hex_weight(bombCapsuleSpaceOdds34)
    fireballCapsulePrice12 = convert_to_hex_weight(fireballCapsulePrice12)
    fireballCapsulePrice34 = convert_to_hex_weight(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = convert_to_hex_weight(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = convert_to_hex_weight(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds12 = convert_to_hex_weight(fireballCapsuleSpaceOdds12)
    fireballCapsuleSpaceOdds34 = convert_to_hex_weight(fireballCapsuleSpaceOdds34)
    flowerCapsulePrice12 = convert_to_hex_weight(flowerCapsulePrice12)
    flowerCapsulePrice34 = convert_to_hex_weight(flowerCapsulePrice34)
    flowerCapsuleShopOdds12 = convert_to_hex_weight(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = convert_to_hex_weight(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds12 = convert_to_hex_weight(flowerCapsuleSpaceOdds12)
    flowerCapsuleSpaceOdds34 = convert_to_hex_weight(flowerCapsuleSpaceOdds34)
    eggCapsulePrice12 = convert_to_hex_weight(eggCapsulePrice12)
    eggCapsulePrice34 = convert_to_hex_weight(eggCapsulePrice34)
    eggCapsuleShopOdds12 = convert_to_hex_weight(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = convert_to_hex_weight(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds12 = convert_to_hex_weight(eggCapsuleSpaceOdds12)
    eggCapsuleSpaceOdds34 = convert_to_hex_weight(eggCapsuleSpaceOdds34)
    vacuumCapsulePrice12 = convert_to_hex_weight(vacuumCapsulePrice12)
    vacuumCapsulePrice34 = convert_to_hex_weight(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = convert_to_hex_weight(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = convert_to_hex_weight(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds12 = convert_to_hex_weight(vacuumCapsuleSpaceOdds12)
    vacuumCapsuleSpaceOdds34 = convert_to_hex_weight(vacuumCapsuleSpaceOdds34)
    magicCapsulePrice12 = convert_to_hex_weight(magicCapsulePrice12)
    magicCapsulePrice34 = convert_to_hex_weight(magicCapsulePrice34)
    magicCapsuleShopOdds12 = convert_to_hex_weight(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = convert_to_hex_weight(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds12 = convert_to_hex_weight(magicCapsuleSpaceOdds12)
    magicCapsuleSpaceOdds34 = convert_to_hex_weight(magicCapsuleSpaceOdds34)
    tripleCapsulePrice12 = convert_to_hex_weight(tripleCapsulePrice12)
    tripleCapsulePrice34 = convert_to_hex_weight(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = convert_to_hex_weight(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = convert_to_hex_weight(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds12 = convert_to_hex_weight(tripleCapsuleSpaceOdds12)
    tripleCapsuleSpaceOdds34 = convert_to_hex_weight(tripleCapsuleSpaceOdds34)
    koopaCapsulePrice12 = convert_to_hex_weight(koopaCapsulePrice12)
    koopaCapsulePrice34 = convert_to_hex_weight(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = convert_to_hex_weight(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = convert_to_hex_weight(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds12 = convert_to_hex_weight(koopaCapsuleSpaceOdds12)
    koopaCapsuleSpaceOdds34 = convert_to_hex_weight(koopaCapsuleSpaceOdds34)
    poisonMushroomPrice12 = convert_to_hex_weight(poisonMushroomPrice12)
    poisonMushroomPrice34 = convert_to_hex_weight(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = convert_to_hex_weight(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = convert_to_hex_weight(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds12 = convert_to_hex_weight(poisonMushroomSpaceOdds12)
    poisonMushroomSpaceOdds34 = convert_to_hex_weight(poisonMushroomSpaceOdds34)
    orbBagCapsulePrice12 = convert_to_hex_weight(orbBagCapsulePrice12)
    orbBagCapsulePrice34 = convert_to_hex_weight(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = convert_to_hex_weight(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = convert_to_hex_weight(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds12 = convert_to_hex_weight(orbBagCapsuleSpaceOdds12)
    orbBagCapsuleSpaceOdds34 = convert_to_hex_weight(orbBagCapsuleSpaceOdds34)
    mysteryCapsulePrice12 = convert_to_hex_weight(mysteryCapsulePrice12)
    mysteryCapsulePrice34 = convert_to_hex_weight(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = convert_to_hex_weight(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = convert_to_hex_weight(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds12 = convert_to_hex_weight(mysteryCapsuleSpaceOdds12)
    mysteryCapsuleSpaceOdds34 = convert_to_hex_weight(mysteryCapsuleSpaceOdds34)
    dkCapsulePrice12 = convert_to_hex_weight(dkCapsulePrice12)
    dkCapsulePrice34 = convert_to_hex_weight(dkCapsulePrice34)
    dkCapsuleShopOdds12 = convert_to_hex_weight(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = convert_to_hex_weight(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds12 = convert_to_hex_weight(dkCapsuleSpaceOdds12)
    dkCapsuleSpaceOdds34 = convert_to_hex_weight(dkCapsuleSpaceOdds34)
    duelCapsulePrice12 = convert_to_hex_weight(duelCapsulePrice12)
    duelCapsulePrice34 = convert_to_hex_weight(duelCapsulePrice34)
    duelCapsuleShopOdds12 = convert_to_hex_weight(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = convert_to_hex_weight(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds12 = convert_to_hex_weight(duelCapsuleSpaceOdds12)
    duelCapsuleSpaceOdds34 = convert_to_hex_weight(duelCapsuleSpaceOdds34)

    generatedCode = getOrbModsSeven(mushroomCapsulePrice12, mushroomCapsulePrice34, mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34, mushroomCapsuleSpaceOdds12, mushroomCapsuleSpaceOdds34, goldenMushroomCapsulePrice12, goldenMushroomCapsulePrice34, goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, goldenMushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds34, slowMushroomCapsulePrice12, slowMushroomCapsulePrice34, slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, slowMushroomCapsuleSpaceOdds12, slowMushroomCapsuleSpaceOdds34, metalMushroomCapsulePrice12, metalMushroomCapsulePrice34, metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, metalMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds34, flutterCapsulePrice12, flutterCapsulePrice34, flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, flutterCapsuleSpaceOdds12, flutterCapsuleSpaceOdds34, cannonCapsulePrice12, cannonCapsulePrice34, cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, cannonCapsuleSpaceOdds12, cannonCapsuleSpaceOdds34, snackCapsulePrice12, snackCapsulePrice34, snackCapsuleShopOdds12, snackCapsuleShopOdds34, snackCapsuleSpaceOdds12, snackCapsuleSpaceOdds34, lakituCapsulePrice12, lakituCapsulePrice34, lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, lakituCapsuleSpaceOdds12, lakituCapsuleSpaceOdds34, hammerBroCapsulePrice12, hammerBroCapsulePrice34, hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, hammerBroCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds34, piranhaPlantCapsulePrice12, piranhaPlantCapsulePrice34, piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, piranhaPlantCapsuleSpaceOdds12, piranhaPlantCapsuleSpaceOdds34, spearGuyCapsulePrice12, spearGuyCapsulePrice34, spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, spearGuyCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds34, kamekCapsulePrice12, kamekCapsulePrice34, kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, kamekCapsuleSpaceOdds12, kamekCapsuleSpaceOdds34, toadyCapsulePrice12, toadyCapsulePrice34, toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, toadyCapsuleSpaceOdds12, toadyCapsuleSpaceOdds34, mrBlizzardCapsulePrice12, mrBlizzardCapsulePrice34, mrBlizzardCapsuleShopOdds12, mrBlizzardCapsulePrice34, mrBlizzardCapsuleSpaceOdds12, mrBlizzardCapsulePrice34, banditCapsulePrice12, banditCapsulePrice34, banditCapsuleShopOdds12, banditCapsuleShopOdds34, banditCapsuleSpaceOdds12, banditCapsuleSpaceOdds34, pinkBooCapsulePrice12, pinkBooCapsulePrice34, pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, pinkBooCapsuleSpaceOdds12, pinkBooCapsuleSpaceOdds34, spinyCapsulePrice12, spinyCapsulePrice34, spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, spinyCapsuleSpaceOdds12, spinyCapsuleSpaceOdds34, zapCapsulePrice12, zapCapsulePrice34, zapCapsuleShopOdds12, zapCapsuleShopOdds34, zapCapsuleSpaceOdds12, zapCapsuleSpaceOdds34, tweesterCapsulePrice12, tweesterCapsulePrice34, tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, tweesterCapsuleSpaceOdds12, tweesterCapsuleSpaceOdds34, thwompCapsulePrice12, thwompCapsulePrice34, thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, thwompCapsuleSpaceOdds12, thwompCapsuleSpaceOdds34, warpCapsulePrice12, warpCapsulePrice34, warpCapsuleShopOdds12, warpCapsuleShopOdds34, warpCapsuleSpaceOdds12, warpCapsuleSpaceOdds34, bombCapsulePrice12, bombCapsulePrice34, bombCapsuleShopOdds12, bombCapsuleShopOdds34, bombCapsuleSpaceOdds12, bombCapsuleSpaceOdds34, fireballCapsulePrice12, fireballCapsulePrice34, fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, fireballCapsuleSpaceOdds12, fireballCapsuleSpaceOdds34, flowerCapsulePrice12, flowerCapsulePrice34, flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, flowerCapsuleSpaceOdds12, flowerCapsuleSpaceOdds34, eggCapsulePrice12, eggCapsulePrice34, eggCapsuleShopOdds12, eggCapsuleShopOdds34, eggCapsuleSpaceOdds12, eggCapsuleSpaceOdds34, vacuumCapsulePrice12, vacuumCapsulePrice34, vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, vacuumCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds34, magicCapsulePrice12, magicCapsulePrice34, magicCapsuleShopOdds12, magicCapsuleShopOdds34, magicCapsuleSpaceOdds12, magicCapsuleSpaceOdds34, tripleCapsulePrice12, tripleCapsulePrice34, tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, tripleCapsuleSpaceOdds12, tripleCapsuleSpaceOdds34, koopaCapsulePrice12, koopaCapsulePrice34, koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, koopaCapsuleSpaceOdds12, koopaCapsuleSpaceOdds34, poisonMushroomPrice34, poisonMushroomPrice12, poisonMushroomShopOdds12, poisonMushroomShopOdds34, poisonMushroomSpaceOdds12, poisonMushroomSpaceOdds34, orbBagCapsulePrice34, orbBagCapsulePrice12, orbBagCapsuleShopOdds12, orbBagCapsuleShopOdds34, orbBagCapsuleSpaceOdds12, orbBagCapsuleSpaceOdds34, mysteryCapsulePrice34, mysteryCapsulePrice12, mysteryCapsuleShopOdds12, mysteryCapsuleShopOdds34, mysteryCapsuleSpaceOdds12, mysteryCapsuleSpaceOdds34, dkCapsulePrice34, dkCapsulePrice12, dkCapsuleShopOdds12, dkCapsuleShopOdds34, dkCapsuleSpaceOdds12, dkCapsuleSpaceOdds34, duelCapsulePrice34, duelCapsulePrice12, duelCapsuleShopOdds12, duelCapsuleShopOdds34, duelCapsuleSpaceOdds12, duelCapsuleSpaceOdds34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def savePresetItems7(mushroomCapsuleShopOdds12 = "0", mushroomCapsuleShopOdds34 = "0", mushroomCapsuleSpaceOdds12 = "0", mushroomCapsuleSpaceOdds34 = "0", goldenMushroomCapsulePrice12 = "0", goldenMushroomCapsulePrice34 = "0", goldenMushroomCapsuleShopOdds12 = "0", goldenMushroomCapsuleShopOdds34 = "0", goldenMushroomCapsuleSpaceOdds12 = "0", goldenMushroomCapsuleSpaceOdds34 = "0", slowMushroomCapsulePrice12 = "0", slowMushroomCapsulePrice34 = "0", slowMushroomCapsuleShopOdds12 = "0", slowMushroomCapsuleShopOdds34 = "0", slowMushroomCapsuleSpaceOdds12 = "0", slowMushroomCapsuleSpaceOdds34 = "0", metalMushroomCapsulePrice12 = "0", metalMushroomCapsulePrice34 = "0", metalMushroomCapsuleShopOdds12 = "0", metalMushroomCapsuleShopOdds34 = "0", metalMushroomCapsuleSpaceOdds12 = "0", metalMushroomCapsuleSpaceOdds34 = "0", flutterCapsulePrice12 = "0", flutterCapsulePrice34 = "0", flutterCapsuleShopOdds12 = "0", flutterCapsuleShopOdds34 = "0", flutterCapsuleSpaceOdds12 = "0", flutterCapsuleSpaceOdds34 = "0", cannonCapsulePrice12 = "0", cannonCapsulePrice34 = "0", cannonCapsuleShopOdds12 = "0", cannonCapsuleShopOdds34 = "0", cannonCapsuleSpaceOdds12 = "0", cannonCapsuleSpaceOdds34 = "0", snackCapsulePrice12 = "0", snackCapsulePrice34 = "0", snackCapsuleShopOdds12 = "0", snackCapsuleShopOdds34 = "0", snackCapsuleSpaceOdds12 = "0", snackCapsuleSpaceOdds34 = "0", lakituCapsulePrice12 = "0", lakituCapsulePrice34 = "0", lakituCapsuleShopOdds12 = "0", lakituCapsuleShopOdds34 = "0", lakituCapsuleSpaceOdds12 = "0", lakituCapsuleSpaceOdds34 = "0", hammerBroCapsulePrice12 = "0", hammerBroCapsulePrice34 = "0", hammerBroCapsuleShopOdds12 = "0", hammerBroCapsuleShopOdds34 = "0", hammerBroCapsuleSpaceOdds12 = "0", hammerBroCapsuleSpaceOdds34 = "0", piranhaPlantCapsulePrice12 = "0", piranhaPlantCapsulePrice34 = "0", piranhaPlantCapsuleShopOdds12 = "0", piranhaPlantCapsuleShopOdds34 = "0", piranhaPlantCapsuleSpaceOdds12 = "0", piranhaPlantCapsuleSpaceOdds34 = "0", spearGuyCapsulePrice12 = "0", spearGuyCapsulePrice34 = "0", spearGuyCapsuleShopOdds12 = "0", spearGuyCapsuleShopOdds34 = "0", spearGuyCapsuleSpaceOdds12 = "0", spearGuyCapsuleSpaceOdds34 = "0", kamekCapsulePrice12 = "0", kamekCapsulePrice34 = "0", kamekCapsuleShopOdds12 = "0", kamekCapsuleShopOdds34 = "0", kamekCapsuleSpaceOdds12 = "0", kamekCapsuleSpaceOdds34 = "0", toadyCapsulePrice12 = "0", toadyCapsulePrice34 = "0", toadyCapsuleShopOdds12 = "0", toadyCapsuleShopOdds34 = "0", toadyCapsuleSpaceOdds12 = "0", toadyCapsuleSpaceOdds34 = "0", mrBlizzardCapsulePrice12 = "0", mrBlizzardCapsulePrice34 = "0", mrBlizzardCapsuleShopOdds12 = "0", mrBlizzardCapsuleShopOdds34 = "0", mrBlizzardCapsuleSpaceOdds12 = "0", mrBlizzardCapsuleSpaceOdds34 = "0", banditCapsulePrice12 = "0", banditCapsulePrice34 = "0", banditCapsuleShopOdds12 = "0", banditCapsuleShopOdds34 = "0", banditCapsuleSpaceOdds12 = "0", banditCapsuleSpaceOdds34 = "0", pinkBooCapsulePrice12 = "0", pinkBooCapsulePrice34 = "0", pinkBooCapsuleShopOdds12 = "0", pinkBooCapsuleShopOdds34 = "0", pinkBooCapsuleSpaceOdds12 = "0", pinkBooCapsuleSpaceOdds34 = "0", spinyCapsulePrice12 = "0", spinyCapsulePrice34 = "0", spinyCapsuleShopOdds12 = "0", spinyCapsuleShopOdds34 = "0", spinyCapsuleSpaceOdds12 = "0", spinyCapsuleSpaceOdds34 = "0", zapCapsulePrice12 = "0", zapCapsulePrice34 = "0", zapCapsuleShopOdds12 = "0", zapCapsuleShopOdds34 = "0", zapCapsuleSpaceOdds12 = "0", zapCapsuleSpaceOdds34 = "0", tweesterCapsulePrice12 = "0", tweesterCapsulePrice34 = "0", tweesterCapsuleShopOdds12 = "0", tweesterCapsuleShopOdds34 = "0", tweesterCapsuleSpaceOdds12 = "0", tweesterCapsuleSpaceOdds34 = "0", thwompCapsulePrice12 = "0", thwompCapsulePrice34 = "0", thwompCapsuleShopOdds12 = "0", thwompCapsuleShopOdds34 = "0", thwompCapsuleSpaceOdds12 = "0", thwompCapsuleSpaceOdds34 = "0", warpCapsulePrice12 = "0", warpCapsulePrice34 = "0", warpCapsuleShopOdds12 = "0", warpCapsuleShopOdds34 = "0", warpCapsuleSpaceOdds12 = "0", warpCapsuleSpaceOdds34 = "0", bombCapsulePrice12 = "0", bombCapsulePrice34 = "0", bombCapsuleShopOdds12 = "0", bombCapsuleShopOdds34 = "0", bombCapsuleSpaceOdds12 = "0", bombCapsuleSpaceOdds34 = "0", fireballCapsulePrice12 = "0", fireballCapsulePrice34 = "0", fireballCapsuleShopOdds12 = "0", fireballCapsuleShopOdds34 = "0", fireballCapsuleSpaceOdds12 = "0", fireballCapsuleSpaceOdds34 = "0", flowerCapsulePrice12 = "0", flowerCapsulePrice34 = "0", flowerCapsuleShopOdds12 = "0", flowerCapsuleShopOdds34 = "0", flowerCapsuleSpaceOdds12 = "0", flowerCapsuleSpaceOdds34 = "0", eggCapsulePrice12 = "0", eggCapsulePrice34 = "0", eggCapsuleShopOdds12 = "0", eggCapsuleShopOdds34 = "0", eggCapsuleSpaceOdds12 = "0", eggCapsuleSpaceOdds34 = "0", vacuumCapsulePrice12 = "0", vacuumCapsulePrice34 = "0", vacuumCapsuleShopOdds12 = "0", vacuumCapsuleShopOdds34 = "0", vacuumCapsuleSpaceOdds12 = "0", vacuumCapsuleSpaceOdds34 = "0", magicCapsulePrice12 = "0", magicCapsulePrice34 = "0", magicCapsuleShopOdds12 = "0", magicCapsuleShopOdds34 = "0", magicCapsuleSpaceOdds12 = "0", magicCapsuleSpaceOdds34 = "0", tripleCapsulePrice12 = "0", tripleCapsulePrice34 = "0", tripleCapsuleShopOdds12 = "0", tripleCapsuleShopOdds34 = "0", tripleCapsuleSpaceOdds12 = "0", tripleCapsuleSpaceOdds34 = "0", koopaCapsulePrice12 = "0", koopaCapsulePrice34 = "0", koopaCapsuleShopOdds12 = "0", koopaCapsuleShopOdds34 = "0", koopaCapsuleSpaceOdds12 = "0", koopaCapsuleSpaceOdds34 = "0", poisonMushroomPrice34 = "0", poisonMushroomPrice12 = "0", poisonMushroomShopOdds12 = "0", poisonMushroomShopOdds34 = "0", poisonMushroomSpaceOdds12 = "0", poisonMushroomSpaceOdds34 = "0", orbBagCapsulePrice34 = "0", orbBagCapsulePrice12 = "0", orbBagCapsuleShopOdds12 = "0", orbBagCapsuleShopOdds34 = "0", orbBagCapsuleSpaceOdds12 = "0", orbBagCapsuleSpaceOdds34 = "0", mysteryCapsulePrice34 = "0", mysteryCapsulePrice12 = "0", mysteryCapsuleShopOdds12 = "0", mysteryCapsuleShopOdds34 = "0", mysteryCapsuleSpaceOdds12 = "0", mysteryCapsuleSpaceOdds34 = "0", dkCapsulePrice34 = "0", dkCapsulePrice12 = "0", dkCapsuleShopOdds12 = "0", dkCapsuleShopOdds34 = "0", dkCapsuleSpaceOdds12 = "0", dkCapsuleSpaceOdds34 = "0", duelCapsulePrice34 = "0", duelCapsulePrice12 = "0", duelCapsuleShopOdds12 = "0", duelCapsuleShopOdds34 = "0", duelCapsuleSpaceOdds12 = "0", duelCapsuleSpaceOdds34 = "0"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    mushroomCapsulePrice12 = "5"
    mushroomCapsulePrice34 = "5"
    mushroomCapsuleShopOdds12 = get_capsule_value(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = get_capsule_value(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds12 = get_capsule_value(mushroomCapsuleSpaceOdds12)
    mushroomCapsuleSpaceOdds34 = get_capsule_value(mushroomCapsuleSpaceOdds34)
    goldenMushroomCapsulePrice12 = get_capsule_value(goldenMushroomCapsulePrice12)
    goldenMushroomCapsulePrice34 = get_capsule_value(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = get_capsule_value(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = get_capsule_value(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds12 = get_capsule_value(goldenMushroomCapsuleSpaceOdds12)
    goldenMushroomCapsuleSpaceOdds34 = get_capsule_value(goldenMushroomCapsuleSpaceOdds34)
    slowMushroomCapsulePrice12 = get_capsule_value(slowMushroomCapsulePrice12)
    slowMushroomCapsulePrice34 = get_capsule_value(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = get_capsule_value(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = get_capsule_value(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds12 = get_capsule_value(slowMushroomCapsuleSpaceOdds12)
    slowMushroomCapsuleSpaceOdds34 = get_capsule_value(slowMushroomCapsuleSpaceOdds34)
    metalMushroomCapsulePrice12 = get_capsule_value(metalMushroomCapsulePrice12)
    metalMushroomCapsulePrice34 = get_capsule_value(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = get_capsule_value(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = get_capsule_value(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds12 = get_capsule_value(metalMushroomCapsuleSpaceOdds12)
    metalMushroomCapsuleSpaceOdds34 = get_capsule_value(metalMushroomCapsuleSpaceOdds34)
    flutterCapsulePrice12 = get_capsule_value(flutterCapsulePrice12)
    flutterCapsulePrice34 = get_capsule_value(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = get_capsule_value(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = get_capsule_value(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds12 = get_capsule_value(flutterCapsuleSpaceOdds12)
    flutterCapsuleSpaceOdds34 = get_capsule_value(flutterCapsuleSpaceOdds34)
    cannonCapsulePrice12 = get_capsule_value(cannonCapsulePrice12)
    cannonCapsulePrice34 = get_capsule_value(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = get_capsule_value(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = get_capsule_value(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds12 = get_capsule_value(cannonCapsuleSpaceOdds12)
    cannonCapsuleSpaceOdds34 = get_capsule_value(cannonCapsuleSpaceOdds34)
    snackCapsulePrice12 = get_capsule_value(snackCapsulePrice12)
    snackCapsulePrice34 = get_capsule_value(snackCapsulePrice34)
    snackCapsuleShopOdds12 = get_capsule_value(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = get_capsule_value(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds12 = get_capsule_value(snackCapsuleSpaceOdds12)
    snackCapsuleSpaceOdds34 = get_capsule_value(snackCapsuleSpaceOdds34)
    lakituCapsulePrice12 = get_capsule_value(lakituCapsulePrice12)
    lakituCapsulePrice34 = get_capsule_value(lakituCapsulePrice34)
    lakituCapsuleShopOdds12 = get_capsule_value(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = get_capsule_value(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds12 = get_capsule_value(lakituCapsuleSpaceOdds12)
    lakituCapsuleSpaceOdds34 = get_capsule_value(lakituCapsuleSpaceOdds34)
    hammerBroCapsulePrice12 = get_capsule_value(hammerBroCapsulePrice12)
    hammerBroCapsulePrice34 = get_capsule_value(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = get_capsule_value(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = get_capsule_value(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds12 = get_capsule_value(hammerBroCapsuleSpaceOdds12)
    hammerBroCapsuleSpaceOdds34 = get_capsule_value(hammerBroCapsuleSpaceOdds34)
    piranhaPlantCapsulePrice12 = get_capsule_value(piranhaPlantCapsulePrice12)
    piranhaPlantCapsulePrice34 = get_capsule_value(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = get_capsule_value(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = get_capsule_value(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds12 = get_capsule_value(piranhaPlantCapsuleSpaceOdds12)
    piranhaPlantCapsuleSpaceOdds34 = get_capsule_value(piranhaPlantCapsuleSpaceOdds34)
    spearGuyCapsulePrice12 = get_capsule_value(spearGuyCapsulePrice12)
    spearGuyCapsulePrice34 = get_capsule_value(spearGuyCapsulePrice34)
    spearGuyCapsuleShopOdds12 = get_capsule_value(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = get_capsule_value(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds12 = get_capsule_value(spearGuyCapsuleSpaceOdds12)
    spearGuyCapsuleSpaceOdds34 = get_capsule_value(spearGuyCapsuleSpaceOdds34)
    kamekCapsulePrice12 = get_capsule_value(kamekCapsulePrice12)
    kamekCapsulePrice34 = get_capsule_value(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = get_capsule_value(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = get_capsule_value(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds12 = get_capsule_value(kamekCapsuleSpaceOdds12)
    kamekCapsuleSpaceOdds34 = get_capsule_value(kamekCapsuleSpaceOdds34)
    toadyCapsulePrice12 = get_capsule_value(toadyCapsulePrice12)
    toadyCapsulePrice34 = get_capsule_value(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = get_capsule_value(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = get_capsule_value(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds12 = get_capsule_value(toadyCapsuleSpaceOdds12)
    toadyCapsuleSpaceOdds34 = get_capsule_value(toadyCapsuleSpaceOdds34)
    mrBlizzardCapsulePrice12 = get_capsule_value(mrBlizzardCapsulePrice12)
    mrBlizzardCapsulePrice34 = get_capsule_value(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = get_capsule_value(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = get_capsule_value(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds12 = get_capsule_value(mrBlizzardCapsuleSpaceOdds12)
    mrBlizzardCapsuleSpaceOdds34 = get_capsule_value(mrBlizzardCapsuleSpaceOdds34)
    banditCapsulePrice12 = get_capsule_value(banditCapsulePrice12)
    banditCapsulePrice34 = get_capsule_value(banditCapsulePrice34)
    banditCapsuleShopOdds12 = get_capsule_value(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = get_capsule_value(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds12 = get_capsule_value(banditCapsuleSpaceOdds12)
    banditCapsuleSpaceOdds34 = get_capsule_value(banditCapsuleSpaceOdds34)
    pinkBooCapsulePrice12 = get_capsule_value(pinkBooCapsulePrice12)
    pinkBooCapsulePrice34 = get_capsule_value(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = get_capsule_value(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = get_capsule_value(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds12 = get_capsule_value(pinkBooCapsuleSpaceOdds12)
    pinkBooCapsuleSpaceOdds34 = get_capsule_value(pinkBooCapsuleSpaceOdds34)
    spinyCapsulePrice12 = get_capsule_value(spinyCapsulePrice12)
    spinyCapsulePrice34 = get_capsule_value(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = get_capsule_value(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = get_capsule_value(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds12 = get_capsule_value(spinyCapsuleSpaceOdds12)
    spinyCapsuleSpaceOdds34 = get_capsule_value(spinyCapsuleSpaceOdds34)
    zapCapsulePrice12 = get_capsule_value(zapCapsulePrice12)
    zapCapsulePrice34 = get_capsule_value(zapCapsulePrice34)
    zapCapsuleShopOdds12 = get_capsule_value(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = get_capsule_value(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds12 = get_capsule_value(zapCapsuleSpaceOdds12)
    zapCapsuleSpaceOdds34 = get_capsule_value(zapCapsuleSpaceOdds34)
    tweesterCapsulePrice12 = get_capsule_value(tweesterCapsulePrice12)
    tweesterCapsulePrice34 = get_capsule_value(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = get_capsule_value(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = get_capsule_value(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds12 = get_capsule_value(tweesterCapsuleSpaceOdds12)
    tweesterCapsuleSpaceOdds34 = get_capsule_value(tweesterCapsuleSpaceOdds34)
    thwompCapsulePrice12 = get_capsule_value(thwompCapsulePrice12)
    thwompCapsulePrice34 = get_capsule_value(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = get_capsule_value(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = get_capsule_value(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds12 = get_capsule_value(thwompCapsuleSpaceOdds12)
    thwompCapsuleSpaceOdds34 = get_capsule_value(thwompCapsuleSpaceOdds34)
    warpCapsulePrice12 = get_capsule_value(warpCapsulePrice12)
    warpCapsulePrice34 = get_capsule_value(warpCapsulePrice34)
    warpCapsuleShopOdds12 = get_capsule_value(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = get_capsule_value(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds12 = get_capsule_value(warpCapsuleSpaceOdds12)
    warpCapsuleSpaceOdds34 = get_capsule_value(warpCapsuleSpaceOdds34)
    bombCapsulePrice12 = get_capsule_value(bombCapsulePrice12)
    bombCapsulePrice34 = get_capsule_value(bombCapsulePrice34)
    bombCapsuleShopOdds12 = get_capsule_value(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = get_capsule_value(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds12 = get_capsule_value(bombCapsuleSpaceOdds12)
    bombCapsuleSpaceOdds34 = get_capsule_value(bombCapsuleSpaceOdds34)
    fireballCapsulePrice12 = get_capsule_value(fireballCapsulePrice12)
    fireballCapsulePrice34 = get_capsule_value(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = get_capsule_value(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = get_capsule_value(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds12 = get_capsule_value(fireballCapsuleSpaceOdds12)
    fireballCapsuleSpaceOdds34 = get_capsule_value(fireballCapsuleSpaceOdds34)
    flowerCapsulePrice12 = get_capsule_value(flowerCapsulePrice12)
    flowerCapsulePrice34 = get_capsule_value(flowerCapsulePrice34)
    flowerCapsuleShopOdds12 = get_capsule_value(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = get_capsule_value(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds12 = get_capsule_value(flowerCapsuleSpaceOdds12)
    flowerCapsuleSpaceOdds34 = get_capsule_value(flowerCapsuleSpaceOdds34)
    eggCapsulePrice12 = get_capsule_value(eggCapsulePrice12)
    eggCapsulePrice34 = get_capsule_value(eggCapsulePrice34)
    eggCapsuleShopOdds12 = get_capsule_value(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = get_capsule_value(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds12 = get_capsule_value(eggCapsuleSpaceOdds12)
    eggCapsuleSpaceOdds34 = get_capsule_value(eggCapsuleSpaceOdds34)
    vacuumCapsulePrice12 = get_capsule_value(vacuumCapsulePrice12)
    vacuumCapsulePrice34 = get_capsule_value(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = get_capsule_value(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = get_capsule_value(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds12 = get_capsule_value(vacuumCapsuleSpaceOdds12)
    vacuumCapsuleSpaceOdds34 = get_capsule_value(vacuumCapsuleSpaceOdds34)
    magicCapsulePrice12 = get_capsule_value(magicCapsulePrice12)
    magicCapsulePrice34 = get_capsule_value(magicCapsulePrice34)
    magicCapsuleShopOdds12 = get_capsule_value(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = get_capsule_value(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds12 = get_capsule_value(magicCapsuleSpaceOdds12)
    magicCapsuleSpaceOdds34 = get_capsule_value(magicCapsuleSpaceOdds34)
    tripleCapsulePrice12 = get_capsule_value(tripleCapsulePrice12)
    tripleCapsulePrice34 = get_capsule_value(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = get_capsule_value(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = get_capsule_value(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds12 = get_capsule_value(tripleCapsuleSpaceOdds12)
    tripleCapsuleSpaceOdds34 = get_capsule_value(tripleCapsuleSpaceOdds34)
    koopaCapsulePrice12 = get_capsule_value(koopaCapsulePrice12)
    koopaCapsulePrice34 = get_capsule_value(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = get_capsule_value(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = get_capsule_value(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds12 = get_capsule_value(koopaCapsuleSpaceOdds12)
    koopaCapsuleSpaceOdds34 = get_capsule_value(koopaCapsuleSpaceOdds34)
    poisonMushroomPrice12 = get_capsule_value(poisonMushroomPrice12)
    poisonMushroomPrice34 = get_capsule_value(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = get_capsule_value(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = get_capsule_value(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds12 = get_capsule_value(poisonMushroomSpaceOdds12)
    poisonMushroomSpaceOdds34 = get_capsule_value(poisonMushroomSpaceOdds34)
    orbBagCapsulePrice12 = get_capsule_value(orbBagCapsulePrice12)
    orbBagCapsulePrice34 = get_capsule_value(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = get_capsule_value(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = get_capsule_value(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds12 = get_capsule_value(orbBagCapsuleSpaceOdds12)
    orbBagCapsuleSpaceOdds34 = get_capsule_value(orbBagCapsuleSpaceOdds34)
    mysteryCapsulePrice12 = get_capsule_value(mysteryCapsulePrice12)
    mysteryCapsulePrice34 = get_capsule_value(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = get_capsule_value(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = get_capsule_value(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds12 = get_capsule_value(mysteryCapsuleSpaceOdds12)
    mysteryCapsuleSpaceOdds34 = get_capsule_value(mysteryCapsuleSpaceOdds34)
    dkCapsulePrice12 = get_capsule_value(dkCapsulePrice12)
    dkCapsulePrice34 = get_capsule_value(dkCapsulePrice34)
    dkCapsuleShopOdds12 = get_capsule_value(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = get_capsule_value(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds12 = get_capsule_value(dkCapsuleSpaceOdds12)
    dkCapsuleSpaceOdds34 = get_capsule_value(dkCapsuleSpaceOdds34)
    duelCapsulePrice12 = get_capsule_value(duelCapsulePrice12)
    duelCapsulePrice34 = get_capsule_value(duelCapsulePrice34)
    duelCapsuleShopOdds12 = get_capsule_value(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = get_capsule_value(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds12 = get_capsule_value(duelCapsuleSpaceOdds12)
    duelCapsuleSpaceOdds34 = get_capsule_value(duelCapsuleSpaceOdds34)

    mushroomCapsuleShopOdds12 = str(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = str(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds12 = str(mushroomCapsuleSpaceOdds12)
    mushroomCapsuleSpaceOdds34 = str(mushroomCapsuleSpaceOdds34)
    goldenMushroomCapsulePrice12 = str(goldenMushroomCapsulePrice12)
    goldenMushroomCapsulePrice34 = str(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = str(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = str(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds12 = str(goldenMushroomCapsuleSpaceOdds12)
    goldenMushroomCapsuleSpaceOdds34 = str(goldenMushroomCapsuleSpaceOdds34)
    slowMushroomCapsulePrice12 = str(slowMushroomCapsulePrice12)
    slowMushroomCapsulePrice34 = str(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = str(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = str(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds12 = str(slowMushroomCapsuleSpaceOdds12)
    slowMushroomCapsuleSpaceOdds34 = str(slowMushroomCapsuleSpaceOdds34)
    metalMushroomCapsulePrice12 = str(metalMushroomCapsulePrice12)
    metalMushroomCapsulePrice34 = str(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = str(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = str(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds12 = str(metalMushroomCapsuleSpaceOdds12)
    metalMushroomCapsuleSpaceOdds34 = str(metalMushroomCapsuleSpaceOdds34)
    flutterCapsulePrice12 = str(flutterCapsulePrice12)
    flutterCapsulePrice34 = str(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = str(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = str(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds12 = str(flutterCapsuleSpaceOdds12)
    flutterCapsuleSpaceOdds34 = str(flutterCapsuleSpaceOdds34)
    cannonCapsulePrice12 = str(cannonCapsulePrice12)
    cannonCapsulePrice34 = str(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = str(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = str(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds12 = str(cannonCapsuleSpaceOdds12)
    cannonCapsuleSpaceOdds34 = str(cannonCapsuleSpaceOdds34)
    snackCapsulePrice12 = str(snackCapsulePrice12)
    snackCapsulePrice34 = str(snackCapsulePrice34)
    snackCapsuleShopOdds12 = str(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = str(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds12 = str(snackCapsuleSpaceOdds12)
    snackCapsuleSpaceOdds34 = str(snackCapsuleSpaceOdds34)
    lakituCapsulePrice12 = str(lakituCapsulePrice12)
    lakituCapsulePrice34 = str(lakituCapsulePrice34)
    lakituCapsuleShopOdds12 = str(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = str(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds12 = str(lakituCapsuleSpaceOdds12)
    lakituCapsuleSpaceOdds34 = str(lakituCapsuleSpaceOdds34)
    hammerBroCapsulePrice12 = str(hammerBroCapsulePrice12)
    hammerBroCapsulePrice34 = str(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = str(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = str(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds12 = str(hammerBroCapsuleSpaceOdds12)
    hammerBroCapsuleSpaceOdds34 = str(hammerBroCapsuleSpaceOdds34)
    piranhaPlantCapsulePrice12 = str(piranhaPlantCapsulePrice12)
    piranhaPlantCapsulePrice34 = str(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = str(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = str(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds12 = str(piranhaPlantCapsuleSpaceOdds12)
    piranhaPlantCapsuleSpaceOdds34 = str(piranhaPlantCapsuleSpaceOdds34)
    spearGuyCapsulePrice12 = str(spearGuyCapsulePrice12)
    spearGuyCapsulePrice34 = str(spearGuyCapsulePrice34)
    spearGuyCapsuleShopOdds12 = str(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = str(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds12 = str(spearGuyCapsuleSpaceOdds12)
    spearGuyCapsuleSpaceOdds34 = str(spearGuyCapsuleSpaceOdds34)
    kamekCapsulePrice12 = str(kamekCapsulePrice12)
    kamekCapsulePrice34 = str(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = str(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = str(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds12 = str(kamekCapsuleSpaceOdds12)
    kamekCapsuleSpaceOdds34 = str(kamekCapsuleSpaceOdds34)
    toadyCapsulePrice12 = str(toadyCapsulePrice12)
    toadyCapsulePrice34 = str(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = str(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = str(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds12 = str(toadyCapsuleSpaceOdds12)
    toadyCapsuleSpaceOdds34 = str(toadyCapsuleSpaceOdds34)
    mrBlizzardCapsulePrice12 = str(mrBlizzardCapsulePrice12)
    mrBlizzardCapsulePrice34 = str(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = str(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = str(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds12 = str(mrBlizzardCapsuleSpaceOdds12)
    mrBlizzardCapsuleSpaceOdds34 = str(mrBlizzardCapsuleSpaceOdds34)
    banditCapsulePrice12 = str(banditCapsulePrice12)
    banditCapsulePrice34 = str(banditCapsulePrice34)
    banditCapsuleShopOdds12 = str(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = str(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds12 = str(banditCapsuleSpaceOdds12)
    banditCapsuleSpaceOdds34 = str(banditCapsuleSpaceOdds34)
    pinkBooCapsulePrice12 = str(pinkBooCapsulePrice12)
    pinkBooCapsulePrice34 = str(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = str(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = str(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds12 = str(pinkBooCapsuleSpaceOdds12)
    pinkBooCapsuleSpaceOdds34 = str(pinkBooCapsuleSpaceOdds34)
    spinyCapsulePrice12 = str(spinyCapsulePrice12)
    spinyCapsulePrice34 = str(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = str(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = str(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds12 = str(spinyCapsuleSpaceOdds12)
    spinyCapsuleSpaceOdds34 = str(spinyCapsuleSpaceOdds34)
    zapCapsulePrice12 = str(zapCapsulePrice12)
    zapCapsulePrice34 = str(zapCapsulePrice34)
    zapCapsuleShopOdds12 = str(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = str(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds12 = str(zapCapsuleSpaceOdds12)
    zapCapsuleSpaceOdds34 = str(zapCapsuleSpaceOdds34)
    tweesterCapsulePrice12 = str(tweesterCapsulePrice12)
    tweesterCapsulePrice34 = str(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = str(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = str(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds12 = str(tweesterCapsuleSpaceOdds12)
    tweesterCapsuleSpaceOdds34 = str(tweesterCapsuleSpaceOdds34)
    thwompCapsulePrice12 = str(thwompCapsulePrice12)
    thwompCapsulePrice34 = str(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = str(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = str(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds12 = str(thwompCapsuleSpaceOdds12)
    thwompCapsuleSpaceOdds34 = str(thwompCapsuleSpaceOdds34)
    warpCapsulePrice12 = str(warpCapsulePrice12)
    warpCapsulePrice34 = str(warpCapsulePrice34)
    warpCapsuleShopOdds12 = str(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = str(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds12 = str(warpCapsuleSpaceOdds12)
    warpCapsuleSpaceOdds34 = str(warpCapsuleSpaceOdds34)
    bombCapsulePrice12 = str(bombCapsulePrice12)
    bombCapsulePrice34 = str(bombCapsulePrice34)
    bombCapsuleShopOdds12 = str(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = str(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds12 = str(bombCapsuleSpaceOdds12)
    bombCapsuleSpaceOdds34 = str(bombCapsuleSpaceOdds34)
    fireballCapsulePrice12 = str(fireballCapsulePrice12)
    fireballCapsulePrice34 = str(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = str(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = str(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds12 = str(fireballCapsuleSpaceOdds12)
    fireballCapsuleSpaceOdds34 = str(fireballCapsuleSpaceOdds34)
    flowerCapsulePrice12 = str(flowerCapsulePrice12)
    flowerCapsulePrice34 = str(flowerCapsulePrice34)
    flowerCapsuleShopOdds12 = str(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = str(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds12 = str(flowerCapsuleSpaceOdds12)
    flowerCapsuleSpaceOdds34 = str(flowerCapsuleSpaceOdds34)
    eggCapsulePrice12 = str(eggCapsulePrice12)
    eggCapsulePrice34 = str(eggCapsulePrice34)
    eggCapsuleShopOdds12 = str(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = str(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds12 = str(eggCapsuleSpaceOdds12)
    eggCapsuleSpaceOdds34 = str(eggCapsuleSpaceOdds34)
    vacuumCapsulePrice12 = str(vacuumCapsulePrice12)
    vacuumCapsulePrice34 = str(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = str(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = str(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds12 = str(vacuumCapsuleSpaceOdds12)
    vacuumCapsuleSpaceOdds34 = str(vacuumCapsuleSpaceOdds34)
    magicCapsulePrice12 = str(magicCapsulePrice12)
    magicCapsulePrice34 = str(magicCapsulePrice34)
    magicCapsuleShopOdds12 = str(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = str(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds12 = str(magicCapsuleSpaceOdds12)
    magicCapsuleSpaceOdds34 = str(magicCapsuleSpaceOdds34)
    tripleCapsulePrice12 = str(tripleCapsulePrice12)
    tripleCapsulePrice34 = str(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = str(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = str(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds12 = str(tripleCapsuleSpaceOdds12)
    tripleCapsuleSpaceOdds34 = str(tripleCapsuleSpaceOdds34)
    koopaCapsulePrice12 = str(koopaCapsulePrice12)
    koopaCapsulePrice34 = str(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = str(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = str(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds12 = str(koopaCapsuleSpaceOdds12)
    koopaCapsuleSpaceOdds34 = str(koopaCapsuleSpaceOdds34)
    poisonMushroomPrice12 = str(poisonMushroomPrice12)
    poisonMushroomPrice34 = str(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = str(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = str(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds12 = str(poisonMushroomSpaceOdds12)
    poisonMushroomSpaceOdds34 = str(poisonMushroomSpaceOdds34)
    orbBagCapsulePrice12 = str(orbBagCapsulePrice12)
    orbBagCapsulePrice34 = str(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = str(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = str(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds12 = str(orbBagCapsuleSpaceOdds12)
    orbBagCapsuleSpaceOdds34 = str(orbBagCapsuleSpaceOdds34)
    mysteryCapsulePrice12 = str(mysteryCapsulePrice12)
    mysteryCapsulePrice34 = str(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = str(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = str(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds12 = str(mysteryCapsuleSpaceOdds12)
    mysteryCapsuleSpaceOdds34 = str(mysteryCapsuleSpaceOdds34)
    dkCapsulePrice12 = str(dkCapsulePrice12)
    dkCapsulePrice34 = str(dkCapsulePrice34)
    dkCapsuleShopOdds12 = str(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = str(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds12 = str(dkCapsuleSpaceOdds12)
    dkCapsuleSpaceOdds34 = str(dkCapsuleSpaceOdds34)
    duelCapsulePrice12 = str(duelCapsulePrice12)
    duelCapsulePrice34 = str(duelCapsulePrice34)
    duelCapsuleShopOdds12 = str(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = str(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds12 = str(duelCapsuleSpaceOdds12)
    duelCapsuleSpaceOdds34 = str(duelCapsuleSpaceOdds34)

    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, lakituCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, spearGuyCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, zapCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, flowerCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, lakituCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, spearGuyCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, zapCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, flowerCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
    ]

    spaceOdds12 = [
        mushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds12,
        slowMushroomCapsuleSpaceOdds12, flutterCapsuleSpaceOdds12, cannonCapsuleSpaceOdds12,
        snackCapsuleSpaceOdds12, lakituCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds12,
        piranhaPlantCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds12, kamekCapsuleSpaceOdds12,
        toadyCapsuleSpaceOdds12, mrBlizzardCapsuleSpaceOdds12, banditCapsuleSpaceOdds12,
        pinkBooCapsuleSpaceOdds12, spinyCapsuleSpaceOdds12, zapCapsuleSpaceOdds12,
        tweesterCapsuleSpaceOdds12, thwompCapsuleSpaceOdds12, warpCapsuleSpaceOdds12,
        bombCapsuleSpaceOdds12, fireballCapsuleSpaceOdds12, flowerCapsuleSpaceOdds12,
        eggCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds12, magicCapsuleSpaceOdds12,
        tripleCapsuleSpaceOdds12, koopaCapsuleSpaceOdds12, mysteryCapsuleSpaceOdds12,
        duelCapsuleSpaceOdds12, dkCapsuleSpaceOdds12, orbBagCapsuleSpaceOdds12
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, lakituCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, spearGuyCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, zapCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, flowerCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
    ]

    prices12 = [
        mushroomCapsulePrice12, goldenMushroomCapsulePrice12, metalMushroomCapsulePrice12,
        slowMushroomCapsulePrice12, flutterCapsulePrice12, cannonCapsulePrice12,
        snackCapsulePrice12, lakituCapsulePrice12, hammerBroCapsulePrice12,
        piranhaPlantCapsulePrice12, spearGuyCapsulePrice12, kamekCapsulePrice12,
        toadyCapsulePrice12, mrBlizzardCapsulePrice12, banditCapsulePrice12,
        pinkBooCapsulePrice12, spinyCapsulePrice12, zapCapsulePrice12,
        tweesterCapsulePrice12, thwompCapsulePrice12, warpCapsulePrice12,
        bombCapsulePrice12, fireballCapsulePrice12, flowerCapsulePrice12,
        eggCapsulePrice12, vacuumCapsulePrice12, magicCapsulePrice12,
        tripleCapsulePrice12, koopaCapsulePrice12, poisonMushroomPrice12,
        orbBagCapsulePrice12, mysteryCapsulePrice12, dkCapsulePrice12,
        duelCapsulePrice12
    ]

    prices34 = [
        mushroomCapsulePrice34, goldenMushroomCapsulePrice34, metalMushroomCapsulePrice34,
        slowMushroomCapsulePrice34, flutterCapsulePrice34, cannonCapsulePrice34,
        snackCapsulePrice34, lakituCapsulePrice34, hammerBroCapsulePrice34,
        piranhaPlantCapsulePrice34, spearGuyCapsulePrice34, kamekCapsulePrice34,
        toadyCapsulePrice34, mrBlizzardCapsulePrice34, banditCapsulePrice34,
        pinkBooCapsulePrice34, spinyCapsulePrice34, zapCapsulePrice34,
        tweesterCapsulePrice34, thwompCapsulePrice34, warpCapsulePrice34,
        bombCapsulePrice34, fireballCapsulePrice34, flowerCapsulePrice34,
        eggCapsulePrice34, vacuumCapsulePrice34, magicCapsulePrice34,
        tripleCapsulePrice34, koopaCapsulePrice34, poisonMushroomPrice34,
        orbBagCapsulePrice34, mysteryCapsulePrice34, dkCapsulePrice34,
        duelCapsulePrice34
    ]
    
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prices12', 'Prices34', "ShopOdds12", "ShopOdds34", "SpaceOdds12", "SpaceOdds34"])
            for price, weight in zip(prices12, prices34, shopOdds12, shopOdds34, spaceOdds12, spaceOdds34):
                writer.writerow([price, weight])
        print("MPT file saved successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def loadPresetItems7(hide_custom, mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34, mushroomCapsuleSpaceOdds12, mushroomCapsuleSpaceOdds34, goldenMushroomCapsulePrice12, goldenMushroomCapsulePrice34, goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, goldenMushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds34, slowMushroomCapsulePrice12, slowMushroomCapsulePrice34, slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, slowMushroomCapsuleSpaceOdds12, slowMushroomCapsuleSpaceOdds34, metalMushroomCapsulePrice12, metalMushroomCapsulePrice34, metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, metalMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds34, flutterCapsulePrice12, flutterCapsulePrice34, flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, flutterCapsuleSpaceOdds12, flutterCapsuleSpaceOdds34, cannonCapsulePrice12, cannonCapsulePrice34, cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, cannonCapsuleSpaceOdds12, cannonCapsuleSpaceOdds34, snackCapsulePrice12, snackCapsulePrice34, snackCapsuleShopOdds12, snackCapsuleShopOdds34, snackCapsuleSpaceOdds12, snackCapsuleSpaceOdds34, lakituCapsulePrice12, lakituCapsulePrice34, lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, lakituCapsuleSpaceOdds12, lakituCapsuleSpaceOdds34, hammerBroCapsulePrice12, hammerBroCapsulePrice34, hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, hammerBroCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds34, piranhaPlantCapsulePrice12, piranhaPlantCapsulePrice34, piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, piranhaPlantCapsuleSpaceOdds12, piranhaPlantCapsuleSpaceOdds34, spearGuyCapsulePrice12, spearGuyCapsulePrice34, spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, spearGuyCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds34, kamekCapsulePrice12, kamekCapsulePrice34, kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, kamekCapsuleSpaceOdds12, kamekCapsuleSpaceOdds34, toadyCapsulePrice12, toadyCapsulePrice34, toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, toadyCapsuleSpaceOdds12, toadyCapsuleSpaceOdds34, mrBlizzardCapsulePrice12, mrBlizzardCapsulePrice34, mrBlizzardCapsuleShopOdds12, mrBlizzardCapsuleShopOdds34, mrBlizzardCapsuleSpaceOdds12, mrBlizzardCapsuleSpaceOdds34, banditCapsulePrice12, banditCapsulePrice34, banditCapsuleShopOdds12, banditCapsuleShopOdds34, banditCapsuleSpaceOdds12, banditCapsuleSpaceOdds34, pinkBooCapsulePrice12, pinkBooCapsulePrice34, pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, pinkBooCapsuleSpaceOdds12, pinkBooCapsuleSpaceOdds34, spinyCapsulePrice12, spinyCapsulePrice34, spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, spinyCapsuleSpaceOdds12, spinyCapsuleSpaceOdds34, zapCapsulePrice12, zapCapsulePrice34, zapCapsuleShopOdds12, zapCapsuleShopOdds34, zapCapsuleSpaceOdds12, zapCapsuleSpaceOdds34, tweesterCapsulePrice12, tweesterCapsulePrice34, tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, tweesterCapsuleSpaceOdds12, tweesterCapsuleSpaceOdds34, thwompCapsulePrice12, thwompCapsulePrice34, thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, thwompCapsuleSpaceOdds12, thwompCapsuleSpaceOdds34, warpCapsulePrice12, warpCapsulePrice34, warpCapsuleShopOdds12, warpCapsuleShopOdds34, warpCapsuleSpaceOdds12, warpCapsuleSpaceOdds34, bombCapsulePrice12, bombCapsulePrice34, bombCapsuleShopOdds12, bombCapsuleShopOdds34, bombCapsuleSpaceOdds12, bombCapsuleSpaceOdds34, fireballCapsulePrice12, fireballCapsulePrice34, fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, fireballCapsuleSpaceOdds12, fireballCapsuleSpaceOdds34, flowerCapsulePrice12, flowerCapsulePrice34, flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, flowerCapsuleSpaceOdds12, flowerCapsuleSpaceOdds34, eggCapsulePrice12, eggCapsulePrice34, eggCapsuleShopOdds12, eggCapsuleShopOdds34, eggCapsuleSpaceOdds12, eggCapsuleSpaceOdds34, vacuumCapsulePrice12, vacuumCapsulePrice34, vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, vacuumCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds34, magicCapsulePrice12, magicCapsulePrice34, magicCapsuleShopOdds12, magicCapsuleShopOdds34, magicCapsuleSpaceOdds12, magicCapsuleSpaceOdds34, tripleCapsulePrice12, tripleCapsulePrice34, tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, tripleCapsuleSpaceOdds12, tripleCapsuleSpaceOdds34, koopaCapsulePrice12, koopaCapsulePrice34, koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, koopaCapsuleSpaceOdds12, koopaCapsuleSpaceOdds34, poisonMushroomPrice34, poisonMushroomPrice12, poisonMushroomShopOdds12, poisonMushroomShopOdds34, poisonMushroomSpaceOdds12, poisonMushroomSpaceOdds34, orbBagCapsulePrice34, orbBagCapsulePrice12, orbBagCapsuleShopOdds12, orbBagCapsuleShopOdds34, orbBagCapsuleSpaceOdds12, orbBagCapsuleSpaceOdds34, mysteryCapsulePrice34, mysteryCapsulePrice12, mysteryCapsuleShopOdds12, mysteryCapsuleShopOdds34, mysteryCapsuleSpaceOdds12, mysteryCapsuleSpaceOdds34, dkCapsulePrice34, dkCapsulePrice12, dkCapsuleShopOdds12, dkCapsuleShopOdds34, dkCapsuleSpaceOdds12, dkCapsuleSpaceOdds34, duelCapsulePrice34, duelCapsulePrice12, duelCapsuleShopOdds12, duelCapsuleShopOdds34, duelCapsuleSpaceOdds12, duelCapsuleSpaceOdds34):
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        prices12In = []
        prices34In = []
        shopOdds12In = []
        shopOdds34In = []
        spaceOdds12In = []
        spaceOdds34In = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                prices12In.append(float(row[0]))
                prices34In.append(float(row[1]))
                shopOdds12In.append(float(row[2]))
                shopOdds34In.append(float(row[3]))
                spaceOdds12In.append(float(row[4]))
                spaceOdds34In.append(float(row[5]))

        mushroomCapsulePrice12 = ""
        mushroomCapsulePrice34 = ""
        # Define a list of Entry widget attributes
        shopOdds12 = [
            mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
            slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
            snackCapsuleShopOdds12, lakituCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
            piranhaPlantCapsuleShopOdds12, spearGuyCapsuleShopOdds12, kamekCapsuleShopOdds12,
            toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
            pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, zapCapsuleShopOdds12,
            tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
            bombCapsuleShopOdds12, fireballCapsuleShopOdds12, flowerCapsuleShopOdds12,
            eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
            tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
            duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
        ]
    
        shopOdds34 = [
            mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
            slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
            snackCapsuleShopOdds34, lakituCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
            piranhaPlantCapsuleShopOdds34, spearGuyCapsuleShopOdds34, kamekCapsuleShopOdds34,
            toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
            pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, zapCapsuleShopOdds34,
            tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
            bombCapsuleShopOdds34, fireballCapsuleShopOdds34, flowerCapsuleShopOdds34,
            eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
            tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
            duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
        ]
    
        spaceOdds12 = [
            mushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds12,
            slowMushroomCapsuleSpaceOdds12, flutterCapsuleSpaceOdds12, cannonCapsuleSpaceOdds12,
            snackCapsuleSpaceOdds12, lakituCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds12,
            piranhaPlantCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds12, kamekCapsuleSpaceOdds12,
            toadyCapsuleSpaceOdds12, mrBlizzardCapsuleSpaceOdds12, banditCapsuleSpaceOdds12,
            pinkBooCapsuleSpaceOdds12, spinyCapsuleSpaceOdds12, zapCapsuleSpaceOdds12,
            tweesterCapsuleSpaceOdds12, thwompCapsuleSpaceOdds12, warpCapsuleSpaceOdds12,
            bombCapsuleSpaceOdds12, fireballCapsuleSpaceOdds12, flowerCapsuleSpaceOdds12,
            eggCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds12, magicCapsuleSpaceOdds12,
            tripleCapsuleSpaceOdds12, koopaCapsuleSpaceOdds12, mysteryCapsuleSpaceOdds12,
            duelCapsuleSpaceOdds12, dkCapsuleSpaceOdds12, orbBagCapsuleSpaceOdds12
        ]
        
        spaceOdds34 = [
            mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
            slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
            snackCapsuleSpaceOdds34, lakituCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
            piranhaPlantCapsuleSpaceOdds34, spearGuyCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
            toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
            pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, zapCapsuleSpaceOdds34,
            tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
            bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, flowerCapsuleSpaceOdds34,
            eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
            tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
            duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
        ]
    
        prices12 = [
            mushroomCapsulePrice12, goldenMushroomCapsulePrice12, metalMushroomCapsulePrice12,
            slowMushroomCapsulePrice12, flutterCapsulePrice12, cannonCapsulePrice12,
            snackCapsulePrice12, lakituCapsulePrice12, hammerBroCapsulePrice12,
            piranhaPlantCapsulePrice12, spearGuyCapsulePrice12, kamekCapsulePrice12,
            toadyCapsulePrice12, mrBlizzardCapsulePrice12, banditCapsulePrice12,
            pinkBooCapsulePrice12, spinyCapsulePrice12, zapCapsulePrice12,
            tweesterCapsulePrice12, thwompCapsulePrice12, warpCapsulePrice12,
            bombCapsulePrice12, fireballCapsulePrice12, flowerCapsulePrice12,
            eggCapsulePrice12, vacuumCapsulePrice12, magicCapsulePrice12,
            tripleCapsulePrice12, koopaCapsulePrice12
        ]
    
        prices34 = [
            mushroomCapsulePrice34, goldenMushroomCapsulePrice34, metalMushroomCapsulePrice34,
            slowMushroomCapsulePrice34, flutterCapsulePrice34, cannonCapsulePrice34,
            snackCapsulePrice34, lakituCapsulePrice34, hammerBroCapsulePrice34,
            piranhaPlantCapsulePrice34, spearGuyCapsulePrice34, kamekCapsulePrice34,
            toadyCapsulePrice34, mrBlizzardCapsulePrice34, banditCapsulePrice34,
            pinkBooCapsulePrice34, spinyCapsulePrice34, zapCapsulePrice34,
            tweesterCapsulePrice34, thwompCapsulePrice34, warpCapsulePrice34,
            bombCapsulePrice34, fireballCapsulePrice34, flowerCapsulePrice34,
            eggCapsulePrice34, vacuumCapsulePrice34, magicCapsulePrice34,
            tripleCapsulePrice34, koopaCapsulePrice34
        ]

        if not hide_custom:
            prices12.extend([
                poisonMushroomPrice12,
                orbBagCapsulePrice12, 
                mysteryCapsulePrice12, 
                dkCapsulePrice12,
                duelCapsulePrice12
            ])
            prices34.extend([
                poisonMushroomPrice34,
                orbBagCapsulePrice34, 
                mysteryCapsulePrice34, 
                dkCapsulePrice34,
                duelCapsulePrice34
            ])
            shopOdds12.extend([
                poisonMushroomShopOdds12,
                orbBagCapsuleShopOdds12,
                mysteryCapsuleShopOdds12,
                dkCapsuleShopOdds12
            ])
            shopOdds34.extend([
                poisonMushroomShopOdds34,
                orbBagCapsuleShopOdds34,
                mysteryCapsuleShopOdds34,
                dkCapsuleShopOdds34
            ])
            spaceOdds12.extend([
                poisonMushroomSpaceOdds12,
                orbBagCapsuleSpaceOdds12,
                mysteryCapsuleSpaceOdds12,
                dkCapsuleSpaceOdds12
            ])
            spaceOdds34.extend([
                poisonMushroomSpaceOdds34,
                orbBagCapsuleSpaceOdds34,
                mysteryCapsuleSpaceOdds34,
                dkCapsuleSpaceOdds34
            ])

        # Update widgets with loaded values
        for index, widget in enumerate(prices12):
            if widget and index < len(prices12In):
                widget.delete(0, 'end')
                widget.insert(0, int(prices12In[index]))
        for index, widget in enumerate(prices34):
            if widget and index < len(prices34In):
                widget.delete(0, 'end')
                widget.insert(0, int(prices34In[index]))
        
        # Update widgets for shop odds
        for index, widget in enumerate(shopOdds12):
            if widget and index < len(shopOdds12In):
                widget.delete(0, 'end')
                widget.insert(0, int(shopOdds12In[index]))
        for index, widget in enumerate(shopOdds34):
            if widget and index < len(shopOdds34In):
                widget.delete(0, 'end')
                widget.insert(0, int(shopOdds34In[index]))

        # Update widgets for space odds
        for index, widget in enumerate(spaceOdds12):
            if widget and index < len(spaceOdds12In):
                widget.delete(0, 'end')
                widget.insert(0, int(spaceOdds12In[index]))
        for index, widget in enumerate(spaceOdds34):
            if widget and index < len(spaceOdds34In):
                widget.delete(0, 'end')
                widget.insert(0, int(spaceOdds34In[index]))

        print("MPT file laoded successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)