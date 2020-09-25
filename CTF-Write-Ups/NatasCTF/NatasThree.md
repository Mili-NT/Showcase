# Level: NatasThree
## Level Credentials: natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
## Level Description: *There's nothing on this page.*  

### Steps:
Inspecting the page html reveals... nothing.  
Except for a comment that says "No more information leaks!! Not even google will find it this time.."  
This probably has something to do with search engine indexing.  
### Solution: 
When viewing the *robots.txt* file by appending `/robots.txt` to the URL, it shows that it bans crawling a directory called `/s3cr3t/`  
This directory contains a *user.txt* file, which contains the flag.  


**Flag: Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ**
