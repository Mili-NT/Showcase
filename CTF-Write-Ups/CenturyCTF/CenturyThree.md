# Level: CenturyThree
## Level Credentials: century2:10.0.14393.3866
## Level Hint: *"The password for Century3 is the name of the built-in cmdlet that performs the wget like function within PowerShell PLUS the name of the file on the desktop.”*

### Steps:
The cmdlet in question is obviously Invoke-WebRequest, and by running `Get-ChildItem ..\desktop`, we see a file named 443 on the desktop. invoke-webrequest + 443 = our flag

**Flag: invoke-webrequest443**
