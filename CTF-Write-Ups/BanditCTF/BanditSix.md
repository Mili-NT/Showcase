# Level: BanditSix
## Level Credentials: banditSix:DXjZPULLxYr17uwoI01bNLQbtFemEgo7
## Level Description: *The password for the next level is stored somewhere on the server and has all of the following properties: owned by user 'bandit7', owned by group 'bandit6', 33 bytes in size*

### Steps:
`ls` returns nothing.  
I use `cd .. && cd .. && ls` to change into the highest directory I can, */*, and list its contents.  
### Solution:
I use `find -size 33c -group bandit6 -user bandit7` to find files that match the description.  
It returns a few files, but most say permission denied. One, however, does not: *./var/lib/dpkg/info/bandit7.password*  
`cat ./var/lib/dpkg/info/bandit7.password` returns the flag.  


**Flag: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs**
