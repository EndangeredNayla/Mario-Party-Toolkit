# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty8 import *
import pyperclip

def coinsEvent_mp8(blueEntry, redEntry, mgEntry, starEntry, bitsizeEntry, hotelEntry):
    if not any((blueEntry.get(), redEntry.get(), mgEntry.get(), starEntry.get(), bitsizeEntry.get(), hotelEntry.get())):
        createDialog("Error", "error", "Please fill out at least one box.", None)
        return
    
    blueSpaceAmountEight = hex(int(blueEntry.get()))[2:].zfill(4).upper() if blueEntry.get() else "DUMMY"
    redSpaceAmountNegativeEight = format(-int(redEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if redEntry.get() else "DUMMY"
    mgSpaceAmountEight = hex(int(mgEntry.get()))[2:].zfill(4).upper() if mgEntry.get() else "DUMMY"
    
    starSpaceAmountEight = hex(int(starEntry.get()))[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpaceAmountEightNeg = format(-int(starEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if starEntry.get() else "DUMMY"

    bitsizeAmountEight = hex(int(bitsizeEntry.get()))[2:].zfill(4).upper() if bitsizeEntry.get() else "DUMMY"
    hotelEight = hex(int(hotelEntry.get()))[2:].zfill(4).upper() if hotelEntry.get() else "DUMMY"

    marioPartyEightBlueSpace = getBlueSpaceCodeEight(blueSpaceAmountEight, blueEntry.get()) if blueSpaceAmountEight != "DUMMY" else ""
    marioPartyEightRedSpace = getRedSpaceCodeEight(redSpaceAmountNegativeEight, redEntry.get()) if redSpaceAmountNegativeEight != "DUMMY" else ""
    marioPartyEightMiniGame = getMinigameCodeEight(mgSpaceAmountEight, mgEntry.get()) if mgSpaceAmountEight != "DUMMY" else ""
    marioPartyEightStarSpace = getStarSpaceCodeEight(starSpaceAmountEight, starSpaceAmountEightNeg, starEntry.get()) if starSpaceAmountEight != "DUMMY" else ""
    marioPartyEightBitsize = getBitsizeCode8(bitsizeAmountEight, bitsizeEntry.get()) if bitsizeAmountEight != "DUMMY" else ""
    marioPartyEightHotel = hotelMaxInvest(hotelEight, hotelEntry.get()) if hotelEight != "DUMMY" else ""

    generatedCode = marioPartyEightBlueSpace + marioPartyEightRedSpace + marioPartyEightMiniGame + marioPartyEightStarSpace + marioPartyEightBitsize + marioPartyEightHotel
    generatedCode = generatedCode.strip()

    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)