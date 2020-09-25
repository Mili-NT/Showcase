# Challenge: Admin Section
## Challenge Description: *Access the administration section of the store.*

### Steps: 
After solving the admin login and password strength challenges, I figured this would be a good challenege to start with, as I should already have the permissions needed to access the section once I find it.

The first step is to do enumeration for the directories using gobuster... which starts getting IOErrors after a few seconds. It did reveal some potentially interesting directories for future challenges, such as /accesskeys, however.

When in doubt, do it by hand. Admin, admin, Administrator, administrator all are no dice.


/#/administration gets us access, however. There is also an alternate way to do this, if you search in the `main-es2015.js` (one of the 3 or 4 main js files on the site) file for "admin" theres a path variable that reveals the path as well.

### Solution:
Directory brute forcing and source inspection can reveal sensitive info like this, so always check source files for potentially interesting inclusions.
