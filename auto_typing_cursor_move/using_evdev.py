from evdev import UInput, ecodes, AbsInfo
import random
import time

# Define screen resolution (replace with your actual screen width/height)
screen_width = 1920  # Replace with your screen width
screen_height = 1080  # Replace with your screen height

# Define input device capabilities for both mouse and keyboard
capabilities = {
    ecodes.EV_ABS: {
        ecodes.ABS_X: AbsInfo(0, 0, screen_width, 0, 0, 0),  # Screen width
        ecodes.ABS_Y: AbsInfo(0, 0, screen_height, 0, 0, 0),  # Screen height
    },
    ecodes.EV_KEY: list(range(ecodes.KEY_A, ecodes.KEY_Z + 1)) + [ecodes.BTN_LEFT],  # Alphabet keys and left mouse button
}

# Create a virtual input device (UInput)
ui = UInput(capabilities)

def move_mouse_randomly():
    """Moves the mouse to a random position on the screen."""
    random_x = random.randint(0, screen_width)
    random_y = random.randint(0, screen_height)
    
    ui.write(ecodes.EV_ABS, ecodes.ABS_X, random_x)
    ui.write(ecodes.EV_ABS, ecodes.ABS_Y, random_y)
    ui.syn()  # Sync the events
    print(f"Moved mouse to ({random_x}, {random_y})")

def type_random_letter():
    """Types a random letter from a to z."""
    letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    key_code = getattr(ecodes, f"KEY_{letter.upper()}")
    
    # Simulate key press and release
    ui.write(ecodes.EV_KEY, key_code, 1)  # Key press
    ui.write(ecodes.EV_KEY, key_code, 0)  # Key release
    ui.syn()  # Sync the events
    print(f"Typed '{letter}'")


while True:
    time.sleep(5)
    move_mouse_randomly() 
    
    time.sleep(1)
    type_random_letter() 

