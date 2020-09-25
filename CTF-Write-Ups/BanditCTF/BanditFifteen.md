# Level: Bandit15
## Level Credentials: bandit15:BfMYroe26WYalil77FoDi9qh59eK5xNr
## Level Description : *The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption. Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…*

### Steps:
Ok, so we've got another send data level. Let's get the data we need to send: `cd /etc/bandit_pass && cat bandit15`.    
> BfMYroe26WYalil77FoDi9qh59eK5xNr  

So we've got the host (*127.0.0.1*), the port (30001), and the data to send (BfMYroe26WYalil77FoDi9qh59eK5xNr).    
But, we have to use SSL encryption. The helpful reading section mentions OpenSSL, so i'll check that out first.    
`openssl` opens the OpenSSL tool and entering `help` gets me the instructions.  
I send the data using `cat bandit15 | openssl s_client -connect 127.0.0.1:30001`    
That just returns the SSL certificate... not what I wanted.    
I forgot the `-ign_eof` parameter, which prevents openssl from closing the connection when the end of the input is reached.    
### Solution: 
I used `cat bandit15 | openssl s_client -connect 127.0.0.1:30001 -ign_eof` and it returned the flag.  

**Flag: cluFn7wTiGryunymYOu4RcffSxQluehd**
