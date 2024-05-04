# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

from functions import *
from frames.marioParty1_frame import *

import customtkinter
import os
from PIL import Image
import tkinter as tk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mario Party Toolkit")
        self.geometry("1330x780")

        customtkinter.set_appearance_mode("Dark")


        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets/logos/")
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "homeDark.png")), dark_image=Image.open(os.path.join(image_path, "homeLight.png")), size=(32, 32))
        self.about_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "infoDark.png")), dark_image=Image.open(os.path.join(image_path, "infoLight.png")), size=(32, 32))
        self.mp1_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "marioParty1.png")), size=(172, 42))
        self.mp2_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "marioParty2.png")), size=(178, 42))
        self.mp3_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "marioParty3.png")), size=(172, 42))
        self.mp4_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "marioParty4.png")), size=(172, 42))
        self.mp5_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "marioParty5.png")), size=(172, 42))
        self.mp6_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "marioParty6.png")), size=(172, 42))
        self.mp7_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "marioParty7.png")), size=(172, 42))
        self.mp8_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "marioParty8.png")), size=(172, 42))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(11, weight=1)

        self.logo_label = create_banner(self.navigation_frame, "assets/logos/mpToolkit_logo.png", 0, 0)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, command=self.home_button_event, font=("Helvetica", 18, "bold"))
        self.home_button.grid(row=1, column=0, sticky="ew")

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

        self.about_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="About",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.about_image, command=self.about_button_event, font=("Helvetica", 18, "bold"))
        self.about_button.grid(row=10, column=0, sticky="ew")


        # create frames
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp1_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp2_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp3_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp4_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp5_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp6_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp7_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mp8_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.select_frame_by_name("home")

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
        self.about_button.configure(fg_color=("gray75", "gray25") if name == "aboutFrame" else "transparent")

        # show selected frame
        if name == "homeFrame":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "mp1Frame":
            self.mp1_frame.grid(row=0, column=1, sticky="nsew")
            create_mario_party_1_interface(self.mp1_frame)
        else:
            self.mp1_frame.grid_forget()
        if name == "mp2Frame":
            self.mp2_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mp2_frame.grid_forget()
        if name == "mp3Frame":
            self.mp3_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mp3_frame.grid_forget()
        if name == "mp4Frame":
            self.mp4_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mp4_frame.grid_forget()
        if name == "mp5Frame":
            self.mp5_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mp5_frame.grid_forget()
        if name == "mp6Frame":
            self.mp6_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mp6_frame.grid_forget()
        if name == "mp7Frame":
            self.mp7_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mp7_frame.grid_forget()
        if name == "mp8Frame":
            self.mp8_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mp8_frame.grid_forget()
        if name == "aboutFrame":
            self.about_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.about_frame.grid_forget()

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

    def about_button_event(self):
        self.select_frame_by_name("aboutFrame")

if __name__ == "__main__":
    app = App()
    app.mainloop()