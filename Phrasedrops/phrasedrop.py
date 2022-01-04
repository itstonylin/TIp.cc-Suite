# does phrasedrop for tip.cc

# imports
import pyautogui
import time

# gets phrase
phrase = input("Enter phrase: \n")

# buffer time to move to Discord
time.sleep(4)

# types phrase
pyautogui.typewrite(phrase + "\n")
