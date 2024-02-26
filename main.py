# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

import tkinter
import tkinter.messagebox
import customtkinter
import version
import tkinter as tk
import pyperclip
import tkinter.filedialog
import os
import subprocess
import threading
import shutil
import time
import csv

from CTkToolTip import *

from functions import *
from credits import *

from codes.marioparty1 import *
from codes.marioparty2 import *
from codes.marioparty3 import *
from codes.marioparty4 import *
from codes.marioparty5 import *
from codes.marioparty6 import *
from codes.marioparty7 import *
from codes.marioparty8_rev1 import *
from codes.marioparty8_rev2 import *

if sys.platform == "win32":
    from get_system_color import *

customtkinter.set_appearance_mode("System")

global sysColor
sysColor = None

try:
    with open('settings.json', 'r') as json_file:
        settings = json.load(json_file)
        if 'color' in settings:
            saved_color = settings['color']
            sysColor = saved_color
            if sysColor == "#system":
                sysColor, sysColorAlt = system_color()
            else:
                hexColorAlt = hex_to_rgb(sysColor)
                sysColorAlt1 = hexColorAlt[0]
                sysColorAlt2 = hexColorAlt[1]
                sysColorAlt3 = hexColorAlt[2]
                sysColorAlt = darken_color(sysColorAlt1, sysColorAlt2, sysColorAlt3, 0.75)
                sysColorAlt = "#{0:02x}{1:02x}{2:02x}".format(int(sysColorAlt[0]), int(sysColorAlt[1]), int(sysColorAlt[2]))
        else:
            print("No color found in settings.")
            sysColor, sysColorAlt = system_color()

except FileNotFoundError:
    print("Settings file not found. Creating a new settings file.")
    # Create a new settings file
    with open('settings.json', 'w') as json_file:
        json.dump({}, json_file)
        sysColor, sysColorAlt = system_color()
    
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("Mario Party: Toolkit")
        self.geometry(f"{1330}x{780}")

        check_for_updates()

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(11, weight=1)

        logo_label = create_banner(self.sidebar_frame, "assets/mptoolkit.png", 0, 0)

        self.mario_party_1_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 1", command=self.mp1ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_1_button.grid(row=1, column=0, padx=20, pady=10)

        self.mario_party_2_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 2", command=self.mp2ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_2_button.grid(row=2, column=0, padx=20, pady=10)

        self.mario_party_3_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 3", command=self.mp3ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_3_button.grid(row=3, column=0, padx=20, pady=10)

        self.mario_party_4_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 4", command=self.mp4ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_4_button.grid(row=4, column=0, padx=20, pady=10)

        self.mario_party_5_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 5", command=self.mp5ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_5_button.grid(row=5, column=0, padx=20, pady=10)
        
        self.mario_party_6_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 6", command=self.mp6ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_6_button.grid(row=6, column=0, padx=20, pady=10)

        self.mario_party_7_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 7", command=self.mp7ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_7_button.grid(row=7, column=0, padx=20, pady=10)

        self.mario_party_8_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 8 (Rev. 1)", command=self.mp8ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_8_button.grid(row=8, column=0, padx=20, pady=10)

        self.mario_party_82_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 8 (Rev. 2)", command=self.mp82ButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.mario_party_82_button.grid(row=9, column=0, padx=20, pady=10)

        self.codeInjector_button = customtkinter.CTkButton(self.sidebar_frame, text="Code Injector", command=self.codeInjectorButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.codeInjector_button.grid(row=10, column=0, padx=20, pady=10)

        self.credits_button = customtkinter.CTkButton(self.sidebar_frame, text="Credits", command=self.creditsButtonEvent, fg_color=sysColor, hover_color=sysColorAlt)
        self.credits_button.grid(row=12, column=0, padx=20, pady=10)
        
        self.version_label = customtkinter.CTkLabel(self.sidebar_frame, text=f"Version: {version.appVersion}", anchor="w", font=("Arial", 14, "bold"))
        self.version_label.grid(row=14, column=0, padx=20, pady=(10, 0))

        self.current_game_frame = None  # To keep track of the currently displayed game frame
    
        # set default values
        self.mario_party_1_button.configure(state="disabled")
        self.current_game_frame = self.create_mp1_frame()
        self.current_game_frame.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), rowspan=3, sticky="nsew")


    def reset_game_frames(self):
        # Reset the main frame to remove any existing game-specific widgets
        if self.current_game_frame:
            self.current_game_frame.destroy()

    def create_game_frame(self, game_name):
        # Create a new game frame based on the selected game_name
        self.reset_game_frames()

        if game_name == "Mario Party 1":
            self.current_game_frame = self.create_mp1_frame()
        elif game_name == "Mario Party 2":
            self.current_game_frame = self.create_mp2_frame()
        elif game_name == "Mario Party 3":
            self.current_game_frame = self.create_mp3_frame()
        elif game_name == "Mario Party 4":
            self.current_game_frame = self.create_mp4_frame()
        elif game_name == "Mario Party 5":
            self.current_game_frame = self.create_mp5_frame()
        elif game_name == "Mario Party 6":
            self.current_game_frame = self.create_mp6_frame()
        elif game_name == "Mario Party 7":
            self.current_game_frame = self.create_mp7_frame()
        elif game_name == "Mario Party 8 (Rev. 1)":
            self.current_game_frame = self.create_mp8_frame()
        elif game_name == "Mario Party 8 (Rev. 2)":
            self.current_game_frame = self.create_mp82_frame()
        elif game_name == "Code Injector":
            self.current_game_frame = self.create_codes_frame()
        elif game_name == "Credits":
            self.current_game_frame = self.create_credits_frame()
        self.current_game_frame.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), rowspan=3, sticky="nsew")

    def create_codes_frame(self):        
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
    
        # Create button for file selection
        select_file_button = ctk.CTkButton(master=frame, text="Select ROM", command=lambda: select_file(self.file_label), fg_color=sysColor, hover_color=sysColorAlt)
        select_file_button.place(x=10, y=10)

        # Create label for file selection
        self.file_label = ctk.CTkLabel(master=frame, text="path/to/rom/file")
        self.file_label.place(x=160, y=10)

        file_label2 = ctk.CTkLabel(master=frame, text="Codes:")
        file_label2.place(x=10, y=60)

        self.cheatCodeEntry = ctk.CTkTextbox(master=frame, width=200, height=500)
        self.cheatCodeEntry.place(x=10, y=65)

        injectCodes = ctk.CTkButton(master=frame, command=self.injectCodesFunc, text="Inject Codes", fg_color=sysColor, hover_color=sysColorAlt)
        injectCodes.place(x=10, y=590)
    
        return frame

    def create_mp1_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"), segmented_button_selected_color=sysColor, segmented_button_selected_hover_color=sysColorAlt)
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.add("Minigame Replacement")
        tabview.set("Coins Mods")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconOne = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Give  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountOne = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountOne.grid(row=1, column=3)
        label1 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label1.grid(row=1, column=4)
        self.blueSpaceTickboxOne = ctk.CTkCheckBox(master=tabview.tab("Coins Mods"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16, fg_color=sysColor, hover_color=sysColorAlt)
        self.blueSpaceTickboxOne.grid(row=1, column=5, padx=10, pady=10)
        
        # Create red space icon and entry, and tickbox
        redSpaceIconOne = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountOne = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountOne.grid(row=2, column=3)
        redSpaceLabel1 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel1.grid(row=2, column=4)
        self.redSpaceTickboxOne = ctk.CTkCheckBox(master=tabview.tab("Coins Mods"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16, fg_color=sysColor, hover_color=sysColorAlt)
        self.redSpaceTickboxOne.grid(row=2, column=5, padx=10, pady=10)

        parseButtonOne = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonOne, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonOne.place(x=10, y=560)

        self.minigame1 = ["Memory Match", "Slot Machine", "Buried Treasure", "Treasure Divers", "Shell Game", "Slot Car Derby 1", "Hot Bob-omb", "Slot Car Derby 2", "Pipe Maze", "Ghost Guess", "Musical Mushroom", "Pedal Power", "Crazy Cutter", "Face Lift", "Whack-a-Plant", "Bash 'n' Cash", "Bowl Over", "Ground Pound", "Balloon Burst", "Coin Block Blitz", "Coin Block Bash", "Skateboard Scamper", "Box Mountain Mayhem", "Platform Peril", "Teetering Towers", "Mushroom Mix-Up", "Bumper Ball Maze 1", "Grab Bag", "Bobsled Run", "Bumper Balls", "TightRope Treachery", "Knock Block Tower", "Tipsy Tourney", "Bombs Away", "Crane Game", "Bumper Ball Maze 2", "Mario Bandstand", "Desert Dash", "Shy Guy Says", "Limbo Dance", "Bombsketball", "Cast Aways", "Key-pa-Way", "Running of the Bulb", "Hot Rope Jump", "Handcar Havoc", "Deep Sea Divers", "Piranha's Pursuit", "Tug o' War", "Paddle Battle", "Bumper Ball Maze 3", "Coin Shower Flower", "Hammer Drop"]
        
        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.comboboxMingames11 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame1)
        self.comboboxMingames11.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.comboboxMingames12 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame1)
        self.comboboxMingames12.grid(row=0, column=3)

        parseButtonOne = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=self.minigameReplaceOne, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonOne.place(x=10, y=560)

        return frame

    def create_mp2_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"), segmented_button_selected_color=sysColor, segmented_button_selected_hover_color=sysColorAlt)
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.add("Minigame Replacement")
        tabview.set("Coins Mods")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconTwo = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Give  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountTwo = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountTwo.grid(row=1, column=3)
        label2 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label2.grid(row=1, column=4)
        self.blueSpaceTickboxTwo = ctk.CTkCheckBox(master=tabview.tab("Coins Mods"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16, fg_color=sysColor, hover_color=sysColorAlt)
        self.blueSpaceTickboxTwo.grid(row=1, column=5, padx=10, pady=10)

        # Create red space icon and entry, and tickbox
        redSpaceIconTwo = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountTwo = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountTwo.grid(row=2, column=3)
        redSpaceLabel2 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel2.grid(row=2, column=4)
        self.redSpaceTickboxTwo = ctk.CTkCheckBox(master=tabview.tab("Coins Mods"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16, fg_color=sysColor, hover_color=sysColorAlt)
        self.redSpaceTickboxTwo.grid(row=2, column=5, padx=10, pady=10)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonTwo, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonTwo.place(x=10, y=560)
        
        self.minigame2 = ["BOWSER Slots", "Roll Out the Barrels", "Coffin Congestion", "Hammer Slammer", "Give Me a Brake!", "Mallet-Go Round", "Grab Bag", "Bumper Balloon Cars", "Rakin' 'em In", "Day at the Races", "Face Lift", "Crazy Cutters", "Hot BOB-OMB", "Bowl Over", "Rainbow Run", "Crane Game", "Move to the Music", "BOB-OMB Barrage", "Look Away", "Shock Drop or Roll", "Lights Out", "Filet Relay", "Archer-ival", "TOAD Bandstand", "Bobsled Run", "Handcar Havoc", "Balloon Burst", "Sky Pilots", "Speed Hockey", "Cake Factory", "Dungeon Dash", "Magnet Carta", "Lava Tile Isle", "Hot Rope Jump", "Shell Shocked", "TOAD in the Box", "Mecha-Marathon", "Roll Call", "Abandon Ship", "Platform Peril", "Totem Pole Pound", "Bumper Balls", "Bombs Away", "Tipsy Tourney", "Honeycomb Havoc", "Hexagon Heat", "Skateboard Scamper", "Slot Car Derby", "Shy Guy Says", "Sneak 'n' Snore", "Driver's Ed", "BOWSER's Big Blast", "Looney Lumberjacks", "Torpedo Targets", "Destruction Duet", "Dizzy Dancing", "Tile Driver", "Quicksand Cache", "Deep Sea Salvage"]

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.comboboxMingames21 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame2)
        self.comboboxMingames21.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.comboboxMingames22 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame2)
        self.comboboxMingames22.grid(row=0, column=3)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=self.minigameReplaceTwo, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonTwo.place(x=10, y=560)

        return frame

    def create_mp3_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"), segmented_button_selected_color=sysColor, segmented_button_selected_hover_color=sysColorAlt)
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.add("Minigame Replacement")
        tabview.set("Coins Mods")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconThree = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Give  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountThree = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountThree.grid(row=1, column=3)
        label3 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label3.grid(row=1, column=4, sticky="w")
        self.blueSpaceTickboxThree = ctk.CTkCheckBox(master=tabview.tab("Coins Mods"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16, fg_color=sysColor, hover_color=sysColorAlt)
        self.blueSpaceTickboxThree.grid(row=1, column=5, padx=10, pady=10)

        # Create red space icon and entry, and tickbox
        redSpaceIconThree = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountThree = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountThree.grid(row=2, column=3)
        redSpaceLabel3 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel3.grid(row=2, column=4, sticky="w")
        self.redSpaceTickboxThree = ctk.CTkCheckBox(master=tabview.tab("Coins Mods"), text="Double the coins on Last 5", width=16, checkbox_width=16, checkbox_height=16, fg_color=sysColor, hover_color=sysColorAlt)
        self.redSpaceTickboxThree.grid(row=2, column=5, padx=10, pady=10)

        # Create Star space icon and entry
        starSpaceIconThree = create_image_icon(tabview.tab("Coins Mods"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountThree = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountThree.grid(row=3, column=3)
        starSpaceLabel3 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when purchasing a Star.", font=("Arial", 16))
        starSpaceLabel3.grid(row=3, column=4, sticky="w")

        # Create koopa bank space icon and entry
        koopaBankIconThree = create_image_icon(tabview.tab("Coins Mods"), "assets/koopaBank3.png", 4, 1)
        koopaBankLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        koopaBankLabel.grid(row=4, column=2)
        self.koopaBankAmountThree = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.koopaBankAmountThree.grid(row=4, column=3)
        koopaBankLabel3 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins to Koopa Bank.", font=("Arial", 16))
        koopaBankLabel3.grid(row=4, column=4, sticky="w")

        parseButtonThree = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonThree, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonThree.place(x=10, y=560)

        self.minigame3 = ["Thwomp Pull", "River Raiders", "Tidal Toss", "Eatsa Pizza", "Baby Bowser Broadside", "Pump, Pump and Away", "Hyper Hydrants", "Picking Panic", "Treadmill Grill", "Toadstoll Titan", "Aces High", "Bounce 'n' Trounce", "Ice Rink Risk", "Locked Out", "Chip Shot Challenge", "Parasol Plummet", "Messy Memory", "Picture Imperfect", "Mario's Puzzle Party", "The Beat Goes On", "M. P. I. Q.", "Curtain Call", "Water Whirled", "Frigid Bridges", "Awful Tower", "Cheep Cheep Chase", "Pipe Cleaners", "Snowball Summit", "All Fired Up", "Stacked Deck", "Three Door Monty", "Rockin' Raceway", "Merry-Go-Chomp", "Slap Down", "Storm Chasers", "Eye Sore", "Vine With Me", "Popgun Pick-Off", "End of the Line", "Bowser Toss", "Baby Bowser Bonkers", "Motor Rooter", "Silly Screws", "Crowd Cover", "Tick Tock Hop", "Fowl Play", "Mecha-Marathon", "Hey, Batter, Batter!", "Bobbing Bow-loons", "Dorrie Dip", "Swinging with Sharks", "Swing 'n' Swipe", "Stardust Battle", "Game Guy's Roulette", "Game Guy's Lucky 7", "Game Guy's Magic Boxes", "Game Guy's Sweet Surprise", "Dizzy Dinghies", "Mario's Puzzle Party Pro"]

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.comboboxMingames31 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame3)
        self.comboboxMingames31.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.comboboxMingames32 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame3)
        self.comboboxMingames32.grid(row=0, column=3)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=self.minigameReplaceThree, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonTwo.place(x=10, y=560)
        return frame


    def create_mp4_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"), segmented_button_selected_color=sysColor, segmented_button_selected_hover_color=sysColorAlt)
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.add("Item Mods")
        tabview.add("Battle Game Mods")
        tabview.add("Minigame Replacement")
        tabview.add("Initial Items")
        tabview.add("Space Replacement")
        tabview.set("Coins Mods")

        # Create faire square grid icon and entry
        warningLabel = ctk.CTkLabel(master=tabview.tab("Battle Game Mods"), text="Battle Mini-Games Can Take These 5 Amounts. ", font=("Arial", 16, "bold"))
        warningLabel.place(x=350, y=5)
        icon = create_image_icon(tabview.tab("Battle Game Mods"), "assets/transparent.png", 3, 1)
        icon = create_image_icon(tabview.tab("Battle Game Mods"), "assets/miniGame.png", 4, 1)
        icon = create_image_icon(tabview.tab("Battle Game Mods"), "assets/miniGame.png", 5, 1)
        icon = create_image_icon(tabview.tab("Battle Game Mods"), "assets/miniGame.png", 6, 1)
        icon = create_image_icon(tabview.tab("Battle Game Mods"), "assets/miniGame.png", 7, 1)
        icon = create_image_icon(tabview.tab("Battle Game Mods"), "assets/miniGame.png", 8, 1)
        label = ctk.CTkLabel(master=tabview.tab("Battle Game Mods"), text="   ", font=("Arial", 16))
        label.grid(row=4, column=2)
        self.battle41 = ctk.CTkEntry(master=tabview.tab("Battle Game Mods"), width=48, font=("Arial", 16, "bold"))
        self.battle41.grid(row=4, column=3)
        self.battle42 = ctk.CTkEntry(master=tabview.tab("Battle Game Mods"), width=48, font=("Arial", 16, "bold"))
        self.battle42.grid(row=5, column=3)
        self.battle43 = ctk.CTkEntry(master=tabview.tab("Battle Game Mods"), width=48, font=("Arial", 16, "bold"))
        self.battle43.grid(row=6, column=3)
        self.battle44 = ctk.CTkEntry(master=tabview.tab("Battle Game Mods"), width=48, font=("Arial", 16, "bold"))
        self.battle44.grid(row=7, column=3)
        self.battle45 = ctk.CTkEntry(master=tabview.tab("Battle Game Mods"), width=48, font=("Arial", 16, "bold"))
        self.battle45.grid(row=8, column=3)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/miniMushroom.png", 2, 1)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=2)
        self.miniPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniPrice4.grid(row=2, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=4)
        self.miniWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniWeight4.grid(row=2, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=2, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/megaMushroom.png", 3, 1)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=2)
        self.megaPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.megaPrice4.grid(row=3, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=4)
        self.megaWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.megaWeight4.grid(row=3, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/superMiniMushroom.png", 4, 1)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=2)
        self.superMiniPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.superMiniPrice4.grid(row=4, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=4)
        self.superMiniWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.superMiniWeight4.grid(row=4, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/superMegaMushroom.png", 5, 1)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=2)
        self.superMegaPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.superMegaPrice4.grid(row=5, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=4)
        self.superMegaWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.superMegaWeight4.grid(row=5, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/miniMegaHammer.png", 6, 1)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=2)
        self.miniMegaHammerPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniMegaHammerPrice4.grid(row=6, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=4)
        self.miniMegaHammerWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniMegaHammerWeight4.grid(row=6, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=6)


        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text="", font=("Arial", 16))
        label.grid(row=2, column=7)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/sparkySticker.png", 2, 8)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=9)
        self.sparkyStickerPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.sparkyStickerPrice4.grid(row=2, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=11)
        self.sparkyStickerWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.sparkyStickerWeight4.grid(row=2, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=2, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/warpPipe.png", 3, 8)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=9)
        self.warpPipePrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.warpPipePrice4.grid(row=3, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=11)
        self.warpPipeWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.warpPipeWeight4.grid(row=3, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/swapCard.png", 4, 8)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=9)
        self.swapCardPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.swapCardPrice4.grid(row=4, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=11)
        self.swapCardWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.swapCardWeight4.grid(row=4, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/bowserSuit4.png", 5, 8)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=9)
        self.bowserSuitPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.bowserSuitPrice4.grid(row=5, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=11)
        self.bowserSuitWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.bowserSuitWeight4.grid(row=5, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/gaddlight.png", 6, 8)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=9)
        self.gaddlightPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.gaddlightPrice4.grid(row=6, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=11)
        self.gaddlightWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.gaddlightWeight4.grid(row=6, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/magicLamp4.png", 2, 15)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=16)
        self.magicLampPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.magicLampPrice4.grid(row=2, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=18)
        self.magicLampWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.magicLampWeight4.grid(row=2, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=2, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/crystalBall.png", 3, 15)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=16)
        self.crystalBallPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.crystalBallPrice4.grid(row=3, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=18)
        self.crystalBallWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.crystalBallWeight4.grid(row=3, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/chompCall.png", 4, 15)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=16)
        self.chompCallPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.chompCallPrice4.grid(row=4, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=18)
        self.chompCallWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.chompCallWeight4.grid(row=4, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Item Mods"), "assets/itemBag4.png", 5, 15)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=16)
        self.itemBagPrice4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.itemBagPrice4.grid(row=5, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=18)
        self.itemBagWeight4 = ctk.CTkEntry(master=tabview.tab("Item Mods"), width=48, font=("Arial", 16, "bold"))
        self.itemBagWeight4.grid(row=5, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Item Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=20)

        # Create blue space icon and entry
        blueSpaceIconFour = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Give  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountFour.grid(row=1, column=3)
        label4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label4.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconFour = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountFour.grid(row=2, column=3)
        redSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel4.grid(row=2, column=4, sticky="w")

        # Create minigame icon and entry
        minigameIconFour = create_image_icon(tabview.tab("Coins Mods"), "assets/miniGame.png", 3, 1)
        minigameLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        minigameLabel.grid(row=3, column=2)
        self.miniGameAmountFour = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniGameAmountFour.grid(row=3, column=3)
        minigameSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when winning a Mini-Game.", font=("Arial", 16))
        minigameSpaceLabel4.grid(row=3, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconFour = create_image_icon(tabview.tab("Coins Mods"), "assets/starSpace.png", 4, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=4, column=2)
        self.starSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountFour.grid(row=4, column=3)
        starSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when purchasing a Star and using a Magic Lamp.", font=("Arial", 16))
        starSpaceLabel4.grid(row=4, column=4, sticky="w")

        # Create squish space icon and entry
        starSpaceIconFour = create_image_icon(tabview.tab("Coins Mods"), "assets/megaMushroom.png", 5, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        starSpaceLabel.grid(row=5, column=2)
        self.squishAmountFour = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.squishAmountFour.grid(row=5, column=3)
        starSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when squishing a player.", font=("Arial", 16))
        starSpaceLabel4.grid(row=5, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconFour = create_image_icon(tabview.tab("Coins Mods"), "assets/booHouseStars.png", 6, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=6, column=2)
        self.booSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.booSpaceAmountFour.grid(row=6, column=3)
        starSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when stealing a Star.", font=("Arial", 16))
        starSpaceLabel4.grid(row=6, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconFour = create_image_icon(tabview.tab("Coins Mods"), "assets/booHouseCoins.png", 7, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=7, column=2)
        self.booSpaceCoinsAmountFour = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.booSpaceCoinsAmountFour.grid(row=7, column=3)
        starSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when stealing coins.", font=("Arial", 16))
        starSpaceLabel4.grid(row=7, column=4, sticky="w")

        # Create star space icon and entry
        lotterySpaceIconFour = create_image_icon(tabview.tab("Coins Mods"), "assets/lottery4.png", 8, 1)
        lotterySpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        lotterySpaceLabel.grid(row=8, column=2)
        self.lotterySpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.lotterySpaceAmountFour.grid(row=8, column=3)
        lotterySpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when playing the Lottery.", font=("Arial", 16))
        lotterySpaceLabel4.grid(row=8, column=4, sticky="w")

        parseButtonFour = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonFour, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFour.place(x=10, y=560)

        parseButtonFour = ctk.CTkButton(master=tabview.tab("Item Mods"), command=self.actionSpaceButtonFourItem, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFour.place(x=10, y=560)

        parseButtonFour = ctk.CTkButton(master=tabview.tab("Item Mods"), command=self.savePresetItems4, text="Save Preset", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFour.place(x=160, y=560)

        parseButtonFour = ctk.CTkButton(master=tabview.tab("Item Mods"), command=self.loadPresetItems4, text="Load Preset", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFour.place(x=310, y=560)

        parseButtonFour = ctk.CTkButton(master=tabview.tab("Battle Game Mods"), command=self.actionBattle4, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFour.place(x=10, y=560)

        warningLabel = ctk.CTkLabel(master=tabview.tab("Item Mods"), text="There must be at least 5 items with a value higher than 0 and the Mega or Mini should be worth 5. ", font=("Arial", 16, "bold"))
        warningLabel.place(x=160, y=270)

        self.minigame4 = ["Manta Rings", "Slime Time", "Booksquirm", "Trace Race", "Mario Medley", "Avalanche!", "Domination", "Paratrooper Plunge", "Toad's Quick Draw", "Three Throw", "Photo Finish", "Mr. Blizzard's Brigade", "Bob-omb Breakers", "Long Claw of the Law", "Stamp Out!", "Candlelight Fright", "Makin' Waves", "Hide and Go BOOM!", "Tree Stomp", "Fish n' Drips", "Hop or Pop", "Money Belts", "GOOOOOOAL!!", "Blame it on the Crane", "The Great Deflate", "Revers-a-Bomb", "Right Oar Left?", "Cliffhangers", "Team Treasure Trek", "Pair-a-sailing", "Order Up", "Dungeon Duos", "Beach Volley Folley", "Cheep Cheep Sweep", "Darts of Doom", "Fruits of Doom", "Balloon of Doom", "Chain Chomp Fever", "Paths of Peril", "Bowser's Bigger Blast", "Butterfly Blitz", "Barrel Baron", "Mario Speedwagons", "Bowser Bop", "Mystic Match 'Em", "Archaeologuess", "Goomba's Chip Flip", "Kareening Koopas", "The Final Battle!", "Rumble Fishing", "Take a Breather", "Bowser Wrestling", "Panels of Doom"]
        
        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.comboboxMingames41 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame4)
        self.comboboxMingames41.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.comboboxMingames42 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame4)
        self.comboboxMingames42.grid(row=0, column=3)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=self.minigameReplaceFour, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonTwo.place(x=10, y=560)

        self.items4 = ["None", "Mini Mushroom", "Mega Mushroom", "Super Mini Mushroom", "Super Mega Mushroom", "Mini-Mega Hammer", "Sparky Sticker", "Warp Pipe", "Swap Card", "Bowser Suit", "Gaddlight", "Magic Lamp", "Boo's Crystal Ball", "Chomp Call", "Item Bag"]
        
        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 1:  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.initalItem41 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items4)
        self.initalItem41.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 2:  ", font=("Arial", 16))
        label.grid(row=1, column=0)

        self.initalItem42 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items4)
        self.initalItem42.grid(row=1, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 3:  ", font=("Arial", 16))
        label.grid(row=2, column=0)

        self.initalItem43 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items4)
        self.initalItem43.grid(row=2, column=1)

        parseButton = ctk.CTkButton(master=tabview.tab("Initial Items"), command=self.initalItems4, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton.place(x=10, y=560)

        self.spaces4 = ["None", "Invisible Space", "Blue Space", "Red Space", "Bowser Space", "Mushroom Space", "Battle Space", "Happening Space", "Chance Time Space", "Spring Space"]

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.spaceRep411 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces4)
        self.spaceRep411.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.spaceRep421 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces4)
        self.spaceRep421.grid(row=0, column=3)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot A) ", font=("Arial", 16))
        label.grid(row=0, column=4)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=1, column=0)

        self.spaceRep412 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces4)
        self.spaceRep412.grid(row=1, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=1, column=2)

        self.spaceRep422 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces4)
        self.spaceRep422.grid(row=1, column=3)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot B) ", font=("Arial", 16))
        label.grid(row=1, column=4)

        parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=self.spaceReplace4, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton.place(x=10, y=560)
        return frame

    def create_mp5_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"), segmented_button_selected_color=sysColor, segmented_button_selected_hover_color=sysColorAlt)
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.add("Capsule Mods")
        tabview.add("Minigame Replacement")
        #tabview.add("Initial Items")
        tabview.add("Other Codes")
        tabview.set("Coins Mods")

        # Create blue space icon and entry
        blueSpaceIconFive = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountFive.grid(row=1, column=3)
        label4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label4.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconFive = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountFive.grid(row=2, column=3)
        redSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel5.grid(row=2, column=4, sticky="w")

        # Create star space icon and entry
        miniGameIconFive = create_image_icon(tabview.tab("Coins Mods"), "assets/miniGame.png", 3, 1)
        miniGameLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        miniGameLabel.grid(row=3, column=2)
        self.miniGameAmountFive = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniGameAmountFive.grid(row=3, column=3)
        miniGameLabel5 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when winning a Mini-Game.", font=("Arial", 16))
        miniGameLabel5.grid(row=3, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconFive = create_image_icon(tabview.tab("Coins Mods"), "assets/starSpace.png", 4, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=4, column=2)
        self.starSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountFive.grid(row=4, column=3)
        starSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when purchasing a Star at a Star Space.", font=("Arial", 16))
        starSpaceLabel5.grid(row=4, column=4, sticky="w")

        # Create wiggler space icon and entry
        wigglerSpaceIconFive = create_image_icon(tabview.tab("Coins Mods"), "assets/wigglerCapsule.png", 5, 1)
        wigglerSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        wigglerSpaceLabel.grid(row=5, column=2)
        self.wigglerSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.wigglerSpaceAmountFive.grid(row=5, column=3)
        wigglerSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins to buy a star via Wiggler.", font=("Arial", 16))
        wigglerSpaceLabel5.grid(row=5, column=4, sticky="w")

        # Create chain chomp space icon and entry
        chompSpaceIconFive = create_image_icon(tabview.tab("Coins Mods"), "assets/chainChomp.png", 6, 1)
        chompSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        chompSpaceLabel.grid(row=6, column=2)
        self.chompSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.chompSpaceAmountFive.grid(row=6, column=3)
        chompSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins to steal a Star.", font=("Arial", 16))
        chompSpaceLabel5.grid(row=6, column=4, sticky="w")

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/mushroomCapsule.png", 2, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=2)
        self.mushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.mushroomCapsulePrice5.grid(row=2, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=4)
        self.mushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.mushroomCapsuleWeight5.grid(row=2, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.   ", font=("Arial", 16))
        label.grid(row=2, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/goldenMushroomCapsule.png", 3, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=2)
        self.goldenMushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.goldenMushroomCapsulePrice5.grid(row=3, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=4)
        self.goldenMushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.goldenMushroomCapsuleWeight5.grid(row=3, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/cursedMushroomCapsule.png", 4, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=2)
        self.cursedMushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.cursedMushroomCapsulePrice5.grid(row=4, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=4)
        self.cursedMushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.cursedMushroomCapsuleWeight5.grid(row=4, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/warpCapsule.png", 5, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=2)
        self.warpPipeCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.warpPipeCapsulePrice5.grid(row=5, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=4)
        self.warpPipeCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.warpPipeCapsuleWeight5.grid(row=5, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/kleptoCapsule.png", 6, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=2)
        self.kleptoCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.kleptoCapsulePrice5.grid(row=6, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=4)
        self.kleptoCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.kleptoCapsuleWeight5.grid(row=6, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/wigglerCapsule.png", 8, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=2)
        self.flutterCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.flutterCapsulePrice5.grid(row=8, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=4)
        self.flutterCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.flutterCapsuleWeight5.grid(row=8, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/podobooCapsule.png", 9, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=2)
        self.podobooCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.podobooCapsulePrice5.grid(row=9, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=4)
        self.podobooCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.podobooCapsuleWeight5.grid(row=9, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/spinyCapsule.png", 10, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=2)
        self.spinyCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.spinyCapsulePrice5.grid(row=10, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=4)
        self.spinyCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.spinyCapsuleWeight5.grid(row=10, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/coinBlockCapsule.png", 11, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=2)
        self.coinBlockCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.coinBlockCapsulePrice5.grid(row=11, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=4)
        self.coinBlockCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.coinBlockCapsuleWeight5.grid(row=11, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/hammerBroCapsule.png", 12, 1)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=12, column=2)
        self.hammerBroCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.hammerBroCapsulePrice5.grid(row=12, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=12, column=4)
        self.hammerBroCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.hammerBroCapsuleWeight5.grid(row=12, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=12, column=6)

        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text="", font=("Arial", 16))
        label.grid(row=2, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/paraTroopaCapsule.png", 2, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=9)
        self.paraTroopaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.paraTroopaCapsulePrice5.grid(row=2, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=11)
        self.paraTroopaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.paraTroopaCapsuleWeight5.grid(row=2, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=2, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/bulletBillCapsule.png", 3, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=9)
        self.bulletBillCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.bulletBillCapsulePrice5.grid(row=3, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=11)
        self.bulletBillCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.bulletBillCapsuleWeight5.grid(row=3, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/blizzardCapsule.png", 4, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=9)
        self.blizzardCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.blizzardCapsulePrice5.grid(row=4, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=11)
        self.blizzardCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.blizzardCapsuleWeight5.grid(row=4, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/kamekCapsule.png", 5, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=9)
        self.kamekCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.kamekCapsulePrice5.grid(row=5, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=11)
        self.kamekCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.kamekCapsuleWeight5.grid(row=5, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/koopaBankCapsule.png", 6, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=9)
        self.koopaBankCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.koopaBankCapsulePrice5.grid(row=6, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=11)
        self.koopaBankCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.koopaBankCapsuleWeight5.grid(row=6, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/goombaCapsule.png", 8, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=9)
        self.goombaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.goombaCapsulePrice5.grid(row=8, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=11)
        self.goombaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.goombaCapsuleWeight5.grid(row=8, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/bombCapsule.png", 9, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=9)
        self.bombCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.bombCapsulePrice5.grid(row=9, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=11)
        self.bombCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.bombCapsuleWeight5.grid(row=9, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/tweesterCapsule.png", 10, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=9)
        self.tweesterCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.tweesterCapsulePrice5.grid(row=10, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=11)
        self.tweesterCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.tweesterCapsuleWeight5.grid(row=10, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/lakituCapsule.png", 11, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=9)
        self.lakituCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.lakituCapsulePrice5.grid(row=11, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=11)
        self.lakituCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.lakituCapsuleWeight5.grid(row=11, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=13)
    
        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/ukikiCapsule.png", 12, 8)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=12, column=9)
        self.ukikiCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.ukikiCapsulePrice5.grid(row=12, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=12, column=11)
        self.ukikiCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.ukikiCapsuleWeight5.grid(row=12, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=12, column=13)

        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text="", font=("Arial", 16))
        label.grid(row=2, column=14)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/miracleCapsule.png", 2, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=16)
        self.miracleCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.miracleCapsulePrice5.grid(row=2, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=18)
        self.miracleCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.miracleCapsuleWeight5.grid(row=2, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=2, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/snackCapsule.png", 3, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=16)
        self.boneCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.boneCapsulePrice5.grid(row=3, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=18)
        self.boneCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.boneCapsuleWeight5.grid(row=3, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/plantCapsule.png", 4, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=16)
        self.plantCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.plantCapsulePrice5.grid(row=4, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=18)
        self.plantCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.plantCapsuleWeight5.grid(row=4, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/chainChompCapsule.png", 5, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=16)
        self.chainChompCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.chainChompCapsulePrice5.grid(row=5, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=18)
        self.chainChompCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.chainChompCapsuleWeight5.grid(row=5, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/chanceCapsule.png", 6, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=16)
        self.chanceCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.chanceCapsulePrice5.grid(row=6, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=18)
        self.chanceCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.chanceCapsuleWeight5.grid(row=6, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/dkCapsule.png", 8, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=16)
        self.dkCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.dkCapsulePrice5.grid(row=8, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=18)
        self.dkCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.dkCapsuleWeight5.grid(row=8, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/bowserCapsule.png", 9, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=16)
        self.bowserCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.bowserCapsulePrice5.grid(row=9, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=18)
        self.bowserCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.bowserCapsuleWeight5.grid(row=9, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/duelCapsule.png", 10, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=16)
        self.duelCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.duelCapsulePrice5.grid(row=10, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=18)
        self.duelCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.duelCapsuleWeight5.grid(row=10, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/toadyCapsule.png", 11, 15)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=16)
        self.magiKoopaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.magiKoopaCapsulePrice5.grid(row=11, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=18)
        self.magiKoopaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
        self.magiKoopaCapsuleWeight5.grid(row=11, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=20)

        # Create Code Checkboxes
        self.checkboxAdvTxt = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Automatically Advance Text Boxes", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxAdvTxt.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxBattleNoStar = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Battle Minigames Don't Affect Mini-Game Star   ", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxBattleNoStar.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxDisableAdv = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Disable Advance on Results", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxDisableAdv.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxBoot = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Faster Boot Time", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxBoot.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxBSpeed = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Increased Board Speed", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxBSpeed.grid(row=4, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxCSpeed = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Increased Capsule Throwing Speed", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxCSpeed.grid(row=5, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxTaunt = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Increased Taunt Capabilities", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxTaunt.grid(row=6, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxTxtDisplay = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Instant Text Display", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxTxtDisplay.grid(row=7, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxShowCtrl = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Show Player Who Paused", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxShowCtrl.grid(row=8, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxUnlockAll = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="QOL - Unlock Everything", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxUnlockAll.grid(row=9, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxBowserNoStealCoins = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Bowser Nightmare - Bowser does not Steal Coins", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxBowserNoStealCoins.grid(row=10, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkbox60RocketShip = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Future Dream - 60 Seconds in Rocket Ship Game", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkbox60RocketShip.grid(row=11, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxFreeTaxi = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Future Dream - Free Taxi Ride", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxFreeTaxi.grid(row=12, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxFreeThwmopWhomp = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Pirate Dream - Free Thwomps & Whomps", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxFreeThwmopWhomp.grid(row=13, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxFreeBridge = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Rainbow Dream - Free Bridge Crossings", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxFreeBridge.grid(row=14, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxDisableHappening = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Sweet Dream - Disable Topmost Happening Space", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxDisableHappening.grid(row=15, column=0, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxAllDK = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="All DK Spaces are Active", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxAllDK.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxCapsulesAny= ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Capsules Can Be Thrown Everywhere", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxCapsulesAny.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxDoubleTurns = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Double the Amount of Turns", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxDoubleTurns.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxCapsulesFinal = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Obtain Capsules on Final Turn", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxCapsulesFinal.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxsameSpaceAlways = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Same Space Duels Always Happen", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxsameSpaceAlways.grid(row=4, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxsameSpaceNever = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Same Space Duels Never Happen", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxsameSpaceNever.grid(row=5, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkbox20Sec = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Beam Team - 20 Second Timer", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkbox20Sec.grid(row=6, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxNoBrick = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Bound of Music - No Bricks", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxNoBrick.grid(row=7, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkbox1Slow = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Curvy Curves - 1 Player is Slower", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkbox1Slow.grid(row=8, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxNoSlow = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Coney Island - No Slow Down", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxNoSlow.grid(row=9, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxFlowers3 = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Flower Shower - All Flowers Worth 3pts", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxFlowers3.grid(row=10, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxNoRocks = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Ground Pound Down - No Rocks Until End", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxNoRocks.grid(row=11, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxLeafDisplay = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Leaf Leap - Leaves Display Quicker", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxLeafDisplay.grid(row=12, column=1, sticky="w", padx=5, pady=5)
        
        # Create Code Checkboxes
        self.checkboxHalvedTime = ctk.CTkCheckBox(master=tabview.tab("Other Codes"), text="Pop Star Piranhas - Halved Time to Pick", font=("Arial", 13), fg_color=sysColor, hover_color=sysColorAlt)
        self.checkboxHalvedTime.grid(row=13, column=1, sticky="w", padx=5, pady=5)
        
        # Default Check Boxes
        self.checkboxDisableAdv.select()
        self.checkboxBoot.select()
        self.checkboxBSpeed.select()
        self.checkboxCSpeed.select()
        self.checkboxTaunt.select()
        self.checkboxTxtDisplay.select()
        self.checkboxShowCtrl.select()
        self.checkboxUnlockAll.select()
        self.checkboxBattleNoStar.select()

        parseButtonFive = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonFive, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFive.place(x=10, y=560)

        parseButtonFiveItems = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=self.actionSpaceButtonFiveCapsule, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFiveItems.place(x=10, y=560)

        parseButtonFiveOther = ctk.CTkButton(master=tabview.tab("Other Codes"), command=self.actionSpaceButtonFiveOther, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFiveOther.place(x=10, y=560)

        parseButtonFive = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=self.savePresetItems5, text="Save Preset", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFive.place(x=160, y=560)

        parseButtonFive = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=self.loadPresetItems5, text="Load Preset", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonFive.place(x=310, y=560)

        self.minigame5 = ["Coney Island", "Ground Pound Down", "Chimp Chase", "Chomp Romp", "Pushy Penguins", "Leaf Leap", "Night Light Fright", "Pop-Star Piranhas", "Mazed & Confused", "Dinger Derby", "Hydrostars", "Later Skater", "Will Flower", "Triple Jump", "Hotel Goomba", "Coin Cache", "Flatiator", "Squared Away", "Mario Mechs", "Revolving Fire", "Clock Stoppers", "Heat Stroke", "Beam Team", "Vicious Vending", "Big Top Drop", "Defuse or Lose", "ID UFO", "Mario Can-Can", "Handy Hoppers", "Berry Basket", "Bus Buffer", "Rumble Ready", "Submarathon", "Manic Mallets", "Astro-Logical", "Bill Blasters", "Tug-o-Dorrie", "Twist 'n' Out", "Lucky Lineup", "Random Ride", "Shock Absorbers", "Countdown Pound", "Whomp Maze", "Shy Guy Showdown", "Button Mashers", "Get a Rope", "Pump 'n' Jump", "Head Waiter", "Blown Away", "Merry Poppings", "Pound Peril", "Piece Out", "Bound of Music", "Wind Wavers", "Sky Survivor", "Cage-in Cookin'", "Rain of Fire", "Scaldin' Cauldron", "Frightmare", "Flower Shower", "Dodge Bomb", "Fish Upon a Star", "Rumble Fumble", "Quilt for Speed", "Tube It or Lose It", "Mathletes", "Fight Cards", "Banana Punch", "Da Vine Climb", "Mass A-peel", "Panic Pinball", "Banking Coins", "Frozen Frenzy", "Curvy Curbs", "Beach Volleyball", "Fish Sticks", "Ice Hockey"]
                
        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.comboboxMingames51 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame5)
        self.comboboxMingames51.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.comboboxMingames52 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame5)
        self.comboboxMingames52.grid(row=0, column=3)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=self.minigameReplaceFive, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonTwo.place(x=10, y=560)

        #self.items5 = ["None", "Mushroom", "Super Mushroom", "Cursed Mushroom", "Warp Pipe", "Klepto", "Bubble", "Wiggler", "Hammer Brother", "Coin Block", "Spiny", "Paratroopa", "Bullet Bill", "Goomba", "Bomomb", "Koopa Bank", "Kamek", "Mr. Blizzard", "Piranha Plant", "Magikoopa", "Ukiki", "Lakitu", "Tweester", "Duel", "Chain Chomp", "Bone", "Bowser", "Chance", "Miracle", "Donkey Kong"]
        
        #label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 1:  ", font=("Arial", 16))
        #label.grid(row=0, column=0)

        #self.initalItem51 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items5)
        #self.initalItem51.grid(row=0, column=1)

        #label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 2:  ", font=("Arial", 16))
        #label.grid(row=1, column=0)

        #self.initalItem52 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items5)
        #self.initalItem52.grid(row=1, column=1)

        #label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 3:  ", font=("Arial", 16))
        #label.grid(row=2, column=0)

        #self.initalItem53 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items5)
        #self.initalItem53.grid(row=2, column=1)

        #parseButton = ctk.CTkButton(master=tabview.tab("Initial Items"), command=self.initalItems5, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        #parseButton.place(x=10, y=560)
        
        # Create boo space icon and entry
        chainChompCoinsSpaceIcon5 = create_image_icon(tabview.tab("Coins Mods"), "assets/chainChomp.png", 7, 1)
        chainChompCoinsSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Steal  ", font=("Arial", 16))
        chainChompCoinsSpaceLabel.grid(row=7, column=2)
        self.chainChompBaseAmountFive = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.chainChompBaseAmountFive.grid(row=7, column=3)
        chainChompCoinsSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" minimum when stealing coins ", font=("Arial", 16))
        chainChompCoinsSpaceLabel5.grid(row=7, column=4, sticky="w")
        return frame

    def create_mp6_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"), segmented_button_selected_color=sysColor, segmented_button_selected_hover_color=sysColorAlt)
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.add("Orb Mods")
        tabview.add("Faire Square Mods")
        tabview.add("Minigame Replacement")
        tabview.add("Initial Items")
        tabview.add("Space Replacement")
        tabview.set("Coins Mods")

        # Create faire square grid icon and entry
        warningLabel = ctk.CTkLabel(master=tabview.tab("Faire Square Mods"), text="Stars Can Cost These 4 Amounts During Nightime in Faire Square. ", font=("Arial", 16, "bold"))
        warningLabel.place(x=260, y=5)
        icon = create_image_icon(tabview.tab("Faire Square Mods"), "assets/transparent.png", 3, 1)
        icon = create_image_icon(tabview.tab("Faire Square Mods"), "assets/starSpace.png", 4, 1)
        icon = create_image_icon(tabview.tab("Faire Square Mods"), "assets/starSpace.png", 5, 1)
        icon = create_image_icon(tabview.tab("Faire Square Mods"), "assets/starSpace.png", 6, 1)
        icon = create_image_icon(tabview.tab("Faire Square Mods"), "assets/starSpace.png", 7, 1)
        label = ctk.CTkLabel(master=tabview.tab("Faire Square Mods"), text="   ", font=("Arial", 16))
        label.grid(row=4, column=2)
        self.faireSquare1 = ctk.CTkEntry(master=tabview.tab("Faire Square Mods"), width=48, font=("Arial", 16, "bold"))
        self.faireSquare1.grid(row=4, column=3)
        self.faireSquare2 = ctk.CTkEntry(master=tabview.tab("Faire Square Mods"), width=48, font=("Arial", 16, "bold"))
        self.faireSquare2.grid(row=5, column=3)
        self.faireSquare3 = ctk.CTkEntry(master=tabview.tab("Faire Square Mods"), width=48, font=("Arial", 16, "bold"))
        self.faireSquare3.grid(row=6, column=3)
        self.faireSquare4 = ctk.CTkEntry(master=tabview.tab("Faire Square Mods"), width=48, font=("Arial", 16, "bold"))
        self.faireSquare4.grid(row=7, column=3)

        # Create blue space icon and entry
        icon = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Give  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountSix.grid(row=1, column=3)
        label4 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label4.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconSix = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountSix.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel6.grid(row=2, column=4, sticky="w")

        # Create character space icon and entry
        characterSpaceIconSix = create_image_icon(tabview.tab("Coins Mods"), "assets/characterSpace.png", 3, 1)
        characterSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        characterSpaceLabel.grid(row=3, column=2)
        self.characterSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.characterSpaceAmountSix.grid(row=3, column=3)
        characterSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when the character lands on their own Character Space.", font=("Arial", 16))
        characterSpaceLabel6.grid(row=3, column=4, sticky="w")

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/mushroomCapsule.png", 2, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=2)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" 5  ", font=("Arial", 24, "bold"))
        label.grid(row=2, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=4)
        self.mushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.mushroomCapsuleWeight6.grid(row=2, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.   ", font=("Arial", 16))
        label.grid(row=2, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/goldenMushroomCapsule.png", 3, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=2)
        self.goldenMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.goldenMushroomCapsulePrice6.grid(row=3, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=4)
        self.goldenMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.goldenMushroomCapsuleWeight6.grid(row=3, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/slowMushroomCapsule.png", 4, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=2)
        self.slowMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.slowMushroomCapsulePrice6.grid(row=4, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=4)
        self.slowMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.slowMushroomCapsuleWeight6.grid(row=4, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/metalMushroomCapsule.png", 5, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=2)
        self.metalMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.metalMushroomCapsulePrice6.grid(row=5, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=4)
        self.metalMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.metalMushroomCapsuleWeight6.grid(row=5, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/warpCapsule.png", 6, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=2)
        self.warpPipeCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.warpPipeCapsulePrice6.grid(row=6, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=4)
        self.warpPipeCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.warpPipeCapsuleWeight6.grid(row=6, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/wigglerCapsule.png", 8, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=2)
        self.flutterCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.flutterCapsulePrice6.grid(row=8, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=4)
        self.flutterCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.flutterCapsuleWeight6.grid(row=8, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/cursedMushroomCapsule.png", 9, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=2)
        self.cursedMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.cursedMushroomCapsulePrice6.grid(row=9, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=4)
        self.cursedMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.cursedMushroomCapsuleWeight6.grid(row=9, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/spinyCapsule.png", 10, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=2)
        self.spinyCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.spinyCapsulePrice6.grid(row=10, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=4)
        self.spinyCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.spinyCapsuleWeight6.grid(row=10, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/goombaCapsule.png", 11, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=2)
        self.goombaCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.goombaCapsulePrice6.grid(row=11, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=4)
        self.goombaCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.goombaCapsuleWeight6.grid(row=11, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/plantCapsule.png", 12, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=12, column=2)
        self.plantCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.plantCapsulePrice6.grid(row=12, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=12, column=4)
        self.plantCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.plantCapsuleWeight6.grid(row=12, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=12, column=6)

        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
        label.grid(row=2, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/kamekCapsule.png", 2, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=9)
        self.kamekCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.kamekCapsulePrice6.grid(row=2, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=11)
        self.kamekCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.kamekCapsuleWeight6.grid(row=2, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=2, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/toadyCapsule.png", 3, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=9)
        self.toadyCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.toadyCapsulePrice6.grid(row=3, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=11)
        self.toadyCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.toadyCapsuleWeight6.grid(row=3, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/blizzardCapsule.png", 4, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=9)
        self.blizzardCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.blizzardCapsulePrice6.grid(row=4, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=11)
        self.blizzardCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.blizzardCapsuleWeight6.grid(row=4, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/kleptoCapsule.png", 5, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=9)
        self.kleptoCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.kleptoCapsulePrice6.grid(row=5, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=11)
        self.kleptoCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.kleptoCapsuleWeight6.grid(row=5, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/pinkBooCapsule.png", 6, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=9)
        self.pinkBooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCapsulePrice6.grid(row=6, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=11)
        self.pinkBooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCapsuleWeight6.grid(row=6, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/podobooCapsule.png", 6, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=9)
        self.podobooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.podobooCapsulePrice6.grid(row=6, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=11)
        self.podobooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.podobooCapsuleWeight6.grid(row=6, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/zapCapsule.png", 8, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=9)
        self.zapCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.zapCapsulePrice6.grid(row=8, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=11)
        self.zapCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.zapCapsuleWeight6.grid(row=8, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/tweesterCapsule.png", 9, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=9)
        self.tweesterCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.tweesterCapsulePrice6.grid(row=9, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=11)
        self.tweesterCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.tweesterCapsuleWeight6.grid(row=9, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/thwompCapsule.png", 10, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=9)
        self.thwompCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.thwompCapsulePrice6.grid(row=10, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=11)
        self.thwompCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.thwompCapsuleWeight6.grid(row=10, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=13)
    
        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/bulletBillCapsule.png", 11, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=9)
        self.bulletBillCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.bulletBillCapsulePrice6.grid(row=11, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=11)
        self.bulletBillCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.bulletBillCapsuleWeight6.grid(row=11, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/bombCapsule.png", 12, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=12, column=9)
        self.bombCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.bombCapsulePrice6.grid(row=12, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=12, column=11)
        self.bombCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.bombCapsuleWeight6.grid(row=12, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=12, column=13)

        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
        label.grid(row=2, column=14)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/paraTroopaCapsule.png", 2, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=16)
        self.paraTroopaCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.paraTroopaCapsulePrice6.grid(row=2, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=18)
        self.paraTroopaCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.paraTroopaCapsuleWeight6.grid(row=2, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=2, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/snackCapsule.png", 3, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=16)
        self.snackCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.snackCapsulePrice6.grid(row=3, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=18)
        self.snackCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.snackCapsuleWeight6.grid(row=3, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/gaddlightCapsule.png", 4, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=16)
        self.gaddLightCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.gaddLightCapsulePrice6.grid(row=4, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=18)
        self.gaddLightCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.gaddLightCapsuleWeight6.grid(row=4, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/pinkBooCapsule.png", 5, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=16)
        self.pinkBooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCapsulePrice6.grid(row=5, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=18)
        self.pinkBooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCapsuleWeight6.grid(row=5, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/chanceCapsule.png", 6, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=16)
        self.chanceTimeCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.chanceTimeCapsulePrice6.grid(row=6, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=18)
        self.chanceTimeCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.chanceTimeCapsuleWeight6.grid(row=6, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/dkCapsule.png", 8, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=16)
        self.dkCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.dkCapsulePrice6.grid(row=8, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=18)
        self.dkCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.dkCapsuleWeight6.grid(row=8, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/bowserCapsule.png", 9, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=16)
        self.bowserCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.bowserCapsulePrice6.grid(row=9, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=18)
        self.bowserCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.bowserCapsuleWeight6.grid(row=9, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/duelCapsule.png", 10, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=16)
        self.duelCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.duelCapsulePrice6.grid(row=10, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=18)
        self.duelCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.duelCapsuleWeight6.grid(row=10, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=20)

        # Create MG space icon and entry
        miniGameIconSix = create_image_icon(tabview.tab("Coins Mods"), "assets/miniGame.png", 4, 1)
        miniGameLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        miniGameLabel.grid(row=4, column=2)
        self.miniGameAmountSix = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniGameAmountSix.grid(row=4, column=3)
        miniGameLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when winning a Mini-Game.", font=("Arial", 16))
        miniGameLabel6.grid(row=4, column=4, sticky="w")

        # Create star space icon and entr
        starSpaceIconSix = create_image_icon(tabview.tab("Coins Mods"), "assets/starSpace.png", 5, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=5, column=2)
        self.starSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountSix.grid(row=5, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when purchasing a Star and using a Flutter.", font=("Arial", 16))
        starSpaceLabel6.grid(row=5, column=4, sticky="w")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel, message="Works on Towering Treetop, E Gadd's Garage, Faire Square (Day), Castaway Bay, and Clockwork Castle.")
        starSpaceLabelHover = CTkToolTip(self.starSpaceAmountSix, message="Works on Towering Treetop, E Gadd's Garage, Faire Square (Day), Castaway Bay, and Clockwork Castle.")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel6, message="Works on Towering Treetop, E Gadd's Garage, Faire Square (Day), Castaway Bay, and Clockwork Castle.")

        # Create boo space icon and entry
        pinkBooCoinsSpaceIconSix = create_image_icon(tabview.tab("Coins Mods"), "assets/pinkBooCoins.png", 6, 1)
        pinkBooCoinsSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        pinkBooCoinsSpaceLabel.grid(row=6, column=2)
        self.pinkBooCoinsSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCoinsSpaceAmountSix.grid(row=6, column=3)
        pinkBooCoinsSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when stealing coins ", font=("Arial", 16))
        pinkBooCoinsSpaceLabel6.grid(row=6, column=4, sticky="w")

        # Create boo space icon and entry
        pinkBooCoinsSpaceIconSix = create_image_icon(tabview.tab("Coins Mods"), "assets/pinkBooCoins.png", 7, 1)
        pinkBooCoinsSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Steal  ", font=("Arial", 16))
        pinkBooCoinsSpaceLabel.grid(row=7, column=2)
        self.pinkBooBaseAmountSix = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooBaseAmountSix.grid(row=7, column=3)
        pinkBooCoinsSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" minimum when stealing coins ", font=("Arial", 16))
        pinkBooCoinsSpaceLabel6.grid(row=7, column=4, sticky="w")

        # Create boo space Coins icon and entry
        pinkBooSpaceIconSix = create_image_icon(tabview.tab("Coins Mods"), "assets/pinkBooStars.png", 8, 1)
        pinkBooSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        pinkBooSpaceLabel.grid(row=8, column=2)
        self.pinkBooSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooSpaceAmountSix.grid(row=8, column=3)
        pinkBooSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when stealing a Star.", font=("Arial", 16))
        pinkBooSpaceLabel6.grid(row=8, column=4, sticky="w")

        parseButtonSix = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonSix, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonSix.place(x=10, y=560)

        parseFaireSquare = ctk.CTkButton(master=tabview.tab("Faire Square Mods"), command=self.actionFaireSquare, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseFaireSquare.place(x=10, y=560)

        parseButton6 = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=self.savePresetItems6, text="Save Preset", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton6.place(x=160, y=620)

        parseButton6 = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=self.loadPresetItems6, text="Load Preset", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton6.place(x=310, y=620)

        parseButtonSixOrbs = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=self.actionSpaceButtonSixOrb, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonSixOrbs.place(x=10, y=620)

        self.minigame6 = ["Smashdance", "Odd Card Out", "Freeze Frame", "What Goes Up...", "Granite Getaway", "Circuit Maximus", "Catch You Letter", "Snow Whirled", "Daft Rafts", "Tricky Tires", "Treasure Trawlers", "Memory Lane", "Mowtown", "Cannonball Fun", "Note to Self", "Same is Lame", "Light Up My Night", "Lift Leapers", "Blooper Scooper", "Trap Ease Artist", "Pokey Punch-out", "Money Belt", "Cash Flow", "Cog Jog", "Sink or Swim", "Snow Brawl", "Ball Dozers", "Surge and Destroy", "Pop Star", "Stage Fright", "Conveyor Bolt", "Crate and Peril", "Ray of Fright", "Dust 'til Dawn", "Garden Grab", "Pixel Perfect", "Slot Trot", "Gondola Glide", "Light Breeze", "Body Builder", "Mole-it!", "Cashapult", "Jump the Gun", "Rocky Road", "Clean Team", "Hyper Sniper", "Insectiride", "Sunday Drivers", "Stamp By Me", "Throw Me a Bone", "Black Hole Boogie", "Full Tilt", "Sumo of Doom-o", "O-Zone", "Pitifall", "Mass Meteor", "Lunar-tics", "T Minus Five", "Asteroad Rage", "Boo'd Off the Stage", "Boonanza!", "Trick or Tree", "Something's Amist", "Wrasslin' Rapids", "Verbal Assault", "Shoot Yer Mouth Off", "Talkie Walkie", "Burnstile", "Word Herd", "Fruit Talktail", "Pit Boss", "Dizzy Rotisserie", "Dark 'n Crispy", "Tally Me Banana", "Banana Shake", "Pier Factor", "Seer Terror", "Block Star", "Lab Brats", "Strawberry Shortfuse", "Control Shtick", "Dunk Bros."]
                
        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.comboboxMingames61 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame6)
        self.comboboxMingames61.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.comboboxMingames62 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame6)
        self.comboboxMingames62.grid(row=0, column=3)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=self.minigameReplaceSix, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonTwo.place(x=10, y=560)

        self.items6 = ["None", "Mushroom", "Golden Mushroom", "Sluggish 'Shroom", "Metal Mushroom", "Bullet Bill", "Warp Pipe", "Flutter", "Cursed Mushroom", "Spiny", "Goomba", "Piranha Plant", "Klepto", "Toady", "Kamek", "Mr. Blizzard", "Podoboo", "Zap", "Tweester", "Thwomp", "Bob-omb", "Paratroopa", "Snack", "Boo-away", "Duel", "Miracle", "Bowser", "Donkey Kong", "Pink Boo"]
        
        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 1:  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.initalItem61 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items6)
        self.initalItem61.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 2:  ", font=("Arial", 16))
        label.grid(row=1, column=0)
        
        self.initalItem62 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items6)
        self.initalItem62.grid(row=1, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 3:  ", font=("Arial", 16))
        label.grid(row=2, column=0)

        self.initalItem63 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items6)
        self.initalItem63.grid(row=2, column=1)

        parseButton = ctk.CTkButton(master=tabview.tab("Initial Items"), command=self.initalItems6, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton.place(x=10, y=560)

        self.spaces6 = ["None", "Invisible Space", "Blue Space", "Red Space", "Happening Space", "Chance Time Space", "Duel Space", "Bowser/DK Space", "Chance Time Space", "Orb Space"]

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.spaceRep611 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces6)
        self.spaceRep611.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.spaceRep621 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces6)
        self.spaceRep621.grid(row=0, column=3)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot A) ", font=("Arial", 16))
        label.grid(row=0, column=4)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=1, column=0)

        self.spaceRep612 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces6)
        self.spaceRep612.grid(row=1, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=1, column=2)

        self.spaceRep622 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces6)
        self.spaceRep622.grid(row=1, column=3)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot B) ", font=("Arial", 16))
        label.grid(row=1, column=4)

        parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=self.spaceReplace6, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton.place(x=10, y=560)
        return frame

    def create_mp7_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"), segmented_button_selected_color=sysColor, segmented_button_selected_hover_color=sysColorAlt)
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.add("Orb Mods")
        tabview.add("Minigame Replacement")
        tabview.add("Initial Items")
        tabview.add("Space Replacement")
        tabview.set("Coins Mods")

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/mushroomCapsule.png", 2, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=2)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" 5  ", font=("Arial", 24, "bold"))
        label.grid(row=2, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=4)
        self.mushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.mushroomCapsuleWeight7.grid(row=2, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.   ", font=("Arial", 16))
        label.grid(row=2, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/goldenMushroomCapsule.png", 3, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=2)
        self.goldenMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.goldenMushroomCapsulePrice7.grid(row=3, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=4)
        self.goldenMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.goldenMushroomCapsuleWeight7.grid(row=3, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/slowMushroomCapsule.png", 4, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=2)
        self.slowMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.slowMushroomCapsulePrice7.grid(row=4, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=4)
        self.slowMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.slowMushroomCapsuleWeight7.grid(row=4, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/metalMushroomCapsule.png", 5, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=2)
        self.metalMushroomCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.metalMushroomCapsulePrice7.grid(row=5, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=4)
        self.metalMushroomCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.metalMushroomCapsuleWeight7.grid(row=5, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/wigglerCapsule.png", 6, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=2)
        self.flutterCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.flutterCapsulePrice7.grid(row=6, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=4)
        self.flutterCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.flutterCapsuleWeight7.grid(row=6, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/cannonCapsule.png", 7, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=7, column=2)
        self.cannonCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.cannonCapsulePrice7.grid(row=7, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=7, column=4)
        self.cannonCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.cannonCapsuleWeight7.grid(row=7, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=7, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/snackCapsule.png", 8, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=2)
        self.snackCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.snackCapsulePrice7.grid(row=8, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=4)
        self.snackCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.snackCapsuleWeight7.grid(row=8, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/lakituCapsule.png", 9, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=2)
        self.lakituCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.lakituCapsulePrice7.grid(row=9, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=4)
        self.lakituCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.lakituCapsuleWeight7.grid(row=9, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/hammerBroCapsule.png", 10, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=2)
        self.hammerBroCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.hammerBroCapsulePrice7.grid(row=10, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=4)
        self.hammerBroCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.hammerBroCapsuleWeight7.grid(row=10, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/spearCapsule.png", 11, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=2)
        self.spearCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.spearCapsulePrice7.grid(row=11, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=4)
        self.spearCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.spearCapsuleWeight7.grid(row=11, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=6)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/plantCapsule.png", 12, 1)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=12, column=2)
        self.plantCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.plantCapsulePrice7.grid(row=12, column=3)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=12, column=4)
        self.plantCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.plantCapsuleWeight7.grid(row=12, column=5)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=12, column=6)

        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
        label.grid(row=2, column=7)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/kamekCapsule.png", 2, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=9)
        self.kamekCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.kamekCapsulePrice7.grid(row=2, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=11)
        self.kamekCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.kamekCapsuleWeight7.grid(row=2, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=2, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/toadyCapsule.png", 3, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=9)
        self.toadyCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.toadyCapsulePrice7.grid(row=3, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=11)
        self.toadyCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.toadyCapsuleWeight7.grid(row=3, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/blizzardCapsule.png", 4, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=9)
        self.blizzardCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.blizzardCapsulePrice7.grid(row=4, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=11)
        self.blizzardCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.blizzardCapsuleWeight7.grid(row=4, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/banditCapsule.png", 5, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=9)
        self.banditCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.banditCapsulePrice7.grid(row=5, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=11)
        self.banditCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.banditCapsuleWeight7.grid(row=5, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/pinkBooCapsule.png", 6, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=9)
        self.pinkBooCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCapsulePrice7.grid(row=6, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=11)
        self.pinkBooCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.pinkBooCapsuleWeight7.grid(row=6, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/spinyCapsule.png", 7, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=7, column=9)
        self.spinyCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.spinyCapsulePrice7.grid(row=7, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=7, column=11)
        self.spinyCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.spinyCapsuleWeight7.grid(row=7, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=7, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/zapCapsule.png", 8, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=9)
        self.zapCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.zapCapsulePrice7.grid(row=8, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=11)
        self.zapCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.zapCapsuleWeight7.grid(row=8, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/tweesterCapsule.png", 9, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=9, column=9)
        self.tweesterCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.tweesterCapsulePrice7.grid(row=9, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=9, column=11)
        self.tweesterCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.tweesterCapsuleWeight7.grid(row=9, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=9, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/thwompCapsule.png", 10, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=10, column=9)
        self.thwompCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.thwompCapsulePrice7.grid(row=10, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=10, column=11)
        self.thwompCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.thwompCapsuleWeight7.grid(row=10, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=10, column=13)
    
        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/warpCapsule.png", 11, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=11, column=9)
        self.warpCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.warpCapsulePrice7.grid(row=11, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=11, column=11)
        self.warpCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.warpCapsuleWeight7.grid(row=11, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=11, column=13)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/bombCapsule.png", 12, 8)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=12, column=9)
        self.bombCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.bombCapsulePrice7.grid(row=12, column=10)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=12, column=11)
        self.bombCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.bombCapsuleWeight7.grid(row=12, column=12)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
        label.grid(row=12, column=13)

        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
        label.grid(row=2, column=14)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/fireballCapsule.png", 2, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=2, column=16)
        self.fireballCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.fireballCapsulePrice7.grid(row=2, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=2, column=18)
        self.fireballCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.fireballCapsuleWeight7.grid(row=2, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=2, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/flowerCapsule.png", 3, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=3, column=16)
        self.flowerCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.flowerCapsulePrice7.grid(row=3, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=3, column=18)
        self.flowerCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.flowerCapsuleWeight7.grid(row=3, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=3, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/eggCapsule.png", 4, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=4, column=16)
        self.eggCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.eggCapsulePrice7.grid(row=4, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=4, column=18)
        self.eggCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.eggCapsuleWeight7.grid(row=4, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=4, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/vacuumCapsule.png", 5, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=5, column=16)
        self.vacuumCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.vacuumCapsulePrice7.grid(row=5, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=5, column=18)
        self.vacuumCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.vacuumCapsuleWeight7.grid(row=5, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=5, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/magicCapsule.png", 6, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=6, column=16)
        self.magicCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.magicCapsulePrice7.grid(row=6, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=6, column=18)
        self.magicCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.magicCapsuleWeight7.grid(row=6, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=6, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/tripleCapsule.png", 7, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=7, column=16)
        self.tripleCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.tripleCapsulePrice7.grid(row=7, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=7, column=18)
        self.tripleCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.tripleCapsuleWeight7.grid(row=7, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=7, column=20)

        # Create mushroom orb space icon and entry
        icon = create_image_icon(tabview.tab("Orb Mods"), "assets/koopaCapsule.png", 8, 15)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
        label.grid(row=8, column=16)
        self.koopaCapsulePrice7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.koopaCapsulePrice7.grid(row=8, column=17)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
        label.grid(row=8, column=18)
        self.koopaCapsuleWeight7 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
        self.koopaCapsuleWeight7.grid(row=8, column=19)
        label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
        label.grid(row=8, column=20)

        # Create blue space icon and entry
        blueSpaceIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Give  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountSeven.grid(row=1, column=3)
        label7 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label7.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountSeven.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel6.grid(row=2, column=4, sticky="w")

        # Create character space icon and entry
        characterSpaceIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/characterSpace7.png", 3, 1)
        characterSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        characterSpaceLabel.grid(row=3, column=2)
        self.characterSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.characterSpaceAmountSeven.grid(row=3, column=3)
        characterSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when the character lands on their own Character Space.", font=("Arial", 16))
        characterSpaceLabel6.grid(row=3, column=4, sticky="w")

        # Create MG space icon and entry
        miniGameIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/miniGame.png", 4, 1)
        miniGameLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        miniGameLabel.grid(row=4, column=2)
        self.miniGameAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniGameAmountSeven.grid(row=4, column=3)
        miniGameLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when winning a Mini-Game.", font=("Arial", 16))
        miniGameLabel6.grid(row=4, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/starSpace.png", 5, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=5, column=2)
        self.starSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountSeven.grid(row=5, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when purchasing a Star and using a Flutter.", font=("Arial", 16))
        starSpaceLabel6.grid(row=5, column=4, sticky="w")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel6, message="Works on Grand Canal, Neon Heights, and Bowser's Enchanted Inferno")
        starSpaceLabelHover = CTkToolTip(self.starSpaceAmountSeven, message="Works on Grand Canal, Neon Heights, and Bowser's Enchanted Inferno")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel, message="Works on Grand Canal, Neon Heights, and Bowser's Enchanted Inferno")

        # Create star space last five icon and entry
        starSpaceIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/starSpaceLastFive.png", 6, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=6, column=2)
        self.starSpaceAmountSevenLastFive = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountSevenLastFive.grid(row=6, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins during the Last 5 Turns Event (only if wheel lands on it).", font=("Arial", 16))
        starSpaceLabel6.grid(row=6, column=4, sticky="w")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel6, message="Works on Grand Canal and Bowser's Enchanted Infern.")
        starSpaceLabelHover = CTkToolTip(self.starSpaceAmountSevenLastFive, message="Works on Grand Canal and Bowser's Enchanted Inferno.")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel, message="Works on Grand Canal and Bowser's Enchanted Inferno.")

        # Create hammer bro
        hammerBroIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/hammerBroCapsule.png", 7, 1)
        hammerBroLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        hammerBroLabel.grid(row=7, column=2)
        self.hammerBroAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.hammerBroAmountSeven.grid(row=7, column=3)
        hammerBroLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins from Hammer Bro.", font=("Arial", 16))
        hammerBroLabel.grid(row=7, column=4, sticky="w")

        # Create zap
        zapIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/zapCapsule.png", 8, 1)
        zapLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        zapLabel.grid(row=8, column=2)
        self.zapAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.zapAmountSeven.grid(row=8, column=3)
        zapLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins from Zaps.", font=("Arial", 16))
        zapLabel.grid(row=8, column=4, sticky="w")

        # create fireball
        fireballIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/fireballCapsule.png", 9, 1)
        fireballLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        fireballLabel.grid(row=9, column=2)
        self.fireballAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.fireballAmountSeven.grid(row=9, column=3)
        fireballLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins from Fireballs.", font=("Arial", 16))
        fireballLabel.grid(row=9, column=4, sticky="w")

        # Create vacuum
        vacuumIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/vacuumCapsule.png", 10, 1)
        vacuumLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Steal  ", font=("Arial", 16))
        vacuumLabel.grid(row=10, column=2)
        self.vacuumAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.vacuumAmountSeven.grid(row=10, column=3)
        vacuumLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins with the Vacuum.", font=("Arial", 16))
        vacuumLabel.grid(row=10, column=4, sticky="w")

        # create fireball
        flowerIconSeven = create_image_icon(tabview.tab("Coins Mods"), "assets/flowerCapsule.png", 11, 1)
        flowerLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        flowerLabel.grid(row=11, column=2)
        self.flowerAmountSeven = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.flowerAmountSeven.grid(row=11, column=3)
        flowerLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins per Space with the Flower.", font=("Arial", 16))
        flowerLabel.grid(row=11, column=4, sticky="w")

        parseButtonSeven = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonSeven, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonSeven.place(x=10, y=620)

        parseButton7 = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=self.savePresetItems7, text="Save Preset", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton7.place(x=160, y=620)

        parseButton7 = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=self.loadPresetItems7, text="Load Preset", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton7.place(x=310, y=620)

        parseButtonSevenOrbs = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=self.actionSpaceButtonSevenOrb, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonSevenOrbs.place(x=10, y=620)

        self.minigame7 = ["Catchy Tunes", "Bubble Brawl", "Track & Yield", "Fun Run", "Cointagious", "Snow Ride", "Picture This", "Ghost in the Hall", "Big Dripper", "Target Tag", "Pokey Pummel", "Take Me Ohm", "Kart Wheeled", "Balloon Busters", "Clock Watchers", "Dart Attack", "Oil Crisis", "La Bomba", "Spray Anything", "Balloonatic", "Spinner Cell", "Think Tank", "Flashfright", "Coin-op Bop", "Easy Pickings", "Wheel of Woe", "Boxing Day", "Be My Chum!", "StratosFEAR!", "Pogo-a-go-go", "Buzzstormer", "Tile and Error", "Battery Ram", "Cardinal Rule", "Ice Moves", "Bumper Crop", "Hop-O-Matic 4000", "Wingin' It", "Sphere Factor", "Herbicidal Maniac", "Pyramid Scheme", "World Piece", "Warp Pipe Dreams", "Weight for It", "Helipopper", "Monty's Revenge", "Deck Hands", "Mad Props", "Gimme a Sign", "Bridge Work", "Spin Doctor", "Hip Hop Drop", "Air Farce", "The Final Countdown", "Royal Rumpus", "Light Speed", "Apes of Wrath", "Fish & Cheeps", "Camp Ukiki", "Funstacle Course!", "Funderwall!", "Magmagical Journey!", "Tunnel of Lava!", "Treasure Dome!", "Slot-O-Whirl!", "Peel Out", "Bananas Faster", "Stump Change", "Jump, Man", "Vine Country", "A Bridge Too Short", "Spider Stomp", "Stick and Spin", "Bowser's Lovely Lift!"]
                
        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.comboboxMingames71 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame7)
        self.comboboxMingames71.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.comboboxMingames72 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame7)
        self.comboboxMingames72.grid(row=0, column=3)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=self.minigameReplaceSeven, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonTwo.place(x=10, y=560)

        self.items7 = ["None", "Mushroom", "Super Mushroom", "Slow 'Shroom", "Metal Mushroom", "Flutter", "Cannon", "Snack", "Lakitu", "Hammer Bro", "Piranha Plant", "Spear Guy", "Kamek", "Toady", "Mr. Blizzard", "Bandit", "Pink Boo", "Spiny", "Zap", "Tweester", "Thwomp", "Warp Pipe", "Bob-omb", "Fireball", "Flower", "Egg", "Vacuum", "Surprise", "Triple 'Shroom", "Koopa Kid"]
        
        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 1:  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.initalItem71 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items7)
        self.initalItem71.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 2:  ", font=("Arial", 16))
        label.grid(row=1, column=0)
        
        self.initalItem72 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items7)
        self.initalItem72.grid(row=1, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 3:  ", font=("Arial", 16))
        label.grid(row=2, column=0)

        self.initalItem73 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items7)
        self.initalItem73.grid(row=2, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 4:  ", font=("Arial", 16))
        label.grid(row=3, column=0)

        self.initalItem74 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items7)
        self.initalItem74.grid(row=3, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" (Only if Can Hold 5 Capsules in On)  ", font=("Arial", 16))
        label.grid(row=3, column=2, sticky="w")

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" Item 5:  ", font=("Arial", 16))
        label.grid(row=4, column=0)

        self.initalItem75 = customtkinter.CTkComboBox(master=tabview.tab("Initial Items"), values=self.items7)
        self.initalItem75.grid(row=4, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Initial Items"), text=" (Only if Can Hold 5 Capsules in On)  ", font=("Arial", 16))
        label.grid(row=4, column=2, sticky="w")

        parseButton = ctk.CTkButton(master=tabview.tab("Initial Items"), command=self.initalItems7, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton.place(x=10, y=560)

        self.spaces7 = ["None", "Invisible Space", "Blue Space", "Red Space", "Happening Space", "Bowser Space", "Duel Space", "DK Space", "Orb Space A", "Orb Space B", "Mic Space"]

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.spaceRep711 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces7)
        self.spaceRep711.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.spaceRep721 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces7)
        self.spaceRep721.grid(row=0, column=3)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot A) ", font=("Arial", 16))
        label.grid(row=0, column=4)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=1, column=0)

        self.spaceRep712 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces7)
        self.spaceRep712.grid(row=1, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=1, column=2)

        self.spaceRep722 = customtkinter.CTkComboBox(master=tabview.tab("Space Replacement"), values=self.spaces7)
        self.spaceRep722.grid(row=1, column=3)

        label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot B) ", font=("Arial", 16))
        label.grid(row=1, column=4)

        parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=self.spaceReplace7, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButton.place(x=10, y=560)
        return frame
    
    def create_credits_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"), segmented_button_selected_color=sysColor, segmented_button_selected_hover_color=sysColorAlt)
        tabview.pack(padx=20, pady=20)
        tabview.add("Credits")
        tabview.add("About")
        tabview.add("License")
        tabview.set("About")
        mit_license_widget = customtkinter.CTkLabel(tabview.tab("License"), width=80, height=20, text=(get_mit_license_text()))
        mit_license_widget.pack(padx=10, pady=10)
        credits_widget = customtkinter.CTkLabel(tabview.tab("Credits"), width=80, height=20, text=(get_credits_text()))
        credits_widget.pack(padx=10, pady=10)
        about_widget = customtkinter.CTkLabel(tabview.tab("About"), width=80, height=20, text=(get_about_text()))
        about_widget.pack(padx=10, pady=10)

        button = ctk.CTkButton(tabview, text="Choose Color", command=pick_color, fg_color=sysColor, hover_color=sysColorAlt)
        button.place(x=10, y=10)

        button = ctk.CTkButton(tabview, text="System Color", command=pick_color_system, fg_color=sysColor, hover_color=sysColorAlt)
        button.place(x=155, y=10)
        return frame

    def create_mp82_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.add("Minigame Replacement")
        tabview.set("Coins Mods")

        # Create blue space icon and entry
        blueSpaceIconEight2 = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Give  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountEight2.grid(row=1, column=3)
        label28 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label28.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconEight2 = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountEight2.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel6.grid(row=2, column=4, sticky="w")

        # Create MG space icon and entry
        miniGameIconEight = create_image_icon(tabview.tab("Coins Mods"), "assets/miniGame.png", 3, 1)
        miniGameLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Gain  ", font=("Arial", 16))
        miniGameLabel.grid(row=3, column=2)
        self.miniGameAmountEight2 = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.miniGameAmountEight2.grid(row=3, column=3)
        miniGameLabel8 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when winning a Mini-Game.", font=("Arial", 16))
        miniGameLabel8.grid(row=3, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconEight2= create_image_icon(tabview.tab("Coins Mods"), "assets/starSpace.png", 4, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=4, column=2)
        self.starSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountEight2.grid(row=4, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when purchasing a Star.", font=("Arial", 16))
        starSpaceLabel6.grid(row=4, column=4, sticky="w")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel, message="Works on DK's Treetop Temple, King Boo's Haunted Hideaway, and Shy Guy's Perplex Express.")
        starSpaceLabelHover = CTkToolTip(self.starSpaceAmountEight2, message="Works on DK's Treetop Temple, King Boo's Haunted Hideaway, and Shy Guy's Perplex Express.")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel6, message="Works on DK's Treetop Temple, King Boo's Haunted Hideaway, and Shy Guy's Perplex Express.")

        self.minigame8 = ["Speedy Graffiti", "Swing Kings", "Water Ski Spree", "Punch-a-Bunch", "Crank to Rank", "At the Chomp Wash", "Mosh-Pit Playroom", "Mario Matrix", "Hammer de Pokari", "Grabby Giridion", "Lava or Leave 'Em", "Kartastrophe", "Ribbon Game", "Aim of the Game", "Rudder Madness", "Gun the Runner", "Grabbin' Gold", "Power Trip", "Bob-ombs Away", "Swervin' Skies", "Picture Perfect", "Snow Way Out", "Thrash 'n' Crash", "Chump Rope", "Sick and Twisted", "Bumper Balloons", "Rowed to Victory", "Winner or Dinner", "Paint Misbehavin'", "Sugar Rush", "King of the Thrill", "Shake It Up", "Lean, Mean Ravine", "Boo-ting Gallery", "Crops 'n' Robbers", "In the Nick of Time", "Cut from the Team", "Snipe for the Picking", "Saucer Swarm", "Glacial Meltdown", "Attention Grabber", "Blazing Lassos", "Wing and a Scare", "Lob to Rob", "Pumper Cars", "Cosmic Slalom", "Lava Lobbers", "Loco Motives", "Specter Inspector", "Frozen Assets", "Breakneck Building", "Surf's Way Up", "Bull Riding", "Balancing Act", "Ion the Prize", "You're the Bob-omb", "Scooter Pursuit", "Cardiators", "Rotation Station", "Eyebrawl", "Table Menace", "Flagging Rights", "Trial by Tile", "Star Carnival Bowling", "Puzzle Pillars", "Canyon Cruisers", "Settle It in Court", "Moped Mayhem", "Flip the Chimp", "Pour to Score", "Fruit Picker", "Stampede", "Superstar Showdown", "Alpine Assault", "Treacherous Tightrope"]
                
        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
        label.grid(row=0, column=0)

        self.comboboxMingames81 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame8)
        self.comboboxMingames81.grid(row=0, column=1)

        label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
        label.grid(row=0, column=2)

        self.comboboxMingames82 = customtkinter.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=self.minigame8)
        self.comboboxMingames82.grid(row=0, column=3)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=self.minigameReplaceEight2, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonTwo.place(x=10, y=560)

        parseButtonEight2 = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonEight2, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonEight2.place(x=10, y=560)
        return frame
        
    def create_mp8_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=750, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Coins Mods")
        tabview.set("Coins Mods")

        # Create blue space icon and entry
        blueSpaceIconEight = create_image_icon(tabview.tab("Coins Mods"), "assets/blueSpace.png", 1, 1)
        label = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Give  ", font=("Arial", 16))
        label.grid(row=1, column=2)
        self.blueSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.blueSpaceAmountEight.grid(row=1, column=3)
        label8 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Blue Space.", font=("Arial", 16))
        label8.grid(row=1, column=4, sticky="w")

        # Create red space icon and entry
        redSpaceIconEight = create_image_icon(tabview.tab("Coins Mods"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Lose  ", font=("Arial", 16))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.redSpaceAmountEight.grid(row=2, column=3)
        redSpaceLabel8 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins on a Red Space.", font=("Arial", 16))
        redSpaceLabel8.grid(row=2, column=4, sticky="w")

        # Create star space icon and entry
        starSpaceIconEight= create_image_icon(tabview.tab("Coins Mods"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Cost  ", font=("Arial", 16))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Coins Mods"), width=48, font=("Arial", 16, "bold"))
        self.starSpaceAmountEight.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Coins Mods"), text=" Coins when purchasing a Star.", font=("Arial", 16))
        starSpaceLabel6.grid(row=3, column=4, sticky="w")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel, message="Works on DK's Treetop Temple, King Boo's Haunted Hideaway, and Shy Guy's Perplex Express.")
        starSpaceLabelHover = CTkToolTip(starSpaceLabel6, message="Works on DK's Treetop Temple, King Boo's Haunted Hideaway, and Shy Guy's Perplex Express.")

        parseButtonEight = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=self.actionSpaceButtonEight, text="Generate Codes", fg_color=sysColor, hover_color=sysColorAlt)
        parseButtonEight.place(x=10, y=560)
        return frame

    def injectCodesFunc(self):
        if not self.cheatCodeEntry.get("1.0", "end"):
            createDialog("Error", "error", "No information provided.", None)
            return

        if not os.path.exists("tmp"):
            os.mkdir("tmp")
        else:
            shutil.rmtree("tmp")
            os.mkdir("tmp")

        with open("tmp/codes.txt", 'w') as file:
            file.write("$MPToolkit\n" + self.cheatCodeEntry.get("1.0", "end"))
        iso_path = self.file_label.cget("text")
        gameName = os.path.basename(iso_path)
        

        if is_file_greater_than_4gb(iso_path):
            if sys.platform == "win32":
                subprocess.run([fetchResource("dependencies/wit.exe"), "extract", iso_path, "tmp/tmpROM/"], check=True)
            else:
                subprocess.run([fetchResource("dependencies/wit"), "extract", iso_path, "tmp/tmpROM/"], check=True)
            tmpromContents = os.listdir("tmp/tmpROM")
            folders = [item for item in tmpromContents if os.path.isdir(os.path.join("tmp/tmpROM", item))]
            folder_name = folders[0]
            folder_path = os.path.join("tmp/tmpROM", folder_name + "/sys/main.dol")
            folder_path_raw = os.path.join("tmp/tmpROM", folder_name)
            if sys.platform == "win32":
                subprocess.run([fetchResource("dependencies/GeckoLoader.exe"), "--hooktype=GX", folder_path, "tmp/codes.txt", "--dest=tmp/tmpDOL"], check=True)
            else:
                subprocess.run([fetchResource("dependencies/GeckoLoader"), "--hooktype=GX", folder_path, "tmp/codes.txt", "--dest=tmp/tmpDOL"], check=True)
            os.remove(folder_path)
            shutil.move("tmp/tmpDOL/main.dol", folder_path)
            if sys.platform == "win32":
                subprocess.run([fetchResource("dependencies/wit.exe"), "copy", folder_path_raw, "--dest=tmp/game.iso"], check=True)
            else:
                subprocess.run([fetchResource("dependencies/wit"), "copy", folder_path_raw, "--dest=tmp/game.iso"], check=True)
            file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".iso", initialfile=gameName[:-4] + " (Modded).iso", filetypes=[("ISO Files", "*.iso")])
            shutil.move("tmp/game.iso", file_path)
            shutil.rmtree("tmp/") 
        elif is_file_less_than_100mb(iso_path):
            if sys.platform == "win32":
                subprocess.run([fetchResource("dependencies/GSInject.exe"), "tmp/codes.txt", iso_path, "tmp/game.z64"], check=True)
            else:
                subprocess.run([fetchResource("dependencies/GSInject"), "tmp/codes.txt", iso_path, "tmp/tmp.z64"], check=True)
            file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".z64", initialfile=gameName[:-4] + " (Modded).z64", filetypes=[("Z64 Files", "*.z64")])
            shutil.move("tmp/game.z64", file_path)
            shutil.rmtree("tmp/")
        else:
            if sys.platform == "win32":
                subprocess.run([fetchResource("dependencies/pyisotools.exe"), iso_path, "E", "--dest=tmp/tmpROM/"], check=True)
            else:
                subprocess.run([fetchResource("dependencies/pyisotools"), iso_path, "E", "--dest=tmp/tmpROM/"], check=True)
            tmpromContents = os.listdir("tmp/tmpROM")
            folders = [item for item in tmpromContents if os.path.isdir(os.path.join("tmp/tmpROM", item))]
            folder_name = folders[0]
            folder_path = os.path.join("tmp/tmpROM", folder_name + "/sys/main.dol")
            folder_path_raw = os.path.join("tmp/tmpROM", folder_name)
            if sys.platform == "win32":
                subprocess.run([fetchResource("dependencies/GeckoLoader.exe"), "--hooktype=GX", folder_path, "tmp/codes.txt", "--dest=tmp/tmpDOL"], check=True)
            else:
                subprocess.run([fetchResource("dependencies/pyisotools"), iso_path, "E", "--dest=tmp/tmpROM/"], check=True)
            os.remove(folder_path)
            shutil.move("tmp/tmpDOL/main.dol", folder_path)
            if sys.platform == "win32":
                subprocess.run([fetchResource("dependencies/pyisotools.exe"), folder_path_raw, "B", "--dest=../../game.iso"], check=True)
            else:
                subprocess.run([fetchResource("dependencies/pyisotools"), folder_path_raw, "B", "--dest=../../game.iso"], check=True)
            file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".iso", initialfile=gameName[:-4] + " (Modded).iso", filetypes=[("ISO Files", "*.iso")])
            shutil.move("tmp/game.iso", file_path)
            shutil.rmtree("tmp/")

    def minigameReplaceOne(self):
        mingameSlot1 = self.comboboxMingames11.get()
        mingameSlot2 = self.comboboxMingames12.get()
        minigameHex = ["00", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "31", "32", "33", "34", "35", "36", "37"]
        minigameSlot1Num = self.minigame1.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame1.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement1(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def minigameReplaceTwo(self):
        mingameSlot1 = self.comboboxMingames21.get()
        mingameSlot2 = self.comboboxMingames22.get()
        minigameHex = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "0B", "0C", "0D", "0E", "0F", "10", "11", "12", "13", "14", "15", "16", "17", "18", "1A", "1B", "1C", "1E", "1F", "20", "21", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "30", "31", "32", "33", "34", "35", "36", "37", "39", "41", "42", "43", "44", "45", "46", "47", "48"]
        minigameSlot1Num = self.minigame2.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame2.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement2(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def minigameReplaceThree(self):
        mingameSlot1 = self.comboboxMingames31.get()
        mingameSlot2 = self.comboboxMingames32.get()
        minigameHex = ["08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F", "40", "42", "43", "44", "45", "46", "47", "48"]
        minigameSlot1Num = self.minigame3.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame3.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement3(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def minigameReplaceFour(self):
        mingameSlot1 = self.comboboxMingames41.get()
        mingameSlot2 = self.comboboxMingames42.get()
        minigameHex = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2C", "2D", "2E", "2F", "30", "31", "36", "37", "38", "39"]
        minigameSlot1Num = self.minigame4.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame4.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement4(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def initalItems4(self):
        itemSlot1 = self.initalItem41.get()
        itemSlot2 = self.initalItem42.get()
        itemSlot3 = self.initalItem43.get()
        itemHex = ["FF", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D"]
        itemSlot1Num = self.items4.index(itemSlot1)
        itemSlot1Hex = itemHex[itemSlot1Num]

        itemSlot2Num = self.items4.index(itemSlot2)
        itemSlot2Hex = itemHex[itemSlot2Num]

        itemSlot3Num = self.items4.index(itemSlot3)
        itemSlot3Hex = itemHex[itemSlot3Num]

        code = getInitialItemsFour(itemSlot1Hex, itemSlot2Hex, itemSlot3Hex, itemSlot1, itemSlot2, itemSlot3)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def spaceReplace4(self):
        spaceSlot1 = self.spaceRep411.get()
        spaceSlot2 = self.spaceRep421.get()

        spaceSlot3 = self.spaceRep412.get()
        spaceSlot4 = self.spaceRep422.get()

        spaceHex = ["NONE", "00", "01", "02", "03", "04", "05", "06", "07", "09"]

        spaceSlot1Num = self.spaces4.index(spaceSlot1)
        spaceSlot1Hex = spaceHex[spaceSlot1Num]

        spaceSlot2Num = self.spaces4.index(spaceSlot2)
        spaceSlot2Hex = spaceHex[spaceSlot2Num]

        spaceSlot3Num = self.spaces4.index(spaceSlot3)
        spaceSlot3Hex = spaceHex[spaceSlot3Num]

        spaceSlot4Num = self.spaces4.index(spaceSlot4)
        spaceSlot4Hex = spaceHex[spaceSlot4Num]

        mpSpace41 = getSpaceReplaceFour1(spaceSlot1Hex, spaceSlot2Hex, spaceSlot1, spaceSlot2)
        mpSpace42 = getSpaceReplaceFour2(spaceSlot3Hex, spaceSlot4Hex, spaceSlot3, spaceSlot4)
    
        if spaceSlot1Hex == "NONE":
            mpSpace41 = ""
        if spaceSlot2Hex == "NONE":
            mpSpace41 = ""
        if spaceSlot3Hex == "NONE":
            mpSpace42 = ""
        if spaceSlot4Hex == "NONE":
            mpSpace42 = ""
        
        generatedCode = mpSpace41 + mpSpace42

        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def spaceReplace6(self):
        spaceSlot1 = self.spaceRep611.get()
        spaceSlot2 = self.spaceRep621.get()

        spaceSlot3 = self.spaceRep612.get()
        spaceSlot4 = self.spaceRep622.get()

        spaceHex = ["NONE", "00", "01", "02", "03", "04", "05", "06", "08"]

        spaceSlot1Num = self.spaces6.index(spaceSlot1)
        spaceSlot1Hex = spaceHex[spaceSlot1Num]

        spaceSlot2Num = self.spaces6.index(spaceSlot2)
        spaceSlot2Hex = spaceHex[spaceSlot2Num]

        spaceSlot3Num = self.spaces6.index(spaceSlot3)
        spaceSlot3Hex = spaceHex[spaceSlot3Num]

        spaceSlot4Num = self.spaces6.index(spaceSlot4)
        spaceSlot4Hex = spaceHex[spaceSlot4Num]

        mpSpace61 = getSpaceReplaceSix1(spaceSlot1Hex, spaceSlot2Hex, spaceSlot1, spaceSlot2)
        mpSpace62 = getSpaceReplaceSix2(spaceSlot3Hex, spaceSlot4Hex, spaceSlot3, spaceSlot4)
    
        if spaceSlot1Hex == "NONE":
            mpSpace61 = ""
        if spaceSlot2Hex == "NONE":
            mpSpace61 = ""
        if spaceSlot3Hex == "NONE":
            mpSpace62 = ""
        if spaceSlot4Hex == "NONE":
            mpSpace62 = ""
        
        generatedCode = mpSpace61 + mpSpace62

        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def spaceReplace7(self):
        spaceSlot1 = self.spaceRep711.get()
        spaceSlot2 = self.spaceRep721.get()

        spaceSlot3 = self.spaceRep712.get()
        spaceSlot4 = self.spaceRep722.get()

        spaceHex = ["NONE", "00", "01", "02", "03", "04", "05", "06", "07", "08", "0B"]

        spaceSlot1Num = self.spaces7.index(spaceSlot1)
        spaceSlot1Hex = spaceHex[spaceSlot1Num]

        spaceSlot2Num = self.spaces7.index(spaceSlot2)
        spaceSlot2Hex = spaceHex[spaceSlot2Num]

        spaceSlot3Num = self.spaces7.index(spaceSlot3)
        spaceSlot3Hex = spaceHex[spaceSlot3Num]

        spaceSlot4Num = self.spaces7.index(spaceSlot4)
        spaceSlot4Hex = spaceHex[spaceSlot4Num]

        mpSpace71 = getSpaceReplaceSeven1(spaceSlot1Hex, spaceSlot2Hex, spaceSlot1, spaceSlot2)
        mpSpace72 = getSpaceReplaceSeven2(spaceSlot3Hex, spaceSlot4Hex, spaceSlot3, spaceSlot4)
    
        if spaceSlot1Hex == "NONE":
            mpSpace71 = ""
        if spaceSlot2Hex == "NONE":
            mpSpace71 = ""
        if spaceSlot3Hex == "NONE":
            mpSpace72 = ""
        if spaceSlot4Hex == "NONE":
            mpSpace72 = ""
        
        generatedCode = mpSpace71 + mpSpace72

        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def initalItems5(self):
        itemSlot1 = self.initalItem51.get()
        itemSlot2 = self.initalItem52.get()
        itemSlot3 = self.initalItem53.get()
        itemHex = ["FF", "00", "01", "02", "03", "04", "05", "06", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "14", "15", "16", "17", "18", "19", "1E", "1F", "20", "21", "22", "23", "24", "25"]
        itemSlot1Num = self.items5.index(itemSlot1)
        itemSlot1Hex = itemHex[itemSlot1Num]

        itemSlot2Num = self.items5.index(itemSlot2)
        itemSlot2Hex = itemHex[itemSlot2Num]

        itemSlot3Num = self.items5.index(itemSlot3)
        itemSlot3Hex = itemHex[itemSlot3Num]

        code = getInitialItemsFive(itemSlot1Hex, itemSlot2Hex, itemSlot3Hex, itemSlot1, itemSlot2, itemSlot3)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def initalItems6(self):
        itemSlot1 = self.initalItem61.get()
        itemSlot2 = self.initalItem62.get()
        itemSlot3 = self.initalItem63.get()
        itemHex = ["FF", "00", "01", "02", "03", "04", "05", "06", "07", "0A", "0B", "0C", "0D", "0F", "10", "11", "14", "15", "16", "17", "18", "19", "1E", "1F", "29", "2A", "2B", "2C", "2E"]
        itemSlot1Num = self.items6.index(itemSlot1)
        itemSlot1Hex = itemHex[itemSlot1Num]

        itemSlot2Num = self.items6.index(itemSlot2)
        itemSlot2Hex = itemHex[itemSlot2Num]

        itemSlot3Num = self.items6.index(itemSlot3)
        itemSlot3Hex = itemHex[itemSlot3Num]

        code = getInitialItemsSix(itemSlot1Hex, itemSlot2Hex, itemSlot3Hex, itemSlot1, itemSlot2, itemSlot3)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def initalItems7(self):
        itemSlot1 = self.initalItem71.get()
        itemSlot2 = self.initalItem72.get()
        itemSlot3 = self.initalItem73.get()
        itemSlot4 = self.initalItem74.get()
        itemSlot5 = self.initalItem75.get()
        itemHex = ["FF", "00", "01", "02", "03", "04", "05", "06", "07", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "14", "15", "16", "17", "18", "19", "1E", "1F", "20", "21", "22", "23", "28"]
        itemSlot1Num = self.items7.index(itemSlot1)
        itemSlot1Hex = itemHex[itemSlot1Num]

        itemSlot2Num = self.items7.index(itemSlot2)
        itemSlot2Hex = itemHex[itemSlot2Num]

        itemSlot3Num = self.items7.index(itemSlot3)
        itemSlot3Hex = itemHex[itemSlot3Num]

        itemSlot4Num = self.items7.index(itemSlot4)
        itemSlot4Hex = itemHex[itemSlot4Num]

        itemSlot5Num = self.items7.index(itemSlot5)
        itemSlot5Hex = itemHex[itemSlot5Num]

        code = getInitialItemsSeven(itemSlot1Hex, itemSlot2Hex, itemSlot3Hex, itemSlot4Hex, itemSlot5Hex, itemSlot1, itemSlot2, itemSlot3, itemSlot4, itemSlot5)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
    
    def minigameReplaceFive(self):
        mingameSlot1 = self.comboboxMingames51.get()
        mingameSlot2 = self.comboboxMingames52.get()
        minigameHex = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31", "32", "33", "34", "35", "36", "37", "3A", "3C", "3D", "3E", "3F", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D", "4E", "4F"]
        minigameSlot1Num = self.minigame5.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame5.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement5(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def minigameReplaceFive(self):
        mingameSlot1 = self.comboboxMingames51.get()
        mingameSlot2 = self.comboboxMingames52.get()
        minigameHex = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31", "32", "33", "34", "35", "36", "37", "3A", "3C", "3D", "3E", "3F", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D", "4E", "4F"]
        minigameSlot1Num = self.minigame5.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame5.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement5(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def minigameReplaceSix(self):
        mingameSlot1 = self.comboboxMingames61.get()
        mingameSlot2 = self.comboboxMingames62.get()
        minigameHex = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D", "4E", "4F", "50", "51"]
        minigameSlot1Num = self.minigame6.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame6.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement6(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def minigameReplaceSeven(self):
        mingameSlot1 = self.comboboxMingames71.get()
        mingameSlot2 = self.comboboxMingames72.get()
        minigameHex = ["00", "01", "02", "03", "04", "05", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "10", "12", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "55"]
        minigameSlot1Num = self.minigame7.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame7.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement7(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)\

    def minigameReplaceEight2(self):
        mingameSlot1 = self.comboboxMingames81.get()
        mingameSlot2 = self.comboboxMingames82.get()
        minigameHex = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "3F", "40", "41", "43", "44", "45", "46", "47", "48", "49", "4A", "4B"]
        minigameSlot1Num = self.minigame8.index(mingameSlot1)
        minigameSlot1Hex = minigameHex[minigameSlot1Num]
        minigameSlot2Num = self.minigame8.index(mingameSlot2)
        minigameSlot2Hex = minigameHex[minigameSlot2Num]
        code = getMinigameReplacement82(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
        code = code.strip()
        pyperclip.copy(code)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonOne(self):
        if not self.blueSpaceAmountOne.get() and not self.redSpaceAmountOne.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseOne = self.blueSpaceAmountOne.get()
        try:
            blueSpaceAmountOne = hex(int(blueSpaceAmountBaseOne))
            if len(blueSpaceAmountOne) == 5:
                blueSpaceAmountOne = "0" + blueSpaceAmountOne[2:]
            elif len(blueSpaceAmountOne) == 4:
                blueSpaceAmountOne = "00" + blueSpaceAmountOne[2:]
            elif len(blueSpaceAmountOne) == 3:
                blueSpaceAmountOne = "000" + blueSpaceAmountOne[2:]
        except:
            blueSpaceAmountOne = "DUMMY"
    
        blueSpaceSwitchOne = self.blueSpaceTickboxOne.get()
        if blueSpaceSwitchOne:
            blueSpaceSwitchOne = "1"
        else:
            blueSpaceSwitchOne = "0"

    
        redSpaceAmountBaseOne = self.redSpaceAmountOne.get()
        try:
            redSpaceAmountOne = hex(int(self.redSpaceAmountOne.get()))
            if len(redSpaceAmountOne) == 5:
                redSpaceAmountOne = "0" + redSpaceAmountOne[2:]
            elif len(redSpaceAmountOne) == 4:
                redSpaceAmountOne = "00" + redSpaceAmountOne[2:]
            elif len(redSpaceAmountOne) == 3:
                redSpaceAmountOne = "000" + redSpaceAmountOne[2:]
        except:
            redSpaceAmountOne = "DUMMY"
    
    
        redSpaceSwitchOne = self.redSpaceTickboxOne.get()
        if redSpaceSwitchOne == True:
            redSpaceSwitchOne = "1"
        elif redSpaceSwitchOne == False:
            redSpaceSwitchOne = "0"
    
        marioPartyOneBlueSpace = getBlueSpaceCodeOne(blueSpaceAmountOne, blueSpaceSwitchOne)
        marioPartyOneRedSpace = getRedSpaceCodeOne(redSpaceAmountOne, redSpaceSwitchOne)
    
        if redSpaceAmountOne == "DUMMY":
            marioPartyOneRedSpace = ""
        if blueSpaceAmountOne == "DUMMY":
            marioPartyOneBlueSpace = ""
    
        generatedCode = marioPartyOneBlueSpace + marioPartyOneRedSpace

        if redSpaceSwitchOne == "0":
            generatedCode = generatedCode.replace("ONEREDSWITCH", "Doesn't Double on Last 5")
        elif redSpaceSwitchOne == "1":
            generatedCode = generatedCode.replace("ONEREDSWITCH", "Doubles on Last 5")
        else:
            pass

        if blueSpaceSwitchOne == "0":
            generatedCode = generatedCode.replace("ONEBLUESWITCH", "Doesn't Double on Last 5")
        elif blueSpaceSwitchOne == "1":
            generatedCode = generatedCode.replace("ONEBLUESWITCH", "Doubles on Last 5")
        else:
            pass

        generatedCode = generatedCode.replace("ONERED", redSpaceAmountBaseOne)
        generatedCode = generatedCode.replace("ONEBLUE", blueSpaceAmountBaseOne)
    
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonTwo(self):
        if not self.blueSpaceAmountTwo.get() and not self.redSpaceAmountTwo.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseTwo = self.blueSpaceAmountTwo.get()
        try:
            blueSpaceAmountTwo = hex(int(blueSpaceAmountBaseTwo))
            if len(blueSpaceAmountTwo) == 5:
                blueSpaceAmountTwo = "0" + blueSpaceAmountTwo[2:]
            elif len(blueSpaceAmountTwo) == 4:
                blueSpaceAmountTwo = "00" + blueSpaceAmountTwo[2:]
            elif len(blueSpaceAmountTwo) == 3:
                blueSpaceAmountTwo = "000" + blueSpaceAmountTwo[2:]
        except:
            blueSpaceAmountTwo = "DUMMY"
    
        blueSpaceSwitchTwo = self.blueSpaceTickboxTwo.get()
        if blueSpaceSwitchTwo:
            blueSpaceSwitchTwo = "1"
        else:
            blueSpaceSwitchTwo = "0"

    
        redSpaceAmountBaseTwo = self.redSpaceAmountTwo.get()
        try:
            redSpaceAmountTwo = hex(int(self.redSpaceAmountTwo.get()))
            if len(redSpaceAmountTwo) == 5:
                redSpaceAmountTwo = "0" + redSpaceAmountTwo[2:]
            elif len(redSpaceAmountTwo) == 4:
                redSpaceAmountTwo = "00" + redSpaceAmountTwo[2:]
            elif len(redSpaceAmountTwo) == 3:
                redSpaceAmountTwo = "000" + redSpaceAmountTwo[2:]
        except:
            redSpaceAmountTwo = "DUMMY"
    
    
        redSpaceSwitchTwo = self.redSpaceTickboxTwo.get()
        if redSpaceSwitchTwo == True:
            redSpaceSwitchTwo = "1"
        elif redSpaceSwitchTwo == False:
            redSpaceSwitchTwo = "0"
    
        marioPartyTwoBlueSpace = getBlueSpaceCodeTwo(blueSpaceAmountTwo, blueSpaceSwitchTwo)
        marioPartyTwoRedSpace = getRedSpaceCodeTwo(redSpaceAmountTwo, redSpaceSwitchTwo)
    
        if redSpaceAmountTwo == "DUMMY":
            marioPartyTwoRedSpace = ""
        if blueSpaceAmountTwo == "DUMMY":
            marioPartyTwoBlueSpace = ""
    
        generatedCode = marioPartyTwoBlueSpace + marioPartyTwoRedSpace
        
        if redSpaceSwitchTwo == "0":
            generatedCode = generatedCode.replace("TWOREDSWITCH", "Doesn't Double on Last 5")
        elif redSpaceSwitchTwo == "1":
            generatedCode = generatedCode.replace("TWOREDSWITCH", "Doubles on Last 5")
        else:
            pass

        if blueSpaceSwitchTwo == "0":
            generatedCode = generatedCode.replace("TWOBLUESWITCH", "Doesn't Double on Last 5")
        elif blueSpaceSwitchTwo == "1":
            generatedCode = generatedCode.replace("TWOBLUESWITCH", "Doubles on Last 5")
        else:
            pass

        generatedCode = generatedCode.replace("TWORED", redSpaceAmountBaseTwo)
        generatedCode = generatedCode.replace("TWOBLUE", blueSpaceAmountBaseTwo)
    
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
    
    def actionSpaceButtonThree(self):
        if not self.blueSpaceAmountThree.get() and not self.redSpaceAmountThree.get() and not self.koopaBankAmountThree.get() and not self.starSpaceAmountThree.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseThree = self.blueSpaceAmountThree.get()
        try:
            blueSpaceAmountThree = hex(int(blueSpaceAmountBaseThree))
            if len(blueSpaceAmountThree) == 5:
                blueSpaceAmountThree = "0" + blueSpaceAmountThree[2:]
            elif len(blueSpaceAmountThree) == 4:
                blueSpaceAmountThree = "00" + blueSpaceAmountThree[2:]
            elif len(blueSpaceAmountThree) == 3:
                blueSpaceAmountThree = "000" + blueSpaceAmountThree[2:]
        except:
            blueSpaceAmountThree = "DUMMY"
    
        blueSpaceSwitchThree = self.blueSpaceTickboxThree.get()
        if blueSpaceSwitchThree:
            blueSpaceSwitchThree = "1"
        else:
            blueSpaceSwitchThree = "0"

    
        redSpaceAmountBaseThree = self.redSpaceAmountThree.get()
        try:
            redSpaceAmountThree = hex(int(self.redSpaceAmountThree.get()))
            if len(redSpaceAmountThree) == 5:
                redSpaceAmountThree = "0" + redSpaceAmountThree[2:]
            elif len(redSpaceAmountThree) == 4:
                redSpaceAmountThree = "00" + redSpaceAmountThree[2:]
            elif len(redSpaceAmountThree) == 3:
                redSpaceAmountThree = "000" + redSpaceAmountThree[2:]
        except:
            redSpaceAmountThree = "DUMMY"

        koopaBankAmountBaseThree = self.koopaBankAmountThree.get()
        try:
            koopaBankAmountThree = hex(int(self.koopaBankAmountThree.get()))
            if len(koopaBankAmountThree) == 5:
                koopaBankAmountThree = "0" + koopaBankAmountThree[2:]
            elif len(koopaBankAmountThree) == 4:
                koopaBankAmountThree = "00" + koopaBankAmountThree[2:]
            elif len(koopaBankAmountThree) == 3:
                koopaBankAmountThree = "000" + koopaBankAmountThree[2:]
            negativeKoopaBankAmountBaseThree = -int(koopaBankAmountBaseThree)
            koopaBankAmountNegativeThree = format(negativeKoopaBankAmountBaseThree & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            koopaBankAmountThree = "DUMMY"
            koopaBankAmountNegativeThree = "DUMMY"

        starSpaceAmountBaseThree = self.starSpaceAmountThree.get()
        try:
            starSpaceAmountThree = hex(int(self.starSpaceAmountThree.get()))
            if len(starSpaceAmountThree) == 5:
                starSpaceAmountThree = "0" + starSpaceAmountThree[2:]
            elif len(starSpaceAmountThree) == 4:
                starSpaceAmountThree = "00" + starSpaceAmountThree[2:]
            elif len(starSpaceAmountThree) == 3:
                starSpaceAmountThree = "000" + starSpaceAmountThree[2:]
            negativestarSpaceAmountBaseThree = -int(starSpaceAmountBaseThree)
            starSpaceAmountNegativeThree = format(negativestarSpaceAmountBaseThree & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            starSpaceAmountThree = "DUMMY"
            starSpaceAmountNegativeThree = "DUMMY"
    
        redSpaceSwitchThree = self.redSpaceTickboxThree.get()
        if redSpaceSwitchThree == True:
            redSpaceSwitchThree = "1"
        elif redSpaceSwitchThree == False:
            redSpaceSwitchThree = "0"
    
        marioPartyThreeBlueSpace = getBlueSpaceCodeThree(blueSpaceAmountThree, blueSpaceSwitchThree)
        marioPartyThreeRedSpace = getRedSpaceCodeThree(redSpaceAmountThree, redSpaceSwitchThree)
        marioPartyThreeKoopaBank = getKoopaBankCodeThree(koopaBankAmountThree, koopaBankAmountNegativeThree)
        marioPartyThreeStarSpace = getStarSpaceCodeThree(starSpaceAmountThree, starSpaceAmountNegativeThree)

        if redSpaceAmountThree == "DUMMY":
            marioPartyThreeRedSpace = ""
        if blueSpaceAmountThree == "DUMMY":
            marioPartyThreeBlueSpace = ""
        if koopaBankAmountThree == "DUMMY":
            marioPartyThreeKoopaBank = ""
        if koopaBankAmountNegativeThree == "DUMMY":
            marioPartyThreeKoopaBank = ""
        if starSpaceAmountThree == "DUMMY":
            marioPartyThreeStarSpace = ""
        if starSpaceAmountNegativeThree == "DUMMY":
            marioPartyThreeStarSpace = ""
    
        generatedCode = marioPartyThreeBlueSpace + marioPartyThreeRedSpace + marioPartyThreeKoopaBank + marioPartyThreeStarSpace

        if redSpaceSwitchThree == "0":
            generatedCode = generatedCode.replace("THREEREDSWITCH", "Doesn't Double on Last 5")
        elif redSpaceSwitchThree == "1":
            generatedCode = generatedCode.replace("THREEREDSWITCH", "Doubles on Last 5")
        else:
            pass

        if blueSpaceSwitchThree == "0":
            generatedCode = generatedCode.replace("THREEBLUESWITCH", "Doesn't Double on Last 5")
        elif blueSpaceSwitchThree == "1":
            generatedCode = generatedCode.replace("THREEBLUESWITCH", "Doubles on Last 5")
        else:
            pass

        generatedCode = generatedCode.replace("THREERED", redSpaceAmountBaseThree)
        generatedCode = generatedCode.replace("THREEBLUE", blueSpaceAmountBaseThree)
        generatedCode = generatedCode.replace("THREEKOOPA", koopaBankAmountBaseThree)
        generatedCode = generatedCode.replace("THREESTAR", starSpaceAmountBaseThree)

        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonFour(self):    
        if not self.blueSpaceAmountFour.get() and not self.miniGameAmountFour.get() and not self.redSpaceAmountFour.get() and not self.starSpaceAmountFour.get() and not self.booSpaceAmountFour.get() and not self.booSpaceCoinsAmountFour.get() and not self.lotterySpaceAmountFour.get() and not self.squishAmountFour.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseFour = self.blueSpaceAmountFour.get()
        try:
            blueSpaceAmountFour = hex(int(self.blueSpaceAmountFour.get()))
            if len(blueSpaceAmountFour) == 5:
                blueSpaceAmountFour = "0" + blueSpaceAmountFour[2:]
            elif len(blueSpaceAmountFour) == 4:
                blueSpaceAmountFour = "00" + blueSpaceAmountFour[2:]
            elif len(blueSpaceAmountFour) == 3:
                blueSpaceAmountFour = "000" + blueSpaceAmountFour[2:]
        except:
            blueSpaceAmountFour = "DUMMY"

        redSpaceAmountBaseFour = self.redSpaceAmountFour.get()
        try:
            redSpaceAmountFour = hex(int(self.redSpaceAmountFour.get()))
            if len(redSpaceAmountFour) == 5:
                redSpaceAmountFour = "0" + redSpaceAmountFour[2:]
            elif len(redSpaceAmountFour) == 4:
                redSpaceAmountFour = "00" + redSpaceAmountFour[2:]
            elif len(redSpaceAmountFour) == 3:
                redSpaceAmountFour = "000" + redSpaceAmountFour[2:]
        except:
            redSpaceAmountFour = "DUMMY"

        miniGameAmountBaseFour = self.miniGameAmountFour.get()
        try:
            miniGameAmountFour = hex(int(self.miniGameAmountFour.get()))
            if len(miniGameAmountFour) == 5:
                miniGameAmountFour = "0" + miniGameAmountFour[2:]
            elif len(miniGameAmountFour) == 4:
                miniGameAmountFour = "00" + miniGameAmountFour[2:]
            elif len(miniGameAmountFour) == 3:
                miniGameAmountFour = "000" + miniGameAmountFour[2:]
        except:
            miniGameAmountFour = "DUMMY"

        starSpaceAmountFourBase = self.starSpaceAmountFour.get()

        try:
            starSpaceAmountFour = hex(int(self.starSpaceAmountFour.get()))
            if len(starSpaceAmountFour) == 5:
                starSpaceAmountFour = "00" + starSpaceAmountFour[2:]
            elif len(starSpaceAmountFour) == 4:
                starSpaceAmountFour = "00" + starSpaceAmountFour[2:]
            elif len(starSpaceAmountFour) == 3:
                starSpaceAmountFour = "000" + starSpaceAmountFour[2:]
        except:
            starSpaceAmountFour = "DUMMY"

        booSpaceAmountFourBase = self.booSpaceAmountFour.get()
        try:
            booSpaceAmountFour = hex(int(self.booSpaceAmountFour.get()))
            if len(booSpaceAmountFour) == 5:
                booSpaceAmountFour = "0" + booSpaceAmountFour[2:]
            elif len(booSpaceAmountFour) == 4:
                booSpaceAmountFour = "00" + booSpaceAmountFour[2:]
            elif len(booSpaceAmountFour) == 3:
                booSpaceAmountFour = "000" + booSpaceAmountFour[2:]
        except:
            booSpaceAmountFour = "DUMMY"

        booSpaceCoinsAmountFourBase = self.booSpaceCoinsAmountFour.get()
        try:
            booSpaceCoinsAmountFour = hex(int(self.booSpaceCoinsAmountFour.get()))
            if len(booSpaceCoinsAmountFour) == 5:
                booSpaceCoinsAmountFour = "0" + booSpaceCoinsAmountFour[2:]
            elif len(booSpaceCoinsAmountFour) == 4:
                booSpaceCoinsAmountFour = "00" + booSpaceCoinsAmountFour[2:]
            elif len(booSpaceCoinsAmountFour) == 3:
                booSpaceCoinsAmountFour = "000" + booSpaceCoinsAmountFour[2:]
        except:
            booSpaceCoinsAmountFour = "DUMMY"

        lotterySpaceAmountFourBase = self.lotterySpaceAmountFour.get()
        try:
            lotterySpaceAmountFour = hex(int(self.lotterySpaceAmountFour.get()))
            if len(lotterySpaceAmountFour) == 5:
                lotterySpaceAmountFour = "0" + lotterySpaceAmountFour[2:]
            elif len(lotterySpaceAmountFour) == 4:
                lotterySpaceAmountFour = "00" + lotterySpaceAmountFour[2:]
            elif len(lotterySpaceAmountFour) == 3:
                lotterySpaceAmountFour = "000" + lotterySpaceAmountFour[2:]
        except:
            lotterySpaceAmountFour = "DUMMY"

        squishAmountFourBase = self.squishAmountFour.get()
        try:
            squishAmountFour = hex(int(self.squishAmountFour.get()))
            if len(squishAmountFour) == 5:
                squishAmountFour = "0" + squishAmountFour[2:]
            elif len(squishAmountFour) == 4:
                squishAmountFour = "00" + squishAmountFour[2:]
            elif len(squishAmountFour) == 3:
                squishAmountFour = "000" + squishAmountFour[2:]
        except:
            squishAmountFour = "DUMMY"

        marioPartyFourBlueSpace = getBlueSpaceCodeFour(blueSpaceAmountFour)
        marioPartyFourRedSpace = getRedSpaceCodeFour(redSpaceAmountFour)
        marioPartyFourStarSpace = getStarSpaceCodeFour(starSpaceAmountFour)
        marioPartyFourLotterySpace = getLotterySpaceCodeFour(lotterySpaceAmountFour)
        marioPartyFourBooSpace = getBooSpaceCodeFour(booSpaceAmountFour)
        marioPartyFourBooSpaceCoins = getBooSpaceCoinsCodeFour(booSpaceCoinsAmountFour)
        marioPartyFourMiniGame = getMinigameCodeFour(miniGameAmountFour)
        marioPartyFourSquish = getSquishCodeFour(squishAmountFour)

        if redSpaceAmountFour == "DUMMY":
            marioPartyFourRedSpace = ""
        if blueSpaceAmountFour == "DUMMY":
            marioPartyFourBlueSpace = ""
        if starSpaceAmountFour == "DUMMY":
            marioPartyFourStarSpace = ""
        if lotterySpaceAmountFour == "DUMMY":
            marioPartyFourLotterySpace = ""
        if booSpaceAmountFour == "DUMMY":
            marioPartyFourBooSpace = ""
        if booSpaceCoinsAmountFour == "DUMMY":
            marioPartyFourBooSpaceCoins = ""
        if miniGameAmountFour == "DUMMY":
            marioPartyFourMiniGame = ""
        if squishAmountFour == "DUMMY":
            marioPartyFourSquish = ""

        generatedCode = marioPartyFourBlueSpace + marioPartyFourRedSpace + marioPartyFourMiniGame + marioPartyFourStarSpace + marioPartyFourBooSpaceCoins + marioPartyFourBooSpace + marioPartyFourLotterySpace + marioPartyFourSquish
        generatedCode = generatedCode.replace("FOURRED", redSpaceAmountBaseFour)
        generatedCode = generatedCode.replace("FOURBLUE", blueSpaceAmountBaseFour)
        generatedCode = generatedCode.replace("FOURMINIGAME", miniGameAmountBaseFour)
        generatedCode = generatedCode.replace("FOURSTAR", starSpaceAmountFourBase)
        generatedCode = generatedCode.replace("FOURBOOSTARS", booSpaceAmountFourBase)
        generatedCode = generatedCode.replace("FOURBOOCOINS", booSpaceCoinsAmountFourBase)
        generatedCode = generatedCode.replace("FOURLOTTERY", lotterySpaceAmountFourBase)
        generatedCode = generatedCode.replace("FOURSQUISH", squishAmountFourBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonFive(self):
        if not self.chainChompBaseAmountFive.get() and not self.blueSpaceAmountFive.get() and not self.miniGameAmountFive.get() and not self.redSpaceAmountFive.get() and not self.starSpaceAmountFive.get() and not self.wigglerSpaceAmountFive.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseFive = self.blueSpaceAmountFive.get()
        try:
            blueSpaceAmountFive = hex(int(self.blueSpaceAmountFive.get()))
            if len(blueSpaceAmountFive) == 5:
                blueSpaceAmountFive = "0" + blueSpaceAmountFive[2:]
            elif len(blueSpaceAmountFive) == 4:
                blueSpaceAmountFive = "00" + blueSpaceAmountFive[2:]
            elif len(blueSpaceAmountFive) == 3:
                blueSpaceAmountFive = "000" + blueSpaceAmountFive[2:]
        except:
            blueSpaceAmountFive = "DUMMY"

        redSpaceAmountBaseFive = self.redSpaceAmountFive.get()
        try:
            redSpaceAmountFive = int(redSpaceAmountBaseFive, 16)
            negativeRedSpaceAmountBaseFive = -int(redSpaceAmountBaseFive)
            redSpaceAmountFive = format(negativeRedSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountFive = "DUMMY"


        miniGameAmountBaseFive = self.miniGameAmountFive.get()
        try:
            miniGameAmountFive = hex(int(self.miniGameAmountFive.get()))
            if len(miniGameAmountFive) == 5:
                miniGameAmountFive = "0" + miniGameAmountFive[2:]
            elif len(miniGameAmountFive) == 4:
                miniGameAmountFive = "00" + miniGameAmountFive[2:]
            elif len(miniGameAmountFive) == 3:
                miniGameAmountFive = "000" + miniGameAmountFive[2:]
        except:
            miniGameAmountFive = "DUMMY"

        starSpaceAmountFiveBase = self.starSpaceAmountFive.get()

        try:
            starSpaceAmountFive = hex(int(self.starSpaceAmountFive.get()))
            if len(starSpaceAmountFive) == 5:
                starSpaceAmountFive = "0" + starSpaceAmountFive[2:]
            elif len(starSpaceAmountFive) == 4:
                starSpaceAmountFive = "00" + starSpaceAmountFive[2:]
            elif len(starSpaceAmountFive) == 3:
                starSpaceAmountFive = "000" + starSpaceAmountFive[2:]

            negativeRedSpaceAmountBaseFive = -int(starSpaceAmountFiveBase)
            starSpaceAmountNegativeFive = format(negativeRedSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            starSpaceAmountFive = "DUMMY"
            starSpaceAmountNegativeFive = "DUMMY"

        wigglerSpaceAmountFiveBase = self.wigglerSpaceAmountFive.get()

        chompSpaceAmountFiveBase = self.chompSpaceAmountFive.get()

        try:
            chompSpaceAmountFive = hex(int(self.chompSpaceAmountFive.get()))
            if len(chompSpaceAmountFive) == 5:
                chompSpaceAmountFive = "0" + chompSpaceAmountFive[2:]
            elif len(chompSpaceAmountFive) == 4:
                chompSpaceAmountFive = "00" + chompSpaceAmountFive[2:]
            elif len(chompSpaceAmountFive) == 3:
                chompSpaceAmountFive = "000" + chompSpaceAmountFive[2:]

            negativeChompSpaceAmountBaseFive = -int(chompSpaceAmountFiveBase)
            chompSpaceAmountNegativeFive = format(negativeChompSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            chompSpaceAmountFive = "DUMMY"
            chompSpaceAmountNegativeFive = "DUMMY"
            
        chainChompStealBaseAmountFiveBase = self.chainChompBaseAmountFive.get()
        try:
            chainChompStealBaseAmountFiveCorrected = int(chainChompStealBaseAmountFiveBase) + 5
            chainChompBaseAmountFive = hex(chainChompStealBaseAmountFiveCorrected)
            if len(chainChompBaseAmountFive) == 5:
                chainChompBaseAmountFive = "0" + chainChompBaseAmountFive[2:]
            elif len(chainChompBaseAmountFive) == 4:
                chainChompBaseAmountFive = "00" + chainChompBaseAmountFive[2:]
            elif len(chainChompBaseAmountFive) == 3:
                chainChompBaseAmountFive = "000" + chainChompBaseAmountFive[2:]
        except:
            chainChompBaseAmountFive = "DUMMY"

        try:
            wigglerSpaceAmountFive = hex(int(self.wigglerSpaceAmountFive.get()))
            if len(wigglerSpaceAmountFive) == 5:
                wigglerSpaceAmountFive = "0" + wigglerSpaceAmountFive[2:]
            elif len(wigglerSpaceAmountFive) == 4:
                wigglerSpaceAmountFive = "00" + wigglerSpaceAmountFive[2:]
            elif len(wigglerSpaceAmountFive) == 3:
                wigglerSpaceAmountFive = "000" + wigglerSpaceAmountFive[2:]

            negativeWigglerSpaceAmountBaseFive = -int(wigglerSpaceAmountFiveBase)
            wigglerSpaceAmountNegativeFive = format(negativeWigglerSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            wigglerSpaceAmountFive = "DUMMY"
            wigglerSpaceAmountNegativeFive = "DUMMY"

        marioPartyFiveStarSpace = getStarSpaceCodeFive(starSpaceAmountFive, starSpaceAmountNegativeFive)
        marioPartyFiveWigglerSpace = getWigglerSpaceCodeFive(wigglerSpaceAmountFive, wigglerSpaceAmountNegativeFive)
        marioPartyFiveChompSpace = getChompSpaceCodeFive(chompSpaceAmountFive, chompSpaceAmountNegativeFive)
        marioPartyFiveChompBase = getCoinStealBaseFive(chainChompBaseAmountFive)
        marioPartyFiveBlueSpace = getBlueSpaceCodeFive(blueSpaceAmountFive)
        marioPartyFiveRedSpace = getRedSpaceCodeFive(redSpaceAmountFive)
        marioPartyFiveMiniGame = getMinigameCodeFive(miniGameAmountFive)

        if redSpaceAmountFive == "DUMMY":
            marioPartyFiveRedSpace = ""
        if blueSpaceAmountFive == "DUMMY":
            marioPartyFiveBlueSpace = ""
        if starSpaceAmountFive == "DUMMY":
            marioPartyFiveStarSpace = ""
        if starSpaceAmountNegativeFive == "DUMMY":
            marioPartyFiveStarSpace = ""
        if wigglerSpaceAmountFive == "DUMMY":
            marioPartyFiveWigglerSpace = ""
        if wigglerSpaceAmountNegativeFive == "DUMMY":
            marioPartyFiveWigglerSpace = ""
        if chompSpaceAmountFive == "DUMMY":
            marioPartyFiveChompSpace = ""
        if chompSpaceAmountNegativeFive == "DUMMY":
            marioPartyFiveChompSpace = ""
        if miniGameAmountFive == "DUMMY":
            marioPartyFiveMiniGame = ""
        if chainChompBaseAmountFive == "DUMMY":
            marioPartyFiveChompBase = ""

        generatedCode = marioPartyFiveBlueSpace + marioPartyFiveRedSpace + marioPartyFiveMiniGame + marioPartyFiveStarSpace + marioPartyFiveWigglerSpace + marioPartyFiveChompSpace + marioPartyFiveChompBase
        generatedCode = generatedCode.replace("FIVERED", redSpaceAmountBaseFive)
        generatedCode = generatedCode.replace("FIVEBLUE", blueSpaceAmountBaseFive)
        generatedCode = generatedCode.replace("FIVEMINIGAME", miniGameAmountBaseFive)
        generatedCode = generatedCode.replace("FIVESTAR", starSpaceAmountFiveBase)
        generatedCode = generatedCode.replace("FIVEWIGGLER", wigglerSpaceAmountFiveBase)
        generatedCode = generatedCode.replace("FIVECHOMP", chompSpaceAmountFiveBase)
        generatedCode = generatedCode.replace("FIVECHPBASE", chainChompStealBaseAmountFiveBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonSix(self):
        if not self.blueSpaceAmountSix.get() and not self.miniGameAmountSix.get() and not self.redSpaceAmountSix.get() and not self.starSpaceAmountSix.get() and not self.pinkBooSpaceAmountSix.get() and not self.pinkBooBaseAmountSix.get() and not self.pinkBooCoinsSpaceAmountSix.get() and not self.characterSpaceAmountSix.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseSix = self.blueSpaceAmountSix.get()
        try:
            blueSpaceAmountSix = hex(int(self.blueSpaceAmountSix.get()))
            if len(blueSpaceAmountSix) == 5:
                blueSpaceAmountSix = "0" + blueSpaceAmountSix[2:]
            elif len(blueSpaceAmountSix) == 4:
                blueSpaceAmountSix = "00" + blueSpaceAmountSix[2:]
            elif len(blueSpaceAmountSix) == 3:
                blueSpaceAmountSix = "000" + blueSpaceAmountSix[2:]
        except:
            blueSpaceAmountSix = "DUMMY"

        redSpaceAmountBaseSix = self.redSpaceAmountSix.get()
        try:
            redSpaceAmountSix = int(redSpaceAmountBaseSix, 16)
            negativeRedSpaceAmountBaseSix = -int(redSpaceAmountBaseSix)
            redSpaceAmountSix = format(negativeRedSpaceAmountBaseSix & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountSix = "DUMMY"

        miniGameAmountBaseSix = self.miniGameAmountSix.get()
        try:
            miniGameAmountSix = hex(int(self.miniGameAmountSix.get()))
            if len(miniGameAmountSix) == 5:
                miniGameAmountSix = "0" + miniGameAmountSix[2:]
            elif len(miniGameAmountSix) == 4:
                miniGameAmountSix = "00" + miniGameAmountSix[2:]
            elif len(miniGameAmountSix) == 3:
                miniGameAmountSix = "000" + miniGameAmountSix[2:]
        except:
            miniGameAmountSix = "DUMMY"

        starSpaceAmountSixBase = self.starSpaceAmountSix.get()
        try:
            starSpaceAmountSix = hex(int(self.starSpaceAmountSix.get()))
            if len(starSpaceAmountSix) == 5:
                starSpaceAmountSix = "0" + starSpaceAmountSix[2:]
            elif len(starSpaceAmountSix) == 4:
                starSpaceAmountSix = "00" + starSpaceAmountSix[2:]
            elif len(starSpaceAmountSix) == 3:
                starSpaceAmountSix = "000" + starSpaceAmountSix[2:]

            negativeRedSpaceAmountBaseSix = -int(starSpaceAmountSixBase)
            starSpaceAmountNegativeSix = format(negativeRedSpaceAmountBaseSix & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            starSpaceAmountSix = "DUMMY"
            starSpaceAmountNegativeSix = "DUMMY"

        pinkBooSpaceAmountSixBase = self.pinkBooSpaceAmountSix.get()
        try:
            pinkBooSpaceAmountSix = hex(int(self.pinkBooSpaceAmountSix.get()))
            if len(pinkBooSpaceAmountSix) == 5:
                pinkBooSpaceAmountSix = "0" + pinkBooSpaceAmountSix[2:]
            elif len(pinkBooSpaceAmountSix) == 4:
                pinkBooSpaceAmountSix = "00" + pinkBooSpaceAmountSix[2:]
            elif len(pinkBooSpaceAmountSix) == 3:
                pinkBooSpaceAmountSix = "000" + pinkBooSpaceAmountSix[2:]

            pinkBooSpaceAmountBaseNegativeSix = -int(pinkBooSpaceAmountSixBase)
            pinkBooSpaceAmountNegativeSix = format(pinkBooSpaceAmountBaseNegativeSix & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            pinkBooSpaceAmountSix = "DUMMY"
            pinkBooSpaceAmountNegativeSix = "DUMMY"

        pinkBooStealBaseAmountSixBase = self.pinkBooBaseAmountSix.get()
        try:
            pinkBooStealBaseAmountSixCorrected = int(pinkBooStealBaseAmountSixBase) + 2
            pinkBooBaseAmountSix = hex(pinkBooStealBaseAmountSixCorrected)
            if len(pinkBooBaseAmountSix) == 5:
                pinkBooBaseAmountSix = "0" + pinkBooBaseAmountSix[2:]
            elif len(pinkBooBaseAmountSix) == 4:
                pinkBooBaseAmountSix = "00" + pinkBooBaseAmountSix[2:]
            elif len(pinkBooBaseAmountSix) == 3:
                pinkBooBaseAmountSix = "000" + pinkBooBaseAmountSix[2:]
        except:
            pinkBooBaseAmountSix = "DUMMY"

        pinkBooCoinsSpaceAmountBaseSix = self.pinkBooCoinsSpaceAmountSix.get()
        try:
            pinkBooCoinsSpaceAmountSix = hex(int(self.pinkBooCoinsSpaceAmountSix.get()))
            if len(pinkBooCoinsSpaceAmountSix) == 5:
                pinkBooCoinsSpaceAmountSix = "0" + pinkBooCoinsSpaceAmountSix[2:]
            elif len(pinkBooCoinsSpaceAmountSix) == 4:
                pinkBooCoinsSpaceAmountSix = "00" + pinkBooCoinsSpaceAmountSix[2:]
            elif len(pinkBooCoinsSpaceAmountSix) == 3:
                pinkBooCoinsSpaceAmountSix = "000" + pinkBooCoinsSpaceAmountSix[2:]

            pinkBooCoinsSpaceAmountBaseNegativeSix = -int(pinkBooCoinsSpaceAmountBaseSix)
            pinkBooCoinsSpaceAmountNegativeSix = format(pinkBooCoinsSpaceAmountBaseNegativeSix & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            pinkBooCoinsSpaceAmountSix = "DUMMY"
            pinkBooCoinsSpaceAmountNegativeSix = "DUMMY"

        characterSpaceAmountBaseSix = self.characterSpaceAmountSix.get()
        try:
            characterSpaceAmountSix = hex(int(self.characterSpaceAmountSix.get()))
            if len(characterSpaceAmountSix) == 5:
                characterSpaceAmountSix = "0" + characterSpaceAmountSix[2:]
            elif len(characterSpaceAmountSix) == 4:
                characterSpaceAmountSix = "00" + characterSpaceAmountSix[2:]
            elif len(characterSpaceAmountSix) == 3:
                characterSpaceAmountSix = "000" + characterSpaceAmountSix[2:]
        except:
            characterSpaceAmountSix = "DUMMY"

        marioPartySixBlueSpace = getBlueSpaceCodeSix(blueSpaceAmountSix)
        marioPartySixRedSpace = getRedSpaceCodeSix(redSpaceAmountSix)
        marioPartySixCharacterSpace = getCharacterSpaceCodeSix(characterSpaceAmountSix)
        marioPartySixStarSpace = getStarSpaceCodeSix(starSpaceAmountSix, starSpaceAmountNegativeSix)
        marioPartySixPinkBooSpace = getPinkBooSpaceCodeSix(pinkBooSpaceAmountSix, pinkBooSpaceAmountNegativeSix)
        marioPartySixPinkBooCoinsSpace = getPinkBooCoinsSpaceCodeSix(pinkBooCoinsSpaceAmountSix, pinkBooCoinsSpaceAmountNegativeSix)
        marioPartySixPinkBooCoinsBase = getCoinStealBaseSix(pinkBooBaseAmountSix)
        marioPartySixMiniGame = getMinigameCodeSix(miniGameAmountSix)

        if redSpaceAmountSix == "DUMMY":
            marioPartySixRedSpace = ""
        if blueSpaceAmountSix == "DUMMY":
            marioPartySixBlueSpace = ""
        if starSpaceAmountSix == "DUMMY":
            marioPartySixStarSpace = ""
        if characterSpaceAmountSix == "DUMMY":
            marioPartySixCharacterSpace = ""
        if starSpaceAmountNegativeSix == "DUMMY":
            marioPartySixStarSpace = ""
        if pinkBooSpaceAmountSix == "DUMMY":
            marioPartySixPinkBooSpace = ""
        if pinkBooSpaceAmountNegativeSix == "DUMMY":
            marioPartySixPinkBooSpace = ""
        if pinkBooCoinsSpaceAmountSix == "DUMMY":
            marioPartySixPinkBooCoinsSpace = ""
        if pinkBooCoinsSpaceAmountNegativeSix == "DUMMY":
            marioPartySixPinkBooCoinsSpace = ""
        if miniGameAmountSix == "DUMMY":
            marioPartySixMiniGame = ""
        if pinkBooBaseAmountSix == "DUMMY":
            marioPartySixPinkBooCoinsBase = ""
        
        generatedCode = marioPartySixBlueSpace + marioPartySixRedSpace + marioPartySixCharacterSpace + marioPartySixMiniGame + marioPartySixStarSpace + marioPartySixPinkBooCoinsSpace + marioPartySixPinkBooSpace + marioPartySixPinkBooCoinsBase
        generatedCode = generatedCode.replace("SIXRED", redSpaceAmountBaseSix)
        generatedCode = generatedCode.replace("SIXBLUE", blueSpaceAmountBaseSix)
        generatedCode = generatedCode.replace("SIXCHARACTER", characterSpaceAmountBaseSix)
        generatedCode = generatedCode.replace("SIXMINIGAME", miniGameAmountBaseSix)
        generatedCode = generatedCode.replace("SIXSTAR", starSpaceAmountSixBase)
        generatedCode = generatedCode.replace("SIXBOOSTARS", pinkBooSpaceAmountSixBase)
        generatedCode = generatedCode.replace("SIXBOOCOINS", pinkBooCoinsSpaceAmountBaseSix)
        generatedCode = generatedCode.replace("SIXBOOMIN", pinkBooStealBaseAmountSixBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonSeven(self):
        if not self.flowerAmountSeven.get() and not self.vacuumAmountSeven.get() and not self.fireballAmountSeven.get() and not self.blueSpaceAmountSeven.get() and not self.miniGameAmountSeven.get() and not self.characterSpaceAmountSeven.get()  and not self.redSpaceAmountSeven.get() and not self.starSpaceAmountSeven.get() and not self.starSpaceAmountSevenLastFive.get() and not self.hammerBroAmountSeven.get() and not self.zapAmountSeven.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseSeven = self.blueSpaceAmountSeven.get()
        try:
            blueSpaceAmountSeven = hex(int(self.blueSpaceAmountSeven.get()))
            if len(blueSpaceAmountSeven) == 5:
                blueSpaceAmountSeven = "0" + blueSpaceAmountSeven[2:]
            elif len(blueSpaceAmountSeven) == 4:
                blueSpaceAmountSeven = "00" + blueSpaceAmountSeven[2:]
            elif len(blueSpaceAmountSeven) == 3:
                blueSpaceAmountSeven = "000" + blueSpaceAmountSeven[2:]
        except:
            blueSpaceAmountSeven = "DUMMY"

        redSpaceAmountBaseSeven = self.redSpaceAmountSeven.get()
        try:
            redSpaceAmountSeven = int(redSpaceAmountBaseSeven, 16)
            negativeRedSpaceAmountBaseSeven = -int(redSpaceAmountBaseSeven)
            redSpaceAmountSeven = format(negativeRedSpaceAmountBaseSeven & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountSeven = "DUMMY"

        starSpaceAmountSevenBase = self.starSpaceAmountSeven.get()
        starSpaceAmountSevenLastFiveBase = self.starSpaceAmountSevenLastFive.get()

        try:
            starSpaceAmountSeven = hex(int(self.starSpaceAmountSeven.get()))
            if len(starSpaceAmountSeven) == 4:
                starSpaceAmountSeven = "00" + starSpaceAmountSeven[2:]
            elif len(starSpaceAmountSeven) == 3:
                starSpaceAmountSeven = "000" + starSpaceAmountSeven[2:]
        except:
            starSpaceAmountSeven = "DUMMY"

        try:
            starSpaceAmountSevenLastFive = hex(int(self.starSpaceAmountSevenLastFive.get()))
            if len(starSpaceAmountSevenLastFive) == 4:
                starSpaceAmountSevenLastFive = "00" + starSpaceAmountSevenLastFive[2:]
            elif len(starSpaceAmountSevenLastFive) == 3:
                starSpaceAmountSevenLastFive = "000" + starSpaceAmountSevenLastFive[2:]
        except:
            starSpaceAmountSevenLastFive = "DUMMY"
        
        miniGameAmountBaseSeven = self.miniGameAmountSeven.get()
        try:
            miniGameAmountSeven = hex(int(self.miniGameAmountSeven.get()))
            if len(miniGameAmountSeven) == 5:
                miniGameAmountSeven = "0" + miniGameAmountSeven[2:]
            elif len(miniGameAmountSeven) == 4:
                miniGameAmountSeven = "00" + miniGameAmountSeven[2:]
            elif len(miniGameAmountSeven) == 3:
                miniGameAmountSeven = "000" + miniGameAmountSeven[2:]
        except:
            miniGameAmountSeven = "DUMMY"
        
        characterSpaceAmountBaseSeven = self.characterSpaceAmountSeven.get()
        try:
            characterSpaceAmountSeven = hex(int(self.characterSpaceAmountSeven.get()))
            if len(characterSpaceAmountSeven) == 5:
                characterSpaceAmountSeven = "0" + characterSpaceAmountSeven[2:]
            elif len(characterSpaceAmountSeven) == 4:
                characterSpaceAmountSeven = "00" + characterSpaceAmountSeven[2:]
            elif len(characterSpaceAmountSeven) == 3:
                characterSpaceAmountSeven = "000" + characterSpaceAmountSeven[2:]
        except:
            characterSpaceAmountSeven = "DUMMY"

        hammerBroAmountSevenBase = self.hammerBroAmountSeven.get()
        try:
            hammerBroAmountSeven = hex(int(self.hammerBroAmountSeven.get()))
            if len(hammerBroAmountSeven) == 4:
                hammerBroAmountSeven = "0" + hammerBroAmountSeven[2:]
            elif len(hammerBroAmountSeven) == 4:
                hammerBroAmountSeven = "00" + hammerBroAmountSeven[2:]
            elif len(hammerBroAmountSeven) == 3:
                hammerBroAmountSeven = "000" + hammerBroAmountSeven[2:]

            hammerBroSpaceAmountBaseNegativeSeven = -int(hammerBroAmountSevenBase)
            hammerBroSpaceAmountNegativeSeven = format(hammerBroSpaceAmountBaseNegativeSeven & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

            hammerBroAmountHalf = hammerBroAmountSevenBase / 2
            if not hammerBroAmountHalf.is_integer():
                hammerBroAmountHalf = hammerBroAmountHalf - 1

            hammerBroSpaceAmountHalfBaseNegativeSeven = -int(hammerBroAmountHalf)
            hammerBroSpaceAmountHalfNegativeSeven = format(hammerBroSpaceAmountHalfBaseNegativeSeven & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            hammerBroAmountSeven = "DUMMY"
            hammerBroSpaceAmountHalfNegativeSeven = "DUMMY"
            hammerBroSpaceAmountNegativeSeven = "DUMMY"

        zapAmountSevenBase = self.zapAmountSeven.get()
        try:
            zapAmountSeven = hex(int(self.zapAmountSeven.get()))
            if len(zapAmountSeven) == 5:
                zapAmountSeven = "0" + zapAmountSeven[2:]
            elif len(zapAmountSeven) == 4:
                zapAmountSeven = "00" + zapAmountSeven[2:]
            elif len(zapAmountSeven) == 3:
                zapAmountSeven = "000" + zapAmountSeven[2:]
        except:
            zapAmountSeven = "DUMMY"

        fireballAmountSevenBase = self.fireballAmountSeven.get()
        try:
            fireballAmountSeven = hex(int(self.fireballAmountSeven.get()))
            if len(fireballAmountSeven) == 5:
                fireballAmountSeven = "00" + fireballAmountSeven[2:]
            elif len(fireballAmountSeven) == 4:
                fireballAmountSeven = "00" + fireballAmountSeven[2:]
            elif len(fireballAmountSeven) == 3:
                fireballAmountSeven = "000" + fireballAmountSeven[2:]

            fireballSpaceAmountBaseNegativeSeven = -int(fireballAmountSevenBase)
            fireballSpaceAmountNegativeSeven = format(fireballSpaceAmountBaseNegativeSeven & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            fireballAmountSeven = "DUMMY"
            fireballSpaceAmountNegativeSeven = "DUMMY"

        flowerAmountSevenBase = self.flowerAmountSeven.get()
        try:
            flowerAmountSeven = hex(int(self.flowerAmountSeven.get()))
            if len(flowerAmountSeven) == 5:
                flowerAmountSeven = "0" + flowerAmountSeven[2:]
            elif len(flowerAmountSeven) == 4:
                flowerAmountSeven = "00" + flowerAmountSeven[2:]
            elif len(flowerAmountSeven) == 3:
                flowerAmountSeven = "000" + flowerAmountSeven[2:]
        except:
            flowerAmountSeven = "DUMMY"
            flowerSpaceAmountNegativeSeven = "DUMMY"

        vacuumAmountSevenBase = self.vacuumAmountSeven.get()
        try:
            vacuumAmountSeven = hex(int(self.vacuumAmountSeven.get()))
            if len(vacuumAmountSeven) == 5:
                vacuumAmountSeven = "0" + vacuumAmountSeven[2:]
            elif len(vacuumAmountSeven) == 4:
                vacuumAmountSeven = "00" + vacuumAmountSeven[2:]
            elif len(vacuumAmountSeven) == 3:
                vacuumAmountSeven = "000" + vacuumAmountSeven[2:]
        except:
            vacuumAmountSeven = "DUMMY"
            vacuumSpaceAmountNegativeSeven = "DUMMY"

        marioPartySevenBlueSpace = getBlueSpaceCodeSeven(blueSpaceAmountSeven)
        marioPartySevenRedSpace = getRedSpaceCodeSeven(redSpaceAmountSeven)
        marioPartySevenCharacterSpace = getCharacterSpaceCodeSeven(characterSpaceAmountSeven)
        marioPartySevenStarSpace = getStarSpaceCodeSeven(starSpaceAmountSeven)
        marioPartySevenStarSpaceLastFive = getStarSpaceCodeSevenLastFive(starSpaceAmountSevenLastFive)
        marioPartySevenHammerBro = getHammerBroSpaceCodeSeven(hammerBroAmountSeven, hammerBroSpaceAmountNegativeSeven, hammerBroSpaceAmountHalfNegativeSeven)
        marioPartySevenZap = getZapSpaceCodeSeven(zapAmountSeven)
        marioPartySevenFlower = getFlowerSpaceCodeSeven(flowerAmountSeven)
        marioPartySevenVacuum = getVacuumSpaceCodeSeven(vacuumAmountSeven)
        marioPartySevenFireball = getFireballSpaceCodeSeven(fireballAmountSeven, fireballSpaceAmountNegativeSeven)
        marioPartySevenMiniGame = getMinigameCodeSeven(miniGameAmountSeven)

        if redSpaceAmountSeven == "DUMMY":
            marioPartySevenRedSpace = ""
        if blueSpaceAmountSeven == "DUMMY":
            marioPartySevenBlueSpace = ""
        if characterSpaceAmountSeven == "DUMMY":
            marioPartySevenCharacterSpace = ""
        if starSpaceAmountSeven == "DUMMY":
            marioPartySevenStarSpace = ""
        if starSpaceAmountSevenLastFive == "DUMMY":
            marioPartySevenStarSpaceLastFive = ""
        if hammerBroSpaceAmountNegativeSeven == "DUMMY":
            marioPartySevenHammerBro = ""
        if hammerBroSpaceAmountHalfNegativeSeven == "DUMMY":
            marioPartySevenHammerBro = ""
        if hammerBroAmountSeven == "DUMMY":
            marioPartySevenHammerBro = ""
        if fireballSpaceAmountNegativeSeven == "DUMMY":
            marioPartySevenFireball = ""
        if fireballAmountSeven == "DUMMY":
            marioPartySevenFireball = ""
        if zapAmountSeven == "DUMMY":
            marioPartySevenZap = ""
        if vacuumAmountSeven == "DUMMY":
            marioPartySevenVacuum = ""
        if flowerAmountSeven == "DUMMY":
            marioPartySevenFlower = ""
        if miniGameAmountSeven == "DUMMY":
            marioPartySevenMiniGame = ""

        generatedCode = marioPartySevenBlueSpace + marioPartySevenRedSpace + marioPartySevenMiniGame + marioPartySevenCharacterSpace + marioPartySevenStarSpace + marioPartySevenStarSpaceLastFive + marioPartySevenHammerBro + marioPartySevenZap + marioPartySevenFireball + marioPartySevenFlower + marioPartySevenVacuum
        generatedCode = generatedCode.replace("SEVENRED", redSpaceAmountBaseSeven)
        generatedCode = generatedCode.replace("SEVENBLUE", blueSpaceAmountBaseSeven)
        generatedCode = generatedCode.replace("SEVENMINIGAME", miniGameAmountBaseSeven)
        generatedCode = generatedCode.replace("SEVENCHARACTER", characterSpaceAmountBaseSeven)
        generatedCode = generatedCode.replace("SEVENSTAR", starSpaceAmountSevenBase)
        generatedCode = generatedCode.replace("SEVENSTLASTFIVE", starSpaceAmountSevenLastFiveBase)
        generatedCode = generatedCode.replace("SEVENHAMMERBRO", hammerBroAmountSevenBase)
        generatedCode = generatedCode.replace("SEVENZAP", zapAmountSevenBase)
        generatedCode = generatedCode.replace("SEVENFIREBALL", fireballAmountSevenBase)
        generatedCode = generatedCode.replace("SEVENFLOWER", flowerAmountSevenBase)
        generatedCode = generatedCode.replace("SEVENVACUUM", vacuumAmountSevenBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonEight(self):
        if not self.blueSpaceAmountEight.get() and not self.redSpaceAmountEight.get() and not self.starSpaceAmountEight.get():
            createDialog("Error", "error", "No information provided.", None)
            return

        blueSpaceAmountBaseEight = self.blueSpaceAmountEight.get()
        try:
            blueSpaceAmountEight = hex(int(self.blueSpaceAmountEight.get()))
            if len(blueSpaceAmountEight) == 5:
                blueSpaceAmountEight = "0" + blueSpaceAmountEight[2:]
            elif len(blueSpaceAmountEight) == 4:
                blueSpaceAmountEight = "00" + blueSpaceAmountEight[2:]
            elif len(blueSpaceAmountEight) == 3:
                blueSpaceAmountEight = "000" + blueSpaceAmountEight[2:]
        except:
            blueSpaceAmountEight = "DUMMY"

        redSpaceAmountBaseEight = self.redSpaceAmountEight.get()
        try:
            redSpaceAmountEight = int(redSpaceAmountBaseEight, 16)
            negativeRedSpaceAmountBaseEight = -int(redSpaceAmountBaseEight)
            redSpaceAmountEight = format(negativeRedSpaceAmountBaseEight & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountEight = "DUMMY"

        starSpaceAmountEightBase = self.starSpaceAmountEight.get()

        try:
            starSpaceAmountEight = hex(int(self.starSpaceAmountEight.get()))
            if len(starSpaceAmountEight) == 5:
                starSpaceAmountEight = "0" + starSpaceAmountEight[2:]
            if len(starSpaceAmountEight) == 4:
                starSpaceAmountEight = "00" + starSpaceAmountEight[2:]
            elif len(starSpaceAmountEight) == 3:
                starSpaceAmountEight = "000" + starSpaceAmountEight[2:]

            negativeRedSpaceAmountBaseEight = -int(starSpaceAmountEightBase)
            starSpaceAmountNegativeEight = format(negativeRedSpaceAmountBaseEight & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            starSpaceAmountEight = "DUMMY"
            starSpaceAmountNegativeEight = "DUMMY"

        marioPartyEightStarSpace = getStarSpaceCodeEight(starSpaceAmountEight, starSpaceAmountNegativeEight)
        marioPartyEightBlueSpace = getBlueSpaceCodeEight(blueSpaceAmountEight)
        marioPartyEightRedSpace = getRedSpaceCodeEight(redSpaceAmountEight)

        if redSpaceAmountEight == "DUMMY":
            marioPartyEightRedSpace = ""
        if blueSpaceAmountEight == "DUMMY":
            marioPartyEightBlueSpace = ""
        if starSpaceAmountEight == "DUMMY":
            marioPartyFiveStarSpace = ""
        if starSpaceAmountNegativeEight == "DUMMY":
            marioPartyEightStarSpace = ""

        generatedCode = marioPartyEightBlueSpace + marioPartyEightRedSpace + marioPartyEightStarSpace
        generatedCode = generatedCode.replace("EIGHTRED", redSpaceAmountBaseEight)
        generatedCode = generatedCode.replace("EIGHTBLUE", blueSpaceAmountBaseEight)
        generatedCode = generatedCode.replace("EIGHTSTAR", starSpaceAmountEightBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonEight2(self):
        if not self.miniGameAmountEight2.get() and not self.blueSpaceAmountEight2.get() and not self.redSpaceAmountEight2.get() and not self.starSpaceAmountEight2.get():
            createDialog("Error", "error", "No information provided.", None)
            return
        blueSpaceAmountBaseEight2 = self.blueSpaceAmountEight2.get()

        try:
            blueSpaceAmountEight2 = hex(int(self.blueSpaceAmountEight2.get()))
            if len(blueSpaceAmountEight2) == 5:
                blueSpaceAmountEight2 = "0" + blueSpaceAmountEight2[2:]
            elif len(blueSpaceAmountEight2) == 4:
                blueSpaceAmountEight2 = "00" + blueSpaceAmountEight2[2:]
            elif len(blueSpaceAmountEight2) == 3:
                blueSpaceAmountEight2 = "000" + blueSpaceAmountEight2[2:]
        except:
            blueSpaceAmountEight2 = "DUMMY"

        redSpaceAmountBaseEight2 = self.redSpaceAmountEight2.get()
        try:
            redSpaceAmountEight2 = int(redSpaceAmountBaseEight2, 16)
            negativeRedSpaceAmountBaseEight2 = -int(redSpaceAmountBaseEight2)
            redSpaceAmountEight2 = format(negativeRedSpaceAmountBaseEight2 & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            redSpaceAmountEight2 = "DUMMY"

        starSpaceAmountEight2Base = self.starSpaceAmountEight2.get()
        try:
            starSpaceAmountEight2 = hex(int(self.starSpaceAmountEight2.get()))
            if len(starSpaceAmountEight2) == 5:
                starSpaceAmountEight2 = "0" + starSpaceAmountEight2[2:]
            elif len(starSpaceAmountEight2) == 4:
                starSpaceAmountEight2 = "00" + starSpaceAmountEight2[2:]
            elif len(starSpaceAmountEight2) == 3:
                starSpaceAmountEight2 = "000" + starSpaceAmountEight2[2:]
            negativeRedSpaceAmountBaseEight2 = -int(starSpaceAmountEight2Base)
            starSpaceAmountNegativeEight2 = format(negativeRedSpaceAmountBaseEight2 & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            starSpaceAmountEight2 = "DUMMY"
            starSpaceAmountNegativeEight2 = "DUMMY"
        
        miniGameAmountBaseEight2 = self.miniGameAmountEight2.get()
        try:
            miniGameAmountEight2 = hex(int(self.miniGameAmountEight2.get()))
            if len(miniGameAmountEight2) == 5:
                miniGameAmountEight2 = "0" + miniGameAmountEight2[2:]
            elif len(miniGameAmountEight2) == 4:
                miniGameAmountEight2 = "00" + miniGameAmountEight2[2:]
            elif len(miniGameAmountEight2) == 3:
                miniGameAmountEight2 = "000" + miniGameAmountEight2[2:]
        except:
            miniGameAmountEight2 = "DUMMY"

        marioPartyEight2StarSpace = getStarSpaceCodeEightGC(starSpaceAmountEight2, starSpaceAmountNegativeEight2)
        marioPartyEight2BlueSpace = getBlueSpaceCodeEightGC(blueSpaceAmountEight2)
        marioPartyEight2RedSpace = getRedSpaceCodeEightGC(redSpaceAmountEight2)
        marioPartyEight2MiniGame = getMinigameCodeEight2(miniGameAmountEight2)

        if redSpaceAmountEight2 == "DUMMY":
            marioPartyEight2RedSpace = ""
        if blueSpaceAmountEight2 == "DUMMY":
            marioPartyEight2BlueSpace = ""
        if starSpaceAmountEight2 == "DUMMY":
            marioPartyFiveStarSpace = ""
        if starSpaceAmountNegativeEight2 == "DUMMY":
            marioPartyEight2StarSpace = ""
        if miniGameAmountEight2 == "DUMMY":
            marioPartyEight2MiniGame = ""

        generatedCode = marioPartyEight2BlueSpace + marioPartyEight2RedSpace + marioPartyEight2MiniGame + marioPartyEight2StarSpace
        generatedCode = generatedCode.replace("EIGHTREDGC", redSpaceAmountBaseEight2)
        generatedCode = generatedCode.replace("EIGHTBLUEGC", blueSpaceAmountBaseEight2)
        generatedCode = generatedCode.replace("EIGHTMINIGAMEGC", miniGameAmountBaseEight2)
        generatedCode = generatedCode.replace("EIGHTSTARGC", starSpaceAmountEight2Base)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionFaireSquare(self):
        if not self.faireSquare1.get() and not self.faireSquare2.get() and not self.faireSquare3.get() and not self.faireSquare4.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return

        faireSquare1Base = self.faireSquare1.get()
        faireSquare2Base = self.faireSquare2.get()
        faireSquare3Base = self.faireSquare3.get()
        faireSquare4Base = self.faireSquare4.get()

        try:
            faireSquare1 = hex(int(self.faireSquare1.get()))
            if len(faireSquare1) == 5:
                faireSquare1 = "0" + faireSquare1[2:]
            elif len(faireSquare1) == 4:
                faireSquare1 = "00" + faireSquare1[2:]
            elif len(faireSquare1) == 3:
                faireSquare1 = "000" + faireSquare1[2:]
        except:
            faireSquare1 = "DUMMY"

        try:
            faireSquare2 = hex(int(self.faireSquare2.get()))
            if len(faireSquare2) == 5:
                faireSquare2 = "0" + faireSquare2[2:]
            elif len(faireSquare2) == 4:
                faireSquare2 = "00" + faireSquare2[2:]
            elif len(faireSquare2) == 3:
                faireSquare2 = "000" + faireSquare2[2:]
        except:
            faireSquare2 = "DUMMY"

        try:
            faireSquare3 = hex(int(self.faireSquare3.get()))
            if len(faireSquare3) == 5:
                faireSquare3 = "0" + faireSquare3[2:]
            elif len(faireSquare3) == 4:
                faireSquare3 = "00" + faireSquare3[2:]
            elif len(faireSquare3) == 3:
                faireSquare3 = "000" + faireSquare3[2:]
        except:
            faireSquare3 = "DUMMY"

        try:
            faireSquare4 = hex(int(self.faireSquare4.get()))
            if len(faireSquare4) == 5:
                faireSquare4 = "0" + faireSquare4[2:]
            elif len(faireSquare4) == 4:
                faireSquare4 = "00" + faireSquare4[2:]
            elif len(faireSquare4) == 3:
                faireSquare4 = "000" + faireSquare4[2:]
        except:
            faireSquare4 = "DUMMY"

        codeFaireSquare = getFaireSquareStarCodeSix(faireSquare1, faireSquare2, faireSquare3, faireSquare4)
        
        if faireSquare1 == "DUMMY":
            faireSquare1 = ""
        if faireSquare2 == "DUMMY":
            faireSquare2 = ""
        if faireSquare3 == "DUMMY":
            faireSquare3 = ""
        if faireSquare4 == "DUMMY":
            faireSquare4 = ""

        generatedCode = codeFaireSquare
        generatedCode = generatedCode.replace("SIXONE", faireSquare1Base)
        generatedCode = generatedCode.replace("SIXTWO", faireSquare2Base)
        generatedCode = generatedCode.replace("SIXTHREE", faireSquare3Base)
        generatedCode = generatedCode.replace("SIXFOUR", faireSquare4Base)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def savePresetItems4(self):
        if not self.miniPrice4.get() or not self.miniWeight4.get() or not self.megaPrice4.get() or not self.megaWeight4.get() or not self.superMegaPrice4.get() or not self.superMegaWeight4.get() or not self.superMiniPrice4.get() or not self.superMiniWeight4.get() or not self.miniMegaHammerPrice4.get() or not self.miniMegaHammerWeight4.get() or not self.warpPipePrice4.get() or not self.warpPipeWeight4.get() or not self.swapCardPrice4.get() or not self.swapCardWeight4.get() or not self.sparkyStickerPrice4.get() or not self.sparkyStickerWeight4.get() or not self.bowserSuitPrice4.get() or not self.bowserSuitWeight4.get() or not self.gaddlightPrice4.get() or not self.gaddlightWeight4.get() or not self.chompCallPrice4.get() or not self.chompCallWeight4.get() or not self.crystalBallPrice4.get() or not self.crystalBallWeight4.get() or not self.magicLampPrice4.get() or not self.magicLampWeight4.get() or not self.itemBagPrice4.get()  or not self.itemBagWeight4.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return

        miniPrice4 = self.miniPrice4.get()
        miniWeight4 = self.miniWeight4.get()

        megaPrice4 = self.megaPrice4.get()
        megaWeight4 = self.megaWeight4.get()

        superMiniPrice4 = self.superMiniPrice4.get()
        superMiniWeight4 = self.superMiniWeight4.get()

        superMegaPrice4 = self.superMegaPrice4.get()
        superMegaWeight4 = self.superMegaWeight4.get()

        miniMegaHammerPrice4 = self.miniMegaHammerPrice4.get()
        miniMegaHammerWeight4 = self.miniMegaHammerWeight4.get()

        warpPipePrice4 = self.warpPipePrice4.get()
        warpPipeWeight4 = self.warpPipeWeight4.get()

        swapCardPrice4 = self.swapCardPrice4.get()
        swapCardWeight4 = self.swapCardWeight4.get()

        sparkyStickerPrice4 = self.sparkyStickerPrice4.get()
        sparkyStickerWeight4 = self.sparkyStickerWeight4.get()

        gaddlightPrice4 = self.gaddlightPrice4.get()
        gaddlightWeight4 = self.gaddlightWeight4.get()

        chompCallPrice4 = self.chompCallPrice4.get()
        chompCallWeight4 = self.chompCallWeight4.get()

        bowserSuitPrice4 = self.bowserSuitPrice4.get()
        bowserSuitWeight4 = self.bowserSuitWeight4.get()

        crystalBallPrice4 = self.crystalBallPrice4.get()
        crystalBallWeight4 = self.crystalBallWeight4.get()

        magicLampPrice4 = self.magicLampPrice4.get()
        magicLampWeight4 = self.magicLampWeight4.get()

        itemBagPrice4 = self.itemBagPrice4.get()
        itemBagWeight4 = self.itemBagWeight4.get()

        prices4 = [miniPrice4, megaPrice4, superMiniPrice4, superMegaPrice4, miniMegaHammerPrice4, warpPipePrice4, swapCardPrice4, sparkyStickerPrice4, gaddlightPrice4, chompCallPrice4, bowserSuitPrice4, crystalBallPrice4, magicLampPrice4, itemBagPrice4]
        weights4 = [miniWeight4, megaWeight4, superMiniWeight4, superMegaWeight4, miniMegaHammerWeight4, warpPipeWeight4, swapCardWeight4, sparkyStickerWeight4, gaddlightWeight4, chompCallWeight4, bowserSuitWeight4, crystalBallWeight4, magicLampWeight4, itemBagWeight4]
     
        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
        if file_path:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Prices', 'Weights'])
                for price, weight in zip(prices4, weights4):
                    writer.writerow([price, weight])
            print("MPT file saved successfully!")
            createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)



    def loadPresetItems4(self):
        file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
        if file_path:
            prices4In = []
            weights4In = []
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    prices4In.append(float(row[0]))
                    weights4In.append(float(row[1]))

            # Define a list of Entry widget attributes
            pricesNames4 = [self.miniPrice4, self.megaPrice4, self.superMiniPrice4, self.superMegaPrice4, self.miniMegaHammerPrice4, self.warpPipePrice4, self.swapCardPrice4, self.sparkyStickerPrice4, self.gaddlightPrice4, self.chompCallPrice4, self.bowserSuitPrice4, self.crystalBallPrice4, self.magicLampPrice4, self.itemBagPrice4]
            weightsNames4 = [self.miniWeight4, self.megaWeight4, self.superMiniWeight4, self.superMegaWeight4, self.miniMegaHammerWeight4, self.warpPipeWeight4, self.swapCardWeight4, self.sparkyStickerWeight4, self.gaddlightWeight4, self.chompCallWeight4, self.bowserSuitWeight4, self.crystalBallWeight4, self.magicLampWeight4, self.itemBagWeight4]

            # Update widgets with loaded values
            for index, widget in enumerate(pricesNames4):
                if widget and index < len(prices4In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(prices4In[index]))

            for index, widget in enumerate(weightsNames4):
                if widget and index < len(weights4In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(weights4In[index]))
            print("MPT file laoded successfully!")
            createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

    def actionBattle4(self):
        if not self.battle41.get() and not self.battle42.get() and not self.battle43.get() and not self.battle44.get() and not self.battle45.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return

        battle41Base = self.battle41.get()
        battle42Base = self.battle42.get()
        battle43Base = self.battle43.get()
        battle44Base = self.battle44.get()
        battle45Base = self.battle45.get()

        try:
            battle41 = hex(int(self.battle41.get()))
            if len(battle41) == 4:
                battle41 = battle41[2:]
            elif len(battle41) == 3:
                battle41 = "0" + battle41[2:]
        except:
            battle41 = "DUMMY"

        try:
            battle42 = hex(int(self.battle42.get()))
            if len(battle42) == 4:
                battle42 = battle42[2:]
            elif len(battle42) == 3:
                battle42 = "0" + battle42[2:]
        except:
            battle42 = "DUMMY"

        try:
            battle43 = hex(int(self.battle43.get()))
            if len(battle43) == 4:
                battle43 = battle43[2:]
            elif len(battle43) == 3:
                battle43 = "0" + battle43[2:]
        except:
            battle43 = "DUMMY"

        try:
            battle44 = hex(int(self.battle44.get()))
            if len(battle44) == 4:
                battle44 = battle44[2:]
            elif len(battle44) == 3:
                battle44 = "0" + battle44[2:]
        except:
            battle44 = "DUMMY"

        try:
            battle45 = hex(int(self.battle45.get()))
            if len(battle45) == 4:
                battle45 = battle45[2:]
            elif len(battle45) == 3:
                battle45 = "0" + battle45[2:]
        except:
            battle45 = "DUMMY"

        codebattle4 = getBattleAmountFour(battle41, battle42, battle43, battle44, battle45)
        
        if battle41 == "DUMMY":
            battle41 = ""
        if battle42 == "DUMMY":
            battle42 = ""
        if battle43 == "DUMMY":
            battle43 = ""
        if battle44 == "DUMMY":
            battle44 = ""
        if battle45 == "DUMMY":
            battle45 = ""

        generatedCode = codebattle4
        generatedCode = generatedCode.replace("FOURBATTLE1", battle41Base)
        generatedCode = generatedCode.replace("FOURBATTLE2", battle42Base)
        generatedCode = generatedCode.replace("FOURBATTLE3", battle43Base)
        generatedCode = generatedCode.replace("FOURBATTLE4", battle44Base)
        generatedCode = generatedCode.replace("FOURBATTLE5", battle45Base)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonFourItem(self):
        if not self.miniPrice4.get() or not self.miniWeight4.get() or not self.megaPrice4.get() or not self.megaWeight4.get() or not self.superMegaPrice4.get() or not self.superMegaWeight4.get() or not self.superMiniPrice4.get() or not self.superMiniWeight4.get() or not self.miniMegaHammerPrice4.get() or not self.miniMegaHammerWeight4.get() or not self.warpPipePrice4.get() or not self.warpPipeWeight4.get() or not self.swapCardPrice4.get() or not self.swapCardWeight4.get() or not self.sparkyStickerPrice4.get() or not self.sparkyStickerWeight4.get() or not self.bowserSuitPrice4.get() or not self.bowserSuitWeight4.get() or not self.gaddlightPrice4.get() or not self.gaddlightWeight4.get() or not self.chompCallPrice4.get() or not self.chompCallWeight4.get() or not self.crystalBallPrice4.get() or not self.crystalBallWeight4.get() or not self.magicLampPrice4.get() or not self.magicLampWeight4.get() or not self.itemBagPrice4.get()  or not self.itemBagWeight4.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return

        miniPrice4 = self.miniPrice4.get()
        miniWeight4 = self.miniWeight4.get()

        megaPrice4 = self.megaPrice4.get()
        megaWeight4 = self.megaWeight4.get()

        superMiniPrice4 = self.superMiniPrice4.get()
        superMiniWeight4 = self.superMiniWeight4.get()

        superMegaPrice4 = self.superMegaPrice4.get()
        superMegaWeight4 = self.superMegaWeight4.get()

        miniMegaHammerPrice4 = self.miniMegaHammerPrice4.get()
        miniMegaHammerWeight4 = self.miniMegaHammerWeight4.get()

        warpPipePrice4 = self.warpPipePrice4.get()
        warpPipeWeight4 = self.warpPipeWeight4.get()

        swapCardPrice4 = self.swapCardPrice4.get()
        swapCardWeight4 = self.swapCardWeight4.get()

        sparkyStickerPrice4 = self.sparkyStickerPrice4.get()
        sparkyStickerWeight4 = self.sparkyStickerWeight4.get()

        gaddlightPrice4 = self.gaddlightPrice4.get()
        gaddlightWeight4 = self.gaddlightWeight4.get()

        chompCallPrice4 = self.chompCallPrice4.get()
        chompCallWeight4 = self.chompCallWeight4.get()

        bowserSuitPrice4 = self.bowserSuitPrice4.get()
        bowserSuitWeight4 = self.bowserSuitWeight4.get()

        crystalBallPrice4 = self.crystalBallPrice4.get()
        crystalBallWeight4 = self.crystalBallWeight4.get()

        magicLampPrice4 = self.magicLampPrice4.get()
        magicLampWeight4 = self.magicLampWeight4.get()

        itemBagPrice4 = self.itemBagPrice4.get()
        itemBagWeight4 = self.itemBagWeight4.get()

        orbWeightTotal = int(miniWeight4) + int(megaWeight4) + int(superMiniWeight4) + int(superMegaWeight4) + int(miniMegaHammerWeight4) + int(warpPipeWeight4) + int(swapCardWeight4) + int(sparkyStickerWeight4) + int(gaddlightWeight4) + int(chompCallWeight4) + int(bowserSuitWeight4) + int(crystalBallWeight4) + int(magicLampWeight4) + int(itemBagWeight4)
        orbPriceMin = find_lowest_integer(*[int(miniPrice4), int(megaPrice4), int(superMiniPrice4), int(superMegaPrice4), int(miniMegaHammerPrice4), int(warpPipePrice4), int(swapCardPrice4), int(sparkyStickerPrice4), int(gaddlightPrice4), int(chompCallPrice4), int(bowserSuitPrice4), int(crystalBallPrice4), int(magicLampPrice4), int(itemBagPrice4)])

        miniWeight4 = (int(miniWeight4) / orbWeightTotal) * 100
        megaWeight4 = (int(megaWeight4) / orbWeightTotal) * 100
        superMegaWeight4 = (int(superMegaWeight4) / orbWeightTotal) * 100
        superMiniWeight4 = (int(superMiniWeight4) / orbWeightTotal) * 100
        miniMegaHammerWeight4 = (int(miniMegaHammerWeight4) / orbWeightTotal) * 100
        warpPipeWeight4 = (int(warpPipeWeight4) / orbWeightTotal) * 100
        swapCardWeight4 = (int(swapCardWeight4) / orbWeightTotal) * 100
        sparkyStickerWeight4 = (int(sparkyStickerWeight4) / orbWeightTotal) * 100
        gaddlightWeight4 = (int(gaddlightWeight4) / orbWeightTotal) * 100
        chompCallWeight4 = (int(chompCallWeight4) / orbWeightTotal) * 100
        bowserSuitWeight4 = (int(bowserSuitWeight4) / orbWeightTotal) * 100
        crystalBallWeight4 = (int(crystalBallWeight4) / orbWeightTotal) * 100
        magicLampWeight4 = (int(magicLampWeight4) / orbWeightTotal) * 100
        itemBagWeight4 = (int(itemBagWeight4) / orbWeightTotal) * 100

        try:
            miniWeight4 = hex(int(miniWeight4))
            if len(miniWeight4) == 4:
                miniWeight4 = miniWeight4[2:]
            elif len(miniWeight4) == 3:
                miniWeight4 = "0" + miniWeight4[2:]
        except:
            miniWeight4 = "00"

        try:
            miniPrice4 = hex(int(miniPrice4))
            if len(miniPrice4) == 4:
                miniPrice4 = miniPrice4[2:]
            elif len(miniPrice4) == 3:
                miniPrice4 = "0" + miniPrice4[2:]
        except:
            miniPrice4 = "00"        

        try:
            megaWeight4 = hex(int(megaWeight4))
            if len(megaWeight4) == 4:
                megaWeight4 = megaWeight4[2:]
            elif len(megaWeight4) == 3:
                megaWeight4 = "0" + megaWeight4[2:]
        except:
            megaWeight4 = "00"

        try:
            megaPrice4 = hex(int(megaPrice4))
            if len(megaPrice4) == 4:
                megaPrice4 = megaPrice4[2:]
            elif len(megaPrice4) == 3:
                megaPrice4 = "0" + megaPrice4[2:]
        except:
            megaPrice4 = "00"

        try:
            superMiniWeight4 = hex(int(superMiniWeight4))
            if len(superMiniWeight4) == 4:
                superMiniWeight4 = superMiniWeight4[2:]
            elif len(superMiniWeight4) == 3:
                superMiniWeight4 = "0" + superMiniWeight4[2:]
        except:
            superMiniWeight4 = "00"

        try:
            superMiniPrice4 = hex(int(superMiniPrice4))
            if len(superMiniPrice4) == 4:
                superMiniPrice4 = superMiniPrice4[2:]
            elif len(superMiniPrice4) == 3:
                superMiniPrice4 = "0" + superMiniPrice4[2:]
        except:
            superMiniPrice4 = "00"

        try:
            superMegaWeight4 = hex(int(superMegaWeight4))
            if len(superMegaWeight4) == 4:
                superMegaWeight4 = superMegaWeight4[2:]
            elif len(superMegaWeight4) == 3:
                superMegaWeight4 = "0" + superMegaWeight4[2:]
        except:
            superMegaWeight4 = "00"

        try:
            superMegaPrice4 = hex(int(superMegaPrice4))
            if len(superMegaPrice4) == 4:
                superMegaPrice4 = superMegaPrice4[2:]
            elif len(superMegaPrice4) == 3:
                superMegaPrice4 = "0" + superMegaPrice4[2:]
        except:
            superMegaPrice4 = "00"

        try:
            miniMegaHammerWeight4 = hex(int(miniMegaHammerWeight4))
            if len(miniMegaHammerWeight4) == 4:
                miniMegaHammerWeight4 = miniMegaHammerWeight4[2:]
            elif len(miniMegaHammerWeight4) == 3:
                miniMegaHammerWeight4 = "0" + miniMegaHammerWeight4[2:]
        except:
            miniMegaHammerWeight4 = "00"

        try:
            miniMegaHammerPrice4 = hex(int(miniMegaHammerPrice4))
            if len(miniMegaHammerPrice4) == 4:
                miniMegaHammerPrice4 = miniMegaHammerPrice4[2:]
            elif len(miniMegaHammerPrice4) == 3:
                miniMegaHammerPrice4 = "0" + miniMegaHammerPrice4[2:]
        except:
            miniMegaHammerPrice4 = "00"

        try:
            warpPipeWeight4 = hex(int(warpPipeWeight4))
            if len(warpPipeWeight4) == 4:
                warpPipeWeight4 = warpPipeWeight4[2:]
            elif len(warpPipeWeight4) == 3:
                warpPipeWeight4 = "0" + warpPipeWeight4[2:]
        except:
            warpPipeWeight4 = "00"

        try:
            warpPipePrice4 = hex(int(warpPipePrice4))
            if len(warpPipePrice4) == 4:
                warpPipePrice4 = warpPipePrice4[2:]
            elif len(warpPipePrice4) == 3:
                warpPipePrice4 = "0" + warpPipePrice4[2:]
        except:
            warpPipePrice4 = "00"

        try:
            swapCardWeight4 = hex(int(swapCardWeight4))
            if len(swapCardWeight4) == 4:
                swapCardWeight4 = swapCardWeight4[2:]
            elif len(swapCardWeight4) == 3:
                swapCardWeight4 = "0" + swapCardWeight4[2:]
        except:
            swapCardWeight4 = "00"

        try:
            swapCardPrice4 = hex(int(swapCardPrice4))
            if len(swapCardPrice4) == 4:
                swapCardPrice4 = swapCardPrice4[2:]
            elif len(swapCardPrice4) == 3:
                swapCardPrice4 = "0" + swapCardPrice4[2:]
        except:
            swapCardPrice4 = "00"

        try:
            sparkyStickerWeight4 = hex(int(sparkyStickerWeight4))
            if len(sparkyStickerWeight4) == 4:
                sparkyStickerWeight4 = sparkyStickerWeight4[2:]
            elif len(sparkyStickerWeight4) == 3:
                sparkyStickerWeight4 = "0" + sparkyStickerWeight4[2:]
        except:
            sparkyStickerWeight4 = "00"

        try:
            sparkyStickerPrice4 = hex(int(sparkyStickerPrice4))
            if len(sparkyStickerPrice4) == 4:
                sparkyStickerPrice4 = sparkyStickerPrice4[2:]
            elif len(sparkyStickerPrice4) == 3:
                sparkyStickerPrice4 = "0" + sparkyStickerPrice4[2:]
        except:
            sparkyStickerPrice4 = "00"

        try:
            gaddlightWeight4 = hex(int(gaddlightWeight4))
            if len(gaddlightWeight4) == 4:
                gaddlightWeight4 = gaddlightWeight4[2:]
            elif len(gaddlightWeight4) == 3:
                gaddlightWeight4 = "0" + gaddlightWeight4[2:]
        except:
            gaddlightWeight4 = "00"

        try:
            gaddlightPrice4 = hex(int(gaddlightPrice4))
            if len(gaddlightPrice4) == 4:
                gaddlightPrice4 = gaddlightPrice4[2:]
            elif len(gaddlightPrice4) == 3:
                gaddlightPrice4 = "0" + gaddlightPrice4[2:]
        except:
            gaddlightPrice4 = "00"

        try:
            chompCallWeight4 = hex(int(chompCallWeight4))
            if len(chompCallWeight4) == 4:
                chompCallWeight4 = chompCallWeight4[2:]
            elif len(chompCallWeight4) == 3:
                chompCallWeight4 = "0" + chompCallWeight4[2:]
        except:
            chompCallWeight4 = "00"

        try:
            chompCallPrice4 = hex(int(chompCallPrice4))
            if len(chompCallPrice4) == 4:
                chompCallPrice4 = chompCallPrice4[2:]
            elif len(chompCallPrice4) == 3:
                chompCallPrice4 = "0" + chompCallPrice4[2:]
        except:
            chompCallPrice4 = "00"

        try:
            bowserSuitWeight4 = hex(int(bowserSuitWeight4))
            if len(bowserSuitWeight4) == 4:
                bowserSuitWeight4 = bowserSuitWeight4[2:]
            elif len(bowserSuitWeight4) == 3:
                bowserSuitWeight4 = "0" + bowserSuitWeight4[2:]
        except:
            bowserSuitWeight4 = "00"

        try:
            bowserSuitPrice4 = hex(int(bowserSuitPrice4))
            if len(bowserSuitPrice4) == 4:
                bowserSuitPrice4 = bowserSuitPrice4[2:]
            elif len(bowserSuitPrice4) == 3:
                bowserSuitPrice4 = "0" + bowserSuitPrice4[2:]
        except:
            bowserSuitPrice4 = "00"

        try:
            crystalBallWeight4 = hex(int(crystalBallWeight4))
            if len(crystalBallWeight4) == 4:
                crystalBallWeight4 = crystalBallWeight4[2:]
            elif len(crystalBallWeight4) == 3:
                crystalBallWeight4 = "0" + crystalBallWeight4[2:]
        except:
            crystalBallWeight4 = "00"

        try:
            crystalBallPrice4 = hex(int(crystalBallPrice4))
            if len(crystalBallPrice4) == 4:
                crystalBallPrice4 = crystalBallPrice4[2:]
            elif len(crystalBallPrice4) == 3:
                crystalBallPrice4 = "0" + crystalBallPrice4[2:]
        except:
            crystalBallPrice4 = "00"

        try:
            magicLampWeight4 = hex(int(magicLampWeight4))
            if len(magicLampWeight4) == 4:
                magicLampWeight4 = magicLampWeight4[2:]
            elif len(magicLampWeight4) == 3:
                magicLampWeight4 = "0" + magicLampWeight4[2:]
        except:
            magicLampWeight4 = "00"

        try:
            magicLampPrice4 = hex(int(magicLampPrice4))
            if len(magicLampPrice4) == 4:
                magicLampPrice4 = magicLampPrice4[2:]
            elif len(magicLampPrice4) == 3:
                magicLampPrice4 = "0" + magicLampPrice4[2:]
        except:
            magicLampPrice4 = "00"

        try:
            itemBagWeight4 = hex(int(itemBagWeight4))
            if len(itemBagWeight4) == 4:
                itemBagWeight4 = itemBagWeight4[2:]
            elif len(itemBagWeight4) == 3:
                itemBagWeight4 = "0" + itemBagWeight4[2:]
        except:
            itemBagWeight4 = "00"

        try:
            itemBagPrice4 = hex(int(itemBagPrice4))
            if len(itemBagPrice4) == 4:
                itemBagPrice4 = itemBagPrice4[2:]
            elif len(itemBagPrice4) == 3:
                itemBagPrice4 = "0" + itemBagPrice4[2:]
        except:
            itemBagPrice4 = "00"

        orbPriceMin = hex(int(orbPriceMin))
        print(orbPriceMin)
        if len(orbPriceMin) == 4:
            orbPriceMin = "00" + orbPriceMin[2:]
        elif len(orbPriceMin) == 3:
            orbPriceMin = "000" + orbPriceMin[2:]

        generatedCode = getItemModsFour(miniPrice4, miniWeight4, megaPrice4, megaWeight4, superMiniPrice4, superMiniWeight4, superMegaPrice4, superMegaWeight4, miniMegaHammerPrice4, miniMegaHammerWeight4, warpPipePrice4, warpPipeWeight4, swapCardPrice4, swapCardWeight4, sparkyStickerPrice4, sparkyStickerWeight4, gaddlightPrice4, gaddlightWeight4, chompCallPrice4, chompCallWeight4, bowserSuitPrice4, bowserSuitWeight4, crystalBallPrice4, crystalBallWeight4, magicLampPrice4, magicLampWeight4, itemBagPrice4, itemBagWeight4, orbPriceMin)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated code copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonSevenOrb(self):
        if not self.mushroomCapsuleWeight7.get() or not self.goldenMushroomCapsulePrice7.get() or not self.goldenMushroomCapsuleWeight7.get() or not self.slowMushroomCapsulePrice7.get() or not self.slowMushroomCapsuleWeight7.get() or not self.metalMushroomCapsulePrice7.get() or not self.metalMushroomCapsuleWeight7.get() or not self.flutterCapsulePrice7.get() or not self.flutterCapsuleWeight7.get() or not self.cannonCapsulePrice7.get() or not self.cannonCapsuleWeight7.get() or not self.snackCapsulePrice7.get() or not self.snackCapsuleWeight7.get() or not self.lakituCapsulePrice7.get() or not self.lakituCapsuleWeight7.get() or not self.hammerBroCapsuleWeight7.get() or not self.hammerBroCapsulePrice7.get() or not self.plantCapsulePrice7.get() or not self.plantCapsuleWeight7.get() or not self.spearCapsuleWeight7.get() or not self.spearCapsulePrice7.get() or not self.kamekCapsuleWeight7.get() or not self.kamekCapsulePrice7.get() or not self.toadyCapsuleWeight7.get() or not self.toadyCapsulePrice7.get() or not self.blizzardCapsuleWeight7.get() or not self.blizzardCapsulePrice7.get() or not self.banditCapsulePrice7.get() or not self.banditCapsuleWeight7.get() or not self.pinkBooCapsuleWeight7.get() or not self.pinkBooCapsulePrice7.get() or not self.spinyCapsulePrice7.get() or not self.spinyCapsuleWeight7.get() or not self.zapCapsulePrice7.get() or not self.zapCapsuleWeight7.get() or not self.tweesterCapsulePrice7.get() or not self.tweesterCapsuleWeight7.get() or not self.thwompCapsulePrice7.get() or not self.thwompCapsuleWeight7.get() or not self.warpCapsulePrice7.get() or not self.warpCapsuleWeight7.get() or not self.bombCapsulePrice7.get() or not self.bombCapsuleWeight7.get() or not self.fireballCapsulePrice7.get() or not self.fireballCapsuleWeight7.get() or not self.eggCapsulePrice7.get() or not self.eggCapsuleWeight7.get() or not self.flowerCapsulePrice7.get() or not self.flowerCapsuleWeight7.get() or not self.vacuumCapsulePrice7.get() or not self.vacuumCapsuleWeight7.get() or not self.magicCapsulePrice7.get() or not self.magicCapsuleWeight7.get() or not self.tripleCapsulePrice7.get() or not self.tripleCapsuleWeight7.get() or not self.koopaCapsulePrice7.get() or not self.koopaCapsuleWeight7.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return
        
        mushroomCapsuleWeight7 = self.mushroomCapsuleWeight7.get()
        
        goldenMushroomCapsulePrice7 = self.goldenMushroomCapsulePrice7.get()
        goldenMushroomCapsuleWeight7 = self.goldenMushroomCapsuleWeight7.get()

        slowMushroomCapsulePrice7 = self.slowMushroomCapsulePrice7.get()
        slowMushroomCapsuleWeight7 = self.slowMushroomCapsuleWeight7.get()

        metalMushroomCapsulePrice7 = self.metalMushroomCapsulePrice7.get()
        metalMushroomCapsuleWeight7 = self.metalMushroomCapsuleWeight7.get()

        flutterCapsulePrice7 = self.flutterCapsulePrice7.get()
        flutterCapsuleWeight7 = self.flutterCapsuleWeight7.get()

        cannonCapsulePrice7 = self.cannonCapsulePrice7.get()
        cannonCapsuleWeight7 = self.cannonCapsuleWeight7.get()

        snackCapsulePrice7 = self.snackCapsulePrice7.get()
        snackCapsuleWeight7 = self.snackCapsuleWeight7.get()

        lakituCapsulePrice7 = self.lakituCapsulePrice7.get()
        lakituCapsuleWeight7 = self.lakituCapsuleWeight7.get()

        hammerBroCapsulePrice7 = self.hammerBroCapsulePrice7.get()
        hammerBroCapsuleWeight7 = self.hammerBroCapsuleWeight7.get()

        plantCapsulePrice7 = self.plantCapsulePrice7.get()
        plantCapsuleWeight7 = self.plantCapsuleWeight7.get()

        spearCapsulePrice7 = self.spearCapsulePrice7.get()
        spearCapsuleWeight7 = self.spearCapsuleWeight7.get()

        kamekCapsulePrice7 = self.kamekCapsulePrice7.get()
        kamekCapsuleWeight7 = self.kamekCapsuleWeight7.get()

        toadyCapsulePrice7 = self.toadyCapsulePrice7.get()
        toadyCapsuleWeight7 = self.toadyCapsuleWeight7.get()

        blizzardCapsulePrice7 = self.blizzardCapsulePrice7.get()
        blizzardCapsuleWeight7 = self.blizzardCapsuleWeight7.get()

        banditCapsulePrice7 = self.banditCapsulePrice7.get()
        banditCapsuleWeight7 = self.banditCapsuleWeight7.get()

        pinkBooCapsulePrice7 = self.pinkBooCapsulePrice7.get()
        pinkBooCapsuleWeight7 = self.pinkBooCapsuleWeight7.get()

        spinyCapsulePrice7 = self.spinyCapsulePrice7.get()
        spinyCapsuleWeight7 = self.spinyCapsuleWeight7.get()

        zapCapsulePrice7 = self.zapCapsulePrice7.get()
        zapCapsuleWeight7 = self.zapCapsuleWeight7.get()

        tweesterCapsulePrice7 = self.tweesterCapsulePrice7.get()
        tweesterCapsuleWeight7 = self.tweesterCapsuleWeight7.get()

        thwompCapsulePrice7 = self.thwompCapsulePrice7.get()
        thwompCapsuleWeight7 = self.thwompCapsuleWeight7.get()

        warpCapsulePrice7 = self.warpCapsulePrice7.get()
        warpCapsuleWeight7 = self.warpCapsuleWeight7.get()

        bombCapsulePrice7 = self.bombCapsulePrice7.get()
        bombCapsuleWeight7 = self.bombCapsuleWeight7.get()

        fireballCapsulePrice7 = self.fireballCapsulePrice7.get()
        fireballCapsuleWeight7 = self.fireballCapsuleWeight7.get()

        flowerCapsulePrice7 = self.flowerCapsulePrice7.get()
        flowerCapsuleWeight7 = self.flowerCapsuleWeight7.get()

        eggCapsulePrice7 = self.eggCapsulePrice7.get()
        eggCapsuleWeight7 = self.eggCapsuleWeight7.get()

        vacuumCapsulePrice7 = self.vacuumCapsulePrice7.get()
        vacuumCapsuleWeight7 = self.vacuumCapsuleWeight7.get()

        magicCapsulePrice7 = self.magicCapsulePrice7.get()
        magicCapsuleWeight7 = self.magicCapsuleWeight7.get()

        tripleCapsulePrice7 = self.tripleCapsulePrice7.get()
        tripleCapsuleWeight7 = self.tripleCapsuleWeight7.get()

        koopaCapsulePrice7 = self.koopaCapsulePrice7.get()
        koopaCapsuleWeight7 = self.koopaCapsuleWeight7.get()

        orbWeightTotal = int(mushroomCapsuleWeight7) + int(goldenMushroomCapsuleWeight7) + int(metalMushroomCapsuleWeight7) + int(slowMushroomCapsuleWeight7) + int(flutterCapsuleWeight7) + int(cannonCapsuleWeight7) + int(snackCapsuleWeight7) + int(lakituCapsuleWeight7) + int(hammerBroCapsuleWeight7) + int(plantCapsuleWeight7) + int(spearCapsuleWeight7) + int(kamekCapsuleWeight7) + int(toadyCapsuleWeight7) + int(blizzardCapsuleWeight7) + int(banditCapsuleWeight7) + int(pinkBooCapsuleWeight7) + int(spinyCapsuleWeight7) + int(zapCapsuleWeight7) + int(tweesterCapsuleWeight7) + int(thwompCapsuleWeight7) + int(warpCapsuleWeight7) + int(bombCapsuleWeight7) + int(fireballCapsuleWeight7) + int(flowerCapsuleWeight7) + int(eggCapsuleWeight7) + int(vacuumCapsuleWeight7) + int(magicCapsuleWeight7) + int(tripleCapsuleWeight7) + int(koopaCapsuleWeight7)

        mushroomCapsuleWeight7 = (int(mushroomCapsuleWeight7) / orbWeightTotal) * 100
        goldenMushroomCapsuleWeight7 = (int(goldenMushroomCapsuleWeight7) / orbWeightTotal) * 100
        metalMushroomCapsuleWeight7 = (int(metalMushroomCapsuleWeight7) / orbWeightTotal) * 100
        slowMushroomCapsuleWeight7 = (int(slowMushroomCapsuleWeight7) / orbWeightTotal) * 100
        flutterCapsuleWeight7 = (int(flutterCapsuleWeight7) / orbWeightTotal) * 100
        cannonCapsuleWeight7 = (int(cannonCapsuleWeight7) / orbWeightTotal) * 100
        snackCapsuleWeight7 = (int(snackCapsuleWeight7) / orbWeightTotal) * 100
        lakituCapsuleWeight7 = (int(lakituCapsuleWeight7) / orbWeightTotal) * 100
        hammerBroCapsuleWeight7 = (int(hammerBroCapsuleWeight7) / orbWeightTotal) * 100
        plantCapsuleWeight7 = (int(plantCapsuleWeight7) / orbWeightTotal) * 100
        spearCapsuleWeight7 = (int(spearCapsuleWeight7) / orbWeightTotal) * 100
        kamekCapsuleWeight7 = (int(kamekCapsuleWeight7) / orbWeightTotal) * 100
        toadyCapsuleWeight7 = (int(toadyCapsuleWeight7) / orbWeightTotal) * 100
        blizzardCapsuleWeight7 = (int(blizzardCapsuleWeight7) / orbWeightTotal) * 100
        banditCapsuleWeight7 = (int(banditCapsuleWeight7) / orbWeightTotal) * 100
        pinkBooCapsuleWeight7 = (int(pinkBooCapsuleWeight7) / orbWeightTotal) * 100
        spinyCapsuleWeight7 = (int(spinyCapsuleWeight7) / orbWeightTotal) * 100
        zapCapsuleWeight7 = (int(zapCapsuleWeight7) / orbWeightTotal) * 100
        tweesterCapsuleWeight7 = (int(tweesterCapsuleWeight7) / orbWeightTotal) * 100
        thwompCapsuleWeight7 = (int(thwompCapsuleWeight7) / orbWeightTotal) * 100
        warpCapsuleWeight7 = (int(warpCapsuleWeight7) / orbWeightTotal) * 100
        bombCapsuleWeight7 = (int(bombCapsuleWeight7) / orbWeightTotal) * 100
        fireballCapsuleWeight7 = (int(fireballCapsuleWeight7) / orbWeightTotal) * 100
        flowerCapsuleWeight7 = (int(flowerCapsuleWeight7) / orbWeightTotal) * 100
        eggCapsuleWeight7 = (int(eggCapsuleWeight7) / orbWeightTotal) * 100
        vacuumCapsuleWeight7 = (int(vacuumCapsuleWeight7) / orbWeightTotal) * 100
        magicCapsuleWeight7 = (int(magicCapsuleWeight7) / orbWeightTotal) * 100
        tripleCapsuleWeight7 = (int(tripleCapsuleWeight7) / orbWeightTotal) * 100
        koopaCapsuleWeight7 = (int(koopaCapsuleWeight7) / orbWeightTotal) * 100
        try:
            mushroomCapsuleWeight7 = hex(int(mushroomCapsuleWeight7))
            if len(mushroomCapsuleWeight7) == 4:
                mushroomCapsuleWeight7 = mushroomCapsuleWeight7[2:]
            elif len(mushroomCapsuleWeight7) == 3:
                mushroomCapsuleWeight7 = "0" + mushroomCapsuleWeight7[2:]
        except:
            mushroomCapsuleWeight7 = "00"

        try:
            goldenMushroomCapsuleWeight7 = hex(int(goldenMushroomCapsuleWeight7))
            if len(goldenMushroomCapsuleWeight7) == 4:
                goldenMushroomCapsuleWeight7 = goldenMushroomCapsuleWeight7[2:]
            elif len(goldenMushroomCapsuleWeight7) == 3:
                goldenMushroomCapsuleWeight7 = "0" + goldenMushroomCapsuleWeight7[2:]
        except:
            goldenMushroomCapsuleWeight7 = "00"

        try:
            goldenMushroomCapsulePrice7 = hex(int(goldenMushroomCapsulePrice7))
            if len(goldenMushroomCapsulePrice7) == 4:
                goldenMushroomCapsulePrice7 = goldenMushroomCapsulePrice7[2:]
            elif len(goldenMushroomCapsulePrice7) == 3:
                goldenMushroomCapsulePrice7 = "0" + goldenMushroomCapsulePrice7[2:]
        except:
            goldenMushroomCapsulePrice7 = "00"
       
        try:
            slowMushroomCapsuleWeight7 = hex(int(slowMushroomCapsuleWeight7))
            if len(slowMushroomCapsuleWeight7) == 4:
                slowMushroomCapsuleWeight7 = slowMushroomCapsuleWeight7[2:]
            elif len(slowMushroomCapsuleWeight7) == 3:
                slowMushroomCapsuleWeight7 = "0" + slowMushroomCapsuleWeight7[2:]
        except:
            slowMushroomCapsuleWeight7 = "00"

        try:
            slowMushroomCapsulePrice7 = hex(int(slowMushroomCapsulePrice7))
            if len(slowMushroomCapsulePrice7) == 4:
                slowMushroomCapsulePrice7 = slowMushroomCapsulePrice7[2:]
            elif len(slowMushroomCapsulePrice7) == 3:
                slowMushroomCapsulePrice7 = "0" + slowMushroomCapsulePrice7[2:]
        except:
            slowMushroomCapsulePrice7 = "00"

        try:
            metalMushroomCapsuleWeight7 = hex(int(metalMushroomCapsuleWeight7))
            if len(metalMushroomCapsuleWeight7) == 4:
                metalMushroomCapsuleWeight7 = metalMushroomCapsuleWeight7[2:]
            elif len(metalMushroomCapsuleWeight7) == 3:
                metalMushroomCapsuleWeight7 = "0" + metalMushroomCapsuleWeight7[2:]
        except:
            metalMushroomCapsuleWeight7 = "00"

        try:
            metalMushroomCapsulePrice7 = hex(int(metalMushroomCapsulePrice7))
            if len(metalMushroomCapsulePrice7) == 4:
                metalMushroomCapsulePrice7 = metalMushroomCapsulePrice7[2:]
            elif len(metalMushroomCapsulePrice7) == 3:
                metalMushroomCapsulePrice7 = "0" + metalMushroomCapsulePrice7[2:]
        except:
            metalMushroomCapsulePrice7 = "00"

        try:
            flutterCapsuleWeight7 = hex(int(flutterCapsuleWeight7))
            if len(flutterCapsuleWeight7) == 4:
                flutterCapsuleWeight7 = flutterCapsuleWeight7[2:]
            elif len(flutterCapsuleWeight7) == 3:
                flutterCapsuleWeight7 = "0" + flutterCapsuleWeight7[2:]
        except:
            flutterCapsuleWeight7 = "00"

        try:
            flutterCapsulePrice7 = hex(int(flutterCapsulePrice7))
            if len(flutterCapsulePrice7) == 4:
                flutterCapsulePrice7 = flutterCapsulePrice7[2:]
            elif len(flutterCapsulePrice7) == 3:
                flutterCapsulePrice7 = "0" + flutterCapsulePrice7[2:]
        except:
            flutterCapsulePrice7 = "00"

        try:
            cannonCapsuleWeight7 = hex(int(cannonCapsuleWeight7))
            if len(cannonCapsuleWeight7) == 4:
                cannonCapsuleWeight7 = cannonCapsuleWeight7[2:]
            elif len(cannonCapsuleWeight7) == 3:
                cannonCapsuleWeight7 = "0" + cannonCapsuleWeight7[2:]
        except:
            cannonCapsuleWeight7 = "00"

        try:
            cannonCapsulePrice7 = hex(int(cannonCapsulePrice7))
            if len(cannonCapsulePrice7) == 4:
                cannonCapsulePrice7 = cannonCapsulePrice7[2:]
            elif len(cannonCapsulePrice7) == 3:
                cannonCapsulePrice7 = "0" + cannonCapsulePrice7[2:]
        except:
            cannonCapsulePrice7 = "00"

        try:
            snackCapsuleWeight7 = hex(int(snackCapsuleWeight7))
            if len(snackCapsuleWeight7) == 4:
                snackCapsuleWeight7 = snackCapsuleWeight7[2:]
            elif len(snackCapsuleWeight7) == 3:
                snackCapsuleWeight7 = "0" + snackCapsuleWeight7[2:]
        except:
            snackCapsuleWeight7 = "00"

        try:
            snackCapsulePrice7 = hex(int(snackCapsulePrice7))
            if len(snackCapsulePrice7) == 4:
                snackCapsulePrice7 = snackCapsulePrice7[2:]
            elif len(snackCapsulePrice7) == 3:
                snackCapsulePrice7 = "0" + snackCapsulePrice7[2:]
        except:
            snackCapsulePrice7 = "00"

        try:
            lakituCapsuleWeight7 = hex(int(lakituCapsuleWeight7))
            if len(lakituCapsuleWeight7) == 4:
                lakituCapsuleWeight7 = lakituCapsuleWeight7[2:]
            elif len(lakituCapsuleWeight7) == 3:
                lakituCapsuleWeight7 = "0" + lakituCapsuleWeight7[2:]
        except:
            lakituCapsuleWeight7 = "00"

        try:
            lakituCapsulePrice7 = hex(int(lakituCapsulePrice7))
            if len(lakituCapsulePrice7) == 4:
                lakituCapsulePrice7 = lakituCapsulePrice7[2:]
            elif len(lakituCapsulePrice7) == 3:
                lakituCapsulePrice7 = "0" + lakituCapsulePrice7[2:]
        except:
            lakituCapsulePrice7 = "00"

        try:
            hammerBroCapsuleWeight7 = hex(int(hammerBroCapsuleWeight7))
            if len(hammerBroCapsuleWeight7) == 4:
                hammerBroCapsuleWeight7 = hammerBroCapsuleWeight7[2:]
            elif len(hammerBroCapsuleWeight7) == 3:
                hammerBroCapsuleWeight7 = "0" + hammerBroCapsuleWeight7[2:]
        except:
            hammerBroCapsuleWeight7 = "00"

        try:
            hammerBroCapsulePrice7 = hex(int(hammerBroCapsulePrice7))
            if len(hammerBroCapsulePrice7) == 4:
                hammerBroCapsulePrice7 = hammerBroCapsulePrice7[2:]
            elif len(hammerBroCapsulePrice7) == 3:
                hammerBroCapsulePrice7 = "0" + hammerBroCapsulePrice7[2:]
        except:
            hammerBroCapsulePrice7 = "00"

        try:
            plantCapsuleWeight7 = hex(int(plantCapsuleWeight7))
            if len(plantCapsuleWeight7) == 4:
                plantCapsuleWeight7 = plantCapsuleWeight7[2:]
            elif len(plantCapsuleWeight7) == 3:
                plantCapsuleWeight7 = "0" + plantCapsuleWeight7[2:]
        except:
            plantCapsuleWeight7 = "00"

        try:
            plantCapsulePrice7 = hex(int(plantCapsulePrice7))
            if len(plantCapsulePrice7) == 4:
                plantCapsulePrice7 = plantCapsulePrice7[2:]
            elif len(plantCapsulePrice7) == 3:
                plantCapsulePrice7 = "0" + plantCapsulePrice7[2:]
        except:
            plantCapsulePrice7 = "00"

        try:
            spearCapsuleWeight7 = hex(int(spearCapsuleWeight7))
            if len(spearCapsuleWeight7) == 4:
                spearCapsuleWeight7 = spearCapsuleWeight7[2:]
            elif len(spearCapsuleWeight7) == 3:
                spearCapsuleWeight7 = "0" + spearCapsuleWeight7[2:]
        except:
            spearCapsuleWeight7 = "00"

        try:
            spearCapsulePrice7 = hex(int(spearCapsulePrice7))
            if len(spearCapsulePrice7) == 4:
                spearCapsulePrice7 = spearCapsulePrice7[2:]
            elif len(spearCapsulePrice7) == 3:
                spearCapsulePrice7 = "0" + spearCapsulePrice7[2:]
        except:
            spearCapsulePrice7 = "00"

        try:
            kamekCapsuleWeight7 = hex(int(kamekCapsuleWeight7))
            if len(kamekCapsuleWeight7) == 4:
                kamekCapsuleWeight7 = kamekCapsuleWeight7[2:]
            elif len(kamekCapsuleWeight7) == 3:
                kamekCapsuleWeight7 = "0" + kamekCapsuleWeight7[2:]
        except:
            kamekCapsuleWeight7 = "00"

        try:
            kamekCapsulePrice7 = hex(int(kamekCapsulePrice7))
            if len(kamekCapsulePrice7) == 4:
                kamekCapsulePrice7 = kamekCapsulePrice7[2:]
            elif len(kamekCapsulePrice7) == 3:
                kamekCapsulePrice7 = "0" + kamekCapsulePrice7[2:]
        except:
            kamekCapsulePrice7 = "00"

        try:
            toadyCapsuleWeight7 = hex(int(toadyCapsuleWeight7))
            if len(toadyCapsuleWeight7) == 4:
                toadyCapsuleWeight7 = toadyCapsuleWeight7[2:]
            elif len(toadyCapsuleWeight7) == 3:
                toadyCapsuleWeight7 = "0" + toadyCapsuleWeight7[2:]
        except:
            toadyCapsuleWeight7 = "00"

        try:
            toadyCapsulePrice7 = hex(int(toadyCapsulePrice7))
            if len(toadyCapsulePrice7) == 4:
                toadyCapsulePrice7 = toadyCapsulePrice7[2:]
            elif len(toadyCapsulePrice7) == 3:
                toadyCapsulePrice7 = "0" + toadyCapsulePrice7[2:]
        except:
            toadyCapsulePrice7 = "00"

        try:
            blizzardCapsuleWeight7 = hex(int(blizzardCapsuleWeight7))
            if len(blizzardCapsuleWeight7) == 4:
                blizzardCapsuleWeight7 = blizzardCapsuleWeight7[2:]
            elif len(blizzardCapsuleWeight7) == 3:
                blizzardCapsuleWeight7 = "0" + blizzardCapsuleWeight7[2:]
        except:
            blizzardCapsuleWeight7 = "00"

        try:
            blizzardCapsulePrice7 = hex(int(blizzardCapsulePrice7))
            if len(blizzardCapsulePrice7) == 4:
                blizzardCapsulePrice7 = blizzardCapsulePrice7[2:]
            elif len(blizzardCapsulePrice7) == 3:
                blizzardCapsulePrice7 = "0" + blizzardCapsulePrice7[2:]
        except:
            blizzardCapsulePrice7 = "00"

        try:
            banditCapsuleWeight7 = hex(int(banditCapsuleWeight7))
            if len(banditCapsuleWeight7) == 4:
                banditCapsuleWeight7 = banditCapsuleWeight7[2:]
            elif len(banditCapsuleWeight7) == 3:
                banditCapsuleWeight7 = "0" + banditCapsuleWeight7[2:]
        except:
            banditCapsuleWeight7 = "00"

        try:
            banditCapsulePrice7 = hex(int(banditCapsulePrice7))
            if len(banditCapsulePrice7) == 4:
                banditCapsulePrice7 = banditCapsulePrice7[2:]
            elif len(banditCapsulePrice7) == 3:
                banditCapsulePrice7 = "0" + banditCapsulePrice7[2:]
        except:
            banditCapsulePrice7 = "00"

        try:
            pinkBooCapsuleWeight7 = hex(int(pinkBooCapsuleWeight7))
            if len(pinkBooCapsuleWeight7) == 4:
                pinkBooCapsuleWeight7 = pinkBooCapsuleWeight7[2:]
            elif len(pinkBooCapsuleWeight7) == 3:
                pinkBooCapsuleWeight7 = "0" + pinkBooCapsuleWeight7[2:]
        except:
            pinkBooCapsuleWeight7 = "00"

        try:
            pinkBooCapsulePrice7 = hex(int(pinkBooCapsulePrice7))
            if len(pinkBooCapsulePrice7) == 4:
                pinkBooCapsulePrice7 = pinkBooCapsulePrice7[2:]
            elif len(pinkBooCapsulePrice7) == 3:
                pinkBooCapsulePrice7 = "0" + pinkBooCapsulePrice7[2:]
        except:
            pinkBooCapsulePrice7 = "00"

        try:
            spinyCapsuleWeight7 = hex(int(spinyCapsuleWeight7))
            if len(spinyCapsuleWeight7) == 4:
                spinyCapsuleWeight7 = spinyCapsuleWeight7[2:]
            elif len(spinyCapsuleWeight7) == 3:
                spinyCapsuleWeight7 = "0" + spinyCapsuleWeight7[2:]
        except:
            spinyCapsuleWeight7 = "00"

        try:
            spinyCapsulePrice7 = hex(int(spinyCapsulePrice7))
            if len(spinyCapsulePrice7) == 4:
                spinyCapsulePrice7 = spinyCapsulePrice7[2:]
            elif len(spinyCapsulePrice7) == 3:
                spinyCapsulePrice7 = "0" + spinyCapsulePrice7[2:]
        except:
            spinyCapsulePrice7 = "00"

        try:
            zapCapsuleWeight7 = hex(int(zapCapsuleWeight7))
            if len(zapCapsuleWeight7) == 4:
                zapCapsuleWeight7 = zapCapsuleWeight7[2:]
            elif len(zapCapsuleWeight7) == 3:
                zapCapsuleWeight7 = "0" + zapCapsuleWeight7[2:]
        except:
            zapCapsuleWeight7 = "00"

        try:
            zapCapsulePrice7 = hex(int(zapCapsulePrice7))
            if len(zapCapsulePrice7) == 4:
                zapCapsulePrice7 = zapCapsulePrice7[2:]
            elif len(zapCapsulePrice7) == 3:
                zapCapsulePrice7 = "0" + zapCapsulePrice7[2:]
        except:
            zapCapsulePrice7 = "00"

        try:
            tweesterCapsuleWeight7 = hex(int(tweesterCapsuleWeight7))
            if len(tweesterCapsuleWeight7) == 4:
                tweesterCapsuleWeight7 = tweesterCapsuleWeight7[2:]
            elif len(tweesterCapsuleWeight7) == 3:
                tweesterCapsuleWeight7 = "0" + tweesterCapsuleWeight7[2:]
        except:
            tweesterCapsuleWeight7 = "00"

        try:
            tweesterCapsulePrice7 = hex(int(tweesterCapsulePrice7))
            if len(tweesterCapsulePrice7) == 4:
                tweesterCapsulePrice7 = tweesterCapsulePrice7[2:]
            elif len(tweesterCapsulePrice7) == 3:
                tweesterCapsulePrice7 = "0" + tweesterCapsulePrice7[2:]
        except:
            tweesterCapsulePrice7 = "00"

        try:
            thwompCapsuleWeight7 = hex(int(thwompCapsuleWeight7))
            if len(thwompCapsuleWeight7) == 4:
                thwompCapsuleWeight7 = thwompCapsuleWeight7[2:]
            elif len(thwompCapsuleWeight7) == 3:
                thwompCapsuleWeight7 = "0" + thwompCapsuleWeight7[2:]
        except:
            thwompCapsuleWeight7 = "00"

        try:
            thwompCapsulePrice7 = hex(int(thwompCapsulePrice7))
            if len(thwompCapsulePrice7) == 4:
                thwompCapsulePrice7 = thwompCapsulePrice7[2:]
            elif len(thwompCapsulePrice7) == 3:
                thwompCapsulePrice7 = "0" + thwompCapsulePrice7[2:]
        except:
            thwompCapsulePrice7 = "00"


        try:
            warpCapsuleWeight7 = hex(int(warpCapsuleWeight7))
            if len(warpCapsuleWeight7) == 4:
                warpCapsuleWeight7 = warpCapsuleWeight7[2:]
            elif len(warpCapsuleWeight7) == 3:
                warpCapsuleWeight7 = "0" + warpCapsuleWeight7[2:]
        except:
            warpCapsuleWeight7 = "00"

        try:
            warpCapsulePrice7 = hex(int(warpCapsulePrice7))
            if len(warpCapsulePrice7) == 4:
                warpCapsulePrice7 = warpCapsulePrice7[2:]
            elif len(warpCapsulePrice7) == 3:
                warpCapsulePrice7 = "0" + warpCapsulePrice7[2:]
        except:
            warpCapsulePrice7 = "00"

        try:
            bombCapsuleWeight7 = hex(int(bombCapsuleWeight7))
            if len(bombCapsuleWeight7) == 4:
                bombCapsuleWeight7 = bombCapsuleWeight7[2:]
            elif len(bombCapsuleWeight7) == 3:
                bombCapsuleWeight7 = "0" + bombCapsuleWeight7[2:]
        except:
            bombCapsuleWeight7 = "00"

        try:
            bombCapsulePrice7 = hex(int(bombCapsulePrice7))
            if len(bombCapsulePrice7) == 4:
                bombCapsulePrice7 = bombCapsulePrice7[2:]
            elif len(bombCapsulePrice7) == 3:
                bombCapsulePrice7 = "0" + bombCapsulePrice7[2:]
        except:
            bombCapsulePrice7 = "00"

        try:
            fireballCapsuleWeight7 = hex(int(fireballCapsuleWeight7))
            if len(fireballCapsuleWeight7) == 4:
                fireballCapsuleWeight7 = fireballCapsuleWeight7[2:]
            elif len(fireballCapsuleWeight7) == 3:
                fireballCapsuleWeight7 = "0" + fireballCapsuleWeight7[2:]
        except:
            fireballCapsuleWeight7 = "00"

        try:
            fireballCapsulePrice7 = hex(int(fireballCapsulePrice7))
            if len(fireballCapsulePrice7) == 4:
                fireballCapsulePrice7 = fireballCapsulePrice7[2:]
            elif len(fireballCapsulePrice7) == 3:
                fireballCapsulePrice7 = "0" + fireballCapsulePrice7[2:]
        except:
            fireballCapsulePrice7 = "00"

        try:
            flowerCapsuleWeight7 = hex(int(flowerCapsuleWeight7))
            if len(flowerCapsuleWeight7) == 4:
                flowerCapsuleWeight7 = flowerCapsuleWeight7[2:]
            elif len(flowerCapsuleWeight7) == 3:
                flowerCapsuleWeight7 = "0" + flowerCapsuleWeight7[2:]
        except:
            flowerCapsuleWeight7 = "00"

        try:
            flowerCapsulePrice7 = hex(int(flowerCapsulePrice7))
            if len(flowerCapsulePrice7) == 4:
                flowerCapsulePrice7 = flowerCapsulePrice7[2:]
            elif len(flowerCapsulePrice7) == 3:
                flowerCapsulePrice7 = "0" + flowerCapsulePrice7[2:]
        except:
            flowerCapsulePrice7 = "00"

        try:
            eggCapsuleWeight7 = hex(int(eggCapsuleWeight7))
            if len(eggCapsuleWeight7) == 4:
                eggCapsuleWeight7 = eggCapsuleWeight7[2:]
            elif len(eggCapsuleWeight7) == 3:
                eggCapsuleWeight7 = "0" + eggCapsuleWeight7[2:]
        except:
            eggCapsuleWeight7 = "00"

        try:
            eggCapsulePrice7 = hex(int(eggCapsulePrice7))
            if len(eggCapsulePrice7) == 4:
                eggCapsulePrice7 = eggCapsulePrice7[2:]
            elif len(eggCapsulePrice7) == 3:
                eggCapsulePrice7 = "0" + eggCapsulePrice7[2:]
        except:
            eggCapsulePrice7 = "00"

        try:
            vacuumCapsuleWeight7 = hex(int(vacuumCapsuleWeight7))
            if len(vacuumCapsuleWeight7) == 4:
                vacuumCapsuleWeight7 = vacuumCapsuleWeight7[2:]
            elif len(vacuumCapsuleWeight7) == 3:
                vacuumCapsuleWeight7 = "0" + vacuumCapsuleWeight7[2:]
        except:
            vacuumCapsuleWeight7 = "00"

        try:
            vacuumCapsulePrice7 = hex(int(vacuumCapsulePrice7))
            if len(vacuumCapsulePrice7) == 4:
                vacuumCapsulePrice7 = vacuumCapsulePrice7[2:]
            elif len(vacuumCapsulePrice7) == 3:
                vacuumCapsulePrice7 = "0" + vacuumCapsulePrice7[2:]
        except:
            vacuumCapsulePrice7 = "00"

        try:
            magicCapsuleWeight7 = hex(int(magicCapsuleWeight7))
            if len(magicCapsuleWeight7) == 4:
                magicCapsuleWeight7 = magicCapsuleWeight7[2:]
            elif len(magicCapsuleWeight7) == 3:
                magicCapsuleWeight7 = "0" + magicCapsuleWeight7[2:]
        except:
            magicCapsuleWeight7 = "00"

        try:
            magicCapsulePrice7 = hex(int(magicCapsulePrice7))
            if len(magicCapsulePrice7) == 4:
                magicCapsulePrice7 = magicCapsulePrice7[2:]
            elif len(magicCapsulePrice7) == 3:
                magicCapsulePrice7 = "0" + magicCapsulePrice7[2:]
        except:
            magicCapsulePrice7 = "00"
        
        try:
            tripleCapsuleWeight7 = hex(int(tripleCapsuleWeight7))
            if len(tripleCapsuleWeight7) == 4:
                tripleCapsuleWeight7 = tripleCapsuleWeight7[2:]
            elif len(tripleCapsuleWeight7) == 3:
                tripleCapsuleWeight7 = "0" + tripleCapsuleWeight7[2:]
        except:
            tripleCapsuleWeight7 = "00"

        try:
            tripleCapsulePrice7 = hex(int(tripleCapsulePrice7))
            if len(tripleCapsulePrice7) == 4:
                tripleCapsulePrice7 = tripleCapsulePrice7[2:]
            elif len(tripleCapsulePrice7) == 3:
                tripleCapsulePrice7 = "0" + tripleCapsulePrice7[2:]
        except:
            tripleCapsulePrice7 = "00"

        try:
            koopaCapsuleWeight7 = hex(int(koopaCapsuleWeight7))
            if len(koopaCapsuleWeight7) == 4:
                koopaCapsuleWeight7 = koopaCapsuleWeight7[2:]
            elif len(koopaCapsuleWeight7) == 3:
                koopaCapsuleWeight7 = "0" + koopaCapsuleWeight7[2:]
        except:
            koopaCapsuleWeight7 = "00"

        try:
            koopaCapsulePrice7 = hex(int(koopaCapsulePrice7))
            if len(koopaCapsulePrice7) == 4:
                koopaCapsulePrice7 = koopaCapsulePrice7[2:]
            elif len(koopaCapsulePrice7) == 3:
                koopaCapsulePrice7 = "0" + koopaCapsulePrice7[2:]
        except:
            koopaCapsulePrice7 = "00"

        generatedCode = getOrbModsSeven(mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated code copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonSixOrb(self):
        if not self.duelCapsulePrice6.get() or not self.duelCapsuleWeight6.get() or not self.metalMushroomCapsulePrice6.get() or not self.metalMushroomCapsuleWeight6.get() or not self.mushroomCapsuleWeight6.get() or not self.goldenMushroomCapsulePrice6.get() or not self.goldenMushroomCapsuleWeight6.get() or not self.slowMushroomCapsulePrice6.get() or not self.slowMushroomCapsuleWeight6.get() or not self.bulletBillCapsulePrice6.get() or not self.bulletBillCapsuleWeight6.get() or not self.warpPipeCapsulePrice6.get() or not self.warpPipeCapsuleWeight6.get() or not self.flutterCapsulePrice6.get() or not self.flutterCapsuleWeight6.get() or not self.cursedMushroomCapsulePrice6.get() or not self.cursedMushroomCapsuleWeight6.get() or not self.spinyCapsulePrice6.get() or not self.spinyCapsuleWeight6.get() or not self.goombaCapsuleWeight6.get() or not self.goombaCapsulePrice6.get() or not self.plantCapsulePrice6.get() or not self.plantCapsuleWeight6.get() or not self.kleptoCapsuleWeight6.get() or not self.kleptoCapsulePrice6.get() or not self.kamekCapsuleWeight6.get() or not self.kamekCapsulePrice6.get() or not self.toadyCapsuleWeight6.get() or not self.toadyCapsulePrice6.get() or not self.blizzardCapsuleWeight6.get() or not self.blizzardCapsulePrice6.get() or not self.podobooCapsulePrice6.get() or not self.podobooCapsuleWeight6.get() or not self.paraTroopaCapsuleWeight6.get() or not self.paraTroopaCapsulePrice6.get() or not self.snackCapsulePrice6.get() or not self.snackCapsuleWeight6.get() or not self.zapCapsulePrice6.get() or not self.zapCapsuleWeight6.get() or not self.tweesterCapsulePrice6.get() or not self.tweesterCapsuleWeight6.get() or not self.thwompCapsulePrice6.get() or not self.thwompCapsuleWeight6.get() or not self.warpPipeCapsulePrice6.get() or not self.warpPipeCapsuleWeight6.get() or not self.bombCapsulePrice6.get() or not self.bombCapsuleWeight6.get() or not self.gaddLightCapsulePrice6.get() or not self.gaddLightCapsuleWeight6.get() or not self.chanceTimeCapsulePrice6.get() or not self.chanceTimeCapsuleWeight6.get() or not self.pinkBooCapsulePrice6.get() or not self.pinkBooCapsuleWeight6.get() or not self.bowserCapsulePrice6.get() or not self.bowserCapsuleWeight6.get() or not self.dkCapsulePrice6.get() or not self.dkCapsuleWeight6.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return
        
        mushroomCapsuleWeight6 = self.mushroomCapsuleWeight6.get()
        
        goldenMushroomCapsulePrice6 = self.goldenMushroomCapsulePrice6.get()
        goldenMushroomCapsuleWeight6 = self.goldenMushroomCapsuleWeight6.get()

        slowMushroomCapsulePrice6 = self.slowMushroomCapsulePrice6.get()
        slowMushroomCapsuleWeight6 = self.slowMushroomCapsuleWeight6.get()

        metalMushroomCapsulePrice6 = self.metalMushroomCapsulePrice6.get()
        metalMushroomCapsuleWeight6 = self.metalMushroomCapsuleWeight6.get()

        bulletBillCapsulePrice6 = self.bulletBillCapsulePrice6.get()
        bulletBillCapsuleWeight6 = self.bulletBillCapsuleWeight6.get()

        flutterCapsulePrice6 = self.flutterCapsulePrice6.get()
        flutterCapsuleWeight6 = self.flutterCapsuleWeight6.get()

        cursedMushroomCapsulePrice6 = self.cursedMushroomCapsulePrice6.get()
        cursedMushroomCapsuleWeight6 = self.cursedMushroomCapsuleWeight6.get()

        spinyCapsulePrice6 = self.spinyCapsulePrice6.get()
        spinyCapsuleWeight6 = self.spinyCapsuleWeight6.get()

        goombaCapsulePrice6 = self.goombaCapsulePrice6.get()
        goombaCapsuleWeight6 = self.goombaCapsuleWeight6.get()

        plantCapsulePrice6 = self.plantCapsulePrice6.get()
        plantCapsuleWeight6 = self.plantCapsuleWeight6.get()

        kleptoCapsulePrice6 = self.kleptoCapsulePrice6.get()
        kleptoCapsuleWeight6 = self.kleptoCapsuleWeight6.get()

        kamekCapsulePrice6 = self.kamekCapsulePrice6.get()
        kamekCapsuleWeight6 = self.kamekCapsuleWeight6.get()

        toadyCapsulePrice6 = self.toadyCapsulePrice6.get()
        toadyCapsuleWeight6 = self.toadyCapsuleWeight6.get()

        blizzardCapsulePrice6 = self.blizzardCapsulePrice6.get()
        blizzardCapsuleWeight6 = self.blizzardCapsuleWeight6.get()

        podobooCapsulePrice6 = self.podobooCapsulePrice6.get()
        podobooCapsuleWeight6 = self.podobooCapsuleWeight6.get()

        paraTroopaCapsulePrice6 = self.paraTroopaCapsulePrice6.get()
        paraTroopaCapsuleWeight6 = self.paraTroopaCapsuleWeight6.get()

        snackCapsulePrice6 = self.snackCapsulePrice6.get()
        snackCapsuleWeight6 = self.snackCapsuleWeight6.get()

        zapCapsulePrice6 = self.zapCapsulePrice6.get()
        zapCapsuleWeight6 = self.zapCapsuleWeight6.get()

        tweesterCapsulePrice6 = self.tweesterCapsulePrice6.get()
        tweesterCapsuleWeight6 = self.tweesterCapsuleWeight6.get()

        thwompCapsulePrice6 = self.thwompCapsulePrice6.get()
        thwompCapsuleWeight6 = self.thwompCapsuleWeight6.get()

        warpPipeCapsulePrice6 = self.warpPipeCapsulePrice6.get()
        warpPipeCapsuleWeight6 = self.warpPipeCapsuleWeight6.get()

        bombCapsulePrice6 = self.bombCapsulePrice6.get()
        bombCapsuleWeight6 = self.bombCapsuleWeight6.get()

        gaddLightCapsulePrice6 = self.gaddLightCapsulePrice6.get()
        gaddLightCapsuleWeight6 = self.gaddLightCapsuleWeight6.get()

        pinkBooCapsulePrice6 = self.pinkBooCapsulePrice6.get()
        pinkBooCapsuleWeight6 = self.pinkBooCapsuleWeight6.get()

        chanceTimeCapsulePrice6 = self.chanceTimeCapsulePrice6.get()
        chanceTimeCapsuleWeight6 = self.chanceTimeCapsuleWeight6.get()

        bowserCapsulePrice6 = self.bowserCapsulePrice6.get()
        bowserCapsuleWeight6 = self.bowserCapsuleWeight6.get()

        dkCapsulePrice6 = self.dkCapsulePrice6.get()
        dkCapsuleWeight6 = self.dkCapsuleWeight6.get()

        duelCapsulePrice6 = self.duelCapsulePrice6.get()
        duelCapsuleWeight6 = self.duelCapsuleWeight6.get()


        orbWeightTotal = int(mushroomCapsuleWeight6) + int(goldenMushroomCapsuleWeight6) + int(bulletBillCapsuleWeight6) + int(slowMushroomCapsuleWeight6) + int(warpPipeCapsuleWeight6) + int(flutterCapsuleWeight6) + int(cursedMushroomCapsuleWeight6) + int(spinyCapsuleWeight6) + int(goombaCapsuleWeight6) + int(plantCapsuleWeight6) + int(kleptoCapsuleWeight6) + int(kamekCapsuleWeight6) + int(toadyCapsuleWeight6) + int(blizzardCapsuleWeight6) + int(podobooCapsuleWeight6) + int(paraTroopaCapsuleWeight6) + int(snackCapsuleWeight6) + int(zapCapsuleWeight6) + int(tweesterCapsuleWeight6) + int(thwompCapsuleWeight6) + int(warpPipeCapsuleWeight6) + int(bombCapsuleWeight6) + int(gaddLightCapsuleWeight6) + int(pinkBooCapsulePrice6) + int(chanceTimeCapsuleWeight6) + int(bowserCapsuleWeight6) + int(dkCapsuleWeight6) + int(metalMushroomCapsuleWeight6) + int(duelCapsuleWeight6)

        mushroomCapsuleWeight6 = (int(mushroomCapsuleWeight6) / orbWeightTotal) * 100
        goldenMushroomCapsuleWeight6 = (int(goldenMushroomCapsuleWeight6) / orbWeightTotal) * 100
        bulletBillCapsuleWeight6 = (int(bulletBillCapsuleWeight6) / orbWeightTotal) * 100
        slowMushroomCapsuleWeight6 = (int(slowMushroomCapsuleWeight6) / orbWeightTotal) * 100
        warpPipeCapsuleWeight6 = (int(warpPipeCapsuleWeight6) / orbWeightTotal) * 100
        flutterCapsuleWeight6 = (int(flutterCapsuleWeight6) / orbWeightTotal) * 100
        cursedMushroomCapsuleWeight6 = (int(cursedMushroomCapsuleWeight6) / orbWeightTotal) * 100
        spinyCapsuleWeight6 = (int(spinyCapsuleWeight6) / orbWeightTotal) * 100
        goombaCapsuleWeight6 = (int(goombaCapsuleWeight6) / orbWeightTotal) * 100
        plantCapsuleWeight6 = (int(plantCapsuleWeight6) / orbWeightTotal) * 100
        kleptoCapsuleWeight6 = (int(kleptoCapsuleWeight6) / orbWeightTotal) * 100
        kamekCapsuleWeight6 = (int(kamekCapsuleWeight6) / orbWeightTotal) * 100
        toadyCapsuleWeight6 = (int(toadyCapsuleWeight6) / orbWeightTotal) * 100
        blizzardCapsuleWeight6 = (int(blizzardCapsuleWeight6) / orbWeightTotal) * 100
        podobooCapsuleWeight6 = (int(podobooCapsuleWeight6) / orbWeightTotal) * 100
        paraTroopaCapsuleWeight6 = (int(paraTroopaCapsuleWeight6) / orbWeightTotal) * 100
        snackCapsuleWeight6 = (int(snackCapsuleWeight6) / orbWeightTotal) * 100
        zapCapsuleWeight6 = (int(zapCapsuleWeight6) / orbWeightTotal) * 100
        tweesterCapsuleWeight6 = (int(tweesterCapsuleWeight6) / orbWeightTotal) * 100
        thwompCapsuleWeight6 = (int(thwompCapsuleWeight6) / orbWeightTotal) * 100
        warpPipeCapsuleWeight6 = (int(warpPipeCapsuleWeight6) / orbWeightTotal) * 100
        bombCapsuleWeight6 = (int(bombCapsuleWeight6) / orbWeightTotal) * 100
        gaddLightCapsuleWeight6 = (int(gaddLightCapsuleWeight6) / orbWeightTotal) * 100
        pinkBooCapsuleWeight6 = (int(pinkBooCapsuleWeight6) / orbWeightTotal) * 100
        chanceTimeCapsuleWeight6 = (int(chanceTimeCapsuleWeight6) / orbWeightTotal) * 100
        bowserCapsuleWeight6 = (int(bowserCapsuleWeight6) / orbWeightTotal) * 100
        dkCapsuleWeight6 = (int(dkCapsuleWeight6) / orbWeightTotal) * 100
        metalMushroomCapsuleWeight6 = (int(metalMushroomCapsuleWeight6) / orbWeightTotal) * 100
        duelCapsuleWeight6 = (int(duelCapsuleWeight6) / orbWeightTotal) * 100

        try:
            mushroomCapsuleWeight6 = hex(int(mushroomCapsuleWeight6))
            if len(mushroomCapsuleWeight6) == 4:
                mushroomCapsuleWeight6 = mushroomCapsuleWeight6[2:]
            elif len(mushroomCapsuleWeight6) == 3:
                mushroomCapsuleWeight6 = "0" + mushroomCapsuleWeight6[2:]
        except:
            mushroomCapsuleWeight6 = "00"

        try:
            goldenMushroomCapsuleWeight6 = hex(int(goldenMushroomCapsuleWeight6))
            if len(goldenMushroomCapsuleWeight6) == 4:
                goldenMushroomCapsuleWeight6 = goldenMushroomCapsuleWeight6[2:]
            elif len(goldenMushroomCapsuleWeight6) == 3:
                goldenMushroomCapsuleWeight6 = "0" + goldenMushroomCapsuleWeight6[2:]
        except:
            goldenMushroomCapsuleWeight6 = "00"

        try:
            goldenMushroomCapsulePrice6 = hex(int(goldenMushroomCapsulePrice6))
            if len(goldenMushroomCapsulePrice6) == 4:
                goldenMushroomCapsulePrice6 = goldenMushroomCapsulePrice6[2:]
            elif len(goldenMushroomCapsulePrice6) == 3:
                goldenMushroomCapsulePrice6 = "0" + goldenMushroomCapsulePrice6[2:]
        except:
            goldenMushroomCapsulePrice6 = "00"
       
        try:
            slowMushroomCapsuleWeight6 = hex(int(slowMushroomCapsuleWeight6))
            if len(slowMushroomCapsuleWeight6) == 4:
                slowMushroomCapsuleWeight6 = slowMushroomCapsuleWeight6[2:]
            elif len(slowMushroomCapsuleWeight6) == 3:
                slowMushroomCapsuleWeight6 = "0" + slowMushroomCapsuleWeight6[2:]
        except:
            slowMushroomCapsuleWeight6 = "00"

        try:
            slowMushroomCapsulePrice6 = hex(int(slowMushroomCapsulePrice6))
            if len(slowMushroomCapsulePrice6) == 4:
                slowMushroomCapsulePrice6 = slowMushroomCapsulePrice6[2:]
            elif len(slowMushroomCapsulePrice6) == 3:
                slowMushroomCapsulePrice6 = "0" + slowMushroomCapsulePrice6[2:]
        except:
            slowMushroomCapsulePrice6 = "00"

        try:
            bulletBillCapsuleWeight6 = hex(int(bulletBillCapsuleWeight6))
            if len(bulletBillCapsuleWeight6) == 4:
                bulletBillCapsuleWeight6 = bulletBillCapsuleWeight6[2:]
            elif len(bulletBillCapsuleWeight6) == 3:
                bulletBillCapsuleWeight6 = "0" + bulletBillCapsuleWeight6[2:]
        except:
            bulletBillCapsuleWeight6 = "00"

        try:
            bulletBillCapsulePrice6 = hex(int(bulletBillCapsulePrice6))
            if len(bulletBillCapsulePrice6) == 4:
                bulletBillCapsulePrice6 = bulletBillCapsulePrice6[2:]
            elif len(bulletBillCapsulePrice6) == 3:
                bulletBillCapsulePrice6 = "0" + bulletBillCapsulePrice6[2:]
        except:
            bulletBillCapsulePrice6 = "00"

        try:
            warpPipeCapsuleWeight6 = hex(int(warpPipeCapsuleWeight6))
            if len(warpPipeCapsuleWeight6) == 4:
                warpPipeCapsuleWeight6 = warpPipeCapsuleWeight6[2:]
            elif len(warpPipeCapsuleWeight6) == 3:
                warpPipeCapsuleWeight6 = "0" + warpPipeCapsuleWeight6[2:]
        except:
            warpPipeCapsuleWeight6 = "00"

        try:
            warpPipeCapsulePrice6 = hex(int(warpPipeCapsulePrice6))
            if len(warpPipeCapsulePrice6) == 4:
                warpPipeCapsulePrice6 = warpPipeCapsulePrice6[2:]
            elif len(warpPipeCapsulePrice6) == 3:
                warpPipeCapsulePrice6 = "0" + warpPipeCapsulePrice6[2:]
        except:
            warpPipeCapsulePrice6 = "00"

        try:
            flutterCapsuleWeight6 = hex(int(flutterCapsuleWeight6))
            if len(flutterCapsuleWeight6) == 4:
                flutterCapsuleWeight6 = flutterCapsuleWeight6[2:]
            elif len(flutterCapsuleWeight6) == 3:
                flutterCapsuleWeight6 = "0" + flutterCapsuleWeight6[2:]
        except:
            flutterCapsuleWeight6 = "00"

        try:
            flutterCapsulePrice6 = hex(int(flutterCapsulePrice6))
            if len(flutterCapsulePrice6) == 4:
                flutterCapsulePrice6 = flutterCapsulePrice6[2:]
            elif len(flutterCapsulePrice6) == 3:
                flutterCapsulePrice6 = "0" + flutterCapsulePrice6[2:]
        except:
            flutterCapsulePrice6 = "00"

        try:
            cursedMushroomCapsuleWeight6 = hex(int(cursedMushroomCapsuleWeight6))
            if len(cursedMushroomCapsuleWeight6) == 4:
                cursedMushroomCapsuleWeight6 = cursedMushroomCapsuleWeight6[2:]
            elif len(cursedMushroomCapsuleWeight6) == 3:
                cursedMushroomCapsuleWeight6 = "0" + cursedMushroomCapsuleWeight6[2:]
        except:
            cursedMushroomCapsuleWeight6 = "00"

        try:
            cursedMushroomCapsulePrice6 = hex(int(cursedMushroomCapsulePrice6))
            if len(cursedMushroomCapsulePrice6) == 4:
                cursedMushroomCapsulePrice6 = cursedMushroomCapsulePrice6[2:]
            elif len(cursedMushroomCapsulePrice6) == 3:
                cursedMushroomCapsulePrice6 = "0" + cursedMushroomCapsulePrice6[2:]
        except:
            cursedMushroomCapsulePrice6 = "00"

        try:
            spinyCapsuleWeight6 = hex(int(spinyCapsuleWeight6))
            if len(spinyCapsuleWeight6) == 4:
                spinyCapsuleWeight6 = spinyCapsuleWeight6[2:]
            elif len(spinyCapsuleWeight6) == 3:
                spinyCapsuleWeight6 = "0" + spinyCapsuleWeight6[2:]
        except:
            spinyCapsuleWeight6 = "00"

        try:
            spinyCapsulePrice6 = hex(int(spinyCapsulePrice6))
            if len(spinyCapsulePrice6) == 4:
                spinyCapsulePrice6 = spinyCapsulePrice6[2:]
            elif len(spinyCapsulePrice6) == 3:
                spinyCapsulePrice6 = "0" + spinyCapsulePrice6[2:]
        except:
            spinyCapsulePrice6 = "00"

        try:
            goombaCapsuleWeight6 = hex(int(goombaCapsuleWeight6))
            if len(goombaCapsuleWeight6) == 4:
                goombaCapsuleWeight6 = goombaCapsuleWeight6[2:]
            elif len(goombaCapsuleWeight6) == 3:
                goombaCapsuleWeight6 = "0" + goombaCapsuleWeight6[2:]
        except:
            goombaCapsuleWeight6 = "00"

        try:
            goombaCapsulePrice6 = hex(int(goombaCapsulePrice6))
            if len(goombaCapsulePrice6) == 4:
                goombaCapsulePrice6 = goombaCapsulePrice6[2:]
            elif len(goombaCapsulePrice6) == 3:
                goombaCapsulePrice6 = "0" + goombaCapsulePrice6[2:]
        except:
            goombaCapsulePrice6 = "00"

        try:
            plantCapsuleWeight6 = hex(int(plantCapsuleWeight6))
            if len(plantCapsuleWeight6) == 4:
                plantCapsuleWeight6 = plantCapsuleWeight6[2:]
            elif len(plantCapsuleWeight6) == 3:
                plantCapsuleWeight6 = "0" + plantCapsuleWeight6[2:]
        except:
            plantCapsuleWeight6 = "00"

        try:
            plantCapsulePrice6 = hex(int(plantCapsulePrice6))
            if len(plantCapsulePrice6) == 4:
                plantCapsulePrice6 = plantCapsulePrice6[2:]
            elif len(plantCapsulePrice6) == 3:
                plantCapsulePrice6 = "0" + plantCapsulePrice6[2:]
        except:
            plantCapsulePrice6 = "00"

        try:
            kleptoCapsuleWeight6 = hex(int(kleptoCapsuleWeight6))
            if len(kleptoCapsuleWeight6) == 4:
                kleptoCapsuleWeight6 = kleptoCapsuleWeight6[2:]
            elif len(kleptoCapsuleWeight6) == 3:
                kleptoCapsuleWeight6 = "0" + kleptoCapsuleWeight6[2:]
        except:
            kleptoCapsuleWeight6 = "00"

        try:
            kleptoCapsulePrice6 = hex(int(kleptoCapsulePrice6))
            if len(kleptoCapsulePrice6) == 4:
                kleptoCapsulePrice6 = kleptoCapsulePrice6[2:]
            elif len(kleptoCapsulePrice6) == 3:
                kleptoCapsulePrice6 = "0" + kleptoCapsulePrice6[2:]
        except:
            kleptoCapsulePrice6 = "00"

        try:
            kamekCapsuleWeight6 = hex(int(kamekCapsuleWeight6))
            if len(kamekCapsuleWeight6) == 4:
                kamekCapsuleWeight6 = kamekCapsuleWeight6[2:]
            elif len(kamekCapsuleWeight6) == 3:
                kamekCapsuleWeight6 = "0" + kamekCapsuleWeight6[2:]
        except:
            kamekCapsuleWeight6 = "00"

        try:
            kamekCapsulePrice6 = hex(int(kamekCapsulePrice6))
            if len(kamekCapsulePrice6) == 4:
                kamekCapsulePrice6 = kamekCapsulePrice6[2:]
            elif len(kamekCapsulePrice6) == 3:
                kamekCapsulePrice6 = "0" + kamekCapsulePrice6[2:]
        except:
            kamekCapsulePrice6 = "00"

        try:
            toadyCapsuleWeight6 = hex(int(toadyCapsuleWeight6))
            if len(toadyCapsuleWeight6) == 4:
                toadyCapsuleWeight6 = toadyCapsuleWeight6[2:]
            elif len(toadyCapsuleWeight6) == 3:
                toadyCapsuleWeight6 = "0" + toadyCapsuleWeight6[2:]
        except:
            toadyCapsuleWeight6 = "00"

        try:
            toadyCapsulePrice6 = hex(int(toadyCapsulePrice6))
            if len(toadyCapsulePrice6) == 4:
                toadyCapsulePrice6 = toadyCapsulePrice6[2:]
            elif len(toadyCapsulePrice6) == 3:
                toadyCapsulePrice6 = "0" + toadyCapsulePrice6[2:]
        except:
            toadyCapsulePrice6 = "00"

        try:
            blizzardCapsuleWeight6 = hex(int(blizzardCapsuleWeight6))
            if len(blizzardCapsuleWeight6) == 4:
                blizzardCapsuleWeight6 = blizzardCapsuleWeight6[2:]
            elif len(blizzardCapsuleWeight6) == 3:
                blizzardCapsuleWeight6 = "0" + blizzardCapsuleWeight6[2:]
        except:
            blizzardCapsuleWeight6 = "00"

        try:
            blizzardCapsulePrice6 = hex(int(blizzardCapsulePrice6))
            if len(blizzardCapsulePrice6) == 4:
                blizzardCapsulePrice6 = blizzardCapsulePrice6[2:]
            elif len(blizzardCapsulePrice6) == 3:
                blizzardCapsulePrice6 = "0" + blizzardCapsulePrice6[2:]
        except:
            blizzardCapsulePrice6 = "00"

        try:
            podobooCapsuleWeight6 = hex(int(podobooCapsuleWeight6))
            if len(podobooCapsuleWeight6) == 4:
                podobooCapsuleWeight6 = podobooCapsuleWeight6[2:]
            elif len(podobooCapsuleWeight6) == 3:
                podobooCapsuleWeight6 = "0" + podobooCapsuleWeight6[2:]
        except:
            podobooCapsuleWeight6 = "00"

        try:
            podobooCapsulePrice6 = hex(int(podobooCapsulePrice6))
            if len(podobooCapsulePrice6) == 4:
                podobooCapsulePrice6 = podobooCapsulePrice6[2:]
            elif len(podobooCapsulePrice6) == 3:
                podobooCapsulePrice6 = "0" + podobooCapsulePrice6[2:]
        except:
            podobooCapsulePrice6 = "00"

        try:
            paraTroopaCapsuleWeight6 = hex(int(paraTroopaCapsuleWeight6))
            if len(paraTroopaCapsuleWeight6) == 4:
                paraTroopaCapsuleWeight6 = paraTroopaCapsuleWeight6[2:]
            elif len(paraTroopaCapsuleWeight6) == 3:
                paraTroopaCapsuleWeight6 = "0" + paraTroopaCapsuleWeight6[2:]
        except:
            paraTroopaCapsuleWeight6 = "00"

        try:
            paraTroopaCapsulePrice6 = hex(int(paraTroopaCapsulePrice6))
            if len(paraTroopaCapsulePrice6) == 4:
                paraTroopaCapsulePrice6 = paraTroopaCapsulePrice6[2:]
            elif len(paraTroopaCapsulePrice6) == 3:
                paraTroopaCapsulePrice6 = "0" + paraTroopaCapsulePrice6[2:]
        except:
            paraTroopaCapsulePrice6 = "00"

        try:
            snackCapsuleWeight6 = hex(int(snackCapsuleWeight6))
            if len(snackCapsuleWeight6) == 4:
                snackCapsuleWeight6 = snackCapsuleWeight6[2:]
            elif len(snackCapsuleWeight6) == 3:
                snackCapsuleWeight6 = "0" + snackCapsuleWeight6[2:]
        except:
            snackCapsuleWeight6 = "00"

        try:
            snackCapsulePrice6 = hex(int(snackCapsulePrice6))
            if len(snackCapsulePrice6) == 4:
                snackCapsulePrice6 = snackCapsulePrice6[2:]
            elif len(snackCapsulePrice6) == 3:
                snackCapsulePrice6 = "0" + snackCapsulePrice6[2:]
        except:
            snackCapsulePrice6 = "00"

        try:
            zapCapsuleWeight6 = hex(int(zapCapsuleWeight6))
            if len(zapCapsuleWeight6) == 4:
                zapCapsuleWeight6 = zapCapsuleWeight6[2:]
            elif len(zapCapsuleWeight6) == 3:
                zapCapsuleWeight6 = "0" + zapCapsuleWeight6[2:]
        except:
            zapCapsuleWeight6 = "00"

        try:
            zapCapsulePrice6 = hex(int(zapCapsulePrice6))
            if len(zapCapsulePrice6) == 4:
                zapCapsulePrice6 = zapCapsulePrice6[2:]
            elif len(zapCapsulePrice6) == 3:
                zapCapsulePrice6 = "0" + zapCapsulePrice6[2:]
        except:
            zapCapsulePrice6 = "00"

        try:
            tweesterCapsuleWeight6 = hex(int(tweesterCapsuleWeight6))
            if len(tweesterCapsuleWeight6) == 4:
                tweesterCapsuleWeight6 = tweesterCapsuleWeight6[2:]
            elif len(tweesterCapsuleWeight6) == 3:
                tweesterCapsuleWeight6 = "0" + tweesterCapsuleWeight6[2:]
        except:
            tweesterCapsuleWeight6 = "00"

        try:
            tweesterCapsulePrice6 = hex(int(tweesterCapsulePrice6))
            if len(tweesterCapsulePrice6) == 4:
                tweesterCapsulePrice6 = tweesterCapsulePrice6[2:]
            elif len(tweesterCapsulePrice6) == 3:
                tweesterCapsulePrice6 = "0" + tweesterCapsulePrice6[2:]
        except:
            tweesterCapsulePrice6 = "00"

        try:
            thwompCapsuleWeight6 = hex(int(thwompCapsuleWeight6))
            if len(thwompCapsuleWeight6) == 4:
                thwompCapsuleWeight6 = thwompCapsuleWeight6[2:]
            elif len(thwompCapsuleWeight6) == 3:
                thwompCapsuleWeight6 = "0" + thwompCapsuleWeight6[2:]
        except:
            thwompCapsuleWeight6 = "00"

        try:
            thwompCapsulePrice6 = hex(int(thwompCapsulePrice6))
            if len(thwompCapsulePrice6) == 4:
                thwompCapsulePrice6 = thwompCapsulePrice6[2:]
            elif len(thwompCapsulePrice6) == 3:
                thwompCapsulePrice6 = "0" + thwompCapsulePrice6[2:]
        except:
            thwompCapsulePrice6 = "00"


        try:
            warpPipeCapsuleWeight6 = hex(int(warpPipeCapsuleWeight6))
            if len(warpPipeCapsuleWeight6) == 4:
                warpPipeCapsuleWeight6 = warpPipeCapsuleWeight6[2:]
            elif len(warpPipeCapsuleWeight6) == 3:
                warpPipeCapsuleWeight6 = "0" + warpPipeCapsuleWeight6[2:]
        except:
            warpPipeCapsuleWeight6 = "00"

        try:
            warpPipeCapsulePrice6 = hex(int(warpPipeCapsulePrice6))
            if len(warpPipeCapsulePrice6) == 4:
                warpPipeCapsulePrice6 = warpPipeCapsulePrice6[2:]
            elif len(warpPipeCapsulePrice6) == 3:
                warpPipeCapsulePrice6 = "0" + warpPipeCapsulePrice6[2:]
        except:
            warpPipeCapsulePrice6 = "00"

        try:
            bombCapsuleWeight6 = hex(int(bombCapsuleWeight6))
            if len(bombCapsuleWeight6) == 4:
                bombCapsuleWeight6 = bombCapsuleWeight6[2:]
            elif len(bombCapsuleWeight6) == 3:
                bombCapsuleWeight6 = "0" + bombCapsuleWeight6[2:]
        except:
            bombCapsuleWeight6 = "00"

        try:
            bombCapsulePrice6 = hex(int(bombCapsulePrice6))
            if len(bombCapsulePrice6) == 4:
                bombCapsulePrice6 = bombCapsulePrice6[2:]
            elif len(bombCapsulePrice6) == 3:
                bombCapsulePrice6 = "0" + bombCapsulePrice6[2:]
        except:
            bombCapsulePrice6 = "00"

        try:
            gaddLightCapsuleWeight6 = hex(int(gaddLightCapsuleWeight6))
            if len(gaddLightCapsuleWeight6) == 4:
                gaddLightCapsuleWeight6 = gaddLightCapsuleWeight6[2:]
            elif len(gaddLightCapsuleWeight6) == 3:
                gaddLightCapsuleWeight6 = "0" + gaddLightCapsuleWeight6[2:]
        except:
            gaddLightCapsuleWeight6 = "00"

        try:
            gaddLightCapsulePrice6 = hex(int(gaddLightCapsulePrice6))
            if len(gaddLightCapsulePrice6) == 4:
                gaddLightCapsulePrice6 = gaddLightCapsulePrice6[2:]
            elif len(gaddLightCapsulePrice6) == 3:
                gaddLightCapsulePrice6 = "0" + gaddLightCapsulePrice6[2:]
        except:
            gaddLightCapsulePrice6 = "00"

        try:
            pinkBooCapsuleWeight6 = hex(int(pinkBooCapsuleWeight6))
            if len(pinkBooCapsuleWeight6) == 4:
                pinkBooCapsuleWeight6 = pinkBooCapsuleWeight6[2:]
            elif len(pinkBooCapsuleWeight6) == 3:
                pinkBooCapsuleWeight6 = "0" + pinkBooCapsuleWeight6[2:]
        except:
            pinkBooCapsuleWeight6 = "00"

        try:
            pinkBooCapsulePrice6 = hex(int(pinkBooCapsulePrice6))
            if len(pinkBooCapsulePrice6) == 4:
                pinkBooCapsulePrice6 = pinkBooCapsulePrice6[2:]
            elif len(pinkBooCapsulePrice6) == 3:
                pinkBooCapsulePrice6 = "0" + pinkBooCapsulePrice6[2:]
        except:
            pinkBooCapsulePrice6 = "00"

        try:
            chanceTimeCapsuleWeight6 = hex(int(chanceTimeCapsuleWeight6))
            if len(chanceTimeCapsuleWeight6) == 4:
                chanceTimeCapsuleWeight6 = chanceTimeCapsuleWeight6[2:]
            elif len(chanceTimeCapsuleWeight6) == 3:
                chanceTimeCapsuleWeight6 = "0" + chanceTimeCapsuleWeight6[2:]
        except:
            chanceTimeCapsuleWeight6 = "00"

        try:
            chanceTimeCapsulePrice6 = hex(int(chanceTimeCapsulePrice6))
            if len(chanceTimeCapsulePrice6) == 4:
                chanceTimeCapsulePrice6 = chanceTimeCapsulePrice6[2:]
            elif len(chanceTimeCapsulePrice6) == 3:
                chanceTimeCapsulePrice6 = "0" + chanceTimeCapsulePrice6[2:]
        except:
            chanceTimeCapsulePrice6 = "00"

        try:
            bowserCapsuleWeight6 = hex(int(bowserCapsuleWeight6))
            if len(bowserCapsuleWeight6) == 4:
                bowserCapsuleWeight6 = bowserCapsuleWeight6[2:]
            elif len(bowserCapsuleWeight6) == 3:
                bowserCapsuleWeight6 = "0" + bowserCapsuleWeight6[2:]
        except:
            bowserCapsuleWeight6 = "00"

        try:
            bowserCapsulePrice6 = hex(int(bowserCapsulePrice6))
            if len(bowserCapsulePrice6) == 4:
                bowserCapsulePrice6 = bowserCapsulePrice6[2:]
            elif len(bowserCapsulePrice6) == 3:
                bowserCapsulePrice6 = "0" + bowserCapsulePrice6[2:]
        except:
            bowserCapsulePrice6 = "00"

        try:
            dkCapsuleWeight6 = hex(int(dkCapsuleWeight6))
            if len(dkCapsuleWeight6) == 4:
                dkCapsuleWeight6 = dkCapsuleWeight6[2:]
            elif len(dkCapsuleWeight6) == 3:
                dkCapsuleWeight6 = "0" + dkCapsuleWeight6[2:]
        except:
            dkCapsuleWeight6 = "00"

        try:
            dkCapsulePrice6 = hex(int(dkCapsulePrice6))
            if len(dkCapsulePrice6) == 4:
                dkCapsulePrice6 = dkCapsulePrice6[2:]
            elif len(dkCapsulePrice6) == 3:
                dkCapsulePrice6 = "0" + dkCapsulePrice6[2:]
        except:
            dkCapsulePrice6 = "00"

        try:
            metalMushroomCapsuleWeight6 = hex(int(metalMushroomCapsuleWeight6))
            if len(metalMushroomCapsuleWeight6) == 4:
                metalMushroomCapsuleWeight6 = metalMushroomCapsuleWeight6[2:]
            elif len(metalMushroomCapsuleWeight6) == 3:
                metalMushroomCapsuleWeight6 = "0" + metalMushroomCapsuleWeight6[2:]
        except:
            metalMushroomCapsuleWeight6 = "00"

        try:
            metalMushroomCapsulePrice6 = hex(int(metalMushroomCapsulePrice6))
            if len(metalMushroomCapsulePrice6) == 4:
                metalMushroomCapsulePrice6 = metalMushroomCapsulePrice6[2:]
            elif len(metalMushroomCapsulePrice6) == 3:
                metalMushroomCapsulePrice6 = "0" + metalMushroomCapsulePrice6[2:]
        except:
            metalMushroomCapsulePrice6 = "00"

        try:
            duelCapsuleWeight6 = hex(int(duelCapsuleWeight6))
            if len(duelCapsuleWeight6) == 4:
                duelCapsuleWeight6 = duelCapsuleWeight6[2:]
            elif len(duelCapsuleWeight6) == 3:
                duelCapsuleWeight6 = "0" + duelCapsuleWeight6[2:]
        except:
            duelCapsuleWeight6 = "00"

        try:
            duelCapsulePrice6 = hex(int(duelCapsulePrice6))
            if len(duelCapsulePrice6) == 4:
                duelCapsulePrice6 = duelCapsulePrice6[2:]
            elif len(duelCapsulePrice6) == 3:
                duelCapsulePrice6 = "0" + duelCapsulePrice6[2:]
        except:
            duelCapsulePrice6 = "00"

        generatedCode = getOrbModsSix(mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, warpPipeCapsulePrice6, warpPipeCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6, pinkBooCapsuleWeight6, chanceTimeCapsulePrice6, chanceTimeCapsuleWeight6, bowserCapsulePrice6, bowserCapsuleWeight6, dkCapsulePrice6, dkCapsuleWeight6, duelCapsulePrice6, duelCapsuleWeight6)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated code copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
    
    def savePresetItems5(self):
        if not self.duelCapsulePrice5.get() or not self.duelCapsuleWeight5.get() or not self.warpPipeCapsulePrice5.get() or not self.warpPipeCapsuleWeight5.get() or not self.mushroomCapsulePrice5.get() or not self.mushroomCapsuleWeight5.get() or not self.goldenMushroomCapsulePrice5.get() or not self.goldenMushroomCapsuleWeight5.get() or not self.cursedMushroomCapsulePrice5.get() or not self.cursedMushroomCapsuleWeight5.get() or not self.kleptoCapsulePrice5.get() or not self.kleptoCapsuleWeight5.get() or not self.warpPipeCapsulePrice5.get() or not self.warpPipeCapsuleWeight5.get() or not self.flutterCapsulePrice5.get() or not self.flutterCapsuleWeight5.get() or not self.cursedMushroomCapsulePrice5.get() or not self.cursedMushroomCapsuleWeight5.get() or not self.spinyCapsulePrice5.get() or not self.spinyCapsuleWeight5.get() or not self.goombaCapsuleWeight5.get() or not self.goombaCapsulePrice5.get() or not self.plantCapsulePrice5.get() or not self.plantCapsuleWeight5.get() or not self.kleptoCapsuleWeight5.get() or not self.kleptoCapsulePrice5.get() or not self.kamekCapsuleWeight5.get() or not self.kamekCapsulePrice5.get() or not self.magiKoopaCapsuleWeight5.get() or not self.magiKoopaCapsulePrice5.get() or not self.blizzardCapsuleWeight5.get() or not self.blizzardCapsulePrice5.get() or not self.podobooCapsulePrice5.get() or not self.podobooCapsuleWeight5.get() or not self.paraTroopaCapsuleWeight5.get() or not self.paraTroopaCapsulePrice5.get() or not self.magiKoopaCapsulePrice5.get() or not self.magiKoopaCapsuleWeight5.get() or not self.ukikiCapsulePrice5.get() or not self.ukikiCapsuleWeight5.get() or not self.tweesterCapsulePrice5.get() or not self.tweesterCapsuleWeight5.get() or not self.lakituCapsulePrice5.get() or not self.lakituCapsuleWeight5.get() or not self.warpPipeCapsulePrice5.get() or not self.warpPipeCapsuleWeight5.get() or not self.miracleCapsulePrice5.get() or not self.miracleCapsuleWeight5.get() or not self.boneCapsulePrice5.get() or not self.boneCapsuleWeight5.get() or not self.chanceCapsulePrice5.get() or not self.chanceCapsuleWeight5.get() or not self.chainChompCapsulePrice5.get() or not self.chainChompCapsuleWeight5.get() or not self.bowserCapsulePrice5.get() or not self.bowserCapsuleWeight5.get() or not self.dkCapsulePrice5.get() or not self.dkCapsuleWeight5.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return

        mushroomCapsulePrice5 = self.mushroomCapsulePrice5.get()
        mushroomCapsuleWeight5 = self.mushroomCapsuleWeight5.get()

        kamekCapsuleWeight5 = self.kamekCapsuleWeight5.get()
        kamekCapsulePrice5 = self.kamekCapsulePrice5.get()
        
        goldenMushroomCapsulePrice5 = self.goldenMushroomCapsulePrice5.get()
        goldenMushroomCapsuleWeight5 = self.goldenMushroomCapsuleWeight5.get()

        cursedMushroomCapsulePrice5 = self.cursedMushroomCapsulePrice5.get()
        cursedMushroomCapsuleWeight5 = self.cursedMushroomCapsuleWeight5.get()

        goombaCapsulePrice5 = self.goombaCapsulePrice5.get()
        goombaCapsuleWeight5 = self.goombaCapsuleWeight5.get()

        kleptoCapsulePrice5 = self.kleptoCapsulePrice5.get()
        kleptoCapsuleWeight5 = self.kleptoCapsuleWeight5.get()

        flutterCapsulePrice5 = self.flutterCapsulePrice5.get()
        flutterCapsuleWeight5 = self.flutterCapsuleWeight5.get()

        podobooCapsulePrice5 = self.podobooCapsulePrice5.get()
        podobooCapsuleWeight5 = self.podobooCapsuleWeight5.get()

        spinyCapsulePrice5 = self.spinyCapsulePrice5.get()
        spinyCapsuleWeight5 = self.spinyCapsuleWeight5.get()

        coinBlockCapsulePrice5 = self.coinBlockCapsulePrice5.get()
        coinBlockCapsuleWeight5 = self.coinBlockCapsuleWeight5.get()

        plantCapsulePrice5 = self.plantCapsulePrice5.get()
        plantCapsuleWeight5 = self.plantCapsuleWeight5.get()

        hammerBroCapsulePrice5 = self.hammerBroCapsulePrice5.get()
        hammerBroCapsuleWeight5 = self.hammerBroCapsuleWeight5.get()

        bulletBillCapsulePrice5 = self.bulletBillCapsulePrice5.get()
        bulletBillCapsuleWeight5 = self.bulletBillCapsuleWeight5.get()

        blizzardCapsulePrice5 = self.blizzardCapsulePrice5.get()
        blizzardCapsuleWeight5 = self.blizzardCapsuleWeight5.get()

        paraTroopaCapsulePrice5 = self.paraTroopaCapsulePrice5.get()
        paraTroopaCapsuleWeight5 = self.paraTroopaCapsuleWeight5.get()

        magiKoopaCapsulePrice5 = self.magiKoopaCapsulePrice5.get()
        magiKoopaCapsuleWeight5 = self.magiKoopaCapsuleWeight5.get()

        ukikiCapsulePrice5 = self.ukikiCapsulePrice5.get()
        ukikiCapsuleWeight5 = self.ukikiCapsuleWeight5.get()

        tweesterCapsulePrice5 = self.tweesterCapsulePrice5.get()
        tweesterCapsuleWeight5 = self.tweesterCapsuleWeight5.get()

        lakituCapsulePrice5 = self.lakituCapsulePrice5.get()
        lakituCapsuleWeight5 = self.lakituCapsuleWeight5.get()

        warpPipeCapsulePrice5 = self.warpPipeCapsulePrice5.get()
        warpPipeCapsuleWeight5 = self.warpPipeCapsuleWeight5.get()

        miracleCapsulePrice5 = self.miracleCapsulePrice5.get()
        miracleCapsuleWeight5 = self.miracleCapsuleWeight5.get()

        boneCapsulePrice5 = self.boneCapsulePrice5.get()
        boneCapsuleWeight5 = self.boneCapsuleWeight5.get()

        chainChompCapsulePrice5 = self.chainChompCapsulePrice5.get()
        chainChompCapsuleWeight5 = self.chainChompCapsuleWeight5.get()

        chanceCapsulePrice5 = self.chanceCapsulePrice5.get()
        chanceCapsuleWeight5 = self.chanceCapsuleWeight5.get()

        bowserCapsulePrice5 = self.bowserCapsulePrice5.get()
        bowserCapsuleWeight5 = self.bowserCapsuleWeight5.get()

        dkCapsulePrice5 = self.dkCapsulePrice5.get()
        dkCapsuleWeight5 = self.dkCapsuleWeight5.get()

        duelCapsulePrice5 = self.duelCapsulePrice5.get()
        duelCapsuleWeight5 = self.duelCapsuleWeight5.get()

        koopaBankCapsulePrice5 = self.koopaBankCapsulePrice5.get()
        koopaBankCapsuleWeight5 = self.koopaBankCapsuleWeight5.get()

        bombCapsulePrice5 = self.bombCapsulePrice5.get()
        bombCapsuleWeight5 = self.bombCapsuleWeight5.get()

        prices5 = [mushroomCapsulePrice5, kamekCapsulePrice5, goldenMushroomCapsulePrice5, cursedMushroomCapsulePrice5, goombaCapsulePrice5, kleptoCapsulePrice5, flutterCapsulePrice5, podobooCapsulePrice5, spinyCapsulePrice5, coinBlockCapsulePrice5, plantCapsulePrice5, hammerBroCapsulePrice5, bulletBillCapsulePrice5, blizzardCapsulePrice5, paraTroopaCapsulePrice5, magiKoopaCapsulePrice5, ukikiCapsulePrice5, tweesterCapsulePrice5, lakituCapsulePrice5, warpPipeCapsulePrice5, miracleCapsulePrice5, boneCapsulePrice5, chainChompCapsulePrice5, chanceCapsulePrice5, bowserCapsulePrice5, dkCapsulePrice5, duelCapsulePrice5, koopaBankCapsulePrice5, bombCapsulePrice5]
        weights5 = [mushroomCapsuleWeight5, kamekCapsuleWeight5, goldenMushroomCapsuleWeight5, cursedMushroomCapsuleWeight5, goombaCapsuleWeight5, kleptoCapsuleWeight5, flutterCapsuleWeight5, podobooCapsuleWeight5, spinyCapsuleWeight5, coinBlockCapsuleWeight5, plantCapsuleWeight5, hammerBroCapsuleWeight5, bulletBillCapsuleWeight5, blizzardCapsuleWeight5, paraTroopaCapsuleWeight5, magiKoopaCapsuleWeight5, ukikiCapsuleWeight5, tweesterCapsuleWeight5, lakituCapsuleWeight5, warpPipeCapsuleWeight5, miracleCapsuleWeight5, boneCapsuleWeight5, chainChompCapsuleWeight5, chanceCapsuleWeight5, bowserCapsuleWeight5, dkCapsuleWeight5, duelCapsuleWeight5, koopaBankCapsuleWeight5, bombCapsuleWeight5]

        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
        if file_path:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Prices', 'Weights'])
                for price, weight in zip(prices5, weights5):
                    writer.writerow([price, weight])
            print("MPT file saved successfully!")
            createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)


    def loadPresetItems5(self):
        file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
        if file_path:
            prices5In = []
            weights5In = []
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    prices5In.append(float(row[0]))
                    weights5In.append(float(row[1]))

            # Define a list of Entry widget attributes
            pricesNames5 = [self.mushroomCapsulePrice5, self.kamekCapsulePrice5, self.goldenMushroomCapsulePrice5, self.cursedMushroomCapsulePrice5, self.goombaCapsulePrice5, self.kleptoCapsulePrice5, self.flutterCapsulePrice5, self.podobooCapsulePrice5, self.spinyCapsulePrice5, self.coinBlockCapsulePrice5, self.plantCapsulePrice5, self.hammerBroCapsulePrice5, self.bulletBillCapsulePrice5, self.blizzardCapsulePrice5, self.paraTroopaCapsulePrice5, self.magiKoopaCapsulePrice5, self.ukikiCapsulePrice5, self.tweesterCapsulePrice5, self.lakituCapsulePrice5, self.warpPipeCapsulePrice5, self.miracleCapsulePrice5, self.boneCapsulePrice5, self.chainChompCapsulePrice5, self.chanceCapsulePrice5, self.bowserCapsulePrice5, self.dkCapsulePrice5, self.duelCapsulePrice5, self.koopaBankCapsulePrice5, self.bombCapsulePrice5]
            weightsNames5 = [self.mushroomCapsuleWeight5, self.kamekCapsuleWeight5, self.goldenMushroomCapsuleWeight5, self.cursedMushroomCapsuleWeight5, self.goombaCapsuleWeight5, self.kleptoCapsuleWeight5, self.flutterCapsuleWeight5, self.podobooCapsuleWeight5, self.spinyCapsuleWeight5, self.coinBlockCapsuleWeight5, self.plantCapsuleWeight5, self.hammerBroCapsuleWeight5, self.bulletBillCapsuleWeight5, self.blizzardCapsuleWeight5, self.paraTroopaCapsuleWeight5, self.magiKoopaCapsuleWeight5, self.ukikiCapsuleWeight5, self.tweesterCapsuleWeight5, self.lakituCapsuleWeight5, self.warpPipeCapsuleWeight5, self.miracleCapsuleWeight5, self.boneCapsuleWeight5, self.chainChompCapsuleWeight5, self.chanceCapsuleWeight5, self.bowserCapsuleWeight5, self.dkCapsuleWeight5, self.duelCapsuleWeight5, self.koopaBankCapsuleWeight5, self.bombCapsuleWeight5]

            # Update widgets with loaded values
            for index, widget in enumerate(pricesNames5):
                if widget and index < len(prices5In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(prices5In[index]))

            for index, widget in enumerate(weightsNames5):
                if widget and index < len(weights5In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(weights5In[index]))
            print("MPT file laoded successfully!")
            createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)
    
    def actionSpaceButtonFiveCapsule(self):
        if not self.duelCapsulePrice5.get() or not self.duelCapsuleWeight5.get() or not self.warpPipeCapsulePrice5.get() or not self.warpPipeCapsuleWeight5.get() or not self.mushroomCapsulePrice5.get() or not self.mushroomCapsuleWeight5.get() or not self.goldenMushroomCapsulePrice5.get() or not self.goldenMushroomCapsuleWeight5.get() or not self.cursedMushroomCapsulePrice5.get() or not self.cursedMushroomCapsuleWeight5.get() or not self.kleptoCapsulePrice5.get() or not self.kleptoCapsuleWeight5.get() or not self.warpPipeCapsulePrice5.get() or not self.warpPipeCapsuleWeight5.get() or not self.flutterCapsulePrice5.get() or not self.flutterCapsuleWeight5.get() or not self.cursedMushroomCapsulePrice5.get() or not self.cursedMushroomCapsuleWeight5.get() or not self.spinyCapsulePrice5.get() or not self.spinyCapsuleWeight5.get() or not self.goombaCapsuleWeight5.get() or not self.goombaCapsulePrice5.get() or not self.plantCapsulePrice5.get() or not self.plantCapsuleWeight5.get() or not self.kleptoCapsuleWeight5.get() or not self.kleptoCapsulePrice5.get() or not self.kamekCapsuleWeight5.get() or not self.kamekCapsulePrice5.get() or not self.magiKoopaCapsuleWeight5.get() or not self.magiKoopaCapsulePrice5.get() or not self.blizzardCapsuleWeight5.get() or not self.blizzardCapsulePrice5.get() or not self.podobooCapsulePrice5.get() or not self.podobooCapsuleWeight5.get() or not self.paraTroopaCapsuleWeight5.get() or not self.paraTroopaCapsulePrice5.get() or not self.magiKoopaCapsulePrice5.get() or not self.magiKoopaCapsuleWeight5.get() or not self.ukikiCapsulePrice5.get() or not self.ukikiCapsuleWeight5.get() or not self.tweesterCapsulePrice5.get() or not self.tweesterCapsuleWeight5.get() or not self.lakituCapsulePrice5.get() or not self.lakituCapsuleWeight5.get() or not self.warpPipeCapsulePrice5.get() or not self.warpPipeCapsuleWeight5.get() or not self.miracleCapsulePrice5.get() or not self.miracleCapsuleWeight5.get() or not self.boneCapsulePrice5.get() or not self.boneCapsuleWeight5.get() or not self.chanceCapsulePrice5.get() or not self.chanceCapsuleWeight5.get() or not self.chainChompCapsulePrice5.get() or not self.chainChompCapsuleWeight5.get() or not self.bowserCapsulePrice5.get() or not self.bowserCapsuleWeight5.get() or not self.dkCapsulePrice5.get() or not self.dkCapsuleWeight5.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return

        mushroomCapsulePrice5 = self.mushroomCapsulePrice5.get()
        mushroomCapsuleWeight5 = self.mushroomCapsuleWeight5.get()

        kamekCapsuleWeight5 = self.kamekCapsuleWeight5.get()
        kamekCapsulePrice5 = self.kamekCapsulePrice5.get()
        
        goldenMushroomCapsulePrice5 = self.goldenMushroomCapsulePrice5.get()
        goldenMushroomCapsuleWeight5 = self.goldenMushroomCapsuleWeight5.get()

        cursedMushroomCapsulePrice5 = self.cursedMushroomCapsulePrice5.get()
        cursedMushroomCapsuleWeight5 = self.cursedMushroomCapsuleWeight5.get()

        goombaCapsulePrice5 = self.goombaCapsulePrice5.get()
        goombaCapsuleWeight5 = self.goombaCapsuleWeight5.get()

        kleptoCapsulePrice5 = self.kleptoCapsulePrice5.get()
        kleptoCapsuleWeight5 = self.kleptoCapsuleWeight5.get()

        flutterCapsulePrice5 = self.flutterCapsulePrice5.get()
        flutterCapsuleWeight5 = self.flutterCapsuleWeight5.get()

        podobooCapsulePrice5 = self.podobooCapsulePrice5.get()
        podobooCapsuleWeight5 = self.podobooCapsuleWeight5.get()

        spinyCapsulePrice5 = self.spinyCapsulePrice5.get()
        spinyCapsuleWeight5 = self.spinyCapsuleWeight5.get()

        coinBlockCapsulePrice5 = self.coinBlockCapsulePrice5.get()
        coinBlockCapsuleWeight5 = self.coinBlockCapsuleWeight5.get()

        plantCapsulePrice5 = self.plantCapsulePrice5.get()
        plantCapsuleWeight5 = self.plantCapsuleWeight5.get()

        hammerBroCapsulePrice5 = self.hammerBroCapsulePrice5.get()
        hammerBroCapsuleWeight5 = self.hammerBroCapsuleWeight5.get()

        bulletBillCapsulePrice5 = self.bulletBillCapsulePrice5.get()
        bulletBillCapsuleWeight5 = self.bulletBillCapsuleWeight5.get()

        blizzardCapsulePrice5 = self.blizzardCapsulePrice5.get()
        blizzardCapsuleWeight5 = self.blizzardCapsuleWeight5.get()

        paraTroopaCapsulePrice5 = self.paraTroopaCapsulePrice5.get()
        paraTroopaCapsuleWeight5 = self.paraTroopaCapsuleWeight5.get()

        magiKoopaCapsulePrice5 = self.magiKoopaCapsulePrice5.get()
        magiKoopaCapsuleWeight5 = self.magiKoopaCapsuleWeight5.get()

        ukikiCapsulePrice5 = self.ukikiCapsulePrice5.get()
        ukikiCapsuleWeight5 = self.ukikiCapsuleWeight5.get()

        tweesterCapsulePrice5 = self.tweesterCapsulePrice5.get()
        tweesterCapsuleWeight5 = self.tweesterCapsuleWeight5.get()

        lakituCapsulePrice5 = self.lakituCapsulePrice5.get()
        lakituCapsuleWeight5 = self.lakituCapsuleWeight5.get()

        warpPipeCapsulePrice5 = self.warpPipeCapsulePrice5.get()
        warpPipeCapsuleWeight5 = self.warpPipeCapsuleWeight5.get()

        miracleCapsulePrice5 = self.miracleCapsulePrice5.get()
        miracleCapsuleWeight5 = self.miracleCapsuleWeight5.get()

        boneCapsulePrice5 = self.boneCapsulePrice5.get()
        boneCapsuleWeight5 = self.boneCapsuleWeight5.get()

        chainChompCapsulePrice5 = self.chainChompCapsulePrice5.get()
        chainChompCapsuleWeight5 = self.chainChompCapsuleWeight5.get()

        chanceCapsulePrice5 = self.chanceCapsulePrice5.get()
        chanceCapsuleWeight5 = self.chanceCapsuleWeight5.get()

        bowserCapsulePrice5 = self.bowserCapsulePrice5.get()
        bowserCapsuleWeight5 = self.bowserCapsuleWeight5.get()

        dkCapsulePrice5 = self.dkCapsulePrice5.get()
        dkCapsuleWeight5 = self.dkCapsuleWeight5.get()

        duelCapsulePrice5 = self.duelCapsulePrice5.get()
        duelCapsuleWeight5 = self.duelCapsuleWeight5.get()

        koopaBankCapsulePrice5 = self.koopaBankCapsulePrice5.get()
        koopaBankCapsuleWeight5 = self.koopaBankCapsuleWeight5.get()

        bombCapsulePrice5 = self.bombCapsulePrice5.get()
        bombCapsuleWeight5 = self.bombCapsuleWeight5.get()

        orbWeightTotal = int(hammerBroCapsuleWeight5) + int(bulletBillCapsuleWeight5) + int(koopaBankCapsuleWeight5) + int(coinBlockCapsuleWeight5) + int(mushroomCapsuleWeight5) + int(goldenMushroomCapsuleWeight5) + int(cursedMushroomCapsuleWeight5) + int(warpPipeCapsuleWeight5) + int(flutterCapsuleWeight5) + int(spinyCapsuleWeight5) + int(goombaCapsuleWeight5) + int(plantCapsuleWeight5) + int(kleptoCapsuleWeight5) + int(kamekCapsuleWeight5) + int(blizzardCapsuleWeight5) + int(podobooCapsuleWeight5) + int(paraTroopaCapsuleWeight5) + int(magiKoopaCapsuleWeight5) + int(ukikiCapsuleWeight5) + int(tweesterCapsuleWeight5) + int(lakituCapsuleWeight5) + int(miracleCapsuleWeight5) + int(boneCapsuleWeight5) + int(chainChompCapsulePrice5) + int(chanceCapsuleWeight5) + int(bowserCapsuleWeight5) + int(dkCapsuleWeight5) + int(duelCapsuleWeight5) + int(bombCapsuleWeight5)

        mushroomCapsuleWeight5 = (int(mushroomCapsuleWeight5) / orbWeightTotal) * 100
        goldenMushroomCapsuleWeight5 = (int(goldenMushroomCapsuleWeight5) / orbWeightTotal) * 100
        warpPipeCapsuleWeight5 = (int(warpPipeCapsuleWeight5) / orbWeightTotal) * 100
        flutterCapsuleWeight5 = (int(flutterCapsuleWeight5) / orbWeightTotal) * 100
        cursedMushroomCapsuleWeight5 = (int(cursedMushroomCapsuleWeight5) / orbWeightTotal) * 100
        spinyCapsuleWeight5 = (int(spinyCapsuleWeight5) / orbWeightTotal) * 100
        goombaCapsuleWeight5 = (int(goombaCapsuleWeight5) / orbWeightTotal) * 100
        plantCapsuleWeight5 = (int(plantCapsuleWeight5) / orbWeightTotal) * 100
        kleptoCapsuleWeight5 = (int(kleptoCapsuleWeight5) / orbWeightTotal) * 100
        kamekCapsuleWeight5 = (int(kamekCapsuleWeight5) / orbWeightTotal) * 100
        blizzardCapsuleWeight5 = (int(blizzardCapsuleWeight5) / orbWeightTotal) * 100
        podobooCapsuleWeight5 = (int(podobooCapsuleWeight5) / orbWeightTotal) * 100
        paraTroopaCapsuleWeight5 = (int(paraTroopaCapsuleWeight5) / orbWeightTotal) * 100
        magiKoopaCapsuleWeight5 = (int(magiKoopaCapsuleWeight5) / orbWeightTotal) * 100
        ukikiCapsuleWeight5 = (int(ukikiCapsuleWeight5) / orbWeightTotal) * 100
        tweesterCapsuleWeight5 = (int(tweesterCapsuleWeight5) / orbWeightTotal) * 100
        lakituCapsuleWeight5 = (int(lakituCapsuleWeight5) / orbWeightTotal) * 100
        miracleCapsuleWeight5 = (int(miracleCapsuleWeight5) / orbWeightTotal) * 100
        boneCapsuleWeight5 = (int(boneCapsuleWeight5) / orbWeightTotal) * 100
        chainChompCapsuleWeight5 = (int(chainChompCapsuleWeight5) / orbWeightTotal) * 100
        chanceCapsuleWeight5 = (int(chanceCapsuleWeight5) / orbWeightTotal) * 100
        bowserCapsuleWeight5 = (int(bowserCapsuleWeight5) / orbWeightTotal) * 100
        dkCapsuleWeight5 = (int(dkCapsuleWeight5) / orbWeightTotal) * 100
        duelCapsuleWeight5 = (int(duelCapsuleWeight5) / orbWeightTotal) * 100
        hammerBroCapsuleWeight5 = (int(hammerBroCapsuleWeight5) / orbWeightTotal) * 100
        bulletBillCapsuleWeight5 = (int(bulletBillCapsuleWeight5) / orbWeightTotal) * 100
        koopaBankCapsuleWeight5 = (int(koopaBankCapsuleWeight5) / orbWeightTotal) * 100
        coinBlockCapsuleWeight5 = (int(coinBlockCapsuleWeight5) / orbWeightTotal) * 100
        bombCapsuleWeight5 = (int(bombCapsuleWeight5) / orbWeightTotal) * 100


        try:
            mushroomCapsuleWeight5 = hex(int(mushroomCapsuleWeight5))
            if len(mushroomCapsuleWeight5) == 4:
                mushroomCapsuleWeight5 = mushroomCapsuleWeight5[2:]
            elif len(mushroomCapsuleWeight5) == 3:
                mushroomCapsuleWeight5 = "0" + mushroomCapsuleWeight5[2:]
        except:
            mushroomCapsuleWeight5 = "00"

        try:
            mushroomCapsulePrice5 = hex(int(mushroomCapsulePrice5))
            if len(mushroomCapsulePrice5) == 4:
                mushroomCapsulePrice5 = mushroomCapsulePrice5[2:]
            elif len(mushroomCapsulePrice5) == 3:
                mushroomCapsulePrice5 = "0" + mushroomCapsulePrice5[2:]
        except:
            mushroomCapsulePrice5 = "00"

        try:
            hammerBroCapsuleWeight5 = hex(int(hammerBroCapsuleWeight5))
            if len(hammerBroCapsuleWeight5) == 4:
                hammerBroCapsuleWeight5 = hammerBroCapsuleWeight5[2:]
            elif len(hammerBroCapsuleWeight5) == 3:
                hammerBroCapsuleWeight5 = "0" + hammerBroCapsuleWeight5[2:]
        except:
            hammerBroCapsuleWeight5 = "00"

        try:
            hammerBroCapsulePrice5 = hex(int(hammerBroCapsulePrice5))
            if len(hammerBroCapsulePrice5) == 4:
                hammerBroCapsulePrice5 = hammerBroCapsulePrice5[2:]
            elif len(hammerBroCapsulePrice5) == 3:
                hammerBroCapsulePrice5 = "0" + hammerBroCapsulePrice5[2:]
        except:
            hammerBroCapsulePrice5 = "00"

        try:
            goldenMushroomCapsuleWeight5 = hex(int(goldenMushroomCapsuleWeight5))
            if len(goldenMushroomCapsuleWeight5) == 4:
                goldenMushroomCapsuleWeight5 = goldenMushroomCapsuleWeight5[2:]
            elif len(goldenMushroomCapsuleWeight5) == 3:
                goldenMushroomCapsuleWeight5 = "0" + goldenMushroomCapsuleWeight5[2:]
        except:
            goldenMushroomCapsuleWeight5 = "00"

        try:
            goldenMushroomCapsulePrice5 = hex(int(goldenMushroomCapsulePrice5))
            if len(goldenMushroomCapsulePrice5) == 4:
                goldenMushroomCapsulePrice5 = goldenMushroomCapsulePrice5[2:]
            elif len(goldenMushroomCapsulePrice5) == 3:
                goldenMushroomCapsulePrice5 = "0" + goldenMushroomCapsulePrice5[2:]
        except:
            goldenMushroomCapsulePrice5 = "00"
       
        try:
            cursedMushroomCapsuleWeight5 = hex(int(cursedMushroomCapsuleWeight5))
            if len(cursedMushroomCapsuleWeight5) == 4:
                cursedMushroomCapsuleWeight5 = cursedMushroomCapsuleWeight5[2:]
            elif len(cursedMushroomCapsuleWeight5) == 3:
                cursedMushroomCapsuleWeight5 = "0" + cursedMushroomCapsuleWeight5[2:]
        except:
            cursedMushroomCapsuleWeight5 = "00"

        try:
            cursedMushroomCapsulePrice5 = hex(int(cursedMushroomCapsulePrice5))
            if len(cursedMushroomCapsulePrice5) == 4:
                cursedMushroomCapsulePrice5 = cursedMushroomCapsulePrice5[2:]
            elif len(cursedMushroomCapsulePrice5) == 3:
                cursedMushroomCapsulePrice5 = "0" + cursedMushroomCapsulePrice5[2:]
        except:
            cursedMushroomCapsulePrice5 = "00"

        try:
            kleptoCapsuleWeight5 = hex(int(kleptoCapsuleWeight5))
            if len(kleptoCapsuleWeight5) == 4:
                kleptoCapsuleWeight5 = kleptoCapsuleWeight5[2:]
            elif len(kleptoCapsuleWeight5) == 3:
                kleptoCapsuleWeight5 = "0" + kleptoCapsuleWeight5[2:]
        except:
            kleptoCapsuleWeight5 = "00"

        try:
            kleptoCapsulePrice5 = hex(int(kleptoCapsulePrice5))
            if len(kleptoCapsulePrice5) == 4:
                kleptoCapsulePrice5 = kleptoCapsulePrice5[2:]
            elif len(kleptoCapsulePrice5) == 3:
                kleptoCapsulePrice5 = "0" + kleptoCapsulePrice5[2:]
        except:
            kleptoCapsulePrice5 = "00"

        try:
            warpPipeCapsuleWeight5 = hex(int(warpPipeCapsuleWeight5))
            if len(warpPipeCapsuleWeight5) == 4:
                warpPipeCapsuleWeight5 = warpPipeCapsuleWeight5[2:]
            elif len(warpPipeCapsuleWeight5) == 3:
                warpPipeCapsuleWeight5 = "0" + warpPipeCapsuleWeight5[2:]
        except:
            warpPipeCapsuleWeight5 = "00"

        try:
            warpPipeCapsulePrice5 = hex(int(warpPipeCapsulePrice5))
            if len(warpPipeCapsulePrice5) == 4:
                warpPipeCapsulePrice5 = warpPipeCapsulePrice5[2:]
            elif len(warpPipeCapsulePrice5) == 3:
                warpPipeCapsulePrice5 = "0" + warpPipeCapsulePrice5[2:]
        except:
            warpPipeCapsulePrice5 = "00"

        try:
            flutterCapsuleWeight5 = hex(int(flutterCapsuleWeight5))
            if len(flutterCapsuleWeight5) == 4:
                flutterCapsuleWeight5 = flutterCapsuleWeight5[2:]
            elif len(flutterCapsuleWeight5) == 3:
                flutterCapsuleWeight5 = "0" + flutterCapsuleWeight5[2:]
        except:
            flutterCapsuleWeight5 = "00"

        try:
            flutterCapsulePrice5 = hex(int(flutterCapsulePrice5))
            if len(flutterCapsulePrice5) == 4:
                flutterCapsulePrice5 = flutterCapsulePrice5[2:]
            elif len(flutterCapsulePrice5) == 3:
                flutterCapsulePrice5 = "0" + flutterCapsulePrice5[2:]
        except:
            flutterCapsulePrice5 = "00"

        try:
            cursedMushroomCapsulePrice5 = hex(int(cursedMushroomCapsulePrice5))
            if len(cursedMushroomCapsulePrice5) == 4:
                cursedMushroomCapsulePrice5 = cursedMushroomCapsulePrice5[2:]
            elif len(cursedMushroomCapsulePrice5) == 3:
                cursedMushroomCapsulePrice5 = "0" + cursedMushroomCapsulePrice5[2:]
        except:
            cursedMushroomCapsulePrice5 = "00"

        try:
            spinyCapsuleWeight5 = hex(int(spinyCapsuleWeight5))
            if len(spinyCapsuleWeight5) == 4:
                spinyCapsuleWeight5 = spinyCapsuleWeight5[2:]
            elif len(spinyCapsuleWeight5) == 3:
                spinyCapsuleWeight5 = "0" + spinyCapsuleWeight5[2:]
        except:
            spinyCapsuleWeight5 = "00"

        try:
            spinyCapsulePrice5 = hex(int(spinyCapsulePrice5))
            if len(spinyCapsulePrice5) == 4:
                spinyCapsulePrice5 = spinyCapsulePrice5[2:]
            elif len(spinyCapsulePrice5) == 3:
                spinyCapsulePrice5 = "0" + spinyCapsulePrice5[2:]
        except:
            spinyCapsulePrice5 = "00"

        try:
            goombaCapsuleWeight5 = hex(int(goombaCapsuleWeight5))
            if len(goombaCapsuleWeight5) == 4:
                goombaCapsuleWeight5 = goombaCapsuleWeight5[2:]
            elif len(goombaCapsuleWeight5) == 3:
                goombaCapsuleWeight5 = "0" + goombaCapsuleWeight5[2:]
        except:
            goombaCapsuleWeight5 = "00"

        try:
            goombaCapsulePrice5 = hex(int(goombaCapsulePrice5))
            if len(goombaCapsulePrice5) == 4:
                goombaCapsulePrice5 = goombaCapsulePrice5[2:]
            elif len(goombaCapsulePrice5) == 3:
                goombaCapsulePrice5 = "0" + goombaCapsulePrice5[2:]
        except:
            goombaCapsulePrice5 = "00"

        try:
            plantCapsuleWeight5 = hex(int(plantCapsuleWeight5))
            if len(plantCapsuleWeight5) == 4:
                plantCapsuleWeight5 = plantCapsuleWeight5[2:]
            elif len(plantCapsuleWeight5) == 3:
                plantCapsuleWeight5 = "0" + plantCapsuleWeight5[2:]
        except:
            plantCapsuleWeight5 = "00"

        try:
            plantCapsulePrice5 = hex(int(plantCapsulePrice5))
            if len(plantCapsulePrice5) == 4:
                plantCapsulePrice5 = plantCapsulePrice5[2:]
            elif len(plantCapsulePrice5) == 3:
                plantCapsulePrice5 = "0" + plantCapsulePrice5[2:]
        except:
            plantCapsulePrice5 = "00"

        try:
            kleptoCapsuleWeight5 = hex(int(kleptoCapsuleWeight5))
            if len(kleptoCapsuleWeight5) == 4:
                kleptoCapsuleWeight5 = kleptoCapsuleWeight5[2:]
            elif len(kleptoCapsuleWeight5) == 3:
                kleptoCapsuleWeight5 = "0" + kleptoCapsuleWeight5[2:]
        except:
            kleptoCapsuleWeight5 = "00"

        try:
            kleptoCapsulePrice5 = hex(int(kleptoCapsulePrice5))
            if len(kleptoCapsulePrice5) == 4:
                kleptoCapsulePrice5 = kleptoCapsulePrice5[2:]
            elif len(kleptoCapsulePrice5) == 3:
                kleptoCapsulePrice5 = "0" + kleptoCapsulePrice5[2:]
        except:
            kleptoCapsulePrice5 = "00"

        try:
            kamekCapsuleWeight5 = hex(int(kamekCapsuleWeight5))
            if len(kamekCapsuleWeight5) == 4:
                kamekCapsuleWeight5 = kamekCapsuleWeight5[2:]
            elif len(kamekCapsuleWeight5) == 3:
                kamekCapsuleWeight5 = "0" + kamekCapsuleWeight5[2:]
        except:
            kamekCapsuleWeight5 = "00"

        try:
            kamekCapsulePrice5 = hex(int(kamekCapsulePrice5))
            if len(kamekCapsulePrice5) == 4:
                kamekCapsulePrice5 = kamekCapsulePrice5[2:]
            elif len(kamekCapsulePrice5) == 3:
                kamekCapsulePrice5 = "0" + kamekCapsulePrice5[2:]
        except:
            kamekCapsulePrice5 = "00"

        try:
            magiKoopaCapsuleWeight5 = hex(int(magiKoopaCapsuleWeight5))
            if len(magiKoopaCapsuleWeight5) == 4:
                magiKoopaCapsuleWeight5 = magiKoopaCapsuleWeight5[2:]
            elif len(magiKoopaCapsuleWeight5) == 3:
                magiKoopaCapsuleWeight5 = "0" + magiKoopaCapsuleWeight5[2:]
        except:
            magiKoopaCapsuleWeight5 = "00"

        try:
            magiKoopaCapsulePrice5 = hex(int(magiKoopaCapsulePrice5))
            if len(magiKoopaCapsulePrice5) == 4:
                magiKoopaCapsulePrice5 = magiKoopaCapsulePrice5[2:]
            elif len(magiKoopaCapsulePrice5) == 3:
                magiKoopaCapsulePrice5 = "0" + magiKoopaCapsulePrice5[2:]
        except:
            magiKoopaCapsulePrice5 = "00"

        try:
            blizzardCapsuleWeight5 = hex(int(blizzardCapsuleWeight5))
            if len(blizzardCapsuleWeight5) == 4:
                blizzardCapsuleWeight5 = blizzardCapsuleWeight5[2:]
            elif len(blizzardCapsuleWeight5) == 3:
                blizzardCapsuleWeight5 = "0" + blizzardCapsuleWeight5[2:]
        except:
            blizzardCapsuleWeight5 = "00"

        try:
            blizzardCapsulePrice5 = hex(int(blizzardCapsulePrice5))
            if len(blizzardCapsulePrice5) == 4:
                blizzardCapsulePrice5 = blizzardCapsulePrice5[2:]
            elif len(blizzardCapsulePrice5) == 3:
                blizzardCapsulePrice5 = "0" + blizzardCapsulePrice5[2:]
        except:
            blizzardCapsulePrice5 = "00"

        try:
            podobooCapsuleWeight5 = hex(int(podobooCapsuleWeight5))
            if len(podobooCapsuleWeight5) == 4:
                podobooCapsuleWeight5 = podobooCapsuleWeight5[2:]
            elif len(podobooCapsuleWeight5) == 3:
                podobooCapsuleWeight5 = "0" + podobooCapsuleWeight5[2:]
        except:
            podobooCapsuleWeight5 = "00"

        try:
            podobooCapsulePrice5 = hex(int(podobooCapsulePrice5))
            if len(podobooCapsulePrice5) == 4:
                podobooCapsulePrice5 = podobooCapsulePrice5[2:]
            elif len(podobooCapsulePrice5) == 3:
                podobooCapsulePrice5 = "0" + podobooCapsulePrice5[2:]
        except:
            podobooCapsulePrice5 = "00"

        try:
            paraTroopaCapsuleWeight5 = hex(int(paraTroopaCapsuleWeight5))
            if len(paraTroopaCapsuleWeight5) == 4:
                paraTroopaCapsuleWeight5 = paraTroopaCapsuleWeight5[2:]
            elif len(paraTroopaCapsuleWeight5) == 3:
                paraTroopaCapsuleWeight5 = "0" + paraTroopaCapsuleWeight5[2:]
        except:
            paraTroopaCapsuleWeight5 = "00"

        try:
            paraTroopaCapsulePrice5 = hex(int(paraTroopaCapsulePrice5))
            if len(paraTroopaCapsulePrice5) == 4:
                paraTroopaCapsulePrice5 = paraTroopaCapsulePrice5[2:]
            elif len(paraTroopaCapsulePrice5) == 3:
                paraTroopaCapsulePrice5 = "0" + paraTroopaCapsulePrice5[2:]
        except:
            paraTroopaCapsulePrice5 = "00"

        try:
            magiKoopaCapsuleWeight5 = hex(int(magiKoopaCapsuleWeight5))
            if len(magiKoopaCapsuleWeight5) == 4:
                magiKoopaCapsuleWeight5 = magiKoopaCapsuleWeight5[2:]
            elif len(magiKoopaCapsuleWeight5) == 3:
                magiKoopaCapsuleWeight5 = "0" + magiKoopaCapsuleWeight5[2:]
        except:
            magiKoopaCapsuleWeight5 = "00"

        try:
            magiKoopaCapsulePrice5 = hex(int(magiKoopaCapsulePrice5))
            if len(magiKoopaCapsulePrice5) == 4:
                magiKoopaCapsulePrice5 = magiKoopaCapsulePrice5[2:]
            elif len(magiKoopaCapsulePrice5) == 3:
                magiKoopaCapsulePrice5 = "0" + magiKoopaCapsulePrice5[2:]
        except:
            magiKoopaCapsulePrice5 = "00"

        try:
            ukikiCapsuleWeight5 = hex(int(ukikiCapsuleWeight5))
            if len(ukikiCapsuleWeight5) == 4:
                ukikiCapsuleWeight5 = ukikiCapsuleWeight5[2:]
            elif len(ukikiCapsuleWeight5) == 3:
                ukikiCapsuleWeight5 = "0" + ukikiCapsuleWeight5[2:]
        except:
            ukikiCapsuleWeight5 = "00"

        try:
            ukikiCapsulePrice5 = hex(int(ukikiCapsulePrice5))
            if len(ukikiCapsulePrice5) == 4:
                ukikiCapsulePrice5 = ukikiCapsulePrice5[2:]
            elif len(ukikiCapsulePrice5) == 3:
                ukikiCapsulePrice5 = "0" + ukikiCapsulePrice5[2:]
        except:
            ukikiCapsulePrice5 = "00"

        try:
            tweesterCapsuleWeight5 = hex(int(tweesterCapsuleWeight5))
            if len(tweesterCapsuleWeight5) == 4:
                tweesterCapsuleWeight5 = tweesterCapsuleWeight5[2:]
            elif len(tweesterCapsuleWeight5) == 3:
                tweesterCapsuleWeight5 = "0" + tweesterCapsuleWeight5[2:]
        except:
            tweesterCapsuleWeight5 = "00"

        try:
            tweesterCapsulePrice5 = hex(int(tweesterCapsulePrice5))
            if len(tweesterCapsulePrice5) == 4:
                tweesterCapsulePrice5 = tweesterCapsulePrice5[2:]
            elif len(tweesterCapsulePrice5) == 3:
                tweesterCapsulePrice5 = "0" + tweesterCapsulePrice5[2:]
        except:
            tweesterCapsulePrice5 = "00"

        try:
            lakituCapsuleWeight5 = hex(int(lakituCapsuleWeight5))
            if len(lakituCapsuleWeight5) == 4:
                lakituCapsuleWeight5 = lakituCapsuleWeight5[2:]
            elif len(lakituCapsuleWeight5) == 3:
                lakituCapsuleWeight5 = "0" + lakituCapsuleWeight5[2:]
        except:
            lakituCapsuleWeight5 = "00"

        try:
            lakituCapsulePrice5 = hex(int(lakituCapsulePrice5))
            if len(lakituCapsulePrice5) == 4:
                lakituCapsulePrice5 = lakituCapsulePrice5[2:]
            elif len(lakituCapsulePrice5) == 3:
                lakituCapsulePrice5 = "0" + lakituCapsulePrice5[2:]
        except:
            lakituCapsulePrice5 = "00"

        try:
            miracleCapsuleWeight5 = hex(int(miracleCapsuleWeight5))
            if len(miracleCapsuleWeight5) == 4:
                miracleCapsuleWeight5 = miracleCapsuleWeight5[2:]
            elif len(miracleCapsuleWeight5) == 3:
                miracleCapsuleWeight5 = "0" + miracleCapsuleWeight5[2:]
        except:
            miracleCapsuleWeight5 = "00"

        try:
            miracleCapsulePrice5 = hex(int(miracleCapsulePrice5))
            if len(miracleCapsulePrice5) == 4:
                miracleCapsulePrice5 = miracleCapsulePrice5[2:]
            elif len(miracleCapsulePrice5) == 3:
                miracleCapsulePrice5 = "0" + miracleCapsulePrice5[2:]
        except:
            miracleCapsulePrice5 = "00"

        try:
            boneCapsuleWeight5 = hex(int(boneCapsuleWeight5))
            if len(boneCapsuleWeight5) == 4:
                boneCapsuleWeight5 = boneCapsuleWeight5[2:]
            elif len(boneCapsuleWeight5) == 3:
                boneCapsuleWeight5 = "0" + boneCapsuleWeight5[2:]
        except:
            boneCapsuleWeight5 = "00"

        try:
            boneCapsulePrice5 = hex(int(boneCapsulePrice5))
            if len(boneCapsulePrice5) == 4:
                boneCapsulePrice5 = boneCapsulePrice5[2:]
            elif len(boneCapsulePrice5) == 3:
                boneCapsulePrice5 = "0" + boneCapsulePrice5[2:]
        except:
            boneCapsulePrice5 = "00"

        try:
            chainChompCapsuleWeight5 = hex(int(chainChompCapsuleWeight5))
            if len(chainChompCapsuleWeight5) == 4:
                chainChompCapsuleWeight5 = chainChompCapsuleWeight5[2:]
            elif len(chainChompCapsuleWeight5) == 3:
                chainChompCapsuleWeight5 = "0" + chainChompCapsuleWeight5[2:]
        except:
            chainChompCapsuleWeight5 = "00"

        try:
            chainChompCapsulePrice5 = hex(int(chainChompCapsulePrice5))
            if len(chainChompCapsulePrice5) == 4:
                chainChompCapsulePrice5 = chainChompCapsulePrice5[2:]
            elif len(chainChompCapsulePrice5) == 3:
                chainChompCapsulePrice5 = "0" + chainChompCapsulePrice5[2:]
        except:
            chainChompCapsulePrice5 = "00"

        try:
            chanceCapsuleWeight5 = hex(int(chanceCapsuleWeight5))
            if len(chanceCapsuleWeight5) == 4:
                chanceCapsuleWeight5 = chanceCapsuleWeight5[2:]
            elif len(chanceCapsuleWeight5) == 3:
                chanceCapsuleWeight5 = "0" + chanceCapsuleWeight5[2:]
        except:
            chanceCapsuleWeight5 = "00"

        try:
            chanceCapsulePrice5 = hex(int(chanceCapsulePrice5))
            if len(chanceCapsulePrice5) == 4:
                chanceCapsulePrice5 = chanceCapsulePrice5[2:]
            elif len(chanceCapsulePrice5) == 3:
                chanceCapsulePrice5 = "0" + chanceCapsulePrice5[2:]
        except:
            chanceCapsulePrice5 = "00"

        try:
            bowserCapsuleWeight5 = hex(int(bowserCapsuleWeight5))
            if len(bowserCapsuleWeight5) == 4:
                bowserCapsuleWeight5 = bowserCapsuleWeight5[2:]
            elif len(bowserCapsuleWeight5) == 3:
                bowserCapsuleWeight5 = "0" + bowserCapsuleWeight5[2:]
        except:
            bowserCapsuleWeight5 = "00"

        try:
            bowserCapsulePrice5 = hex(int(bowserCapsulePrice5))
            if len(bowserCapsulePrice5) == 4:
                bowserCapsulePrice5 = bowserCapsulePrice5[2:]
            elif len(bowserCapsulePrice5) == 3:
                bowserCapsulePrice5 = "0" + bowserCapsulePrice5[2:]
        except:
            bowserCapsulePrice5 = "00"

        try:
            dkCapsuleWeight5 = hex(int(dkCapsuleWeight5))
            if len(dkCapsuleWeight5) == 4:
                dkCapsuleWeight5 = dkCapsuleWeight5[2:]
            elif len(dkCapsuleWeight5) == 3:
                dkCapsuleWeight5 = "0" + dkCapsuleWeight5[2:]
        except:
            dkCapsuleWeight5 = "00"

        try:
            dkCapsulePrice5 = hex(int(dkCapsulePrice5))
            if len(dkCapsulePrice5) == 4:
                dkCapsulePrice5 = dkCapsulePrice5[2:]
            elif len(dkCapsulePrice5) == 3:
                dkCapsulePrice5 = "0" + dkCapsulePrice5[2:]
        except:
            dkCapsulePrice5 = "00"

        try:
            warpPipeCapsuleWeight5 = hex(int(warpPipeCapsuleWeight5))
            if len(warpPipeCapsuleWeight5) == 4:
                warpPipeCapsuleWeight5 = warpPipeCapsuleWeight5[2:]
            elif len(warpPipeCapsuleWeight5) == 3:
                warpPipeCapsuleWeight5 = "0" + warpPipeCapsuleWeight5[2:]
        except:
            warpPipeCapsuleWeight5 = "00"

        try:
            warpPipeCapsulePrice5 = hex(int(warpPipeCapsulePrice5))
            if len(warpPipeCapsulePrice5) == 4:
                warpPipeCapsulePrice5 = warpPipeCapsulePrice5[2:]
            elif len(warpPipeCapsulePrice5) == 3:
                warpPipeCapsulePrice5 = "0" + warpPipeCapsulePrice5[2:]
        except:
            warpPipeCapsulePrice5 = "00"

        try:
            duelCapsuleWeight5 = hex(int(duelCapsuleWeight5))
            if len(duelCapsuleWeight5) == 4:
                duelCapsuleWeight5 = duelCapsuleWeight5[2:]
            elif len(duelCapsuleWeight5) == 3:
                duelCapsuleWeight5 = "0" + duelCapsuleWeight5[2:]
        except:
            duelCapsuleWeight5 = "00"

        try:
            duelCapsulePrice5 = hex(int(duelCapsulePrice5))
            if len(duelCapsulePrice5) == 4:
                duelCapsulePrice5 = duelCapsulePrice5[2:]
            elif len(duelCapsulePrice5) == 3:
                duelCapsulePrice5 = "0" + duelCapsulePrice5[2:]
        except:
            duelCapsulePrice5 = "00"

        try:
            coinBlockCapsuleWeight5 = hex(int(coinBlockCapsuleWeight5))
            if len(coinBlockCapsuleWeight5) == 4:
                coinBlockCapsuleWeight5 = coinBlockCapsuleWeight5[2:]
            elif len(coinBlockCapsuleWeight5) == 3:
                coinBlockCapsuleWeight5 = "0" + coinBlockCapsuleWeight5[2:]
        except:
            coinBlockCapsuleWeight5 = "00"

        try:
            coinBlockCapsulePrice5 = hex(int(coinBlockCapsulePrice5))
            if len(coinBlockCapsulePrice5) == 4:
                coinBlockCapsulePrice5 = coinBlockCapsulePrice5[2:]
            elif len(coinBlockCapsulePrice5) == 3:
                coinBlockCapsulePrice5 = "0" + coinBlockCapsulePrice5[2:]
        except:
            coinBlockCapsulePrice5 = "00"

        try:
            bombCapsuleWeight5 = hex(int(bombCapsuleWeight5))
            if len(bombCapsuleWeight5) == 4:
                bombCapsuleWeight5 = bombCapsuleWeight5[2:]
            elif len(bombCapsuleWeight5) == 3:
                bombCapsuleWeight5 = "0" + bombCapsuleWeight5[2:]
        except:
            bombCapsuleWeight5 = "00"

        try:
            bombCapsulePrice5 = hex(int(bombCapsulePrice5))
            if len(bombCapsulePrice5) == 4:
                bombCapsulePrice5 = bombCapsulePrice5[2:]
            elif len(bombCapsulePrice5) == 3:
                bombCapsulePrice5 = "0" + bombCapsulePrice5[2:]
        except:
            bombCapsulePrice5 = "00"

        try:
            koopaBankCapsuleWeight5 = hex(int(koopaBankCapsuleWeight5))
            if len(koopaBankCapsuleWeight5) == 4:
                koopaBankCapsuleWeight5 = koopaBankCapsuleWeight5[2:]
            elif len(koopaBankCapsuleWeight5) == 3:
                koopaBankCapsuleWeight5 = "0" + koopaBankCapsuleWeight5[2:]
        except:
            koopaBankCapsuleWeight5 = "00"

        try:
            koopaBankCapsulePrice5 = hex(int(koopaBankCapsulePrice5))
            if len(koopaBankCapsulePrice5) == 4:
                koopaBankCapsulePrice5 = koopaBankCapsulePrice5[2:]
            elif len(koopaBankCapsulePrice5) == 3:
                koopaBankCapsulePrice5 = "0" + koopaBankCapsulePrice5[2:]
        except:
            koopaBankCapsulePrice5 = "00"

        try:
            bulletBillCapsuleWeight5 = hex(int(bulletBillCapsuleWeight5))
            if len(bulletBillCapsuleWeight5) == 4:
                bulletBillCapsuleWeight5 = bulletBillCapsuleWeight5[2:]
            elif len(bulletBillCapsuleWeight5) == 3:
                bulletBillCapsuleWeight5 = "0" + bulletBillCapsuleWeight5[2:]
        except:
            bulletBillCapsuleWeight5 = "00"

        try:
            bulletBillCapsulePrice5 = hex(int(bulletBillCapsulePrice5))
            if len(bulletBillCapsulePrice5) == 4:
                bulletBillCapsulePrice5 = bulletBillCapsulePrice5[2:]
            elif len(bulletBillCapsulePrice5) == 3:
                bulletBillCapsulePrice5 = "0" + bulletBillCapsulePrice5[2:]
        except:
            bulletBillCapsulePrice5 = "00"

        generatedCode = getCapsuleModsFive(mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, kleptoCapsulePrice5, kleptoCapsuleWeight5, podobooCapsulePrice5, podobooCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, paraTroopaCapsulePrice5, paraTroopaCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, goombaCapsulePrice5, goombaCapsuleWeight5, bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, kamekCapsulePrice5, kamekCapsuleWeight5, blizzardCapsulePrice5, blizzardCapsuleWeight5, plantCapsulePrice5, plantCapsuleWeight5, magiKoopaCapsulePrice5, magiKoopaCapsuleWeight5, ukikiCapsulePrice5, ukikiCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated code copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

    def actionSpaceButtonFiveOther(self):
        if self.checkboxDisableAdv.get() == 0 and self.checkboxBoot.get() == 0 and self.checkboxBSpeed.get() == 0 and self.checkboxCSpeed.get() == 0 and self.checkboxTaunt.get() == 0 and self.checkboxTxtDisplay.get() == 0 and self.checkboxShowCtrl.get() == 0 and self.checkboxUnlockAll.get() == 0 and self.checkboxBowserNoStealCoins.get() == 0 and self.checkbox60RocketShip.get() == 0 and self.checkboxFreeTaxi.get() == 0 and self.checkboxFreeThwmopWhomp.get() == 0 and self.checkboxFreeBridge.get() == 0 and self.checkboxDisableHappening.get() == 0 and self.checkboxAdvTxt.get() == 0 and self.checkboxAllDK.get() == 0 and self.checkboxBattleNoStar.get() == 0 and self.checkboxCapsulesAny.get() == 0 and self.checkboxDoubleTurns.get() == 0 and self.checkboxCapsulesFinal.get() == 0 and self.checkbox20Sec.get() == 0 and self.checkboxNoBrick.get() == 0 and self.checkbox1Slow.get() == 0 and self.checkboxNoSlow.get() == 0 and self.checkboxFlowers3.get() == 0 and self.checkboxNoRocks.get() == 0 and self.checkboxLeafDisplay.get() == 0 and self.checkboxHalvedTime.get() == 0:
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please check at least 1 box.", None)
            else:
                createDialog("Error", "error", "Please check at least 1 box.", None)
            return
        
        generatedCode = ''''''
        
        ticked = self.checkboxDisableAdv.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("DisableAdv")
        
        ticked = self.checkboxBoot.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("Boot")
        
        ticked = self.checkboxBSpeed.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("BSpeed")
        
        ticked = self.checkboxCSpeed.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("CSpeed")
        
        ticked = self.checkboxTaunt.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("Taunt")
        
        ticked = self.checkboxTxtDisplay.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("TxtDisplay")
        
        ticked = self.checkboxShowCtrl.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("ShowCtrl")
        
        ticked = self.checkboxUnlockAll.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("UnlockAll")
        
        ticked = self.checkboxBowserNoStealCoins.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("BowserNoStealCoins")
        
        ticked = self.checkbox60RocketShip.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("60RocketShip")
        
        ticked = self.checkboxFreeTaxi.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("FreeTaxi")
        
        ticked = self.checkboxFreeThwmopWhomp.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("FreeThwmopWhomp")
        
        ticked = self.checkboxFreeBridge.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("FreeBridge")
        
        ticked = self.checkboxDisableHappening.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("DisableHappening")
        
        ticked = self.checkboxAdvTxt.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("AdvTxt")
        
        ticked = self.checkboxAllDK.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("AllDK")
        
        ticked = self.checkboxBattleNoStar.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("BattleNoStar")
        
        ticked = self.checkboxCapsulesAny.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("CapsulesAny")
        
        ticked = self.checkboxDoubleTurns.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("DoubleTurns")
        
        ticked = self.checkboxCapsulesFinal.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("CapsulesFinal")
        
        ticked = self.checkbox20Sec.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("20Sec")
        
        ticked = self.checkboxNoBrick.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("NoBrick")
        
        ticked = self.checkbox1Slow.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("1Slow")
        
        ticked = self.checkboxNoSlow.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("NoSlow")
        
        ticked = self.checkboxFlowers3.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("Flowers3")
        
        ticked = self.checkboxNoRocks.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("NoRocks")
        
        ticked = self.checkboxLeafDisplay.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("LeafDisplay")
        
        ticked = self.checkboxHalvedTime.get()
        
        if ticked == 1:
            generatedCode = generatedCode + getOtherCodesFive("HalvedTime")

        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated code copied to the clipboard.")
        createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
    
    def savePresetItems7(self):
        if not self.mushroomCapsuleWeight7.get() or not self.goldenMushroomCapsulePrice7.get() or not self.goldenMushroomCapsuleWeight7.get() or not self.slowMushroomCapsulePrice7.get() or not self.slowMushroomCapsuleWeight7.get() or not self.metalMushroomCapsulePrice7.get() or not self.metalMushroomCapsuleWeight7.get() or not self.flutterCapsulePrice7.get() or not self.flutterCapsuleWeight7.get() or not self.cannonCapsulePrice7.get() or not self.cannonCapsuleWeight7.get() or not self.snackCapsulePrice7.get() or not self.snackCapsuleWeight7.get() or not self.lakituCapsulePrice7.get() or not self.lakituCapsuleWeight7.get() or not self.hammerBroCapsuleWeight7.get() or not self.hammerBroCapsulePrice7.get() or not self.plantCapsulePrice7.get() or not self.plantCapsuleWeight7.get() or not self.spearCapsuleWeight7.get() or not self.spearCapsulePrice7.get() or not self.kamekCapsuleWeight7.get() or not self.kamekCapsulePrice7.get() or not self.toadyCapsuleWeight7.get() or not self.toadyCapsulePrice7.get() or not self.blizzardCapsuleWeight7.get() or not self.blizzardCapsulePrice7.get() or not self.banditCapsulePrice7.get() or not self.banditCapsuleWeight7.get() or not self.pinkBooCapsuleWeight7.get() or not self.pinkBooCapsulePrice7.get() or not self.spinyCapsulePrice7.get() or not self.spinyCapsuleWeight7.get() or not self.zapCapsulePrice7.get() or not self.zapCapsuleWeight7.get() or not self.tweesterCapsulePrice7.get() or not self.tweesterCapsuleWeight7.get() or not self.thwompCapsulePrice7.get() or not self.thwompCapsuleWeight7.get() or not self.warpCapsulePrice7.get() or not self.warpCapsuleWeight7.get() or not self.bombCapsulePrice7.get() or not self.bombCapsuleWeight7.get() or not self.fireballCapsulePrice7.get() or not self.fireballCapsuleWeight7.get() or not self.eggCapsulePrice7.get() or not self.eggCapsuleWeight7.get() or not self.flowerCapsulePrice7.get() or not self.flowerCapsuleWeight7.get() or not self.vacuumCapsulePrice7.get() or not self.vacuumCapsuleWeight7.get() or not self.magicCapsulePrice7.get() or not self.magicCapsuleWeight7.get() or not self.tripleCapsulePrice7.get() or not self.tripleCapsuleWeight7.get() or not self.koopaCapsulePrice7.get() or not self.koopaCapsuleWeight7.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return
        
        mushroomCapsuleWeight7 = self.mushroomCapsuleWeight7.get()
        
        goldenMushroomCapsulePrice7 = self.goldenMushroomCapsulePrice7.get()
        goldenMushroomCapsuleWeight7 = self.goldenMushroomCapsuleWeight7.get()

        slowMushroomCapsulePrice7 = self.slowMushroomCapsulePrice7.get()
        slowMushroomCapsuleWeight7 = self.slowMushroomCapsuleWeight7.get()

        metalMushroomCapsulePrice7 = self.metalMushroomCapsulePrice7.get()
        metalMushroomCapsuleWeight7 = self.metalMushroomCapsuleWeight7.get()

        flutterCapsulePrice7 = self.flutterCapsulePrice7.get()
        flutterCapsuleWeight7 = self.flutterCapsuleWeight7.get()

        cannonCapsulePrice7 = self.cannonCapsulePrice7.get()
        cannonCapsuleWeight7 = self.cannonCapsuleWeight7.get()

        snackCapsulePrice7 = self.snackCapsulePrice7.get()
        snackCapsuleWeight7 = self.snackCapsuleWeight7.get()

        lakituCapsulePrice7 = self.lakituCapsulePrice7.get()
        lakituCapsuleWeight7 = self.lakituCapsuleWeight7.get()

        hammerBroCapsulePrice7 = self.hammerBroCapsulePrice7.get()
        hammerBroCapsuleWeight7 = self.hammerBroCapsuleWeight7.get()

        plantCapsulePrice7 = self.plantCapsulePrice7.get()
        plantCapsuleWeight7 = self.plantCapsuleWeight7.get()

        spearCapsulePrice7 = self.spearCapsulePrice7.get()
        spearCapsuleWeight7 = self.spearCapsuleWeight7.get()

        kamekCapsulePrice7 = self.kamekCapsulePrice7.get()
        kamekCapsuleWeight7 = self.kamekCapsuleWeight7.get()

        toadyCapsulePrice7 = self.toadyCapsulePrice7.get()
        toadyCapsuleWeight7 = self.toadyCapsuleWeight7.get()

        blizzardCapsulePrice7 = self.blizzardCapsulePrice7.get()
        blizzardCapsuleWeight7 = self.blizzardCapsuleWeight7.get()

        banditCapsulePrice7 = self.banditCapsulePrice7.get()
        banditCapsuleWeight7 = self.banditCapsuleWeight7.get()

        pinkBooCapsulePrice7 = self.pinkBooCapsulePrice7.get()
        pinkBooCapsuleWeight7 = self.pinkBooCapsuleWeight7.get()

        spinyCapsulePrice7 = self.spinyCapsulePrice7.get()
        spinyCapsuleWeight7 = self.spinyCapsuleWeight7.get()

        zapCapsulePrice7 = self.zapCapsulePrice7.get()
        zapCapsuleWeight7 = self.zapCapsuleWeight7.get()

        tweesterCapsulePrice7 = self.tweesterCapsulePrice7.get()
        tweesterCapsuleWeight7 = self.tweesterCapsuleWeight7.get()

        thwompCapsulePrice7 = self.thwompCapsulePrice7.get()
        thwompCapsuleWeight7 = self.thwompCapsuleWeight7.get()

        warpCapsulePrice7 = self.warpCapsulePrice7.get()
        warpCapsuleWeight7 = self.warpCapsuleWeight7.get()

        bombCapsulePrice7 = self.bombCapsulePrice7.get()
        bombCapsuleWeight7 = self.bombCapsuleWeight7.get()

        fireballCapsulePrice7 = self.fireballCapsulePrice7.get()
        fireballCapsuleWeight7 = self.fireballCapsuleWeight7.get()

        flowerCapsulePrice7 = self.flowerCapsulePrice7.get()
        flowerCapsuleWeight7 = self.flowerCapsuleWeight7.get()

        eggCapsulePrice7 = self.eggCapsulePrice7.get()
        eggCapsuleWeight7 = self.eggCapsuleWeight7.get()

        vacuumCapsulePrice7 = self.vacuumCapsulePrice7.get()
        vacuumCapsuleWeight7 = self.vacuumCapsuleWeight7.get()

        magicCapsulePrice7 = self.magicCapsulePrice7.get()
        magicCapsuleWeight7 = self.magicCapsuleWeight7.get()

        tripleCapsulePrice7 = self.tripleCapsulePrice7.get()
        tripleCapsuleWeight7 = self.tripleCapsuleWeight7.get()

        koopaCapsulePrice7 = self.koopaCapsulePrice7.get()
        koopaCapsuleWeight7 = self.koopaCapsuleWeight7.get()


        prices7 = ["5", goldenMushroomCapsulePrice7, slowMushroomCapsulePrice7, metalMushroomCapsulePrice7, flutterCapsulePrice7, cannonCapsulePrice7, snackCapsulePrice7, lakituCapsulePrice7, hammerBroCapsulePrice7, plantCapsulePrice7, spearCapsulePrice7, kamekCapsulePrice7, toadyCapsulePrice7, blizzardCapsulePrice7, banditCapsulePrice7, pinkBooCapsulePrice7, spinyCapsulePrice7, zapCapsulePrice7, tweesterCapsulePrice7, thwompCapsulePrice7, warpCapsulePrice7, bombCapsulePrice7, fireballCapsulePrice7, flowerCapsulePrice7, eggCapsulePrice7, vacuumCapsulePrice7, magicCapsulePrice7, tripleCapsulePrice7, koopaCapsulePrice7]
        weights7 = [mushroomCapsuleWeight7, goldenMushroomCapsuleWeight7, slowMushroomCapsuleWeight7, metalMushroomCapsuleWeight7, flutterCapsuleWeight7, cannonCapsuleWeight7, snackCapsuleWeight7, lakituCapsuleWeight7, hammerBroCapsuleWeight7, plantCapsuleWeight7, spearCapsuleWeight7, kamekCapsuleWeight7, toadyCapsuleWeight7, blizzardCapsuleWeight7, banditCapsuleWeight7, pinkBooCapsuleWeight7, spinyCapsuleWeight7, zapCapsuleWeight7, tweesterCapsuleWeight7, thwompCapsuleWeight7, warpCapsuleWeight7, bombCapsuleWeight7, fireballCapsuleWeight7, flowerCapsuleWeight7, eggCapsuleWeight7, vacuumCapsuleWeight7, magicCapsuleWeight7, tripleCapsuleWeight7, koopaCapsuleWeight7]

        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
        if file_path:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Prices', 'Weights'])
                for price, weight in zip(prices7, weights7):
                    writer.writerow([price, weight])
            print("MPT file saved successfully!")
            createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)


    def loadPresetItems7(self):
        file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
        if file_path:
            prices7In = []
            weights7In = []
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    prices7In.append(float(row[0]))
                    weights7In.append(float(row[1]))
            
            testVar = ""
            # Define a list of Entry widget attributes
            
            pricesNames7 = [testVar, self.goldenMushroomCapsulePrice7, self.slowMushroomCapsulePrice7, self.metalMushroomCapsulePrice7, self.flutterCapsulePrice7, self.cannonCapsulePrice7, self.snackCapsulePrice7, self.lakituCapsulePrice7, self.hammerBroCapsulePrice7, self.plantCapsulePrice7, self.spearCapsulePrice7, self.kamekCapsulePrice7, self.toadyCapsulePrice7, self.blizzardCapsulePrice7, self.banditCapsulePrice7, self.pinkBooCapsulePrice7, self.spinyCapsulePrice7, self.zapCapsulePrice7, self.tweesterCapsulePrice7, self.thwompCapsulePrice7, self.warpCapsulePrice7, self.bombCapsulePrice7, self.fireballCapsulePrice7, self.flowerCapsulePrice7, self.eggCapsulePrice7, self.vacuumCapsulePrice7, self.magicCapsulePrice7, self.tripleCapsulePrice7, self.koopaCapsulePrice7]
            weightsNames7 = [self.mushroomCapsuleWeight7, self.goldenMushroomCapsuleWeight7, self.slowMushroomCapsuleWeight7, self.metalMushroomCapsuleWeight7, self.flutterCapsuleWeight7, self.cannonCapsuleWeight7, self.snackCapsuleWeight7, self.lakituCapsuleWeight7, self.hammerBroCapsuleWeight7, self.plantCapsuleWeight7, self.spearCapsuleWeight7, self.kamekCapsuleWeight7, self.toadyCapsuleWeight7, self.blizzardCapsuleWeight7, self.banditCapsuleWeight7, self.pinkBooCapsuleWeight7, self.spinyCapsuleWeight7, self.zapCapsuleWeight7, self.tweesterCapsuleWeight7, self.thwompCapsuleWeight7, self.warpCapsuleWeight7, self.bombCapsuleWeight7, self.fireballCapsuleWeight7, self.flowerCapsuleWeight7, self.eggCapsuleWeight7, self.vacuumCapsuleWeight7, self.magicCapsuleWeight7, self.tripleCapsuleWeight7, self.koopaCapsuleWeight7]

            # Update widgets with loaded values
            for index, widget in enumerate(pricesNames7):
                if widget and index < len(prices7In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(prices7In[index]))

            for index, widget in enumerate(weightsNames7):
                if widget and index < len(weights7In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(weights7In[index]))
            print("MPT file laoded successfully!")
            createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

    def savePresetItems6(self):
        if not self.duelCapsulePrice6.get() or not self.duelCapsuleWeight6.get() or not self.metalMushroomCapsulePrice6.get() or not self.metalMushroomCapsuleWeight6.get() or not self.mushroomCapsuleWeight6.get() or not self.goldenMushroomCapsulePrice6.get() or not self.goldenMushroomCapsuleWeight6.get() or not self.slowMushroomCapsulePrice6.get() or not self.slowMushroomCapsuleWeight6.get() or not self.bulletBillCapsulePrice6.get() or not self.bulletBillCapsuleWeight6.get() or not self.warpPipeCapsulePrice6.get() or not self.warpPipeCapsuleWeight6.get() or not self.flutterCapsulePrice6.get() or not self.flutterCapsuleWeight6.get() or not self.cursedMushroomCapsulePrice6.get() or not self.cursedMushroomCapsuleWeight6.get() or not self.spinyCapsulePrice6.get() or not self.spinyCapsuleWeight6.get() or not self.goombaCapsuleWeight6.get() or not self.goombaCapsulePrice6.get() or not self.plantCapsulePrice6.get() or not self.plantCapsuleWeight6.get() or not self.kleptoCapsuleWeight6.get() or not self.kleptoCapsulePrice6.get() or not self.kamekCapsuleWeight6.get() or not self.kamekCapsulePrice6.get() or not self.toadyCapsuleWeight6.get() or not self.toadyCapsulePrice6.get() or not self.blizzardCapsuleWeight6.get() or not self.blizzardCapsulePrice6.get() or not self.podobooCapsulePrice6.get() or not self.podobooCapsuleWeight6.get() or not self.paraTroopaCapsuleWeight6.get() or not self.paraTroopaCapsulePrice6.get() or not self.snackCapsulePrice6.get() or not self.snackCapsuleWeight6.get() or not self.zapCapsulePrice6.get() or not self.zapCapsuleWeight6.get() or not self.tweesterCapsulePrice6.get() or not self.tweesterCapsuleWeight6.get() or not self.thwompCapsulePrice6.get() or not self.thwompCapsuleWeight6.get() or not self.warpPipeCapsulePrice6.get() or not self.warpPipeCapsuleWeight6.get() or not self.bombCapsulePrice6.get() or not self.bombCapsuleWeight6.get() or not self.gaddLightCapsulePrice6.get() or not self.gaddLightCapsuleWeight6.get() or not self.chanceTimeCapsulePrice6.get() or not self.chanceTimeCapsuleWeight6.get() or not self.pinkBooCapsulePrice6.get() or not self.pinkBooCapsuleWeight6.get() or not self.bowserCapsulePrice6.get() or not self.bowserCapsuleWeight6.get() or not self.dkCapsulePrice6.get() or not self.dkCapsuleWeight6.get():
            if sys.platform == "darwin":
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            else:
                createDialog("Error", "error", "Please fill out all the boxes.", None)
            return
        
        mushroomCapsuleWeight6 = self.mushroomCapsuleWeight6.get()
        
        goldenMushroomCapsulePrice6 = self.goldenMushroomCapsulePrice6.get()
        goldenMushroomCapsuleWeight6 = self.goldenMushroomCapsuleWeight6.get()

        slowMushroomCapsulePrice6 = self.slowMushroomCapsulePrice6.get()
        slowMushroomCapsuleWeight6 = self.slowMushroomCapsuleWeight6.get()

        metalMushroomCapsulePrice6 = self.metalMushroomCapsulePrice6.get()
        metalMushroomCapsuleWeight6 = self.metalMushroomCapsuleWeight6.get()

        bulletBillCapsulePrice6 = self.bulletBillCapsulePrice6.get()
        bulletBillCapsuleWeight6 = self.bulletBillCapsuleWeight6.get()

        flutterCapsulePrice6 = self.flutterCapsulePrice6.get()
        flutterCapsuleWeight6 = self.flutterCapsuleWeight6.get()

        cursedMushroomCapsulePrice6 = self.cursedMushroomCapsulePrice6.get()
        cursedMushroomCapsuleWeight6 = self.cursedMushroomCapsuleWeight6.get()

        spinyCapsulePrice6 = self.spinyCapsulePrice6.get()
        spinyCapsuleWeight6 = self.spinyCapsuleWeight6.get()

        goombaCapsulePrice6 = self.goombaCapsulePrice6.get()
        goombaCapsuleWeight6 = self.goombaCapsuleWeight6.get()

        plantCapsulePrice6 = self.plantCapsulePrice6.get()
        plantCapsuleWeight6 = self.plantCapsuleWeight6.get()

        kleptoCapsulePrice6 = self.kleptoCapsulePrice6.get()
        kleptoCapsuleWeight6 = self.kleptoCapsuleWeight6.get()

        kamekCapsulePrice6 = self.kamekCapsulePrice6.get()
        kamekCapsuleWeight6 = self.kamekCapsuleWeight6.get()

        toadyCapsulePrice6 = self.toadyCapsulePrice6.get()
        toadyCapsuleWeight6 = self.toadyCapsuleWeight6.get()

        blizzardCapsulePrice6 = self.blizzardCapsulePrice6.get()
        blizzardCapsuleWeight6 = self.blizzardCapsuleWeight6.get()

        podobooCapsulePrice6 = self.podobooCapsulePrice6.get()
        podobooCapsuleWeight6 = self.podobooCapsuleWeight6.get()

        paraTroopaCapsulePrice6 = self.paraTroopaCapsulePrice6.get()
        paraTroopaCapsuleWeight6 = self.paraTroopaCapsuleWeight6.get()

        snackCapsulePrice6 = self.snackCapsulePrice6.get()
        snackCapsuleWeight6 = self.snackCapsuleWeight6.get()

        zapCapsulePrice6 = self.zapCapsulePrice6.get()
        zapCapsuleWeight6 = self.zapCapsuleWeight6.get()

        tweesterCapsulePrice6 = self.tweesterCapsulePrice6.get()
        tweesterCapsuleWeight6 = self.tweesterCapsuleWeight6.get()

        thwompCapsulePrice6 = self.thwompCapsulePrice6.get()
        thwompCapsuleWeight6 = self.thwompCapsuleWeight6.get()

        warpPipeCapsulePrice6 = self.warpPipeCapsulePrice6.get()
        warpPipeCapsuleWeight6 = self.warpPipeCapsuleWeight6.get()

        bombCapsulePrice6 = self.bombCapsulePrice6.get()
        bombCapsuleWeight6 = self.bombCapsuleWeight6.get()

        gaddLightCapsulePrice6 = self.gaddLightCapsulePrice6.get()
        gaddLightCapsuleWeight6 = self.gaddLightCapsuleWeight6.get()

        pinkBooCapsulePrice6 = self.pinkBooCapsulePrice6.get()
        pinkBooCapsuleWeight6 = self.pinkBooCapsuleWeight6.get()

        chanceTimeCapsulePrice6 = self.chanceTimeCapsulePrice6.get()
        chanceTimeCapsuleWeight6 = self.chanceTimeCapsuleWeight6.get()

        bowserCapsulePrice6 = self.bowserCapsulePrice6.get()
        bowserCapsuleWeight6 = self.bowserCapsuleWeight6.get()

        dkCapsulePrice6 = self.dkCapsulePrice6.get()
        dkCapsuleWeight6 = self.dkCapsuleWeight6.get()

        duelCapsulePrice6 = self.duelCapsulePrice6.get()
        duelCapsuleWeight6 = self.duelCapsuleWeight6.get()


        prices6 = ["5", goldenMushroomCapsulePrice6, slowMushroomCapsulePrice6, metalMushroomCapsulePrice6, bulletBillCapsulePrice6, flutterCapsulePrice6, cursedMushroomCapsulePrice6, spinyCapsulePrice6, goombaCapsulePrice6, plantCapsulePrice6, kleptoCapsulePrice6, kamekCapsulePrice6, toadyCapsulePrice6, blizzardCapsulePrice6, podobooCapsulePrice6, paraTroopaCapsulePrice6, snackCapsulePrice6, zapCapsulePrice6, tweesterCapsulePrice6, thwompCapsulePrice6, warpPipeCapsulePrice6, bombCapsulePrice6, gaddLightCapsulePrice6, pinkBooCapsulePrice6, chanceTimeCapsulePrice6, bowserCapsulePrice6, dkCapsulePrice6, duelCapsulePrice6]
        weights6 = [mushroomCapsuleWeight6, goldenMushroomCapsuleWeight6, slowMushroomCapsuleWeight6, metalMushroomCapsuleWeight6, bulletBillCapsuleWeight6, flutterCapsuleWeight6, cursedMushroomCapsuleWeight6, spinyCapsuleWeight6, goombaCapsuleWeight6, plantCapsuleWeight6, kleptoCapsuleWeight6, kamekCapsuleWeight6, toadyCapsuleWeight6, blizzardCapsuleWeight6, podobooCapsuleWeight6, paraTroopaCapsuleWeight6, snackCapsuleWeight6, zapCapsuleWeight6, tweesterCapsuleWeight6, thwompCapsuleWeight6, warpPipeCapsuleWeight6, bombCapsuleWeight6, gaddLightCapsuleWeight6, pinkBooCapsuleWeight6, chanceTimeCapsuleWeight6, bowserCapsuleWeight6, dkCapsuleWeight6, duelCapsuleWeight6]

        file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
        if file_path:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Prices', 'Weights'])
                for price, weight in zip(prices6, weights6):
                    writer.writerow([price, weight])
            print("MPT file saved successfully!")
            createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)


    def loadPresetItems6(self):
        file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
        if file_path:
            prices6In = []
            weights6In = []
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    prices6In.append(float(row[0]))
                    weights6In.append(float(row[1]))
            testVar = ""
            # Define a list of Entry widget attributes
            pricesNames6 = [testVar, self.goldenMushroomCapsulePrice6, self.slowMushroomCapsulePrice6, self.metalMushroomCapsulePrice6, self.bulletBillCapsulePrice6, self.flutterCapsulePrice6, self.cursedMushroomCapsulePrice6, self.spinyCapsulePrice6, self.goombaCapsulePrice6, self.plantCapsulePrice6, self.kleptoCapsulePrice6, self.kamekCapsulePrice6, self.toadyCapsulePrice6, self.blizzardCapsulePrice6, self.podobooCapsulePrice6, self.paraTroopaCapsulePrice6, self.snackCapsulePrice6, self.zapCapsulePrice6, self.tweesterCapsulePrice6, self.thwompCapsulePrice6, self.warpPipeCapsulePrice6, self.bombCapsulePrice6, self.gaddLightCapsulePrice6, self.pinkBooCapsulePrice6, self.chanceTimeCapsulePrice6, self.bowserCapsulePrice6, self.dkCapsulePrice6, self.duelCapsulePrice6]
            weightsNames6 = [self.mushroomCapsuleWeight6, self.goldenMushroomCapsuleWeight6, self.slowMushroomCapsuleWeight6, self.metalMushroomCapsuleWeight6, self.bulletBillCapsuleWeight6, self.flutterCapsuleWeight6, self.cursedMushroomCapsuleWeight6, self.spinyCapsuleWeight6, self.goombaCapsuleWeight6, self.plantCapsuleWeight6, self.kleptoCapsuleWeight6, self.kamekCapsuleWeight6, self.toadyCapsuleWeight6, self.blizzardCapsuleWeight6, self.podobooCapsuleWeight6, self.paraTroopaCapsuleWeight6, self.snackCapsuleWeight6, self.zapCapsuleWeight6, self.tweesterCapsuleWeight6, self.thwompCapsuleWeight6, self.warpPipeCapsuleWeight6, self.bombCapsuleWeight6, self.gaddLightCapsuleWeight6, self.pinkBooCapsuleWeight6, self.chanceTimeCapsuleWeight6, self.bowserCapsuleWeight6, self.dkCapsuleWeight6, self.duelCapsuleWeight6]

            # Update widgets with loaded values
            for index, widget in enumerate(pricesNames6):
                if widget and index < len(prices6In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(prices6In[index]))

            for index, widget in enumerate(weightsNames6):
                if widget and index < len(weights6In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(weights6In[index]))
            print("MPT file laoded successfully!")
            createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

    def mp1ButtonEvent(self):
        self.mario_party_1_button.configure(state="disabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 1")

    def mp2ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="disabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 2")

    def mp3ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="disabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 3")

    def mp4ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="disabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 4")

    def mp5ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="disabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 5")

    def mp6ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="disabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 6")

    def mp7ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="disabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 7")

    def mp8ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="disabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 8 (Rev. 1)")

    def mp82ButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="disabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Mario Party 8 (Rev. 2)")

    def creditsButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="enabled")
        self.credits_button.configure(state="disabled")
        self.reset_game_frames()
        self.create_game_frame("Credits")

    def codeInjectorButtonEvent(self):
        self.mario_party_1_button.configure(state="enabled")
        self.mario_party_2_button.configure(state="enabled")
        self.mario_party_3_button.configure(state="enabled")
        self.mario_party_4_button.configure(state="enabled")
        self.mario_party_5_button.configure(state="enabled")
        self.mario_party_6_button.configure(state="enabled")
        self.mario_party_7_button.configure(state="enabled")
        self.mario_party_8_button.configure(state="enabled")
        self.mario_party_82_button.configure(state="enabled")
        self.codeInjector_button.configure(state="disabled")
        self.credits_button.configure(state="enabled")
        self.reset_game_frames()
        self.create_game_frame("Code Injector")

if __name__ == "__main__":
    app = App()
    app.mainloop()