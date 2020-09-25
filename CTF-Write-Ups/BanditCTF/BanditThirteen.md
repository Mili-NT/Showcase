# Level: BanditThirteen
## Level Credentials: bandit13:8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
## Level Description: *The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on*  

### Steps:
I don't really know where to start, so I `cd /etc/bandit_pass`.    
I can't read the bandit14 password, because I need a private ssh key. I either have to generate(?) one or find one.    
I do `cd /etc/ssh && ls` to view the *ssh* directory contents.  
> moduli            ssh_host_dsa_key.pub    ssh_host_ed25519_key.pub  
> ssh_config        ssh_host_ecdsa_key      ssh_host_rsa_key  
> sshd_config       ssh_host_ecdsa_key.pub  ssh_host_rsa_key.pub  
> ssh_host_dsa_key  ssh_host_ed25519_key  

So, pretty normal. I was looking for something like *id_dsa*, but no luck.    
Like an absolute idiot, I neglected to check the */home/bandit13* directory, which contains a private ssh key... of course.    
### Solution:
`cat ssh*` reveals the ssh key, which I copy into a text file on my machine, which I use puttygen to convert into a .ppk file, and then make the connection again and use the key for authentication.  


**Flag: SSH Key**
