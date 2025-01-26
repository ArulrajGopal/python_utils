import os
import random

def move_mouse(x, y):
    os.system(f"xdotool mousemove {x} {y}")

screen_width, screen_height = 1920, 1080  # Replace with your screen resolution
random_x = random.randint(0, screen_width)
random_y = random.randint(0, screen_height)
move_mouse(random_x, random_y)
