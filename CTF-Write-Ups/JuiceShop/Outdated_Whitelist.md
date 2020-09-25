# Challenge: Outdated Whitelist
## Challenge Description: *Let us redirect you to one of our crypto currency addresses which are not promoted any longer.*

### Steps: 
So while I was looking through redirect links to find scoreboard, I remember seeing several cryptocurrency links that confused me. It looks likes its time to investigate those.
I picked: `https://etherscan.io/address/0x0f933ab9fcaaa782d0279c300d73750e1311eae6` from the js code and added a redirect method to the url like so:
`http://localhost:3000/#/redirect?to=https://etherscan.io/address/0x0f933ab9fcaaa782d0279c300d73750e1311eae6` and sure enough that completed the challenge.

### Solution:
Search for outdated redirects
