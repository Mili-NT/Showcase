# Level: CenturyEight
## Level Credentials: century7:197
## Level Hint: *"The password for Century8 is in a readme file somewhere within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile"*

### Steps:
So we need to use `Get-ChildItem`, but starting at the directory level higher than the one we start in. We can use three flags to properly search for the password: `-Recurse` (to make it recursively search the tree), `-File` (to ensure we are only viewing files), and `-Filter` (to filter for the string “readme” as mentioned in the hint). All together that looks like: `Get-ChildItem ..\ -Recurse -File -Filter readme* | Get-Content`

**Flag: 7points**
