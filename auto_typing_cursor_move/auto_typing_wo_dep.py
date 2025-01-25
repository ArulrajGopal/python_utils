import time

# Define helper functions for HID reports
def send_keyboard_report(hid_file, modifier, keycode):
    """
    Sends a keyboard HID report.
    :param hid_file: Path to the HID device file.
    :param modifier: Modifier keys (e.g., 0x02 for Left Shift, 0x00 for none).
    :param keycode: Keycode to send (e.g., 0x04 for 'a').
    """
    # HID keyboard report: [modifier, reserved, key1, key2, key3, key4, key5, key6]
    report = bytearray(8)
    report[0] = modifier  # Modifier keys (e.g., Left Shift, Ctrl)
    report[2] = keycode   # Main key (HID keycode)
    with open(hid_file, 'wb') as f:
        f.write(report)
        f.flush()

    # Release the key
    report[0] = 0x00  # No modifiers
    report[2] = 0x00  # No key
    with open(hid_file, 'wb') as f:
        f.write(report)
        f.flush()

def send_mouse_report(hid_file, x, y, buttons=0):
    """
    Sends a mouse HID report.
    :param hid_file: Path to the HID device file.
    :param x: Relative movement on the X-axis.
    :param y: Relative movement on the Y-axis.
    :param buttons: Mouse button state (e.g., 0 for none, 1 for left-click).
    """
    # HID mouse report: [buttons, x movement, y movement]
    report = bytearray(3)
    report[0] = buttons  # Buttons (e.g., 1 for left click)
    report[1] = x        # X movement
    report[2] = y        # Y movement
    with open(hid_file, 'wb') as f:
        f.write(report)
        f.flush()

# Paths to HID gadget device files
keyboard_hid = '/dev/hidg0'  # Keyboard HID gadget
mouse_hid = '/dev/hidg1'     # Mouse HID gadget

# Example: Type "Hello" and move the mouse diagonally
try:
    # Type "Hello" (HID keycodes for Windows)
    # 'H': 0x0B, 'e': 0x08, 'l': 0x0F, 'o': 0x12
    keymap = {'H': 0x0B, 'e': 0x08, 'l': 0x0F, 'o': 0x12}
    for char in "Hello":
        keycode = keymap[char]
        send_keyboard_report(keyboard_hid, 0x02 if char.isupper() else 0x00, keycode)  # Use Left Shift for uppercase
        time.sleep(0.2)  # Delay between keystrokes

    # Move mouse diagonally (e.g., 50px right and 50px down)
    for _ in range(50):
        send_mouse_report(mouse_hid, 1, 1)  # Move diagonally
        time.sleep(0.01)

    # Perform a left mouse click
    send_mouse_report(mouse_hid, 0, 0, buttons=1)  # Press left button
    time.sleep(0.1)
    send_mouse_report(mouse_hid, 0, 0, buttons=0)  # Release left button

except PermissionError:
    print("Run the program as root to access HID gadget files.")
except FileNotFoundError:
    print("Ensure the HID gadget is set up and the correct /dev/hidg* files exist.")
