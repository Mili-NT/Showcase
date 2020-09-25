# Level: NatasNine
## Level Credentials: natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
## Level Description: *none*

### Steps:
The page shows an input box titled "find words containing*, a section for output, and a view sourcecode button.  
Here is the source code:  
>$key = "";  
>  
>if(array_key_exists("needle", $_REQUEST)) {  
>    $key = $_REQUEST["needle"];  
>}  
>  
>if($key != "") {  
>    passthru("grep -i $key dictionary.txt");  
>}  

The code mentions a *dictionary.txt* file that we can access by appending `/dictionary.txt` to the URL, but its a long file.    
Now, if we input something like `-c giraffe`, we can see that there is no input sanitization, and that grep takes the -c as an argument and outputs the times giraffe occurs.    
So I got a little side tracked and decided to see if the password itself was stored in *dictionary.txt* by copying the file and running it through `cat dictionary.txt | sort | uniq -u -c`    
Unfortunately, it looks like we're dealing with another passphrase to get the password deal.    
Or... if the input is prepended by a semi-colon, linux will execute the commands sequentially. Kind of like &&.  
Inputting `; pwd` shows we are in the */var/www/natas/natas9* directory.  
### Solution:
We can use `; cat /etc/natas_webpass/natas10` as input to print out the natas9 flag.  


**Flag: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu**
