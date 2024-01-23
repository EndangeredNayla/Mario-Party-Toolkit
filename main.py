# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 1/23/2024
# License: MIT
# ============================================


import tkinter
import tkinter.messagebox
import customtkinter
import version
import tkinter as tk
import pyperclip

from CTkToolTip import *

from functions import *
from credits import *
from codes import *

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Mario Party: Toolkit")
        self.geometry(f"{1100}x{680}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Mario Party Toolkit", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.mario_party_1_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 1", command=self.mp1ButtonEvent)
        self.mario_party_1_button.grid(row=1, column=0, padx=20, pady=10)

        self.mario_party_2_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 2", command=self.mp2ButtonEvent)
        self.mario_party_2_button.grid(row=2, column=0, padx=20, pady=10)

        self.mario_party_3_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 3", command=self.mp3ButtonEvent)
        self.mario_party_3_button.grid(row=3, column=0, padx=20, pady=10)

        self.mario_party_4_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 4", command=self.mp4ButtonEvent)
        self.mario_party_4_button.grid(row=4, column=0, padx=20, pady=10)

        self.mario_party_5_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 5", command=self.mp5ButtonEvent)
        self.mario_party_5_button.grid(row=5, column=0, padx=20, pady=10)
        
        self.mario_party_6_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 6", command=self.mp6ButtonEvent)
        self.mario_party_6_button.grid(row=6, column=0, padx=20, pady=10)

        self.mario_party_7_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 7", command=self.mp7ButtonEvent)
        self.mario_party_7_button.grid(row=7, column=0, padx=20, pady=10)

        self.mario_party_8_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 8 (Rev. 1)", command=self.mp8ButtonEvent)
        self.mario_party_8_button.grid(row=8, column=0, padx=20, pady=10)

        self.mario_party_82_button = customtkinter.CTkButton(self.sidebar_frame, text="Mario Party 8 (Rev. 2)", command=self.mp82ButtonEvent)
        self.mario_party_82_button.grid(row=9, column=0, padx=20, pady=10)

        self.credits_button = customtkinter.CTkButton(self.sidebar_frame, text="Credits", command=self.creditsButtonEvent)
        self.credits_button.grid(row=11, column=0, padx=20, pady=10)
        
        self.version_label = customtkinter.CTkLabel(self.sidebar_frame, text=f"Version: {version.appVersion}", anchor="w", font=("Arial", 14, "bold"))
        self.version_label.grid(row=13, column=0, padx=20, pady=(10, 0))

        self.current_game_frame = None  # To keep track of the currently displayed game frame
    
        # set default values
        self.mario_party_1_button.configure(state="disabled")

    
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

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
        elif game_name == "Credits":
            self.current_game_frame = self.create_credits_frame()
        self.current_game_frame.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), rowspan=3, sticky="nsew")

    def create_mp1_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconOne = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountOne = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountOne.grid(row=1, column=3)
        blueSpaceLabel1 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel1.grid(row=1, column=4)
        self.blueSpaceTickboxOne = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.blueSpaceTickboxOne.grid(row=1, column=5, padx=10, pady=10)
        
        # Create red space icon and entry, and tickbox
        redSpaceIconOne = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountOne = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountOne.grid(row=2, column=3)
        redSpaceLabel1 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel1.grid(row=2, column=4)
        self.redSpaceTickboxOne = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.redSpaceTickboxOne.grid(row=2, column=5, padx=10, pady=10)

        parseButtonOne = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonOne, text="Generate Codes")
        parseButtonOne.place(x=345, y=530)

        return frame

    def create_mp2_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconTwo = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountTwo = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountTwo.grid(row=1, column=3)
        blueSpaceLabel2 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel2.grid(row=1, column=4)
        self.blueSpaceTickboxTwo = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.blueSpaceTickboxTwo.grid(row=1, column=5, padx=10, pady=10)

        # Create red space icon and entry, and tickbox
        redSpaceIconTwo = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountTwo = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountTwo.grid(row=2, column=3)
        redSpaceLabel2 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel2.grid(row=2, column=4)
        self.redSpaceTickboxTwo = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.redSpaceTickboxTwo.grid(row=2, column=5, padx=10, pady=10)

        parseButtonTwo = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonTwo, text="Generate Codes")
        parseButtonTwo.place(x=345, y=530)

        return frame

    def create_mp3_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry, and tickbox
        blueSpaceIconThree = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountThree = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountThree.grid(row=1, column=3)
        blueSpaceLabel3 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel3.grid(row=1, column=4)
        self.blueSpaceTickboxThree = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.blueSpaceTickboxThree.grid(row=1, column=5, padx=10, pady=10)

        # Create red space icon and entry, and tickbox
        redSpaceIconThree = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountThree = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountThree.grid(row=2, column=3)
        redSpaceLabel3 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel3.grid(row=2, column=4)
        self.redSpaceTickboxThree = ctk.CTkCheckBox(master=tabview.tab("Space Modifiers"), text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
        self.redSpaceTickboxThree.grid(row=2, column=5, padx=10, pady=10)
        parseButtonThree = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonThree, text="Generate Codes")
        parseButtonThree.place(x=345, y=530)
        return frame


    def create_mp4_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconFour = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountFour.grid(row=1, column=3)
        blueSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel4.grid(row=1, column=4)

        # Create red space icon and entry
        redSpaceIconFour = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountFour.grid(row=2, column=3)
        redSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel4.grid(row=2, column=4)

        # Create star space icon and entry
        starSpaceIconFour = create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Costs  ", font=("Arial", 18))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountFour = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.starSpaceAmountFour.grid(row=3, column=3)
        starSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        starSpaceLabel4.grid(row=3, column=4)

        parseButtonFour = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonFour, text="Generate Codes")
        parseButtonFour.place(x=345, y=530)
        return frame

    def create_mp5_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountFive.grid(row=1, column=3)
        blueSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel4.grid(row=1, column=4)

        # Create red space icon and entry
        redSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountFive.grid(row=2, column=3)
        redSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel5.grid(row=2, column=4)

        # Create star space icon and entry
        starSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Costs  ", font=("Arial", 18))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.starSpaceAmountFive.grid(row=3, column=3)
        starSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        starSpaceLabel5.grid(row=3, column=4)

        # Create wiggler space icon and entry
        wigglerSpaceIconFive = create_image_icon(tabview.tab("Space Modifiers"), "assets/wigglerCapsule.png", 4, 1)
        wigglerSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Costs  ", font=("Arial", 18))
        wigglerSpaceLabel.grid(row=4, column=2)
        self.wigglerSpaceAmountFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.wigglerSpaceAmountFive.grid(row=4, column=3)
        wigglerSpaceLabel5 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        wigglerSpaceLabel5.grid(row=4, column=4)

        parseButtonFive = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonFive, text="Generate Codes")
        parseButtonFive.place(x=345, y=530)
        return frame

    def create_mp6_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconSix = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountSix.grid(row=1, column=3)
        blueSpaceLabel4 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel4.grid(row=1, column=4)

        # Create red space icon and entry
        redSpaceIconSix = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountSix.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel6.grid(row=2, column=4)

        # Create star space icon and entry
        starSpaceIconSix = create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Costs  ", font=("Arial", 18))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountSix = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.starSpaceAmountSix.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        starSpaceLabel6.grid(row=3, column=4)
        
        parseButtonSix = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonSix, text="Generate Codes")
        parseButtonSix.place(x=345, y=530)
        return frame

    def create_mp7_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconSeven = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountSeven.grid(row=1, column=3)
        blueSpaceLabel7 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel7.grid(row=1, column=4)

        # Create red space icon and entry
        redSpaceIconSeven = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountSeven.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel6.grid(row=2, column=4)

        # Create star space icon and entry
        starSpaceIconSeven= create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Costs  ", font=("Arial", 18))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountSeven = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.starSpaceAmountSeven.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        starSpaceLabel6.grid(row=3, column=4)

        # Create star space last five icon and entry
        starSpaceIconSeven= create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpaceLastFive.png", 4, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Costs  ", font=("Arial", 18))
        starSpaceLabel.grid(row=4, column=2)
        self.starSpaceAmountSevenLastFive = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.starSpaceAmountSevenLastFive.grid(row=4, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        starSpaceLabel6.grid(row=4, column=4)

        parseButtonSeven = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonSeven, text="Generate Codes")
        parseButtonSeven.place(x=345, y=530)
        return frame
    
    def create_credits_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
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
        return frame

    def create_mp82_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconEight2 = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountEight2.grid(row=1, column=3)
        blueSpaceLabel28 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel28.grid(row=1, column=4)

        # Create red space icon and entry
        redSpaceIconEight2 = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountEight2.grid(row=2, column=3)
        redSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel6.grid(row=2, column=4)

        # Create star space icon and entry
        starSpaceIconEight2= create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Costs  ", font=("Arial", 18))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountEight2 = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.starSpaceAmountEight2.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        starSpaceLabel6.grid(row=3, column=4)

        parseButtonEight2 = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonEight2, text="Generate Codes")
        parseButtonEight2.place(x=345, y=530)
        return frame
        
    def create_mp8_frame(self):
        frame = customtkinter.CTkFrame(self, fg_color=("#fcfcfc", "#2e2e2e"))
        tabview = customtkinter.CTkTabview(frame, width=2000, height=650, fg_color=("#fcfcfc", "#323232"))
        tabview.pack(padx=20, pady=20)
        tabview.add("Space Modifiers")
        tabview.set("Space Modifiers")

        # Create blue space icon and entry
        blueSpaceIconEight = create_image_icon(tabview.tab("Space Modifiers"), "assets/blueSpace.png", 1, 1)
        blueSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        blueSpaceLabel.grid(row=1, column=2)
        self.blueSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.blueSpaceAmountEight.grid(row=1, column=3)
        blueSpaceLabel8 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        blueSpaceLabel8.grid(row=1, column=4)

        # Create red space icon and entry
        redSpaceIconEight = create_image_icon(tabview.tab("Space Modifiers"), "assets/redSpace.png", 2, 1)
        redSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Gives  ", font=("Arial", 18))
        redSpaceLabel.grid(row=2, column=2)
        self.redSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.redSpaceAmountEight.grid(row=2, column=3)
        redSpaceLabel8 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        redSpaceLabel8.grid(row=2, column=4)

        # Create star space icon and entry
        starSpaceIconEight= create_image_icon(tabview.tab("Space Modifiers"), "assets/starSpace.png", 3, 1)
        starSpaceLabel = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Costs  ", font=("Arial", 18))
        starSpaceLabel.grid(row=3, column=2)
        self.starSpaceAmountEight = ctk.CTkEntry(master=tabview.tab("Space Modifiers"), width=48, font=("Arial", 18, "bold"))
        self.starSpaceAmountEight.grid(row=3, column=3)
        starSpaceLabel6 = ctk.CTkLabel(master=tabview.tab("Space Modifiers"), text=" Coins", font=("Arial", 18))
        starSpaceLabel6.grid(row=3, column=4)

        parseButtonEight = ctk.CTkButton(master=tabview.tab("Space Modifiers"), command=self.actionSpaceButtonEight, text="Generate Codes")
        parseButtonEight.place(x=345, y=530)
        return frame

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
    
        generatedCode = marioPartyOneRedSpace + marioPartyOneBlueSpace
        generatedCode = generatedCode.replace("ONEBLUESWITCH", "Doesn't Double on Last 5")
        generatedCode = generatedCode.replace("ONEREDSWITCH", "Doubles on Last 5")
        generatedCode = generatedCode.replace("ONERED", redSpaceAmountBaseOne)
        generatedCode = generatedCode.replace("ONEBLUE", blueSpaceAmountBaseOne)
    
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
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
    
        generatedCode = marioPartyTwoRedSpace + marioPartyTwoBlueSpace
        generatedCode = generatedCode.replace("TWOBLUESWITCH", "Doesn't Double on Last 5")
        generatedCode = generatedCode.replace("TWOREDSWITCH", "Doubles on Last 5")
        generatedCode = generatedCode.replace("TWORED", redSpaceAmountBaseTwo)
        generatedCode = generatedCode.replace("TWOBLUE", blueSpaceAmountBaseTwo)
    
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
    def actionSpaceButtonThree(self):
        if not self.blueSpaceAmountThree.get() and not self.redSpaceAmountThree.get():
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
    
    
        redSpaceSwitchThree = self.redSpaceTickboxThree.get()
        if redSpaceSwitchThree == True:
            redSpaceSwitchThree = "1"
        elif redSpaceSwitchThree == False:
            redSpaceSwitchThree = "0"
    
        marioPartyThreeBlueSpace = getBlueSpaceCodeThree(blueSpaceAmountThree, blueSpaceSwitchThree)
        marioPartyThreeRedSpace = getRedSpaceCodeThree(redSpaceAmountThree, redSpaceSwitchThree)
    
        if redSpaceAmountThree == "DUMMY":
            marioPartyThreeRedSpace = ""
        if blueSpaceAmountThree == "DUMMY":
            marioPartyThreeBlueSpace = ""
    
        generatedCode = marioPartyThreeRedSpace + marioPartyThreeBlueSpace
        generatedCode = generatedCode.replace("THREEBLUESWITCH", "Doesn't Double on Last 5")
        generatedCode = generatedCode.replace("THREEREDSWITCH", "Doubles on Last 5")
        generatedCode = generatedCode.replace("THREERED", redSpaceAmountBaseThree)
        generatedCode = generatedCode.replace("THREEBLUE", blueSpaceAmountBaseThree)
    
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
    def actionSpaceButtonFour(self):    
        if not self.blueSpaceAmountFour.get() and not self.redSpaceAmountFour.get() and not self.starSpaceAmountFour.get():
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

        starSpaceAmountFourBase = self.starSpaceAmountFour.get()

        try:
            starSpaceAmountFour = hex(int(self.starSpaceAmountFour.get()))
            if len(starSpaceAmountFour) == 4:
                starSpaceAmountFour = "00" + starSpaceAmountFour[2:]
            elif len(starSpaceAmountFour) == 3:
                starSpaceAmountFour = "000" + starSpaceAmountFour[2:]
        except:
            starSpaceAmountFour = "DUMMY"


        marioPartyFourBlueSpace = getBlueSpaceCodeFour(blueSpaceAmountFour)
        marioPartyFourRedSpace = getRedSpaceCodeFour(redSpaceAmountFour)
        marioPartyFourStarSpace = getStarSpaceCodeFour(starSpaceAmountFour)

        if redSpaceAmountFour == "DUMMY":
            marioPartyFourRedSpace = ""
        if blueSpaceAmountFour == "DUMMY":
            marioPartyFourBlueSpace = ""
        if starSpaceAmountFour == "DUMMY":
            marioPartyFourStarSpace = ""

        generatedCode = marioPartyFourRedSpace + marioPartyFourBlueSpace + marioPartyFourStarSpace
        generatedCode = generatedCode.replace("FOURRED", redSpaceAmountBaseFour)
        generatedCode = generatedCode.replace("FOURBLUE", blueSpaceAmountBaseFour)
        generatedCode = generatedCode.replace("FOURSTAR", starSpaceAmountFourBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
    def actionSpaceButtonFive(self):
        if not self.blueSpaceAmountFive.get() and not self.redSpaceAmountFive.get() and not self.starSpaceAmountFive.get() and not self.wigglerSpaceAmountFive.get():
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

        starSpaceAmountFiveBase = self.starSpaceAmountFive.get()

        try:
            starSpaceAmountFive = hex(int(self.starSpaceAmountFive.get()))
            if len(starSpaceAmountFive) == 4:
                starSpaceAmountFive = "00" + starSpaceAmountFive[2:]
            elif len(starSpaceAmountFive) == 3:
                starSpaceAmountFive = "000" + starSpaceAmountFive[2:]

            negativeRedSpaceAmountBaseFive = -int(starSpaceAmountFiveBase)
            starSpaceAmountNegativeFive = format(negativeRedSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            starSpaceAmountFive = "DUMMY"
            starSpaceAmountNegativeFive = "DUMMY"

        wigglerSpaceAmountFiveBase = self.wigglerSpaceAmountFive.get()

        try:
            wigglerSpaceAmountFive = hex(int(self.wigglerSpaceAmountFive.get()))
            if len(wigglerSpaceAmountFive) == 4:
                wigglerSpaceAmountFive = "00" + wigglerSpaceAmountFive[2:]
            elif len(wigglerSpaceAmountFive) == 3:
                wigglerSpaceAmountFive = "000" + wigglerSpaceAmountFive[2:]

            negativeRedSpaceAmountBaseFive = -int(wigglerSpaceAmountFiveBase)
            wigglerSpaceAmountNegativeFive = format(negativeRedSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]

        except:
            wigglerSpaceAmountFive = "DUMMY"
            wigglerSpaceAmountNegativeFive = "DUMMY"

        marioPartyFiveStarSpace = getStarSpaceCodeFive(starSpaceAmountFive, starSpaceAmountNegativeFive)
        marioPartyFiveWigglerSpace = getWigglerSpaceCodeFive(wigglerSpaceAmountFive, wigglerSpaceAmountNegativeFive)
        marioPartyFiveBlueSpace = getBlueSpaceCodeFive(blueSpaceAmountFive)
        marioPartyFiveRedSpace = getRedSpaceCodeFive(redSpaceAmountFive)

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

        generatedCode = marioPartyFiveRedSpace + marioPartyFiveBlueSpace + marioPartyFiveStarSpace + marioPartyFiveWigglerSpace
        generatedCode = generatedCode.replace("FIVERED", redSpaceAmountBaseFive)
        generatedCode = generatedCode.replace("FIVEBLUE", blueSpaceAmountBaseFive)
        generatedCode = generatedCode.replace("FIVESTAR", starSpaceAmountFiveBase)
        generatedCode = generatedCode.replace("FIVEWIGGLER", wigglerSpaceAmountFiveBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
    def actionSpaceButtonSix(self):
        if not self.blueSpaceAmountSix.get() and not self.redSpaceAmountSix.get() and not self.starSpaceAmountSix.get():
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

        starSpaceAmountSixBase = self.starSpaceAmountSix.get()
        try:
            starSpaceAmountSix = hex(int(self.starSpaceAmountSix.get()))
            if len(starSpaceAmountSix) == 4:
                starSpaceAmountSix = "00" + starSpaceAmountSix[2:]
            elif len(starSpaceAmountSix) == 3:
                starSpaceAmountSix = "000" + starSpaceAmountSix[2:]
        except:
            starSpaceAmountSix = "DUMMY"

        marioPartySixBlueSpace = getBlueSpaceCodeSix(blueSpaceAmountSix)
        marioPartySixRedSpace = getRedSpaceCodeSix(redSpaceAmountSix)
        marioPartySixStarSpace = getStarSpaceCodeSix(starSpaceAmountSix)

        if redSpaceAmountSix == "DUMMY":
            marioPartySixRedSpace = ""
        if blueSpaceAmountSix == "DUMMY":
            marioPartySixBlueSpace = ""
        if starSpaceAmountSix == "DUMMY":
            marioPartySixStarSpace = ""

        generatedCode = marioPartySixRedSpace + marioPartySixBlueSpace + marioPartySixStarSpace
        generatedCode = generatedCode.replace("SIXRED", redSpaceAmountBaseSix)
        generatedCode = generatedCode.replace("SIXBLUE", blueSpaceAmountBaseSix)
        generatedCode = generatedCode.replace("SIXSTAR", starSpaceAmountSixBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)

    def actionSpaceButtonSeven(self):
        if not self.blueSpaceAmountSeven.get() and not self.redSpaceAmountSeven.get() and not self.starSpaceAmountSeven.get() and not self.starSpaceAmountSevenLastFive.get():
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

        marioPartySevenBlueSpace = getBlueSpaceCodeSeven(blueSpaceAmountSeven)
        marioPartySevenRedSpace = getRedSpaceCodeSeven(redSpaceAmountSeven)
        marioPartySevenStarSpace = getStarSpaceCodeSeven(starSpaceAmountSeven)
        marioPartySevenStarSpaceLastFive = getStarSpaceCodeSevenLastFive(starSpaceAmountSevenLastFive)

        if redSpaceAmountSeven == "DUMMY":
            marioPartySevenRedSpace = ""
        if blueSpaceAmountSeven == "DUMMY":
            marioPartySevenBlueSpace = ""
        if starSpaceAmountSeven == "DUMMY":
            marioPartySevenStarSpace = ""
        if starSpaceAmountSevenLastFive == "DUMMY":
            marioPartySevenStarSpaceLastFive = ""

        generatedCode = marioPartySevenRedSpace + marioPartySevenBlueSpace + marioPartySevenStarSpace + marioPartySevenStarSpaceLastFive
        generatedCode = generatedCode.replace("SEVENRED", redSpaceAmountBaseSeven)
        generatedCode = generatedCode.replace("SEVENBLUE", blueSpaceAmountBaseSeven)
        generatedCode = generatedCode.replace("SEVENSTAR", starSpaceAmountSevenBase)
        generatedCode = generatedCode.replace("SEVENSTLASTFIVE", starSpaceAmountSevenLastFiveBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
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

        generatedCode = marioPartyEightRedSpace + marioPartyEightBlueSpace + marioPartyEightStarSpace
        generatedCode = generatedCode.replace("EIGHTRED", redSpaceAmountBaseEight)
        generatedCode = generatedCode.replace("EIGHTBLUE", blueSpaceAmountBaseEight)
        generatedCode = generatedCode.replace("EIGHTSTAR", starSpaceAmountEightBase)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)
        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
    def actionSpaceButtonEight2(self):
        if not self.blueSpaceAmountEight2.get() and not self.redSpaceAmountEight2.get() and not self.starSpaceAmountEight2.get():
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
            if len(starSpaceAmountEight2) == 4:
                starSpaceAmountEight2 = "00" + starSpaceAmountEight2[2:]
            elif len(starSpaceAmountEight2) == 3:
                starSpaceAmountEight2 = "000" + starSpaceAmountEight2[2:]
            negativeRedSpaceAmountBaseEight2 = -int(starSpaceAmountEight2Base)
            starSpaceAmountNegativeEight2 = format(negativeRedSpaceAmountBaseEight2 & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
        except:
            starSpaceAmountEight2 = "DUMMY"
            starSpaceAmountNegativeEight2 = "DUMMY"

        marioPartyEight2StarSpace = getStarSpaceCodeEightGC(starSpaceAmountEight2, starSpaceAmountNegativeEight2)
        marioPartyEight2BlueSpace = getBlueSpaceCodeEightGC(blueSpaceAmountEight2)
        marioPartyEight2RedSpace = getRedSpaceCodeEightGC(redSpaceAmountEight2)

        if redSpaceAmountEight2 == "DUMMY":
            marioPartyEight2RedSpace = ""
        if blueSpaceAmountEight2 == "DUMMY":
            marioPartyEight2BlueSpace = ""
        if starSpaceAmountEight2 == "DUMMY":
            marioPartyFiveStarSpace = ""
        if starSpaceAmountNegativeEight2 == "DUMMY":
            marioPartyEight2StarSpace = ""

        generatedCode = marioPartyEight2RedSpace + marioPartyEight2BlueSpace + marioPartyEight2StarSpace
        generatedCode = generatedCode.replace("EIGHTREDGC", redSpaceAmountBaseEight2)
        generatedCode = generatedCode.replace("EIGHTBLUEGC", blueSpaceAmountBaseEight2)
        generatedCode = generatedCode.replace("EIGHTSTARGC", starSpaceAmountEight2Base)
        generatedCode = generatedCode.strip()
        pyperclip.copy(generatedCode)

        print("Generated codes copied to the clipboard.")
        createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!", None)
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
        self.credits_button.configure(state="disabled")
        self.reset_game_frames()
        self.create_game_frame("Credits")

if __name__ == "__main__":
    app = App()
    app.mainloop()