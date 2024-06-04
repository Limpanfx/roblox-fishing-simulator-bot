# Import necessary libraries
from pydoc import cli
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pydirectinput

# ... (rest of your code)

# Main loop to check for fish and bubbles until 'q' is pressed
while keyboard.is_pressed('q') == False:
    # Check if fish is found
    if pyautogui.pixel(847, 820)[0] == 255 or pyautogui.pixel(860, 800)[0] == 255:
        # Reel in the fish
        click_random_throw()
        counter = get_counter()
        fish_found = True
    # Increase fish counter if found
    if fish_found == True:
        if pyautogui.pixel(830, 800) != (83, 250, 83):
            # Pause for 3 seconds
            time.sleep(3)
            # Click another 7 times
            for _ in range(7):
                click_random_throw()
                time.sleep(random.uniform(0.02, 0.025))
            fish_counter += 1
            print('Fish caught: ' + str(fish_counter))
            fish_found = False
            double_click_random_throw()
    # If fish not found, check for air bubbles
    if fish_found == False:
        if check_air_bubbles_on_screen() == True:
            # Reel in the fish
            click_random_throw()
            counter = get_counter()
            fish_found = True
    if counter == 0:
        # Cast or reel in the fishing rod
        double_click_random_throw()
        counter = get_counter()
    # If inventory is full, sell
    if fish_counter == 2000:
        print('Inventory full, selling...')
        exit()
    counter -= 1
    time.sleep(0.025)
