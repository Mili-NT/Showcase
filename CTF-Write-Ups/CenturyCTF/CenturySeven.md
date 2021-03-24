# Level: CenturySeven
## Level Credentials: century6:underthewire3347
## Level Hint: *"The password for Century7 is the number of folders on the desktop"*

### Steps:
Extremely easy, all we have to do is take our trusty `Get-ChildItem ..\Desktop\` command, apply the `-Directory` flag to only count directories, and pipe it through `Measure-Object` to count it: `Get-ChildItem ..\Desktop\ -Directory | Measure-Object`

**Flag: 197**
