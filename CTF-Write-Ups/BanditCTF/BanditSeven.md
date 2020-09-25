# Level: BanditSeven
## Level Credentials: bandit7:HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
## Level Description: *The password for the next level is stored in the file data.txt next to the word millionth*

### Steps:
`ls` shows theres one file called *data.txt*   
`cat data.txt` shows there is a long list of words and an associated password string.      
### Solution:
The real password is on the line that has millionth in it, so I use `grep 'millionth' data.txt` to find that line.    
This returns the line with millionth on it, and the also the flag.  


**Flag: cvX2JJa4CFALtqS87jk27qwqGhBM9plV**  
