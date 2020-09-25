# Level: KryptonFive
## Level Credentials: krypton5:CLEARTEXT
### Level Description: *FA can break a known key length as well. Lets try one last polyalphabetic cipher, but this time the key length is unknown.*

### Steps:
Using `ls` to check out the `/krypton/krypton5` directory shows that we have some encrypted documents, and the encrypted flag.  
Using the same site as last time, I plugged the document into the decoder and got a key of *KEYLENGTH*  
### Solution:  
*VigSquare.py*  
> Enter the cipher: BELOS Z  
> [m]anual or [w]ordlist?: m   
> Enter the key: KEYLENGTH   
> RANDOM  

**Flag: RANDOM**
