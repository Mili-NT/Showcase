# Level: CenturyFifteen
## Level Credentials: century14:755
## Level Hint: *"The password for Century15 is the number of times the word “polo” appears within the file on the desktop"*

### Steps:
Ok, so there is almost certainly a less quirky way to do this, but I came up with this lovely one-liner: 

`$i=0;foreach ($word in (-split(Get-ChildItem ..\Desktop\ | Get-Content))){if($word -eq 'polo'){$i++}};Write-Host $i`

This does is initialize a variable $i to 0 which is what we’re gonna use to count our instances of polo. We read the contents of the file on the desktop into an array, using the code from Level #10: `(-split(Get-ChildItem ..\Desktop\ | Get-Content)`, next we iterate over this array and use the `-eq` operator to check if each element is the word “polo”. If it is, it increments `$i`. Finally, we use Write-Host to print the number.

**Flag: 153**
