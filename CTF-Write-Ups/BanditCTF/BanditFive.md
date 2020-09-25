# Level: BanditFive
## Level Credentials: bandit5:koReBOKuIDDepwhWk7jZC0RTdopnAYKh
## Level Description: *The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties: human readable, 1033 bytes in size, not executable*

### Steps:
`ls` to list the directories  
`cd inhere && ls` to change to the *inhere* directory and list is contents  
There are 20 subdirectories named *maybehere00* to *maybehere19*  
`cd maybehere00 && ls` shows that each subdirectory has a few different files.    
### Solution:
I used `find -type f -size 1033c` to find only files and find the one that was 1033 bytes.      
This returns only one file: *./maybehere07/.file2*      
Using `cat ./maybehere07/.file2` returns the flag  


**Flag: DXjZPULLxYr17uwoI01bNLQbtFemEgo7**

