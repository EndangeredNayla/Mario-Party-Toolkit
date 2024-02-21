# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/15/2024
# License: MIT
# ============================================

def getBlueSpaceCodeOne(amount, switch):
    return f'''
MP1 - Blue Spaces Give ONEBLUE Coins: ONEBLUESWITCH
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

def getRedSpaceCodeOne(amount, switch):
    return f'''
MP1 - Red Spaces Take Away ONERED Coins: ONEREDSWITCH
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