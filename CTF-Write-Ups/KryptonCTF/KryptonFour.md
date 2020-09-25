# Level: KryptonFour
## Level Credentials: krypton4:BRUTE
## Level Description: *Good job! You more than likely used some form of FA and some common sense to solve that one. So far we have worked with simple substitution ciphers. They have also been ‘monoalphabetic’, meaning using a fixed key, and giving a one to one mapping of plaintext (P) to ciphertext (C). Another type of substitution cipher is referred to as ‘polyalphabetic’, where one character of P may map to many, or all, possible ciphertext characters. This level is a Vigenère Cipher. You have intercepted two longer, english language messages. You also have a key piece of information. You know the key length! For this exercise, the key length is 6. The password to level five is in the usual place, encrypted with the 6 letter key.*

### Steps:
Theres a hint and a few documents in the folder. Here is the hint:  
> Frequency analysis will still work, but you need to analyse it
> by "keylength".  Analysis of cipher text at position 1, 6, 12, etc
> should reveal the 1st letter of the key, in this case.  Treat this as
> 6 different mono-alphabetic ciphers...
>
> Persistence and some good guesses are the key!

So, a little backstory on how I actually went about this challenge.  
I really didn't want to look up hints on this one. I wanted to write my own vigenere cipher decoder.  
[So I did.](https://gist.github.com/Mili-NT/a7f19488cce063382c96110cb251688f)  
Its really bad code and only supports wordlist attacks (which worked on the example cipher for this level)  
I might make it support actual brute force attacks but... probably not.  
Anyway, I used [this website](https://www.boxentriq.com/code-breaking/vigenere-cipher) to do the actual brute forcing  
### Solution: 
Running the ciphertext through the decoder reveals the key is `FREKEY`

**Flag: CLEARTEXT**
