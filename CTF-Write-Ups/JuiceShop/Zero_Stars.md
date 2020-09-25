# Challenge: Zero Stars
## Challenge Description: *Give a devastating zero-star feedback to the store.*

### Steps: 
This one was fairly straightforward. In the review store page, you can enter a comment and a 5 star rating. By using burp to proxy and edit the requests, all I had to do was change the `"rating":5` to `"rating":0`

### Solution:
Proxy and intercept HTTP requests between the browser and server. Abuse improper input validation to edit the request data and give a 0 star review.
