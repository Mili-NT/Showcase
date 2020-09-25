# Challenge: Login Admin
## Challenge Description: *Log in with the administrator's user account.*

### Steps: 
The first step is obviously to find the admin account name. Looking through the shop, we can find a user by the name of "admin@juice-sh.op" in the review section of a product. 
The challenge type is listed under injection, so we're likely dealing with SQL injection.

... but as it turns out, the path of least resistance is the fastest. Using a python script with selenium to guess variations of weak administrator passwords reveals that the unfortunate administrator was using admin123 as a password

### Solution:
Check password strength first and foremost, then test for injections. If the login application is homebrewed, then parameter tampering or SQL injection is a definitely possibly for authentication bypass leading to privilege escalation.
