Notes:

- Created new Introduction to Metasploit Metasploit_golden.py with SeleniumIDE
- Copied make_enhanced.py to make new Metasploit_make_enhanced

- Metasploit ran through ok, same keyboard bug as original when passing keys (keys not passing)
- Commented out all "exercise-page" clicks
- Keys passed ok, enter not passed (probably due to KeyboardEvent -> string)

- Comparing original and new tests, "exercise-page" clicks puts the browser page back in focus. The keys are passed to the canvas element on the browser and not within the canvas itself. Thus the keys are lost.

- Working on blocking c, m, and k keys passing into terminal/recording when prompt_user is called (not a necessity)
- Key is passed after the print of options in prompt_user, trying to find a way to block the key being passed into the terminal but is also read for the if statement