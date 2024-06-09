# Import necessary libraries
from pydoc import cli
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import autoit
from pynput.keyboard import Controller, Key

# Function to simulate a mouse click at given coordinates using AutoIt
def autoit_click(x, y):
    autoit.mouse_click('left', x, y, 1)

# Function to simulate a mouse click at given coordinates using win32con
def click(x, y):
	win32api.SetCursorPos((x, y))
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(random.uniform(0.001, 0.005))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Function to check for air bubbles on the screen
def check_air_bubbles_on_screen():
	s = pyautogui.screenshot()
	for x in range(770, 1160):
		for y in range(350, 730):
			colorcode = (68, 252, 234)  # Blue bubbles
			tempvar = False
			for x2 in range(5):
				if s.getpixel((x + x2, y)) == colorcode:
					tempvar = True
				else:
					tempvar = False
					break
			if tempvar is True:
				return True
			
def fish_click():
	for _ in range(8):
		time.sleep(0.47)
		click(960, 960)

def autoit_click(x, y):
    autoit.mouse_click('left', x, y, 1)

def sell_fish():
    time.sleep(8)
    keyboard.press('o')
    time.sleep(0.4)
    keyboard.release('o')
    autoit_click(1263,1111)
    time.sleep(2)
    autoit_click(1094,379)
    time.sleep(0.5)
    autoit_click(1094,379)
    time.sleep(1)
    autoit_click(1244,468)
    time.sleep(1)
    autoit_click(1244,468)
    time.sleep(0.9)
    autoit_click(1244,468)
    time.sleep(0.9)
    autoit_click(1244,468)
    time.sleep(1)
    autoit_click(1482,395)
    time.sleep(0.5)
    keyboard.press('i')
    time.sleep(0.4)
    keyboard.release('i')

fish_collected = 0
last_bubble_time = time.time()  # Initialize the last bubble time
while keyboard.is_pressed('q') == False:
	if check_air_bubbles_on_screen() == True:
		click(960, 540)
		fish_click()
		last_bubble_time = time.time()  # Update the last bubble time
		fish_collected = fish_collected + 1
		print("You've collected:", fish_collected, "fishes!")
	elif time.time() - last_bubble_time > 20:  # If no bubbles for 20 seconds
		sell_fish()
		click(960, 540)  # Throw the bait back into the water
		last_bubble_time = time.time()  # Update the last bubble time
		fish_collected = fish_collected - 1
		print("You've collected:", fish_collected, "fishes!")
print("In total you've collected:", fish_collected, "fishes!")
