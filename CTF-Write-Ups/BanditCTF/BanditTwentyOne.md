# Level: BanditTwentyOne
## Level Credentials: bandit21:gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
## Level Descripton: *A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.*

### Steps:
`cd /etc/cron.d && ls` shows that there are three cron jobs running: *cronjob_bandit22*, *cronjob_bandit23*, and *cronjob_bandit24*.    
`cat cronjob_bandit22` returns:    
> @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
> * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

### Solution:
Well, let's check that bash script out: `cd /usr/bin/ && cat cronjob_bandit22.sh`:
> chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
> cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

While that may LOOK like the flag, that's just the file which the real flag is being written into.  
`cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv` gives us the real flag.  


**Flag: Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI**
