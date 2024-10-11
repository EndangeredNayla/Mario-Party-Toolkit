# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 7/12/2024
# License: MIT
# ============================================

from functions import *
from frames.about_frame import *
from frames.injector_frame import *
from frames.marioParty1_frame import *
from frames.marioParty2_frame import *
from frames.marioParty3_frame import *
from frames.marioParty4_frame import *
from frames.marioParty5_frame import *
from frames.marioParty6_frame import *
from frames.marioParty7_frame import *
from frames.marioParty8_frame import *
from frames.marioParty9_frame import *
from frames.marioPartyDS_frame import *
from frames.welcome_frame import *
from version import *

import customtkinter
import os
import sys
import threading
from PIL import Image
import tkinter as tk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mario Party Toolkit")
        self.geometry("1342x900")
        customtkinter.set_appearance_mode("Dark")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/mpToolkit_logo.png"))), size=(172, 70))
        self.about_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/info.png"))), size=(32, 32))
        self.mp1_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty1.png"))), size=(172, 42))
        self.mp2_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty2.png"))), size=(178, 42))
        self.mp3_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty3.png"))), size=(172, 42))
        self.mp4_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty4.png"))), size=(172, 42))
        self.mp5_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty5.png"))), size=(172, 42))
        self.mp6_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty6.png"))), size=(172, 42))
        self.mp7_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty7.png"))), size=(172, 42))
        self.mp8_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty8.png"))), size=(172, 42))
        self.mp9_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioParty9.png"))), size=(172, 42))
        self.mpds_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/marioPartyDS.png"))), size=(172, 42))
        self.injector_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(fetchResource("assets/logos/injector.png"))), size=(32, 32))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(14, weight=2)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                   fg_color="transparent", hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=0, column=0, sticky="ew")

        self.mp1_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                   fg_color="transparent", hover_color=("gray70", "gray30"),
                                                   image=self.mp1_image, anchor="w", command=self.mp1_button_event)
        self.mp1_button.grid(row=2, column=0, sticky="ew")

        self.mp2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mp2_image, anchor="w", command=self.mp2_button_event)
        self.mp2_button.grid(row=3, column=0, sticky="ew")

        self.mp3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mp3_image, anchor="w", command=self.mp3_button_event)
        self.mp3_button.grid(row=4, column=0, sticky="ew")

        self.mp4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mp4_image, anchor="w", command=self.mp4_button_event)
        self.mp4_button.grid(row=5, column=0, sticky="ew")

        self.mp5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mp5_image, anchor="w", command=self.mp5_button_event)
        self.mp5_button.grid(row=6, column=0, sticky="ew")

        self.mp6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mp6_image, anchor="w", command=self.mp6_button_event)
        self.mp6_button.grid(row=7, column=0, sticky="ew")

        self.mp7_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mp7_image, anchor="w", command=self.mp7_button_event)
        self.mp7_button.grid(row=8, column=0, sticky="ew")

        self.mp8_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mp8_image, anchor="w", command=self.mp8_button_event)
        self.mp8_button.grid(row=9, column=0, sticky="ew")

        self.mp9_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mp9_image, anchor="w", command=self.mp9_button_event)
        self.mp9_button.grid(row=10, column=0, sticky="ew")
        
        self.mpDS_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text=None,
                                                      fg_color="transparent", hover_color=("gray70", "gray30"),
                                                      image=self.mpds_image, anchor="w", command=self.mpDS_button_event)
        self.mpDS_button.grid(row=11, column=0, sticky="ew")

        self.injector_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Injector",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.injector_image, command=self.injector_button_event, font=("Helvetica", 18, "bold"))
        self.injector_button.grid(row=13, column=0, sticky="ew")

        self.about_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.about_image, command=self.about_button_event, font=("Helvetica", 18, "bold"))
        self.about_button.grid(row=14, column=0, sticky="ew")

        self.versionPanel = ctk.CTkLabel(self.navigation_frame, text=versionString, font=("Helvetica", 18, "bold"))
        self.versionPanel.grid(row=15, column=0, sticky="ew")

        # create frames
        self.welcome_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp1_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp2_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp3_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp4_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp5_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp6_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp7_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp8_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp9_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mpDS_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.injector_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.welcome_frame.grid(row=0, column=1, sticky="nsew")
        welcome_interface(self.welcome_frame)
        self.home_button.configure(fg_color=("gray75", "gray25"))

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "homeFrame" else "transparent")
        self.mp1_button.configure(fg_color=("gray75", "gray25") if name == "mp1Frame" else "transparent")
        self.mp2_button.configure(fg_color=("gray75", "gray25") if name == "mp2Frame" else "transparent")
        self.mp3_button.configure(fg_color=("gray75", "gray25") if name == "mp3Frame" else "transparent")
        self.mp4_button.configure(fg_color=("gray75", "gray25") if name == "mp4Frame" else "transparent")
        self.mp5_button.configure(fg_color=("gray75", "gray25") if name == "mp5Frame" else "transparent")
        self.mp6_button.configure(fg_color=("gray75", "gray25") if name == "mp6Frame" else "transparent")
        self.mp7_button.configure(fg_color=("gray75", "gray25") if name == "mp7Frame" else "transparent")
        self.mp8_button.configure(fg_color=("gray75", "gray25") if name == "mp8Frame" else "transparent")
        self.mp9_button.configure(fg_color=("gray75", "gray25") if name == "mp9Frame" else "transparent")
        self.mpDS_button.configure(fg_color=("gray75", "gray25") if name == "mpDSFrame" else "transparent")
        self.about_button.configure(fg_color=("gray75", "gray25") if name == "aboutFrame" else "transparent")
        self.injector_button.configure(fg_color=("gray75", "gray25") if name == "injectorFrame" else "transparent")

        # show selected frame
        if name == "homeFrame":
            self.welcome_frame.grid(row=0, column=1, sticky="nsew")
            welcome_interface(self.welcome_frame)
        else:
            self.welcome_frame.grid_forget()
        if name == "mp1Frame":
            self.mp1_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_1_interface(self.mp1_frame)
        else:
            self.mp1_frame.grid_forget()
        if name == "mp2Frame":
            self.mp2_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_2_interface(self.mp2_frame)
        else:
            self.mp2_frame.grid_forget()
        if name == "mp3Frame":
            self.mp3_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_3_interface(self.mp3_frame)
        else:
            self.mp3_frame.grid_forget()
        if name == "mp4Frame":
            self.mp4_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_4_interface(self.mp4_frame)
        else:
            self.mp4_frame.grid_forget()
        if name == "mp5Frame":
            self.mp5_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_5_interface(self.mp5_frame)
        else:
            self.mp5_frame.grid_forget()
        if name == "mp6Frame":
            self.mp6_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_6_interface(self.mp6_frame)
        else:
            self.mp6_frame.grid_forget()
        if name == "mp7Frame":
            self.mp7_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_7_interface(self.mp7_frame)
        else:
            self.mp7_frame.grid_forget()
        if name == "mp8Frame":
            self.mp8_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_8_interface(self.mp8_frame)
        else:
            self.mp8_frame.grid_forget()
        if name == "mp9Frame":
            self.mp9_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_9_interface(self.mp9_frame)
        else:
            self.mp9_frame.grid_forget()
        if name == "mpDSFrame":
            self.mpDS_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_DS_interface(self.mpDS_frame)
        else:
            self.mpDS_frame.grid_forget()
        if name == "aboutFrame":
            self.about_frame.grid(row=0, column=1, sticky="nsew")
            about_interface(self.about_frame)
        else:
            self.about_frame.grid_forget()
        if name == "injectorFrame":
            self.injector_frame.grid(row=0, column=1, sticky="nsew")
            injector_interface(self.injector_frame)
        else:
            self.injector_frame.grid_forget()
    
    def home_button_event(self):
        self.select_frame_by_name("homeFrame")
    
    def mp1_button_event(self):
        self.select_frame_by_name("mp1Frame")

    def mp2_button_event(self):
        self.select_frame_by_name("mp2Frame")

    def mp3_button_event(self):
        self.select_frame_by_name("mp3Frame")

    def mp4_button_event(self):
        self.select_frame_by_name("mp4Frame")

    def mp5_button_event(self):
        self.select_frame_by_name("mp5Frame")

    def mp6_button_event(self):
        self.select_frame_by_name("mp6Frame")

    def mp7_button_event(self):
        self.select_frame_by_name("mp7Frame")

    def mp8_button_event(self):
        self.select_frame_by_name("mp8Frame")

    def mp9_button_event(self):
        self.select_frame_by_name("mp9Frame")

    def mpDS_button_event(self):
        self.select_frame_by_name("mpDSFrame")

    def injector_button_event(self):
        self.select_frame_by_name("injectorFrame")

    def about_button_event(self):
        self.select_frame_by_name("aboutFrame")

if __name__ == "__main__":
    app = App()
    app.resizable(width=False, height=False)
    threading.Thread(target=app.mainloop()).start()
    