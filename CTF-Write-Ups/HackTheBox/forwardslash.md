# ForwardSlash Writeup
My best tips for this box:
1. Read and read carefully
2. DON'T OVERTHINK! Rabbit holes are easy to get into, hard to get out of
3. Whenever you think "yeah thats enough enumeration", keep enumerating
## Enumeration:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 3c:3b:eb:54:96:81:1d:da:d7:96:c7:0f:b4:7e:e1:cf (RSA)
|   256 f6:b3:5f:a2:59:e3:1e:57:35:36:c3:fe:5e:3d:1f:66 (ECDSA)
|_  256 1b:de:b8:07:35:e8:18:2c:19:d8:cc:dd:77:9c:f2:5e (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Backslash Gang
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Looks like web exploitation is back on the menu. Connecting to the webserver on port 80 shows a defaced webpage, which says:
```
|  You call this security? LOL, absolute trash server...  |
#Defaced • This was ridiculous, who even uses XML and Automatic FTP Logins
```
and a some other shit we really dont care about. 
After a **lot** of fuzzing, we can see a file telling us that theres a backup site for the defaced page:

Accessing it (after more fuzzing to find it) shows us an option to login or register. 
### (Helpful hint: There are more types of fuzzing than looking for directories and files)
We have two options here:
1. Register an arbitrary user and proceed
2. Register with the username 'admin' and proceed

Now registering as admin wont inherently give you any privilege, but we'll get to that.

## Initial Compromise
Let's proceed as a regular user first. First things first, we fuzz the backup site and look for directories. There is one directory and fuzzing for files in it shows us some files we have to figure out how to read.

We can see a few options, but the only thing of interest to us is an option to change profile pictures by providing a URL. We can use Server Side Request Forgery (SSRF) to turn this into a Local File Inclusion (LFI). By tampering with the method and pointing the URL to the files we need to read, we can access the files.
### (Helpful hint: you're browsing a filesystem. Remember that.)
So before looking at the main file, a different file on the webserver shows us a glimpse into the backend:
```
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'www-data');
define('DB_PASSWORD', '5iIwJX0C2nZiIhkLYE7n314VcKNx8uMkxfLvCTz2USGY180ocz3FQuVtdCy3dAgIMK3Y8XFZv9fBi6OwG6OYxoAVnhaQkm7r2ec');
define('DB_NAME', 'site');
```
Those credentials arent worth pursuing, but it tells us something really important: they are using a file that stores credentials and they have a MySQL DB on localhost.

Moving on to the code of the main file shows why my discovery of creating a user of admin would've saved me so much time:
```
if((!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true || $_SESSION['username'] !== "admin") && $_SERVER['REMOTE_ADDR'] !== "127.0.0.1"){
    header('HTTP/1.0 403 Forbidden');
}
```
Simply by having the username admin, we gain permission to view this file directly without needing SSRF, although I believe I'd still need to use SSRF to view the php code. The file appears to be an API that uses XML:
```
<html>
	<h1>XML Api Test</h1>
	<h3>This is our api test for when our new website gets refurbished</h3>
	<form action="/***/*****.php" method="get" id="xmltest">
		<textarea name="xml" form="xmltest" rows="20" cols="50"><api>
    <request>test</request>
</api>
</textarea>
		<input type="submit">
	</form>

</html>
```
More interesting is the php code in this file that appears to deal with FTP. Remember how the defaced webpage blasted these guys for automatic FTP logins? Looks like somebody didn't quite learn their lesson:
```
		if (@ftp_login($conn_id, "chiv", '<password here>')) {

			error_log("Getting file");
			echo ftp_get_string($conn_id, "debug.txt");
		}
```
So now we can ssh in as chiv, as go from there. I initially tried dumping the SQL database as `www-data` and then as `shiv`, but no luck. Then I went back and reread the file, and saw a interesting comment:
```
//credentials for the temp db while we recover, had to backup old config, didn't want it getting compromised -pain
```
So I did some snooping around and found the backed up file at `/var/backups/config.php.bak`. We dont have permission to read it directly, *however* we can make a symlink linking `/var/backups/config.php.bak` to `/home/chiv/backup_config.php` and then executing `/usr/bin/backup` and read via that method:
```
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'pain');
define('DB_PASSWORD', 'db1f73a72678e857d91e71d2963a1afa9efbabb32164cc1d94dbc704');
define('DB_NAME', 'site');
```
And wala, we can SSH in as `pain` and get the user flag!

# PrivEsc
So off the bat we can see a directory called `encryptorinator` in `/home/pain`. It contains a ciphertext, a `decoder.py`, and an `encoder.py`.

Let's check out encrypt function first:
```
def encrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in key:
        for i in range(len(msg)):
            if i == 0:
                tmp = ord(msg[i]) + ord(char_key) + ord(msg[-1])
            else:
                tmp = ord(msg[i]) + ord(char_key) + ord(msg[i-1])

            while tmp > 255:
                tmp -= 256
            msg[i] = chr(tmp)
    return ''.join(msg)
```
So it takes a `key` and a `msg`, splits them both into lists of characters.
It loops over every character in the `key` and every item in a range of length of `msg`.
**Where `i` is the position in len(msg)**
if `i` is 0, aka the first, it assigns:
`ord(msg[i]) + ord(char_key) + ord(msg[-1])` to `tmp`
if `i` is not 0, aka any other position, it assigns:
`ord(msg[i]) + ord(char_key) + ord(msg[i-1])` to `tmp`

It then checks if `tmp` is greater than 255, and while it is, 256 is subtracted from `tmp`.
then it sets whatever letter is in position `i` in the msg to the `chr` value of `tmp`

Finally, it returns `msg` as a string. Not too bad.

Let's check out the decrypter:
```
def decrypt(key, msg):
    key = list(key)
    msg = list(msg)
    for char_key in reversed(key):
        for i in reversed(range(len(msg))):
            if i == 0:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[-1]))
            else:
                tmp = ord(msg[i]) - (ord(char_key) + ord(msg[i-1]))
            while tmp < 0:
                tmp += 256
            msg[i] = chr(tmp)
    return ''.join(msg)
```
Takes a `key` and an **encrypted** `msg` and essentially perform the reverse operation.
`ord(msg[i]) - (ord(char_key) + ord(msg[-1]))`
`ord(msg[i]) - (ord(char_key) + ord(msg[i-1]))`
`tmp += 256`

I split the actual decoding into a seperate function:
```
def decoder(key, msg):
    for i in range(1, 165):
        for j in range(33, 127):
            key = chr(j) * i
            msg = decrypt(key, cipher)
            if 'the ' in msg or 'be ' in msg or 'and ' in msg or 'of ' in msg :
                exit("Key: {0}, Key length: {1}, Msg: {2}".format(key, len(key), msg))
```
Here's the interesting thing: `key` is passed as a parameter into `decoder()` but get this: *its not needed*
Decoder redeclares key as `key = chr(j) * i`.

Let's make some changes to the code:
First we'll get rid of the unnecessary while loops to consolidate our possible keys in one spot:
```
keys = [chr(j) * i for i in range(1, 165) for j in range(33, 127)]
```
We can see there are 15416 possible keys and we all have them one one big happy list.
Now, to decode them:
```
def decoder():
    keys = [chr(j) * i for i in range(1, 165) for j in range(33, 127)]
    print(len(keys))
    for key in keys:
        decoded = str(decrypt(key, cipher))
        if any(artifact in decoded for artifact in ['the ', 'be ', 'and ', 'of ']):
            exit(f"Key: {key},\n Key length: {len(key)},\n Msg: {decoded}")
```
This returned no matches, so I inspected the input and realized I forgot to remove newlines:
```
cipher = open("ciphertext", 'r', encoding="UTF-8").read().replace("\n", "")
```
And when we run this, we get a message giving us the key to an encrypted backup at `/var/backups/recovery/encrypted_backup.img`

Running `sudo -l` shows we can do a few things as root:
1. mount
2. use openluks
3. unmount

So, we mount the `encrypted_backup.img`, enter the key, and get a ssh key for root. 

And finally, we have the root flag. This box was hard, I suffered a lot, goodnight.
