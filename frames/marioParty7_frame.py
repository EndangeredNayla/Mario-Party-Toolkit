# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty7_coins import *
from events.marioParty7_initialItems import *
from events.marioParty7_mgreplace import *
from events.marioParty7_boardSpecific import *
from events.marioParty7_handicap import *
from events.marioParty7_items import *
from events.marioParty7_spaceReplace import *
from events.marioParty7_bonusStarReplace import *
from events.marioParty7_battle import *

# Import custom tkinter module as ctk
import customtkinter as ctk
from CTkToolTip import *

# Function to create the main interface for Mario Party 1
def create_mario_party_7_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Orb Mods")
    tabview.add("Space Replacement")
    tabview.add("Initial Orbs")
    tabview.add("Battle Minigame")
    tabview.add("Star Handicaps")
    tabview.add("Bonus Star Replacement")
    tabview.add("Board Specific")
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
    
    # Function to create an entry field and checkbox
    def create_entry2(tab, row, icon_path, label_text, color):
        create_image_icon(tab, icon_path, row, 5)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=6, sticky="w", pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"))
        entry.grid(row=row, column=7)
        label1 = ctk.CTkLabel(master=tab, text=color, font=("Arial", 16))
        label1.grid(row=row, column=8, sticky="w")
        return entry

    # Create entry fields and checkboxes for Coins Mods tab
    blue_entry = create_entry(tabview.tab("Coins Mods"), 1, "assets/eventTags/blueSpace.png", " Gain  ", " Coins on a Blue Space.")
    red_entry = create_entry(tabview.tab("Coins Mods"), 2, "assets/eventTags/redSpace.png", " Lose  ", " Coins on a Red Space.")
    character_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/characterSpace7.png", " Gain  ", " Coins on your own Character Space.")
    mgWin_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/miniGame.png", " Gain  ", " Coins when winning a Minigame.")

    star_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star at a Star Space and when using Flutter.  ")
    windmill_entryTooltip = CTkToolTip(star_entry, message="Works on Canal, Pagoda, Neon Heights, and Bowser.")

    star_last4_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star during Last 4 Turns.")
    hammerBro_entry = create_entry2(tabview.tab("Coins Mods"), 1, "assets/items/hammerBroCapsule.png", " Steal ", " Coins from Hammer Bro.")
    zap_entry = create_entry2(tabview.tab("Coins Mods"), 2, "assets/items/zapCapsule.png", " Lose ", " Coins from Zaps.")
    fireball_entry = create_entry2(tabview.tab("Coins Mods"), 3, "assets/items/fireballCapsule.png", " Steal ", " Coins from Fireballs.")
    vacuum_entry = create_entry2(tabview.tab("Coins Mods"), 4, "assets/items/vacuumCapsule.png", " Steal ", " Coins despite Vacuum Roulette.")
    flower_entry = create_entry2(tabview.tab("Coins Mods"), 5, "assets/items/flowerCapsule.png", " Gain ", " Per Space with Flower.")
    initial_entry = create_entry2(tabview.tab("Coins Mods"), 6, "assets/eventTags/initialCoins.png", " Gain ", " Coins at the start of the game.")

    # Create button to generate coins modification codes  
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp7(blue_entry, red_entry, character_entry, mgWin_entry, star_entry, star_last4_entry, hammerBro_entry, zap_entry, fireball_entry, vacuum_entry, flower_entry, initial_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

    # List of minigame names
    minigames_list = ["Catchy Tunes", "Bubble Brawl", "Track & Yield", "Fun Run", "Cointagious", "Snow Ride", "Picture This", "Ghost in the Hall", "Big Dripper", "Target Tag", "Pokey Pummel", "Take Me Ohm", "Kart Wheeled", "Balloon Busters", "Clock Watchers", "Dart Attack", "Oil Crisis", "La Bomba", "Spray Anything", "Balloonatic", "Spinner Cell", "Think Tank", "Flashfright", "Coin-op Bop", "Easy Pickings", "Wheel of Woe", "Boxing Day", "Be My Chum!", "StratosFEAR!", "Pogo-a-go-go", "Buzzstormer", "Tile and Error", "Battery Ram", "Cardinal Rule", "Ice Moves", "Bumper Crop", "Hop-O-Matic 4000", "Wingin' It", "Sphere Factor", "Herbicidal Maniac", "Pyramid Scheme", "World Piece", "Warp Pipe Dreams", "Weight for It", "Helipopper", "Monty's Revenge", "Deck Hands", "Mad Props", "Gimme a Sign", "Bridge Work", "Spin Doctor", "Hip Hop Drop", "Air Farce", "The Final Countdown", "Royal Rumpus", "Light Speed", "Apes of Wrath", "Fish & Cheeps", "Camp Ukiki", "Funstacle Course!", "Funderwall!", "Magmagical Journey!", "Tunnel of Lava!", "Treasure Dome!", "Slot-O-Whirl!", "Peel Out", "Bananas Faster", "Stump Change", "Jump, Man", "Vine Country", "A Bridge Too Short", "Spider Stomp", "Stick and Spin", "Bowser's Lovely Lift!"]    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp7(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)


    # ORB GEN
    scrollable_frame = ctk.CTkFrame(master=tabview.tab("Orb Mods"), fg_color=("#fcfcfc", "#2e2e2e"))
    scrollable_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 50))
    # Configure grid to allow stretching
    tabview.tab("Orb Mods").grid_rowconfigure(0, weight=1)
    tabview.tab("Orb Mods").grid_columnconfigure(0, weight=1)
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
    canvas.grid_rowconfigure(0, weight=1)  # Ensure the canvas fills the height

    # Mushroom
    icon = create_image_icon(content_frame, "assets/items/mushroomCapsule.png", 2, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=2, column=2)
    label = ctk.CTkLabel(master=content_frame, text=" 5 ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=2, column=4)
    label = ctk.CTkLabel(master=content_frame, text=" 5 ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=2, column=6)
    mushroomCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleShopOdds12.grid(row=2, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=2, column=8)
    mushroomCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleShopOdds34.grid(row=2, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=2, column=10)
    mushroomCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleSpaceOdds12.grid(row=2, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=2, column=12)
    mushroomCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleSpaceOdds34.grid(row=2, column=13)

    # Golden Mushroom
    icon = create_image_icon(content_frame, "assets/items/goldenMushroomCapsule.png", 3, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=3, column=2)
    goldenMushroomCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice12.grid(row=3, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=3, column=4)
    goldenMushroomCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice34.grid(row=3, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=3, column=6)
    goldenMushroomCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleShopOdds12.grid(row=3, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=3, column=8)
    goldenMushroomCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleShopOdds34.grid(row=3, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=3, column=10)
    goldenMushroomCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleSpaceOdds12.grid(row=3, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=3, column=12)
    goldenMushroomCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleSpaceOdds34.grid(row=3, column=13)

    # Slow Mushroom
    icon = create_image_icon(content_frame, "assets/items/slowMushroomCapsule.png", 4, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=4, column=2)
    slowMushroomCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsulePrice12.grid(row=4, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=4, column=4)
    slowMushroomCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsulePrice34.grid(row=4, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=4, column=6)
    slowMushroomCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleShopOdds12.grid(row=4, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=4, column=8)
    slowMushroomCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleShopOdds34.grid(row=4, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=4, column=10)
    slowMushroomCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleSpaceOdds12.grid(row=4, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=4, column=12)
    slowMushroomCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleSpaceOdds34.grid(row=4, column=13)

    # Metal Mushroom
    icon = create_image_icon(content_frame, "assets/items/metalMushroomCapsule.png", 5, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=5, column=2)
    metalMushroomCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsulePrice12.grid(row=5, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=5, column=4)
    metalMushroomCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsulePrice34.grid(row=5, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=5, column=6)
    metalMushroomCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleShopOdds12.grid(row=5, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=5, column=8)
    metalMushroomCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleShopOdds34.grid(row=5, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=5, column=10)
    metalMushroomCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleSpaceOdds12.grid(row=5, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=5, column=12)
    metalMushroomCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleSpaceOdds34.grid(row=5, column=13)

    # Flutter
    icon = create_image_icon(content_frame, "assets/items/wigglerCapsule.png", 6, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=6, column=2)
    flutterCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice12.grid(row=6, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=6, column=4)
    flutterCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice34.grid(row=6, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=6, column=6)
    flutterCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleShopOdds12.grid(row=6, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=6, column=8)
    flutterCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleShopOdds34.grid(row=6, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=6, column=10)
    flutterCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleSpaceOdds12.grid(row=6, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=6, column=12)
    flutterCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleSpaceOdds34.grid(row=6, column=13)

    # Cannon
    icon = create_image_icon(content_frame, "assets/items/cannonCapsule.png", 7, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=7, column=2)
    cannonCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsulePrice12.grid(row=7, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=7, column=4)
    cannonCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsulePrice34.grid(row=7, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=7, column=6)
    cannonCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleShopOdds12.grid(row=7, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=7, column=8)
    cannonCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleShopOdds34.grid(row=7, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=7, column=10)
    cannonCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleSpaceOdds12.grid(row=7, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=7, column=12)
    cannonCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleSpaceOdds34.grid(row=7, column=13)

    # Snack
    icon = create_image_icon(content_frame, "assets/items/snackCapsule.png", 8, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=8, column=2)
    snackCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsulePrice12.grid(row=8, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=8, column=4)
    snackCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsulePrice34.grid(row=8, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=8, column=6)
    snackCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleShopOdds12.grid(row=8, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=8, column=8)
    snackCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleShopOdds34.grid(row=8, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=8, column=10)
    snackCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleSpaceOdds12.grid(row=8, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=8, column=12)
    snackCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleSpaceOdds34.grid(row=8, column=13)

    # Lakitu
    icon = create_image_icon(content_frame, "assets/items/lakituCapsule.png", 9, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=9, column=2)
    lakituCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsulePrice12.grid(row=9, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=9, column=4)
    lakituCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsulePrice34.grid(row=9, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=9, column=6)
    lakituCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleShopOdds12.grid(row=9, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=9, column=8)
    lakituCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleShopOdds34.grid(row=9, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=9, column=10)
    lakituCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleSpaceOdds12.grid(row=9, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=9, column=12)
    lakituCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleSpaceOdds34.grid(row=9, column=13)

    # Hammer Bro
    icon = create_image_icon(content_frame, "assets/items/hammerBroCapsule.png", 10, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=10, column=2)
    hammerBroCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsulePrice12.grid(row=10, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=10, column=4)
    hammerBroCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsulePrice34.grid(row=10, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=10, column=6)
    hammerBroCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleShopOdds12.grid(row=10, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=10, column=8)
    hammerBroCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleShopOdds34.grid(row=10, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=10, column=10)
    hammerBroCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleSpaceOdds12.grid(row=10, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=10, column=12)
    hammerBroCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleSpaceOdds34.grid(row=10, column=13)

    # Piranha Plant
    icon = create_image_icon(content_frame, "assets/items/plantCapsule.png", 11, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=11, column=2)
    piranhaPlantCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsulePrice12.grid(row=11, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=11, column=4)
    piranhaPlantCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsulePrice34.grid(row=11, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=11, column=6)
    piranhaPlantCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleShopOdds12.grid(row=11, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=11, column=8)
    piranhaPlantCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleShopOdds34.grid(row=11, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=11, column=10)
    piranhaPlantCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleSpaceOdds12.grid(row=11, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=11, column=12)
    piranhaPlantCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleSpaceOdds34.grid(row=11, column=13)

    # Spear Guy
    icon = create_image_icon(content_frame, "assets/items/spearCapsule.png", 12, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=12, column=2)
    spearGuyCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsulePrice12.grid(row=12, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=12, column=4)
    spearGuyCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsulePrice34.grid(row=12, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=12, column=6)
    spearGuyCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleShopOdds12.grid(row=12, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=12, column=8)
    spearGuyCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleShopOdds34.grid(row=12, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=12, column=10)
    spearGuyCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleSpaceOdds12.grid(row=12, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=12, column=12)
    spearGuyCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleSpaceOdds34.grid(row=12, column=13)

    # Kamek
    icon = create_image_icon(content_frame, "assets/items/kamekCapsule.png", 13, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=13, column=2)
    kamekCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice12.grid(row=13, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=13, column=4)
    kamekCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice34.grid(row=13, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=13, column=6)
    kamekCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleShopOdds12.grid(row=13, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=13, column=8)
    kamekCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleShopOdds34.grid(row=13, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=13, column=10)
    kamekCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleSpaceOdds12.grid(row=13, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=13, column=12)
    kamekCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleSpaceOdds34.grid(row=13, column=13)

    # Toady
    icon = create_image_icon(content_frame, "assets/items/toadyCapsule.png", 14, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=14, column=2)
    toadyCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsulePrice12.grid(row=14, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=14, column=4)
    toadyCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsulePrice34.grid(row=14, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=14, column=6)
    toadyCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleShopOdds12.grid(row=14, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=14, column=8)
    toadyCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleShopOdds34.grid(row=14, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=14, column=10)
    toadyCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleSpaceOdds12.grid(row=14, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=14, column=12)
    toadyCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleSpaceOdds34.grid(row=14, column=13)

    # Mr. Blizzard
    icon = create_image_icon(content_frame, "assets/items/blizzardCapsule.png", 15, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=15, column=2)
    mrBlizzardCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsulePrice12.grid(row=15, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=15, column=4)
    mrBlizzardCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsulePrice34.grid(row=15, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=15, column=6)
    mrBlizzardCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleShopOdds12.grid(row=15, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=15, column=8)
    mrBlizzardCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleShopOdds34.grid(row=15, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=15, column=10)
    mrBlizzardCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleSpaceOdds12.grid(row=15, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=15, column=12)
    mrBlizzardCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleSpaceOdds34.grid(row=15, column=13)

    # Bandit
    icon = create_image_icon(content_frame, "assets/items/banditCapsule.png", 16, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=16, column=2)
    banditCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsulePrice12.grid(row=16, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=16, column=4)
    banditCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsulePrice34.grid(row=16, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=16, column=6)
    banditCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleShopOdds12.grid(row=16, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=16, column=8)
    banditCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleShopOdds34.grid(row=16, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=16, column=10)
    banditCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleSpaceOdds12.grid(row=16, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=16, column=12)
    banditCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleSpaceOdds34.grid(row=16, column=13)

    # Pink Boo
    icon = create_image_icon(content_frame, "assets/items/pinkBooCapsule.png", 17, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=17, column=2)
    pinkBooCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice12.grid(row=17, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=17, column=4)
    pinkBooCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice34.grid(row=17, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=17, column=6)
    pinkBooCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleShopOdds12.grid(row=17, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=17, column=8)
    pinkBooCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleShopOdds34.grid(row=17, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=17, column=10)
    pinkBooCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleSpaceOdds12.grid(row=17, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=17, column=12)
    pinkBooCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleSpaceOdds34.grid(row=17, column=13)

    # Spiny
    icon = create_image_icon(content_frame, "assets/items/spinyCapsule.png", 18, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=18, column=2)
    spinyCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice12.grid(row=18, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=18, column=4)
    spinyCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice34.grid(row=18, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=18, column=6)
    spinyCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleShopOdds12.grid(row=18, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=18, column=8)
    spinyCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleShopOdds34.grid(row=18, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=18, column=10)
    spinyCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleSpaceOdds12.grid(row=18, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=18, column=12)
    spinyCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleSpaceOdds34.grid(row=18, column=13)

    # Zap
    icon = create_image_icon(content_frame, "assets/items/zapCapsule.png", 19, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=19, column=2)
    zapCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsulePrice12.grid(row=19, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=19, column=4)
    zapCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsulePrice34.grid(row=19, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=19, column=6)
    zapCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleShopOdds12.grid(row=19, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=19, column=8)
    zapCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleShopOdds34.grid(row=19, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=19, column=10)
    zapCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleSpaceOdds12.grid(row=19, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=19, column=12)
    zapCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleSpaceOdds34.grid(row=19, column=13)

    # Tweester
    icon = create_image_icon(content_frame, "assets/items/tweesterCapsule.png", 20, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=20, column=2)
    tweesterCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice12.grid(row=20, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=20, column=4)
    tweesterCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice34.grid(row=20, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=20, column=6)
    tweesterCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleShopOdds12.grid(row=20, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=20, column=8)
    tweesterCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleShopOdds34.grid(row=20, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=20, column=10)
    tweesterCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleSpaceOdds12.grid(row=20, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=20, column=12)
    tweesterCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleSpaceOdds34.grid(row=20, column=13)

    # Thwomp
    icon = create_image_icon(content_frame, "assets/items/thwompCapsule.png", 21, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=21, column=2)
    thwompCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsulePrice12.grid(row=21, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=21, column=4)
    thwompCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsulePrice34.grid(row=21, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=21, column=6)
    thwompCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleShopOdds12.grid(row=21, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=21, column=8)
    thwompCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleShopOdds34.grid(row=21, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=21, column=10)
    thwompCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleSpaceOdds12.grid(row=21, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=21, column=12)
    thwompCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleSpaceOdds34.grid(row=21, column=13)

    # Warp
    icon = create_image_icon(content_frame, "assets/items/warpCapsule.png", 22, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=22, column=2)
    warpCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsulePrice12.grid(row=22, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=22, column=4)
    warpCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsulePrice34.grid(row=22, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=22, column=6)
    warpCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleShopOdds12.grid(row=22, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=22, column=8)
    warpCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleShopOdds34.grid(row=22, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=22, column=10)
    warpCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleSpaceOdds12.grid(row=22, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=22, column=12)
    warpCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleSpaceOdds34.grid(row=22, column=13)

    # Bomb
    icon = create_image_icon(content_frame, "assets/items/bombCapsule.png", 23, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=23, column=2)
    bombCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice12.grid(row=23, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=23, column=4)
    bombCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice34.grid(row=23, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=23, column=6)
    bombCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleShopOdds12.grid(row=23, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=23, column=8)
    bombCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleShopOdds34.grid(row=23, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=23, column=10)
    bombCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleSpaceOdds12.grid(row=23, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=23, column=12)
    bombCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleSpaceOdds34.grid(row=23, column=13)

    # Fireball
    icon = create_image_icon(content_frame, "assets/items/fireballCapsule.png", 24, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=24, column=2)
    fireballCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsulePrice12.grid(row=24, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=24, column=4)
    fireballCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsulePrice34.grid(row=24, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=24, column=6)
    fireballCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleShopOdds12.grid(row=24, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=24, column=8)
    fireballCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleShopOdds34.grid(row=24, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=24, column=10)
    fireballCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleSpaceOdds12.grid(row=24, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=24, column=12)
    fireballCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleSpaceOdds34.grid(row=24, column=13)

    # Flower
    icon = create_image_icon(content_frame, "assets/items/flowerCapsule.png", 25, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=25, column=2)
    flowerCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsulePrice12.grid(row=25, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=25, column=4)
    flowerCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsulePrice34.grid(row=25, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=25, column=6)
    flowerCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleShopOdds12.grid(row=25, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=25, column=8)
    flowerCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleShopOdds34.grid(row=25, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=25, column=10)
    flowerCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleSpaceOdds12.grid(row=25, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=25, column=12)
    flowerCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleSpaceOdds34.grid(row=25, column=13)

    # Egg
    icon = create_image_icon(content_frame, "assets/items/eggCapsule.png", 26, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=26, column=2)
    eggCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsulePrice12.grid(row=26, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=26, column=4)
    eggCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsulePrice34.grid(row=26, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=26, column=6)
    eggCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleShopOdds12.grid(row=26, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=26, column=8)
    eggCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleShopOdds34.grid(row=26, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=26, column=10)
    eggCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleSpaceOdds12.grid(row=26, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=26, column=12)
    eggCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleSpaceOdds34.grid(row=26, column=13)

    # Vacuum
    icon = create_image_icon(content_frame, "assets/items/vacuumCapsule.png", 27, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=27, column=2)
    vacuumCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsulePrice12.grid(row=27, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=27, column=4)
    vacuumCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsulePrice34.grid(row=27, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=27, column=6)
    vacuumCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleShopOdds12.grid(row=27, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=27, column=8)
    vacuumCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleShopOdds34.grid(row=27, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=27, column=10)
    vacuumCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleSpaceOdds12.grid(row=27, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=27, column=12)
    vacuumCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleSpaceOdds34.grid(row=27, column=13)

    # Magic
    icon = create_image_icon(content_frame, "assets/items/magicCapsule.png", 28, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=28, column=2)
    magicCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsulePrice12.grid(row=28, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=28, column=4)
    magicCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsulePrice34.grid(row=28, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=28, column=6)
    magicCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleShopOdds12.grid(row=28, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=28, column=8)
    magicCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleShopOdds34.grid(row=28, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=28, column=10)
    magicCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleSpaceOdds12.grid(row=28, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=28, column=12)
    magicCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleSpaceOdds34.grid(row=28, column=13)

    # Triple
    icon = create_image_icon(content_frame, "assets/items/tripleCapsule.png", 29, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=29, column=2)
    tripleCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsulePrice12.grid(row=29, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=29, column=4)
    tripleCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsulePrice34.grid(row=29, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=29, column=6)
    tripleCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleShopOdds12.grid(row=29, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=29, column=8)
    tripleCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleShopOdds34.grid(row=29, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=29, column=10)
    tripleCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleSpaceOdds12.grid(row=29, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=29, column=12)
    tripleCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleSpaceOdds34.grid(row=29, column=13)

    # Triple
    icon = create_image_icon(content_frame, "assets/items/koopaCapsule.png", 30, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    label.grid(row=30, column=2)
    koopaCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsulePrice12.grid(row=30, column=3)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=30, column=4)
    koopaCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsulePrice34.grid(row=30, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=30, column=6)
    koopaCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleShopOdds12.grid(row=30, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=30, column=8)
    koopaCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleShopOdds34.grid(row=30, column=9)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=30, column=10)
    koopaCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleSpaceOdds12.grid(row=30, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=30, column=12)
    koopaCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleSpaceOdds34.grid(row=30, column=13)

    # Cursed Mushroom
    icon = create_image_icon(content_frame, "assets/items/cursedMushroomCapsule7.png", 31, 1)
    labelPoison1 = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    labelPoison1.grid(row=31, column=2)
    poisonMushroomPrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomPrice12.grid(row=31, column=3)
    labelPoison2 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelPoison2.grid(row=31, column=4)
    poisonMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomPrice34.grid(row=31, column=5)
    labelPoison3 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelPoison3.grid(row=31, column=6)
    poisonMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomShopOdds12.grid(row=31, column=7)
    labelPoison4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelPoison4.grid(row=31, column=8)
    poisonMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomShopOdds34.grid(row=31, column=9)
    labelPoison5 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    labelPoison5.grid(row=31, column=10)
    poisonMushroomSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomSpaceOdds12.grid(row=31, column=11)
    labelPoison6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelPoison6.grid(row=31, column=12)
    poisonMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomSpaceOdds34.grid(row=31, column=13)

    # Duel Capsule
    icon = create_image_icon(content_frame, "assets/items/duelCapsule.png", 32, 1)
    labelDuel1 = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    labelDuel1.grid(row=32, column=2)
    duelCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice12.grid(row=32, column=3)
    labelDuel2 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelDuel2.grid(row=32, column=4)
    duelCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice34.grid(row=32, column=5)
    labelDuel3 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelDuel3.grid(row=32, column=6)
    duelCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleShopOdds12.grid(row=32, column=7)
    labelDuel4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelDuel4.grid(row=32, column=8)
    duelCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleShopOdds34.grid(row=32, column=9)
    labelDuel5 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    labelDuel5.grid(row=32, column=10)
    duelCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleSpaceOdds12.grid(row=32, column=11)
    labelDuel6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelDuel6.grid(row=32, column=12)
    duelCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleSpaceOdds34.grid(row=32, column=13)

    # DK Capsule
    icon = create_image_icon(content_frame, "assets/items/dkCapsule.png", 33, 1)
    labelDK1 = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    labelDK1.grid(row=33, column=2)
    dkCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice12.grid(row=33, column=3)
    labelDK2 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelDK2.grid(row=33, column=4)
    dkCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice34.grid(row=33, column=5)
    labelDK3 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelDK3.grid(row=33, column=6)
    dkCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleShopOdds12.grid(row=33, column=7)
    labelDK4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelDK4.grid(row=33, column=8)
    dkCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleShopOdds34.grid(row=33, column=9)
    labelDK5 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    labelDK5.grid(row=33, column=10)
    dkCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleSpaceOdds12.grid(row=33, column=11)
    labelDK6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelDK6.grid(row=33, column=12)
    dkCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleSpaceOdds34.grid(row=33, column=13)

    # Orb Bag Capsule
    icon = create_image_icon(content_frame, "assets/items/orbBagCapsule.png", 34, 1)
    labelOrbBag1 = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    labelOrbBag1.grid(row=34, column=2)
    orbBagCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsulePrice12.grid(row=34, column=3)
    labelOrbBag2 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelOrbBag2.grid(row=34, column=4)
    orbBagCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsulePrice34.grid(row=34, column=5)
    labelOrbBag3 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelOrbBag3.grid(row=34, column=6)
    orbBagCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleShopOdds12.grid(row=34, column=7)
    labelOrbBag4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelOrbBag4.grid(row=34, column=8)
    orbBagCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleShopOdds34.grid(row=34, column=9)
    labelOrbBag5 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    labelOrbBag5.grid(row=34, column=10)
    orbBagCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleSpaceOdds12.grid(row=34, column=11)
    labelOrbBag6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelOrbBag6.grid(row=34, column=12)
    orbBagCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleSpaceOdds34.grid(row=34, column=13)

    # Mystery Capsule
    icon = create_image_icon(content_frame, "assets/items/mysteryCapsule.png", 35, 1)
    labelMystery1 = ctk.CTkLabel(master=content_frame, text="  Cost\n  1st / 2nd  ", font=("Arial", 14))
    labelMystery1.grid(row=35, column=2)
    mysteryCapsulePrice12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsulePrice12.grid(row=35, column=3)
    labelMystery2 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelMystery2.grid(row=35, column=4)
    mysteryCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsulePrice34.grid(row=35, column=5)
    labelMystery3 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelMystery3.grid(row=35, column=6)
    mysteryCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleShopOdds12.grid(row=35, column=7)
    labelMystery4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelMystery4.grid(row=35, column=8)
    mysteryCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleShopOdds34.grid(row=35, column=9)
    labelMystery5 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    labelMystery5.grid(row=35, column=10)
    mysteryCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleSpaceOdds12.grid(row=35, column=11)
    labelMystery6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelMystery6.grid(row=35, column=12)
    mysteryCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleSpaceOdds34.grid(row=35, column=13)

    global hide_custom
    hide_custom = False
    
    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: itemsEvent_mp7(
        mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34,
        mushroomCapsuleSpaceOdds12, mushroomCapsuleSpaceOdds34,
        goldenMushroomCapsulePrice12, goldenMushroomCapsulePrice34, 
        goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, 
        goldenMushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds34,
        slowMushroomCapsulePrice12, slowMushroomCapsulePrice34, 
        slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, 
        slowMushroomCapsuleSpaceOdds12, slowMushroomCapsuleSpaceOdds34,
        metalMushroomCapsulePrice12, metalMushroomCapsulePrice34, 
        metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, 
        metalMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds34,
        flutterCapsulePrice12, flutterCapsulePrice34, 
        flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, 
        flutterCapsuleSpaceOdds12, flutterCapsuleSpaceOdds34,
        cannonCapsulePrice12, cannonCapsulePrice34, 
        cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, 
        cannonCapsuleSpaceOdds12, cannonCapsuleSpaceOdds34,
        snackCapsulePrice12, snackCapsulePrice34, 
        snackCapsuleShopOdds12, snackCapsuleShopOdds34, 
        snackCapsuleSpaceOdds12, snackCapsuleSpaceOdds34,
        lakituCapsulePrice12, lakituCapsulePrice34, 
        lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, 
        lakituCapsuleSpaceOdds12, lakituCapsuleSpaceOdds34,
        hammerBroCapsulePrice12, hammerBroCapsulePrice34, 
        hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, 
        hammerBroCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsulePrice12, piranhaPlantCapsulePrice34, 
        piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, 
        piranhaPlantCapsuleSpaceOdds12, piranhaPlantCapsuleSpaceOdds34,
        spearGuyCapsulePrice12, spearGuyCapsulePrice34, 
        spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, 
        spearGuyCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds34,
        kamekCapsulePrice12, kamekCapsulePrice34, 
        kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, 
        kamekCapsuleSpaceOdds12, kamekCapsuleSpaceOdds34,
        toadyCapsulePrice12, toadyCapsulePrice34, 
        toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, 
        toadyCapsuleSpaceOdds12, toadyCapsuleSpaceOdds34,
        mrBlizzardCapsulePrice12, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleShopOdds12, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleSpaceOdds12, mrBlizzardCapsulePrice34,
        banditCapsulePrice12, banditCapsulePrice34, 
        banditCapsuleShopOdds12, banditCapsuleShopOdds34, 
        banditCapsuleSpaceOdds12, banditCapsuleSpaceOdds34,
        pinkBooCapsulePrice12, pinkBooCapsulePrice34, 
        pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, 
        pinkBooCapsuleSpaceOdds12, pinkBooCapsuleSpaceOdds34,
        spinyCapsulePrice12, spinyCapsulePrice34, 
        spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, 
        spinyCapsuleSpaceOdds12, spinyCapsuleSpaceOdds34,
        zapCapsulePrice12, zapCapsulePrice34, 
        zapCapsuleShopOdds12, zapCapsuleShopOdds34, 
        zapCapsuleSpaceOdds12, zapCapsuleSpaceOdds34,
        tweesterCapsulePrice12, tweesterCapsulePrice34, 
        tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, 
        tweesterCapsuleSpaceOdds12, tweesterCapsuleSpaceOdds34,
        thwompCapsulePrice12, thwompCapsulePrice34, 
        thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, 
        thwompCapsuleSpaceOdds12, thwompCapsuleSpaceOdds34,
        warpCapsulePrice12, warpCapsulePrice34, 
        warpCapsuleShopOdds12, warpCapsuleShopOdds34, 
        warpCapsuleSpaceOdds12, warpCapsuleSpaceOdds34,
        bombCapsulePrice12, bombCapsulePrice34, 
        bombCapsuleShopOdds12, bombCapsuleShopOdds34, 
        bombCapsuleSpaceOdds12, bombCapsuleSpaceOdds34,
        fireballCapsulePrice12, fireballCapsulePrice34, 
        fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, 
        fireballCapsuleSpaceOdds12, fireballCapsuleSpaceOdds34,
        flowerCapsulePrice12, flowerCapsulePrice34, 
        flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, 
        flowerCapsuleSpaceOdds12, flowerCapsuleSpaceOdds34,
        eggCapsulePrice12, eggCapsulePrice34, 
        eggCapsuleShopOdds12, eggCapsuleShopOdds34, 
        eggCapsuleSpaceOdds12, eggCapsuleSpaceOdds34,
        vacuumCapsulePrice12, vacuumCapsulePrice34, 
        vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, 
        vacuumCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds34,
        magicCapsulePrice12, magicCapsulePrice34, 
        magicCapsuleShopOdds12, magicCapsuleShopOdds34, 
        magicCapsuleSpaceOdds12, magicCapsuleSpaceOdds34,
        tripleCapsulePrice12, tripleCapsulePrice34, 
        tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, 
        tripleCapsuleSpaceOdds12, tripleCapsuleSpaceOdds34,
        koopaCapsulePrice12, koopaCapsulePrice34, 
        koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, 
        koopaCapsuleSpaceOdds12, koopaCapsuleSpaceOdds34,
        poisonMushroomPrice34 if hide_custom == False else "0", 
        poisonMushroomPrice12 if hide_custom == False else "0", 
        poisonMushroomShopOdds12 if hide_custom == False else "0", 
        poisonMushroomShopOdds34 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds12 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds34 if hide_custom == False else "0", 
        orbBagCapsulePrice34 if hide_custom == False else "0", 
        orbBagCapsulePrice12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds34 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds12 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds34 if hide_custom == False else "0", 
        mysteryCapsulePrice34 if hide_custom == False else "0", 
        mysteryCapsulePrice12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds34 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds12 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds34 if hide_custom == False else "0", 
        dkCapsulePrice34 if hide_custom == False else "0", 
        dkCapsulePrice12 if hide_custom == False else "0", 
        dkCapsuleShopOdds12 if hide_custom == False else "0", 
        dkCapsuleShopOdds34 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds12 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds34 if hide_custom == False else "0", 
        duelCapsulePrice34 if hide_custom == False else "0", 
        duelCapsulePrice12 if hide_custom == False else "0", 
        duelCapsuleShopOdds12 if hide_custom == False else "0", 
        duelCapsuleShopOdds34 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds12 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds34 if hide_custom == False else "0"
    ), text="Generate Code")
    parseButton.place(x=10, y=800)


    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: savePresetItems7(
        mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34,
        mushroomCapsuleSpaceOdds12, mushroomCapsuleSpaceOdds34,
        goldenMushroomCapsulePrice12, goldenMushroomCapsulePrice34, 
        goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, 
        goldenMushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds34,
        slowMushroomCapsulePrice12, slowMushroomCapsulePrice34, 
        slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, 
        slowMushroomCapsuleSpaceOdds12, slowMushroomCapsuleSpaceOdds34,
        metalMushroomCapsulePrice12, metalMushroomCapsulePrice34, 
        metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, 
        metalMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds34,
        flutterCapsulePrice12, flutterCapsulePrice34, 
        flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, 
        flutterCapsuleSpaceOdds12, flutterCapsuleSpaceOdds34,
        cannonCapsulePrice12, cannonCapsulePrice34, 
        cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, 
        cannonCapsuleSpaceOdds12, cannonCapsuleSpaceOdds34,
        snackCapsulePrice12, snackCapsulePrice34, 
        snackCapsuleShopOdds12, snackCapsuleShopOdds34, 
        snackCapsuleSpaceOdds12, snackCapsuleSpaceOdds34,
        lakituCapsulePrice12, lakituCapsulePrice34, 
        lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, 
        lakituCapsuleSpaceOdds12, lakituCapsuleSpaceOdds34,
        hammerBroCapsulePrice12, hammerBroCapsulePrice34, 
        hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, 
        hammerBroCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsulePrice12, piranhaPlantCapsulePrice34, 
        piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, 
        piranhaPlantCapsuleSpaceOdds12, piranhaPlantCapsuleSpaceOdds34,
        spearGuyCapsulePrice12, spearGuyCapsulePrice34, 
        spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, 
        spearGuyCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds34,
        kamekCapsulePrice12, kamekCapsulePrice34, 
        kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, 
        kamekCapsuleSpaceOdds12, kamekCapsuleSpaceOdds34,
        toadyCapsulePrice12, toadyCapsulePrice34, 
        toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, 
        toadyCapsuleSpaceOdds12, toadyCapsuleSpaceOdds34,
        mrBlizzardCapsulePrice12, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleShopOdds12, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleSpaceOdds12, mrBlizzardCapsulePrice34,
        banditCapsulePrice12, banditCapsulePrice34, 
        banditCapsuleShopOdds12, banditCapsuleShopOdds34, 
        banditCapsuleSpaceOdds12, banditCapsuleSpaceOdds34,
        pinkBooCapsulePrice12, pinkBooCapsulePrice34, 
        pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, 
        pinkBooCapsuleSpaceOdds12, pinkBooCapsuleSpaceOdds34,
        spinyCapsulePrice12, spinyCapsulePrice34, 
        spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, 
        spinyCapsuleSpaceOdds12, spinyCapsuleSpaceOdds34,
        zapCapsulePrice12, zapCapsulePrice34, 
        zapCapsuleShopOdds12, zapCapsuleShopOdds34, 
        zapCapsuleSpaceOdds12, zapCapsuleSpaceOdds34,
        tweesterCapsulePrice12, tweesterCapsulePrice34, 
        tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, 
        tweesterCapsuleSpaceOdds12, tweesterCapsuleSpaceOdds34,
        thwompCapsulePrice12, thwompCapsulePrice34, 
        thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, 
        thwompCapsuleSpaceOdds12, thwompCapsuleSpaceOdds34,
        warpCapsulePrice12, warpCapsulePrice34, 
        warpCapsuleShopOdds12, warpCapsuleShopOdds34, 
        warpCapsuleSpaceOdds12, warpCapsuleSpaceOdds34,
        bombCapsulePrice12, bombCapsulePrice34, 
        bombCapsuleShopOdds12, bombCapsuleShopOdds34, 
        bombCapsuleSpaceOdds12, bombCapsuleSpaceOdds34,
        fireballCapsulePrice12, fireballCapsulePrice34, 
        fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, 
        fireballCapsuleSpaceOdds12, fireballCapsuleSpaceOdds34,
        flowerCapsulePrice12, flowerCapsulePrice34, 
        flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, 
        flowerCapsuleSpaceOdds12, flowerCapsuleSpaceOdds34,
        eggCapsulePrice12, eggCapsulePrice34, 
        eggCapsuleShopOdds12, eggCapsuleShopOdds34, 
        eggCapsuleSpaceOdds12, eggCapsuleSpaceOdds34,
        vacuumCapsulePrice12, vacuumCapsulePrice34, 
        vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, 
        vacuumCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds34,
        magicCapsulePrice12, magicCapsulePrice34, 
        magicCapsuleShopOdds12, magicCapsuleShopOdds34, 
        magicCapsuleSpaceOdds12, magicCapsuleSpaceOdds34,
        tripleCapsulePrice12, tripleCapsulePrice34, 
        tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, 
        tripleCapsuleSpaceOdds12, tripleCapsuleSpaceOdds34,
        koopaCapsulePrice12, koopaCapsulePrice34, 
        koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, 
        koopaCapsuleSpaceOdds12, koopaCapsuleSpaceOdds34,
        poisonMushroomPrice34 if hide_custom == False else "0", 
        poisonMushroomPrice12 if hide_custom == False else "0", 
        poisonMushroomShopOdds12 if hide_custom == False else "0", 
        poisonMushroomShopOdds34 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds12 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds34 if hide_custom == False else "0", 
        orbBagCapsulePrice34 if hide_custom == False else "0", 
        orbBagCapsulePrice12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds34 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds12 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds34 if hide_custom == False else "0", 
        mysteryCapsulePrice34 if hide_custom == False else "0", 
        mysteryCapsulePrice12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds34 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds12 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds34 if hide_custom == False else "0", 
        dkCapsulePrice34 if hide_custom == False else "0", 
        dkCapsulePrice12 if hide_custom == False else "0", 
        dkCapsuleShopOdds12 if hide_custom == False else "0", 
        dkCapsuleShopOdds34 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds12 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds34 if hide_custom == False else "0", 
        duelCapsulePrice34 if hide_custom == False else "0", 
        duelCapsulePrice12 if hide_custom == False else "0", 
        duelCapsuleShopOdds12 if hide_custom == False else "0", 
        duelCapsuleShopOdds34 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds12 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds34 if hide_custom == False else "0"
    ), text="Save Preset")
    parseButton.place(x=160, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: loadPresetItems7(
        hide_custom,
        mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34,
        mushroomCapsuleSpaceOdds12, mushroomCapsuleSpaceOdds34,
        goldenMushroomCapsulePrice12, goldenMushroomCapsulePrice34, 
        goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, 
        goldenMushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds34,
        slowMushroomCapsulePrice12, slowMushroomCapsulePrice34, 
        slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, 
        slowMushroomCapsuleSpaceOdds12, slowMushroomCapsuleSpaceOdds34,
        metalMushroomCapsulePrice12, metalMushroomCapsulePrice34, 
        metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, 
        metalMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds34,
        flutterCapsulePrice12, flutterCapsulePrice34, 
        flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, 
        flutterCapsuleSpaceOdds12, flutterCapsuleSpaceOdds34,
        cannonCapsulePrice12, cannonCapsulePrice34, 
        cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, 
        cannonCapsuleSpaceOdds12, cannonCapsuleSpaceOdds34,
        snackCapsulePrice12, snackCapsulePrice34, 
        snackCapsuleShopOdds12, snackCapsuleShopOdds34, 
        snackCapsuleSpaceOdds12, snackCapsuleSpaceOdds34,
        lakituCapsulePrice12, lakituCapsulePrice34, 
        lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, 
        lakituCapsuleSpaceOdds12, lakituCapsuleSpaceOdds34,
        hammerBroCapsulePrice12, hammerBroCapsulePrice34, 
        hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, 
        hammerBroCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsulePrice12, piranhaPlantCapsulePrice34, 
        piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, 
        piranhaPlantCapsuleSpaceOdds12, piranhaPlantCapsuleSpaceOdds34,
        spearGuyCapsulePrice12, spearGuyCapsulePrice34, 
        spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, 
        spearGuyCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds34,
        kamekCapsulePrice12, kamekCapsulePrice34, 
        kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, 
        kamekCapsuleSpaceOdds12, kamekCapsuleSpaceOdds34,
        toadyCapsulePrice12, toadyCapsulePrice34, 
        toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, 
        toadyCapsuleSpaceOdds12, toadyCapsuleSpaceOdds34,
        mrBlizzardCapsulePrice12, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleShopOdds12, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleSpaceOdds12, mrBlizzardCapsulePrice34,
        banditCapsulePrice12, banditCapsulePrice34, 
        banditCapsuleShopOdds12, banditCapsuleShopOdds34, 
        banditCapsuleSpaceOdds12, banditCapsuleSpaceOdds34,
        pinkBooCapsulePrice12, pinkBooCapsulePrice34, 
        pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, 
        pinkBooCapsuleSpaceOdds12, pinkBooCapsuleSpaceOdds34,
        spinyCapsulePrice12, spinyCapsulePrice34, 
        spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, 
        spinyCapsuleSpaceOdds12, spinyCapsuleSpaceOdds34,
        zapCapsulePrice12, zapCapsulePrice34, 
        zapCapsuleShopOdds12, zapCapsuleShopOdds34, 
        zapCapsuleSpaceOdds12, zapCapsuleSpaceOdds34,
        tweesterCapsulePrice12, tweesterCapsulePrice34, 
        tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, 
        tweesterCapsuleSpaceOdds12, tweesterCapsuleSpaceOdds34,
        thwompCapsulePrice12, thwompCapsulePrice34, 
        thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, 
        thwompCapsuleSpaceOdds12, thwompCapsuleSpaceOdds34,
        warpCapsulePrice12, warpCapsulePrice34, 
        warpCapsuleShopOdds12, warpCapsuleShopOdds34, 
        warpCapsuleSpaceOdds12, warpCapsuleSpaceOdds34,
        bombCapsulePrice12, bombCapsulePrice34, 
        bombCapsuleShopOdds12, bombCapsuleShopOdds34, 
        bombCapsuleSpaceOdds12, bombCapsuleSpaceOdds34,
        fireballCapsulePrice12, fireballCapsulePrice34, 
        fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, 
        fireballCapsuleSpaceOdds12, fireballCapsuleSpaceOdds34,
        flowerCapsulePrice12, flowerCapsulePrice34, 
        flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, 
        flowerCapsuleSpaceOdds12, flowerCapsuleSpaceOdds34,
        eggCapsulePrice12, eggCapsulePrice34, 
        eggCapsuleShopOdds12, eggCapsuleShopOdds34, 
        eggCapsuleSpaceOdds12, eggCapsuleSpaceOdds34,
        vacuumCapsulePrice12, vacuumCapsulePrice34, 
        vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, 
        vacuumCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds34,
        magicCapsulePrice12, magicCapsulePrice34, 
        magicCapsuleShopOdds12, magicCapsuleShopOdds34, 
        magicCapsuleSpaceOdds12, magicCapsuleSpaceOdds34,
        tripleCapsulePrice12, tripleCapsulePrice34, 
        tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, 
        tripleCapsuleSpaceOdds12, tripleCapsuleSpaceOdds34,
        koopaCapsulePrice12, koopaCapsulePrice34, 
        koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, 
        koopaCapsuleSpaceOdds12, koopaCapsuleSpaceOdds34,
        poisonMushroomPrice34 if hide_custom == False else "0", 
        poisonMushroomPrice12 if hide_custom == False else "0", 
        poisonMushroomShopOdds12 if hide_custom == False else "0", 
        poisonMushroomShopOdds34 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds12 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds34 if hide_custom == False else "0", 
        orbBagCapsulePrice34 if hide_custom == False else "0", 
        orbBagCapsulePrice12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds34 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds12 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds34 if hide_custom == False else "0", 
        mysteryCapsulePrice34 if hide_custom == False else "0", 
        mysteryCapsulePrice12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds34 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds12 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds34 if hide_custom == False else "0", 
        dkCapsulePrice34 if hide_custom == False else "0", 
        dkCapsulePrice12 if hide_custom == False else "0", 
        dkCapsuleShopOdds12 if hide_custom == False else "0", 
        dkCapsuleShopOdds34 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds12 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds34 if hide_custom == False else "0", 
        duelCapsulePrice34 if hide_custom == False else "0", 
        duelCapsulePrice12 if hide_custom == False else "0", 
        duelCapsuleShopOdds12 if hide_custom == False else "0", 
        duelCapsuleShopOdds34 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds12 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds34 if hide_custom == False else "0"
    ), text="Load Preset")
    parseButton.place(x=310, y=800)

    #parseButtonSevenFillViaCode = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: fillViaCode7Actions(), text="Fill Via Code")
    #parseButtonSevenFillViaCode.place(x=460, y=800)

    hideCustomSwitch = ctk.CTkSwitch(master=tabview.tab("Orb Mods"), text="Show Custom Orbs")
    hideCustomSwitch.place(x=460, y=800) # x=610

    def toggle_hide_custom():
        global hide_custom
        hide_custom = not hide_custom

        if hide_custom:
            mysteryCapsulePrice12.grid_forget()
            mysteryCapsulePrice34.grid_forget()
            mysteryCapsuleShopOdds12.grid_forget()
            mysteryCapsuleShopOdds34.grid_forget()
            mysteryCapsuleSpaceOdds12.grid_forget()
            mysteryCapsuleSpaceOdds34.grid_forget()
            dkCapsulePrice12.grid_forget()
            dkCapsulePrice34.grid_forget()
            dkCapsuleShopOdds12.grid_forget()
            dkCapsuleShopOdds34.grid_forget()
            dkCapsuleSpaceOdds12.grid_forget()
            dkCapsuleSpaceOdds34.grid_forget()
            orbBagCapsulePrice12.grid_forget()
            orbBagCapsulePrice34.grid_forget()
            orbBagCapsuleShopOdds12.grid_forget()
            orbBagCapsuleShopOdds34.grid_forget()
            orbBagCapsuleSpaceOdds12.grid_forget()
            orbBagCapsuleSpaceOdds34.grid_forget()
            duelCapsulePrice12.grid_forget()
            duelCapsulePrice34.grid_forget()
            duelCapsuleShopOdds12.grid_forget()
            duelCapsuleShopOdds34.grid_forget()
            duelCapsuleSpaceOdds12.grid_forget()
            duelCapsuleSpaceOdds34.grid_forget()
            poisonMushroomPrice12.grid_forget()
            poisonMushroomPrice34.grid_forget()
            poisonMushroomShopOdds12.grid_forget()
            poisonMushroomShopOdds34.grid_forget()
            poisonMushroomSpaceOdds12.grid_forget()
            poisonMushroomSpaceOdds34.grid_forget()
            labelMystery1.grid_forget()
            labelMystery2.grid_forget()
            labelMystery3.grid_forget()
            labelMystery4.grid_forget()
            labelMystery5.grid_forget()
            labelMystery6.grid_forget()
            labelDK1.grid_forget()
            labelDK2.grid_forget()
            labelDK3.grid_forget()
            labelDK4.grid_forget()
            labelDK5.grid_forget()
            labelDK6.grid_forget()
            labelOrbBag1.grid_forget()
            labelOrbBag2.grid_forget()
            labelOrbBag3.grid_forget()
            labelOrbBag4.grid_forget() 
            labelOrbBag5.grid_forget() 
            labelOrbBag6.grid_forget() 
            labelDuel1.grid_forget()
            labelDuel2.grid_forget()
            labelDuel3.grid_forget()
            labelDuel4.grid_forget()
            labelDuel5.grid_forget()
            labelDuel6.grid_forget()
            labelPoison1.grid_forget()
            labelPoison2.grid_forget()
            labelPoison3.grid_forget()
            labelPoison4.grid_forget() 
            labelPoison5.grid_forget() 
            labelPoison6.grid_forget()
            
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "31:1":
                    widget.grid_forget()
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "32:1":
                    widget.grid_forget()
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "33:1":
                    widget.grid_forget()
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "34:1":
                    widget.grid_forget()
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "35:1":
                    widget.grid_forget()
        else:
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "31:1":
                    widget.grid(row=31, column=1)
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "32:1":
                    widget.grid(row=32, column=1)
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "33:1":
                    widget.grid(row=33, column=1)
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "34:1":
                    widget.grid(row=34, column=1)
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "35:1":
                    widget.grid(row=35, column=1)

            # Mystery Capsule
            labelMystery1.grid(row=35, column=2)
            labelMystery2.grid(row=35, column=4)
            labelMystery3.grid(row=35, column=6)  # Fixed from labelMystery2 to labelMystery3
            labelMystery4.grid(row=35, column=8)
            labelMystery5.grid(row=35, column=10)
            labelMystery6.grid(row=35, column=12)

            # Orb Bag Capsule
            labelOrbBag1.grid(row=34, column=2)
            labelOrbBag2.grid(row=34, column=4)
            labelOrbBag3.grid(row=34, column=6)
            labelOrbBag4.grid(row=34, column=8)
            labelOrbBag5.grid(row=34, column=10)
            labelOrbBag6.grid(row=34, column=12)

            # DK Capsule
            labelDK1.grid(row=33, column=2)
            labelDK2.grid(row=33, column=4)  # Fixed from column=2 to column=4
            labelDK3.grid(row=33, column=6)
            labelDK4.grid(row=33, column=8)
            labelDK5.grid(row=33, column=10)
            labelDK6.grid(row=33, column=12)

            # Duel Capsule
            labelDuel1.grid(row=32, column=2)
            labelDuel2.grid(row=32, column=4)
            labelDuel3.grid(row=32, column=6)
            labelDuel4.grid(row=32, column=8)
            labelDuel5.grid(row=32, column=10)
            labelDuel6.grid(row=32, column=12)

            # Poison Mushroom
            labelPoison1.grid(row=31, column=2)
            labelPoison2.grid(row=31, column=4)
            labelPoison3.grid(row=31, column=6)
            labelPoison4.grid(row=31, column=8)
            labelPoison5.grid(row=31, column=10)
            labelPoison6.grid(row=31, column=12)

            # Prices and Odds for the last five items
            mysteryCapsulePrice12.grid(row=35, column=3)
            mysteryCapsulePrice34.grid(row=35, column=5)
            mysteryCapsuleShopOdds12.grid(row=35, column=7)
            mysteryCapsuleShopOdds34.grid(row=35, column=9)
            mysteryCapsuleSpaceOdds12.grid(row=35, column=11)
            mysteryCapsuleSpaceOdds34.grid(row=35, column=13)

            orbBagCapsulePrice12.grid(row=34, column=3)
            orbBagCapsulePrice34.grid(row=34, column=5)
            orbBagCapsuleShopOdds12.grid(row=34, column=7)
            orbBagCapsuleShopOdds34.grid(row=34, column=9)
            orbBagCapsuleSpaceOdds12.grid(row=34, column=11)
            orbBagCapsuleSpaceOdds34.grid(row=34, column=13)

            dkCapsulePrice12.grid(row=33, column=3)
            dkCapsulePrice34.grid(row=33, column=5)
            dkCapsuleShopOdds12.grid(row=33, column=7)
            dkCapsuleShopOdds34.grid(row=33, column=9)
            dkCapsuleSpaceOdds12.grid(row=33, column=11)
            dkCapsuleSpaceOdds34.grid(row=33, column=13)

            duelCapsulePrice12.grid(row=32, column=3)
            duelCapsulePrice34.grid(row=32, column=5)
            duelCapsuleShopOdds12.grid(row=32, column=7)
            duelCapsuleShopOdds34.grid(row=32, column=9)
            duelCapsuleSpaceOdds12.grid(row=32, column=11)
            duelCapsuleSpaceOdds34.grid(row=32, column=13)

            poisonMushroomPrice12.grid(row=31, column=3)
            poisonMushroomPrice34.grid(row=31, column=5)
            poisonMushroomShopOdds12.grid(row=31, column=7)
            poisonMushroomShopOdds34.grid(row=31, column=9)
            poisonMushroomSpaceOdds12.grid(row=31, column=11)
            poisonMushroomSpaceOdds34.grid(row=31, column=13)

    hideCustomSwitch.configure(command=toggle_hide_custom)
    toggle_hide_custom()

    def fillViaCode7Actions():
        top = ctk.CTkToplevel(height=500, width=500)
        top.attributes('-topmost', True)
        top.title("Enter Code")
        
        enterCodeLabel = ctk.CTkLabel(master=top, text="Enter Code")
        enterCodeLabel.place(x=10, y=10)
        
        codeText = ctk.CTkTextbox(master=top, width=200, height=400)
        codeText.place(x=10, y=65)

        submitButton = ctk.CTkButton(master=top, command=lambda: fillViaCode7(hide_custom, top, codeText, mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, dkCapsulePrice7 if hide_custom == False else "0", dkCapsuleWeight7 if hide_custom == False else "0", poisonMushroomPrice7 if hide_custom == False else "0", poisonMushroomWeight7 if hide_custom == False else "0", duelCapsulePrice7 if hide_custom == False else "0", duelCapsuleWeight7 if hide_custom == False else "0", mysteryCapsulePrice7 if hide_custom == False else "0", mysteryCapsuleWeight7 if hide_custom == False else "0", orbBagCapsulePrice7 if hide_custom == False else "0", orbBagCapsuleWeight7 if hide_custom == False else "0"), text="Submit")
        submitButton.place(x=250, y=425)

    spaces7 = ["None", "Invisible Space", "Blue Space", "Red Space", "Happening Space", "Bowser Space", "Duel Space", "DK Space", "Orb Space A", "Orb Space B", "Mic Space"]
    
    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    spaceRep411 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces7)
    spaceRep411.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=0, column=2)

    spaceRep421 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces7)
    spaceRep421.grid(row=0, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot A) ", font=("Arial", 16))
    label.grid(row=0, column=4)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=1, column=0)

    spaceRep412 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces7)
    spaceRep412.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=1, column=2)

    spaceRep422 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces7)
    spaceRep422.grid(row=1, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot B) ", font=("Arial", 16))
    label.grid(row=1, column=4)

    parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=lambda: spaceReplaceEvent_mp7(spaceRep411, spaceRep421, spaceRep412, spaceRep422, spaces7), text="Generate Codes")
    parseButton.place(x=10, y=800)

    items7 = ["None", "Mushroom", "Super Mushroom", "Slow 'Shroom", "Metal Mushroom", "Flutter", "Cannon", "Snack", "Lakitu", "Hammer Bro", "Piranha Plant", "Spear Guy", "Kamek", "Toady", "Mr. Blizzard", "Bandit", "Pink Boo", "Spiny", "Zap", "Tweester", "Thwomp", "Warp Pipe", "Bob-omb", "Fireball", "Flower", "Egg", "Vacuum", "Surprise", "Triple 'Shroom", "Koopa Kid"]
    
    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 1:  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    initalItem71 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem71.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 2:  ", font=("Arial", 16))
    label.grid(row=1, column=0)
    
    initalItem72 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem72.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 3:  ", font=("Arial", 16))
    label.grid(row=2, column=0)

    initalItem73 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem73.grid(row=2, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 4:  ", font=("Arial", 16))
    label.grid(row=3, column=0)

    initalItem74 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem74.grid(row=3, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" (Only if Can Hold 5 Capsules in On)  ", font=("Arial", 16))
    label.grid(row=3, column=2, sticky="w")

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 5:  ", font=("Arial", 16))
    label.grid(row=4, column=0)

    initalItem75 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem75.grid(row=4, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" (Only if Can Hold 5 Capsules in On)  ", font=("Arial", 16))
    label.grid(row=4, column=2, sticky="w")

    parseButton = ctk.CTkButton(master=tabview.tab("Initial Orbs"), command=lambda: initialItemsEvent_mp7(initalItem71, initalItem72, initalItem73, initalItem74, initalItem75, items7), text="Generate Codes")
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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp7(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    spinx_list = ["Do Nothing", "Blue to Red Spaces", "Half Chomp Price", "Coin Equality"]
    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Pyramid Park - Spinx Event is               ", font=("Arial", 16))
    label.grid(row=0, column=0, pady=10)
    comboSpinx = ctk.CTkComboBox(master=tabview.tab("Board Specific"), values=spinx_list)
    comboSpinx.grid(row=0, column=1)
    spinx_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: spinxEvent_mp7(comboSpinx, spinx_list), text="Generate Code")
    spinx_button.place(x=430, y=10)

    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text=" Pyramid Park - Standard Chomp Costs", font=("Arial", 16))
    label.grid(row=1, column=0, pady=10)
    coinAmount = ctk.CTkEntry(master=tabview.tab("Board Specific"), width=100, font=("Arial", 16, "bold"), placeholder_text="10")
    coinAmount.grid(row=1, column=1)
    chomp_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: chompEvent_mp7(coinAmount), text="Generate Code")
    chomp_button.place(x=430, y=57)

    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text=" Pyramid Park - Red Chomp Costs        ", font=("Arial", 16))
    label.grid(row=2, column=0, pady=10)
    coin2Amount = ctk.CTkEntry(master=tabview.tab("Board Specific"), width=100, font=("Arial", 16, "bold"), placeholder_text="10")
    coin2Amount.grid(row=2, column=1)
    chomp_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: redChompEvent_mp7(coin2Amount), text="Generate Code")
    chomp_button.place(x=430, y=104)

    glider_list = ["1 Star (right)", "2 Star (left)", "3 Star (center)"]
    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Windmillville - Flower Glider Goes To  ", font=("Arial", 16))
    label.grid(row=3, column=0, pady=10)
    comboGlider = ctk.CTkComboBox(master=tabview.tab("Board Specific"), values=glider_list)
    comboGlider.grid(row=3, column=1)
    spinx_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: gliderEvent_mp7(comboSpinx, spinx_list), text="Generate Code")
    spinx_button.place(x=430, y=152)

    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Windmillville - Flower Glider Costs       ", font=("Arial", 16))
    label.grid(row=4, column=0, pady=10)
    coin3Amount = ctk.CTkEntry(master=tabview.tab("Board Specific"), width=100, font=("Arial", 16, "bold"), placeholder_text="10")
    coin3Amount.grid(row=4, column=1)
    chomp_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: gliderCostEvent_mp7(coin3Amount), text="Generate Code")
    chomp_button.place(x=430, y=200)

    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Windmillville - Invest Up Too                 ", font=("Arial", 16))
    label.grid(row=5, column=0, pady=10)
    coin4Amount = ctk.CTkEntry(master=tabview.tab("Board Specific"), width=100, font=("Arial", 16, "bold"), placeholder_text="100")
    coin4Amount.grid(row=5, column=1)
    chomp_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: gliderCostEvent_mp7(coin4Amount), text="Generate Code")
    chomp_button.place(x=430, y=252)

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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Battle Minigame"), command=lambda: battleCoins_mp7(fiveCoins, tenCoins, twentyCoins, thirtyCoins, fiftyCoins), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    stars7 = ["None", "Blue Star", "Red Star", "Character Space Star", "Happening Star", "Duel Star", "Mic Star", "Bowser Star", "DK Star", "Minigame Star", "Coin Star", "Star Star", "Orb Star", "Shopping Star", "Running Star"]
    
    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Minigame Star with:  ", font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w")

    star1 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star1.grid(row=0, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Orb Star with:  ", font=("Arial", 16))
    label.grid(row=1, column=0, sticky="w")

    star2 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star2.grid(row=1, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Happening Star with:  ", font=("Arial", 16))
    label.grid(row=2, column=0, sticky="w")

    star3 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star3.grid(row=2, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Red Star with:  ", font=("Arial", 16))
    label.grid(row=3, column=0, sticky="w")

    star4 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star4.grid(row=3, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Running Star with:  ", font=("Arial", 16))
    label.grid(row=4, column=0, sticky="w")

    star5 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star5.grid(row=4, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Shopping Star with:  ", font=("Arial", 16))
    label.grid(row=5, column=0, sticky="w")

    star6 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star6.grid(row=5, column=1, pady=10)

    parseButton = ctk.CTkButton(master=tabview.tab("Bonus Star Replacement"), command=lambda: customBonusStarEvent_mp7(star1, star2, star3, star4, star5, star6, stars7), text="Generate Codes")
    parseButton.place(x=10, y=800)

    return frame
    