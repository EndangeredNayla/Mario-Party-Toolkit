# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty1 import *

import pyperclip

def coinsEvent_mp1(blueAmount, blueTick, redAmount, redTick):
    if not blueAmount.get() and not redAmount.get():
        createDialog("Error", "error", "Please fill out atleast one box.", None)
        return
    # Extract blue space information
    blueSpaceAmountBaseOne = blueAmount.get()
    blueSpaceAmountOne = hex(int(blueSpaceAmountBaseOne))[2:].zfill(4).upper() if blueSpaceAmountBaseOne else "DUMMY"
    blueSpaceSwitchOne = "1" if blueTick.get() else "0"

    # Extract red space information
    redSpaceAmountBaseOne = redAmount.get()
    redSpaceAmountOne = hex(int(redSpaceAmountBaseOne))[2:].zfill(4).upper() if redSpaceAmountBaseOne else "DUMMY"
    redSpaceSwitchOne = "1" if redTick.get() else "0"

    # Generate codes for blue and red spaces
    if blueSpaceSwitchOne == "0":
        marioPartyOneBlueSpace = getBlueSpaceCodeOne(blueSpaceAmountOne, blueSpaceSwitchOne, blueSpaceAmountBaseOne, "Doesn't Double on Last 5") if blueSpaceAmountOne != "DUMMY" else ""
    elif blueSpaceSwitchOne == "1":
        marioPartyOneBlueSpace = getBlueSpaceCodeOne(blueSpaceAmountOne, blueSpaceSwitchOne, blueSpaceAmountBaseOne, "Doubles on Last 5") if blueSpaceAmountOne != "DUMMY" else ""

    if redSpaceSwitchOne == "0":
        marioPartyOneRedSpace = getRedSpaceCodeOne(redSpaceAmountOne, redSpaceSwitchOne, redSpaceAmountBaseOne, "Doesn't Double on Last 5") if redSpaceAmountOne != "DUMMY" else ""
    elif redSpaceSwitchOne == "1":
        marioPartyOneRedSpace = getRedSpaceCodeOne(redSpaceAmountOne, redSpaceSwitchOne, redSpaceAmountBaseOne, "Doubles on Last 5") if redSpaceAmountOne != "DUMMY" else ""


    # Replace placeholder in generated codes
    generatedCode = (marioPartyOneBlueSpace + marioPartyOneRedSpace).strip()

    # Copy generated codes to clipboard
    pyperclip.copy(generatedCode)

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)