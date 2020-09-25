# Level: Natas12
## Level Credentials: natas12:EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
## Level Description: *None*

### Steps:
So there's an option to upload an image. Inspecting the source code shows a few functions.    
The first generates a random string and returns it as *$string*    
The next generates a random path and takes *$dir* and *$ext* as parameters, assigns `$dir."/".genRandomString().".".$ext;` to the variable *$path* variable, and returns path  
The third generates a random path from filename and takes *$dir* and *$fn*, assigns `pathinfo($fn, PATHINFO_EXTENSION);` to *$ext* and returns the value of the *makeRandomPath*(*$dir*, *$ext*) function.  
Uploading a file successfully shows something like:
> The file upload/ftpoowtrtu.jpg has been uploaded

Trying to access the */upload/* directory returns a permission error.
### Solution:
**Flag: **
