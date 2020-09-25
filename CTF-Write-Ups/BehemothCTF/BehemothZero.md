# Level: BehemothZero
## Level Credentials: behemoth0:behemoth0
## Level Description: *none*

### Steps:  
Changing directories to */behemoth* and using `ls` shows an executable for each level    
Running `./behemoth0` asks for a password... back to good ol `ltrace`:  
> __libc_start_main(0x80485b1, 1, 0xffffd794, 0x8048680 <unfinished ...>  
> printf("Password: ")                             = 10  
> __isoc99_scanf(0x804874c, 0xffffd69b, 0xf7fc5000, 13Password: pass  
> ) = 1  
> strlen("OK^GSYBEX^Y")                            = 11    
> strcmp("pass", "eatmyshorts")                    = 1  
> puts("Access denied.."Access denied..  
> )                          = 16  
> +++ exited (status 0) +++  

Well, easy enough. Using *eatmyshorts* as a password opens an elevated shell.      
### Solution:
With a simple `cat /etc/behemoth_pass/behemoth1` we have our flag:  

**Flag: aesebootiv**
