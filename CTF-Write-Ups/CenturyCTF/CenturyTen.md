# Level: CenturyTen
## Level Credentials: century9:696
## Level Hint: *"The password for Century10 is the 161st element within the file on the desktop."*

### Steps:
We first see what the file on desktop is with `Get-ChildItem ..\Desktop\` and load the file with `Get-Content`, and use the `-split` function to split the resulting string into an array. Then we access index 160 of that array, because arrays are zero-indexed. The resulting command was not near as bad as I thought it would be: `(-split(Get-ChildItem ..\Desktop\ | Get-Content))[160]`

**Flag: pierid**
