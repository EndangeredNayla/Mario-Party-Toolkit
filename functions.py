# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/4/2024
# License: MIT
# ============================================

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
import requests
import sys
import webbrowser
from version import appVersion

def fetchResource(resource_path: Path) -> Path:
    try:  # Running as *.exe; fetch resource from temp directory
        base_path = Path(sys._MEIPASS)
    except AttributeError:  # Running as script; return unmodified path
        return resource_path
    else:   # Return temp resource path
        return base_path.joinpath(resource_path)

def create_image_icon(frame, image_path, row, column):
    # Create and configure the canvas with the provided image
    image = Image.open(fetchResource(image_path))
    image = image.resize((48, 48))
    image_tk = ImageTk.PhotoImage(image)
    label = tk.Label(frame, image=image_tk)
    label.configure(bg='#323232') # Windows fix
    label.image = image_tk  # Keep a reference to the image to prevent it from being garbage collected
    label.grid(row=row, column=column)

def check_for_updates():
    pastebin_url = "https://pastebin.com/raw/MrpYHUHy"
    response = requests.get(pastebin_url)
    
    if response.status_code == 200:
        latest_version = response.text.strip()
                
        if latest_version > appVersion:
            notification.notify(title= "Error", message = "Update Available!", app_icon=fetchResource("assets/diceBlock.ico"), timeout = 10)

    else:
        notification.notify(title= "Error", message = "Unable to check for updates!", app_icon=fetchResource("assets/diceBlock.ico"), timeout = 10)

def run_update():
    url = "https://github.com/EndangeredNayla/Mario-Party-Toolkit/releases"
    webbrowser.open_new_tab(url)
