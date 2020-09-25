# Level: NatasSeven
## Level Credentials: natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9
## Level Description: *none*

### Steps:
There are two hyperlinks: *home* and *about*    
Clicking them shows text that says "this is the (front/about) page"    
Inspecting the *about* source code shows a hint:  
> !-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8  

Inspecting the *home* source code shows a different hint:  
> !-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8  

Trying to append `/etc/natas_webpass/natas8` to the URL returns a 404.    
### Solution:   
However, appending `/etc/natas_webpass/natas8` to the `/index.php?page=` parameter, it reveals the flag.    


**Flag: DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe **
