# Level: KryptonTwo.md
## Level Credentials: krypton2:ROTTEN
## Level Description: *The password for level 3 is in the file krypton3. It is in 5 letter group ciphertext. It is encrypted with a Caesar Cipher. Without any further information, this cipher text may be difficult to break. You do not have direct access to the key, however you do have access to a program that will encrypt anything you wish to give it using the key. If you think logically, this is completely easy.*    

### Steps:
After linking the files to a new temporary directory, I examined the cipher text using `cat ciphertext`:
> GNGZFGXFEZX

We also have an executable that encrypts things. I think an easy way would be to use:
`echo "a b c d e f g h i j k l m n o p q r s t u v w x y z" > test.txt`

to echo the alphabet into a text file, then encrypt the text file and see what shifts to what.  
`/krypton/krypton2/encrypt test.txt && cat ciphertext` returns:  
> MNOPQRSTUVWXYZABCDEFGHIJKL   

This is an ezpz rotation cipher. A is the first letter of the alphabet and it's replaced with M, the 13th letter of the alphabet. This means the encryption is ROT12.  
So, that's very easily decrypted using a slightly modified version of the translate command I used in Bandit level 11.    
### Solution:  
Original command intended for ROT13:    
> cat data.txt | tr ‘n-za-mN-ZA-M’ ‘a-zA-Z’  

New command for ROT12:  
> cat /krypton/krypton2/krypton3 | tr 'm-za-lM-ZA-L' 'a-zA-Z'  

This returns the flag!  


**Flag: CAESARISEASY**
