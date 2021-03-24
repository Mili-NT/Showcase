# Level: CenturyTwelve
## Level Credentials: century11:windowsupdates110
## Level Hint: *"The password for Century12 is the name of the hidden file within the contacts, desktop, documents, downloads, favorites, music, or videos folder in the user’s profile."*

### Steps:
Easy use of `Get-ChildItem`, but we will want to use the `-Recurse` flag to recursively search, the `-File` flag to specify that we are looking for a file, and the `-Hidden flag` to search for hidden files. We will also want to `-Exclude` the AppData folder, because it contains many hidden files. Also I muted the errors because they were in the way, as one does: `Get-ChildItem -Recurse -File -Hidden -erroraction 'silentlycontinue' -Exclude AppData ..`

**Flag: secret_sauce**
