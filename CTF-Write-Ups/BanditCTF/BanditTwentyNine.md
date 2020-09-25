# Level: BanditTwentyNine
## Level Credentials: bandit29:bbc96594b4e001778eee9975372716b2
## Level Descripton: *There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo. The password for the user bandit29-git is the same as for the user bandit29. Clone the repository and find the password for the next level.*


### Steps:
We go ahead and `git clone ssh://bandit29-git@localhost/home/bandit29-git/repo` and check its contents.  
Inside is a README.md that is pretty similar to the last one:
> Bandit Notes
> Some notes for bandit30 of bandit.
>
> credentials
>
> - username: bandit30
> - password: <no passwords in production!>


`git log -p` reveals something weird: the password was never changed, but the username was changed from bandit29 to bandit30.    
The 'no passwords in production' makes me think maybe theres a seperate branch.    
`git branch --list` shows that there is only the master branch, sadly.    
Looking back at git documentation, I realized master is the only LOCAL branch, but I need to add the `-a` arg to show remote:  
>  master  
>  remotes/origin/HEAD -> origin/master  
>  remotes/origin/dev  
>  remotes/origin/master  
>  remotes/origin/sploits-dev  

Thats better. Let's use `git checkout` to check these out.  
### Solution:
Luckily, the first try is the charm. Looking at the remotes/origin/dev for the pre-production branch shpws our flag.  


**Flag: 5b90576bedb2cc04c86a9e924ce42faf**
