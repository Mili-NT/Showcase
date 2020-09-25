# Level: Bandit20
## Level Credentials: bandit20:GbKksEFF4yrVs6il55v6gwY5aVje5f0j
## Level Description: *There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21). NOTE: Try connecting to your own network daemon to see if it works as you think*

### Steps:
`ls` reveals an executable called *suconnect* that runs with elevated privileges.    
We need a client and a server for this, so we'll need two terminal windows. The helpful reading section mentions tmux.    
`tmux` starts the service `ctrl+b %` opens another window.    
`cat /etc/bandit_pass/bandit20 | nc -l 4200` starts a listener on port 4200.    
In the other window, I run the *suconnect* with the arg 4200:  
> Could Not Connect

I forgot to set an arg, and decided that using & is cleaner than tmux.  
### Solution:
`nc -l -p 4200 < /etc/bandit_pass/bandit20 &` and `./suconnect 4200` returns our flag.  


**Flag: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr**
