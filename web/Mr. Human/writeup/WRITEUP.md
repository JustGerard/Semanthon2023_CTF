### Discovery

* We are given url to the site with what looks like a captcha.
* Site suggests that we need to input the captcha 744 times.
* Letters of the password are "obfuscated" in HTML.

### Exploitation


We can automate it using any language and library to:
* Get the letters from HTML.    
* Compose captcha string.
* Send request to the server.
* Print resulting HTML.
* Repeat until we get the flag.