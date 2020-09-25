# Level: BanditEight
## Level Credentials: bandit8:cvX2JJa4CFALtqS87jk27qwqGhBM9plV
## Level Description: *The password for the next level is stored in the file data.txt and is the only line of text that occurs only once*

### Steps:
`ls` shows one file named *data.txt*  
I tried `cat data.txt | uniq -c -u` to only print the unique lines, but for some reason it says theres more than one unique line.  
### Solution:
I instead tried `cat data.txt | sort | uniq -c -u`, and that returned the flag.  

**Command Breakdown:**
`cat data.txt` gets the text from the file. `| sort` pipes the text into the the sort function, which sorts the lines

**Flag: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR**
