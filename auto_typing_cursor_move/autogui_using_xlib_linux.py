from Xlib import X, display, XK, ext
import time
import random

def move_to(x,y):
    d = display.Display() 
    root = d.screen().root
    root.warp_pointer(x,y)
    d.sync()

def write(letter):
    d = display.Display()
    keycode = d.keysym_to_keycode(XK.string_to_keysym(letter))
    ext.xtest.fake_input(d, X.KeyPress, keycode)
    ext.xtest.fake_input(d, X.KeyRelease, keycode)
    d.sync() 


def perform_action():
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    
    d = display.Display()
    screen = d.screen()
    screen_width = screen.width_in_pixels
    screen_height = screen.height_in_pixels
    
    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_height)
    
    move_to(random_x,random_y)
    write(letter)
    
    print(f"Typed '{letter}' and moved the cursor to ({random_x},{random_y})")
    
while True:
    time.sleep(10)
    perform_action()

