# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty1_coins import *
from events.marioParty1_mgreplace import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_1_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=752, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.set("Coins Mods")

    # Function to create an entry field and checkbox
    def create_entry_and_checkbox(tab, row, icon_path, label_text, color, checkbox_text):
        create_image_icon(tab, icon_path, row, 1)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=2, pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"))
        entry.grid(row=row, column=3)
        label1 = ctk.CTkLabel(master=tab, text=" Coins on a " + color + " Space. ", font=("Arial", 16))
        label1.grid(row=row, column=4)
        checkbox = ctk.CTkCheckBox(master=tab, text=checkbox_text, width=16, checkbox_width=16, checkbox_height=16)
        checkbox.grid(row=row, column=5, padx=10, pady=10)
        return entry, checkbox

    # Create entry fields and checkboxes for Coins Mods tab
    blue_entry, blue_checkbox = create_entry_and_checkbox(tabview.tab("Coins Mods"), 1, "assets/eventTags/blueSpace.png", " Gain  ", "Blue", "Double the coins on Last 5")
    red_entry, red_checkbox = create_entry_and_checkbox(tabview.tab("Coins Mods"), 2, "assets/eventTags/redSpace.png", " Lose  ", "Red", "Double the coins on Last 5")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp1(blue_entry, blue_checkbox, red_entry, red_checkbox), text="Generate Codes")
    parse_coins_button.place(x=10, y=660)

    # List of minigame names
    minigames_list = ["Memory Match", "Slot Machine", "Buried Treasure", "Treasure Divers", "Shell Game", "Slot Car Derby 1", "Hot Bob-omb", "Slot Car Derby 2", "Pipe Maze", "Ghost Guess", "Musical Mushroom", "Pedal Power", "Crazy Cutter", "Face Lift", "Whack-a-Plant", "Bash 'n' Cash", "Bowl Over", "Ground Pound", "Balloon Burst", "Coin Block Blitz", "Coin Block Bash", "Skateboard Scamper", "Box Mountain Mayhem", "Platform Peril", "Teetering Towers", "Mushroom Mix-Up", "Bumper Ball Maze 1", "Grab Bag", "Bobsled Run", "Bumper Balls", "TightRope Treachery", "Knock Block Tower", "Tipsy Tourney", "Bombs Away", "Crane Game", "Bumper Ball Maze 2", "Mario Bandstand", "Desert Dash", "Shy Guy Says", "Limbo Dance", "Bombsketball", "Cast Aways", "Key-pa-Way", "Running of the Bulb", "Hot Rope Jump", "Handcar Havoc", "Deep Sea Divers", "Piranha's Pursuit", "Tug o' War", "Paddle Battle", "Bumper Ball Maze 3", "Coin Shower Flower", "Hammer Drop"]

    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp1(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=640)
    return frame