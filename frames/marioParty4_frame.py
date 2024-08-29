# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty4_coins import *
from events.marioParty4_handicap import *
from events.marioParty4_lotteryPrize import *
from events.marioParty4_mgreplace import *
from events.marioParty4_items import *
from events.marioParty4_battle import *
from events.marioParty4_initialItems import *
from events.marioParty4_spaceReplace import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_4_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Item Mods")
    tabview.add("Initial Items")
    tabview.add("Space Replacement")
    tabview.add("Lottery Rewards")
    tabview.add("Battle Minigame")
    tabview.add("Star Handicaps")
    tabview.set("Coins Mods")

    # Function to create an entry field and checkbox
    def create_entry(tab, row, icon_path, label_text, color, placerholder):
        create_image_icon(tab, icon_path, row, 1)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=2, sticky="w", pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"), placeholder_text=placerholder)
        entry.grid(row=row, column=3)
        label1 = ctk.CTkLabel(master=tab, text=color, font=("Arial", 16))
        label1.grid(row=row, column=4, sticky="w")
        return entry

    # Create entry fields and checkboxes for Coins Mods tab
    blue_entry = create_entry(tabview.tab("Coins Mods"), 1, "assets/eventTags/blueSpace.png", " Gain  ", " Coins on a Blue Space.", "3")
    red_entry = create_entry(tabview.tab("Coins Mods"), 2, "assets/eventTags/redSpace.png", " Lose  ", " Coins on a Red Space.", "3")
    mgWin_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/miniGame.png", " Gain  ", " Coins when winning a Minigame.", "10")
    star_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star.", "20")
    mega_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/items/megaMushroom.png", " Gain ", " Coins when squishing a player.", "10")
    bowser_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/items/bowserSuit4.png", " Gain ", " Coins when squishing a player.", "30")
    booHouseStar_entry = create_entry(tabview.tab("Coins Mods"), 7, "assets/eventTags/booHouseStars.png", " Costs ", " Coins when stealing a Star.", "50")
    booHouseCoins_entry = create_entry(tabview.tab("Coins Mods"), 8, "assets/eventTags/booHouseCoins.png", " Costs ", " Coins when stealing coins.", "5")
    booHouseCoinsMin_entry = create_entry(tabview.tab("Coins Mods"), 9, "assets/eventTags/booHouseCoins.png", " Steal ", " Minimum when stealing coins.", "")
    lottery_entry = create_entry(tabview.tab("Coins Mods"), 10, "assets/eventTags/lottery4.png", " Costs ", " Coins to play the Lottery.", "5")
    initial_entry = create_entry(tabview.tab("Coins Mods"), 11, "assets/eventTags/initialCoins.png", " Gain ", " Coins at the start of the game.", "10")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp4(blue_entry, red_entry, mgWin_entry, star_entry, mega_entry, booHouseStar_entry, booHouseCoins_entry, lottery_entry, booHouseCoinsMin_entry, bowser_entry, initial_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

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
    parse_minigame_button.place(x=10, y=800)

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
    parseButtonThree.place(x=10, y=800)

    parseButtonFour = ctk.CTkButton(master=tabview.tab("Item Mods"), command=lambda: savePresetItems4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4), text="Save Preset")
    parseButtonFour.place(x=160, y=800)

    parseButtonFour = ctk.CTkButton(master=tabview.tab("Item Mods"), command=lambda: loadPresetItems4(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4), text="Load Preset")
    parseButtonFour.place(x=310, y=800)

    items4 = ["None", "Mini Mushroom", "Mega Mushroom", "Super Mini Mushroom", "Super Mega Mushroom", "Mini-Mega Hammer", "Warp Pipe", "Swap Card", "Sparky Sticker", "Gaddlight", "Chomp Call", "Bowser Suit", "Boo's Crystal Ball", "Magic Lamp", "Item Bag"]
    
    parseButtonFiveFillViaCode = ctk.CTkButton(master=tabview.tab("Item Mods"), command=lambda: fillViaCode4Actions(), text="Fill Via Code")
    parseButtonFiveFillViaCode.place(x=460, y=800)

    def fillViaCode4Actions():
        top = ctk.CTkToplevel(height=500, width=500)
        top.attributes('-topmost', True)
        top.title("Enter Code")
        
        enterCodeLabel = ctk.CTkLabel(master=top, text="Enter Code")
        enterCodeLabel.place(x=10, y=10)
        
        codeText = ctk.CTkTextbox(master=top, width=200, height=400)
        codeText.place(x=10, y=65)

        submitButton = ctk.CTkButton(master=top, command=lambda: fillViaCode4(top, codeText, miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, sparkyStickerPrice4, sparkyStickerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, bowserSuitPrice4, bowserSuitWeight4, gaddlightPrice4, gaddlightWeight4, magicLampPrice4, magicLampWeight4, crystalBallPrice4, crystalBallWeight4, chompCallPrice4, chompCallWeight4, itemBagPrice4, itemBagWeight4), text="Submit")
        submitButton.place(x=250, y=425)

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
    parseButton.place(x=10, y=800)
    
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
    parseButton.place(x=10, y=800)

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

    parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=lambda: spaceReplaceEvent_mp4(spaceRep411, spaceRep421, spaceRep412, spaceRep422, spaces4), text="Generate Codes")
    parseButton.place(x=10, y=800)

    icon = create_image_icon(tabview.tab("Star Handicaps"), "assets/eventTags/starSpace.png", 0, 0)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" P1 Starts with  ", font=("Arial", 16))
    label.grid(row=0, column=1)
    p1Stars = ctk.CTkEntry(master=tabview.tab("Star Handicaps"), width=48, font=("Arial", 16, "bold"))
    p1Stars.grid(row=0, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" Stars ", font=("Arial", 16))
    label.grid(row=0, column=3)
    
    icon = create_image_icon(tabview.tab("Star Handicaps"), "assets/eventTags/starSpace.png", 1, 0)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" P2 Starts with  ", font=("Arial", 16))
    label.grid(row=1, column=1)
    p2Stars = ctk.CTkEntry(master=tabview.tab("Star Handicaps"), width=48, font=("Arial", 16, "bold"))
    p2Stars.grid(row=1, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" Stars ", font=("Arial", 16))
    label.grid(row=1, column=3)

    icon = create_image_icon(tabview.tab("Star Handicaps"), "assets/eventTags/starSpace.png", 2, 0)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" P3 Starts with  ", font=("Arial", 16))
    label.grid(row=2, column=1)
    p3Stars = ctk.CTkEntry(master=tabview.tab("Star Handicaps"), width=48, font=("Arial", 16, "bold"))
    p3Stars.grid(row=2, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" Stars ", font=("Arial", 16))
    label.grid(row=2, column=3)

    icon = create_image_icon(tabview.tab("Star Handicaps"), "assets/eventTags/starSpace.png", 3, 0)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" P4 Starts with  ", font=("Arial", 16))
    label.grid(row=3, column=1)
    p4Stars = ctk.CTkEntry(master=tabview.tab("Star Handicaps"), width=48, font=("Arial", 16, "bold"))
    p4Stars.grid(row=3, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" Stars ", font=("Arial", 16))
    label.grid(row=3, column=3)

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp4(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 5 Coins with  ", font=("Arial", 16))
    label.grid(row=0, column=1, pady=10)
    fiveCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    fiveCoins.grid(row=0, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=0, column=3)
    
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 10 Coins with  ", font=("Arial", 16))
    label.grid(row=1, column=1, pady=10)
    tenCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    tenCoins.grid(row=1, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=1, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 20 Coins with  ", font=("Arial", 16))
    label.grid(row=2, column=1, pady=10)
    twentyCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    twentyCoins.grid(row=2, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=2, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 30 Coins with  ", font=("Arial", 16))
    label.grid(row=3, column=1, pady=10)
    thirtyCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    thirtyCoins.grid(row=3, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=3, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 50 Coins with  ", font=("Arial", 16))
    label.grid(row=4, column=1, pady=10)
    fiftyCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    fiftyCoins.grid(row=4, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=4, column=3)

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Battle Minigame"), command=lambda: battleCoins_mp4(fiveCoins, tenCoins, twentyCoins, thirtyCoins, fiftyCoins), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    return frame