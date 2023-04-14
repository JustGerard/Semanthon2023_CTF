#!/usr/bin/env python
import re
import string
from collections import deque

from flask import Flask, request

app = Flask(__name__)

FLAG = "flag{7h1nK1n9_a80U7_P1nK_3l3PhaN72}"
MIN_SCORE = 2023
CERTIFICATE = """MIICljCCAX4CAQEwDQYJKoZIhvcNAQELBQAwETEPMA0GA1UEAwwGR2VyYXJkMB4XDTIzMDQwOTIx
NDEzM1oXDTQ4MDQwMjIxNDEzM1owETEPMA0GA1UEAwwGR2VyYXJkMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAgD6G3YsSpSudfMviIc4SrEUGDiUrkm7alsU17dT8Qu+I575g3xhZ3J4t
eTyMtvSQGFCk6wPmDtzVuvWMgdOa/dkpTWrIS3WPlidT+uIovF/Rc4iNgUYoqXGeO5wqUKtoTEz+
bndwCKfBZpqeCdOuKI2tferXBDBIUP4UrTO40zo7r4/bENg+Xb/FfFRWwqD5q1t81+2kVWCr3Ge3
H/jWKqTOZBOwnk4f+E6JkTwskU9gdSB4YTls2X+ca2UC/YpqwJXPQ0cG4HErwYcJrikSfJqIiPUc
XG0wbr9D8nO7wVELs4tFbEGX5rmcHXiBqLY/Y81KIBIaNMvWKqDKW/P6fwIDAQABMA0GCSqGSIb3
DQEBCwUAA4IBAQBHAiJpEsO6L94dK9x9cxWAyfcuU4nhMWFKTvFjzgZQyp6E7JMZrqn8V7q9ybm1
7ucn3Xc5jxvHr/M8dqdoMOF4mjqKlEGhArQN90X0rJlJXXfA5k+dS3VRGY6ajqytPhf+qohpCF0P
HwTpkrOeWTpZf6oLW1CLIUxpaSalh0ox+f3827yvEjl+CwRUeTho4AhwsfLcPO6pSI7my5W53N/k
bD/pnpdKY5yKgjwmmfyQy4YFiYixTkg68fRSD55eGu+lPKmnHq6AzSC64PTkQj05NFMIl7h1fl2n
qs8pDHCRcWYVH1bWVUcQhWKxVyZRHS/TGLe936+2k7WSGrqygO0p
"""

CERTIFICATE = re.sub(r"\s+", "", CERTIFICATE)


class MyException(Exception):
    pass


alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits


def _is_valid_cert(certificate: str) -> bool:
    user_cert = re.sub(r"\s+", "", certificate)
    return user_cert == CERTIFICATE


@app.get("/")
def healthcheck():
    return "", 200


@app.post("/validate-cert")
def validate_cert():
    try:
        certificate = request.json["cert"]
        if _is_valid_cert(certificate):
            return "", 200
    except Exception as _:
        pass
    return "No hacking!!!", 400


def _is_valid_validity_string(validity_string: str, score: int) -> bool:
    if len(validity_string) != 50:
        return False
    deq = deque(validity_string)
    deq.rotate(score * -1)
    parsed_str = ''.join(deq)
    return parsed_str == CERTIFICATE[:50]


@app.post("/validate-score")
def validate_score():
    try:
        data = request.json
        if not _is_valid_cert(data["cert"]):
            raise MyException("No hacking!!!")
        score = data['score']
        if score < MIN_SCORE:
            raise MyException("You lost!!!")
        if not _is_valid_validity_string(data["validity"], score):
            raise MyException("No hacking!!!")
        return f"You won!!!\n{FLAG}", 200
    except MyException as e:
        return str(e), 400


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=8000, host="0.0.0.0")
