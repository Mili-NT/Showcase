# Level: LeviathanFive
## Level Credentials: leviathan5:Tith4cokei
## Level Description: *none*

### Steps:
`ls` reveals an executable called *leviathan5*, and running that with `./l*` shows an error:   
> Cannot find /tmp/file.log    

Well, lets see what happens if theres an */tmp/file.log*  
The answer is it prints a large amount of characters before I ctrl+z.    
### Solution:
Let's create a symlink to the password instead using `ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log` 
Running `./l*` returns the flag! 


**Flag: UgaoFee4li**
