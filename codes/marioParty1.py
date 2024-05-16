# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

def getBlueSpaceCodeOne(amount, switch, amountDec, switchDec):
    return f'''
MP1 - Blue Spaces Give {amountDec} Coins: {switchDec}
81057D80 3408
81057D82 000{switch}
81057D84 1100
81057D86 0003
81057D88 3410
81057D8A {amount}
81057D8C 5440
81057D8E 0001
81057D90 0010
81057D92 8040
0407FBE0 3BC0
'''

def getRedSpaceCodeOne(amount, switch, amountDec, switchDec):
    return f'''
MP1 - Red Spaces Take Away {amountDec} Coins: {switchDec}
81057DD8 3408
81057DDA 000{switch}
81057DDC 1100
81057DDE 0003
81057DE0 3410
81057DE2 {amount}
81057DE4 5440
81057DE6 0001
81057DE8 0010
81057DEA 8040
'''

def getMinigameReplacement1(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP1 - Minigame Replacement: {gameUno} -> {gameDos}
D10ED5DE 00{hexUno}
810ED5DE 00{hexDos}		
'''

def getStarHandicapP1(amount, amountDec):
    return f'''
MP1 - P1 Starts With {amountDec} Stars
D10F32D6 0000
810F32BC {amount}	
'''

def getStarHandicapP2(amount, amountDec):
    return f'''
MP1 - P2 Starts With {amountDec} Stars
D10F32D6 0000
810F32EC {amount}	
'''

def getStarHandicapP3(amount, amountDec):
    return f'''
MP1 - P3 Starts With {amountDec} Stars
D10F32D6 0000
810F331C {amount}	
'''

def getStarHandicapP4(amount, amountDec):
    return f'''
MP1 - P4 Starts With {amountDec} Stars
D10F32D6 0000
810F334C {amount}	
'''