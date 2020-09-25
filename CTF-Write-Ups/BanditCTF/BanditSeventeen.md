# Level: BanditSeventeen
## Level Credentials: bandit17:SSH Key
## Level Description: *There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new. NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19*

### Steps:
Setup the SSH key with puttygen and logged in.  
`ls` shows passwords.new and passwords.old  
### Solution: 
So we have two files that we have to compare, so let's try `diff passwords.new passwords.old`  
> '42c42'  
> '< kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd'  
> '---'  
> '> hlbSBPAWJmL6WFDb06gpTx1pPButblOA'

So the top string has been changed between .old and .new so thats our flag.


**Flag: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd**
