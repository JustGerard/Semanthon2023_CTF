### Discovery
* Inside the zip file there are folders: `books`, `memes` and two files: `employees.ods` and `passwords.kdbx`.
* `passwords.kdbx` is a KeePass database file, which is password protected. We can assume the flag is there.
* `employees.ods` contains rows of what looks like: `name;surname;password`.
* `books` folder contains two ebooks and `memes` folder contains six images.

### Exploitation
* We want to build a wordlist for a dictionary attack.
* We gather keywords from ebooks, images and their metadata.
* Also use information from `employees.ods` in the wordlist.
* The passwords there look like MD5 hashes, we can crack them using any online database, getting following results:

```5f4dcc3b5aa765d61d8327deb882cf99	md5	password
0d94d92e3dc096f64213a5b34fa9d098	md5	ironman
49116107dedf15cbbf495e68b17cc0bc	md5	lovecraft
7c6a180b36896a0a8c02787eeafb0e4c	md5	password1
9f05aa4202e4ce8d6a72511dc735cce9	md5	spiderman
```

* We input all of that info into our wordlist.
* Using any cracking software and our wordlist gain password for the `passwords.kdbx` file: `Lovecraft1`
* In KeePass file there is an entry called `flag` with url to password-protected pastebin.
* Password in this entry doesn't work.
* Checking edit history of this entry we can see the password changed.
* Old password works, getting us access to the flag in pastebin.