# tips all the money from one account to another in tip.cc

# imports
import pyautogui 
import time 

# receiver
person = "@person#4567"

# idle time before starting
time.sleep(5)

# tips all coins in tip.txt
with open("tip.txt") as currencies:
    # the first time is buggy, warms up the autocorrect
    pyautogui.typewrite("$tip " + person + " all lol \n")
    for line in currencies:
        if line.split(":")[0] == "Random Number Generator":
            pyautogui.typewrite("$tip " + person + " all rng \n")
        elif line.split(":")[0] == "1Million Token":
            pyautogui.typewrite("$tip " + person + " all 1mt \n")
        elif line.split(":")[0] == "Trade Butler Bot":
            pyautogui.typewrite("$tip " + person + " all tbb \n")
        elif line.split(":")[0] == "BITToken (BSC)":
            pyautogui.typewrite("$tip " + person + " all bBITT \n")
        elif line.split(":")[0] == "DexKit (BSC)":
            pyautogui.typewrite("$tip " + person + " all bkit \n")
        elif line.split(":")[0] == "Zero":
            pyautogui.typewrite("$tip " + person + " all zer \n")
        elif line.split(":")[0] == "Invictus Hyperion Fund":
            pyautogui.typewrite("$tip " + person + " all ihf \n")
        elif line.split(":")[0] == "BITToken":
            pyautogui.typewrite("$tip " + person + " all bitt \n")
        elif line.split(":")[0] == "USD Coin":
            pyautogui.typewrite("$tip " + person + " all USDC \n")
        elif line.split(":")[0] == "Name Change Token":
            pyautogui.typewrite("$tip " + person + " all NCT \n")
        elif line.split(":")[0] == "Metal (Proton)":
            pyautogui.typewrite("$tip " + person + " all xmt \n")
        elif line.split(":")[0] == "Invictus Capital Token":
            pyautogui.typewrite("$tip " + person + " all icap \n")
        elif line.split(":")[0] == "Trade Butler Bot (BSC)":
            pyautogui.typewrite("$tip " + person + " all btbb \n")
        else:
            pyautogui.typewrite("$tip " + person + " all " + line.split(":")[0] + " \n")
        time.sleep(0.5)

