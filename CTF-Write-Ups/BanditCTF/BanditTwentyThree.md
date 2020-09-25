# Level: BanditTwentyThree
## Level Credentials: bandit23:jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
## Level Description: *A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed. NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level! NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…*

### Steps:  
We know from the previous levels that there's a cronjob in the same directory an with the same naming scheme as before.    
`cd /etc/cron.d/ && cat cronjob_bandit24` gives us the name and location of the shell script, `cat /usr/bin/cronjob_bandit24.sh`:    
> #!/bin/bash  
> myname=$(whoami)  
> cd /var/spool/$myname  
> echo "Executing and deleting all scripts in /var/spool/$myname:"  
> for i in * .*;  
> do  
>    if [ "$i" != "." -a "$i" != ".." ];  
>    then  
>        echo "Handling $i"  
>        timeout -s 9 60 ./$i  
>        rm -f ./$i    
>    fi  
> done  

Let's look at this line for line:    
> It initializes bash      
> It assigns the output of `whoami` to *myname*      
> It changes directory to */var/spool/$myname*    
> It announces that it is "Executing and deleting all scripts in /var/spool/$myname"    
> The for loop deletes all the files in the directory, and with a timeout of 60 and sends the signal '9' upon timeout.    

It executes all scripts in that directory, so all I should have to do is write a script to copy the flag.    
I had to create a new temp directory as well `mkdir /tmp/mili100/dumbshit/`  
`vim pas.sh`  
> #!/bin/bash  
> cat /etc/bandit_pass/bandit24 > /tmp/mili100/dumbshit/solution  

And then `chmod 777` the pas.sh script, `cp pas.sh /var/spool/bandit24` and we're good to go.    
Wait for the cronjob to execute and... nothing.     
Maybe specifiying the file type in the pas.sh script would help:  
> #!/bin/bash  
> cat /etc/bandit_pass/bandit24 > /tmp/mili100/dumbshit/solution.txt 

Still nothing. I do `cd /var/spool/bandit24 && cp /tmp/mili100/dumbshit/pas.sh /var/spool/bandit24 && ls` to check if the script is actually going anywhere. After a few seconds, it disappears from the directory, which means it SHOULD have been executed and deleted.  
`cd /tmp/mili100/dumbshit && ls` shows that *solution.txt* is nowhere to be found.  
Tried changing `cat /etc/bandit_pass/bandit24 > /tmp/mili100/dumbshit/solution.txt` to `cat /etc/bandit_pass/bandit24 >> /tmp/mili100/dumbshit/solution`. Nothing.  

### Solution:    
I think this challenge is broken, so I found a different way `cat /tmp/bandit24/bandit24`  


**Flag: UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ**
