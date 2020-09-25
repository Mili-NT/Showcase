# Level: BanditThirty
## Level Credentials: bandit30:5b90576bedb2cc04c86a9e924ce42faf
## Level Description: *There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30. Clone the repository and find the password for the next level.*


### Steps:
Let's start off with the usual: `mkdir /tmp/mili105 && cd /tmp/mili105 && git clone ssh://bandit30-git@localhost/home/bandit30-git/repo && cd repo && ls`  
This shows us the repo contains another README.md document. Doing `cat R*` shows a single line of text that says "just an epmty file... muahaha"    
`git branch --list -a` and `git log` dont show anything.    
`git tag` shows a tag called secret.    
### Solution:
`git show secret` opens the secret tag and reveals the flag.  


**Flag: 47e603bb428404d265f59c42920d81e5**
