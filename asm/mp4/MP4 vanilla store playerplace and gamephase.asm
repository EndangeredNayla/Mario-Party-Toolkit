#To be inserted at 80086480
#Original instruction
lwz r3, 0 (r4)

#Store current player's placement
#Load curplayer index, multiply by 0x30
lis r15, 0x8018 
ori r15, r15, 0xFD02
lbz r15, 0 (r15)

mulli r15, r15, 0x30

#Get current player placement
lis r4, 0x8018
ori r4, r4, 0xFC38 #player structs start

add r4, r4, r15 #now points to cur player

lbz r4, 0x0009 (r4) #cur player placement byte
andi. r4, r4, 0x60
srwi r4, r4, 5 #return player placement

lis r15, 0x8018
ori r15, r15, 0xFD62 #Store player placement on 0x8018FD62

sth r4, 0 (r15)

#Store current game phase (00: Early, 01: Mid, 02: Late)
#Get turn data used for the code
lis r14, 0x8018
ori r14, r14, 0xFCFC
lbz r4, 1 (r14) #Max Turn
lbz r14, 0 (r14) #Current Turn

li r14, 3
divw r4, r4, r14 #Divide Max Turn / 3.

lis r14, 0x8018 
ori r14, r14, 0xFCFC
lbz r14, 0 (r14) #Current Turn


li r15, 0 #Earlygame byte
cmpw r14, r4
ble set_gamephase

li r15, 1 #Midgame byte

mulli r4, r4, 2
cmpw r14, r4
ble set_gamephase 

li r15, 2 #Lategame byte

set_gamephase:

lis r4, 0x8018
ori r4, r4, 0xFD72 #Store gamephase on 0x8018FD72

sth r15, 0 (r4)

li r14, 0
li r15, 0


