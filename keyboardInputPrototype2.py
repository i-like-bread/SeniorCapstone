import keyboard

def keyboardInput():
    recorded_keys = []

    # Create a function to be called every time a key is pressed
    def on_key_press(event):
        key_name = event.name
        recorded_keys.append(key_name)
        print(recorded_keys)

        # Stop the script when the "esc" key is pressed
        if key_name == 'esc':
            keyboard.unhook_all()
            print("Script terminated.")
            print("Recorded keys:", recorded_keys)
            return recorded_keys

    # Bind the function to the keyboard events
    keyboard.on_press(on_key_press)

    # Block the main thread so the script can continue to listen to the keyboard events
    keyboard.wait()

    # Return the recorded keys
    return recorded_keys

# Call the keyboardInput() function and print the recorded keys
recorded_keys = keyboardInput()
print('dafq')
print("Recorded keys:", recorded_keys)