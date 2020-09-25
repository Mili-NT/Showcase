# Level: NatasEight
## Level Credentials: natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
## Level Description: **

### Steps:
There's another input field with a view source button.  
The basic structure is the same as the last as far as the actual authentication code goes.  
However, theres a variable called *encodedSecret* which has a value of *3d3d516343746d4d6d6c315669563362*  
Next, theres a function called *encodeSecret* which is being passed the *secret* variable as a parameter.  
*encodeSecret* returns the hexadecimal value of the binary data of the reversed version of the base64 encoded value of *$secret*... whew.  
Take the *encodedSecret* variable, and first convert it to binary ([This is the tool I used](http://hex2bin.onlinephpfunctions.com/)):
> ==QcCtmMml1ViV3b 

Then, reverse that:
>  b3ViV1lmMmtCcQ==

Now that looks familar. Decode this from base64:
> oubWYf2kBq

And that looks like the correct input for the *secret* variable.  
### Solution:
Sure enough, inputting `oubWYf2kBq` will return the flag.  


**Flag: W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl**
