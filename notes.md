Jacob:

- Removed exercise-page clicks to stop putting the browser page in focus after every action (Alex finished)

- Kept the KeyboardEvent -> string parsing for the keyboard-input function, hotkeys are still lost. Added an enter key press and release after each keyboard-input perform_action call to act as a user pressing enter

- Did not address blocking c, m, and k keys when user presses them when prompted, deleting the key (if needed) works just fine

- The lab runs through steps until a goal is reached. Once a goal is reached, a popup appears to allow the user to either continue on with the lab or close the popup. Due to the popup being a new html div, the test crashes if you try to make a call/do more steps in the lab. To address this, there are no more calls after the goal is complete (a fragile solution), only 4 prompt_users/perform_actions are made to run through the lab. Extra time is added after the lab is finished (45 seconds) to allow the final fping command to run, allow the user to close the goal popup, and allow the user to exit the lab.

- For the expo demo, the process is:
    - login
    - click start button
    - wait for vm to spin up
    - click terminal icon (5 second wait)
    - click terminal window (5 second wait)
    - enter 'nmap -n -sn 192.168.177.0/24' (15 second wait)
    - enter 'fping -g -s 192.168.177.0/24' (15 second wait) (popup appears here after the command finishes) 
    - stop script and say to close/continue on the popup and let the user exit the lab (45 second wait)

- The first goal of the lab is to identify live machines on the network (the process explained above). The nmap command sends packets to all 255 ip addresses in the 192.168.177.0/24 network. The -n option tells nmap to not do DNS resolution and the -sn option tells nmap to do a ping scan rather than a port scan; this command finds 4 live machines on the network (including the vm you're running). The fping command is similar to a ping, but it runs more efficiently when used against multiple hosts. The -g option tells fping to generate ip addresses to scan and the -s option tells fping to print the cumulative statistics it found during the run at exit. At the top of the finished fping command, you should see the live hosts.