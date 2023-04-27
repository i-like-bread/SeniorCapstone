###
# Utility functions for make_enhanced.py
###

# Create the explicit wait command as a list of strings
def make_wait_command(time, element_id):
    wait_command = [  # the multi-line wait command
        "try:", 
        "    wait = WebDriverWait(self.driver, {TIME})",
        "    wait.until(expected_conditions.element_to_be_clickable(({ELEMENT_ID})))",
        "except:",
        "    print('{ELEMENT_ID} did not become clickable')",
        "    self.driver.quit()"
    ]

    # Replace placeholders {TIME} and {ELEMENT_ID} with provided values
    # Time is second element of wait_command
    wait_command[1] = wait_command[1].format(TIME = time)
    # ELEMENT_ID is in lines 3 and 5
    wait_command[2] = wait_command[2].format(ELEMENT_ID = element_id)
    wait_command[4] = wait_command[4].format(ELEMENT_ID = element_id)

    return wait_command
