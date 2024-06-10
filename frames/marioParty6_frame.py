# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty6_bonusStarReplace import *
from events.marioParty6_coins import *
from events.marioParty6_initialItems import *
from events.marioParty6_mgreplace import *
from events.marioParty6_items import *
from events.marioParty6_handicap import *
from events.marioParty6_spaceReplace import *

# Import custom tkinter module as ctk
import customtkinter as ctk
from CTkToolTip import *

# Function to create the main interface for Mario Party 1
def create_mario_party_6_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=752, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Orb Mods")
    tabview.add("Space Replacement")
    tabview.add("Initial Orbs")
    tabview.add("Star Handicaps")
    tabview.add("Bonus Star Replacement")
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
    character_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/characterSpace.png", " Gain  ", " Coins on your own Character Space.")
    mgWin_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/miniGame.png", " Gain  ", " Coins when winning a Minigame.")
    
    star_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star at a Star Space and when using Flutter.")
    star_entryTooltip = CTkToolTip(star_entry, message="Works on Treetop, Garage, Castaway, and Clockwork.")
    
    pinkBooCoins_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/pinkBooCoins.png", " Costs ", " Coins to steal Coins.")
    pinkBooMin_entry = create_entry(tabview.tab("Coins Mods"), 7, "assets/eventTags/pinkBooCoins.png", " Steal ", " Mininum when stealing Coins.")
    pinkBooStar_entry = create_entry(tabview.tab("Coins Mods"), 8, "assets/eventTags/pinkBooStars.png", " Costs ", " Coins to steal a Star.")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp6(blue_entry, red_entry, character_entry, mgWin_entry, star_entry, pinkBooCoins_entry, pinkBooMin_entry, pinkBooStar_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=660)

    # List of minigame names
    minigames_list = ["Smashdance", "Odd Card Out", "Freeze Frame", "What Goes Up...", "Granite Getaway", "Circuit Maximus", "Catch You Letter", "Snow Whirled", "Daft Rafts", "Tricky Tires", "Treasure Trawlers", "Memory Lane", "Mowtown", "Cannonball Fun", "Note to Self", "Same is Lame", "Light Up My Night", "Lift Leapers", "Blooper Scooper", "Trap Ease Artist", "Pokey Punch-out", "Money Belt", "Cash Flow", "Cog Jog", "Sink or Swim", "Snow Brawl", "Ball Dozers", "Surge and Destroy", "Pop Star", "Stage Fright", "Conveyor Bolt", "Crate and Peril", "Ray of Fright", "Dust 'til Dawn", "Garden Grab", "Pixel Perfect", "Slot Trot", "Gondola Glide", "Light Breeze", "Body Builder", "Mole-it!", "Cashapult", "Jump the Gun", "Rocky Road", "Clean Team", "Hyper Sniper", "Insectiride", "Sunday Drivers", "Stamp By Me", "Throw Me a Bone", "Black Hole Boogie", "Full Tilt", "Sumo of Doom-o", "O-Zone", "Pitifall", "Mass Meteor", "Lunar-tics", "T Minus Five", "Asteroad Rage", "Boo'd Off the Stage", "Boonanza!", "Trick or Tree", "Something's Amist", "Wrasslin' Rapids", "Verbal Assault", "Shoot Yer Mouth Off", "Talkie Walkie", "Burnstile", "Word Herd", "Fruit Talktail", "Pit Boss", "Dizzy Rotisserie", "Dark 'n Crispy", "Tally Me Banana", "Banana Shake", "Pier Factor", "Seer Terror", "Block Star", "Lab Brats", "Strawberry Shortfuse", "Control Shtick", "Dunk Bros."]
    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp6(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=640)

    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/mushroomCapsule.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" 5  ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=4)
    mushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleWeight6.grid(row=2, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.   ", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/goldenMushroomCapsule.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    goldenMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice6.grid(row=3, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=4)
    goldenMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleWeight6.grid(row=3, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/slowMushroomCapsule.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    slowMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsulePrice6.grid(row=4, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=4)
    slowMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleWeight6.grid(row=4, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/metalMushroomCapsule.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    metalMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsulePrice6.grid(row=5, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=4)
    metalMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleWeight6.grid(row=5, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/warpCapsule.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    warpPipeCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeCapsulePrice6.grid(row=6, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=4)
    warpPipeCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeCapsuleWeight6.grid(row=6, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/wigglerCapsule.png", 8, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=2)
    flutterCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice6.grid(row=8, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=4)
    flutterCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsuleWeight6.grid(row=8, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/cursedMushroomCapsule.png", 9, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=2)
    cursedMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    cursedMushroomCapsulePrice6.grid(row=9, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=4)
    cursedMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    cursedMushroomCapsuleWeight6.grid(row=9, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/spinyCapsule.png", 10, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=2)
    spinyCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice6.grid(row=10, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=4)
    spinyCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsuleWeight6.grid(row=10, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/goombaCapsule.png", 11, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=2)
    goombaCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goombaCapsulePrice6.grid(row=11, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=4)
    goombaCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goombaCapsuleWeight6.grid(row=11, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/plantCapsule.png", 12, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=2)
    plantCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsulePrice6.grid(row=12, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=4)
    plantCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsuleWeight6.grid(row=12, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=12, column=6)

    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/kamekCapsule.png", 2, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=9)
    kamekCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice6.grid(row=2, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=11)
    kamekCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsuleWeight6.grid(row=2, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=2, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/toadyCapsule.png", 3, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=9)
    toadyCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    toadyCapsulePrice6.grid(row=3, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=11)
    toadyCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    toadyCapsuleWeight6.grid(row=3, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/blizzardCapsule.png", 4, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=9)
    blizzardCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsulePrice6.grid(row=4, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=11)
    blizzardCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsuleWeight6.grid(row=4, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/kleptoCapsule.png", 5, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=9)
    kleptoCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kleptoCapsulePrice6.grid(row=5, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=11)
    kleptoCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kleptoCapsuleWeight6.grid(row=5, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/pinkBooCapsule.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    pinkBooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice6.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    pinkBooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleWeight6.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/podobooCapsule.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    podobooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    podobooCapsulePrice6.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    podobooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    podobooCapsuleWeight6.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/zapCapsule.png", 8, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=9)
    zapCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    zapCapsulePrice6.grid(row=8, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=11)
    zapCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    zapCapsuleWeight6.grid(row=8, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/tweesterCapsule.png", 9, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=9)
    tweesterCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice6.grid(row=9, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=11)
    tweesterCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleWeight6.grid(row=9, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/thwompCapsule.png", 10, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=9)
    thwompCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    thwompCapsulePrice6.grid(row=10, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=11)
    thwompCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    thwompCapsuleWeight6.grid(row=10, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=13)
    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/bulletBillCapsule.png", 11, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=9)
    bulletBillCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bulletBillCapsulePrice6.grid(row=11, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=11)
    bulletBillCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bulletBillCapsuleWeight6.grid(row=11, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/bombCapsule.png", 12, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=9)
    bombCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice6.grid(row=12, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=11)
    bombCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsuleWeight6.grid(row=12, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=12, column=13)

    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=14)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/paraTroopaCapsule.png", 2, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=16)
    paraTroopaCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    paraTroopaCapsulePrice6.grid(row=2, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=18)
    paraTroopaCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    paraTroopaCapsuleWeight6.grid(row=2, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/snackCapsule.png", 3, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=16)
    snackCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    snackCapsulePrice6.grid(row=3, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=18)
    snackCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    snackCapsuleWeight6.grid(row=3, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/gaddlightCapsule.png", 4, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=16)
    gaddLightCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    gaddLightCapsulePrice6.grid(row=4, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=18)
    gaddLightCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    gaddLightCapsuleWeight6.grid(row=4, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=20)


    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: itemsEvent_mp6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6, pinkBooCapsuleWeight6, chanceTimeCapsulePrice6, chanceTimeCapsuleWeight6, bowserCapsulePrice6, bowserCapsuleWeight6, dkCapsulePrice6, dkCapsuleWeight6, duelCapsulePrice6, duelCapsuleWeight6), text="Generate Codes")
    parseButton.place(x=10, y=640)

    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: savePresetItems6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6, pinkBooCapsuleWeight6, chanceTimeCapsulePrice6, chanceTimeCapsuleWeight6, bowserCapsulePrice6, bowserCapsuleWeight6, dkCapsulePrice6, dkCapsuleWeight6, duelCapsulePrice6, duelCapsuleWeight6), text="Save Preset")
    parseButton.place(x=160, y=640)

    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: loadPresetItems6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6, pinkBooCapsuleWeight6, chanceTimeCapsulePrice6, chanceTimeCapsuleWeight6, bowserCapsulePrice6, bowserCapsuleWeight6, dkCapsulePrice6, dkCapsuleWeight6, duelCapsulePrice6, duelCapsuleWeight6), text="Load Preset")
    parseButton.place(x=310, y=640)

    pinkBooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    chanceTimeCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    chanceTimeCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    dkCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bowserCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bowserCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    duelCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    
# Function to toggle the visibility of custom orbs' grids
    def toggle_orbs_visibility(state):
        global custom_orb_widgets
        if state.get() == "on":
            # Show custom orbs
            custom_orb_widgets = {}

            custom_orb_widgets['pinkBooIcon'] = create_image_icon(tabview.tab("Orb Mods"), "assets/items/pinkBooCapsule.png", 5, 15)
            custom_orb_widgets['pinkBooLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
            custom_orb_widgets['pinkBooLabel'].grid(row=5, column=16)
            custom_orb_widgets['pinkBooCapsulePrice6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['pinkBooCapsulePrice6'].grid(row=5, column=17)
            custom_orb_widgets['pinkBooWeightLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
            custom_orb_widgets['pinkBooWeightLabel'].grid(row=5, column=18)
            custom_orb_widgets['pinkBooCapsuleWeight6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['pinkBooCapsuleWeight6'].grid(row=5, column=19)
            custom_orb_widgets['pinkBooCommonLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
            custom_orb_widgets['pinkBooCommonLabel'].grid(row=5, column=20)

            custom_orb_widgets['chanceIcon'] = create_image_icon(tabview.tab("Orb Mods"), "assets/items/chanceCapsule.png", 6, 15)
            custom_orb_widgets['chanceLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
            custom_orb_widgets['chanceLabel'].grid(row=6, column=16)
            custom_orb_widgets['chanceTimeCapsulePrice6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['chanceTimeCapsulePrice6'].grid(row=6, column=17)
            custom_orb_widgets['chanceWeightLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
            custom_orb_widgets['chanceWeightLabel'].grid(row=6, column=18)
            custom_orb_widgets['chanceTimeCapsuleWeight6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['chanceTimeCapsuleWeight6'].grid(row=6, column=19)
            custom_orb_widgets['chanceCommonLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
            custom_orb_widgets['chanceCommonLabel'].grid(row=6, column=20)

            custom_orb_widgets['dkIcon'] = create_image_icon(tabview.tab("Orb Mods"), "assets/items/dkCapsule.png", 8, 15)
            custom_orb_widgets['dkLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
            custom_orb_widgets['dkLabel'].grid(row=8, column=16)
            custom_orb_widgets['dkCapsulePrice6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['dkCapsulePrice6'].grid(row=8, column=17)
            custom_orb_widgets['dkWeightLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
            custom_orb_widgets['dkWeightLabel'].grid(row=8, column=18)
            custom_orb_widgets['dkCapsuleWeight6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['dkCapsuleWeight6'].grid(row=8, column=19)
            custom_orb_widgets['dkCommonLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
            custom_orb_widgets['dkCommonLabel'].grid(row=8, column=20)

            custom_orb_widgets['bowserIcon'] = create_image_icon(tabview.tab("Orb Mods"), "assets/items/bowserCapsule.png", 9, 15)
            custom_orb_widgets['bowserLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
            custom_orb_widgets['bowserLabel'].grid(row=9, column=16)
            custom_orb_widgets['bowserCapsulePrice6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['bowserCapsulePrice6'].grid(row=9, column=17)
            custom_orb_widgets['bowserWeightLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
            custom_orb_widgets['bowserWeightLabel'].grid(row=9, column=18)
            custom_orb_widgets['bowserCapsuleWeight6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['bowserCapsuleWeight6'].grid(row=9, column=19)
            custom_orb_widgets['bowserCommonLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
            custom_orb_widgets['bowserCommonLabel'].grid(row=9, column=20)

            custom_orb_widgets['duelIcon'] = create_image_icon(tabview.tab("Orb Mods"), "assets/items/duelCapsule.png", 10, 15)
            custom_orb_widgets['duelLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
            custom_orb_widgets['duelLabel'].grid(row=10, column=16)
            custom_orb_widgets['duelCapsulePrice6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['duelCapsulePrice6'].grid(row=10, column=17)
            custom_orb_widgets['duelWeightLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
            custom_orb_widgets['duelWeightLabel'].grid(row=10, column=18)
            custom_orb_widgets['duelCapsuleWeight6'] = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
            custom_orb_widgets['duelCapsuleWeight6'].grid(row=10, column=19)
            custom_orb_widgets['duelCommonLabel'] = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
            custom_orb_widgets['duelCommonLabel'].grid(row=10, column=20)

        elif state.get() == "off":
            # Hide custom orbs
            for widget in custom_orb_widgets.values():
                if widget is not None and hasattr(widget, 'grid_remove'):
                    widget.grid_remove()

    # Add the switch to the interface
    toggle_orbs_switch = ctk.CTkSwitch(master=tabview.tab("Orb Mods"), text="Show Custom Orbs", command=lambda: toggle_orbs_visibility(toggle_orbs_switch), onvalue="on", offvalue="off")
    toggle_orbs_switch.place(x=10, y=600)
    
    spaces6 = ["None", "Invisible Space", "Blue Space", "Red Space", "Happening Space", "Chance Time Space", "Duel Space", "Bowser/DK Space", "Orb Space"]
    
    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    spaceRep411 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces6)
    spaceRep411.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=0, column=2)

    spaceRep421 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces6)
    spaceRep421.grid(row=0, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot A) ", font=("Arial", 16))
    label.grid(row=0, column=4)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=1, column=0)

    spaceRep412 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces6)
    spaceRep412.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=1, column=2)

    spaceRep422 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces6)
    spaceRep422.grid(row=1, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot B) ", font=("Arial", 16))
    label.grid(row=1, column=4)

    parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=lambda: spaceReplaceEvent_mp6(spaceRep411, spaceRep412, spaceRep421, spaceRep422, spaces6), text="Generate Codes")
    parseButton.place(x=10, y=640)

    items6 = ["None", "Mushroom", "Golden Mushroom", "Sluggish 'Shroom", "Metal Mushroom", "Bullet Bill", "Warp Pipe", "Flutter", "Cursed Mushroom", "Spiny", "Goomba", "Piranha Plant", "Klepto", "Toady", "Kamek", "Mr. Blizzard", "Podoboo", "Zap", "Tweester", "Thwomp", "Bob-omb", "Paratroopa", "Snack", "Boo-away", "Duel", "Miracle", "Bowser", "Donkey Kong", "Pink Boo"]
    
    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 1:  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    initalItem41 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items6)
    initalItem41.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 2:  ", font=("Arial", 16))
    label.grid(row=1, column=0)

    initalItem42 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items6)
    initalItem42.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 3:  ", font=("Arial", 16))
    label.grid(row=2, column=0)

    initalItem43 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items6)
    initalItem43.grid(row=2, column=1)

    parseButton = ctk.CTkButton(master=tabview.tab("Initial Orbs"), command=lambda: initialItemsEvent_mp6(initalItem41, initalItem42, initalItem43, items6), text="Generate Codes")
    parseButton.place(x=10, y=640)


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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp6(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=640)

    stars6 = ["None", "Blue Star", "Red Star", "Character Space Star", "Happening Star", "Duel Star", "Chance Time Star", "Bowser Star", "DK Star", "Minigame Star", "Current Coins Star", "Coin Star", "Star Star", "Orb Star"]
    
    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Minigame Star with:  ", font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w")

    star1 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star1.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Orb Star with:  ", font=("Arial", 16))
    label.grid(row=1, column=0, sticky="w")

    star2 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star2.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Happening Star with:  ", font=("Arial", 16))
    label.grid(row=2, column=0, sticky="w")

    star3 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star3.grid(row=2, column=1)

    parseButton = ctk.CTkButton(master=tabview.tab("Bonus Star Replacement"), command=lambda: customBonusStarEvent_mp6(star1, star2, star3, stars6), text="Generate Codes")
    parseButton.place(x=10, y=640)

    return frame
    