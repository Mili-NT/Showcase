# Level: BehemothOne
## Level Credentials: behemoth1:aesebootiv
## Level Description: *none*

### Steps: 
This time we're working with an aexecutable called *behemoth1*.  
When ran with `./behemoth1`, it asks for a password.  
Running it with `ltrace ./behemoth1` doesn't reveal an obvious string comparison like last time.  
It does use `gets` however, and a google search for "gets C vuln" shows that we're dealing with a buffer overflow.  

### Solution:


**Flag: **
