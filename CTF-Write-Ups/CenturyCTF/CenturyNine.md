# Level: CenturyNine
## Level Credentials: century8:7points
## Level Hint: *"The password for Century9 is the number of unique entries within the file on the desktop."*

### Steps:
All we actually need to do is read the file with `Get-Content`, pipe it into the `Get-Unique` cmdlet (which eliminates duplicates), then count them with `Measure-Object` like so: `Get-ChildItem ..\Desktop\ | Get-Content | Get-Unique | Measure-Object`

**Flag: 696**
