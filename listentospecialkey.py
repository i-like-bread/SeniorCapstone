

from pynput import keyboard

def on_press(key):
    try:
        # Convert the key to a string
        key_str = str(key.char)
        # Check if the key is between 1 and 2
        if '1' <= key_str <= '2':
            # Print the key
            print(key_str)
            # Stop listening to key events
            return False
    except AttributeError:
        # Ignore special keys like 'ctrl', 'shift', etc.
        pass

# Create a keyboard listener
listener = keyboard.Listener(on_press=on_press)
# Start the listener
listener.start()
# Wait for the listener to stop (when a key between 1 and 2 is pressed)
listener.join()