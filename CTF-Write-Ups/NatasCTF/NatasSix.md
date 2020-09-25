# Level: NatasSix
## Level Credentials: natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1  
## Level Description: *None*  

### Steps: 
There's an input field titled *input secret* and a button that says *view source code*  
Looking at the php source code, it makes a POST request which, if the input is correct, returns the password.  
### Solution: 
The php code includes a file from the path */includes/secret.inc*, if we navigate to thay path and inspect the source again, it shows the correct input: *FOEIUWGHFEEUHOFUOIU*

Which returns our flag.  


**Flag: 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9**
