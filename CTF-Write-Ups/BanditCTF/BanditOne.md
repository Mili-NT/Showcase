# Level: Bandit1
## Level Credentials: bandit1:boJ9jbbUNNfktd78OOpsqOltutMc3MY1
## Level Description: *The password for the next level is stored in a file called - located in the home directory*

### Steps:
First, list files using `ls`  
This shows one file named *-*  
I tried to use `cat` to view the file, but the command can't open it and I had to use `^c` to stop the command  

### Solution:
Because *-* is a special character, linux doesn't like using it in filenames. It's used before args, so `cat -` looks like an unspecified argument. Instead, I had to prefix it with a path. Using `cat ./-` opens the file and retuns the flag.  

**Flag: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9**
