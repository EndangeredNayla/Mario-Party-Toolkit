from functions import *
from codes.marioParty4 import *
import pyperclip

def coinsEvent_mp4(blueEntry, redEntry, mgEntry, starEntry, megaEntry, booStarEntry, booCoinsEntry, lotteryEntry):
    if not any((blueEntry.get(), redEntry.get(), starEntry.get(), mgEntry.get(), megaEntry.get(), booStarEntry.get(), booCoinsEntry.get(), lotteryEntry.get())):
        createDialog("Error", "error", "Please fill out at least one box.", None)
        return
    
    blueSpaceAmountFour = hex(int(blueEntry.get()))[2:].zfill(4).upper() if blueEntry.get() else "DUMMY"
    redSpaceAmountFour = hex(int(redEntry.get()))[2:].zfill(4).upper() if redEntry.get() else "DUMMY"
    mgSpaceAmountFour = hex(int(mgEntry.get()))[2:].zfill(4).upper() if mgEntry.get() else "DUMMY"
    starSpaceAmountFour = hex(int(starEntry.get()))[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    lotterySpaceAmountFour = hex(int(lotteryEntry.get()))[2:].zfill(4).upper() if lotteryEntry.get() else "DUMMY"
    booStarSpaceAmountFour = hex(int(booStarEntry.get()))[2:].zfill(4).upper() if booStarEntry.get() else "DUMMY"
    booCoinsSpaceAmountFour = hex(int(booCoinsEntry.get()))[2:].zfill(4).upper() if booCoinsEntry.get() else "DUMMY"
    megaAmountNegativeBaseFour = -int(megaEntry.get()) if megaEntry.get() else "DUMMY"
    megaAmountNegativeBaseFour = format(megaAmountNegativeBaseFour & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if megaEntry.get() else "DUMMY"

    marioPartyFourBlueSpace = getBlueSpaceCodeFour(blueSpaceAmountFour, blueEntry.get()) if blueSpaceAmountFour != "DUMMY" else ""
    marioPartyFourRedSpace = getRedSpaceCodeFour(redSpaceAmountFour, redEntry.get()) if redSpaceAmountFour != "DUMMY" else ""
    marioPartyFourStarSpace = getStarSpaceCodeFour(starSpaceAmountFour, starEntry.get()) if starSpaceAmountFour != "DUMMY" else ""
    marioPartyFourLotterySpace = getLotterySpaceCodeFour(lotterySpaceAmountFour, lotteryEntry.get()) if lotterySpaceAmountFour != "DUMMY" else ""
    marioPartyFourMGSpace = getMinigameCodeFour(mgSpaceAmountFour, mgEntry.get()) if mgSpaceAmountFour != "DUMMY" else ""
    marioPartyFourBooStar = getBooSpaceStarFour(booStarSpaceAmountFour, booStarEntry.get()) if booStarSpaceAmountFour != "DUMMY" else ""
    marioPartyFourBooCoins = getBooSpaceCoinsFour(booCoinsSpaceAmountFour, booCoinsEntry.get()) if booCoinsSpaceAmountFour != "DUMMY" else ""
    marioPartyFourSquish = getSquishCodeFour(megaAmountNegativeBaseFour, megaEntry.get()) if megaAmountNegativeBaseFour != "DUMMY" else ""

    generatedCode = (marioPartyFourBlueSpace + marioPartyFourRedSpace + marioPartyFourMGSpace + marioPartyFourStarSpace + marioPartyFourSquish + marioPartyFourBooStar + marioPartyFourBooCoins + marioPartyFourLotterySpace).strip()

    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)