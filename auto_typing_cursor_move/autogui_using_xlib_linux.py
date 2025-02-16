from Xlib import X, display
from Xlib.ext import xtest
import time

# Function to move cursor to (x, y) position
def move_cursor(x, y):
    d = display.Display()
    root = d.screen().root
    root.warp_pointer(x, y)
    d.sync()

# Function to simulate key press and release
def type_text(text, delay=0.1):
    d = display.Display()
    for char in text:
        keysym = ord(char)  # Convert character to key symbol
        xtest.fake_input(d, X.KeyPress, keysym)
        xtest.fake_input(d, X.KeyRelease, keysym)
        d.sync()
        time.sleep(delay)

# Example Usage
if __name__ == "__main__":
    time.sleep(2)  # Wait 2 seconds before executing

    # Move the cursor to a specific position
    move_cursor(500, 500)
    time.sleep(1)

    # Auto type "Hello, Linux!"
    type_text("Hello, Linux!", delay=0.2)
