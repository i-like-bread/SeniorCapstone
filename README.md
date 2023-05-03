# Senior Capstone Project 
- For the expo demo, the process is:
    - Login
    - Click start button
    - Wait for vm to spin up
    - Click terminal icon (5 second wait)
    - Click terminal window (5 second wait)
    - Enter 'nmap -n -sn 192.168.177.0/24' (15 second wait)
    - Enter 'fping -g -s 192.168.177.0/24' (15 second wait) (popup appears here after the command finishes) 
    - Stop script and say to close/continue on the popup and let the user exit the lab (45 second wait)

- The first goal of the lab is to identify live machines on the network (the process explained above)
    - The nmap command sends packets to all 255 ip addresses in the 192.168.177.0/24 network. 
        - The -n option tells nmap to not do DNS resolution and the -sn option tells nmap to do a ping scan rather than a port scan; this command finds 4 live machines on the network (including the vm you're running). 
    - The fping command is similar to a ping, but it runs more efficiently when used against multiple hosts. 
        - The -g option tells fping to generate ip addresses to scan and the -s option tells fping to print the cumulative statistics it found during the run at exit. At the top of the finished fping command, you should see the live hosts.