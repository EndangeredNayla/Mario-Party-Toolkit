#To be inserted at 80083878
#To be inserted at 80083878
#Item Space weights struct
lis r7, 0x8018
ori r7, r7, 0xFD64

# Calculate the range of random values based on percentages
li r3, 0
li r4, 0

loop_calc:
    cmpwi r3, 0xE # Exit at 0xE 
    beq- exit_calc
	
    lhzx r5, r7, r3 # Load the percentage for the current item using r3 as index
    add r4, r4, r5 # Add the percentage to the range of random values
    addi r3, r3, 1 # Increment index by 1
    b loop_calc
exit_calc:

# Call the random integer function
lis r5, 0x8005
ori r5, r5, 0xFB40 # 0x8005FB40 get rand int function
mtctr r5
mr r3, r4
bctrl

# rand integer in r3 in range of percentages array

# Select the item based on the random integer
li r4, 0
li r5, 0
loop_select:
    cmpwi r5, 0xE # Exit at 0xE
    beq- exit_select
	
    lhzx r6, r7, r5 # Load the percentage for the current item using r5 as index
    sub r3, r3, r6 # Subtract the percentage from the random integer
    cmpwi r3, 0 # Compare the updated random integer with 0
    bge+ loop_increment # If the updated random integer is greater than or equal to 0, continue to the next item
    b exit
loop_increment:
    addi r4, r4, 1 #item id increment
    addi r5, r5, 1 # Increment index by 1 
    b loop_select
exit:
lis r5, 0x817F
ori r5, r5, 0xFFF0
stw r4, 0 (r5)
cmpwi r4, 8
blt- skipModelIncrement
#there's a gap in the item models starting at gaddlight's item id (8)
addi r4, r4, 1

skipModelIncrement:
lis r5, 0x0007
ori r5, r5, 0x006d #base item id
add r3, r4, r5
li r4, 0 #restore from hook
li r5, 0 #restore from hook
