# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/15/2024
# License: MIT
# ============================================

def getBlueSpaceCodeTwo(amount, switch):
    return f'''
MP2 - Blue Spaces Give TWOBLUE Coins: TWOBLUESWITCH
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

def getRedSpaceCodeTwo(amount, switch):
    return f'''
MP2 - Red Spaces Take Away TWORED Coins: TWOREDSWITCH
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