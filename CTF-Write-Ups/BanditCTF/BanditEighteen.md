# Level: Bandit18
## Level Credentials: bandit18:kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
## Level Description: *The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH*

### Steps:
So, right off the bat, connecting using the level credentials will immediately close the connection.  
### Solution:
Using putty, I loaded up the default bandit connection, added `cat readme && read` as remote commands.  
`cat readme` shows us the flag, and `read` prevents the session from immediately closing.  


**Flag: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x**
