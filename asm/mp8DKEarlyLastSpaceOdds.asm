# Insertion Address: 804D2E54
# 3rd/4th Shop Odds
# Created by Nayla

# Twice Candy: ID 0
cmpwi r0, 0x0
beq replaceTwice

# Thrice Candy: ID 1
cmpwi r0, 0x1
beq replaceThrice

# Slowgo Candy: ID 2
cmpwi r0, 0x2
beq replaceSlowgo

# Springo Candy: ID 4
cmpwi r0, 0x4
beq replaceSpringo

# Cashzap Candy: ID 5
cmpwi r0, 0x5
beq replaceCashzap

# Vampire Candy: ID 6
cmpwi r0, 0x6
beq replaceVampire

# Bitsize Candy: ID 7
cmpwi r0, 0x7
beq replaceBitsize

# Bloway Candy: ID 8
cmpwi r0, 0x8
beq replaceBitsize

# Bowlo Candy: ID 9
cmpwi r0, 0x9
beq replaceBowlo

# Weeglee Candy: ID A
cmpwi r0, 0xA
beq replaceWeeglee

# Thwomp Candy: ID C
cmpwi r0, 0xC
beq replaceThwomp

# Bullet Candy: ID D
cmpwi r0, 0xD
beq replaceBullet

# Bowser Candy: ID E
cmpwi r0, 0xE
beq replaceBowser

# Duelo Candy: ID F
cmpwi r0, 0xF
beq replaceDuelo

replaceTwice:
li r0, 0x1 # store ID to r0
b end

replaceThrice:
li r0, 0x1 # store ID to r0
b end

replaceSlowgo:
li r0, 0x1 # store ID to r0
b end

replaceSpringo:
li r0, 0x1 # store ID to r0
b end

replaceCashzap:
li r0, 0x1 # store ID to r0
b end

replaceVampire:
li r0, 0x1 # store ID to r0
b end

replaceBitsize:
li r0, 0x1 # store ID to r0
b end

replaceBloway:
li r0, 0x1 # store ID to r0
b end

replaceBowlo:
li r0, 0x1 # store ID to r0
b end

replaceWeeglee:
li r0, 0x1 # store ID to r0
b end

replaceThwomp:
li r0, 0x1 # store ID to r0
b end

replaceBullet:
li r0, 0x1 # store ID to r0
b end

replaceBowser:
li r0, 0x1 # store ID to r0
b end

replaceDuelo:
li r0, 0x63 # store ID to r0
b end

end:
stw r0, 0x0008 (r3)