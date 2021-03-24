# Level: CenturyThirteen
## Level Credentials: century12:secret_sauce
## Level Hint: *"The password for Century13 is the description of the computer designated as a Domain Controller within this domain PLUS the name of the file on the desktop.”*

### Steps:
First, we need to get the name of the domain controller using `Get-ADDomainController` and use the `Select-Object` cmdlet to get the name. 
I initially tried to pipe this directly into `Get-ADComputer` to get the description, but that obviously failed as I was trying to pipe in an object. 
I had to pick out the property I wanted to return as a string (`name` in this case), and THEN piping that into `Get-ADComputer` with the `-Properties Description` flag, and finally using `Select-Object` to isolate that. Now from there I just convert the description into a string, do the same for the filename found by `(Get-ChildItem ..\Desktop | Select-Object Name)`, and concatenate them. 

All in all, an actually pretty neat command: `Get-ADDomainController | Select-Object name | foreach {$_.name} | Get-ADComputer -Properties Description | Select-Object Description | foreach {$_.Description+(Get-ChildItem ..\Desktop | Select-Object Name | foreach {$_.Name})}`

**Flag: i_authenticate_things**
