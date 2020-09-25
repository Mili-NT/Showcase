# Level: LeviathanSix
## Level Credentials: leviathan6:UgaoFee4li
## Level Description: *none*

### Steps:
Using `ls` shows theres a single executable called *leviathan6*    
Running it with `./l*` shows a usage guide:    
> ./leviathan6 <4 digit code>  

We all know what this calls for:  
> for i in {0000..9999};
> do
>        echo -n "$i is "; ./leviathan6 "$i";
> done

On pin 7123, instead of "Wrong" it executes a shell as leviathan7  
### Solution:
With a `cat /etc/leviathan_pass/leviathan7` we have our flag.  

**Flag: ahy7MaeBo9**
