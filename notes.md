Notes:

- Created new Introduction to Metasploit Metasploit_golden.py with SeleniumIDE
- Copied make_enhanced.py to make new Metasploit_make_enhanced

- Metasploit ran through ok, same freezing bug as original when passing keys
- Commented out all "exercise-page" clicks
- Keys passed ok, enter not passed (probably due to KeyboardEvent -> string)

- Comparing original and new tests, "exercise-page" clicks puts the browser page back in focus. The keys are passed to the canvas element on the browser and not within the canvas itself. Thus the keys are lost.

- Working on blocking c, m, and k keys passing into terminal/recording when prompt_user is called (not a necessity)