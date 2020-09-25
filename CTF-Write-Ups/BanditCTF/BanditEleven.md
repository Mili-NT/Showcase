# Level: BanditEleven
## Level Credentials: bandit11:IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
## Level Description: *The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions*

### Steps:
`ls` shows another data.txt file.  
From the level description, I know it's encoded in ROT13.  
### Solution:
I pipe the text from data.txt into the translate command like this `cat data.txt | tr ‘n-za-mN-ZA-M’ ‘a-zA-Z’`, which returns the flag.

**Command breakdown:**
`cat data.txt | tr` pipes the text from data.txt into the translate command. The parameter for translate is `‘n-za-mN-ZA-M’ ‘a-zA-Z’`.  
The parameter is split into two sets, set one is `‘n-za-mN-ZA-M’` and set two is `‘a-zA-Z’`. Set one is input, and set two is output
 of set one translated. Set one is alphanumeric characters n-z + a-m (nopqrstuvwxyzabcdefghijklm) and N-Z + A-M, so set one is the alphabet rotated by 13. This then replaces it with the standard alphabet `'a-zA-Z'`
 
 
**Flag: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu**
