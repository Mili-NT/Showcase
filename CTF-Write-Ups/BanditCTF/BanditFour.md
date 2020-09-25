# Level: BanditFour
## Level Credentials: bandit4:pIwrPrtPN36QITSp3EQaw936yaFoFgAB
## Level Description: *The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.*

### Steps:
As always, `ls` to see the directories  
`cd inhere` to change to the inhere directory and `ls` to see the files.  
There are ten files named *-file00* to *-file09*  
Using `cat ./-file00` returns a string of unreadable characters.  
### Solution:
While going through each file and using `cat ./-file0X`on it would work, it's not efficient.  
I used `find -type f | xargs file | grep text` to find the only file with ASCII text. This shows *./-file07* has ASCII text.  
Then, I use `cat ./-file07` to find the flag.  
 
**Command breakdown:**  
I found the command [here](https://stackoverflow.com/questions/14505218/finding-human-readable-files-on-unix)   
The `find` command finds files. `type -f` specifies to only find regular files. `|` pipes the output to `xargs` which converts the input into arguments for a command. `file` returns only the files, and `| grep text` looks through those files for readable text.

**Flag: koReBOKuIDDepwhWk7jZC0RTdopnAYKh**

