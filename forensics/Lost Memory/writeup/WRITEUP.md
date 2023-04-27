### Discovery
* `Secrets` folder immediately looks like what we should look into.
* Inside of it is a password-protected `passwords.zip` file.
* Other folders contain various things like images, videos, pdfs etc.

### Exploitation
* Idea is to build a wordlist for a dictionary attack.
* We can base it on some standard wordlist like `rockyou.txt`
* Extend the wordlist with keywords from all of the files.
* Also include information from metadata, for example location and creation dates of images.
* Run any cracking program using created wordlist.
* You should find a password `Italy2008`
* Using this password get a flag from `passwords.zip`