# Level: CenturyFourteen
## Level Credentials: century13:i_authenticate_things
## Level Hint: *"The password for Century14 is the number of words within the file on the desktop."*

### Steps:
Absolutely easy, same solution as Level #4, but with the `-Word` flag enabled: `Get-ChildItem ..\Desktop\ | Get-Content | Measure-Object -Word | Select-Object Words`


**Flag: 755**
