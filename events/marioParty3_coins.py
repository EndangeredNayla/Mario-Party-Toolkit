# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty3 import *

import pyperclip

def coinsEvent_mp3(blueAmount, blueTick, redAmount, redTick, starAmount, koopaBankAmount):
    # Extract blue space information
    blueSpaceAmountBaseThree = blueAmount.get()
    blueSpaceAmountThree = hex(int(blueSpaceAmountBaseThree))[2:].zfill(4).upper() if blueSpaceAmountBaseThree else "DUMMY"
    blueSpaceSwitchThree = "1" if blueTick.get() else "0"

    # Extract red space information
    redSpaceAmountBaseThree = redAmount.get()
    redSpaceAmountThree = hex(int(redSpaceAmountBaseThree))[2:].zfill(4).upper() if redSpaceAmountBaseThree else "DUMMY"
    redSpaceSwitchThree = "1" if redTick.get() else "0"

    # Extract star space information
    starSpaceAmountBaseThree = starAmount.get()
    starSpaceAmountThree = hex(int(starSpaceAmountBaseThree))[2:].zfill(4).upper() if starSpaceAmountBaseThree else "DUMMY"
    negativeStarSpaceAmountBaseThree = -int(starSpaceAmountBaseThree) if starSpaceAmountBaseThree else "DUMMY" 
    starSpaceAmountNegativeThree = format(negativeStarSpaceAmountBaseThree & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if starSpaceAmountBaseThree else "DUMMY"

    # Extract koopa bank information
    koopaBankAmountBaseThree = koopaBankAmount.get()
    koopaBankAmountThree = hex(int(koopaBankAmountBaseThree))[2:].zfill(4).upper() if koopaBankAmountBaseThree else "DUMMY"
    kbAmountNegativeBaseThree = -int(koopaBankAmountBaseThree) if starSpaceAmountBaseThree else "DUMMY"
    kbAmountNegativeBaseThree = format(kbAmountNegativeBaseThree & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if starSpaceAmountBaseThree else "DUMMY"


    # Generate codes for blue and red spaces
    if blueSpaceSwitchThree == "0":
        marioPartyThreeBlueSpace = getBlueSpaceCodeThree(blueSpaceAmountThree, blueSpaceSwitchThree, blueSpaceAmountBaseThree, "Doesn't Double on Last 5") if blueSpaceAmountThree != "DUMMY" else ""
    elif blueSpaceSwitchThree == "1":
        marioPartyThreeBlueSpace = getBlueSpaceCodeThree(blueSpaceAmountThree, blueSpaceSwitchThree, blueSpaceAmountBaseThree, "Doubles on Last 5") if blueSpaceAmountThree != "DUMMY" else ""

    if redSpaceSwitchThree == "0":
        marioPartyThreeRedSpace = getRedSpaceCodeThree(redSpaceAmountThree, redSpaceSwitchThree, redSpaceAmountBaseThree, "Doesn't Double on Last 5") if redSpaceAmountThree != "DUMMY" else ""
    elif redSpaceSwitchThree == "1":
        marioPartyThreeRedSpace = getRedSpaceCodeThree(redSpaceAmountThree, redSpaceSwitchThree, redSpaceAmountBaseThree, "Doubles on Last 5") if redSpaceAmountThree != "DUMMY" else ""

    marioPartyThreeStarSpace = getStarSpaceCodeThree(starSpaceAmountThree, starSpaceAmountNegativeThree, starSpaceAmountBaseThree) if starSpaceAmountThree != "DUMMY" else ""
    marioPartyThreeKoopaBank = getKoopaBankCodeThree(koopaBankAmountThree, kbAmountNegativeBaseThree, koopaBankAmountBaseThree) if koopaBankAmountThree != "DUMMY" else ""

    # Replace placeholder in generated codes
    generatedCode = (marioPartyThreeBlueSpace + marioPartyThreeRedSpace + marioPartyThreeStarSpace + marioPartyThreeKoopaBank).strip()

    # Copy generated codes to clipboard
    pyperclip.copy(generatedCode)

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)