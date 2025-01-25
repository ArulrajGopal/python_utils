import pyautogui
import time
import random

def perform_action():
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    
    screen_width, screen_height = pyautogui.size()
    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_height)
    
    pyautogui.moveTo(random_x, random_y)
    
    pyautogui.write(letter)
    
    print(f"Typed '{letter}' and moved the cursor")
    
while True:
    time.sleep(10)
    perform_action()