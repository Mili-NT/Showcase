# Level: NatasEleven
## Level Credentials: natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK
## Level Description: *None*

### Steps:
The page has a box that allows you to change the background color, and an annoucement that says "Cookies are protected with XOR encryption"  
So, lets check out the code.  
We can see three (probably) important functions:   
**Encryption:**  
>function xor_encrypt($in) {  
>    $key = '<censored>';  
>    $text = $in;  
>    $outText = '';  
>  
>    // Iterate through each character  
>    for($i=0;$i<strlen($text);$i++) {  
>    $outText .= $text[$i] ^ $key[$i % strlen($key)];  
>    }  
>  
>    return $outText;    
>}  

**Load Data:**  
>function loadData($def) {  
>   global $_COOKIE;  
>   $mydata = $def;  
>   if(array_key_exists("data", $_COOKIE)) {  
>    $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);  
>    if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {  
>        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {  
>        $mydata['showpassword'] = $tempdata['showpassword'];  
>        $mydata['bgcolor'] = $tempdata['bgcolor'];    
>        }    
>    }    
>    }    
>    return $mydata;    
>}    
  
**Save Data:**  
>function saveData($d) {    
>   setcookie("data", base64_encode(xor_encrypt(json_encode($d))));    
>}    

So by intercepting the requests with Burp, we can get the end product of all of this (the value stored in the 'data' cookie):  
> ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSFlkrEBZZaAw  

This is the json encoded, xor encrypted, base64 encoded data. So, we'll need the *$key* variable from the *xor_encrypt* function to decode this.    
[Here](https://gist.github.com/Mili-NT/b9e40efb81d68415d1608a1c13085b6a) is the code I used to get the *$key* variable.   
This decodes the base64 encrypted data, and passes it into the *xor_encryption*.    
One thing that has changed in the *xor_encryption* function is that i've set the key as the default encoded value: *json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"));*   
Running this script returns: 
> qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq  

So our key is *qw8J*.    
Now, we need to get the data for the new cookie by passing in our key to the *xor_encrypt* function, and then do the reverse of all this to it: `base64_encode(xor_encrypt(json_encode($d))))`    
[Here](https://gist.github.com/Mili-NT/12ef311e7d96ed65b0331ab3813d4c70) is the script I wrote to decode it. This yields our new cookie data:  
> ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK  

### Solution: 
Now, all we have to do is intercept the HTTP request sent when the background is changed, swap the value stored in the *data* cookie with the new cookie data, and send it forward.  


**Flag: EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3**
