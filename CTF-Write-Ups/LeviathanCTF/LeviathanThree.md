# Level: LeviathanThree
## Level Credentials: leviathan3:Ahdiemoo1j
## Level Description: *none*

### Steps:
Using `ls` we see an executable called *file3*. Running it reveals we need to enter a password.    
Running it with `ltrace ./file3` show us what exactly is going on:  
> __libc_start_main(0x8048618, 1, 0xffffd794, 0x80486d0 <unfinished ...>  
> strcmp("h0no33", "kakaka")                       = -1   
> printf("Enter the password> ")                   = 20  
> fgets(Enter the password> kakaka  
> "kakaka\n", 256, 0xf7fc55a0)               = 0xffffd5a0  
> strcmp("kakaka\n", "snlprintf\n")                = -1  
> puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG  
> )                       = 19  
> +++ exited (status 0) +++  

So it compares "h0no33" and "kakaka" for seemingly no reason, then prints the password prompt, and compares it to "snlprintf\n"    
### Solution:
So we run it again and provide snlprintf as the password, and bingo.  


**Flag: vuH0coox6m**
