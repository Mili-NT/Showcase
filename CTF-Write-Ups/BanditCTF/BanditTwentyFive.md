# Level: BanditTwentyFive
## Level Credentials: bandit25:uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
## Level Description: *Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.*

### Steps:
Using `ls` right off the bat reveals a file called *bandit26.sshkey*. Using `cat bandit26.sshkey` shows that its a normal SSH key.  
Attempting to connect shows a brief post-auth message, before shutting down.  
So, we can view the /etc/passwd file, and see what shell bandit26 IS using: `grep bandit26 /etc/passwd`  
> bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext

Attempting to use `chsh --shell /bin/bash bandit26` reveals that we arent allowed to change the shell for bandit26.  
I cant lie, I had to look this one up.  
### Solution:
Minimize the terminal to force the post-auth banner to use `more`, then open vim using `vim`.  
Read the bandit26 password by entering `:e /etc/bandit_pass/bandit26`  


**Flag: 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z**
