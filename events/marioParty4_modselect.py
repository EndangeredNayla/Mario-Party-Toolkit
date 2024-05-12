# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import pyperclip


def modSelect_mp4(checkbox30hz, checkboxEventAcc, checkboxItemDeletion, checkboxBowserDD, checkboxDigitalPress, checkboxAdvTxt, checkboxCPUItems, checkboxDisableAdv, checkboxDisableMusic, checkboxBoot, checkboxBSpeed, checkboxTaunt, checkboxTxtDisplay, checkboxShowCtrl, checkboxUnlockAll, checkboxBooRed, checkboxBridgeGnarly, checkboxNeverGoBack, checkboxBananaJct, checkboxTeacupsJct, checkboxBowserItemBag, checkboxDoubleTurns, checkboxKKAlways, checkboxBowserAlways, checkboxDisableLast5, checkboxForceLast5, comboboxLast5Event, checkboxMini2Dice, checkboxMiniPipeS, checkboxMiniRoll, checkboxSuperMiniRoll, checkboxUseAfterBag, checkboxUseMoreItems, checkboxDomination, checkboxHoopsEmpty):
    if checkbox30hz.get() == 0 and checkboxEventAcc.get() == 0 and checkboxItemDeletion.get() == 0 and checkboxBowserDD.get() == 0 and checkboxDigitalPress.get() == 0 and checkboxAdvTxt.get() == 0 and checkboxCPUItems.get() == 0 and checkboxDisableAdv.get() == 0 and checkboxDisableMusic.get() == 0 and checkboxBoot.get() == 0 and checkboxBSpeed.get() == 0 and checkboxTaunt.get() == 0 and checkboxTxtDisplay.get() == 0 and checkboxShowCtrl.get() == 0 and checkboxUnlockAll.get() == 0 and checkboxBooRed.get() == 0 and checkboxBridgeGnarly.get() == 0 and checkboxNeverGoBack.get() == 0 and checkboxBananaJct.get() == 0 and checkboxTeacupsJct.get() == 0 and checkboxBowserItemBag.get() == 0 and checkboxDoubleTurns.get() == 0 and checkboxKKAlways.get() == 0 and checkboxBowserAlways.get() == 0 and checkboxDisableLast5.get() == 0 and checkboxForceLast5.get() == 0 and comboboxLast5Event.get() == 0 and checkboxMini2Dice.get() == 0 and checkboxMiniPipeS.get() == 0 and checkboxMiniRoll.get() == 0 and checkboxSuperMiniRoll.get() == 0 and checkboxUseAfterBag.get() == 0 and checkboxUseMoreItems.get() == 0 and checkboxDomination.get() == 0 and checkboxHoopsEmpty.get() == 00 and comboboxLast5Event.get() == "Random":
        createDialog("Error", "error", "Please check at least 1 box.", None)
        return
    
    generatedCode = '''MP4 - Mods'''
    
    ticked = checkbox30hz.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("30Hz")
    
    ticked = checkboxDigitalPress.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("DigtPress")
    
    ticked = checkboxAdvTxt.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("AdvanceText")
    
    ticked = checkboxCPUItems.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("CPUItems")
    
    ticked = checkboxDisableAdv.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("DisableAdv")
    
    ticked = checkboxBoot.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("Boot")

    ticked = checkboxBSpeed.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("BSpeed")

    ticked = checkboxTaunt.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("TSpam")

    ticked = checkboxTxtDisplay.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("TxtDisplay")

    ticked = checkboxShowCtrl.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("ShowCtrl")
    
    ticked = checkboxUnlockAll.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("UnlockAll")
    
    ticked = checkboxBooRed.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("BooRed")
    
    ticked = checkboxBridgeGnarly.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("BridgeGnarly")
    
    ticked = checkboxNeverGoBack.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("NeverBack")
    
    ticked = checkboxBananaJct.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("BananaJct")
    
    ticked = checkboxTeacupsJct.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("TeacupJct")
    
    ticked = checkboxBowserItemBag.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("BowserBag")
    
    ticked = checkboxBowserDD.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("DoubleDice")
    
    ticked = checkboxDoubleTurns.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("DoubleTurns")
    
    ticked = checkboxKKAlways.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("AlwaysKK")
    
    ticked = checkboxBowserAlways.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("AlwaysBowser")
    
    ticked = checkboxEventAcc.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("EventAcc")
    
    ticked = checkboxItemDeletion.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("ItemDeletion")
    
    ticked = checkboxForceLast5.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("ForceL5")
    
    ticked = checkboxMini2Dice.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("Mini2Dice")

    ticked = checkboxMiniPipeS.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("MiniPipeSize")

    ticked = checkboxMiniRoll.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("MiniRoll")
    
    ticked = checkboxSuperMiniRoll.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("SMiniRoll")
    
    ticked = checkboxUseAfterBag.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("AfterBag")
    
    ticked = checkboxUseMoreItems.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("AfterItems")
    
    ticked = checkboxDomination.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("Domination")
    
    ticked = checkboxHoopsEmpty.get()
    if ticked == 1:
        generatedCode = generatedCode + getOtherCodesFour("HoopsE")
    
    choice = comboboxLast5Event.get()
    if choice == "x2 Coins":
        generatedCode = generatedCode + getOtherCodesFour("x3 Coins")

    choice = comboboxLast5Event.get()
    if choice == "Free Stars":
        generatedCode = generatedCode + getOtherCodesFour("Free Spaces")
    
    choice = comboboxLast5Event.get()
    if choice == "Red Spaces are Fortune Spaces":
        generatedCode = generatedCode + getOtherCodesFour("Red Spaces are Fortune Spaces")
    
    choice = comboboxLast5Event.get()
    if choice == "Red Spaces are Bowser Spaces":
        generatedCode = generatedCode + getOtherCodesFour("Red Spaces are Bowser Spaces")

    choice = comboboxLast5Event.get()
    if choice == "Disabled":
        generatedCode = generatedCode + getOtherCodesFour("Disabled")

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)