# Level: CenturyTwo
## Level Credentials: century1:century1
## Level Hint: *"The password for Century2 is the build version of the instance of PowerShell installed on this system"*

### Steps:
This means all we have to do is use `$PSVersionTable` to view some basic information about PowerShell, including the build version:
```
Name                           Value
----                           -----
PSVersion                      5.1.14393.3866
PSEdition                      Desktop
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0...}
BuildVersion                   10.0.14393.3866
CLRVersion                     4.0.30319.42000
WSManStackVersion              3.0
PSRemotingProtocolVersion      2.3
SerializationVersion           1.1.0.1
```

**Flag: 10.0.14393.3866**
