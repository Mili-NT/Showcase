# Level: LeviathanZero
## Level Credentials: leviathan0:leviathan0
## Level Description: none

### Steps:
Using `ls` to check the */home/leviathan0* directory shows its empty.    
... or is it? Using `ls -la` shows a variety of hidden files. Most are standard, *.bashrc*, *.bash_logout*, and *profile*    
One however, sticks out: a directory called *.backup*, which contains a single file called *backup.html*    
Using `cat b*` to check it out shows a looooooong list of URLs in HREF tags. It's a... netscape bookmark file?   
First I try using `cat b* | grep flag` but no dice.  
### Solution:
However, `cat b* | grep password` reveals the flag.  


**Flag: rioGegei8m**
