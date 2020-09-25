# Level: BanditTwelve
## Level Credentials: bandit12:5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
## Level Description: *The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)*


### Steps:
`ls` shows *data.txt*    
`cat data.txt` shows a hexdump    
Following the level description advice, I create a directory in */tmp* using `mkdir /tmp/mili99`    
I then used `cp data.txt /tmp/mili99` to copy it to my directory.    
I tried using `xxd -r data.txt data.txt` to convert the hex to text and overwrite data.txt with the text. Unfortunately, this didn't work and made xxd not work on the data.txt.   
I used `cd /home/bandit12 && cp data.txt /tmp/mili99 && cd /tmp/mili99` to get the original data.txt back.  
I tried using `xxd -r data.txt data2.txt` multiple times, but when I got to *data4.txt* the file was empty.  
So, I used `rm data*` to delete all the files, and copied the original again.    
`cat data.txt | xxd -r | strings` pipes the reverse hexdump through strings to get rid of the binary, which outputs  
> data2.bin  
> BZh91AY&SY  
> P"2@  

I decided to take a different approach. Decompression is obviously involved, but `file data.txt` shows that data.txt is a plain ASCII text file.    
I used `xxd -r data.txt data.bin` to convert it to a binary file, and used `file data.bin` to examine the new file type.  
> data.bin: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix  

Now i'm on to something, but I still cant decompress *data.bin*, so I use `mv data.bin databin.gz` to rename it in gzip format.    
I decompress it using `gzip -d databin.gz` and inspect using `file databin`, which reveals this is now a bzip2 compressed file.    
So I add the bzip2 extension, `mv databin databin.bzip2`, and decompress it: `bzip2 -d databin.bzip2`.    
This outputs *databin.bzip2.out*, which `file databin.bzip2.out` reveals to be... a gzip file. Here we go again.    
`mv databin.bzip2.out databin.gz` to get the .gz extension, `gzip -d databin.gz` to decompress, and `file databin` to inspect the new file.  
> databin: POSIX tar archive (GNU)  

Finally, not a zipped file. It's a taped file, so I need to use `tar` to unarchive it... but I need the extension first.    
`mv databin databin.tar` returns databin as a .tar file, and I tried to use `tar -x databin.tar` to unarchive it.    
> tar: Refusing to read archive contents from terminal (missing -f option?)  
> tar: Error is not recoverable: exiting now    

Crap. After all those successful commands too. I add the -f arg in and retry `tar -xf databin.tar`, which gives me *data5.bin*  
`file data5.bin` is... another posix tar archive. This is getting a little crazy.    
`mv data5.bin data5bin.tar` to get the extension, `tar -xf data5bin.tar` to decompress, which outputs *data6.bin*, another bzip file.      
My connection got timed out, but my directory and progress were saved!    
I decided to declutter my */tmp/mili99* directory and move all the old files to a new subdirectory using `mkdir progress && mv data5bin.tar /tmp/mili99/progress && mv databin.tar /tmp/mili99/progress && mv data.txt /tmp/mili99/progress`    
So, back to the *data6.bin*... ` mv data6.bin data6.bzip2 && bzip2 -d data6.bzip2`, which gives us another tar archive.    
`mv data6.bzip2.out data6bin.tar && tar -xf data6bin.tar` gives us data9.bin, a gzip file.    
`mv data8.bin data8.gz && gzip -d data8.gz` which gives us *data8*, and when inspected with `file data8` which shows us... ITS AN ASCII FILE! Could this be our flag?    
`cat data8`  
> The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL  

Sure is, finally!

### Solution:
- convert data.txt to binary with `xxd -r`
- use `file` to inspect type
- rename file to have the matching extension for that type
- unzip/unarchive
- repeat... a LOT.


**Flag: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL**
