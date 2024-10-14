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

    # ITEM GEN
    scrollable_frame = ctk.CTkFrame(master=tabview.tab("Item Mods"), fg_color=("#fcfcfc", "#2e2e2e"))
    scrollable_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 50))
    # Configure grid to allow stretching
    tabview.tab("Item Mods").grid_rowconfigure(0, weight=1)
    tabview.tab("Item Mods").grid_columnconfigure(0, weight=1)
    scrollable_frame.grid_rowconfigure(0, weight=1)

    # Create a canvas for scrolling
    canvas = ctk.CTkCanvas(master=scrollable_frame, bg="#2e2e2e", highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Create a vertical scrollbar linked to the canvas
    scrollbar = ctk.CTkScrollbar(master=scrollable_frame, orientation="vertical", command=canvas.yview, fg_color=("#ffffff", "#3a3a3a"))
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configure the canvas to work with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the content
    content_frame = ctk.CTkFrame(master=canvas, fg_color=("#fcfcfc", "#2e2e2e"))
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Function to update the scroll region
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    content_frame.bind("<Configure>", update_scroll_region)
    
    # Configure the canvas to fill the width of the scrollable frame
    scrollable_frame.grid_columnconfigure(0, weight=1)  # Ensure the canvas fills the width
    canvas.grid_rowconfigure(0, weight=1)  # Ensure the canvas fills the heigh

    # Mini Mushroom
    icon = create_image_icon(content_frame, "assets/items/miniMushroom.png", 2, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=2, column=2)
    miniMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMushroomPrice1.grid(row=2, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=2, column=4)
    miniMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMushroomPrice2.grid(row=2, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=2, column=6)
    miniMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMushroomPrice34.grid(row=2, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=2, column=8)
    miniMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMushroomShopOdds12.grid(row=2, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=2, column=10)
    miniMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMushroomShopOdds34.grid(row=2, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=2, column=12)
    miniMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMushroomSpaceOdds1.grid(row=2, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=2, column=14)
    miniMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMushroomSpaceOdds2.grid(row=2, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=2, column=16)
    miniMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMushroomSpaceOdds34.grid(row=2, column=17)

    # Mega Mushroom
    icon = create_image_icon(content_frame, "assets/items/megaMushroom.png", 3, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=3, column=2)
    megaMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    megaMushroomPrice1.grid(row=3, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=3, column=4)
    megaMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    megaMushroomPrice2.grid(row=3, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=3, column=6)
    megaMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    megaMushroomPrice34.grid(row=3, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=3, column=8)
    megaMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    megaMushroomShopOdds12.grid(row=3, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=3, column=10)
    megaMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    megaMushroomShopOdds34.grid(row=3, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=3, column=12)
    megaMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    megaMushroomSpaceOdds1.grid(row=3, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=3, column=14)
    megaMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    megaMushroomSpaceOdds2.grid(row=3, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=3, column=16)
    megaMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    megaMushroomSpaceOdds34.grid(row=3, column=17)

    # Super Mini Mushroom
    icon = create_image_icon(content_frame, "assets/items/superMiniMushroom.png", 4, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=4, column=2)
    superMiniMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMiniMushroomPrice1.grid(row=4, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=4, column=4)
    superMiniMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMiniMushroomPrice2.grid(row=4, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=4, column=6)
    superMiniMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMiniMushroomPrice34.grid(row=4, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=4, column=8)
    superMiniMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMiniMushroomShopOdds12.grid(row=4, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=4, column=10)
    superMiniMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMiniMushroomShopOdds34.grid(row=4, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=4, column=12)
    superMiniMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMiniMushroomSpaceOdds1.grid(row=4, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=4, column=14)
    superMiniMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMiniMushroomSpaceOdds2.grid(row=4, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=4, column=16)
    superMiniMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMiniMushroomSpaceOdds34.grid(row=4, column=17)

    # Super Mega Mushroom
    icon = create_image_icon(content_frame, "assets/items/superMegaMushroom.png", 5, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=5, column=2)
    superMegaMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMegaMushroomPrice1.grid(row=5, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=5, column=4)
    superMegaMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMegaMushroomPrice2.grid(row=5, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=5, column=6)
    superMegaMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMegaMushroomPrice34.grid(row=5, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=5, column=8)
    superMegaMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMegaMushroomShopOdds12.grid(row=5, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=5, column=10)
    superMegaMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMegaMushroomShopOdds34.grid(row=5, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=5, column=12)
    superMegaMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMegaMushroomSpaceOdds1.grid(row=5, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=5, column=14)
    superMegaMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMegaMushroomSpaceOdds2.grid(row=5, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=5, column=16)
    superMegaMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    superMegaMushroomSpaceOdds34.grid(row=5, column=17)

    # Mini-Mega Hammer
    icon = create_image_icon(content_frame, "assets/items/miniMegaHammer.png", 6, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=6, column=2)
    miniMegaHammerPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMegaHammerPrice1.grid(row=6, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=6, column=4)
    miniMegaHammerPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMegaHammerPrice2.grid(row=6, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=6, column=6)
    miniMegaHammerPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMegaHammerPrice34.grid(row=6, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=6, column=8)
    miniMegaHammerShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMegaHammerShopOdds12.grid(row=6, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=6, column=10)
    miniMegaHammerShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMegaHammerShopOdds34.grid(row=6, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=6, column=12)
    miniMegaHammerSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMegaHammerSpaceOdds1.grid(row=6, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=6, column=14)
    miniMegaHammerSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMegaHammerSpaceOdds2.grid(row=6, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=6, column=16)
    miniMegaHammerSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    miniMegaHammerSpaceOdds34.grid(row=6, column=17)

    # Warp Pipe
    icon = create_image_icon(content_frame, "assets/items/warpPipe.png", 7, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=7, column=2)
    warpPipePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpPipePrice1.grid(row=7, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=7, column=4)
    warpPipePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpPipePrice2.grid(row=7, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=7, column=6)
    warpPipePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpPipePrice34.grid(row=7, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=7, column=8)
    warpPipeShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpPipeShopOdds12.grid(row=7, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=7, column=10)
    warpPipeShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpPipeShopOdds34.grid(row=7, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=7, column=12)
    warpPipeSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpPipeSpaceOdds1.grid(row=7, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=7, column=14)
    warpPipeSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpPipeSpaceOdds2.grid(row=7, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=7, column=16)
    warpPipeSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpPipeSpaceOdds34.grid(row=7, column=17)

    # Swap Card
    icon = create_image_icon(content_frame, "assets/items/swapCard.png", 8, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=8, column=2)
    swapCardPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    swapCardPrice1.grid(row=8, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=8, column=4)
    swapCardPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    swapCardPrice2.grid(row=8, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=8, column=6)
    swapCardPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    swapCardPrice34.grid(row=8, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=8, column=8)
    swapCardShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    swapCardShopOdds12.grid(row=8, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=8, column=10)
    swapCardShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    swapCardShopOdds34.grid(row=8, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=8, column=12)
    swapCardSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    swapCardSpaceOdds1.grid(row=8, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=8, column=14)
    swapCardSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    swapCardSpaceOdds2.grid(row=8, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=8, column=16)
    swapCardSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    swapCardSpaceOdds34.grid(row=8, column=17)

    # Sparky Sticker
    icon = create_image_icon(content_frame, "assets/items/sparkySticker.png", 9, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=9, column=2)
    sparkyStickerPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    sparkyStickerPrice1.grid(row=9, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=9, column=4)
    sparkyStickerPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    sparkyStickerPrice2.grid(row=9, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=9, column=6)
    sparkyStickerPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    sparkyStickerPrice34.grid(row=9, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=9, column=8)
    sparkyStickerShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    sparkyStickerShopOdds12.grid(row=9, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=9, column=10)
    sparkyStickerShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    sparkyStickerShopOdds34.grid(row=9, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=9, column=12)
    sparkyStickerSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    sparkyStickerSpaceOdds1.grid(row=9, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=9, column=14)
    sparkyStickerSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    sparkyStickerSpaceOdds2.grid(row=9, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=9, column=16)
    sparkyStickerSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    sparkyStickerSpaceOdds34.grid(row=9, column=17)

    # Gaddlight
    icon = create_image_icon(content_frame, "assets/items/gaddlight.png", 10, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=10, column=2)
    gaddlightPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    gaddlightPrice1.grid(row=10, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=10, column=4)
    gaddlightPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    gaddlightPrice2.grid(row=10, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=10, column=6)
    gaddlightPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    gaddlightPrice34.grid(row=10, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=10, column=8)
    gaddlightShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    gaddlightShopOdds12.grid(row=10, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=10, column=10)
    gaddlightShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    gaddlightShopOdds34.grid(row=10, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=10, column=12)
    gaddlightSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    gaddlightSpaceOdds1.grid(row=10, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=10, column=14)
    gaddlightSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    gaddlightSpaceOdds2.grid(row=10, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=10, column=16)
    gaddlightSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    gaddlightSpaceOdds34.grid(row=10, column=17)

    # Chomp Call
    icon = create_image_icon(content_frame, "assets/items/chompCall.png", 11, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=11, column=2)
    chompCallPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    chompCallPrice1.grid(row=11, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=11, column=4)
    chompCallPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    chompCallPrice2.grid(row=11, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=11, column=6)
    chompCallPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    chompCallPrice34.grid(row=11, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=11, column=8)
    chompCallShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    chompCallShopOdds12.grid(row=11, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=11, column=10)
    chompCallShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    chompCallShopOdds34.grid(row=11, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=11, column=12)
    chompCallSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    chompCallSpaceOdds1.grid(row=11, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=11, column=14)
    chompCallSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    chompCallSpaceOdds2.grid(row=11, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=11, column=16)
    chompCallSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    chompCallSpaceOdds34.grid(row=11, column=17)

    # Bowser Suit
    icon = create_image_icon(content_frame, "assets/items/bowserSuit4.png", 12, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=12, column=2)
    bowserSuitPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bowserSuitPrice1.grid(row=12, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=12, column=4)
    bowserSuitPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bowserSuitPrice2.grid(row=12, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=12, column=6)
    bowserSuitPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bowserSuitPrice34.grid(row=12, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=12, column=8)
    bowserSuitShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bowserSuitShopOdds12.grid(row=12, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=12, column=10)
    bowserSuitShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bowserSuitShopOdds34.grid(row=12, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=12, column=12)
    bowserSuitSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bowserSuitSpaceOdds1.grid(row=12, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=12, column=14)
    bowserSuitSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bowserSuitSpaceOdds2.grid(row=12, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=12, column=16)
    bowserSuitSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bowserSuitSpaceOdds34.grid(row=12, column=17)

    # Boo's Crystal Ball
    icon = create_image_icon(content_frame, "assets/items/crystalBall.png", 13, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=13, column=2)
    crystalBallPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    crystalBallPrice1.grid(row=13, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=13, column=4)
    crystalBallPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    crystalBallPrice2.grid(row=13, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=13, column=6)
    crystalBallPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    crystalBallPrice34.grid(row=13, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=13, column=8)
    crystalBallShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    crystalBallShopOdds12.grid(row=13, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=13, column=10)
    crystalBallShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    crystalBallShopOdds34.grid(row=13, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=13, column=12)
    crystalBallSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    crystalBallSpaceOdds1.grid(row=13, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=13, column=14)
    crystalBallSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    crystalBallSpaceOdds2.grid(row=13, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=13, column=16)
    crystalBallSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    crystalBallSpaceOdds34.grid(row=13, column=17)

    # Magic Lamp
    icon = create_image_icon(content_frame, "assets/items/magicLamp4.png", 14, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=14, column=2)
    magicLampPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicLampPrice1.grid(row=14, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=14, column=4)
    magicLampPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicLampPrice2.grid(row=14, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=14, column=6)
    magicLampPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicLampPrice34.grid(row=14, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=14, column=8)
    magicLampShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicLampShopOdds12.grid(row=14, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=14, column=10)
    magicLampShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicLampShopOdds34.grid(row=14, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=14, column=12)
    magicLampSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicLampSpaceOdds1.grid(row=14, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=14, column=14)
    magicLampSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicLampSpaceOdds2.grid(row=14, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=14, column=16)
    magicLampSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicLampSpaceOdds34.grid(row=14, column=17)

    # Item Bag
    icon = create_image_icon(content_frame, "assets/items/itemBag4.png", 15, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=15, column=2)
    itemBagPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    itemBagPrice1.grid(row=15, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=15, column=4)
    itemBagPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    itemBagPrice2.grid(row=15, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=15, column=6)
    itemBagPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    itemBagPrice34.grid(row=15, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=15, column=8)
    itemBagShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    itemBagShopOdds12.grid(row=15, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=15, column=10)
    itemBagShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    itemBagShopOdds34.grid(row=15, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=15, column=12)
    itemBagSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    itemBagSpaceOdds1.grid(row=15, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=15, column=14)
    itemBagSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    itemBagSpaceOdds2.grid(row=15, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=15, column=16)
    itemBagSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    itemBagSpaceOdds34.grid(row=15, column=17)

    # Mushroom: DX
    icon = create_image_icon(content_frame, "assets/items/mushroom4.png", 16, 1)
    labelMushroom1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    mushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMushroom2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    mushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMushroom3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    mushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMushroom4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    mushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMushroom5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    mushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMushroom6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    mushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMushroom7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    mushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMushroom8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    mushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Golden Mushroom: DX
    icon = create_image_icon(content_frame, "assets/items/goldenMushroom4.png", 17, 1)
    labelGoldenMushroom1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    goldenMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGoldenMushroom2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    goldenMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGoldenMushroom3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    goldenMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGoldenMushroom4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    goldenMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGoldenMushroom5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    goldenMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGoldenMushroom6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    goldenMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGoldenMushroom7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    goldenMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGoldenMushroom8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    goldenMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Reverse Mushroom: DX
    icon = create_image_icon(content_frame, "assets/items/reverseMushroom.png", 18, 1)
    labelReverseMushroom1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    reverseMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelReverseMushroom2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    reverseMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelReverseMushroom3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    reverseMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelReverseMushroom4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    reverseMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelReverseMushroom5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    reverseMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelReverseMushroom6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    reverseMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelReverseMushroom7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    reverseMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelReverseMushroom8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    reverseMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    
    # Poison Mushroom: DX
    icon = create_image_icon(content_frame, "assets/items/poisonMushroom.png", 19, 1)
    labelPoisonMushroom1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    poisonMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPoisonMushroom2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    poisonMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPoisonMushroom3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    poisonMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPoisonMushroom4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    poisonMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPoisonMushroom5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    poisonMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPoisonMushroom6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    poisonMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPoisonMushroom7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    poisonMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPoisonMushroom8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    poisonMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Triple Poison Mushroom: DX
    icon = create_image_icon(content_frame, "assets/items/triplePoison.png", 20, 1)
    labelTriplePoisonMushroom1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    triplePoisonMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelTriplePoisonMushroom2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    triplePoisonMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelTriplePoisonMushroom3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    triplePoisonMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelTriplePoisonMushroom4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    triplePoisonMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelTriplePoisonMushroom5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    triplePoisonMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelTriplePoisonMushroom6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    triplePoisonMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelTriplePoisonMushroom7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    triplePoisonMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelTriplePoisonMushroom8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    triplePoisonMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    
    # Celluar Shopper: DX
    icon = create_image_icon(content_frame, "assets/items/celluarShopper.png", 21, 1)
    labelCelluarShopper1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    celluarShopperPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelCelluarShopper2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    celluarShopperPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelCelluarShopper3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    celluarShopperPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelCelluarShopper4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    celluarShopperShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelCelluarShopper5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    celluarShopperShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelCelluarShopper6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    celluarShopperSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelCelluarShopper7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    celluarShopperSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelCelluarShopper8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    celluarShopperSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))

    # Skeleton Key: DX
    icon = create_image_icon(content_frame, "assets/items/skeletonKey.png", 22, 1)
    labelSkeletonKey1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    skeletonKeyPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSkeletonKey2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    skeletonKeyPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSkeletonKey3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    skeletonKeyPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSkeletonKey4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    skeletonKeyShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSkeletonKey5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    skeletonKeyShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSkeletonKey6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    skeletonKeySpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSkeletonKey7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    skeletonKeySpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSkeletonKey8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    skeletonKeySpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Plunder Chest: DX
    icon = create_image_icon(content_frame, "assets/items/plunderChest.png", 23, 1)
    labelPlunderChest1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    plunderChestPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlunderChest2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    plunderChestPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlunderChest3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    plunderChestPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlunderChest4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    plunderChestShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlunderChest5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    plunderChestShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlunderChest6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    plunderChestSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlunderChest7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    plunderChestSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlunderChest8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    plunderChestSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))

    # Gaddbrush: DX
    icon = create_image_icon(content_frame, "assets/items/gaddbrush.png", 24, 1)
    labelGaddbrush1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    gaddbrushPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGaddbrush2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    gaddbrushPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGaddbrush3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    gaddbrushPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGaddbrush4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    gaddbrushShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGaddbrush5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    gaddbrushShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGaddbrush6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    gaddbrushSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGaddbrush7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    gaddbrushSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelGaddbrush8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    gaddbrushSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    
    # Warp Block: DX
    icon = create_image_icon(content_frame, "assets/items/warpBlock.png", 25, 1)
    labelWarpBlock1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    warpBlockPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWarpBlock2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    warpBlockPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWarpBlock3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    warpBlockPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWarpBlock4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    warpBlockShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWarpBlock5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    warpBlockShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWarpBlock6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    warpBlockSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWarpBlock7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    warpBlockSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWarpBlock8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    warpBlockSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Fly Guy: DX
    icon = create_image_icon(content_frame, "assets/items/flyGuy.png", 26, 1)
    labelFlyGuy1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    flyGuyPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelFlyGuy2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    flyGuyPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelFlyGuy3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    flyGuyPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelFlyGuy4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    flyGuyShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelFlyGuy5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    flyGuyShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelFlyGuy6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    flyGuySpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelFlyGuy7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    flyGuySpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelFlyGuy8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    flyGuySpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Plus Block: DX
    icon = create_image_icon(content_frame, "assets/items/plusBlock.png", 27, 1)
    labelPlusBlock1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    plusBlockPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlusBlock2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    plusBlockPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlusBlock3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    plusBlockPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlusBlock4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    plusBlockShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlusBlock5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    plusBlockShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlusBlock6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    plusBlockSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlusBlock7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    plusBlockSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelPlusBlock8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    plusBlockSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Minus Block: DX
    icon = create_image_icon(content_frame, "assets/items/minusBlock.png", 28, 1)
    labelMinusBlock1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    minusBlockPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMinusBlock2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    minusBlockPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMinusBlock3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    minusBlockPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMinusBlock4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    minusBlockShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMinusBlock5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    minusBlockShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMinusBlock6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    minusBlockSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMinusBlock7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    minusBlockSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelMinusBlock8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    minusBlockSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Speed Block: DX
    icon = create_image_icon(content_frame, "assets/items/speedBlock.png", 29, 1)
    labelSpeedBlock1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    speedBlockPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSpeedBlock2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    speedBlockPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSpeedBlock3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    speedBlockPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSpeedBlock4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    speedBlockShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSpeedBlock5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    speedBlockShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSpeedBlock6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    speedBlockSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSpeedBlock7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    speedBlockSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSpeedBlock8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    speedBlockSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Slow Block: DX
    icon = create_image_icon(content_frame, "assets/items/slowBlock.png", 30, 1)
    labelSlowBlock1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    slowBlockPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSlowBlock2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    slowBlockPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSlowBlock3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    slowBlockPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSlowBlock4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    slowBlockShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSlowBlock5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    slowBlockShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSlowBlock6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    slowBlockSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSlowBlock7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    slowBlockSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSlowBlock8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    slowBlockSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    
    # Bowser Phone: DX
    icon = create_image_icon(content_frame, "assets/items/bowserPhone.png", 31, 1)
    labelBowserPhone1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    bowserPhonePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBowserPhone2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    bowserPhonePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBowserPhone3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    bowserPhonePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBowserPhone4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    bowserPhoneShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBowserPhone5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    bowserPhoneShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBowserPhone6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    bowserPhoneSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBowserPhone7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    bowserPhoneSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBowserPhone8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    bowserPhoneSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Double Dip: DX
    icon = create_image_icon(content_frame, "assets/items/doubleDip.png", 32, 1)
    labelDoubleDip1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    doubleDipPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelDoubleDip2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    doubleDipPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelDoubleDip3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    doubleDipPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelDoubleDip4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    doubleDipShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelDoubleDip5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    doubleDipShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelDoubleDip6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    doubleDipSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelDoubleDip7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    doubleDipSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelDoubleDip8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    doubleDipSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Hidden Block Card: DX
    icon = create_image_icon(content_frame, "assets/items/hiddenBlockCard.png", 33, 1)
    labelHiddenBlockCard1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    hiddenBlockCardPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelHiddenBlockCard2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    hiddenBlockCardPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelHiddenBlockCard3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    hiddenBlockCardPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelHiddenBlockCard4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    hiddenBlockCardShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelHiddenBlockCard5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    hiddenBlockCardShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelHiddenBlockCard6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    hiddenBlockCardSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelHiddenBlockCard7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    hiddenBlockCardSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelHiddenBlockCard8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    hiddenBlockCardSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))

    # Barter Box: DX
    icon = create_image_icon(content_frame, "assets/items/barterBox.png", 34, 1)
    labelBarterBox1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    barterBoxPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBarterBox2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    barterBoxPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBarterBox3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    barterBoxPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBarterBox4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    barterBoxShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBarterBox5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    barterBoxShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBarterBox6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    barterBoxSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBarterBox7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    barterBoxSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelBarterBox8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    barterBoxSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Super Warp Pipe: DX
    icon = create_image_icon(content_frame, "assets/items/superWarpPipe.png", 35, 1)
    labelSuperWarpPipe1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    superWarpPipePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSuperWarpPipe2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    superWarpPipePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSuperWarpPipe3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    superWarpPipePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSuperWarpPipe4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    superWarpPipeShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSuperWarpPipe5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    superWarpPipeShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSuperWarpPipe6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    superWarpPipeSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSuperWarpPipe7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    superWarpPipeSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelSuperWarpPipe8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    superWarpPipeSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
 
    # Chance Time Charm: DX
    icon = create_image_icon(content_frame, "assets/items/chanceTimeCharm.png", 36, 1)
    labelChanceTimeCharm1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    chanceTimeCharmPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelChanceTimeCharm2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    chanceTimeCharmPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelChanceTimeCharm3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    chanceTimeCharmPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelChanceTimeCharm4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    chanceTimeCharmShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelChanceTimeCharm5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    chanceTimeCharmShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelChanceTimeCharm6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    chanceTimeCharmSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelChanceTimeCharm7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    chanceTimeCharmSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelChanceTimeCharm8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    chanceTimeCharmSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    
    # Wacky Watch: DX
    icon = create_image_icon(content_frame, "assets/items/wackyWatch.png", 37, 1)
    labelWackyWatch1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    wackyWatchPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWackyWatch2 = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    wackyWatchPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWackyWatch3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    wackyWatchPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWackyWatch4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    wackyWatchShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWackyWatch5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    wackyWatchShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWackyWatch6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    wackyWatchSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWackyWatch7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    wackyWatchSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    labelWackyWatch8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    wackyWatchSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))

    global hide_custom
    hide_custom = False

    global hide_itemSpace
    hide_itemSpace = False


    def handle_button_command():
        if hide_custom and (hide_itemSpace):
            itemsEvent_mp4(
                miniMushroomPrice1, miniMushroomPrice2, miniMushroomPrice34,
                miniMushroomShopOdds12, miniMushroomShopOdds34,
                miniMushroomSpaceOdds1, miniMushroomSpaceOdds2, miniMushroomSpaceOdds34,
                megaMushroomPrice1, megaMushroomPrice2, megaMushroomPrice34,
                megaMushroomShopOdds12, megaMushroomShopOdds34,
                megaMushroomSpaceOdds1, megaMushroomSpaceOdds2, megaMushroomSpaceOdds34,
                superMiniMushroomPrice1, superMiniMushroomPrice2, superMiniMushroomPrice34,
                superMiniMushroomShopOdds12, superMiniMushroomShopOdds34,
                superMiniMushroomSpaceOdds1, superMiniMushroomSpaceOdds2, superMiniMushroomSpaceOdds34,
                superMegaMushroomPrice1, superMegaMushroomPrice2, superMegaMushroomPrice34,
                superMegaMushroomShopOdds12, superMegaMushroomShopOdds34,
                superMegaMushroomSpaceOdds1, superMegaMushroomSpaceOdds2, superMiniMushroomSpaceOdds34,
                miniMegaHammerPrice1, miniMegaHammerPrice2, miniMegaHammerPrice34,
                miniMegaHammerShopOdds12, miniMegaHammerShopOdds34,
                miniMegaHammerSpaceOdds1, miniMegaHammerSpaceOdds2, miniMegaHammerSpaceOdds34,
                warpPipePrice1, warpPipePrice2, warpPipePrice34,
                warpPipeShopOdds12, warpPipeShopOdds34,
                warpPipeSpaceOdds1, warpPipeSpaceOdds2, warpPipeSpaceOdds34,
                swapCardPrice1, swapCardPrice2, swapCardPrice34,
                swapCardShopOdds12, swapCardShopOdds34,
                swapCardSpaceOdds1, swapCardSpaceOdds2, swapCardSpaceOdds34,
                sparkyStickerPrice1, sparkyStickerPrice2, sparkyStickerPrice34,
                sparkyStickerShopOdds12, sparkyStickerShopOdds34,
                sparkyStickerSpaceOdds1, sparkyStickerSpaceOdds2, sparkyStickerSpaceOdds34,
                gaddlightPrice1, gaddlightPrice2, gaddlightPrice34,
                gaddlightShopOdds12, gaddlightShopOdds34,
                gaddlightSpaceOdds1, gaddlightSpaceOdds2, gaddlightSpaceOdds34,
                chompCallPrice1, chompCallPrice2, chompCallPrice34,
                chompCallShopOdds12, chompCallShopOdds34,
                chompCallSpaceOdds1, chompCallSpaceOdds2, chompCallSpaceOdds34,
                bowserSuitPrice1, bowserSuitPrice2, bowserSuitPrice34,
                bowserSuitShopOdds12, bowserSuitShopOdds34,
                bowserSuitSpaceOdds1, bowserSuitSpaceOdds2, bowserSuitSpaceOdds34,
                crystalBallPrice1, crystalBallPrice2, crystalBallPrice34,
                crystalBallShopOdds12, crystalBallShopOdds34,
                crystalBallSpaceOdds1, crystalBallSpaceOdds2, crystalBallSpaceOdds34,
                magicLampPrice1, magicLampPrice2, magicLampPrice34,
                magicLampShopOdds12, magicLampShopOdds34,
                magicLampSpaceOdds1, magicLampSpaceOdds2, magicLampSpaceOdds34,
                itemBagPrice1, itemBagPrice2, itemBagPrice34,
                itemBagShopOdds12, itemBagShopOdds34,
                itemBagSpaceOdds1, itemBagSpaceOdds2, itemBagSpaceOdds34
            )
        elif hide_custom and (not hide_itemSpace):
            itemsEvent_mp4ItemSpace(
                miniMushroomPrice1, miniMushroomPrice2, miniMushroomPrice34,
                miniMushroomShopOdds12, miniMushroomShopOdds34,
                megaMushroomPrice1, megaMushroomPrice2, megaMushroomPrice34,
                megaMushroomShopOdds12, megaMushroomShopOdds34,
                superMiniMushroomPrice1, superMiniMushroomPrice2, superMiniMushroomPrice34,
                superMiniMushroomShopOdds12, superMiniMushroomShopOdds34,
                superMegaMushroomPrice1, superMegaMushroomPrice2, superMegaMushroomPrice34,
                superMegaMushroomShopOdds12, superMegaMushroomShopOdds34,
                miniMegaHammerPrice1, miniMegaHammerPrice2, miniMegaHammerPrice34,
                miniMegaHammerShopOdds12, miniMegaHammerShopOdds34,
                warpPipePrice1, warpPipePrice2, warpPipePrice34,
                warpPipeShopOdds12, warpPipeShopOdds34,
                swapCardPrice1, swapCardPrice2, swapCardPrice34,
                swapCardShopOdds12, swapCardShopOdds34,
                sparkyStickerPrice1, sparkyStickerPrice2, sparkyStickerPrice34,
                sparkyStickerShopOdds12, sparkyStickerShopOdds34,
                gaddlightPrice1, gaddlightPrice2, gaddlightPrice34,
                gaddlightShopOdds12, gaddlightShopOdds34,
                chompCallPrice1, chompCallPrice2, chompCallPrice34,
                chompCallShopOdds12, chompCallShopOdds34,
                bowserSuitPrice1, bowserSuitPrice2, bowserSuitPrice34,
                bowserSuitShopOdds12, bowserSuitShopOdds34,
                crystalBallPrice1, crystalBallPrice2, crystalBallPrice34,
                crystalBallShopOdds12, crystalBallShopOdds34,
                magicLampPrice1, magicLampPrice2, magicLampPrice34,
                magicLampShopOdds12, magicLampShopOdds34,
                itemBagPrice1, itemBagPrice2, itemBagPrice34,
                itemBagShopOdds12, itemBagShopOdds34
            )
        elif (not hide_custom) and (hide_itemSpace):
            itemsEvent_mp4Custom(
                miniMushroomPrice1, miniMushroomPrice2, miniMushroomPrice34,
                miniMushroomShopOdds12, miniMushroomShopOdds34,
                miniMushroomSpaceOdds1, miniMushroomSpaceOdds2, miniMushroomSpaceOdds34,
                megaMushroomPrice1, megaMushroomPrice2, megaMushroomPrice34,
                megaMushroomShopOdds12, megaMushroomShopOdds34,
                megaMushroomSpaceOdds1, megaMushroomSpaceOdds2, megaMushroomSpaceOdds34,
                superMiniMushroomPrice1, superMiniMushroomPrice2, superMiniMushroomPrice34,
                superMiniMushroomShopOdds12, superMiniMushroomShopOdds34,
                superMiniMushroomSpaceOdds1, superMiniMushroomSpaceOdds2, superMiniMushroomSpaceOdds34,
                superMegaMushroomPrice1, superMegaMushroomPrice2, superMegaMushroomPrice34,
                superMegaMushroomShopOdds12, superMegaMushroomShopOdds34,
                superMegaMushroomSpaceOdds1, superMegaMushroomSpaceOdds2, superMiniMushroomSpaceOdds34,
                miniMegaHammerPrice1, miniMegaHammerPrice2, miniMegaHammerPrice34,
                miniMegaHammerShopOdds12, miniMegaHammerShopOdds34,
                miniMegaHammerSpaceOdds1, miniMegaHammerSpaceOdds2, miniMegaHammerSpaceOdds34,
                warpPipePrice1, warpPipePrice2, warpPipePrice34,
                warpPipeShopOdds12, warpPipeShopOdds34,
                warpPipeSpaceOdds1, warpPipeSpaceOdds2, warpPipeSpaceOdds34,
                swapCardPrice1, swapCardPrice2, swapCardPrice34,
                swapCardShopOdds12, swapCardShopOdds34,
                swapCardSpaceOdds1, swapCardSpaceOdds2, swapCardSpaceOdds34,
                sparkyStickerPrice1, sparkyStickerPrice2, sparkyStickerPrice34,
                sparkyStickerShopOdds12, sparkyStickerShopOdds34,
                sparkyStickerSpaceOdds1, sparkyStickerSpaceOdds2, sparkyStickerSpaceOdds34,
                gaddlightPrice1, gaddlightPrice2, gaddlightPrice34,
                gaddlightShopOdds12, gaddlightShopOdds34,
                gaddlightSpaceOdds1, gaddlightSpaceOdds2, gaddlightSpaceOdds34,
                chompCallPrice1, chompCallPrice2, chompCallPrice34,
                chompCallShopOdds12, chompCallShopOdds34,
                chompCallSpaceOdds1, chompCallSpaceOdds2, chompCallSpaceOdds34,
                bowserSuitPrice1, bowserSuitPrice2, bowserSuitPrice34,
                bowserSuitShopOdds12, bowserSuitShopOdds34,
                bowserSuitSpaceOdds1, bowserSuitSpaceOdds2, bowserSuitSpaceOdds34,
                crystalBallPrice1, crystalBallPrice2, crystalBallPrice34,
                crystalBallShopOdds12, crystalBallShopOdds34,
                crystalBallSpaceOdds1, crystalBallSpaceOdds2, crystalBallSpaceOdds34,
                magicLampPrice1, magicLampPrice2, magicLampPrice34,
                magicLampShopOdds12, magicLampShopOdds34,
                magicLampSpaceOdds1, magicLampSpaceOdds2, magicLampSpaceOdds34,
                itemBagPrice1, itemBagPrice2, itemBagPrice34,
                itemBagShopOdds12, itemBagShopOdds34,
                itemBagSpaceOdds1, itemBagSpaceOdds2, itemBagSpaceOdds34,
                mushroomPrice1, mushroomPrice2, mushroomPrice34,
                mushroomShopOdds12, mushroomShopOdds34,
                mushroomSpaceOdds1, mushroomSpaceOdds2, mushroomSpaceOdds34,
                goldenMushroomPrice1, goldenMushroomPrice2, goldenMushroomPrice34,
                goldenMushroomShopOdds12, goldenMushroomShopOdds34,
                goldenMushroomSpaceOdds1, goldenMushroomSpaceOdds2, goldenMushroomSpaceOdds34,
                reverseMushroomPrice1, reverseMushroomPrice2, reverseMushroomPrice34,
                reverseMushroomShopOdds12, reverseMushroomShopOdds34,
                reverseMushroomSpaceOdds1, reverseMushroomSpaceOdds2, reverseMushroomSpaceOdds34,
                poisonMushroomPrice1, poisonMushroomPrice2, poisonMushroomPrice34,
                poisonMushroomShopOdds12, poisonMushroomShopOdds34,
                poisonMushroomSpaceOdds1, poisonMushroomSpaceOdds2, poisonMushroomSpaceOdds34,
                triplePoisonMushroomPrice1, triplePoisonMushroomPrice2, triplePoisonMushroomPrice34,
                triplePoisonMushroomShopOdds12, triplePoisonMushroomShopOdds34,
                triplePoisonMushroomSpaceOdds1, triplePoisonMushroomSpaceOdds2, triplePoisonMushroomSpaceOdds34,
                celluarShopperPrice1, celluarShopperPrice2, celluarShopperPrice34,
                celluarShopperShopOdds12, celluarShopperShopOdds34,
                celluarShopperSpaceOdds1, celluarShopperSpaceOdds2, celluarShopperSpaceOdds34,
                skeletonKeyPrice1, skeletonKeyPrice2, skeletonKeyPrice34,
                skeletonKeyShopOdds12, skeletonKeyShopOdds34,
                skeletonKeySpaceOdds1, skeletonKeySpaceOdds2, skeletonKeySpaceOdds34,
                plunderChestPrice1, plunderChestPrice2, plunderChestPrice34,
                plunderChestShopOdds12, plunderChestShopOdds34,
                plunderChestSpaceOdds1, plunderChestSpaceOdds2, plunderChestSpaceOdds34,
                gaddbrushPrice1, gaddbrushPrice2, gaddbrushPrice34,
                gaddbrushShopOdds12, gaddbrushShopOdds34,
                gaddbrushSpaceOdds1, gaddbrushSpaceOdds2, gaddbrushSpaceOdds34,
                warpBlockPrice1, warpBlockPrice2, warpBlockPrice34,
                warpBlockShopOdds12, warpBlockShopOdds34,
                warpBlockSpaceOdds1, warpBlockSpaceOdds2, warpBlockSpaceOdds34,
                flyGuyPrice1, flyGuyPrice2, flyGuyPrice34,
                flyGuyShopOdds12, flyGuyShopOdds34,
                flyGuySpaceOdds1, flyGuySpaceOdds2, flyGuySpaceOdds34,
                plusBlockPrice1, plusBlockPrice2, plusBlockPrice34,
                plusBlockShopOdds12, plusBlockShopOdds34,
                plusBlockSpaceOdds1, plusBlockSpaceOdds2, plusBlockSpaceOdds34,
                minusBlockPrice1, minusBlockPrice2, minusBlockPrice34,
                minusBlockShopOdds12, minusBlockShopOdds34,
                minusBlockSpaceOdds1, minusBlockSpaceOdds2, minusBlockSpaceOdds34,
                speedBlockPrice1, speedBlockPrice2, speedBlockPrice34,
                speedBlockShopOdds12, speedBlockShopOdds34,
                speedBlockSpaceOdds1, speedBlockSpaceOdds2, speedBlockSpaceOdds34,
                slowBlockPrice1, slowBlockPrice2, slowBlockPrice34,
                slowBlockShopOdds12, slowBlockShopOdds34,
                slowBlockSpaceOdds1, slowBlockSpaceOdds2, slowBlockSpaceOdds34,
                bowserPhonePrice1, bowserPhonePrice2, bowserPhonePrice34,
                bowserPhoneShopOdds12, bowserPhoneShopOdds34,
                bowserPhoneSpaceOdds1, bowserPhoneSpaceOdds2, bowserPhoneSpaceOdds34,
                doubleDipPrice1, doubleDipPrice2, doubleDipPrice34,
                doubleDipShopOdds12, doubleDipShopOdds34,
                doubleDipSpaceOdds1, doubleDipSpaceOdds2, doubleDipSpaceOdds34,
                hiddenBlockCardPrice1, hiddenBlockCardPrice2, hiddenBlockCardPrice34,
                hiddenBlockCardShopOdds12, hiddenBlockCardShopOdds34,
                hiddenBlockCardSpaceOdds1, hiddenBlockCardSpaceOdds2, hiddenBlockCardSpaceOdds34,
                barterBoxPrice1, barterBoxPrice2, barterBoxPrice34,
                barterBoxShopOdds12, barterBoxShopOdds34,
                barterBoxSpaceOdds1, barterBoxSpaceOdds2, barterBoxSpaceOdds34,
                superWarpPipePrice1, superWarpPipePrice2, superWarpPipePrice34,
                superWarpPipeShopOdds12, superWarpPipeShopOdds34,
                superWarpPipeSpaceOdds1, superWarpPipeSpaceOdds2, superWarpPipeSpaceOdds34,
                chanceTimeCharmPrice1, chanceTimeCharmPrice2, chanceTimeCharmPrice34,
                chanceTimeCharmShopOdds12, chanceTimeCharmShopOdds34,
                chanceTimeCharmSpaceOdds1, chanceTimeCharmSpaceOdds2, chanceTimeCharmSpaceOdds34,
                wackyWatchPrice1, wackyWatchPrice2, wackyWatchPrice34,
                wackyWatchShopOdds12, wackyWatchShopOdds34,
                wackyWatchSpaceOdds1, wackyWatchSpaceOdds2, wackyWatchSpaceOdds34
            )
        elif (not hide_custom) and (not hide_itemSpace):
            itemsEvent_mp4CustomItemSpace(
                miniMushroomPrice1, miniMushroomPrice2, miniMushroomPrice34,
                miniMushroomShopOdds12, miniMushroomShopOdds34,
                megaMushroomPrice1, megaMushroomPrice2, megaMushroomPrice34,
                megaMushroomShopOdds12, megaMushroomShopOdds34,
                superMiniMushroomPrice1, superMiniMushroomPrice2, superMiniMushroomPrice34,
                superMiniMushroomShopOdds12, superMiniMushroomShopOdds34,
                superMegaMushroomPrice1, superMegaMushroomPrice2, superMegaMushroomPrice34,
                superMegaMushroomShopOdds12, superMegaMushroomShopOdds34,
                miniMegaHammerPrice1, miniMegaHammerPrice2, miniMegaHammerPrice34,
                miniMegaHammerShopOdds12, miniMegaHammerShopOdds34,
                warpPipePrice1, warpPipePrice2, warpPipePrice34,
                warpPipeShopOdds12, warpPipeShopOdds34,
                swapCardPrice1, swapCardPrice2, swapCardPrice34,
                swapCardShopOdds12, swapCardShopOdds34,
                sparkyStickerPrice1, sparkyStickerPrice2, sparkyStickerPrice34,
                sparkyStickerShopOdds12, sparkyStickerShopOdds34,
                gaddlightPrice1, gaddlightPrice2, gaddlightPrice34,
                gaddlightShopOdds12, gaddlightShopOdds34,
                chompCallPrice1, chompCallPrice2, chompCallPrice34,
                chompCallShopOdds12, chompCallShopOdds34,
                bowserSuitPrice1, bowserSuitPrice2, bowserSuitPrice34,
                bowserSuitShopOdds12, bowserSuitShopOdds34,
                crystalBallPrice1, crystalBallPrice2, crystalBallPrice34,
                crystalBallShopOdds12, crystalBallShopOdds34,
                magicLampPrice1, magicLampPrice2, magicLampPrice34,
                magicLampShopOdds12, magicLampShopOdds34,
                itemBagPrice1, itemBagPrice2, itemBagPrice34,
                itemBagShopOdds12, itemBagShopOdds34,
                mushroomPrice1, mushroomPrice2, mushroomPrice34,
                mushroomShopOdds12, mushroomShopOdds34,
                goldenMushroomPrice1, goldenMushroomPrice2, goldenMushroomPrice34,
                goldenMushroomShopOdds12, goldenMushroomShopOdds34,
                reverseMushroomPrice1, reverseMushroomPrice2, reverseMushroomPrice34,
                reverseMushroomShopOdds12, reverseMushroomShopOdds34,
                poisonMushroomPrice1, poisonMushroomPrice2, poisonMushroomPrice34,
                poisonMushroomShopOdds12, poisonMushroomShopOdds34,
                triplePoisonMushroomPrice1, triplePoisonMushroomPrice2, triplePoisonMushroomPrice34,
                triplePoisonMushroomShopOdds12, triplePoisonMushroomShopOdds34,
                celluarShopperPrice1, celluarShopperPrice2, celluarShopperPrice34,
                celluarShopperShopOdds12, celluarShopperShopOdds34,
                skeletonKeyPrice1, skeletonKeyPrice2, skeletonKeyPrice34,
                skeletonKeyShopOdds12, skeletonKeyShopOdds34,
                plunderChestPrice1, plunderChestPrice2, plunderChestPrice34,
                plunderChestShopOdds12, plunderChestShopOdds34,
                gaddbrushPrice1, gaddbrushPrice2, gaddbrushPrice34,
                gaddbrushShopOdds12, gaddbrushShopOdds34,
                warpBlockPrice1, warpBlockPrice2, warpBlockPrice34,
                warpBlockShopOdds12, warpBlockShopOdds34,
                flyGuyPrice1, flyGuyPrice2, flyGuyPrice34,
                flyGuyShopOdds12, flyGuyShopOdds34,
                plusBlockPrice1, plusBlockPrice2, plusBlockPrice34,
                plusBlockShopOdds12, plusBlockShopOdds34,
                minusBlockPrice1, minusBlockPrice2, minusBlockPrice34,
                minusBlockShopOdds12, minusBlockShopOdds34,
                speedBlockPrice1, speedBlockPrice2, speedBlockPrice34,
                speedBlockShopOdds12, speedBlockShopOdds34,
                slowBlockPrice1, slowBlockPrice2, slowBlockPrice34,
                slowBlockShopOdds12, slowBlockShopOdds34,
                bowserPhonePrice1, bowserPhonePrice2, bowserPhonePrice34,
                bowserPhoneShopOdds12, bowserPhoneShopOdds34,
                doubleDipPrice1, doubleDipPrice2, doubleDipPrice34,
                doubleDipShopOdds12, doubleDipShopOdds34,
                hiddenBlockCardPrice1, hiddenBlockCardPrice2, hiddenBlockCardPrice34,
                hiddenBlockCardShopOdds12, hiddenBlockCardShopOdds34,
                barterBoxPrice1, barterBoxPrice2, barterBoxPrice34,
                barterBoxShopOdds12, barterBoxShopOdds34,
                superWarpPipePrice1, superWarpPipePrice2, superWarpPipePrice34,
                superWarpPipeShopOdds12, superWarpPipeShopOdds34,
                chanceTimeCharmPrice1, chanceTimeCharmPrice2, chanceTimeCharmPrice34,
                chanceTimeCharmShopOdds12, chanceTimeCharmShopOdds34,
                wackyWatchPrice1, wackyWatchPrice2, wackyWatchPrice34,
                wackyWatchShopOdds12, wackyWatchShopOdds34),
        else:
            pass
    # Create the button with the command set to the new function
    parseButton = ctk.CTkButton(
        master=tabview.tab("Item Mods"),
        command=handle_button_command,
        text="Generate Code"
    )


    parseButton.place(x=10, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Item Mods"), command=lambda: savePresetItems4(
        miniMushroomPrice1, miniMushroomPrice2, miniMushroomPrice34,
        miniMushroomShopOdds12, miniMushroomShopOdds34,
        miniMushroomSpaceOdds1, miniMushroomSpaceOdds2, miniMushroomSpaceOdds34,
        megaMushroomPrice1, megaMushroomPrice2, megaMushroomPrice34,
        megaMushroomShopOdds12, megaMushroomShopOdds34,
        megaMushroomSpaceOdds1, megaMushroomSpaceOdds2, megaMushroomSpaceOdds34,
        superMiniMushroomPrice1, superMiniMushroomPrice2, superMiniMushroomPrice34,
        superMiniMushroomShopOdds12, superMiniMushroomShopOdds34,
        superMiniMushroomSpaceOdds1, superMiniMushroomSpaceOdds2, superMiniMushroomSpaceOdds34,
        superMegaMushroomPrice1, superMegaMushroomPrice2, superMegaMushroomPrice34,
        superMegaMushroomShopOdds12, superMegaMushroomShopOdds34,
        superMegaMushroomSpaceOdds1, superMegaMushroomSpaceOdds2, superMiniMushroomSpaceOdds34,
        miniMegaHammerPrice1, miniMegaHammerPrice2, miniMegaHammerPrice34,
        miniMegaHammerShopOdds12, miniMegaHammerShopOdds34,
        miniMegaHammerSpaceOdds1, miniMegaHammerSpaceOdds2, miniMegaHammerSpaceOdds34,
        warpPipePrice1, warpPipePrice2, warpPipePrice34,
        warpPipeShopOdds12, warpPipeShopOdds34,
        warpPipeSpaceOdds1, warpPipeSpaceOdds2, warpPipeSpaceOdds34,
        swapCardPrice1, swapCardPrice2, swapCardPrice34,
        swapCardShopOdds12, swapCardShopOdds34,
        swapCardSpaceOdds1, swapCardSpaceOdds2, swapCardSpaceOdds34,
        sparkyStickerPrice1, sparkyStickerPrice2, sparkyStickerPrice34,
        sparkyStickerShopOdds12, sparkyStickerShopOdds34,
        sparkyStickerSpaceOdds1, sparkyStickerSpaceOdds2, sparkyStickerSpaceOdds34,
        gaddlightPrice1, gaddlightPrice2, gaddlightPrice34,
        gaddlightShopOdds12, gaddlightShopOdds34,
        gaddlightSpaceOdds1, gaddlightSpaceOdds2, gaddlightSpaceOdds34,
        chompCallPrice1, chompCallPrice2, chompCallPrice34,
        chompCallShopOdds12, chompCallShopOdds34,
        chompCallSpaceOdds1, chompCallSpaceOdds2, chompCallSpaceOdds34,
        bowserSuitPrice1, bowserSuitPrice2, bowserSuitPrice34,
        bowserSuitShopOdds12, bowserSuitShopOdds34,
        bowserSuitSpaceOdds1, bowserSuitSpaceOdds2, bowserSuitSpaceOdds34,
        crystalBallPrice1, crystalBallPrice2, crystalBallPrice34,
        crystalBallShopOdds12, crystalBallShopOdds34,
        crystalBallSpaceOdds1, crystalBallSpaceOdds2, crystalBallSpaceOdds34,
        magicLampPrice1, magicLampPrice2, magicLampPrice34,
        magicLampShopOdds12, magicLampShopOdds34,
        magicLampSpaceOdds1, magicLampSpaceOdds2, magicLampSpaceOdds34,
        itemBagPrice1, itemBagPrice2, itemBagPrice34,
        itemBagShopOdds12, itemBagShopOdds34,
        itemBagSpaceOdds1, itemBagSpaceOdds2, itemBagSpaceOdds34,
        mushroomPrice1 if hide_custom == False else "0", mushroomPrice2 if hide_custom == False else "0", mushroomPrice34 if hide_custom == False else "0",
        mushroomShopOdds12 if hide_custom == False else "0", mushroomShopOdds34 if hide_custom == False else "0",
        mushroomSpaceOdds1 if hide_custom == False else "0", mushroomSpaceOdds2 if hide_custom == False else "0", mushroomSpaceOdds34 if hide_custom == False else "0",
        goldenMushroomPrice1 if hide_custom == False else "0", goldenMushroomPrice2 if hide_custom == False else "0", goldenMushroomPrice34 if hide_custom == False else "0",
        goldenMushroomShopOdds12 if hide_custom == False else "0", goldenMushroomShopOdds34 if hide_custom == False else "0",
        goldenMushroomSpaceOdds1 if hide_custom == False else "0", goldenMushroomSpaceOdds2 if hide_custom == False else "0", goldenMushroomSpaceOdds34 if hide_custom == False else "0",
        reverseMushroomPrice1 if hide_custom == False else "0", reverseMushroomPrice2 if hide_custom == False else "0", reverseMushroomPrice34 if hide_custom == False else "0",
        reverseMushroomShopOdds12 if hide_custom == False else "0", reverseMushroomShopOdds34 if hide_custom == False else "0",
        reverseMushroomSpaceOdds1 if hide_custom == False else "0", reverseMushroomSpaceOdds2 if hide_custom == False else "0", reverseMushroomSpaceOdds34 if hide_custom == False else "0",
        poisonMushroomPrice1 if hide_custom == False else "0", poisonMushroomPrice2 if hide_custom == False else "0", poisonMushroomPrice34 if hide_custom == False else "0",
        poisonMushroomShopOdds12 if hide_custom == False else "0", poisonMushroomShopOdds34 if hide_custom == False else "0",
        poisonMushroomSpaceOdds1 if hide_custom == False else "0", poisonMushroomSpaceOdds2 if hide_custom == False else "0", poisonMushroomSpaceOdds34 if hide_custom == False else "0",
        triplePoisonMushroomPrice1 if hide_custom == False else "0", triplePoisonMushroomPrice2 if hide_custom == False else "0", triplePoisonMushroomPrice34 if hide_custom == False else "0",
        triplePoisonMushroomShopOdds12 if hide_custom == False else "0", triplePoisonMushroomShopOdds34 if hide_custom == False else "0",
        triplePoisonMushroomSpaceOdds1 if hide_custom == False else "0", triplePoisonMushroomSpaceOdds2 if hide_custom == False else "0", triplePoisonMushroomSpaceOdds34 if hide_custom == False else "0",
        celluarShopperPrice1 if hide_custom == False else "0", celluarShopperPrice2 if hide_custom == False else "0", celluarShopperPrice34 if hide_custom == False else "0",
        celluarShopperShopOdds12 if hide_custom == False else "0", celluarShopperShopOdds34 if hide_custom == False else "0",
        celluarShopperSpaceOdds1 if hide_custom == False else "0", celluarShopperSpaceOdds2 if hide_custom == False else "0", celluarShopperSpaceOdds34 if hide_custom == False else "0",
        skeletonKeyPrice1 if hide_custom == False else "0", skeletonKeyPrice2 if hide_custom == False else "0", skeletonKeyPrice34 if hide_custom == False else "0",
        skeletonKeyShopOdds12 if hide_custom == False else "0", skeletonKeyShopOdds34 if hide_custom == False else "0",
        skeletonKeySpaceOdds1 if hide_custom == False else "0", skeletonKeySpaceOdds2 if hide_custom == False else "0", skeletonKeySpaceOdds34 if hide_custom == False else "0",
        plunderChestPrice1 if hide_custom == False else "0", plunderChestPrice2 if hide_custom == False else "0", plunderChestPrice34 if hide_custom == False else "0",
        plunderChestShopOdds12 if hide_custom == False else "0", plunderChestShopOdds34 if hide_custom == False else "0",
        plunderChestSpaceOdds1 if hide_custom == False else "0", plunderChestSpaceOdds2 if hide_custom == False else "0", plunderChestSpaceOdds34 if hide_custom == False else "0",
        gaddlightPrice1 if hide_custom == False else "0", gaddlightPrice2 if hide_custom == False else "0", gaddlightPrice34 if hide_custom == False else "0",
        gaddlightShopOdds12 if hide_custom == False else "0", gaddlightShopOdds34 if hide_custom == False else "0",
        gaddlightSpaceOdds1 if hide_custom == False else "0", gaddlightSpaceOdds2 if hide_custom == False else "0", gaddlightSpaceOdds34 if hide_custom == False else "0",
        warpBlockPrice1 if hide_custom == False else "0", warpBlockPrice2 if hide_custom == False else "0", warpBlockPrice34 if hide_custom == False else "0",
        warpBlockShopOdds12 if hide_custom == False else "0", warpBlockShopOdds34 if hide_custom == False else "0",
        warpBlockSpaceOdds1 if hide_custom == False else "0", warpBlockSpaceOdds2 if hide_custom == False else "0", warpBlockSpaceOdds34 if hide_custom == False else "0",
        flyGuyPrice1 if hide_custom == False else "0", flyGuyPrice2 if hide_custom == False else "0", flyGuyPrice34 if hide_custom == False else "0",
        flyGuyShopOdds12 if hide_custom == False else "0", flyGuyShopOdds34 if hide_custom == False else "0",
        flyGuySpaceOdds1 if hide_custom == False else "0", flyGuySpaceOdds2 if hide_custom == False else "0", flyGuySpaceOdds34 if hide_custom == False else "0",
        plusBlockPrice1 if hide_custom == False else "0", plusBlockPrice2 if hide_custom == False else "0", plusBlockPrice34 if hide_custom == False else "0",
        plusBlockShopOdds12 if hide_custom == False else "0", plusBlockShopOdds34 if hide_custom == False else "0",
        plusBlockSpaceOdds1 if hide_custom == False else "0", plusBlockSpaceOdds2 if hide_custom == False else "0", plusBlockSpaceOdds34 if hide_custom == False else "0",
        minusBlockPrice1 if hide_custom == False else "0", minusBlockPrice2 if hide_custom == False else "0", minusBlockPrice34 if hide_custom == False else "0",
        minusBlockShopOdds12 if hide_custom == False else "0", minusBlockShopOdds34 if hide_custom == False else "0",
        minusBlockSpaceOdds1 if hide_custom == False else "0", minusBlockSpaceOdds2 if hide_custom == False else "0", minusBlockSpaceOdds34 if hide_custom == False else "0",
        speedBlockPrice1 if hide_custom == False else "0", speedBlockPrice2 if hide_custom == False else "0", speedBlockPrice34 if hide_custom == False else "0",
        speedBlockShopOdds12 if hide_custom == False else "0", speedBlockShopOdds34 if hide_custom == False else "0",
        speedBlockSpaceOdds1 if hide_custom == False else "0", speedBlockSpaceOdds2 if hide_custom == False else "0", speedBlockSpaceOdds34 if hide_custom == False else "0",
        slowBlockPrice1 if hide_custom == False else "0", slowBlockPrice2 if hide_custom == False else "0", slowBlockPrice34 if hide_custom == False else "0",
        slowBlockShopOdds12 if hide_custom == False else "0", slowBlockShopOdds34 if hide_custom == False else "0",
        slowBlockSpaceOdds1 if hide_custom == False else "0", slowBlockSpaceOdds2 if hide_custom == False else "0", slowBlockSpaceOdds34 if hide_custom == False else "0",
        bowserPhonePrice1 if hide_custom == False else "0", bowserPhonePrice2 if hide_custom == False else "0", bowserPhonePrice34 if hide_custom == False else "0",
        bowserPhoneShopOdds12 if hide_custom == False else "0", bowserPhoneShopOdds34 if hide_custom == False else "0",
        bowserPhoneSpaceOdds1 if hide_custom == False else "0", bowserPhoneSpaceOdds2 if hide_custom == False else "0", bowserPhoneSpaceOdds34 if hide_custom == False else "0",
        doubleDipPrice1 if hide_custom == False else "0", doubleDipPrice2 if hide_custom == False else "0", doubleDipPrice34 if hide_custom == False else "0",
        doubleDipShopOdds12 if hide_custom == False else "0", doubleDipShopOdds34 if hide_custom == False else "0",
        doubleDipSpaceOdds1 if hide_custom == False else "0", doubleDipSpaceOdds2 if hide_custom == False else "0", doubleDipSpaceOdds34 if hide_custom == False else "0",
        hiddenBlockCardPrice1 if hide_custom == False else "0", hiddenBlockCardPrice2 if hide_custom == False else "0", hiddenBlockCardPrice34 if hide_custom == False else "0",
        hiddenBlockCardShopOdds12 if hide_custom == False else "0", hiddenBlockCardShopOdds34 if hide_custom == False else "0",
        hiddenBlockCardSpaceOdds1 if hide_custom == False else "0", hiddenBlockCardSpaceOdds2 if hide_custom == False else "0", hiddenBlockCardSpaceOdds34 if hide_custom == False else "0",
        barterBoxPrice1 if hide_custom == False else "0", barterBoxPrice2 if hide_custom == False else "0", barterBoxPrice34 if hide_custom == False else "0",
        barterBoxShopOdds12 if hide_custom == False else "0", barterBoxShopOdds34 if hide_custom == False else "0",
        barterBoxSpaceOdds1 if hide_custom == False else "0", barterBoxSpaceOdds2 if hide_custom == False else "0", barterBoxSpaceOdds34 if hide_custom == False else "0",
        superWarpPipePrice1 if hide_custom == False else "0", superWarpPipePrice2 if hide_custom == False else "0", superWarpPipePrice34 if hide_custom == False else "0",
        superWarpPipeShopOdds12 if hide_custom == False else "0", superWarpPipeShopOdds34 if hide_custom == False else "0",
        superWarpPipeSpaceOdds1 if hide_custom == False else "0", superWarpPipeSpaceOdds2 if hide_custom == False else "0", superWarpPipeSpaceOdds34 if hide_custom == False else "0",
        chanceTimeCharmPrice1 if hide_custom == False else "0", chanceTimeCharmPrice2 if hide_custom == False else "0", chanceTimeCharmPrice34 if hide_custom == False else "0",
        chanceTimeCharmShopOdds12 if hide_custom == False else "0", chanceTimeCharmShopOdds34 if hide_custom == False else "0",
        chanceTimeCharmSpaceOdds1 if hide_custom == False else "0", chanceTimeCharmSpaceOdds2 if hide_custom == False else "0", chanceTimeCharmSpaceOdds34 if hide_custom == False else "0",
        wackyWatchPrice1 if hide_custom == False else "0", wackyWatchPrice2 if hide_custom == False else "0", wackyWatchPrice34 if hide_custom == False else "0",
        wackyWatchShopOdds12 if hide_custom == False else "0", wackyWatchShopOdds34 if hide_custom == False else "0",
        wackyWatchSpaceOdds1 if hide_custom == False else "0", wackyWatchSpaceOdds2 if hide_custom == False else "0", wackyWatchSpaceOdds34 if hide_custom == False else "0"), text="Save Preset")
    parseButton.place(x=160, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Item Mods"), command=lambda: loadPresetItems4(
        hide_custom,
        miniMushroomPrice1, miniMushroomPrice2, miniMushroomPrice34,
        miniMushroomShopOdds12, miniMushroomShopOdds34,
        miniMushroomSpaceOdds1, miniMushroomSpaceOdds2, miniMushroomSpaceOdds34,
        megaMushroomPrice1, megaMushroomPrice2, megaMushroomPrice34,
        megaMushroomShopOdds12, megaMushroomShopOdds34,
        megaMushroomSpaceOdds1, megaMushroomSpaceOdds2, megaMushroomSpaceOdds34,
        superMiniMushroomPrice1, superMiniMushroomPrice2, superMiniMushroomPrice34,
        superMiniMushroomShopOdds12, superMiniMushroomShopOdds34,
        superMiniMushroomSpaceOdds1, superMiniMushroomSpaceOdds2, superMiniMushroomSpaceOdds34,
        superMegaMushroomPrice1, superMegaMushroomPrice2, superMegaMushroomPrice34,
        superMegaMushroomShopOdds12, superMegaMushroomShopOdds34,
        superMegaMushroomSpaceOdds1, superMegaMushroomSpaceOdds2, superMiniMushroomSpaceOdds34,
        miniMegaHammerPrice1, miniMegaHammerPrice2, miniMegaHammerPrice34,
        miniMegaHammerShopOdds12, miniMegaHammerShopOdds34,
        miniMegaHammerSpaceOdds1, miniMegaHammerSpaceOdds2, miniMegaHammerSpaceOdds34,
        warpPipePrice1, warpPipePrice2, warpPipePrice34,
        warpPipeShopOdds12, warpPipeShopOdds34,
        warpPipeSpaceOdds1, warpPipeSpaceOdds2, warpPipeSpaceOdds34,
        swapCardPrice1, swapCardPrice2, swapCardPrice34,
        swapCardShopOdds12, swapCardShopOdds34,
        swapCardSpaceOdds1, swapCardSpaceOdds2, swapCardSpaceOdds34,
        sparkyStickerPrice1, sparkyStickerPrice2, sparkyStickerPrice34,
        sparkyStickerShopOdds12, sparkyStickerShopOdds34,
        sparkyStickerSpaceOdds1, sparkyStickerSpaceOdds2, sparkyStickerSpaceOdds34,
        gaddlightPrice1, gaddlightPrice2, gaddlightPrice34,
        gaddlightShopOdds12, gaddlightShopOdds34,
        gaddlightSpaceOdds1, gaddlightSpaceOdds2, gaddlightSpaceOdds34,
        chompCallPrice1, chompCallPrice2, chompCallPrice34,
        chompCallShopOdds12, chompCallShopOdds34,
        chompCallSpaceOdds1, chompCallSpaceOdds2, chompCallSpaceOdds34,
        bowserSuitPrice1, bowserSuitPrice2, bowserSuitPrice34,
        bowserSuitShopOdds12, bowserSuitShopOdds34,
        bowserSuitSpaceOdds1, bowserSuitSpaceOdds2, bowserSuitSpaceOdds34,
        crystalBallPrice1, crystalBallPrice2, crystalBallPrice34,
        crystalBallShopOdds12, crystalBallShopOdds34,
        crystalBallSpaceOdds1, crystalBallSpaceOdds2, crystalBallSpaceOdds34,
        magicLampPrice1, magicLampPrice2, magicLampPrice34,
        magicLampShopOdds12, magicLampShopOdds34,
        magicLampSpaceOdds1, magicLampSpaceOdds2, magicLampSpaceOdds34,
        itemBagPrice1, itemBagPrice2, itemBagPrice34,
        itemBagShopOdds12, itemBagShopOdds34,
        itemBagSpaceOdds1, itemBagSpaceOdds2, itemBagSpaceOdds34,
        mushroomPrice1 if hide_custom == False else "0", mushroomPrice2 if hide_custom == False else "0", mushroomPrice34 if hide_custom == False else "0",
        mushroomShopOdds12 if hide_custom == False else "0", mushroomShopOdds34 if hide_custom == False else "0",
        mushroomSpaceOdds1 if hide_custom == False else "0", mushroomSpaceOdds2 if hide_custom == False else "0", mushroomSpaceOdds34 if hide_custom == False else "0",
        goldenMushroomPrice1 if hide_custom == False else "0", goldenMushroomPrice2 if hide_custom == False else "0", goldenMushroomPrice34 if hide_custom == False else "0",
        goldenMushroomShopOdds12 if hide_custom == False else "0", goldenMushroomShopOdds34 if hide_custom == False else "0",
        goldenMushroomSpaceOdds1 if hide_custom == False else "0", goldenMushroomSpaceOdds2 if hide_custom == False else "0", goldenMushroomSpaceOdds34 if hide_custom == False else "0",
        reverseMushroomPrice1 if hide_custom == False else "0", reverseMushroomPrice2 if hide_custom == False else "0", reverseMushroomPrice34 if hide_custom == False else "0",
        reverseMushroomShopOdds12 if hide_custom == False else "0", reverseMushroomShopOdds34 if hide_custom == False else "0",
        reverseMushroomSpaceOdds1 if hide_custom == False else "0", reverseMushroomSpaceOdds2 if hide_custom == False else "0", reverseMushroomSpaceOdds34 if hide_custom == False else "0",
        poisonMushroomPrice1 if hide_custom == False else "0", poisonMushroomPrice2 if hide_custom == False else "0", poisonMushroomPrice34 if hide_custom == False else "0",
        poisonMushroomShopOdds12 if hide_custom == False else "0", poisonMushroomShopOdds34 if hide_custom == False else "0",
        poisonMushroomSpaceOdds1 if hide_custom == False else "0", poisonMushroomSpaceOdds2 if hide_custom == False else "0", poisonMushroomSpaceOdds34 if hide_custom == False else "0",
        triplePoisonMushroomPrice1 if hide_custom == False else "0", triplePoisonMushroomPrice2 if hide_custom == False else "0", triplePoisonMushroomPrice34 if hide_custom == False else "0",
        triplePoisonMushroomShopOdds12 if hide_custom == False else "0", triplePoisonMushroomShopOdds34 if hide_custom == False else "0",
        triplePoisonMushroomSpaceOdds1 if hide_custom == False else "0", triplePoisonMushroomSpaceOdds2 if hide_custom == False else "0", triplePoisonMushroomSpaceOdds34 if hide_custom == False else "0",
        celluarShopperPrice1 if hide_custom == False else "0", celluarShopperPrice2 if hide_custom == False else "0", celluarShopperPrice34 if hide_custom == False else "0",
        celluarShopperShopOdds12 if hide_custom == False else "0", celluarShopperShopOdds34 if hide_custom == False else "0",
        celluarShopperSpaceOdds1 if hide_custom == False else "0", celluarShopperSpaceOdds2 if hide_custom == False else "0", celluarShopperSpaceOdds34 if hide_custom == False else "0",
        skeletonKeyPrice1 if hide_custom == False else "0", skeletonKeyPrice2 if hide_custom == False else "0", skeletonKeyPrice34 if hide_custom == False else "0",
        skeletonKeyShopOdds12 if hide_custom == False else "0", skeletonKeyShopOdds34 if hide_custom == False else "0",
        skeletonKeySpaceOdds1 if hide_custom == False else "0", skeletonKeySpaceOdds2 if hide_custom == False else "0", skeletonKeySpaceOdds34 if hide_custom == False else "0",
        plunderChestPrice1 if hide_custom == False else "0", plunderChestPrice2 if hide_custom == False else "0", plunderChestPrice34 if hide_custom == False else "0",
        plunderChestShopOdds12 if hide_custom == False else "0", plunderChestShopOdds34 if hide_custom == False else "0",
        plunderChestSpaceOdds1 if hide_custom == False else "0", plunderChestSpaceOdds2 if hide_custom == False else "0", plunderChestSpaceOdds34 if hide_custom == False else "0",
        gaddlightPrice1 if hide_custom == False else "0", gaddlightPrice2 if hide_custom == False else "0", gaddlightPrice34 if hide_custom == False else "0",
        gaddlightShopOdds12 if hide_custom == False else "0", gaddlightShopOdds34 if hide_custom == False else "0",
        gaddlightSpaceOdds1 if hide_custom == False else "0", gaddlightSpaceOdds2 if hide_custom == False else "0", gaddlightSpaceOdds34 if hide_custom == False else "0",
        warpBlockPrice1 if hide_custom == False else "0", warpBlockPrice2 if hide_custom == False else "0", warpBlockPrice34 if hide_custom == False else "0",
        warpBlockShopOdds12 if hide_custom == False else "0", warpBlockShopOdds34 if hide_custom == False else "0",
        warpBlockSpaceOdds1 if hide_custom == False else "0", warpBlockSpaceOdds2 if hide_custom == False else "0", warpBlockSpaceOdds34 if hide_custom == False else "0",
        flyGuyPrice1 if hide_custom == False else "0", flyGuyPrice2 if hide_custom == False else "0", flyGuyPrice34 if hide_custom == False else "0",
        flyGuyShopOdds12 if hide_custom == False else "0", flyGuyShopOdds34 if hide_custom == False else "0",
        flyGuySpaceOdds1 if hide_custom == False else "0", flyGuySpaceOdds2 if hide_custom == False else "0", flyGuySpaceOdds34 if hide_custom == False else "0",
        plusBlockPrice1 if hide_custom == False else "0", plusBlockPrice2 if hide_custom == False else "0", plusBlockPrice34 if hide_custom == False else "0",
        plusBlockShopOdds12 if hide_custom == False else "0", plusBlockShopOdds34 if hide_custom == False else "0",
        plusBlockSpaceOdds1 if hide_custom == False else "0", plusBlockSpaceOdds2 if hide_custom == False else "0", plusBlockSpaceOdds34 if hide_custom == False else "0",
        minusBlockPrice1 if hide_custom == False else "0", minusBlockPrice2 if hide_custom == False else "0", minusBlockPrice34 if hide_custom == False else "0",
        minusBlockShopOdds12 if hide_custom == False else "0", minusBlockShopOdds34 if hide_custom == False else "0",
        minusBlockSpaceOdds1 if hide_custom == False else "0", minusBlockSpaceOdds2 if hide_custom == False else "0", minusBlockSpaceOdds34 if hide_custom == False else "0",
        speedBlockPrice1 if hide_custom == False else "0", speedBlockPrice2 if hide_custom == False else "0", speedBlockPrice34 if hide_custom == False else "0",
        speedBlockShopOdds12 if hide_custom == False else "0", speedBlockShopOdds34 if hide_custom == False else "0",
        speedBlockSpaceOdds1 if hide_custom == False else "0", speedBlockSpaceOdds2 if hide_custom == False else "0", speedBlockSpaceOdds34 if hide_custom == False else "0",
        slowBlockPrice1 if hide_custom == False else "0", slowBlockPrice2 if hide_custom == False else "0", slowBlockPrice34 if hide_custom == False else "0",
        slowBlockShopOdds12 if hide_custom == False else "0", slowBlockShopOdds34 if hide_custom == False else "0",
        slowBlockSpaceOdds1 if hide_custom == False else "0", slowBlockSpaceOdds2 if hide_custom == False else "0", slowBlockSpaceOdds34 if hide_custom == False else "0",
        bowserPhonePrice1 if hide_custom == False else "0", bowserPhonePrice2 if hide_custom == False else "0", bowserPhonePrice34 if hide_custom == False else "0",
        bowserPhoneShopOdds12 if hide_custom == False else "0", bowserPhoneShopOdds34 if hide_custom == False else "0",
        bowserPhoneSpaceOdds1 if hide_custom == False else "0", bowserPhoneSpaceOdds2 if hide_custom == False else "0", bowserPhoneSpaceOdds34 if hide_custom == False else "0",
        doubleDipPrice1 if hide_custom == False else "0", doubleDipPrice2 if hide_custom == False else "0", doubleDipPrice34 if hide_custom == False else "0",
        doubleDipShopOdds12 if hide_custom == False else "0", doubleDipShopOdds34 if hide_custom == False else "0",
        doubleDipSpaceOdds1 if hide_custom == False else "0", doubleDipSpaceOdds2 if hide_custom == False else "0", doubleDipSpaceOdds34 if hide_custom == False else "0",
        hiddenBlockCardPrice1 if hide_custom == False else "0", hiddenBlockCardPrice2 if hide_custom == False else "0", hiddenBlockCardPrice34 if hide_custom == False else "0",
        hiddenBlockCardShopOdds12 if hide_custom == False else "0", hiddenBlockCardShopOdds34 if hide_custom == False else "0",
        hiddenBlockCardSpaceOdds1 if hide_custom == False else "0", hiddenBlockCardSpaceOdds2 if hide_custom == False else "0", hiddenBlockCardSpaceOdds34 if hide_custom == False else "0",
        barterBoxPrice1 if hide_custom == False else "0", barterBoxPrice2 if hide_custom == False else "0", barterBoxPrice34 if hide_custom == False else "0",
        barterBoxShopOdds12 if hide_custom == False else "0", barterBoxShopOdds34 if hide_custom == False else "0",
        barterBoxSpaceOdds1 if hide_custom == False else "0", barterBoxSpaceOdds2 if hide_custom == False else "0", barterBoxSpaceOdds34 if hide_custom == False else "0",
        superWarpPipePrice1 if hide_custom == False else "0", superWarpPipePrice2 if hide_custom == False else "0", superWarpPipePrice34 if hide_custom == False else "0",
        superWarpPipeShopOdds12 if hide_custom == False else "0", superWarpPipeShopOdds34 if hide_custom == False else "0",
        superWarpPipeSpaceOdds1 if hide_custom == False else "0", superWarpPipeSpaceOdds2 if hide_custom == False else "0", superWarpPipeSpaceOdds34 if hide_custom == False else "0",
        chanceTimeCharmPrice1 if hide_custom == False else "0", chanceTimeCharmPrice2 if hide_custom == False else "0", chanceTimeCharmPrice34 if hide_custom == False else "0",
        chanceTimeCharmShopOdds12 if hide_custom == False else "0", chanceTimeCharmShopOdds34 if hide_custom == False else "0",
        chanceTimeCharmSpaceOdds1 if hide_custom == False else "0", chanceTimeCharmSpaceOdds2 if hide_custom == False else "0", chanceTimeCharmSpaceOdds34 if hide_custom == False else "0",
        wackyWatchPrice1 if hide_custom == False else "0", wackyWatchPrice2 if hide_custom == False else "0", wackyWatchPrice34 if hide_custom == False else "0",
        wackyWatchShopOdds12 if hide_custom == False else "0", wackyWatchShopOdds34 if hide_custom == False else "0",
        wackyWatchSpaceOdds1 if hide_custom == False else "0", wackyWatchSpaceOdds2 if hide_custom == False else "0", wackyWatchSpaceOdds34 if hide_custom == False else "0"), text="Load Preset")
    parseButton.place(x=310, y=800)

    hideCustomSwitch = ctk.CTkSwitch(master=tabview.tab("Item Mods"), text="Show DX Items")
    hideCustomSwitch.place(x=460, y=800) # x=610

    hideSpaceSwitch = ctk.CTkSwitch(master=tabview.tab("Item Mods"), text="Modify Item Space")
    hideSpaceSwitch.place(x=610, y=800)


    def toggle_hide_itemSpace():
        global hide_itemSpace
        hide_itemSpace = not hide_itemSpace

    def toggle_hide_custom():
        global hide_custom
        hide_custom = not hide_custom

        if hide_custom:
            mushroomPrice1.grid_forget()
            mushroomPrice2.grid_forget()
            mushroomPrice34.grid_forget()
            mushroomShopOdds12.grid_forget()
            mushroomShopOdds34.grid_forget()
            mushroomSpaceOdds1.grid_forget()
            mushroomSpaceOdds2.grid_forget()
            mushroomSpaceOdds34.grid_forget()
            labelMushroom1.grid_forget()
            labelMushroom2.grid_forget()
            labelMushroom3.grid_forget()
            labelMushroom4.grid_forget()
            labelMushroom5.grid_forget()
            labelMushroom6.grid_forget()
            labelMushroom7.grid_forget()
            labelMushroom8.grid_forget()

            bowserPhonePrice1.grid_forget()
            bowserPhonePrice2.grid_forget()
            bowserPhonePrice34.grid_forget()
            bowserPhoneShopOdds12.grid_forget()
            bowserPhoneShopOdds34.grid_forget()
            bowserPhoneSpaceOdds1.grid_forget()
            bowserPhoneSpaceOdds2.grid_forget()
            bowserPhoneSpaceOdds34.grid_forget()
            labelBowserPhone1.grid_forget()
            labelBowserPhone2.grid_forget()
            labelBowserPhone3.grid_forget()
            labelBowserPhone4.grid_forget()
            labelBowserPhone5.grid_forget()
            labelBowserPhone6.grid_forget()
            labelBowserPhone7.grid_forget()
            labelBowserPhone8.grid_forget()

            goldenMushroomPrice1.grid_forget()
            goldenMushroomPrice2.grid_forget()
            goldenMushroomPrice34.grid_forget()
            goldenMushroomShopOdds12.grid_forget()
            goldenMushroomShopOdds34.grid_forget()
            goldenMushroomSpaceOdds1.grid_forget()
            goldenMushroomSpaceOdds2.grid_forget()
            goldenMushroomSpaceOdds34.grid_forget()
            labelGoldenMushroom1.grid_forget()
            labelGoldenMushroom2.grid_forget()
            labelGoldenMushroom3.grid_forget()
            labelGoldenMushroom4.grid_forget()
            labelGoldenMushroom5.grid_forget()
            labelGoldenMushroom6.grid_forget()
            labelGoldenMushroom7.grid_forget()
            labelGoldenMushroom8.grid_forget()

            hiddenBlockCardPrice1.grid_forget()
            hiddenBlockCardPrice2.grid_forget()
            hiddenBlockCardPrice34.grid_forget()
            hiddenBlockCardShopOdds12.grid_forget()
            hiddenBlockCardShopOdds34.grid_forget()
            hiddenBlockCardSpaceOdds1.grid_forget()
            hiddenBlockCardSpaceOdds2.grid_forget()
            hiddenBlockCardSpaceOdds34.grid_forget()
            labelHiddenBlockCard1.grid_forget()
            labelHiddenBlockCard2.grid_forget()
            labelHiddenBlockCard3.grid_forget()
            labelHiddenBlockCard4.grid_forget()
            labelHiddenBlockCard5.grid_forget()
            labelHiddenBlockCard6.grid_forget()
            labelHiddenBlockCard7.grid_forget()
            labelHiddenBlockCard8.grid_forget()

            celluarShopperPrice1.grid_forget()
            celluarShopperPrice2.grid_forget()
            celluarShopperPrice34.grid_forget()
            celluarShopperShopOdds12.grid_forget()
            celluarShopperShopOdds34.grid_forget()
            celluarShopperSpaceOdds1.grid_forget()
            celluarShopperSpaceOdds2.grid_forget()
            celluarShopperSpaceOdds34.grid_forget()
            labelCelluarShopper1.grid_forget()
            labelCelluarShopper2.grid_forget()
            labelCelluarShopper3.grid_forget()
            labelCelluarShopper4.grid_forget()
            labelCelluarShopper5.grid_forget()
            labelCelluarShopper6.grid_forget()
            labelCelluarShopper7.grid_forget()
            labelCelluarShopper8.grid_forget()

            barterBoxPrice1.grid_forget()
            barterBoxPrice2.grid_forget()
            barterBoxPrice34.grid_forget()
            barterBoxShopOdds12.grid_forget()
            barterBoxShopOdds34.grid_forget()
            barterBoxSpaceOdds1.grid_forget()
            barterBoxSpaceOdds2.grid_forget()
            barterBoxSpaceOdds34.grid_forget()
            labelBarterBox1.grid_forget()
            labelBarterBox2.grid_forget()
            labelBarterBox3.grid_forget()
            labelBarterBox4.grid_forget()
            labelBarterBox5.grid_forget()
            labelBarterBox6.grid_forget()
            labelBarterBox7.grid_forget()
            labelBarterBox8.grid_forget()

            superWarpPipePrice1.grid_forget()
            superWarpPipePrice2.grid_forget()
            superWarpPipePrice34.grid_forget()
            superWarpPipeShopOdds12.grid_forget()
            superWarpPipeShopOdds34.grid_forget()
            superWarpPipeSpaceOdds1.grid_forget()
            superWarpPipeSpaceOdds2.grid_forget()
            superWarpPipeSpaceOdds34.grid_forget()
            labelSuperWarpPipe1.grid_forget()
            labelSuperWarpPipe2.grid_forget()
            labelSuperWarpPipe3.grid_forget()
            labelSuperWarpPipe4.grid_forget()
            labelSuperWarpPipe5.grid_forget()
            labelSuperWarpPipe6.grid_forget()
            labelSuperWarpPipe7.grid_forget()
            labelSuperWarpPipe8.grid_forget()

            chanceTimeCharmPrice1.grid_forget()
            chanceTimeCharmPrice2.grid_forget()
            chanceTimeCharmPrice34.grid_forget()
            chanceTimeCharmShopOdds12.grid_forget()
            chanceTimeCharmShopOdds34.grid_forget()
            chanceTimeCharmSpaceOdds1.grid_forget()
            chanceTimeCharmSpaceOdds2.grid_forget()
            chanceTimeCharmSpaceOdds34.grid_forget()
            labelChanceTimeCharm1.grid_forget()
            labelChanceTimeCharm2.grid_forget()
            labelChanceTimeCharm3.grid_forget()
            labelChanceTimeCharm4.grid_forget()
            labelChanceTimeCharm5.grid_forget()
            labelChanceTimeCharm6.grid_forget()
            labelChanceTimeCharm7.grid_forget()
            labelChanceTimeCharm8.grid_forget()

            wackyWatchPrice1.grid_forget()
            wackyWatchPrice2.grid_forget()
            wackyWatchPrice34.grid_forget()
            wackyWatchShopOdds12.grid_forget()
            wackyWatchShopOdds34.grid_forget()
            wackyWatchSpaceOdds1.grid_forget()
            wackyWatchSpaceOdds2.grid_forget()
            wackyWatchSpaceOdds34.grid_forget()
            labelWackyWatch1.grid_forget()
            labelWackyWatch2.grid_forget()
            labelWackyWatch3.grid_forget()
            labelWackyWatch4.grid_forget()
            labelWackyWatch5.grid_forget()
            labelWackyWatch6.grid_forget()
            labelWackyWatch7.grid_forget()
            labelWackyWatch8.grid_forget()

            plunderChestPrice1.grid_forget()
            plunderChestPrice2.grid_forget()
            plunderChestPrice34.grid_forget()
            plunderChestShopOdds12.grid_forget()
            plunderChestShopOdds34.grid_forget()
            plunderChestSpaceOdds1.grid_forget()
            plunderChestSpaceOdds2.grid_forget()
            plunderChestSpaceOdds34.grid_forget()
            labelPlunderChest1.grid_forget()
            labelPlunderChest2.grid_forget()
            labelPlunderChest3.grid_forget()
            labelPlunderChest4.grid_forget()
            labelPlunderChest5.grid_forget()
            labelPlunderChest6.grid_forget()
            labelPlunderChest7.grid_forget()
            labelPlunderChest8.grid_forget()

            gaddbrushPrice1.grid_forget()
            gaddbrushPrice2.grid_forget()
            gaddbrushPrice34.grid_forget()
            gaddbrushShopOdds12.grid_forget()
            gaddbrushShopOdds34.grid_forget()
            gaddbrushSpaceOdds1.grid_forget()
            gaddbrushSpaceOdds2.grid_forget()
            gaddbrushSpaceOdds34.grid_forget()
            labelGaddbrush1.grid_forget()
            labelGaddbrush2.grid_forget()
            labelGaddbrush3.grid_forget()
            labelGaddbrush4.grid_forget()
            labelGaddbrush5.grid_forget()
            labelGaddbrush6.grid_forget()
            labelGaddbrush7.grid_forget()
            labelGaddbrush8.grid_forget()

            skeletonKeyPrice1.grid_forget()
            skeletonKeyPrice2.grid_forget()
            skeletonKeyPrice34.grid_forget()
            skeletonKeyShopOdds12.grid_forget()
            skeletonKeyShopOdds34.grid_forget()
            skeletonKeySpaceOdds1.grid_forget()
            skeletonKeySpaceOdds2.grid_forget()
            skeletonKeySpaceOdds34.grid_forget()
            labelSkeletonKey1.grid_forget()
            labelSkeletonKey2.grid_forget()
            labelSkeletonKey3.grid_forget()
            labelSkeletonKey4.grid_forget()
            labelSkeletonKey5.grid_forget()
            labelSkeletonKey6.grid_forget()
            labelSkeletonKey7.grid_forget()
            labelSkeletonKey8.grid_forget()

            warpBlockPrice1.grid_forget()
            warpBlockPrice2.grid_forget()
            warpBlockPrice34.grid_forget()
            warpBlockShopOdds12.grid_forget()
            warpBlockShopOdds34.grid_forget()
            warpBlockSpaceOdds1.grid_forget()
            warpBlockSpaceOdds2.grid_forget()
            warpBlockSpaceOdds34.grid_forget()
            labelWarpBlock1.grid_forget()
            labelWarpBlock2.grid_forget()
            labelWarpBlock3.grid_forget()
            labelWarpBlock4.grid_forget()
            labelWarpBlock5.grid_forget()
            labelWarpBlock6.grid_forget()
            labelWarpBlock7.grid_forget()
            labelWarpBlock8.grid_forget()

            flyGuyPrice1.grid_forget()
            flyGuyPrice2.grid_forget()
            flyGuyPrice34.grid_forget()
            flyGuyShopOdds12.grid_forget()
            flyGuyShopOdds34.grid_forget()
            flyGuySpaceOdds1.grid_forget()
            flyGuySpaceOdds2.grid_forget()
            flyGuySpaceOdds34.grid_forget()
            labelFlyGuy1.grid_forget()
            labelFlyGuy2.grid_forget()
            labelFlyGuy3.grid_forget()
            labelFlyGuy4.grid_forget()
            labelFlyGuy5.grid_forget()
            labelFlyGuy6.grid_forget()
            labelFlyGuy7.grid_forget()
            labelFlyGuy8.grid_forget()

            plusBlockPrice1.grid_forget()
            plusBlockPrice2.grid_forget()
            plusBlockPrice34.grid_forget()
            plusBlockShopOdds12.grid_forget()
            plusBlockShopOdds34.grid_forget()
            plusBlockSpaceOdds1.grid_forget()
            plusBlockSpaceOdds2.grid_forget()
            plusBlockSpaceOdds34.grid_forget()
            labelPlusBlock1.grid_forget()
            labelPlusBlock2.grid_forget()
            labelPlusBlock3.grid_forget()
            labelPlusBlock4.grid_forget()
            labelPlusBlock5.grid_forget()
            labelPlusBlock6.grid_forget()
            labelPlusBlock7.grid_forget()
            labelPlusBlock8.grid_forget()

            minusBlockPrice1.grid_forget()
            minusBlockPrice2.grid_forget()
            minusBlockPrice34.grid_forget()
            minusBlockShopOdds12.grid_forget()
            minusBlockShopOdds34.grid_forget()
            minusBlockSpaceOdds1.grid_forget()
            minusBlockSpaceOdds2.grid_forget()
            minusBlockSpaceOdds34.grid_forget()
            labelMinusBlock1.grid_forget()
            labelMinusBlock2.grid_forget()
            labelMinusBlock3.grid_forget()
            labelMinusBlock4.grid_forget()
            labelMinusBlock5.grid_forget()
            labelMinusBlock6.grid_forget()
            labelMinusBlock7.grid_forget()
            labelMinusBlock8.grid_forget()

            speedBlockPrice1.grid_forget()
            speedBlockPrice2.grid_forget()
            speedBlockPrice34.grid_forget()
            speedBlockShopOdds12.grid_forget()
            speedBlockShopOdds34.grid_forget()
            speedBlockSpaceOdds1.grid_forget()
            speedBlockSpaceOdds2.grid_forget()
            speedBlockSpaceOdds34.grid_forget()
            labelSpeedBlock1.grid_forget()
            labelSpeedBlock2.grid_forget()
            labelSpeedBlock3.grid_forget()
            labelSpeedBlock4.grid_forget()
            labelSpeedBlock5.grid_forget()
            labelSpeedBlock6.grid_forget()
            labelSpeedBlock7.grid_forget()
            labelSpeedBlock8.grid_forget()

            slowBlockPrice1.grid_forget()
            slowBlockPrice2.grid_forget()
            slowBlockPrice34.grid_forget()
            slowBlockShopOdds12.grid_forget()
            slowBlockShopOdds34.grid_forget()
            slowBlockSpaceOdds1.grid_forget()
            slowBlockSpaceOdds2.grid_forget()
            slowBlockSpaceOdds34.grid_forget()
            labelSlowBlock1.grid_forget()
            labelSlowBlock2.grid_forget()
            labelSlowBlock3.grid_forget()
            labelSlowBlock4.grid_forget()
            labelSlowBlock5.grid_forget()
            labelSlowBlock6.grid_forget()
            labelSlowBlock7.grid_forget()
            labelSlowBlock8.grid_forget()

            poisonMushroomPrice1.grid_forget()
            poisonMushroomPrice2.grid_forget()
            poisonMushroomPrice34.grid_forget()
            poisonMushroomShopOdds12.grid_forget()
            poisonMushroomShopOdds34.grid_forget()
            poisonMushroomSpaceOdds1.grid_forget()
            poisonMushroomSpaceOdds2.grid_forget()
            poisonMushroomSpaceOdds34.grid_forget()
            labelPoisonMushroom1.grid_forget()
            labelPoisonMushroom2.grid_forget()
            labelPoisonMushroom3.grid_forget()
            labelPoisonMushroom4.grid_forget()
            labelPoisonMushroom5.grid_forget()
            labelPoisonMushroom6.grid_forget()
            labelPoisonMushroom7.grid_forget()
            labelPoisonMushroom8.grid_forget()

            triplePoisonMushroomPrice1.grid_forget()
            triplePoisonMushroomPrice2.grid_forget()
            triplePoisonMushroomPrice34.grid_forget()
            triplePoisonMushroomShopOdds12.grid_forget()
            triplePoisonMushroomShopOdds34.grid_forget()
            triplePoisonMushroomSpaceOdds1.grid_forget()
            triplePoisonMushroomSpaceOdds2.grid_forget()
            triplePoisonMushroomSpaceOdds34.grid_forget()
            labelTriplePoisonMushroom1.grid_forget()
            labelTriplePoisonMushroom2.grid_forget()
            labelTriplePoisonMushroom3.grid_forget()
            labelTriplePoisonMushroom4.grid_forget()
            labelTriplePoisonMushroom5.grid_forget()
            labelTriplePoisonMushroom6.grid_forget()
            labelTriplePoisonMushroom7.grid_forget()
            labelTriplePoisonMushroom8.grid_forget()

            doubleDipPrice1.grid_forget()
            doubleDipPrice2.grid_forget()
            doubleDipPrice34.grid_forget()
            doubleDipShopOdds12.grid_forget()
            doubleDipShopOdds34.grid_forget()
            doubleDipSpaceOdds1.grid_forget()
            doubleDipSpaceOdds2.grid_forget()
            doubleDipSpaceOdds34.grid_forget()
            labelDoubleDip1.grid_forget()
            labelDoubleDip2.grid_forget()
            labelDoubleDip3.grid_forget()
            labelDoubleDip4.grid_forget()
            labelDoubleDip5.grid_forget()
            labelDoubleDip6.grid_forget()
            labelDoubleDip7.grid_forget()
            labelDoubleDip8.grid_forget()

            reverseMushroomPrice1.grid_forget()
            reverseMushroomPrice2.grid_forget()
            reverseMushroomPrice34.grid_forget()
            reverseMushroomShopOdds12.grid_forget()
            reverseMushroomShopOdds34.grid_forget()
            reverseMushroomSpaceOdds1.grid_forget()
            reverseMushroomSpaceOdds2.grid_forget()
            reverseMushroomSpaceOdds34.grid_forget()
            labelReverseMushroom1.grid_forget()
            labelReverseMushroom2.grid_forget()
            labelReverseMushroom3.grid_forget()
            labelReverseMushroom4.grid_forget()
            labelReverseMushroom5.grid_forget()
            labelReverseMushroom6.grid_forget()
            labelReverseMushroom7.grid_forget()
            labelReverseMushroom8.grid_forget()

            for i in range(16, 38):
                for widget in content_frame.winfo_children():
                    if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == f"{i}:1":
                        widget.grid_forget()
        else:
            for i in range(16, 38):
                for widget in content_frame.winfo_children():
                    if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == f"{i}:1":
                        widget.grid(row=i, column=1)

            # Mushroom: DX
            mushroomPrice1.grid(row=16, column=3)
            mushroomPrice2.grid(row=16, column=5)
            mushroomPrice34.grid(row=16, column=7)
            mushroomShopOdds12.grid(row=16, column=9)
            mushroomShopOdds34.grid(row=16, column=11)
            mushroomSpaceOdds1.grid(row=16, column=13)
            mushroomSpaceOdds2.grid(row=16, column=15)
            mushroomSpaceOdds34.grid(row=16, column=17)
            labelMushroom1.grid(row=16, column=2)
            labelMushroom2.grid(row=16, column=4)
            labelMushroom3.grid(row=16, column=6)
            labelMushroom4.grid(row=16, column=8)
            labelMushroom5.grid(row=16, column=10)
            labelMushroom6.grid(row=16, column=12)
            labelMushroom7.grid(row=16, column=14)
            labelMushroom8.grid(row=16, column=16)

            # Golden Mushroom: DX
            goldenMushroomPrice1.grid(row=17, column=3)
            goldenMushroomPrice2.grid(row=17, column=5)
            goldenMushroomPrice34.grid(row=17, column=7)
            goldenMushroomShopOdds12.grid(row=17, column=9)
            goldenMushroomShopOdds34.grid(row=17, column=11)
            goldenMushroomSpaceOdds1.grid(row=17, column=13)
            goldenMushroomSpaceOdds2.grid(row=17, column=15)
            goldenMushroomSpaceOdds34.grid(row=17, column=17)
            labelGoldenMushroom1.grid(row=17, column=2)
            labelGoldenMushroom2.grid(row=17, column=4)
            labelGoldenMushroom3.grid(row=17, column=6)
            labelGoldenMushroom4.grid(row=17, column=8)
            labelGoldenMushroom5.grid(row=17, column=10)
            labelGoldenMushroom6.grid(row=17, column=12)
            labelGoldenMushroom7.grid(row=17, column=14)
            labelGoldenMushroom8.grid(row=17, column=16)

            # Reverse Mushroom: DX
            reverseMushroomPrice1.grid(row=18, column=3)
            reverseMushroomPrice2.grid(row=18, column=5)
            reverseMushroomPrice34.grid(row=18, column=7)
            reverseMushroomShopOdds12.grid(row=18, column=9)
            reverseMushroomShopOdds34.grid(row=18, column=11)
            reverseMushroomSpaceOdds1.grid(row=18, column=13)
            reverseMushroomSpaceOdds2.grid(row=18, column=15)
            reverseMushroomSpaceOdds34.grid(row=18, column=17)
            labelReverseMushroom1.grid(row=18, column=2)
            labelReverseMushroom2.grid(row=18, column=4)
            labelReverseMushroom3.grid(row=18, column=6)
            labelReverseMushroom4.grid(row=18, column=8)
            labelReverseMushroom5.grid(row=18, column=10)
            labelReverseMushroom6.grid(row=18, column=12)
            labelReverseMushroom7.grid(row=18, column=14)
            labelReverseMushroom8.grid(row=18, column=16)

            # Poison Mushroom: DX
            poisonMushroomPrice1.grid(row=19, column=3)
            poisonMushroomPrice2.grid(row=19, column=5)
            poisonMushroomPrice34.grid(row=19, column=7)
            poisonMushroomShopOdds12.grid(row=19, column=9)
            poisonMushroomShopOdds34.grid(row=19, column=11)
            poisonMushroomSpaceOdds1.grid(row=19, column=13)
            poisonMushroomSpaceOdds2.grid(row=19, column=15)
            poisonMushroomSpaceOdds34.grid(row=19, column=17)
            labelPoisonMushroom1.grid(row=19, column=2)
            labelPoisonMushroom2.grid(row=19, column=4)
            labelPoisonMushroom3.grid(row=19, column=6)
            labelPoisonMushroom4.grid(row=19, column=8)
            labelPoisonMushroom5.grid(row=19, column=10)
            labelPoisonMushroom6.grid(row=19, column=12)
            labelPoisonMushroom7.grid(row=19, column=14)
            labelPoisonMushroom8.grid(row=19, column=16)

            # Triple Poison Mushroom: DX
            triplePoisonMushroomPrice1.grid(row=20, column=3)
            triplePoisonMushroomPrice2.grid(row=20, column=5)
            triplePoisonMushroomPrice34.grid(row=20, column=7)
            triplePoisonMushroomShopOdds12.grid(row=20, column=9)
            triplePoisonMushroomShopOdds34.grid(row=20, column=11)
            triplePoisonMushroomSpaceOdds1.grid(row=20, column=13)
            triplePoisonMushroomSpaceOdds2.grid(row=20, column=15)
            triplePoisonMushroomSpaceOdds34.grid(row=20, column=17)
            labelTriplePoisonMushroom1.grid(row=20, column=2)
            labelTriplePoisonMushroom2.grid(row=20, column=4)
            labelTriplePoisonMushroom3.grid(row=20, column=6)
            labelTriplePoisonMushroom4.grid(row=20, column=8)
            labelTriplePoisonMushroom5.grid(row=20, column=10)
            labelTriplePoisonMushroom6.grid(row=20, column=12)
            labelTriplePoisonMushroom7.grid(row=20, column=14)
            labelTriplePoisonMushroom8.grid(row=20, column=16)

            # Cellular Shopper: DX
            celluarShopperPrice1.grid(row=21, column=3)
            celluarShopperPrice2.grid(row=21, column=5)
            celluarShopperPrice34.grid(row=21, column=7)
            celluarShopperShopOdds12.grid(row=21, column=9)
            celluarShopperShopOdds34.grid(row=21, column=11)
            celluarShopperSpaceOdds1.grid(row=21, column=13)
            celluarShopperSpaceOdds2.grid(row=21, column=15)
            celluarShopperSpaceOdds34.grid(row=21, column=17)
            labelCelluarShopper1.grid(row=21, column=2)
            labelCelluarShopper2.grid(row=21, column=4)
            labelCelluarShopper3.grid(row=21, column=6)
            labelCelluarShopper4.grid(row=21, column=8)
            labelCelluarShopper5.grid(row=21, column=10)
            labelCelluarShopper6.grid(row=21, column=12)
            labelCelluarShopper7.grid(row=21, column=14)
            labelCelluarShopper8.grid(row=21, column=16)

            # Skeleton Key: DX
            skeletonKeyPrice1.grid(row=22, column=3)
            skeletonKeyPrice2.grid(row=22, column=5)
            skeletonKeyPrice34.grid(row=22, column=7)
            skeletonKeyShopOdds12.grid(row=22, column=9)
            skeletonKeyShopOdds34.grid(row=22, column=11)
            skeletonKeySpaceOdds1.grid(row=22, column=13)
            skeletonKeySpaceOdds2.grid(row=22, column=15)
            skeletonKeySpaceOdds34.grid(row=22, column=17)
            labelSkeletonKey1.grid(row=22, column=2)
            labelSkeletonKey2.grid(row=22, column=4)
            labelSkeletonKey3.grid(row=22, column=6)
            labelSkeletonKey4.grid(row=22, column=8)
            labelSkeletonKey5.grid(row=22, column=10)
            labelSkeletonKey6.grid(row=22, column=12)
            labelSkeletonKey7.grid(row=22, column=14)
            labelSkeletonKey8.grid(row=22, column=16)

            # Plunder Chest: DX
            plunderChestPrice1.grid(row=23, column=3)
            plunderChestPrice2.grid(row=23, column=5)
            plunderChestPrice34.grid(row=23, column=7)
            plunderChestShopOdds12.grid(row=23, column=9)
            plunderChestShopOdds34.grid(row=23, column=11)
            plunderChestSpaceOdds1.grid(row=23, column=13)
            plunderChestSpaceOdds2.grid(row=23, column=15)
            plunderChestSpaceOdds34.grid(row=23, column=17)
            labelPlunderChest1.grid(row=23, column=2)
            labelPlunderChest2.grid(row=23, column=4)
            labelPlunderChest3.grid(row=23, column=6)
            labelPlunderChest4.grid(row=23, column=8)
            labelPlunderChest5.grid(row=23, column=10)
            labelPlunderChest6.grid(row=23, column=12)
            labelPlunderChest7.grid(row=23, column=14)
            labelPlunderChest8.grid(row=23, column=16)

            # Gaddbrush: DX
            gaddbrushPrice1.grid(row=24, column=3)
            gaddbrushPrice2.grid(row=24, column=5)
            gaddbrushPrice34.grid(row=24, column=7)
            gaddbrushShopOdds12.grid(row=24, column=9)
            gaddbrushShopOdds34.grid(row=24, column=11)
            gaddbrushSpaceOdds1.grid(row=24, column=13)
            gaddbrushSpaceOdds2.grid(row=24, column=15)
            gaddbrushSpaceOdds34.grid(row=24, column=17)
            labelGaddbrush1.grid(row=24, column=2)
            labelGaddbrush2.grid(row=24, column=4)
            labelGaddbrush3.grid(row=24, column=6)
            labelGaddbrush4.grid(row=24, column=8)
            labelGaddbrush5.grid(row=24, column=10)
            labelGaddbrush6.grid(row=24, column=12)
            labelGaddbrush7.grid(row=24, column=14)
            labelGaddbrush8.grid(row=24, column=16)

            # Warp Block: DX
            warpBlockPrice1.grid(row=25, column=3)
            warpBlockPrice2.grid(row=25, column=5)
            warpBlockPrice34.grid(row=25, column=7)
            warpBlockShopOdds12.grid(row=25, column=9)
            warpBlockShopOdds34.grid(row=25, column=11)
            warpBlockSpaceOdds1.grid(row=25, column=13)
            warpBlockSpaceOdds2.grid(row=25, column=15)
            warpBlockSpaceOdds34.grid(row=25, column=17)
            labelWarpBlock1.grid(row=25, column=2)
            labelWarpBlock2.grid(row=25, column=4)
            labelWarpBlock3.grid(row=25, column=6)
            labelWarpBlock4.grid(row=25, column=8)
            labelWarpBlock5.grid(row=25, column=10)
            labelWarpBlock6.grid(row=25, column=12)
            labelWarpBlock7.grid(row=25, column=14)
            labelWarpBlock8.grid(row=25, column=16)

            # Fly Guy: DX
            flyGuyPrice1.grid(row=26, column=3)
            flyGuyPrice2.grid(row=26, column=5)
            flyGuyPrice34.grid(row=26, column=7)
            flyGuyShopOdds12.grid(row=26, column=9)
            flyGuyShopOdds34.grid(row=26, column=11)
            flyGuySpaceOdds1.grid(row=26, column=13)
            flyGuySpaceOdds2.grid(row=26, column=15)
            flyGuySpaceOdds34.grid(row=26, column=17)
            labelFlyGuy1.grid(row=26, column=2)
            labelFlyGuy2.grid(row=26, column=4)
            labelFlyGuy3.grid(row=26, column=6)
            labelFlyGuy4.grid(row=26, column=8)
            labelFlyGuy5.grid(row=26, column=10)
            labelFlyGuy6.grid(row=26, column=12)
            labelFlyGuy7.grid(row=26, column=14)
            labelFlyGuy8.grid(row=26, column=16)

            # Plus Block: DX
            plusBlockPrice1.grid(row=27, column=3)
            plusBlockPrice2.grid(row=27, column=5)
            plusBlockPrice34.grid(row=27, column=7)
            plusBlockShopOdds12.grid(row=27, column=9)
            plusBlockShopOdds34.grid(row=27, column=11)
            plusBlockSpaceOdds1.grid(row=27, column=13)
            plusBlockSpaceOdds2.grid(row=27, column=15)
            plusBlockSpaceOdds34.grid(row=27, column=17)
            labelPlusBlock1.grid(row=27, column=2)
            labelPlusBlock2.grid(row=27, column=4)
            labelPlusBlock3.grid(row=27, column=6)
            labelPlusBlock4.grid(row=27, column=8)
            labelPlusBlock5.grid(row=27, column=10)
            labelPlusBlock6.grid(row=27, column=12)
            labelPlusBlock7.grid(row=27, column=14)
            labelPlusBlock8.grid(row=27, column=16)


            # Minus Block: DX
            minusBlockPrice1.grid(row=28, column=3)
            minusBlockPrice2.grid(row=28, column=5)
            minusBlockPrice34.grid(row=28, column=7)
            minusBlockShopOdds12.grid(row=28, column=9)
            minusBlockShopOdds34.grid(row=28, column=11)
            minusBlockSpaceOdds1.grid(row=28, column=13)
            minusBlockSpaceOdds2.grid(row=28, column=15)
            minusBlockSpaceOdds34.grid(row=28, column=17)
            labelMinusBlock1.grid(row=28, column=2)
            labelMinusBlock2.grid(row=28, column=4)
            labelMinusBlock3.grid(row=28, column=6)
            labelMinusBlock4.grid(row=28, column=8)
            labelMinusBlock5.grid(row=28, column=10)
            labelMinusBlock6.grid(row=28, column=12)
            labelMinusBlock7.grid(row=28, column=14)
            labelMinusBlock8.grid(row=28, column=16)

            # Speed Block: DX
            speedBlockPrice1.grid(row=29, column=3)
            speedBlockPrice2.grid(row=29, column=5)
            speedBlockPrice34.grid(row=29, column=7)
            speedBlockShopOdds12.grid(row=29, column=9)
            speedBlockShopOdds34.grid(row=29, column=11)
            speedBlockSpaceOdds1.grid(row=29, column=13)
            speedBlockSpaceOdds2.grid(row=29, column=15)
            speedBlockSpaceOdds34.grid(row=29, column=17)
            labelSpeedBlock1.grid(row=29, column=2)
            labelSpeedBlock2.grid(row=29, column=4)
            labelSpeedBlock3.grid(row=29, column=6)
            labelSpeedBlock4.grid(row=29, column=8)
            labelSpeedBlock5.grid(row=29, column=10)
            labelSpeedBlock6.grid(row=29, column=12)
            labelSpeedBlock7.grid(row=29, column=14)
            labelSpeedBlock8.grid(row=29, column=16)

            # Slow Block: DX
            slowBlockPrice1.grid(row=30, column=3)
            slowBlockPrice2.grid(row=30, column=5)
            slowBlockPrice34.grid(row=30, column=7)
            slowBlockShopOdds12.grid(row=30, column=9)
            slowBlockShopOdds34.grid(row=30, column=11)
            slowBlockSpaceOdds1.grid(row=30, column=13)
            slowBlockSpaceOdds2.grid(row=30, column=15)
            slowBlockSpaceOdds34.grid(row=30, column=17)
            labelSlowBlock1.grid(row=30, column=2)
            labelSlowBlock2.grid(row=30, column=4)
            labelSlowBlock3.grid(row=30, column=6)
            labelSlowBlock4.grid(row=30, column=8)
            labelSlowBlock5.grid(row=30, column=10)
            labelSlowBlock6.grid(row=30, column=12)
            labelSlowBlock7.grid(row=30, column=14)
            labelSlowBlock8.grid(row=30, column=16)

            # Bowser Phone: DX
            bowserPhonePrice1.grid(row=31, column=3)
            bowserPhonePrice2.grid(row=31, column=5)
            bowserPhonePrice34.grid(row=31, column=7)
            bowserPhoneShopOdds12.grid(row=31, column=9)
            bowserPhoneShopOdds34.grid(row=31, column=11)
            bowserPhoneSpaceOdds1.grid(row=31, column=13)
            bowserPhoneSpaceOdds2.grid(row=31, column=15)
            bowserPhoneSpaceOdds34.grid(row=31, column=17)
            labelBowserPhone1.grid(row=31, column=2)
            labelBowserPhone2.grid(row=31, column=4)
            labelBowserPhone3.grid(row=31, column=6)
            labelBowserPhone4.grid(row=31, column=8)
            labelBowserPhone5.grid(row=31, column=10)
            labelBowserPhone6.grid(row=31, column=12)
            labelBowserPhone7.grid(row=31, column=14)
            labelBowserPhone8.grid(row=31, column=16)

            # Double Dip: DX
            doubleDipPrice1.grid(row=32, column=3)
            doubleDipPrice2.grid(row=32, column=5)
            doubleDipPrice34.grid(row=32, column=7)
            doubleDipShopOdds12.grid(row=32, column=9)
            doubleDipShopOdds34.grid(row=32, column=11)
            doubleDipSpaceOdds1.grid(row=32, column=13)
            doubleDipSpaceOdds2.grid(row=32, column=15)
            doubleDipSpaceOdds34.grid(row=32, column=17)
            labelDoubleDip1.grid(row=32, column=2)
            labelDoubleDip2.grid(row=32, column=4)
            labelDoubleDip3.grid(row=32, column=6)
            labelDoubleDip4.grid(row=32, column=8)
            labelDoubleDip5.grid(row=32, column=10)
            labelDoubleDip6.grid(row=32, column=12)
            labelDoubleDip7.grid(row=32, column=14)
            labelDoubleDip8.grid(row=32, column=16)

            # Hidden Block Card: DX
            hiddenBlockCardPrice1.grid(row=33, column=3)
            hiddenBlockCardPrice2.grid(row=33, column=5)
            hiddenBlockCardPrice34.grid(row=33, column=7)
            hiddenBlockCardShopOdds12.grid(row=33, column=9)
            hiddenBlockCardShopOdds34.grid(row=33, column=11)
            hiddenBlockCardSpaceOdds1.grid(row=33, column=13)
            hiddenBlockCardSpaceOdds2.grid(row=33, column=15)
            hiddenBlockCardSpaceOdds34.grid(row=33, column=17)
            labelHiddenBlockCard1.grid(row=33, column=2)
            labelHiddenBlockCard2.grid(row=33, column=4)
            labelHiddenBlockCard3.grid(row=33, column=6)
            labelHiddenBlockCard4.grid(row=33, column=8)
            labelHiddenBlockCard5.grid(row=33, column=10)
            labelHiddenBlockCard6.grid(row=33, column=12)
            labelHiddenBlockCard7.grid(row=33, column=14)
            labelHiddenBlockCard8.grid(row=33, column=16)

            # Super Warp Pipe: DX
            superWarpPipePrice1.grid(row=34, column=3)
            superWarpPipePrice2.grid(row=34, column=5)
            superWarpPipePrice34.grid(row=34, column=7)
            superWarpPipeShopOdds12.grid(row=34, column=9)
            superWarpPipeShopOdds34.grid(row=34, column=11)
            superWarpPipeSpaceOdds1.grid(row=34, column=13)
            superWarpPipeSpaceOdds2.grid(row=34, column=15)
            superWarpPipeSpaceOdds34.grid(row=34, column=17)
            labelSuperWarpPipe1.grid(row=34, column=2)
            labelSuperWarpPipe2.grid(row=34, column=4)
            labelSuperWarpPipe3.grid(row=34, column=6)
            labelSuperWarpPipe4.grid(row=34, column=8)
            labelSuperWarpPipe5.grid(row=34, column=10)
            labelSuperWarpPipe6.grid(row=34, column=12)
            labelSuperWarpPipe7.grid(row=34, column=14)
            labelSuperWarpPipe8.grid(row=34, column=16)

            # Barter Box: DX
            barterBoxPrice1.grid(row=35, column=3)
            barterBoxPrice2.grid(row=35, column=5)
            barterBoxPrice34.grid(row=35, column=7)
            barterBoxShopOdds12.grid(row=35, column=9)
            barterBoxShopOdds34.grid(row=35, column=11)
            barterBoxSpaceOdds1.grid(row=35, column=13)
            barterBoxSpaceOdds2.grid(row=35, column=15)
            barterBoxSpaceOdds34.grid(row=35, column=17)
            labelBarterBox1.grid(row=35, column=2)
            labelBarterBox2.grid(row=35, column=4)
            labelBarterBox3.grid(row=35, column=6)
            labelBarterBox4.grid(row=35, column=8)
            labelBarterBox5.grid(row=35, column=10)
            labelBarterBox6.grid(row=35, column=12)
            labelBarterBox7.grid(row=35, column=14)
            labelBarterBox8.grid(row=35, column=16)

            # Chance Time Charm: DX
            chanceTimeCharmPrice1.grid(row=36, column=3)
            chanceTimeCharmPrice2.grid(row=36, column=5)
            chanceTimeCharmPrice34.grid(row=36, column=7)
            chanceTimeCharmShopOdds12.grid(row=36, column=9)
            chanceTimeCharmShopOdds34.grid(row=36, column=11)
            chanceTimeCharmSpaceOdds1.grid(row=36, column=13)
            chanceTimeCharmSpaceOdds2.grid(row=36, column=15)
            chanceTimeCharmSpaceOdds34.grid(row=36, column=17)
            labelChanceTimeCharm1.grid(row=36, column=2)
            labelChanceTimeCharm2.grid(row=36, column=4)
            labelChanceTimeCharm3.grid(row=36, column=6)
            labelChanceTimeCharm4.grid(row=36, column=8)
            labelChanceTimeCharm5.grid(row=36, column=10)
            labelChanceTimeCharm6.grid(row=36, column=12)
            labelChanceTimeCharm7.grid(row=36, column=14)
            labelChanceTimeCharm8.grid(row=36, column=16)

            # Wacky Watch: DX
            wackyWatchPrice1.grid(row=37, column=3)
            wackyWatchPrice2.grid(row=37, column=5)
            wackyWatchPrice34.grid(row=37, column=7)
            wackyWatchShopOdds12.grid(row=37, column=9)
            wackyWatchShopOdds34.grid(row=37, column=11)
            wackyWatchSpaceOdds1.grid(row=37, column=13)
            wackyWatchSpaceOdds2.grid(row=37, column=15)
            wackyWatchSpaceOdds34.grid(row=37, column=17)
            labelWackyWatch1.grid(row=37, column=2)
            labelWackyWatch2.grid(row=37, column=4)
            labelWackyWatch3.grid(row=37, column=6)
            labelWackyWatch4.grid(row=37, column=8)
            labelWackyWatch5.grid(row=37, column=10)
            labelWackyWatch6.grid(row=37, column=12)
            labelWackyWatch7.grid(row=37, column=14)
            labelWackyWatch8.grid(row=37, column=16)
           
    hideCustomSwitch.configure(command=toggle_hide_custom)
    toggle_hide_custom()

    hideSpaceSwitch.configure(command=toggle_hide_itemSpace)
    toggle_hide_itemSpace()

    # END ITEMS

    items4 = ["None", "Mini Mushroom", "Mega Mushroom", "Super Mini Mushroom", "Super Mega Mushroom", "Mini-Mega Hammer", "Warp Pipe", "Swap Card", "Sparky Sticker", "Gaddlight", "Chomp Call", "Bowser Suit", "Boo's Crystal Ball", "Magic Lamp", "Item Bag"]

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