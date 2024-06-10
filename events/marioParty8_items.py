# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 6/10/2024
# License: MIT
# ============================================

from codes.marioParty8 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp8(board, twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4):
    if not twiceWeight4.get() or not thricePrice4.get() or not thriceWeight4.get() or not springoPrice4.get() or not springoWeight4.get() or not slowgoPrice4.get() or not slowgoWeight4.get() or not cashzapPrice4.get() or not cashzapWeight4.get() or not bitsizePrice4.get() or not bitsizeWeight4.get() or not blowayPrice4.get() or not blowayWeight4.get() or not vampirePrice4.get() or not vampireWeight4.get() or not bowloPrice4.get() or not bowloWeight4.get() or not weeglePrice4.get() or not weegleWeight4.get() or not bowserPrice4.get() or not bowserWeight4.get() or not bulletPrice4.get() or not bulletWeight4.get() or not thwompPrice4.get() or not thwompWeight4.get() or not dueloPrice4.get()  or not dueloWeight4.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    
    board = board.get()

    twiceWeight4 = twiceWeight4.get()
    thricePrice4 = thricePrice4.get()
    thriceWeight4 = thriceWeight4.get()
    slowgoPrice4 = slowgoPrice4.get()
    slowgoWeight4 = slowgoWeight4.get()
    springoPrice4 = springoPrice4.get()
    springoWeight4 = springoWeight4.get()
    cashzapPrice4 = cashzapPrice4.get()
    cashzapWeight4 = cashzapWeight4.get()
    bitsizePrice4 = bitsizePrice4.get()
    bitsizeWeight4 = bitsizeWeight4.get()
    blowayPrice4 = blowayPrice4.get()
    blowayWeight4 = blowayWeight4.get()
    vampirePrice4 = vampirePrice4.get()
    vampireWeight4 = vampireWeight4.get()
    weeglePrice4 = weeglePrice4.get()
    weegleWeight4 = weegleWeight4.get()
    bowserPrice4 = bowserPrice4.get()
    bowserWeight4 = bowserWeight4.get()
    bowloPrice4 = bowloPrice4.get()
    bowloWeight4 = bowloWeight4.get()
    bulletPrice4 = bulletPrice4.get()
    bulletWeight4 = bulletWeight4.get()
    thwompPrice4 = thwompPrice4.get()
    thwompWeight4 = thwompWeight4.get()
    dueloPrice4 = dueloPrice4.get()
    dueloWeight4 = dueloWeight4.get()
    
    orbWeightTotal = int(twiceWeight4) + int(thriceWeight4) + int(slowgoWeight4) + int(springoWeight4) + int(cashzapWeight4) + int(bitsizeWeight4) + int(blowayWeight4) + int(vampireWeight4) + int(weegleWeight4) + int(bowserWeight4) + int(bowloWeight4) + int(bulletWeight4) + int(thwompWeight4) + int(dueloWeight4)
    
    def calculateWeight(weight):
        percentage = (int(weight) / orbWeightTotal) * 100
        if 0< percentage < 1:
            return str(math.ceil(percentage))
        return str(round(percentage))


    for i in range(10):
        twiceWeight4 = twiceWeight4.replace("100", "99")
        thricePrice4 = thricePrice4.replace("100", "99")
        thriceWeight4 = thriceWeight4.replace("100", "99")
        slowgoPrice4 = slowgoPrice4.replace("100", "99")
        slowgoWeight4 = slowgoWeight4.replace("100", "99")
        springoPrice4 = springoPrice4.replace("100", "99")
        springoWeight4 = springoWeight4.replace("100", "99")
        cashzapPrice4 = cashzapPrice4.replace("100", "99")
        cashzapWeight4 = cashzapWeight4.replace("100", "99")
        bitsizePrice4 = bitsizePrice4.replace("100", "99")
        bitsizeWeight4 = bitsizeWeight4.replace("100", "99")
        blowayPrice4 = blowayPrice4.replace("100", "99")
        blowayWeight4 = blowayWeight4.replace("100", "99")
        vampirePrice4 = vampirePrice4.replace("100", "99")
        vampireWeight4 = vampireWeight4.replace("100", "99")
        weeglePrice4 = weeglePrice4.replace("100", "99")
        weegleWeight4 = weegleWeight4.replace("100", "99")
        bowserPrice4 = bowserPrice4.replace("100", "99")
        bowserWeight4 = bowserWeight4.replace("100", "99")
        bowloPrice4 = bowloPrice4.replace("100", "99")
        bowloWeight4 = bowloWeight4.replace("100", "99")
        bulletPrice4 = bulletPrice4.replace("100", "99")
        bulletWeight4 = bulletWeight4.replace("100", "99")
        thwompPrice4 = thwompPrice4.replace("100", "99")
        thwompWeight4 = thwompWeight4.replace("100", "99")
        dueloPrice4 = dueloPrice4.replace("100", "99")
        dueloWeight4 = dueloWeight4.replace("100", "99")

    if len(twiceWeight4) == 2:
        twiceWeightA = twiceWeight4[0]
        twiceWeightB = twiceWeight4[1]
    elif len(twiceWeight4) == 3:
        createDialog("Error", "error", "Twice Candy Weight is set to a number\nhigher then 100.", None)
    else:
        twiceWeightA = twiceWeight4
        twiceWeightB = "-30"

    # For thriceWeight4
    if len(thriceWeight4) == 2:
        thriceWeightA = thriceWeight4[0]
        thriceWeightB = thriceWeight4[1]
    else:
        thriceWeightA = thriceWeight4
        thriceWeightB = "-30"

    # For slowgoWeight4
    if len(slowgoWeight4) == 2:
        slowgoWeightA = slowgoWeight4[0]
        slowgoWeightB = slowgoWeight4[1]
    else:
        slowgoWeightA = slowgoWeight4
        slowgoWeightB = "-30"
    
    # For springoWeight4
    if len(springoWeight4) == 2:
        springoWeightA = springoWeight4[0]
        springoWeightB = springoWeight4[1]
    else:
        springoWeightA = springoWeight4
        springoWeightB = "-30"

    # For cashzapWeight4
    if len(cashzapWeight4) == 2:
        cashzapWeightA = cashzapWeight4[0]
        cashzapWeightB = cashzapWeight4[1]
    else:
        cashzapWeightA = cashzapWeight4
        cashzapWeightB = "-30"

    # For bitsizeWeight4
    if len(bitsizeWeight4) == 2:
        bitsizeWeightA = bitsizeWeight4[0]
        bitsizeWeightB = bitsizeWeight4[1]
    else:
        bitsizeWeightA = bitsizeWeight4
        bitsizeWeightB = "-30"

    # For blowayWeight4
    if len(blowayWeight4) == 2:
        blowayWeightA = blowayWeight4[0]
        blowayWeightB = blowayWeight4[1]
    else:
        blowayWeightA = blowayWeight4
        blowayWeightB = "-30"

    # For vampireWeight4
    if len(vampireWeight4) == 2:
        vampireWeightA = vampireWeight4[0]
        vampireWeightB = vampireWeight4[1]
    else:
        vampireWeightA = vampireWeight4
        vampireWeightB = "-30"

    # For weegleWeight4
    if len(weegleWeight4) == 2:
        weegleWeightA = weegleWeight4[0]
        weegleWeightB = weegleWeight4[1]
    else:
        weegleWeightA = weegleWeight4
        weegleWeightB = "-30"

    # For bowserWeight4
    if len(bowserWeight4) == 2:
        bowserWeightA = bowserWeight4[0]
        bowserWeightB = bowserWeight4[1]
    else:
        bowserWeightA = bowserWeight4
        bowserWeightB = "-30"

    # For bowloWeight4
    if len(bowloWeight4) == 2:
        bowloWeightA = bowloWeight4[0]
        bowloWeightB = bowloWeight4[1]
    else:
        bowloWeightA = bowloWeight4
        bowloWeightB = "-30"

    # For bulletWeight4
    if len(bulletWeight4) == 2:
        bulletWeightA = bulletWeight4[0]
        bulletWeightB = bulletWeight4[1]
    else:
        bulletWeightA = bulletWeight4
        bulletWeightB = "-30"

    # For thwompWeight4
    if len(thwompWeight4) == 2:
        thwompWeightA = thwompWeight4[0]
        thwompWeightB = thwompWeight4[1]
    else:
        thwompWeightA = thwompWeight4
        thwompWeightB = "-30"

    # For dueloWeight4
    if len(dueloWeight4) == 2:
        dueloWeightA = dueloWeight4[0]
        dueloWeightB = dueloWeight4[1]
    else:
        dueloWeightA = dueloWeight4
        dueloWeightB = "-30"

    # For slowgoPrice4
    if len(slowgoPrice4) == 2:
        slowgoPriceA = slowgoPrice4[0]
        slowgoPriceB = slowgoPrice4[1]
    else:
        slowgoPriceA = slowgoPrice4
        slowgoPriceB = "-30"

    # For springoPrice4
    if len(springoPrice4) == 2:
        springoPriceA = springoPrice4[0]
        springoPriceB = springoPrice4[1]
    else:
        springoPriceA = springoPrice4
        springoPriceB = "-30"

    # For cashzapPrice4
    if len(cashzapPrice4) == 2:
        cashzapPriceA = cashzapPrice4[0]
        cashzapPriceB = cashzapPrice4[1]
    else:
        cashzapPriceA = cashzapPrice4
        cashzapPriceB = "-30"

    # For bitsizePrice4
    if len(bitsizePrice4) == 2:
        bitsizePriceA = bitsizePrice4[0]
        bitsizePriceB = bitsizePrice4[1]
    else:
        bitsizePriceA = bitsizePrice4
        bitsizePriceB = "-30"

    # For blowayPrice4
    if len(blowayPrice4) == 2:
        blowayPriceA = blowayPrice4[0]
        blowayPriceB = blowayPrice4[1]
    else:
        blowayPriceA = blowayPrice4
        blowayPriceB = "-30"

    # For vampirePrice4
    if len(vampirePrice4) == 2:
        vampirePriceA = vampirePrice4[0]
        vampirePriceB = vampirePrice4[1]
    else:
        vampirePriceA = vampirePrice4
        vampirePriceB = "-30"

    # For weeglePrice4
    if len(weeglePrice4) == 2:
        weeglePriceA = weeglePrice4[0]
        weeglePriceB = weeglePrice4[1]
    else:
        weeglePriceA = weeglePrice4
        weeglePriceB = "-30"

    # For bowserPrice4
    if len(bowserPrice4) == 2:
        bowserPriceA = bowserPrice4[0]
        bowserPriceB = bowserPrice4[1]
    else:
        bowserPriceA = bowserPrice4
        bowserPriceB = "-30"

    # For bowloPrice4
    if len(bowloPrice4) == 2:
        bowloPriceA = bowloPrice4[0]
        bowloPriceB = bowloPrice4[1]
    else:
        bowloPriceA = bowloPrice4
        bowloPriceB = "-30"

    # For bulletPrice4
    if len(bulletPrice4) == 2:
        bulletPriceA = bulletPrice4[0]
        bulletPriceB = bulletPrice4[1]
    else:
        bulletPriceA = bulletPrice4
        bulletPriceB = "-30"

    # For thwompPrice4
    if len(thwompPrice4) == 2:
        thwompPriceA = thwompPrice4[0]
        thwompPriceB = thwompPrice4[1]
    else:
        thwompPriceA = thwompPrice4
        thwompPriceB = "-30"

    # For dueloPrice4
    if len(dueloPrice4) == 2:
        dueloPriceA = dueloPrice4[0]
        dueloPriceB = dueloPrice4[1]
    else:
        dueloPriceA = dueloPrice4
        dueloPriceB = "-30"

    # For thricePrice
    if len(thricePrice4) == 2:
        thricePriceA = thricePrice4[0]
        thricePriceB = thricePrice4[1]
    else:
        thricePriceA = thricePrice4
        thricePriceB = "-30"

    def add_30_to_digit(string):
        if string == "-30":
            return "00"
        result = ""
        for char in string:
            if char.isdigit():
                result += str(int(char) + 30)
            else:
                result += char
        return result

    twiceWeightA = add_30_to_digit(twiceWeightA)
    thricePriceA = add_30_to_digit(thricePriceA)
    thriceWeightA = add_30_to_digit(thriceWeightA)
    slowgoPriceA = add_30_to_digit(slowgoPriceA)
    slowgoWeightA = add_30_to_digit(slowgoWeightA)
    springoPriceA = add_30_to_digit(springoPriceA)
    springoWeightA = add_30_to_digit(springoWeightA)
    cashzapPriceA = add_30_to_digit(cashzapPriceA)
    cashzapWeightA = add_30_to_digit(cashzapWeightA)
    bitsizePriceA = add_30_to_digit(bitsizePriceA)
    bitsizeWeightA = add_30_to_digit(bitsizeWeightA)
    blowayPriceA = add_30_to_digit(blowayPriceA)
    blowayWeightA = add_30_to_digit(blowayWeightA)
    vampirePriceA = add_30_to_digit(vampirePriceA)
    vampireWeightA = add_30_to_digit(vampireWeightA)
    weeglePriceA = add_30_to_digit(weeglePriceA)
    weegleWeightA = add_30_to_digit(weegleWeightA)
    bowserPriceA = add_30_to_digit(bowserPriceA)
    bowserWeightA = add_30_to_digit(bowserWeightA)
    bowloPriceA = add_30_to_digit(bowloPriceA)
    bowloWeightA = add_30_to_digit(bowloWeightA)
    bulletPriceA = add_30_to_digit(bulletPriceA)
    bulletWeightA = add_30_to_digit(bulletWeightA)
    thwompPriceA = add_30_to_digit(thwompPriceA)
    thwompWeightA = add_30_to_digit(thwompWeightA)
    dueloPriceA = add_30_to_digit(dueloPriceA)
    dueloWeightA = add_30_to_digit(dueloWeightA)

    variables_to_process = [twiceWeightB, thricePriceB, thriceWeightB, slowgoPriceB, slowgoWeightB, springoPriceB, springoWeightB, cashzapPriceB, cashzapWeightB, bitsizePriceB, bitsizeWeightB, blowayPriceB, blowayWeightB, vampirePriceB, vampireWeightB, weeglePriceB, weegleWeightB, bowserPriceB, bowserWeightB, bowloPriceB, bowloWeightB, bulletPriceB, bulletWeightB, thwompPriceB, thwompWeightB, dueloPriceB, dueloWeightB]

    for i in range(len(variables_to_process)):
        variables_to_process[i] = add_30_to_digit(variables_to_process[i])

    # Update the variables with the processed values
    twiceWeightB, thricePriceB, thriceWeightB, slowgoPriceB, slowgoWeightB, springoPriceB, springoWeightB, cashzapPriceB, cashzapWeightB, bitsizePriceB, bitsizeWeightB, blowayPriceB, blowayWeightB, vampirePriceB, vampireWeightB, weeglePriceB, weegleWeightB, bowserPriceB, bowserWeightB, bowloPriceB, bowloWeightB, bulletPriceB, bulletWeightB, thwompPriceB, thwompWeightB, dueloPriceB, dueloWeightB = variables_to_process


    if board == "DK's Treetop Temple":
        generatedCode = getCandyCodeDK(twiceWeightA, twiceWeightB, thricePriceA, thricePriceB, thriceWeightA, thriceWeightB, slowgoPriceA, slowgoPriceB, slowgoWeightA, slowgoWeightB, bitsizePriceA, bitsizePriceB, bitsizeWeightA, bitsizeWeightB, bowloPriceA, bowloPriceB, bowloWeightA, bowloWeightB, weeglePriceA, weeglePriceB, weegleWeightA, weegleWeightB, thwompPriceA, thwompPriceB, thwompWeightA, thwompWeightB, dueloPriceA, dueloPriceB, dueloWeightA, dueloWeightB, vampirePriceA, vampirePriceB, vampireWeightA, vampireWeightB, springoPriceA, springoPriceB, springoWeightA, springoWeightB, cashzapPriceA, cashzapPriceB, cashzapWeightA, cashzapWeightB, blowayPriceA, blowayPriceB, blowayWeightA, blowayWeightB, bowserPriceA, bowserPriceB, bowserWeightA, bowserWeightB, bulletPriceA, bulletPriceB, bulletWeightA, bulletWeightB)
    elif board == "Goomba's Booty Boardwalk":
        generatedCode = getCandyCodeGoomba(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, vampirePrice4, vampireWeight4, weeglePrice4, weegleWeight4, bowserPrice4, bowserWeight4, bowloPrice4, bowloWeight4, bulletPrice4, bulletWeight4, thwompPrice4, thwompWeight4, dueloPrice4, dueloWeight4)
    elif board == "King Boo's Haunted Hideaway":
        generatedCode = getCandyCodeBoo(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, vampirePrice4, vampireWeight4, weeglePrice4, weegleWeight4, bowserPrice4, bowserWeight4, bowloPrice4, bowloWeight4, bulletPrice4, bulletWeight4, thwompPrice4, thwompWeight4, dueloPrice4, dueloWeight4)
    elif board == "Shy Guy's Perplex Express":
        generatedCode = getCandyCodeShyGuy(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, vampirePrice4, vampireWeight4, weeglePrice4, weegleWeight4, bowserPrice4, bowserWeight4, bowloPrice4, bowloWeight4, bulletPrice4, bulletWeight4, thwompPrice4, thwompWeight4, dueloPrice4, dueloWeight4)
    elif board == "Koopa's Tycoon Town":
        generatedCode = getCandyCodeKoopa(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, vampirePrice4, vampireWeight4, weeglePrice4, weegleWeight4, bowserPrice4, bowserWeight4, bowloPrice4, bowloWeight4, bulletPrice4, bulletWeight4, thwompPrice4, thwompWeight4, dueloPrice4, dueloWeight4)
    elif board == "Bowser's Warped Orbit":
        generatedCode = getCandyCodeBowser(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, vampirePrice4, vampireWeight4, weeglePrice4, weegleWeight4, bowserPrice4, bowserWeight4, bowloPrice4, bowloWeight4, bulletPrice4, bulletWeight4, thwompPrice4, thwompWeight4, dueloPrice4, dueloWeight4)
        
    
    
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)