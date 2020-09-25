# Level: BanditTwentyTwo
## Level Credentials: bandit22:Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
## Level Description: *A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed. NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.*

### Steps:
I know from last level that there were two cronjobs for level 23 and 24, so we know we'll be using those.    
`cd /etc/cron.d/ && cat cronjob_bandit23` will show us the relevant shell script:  
> @reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null  
> * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null  

Almost identical to the last cronjob, so let's try the same thing:    
`/etc/cron.d$ cd /usr/bin && cat cronjob_bandit23.sh`:  
> #!/bin/bash   
> myname=$(whoami)  
> mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)  
> echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"  
> cat /etc/bandit_pass/$myname > /tmp/$mytarget  

This is a more complicated bash script than the last one. I'll go through it line for line:    
> intitializes the script    
> It assigns the output of `whoami` to the *$myname* variable  
> It pipes I am user *$myname*" through md5sum, and then pipes the md5 checksum the cut command with space set as the delimiter and only cuts the first line, and assigns all this to the *mytarget* variable  
> It then copies the contents of */etc/bandit_pass/$myname* to */tmp/$mytarget*    

It's not relevant, but I was a little curious about the difference between `echo I am user $myname | md5sum | cut -d ' ' -f 1` and `echo I am user $myname | md5sum`, so I ran this lovely command to compare the two:    
`nocut=$(myname=$(whoami) && echo I am user $myname | md5sum) && cuttrue=$(myname=$(whoami) && echo I am user $myname | md5sum | cut -d ' ' -f 1) && diff -u <(echo "$nocut") <(echo "$cuttrue")`  
> '>--- /dev/fd/63  2019-07-21 19:17:07.168903177 +0200'  
> +++ /dev/fd/62  2019-07-21 19:17:07.168903177 +0200  
> @@ -1 +1 @@  
> -8169b67bd894ddbb4412f91573b38db3  -  
> +8169b67bd894ddbb4412f91573b38db3  

So the cut just removes the dash at the end and adds a plus to the beginning. But, back to the important stuff.    
I got into the new file, */tmp/$mytarget*, using `myname=$(whoami) && mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1) && cat /tmp/$mytarget`  
> Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI  

But, thats the flag for this level, not level 23.  
So let's make a slight modification to the bash script.  
`myname=$(whoami) && echo $myname` returns 'bandit22', but we want to be bandit23.   
### Solution:
Simply replace the *myname* var with bandit23:  
` myname=(bandit23) && mytarget=$(echo I am user $myname                                                                                                              | md5sum | cut -d ' ' -f 1) && cat /tmp/$mytarget`  
> jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n

And there's the flag.


**Flag: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n**
