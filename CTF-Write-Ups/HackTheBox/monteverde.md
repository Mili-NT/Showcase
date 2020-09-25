# Monteverde Writeup
## Enumeration
```
53/tcp   open  domain?
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2020-04-27 23:51:13Z)
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: MEGABANK.LOCAL0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
```
Doing some enumeration LDAP nets us some usernames:
```
Guest
AAD_987d7f2f57d2
mhope
SABatchJobs
svc-ata
svc-bexec
svc-netapp
dgalanos
roleary
smorgan
```
I made a list of potentially easy passwords: blank, admin, the username, etc. and attempted to authenticate each.
We got a hit on `SABatchJobs:SABatchJobs` and can use it's privileges to enumerate the SMB shares. 
## Initial Compromise
The standard ones like `IPC$` are there, but more interesting is `Users$`. We can use smbclient to dig through the user shares, and in `mhope`'s share, we find an XML file with credentials, ezpz.
We can do open a reverse *powershell* shell as `mhope` and nab the user flag. Doing AD privilege enumeration shows we are part of `MEGABANK\Azure Admins` 
## PrivEsc
We can connect to the Azure AD instance *on localhost* and perform a DCSync attack to get us credentials for Administrator, which we can in turn use to authenticate to the non-local AD instance as the Domain Admin.

Another fun, easy AD box
