# Level: KryptonOne
## Level Credentials: krypton1:KRYPTONISGREAT
## Level Description: *The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!*  

### Steps:
Using `file k*` shows that *krypton2* is just ASCII text.    
`cat k*` shows us:  
> YRIRY GJB CNFFJBEQ EBGGRA  

The level description mentions a "simple rotation", which is probably ROT13  
### Solution:  
Sure enough, decoding the cipher text with ROT13 reveals:  
> LEVEL TWO PASSWORD ROTTEN  


**Flag: ROTTEN**
