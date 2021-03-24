# Level: CenturyFour
## Level Credentials: century3:invoke-webrequest443
## Level Hint: *"The password for Century4 is the number of files on the desktop."*

### Steps:
We can simply use the same command used to view a file on the Desktop last level, and pipe it through `Measure-Object` to count it, like so: `Get-ChildItem  ..\desktop | Measure-Object`, and additionally through `Select-Object Count` if you're feeling fancy.

**Flag: 123**
