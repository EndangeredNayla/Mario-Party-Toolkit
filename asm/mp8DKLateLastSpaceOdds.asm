# Insertion Address: 80010AAC
# 3rd/4th Shop Odds
# Created by Nayla

# Twice Candy: ID 0
cmpwi r29, 0x0
beq replaceTwice

# Thrice Candy: ID 1
cmpwi r29, 0x1
beq replaceThrice

# Slowgo Candy: ID 2
cmpwi r29, 0x2
beq replaceSlowgo

# Springo Candy: ID 4
cmpwi r29, 0x4
beq replaceSpringo

# Cashzap Candy: ID 5
cmpwi r29, 0x5
beq replaceCashzap

# Vampire Candy: ID 6
cmpwi r29, 0x6
beq replaceVampire

# Bitsize Candy: ID 7
cmpwi r29, 0x7
beq replaceBitsize

# Bloway Candy: ID 8
cmpwi r29, 0x8
beq replaceBitsize

# Bowlo Candy: ID 9
cmpwi r29, 0x9
beq replaceBowlo

# Weeglee Candy: ID A
cmpwi r29, 0xA
beq replaceWeeglee

# Thwomp Candy: ID C
cmpwi r29, 0xC
beq replaceThwomp

# Bullet Candy: ID D
cmpwi r29, 0xD
beq replaceBullet

# Bowser Candy: ID E
cmpwi r29, 0xE
beq replaceBowser

# Duelo Candy: ID F
cmpwi r29, 0xF
beq replaceDuelo

replaceTwice:
li r29, 0x1 # store ID to r29
b end

replaceThrice:
li r29, 0x1 # store ID to r29
b end

replaceSlowgo:
li r29, 0x1 # store ID to r29
b end

replaceSpringo:
li r29, 0x1 # store ID to r29
b end

replaceCashzap:
li r29, 0x1 # store ID to r29
b end

replaceVampire:
li r29, 0x1 # store ID to r29
b end

replaceBitsize:
li r29, 0x1 # store ID to r29
b end

replaceBloway:
li r29, 0x1 # store ID to r29
b end

replaceBowlo:
li r29, 0x1 # store ID to r29
b end

replaceWeeglee:
li r29, 0x1 # store ID to r29
b end

replaceThwomp:
li r29, 0x1 # store ID to r29
b end

replaceBullet:
li r29, 0x1 # store ID to r29
b end

replaceBowser:
li r29, 0x1 # store ID to r29
b end

replaceDuelo:
li r29, 0x63 # store ID to r29
b end

end:
stw r29, 0x000C (r31)