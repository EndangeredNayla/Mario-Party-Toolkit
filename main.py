# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 12/21/2023
# License: MIT
# ============================================

import customtkinter as ctk
from PIL import Image, ImageTk
import pyperclip
import sys
from pathlib import Path
from codes import *


def fetchResource(resource_path: Path) -> Path:
    try:  # Running as *.exe; fetch resource from temp directory
        base_path = Path(sys._MEIPASS)
    except AttributeError:  # Running as script; return unmodified path
        return resource_path
    else:   # Return temp resource path
        return base_path.joinpath(resource_path)

def create_image_icon(frame, image_path, row, column):
    # Create and configure the canvas with the provided image
    image = Image.open(fetchResource(image_path)).convert("RGBA")
    image = image.resize((32, 32))
    image_tk = ImageTk.PhotoImage(image)
    
    canvas = ctk.CTkCanvas(master=frame, background="#2b2b2b", highlightthickness=0, width=image.width, height=image.height)
    canvas.grid(row=row, column=column)
    canvas.create_image(0, 0, anchor="nw", image=image_tk)

    return canvas, image_tk

# Set the appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Create the main application window
app = ctk.CTk()
app.geometry("360x320")
app.title("Mario Party: Toolkit")

tabviewGame = ctk.CTkTabview(master=app)
tabviewGame.pack(padx=0, pady=0)
tabviewGame.add("MP1")
tabviewGame.add("MP2")
tabviewGame.add("MP3")
tabviewGame.add("MP4")
tabviewGame.add("MP5")
tabviewGame.add("MP6")
tabviewGame.add("MP7")
tabviewGame.add("MP8")

tabviewEight = ctk.CTkTabview(master=tabviewGame.tab("MP8"), height=20)
tabviewEight.pack(padx=0, pady=0)
tabviewEight.add("Space Modifier")
tabviewEight.add("Space Modifier (GC Mod)")

# Create a frame inside the "Space Modifier" tab
frameEight = ctk.CTkFrame(master=tabviewEight.tab("Space Modifier"), border_color="#2b2b2b")
frameEight.pack(padx=20, pady=20)

# Create blue space icon and entry
blueSpaceIconEight = create_image_icon(frameEight, "assets/blueSpace.png", 1, 1)
blueSpaceAmountEight = ctk.CTkEntry(master=frameEight, width=28)
blueSpaceAmountEight.grid(row=1, column=3)

# Create red space icon and entry
redSpaceIconEight = create_image_icon(frameEight, "assets/redSpace.png", 2, 1)
redSpaceAmountEight = ctk.CTkEntry(master=frameEight, width=28)
redSpaceAmountEight.grid(row=2, column=3)


# Create a frame inside the "Space Modifier" tab
frameEightGC = ctk.CTkFrame(master=tabviewEight.tab("Space Modifier (GC Mod)"), border_color="#2b2b2b")
frameEightGC.pack(padx=20, pady=20)

# Create blue space icon and entry
blueSpaceIconEightGC = create_image_icon(frameEightGC, "assets/blueSpace.png", 1, 1)
blueSpaceAmountEightGC = ctk.CTkEntry(master=frameEightGC, width=28)
blueSpaceAmountEightGC.grid(row=1, column=3)

# Create red space icon and entry
redSpaceIconEightGC = create_image_icon(frameEightGC, "assets/redSpace.png", 2, 1)
redSpaceAmountEightGC = ctk.CTkEntry(master=frameEightGC, width=28)
redSpaceAmountEightGC.grid(row=2, column=3)

tabviewSeven = ctk.CTkTabview(master=tabviewGame.tab("MP7"), height=20)
tabviewSeven.pack(padx=0, pady=0)
tabviewSeven.add("Space Modifier")

# Create a frame inside the "Space Modifier" tab    
frameSeven = ctk.CTkFrame(master=tabviewSeven.tab("Space Modifier"), border_color="#2b2b2b")
frameSeven.pack(padx=20, pady=20)

# Create blue space icon and entry
blueSpaceIconSeven = create_image_icon(frameSeven, "assets/blueSpace.png", 1, 1)
blueSpaceAmountSeven = ctk.CTkEntry(master=frameSeven, width=28)
blueSpaceAmountSeven.grid(row=1, column=3)

# Create red space icon and entry
redSpaceIconSeven = create_image_icon(frameSeven, "assets/redSpace.png", 2, 1)
redSpaceAmountSeven = ctk.CTkEntry(master=frameSeven, width=28)
redSpaceAmountSeven.grid(row=2, column=3)

# Create red space icon and entry
starSpaceIconSeven = create_image_icon(frameSeven, "assets/starSpace.png", 3, 1)
starSpaceIconSevenLastFive = create_image_icon(frameSeven, "assets/starSpaceLastFive.png", 4, 1)
starSpaceAmountSeven = ctk.CTkEntry(master=frameSeven, width=28)
starSpaceAmountSeven.grid(row=3, column=3)
starSpaceAmountSevenLastFive = ctk.CTkEntry(master=frameSeven, width=28)
starSpaceAmountSevenLastFive.grid(row=4, column=3)

tabviewSix = ctk.CTkTabview(master=tabviewGame.tab("MP6"), height=20)
tabviewSix.pack(padx=0, pady=0)
tabviewSix.add("Space Modifier")

# Create a frame inside the "Space Modifier" tab
frameSix = ctk.CTkFrame(master=tabviewSix.tab("Space Modifier"), border_color="#2b2b2b")
frameSix.pack(padx=20, pady=20)

# Create blue space icon and entry
blueSpaceIconSix = create_image_icon(frameSix, "assets/blueSpace.png", 1, 1)
blueSpaceAmountSix = ctk.CTkEntry(master=frameSix, width=28)
blueSpaceAmountSix.grid(row=1, column=3)

# Create red space icon and entry
redSpaceIconSix = create_image_icon(frameSix, "assets/redSpace.png", 2, 1)
redSpaceAmountSix = ctk.CTkEntry(master=frameSix, width=28)
redSpaceAmountSix.grid(row=2, column=3)

# Create star space icon and entry
starSpaceIconSix = create_image_icon(frameSix, "assets/starSpace.png", 3, 1)
starSpaceAmountSix = ctk.CTkEntry(master=frameSix, width=28)
starSpaceAmountSix.grid(row=3, column=3)

tabviewFive = ctk.CTkTabview(master=tabviewGame.tab("MP5"), height=20)
tabviewFive.pack(padx=0, pady=0)
tabviewFive.add("Space Modifier")

# Create a frame inside the "Space Modifier" tab
frameFive = ctk.CTkFrame(master=tabviewFive.tab("Space Modifier"), border_color="#2b2b2b")
frameFive.pack(padx=20, pady=20)

# Create blue space icon and entry
blueSpaceIconFive = create_image_icon(frameFive, "assets/blueSpace.png", 1, 1)
blueSpaceAmountFive = ctk.CTkEntry(master=frameFive, width=28)
blueSpaceAmountFive.grid(row=1, column=3)

# Create red space icon and entry
redSpaceIconFive = create_image_icon(frameFive, "assets/redSpace.png", 2, 1)
redSpaceAmountFive = ctk.CTkEntry(master=frameFive, width=28)
redSpaceAmountFive.grid(row=2, column=3)

tabviewFour = ctk.CTkTabview(master=tabviewGame.tab("MP4"), height=20)
tabviewFour.pack(padx=0, pady=0)
tabviewFour.add("Space Modifier")

# Create a frame inside the "Space Modifier" tab
frameFour = ctk.CTkFrame(master=tabviewFour.tab("Space Modifier"), border_color="#2b2b2b")
frameFour.pack(padx=20, pady=20)

# Create blue space icon and entry
blueSpaceIconFour = create_image_icon(frameFour, "assets/blueSpace.png", 1, 1)
blueSpaceAmountFour = ctk.CTkEntry(master=frameFour, width=28)
blueSpaceAmountFour.grid(row=1, column=3)

# Create red space icon and entry
redSpaceIconFour = create_image_icon(frameFour, "assets/redSpace.png", 2, 1)
redSpaceAmountFour = ctk.CTkEntry(master=frameFour, width=28)
redSpaceAmountFour.grid(row=2, column=3)

tabviewThree = ctk.CTkTabview(master=tabviewGame.tab("MP3"), height=20)
tabviewThree.pack(padx=0, pady=0)
tabviewThree.add("Space Modifier")

# Create a frame inside the "Space Modifier" tab
frameThree = ctk.CTkFrame(master=tabviewThree.tab("Space Modifier"), border_color="#2b2b2b")
frameThree.pack(padx=20, pady=20)

# Create blue space icon and entry, and tickbox
blueSpaceIconThree = create_image_icon(frameThree, "assets/blueSpace.png", 1, 1)
blueSpaceAmountThree = ctk.CTkEntry(master=frameThree, width=28)
blueSpaceAmountThree.grid(row=1, column=3)
blueSpaceTickboxThree = ctk.CTkCheckBox(master=frameThree, text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
blueSpaceTickboxThree.grid(row=1, column=5, padx=10, pady=10)

# Create red space icon and entry, and tickbox
redSpaceIconThree = create_image_icon(frameThree, "assets/redSpace.png", 2, 1)
redSpaceAmountThree = ctk.CTkEntry(master=frameThree, width=28)
redSpaceAmountThree.grid(row=2, column=3)
redSpaceTickboxThree = ctk.CTkCheckBox(master=frameThree, text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
redSpaceTickboxThree.grid(row=2, column=5, padx=10, pady=10)

tabviewTwo = ctk.CTkTabview(master=tabviewGame.tab("MP2"), height=20)
tabviewTwo.pack(padx=0, pady=0)
tabviewTwo.add("Space Modifier")

# Create a frame inside the "Space Modifier" tab
frameTwo = ctk.CTkFrame(master=tabviewTwo.tab("Space Modifier"), border_color="#2b2b2b")
frameTwo.pack(padx=20, pady=20)

# Create blue space icon and entry, and tickbox
blueSpaceIconTwo = create_image_icon(frameTwo, "assets/blueSpace.png", 1, 1)
blueSpaceAmountTwo = ctk.CTkEntry(master=frameTwo, width=28)
blueSpaceAmountTwo.grid(row=1, column=3)
blueSpaceTickboxTwo = ctk.CTkCheckBox(master=frameTwo, text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
blueSpaceTickboxTwo.grid(row=1, column=5, padx=10, pady=10)

# Create red space icon and entry, and tickbox
redSpaceIconTwo = create_image_icon(frameTwo, "assets/redSpace.png", 2, 1)
redSpaceAmountTwo = ctk.CTkEntry(master=frameTwo, width=28)
redSpaceAmountTwo.grid(row=2, column=3)
redSpaceTickboxTwo = ctk.CTkCheckBox(master=frameTwo, text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
redSpaceTickboxTwo.grid(row=2, column=5, padx=10, pady=10)

tabviewOne = ctk.CTkTabview(master=tabviewGame.tab("MP1"), height=20)
tabviewOne.pack(padx=0, pady=0)
tabviewOne.add("Space Modifier")

# Create a frame inside the "Space Modifier" tab
frameOne = ctk.CTkFrame(master=tabviewOne.tab("Space Modifier"), border_color="#2b2b2b")
frameOne.pack(padx=20, pady=20)

# Create blue space icon and entry, and tickbox
blueSpaceIconOne = create_image_icon(frameOne, "assets/blueSpace.png", 1, 1)
blueSpaceAmountOne = ctk.CTkEntry(master=frameOne, width=28)
blueSpaceAmountOne.grid(row=1, column=3)
blueSpaceTickboxOne = ctk.CTkCheckBox(master=frameOne, text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
blueSpaceTickboxOne.grid(row=1, column=5, padx=10, pady=10)

# Create red space icon and entry, and tickbox
redSpaceIconOne = create_image_icon(frameOne, "assets/redSpace.png", 2, 1)
redSpaceAmountOne = ctk.CTkEntry(master=frameOne, width=28)
redSpaceAmountOne.grid(row=2, column=3)
redSpaceTickboxOne = ctk.CTkCheckBox(master=frameOne, text="x2 on Last 5", width=16, checkbox_width=16, checkbox_height=16)
redSpaceTickboxOne.grid(row=2, column=5, padx=10, pady=10)

def parseCoinsEight():
    global blueSpaceAmountEight, redSpaceAmountEight

    if not blueSpaceAmountEight.get() and not redSpaceAmountEight.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseEight = blueSpaceAmountEight.get()
    try:
        blueSpaceAmountEight = hex(int(blueSpaceAmountEight.get()))
        if len(blueSpaceAmountEight) == 4:
            blueSpaceAmountEight = "00" + blueSpaceAmountEight[2:]
        elif len(blueSpaceAmountEight) == 3:
            blueSpaceAmountEight = "000" + blueSpaceAmountEight[2:]
    except:
        blueSpaceAmountEight = "DUMMY"

    redSpaceAmountBaseEight = redSpaceAmountEight.get()
    try:
        redSpaceAmountEight = int(redSpaceAmountBaseEight, 16)
        negativeRedSpaceAmountBaseEight = -int(redSpaceAmountBaseEight)
        redSpaceAmountEight = format(negativeRedSpaceAmountBaseEight & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
    except:
        redSpaceAmountEight = "DUMMY"

    marioPartyEightBlueSpace = getBlueSpaceCodeEight(blueSpaceAmountEight)
    marioPartyEightRedSpace = getRedSpaceCodeEight(redSpaceAmountEight)

    if redSpaceAmountEight == "DUMMY":
        marioPartyEightRedSpace = ""
    if blueSpaceAmountEight == "DUMMY":
        marioPartyEightBlueSpace = ""

    generatedCode = marioPartyEightRedSpace + marioPartyEightBlueSpace
    generatedCode = generatedCode.replace("EIGHTRED", redSpaceAmountBaseEight)
    generatedCode = generatedCode.replace("EIGHTBLUE", blueSpaceAmountBaseEight)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsEightGC():
    global blueSpaceAmountEightGC, redSpaceAmountEightGC

    if not blueSpaceAmountEightGC.get() and not redSpaceAmountEightGC.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseEightGC = blueSpaceAmountEightGC.get()
    try:
        blueSpaceAmountEightGC = hex(int(blueSpaceAmountEightGC.get()))
        if len(blueSpaceAmountEightGC) == 4:
            blueSpaceAmountEightGC = "00" + blueSpaceAmountEightGC[2:]
        elif len(blueSpaceAmountEightGC) == 3:
            blueSpaceAmountEightGC = "000" + blueSpaceAmountEightGC[2:]
    except:
        blueSpaceAmountEightGC = "DUMMY"

    redSpaceAmountBaseEightGC = redSpaceAmountEightGC.get()
    try:
        redSpaceAmountEightGC = int(redSpaceAmountBaseEightGC, 16)
        negativeRedSpaceAmountBaseEightGC = -int(redSpaceAmountBaseEightGC)
        redSpaceAmountEightGC = format(negativeRedSpaceAmountBaseEightGC & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
    except:
        redSpaceAmountEightGC = "DUMMY"

    marioPartyEightGCBlueSpace = getBlueSpaceCodeEightGC(blueSpaceAmountEightGC)
    marioPartyEightGCRedSpace = getRedSpaceCodeEightGC(redSpaceAmountEightGC)

    if redSpaceAmountEightGC == "DUMMY":
        marioPartyEightGCRedSpace = ""
    if blueSpaceAmountEightGC == "DUMMY":
        marioPartyEightGCBlueSpace = ""

    generatedCode = marioPartyEightGCRedSpace + marioPartyEightGCBlueSpace
    generatedCode = generatedCode.replace("EIGHTREDGC", redSpaceAmountBaseEightGC)
    generatedCode = generatedCode.replace("EIGHTBLUEGC", blueSpaceAmountBaseEightGC)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsSeven():
    global blueSpaceAmountSeven, redSpaceAmountSeven, starSpaceAmountSeven, starSpaceAmountSevenLastFive

    if not blueSpaceAmountSeven.get() and not redSpaceAmountSeven.get() and not starSpaceAmountSeven.get() and not starSpaceAmountSevenLastFive.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseSeven = blueSpaceAmountSeven.get()
    try:
        blueSpaceAmountSeven = hex(int(blueSpaceAmountSeven.get()))
        if len(blueSpaceAmountSeven) == 4:
            blueSpaceAmountSeven = "00" + blueSpaceAmountSeven[2:]
        elif len(blueSpaceAmountSeven) == 3:
            blueSpaceAmountSeven = "000" + blueSpaceAmountSeven[2:]
    except:
        blueSpaceAmountSeven = "DUMMY"

    redSpaceAmountBaseSeven = redSpaceAmountSeven.get()
    try:
        redSpaceAmountSeven = int(redSpaceAmountBaseSeven, 16)
        negativeRedSpaceAmountBaseSeven = -int(redSpaceAmountBaseSeven)
        redSpaceAmountSeven = format(negativeRedSpaceAmountBaseSeven & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
    except:
        redSpaceAmountSeven = "DUMMY"

    starSpaceAmountSevenBase = starSpaceAmountSeven.get()
    starSpaceAmountSevenLastFiveBase = starSpaceAmountSevenLastFive.get()

    try:
        starSpaceAmountSeven = hex(int(starSpaceAmountSeven.get()))
        if len(starSpaceAmountSeven) == 4:
            starSpaceAmountSeven = "00" + starSpaceAmountSeven[2:]
        elif len(starSpaceAmountSeven) == 3:
            starSpaceAmountSeven = "000" + starSpaceAmountSeven[2:]
    except:
        starSpaceAmountSeven = "DUMMY"

    try:
        starSpaceAmountSevenLastFive = hex(int(starSpaceAmountSevenLastFive.get()))
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
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsSix():
    global blueSpaceAmountSix, redSpaceAmountSix, starSpaceAmountSix

    if not blueSpaceAmountSix.get() and not redSpaceAmountSix.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseSix = blueSpaceAmountSix.get()
    try:
        blueSpaceAmountSix = hex(int(blueSpaceAmountSix.get()))
        if len(blueSpaceAmountSix) == 4:
            blueSpaceAmountSix = "00" + blueSpaceAmountSix[2:]
        elif len(blueSpaceAmountSix) == 3:
            blueSpaceAmountSix = "000" + blueSpaceAmountSix[2:]
    except:
        blueSpaceAmountSix = "DUMMY"
    
    redSpaceAmountBaseSix = redSpaceAmountSix.get()
    try:
        redSpaceAmountSix = int(redSpaceAmountBaseSix, 16)
        negativeRedSpaceAmountBaseSix = -int(redSpaceAmountBaseSix)
        redSpaceAmountSix = format(negativeRedSpaceAmountBaseSix & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
    except:
        redSpaceAmountSix = "DUMMY"

    starSpaceAmountSixBase = starSpaceAmountSix.get()

    try:
        starSpaceAmountSix = hex(int(starSpaceAmountSix.get()))
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
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsFive():
    global blueSpaceAmountFive, redSpaceAmountFive

    if not blueSpaceAmountFive.get() and not redSpaceAmountFive.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseFive = blueSpaceAmountFive.get()
    try:
        blueSpaceAmountFive = hex(int(blueSpaceAmountFive.get()))
        if len(blueSpaceAmountFive) == 4:
            blueSpaceAmountFive = "00" + blueSpaceAmountFive[2:]
        elif len(blueSpaceAmountFive) == 3:
            blueSpaceAmountFive = "000" + blueSpaceAmountFive[2:]
    except:
        blueSpaceAmountFive = "DUMMY"

    redSpaceAmountBaseFive = redSpaceAmountFive.get()
    try:
        redSpaceAmountFive = int(redSpaceAmountBaseFive, 16)
        negativeRedSpaceAmountBaseFive = -int(redSpaceAmountBaseFive)
        redSpaceAmountFive = format(negativeRedSpaceAmountBaseFive & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
    except:
        redSpaceAmountFive = "DUMMY"

    marioPartyFiveBlueSpace = getBlueSpaceCodeFive(blueSpaceAmountFive)
    marioPartyFiveRedSpace = getRedSpaceCodeFive(redSpaceAmountFive)

    if redSpaceAmountFive == "DUMMY":
        marioPartyFiveRedSpace = ""
    if blueSpaceAmountFive == "DUMMY":
        marioPartyFiveBlueSpace = ""

    generatedCode = marioPartyFiveRedSpace + marioPartyFiveBlueSpace
    generatedCode = generatedCode.replace("FIVERED", redSpaceAmountBaseFive)
    generatedCode = generatedCode.replace("FIVEBLUE", blueSpaceAmountBaseFive)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsFour():
    global blueSpaceAmountFour, redSpaceAmountFour

    if not blueSpaceAmountFour.get() and not redSpaceAmountFour.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseFour = blueSpaceAmountFour.get()
    try:
        blueSpaceAmountFour = hex(int(blueSpaceAmountFour.get()))
        if len(blueSpaceAmountFour) == 4:
            blueSpaceAmountFour = "00" + blueSpaceAmountFour[2:]
        elif len(blueSpaceAmountFour) == 3:
            blueSpaceAmountFour = "000" + blueSpaceAmountFour[2:]
    except:
        blueSpaceAmountFour = "DUMMY"
        
    redSpaceAmountBaseFour = redSpaceAmountFour.get()
    try:
        redSpaceAmountFour = int(redSpaceAmountBaseFour, 16)
        negativeRedSpaceAmountBaseFour = -int(redSpaceAmountBaseFour)
        redSpaceAmountFour = format(negativeRedSpaceAmountBaseFour & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
    except:
        redSpaceAmountFour = "DUMMY"

    marioPartyFourBlueSpace = getBlueSpaceCodeFour(blueSpaceAmountFour)
    marioPartyFourRedSpace = getRedSpaceCodeFour(redSpaceAmountFour)

    if redSpaceAmountFour == "DUMMY":
        marioPartyFourRedSpace = ""
    if blueSpaceAmountFour == "DUMMY":
        marioPartyFourBlueSpace = ""

    generatedCode = marioPartyFourRedSpace + marioPartyFourBlueSpace
    generatedCode = generatedCode.replace("FOURRED", redSpaceAmountBaseFour)
    generatedCode = generatedCode.replace("FOURBLUE", blueSpaceAmountBaseFour)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsThree():
    global blueSpaceAmountThree, redSpaceAmountThree

    if not blueSpaceAmountThree.get() and not redSpaceAmountThree.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseThree = blueSpaceAmountThree.get()
    try:
        blueSpaceAmountThree = hex(int(blueSpaceAmountThree.get()))
        if len(blueSpaceAmountThree) == 4:
            blueSpaceAmountThree = "00" + blueSpaceAmountThree[2:]
        elif len(blueSpaceAmountThree) == 3:
            blueSpaceAmountThree = "000" + blueSpaceAmountThree[2:]
    except:
        blueSpaceAmountThree = "DUMMY"

    blueSpaceSwitchThree = blueSpaceTickboxThree.get()
    if blueSpaceSwitchThree == True:
        blueSpaceSwitchThree = "1"
    elif blueSpaceSwitchThree == False:
        blueSpaceSwitchThree = "0"

    redSpaceAmountBaseThree = redSpaceAmountThree.get()
    try:
        redSpaceAmountThree = hex(int(redSpaceAmountThree.get()))
        if len(redSpaceAmountThree) == 4:
            redSpaceAmountThree = "00" + redSpaceAmountThree[2:]
        elif len(redSpaceAmountThree) == 3:
            redSpaceAmountThree = "000" + redSpaceAmountThree[2:]
    except:
        redSpaceAmountThree = "DUMMY"


    redSpaceSwitchThree = redSpaceTickboxThree.get()
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
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsTwo():
    global blueSpaceAmountTwo, redSpaceAmountTwo

    if not blueSpaceAmountTwo.get() and not redSpaceAmountTwo.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseTwo = blueSpaceAmountTwo.get()
    try:
        blueSpaceAmountTwo = hex(int(blueSpaceAmountTwo.get()))
        if len(blueSpaceAmountTwo) == 4:
            blueSpaceAmountTwo = "00" + blueSpaceAmountTwo[2:]
        elif len(blueSpaceAmountTwo) == 3:
            blueSpaceAmountTwo = "000" + blueSpaceAmountTwo[2:]
    except:
        blueSpaceAmountTwo = "DUMMY"

    blueSpaceSwitchTwo = blueSpaceTickboxTwo.get()
    if blueSpaceSwitchTwo == True:
        blueSpaceSwitchTwo = "1"
    elif blueSpaceSwitchTwo == False:
        blueSpaceSwitchTwo = "0"

    redSpaceAmountBaseTwo = redSpaceAmountTwo.get()
    try:
        redSpaceAmountTwo = hex(int(redSpaceAmountTwo.get()))
        if len(redSpaceAmountTwo) == 4:
            redSpaceAmountTwo = "00" + redSpaceAmountTwo[2:]
        elif len(redSpaceAmountTwo) == 3:
            redSpaceAmountTwo = "000" + redSpaceAmountTwo[2:]
    except:
        redSpaceAmountTwo = "DUMMY"


    redSpaceSwitchTwo = redSpaceTickboxTwo.get()
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
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsOne():
    global blueSpaceAmountOne, redSpaceAmountOne

    if not blueSpaceAmountOne.get() and not redSpaceAmountOne.get():
        createDialog("Error", "error", "No information provided.")
        return

    blueSpaceAmountBaseOne = blueSpaceAmountOne.get()
    try:
        blueSpaceAmountOne = hex(int(blueSpaceAmountOne.get()))
        if len(blueSpaceAmountOne) == 4:
            blueSpaceAmountOne = "00" + blueSpaceAmountOne[2:]
        elif len(blueSpaceAmountOne) == 3:
            blueSpaceAmountOne = "000" + blueSpaceAmountOne[2:]
    except:
        blueSpaceAmountOne = "DUMMY"

    blueSpaceSwitchOne = blueSpaceTickboxOne.get()
    if blueSpaceSwitchOne == True:
        blueSpaceSwitchOne = "1"
    elif blueSpaceSwitchOne == False:
        blueSpaceSwitchOne = "0"

    redSpaceAmountBaseOne = redSpaceAmountOne.get()
    try:
        redSpaceAmountOne = hex(int(redSpaceAmountOne.get()))
        if len(redSpaceAmountOne) == 4:
            redSpaceAmountOne = "00" + redSpaceAmountOne[2:]
        elif len(redSpaceAmountOne) == 3:
            redSpaceAmountOne = "000" + redSpaceAmountOne[2:]
    except:
        redSpaceAmountOne = "DUMMY"


    redSpaceSwitchOne = redSpaceTickboxOne.get()
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
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def createDialog(windowTitle, warn, info):
    completeWindow = ctk.CTkToplevel()
    completeWindow.geometry("500x145")
    completeWindow.title(windowTitle)
    
    # Load success image and display it in the success window
    img = ctk.CTkImage(Image.open(fetchResource("assets/" + warn + ".png")), size=(100, 100))
    imgLabel = ctk.CTkLabel(completeWindow, image=img, text="")
    imgLabel.grid(row=0, column=0, padx=10, pady=10)
    imgLabel.image = img  # Keep a reference to the image
    
    # Display success message in the success window
    label = ctk.CTkLabel(completeWindow, text=info, font=ctk.CTkFont(size=18))
    label.grid(row=0, column=1, padx=25, pady=10)
    completeWindow.focus()

# Labels and button configuration
preBlueLabelEight = ctk.CTkLabel(master=frameEight, text=":  Gives   ", font=("Arial", 12))
preBlueLabelEight.grid(row=1, column=2)

preRedLabelEight = ctk.CTkLabel(master=frameEight, text=":  Gives - ", font=("Arial", 12))
preRedLabelEight.grid(row=2, column=2)

coinsBlueLabelEight = ctk.CTkLabel(master=frameEight, text=" Coins", font=("Arial", 12))
coinsBlueLabelEight.grid(row=1, column=4)

coinsRedLabelEight = ctk.CTkLabel(master=frameEight, text=" Coins", font=("Arial", 12))
coinsRedLabelEight.grid(row=2, column=4)

parseButtonEight = ctk.CTkButton(master=tabviewEight.tab("Space Modifier"), command=parseCoinsEight, text="Generate Codes")
parseButtonEight.pack(padx=20, pady=20)

preBlueLabelEightGC = ctk.CTkLabel(master=frameEightGC, text=":  Gives   ", font=("Arial", 12))
preBlueLabelEightGC.grid(row=1, column=2)

preRedLabelEightGC = ctk.CTkLabel(master=frameEightGC, text=":  Gives - ", font=("Arial", 12))
preRedLabelEightGC.grid(row=2, column=2)

coinsBlueLabelEightGC = ctk.CTkLabel(master=frameEightGC, text=" Coins", font=("Arial", 12))
coinsBlueLabelEightGC.grid(row=1, column=4)

coinsRedLabelEightGC = ctk.CTkLabel(master=frameEightGC, text=" Coins", font=("Arial", 12))
coinsRedLabelEightGC.grid(row=2, column=4)

parseButtonEightGC = ctk.CTkButton(master=tabviewEight.tab("Space Modifier (GC Mod)"), command=parseCoinsEightGC, text="Generate Codes")
parseButtonEightGC.pack(padx=20, pady=20)

preBlueLabelSeven = ctk.CTkLabel(master=frameSeven, text=": Gives   ", font=("Arial", 12))
preBlueLabelSeven.grid(row=1, column=2)

preRedLabelSeven = ctk.CTkLabel(master=frameSeven, text=":  Gives - ", font=("Arial", 12))
preRedLabelSeven.grid(row=2, column=2)

coinsBlueLabelSeven = ctk.CTkLabel(master=frameSeven, text=" Coins", font=("Arial", 12))
coinsBlueLabelSeven.grid(row=1, column=4)

coinsRedLabelSeven = ctk.CTkLabel(master=frameSeven, text=" Coins", font=("Arial", 12))
coinsRedLabelSeven.grid(row=2, column=4)

coinsStarLabelSeven = ctk.CTkLabel(master=frameSeven, text=":  Costs   ", font=("Arial", 12))
coinsStarLabelSeven.grid(row=3, column=2)

coinsStarLabelSeven = ctk.CTkLabel(master=frameSeven, text=":  Costs   ", font=("Arial", 12))
coinsStarLabelSeven.grid(row=4, column=2)

parseButtonSeven = ctk.CTkButton(master=tabviewSeven.tab("Space Modifier"), command=parseCoinsSeven, text="Generate Codes")
parseButtonSeven.pack(padx=20, pady=20)

coinsRedLabelSeven = ctk.CTkLabel(master=frameSeven, text=" Coins", font=("Arial", 12))
coinsRedLabelSeven.grid(row=3, column=4)

coinsStarLabelSeven = ctk.CTkLabel(master=frameSeven, text=" Coins", font=("Arial", 12))
coinsStarLabelSeven.grid(row=4, column=4)

preBlueLabelSix = ctk.CTkLabel(master=frameSix, text=":  Gives   ", font=("Arial", 12))
preBlueLabelSix.grid(row=1, column=2)

preRedLabelSix = ctk.CTkLabel(master=frameSix, text=":  Gives - ", font=("Arial", 12))
preRedLabelSix.grid(row=2, column=2)

preBlueLabelSix = ctk.CTkLabel(master=frameSix, text=":  Costs   ", font=("Arial", 12))
preBlueLabelSix.grid(row=3, column=2)

coinsBlueLabelSix = ctk.CTkLabel(master=frameSix, text=" Coins", font=("Arial", 12))
coinsBlueLabelSix.grid(row=1, column=4)

coinsRedLabelSix = ctk.CTkLabel(master=frameSix, text=" Coins", font=("Arial", 12))
coinsRedLabelSix.grid(row=2, column=4)

parseButtonSix = ctk.CTkButton(master=tabviewSix.tab("Space Modifier"), command=parseCoinsSix, text="Generate Codes")
parseButtonSix.pack(padx=20, pady=20)

coinsStarLabelSix = ctk.CTkLabel(master=frameSix, text=" Coins", font=("Arial", 12))
coinsStarLabelSix.grid(row=3, column=4)

coinsStarLabelSeven = ctk.CTkLabel(master=frameSeven, text=":  Costs   ", font=("Arial", 12))
coinsStarLabelSeven.grid(row=4, column=2)

preBlueLabelFive = ctk.CTkLabel(master=frameFive, text=":  Costs   ", font=("Arial", 12))
preBlueLabelFive.grid(row=1, column=2)

preRedLabelFive = ctk.CTkLabel(master=frameFive, text=":  Gives - ", font=("Arial", 12))
preRedLabelFive.grid(row=2, column=2)

coinsBlueLabelFive = ctk.CTkLabel(master=frameFive, text=" Coins", font=("Arial", 12))
coinsBlueLabelFive.grid(row=1, column=4)

coinsRedLabelFive = ctk.CTkLabel(master=frameFive, text=" Coins", font=("Arial", 12))
coinsRedLabelFive.grid(row=2, column=4)

parseButtonFive = ctk.CTkButton(master=tabviewFive.tab("Space Modifier"), command=parseCoinsFive, text="Generate Codes")
parseButtonFive.pack(padx=20, pady=20)

preBlueLabelFour = ctk.CTkLabel(master=frameFour, text=":  Costs   ", font=("Arial", 12))
preBlueLabelFour.grid(row=1, column=2)

preRedLabelFour = ctk.CTkLabel(master=frameFour, text=":  Gives - ", font=("Arial", 12))
preRedLabelFour.grid(row=2, column=2)

coinsBlueLabelFour = ctk.CTkLabel(master=frameFour, text=" Coins", font=("Arial", 12))
coinsBlueLabelFour.grid(row=1, column=4)

coinsRedLabelFour = ctk.CTkLabel(master=frameFour, text=" Coins", font=("Arial", 12))
coinsRedLabelFour.grid(row=2, column=4)

parseButtonFour = ctk.CTkButton(master=tabviewFour.tab("Space Modifier"), command=parseCoinsFour, text="Generate Codes")
parseButtonFour.pack(padx=20, pady=20)

preBlueLabelThree = ctk.CTkLabel(master=frameThree, text=":  Costs   ", font=("Arial", 12))
preBlueLabelThree.grid(row=1, column=2)

preRedLabelThree = ctk.CTkLabel(master=frameThree, text=":  Gives - ", font=("Arial", 12))
preRedLabelThree.grid(row=2, column=2)

coinsBlueLabelThree = ctk.CTkLabel(master=frameThree, text=" Coins", font=("Arial", 12))
coinsBlueLabelThree.grid(row=1, column=4)

coinsRedLabelThree = ctk.CTkLabel(master=frameThree, text=" Coins", font=("Arial", 12))
coinsRedLabelThree.grid(row=2, column=4)

parseButtonThree = ctk.CTkButton(master=tabviewThree.tab("Space Modifier"), command=parseCoinsThree, text="Generate Codes")
parseButtonThree.pack(padx=20, pady=20)

preBlueLabelTwo = ctk.CTkLabel(master=frameTwo, text=":  Costs   ", font=("Arial", 12))
preBlueLabelTwo.grid(row=1, column=2)

preRedLabelTwo = ctk.CTkLabel(master=frameTwo, text=":  Gives - ", font=("Arial", 12))
preRedLabelTwo.grid(row=2, column=2)

coinsBlueLabelTwo = ctk.CTkLabel(master=frameTwo, text=" Coins", font=("Arial", 12))
coinsBlueLabelTwo.grid(row=1, column=4)

coinsRedLabelTwo = ctk.CTkLabel(master=frameTwo, text=" Coins", font=("Arial", 12))
coinsRedLabelTwo.grid(row=2, column=4)

parseButtonTwo = ctk.CTkButton(master=tabviewTwo.tab("Space Modifier"), command=parseCoinsTwo, text="Generate Codes")
parseButtonTwo.pack(padx=20, pady=20)

preBlueLabelOne = ctk.CTkLabel(master=frameOne, text=":  Costs   ", font=("Arial", 12))
preBlueLabelOne.grid(row=1, column=2)

preRedLabelOne = ctk.CTkLabel(master=frameOne, text=":  Gives - ", font=("Arial", 12))
preRedLabelOne.grid(row=2, column=2)

coinsBlueLabelOne = ctk.CTkLabel(master=frameOne, text=" Coins", font=("Arial", 12))
coinsBlueLabelOne.grid(row=1, column=4)

coinsRedLabelOne = ctk.CTkLabel(master=frameOne, text=" Coins", font=("Arial", 12))
coinsRedLabelOne.grid(row=2, column=4)

parseButtonOne = ctk.CTkButton(master=tabviewOne.tab("Space Modifier"), command=parseCoinsOne, text="Generate Codes")
parseButtonOne.pack(padx=20, pady=20)

# Run the main application loop
app.mainloop()