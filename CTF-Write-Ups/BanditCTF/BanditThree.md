# Level: Bandit3
## Level Credentials: bandit3:UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
## Level Description: *The password for the next level is stored in a hidden file in the inhere directory.*

### Steps:
Using `ls` reveals the *inhere* directory  
I swap into *inhere* using `cd inhere`  
Using `ls` shows nothing

### Solution:
Using `ls -la` shows a file called *.hidden*, which we can then use `cat .hidden` to open. This is because the `-la` arg makes `ls` not ignore files starting with .  
Alternatively, using `find` shows a directory called *.* and a file called *.hidden* in the *.* directory. 

**Flag: pIwrPrtPN36QITSp3EQaw936yaFoFgAB**
