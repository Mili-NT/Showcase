# Level: BanditTwentySix
## Level Credentials: bandit27:5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
## Level Description: *Good job getting a shell! Now hurry and grab the password for bandit27!*

### Steps:
Starting off where level 25 left off, we need to use some of the shell escape techniques I learned but didnt use because im retarded.
Use `:set shell=/bin/bash` to set the shell to bash, then `:shell` to launch it.  
Now, we've got a shell. 
Using `ls` shows there are two files: an executable named *bandit27-do* and *text.txt*.  
*text.txt* is just the ascii banner for the bandit26 logon. 
*bandit27-do* is a lot more interesting. Running it with `./b*` (`./bandit27-do` for the non-lazy) shows it executes commands as bandit27.  
I think we all know what this means.

### Solution:
`./bandit27-do cat /etc/bandit_pass/bandit27`


**Flag: 3ba3118a22e93127a4ed485be72ef5ea**
