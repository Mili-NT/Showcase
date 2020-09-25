# Level: BanditNineteen
## Level Credentials: bandit19:IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
## Level Description: *To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.*

### Steps:
`ls` shows there is an executable called *bandit20-do*.  
Running it with `./bandit20-do` returns:
> Run a command as another user.
>   Example: ./bandit20-do id

### Solution:
The executable is owned by bandit20, and runs as if bandit20 was running it.  
The flag is located at /etc/bandit_pass/bandit20, so `./bandit20-do cat /etc/bandit_pass/bandit20` returns the flag.


**Flag: GbKksEFF4yrVs6il55v6gwY5aVje5f0j**
