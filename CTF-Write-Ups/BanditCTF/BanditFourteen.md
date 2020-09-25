# Level: BanditFourteen
## Level Credentials: bandit14:SSH Key
## Level Description: *The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.*  

### Steps:
So, it wants me to submit the current password, so I revisit that file I couldn't open last level: `cd /etc/bandit_pass && cat bandit14`  
> 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e

Now, to send this to port 30000 on localhost (fun fact: port 30000 is the unofficial pokemon netbattle port).  
I feel pretty confident that localhost is *127.0.0.1*. So I know the host, the port, and the data to send.

### Solution:
I haven't used netcat much, but it's fairly easy with the man page: `nc 127.0.0.1 30000 < bandit14`
> Correct!  
> BfMYroe26WYalil77FoDi9qh59eK5xNr


**Flag: BfMYroe26WYalil77FoDi9qh59eK5xNr**
