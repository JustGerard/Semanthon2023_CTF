### Discovery

* We are given an `apk` file which is an Android application.
* Running it on an emulator or phisical device we see a "game", in which we have to guess which button is correct 2023 times.
* Knowing we can't possibly beat the game we want to analyze the network traffic that it sends.
* In the network traffic we can see that when running the game there is a request sent to the server, with json containing `cert` field to `/validate-cert` endpoint.
* This suggests that we need to send this certificate to keep our application `valid` for the server.
* No other requests are being send while pushing the buttons.
* We need to decompile the application, with for example `apktool` and look into it.
* There is no flag in the decompiled code.
* We can see that there is a constant called `MIN_SCORE`, which suggests that there is a minimal score that we need to achive in order to send it to the server.
* In the `WrongGuess` function current score is compared with `MIN_SCORE` and if it's lower you get `"You lost!!!"` text.



### Exploitation
* We can modify the `MIN_SCORE` value to for example `2` and recompile the application, while also keeping the original certificate or modifing the code to always send the original one.
* Then when running the modified application we can analyze the traffic of sending the `/validate-score` requests.
* In those requests we can see three values: `score`, `validity` and `cert`.
* `score` and `cert` are obvious.
* Looking at how `validity` changes with score value, we can see that it's just a substring of `cert` shifted by `score` value.
* Knowing all of this we can prepare a request with score of our choosing.
* Following curl would give us a flag:

```
curl --location 'https://the-game.semanthon.com/validate-score' \
--header 'Content-Type: application/json' \
--data '{
    "cert": "MIICljCCAX4CAQEwDQYJKoZIhvcNAQELBQAwETEPMA0GA1UEAwwGR2VyYXJkMB4XDTIzMDQwOTIx\nNDEzM1oXDTQ4MDQwMjIxNDEzM1owETEPMA0GA1UEAwwGR2VyYXJkMIIBIjANBgkqhkiG9w0BAQEF\nAAOCAQ8AMIIBCgKCAQEAgD6G3YsSpSudfMviIc4SrEUGDiUrkm7alsU17dT8Qu+I575g3xhZ3J4t\neTyMtvSQGFCk6wPmDtzVuvWMgdOa\/dkpTWrIS3WPlidT+uIovF\/Rc4iNgUYoqXGeO5wqUKtoTEz+\nbndwCKfBZpqeCdOuKI2tferXBDBIUP4UrTO40zo7r4\/bENg+Xb\/FfFRWwqD5q1t81+2kVWCr3Ge3\nH\/jWKqTOZBOwnk4f+E6JkTwskU9gdSB4YTls2X+ca2UC\/YpqwJXPQ0cG4HErwYcJrikSfJqIiPUc\nXG0wbr9D8nO7wVELs4tFbEGX5rmcHXiBqLY\/Y81KIBIaNMvWKqDKW\/P6fwIDAQABMA0GCSqGSIb3\nDQEBCwUAA4IBAQBHAiJpEsO6L94dK9x9cxWAyfcuU4nhMWFKTvFjzgZQyp6E7JMZrqn8V7q9ybm1\n7ucn3Xc5jxvHr\/M8dqdoMOF4mjqKlEGhArQN90X0rJlJXXfA5k+dS3VRGY6ajqytPhf+qohpCF0P\nHwTpkrOeWTpZf6oLW1CLIUxpaSalh0ox+f3827yvEjl+CwRUeTho4AhwsfLcPO6pSI7my5W53N\/k\nbD\/pnpdKY5yKgjwmmfyQy4YFiYixTkg68fRSD55eGu+lPKmnHq6AzSC64PTkQj05NFMIl7h1fl2n\nqs8pDHCRcWYVH1bWVUcQhWKxVyZRHS\/TGLe936+2k7WSGrqygO0p",
    "score": 2023,
    "validity": "NAQELBQAwETEPMA0GA1UEAwMIICljCCAX4CAQEwDQYJKoZIhvc"
}'
```