# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty8_coins import *
from events.marioParty8_mgreplace import *

from CTkToolTip import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_8_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=752, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
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
    mgWin_entryTT = CTkToolTip(mgWin_entry, message="Some minigames may be broken. Please report if so.")

    star_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star.")
    star_entryTT = CTkToolTip(mgWin_entry, message="Works on DK's, Goomba's, King Boo's and Shy Guy's.")

    bitsize_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/bitsizeCandy.png", " Gain ", " Coins when Bitsized.")
    bowlo_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/bowloCandy.png", " Lose ", " Coins when Bowloed.")
    hotel_entry = create_entry(tabview.tab("Coins Mods"), 7, "assets/eventTags/hotel.png", " Max ", " coins.")
    hotel_entryTooltip = CTkToolTip(hotel_entry, message="Max Coin Value is 255")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp8(blue_entry, red_entry, mgWin_entry, star_entry, bitsize_entry, hotel_entry, bowlo_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=660)

    # List of minigame names
    minigames_list = ["Speedy Graffiti", "Swing Kings", "Water Ski Spree", "Punch-a-Bunch", "Crank to Rank", "At the Chomp Wash", "Mosh-Pit Playroom", "Mario Matrix", "Hammer de Pokari", "Grabby Giridion", "Lava or Leave 'Em", "Kartastrophe", "Ribbon Game", "Aim of the Game", "Rudder Madness", "Gun the Runner", "Grabbin' Gold", "Power Trip", "Bob-ombs Away", "Swervin' Skies", "Picture Perfect", "Snow Way Out", "Thrash 'n' Crash", "Chump Rope", "Sick and Twisted", "Bumper Balloons", "Rowed to Victory", "Winner or Dinner", "Paint Misbehavin'", "Sugar Rush", "King of the Thrill", "Shake It Up", "Lean, Mean Ravine", "Boo-ting Gallery", "Crops 'n' Robbers", "In the Nick of Time", "Cut from the Team", "Snipe for the Picking", "Saucer Swarm", "Glacial Meltdown", "Attention Grabber", "Blazing Lassos", "Wing and a Scare", "Lob to Rob", "Pumper Cars", "Cosmic Slalom", "Lava Lobbers", "Loco Motives", "Specter Inspector", "Frozen Assets", "Breakneck Building", "Surf's Way Up", "Bull Riding", "Balancing Act", "Ion the Prize", "You're the Bob-omb", "Scooter Pursuit", "Cardiators", "Rotation Station", "Eyebrawl", "Table Menace", "Flagging Rights", "Trial by Tile", "Star Carnival Bowling", "Puzzle Pillars", "Canyon Cruisers", "Settle It in Court", "Moped Mayhem", "Flip the Chimp", "Pour to Score", "Fruit Picker", "Stampede", "Superstar Showdown", "Alpine Assault", "Treacherous Tightrope"]    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp8(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=650)
    
    return frame
    