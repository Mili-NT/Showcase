# Level: BanditTwentySeven
  ## Level Credentials: bandit27:3ba3118a22e93127a4ed485be72ef5ea
## Level Description: *There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo. The password for the user bandit27-git is the same as for the user bandit27. Clone the repository and find the password for the next level.*

### Steps:
Right off the bat, I know I need to git clone the repository     
I'm going to go ahead and make a new temp directory to clone it into: `mkdir /tmp/mili102 && cd /tmp/mili102`    
### Solution:
`git clone ssh://bandit27-git@localhost/home/bandit27-git/repo`  
I cant believe we went from shell escapes to this.  


**Flag: 0ef186ac70e04ea33b4c1853d2526fa2**
