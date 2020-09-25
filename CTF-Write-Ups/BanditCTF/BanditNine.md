# Level: BanditNine
## Level Credentials: bandit9:UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
## Level Description: *The password for the next level is stored in the file data.txt in one of the few human-readable strings, beginning with several ‘=’ characters.*

### Steps:
`ls` shows i'm working with *data.txt* again.  
`cat data.txt` shows a long file with a lot of unreadable text in it.  
I tried using`cat data.txt | grep text` because I used `grep text` in level 4, but that didn't work because when I used `grep text`, I was piping the output from a different command into it.    
I tried `cat data.txt | grep = -a` to read the binary as text, but it still returned a bunch of unreadable lines.  
### Solution:
`cat data.txt | strings` cleans the file into readable strings.  
`cat data.txt | strings | grep "^="` returns all the lines that start with *=* (about 5 of them), and the last one is the flag  


**Flag: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk**
