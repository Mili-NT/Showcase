# Level: BanditSixteen
## Level Credentials: bandit16:cluFn7wTiGryunymYOu4RcffSxQluehd
## Level Description: *The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.*

### Steps: 
Let's get the data we need to send: `cd /etc/bandit_pass && cat bandit16`  
> cluFn7wTiGryunymYOu4RcffSxQluehd  

Ok, so we have the host (*127.0.0.1*) and the data (cluFn7wTiGryunymYOu4RcffSxQluehd), but we have a port range this time.    
I tried using `netstat -plnt | grep 3[1][0-9][0-9][0-9]`, but the unfortunately this returned an error (I think because it needs sudo):  
> netstat: no support for `AF INET (tcp)' on this system.`  

Well, I'll use nmap, because I have more experience with it.    
### Solution:
`nmap -p 31000-32000 127.0.0.1` This scans all the ports from 31000-32000.  
> PORT      STATE SERVICE  
> 31518/tcp open  unknown  
> 31790/tcp open  unknown  

Fortunately, this isnt a large list. So whichever port isn't correct will just echo the bandit16 password back.  
`cat bandit16 | openssl s_client -connect 127.0.0.1:31518 -ign_eof`  
> cluFn7wTiGryunymYOu4RcffSxQluehd  

No luck. `cat bandit16 | openssl s_client -connect 127.0.0.1:31790 -ign_eof`  
And it returns our flag: a new private key!  

**Flag: SSH Key**
