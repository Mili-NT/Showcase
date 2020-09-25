# Challenge: Error Handling
## Challenge Description: *Provoke an error that is neither very gracefully nor consistently handled.*

### Steps: 
I was checking for SQL Injection on the login form. I checked for improper input sanitization for ; but no results. When I checked for a single apostrophe, it returns a javascript error `[object Object]` which is improperly handled. This triggers the 

### Solution:
Check for improper character sanitization on the login form
