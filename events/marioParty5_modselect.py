# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

from codes.marioParty5 import *
from functions import *

import pyperclip


def modSelect_mp5(checkboxDisableAdv, checkboxDisableMus, checkboxBoot, checkboxBSpeed, checkboxCSpeed, checkboxTaunt, checkboxTxtDisplay, checkboxShowCtrl, checkboxUnlockAll, checkboxBowserNoStealCoins, checkbox60RocketShip, checkboxFreeTaxi, checkboxFreeThwmopWhomp, checkboxFreeBridge, checkboxDisableHappening, checkboxAdvTxt, checkboxAllDK, checkboxBattleNoStar, checkboxCapsulesAny, checkboxDoubleTurns, checkboxCapsulesFinal, checkboxsameSpaceAlways, checkboxsameSpaceNever, checkbox20Sec, checkboxNoBrick, checkbox1Slow, checkboxNoSlow, checkboxFlowers3, checkboxNoRocks, checkboxLeafDisplay, checkboxHalvedTime, checkboxForceLast5, comboboxLast5Event):
    if checkboxDisableAdv.get() == 0 and checkboxDisableMus.get() == 0 and checkboxBoot.get() == 0 and checkboxBSpeed.get() == 0 and checkboxCSpeed.get() == 0 and checkboxTaunt.get() == 0 and checkboxTxtDisplay.get() == 0 and checkboxShowCtrl.get() == 0 and checkboxUnlockAll.get() == 0 and checkboxBowserNoStealCoins.get() == 0 and checkbox60RocketShip.get() == 0 and checkboxFreeTaxi.get() == 0 and checkboxFreeThwmopWhomp.get() == 0 and checkboxFreeBridge.get() == 0 and checkboxDisableHappening.get() == 0 and checkboxAdvTxt.get() == 0 and checkboxAllDK.get() == 0 and checkboxBattleNoStar.get() == 0 and checkboxCapsulesAny.get() == 0 and checkboxDoubleTurns.get() == 0 and checkboxCapsulesFinal.get() == 0 and checkboxsameSpaceAlways.get() == 0 and checkboxsameSpaceNever.get() == 0  and checkbox20Sec.get() == 0 and checkboxNoBrick.get() == 0 and checkbox1Slow.get() == 0 and checkboxNoSlow.get() == 0 and checkboxFlowers3.get() == 0 and checkboxNoRocks.get() == 0 and checkboxLeafDisplay.get() == 0 and checkboxHalvedTime.get() == 0 and checkboxForceLast5.get() == 0 and comboboxLast5Event.get() == "Random":
        createDialog("Error", "error", "Please check at least 1 box.", None)
        return
    
    generatedCode = '''MP5 - Mods'''
    
    ticked = checkboxDisableAdv.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("DisableAdv")
    
    ticked = checkboxDisableMus.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("DisableMusic")

    ticked = checkboxBoot.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("Boot")
    
    ticked = checkboxBSpeed.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("BSpeed")
    
    ticked = checkboxCSpeed.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("CSpeed")
    
    ticked = checkboxTaunt.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("Taunt")
    
    ticked = checkboxTxtDisplay.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("TxtDisplay")
    
    ticked = checkboxShowCtrl.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("ShowCtrl")
    
    ticked = checkboxUnlockAll.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("UnlockAll")
    
    ticked = checkboxBowserNoStealCoins.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("BowserNoStealCoins")
    
    ticked = checkbox60RocketShip.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("60RocketShip")
    
    ticked = checkboxFreeTaxi.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("FreeTaxi")
    
    ticked = checkboxFreeThwmopWhomp.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("FreeThwmopWhomp")
    
    ticked = checkboxFreeBridge.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("FreeBridge")
    
    ticked = checkboxDisableHappening.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("DisableHappening")
    
    ticked = checkboxAdvTxt.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("AdvTxt")
    
    ticked = checkboxAllDK.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("AllDK")
    
    ticked = checkboxBattleNoStar.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("BattleNoStar")
    
    ticked = checkboxCapsulesAny.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("CapsulesAny")
    
    ticked = checkboxDoubleTurns.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("DoubleTurns")
    
    ticked = checkboxCapsulesFinal.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("CapsulesFinal")

    ticked = checkboxsameSpaceAlways.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("sameSpaceAlways")

    ticked = checkboxsameSpaceNever.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("sameSpaceNever")
    
    ticked = checkbox20Sec.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("20Sec")
    
    ticked = checkboxNoBrick.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("NoBrick")
    
    ticked = checkbox1Slow.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("1Slow")
    
    ticked = checkboxNoSlow.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("NoSlow")
    
    ticked = checkboxFlowers3.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("Flowers3")
    
    ticked = checkboxNoRocks.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("NoRocks")
    
    ticked = checkboxLeafDisplay.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("LeafDisplay")
    
    ticked = checkboxHalvedTime.get()
    
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("HalvedTime")

    ticked = checkboxForceLast5.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFive("ForceLast5")
    
    choice = comboboxLast5Event.get()
    if choice == "x3 Coins":
        generatedCode = generatedCode + getOtherCodesFive("x3 Coins")
    
    choice = comboboxLast5Event.get()
    if choice == "5 Star Spaces":
        generatedCode = generatedCode + getOtherCodesFive("5 Star Spaces")
    
    choice = comboboxLast5Event.get()
    if choice == "Capsule Sapces on Every Space":
        generatedCode = generatedCode + getOtherCodesFive("Capsule Sapces on Every Space")
    
    choice = comboboxLast5Event.get()
    if choice == "Red Spaces are Bowser Spaces":
        generatedCode = generatedCode + getOtherCodesFive("Red Spaces are Bowser Spaces")

    choice = comboboxLast5Event.get()
    if choice == "Disabled":
        generatedCode = generatedCode + getOtherCodesFive("DisableLast5")

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)