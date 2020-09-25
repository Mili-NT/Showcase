# Challenge: Reflected XSS
## Challenge Description: *Perform a reflected XSS attack with <iframe src="javascript:alert(`xss`)">.*

### Steps: 
First I browsed around the website for parameters that might be vulnerable to XSS (or SQLi).
I found the ordering tracking input form, and when you enter in anything (for example, `a`) the parameter looks like this: `track-result?id=a`. This is a prime spot for XSS. The challenge says to use the payload `<iframe src="javascript:alert(`xss`)">`. So by entering that javascript into the order tracker, we can see the id parameter is indeed vulnerable to reflected XSS.

### Solution:
Identify potentially vulnerable parameters, such as the order tracker.
Inject javascript to determine vulnerability.
