# Level: CenturySix
## Level Credentials: century5:61580
## Level Hint: *"The password for Century6 is the short name of the domain in which this system resides in PLUS the name of the file on the desktop."*

### Steps:
We can use `Get-CimInstance`, a newer replacement for `Get-WmiObject` cmdlet) to find the short domain like so: `Get-CimInstance Win32_ComputerSystem | Select-Object -Property Domain` which yields "underthewire.tech", but we only need "underthewire". By running `Get-ChildItem ..\desktop`, we get the other piece of the puzzle: a file named 3347

**Flag: underthewire3347**
