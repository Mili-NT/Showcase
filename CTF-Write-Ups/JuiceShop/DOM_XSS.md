# Challenge: DOM XSS
## Challenge Description: *Perform a <iframe src="javascript:alert(`xss`)">.*

### Steps: 
Honestly this was a bit of luck. I read about DOM XSS attacks on OWASP's top ten list. It mentioned language changing functionality as a specific attack vector, so I wasted a few minutes toying with requests in burp to try and execute it that way.
Eventually I simply went the brute force route and decided to attack any input form I could find. Luckily the search function was the first I found, and is also the only one that modifies DOM.

### Solution:
Identify vulnerable input form and send payload
