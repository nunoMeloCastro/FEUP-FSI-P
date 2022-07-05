# CTF realizado na Semana #4

To find the flag we first searched the source code hoping to find versions of applications or plug-ins, which we did find (WordPress 5.8.2 and WooCommerce 5.7.1).
Then, based on the nicknames exposed in the comment section we tried to find usernames registered in the platform and found that "admin" indeed was a username.
Finally, we went to Exploit Database to find a exploit related to that software (CVE-2021-34646). 
After obtaining the right one, we ran it and gained access to the admin page and on a private post there was the flag (flag{d491cab1d700b83b945df9386160dc4c}).
