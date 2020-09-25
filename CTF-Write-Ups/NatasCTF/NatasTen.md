# Level: NatasTen
## Level Credentials: natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
## Level Description : *None*

### Steps:
This looks identical to the last input form, except for an important few lines:      
>if($key != "") {  
>    if(preg_match('/[;|&]/',$key)) {  
>        print "Input contains an illegal character!";  
>    } else {  
>        passthru("grep -i $key dictionary.txt");  
>    }  

This means there's now input sanitization that blocks these characters: `/[;|&]/`    
But, because we can still input arguments for grep, thats not really an issue.  
### Solution:
Grep can scan multiple files at once, so all we need to do is to scan /etc/natas_webpass/natas11 too.    
`.* /etc/natas_webpass/natas11` will search for any characters in the */etc/natas_webpass/natas11* file and show the results.    


**Flag: U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK**
