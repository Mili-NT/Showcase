# Level: NatasFour
## Level Credentials: natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
## Level Description: *Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"*

### Steps:
This obviously wants me to change the referer on the request.    
### Solution: 
I used Burp Suite to intercept the request, and changed the referer to *http://natas5.natas.labs.overthewire.org/*  


**Flag: iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq**
