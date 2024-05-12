# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty4_coins import *
from events.marioParty4_lotteryPrize import *
from events.marioParty4_mgreplace import *
from events.marioParty4_modselect import *
from events.marioParty4_items import *
from events.marioParty4_initialItems import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_4_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=752, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Mod Selection")
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Item Mods")
    tabview.add("Initial Items")
    tabview.add("Space Replacement")
    tabview.add("Lottery Rewards")
    tabview.set("Coins Mods")

    # Function to create an entry field and checkbox
    def create_entry(tab, row, icon_path, label_text, color):
        create_image_icon(tab, icon_path, row, 1)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=2, sticky="w", pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"))
        entry.grid(row=row, column=3)
        label1 = ctk.CTkLabel(master=tab, text=color, font=("Arial", 16))
        label1.grid(row=row, column=4, sticky="w")
        return entry

    # Create entry fields and checkboxes for Coins Mods tab
    blue_entry = create_entry(tabview.tab("Coins Mods"), 1, "assets/eventTags/blueSpace.png", " Gain  ", " Coins on a Blue Space.")
    red_entry = create_entry(tabview.tab("Coins Mods"), 2, "assets/eventTags/redSpace.png", " Lose  ", " Coins on a Red Space.")
    mgWin_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/miniGame.png", " Gain  ", " Coins when winning a Minigame.")
    star_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star.")
    mega_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/megaMushroom.png", " Gain ", " Coins when squishing a player.")
    booHouseStar_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/booHouseStars.png", " Costs ", " Coins when stealing a Star.")
    booHouseCoins_entry = create_entry(tabview.tab("Coins Mods"), 7, "assets/eventTags/booHouseCoins.png", " Costs ", " Coins when stealing coins.")
    lottery_entry = create_entry(tabview.tab("Coins Mods"), 8, "assets/eventTags/lottery4.png", " Costs ", " Coins to play the Lottery.")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp4(blue_entry, red_entry, mgWin_entry, star_entry, mega_entry, booHouseStar_entry, booHouseCoins_entry, lottery_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=640)

    # List of minigame names
    minigames_list = ["Manta Rings", "Slime Time", "Booksquirm", "Trace Race", "Mario Medley", "Avalanche!", "Domination", "Paratrooper Plunge", "Toad's Quick Draw", "Three Throw", "Photo Finish", "Mr. Blizzard's Brigade", "Bob-omb Breakers", "Long Claw of the Law", "Stamp Out!", "Candlelight Fright", "Makin' Waves", "Hide and Go BOOM!", "Tree Stomp", "Fish n' Drips", "Hop or Pop", "Money Belts", "GOOOOOOAL!!", "Blame it on the Crane", "The Great Deflate", "Revers-a-Bomb", "Right Oar Left?", "Cliffhangers", "Team Treasure Trek", "Pair-a-sailing", "Order Up", "Dungeon Duos", "Beach Volley Folley", "Cheep Cheep Sweep", "Darts of Doom", "Fruits of Doom", "Balloon of Doom", "Chain Chomp Fever", "Paths of Peril", "Bowser's Bigger Blast", "Butterfly Blitz", "Barrel Baron", "Mario Speedwagons", "Bowser Bop", "Mystic Match 'Em", "Archaeologuess", "Goomba's Chip Flip", "Kareening Koopas", "The Final Battle!", "Rumble Fishing", "Take a Breather", "Bowser Wrestling", "Panels of Doom"]   
    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp4(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=640)

    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/miniMushroom.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    miniPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    miniPrice4.grid(row=2, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=4)
    miniWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    miniWeight4.grid(row=2, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/megaMushroom.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    megaPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    megaPrice4.grid(row=3, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=4)
    megaWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    megaWeight4.grid(row=3, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=6)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/superMiniMushroom.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    superMiniPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    superMiniPrice4.grid(row=4, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=4)
    superMiniWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    superMiniWeight4.grid(row=4, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=6)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/superMegaMushroom.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    superMegaPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    superMegaPrice4.grid(row=5, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=4)
    superMegaWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    superMegaWeight4.grid(row=5, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=6)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/miniMegaHammer.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    miniMegaHammerPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    miniMegaHammerPrice4.grid(row=6, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=4)
    miniMegaHammerWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    miniMegaHammerWeight4.grid(row=6, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=6)


    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=7)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/sparkySticker.png", 2, 8)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=9)
    sparkyStickerPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    sparkyStickerPrice4.grid(row=2, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=11)
    sparkyStickerWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    sparkyStickerWeight4.grid(row=2, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=2, column=13)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/warpPipe.png", 3, 8)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=9)
    warpPipePrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipePrice4.grid(row=3, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=11)
    warpPipeWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeWeight4.grid(row=3, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=13)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/swapCard.png", 4, 8)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=9)
    swapCardPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    swapCardPrice4.grid(row=4, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=11)
    swapCardWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    swapCardWeight4.grid(row=4, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=13)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/bowserSuit4.png", 5, 8)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=9)
    bowserSuitPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    bowserSuitPrice4.grid(row=5, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=11)
    bowserSuitWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    bowserSuitWeight4.grid(row=5, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=13)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/gaddlight.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    gaddlightPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    gaddlightPrice4.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    gaddlightWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    gaddlightWeight4.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/magicLamp4.png", 2, 15)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=16)
    magicLampPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    magicLampPrice4.grid(row=2, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=18)
    magicLampWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    magicLampWeight4.grid(row=2, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=20)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/crystalBall.png", 3, 15)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=16)
    crystalBallPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    crystalBallPrice4.grid(row=3, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=18)
    crystalBallWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    crystalBallWeight4.grid(row=3, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=20)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/chompCall.png", 4, 15)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=16)
    chompCallPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    chompCallPrice4.grid(row=4, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=18)
    chompCallWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    chompCallWeight4.grid(row=4, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=20)

    
    icon = create_image_icon(tabview.tab("Item Mods"), "assets/items/itemBag4.png", 5, 15)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=16)
    itemBagPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    itemBagPrice4.grid(row=5, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=18)
    itemBagWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
    itemBagWeight4.grid(row=5, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=20)
    
    parseButtonThree = ctk.CTkButton(master=tabview.tab("Item Mods"), command=lambda: itemsEvent_mp4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4), text="Generate Codes")
    parseButtonThree.place(x=10, y=640)

    parseButtonFour = ctk.CTkButton(master=tabview.tab("Item Mods"), command=lambda: savePresetItems4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4), text="Save Preset")
    parseButtonFour.place(x=160, y=640)

    parseButtonFour = ctk.CTkButton(master=tabview.tab("Item Mods"), command=lambda: loadPresetItems4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4), text="Load Preset")
    parseButtonFour.place(x=310, y=640)

    items4 = ["None", "Mini Mushroom", "Mega Mushroom", "Super Mini Mushroom", "Super Mega Mushroom", "Mini-Mega Hammer", "Sparky Sticker", "Warp Pipe", "Swap Card", "Bowser Suit", "Gaddlight", "Magic Lamp", "Boo's Crystal Ball", "Chomp Call", "Item Bag"]
    
    label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 1:  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    initalItem41 = ctk.CTkComboBox(master=tabview.tab("Initial Items"), values=items4)
    initalItem41.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 2:  ", font=("Arial", 16))
    label.grid(row=1, column=0)

    initalItem42 = ctk.CTkComboBox(master=tabview.tab("Initial Items"), values=items4)
    initalItem42.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 3:  ", font=("Arial", 16))
    label.grid(row=2, column=0)

    initalItem43 = ctk.CTkComboBox(master=tabview.tab("Initial Items"), values=items4)
    initalItem43.grid(row=2, column=1)

    parseButton = ctk.CTkButton(master=tabview.tab("Initial Items"), command=lambda: initialItemsEvent_mp4(initalItem41, initalItem42, initalItem43, items4), text="Generate Codes")
    parseButton.place(x=10, y=640)
    
    label = ctk.CTkLabel(master=tabview.tab("Lottery Rewards"), text=" 1st Place Prize (Coins):  ", font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w")

    lotteryPrizeA =  ctk.CTkEntry(master=tabview.tab("Lottery Rewards"), width=48, font=("Arial", 16, "bold"), placeholder_text="100")
    lotteryPrizeA.grid(row=0, column=1, sticky="w")

    label = ctk.CTkLabel(master=tabview.tab("Lottery Rewards"), text=" 2nd Place Prize (Coins):  ", font=("Arial", 16))
    label.grid(row=1, column=0, sticky="w")

    lotteryPrizeB = ctk.CTkEntry(master=tabview.tab("Lottery Rewards"), width=48, font=("Arial", 16, "bold"), placeholder_text="30")
    lotteryPrizeB.grid(row=1, column=1, sticky="w")

    label = ctk.CTkLabel(master=tabview.tab("Lottery Rewards"), text=" 3rd Place Prize A (Item):  ", font=("Arial", 16))
    label.grid(row=2, column=0, sticky="w")

    lotteryPrizeC = ctk.CTkComboBox(master=tabview.tab("Lottery Rewards"), values=items4)
    lotteryPrizeC.grid(row=2, column=1, sticky="w")

    label = ctk.CTkLabel(master=tabview.tab("Lottery Rewards"), text=" 3rd Place Prize B (Item):  ", font=("Arial", 16))
    label.grid(row=3, column=0, sticky="w")

    lotteryPrizeD = ctk.CTkComboBox(master=tabview.tab("Lottery Rewards"), values=items4)
    lotteryPrizeD.grid(row=3, column=1, sticky="w")

    parseButton = ctk.CTkButton(master=tabview.tab("Lottery Rewards"), command=lambda: itemsLotteryEvent_mp4(lotteryPrizeA, lotteryPrizeB, lotteryPrizeC, lotteryPrizeD, items4), text="Generate Codes")
    parseButton.place(x=10, y=640)

    spaces4 = ["None", "Invisible Space", "Blue Space", "Red Space", "Bowser Space", "Mushroom Space", "Battle Space", "Happening Space", "Chance Time Space", "Spring Space"]

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    spaceRep411 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces4)
    spaceRep411.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=0, column=2)

    spaceRep421 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces4)
    spaceRep421.grid(row=0, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot A) ", font=("Arial", 16))
    label.grid(row=0, column=4)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=1, column=0)

    spaceRep412 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces4)
    spaceRep412.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=1, column=2)

    spaceRep422 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces4)
    spaceRep422.grid(row=1, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot B) ", font=("Arial", 16))
    label.grid(row=1, column=4)

    parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=lambda: spaceReplace4(spaceRep411, spaceRep412, spaceRep421, spaceRep422, spaces4), text="Generate Codes")
    parseButton.place(x=10, y=640)

    # Create Code Checkboxes
    checkbox30hz = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - 30Hz Gameplay", font=("Arial", 13))
    checkbox30hz.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxDigitalPress = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Allow Digital Presses for Map Screen", font=("Arial", 13))
    checkboxDigitalPress.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxAdvTxt = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Automatically Advance Text Boxes", font=("Arial", 13))
    checkboxAdvTxt.grid(row=2, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxCPUItems = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - CPUs can use Bowser Suit and Item Bags", font=("Arial", 13))
    checkboxCPUItems.grid(row=3, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxDisableAdv = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Disable Advance on Results", font=("Arial", 13))
    checkboxDisableAdv.grid(row=4, column=0, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxDisableMusic = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Disable In-game Music", font=("Arial", 13))
    checkboxDisableMusic.grid(row=5, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBoot = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Faster Boot Time", font=("Arial", 13))
    checkboxBoot.grid(row=6, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBSpeed = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Increased Board Speed", font=("Arial", 13))
    checkboxBSpeed.grid(row=7, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxTaunt = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Increased Taunt Capabilities", font=("Arial", 13))
    checkboxTaunt.grid(row=8, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxTxtDisplay = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Instant Text Display", font=("Arial", 13))
    checkboxTxtDisplay.grid(row=9, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxShowCtrl = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Show Player Who Paused", font=("Arial", 13))
    checkboxShowCtrl.grid(row=10, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxUnlockAll = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="QOL - Unlock Everything", font=("Arial", 13))
    checkboxUnlockAll.grid(row=11, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBooRed = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Boo's Haunted Bash - Red Boo Always On", font=("Arial", 13))
    checkboxBooRed.grid(row=12, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBridgeGnarly = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Bowser's Gnarly Party - Bridges Fall After One Cross", font=("Arial", 13))
    checkboxBridgeGnarly.grid(row=13, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxNeverGoBack = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Goomba's Greedy Gala - Never Go Back To Start", font=("Arial", 13))
    checkboxNeverGoBack.grid(row=14, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBananaJct = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Koopa's Seaside Soiree - Banana Peel is Normal Junction", font=("Arial", 13))
    checkboxBananaJct.grid(row=15, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxTeacupsJct = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Toad's Midway Madness - Teacups are Normal Junctions", font=("Arial", 13))
    checkboxTeacupsJct.grid(row=16, column=0, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBowserAlways = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Bowser Always Appears on Bowser Space", font=("Arial", 13))
    checkboxBowserAlways.grid(row=0, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxBowserItemBag = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Bowser Suit from Item Bag", font=("Arial", 13))
    checkboxBowserItemBag.grid(row=1, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxBowserDD = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Bowser Suit Gives Double Dice", font=("Arial", 13))
    checkboxBowserDD.grid(row=2, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxDoubleTurns = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Double the Amount of Turns", font=("Arial", 13))
    checkboxDoubleTurns.grid(row=3, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxEventAcc = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Events Don't Depend on Mini/Mega/Suit Status", font=("Arial", 13))
    checkboxEventAcc.grid(row=4, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxItemDeletion = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Item Deletion", font=("Arial", 13))
    checkboxItemDeletion.grid(row=5, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxKKAlways = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Koopa Kid Always Appears on Bowser Space", font=("Arial", 13))
    checkboxKKAlways.grid(row=6, column=1, sticky="w", padx=5, pady=5)

    def checkbox_callback_BowserSpace():
        if checkboxKKAlways.get() == 1:
            checkboxBowserAlways.configure(state="disabled")
        else:
            checkboxBowserAlways.configure(state="normal")

        if checkboxBowserAlways.get() == 1:
            checkboxKKAlways.configure(state="disabled")
        else:
            checkboxKKAlways.configure(state="normal")
    

    # Attach the callback function to the checkboxes
    checkboxKKAlways.configure(command=checkbox_callback_BowserSpace)
    checkboxBowserAlways.configure(command=checkbox_callback_BowserSpace)
    
    # Create Code Checkboxes
    checkboxForceLast5 = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Last 5 Turns Event - First Turn", font=("Arial", 13))
    checkboxForceLast5.grid(row=7, column=1, sticky="w", padx=5, pady=5)

    # Create Code Comboboxes
    label = ctk.CTkLabel(master=tabview.tab("Mod Selection"), text="Last 5 Turns Events", font=("Arial", 17, "bold"))
    label.grid(row=0, column=2, sticky="w", padx=5, pady=5)
    comboboxLast5Event = ctk.CTkComboBox(master=tabview.tab("Mod Selection"), values=["Random", "Disabled", "x2 Coins", "Free Stars", "Red Spaces are Fortune Spaces", "Red Spaces are Bowser Spaces"], font=("Arial", 13), width=300)
    comboboxLast5Event.grid(row=1, column=2, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxMini2Dice = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Mini Mushroom has 2 Dice", font=("Arial", 13))
    checkboxMini2Dice.grid(row=8, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxMiniPipeS = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Mini Pipes Work at Normal Size", font=("Arial", 13))
    checkboxMiniPipeS.grid(row=9, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxMiniRoll = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Mini Status Rolls 1-10", font=("Arial", 13))
    checkboxMiniRoll.grid(row=10, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxSuperMiniRoll = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Super Mini Mushroom has 3 Dice", font=("Arial", 13))
    checkboxSuperMiniRoll.grid(row=11, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxUseAfterBag = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Use Another Item After an Item Bag", font=("Arial", 13))
    checkboxUseAfterBag.grid(row=12, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxUseMoreItems = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Use Multiple Items on the Same Turn", font=("Arial", 13))
    checkboxUseMoreItems.grid(row=13, column=1, sticky="w", padx=5, pady=5)

    # Create Code Checkboxes
    checkboxDomination = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Domination - More Whomps", font=("Arial", 13))
    checkboxDomination.grid(row=14, column=1, sticky="w", padx=5, pady=5)
    
    # Create Code Checkboxes
    checkboxHoopsEmpty = ctk.CTkCheckBox(master=tabview.tab("Mod Selection"), text="Three Throw - All Hoops Empty", font=("Arial", 13))
    checkboxHoopsEmpty.grid(row=15, column=1, sticky="w", padx=5, pady=5)

    def checkbox_callback_Last5():
        if checkboxDisableLast5.get() == 1:
            checkboxForceLast5.configure(state="disabled")
            comboboxLast5Event.configure(state="disabled")
        else:
            checkboxForceLast5.configure(state="normal")
            comboboxLast5Event.configure(state="normal")
        if checkboxForceLast5.get() == 1:
            checkboxDisableLast5.configure(state="disabled")
            
    def combobox_callback_Last5(choice):  
        if comboboxLast5Event.get() == "Disabled":
            checkboxForceLast5.configure(state="disabled")

    # Attach the callback function to the checkboxes
    checkboxForceLast5.configure(command=checkbox_callback_Last5)
    comboboxLast5Event.configure(command=combobox_callback_Last5)

    # Default Check Boxes
    checkboxDisableAdv.select()
    checkboxBoot.select()
    checkboxBSpeed.select()
    checkboxCPUItems.select()
    checkboxTaunt.select()
    checkboxTxtDisplay.select()
    checkboxShowCtrl.select()
    checkboxUnlockAll.select()
    checkboxDigitalPress.select()

    parseButtonFiveOther = ctk.CTkButton(master=tabview.tab("Mod Selection"), command=lambda: modSelect_mp4(checkbox30hz, checkboxEventAcc, checkboxItemDeletion, checkboxBowserDD, checkboxDigitalPress, checkboxAdvTxt, checkboxCPUItems, checkboxDisableAdv, checkboxDisableMusic, checkboxBoot, checkboxBSpeed, checkboxTaunt, checkboxTxtDisplay, checkboxShowCtrl, checkboxUnlockAll, checkboxBooRed, checkboxBridgeGnarly, checkboxNeverGoBack, checkboxBananaJct, checkboxTeacupsJct, checkboxBowserItemBag, checkboxDoubleTurns, checkboxKKAlways, checkboxBowserAlways, checkboxDisableLast5, checkboxForceLast5, comboboxLast5Event, checkboxMini2Dice, checkboxMiniPipeS, checkboxMiniRoll, checkboxSuperMiniRoll, checkboxUseAfterBag, checkboxUseMoreItems, checkboxDomination, checkboxHoopsEmpty), text="Generate Codes")
    parseButtonFiveOther.place(x=10, y=640)

    return frame