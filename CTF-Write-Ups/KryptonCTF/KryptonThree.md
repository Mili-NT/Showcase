# Level: KryptonThree
## Level Credentials: krypton3:CAESARISEASY
## Level Description: *The main weakness of a simple substitution cipher is repeated use of a simple key. In the previous exercise you were able to introduce arbitrary plaintext to expose the key. In this example, the cipher mechanism is not available to you, the attacker. However, you have been lucky. You have intercepted more than one message. The password to the next level is found in the file ‘krypton4’. You have also found 3 other files. (found1, found2, found3). You know the following important details: The message plaintexts are in English (very important) - They were produced from the same key (even better!)*

### Steps: 
There are two hints located in the *krypton3* directory:  
> Some letters are more prevalent in English than others. 
> "Frequency Analysis" is your friend.  

So the key to all of this probably has to do with how frequently a letter, or a group of letters, appears in the encrypted file.  
This is the contents of the encrypted file, *krypton4*:    
> KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS  


Let's inspect the intercepted files:  
(They're pretty lengthy, so I put them in a gist to make sure the format was preserved.)  
[found files](https://gist.github.com/Mili-NT/e2063de816ad8513c911ea56c38f168d)  
I wrote a frequency analysis program found [here](https://github.com/Mili-NT/Misc-Toolkit/blob/master/EncryptionTools/FrequencyAnalysis.py)  
Which revealed the most common letter is S, since E is the most common letter, maybe S = E, which would make the encryption ROT-12.  
`cat krypton4 | tr 't-za-eT-ZA-E' 'a-zA-z'` returns:  
>KSoop uGSJw SoSIS oquMN rQnnK uNpvn tNMJS  

so, maybe not. However, manually mapping each letter according to its frequency works well.  
[python code here](https://gist.github.com/Mili-NT/54dee65e00df54255cd3a5977b1cae10)  

### Solution:   
So, that code returns:  
> WELLDONETHELEVELFOORPASSWORDISBROTE  

So I messed up the mapping a little bit, but we all got the point.  
>WELLDONETHELEVELFOURPASSWORDISBRUTE  


**Flag: BRUTE**
