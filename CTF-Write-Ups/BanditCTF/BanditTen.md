# Level: BanditTen
## Level Credentials: bandit10:truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
## Level Description: *The password for the next level is stored in the file data.txt, which contains base64 encoded data*

### Steps:
`ls` shows another data.txt file.  
`cat data.txt` shows a b64 encoded string.  
### Solution:
`cat data.txt | base64 -d` pipes the output and decodes it, returning the flag 


**Flag: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR**
