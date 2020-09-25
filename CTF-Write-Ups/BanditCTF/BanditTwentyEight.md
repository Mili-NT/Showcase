# Level: BanditTwentyEight
## Level Credentials: bandit28:0ef186ac70e04ea33b4c1853d2526fa2
## Level Description: *There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28. Clone the repository and find the password for the next level.*

### Steps:
So, we create a new drectory for bandit28 and clone the repo into it using `mkdir /tmp/mili103 && cd /tmp/mili103 && git clone ssh://bandit28-git@localhost/home/bandit28-git/repo`    
That gives us a folder called *repo* with a document called *README.md* inside. `cat R*` shows us:  
> Bandit Notes  
> Some notes for level29 of bandit.  
>
> credentials  
>
> - username: bandit29  
> - password: xxxxxxxxxx  

So, no password. Let's check the commit history using `git log`.    
This reveals three commits: initial, 'add missing data', and 'fix info leak'.  
### Solution:  
Using the patch argument on `git log` shows us the data changed with each commit, and shows us the deleted flag.  


**Flag: bbc96594b4e001778eee9975372716b2**
