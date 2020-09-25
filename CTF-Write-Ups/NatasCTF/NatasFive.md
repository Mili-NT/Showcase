# Level: NatasFive
## Level Credentials: natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
## Level Description: *Access disallowed. You are not logged in*

### Steps:
I start by looking through the source html, but theres nothing.    
I start intercepting the requests again, and see a GET request of interest.    
### Solution:
The GET request has two parameters (each of which are cookies).    
Only one is of interest here: the *loggedin* cookie, which has a value of 0.    
Using Burp, we change the value to 1 and we are logged in and can see the flag.   


**Flag: aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1**
