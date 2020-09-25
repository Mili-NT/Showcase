# Level: BanditThirtyOne
## Level Credentials: bandit31:47e603bb428404d265f59c42920d81e5
## Level Description: *There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31. Clone the repository and find the password for the next level.*

### Steps:
`git clone ssh://bandit31-git@localhost/home/bandit31-git/repo`    
Inspecting the *README.md* file tells us we have to push a file to master, with the name *key.txt* and the contents "May I come in?"    
`echo May I come in? > key.txt`    
### Solution:
`git add key.txt -f && git commit && git push` reveals the flag.  


**Flag: 56a9bf19c63d650ce78e6ec0354ee45e**
