### Discovery

* We are given url to the site with content: ```I can't feel your GET!```

### Exploitation

* `GET` in response content suggests something with HTTP methods.
* Trying to send `POST` gives following result:

```
curl -X POST https://cant-feel-my-get.semanthon.com/
I can't feel your POST!
```

* So I tried sending a custom HTTP method `FLAG` and got the flag:

```
curl -X FLAG https://cant-feel-my-get.semanthon.com/
FLAG? I love it! Here is your flag: flag{8Ut_1_L0V3_1T}
```