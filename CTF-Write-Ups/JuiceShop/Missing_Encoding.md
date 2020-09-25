# Challenge: Missing Encoding
## Challenge Description: *Retrieve the photo of Bjoern's cat in "melee combat-mode".*

### Steps: 
Since the description mentions photos, we're probably gonna be dealing with the photo wall section.
Upon visiting the page, there are two images and one broken image. Inspecting the source reveals an asset link, but visiting it doesn't show the image. Sending a requests to the asset URL stored in the html shows why-- there are characters which are not percet encoded in the url. Specifically #s which are html anchor tags. Encoding them and sending the requests returns the cat picture.

### Solution:
View request, verify encoding
