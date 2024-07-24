# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 7/24/2024
# License: MIT
# ============================================

from codes.marioParty1 import *
from functions import *

import pyperclip


def itemsEvent_mp1(plus, minus, speed, slow, warp):
    if not all([plus.get(), minus.get(), speed.get(), slow.get(), warp.get()]):
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return

    try:
        plusWeight = float(plus.get())
        minusWeight = plusWeight + float(minus.get())
        speedWeight = minusWeight + float(speed.get())
        slowWeight = speedWeight + float(slow.get())
        warpWeight = slowWeight + float(warp.get())
    except ValueError:
        createDialog("Error", "error", "Please enter valid integers.", None)
        return

    weights = [plusWeight, minusWeight, speedWeight, slowWeight, warpWeight]
    weights = [min(weight * 2.56 / 10, 256) for weight in weights]  # Apply hard cap at 256

    # Sort weights and adjust duplicates to the smallest possible unique values
    sorted_weights = sorted(weights)
    for i in range(1, len(sorted_weights)):
        if sorted_weights[i] <= sorted_weights[i - 1]:
            sorted_weights[i] = sorted_weights[i - 1] + 0.01
            if sorted_weights[i] > 256:
                createDialog("Error", "error", "Adjusted weight value exceeds 256. Adjust inputs.", None)
                return

    # Map sorted weights back to their original positions
    weights_map = {original: adjusted for original, adjusted in zip(weights, sorted_weights)}
    adjusted_weights = [weights_map[weight] for weight in weights]

    hex_weights = []
    for weight in adjusted_weights:
        hex_weight = hex(int(weight))[2:].zfill(2)
        hex_weights.append(hex_weight.upper())  # Ensure uppercase for consistency

    code = getBlockWeights(*hex_weights).strip()
    pyperclip.copy(code)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)
