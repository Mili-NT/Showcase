# Challenge: Score Board
## Challenge Description: *Find the carefully hidden 'Score Board' page.*

### Steps: 
I ran OWASP:ZAP looking for a direct link to the scoreboard. Unfortunately, none were found. I manually tried almost every variation of scoreboard, but to nom avail. I grepped through the spider results and found a few references to a `scoreBoard` variable in a `main-es5.js` file. Searching the instances of those variables, none directly had a link attached to them. Looking for a redirect link, however turned up the directory `/score-board`, which I swear I tried but whatever.

### Solution:
Spider the website, grep through the results for relevant scoreboard variables, and abusing redirect links to find the scoreboard
