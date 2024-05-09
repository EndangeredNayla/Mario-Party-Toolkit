# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

def getBlueSpaceCodeTwo(amount, switch, amountDec, switchDec):
    return f'''
MP2 - Blue Spaces Give {amountDec} Coins: {switchDec}
81066300 3408
81066302 000{switch}
81066304 1100
81066306 0003
81066308 3410
8106630A {amount}
8106630C 5440
8106630E 0001
81066310 0010
81066312 8040
'''

def getRedSpaceCodeTwo(amount, switch, amountDec, switchDec):
    return f'''
MP2 - Red Spaces Take Away {amountDec} Coins: {switchDec}
8106634C 3408
8106634E 000{switch}
81066350 1100
81066352 0003
81066354 3410
81066356 {amount}
81066358 5440
8106635A 0001
8106635C 0010
8106635E 8040
'''

def getMinigameReplacement2(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP2 - Minigame Replacement: {gameUno} -> {gameDos}
D00F93C9 00{hexUno}
800F93C9 00{hexDos}	
'''

# Items with 00 never show. this includes Bowser Bomb at CC003.
# Boo Bell at CC007, and the Bowser Suit at CC008
def getItems2(one, two, three, five, six, nine, ten):
    return f'''
MP2 - Item Modifer
D00CC000 000A
800CC000 00{one}
D00CC001 000A
800CC001 00{two}
D00CC002 000F
800CC002 00{three}
D00CC004 000F
800CC004 00{five}
D00CC005 000F
800CC005 00{six}
D00CC006 0014
800CC006 00{nine}
D00CC009 001E
800CC009 00{ten}
'''