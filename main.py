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


def fetchResource(resource_path:     Path) -> Path:
    try:     # Running as *.exe; fetch resource from temp directory
        base_path = Path(sys._MEIPASS)
    except AttributeError:     # Running as script; return unmodified path
        return resource_path
    else:     # Return temp resource path
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
app.geometry("360x280")
app.title("Mario Party:     Toolkit")

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


def parseCoinsEight():
    global blueSpaceAmountEight, redSpaceAmountEight

    if not blueSpaceAmountEight.get() and not redSpaceAmountEight.get():
        createDialog("Error", "error", "No information provided.")
        return

    try:
        blueSpaceAmountBaseEight = blueSpaceAmountEight.get()
        blueSpaceAmountEight = hex(int(blueSpaceAmountEight.get()))
        if len(blueSpaceAmountEight) == 4:
            blueSpaceAmountEight = "00" + blueSpaceAmountEight[2:]
        elif len(blueSpaceAmountEight) == 3:
            blueSpaceAmountEight = "000" + blueSpaceAmountEight[2:]
    except:
        blueSpaceAmountEight = "DUMMY"

    try:
        redSpaceAmountBaseEight = redSpaceAmountEight.get()
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

    try:
        blueSpaceAmountBaseEightGC = blueSpaceAmountEightGC.get()
        blueSpaceAmountEightGC = hex(int(blueSpaceAmountEightGC.get()))
        if len(blueSpaceAmountEightGC) == 4:
            blueSpaceAmountEightGC = "00" + blueSpaceAmountEightGC[2:]
        elif len(blueSpaceAmountEightGC) == 3:
            blueSpaceAmountEightGC = "000" + blueSpaceAmountEightGC[2:]
    except:
        blueSpaceAmountEightGC = "DUMMY"

    try:
        redSpaceAmountBaseEightGC = redSpaceAmountEightGC.get()
        redSpaceAmountEightGC = int(redSpaceAmountBaseEightGC, 16)
        negativeRedSpaceAmountBaseEightGC = -int(redSpaceAmountBaseEightGC)
        redSpaceAmountEightGC = format(negativeRedSpaceAmountBaseEightGC & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
    except:
        redSpaceAmountEight = "DUMMY"

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
    global blueSpaceAmountSeven, redSpaceAmountSeven

    if not blueSpaceAmountSeven.get() and not redSpaceAmountSeven.get():
        createDialog("Error", "error", "No information provided.")
        return

    try:
        blueSpaceAmountBaseSeven = blueSpaceAmountSeven.get()
        blueSpaceAmountSeven = hex(int(blueSpaceAmountSeven.get()))
        if len(blueSpaceAmountSeven) == 4:
            blueSpaceAmountSeven = "00" + blueSpaceAmountSeven[2:]
        elif len(blueSpaceAmountSeven) == 3:
            blueSpaceAmountSeven = "000" + blueSpaceAmountSeven[2:]
    except:
        blueSpaceAmountSeven = "DUMMY"

    try:
        redSpaceAmountBaseSeven = redSpaceAmountSeven.get()
        redSpaceAmountSeven = int(redSpaceAmountBaseSeven, 16)
        negativeRedSpaceAmountBaseSeven = -int(redSpaceAmountBaseSeven)
        redSpaceAmountSeven = format(negativeRedSpaceAmountBaseSeven & 0xFFFFFFFFFFFFFFFF, 'X')[12:]
    except:
        redSpaceAmountSeven = "DUMMY"
    marioPartySevenBlueSpace = getBlueSpaceCodeSeven(blueSpaceAmountSeven)
    marioPartySevenRedSpace = getRedSpaceCodeSeven(redSpaceAmountSeven)
    if redSpaceAmountSeven == "DUMMY":
        marioPartySevenRedSpace = ""
    if blueSpaceAmountSeven == "DUMMY":
        marioPartySevenBlueSpace = ""

    generatedCode = marioPartySevenRedSpace + marioPartySevenBlueSpace
    generatedCode = generatedCode.replace("SEVENRED", redSpaceAmountBaseSeven)
    generatedCode = generatedCode.replace("SEVENBLUE", blueSpaceAmountBaseSeven)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsSix():
    global blueSpaceAmountSix, redSpaceAmountSix

    if not blueSpaceAmountSix.get() and not redSpaceAmountSix.get():
        createDialog("Error", "error", "No information provided.")
        return

    try:
        blueSpaceAmountBaseSix = blueSpaceAmountSix.get()
        blueSpaceAmountSix = hex(int(blueSpaceAmountSix.get()))
        if len(blueSpaceAmountSix) == 4:
            blueSpaceAmountSix = "00" + blueSpaceAmountSix[2:]
        elif len(blueSpaceAmountSix) == 3:
            blueSpaceAmountSix = "000" + blueSpaceAmountSix[2:]
    except:
        blueSpaceAmountSix = "DUMMY"

    try:
        redSpaceAmountBaseSix = redSpaceAmountSix.get()
        redSpaceAmountSix = hex(int(redSpaceAmountSix.get()))
        if len(redSpaceAmountSix) == 4:
            redSpaceAmountSix = "FF" + redSpaceAmountSix[2:]
        elif len(redSpaceAmountSix) == 3:
            redSpaceAmountSix = "FFF" + redSpaceAmountSix[2:]
    except:
        redSpaceAmountSix = "DUMMY"

    marioPartySixBlueSpace = getBlueSpaceCodeSix(blueSpaceAmountSix)
    marioPartySixRedSpace = getRedSpaceCodeSix(redSpaceAmountSix)

    if redSpaceAmountSix == "DUMMY":
        marioPartySixRedSpace = ""
    if blueSpaceAmountSix == "DUMMY":
        marioPartySixBlueSpace = ""

    generatedCode = marioPartySixRedSpace + marioPartySixBlueSpace
    generatedCode = generatedCode.replace("SIXRED", redSpaceAmountBaseSix)
    generatedCode = generatedCode.replace("SIXBLUE", blueSpaceAmountBaseSix)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucesssful", "success", "Generated codes copied to clipboard!")

def parseCoinsFive():
    global blueSpaceAmountFive, redSpaceAmountFive

    if not blueSpaceAmountFive.get() and not redSpaceAmountFive.get():
        createDialog("Error", "error", "No information provided.")
        return

    try:
        blueSpaceAmountBaseFive = blueSpaceAmountFive.get()
        blueSpaceAmountFive = hex(int(blueSpaceAmountFive.get()))
        if len(blueSpaceAmountFive) == 4:
            blueSpaceAmountFive = "00" + blueSpaceAmountFive[2:]
        elif len(blueSpaceAmountFive) == 3:
            blueSpaceAmountFive = "000" + blueSpaceAmountFive[2:]
    except:
        blueSpaceAmountFive = "DUMMY"

    try:
        redSpaceAmountBaseFive = redSpaceAmountFive.get()
        redSpaceAmountFive = hex(int(redSpaceAmountFive.get()))
        if len(redSpaceAmountFive) == 4:
            redSpaceAmountFive = "FF" + redSpaceAmountFive[2:]
        elif len(redSpaceAmountFive) == 3:
            redSpaceAmountFive = "FFF" + redSpaceAmountFive[2:]
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

    try:
        blueSpaceAmountBaseFour = blueSpaceAmountFour.get()
        blueSpaceAmountFour = hex(int(blueSpaceAmountFour.get()))
        if len(blueSpaceAmountFour) == 4:
            blueSpaceAmountFour = "00" + blueSpaceAmountFour[2:]
        elif len(blueSpaceAmountFour) == 3:
            blueSpaceAmountFour = "000" + blueSpaceAmountFour[2:]
    except:
        blueSpaceAmountFour = "DUMMY"

    try:
        redSpaceAmountBaseFour = redSpaceAmountFour.get()
        redSpaceAmountFour = hex(int(redSpaceAmountFour.get()))
        if len(redSpaceAmountFour) == 4:
            redSpaceAmountFour = "FF" + redSpaceAmountFour[2:]
        elif len(redSpaceAmountFour) == 3:
            redSpaceAmountFour = "FFF" + redSpaceAmountFour[2:]
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

def createDialog(windowTitle, warn, info):
    completeWindow = ctk.CTkToplevel()
    completeWindow.geometry("500x125")
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
preBlueLabelEight = ctk.CTkLabel(master=frameEight, text=":     ", font=("Arial", 12))
preBlueLabelEight.grid(row=1, column=2)

preRedLabelEight = ctk.CTkLabel(master=frameEight, text=":   - ", font=("Arial", 12))
preRedLabelEight.grid(row=2, column=2)

coinsBlueLabelEight = ctk.CTkLabel(master=frameEight, text=" Coins", font=("Arial", 12))
coinsBlueLabelEight.grid(row=1, column=4)

coinsRedLabelEight = ctk.CTkLabel(master=frameEight, text=" Coins", font=("Arial", 12))
coinsRedLabelEight.grid(row=2, column=4)

parseButtonEight = ctk.CTkButton(master=tabviewEight.tab("Space Modifier"), command=parseCoinsEight, text="Generate Codes")
parseButtonEight.pack(padx=20, pady=20)

preBlueLabelEightGC = ctk.CTkLabel(master=frameEightGC, text=":    ", font=("Arial", 12))
preBlueLabelEightGC.grid(row=1, column=2)

preRedLabelEightGC = ctk.CTkLabel(master=frameEightGC, text=":   - ", font=("Arial", 12))
preRedLabelEightGC.grid(row=2, column=2)

coinsBlueLabelEightGC = ctk.CTkLabel(master=frameEightGC, text=" Coins", font=("Arial", 12))
coinsBlueLabelEightGC.grid(row=1, column=4)

coinsRedLabelEightGC = ctk.CTkLabel(master=frameEightGC, text=" Coins", font=("Arial", 12))
coinsRedLabelEightGC.grid(row=2, column=4)

parseButtonEightGC = ctk.CTkButton(master=tabviewEight.tab("Space Modifier (GC Mod)"), command=parseCoinsEightGC, text="Generate Codes")
parseButtonEightGC.pack(padx=20, pady=20)

preBlueLabelSeven = ctk.CTkLabel(master=frameSeven, text=":     ", font=("Arial", 12))
preBlueLabelSeven.grid(row=1, column=2)

preRedLabelSeven = ctk.CTkLabel(master=frameSeven, text=":   - ", font=("Arial", 12))
preRedLabelSeven.grid(row=2, column=2)

coinsBlueLabelSeven = ctk.CTkLabel(master=frameSeven, text=" Coins", font=("Arial", 12))
coinsBlueLabelSeven.grid(row=1, column=4)

coinsRedLabelSeven = ctk.CTkLabel(master=frameSeven, text=" Coins", font=("Arial", 12))
coinsRedLabelSeven.grid(row=2, column=4)

parseButtonSeven = ctk.CTkButton(master=tabviewSeven.tab("Space Modifier"), command=parseCoinsSeven, text="Generate Codes")
parseButtonSeven.pack(padx=20, pady=20)

preBlueLabelSix = ctk.CTkLabel(master=frameSix, text=":     ", font=("Arial", 12))
preBlueLabelSix.grid(row=1, column=2)

preRedLabelSix = ctk.CTkLabel(master=frameSix, text=":   - ", font=("Arial", 12))
preRedLabelSix.grid(row=2, column=2)

coinsBlueLabelSix = ctk.CTkLabel(master=frameSix, text=" Coins", font=("Arial", 12))
coinsBlueLabelSix.grid(row=1, column=4)

coinsRedLabelSix = ctk.CTkLabel(master=frameSix, text=" Coins", font=("Arial", 12))
coinsRedLabelSix.grid(row=2, column=4)

parseButtonSix = ctk.CTkButton(master=tabviewSix.tab("Space Modifier"), command=parseCoinsSix, text="Generate Codes")
parseButtonSix.pack(padx=20, pady=20)

preBlueLabelFive = ctk.CTkLabel(master=frameFive, text=":     ", font=("Arial", 12))
preBlueLabelFive.grid(row=1, column=2)

preRedLabelFive = ctk.CTkLabel(master=frameFive, text=":   - ", font=("Arial", 12))
preRedLabelFive.grid(row=2, column=2)

coinsBlueLabelFive = ctk.CTkLabel(master=frameFive, text=" Coins", font=("Arial", 12))
coinsBlueLabelFive.grid(row=1, column=4)

coinsRedLabelFive = ctk.CTkLabel(master=frameFive, text=" Coins", font=("Arial", 12))
coinsRedLabelFive.grid(row=2, column=4)

parseButtonFive = ctk.CTkButton(master=tabviewFive.tab("Space Modifier"), command=parseCoinsFive, text="Generate Codes")
parseButtonFive.pack(padx=20, pady=20)

preBlueLabelFour = ctk.CTkLabel(master=frameFour, text=":     ", font=("Arial", 12))
preBlueLabelFour.grid(row=1, column=2)

preRedLabelFour = ctk.CTkLabel(master=frameFour, text=":   - ", font=("Arial", 12))
preRedLabelFour.grid(row=2, column=2)

coinsBlueLabelFour = ctk.CTkLabel(master=frameFour, text=" Coins", font=("Arial", 12))
coinsBlueLabelFour.grid(row=1, column=4)

coinsRedLabelFour = ctk.CTkLabel(master=frameFour, text=" Coins", font=("Arial", 12))
coinsRedLabelFour.grid(row=2, column=4)

parseButtonFour = ctk.CTkButton(master=tabviewFour.tab("Space Modifier"), command=parseCoinsFour, text="Generate Codes")
parseButtonFour.pack(padx=20, pady=20)

# Run the main application loop
app.mainloop()