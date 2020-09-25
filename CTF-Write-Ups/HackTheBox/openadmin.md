# OpenAdmin Writeup

## Enumeration:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4b:98:df:85:d1:7e:f0:3d:da:48:cd:bc:92:00:b7:54 (RSA)
|   256 dc:eb:3d:c9:44:d1:18:b1:22:b4:cf:de:bd:6c:7a:54 (ECDSA)
|_  256 dc:ad:ca:3c:11:31:5b:6f:e6:a4:89:34:7c:9b:e5:50 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
So we've got secure shell and a web server. Upon further inspection, the webpage is a default apache page.
I try a little directory brute forcing, looking for `.php`, `.log`, and `.txt` files. I found quite a lot actually, but one directory stood out: `/ona`. And well, well, well its an admin page. An *open* admin page. Surface level inspection shows a normal admin page, with a lists of hosts, DNS domains, etc. 

One snippet that may be useful when we get on the box is `Database Type	mysqli` in the user info panel. Attempting to go one step deeper in the directory tree reveals that we **can** list the contents of `/ona/include`. 
## Initial Compromise
I dug around and found several interesting exploits for OpenNetAdmin, including a command injection and a RCE. I took the command injection vulnerability and wrote an exploit in python for it.

I now had command execution, so I fetched a webshell from my VM and accessed the machine. I dug around for a bit and found a database settings file with some credentials for an ONA system account on a local db.
```
        'db_type' => 'mysqli',
        'db_host' => 'localhost',
        'db_login' => 'ona_sys',
        'db_passwd' => 'n1nj4W4rri0R!',
```
Attempting to dump the db with those credentials didn't work, but I spawned a reverse shell and tried `su jimmy` and lo and behold: I am now jimmy.

I poked around here are there before finally returning to the www directory tree. I realized that as jimmy, I can see three files in `/var/www/internal`: `index.php`, `main.php`, and `logout.php`. `index.php` has a reference to `main.php`, which will reveal joanna's SSH key! So, by reaching out on port 52846 (found using netstat), we can get joanna's SSH key.

Once we do, we have a problem: its encrypted. Not well, thankfully. After converting it to a JtR compatible format and running rockyou.txt on it, we get a password.

And just like that, we're logged in as joanna and have the user flag.
## PrivEsc
A cursory `su` and `sudo -l` reveals we have sudo privileges on some files:
```
User joanna may run the following commands on openadmin:
    (ALL) NOPASSWD: /bin/nano /opt/priv

```
priv is empty, but we also have sudo privileges on nano, so looks like free access to me. `sudo -u root nano /opt/priv` and now that we're running nano as root, we can just issue a `cat /root/root.txt` from nano.
