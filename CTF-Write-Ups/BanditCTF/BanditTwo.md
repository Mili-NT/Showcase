# Level: BanditTwo
## Level Credentials: banditTwo:CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
## Level Description: *The password for the next level is stored in a file called spaces in this filename located in the home directory*

### Steps:
First, enumerate the files using `ls`  
This shows one file named *spaces in this filename*  
Trying to use `cat spaces in this filename` shows linux isn't fond of, well, spaces in filenames. It returns an error for each word saying it cant find the file.  
Using `cat ./spaces in this filename` does the same.  
### Solution: 
I had to pass the filename as a string, using `cat 'spaces in this filename'`, which works and returns the flag  

**Flag: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK**
