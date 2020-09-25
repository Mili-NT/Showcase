# Level: LeviathanOne
## Level Credentials: leviathan1:rioGegei8m
## Level Description: *none*

### Steps:
using `ls` shows a single file called *check*.    
Its a setuid ELF 32-bit executable, so lets try executing it with `./c*`  
It asks for a password, but rejects *rioGegei8m*  
using itrace to analyze the program (`itrace ./check`) shows it compares the entered string to the string *sex*  
### Solution:
Which, of course, is the correct password for *check*. Entering it grants us a bash shell with the priviledges to access *etc/leviathan_pass/leviathan2*, where the flag is stored.  

**Flag: ougahZi8Ta**
