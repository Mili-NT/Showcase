# Level: BanditThirtyTwo
## Level Credentials: bandit32:56a9bf19c63d650ce78e6ec0354ee45e
## Level Description: *After all this git stuff its time for another escape. Good luck!*

### Steps:
After logging in, we're greeted with a prompt that says "WELCOME TO THE UPPERCASE SHELL"  
I'm going to try and get to vi, and use the same shell escape techniques from there.  
It appears that everything entered is processed as uppercase, which makes commands impossible.   
### Solution:
We can use the positional parameter `$0` to reset the shell, then just use `cat /etc/bandit_pass/bandit33`  


**Flag: c9c3199ddf4121b10cf581a98d51caee**
