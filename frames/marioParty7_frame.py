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

    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/mushroomCapsule.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" 5  ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=4)
    mushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleWeight7.grid(row=2, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.   ", font=("Arial", 16))
    label.grid(row=2, column=6)
    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/goldenMushroomCapsule.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    goldenMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice7.grid(row=3, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=4)
    goldenMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleWeight7.grid(row=3, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/slowMushroomCapsule.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    slowMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsulePrice7.grid(row=4, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=4)
    slowMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleWeight7.grid(row=4, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/metalMushroomCapsule.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    metalMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsulePrice7.grid(row=5, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=4)
    metalMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleWeight7.grid(row=5, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/wigglerCapsule.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    flutterCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice7.grid(row=6, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=4)
    flutterCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsuleWeight7.grid(row=6, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/cannonCapsule.png", 7, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=7, column=2)
    cannonCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    cannonCapsulePrice7.grid(row=7, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=7, column=4)
    cannonCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    cannonCapsuleWeight7.grid(row=7, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=7, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/snackCapsule7.png", 8, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=2)
    snackCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    snackCapsulePrice7.grid(row=8, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=4)
    snackCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    snackCapsuleWeight7.grid(row=8, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/lakituCapsule.png", 9, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=2)
    lakituCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    lakituCapsulePrice7.grid(row=9, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=4)
    lakituCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    lakituCapsuleWeight7.grid(row=9, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/hammerBroCapsule.png", 10, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=2)
    hammerBroCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    hammerBroCapsulePrice7.grid(row=10, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=4)
    hammerBroCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleWeight7.grid(row=10, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/spearCapsule.png", 11, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=2)
    spearCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    spearCapsulePrice7.grid(row=11, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=4)
    spearCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    spearCapsuleWeight7.grid(row=11, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/plantCapsule.png", 12, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=2)
    plantCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsulePrice7.grid(row=12, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=4)
    plantCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsuleWeight7.grid(row=12, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=12, column=6)

    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/koopaCapsule.png", 13, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=13, column=2)
    koopaCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    koopaCapsulePrice7.grid(row=13, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=13, column=4)
    koopaCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    koopaCapsuleWeight7.grid(row=13, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=13, column=6)

    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=7)
    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/kamekCapsule.png", 2, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=9)
    kamekCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice7.grid(row=2, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=11)
    kamekCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsuleWeight7.grid(row=2, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=2, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/toadyCapsule.png", 3, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=9)
    toadyCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    toadyCapsulePrice7.grid(row=3, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=11)
    toadyCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    toadyCapsuleWeight7.grid(row=3, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/blizzardCapsule.png", 4, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=9)
    blizzardCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsulePrice7.grid(row=4, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=11)
    blizzardCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsuleWeight7.grid(row=4, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/banditCapsule.png", 5, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=9)
    banditCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    banditCapsulePrice7.grid(row=5, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=11)
    banditCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    banditCapsuleWeight7.grid(row=5, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/pinkBooCapsule.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    pinkBooCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice7.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    pinkBooCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleWeight7.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/spinyCapsule.png", 7, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=7, column=9)
    spinyCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice7.grid(row=7, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=7, column=11)
    spinyCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsuleWeight7.grid(row=7, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=7, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/zapCapsule.png", 8, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=9)
    zapCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    zapCapsulePrice7.grid(row=8, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=11)
    zapCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    zapCapsuleWeight7.grid(row=8, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/tweesterCapsule.png", 9, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=9)
    tweesterCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice7.grid(row=9, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=11)
    tweesterCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleWeight7.grid(row=9, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/thwompCapsule7.png", 10, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=9)
    thwompCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    thwompCapsulePrice7.grid(row=10, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=11)
    thwompCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    thwompCapsuleWeight7.grid(row=10, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=13)
    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/warpCapsule.png", 11, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=9)
    warpCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    warpCapsulePrice7.grid(row=11, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=11)
    warpCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    warpCapsuleWeight7.grid(row=11, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/bombCapsule7.png", 12, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=9)
    bombCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice7.grid(row=12, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=11)
    bombCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsuleWeight7.grid(row=12, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=12, column=13)

    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=14)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/fireballCapsule.png", 2, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=16)
    fireballCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    fireballCapsulePrice7.grid(row=2, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=18)
    fireballCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    fireballCapsuleWeight7.grid(row=2, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/flowerCapsule.png", 3, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=16)
    flowerCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    flowerCapsulePrice7.grid(row=3, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=18)
    flowerCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    flowerCapsuleWeight7.grid(row=3, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/eggCapsule.png", 4, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=16)
    eggCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    eggCapsulePrice7.grid(row=4, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=18)
    eggCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    eggCapsuleWeight7.grid(row=4, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/vacuumCapsule.png", 5, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=16)
    vacuumCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    vacuumCapsulePrice7.grid(row=5, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=18)
    vacuumCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleWeight7.grid(row=5, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/magicCapsule.png", 6, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=16)
    magicCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    magicCapsulePrice7.grid(row=6, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=18)
    magicCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    magicCapsuleWeight7.grid(row=6, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/tripleCapsule.png", 7, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=7, column=16)
    tripleCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    tripleCapsulePrice7.grid(row=7, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=7, column=18)
    tripleCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    tripleCapsuleWeight7.grid(row=7, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=7, column=20)
    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/cursedMushroomCapsule7.png", 9, 15)
    labelPoison1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    poisonMushroomPrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelPoison2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    poisonMushroomWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelPoison3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))

    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/duelCapsule.png", 10, 15)
    labelDuel1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    duelCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelDuel2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    duelCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelDuel3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))

    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/dkCapsule.png", 11, 15)
    labelDK1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    dkCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelDK2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    dkCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelDK3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))

    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/orbBagCapsule.png", 12, 15)
    labelOrbBag1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    orbBagCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelOrbBag2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    orbBagCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelOrbBag3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/mysteryCapsule.png", 8, 15)
    labelMystery1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    mysteryCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelMystery2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    mysteryCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    labelMystery3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))

    global hide_custom
    hide_custom = False
    
    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: itemsEvent_mp7(mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, poisonMushroomWeight7 if hide_custom == False else "0", poisonMushroomPrice7 if hide_custom == False else "0", orbBagCapsuleWeight7 if hide_custom == False else "0", orbBagCapsulePrice7 if hide_custom == False else "0", mysteryCapsuleWeight7 if hide_custom == False else "0", mysteryCapsulePrice7 if hide_custom == False else "0", dkCapsuleWeight7 if hide_custom == False else "0", dkCapsulePrice7 if hide_custom == False else "0", duelCapsuleWeight7 if hide_custom == False else "0", duelCapsulePrice7  if hide_custom == False else "0"), text="Generate Codes")
    parseButton.place(x=10, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: savePresetItems7(mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, poisonMushroomWeight7 if hide_custom == False else "0", poisonMushroomPrice7 if hide_custom == False else "0", orbBagCapsuleWeight7 if hide_custom == False else "0", orbBagCapsulePrice7 if hide_custom == False else "0", mysteryCapsuleWeight7 if hide_custom == False else "0", mysteryCapsulePrice7 if hide_custom == False else "0", dkCapsuleWeight7 if hide_custom == False else "0", dkCapsulePrice7 if hide_custom == False else "0", duelCapsuleWeight7 if hide_custom == False else "0", duelCapsulePrice7  if hide_custom == False else "0"), text="Save Preset")
    parseButton.place(x=160, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: loadPresetItems7(hide_custom, mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, poisonMushroomWeight7 if hide_custom == False else "0", poisonMushroomPrice7 if hide_custom == False else "0", orbBagCapsuleWeight7 if hide_custom == False else "0", orbBagCapsulePrice7 if hide_custom == False else "0", mysteryCapsuleWeight7 if hide_custom == False else "0", mysteryCapsulePrice7 if hide_custom == False else "0", dkCapsuleWeight7 if hide_custom == False else "0", dkCapsulePrice7 if hide_custom == False else "0", duelCapsuleWeight7 if hide_custom == False else "0", duelCapsulePrice7  if hide_custom == False else "0"), text="Load Preset")
    parseButton.place(x=310, y=800)

    parseButtonSevenFillViaCode = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: fillViaCode7Actions(), text="Fill Via Code")
    parseButtonSevenFillViaCode.place(x=460, y=800)

    hideCustomSwitch = ctk.CTkSwitch(master=tabview.tab("Orb Mods"), text="Show Custom Orbs")
    hideCustomSwitch.place(x=610, y=800)

    def toggle_hide_custom():
        global hide_custom
        hide_custom = not hide_custom

        if hide_custom:
            mysteryCapsulePrice7.grid_forget()
            mysteryCapsuleWeight7.grid_forget()
            dkCapsulePrice7.grid_forget()
            dkCapsuleWeight7.grid_forget()
            orbBagCapsulePrice7.grid_forget()
            orbBagCapsuleWeight7.grid_forget()
            duelCapsulePrice7.grid_forget()
            duelCapsuleWeight7.grid_forget()
            poisonMushroomPrice7.grid_forget()
            poisonMushroomWeight7.grid_forget()
            labelMystery1.grid_forget()
            labelMystery2.grid_forget()
            labelMystery3.grid_forget()
            labelDK1.grid_forget()
            labelDK2.grid_forget()
            labelDK3.grid_forget()
            labelOrbBag1.grid_forget()
            labelOrbBag2.grid_forget()
            labelOrbBag3.grid_forget()
            labelDuel1.grid_forget()
            labelDuel2.grid_forget()
            labelDuel3.grid_forget()
            labelPoison1.grid_forget()
            labelPoison2.grid_forget()
            labelPoison3.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "10:15":
                    widget.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "9:15":
                    widget.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "8:15":
                    widget.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "11:15":
                    widget.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "12:15":
                    widget.grid_forget()
        else:
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "8:15":
                    widget.grid(row=8, column=15)
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "9:15":
                    widget.grid(row=9, column=15)
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "10:15":
                    widget.grid(row=10, column=15)
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "11:15":
                    widget.grid(row=11, column=15)
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "12:15":
                    widget.grid(row=12, column=15)
            mysteryCapsulePrice7.grid(row=12, column=17)
            mysteryCapsuleWeight7.grid(row=12, column=19)
            orbBagCapsulePrice7.grid(row=11, column=17)
            orbBagCapsuleWeight7.grid(row=11, column=19)
            dkCapsulePrice7.grid(row=10, column=17)
            dkCapsuleWeight7.grid(row=10, column=19)
            duelCapsulePrice7.grid(row=9, column=17)
            duelCapsuleWeight7.grid(row=9, column=19)
            poisonMushroomPrice7.grid(row=8, column=17)
            poisonMushroomWeight7.grid(row=8, column=19)
            labelMystery1.grid(row=12, column=16)
            labelMystery2.grid(row=12, column=18)
            labelMystery3.grid(row=12, column=20)
            labelOrbBag1.grid(row=11, column=16)
            labelOrbBag2.grid(row=11, column=18)
            labelOrbBag3.grid(row=11, column=20)
            labelDK1.grid(row=10, column=16)
            labelDK2.grid(row=10, column=18)
            labelDK3.grid(row=10, column=20)
            labelDuel1.grid(row=9, column=16)
            labelDuel2.grid(row=9, column=18)
            labelDuel3.grid(row=9, column=20)
            labelPoison1.grid(row=8, column=16)
            labelPoison2.grid(row=8, column=18)
            labelPoison3.grid(row=8, column=20)

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
    