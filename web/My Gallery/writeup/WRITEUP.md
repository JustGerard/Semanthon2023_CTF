### Discovery

* We are given url to the site with list of images which we can click and look at.
* Site url ends with `/images/` which suggests something with path.
* Looking at the response headers we can see that the server is `nginx`.

### Exploitation

* Taking into account suspection of path-related vulnerability and that `nginx` is the server we can find a popular `path traversal` vulnerability in badly configured server.
* To test this we can simply try to access higher level directory and assume that usually flag is located in `flag.txt` file. For example: 
    * https://my-gallery.semanthon.com/images../flag.txt
    * https://my-gallery.semanthon.com/flag.txt
* Both of those would give us the flag.