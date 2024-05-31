# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/31/2024
# License: MIT
# ============================================

from codes.marioParty6 import *
from functions import *

import pyperclip

def customBonusStarEvent_mp6(star1, star2, star3, stars6):
    starSlot1 = star1.get()
    starSlot2 = star2.get()
    starSlot3 = star3.get()

    starHex = ["NONE", "88830014", "88830015", "88830016", "88830017", "88830018", "88830019", "8883001A", "8883001B", "A883001C", "A883001E", "A8830022", "A8830030", "A88300234"]

    starSlot1Num = stars6.index(starSlot1)
    starSlot1Hex = starHex[starSlot1Num]

    starSlot2Num = stars6.index(starSlot2)
    starSlot2Hex = starHex[starSlot2Num]

    starSlot3Num = stars6.index(starSlot3)
    starSlot3Hex = starHex[starSlot3Num]

    mpStar41 = getStarReplaceSix1(starSlot1Hex, starSlot1)
    mpStar42 = getStarReplaceSix2(starSlot2Hex, starSlot2)
    mpStar43 = getStarReplaceSix2(starSlot3Hex, starSlot3)

    if starSlot1Hex == "NONE":
        mpStar41 = ""
    if starSlot2Hex == "NONE":
        mpStar42 = ""
    if starSlot3Hex == "NONE":
        mpStar43 = ""

    generatedCode = mpStar41 + mpStar42 + mpStar43

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
