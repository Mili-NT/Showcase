# Upgrades (2021 Uni CTF) Writeup
## Materials:
- upgrades.pptm

## Steps:

The PowerPoint is a short 4 slide presentation. By opening it and checking the macros viewer in PowerPoint, we can see there's one macro: `OnSlideShowPageChange()`.


When attempting to edit the macro in PowerPoint Visual Basic IDE, it prompts for a password to access the Visual Basic project. My first approach was to try and bypass the password protection by patching the `ID`, `CMG`, `DPG`, and `GC` attributes to the ones obtained from a non-protected project.

This turned out to be a bit of a hassle, and I opted to use [OfficeMalScanner.exe](http://www.reconstructer.org/code.html) to extract the Visual Basic code without needing to have the password. There are two files that are extracted: `module1` and `slide1`.


```vb
Attribute VB_Name = "Module1"
Private Function q(g) As String
q = ""
For Each I In g
q = q & Chr((I * 59 - 54) And 255)
Next I
End Function
Sub OnSlideShowPageChange()
j = Array(q(Array(245, 46, 46, 162, 245, 162, 254, 250, 33, 185, 33)), _
q(Array(215, 120, 237, 94, 33, 162, 241, 107, 33, 20, 81, 198, 162, 219, 159, 172, 94, 33, 172, 94)), _
q(Array(245, 46, 46, 162, 89, 159, 120, 33, 162, 254, 63, 206, 63)), _
q(Array(89, 159, 120, 33, 162, 11, 198, 237, 46, 33, 107)), _
q(Array(232, 33, 94, 94, 33, 120, 162, 254, 237, 94, 198, 33)))
g = Int((UBound(j) + 1) * Rnd)
With ActivePresentation.Slides(2).Shapes(2).TextFrame
.TextRange.Text = j(g)
End With
If StrComp(Environ$(q(Array(81, 107, 33, 120, 172, 85, 185, 33))), q(Array(154, 254, 232, 3, 171, 171, 16, 29, 111, 228, 232, 245, 111, 89, 158, 219, 24, 210, 111, 171, 172, 219, 210, 46, 197, 76, 167, 233)), vbBinaryCompare) = 0 Then
VBA.CreateObject(q(Array(215, 11, 59, 120, 237, 146, 94, 236, 11, 250, 33, 198, 198))).Run (q(Array(59, 185, 46, 236, 33, 42, 33, 162, 223, 219, 162, 107, 250, 81, 94, 46, 159, 55, 172, 162, 223, 11)))
End If
End Sub
```
It's rather obvious here that all the strings are obfuscated, so I rewrote the `q()` function in python to deobfuscate any particular string:
```python
def deobfuscate(array_of_ints):
    return ''.join([chr((i * 59-54) & 255) for i in array_of_ints])
```
Now, I think I can largely ignore the nested array `j`, as the important bits will likely be around the `StrComp()` function, so I first deobfuscated those strings:
```python
def deobfuscate(array_of_ints):
    return ''.join([chr((i * 59-54) & 255) for i in array_of_ints])
all_strcomp_arrays = [
    [81, 107, 33, 120, 172, 85, 185, 33],
    [154, 254, 232, 3, 171, 171, 16, 29, 111, 228, 232, 245, 111, 89, 158, 219, 24, 210, 111, 171, 172, 219, 210, 46, 197, 76, 167, 233],
    [215, 11, 59, 120, 237, 146, 94, 236, 11, 250, 33, 198, 198],
    [59, 185, 46, 236, 33, 42, 33, 162, 223, 219, 162, 107, 250, 81, 94, 46, 159, 55, 172, 162, 223, 11]
]
for arr in all_strcomp_arrays:
    print(deobfuscate(arr))
```
Which does indeed show our flag, as well as `username`, `WScript.Shell`, and `cmd.exe /C shutdown /S`.
