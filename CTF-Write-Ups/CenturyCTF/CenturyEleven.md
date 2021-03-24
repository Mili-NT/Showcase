# Level: CenturyEleven
## Level Credentials: century10:pierid
## Level Hint: "*The password for Century11 is the 10th and 8th word of the Windows Update service description combined PLUS the name of the file on the desktop.*"

### Steps:
Now I did this two different ways. The first, and LAMEST way, is to use the `Get-CimInstance` cmdlet to search for services, `-Filter` those services to the name of the WUA service name “wuauserv”, then simply pipe it to `Select-Object` to get the description: `Get-CimInstance win32_Service -Filter "Name = 'wuauserv'" | Select-Object`. Then count the words, see that the 10th word is "windows" and the 8th is "updates", use `Get-ChildItem ..\Desktop` to view the file on the desktop named 110, and slam em together yourself.

OR, we use some tricks from other levels to do it all for us. 

Now, our base is still the same: `Get-CimInstance win32_Service -Filter "Name = 'wuauserv'" | Select-Object -Property Description`. But say, since we know the indexes (9 and 7 respectively), wouldn't it be useful to access it as an array? So let's first get the string value of the Description property: `Get-CimInstance win32_Service -Filter "Name = 'wuauserv'" | Select-Object -Property Description | foreach {$_.Description}`, then use `-split` to break it into an array of strings: `$arr=(-split(Get-CimInstance win32_Service -Filter "Name = 'wuauserv'" | Select-Object -Property Description | foreach {$_.Description}))`. So now we can do `$arr[9].ToLower()+$arr[7].ToLower()` and we can get "windowsupdate". But that's not quite good enough, we need to get the desktop filename as a string. We can do this with `Get-ChildItem ..\Desktop | Select-Object Name | foreach {$_.Name}`

So, put it all together on one happy line: `$arr=(-split(Get-CimInstance win32_Service -Filter "Name = 'wuauserv'" | Select-Object -Property Description | foreach {$_.Description}));$arr[9].ToLower()+$arr[7].ToLower()+(Get-ChildItem ..\Desktop | Select-Object Name | foreach {$_.Name})`

and sure enough, it gives us our flag.

**Flag: windowsupdates110**
