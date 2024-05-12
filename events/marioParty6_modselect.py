# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

from codes.marioParty6 import *
from functions import *

import pyperclip


def modSelect_mp6(checkboxTankAir, checkboxsameSpaceNever, checkboxsameSpaceAlways, checkbox30hz, checkboxBattlMinigame, checkboxCoinStar, checkboxPermaPaths, checkboxRandomMus, checkboxAdvTxt, checkboxChangeTurnCount, checkboxDisableAdv, checkboxDisableMusic, checkboxBoot, checkboxBSpeed, checkboxTaunt, checkboxOrbThrow, checkboxTxtDisplay, checkboxShowCtrl, checkboxUnlockAll, checkboxZtarCoins, checkboxHapFaire, checkboxLakeRoll, checkboxLakeSellStar, checkboxLakeRollLowerThan5, checkboxAlwaysSneeze, checkboxDoubleTurns, checkboxLakeStart3, checkboxForceLast5, comboboxLast5Event, checkboxLastTOrbs, checkboxPPALL, checkbox3Jump, checkboxDizzy, checkboxInsectiride, checkboxQuickerFinish, checkboxTiesareTies, checkboxPermDeath, checkboxSlowerLazer, checkboxStageFright, checkboxNoTrail):
    if checkboxTankAir.get() == 0 and checkboxsameSpaceNever.get() == 0 and checkboxsameSpaceAlways.get() == 0 and checkbox30hz.get() == 0 and checkboxBattlMinigame.get() == 0 and checkboxCoinStar.get() == 0 and checkboxPermaPaths.get() == 0 and checkboxRandomMus.get() == 0 and checkboxAdvTxt.get() == 0 and checkboxChangeTurnCount.get() == 0 and checkboxDisableAdv.get() == 0 and checkboxDisableMusic.get() == 0 and checkboxBoot.get() == 0 and checkboxBSpeed.get() == 0 and checkboxTaunt.get() == 0 and checkboxOrbThrow.get() == 0 and checkboxTxtDisplay.get() == 0 and checkboxShowCtrl.get() == 0 and checkboxUnlockAll.get() == 0 and checkboxZtarCoins.get() == 0 and checkboxHapFaire.get() == 0 and checkboxLakeRoll.get() == 0 and checkboxLakeSellStar.get() == 0 and checkboxLakeRollLowerThan5.get() == 0 and checkboxAlwaysSneeze.get() == 0 and checkboxDoubleTurns.get() == 0 and checkboxLakeStart3.get() == 0 and checkboxForceLast5.get() == 0 and checkboxLastTOrbs.get() == 0 and checkboxPPALL.get() == 0 and checkbox3Jump.get() == 0 and checkboxDizzy.get() == 0 and checkboxInsectiride.get() == 0 and checkboxQuickerFinish.get() == 0 and checkboxTiesareTies.get() == 0 and checkboxPermDeath.get() == 0 and checkboxSlowerLazer.get() == 0 and checkboxStageFright.get() == 0 and checkboxNoTrail.get == 0 and comboboxLast5Event.get() == "Random" and comboboxLast5Event.get() == "Normal (3 Turns)":
        createDialog("Error", "error", "Please check at least 1 box.", None)
        return
    
    generatedCode = '''MP6 - Mods'''
    
    ticked = checkbox30hz.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("30Hz")
    
    ticked = checkboxBattlMinigame.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("BattleMinigame")

    ticked = checkboxCoinStar.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("CoinStar")

    ticked = checkboxPermaPaths.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("PermaPaths")

    ticked = checkboxRandomMus.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("RandomMusic")

    ticked = checkboxAdvTxt.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("AdvanceText")
    
    ticked = checkboxChangeTurnCount.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("ChangeTurnCount")
    
    ticked = checkboxDisableAdv.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("DisableAdv")

    ticked = checkboxDisableMusic.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("DisableMus")

    ticked = checkboxBoot.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("Boot")

    ticked = checkboxBSpeed.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("BSpeed")

    ticked = checkboxTaunt.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("TSpam")

    ticked = checkboxOrbThrow.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("OThrow")

    ticked = checkboxTxtDisplay.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("TxtDisplay")

    ticked = checkboxShowCtrl.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("ShowCtrl")
    
    ticked = checkboxUnlockAll.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("UnlockAll")
    
    ticked = checkboxZtarCoins.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("ZtarC")
    
    ticked = checkboxHapFaire.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("FaireHappening")
    
    ticked = checkboxLakeRoll.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("LakeRoll")
    
    ticked = checkboxLakeSellStar.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("LakeSellStar")
    
    ticked = checkboxLakeRollLowerThan5.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("LakeRollPlus5")
    
    ticked = checkboxAlwaysSneeze.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("AlwaysSneeze")
    
    ticked = checkboxDoubleTurns.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("DoubleTurns")
    
    ticked = checkboxLakeStart3.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("LakeStart3")
    
    ticked = checkboxForceLast5.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("ForceL5")
    
    ticked = checkboxLastTOrbs.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("LastTOrbs")

    ticked = checkboxPPALL.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("PPAll")

    ticked = checkbox3Jump.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("3Jump")
    
    ticked = checkboxDizzy.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("DizzyR")
    
    ticked = checkboxInsectiride.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("Insectiride")
    
    ticked = checkboxQuickerFinish.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("QuickFinish")
    
    ticked = checkboxTiesareTies.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("TiesAreTies")
    
    ticked = checkboxPermDeath.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("PermDeath")

    ticked = checkboxSlowerLazer.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("SlowerLazer")
    
    ticked = checkboxStageFright.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("StageFright")
    
    choice = checkboxsameSpaceAlways.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("SameSpaceAlways")

    ticked = checkboxsameSpaceNever.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("SameSpaceNever")

    ticked = checkboxTankAir.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesSix("TankAir")

    choice = checkboxNoTrail.get()
    if choice == "x2 Coins":
        generatedCode = generatedCode + getOtherCodesSix("NoTrail")

    choice = comboboxLast5Event.get()
    if choice == "40 Coins":
        generatedCode = generatedCode + getOtherCodesSix("40 Coins")
    
    choice = comboboxLast5Event.get()
    if choice == "5 Character Spaces":
        generatedCode = generatedCode + getOtherCodesSix("5 Character Spaces")
    
    choice = comboboxLast5Event.get()
    if choice == "Bowser Revolution":
        generatedCode = generatedCode + getOtherCodesSix("Bowser Revolution")

    choice = comboboxLast5Event.get()
    if choice == "Disabled":
        generatedCode = generatedCode + getOtherCodesSix("Disabled")

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)