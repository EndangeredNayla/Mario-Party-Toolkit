# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/7/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty4 import *

import pyperclip

def coinsEvent_mp4(blueAmount, redAmount, mgAmount, starAmount, megaAmount, booStarAmount, booCoinsAmount, lotteryAmount):
    # Extract blue space information
    blueSpaceAmountBaseFour = blueAmount.get()
    blueSpaceAmountFour = hex(int(blueSpaceAmountBaseFour))[2:].zfill(4).upper() if blueSpaceAmountBaseFour else "DUMMY"

    # Extract red space information
    redSpaceAmountBaseFour = redAmount.get()
    redSpaceAmountFour = hex(int(redSpaceAmountBaseFour))[2:].zfill(4).upper() if redSpaceAmountBaseFour else "DUMMY"

    # Extract mg space information
    mgSpaceAmountBaseFour = mgAmount.get()
    mgSpaceAmountFour = hex(int(mgSpaceAmountBaseFour))[2:].zfill(4).upper() if mgSpaceAmountBaseFour else "DUMMY"

    # Extract star space information
    starSpaceAmountBaseFour = starAmount.get()
    starSpaceAmountFour = hex(int(starSpaceAmountBaseFour))[2:].zfill(4).upper() if starSpaceAmountBaseFour else "DUMMY"

    # Extract lottery space information
    lotterySpaceAmountBaseFour = lotteryAmount.get()
    lotterySpaceAmountFour = hex(int(lotterySpaceAmountBaseFour))[2:].zfill(4).upper() if lotterySpaceAmountBaseFour else "DUMMY"

    # Extract booStar space information
    booStarSpaceAmountBaseFour = booStarAmount.get()
    booStarSpaceAmountFour = hex(int(booStarSpaceAmountBaseFour))[2:].zfill(4).upper() if booStarSpaceAmountBaseFour else "DUMMY"

    # Extract booCoins space information
    booCoinsSpaceAmountBaseFour = booCoinsAmount.get()
    booCoinsSpaceAmountFour = hex(int(booCoinsSpaceAmountBaseFour))[2:].zfill(4).upper() if booCoinsSpaceAmountBaseFour else "DUMMY"

    # Extract mega squish information
    megaAmountBaseFour = megaAmount.get()
    megaAmountNegativeBaseFour = -int(megaAmountBaseFour)   
    megaAmountNegativeBaseFour = format(megaAmountNegativeBaseFour & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

    marioPartyFourBlueSpace = getBlueSpaceCodeFour(blueSpaceAmountFour, blueSpaceAmountBaseFour)
    marioPartyFourRedSpace = getRedSpaceCodeFour(redSpaceAmountFour, blueSpaceAmountBaseFour)
    marioPartyFourStarSpace = getStarSpaceCodeFour(starSpaceAmountFour, starSpaceAmountBaseFour)
    marioPartyFourLotterySpace = getLotterySpaceCodeFour(lotterySpaceAmountFour, lotterySpaceAmountBaseFour)
    marioPartyFourMGSpace = getMinigameCodeFour(mgSpaceAmountFour, mgSpaceAmountBaseFour)
    marioPartyFourBooStar = getBooSpaceStarFour(booStarSpaceAmountFour, booStarSpaceAmountBaseFour)
    marioPartyFourBooCoins = getBooSpaceCoinsFour(booCoinsSpaceAmountFour, booCoinsSpaceAmountBaseFour)
    marioPartyFourSquish = getSquishCodeFour(megaAmountNegativeBaseFour, megaAmountBaseFour)

    # Replace placeholder in generated codes
    generatedCode = (marioPartyFourBlueSpace + marioPartyFourRedSpace + marioPartyFourMGSpace + marioPartyFourStarSpace + marioPartyFourSquish + marioPartyFourBooStar + marioPartyFourBooCoins + marioPartyFourLotterySpace).strip()

    # Copy generated codes to clipboard
    pyperclip.copy(generatedCode)

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)