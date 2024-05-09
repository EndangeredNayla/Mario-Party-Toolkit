# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty2 import *

import pyperclip

def coinsEvent_mp2(blueAmount, blueTick, redAmount, redTick):
    if not blueAmount.get() and not redAmount.get():
        createDialog("Error", "error", "Please fill out atleast one box.", None)
        return
    # Extract blue space information
    blueSpaceAmountBaseTwo = blueAmount.get()
    blueSpaceAmountTwo = hex(int(blueSpaceAmountBaseTwo))[2:].zfill(4).upper() if blueSpaceAmountBaseTwo else "DUMMY"
    blueSpaceSwitchTwo = "1" if blueTick.get() else "0"

    # Extract red space information
    redSpaceAmountBaseTwo = redAmount.get()
    redSpaceAmountTwo = hex(int(redSpaceAmountBaseTwo))[2:].zfill(4).upper() if redSpaceAmountBaseTwo else "DUMMY"
    redSpaceSwitchTwo = "1" if redTick.get() else "0"

    # Generate codes for blue and red spaces
    if blueSpaceSwitchTwo == "0":
        marioPartyTwoBlueSpace = getBlueSpaceCodeTwo(blueSpaceAmountTwo, blueSpaceSwitchTwo, blueSpaceAmountBaseTwo, "Doesn't Double on Last 5") if blueSpaceAmountTwo != "DUMMY" else ""
    elif blueSpaceSwitchTwo == "1":
        marioPartyTwoBlueSpace = getBlueSpaceCodeTwo(blueSpaceAmountTwo, blueSpaceSwitchTwo, blueSpaceAmountBaseTwo, "Doubles on Last 5") if blueSpaceAmountTwo != "DUMMY" else ""

    if redSpaceSwitchTwo == "0":
        marioPartyTwoRedSpace = getRedSpaceCodeTwo(redSpaceAmountTwo, redSpaceSwitchTwo, redSpaceAmountBaseTwo, "Doesn't Double on Last 5") if redSpaceAmountTwo != "DUMMY" else ""
    elif redSpaceSwitchTwo == "1":
        marioPartyTwoRedSpace = getRedSpaceCodeTwo(redSpaceAmountTwo, redSpaceSwitchTwo, redSpaceAmountBaseTwo, "Doubles on Last 5") if redSpaceAmountTwo != "DUMMY" else ""


    # Replace placeholder in generated codes
    generatedCode = (marioPartyTwoBlueSpace + marioPartyTwoRedSpace).strip()

    # Copy generated codes to clipboard
    pyperclip.copy(generatedCode)

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)