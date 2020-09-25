# Book Writeup
## Enumeration:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 f7:fc:57:99:f6:82:e0:03:d6:03:bc:09:43:01:55:b7 (RSA)
|   256 a3:e5:d1:74:c4:8a:e8:c8:52:c7:17:83:4a:54:31:bd (ECDSA)
|_  256 e3:62:68:72:e2:c0:ae:46:67:3d:cb:46:bf:69:b9:6a (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: LIBRARY - Read | Learn | Have Fun
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
So lets check out that webpage on port 80. It's a sign in/sign up page for a library. 
I create a user and sign in. There's a way to upload books, which is what we'll start with. 
Submitting a php file says "We will review and update later", so we might need to find something else.

I fiddled around for a bit before going back to look at index.php, the signup page. Here's the sign-up script:
```
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
function validateForm() {
  var x = document.forms["myForm"]["name"].value;
  var y = document.forms["myForm"]["email"].value;
  if (x == "") {
    alert("Please fill name field. Should not be more than 10 characters");
    return false;
  }
  if (y == "") {
    alert("Please fill email field. Should not be more than 20 characters");
    return false;
  }
}
</script>
```
Yeah so what if we just do the exact opposite of this. By modifying the POST request and making a 20+ character email,
it effectively lets us sign up with any email we want-- including those already registered.
This is a SQL Truncation vulnerability, kinda embarrassed I missed this and just barreled past it, but what can you do.
## Initial Compromise
So we have effectively overwritten the password for `admin@book.htb` (and `admin@htb.local` because im stupid),
so we can sign into the admin portal at `/admin/index.php`. We now can see some users that might be handy later:
```
test	a@b.com
shaunwhort	test@test.com
peter	hi@hello.com
degree	degree@gmail.com
ZAP	foo-bar@example.com
mili	admin@htb.local # lol
```
Now that we can see the backend of that book upload form, things are starting to piece together. There's obviously a lot of XSS attempts
visible, but more importantly we can see theres an option to export to PDF.

It took a little digging, but I found an XSS method that results in a local file read when the server generates a PDF ([read here](https://www.esecurify.com/local-file-read-access-through-xss-in-dynamically-generated-email-template-pdf/))

So we submit the `<script>x=new XMLHttpRequest;x.onload=function(){document.write(this.responseText)};x.open("GET","file:///etc/passwd");x.send();</script>` through the upload form as a user, go to the admin panel and generate the PDF, which causes the `/etc/passwd` file to be included.
```
reader:x:1000:1000:reader:/home/reader:/bin/bash
```
We can go ahead and get the user flag by including the `/home/reader/user.txt` file. But, now we need a shell.
## PrivEsc
First, we get can get reader's ssh key by including `/home/reader/.ssh/id_rsa`. 
I tried using it directly, but it needs some tweaking to get it in the correct format. PDF copy/paste is a little weird.

So now we have a shell as reader. Using python and wget, I drop a linpeas script on there and start digging. There is one interesting process:
`20K -rwxrwxr-x 1 reader reader  18K Apr 27 17:54 ./logrotten`
[well well well](https://www.exploit-db.com/exploits/47466)

Using this, we can create a reverse shell as root and cat the roo flag... but quickly because it shuts our connection.
