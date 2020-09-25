# Challenge: Repetitive Registration
## Challenge Description: *Follow the DRY principle while registering a user.*

### Steps: 
The words "repetitive" and "DRY" (Dont Repeat Yourself) makes me think theres an issue with the repeat password form for registering new user.
To test this I registered a new user `test@localhost.com`. I entered the password `password` and tried proceeding with an empty repeat password field.
Expectedly, this threw an error. I tried matching the passwords, and changing the first password field (Dont repeat yourself!), and it allowed me to register a new user.

### Solution:
Manipulate the repeat password field to believe there are matching passwords
