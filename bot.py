# Import necessary libraries
from pydoc import cli
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pydirectinput

# Function to simulate a mouse click at given coordinates
def click(x, y):
	win32api.SetCursorPos((x, y))
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	time.sleep(1)

# Function to check for air bubbles on the screen
def check_air_bubbles_on_screen():
	s = pyautogui.screenshot()
	for x in range(770, 1160):
		for y in range(350, 730):
			colorcode = (68, 252, 234)  # Blue bubbles / Blaue Blasen
			tempvar = False
			for x2 in range(5):
				if s.getpixel((x + x2, y)) == colorcode:
					tempvar = True
				else:
					tempvar = False
					break
			if tempvar is True:
				return True

# Main loop to check for bubbles until 'q' is pressed
while keyboard.is_pressed('q') == False:
	# If bubbles are found, click
	if check_air_bubbles_on_screen() == True:
		click()
	time.sleep(0.025)
