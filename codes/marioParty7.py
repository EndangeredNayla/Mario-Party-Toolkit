# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Blue Spaces Give {amountDec} Coins
04168578 60000000
0416857C 3880{amount}
'''

def getRedSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Red Spaces Take Away {amountDec} Coins
04168600 60000000
04168604 3880{amount}
'''

def getCharacterSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Character Spaces Give {amountDec} Coins
C21685B8 00000001
3880{amount} 00000000
'''

def getMinigameCodeSeven(amount, amountDec):
    return f'''
MP7 - Minigames Award {amountDec} Coins
C20098A4 00000012
3DC08029 61CE1559
89EE0000 2C0F0004
41820068 2C0F001A
41820060 2C0F002B
41820058 2C0F002F
41820050 2C0F0030
41820048 2C0F0031
41820040 2C0F0037
41820038 2C0F0038
41820030 3DC08029
61CE0CCA A1EE0000
2C0F0000 4182000C
39E0{amount} B1EE0000
39CE0110 3A100001
2C100003 4081FFE0
3800FFFF 39C00000
39E00000 3A000000
60000000 00000000
'''

def getStarSpaceCodeSeven(amount, amountDec, x2, x3, x4):
    return f'''
MP7 - Stars Cost {amountDec} Coins
04188774 3B80{amount}
204E0640 38030001
044E0644 1C00000A
044E0574 3800{amount} 
044E08D8 3800{amount}
044E09B8 1C00000A
044E0BAC 38A0{amount}
044E0C8C 1C60000A
E2000001 80008000
204F92AC 804F929D
044F9268 0000{amount}
044F926C 0000{x2}
044F9270 0000{x3}
044F9274 0000{x4}
E2000001 80008000
'''

def getStarSpaceCodeSevenLastFive(amount, amountDec):
    return f'''
MP7 - Stars Cost {amountDec} Coins During the Last 5 Turns Event
0418876C 3B80{amount}
'''

def getHammerBroSpaceCodeSeven(amount, negAmount, halfAmount, amountDec):
    return f'''
MP7 - Hammer Bro Takes {amountDec} Coins
041A902C 3AC0{amount}
041A9A28 38A0{negAmount}
041A973C 38000000
041A9744 3800{halfAmount}
041A974C 38000000
041A9754 3800{halfAmount}
'''

def getZapSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Zap Takes {amountDec} Coins
C21B652C 00000001
3880{amount} 00000000
'''

def getFlowerSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Flower Gives {amountDec} Coins Per Space
041C4F24 3B40{amount}
'''

def getVacuumSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Vaccum Always Steals {amountDec} Coins
041C8A34 3860{amount}
'''

def getFireballSpaceCodeSeven(amount, negAmount, amountDec):
    return f'''
MP7 - Fireball Takes {amountDec} Coins
041C1464 3b80{amount}
041C148C 38A0{negAmount}
'''

def getMinigameReplacement7(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP7 - Minigame Replacement: {gameUno} ➜ {gameDos}
28291558 000000{hexUno}
02291558 000000{hexDos}
E2000001 80008000
'''

def getOrbModsSeven(mushroomCapsulePrice12, mushroomCapsulePrice34, mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34, mushroomCapsuleSpaceOdds12, mushroomCapsuleSpaceOdds34, goldenMushroomCapsulePrice12, goldenMushroomCapsulePrice34, goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, goldenMushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds34, slowMushroomCapsulePrice12, slowMushroomCapsulePrice34, slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, slowMushroomCapsuleSpaceOdds12, slowMushroomCapsuleSpaceOdds34, metalMushroomCapsulePrice12, metalMushroomCapsulePrice34, metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, metalMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds34, flutterCapsulePrice12, flutterCapsulePrice34, flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, flutterCapsuleSpaceOdds12, flutterCapsuleSpaceOdds34, cannonCapsulePrice12, cannonCapsulePrice34, cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, cannonCapsuleSpaceOdds12, cannonCapsuleSpaceOdds34, snackCapsulePrice12, snackCapsulePrice34, snackCapsuleShopOdds12, snackCapsuleShopOdds34, snackCapsuleSpaceOdds12, snackCapsuleSpaceOdds34, lakituCapsulePrice12, lakituCapsulePrice34, lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, lakituCapsuleSpaceOdds12, lakituCapsuleSpaceOdds34, hammerBroCapsulePrice12, hammerBroCapsulePrice34, hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, hammerBroCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds34, piranhaPlantCapsulePrice12, piranhaPlantCapsulePrice34, piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, piranhaPlantCapsuleSpaceOdds12, piranhaPlantCapsuleSpaceOdds34, spearGuyCapsulePrice12, spearGuyCapsulePrice34, spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, spearGuyCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds34, kamekCapsulePrice12, kamekCapsulePrice34, kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, kamekCapsuleSpaceOdds12, kamekCapsuleSpaceOdds34, toadyCapsulePrice12, toadyCapsulePrice34, toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, toadyCapsuleSpaceOdds12, toadyCapsuleSpaceOdds34, mrBlizzardCapsulePrice12, mrBlizzardCapsulePrice34, mrBlizzardCapsuleShopOdds12, mrBlizzardCapsuleShopOdds34, mrBlizzardCapsuleSpaceOdds12, mrBlizzardCapsuleSpaceOdds34, banditCapsulePrice12, banditCapsulePrice34, banditCapsuleShopOdds12, banditCapsuleShopOdds34, banditCapsuleSpaceOdds12, banditCapsuleSpaceOdds34, pinkBooCapsulePrice12, pinkBooCapsulePrice34, pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, pinkBooCapsuleSpaceOdds12, pinkBooCapsuleSpaceOdds34, spinyCapsulePrice12, spinyCapsulePrice34, spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, spinyCapsuleSpaceOdds12, spinyCapsuleSpaceOdds34, zapCapsulePrice12, zapCapsulePrice34, zapCapsuleShopOdds12, zapCapsuleShopOdds34, zapCapsuleSpaceOdds12, zapCapsuleSpaceOdds34, tweesterCapsulePrice12, tweesterCapsulePrice34, tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, tweesterCapsuleSpaceOdds12, tweesterCapsuleSpaceOdds34, thwompCapsulePrice12, thwompCapsulePrice34, thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, thwompCapsuleSpaceOdds12, thwompCapsuleSpaceOdds34, warpCapsulePrice12, warpCapsulePrice34, warpCapsuleShopOdds12, warpCapsuleShopOdds34, warpCapsuleSpaceOdds12, warpCapsuleSpaceOdds34, bombCapsulePrice12, bombCapsulePrice34, bombCapsuleShopOdds12, bombCapsuleShopOdds34, bombCapsuleSpaceOdds12, bombCapsuleSpaceOdds34, fireballCapsulePrice12, fireballCapsulePrice34, fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, fireballCapsuleSpaceOdds12, fireballCapsuleSpaceOdds34, flowerCapsulePrice12, flowerCapsulePrice34, flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, flowerCapsuleSpaceOdds12, flowerCapsuleSpaceOdds34, eggCapsulePrice12, eggCapsulePrice34, eggCapsuleShopOdds12, eggCapsuleShopOdds34, eggCapsuleSpaceOdds12, eggCapsuleSpaceOdds34, vacuumCapsulePrice12, vacuumCapsulePrice34, vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, vacuumCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds34, magicCapsulePrice12, magicCapsulePrice34, magicCapsuleShopOdds12, magicCapsuleShopOdds34, magicCapsuleSpaceOdds12, magicCapsuleSpaceOdds34, tripleCapsulePrice12, tripleCapsulePrice34, tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, tripleCapsuleSpaceOdds12, tripleCapsuleSpaceOdds34, koopaCapsulePrice12, koopaCapsulePrice34, koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, koopaCapsuleSpaceOdds12, koopaCapsuleSpaceOdds34, poisonMushroomPrice34, poisonMushroomPrice12, poisonMushroomShopOdds12, poisonMushroomShopOdds34, poisonMushroomSpaceOdds12, poisonMushroomSpaceOdds34, orbBagCapsulePrice34, orbBagCapsulePrice12, orbBagCapsuleShopOdds12, orbBagCapsuleShopOdds34, orbBagCapsuleSpaceOdds12, orbBagCapsuleSpaceOdds34, mysteryCapsulePrice34, mysteryCapsulePrice12, mysteryCapsuleShopOdds12, mysteryCapsuleShopOdds34, mysteryCapsuleSpaceOdds12, mysteryCapsuleSpaceOdds34, dkCapsulePrice34, dkCapsulePrice12, dkCapsuleShopOdds12, dkCapsuleShopOdds34, dkCapsuleSpaceOdds12, dkCapsuleSpaceOdds34, duelCapsulePrice34, duelCapsulePrice12, duelCapsuleShopOdds12, duelCapsuleShopOdds34, duelCapsuleSpaceOdds12, duelCapsuleSpaceOdds34):
    return f'''
MP7 - Orb Modifer
042EF588 00{mushroomCapsulePrice12}{mushroomCapsulePrice12}{mushroomCapsulePrice34}
042EF58C {mushroomCapsuleSpaceOdds12}{mushroomCapsuleSpaceOdds12}{mushroomCapsuleSpaceOdds34}{mushroomCapsuleSpaceOdds34}
042EF590 {mushroomCapsuleSpaceOdds12}{mushroomCapsuleSpaceOdds12}{mushroomCapsuleSpaceOdds34}{mushroomCapsuleSpaceOdds34}
042EF594 {mushroomCapsuleShopOdds12}{mushroomCapsuleShopOdds34}0000
042EF598 01{goldenMushroomCapsulePrice12}{goldenMushroomCapsulePrice12}{goldenMushroomCapsulePrice34}
042EF59C {goldenMushroomCapsuleSpaceOdds12}{goldenMushroomCapsuleSpaceOdds12}{goldenMushroomCapsuleSpaceOdds34}{goldenMushroomCapsuleSpaceOdds34}
042EF5A0 {goldenMushroomCapsuleSpaceOdds12}{goldenMushroomCapsuleSpaceOdds12}{goldenMushroomCapsuleSpaceOdds34}{goldenMushroomCapsuleSpaceOdds34}
042EF5A4 {goldenMushroomCapsuleShopOdds12}{goldenMushroomCapsuleShopOdds34}0000
042EF5A8 02{slowMushroomCapsulePrice12}{slowMushroomCapsulePrice12}{slowMushroomCapsulePrice34}
042EF5AC {slowMushroomCapsuleSpaceOdds12}{slowMushroomCapsuleSpaceOdds12}{slowMushroomCapsuleSpaceOdds34}{slowMushroomCapsuleSpaceOdds34}
042EF5B0 {slowMushroomCapsuleSpaceOdds12}{slowMushroomCapsuleSpaceOdds12}{slowMushroomCapsuleSpaceOdds34}{slowMushroomCapsuleSpaceOdds34}
042EF5B4 {slowMushroomCapsuleShopOdds12}{slowMushroomCapsuleShopOdds34}0000
042EF5B8 03{metalMushroomCapsulePrice12}{metalMushroomCapsulePrice12}{metalMushroomCapsulePrice34}
042EF5BC {metalMushroomCapsuleSpaceOdds12}{metalMushroomCapsuleSpaceOdds12}{metalMushroomCapsuleSpaceOdds34}{metalMushroomCapsuleSpaceOdds34}
042EF5C0 {metalMushroomCapsuleSpaceOdds12}{metalMushroomCapsuleSpaceOdds12}{metalMushroomCapsuleSpaceOdds34}{metalMushroomCapsuleSpaceOdds34}
042EF5C4 {metalMushroomCapsuleShopOdds12}{metalMushroomCapsuleShopOdds34}0000
042EF5C8 04{flutterCapsulePrice12}{flutterCapsulePrice12}{flutterCapsulePrice34}
042EF5CC {flutterCapsuleSpaceOdds12}{flutterCapsuleSpaceOdds12}{flutterCapsuleSpaceOdds34}{flutterCapsuleSpaceOdds34}
042EF5D0 {flutterCapsuleSpaceOdds12}{flutterCapsuleSpaceOdds12}{flutterCapsuleSpaceOdds34}{flutterCapsuleSpaceOdds34}
042EF5D4 {flutterCapsuleShopOdds12}{flutterCapsuleShopOdds34}0000
042EF5D8 05{cannonCapsulePrice12}{cannonCapsulePrice12}{cannonCapsulePrice34}
042EF5DC {cannonCapsuleSpaceOdds12}{cannonCapsuleSpaceOdds12}{cannonCapsuleSpaceOdds34}{cannonCapsuleSpaceOdds34}
042EF5E0 {cannonCapsuleSpaceOdds12}{cannonCapsuleSpaceOdds12}{cannonCapsuleSpaceOdds34}{cannonCapsuleSpaceOdds34}
042EF5E4 {cannonCapsuleShopOdds12}{cannonCapsuleShopOdds34}0000
042EF5E8 06{snackCapsulePrice12}{snackCapsulePrice12}{snackCapsulePrice34}
042EF5EC {snackCapsuleSpaceOdds12}{snackCapsuleSpaceOdds12}{snackCapsuleSpaceOdds34}{snackCapsuleSpaceOdds34}
042EF5F0 {snackCapsuleSpaceOdds12}{snackCapsuleSpaceOdds12}{snackCapsuleSpaceOdds34}{snackCapsuleSpaceOdds34}
042EF5F4 {snackCapsuleShopOdds12}{snackCapsuleShopOdds34}0000
042EF5F8 07{lakituCapsulePrice12}{lakituCapsulePrice12}{lakituCapsulePrice34}
042EF5FC {lakituCapsuleSpaceOdds12}{lakituCapsuleSpaceOdds12}{lakituCapsuleSpaceOdds34}{lakituCapsuleSpaceOdds34}
042EF600 {lakituCapsuleSpaceOdds12}{lakituCapsuleSpaceOdds12}{lakituCapsuleSpaceOdds34}{lakituCapsuleSpaceOdds34}
042EF604 {lakituCapsuleShopOdds12}{lakituCapsuleShopOdds34}0000
042EF608 0A{hammerBroCapsulePrice12}{hammerBroCapsulePrice12}{hammerBroCapsulePrice34}
042EF60C {hammerBroCapsuleSpaceOdds12}{hammerBroCapsuleSpaceOdds12}{hammerBroCapsuleSpaceOdds34}{hammerBroCapsuleSpaceOdds34}
042EF610 {hammerBroCapsuleSpaceOdds12}{hammerBroCapsuleSpaceOdds12}{hammerBroCapsuleSpaceOdds34}{hammerBroCapsuleSpaceOdds34}
042EF614 {hammerBroCapsuleShopOdds12}{hammerBroCapsuleShopOdds34}0000
042EF618 0B{piranhaPlantCapsulePrice12}{piranhaPlantCapsulePrice12}{piranhaPlantCapsulePrice34}
042EF61C {piranhaPlantCapsuleSpaceOdds12}{piranhaPlantCapsuleSpaceOdds12}{piranhaPlantCapsuleSpaceOdds34}{piranhaPlantCapsuleSpaceOdds34}
042EF620 {piranhaPlantCapsuleSpaceOdds12}{piranhaPlantCapsuleSpaceOdds12}{piranhaPlantCapsuleSpaceOdds34}{piranhaPlantCapsuleSpaceOdds34}
042EF624 {piranhaPlantCapsuleShopOdds12}{piranhaPlantCapsuleShopOdds34}0000
042EF628 0C{spearGuyCapsulePrice12}{spearGuyCapsulePrice12}{spearGuyCapsulePrice34}
042EF62C {spearGuyCapsuleSpaceOdds12}{spearGuyCapsuleSpaceOdds12}{spearGuyCapsuleSpaceOdds34}{spearGuyCapsuleSpaceOdds34}
042EF630 {spearGuyCapsuleSpaceOdds12}{spearGuyCapsuleSpaceOdds12}{spearGuyCapsuleSpaceOdds34}{spearGuyCapsuleSpaceOdds34}
042EF634 {spearGuyCapsuleShopOdds12}{spearGuyCapsuleShopOdds34}0000
042EF638 0D{kamekCapsulePrice12}{kamekCapsulePrice12}{kamekCapsulePrice34}
042EF63C {kamekCapsuleSpaceOdds12}{kamekCapsuleSpaceOdds12}{kamekCapsuleSpaceOdds34}{kamekCapsuleSpaceOdds34}
042EF640 {kamekCapsuleSpaceOdds12}{kamekCapsuleSpaceOdds12}{kamekCapsuleSpaceOdds34}{kamekCapsuleSpaceOdds34}
042EF644 {kamekCapsuleShopOdds12}{kamekCapsuleShopOdds34}0000
042EF648 0E{toadyCapsulePrice12}{toadyCapsulePrice12}{toadyCapsulePrice34}
042EF64C {toadyCapsuleSpaceOdds12}{toadyCapsuleSpaceOdds12}{toadyCapsuleSpaceOdds34}{toadyCapsuleSpaceOdds34}
042EF650 {toadyCapsuleSpaceOdds12}{toadyCapsuleSpaceOdds12}{toadyCapsuleSpaceOdds34}{toadyCapsuleSpaceOdds34}
042EF654 {toadyCapsuleShopOdds12}{toadyCapsuleShopOdds34}0000
042EF658 0F{mrBlizzardCapsulePrice12}{mrBlizzardCapsulePrice12}{mrBlizzardCapsulePrice34}
042EF65C {mrBlizzardCapsuleSpaceOdds12}{mrBlizzardCapsuleSpaceOdds12}{mrBlizzardCapsuleSpaceOdds34}{mrBlizzardCapsuleSpaceOdds34}
042EF660 {mrBlizzardCapsuleSpaceOdds12}{mrBlizzardCapsuleSpaceOdds12}{mrBlizzardCapsuleSpaceOdds34}{mrBlizzardCapsuleSpaceOdds34}
042EF664 {mrBlizzardCapsuleShopOdds12}{mrBlizzardCapsuleShopOdds34}0000
042EF668 10{banditCapsulePrice12}{banditCapsulePrice12}{banditCapsulePrice34}
042EF66C {banditCapsuleSpaceOdds12}{banditCapsuleSpaceOdds12}{banditCapsuleSpaceOdds34}{banditCapsuleSpaceOdds34}
042EF670 {banditCapsuleSpaceOdds12}{banditCapsuleSpaceOdds12}{banditCapsuleSpaceOdds34}{banditCapsuleSpaceOdds34}
042EF674 {banditCapsuleShopOdds12}{banditCapsuleShopOdds34}0000
042EF678 11{pinkBooCapsulePrice12}{pinkBooCapsulePrice12}{pinkBooCapsulePrice34}
042EF67C {pinkBooCapsuleSpaceOdds12}{pinkBooCapsuleSpaceOdds12}{pinkBooCapsuleSpaceOdds34}{pinkBooCapsuleSpaceOdds34}
042EF680 {pinkBooCapsuleSpaceOdds12}{pinkBooCapsuleSpaceOdds12}{pinkBooCapsuleSpaceOdds34}{pinkBooCapsuleSpaceOdds34}
042EF684 {pinkBooCapsuleShopOdds12}{pinkBooCapsuleShopOdds34}0000
042EF688 14{spinyCapsulePrice12}{spinyCapsulePrice12}{spinyCapsulePrice34}
042EF68C {spinyCapsuleSpaceOdds12}{spinyCapsuleSpaceOdds12}{spinyCapsuleSpaceOdds34}{spinyCapsuleSpaceOdds34}
042EF690 {spinyCapsuleSpaceOdds12}{spinyCapsuleSpaceOdds12}{spinyCapsuleSpaceOdds34}{spinyCapsuleSpaceOdds34}
042EF694 {spinyCapsuleShopOdds12}{spinyCapsuleShopOdds34}0000
042EF698 15{zapCapsulePrice12}{zapCapsulePrice12}{zapCapsulePrice34}
042EF69C {zapCapsuleSpaceOdds12}{zapCapsuleSpaceOdds12}{zapCapsuleSpaceOdds34}{zapCapsuleSpaceOdds34}
042EF6A0 {zapCapsuleSpaceOdds12}{zapCapsuleSpaceOdds12}{zapCapsuleSpaceOdds34}{zapCapsuleSpaceOdds34}
042EF6A4 {zapCapsuleShopOdds12}{zapCapsuleShopOdds34}0000
042EF6A8 16{tweesterCapsulePrice12}{tweesterCapsulePrice12}{tweesterCapsulePrice34}
042EF6AC {tweesterCapsuleSpaceOdds12}{tweesterCapsuleSpaceOdds12}{tweesterCapsuleSpaceOdds34}{tweesterCapsuleSpaceOdds34}
042EF6B0 {tweesterCapsuleSpaceOdds12}{tweesterCapsuleSpaceOdds12}{tweesterCapsuleSpaceOdds34}{tweesterCapsuleSpaceOdds34}
042EF6B4 {tweesterCapsuleShopOdds12}{tweesterCapsuleShopOdds34}0000
042EF6B8 17{thwompCapsulePrice12}{thwompCapsulePrice12}{thwompCapsulePrice34}
042EF6BC {thwompCapsuleSpaceOdds12}{thwompCapsuleSpaceOdds12}{thwompCapsuleSpaceOdds34}{thwompCapsuleSpaceOdds34}
042EF6C0 {thwompCapsuleSpaceOdds12}{thwompCapsuleSpaceOdds12}{thwompCapsuleSpaceOdds34}{thwompCapsuleSpaceOdds34}
042EF6C4 {thwompCapsuleShopOdds12}{thwompCapsuleShopOdds34}0000
042EF6C8 18{warpCapsulePrice12}{warpCapsulePrice12}{warpCapsulePrice34}
042EF6CC {warpCapsuleSpaceOdds12}{warpCapsuleSpaceOdds12}{warpCapsuleSpaceOdds34}{warpCapsuleSpaceOdds34}
042EF6D0 {warpCapsuleSpaceOdds12}{warpCapsuleSpaceOdds12}{warpCapsuleSpaceOdds34}{warpCapsuleSpaceOdds34}
042EF6D4 {warpCapsuleShopOdds12}{warpCapsuleShopOdds34}0000
042EF6D8 19{bombCapsulePrice12}{bombCapsulePrice12}{bombCapsulePrice34}
042EF6DC {bombCapsuleSpaceOdds12}{bombCapsuleSpaceOdds12}{bombCapsuleSpaceOdds34}{bombCapsuleSpaceOdds34}
042EF6E0 {bombCapsuleSpaceOdds12}{bombCapsuleSpaceOdds12}{bombCapsuleSpaceOdds34}{bombCapsuleSpaceOdds34}
042EF6E4 {bombCapsuleShopOdds12}{bombCapsuleShopOdds34}0000
042EF6E8 1E{fireballCapsulePrice12}{fireballCapsulePrice12}{fireballCapsulePrice34}
042EF6EC {fireballCapsuleSpaceOdds12}{fireballCapsuleSpaceOdds12}{fireballCapsuleSpaceOdds34}{fireballCapsuleSpaceOdds34}
042EF6F0 {fireballCapsuleSpaceOdds12}{fireballCapsuleSpaceOdds12}{fireballCapsuleSpaceOdds34}{fireballCapsuleSpaceOdds34}
042EF6F4 {fireballCapsuleShopOdds12}{fireballCapsuleShopOdds34}0000
042EF6F8 1F{flowerCapsulePrice12}{flowerCapsulePrice12}{flowerCapsulePrice34}
042EF6FC {flowerCapsuleSpaceOdds12}{flowerCapsuleSpaceOdds12}{flowerCapsuleSpaceOdds34}{flowerCapsuleSpaceOdds34}
042EF700 {flowerCapsuleSpaceOdds12}{flowerCapsuleSpaceOdds12}{flowerCapsuleSpaceOdds34}{flowerCapsuleSpaceOdds34}
042EF704 {flowerCapsuleShopOdds12}{flowerCapsuleShopOdds34}0000
042EF708 20{eggCapsulePrice12}{eggCapsulePrice12}{eggCapsulePrice34}
042EF70C {eggCapsuleSpaceOdds12}{eggCapsuleSpaceOdds12}{eggCapsuleSpaceOdds34}{eggCapsuleSpaceOdds34}
042EF710 {eggCapsuleSpaceOdds12}{eggCapsuleSpaceOdds12}{eggCapsuleSpaceOdds34}{eggCapsuleSpaceOdds34}
042EF714 {eggCapsuleShopOdds12}{eggCapsuleShopOdds34}0000
042EF718 21{vacuumCapsulePrice12}{vacuumCapsulePrice12}{vacuumCapsulePrice34}
042EF71C {vacuumCapsuleSpaceOdds12}{vacuumCapsuleSpaceOdds12}{vacuumCapsuleSpaceOdds34}{vacuumCapsuleSpaceOdds34}
042EF720 {vacuumCapsuleSpaceOdds12}{vacuumCapsuleSpaceOdds12}{vacuumCapsuleSpaceOdds34}{vacuumCapsuleSpaceOdds34}
042EF724 {vacuumCapsuleShopOdds12}{vacuumCapsuleShopOdds34}0000
042EF728 22{magicCapsulePrice12}{magicCapsulePrice12}{magicCapsulePrice34}
042EF72C {magicCapsuleSpaceOdds12}{magicCapsuleSpaceOdds12}{magicCapsuleSpaceOdds34}{magicCapsuleSpaceOdds34}
042EF730 {magicCapsuleSpaceOdds12}{magicCapsuleSpaceOdds12}{magicCapsuleSpaceOdds34}{magicCapsuleSpaceOdds34}
042EF734 {magicCapsuleShopOdds12}{magicCapsuleShopOdds34}0000
042EF738 23{tripleCapsulePrice12}{tripleCapsulePrice12}{tripleCapsulePrice34}
042EF73C {tripleCapsuleSpaceOdds12}{tripleCapsuleSpaceOdds12}{tripleCapsuleSpaceOdds34}{tripleCapsuleSpaceOdds34}
042EF740 {tripleCapsuleSpaceOdds12}{tripleCapsuleSpaceOdds12}{tripleCapsuleSpaceOdds34}{tripleCapsuleSpaceOdds34}
042EF744 {tripleCapsuleShopOdds12}{tripleCapsuleShopOdds34}0000
042EF748 28{koopaCapsulePrice12}{koopaCapsulePrice12}{koopaCapsulePrice34}
042EF74C {koopaCapsuleSpaceOdds12}{koopaCapsuleSpaceOdds12}{koopaCapsuleSpaceOdds34}{koopaCapsuleSpaceOdds34}
042EF750 {koopaCapsuleSpaceOdds12}{koopaCapsuleSpaceOdds12}{koopaCapsuleSpaceOdds34}{koopaCapsuleSpaceOdds34}
042EF754 {koopaCapsuleShopOdds12}{koopaCapsuleShopOdds34}0000
042EF758 08{duelCapsulePrice12}{duelCapsulePrice12}{duelCapsulePrice34}
042EF75C {duelCapsuleSpaceOdds12}{duelCapsuleSpaceOdds12}{duelCapsuleSpaceOdds34}{duelCapsuleSpaceOdds34}
042EF760 {duelCapsuleSpaceOdds12}{duelCapsuleSpaceOdds12}{duelCapsuleSpaceOdds34}{duelCapsuleSpaceOdds34}
042EF764 {duelCapsuleShopOdds12}{duelCapsuleShopOdds34}0000
042EF768 09{dkCapsulePrice12}{dkCapsulePrice12}{dkCapsulePrice34}
042EF76C {dkCapsuleSpaceOdds12}{dkCapsuleSpaceOdds12}{dkCapsuleSpaceOdds34}{dkCapsuleSpaceOdds34}
042EF770 {dkCapsuleSpaceOdds12}{dkCapsuleSpaceOdds12}{dkCapsuleSpaceOdds34}{dkCapsuleSpaceOdds34}
042EF774 {dkCapsuleShopOdds12}{dkCapsuleShopOdds34}0000
042EF778 32{poisonMushroomPrice12}{poisonMushroomPrice12}{poisonMushroomPrice34}
042EF78C {poisonMushroomSpaceOdds12}{poisonMushroomSpaceOdds12}{poisonMushroomSpaceOdds34}{poisonMushroomSpaceOdds34}
042EF790 {poisonMushroomSpaceOdds12}{poisonMushroomSpaceOdds12}{poisonMushroomSpaceOdds34}{poisonMushroomSpaceOdds34}
042EF794 {poisonMushroomShopOdds12}{poisonMushroomShopOdds34}0000
042EF798 33{orbBagCapsulePrice12}{orbBagCapsulePrice12}{orbBagCapsulePrice34}
042EF79C {orbBagCapsuleSpaceOdds12}{orbBagCapsuleSpaceOdds12}{orbBagCapsuleSpaceOdds34}{orbBagCapsuleSpaceOdds34}
042EF7A0 {orbBagCapsuleSpaceOdds12}{orbBagCapsuleSpaceOdds12}{orbBagCapsuleSpaceOdds34}{orbBagCapsuleSpaceOdds34}
042EF7A4 {orbBagCapsuleShopOdds12}{orbBagCapsuleShopOdds34}0000
042EF7A8 35{mysteryCapsulePrice12}{mysteryCapsulePrice12}{mysteryCapsulePrice34}
042EF7AC {mysteryCapsuleSpaceOdds12}{mysteryCapsuleSpaceOdds12}{mysteryCapsuleSpaceOdds34}{mysteryCapsuleSpaceOdds34}
042EF7B0 {mysteryCapsuleSpaceOdds12}{mysteryCapsuleSpaceOdds12}{mysteryCapsuleSpaceOdds34}{mysteryCapsuleSpaceOdds34}
042EF7B4 {mysteryCapsuleShopOdds12}{mysteryCapsuleShopOdds34}0000
042EF7B8 FF000000
042EF7BC 00000000
042EF7C0 00000000
042EF7C4 00000000
'''

def getInitialItemsSeven(one, two, three, four, five, oneItem, twoItem, threeItem, fourItem, fiveItem):
    return f'''
MP7 - Start with {oneItem}, {twoItem}, and {threeItem}
06003620 00000030
3D808000 618C363C
1C060005 7C005A14
7C8C00AE 98830006
48164338 {one}{two}{three}{four}
{five}{one}{two}{three} {four}{five}{one}{two}
{three}{four}{five}{one} {two}{three}{four}{five}
0416796C 4BE9BCB4
'''

def getSpaceReplaceSeven1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP7 - Replace {spaceName} with {spaceName2} (Slot A)
C217942C 00000005
A01F0030 280000{spaceHex1}
40820018 A09F0032
2804FFFF 4082000C
380000{spaceHex2} B01F0030
60000000 00000000
'''

def getSpaceReplaceSeven2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP7 - Replace {spaceName} with {spaceName2} (Slot B)
C2179430 00000005
280000{spaceHex1} 40820018
A09F0032 2804FFFF
4082000C 380000{spaceHex2}
B01F0030 5404083C
60000000 00000000
'''

def getWindmillMaxSeven(amount, amountDec):
    return f'''
MP7 - Windmillville: Invest Up To {amountDec}
204E4C7C 2C040064
044E4C7C 2C04{amount}
E2000001 80008000
204E4CCC 2C040064
044E4CCC 2C04{amount}
E2000001 80008000
'''

def getStarHandicap(p1, p2, p3, p4):
    return f'''
MP7 - Star Handicap
20290CC4 00000000
02290CD0 0000{p1}
02290DE0 0000{p2}
02290EF0 0000{p3}
02291000 0000{p4}
E2000001 80008000
'''

def getSpinxEvent(a, b):
    return f'''
MP7 - Pyramid Park: Spinx Event is Always {b}
282F2F3E 0000007C
28290CA8 0000004D
28291522 00000023
0052449F 000000{a}
E2000002 80008000
28290DB8 0000004D
28291522 00000123
0052449F 000000{a}
E2000002 80008000
28290EC8 0000004D
28291522 00000223
0052449F 000000{a}
E2000002 80008000
28290FD8 0000004D
28291522 00000323
0052449F 000000{a}
E2000003 80008000
'''

def getGliderEvent(a, b):
    return f'''
MP7 - Windmillvlle: Flower Glider Always Goes To
282F2F3E 0000007E
28290CA8 00000031
28291522 0000001A
026370B2 000000{a}
E2000002 80008000
28290DB8 00000031
28291522 0000011A
026370B2 000000{a}
E2000002 80008000
28290EC8 00000031
28291522 0000021A
026370B2 000000{a}
E2000002 80008000
28290FD8 00000031
28291522 0000031A
026370B2 000000{a}
E2000003 80008000
'''

def getGliderCostEvent(a, b, c):
    return f'''
MP7 - Windmillville: Flower Glider Costs {c}
282F2F3E 0000007E
284E73AE 0000000A
024E73AE 0000{a}
E2000001 80008000
284E7D12 0000FFF6
024E7D12 0000{b}
E2000002 80008000
'''

def getBlackChomp(a, b):
    return f'''
MP7 - Pyramid Park: Standard Chomp Costs {b}
282F2F3E 0000007C
28511722 0000000A
02511722 0000{a}
E2000002 80008000
'''

def getRedChomp(a, b):
    return f'''
MP7 - Pyramid Park: Red Chomp Costs {b}
282F2F3E 0000007C
28511726 0000000A
02511726 0000{a}
E2000002 80008000
'''

def initialCoinsMod7(hex, hexDec):
    return f'''
MP7 - Gain {hexDec} Coins at the Start of the Game
02196D12 0000{hex}
02151DEA 0000{hex}
'''

def getBattleGame7(p1, p2, p3, p4, p5, s1, s2, s3, s4, s5):
    return f'''
MP7 - Battle Minigames Bounties are {s1}, {s2}, {s3}, {s4}, and {s5}
04276F34 0000{p1}
04276F38 0000{p2}
04276F3C 0000{p3}
04276F40 0000{p4}
04276F44 0000{p5}
04276F48 0000{p5}
042215E0 60000000
'''

def getStarReplaceSeven1(amount, amountDec):
    return f'''
MP7 - Replace Minigame Star with {amountDec}
204E185C A8A70028
044E185C {amount}
E2000001 80008000
'''

def getStarReplaceSeven2(amount, amountDec):
    return f'''
MP7 - Replace Orb Star with {amountDec}
204E18D4 A8C3003C
044E18D4 {amount}
E2000001 80008000
'''

def getStarReplaceSeven3(amount, amountDec):
    return f'''
MP7 - Replace Happening Star with {amountDec}
204E1A0C 8903001F
044E1A0C {amount}
E2000001 80008000
204E1A10 7D060774
044E1A10 7D064378
E2000001 80008000
'''

def getStarReplaceSeven4(amount, amountDec):
    return f'''
MP7 - Replace Shopping Star with {amountDec}
204E1898 A885003E
044E1898 {amount}
E2000001 80008000
'''

def getStarReplaceSeven5(amount, amountDec):
    return f'''
MP7 - Replace Running Star with {amountDec}
204E1910 A8C40018
044E1910 {amount}
E2000001 80008000
'''

def getStarReplaceSeven6(amount, amountDec):
    return f'''
MP7 - Replace Running Star with {amountDec}
204E198C 8904001D
044E198C {amount}
E2000001 80008000
204E1990 7D060774
044E1990 7D064378
E2000001 80008000
'''