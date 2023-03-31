#!/usr/bin/env python
import re
import string

from flask import Flask, request

app = Flask(__name__)

FLAG = "flag{7h1nK1n9_a80U7_P1nK_3l3PhaN72}"
MIN_SCORE = 2023
CERTIFICATE = """MIICljCCAX4CAQEwDQYJKoZIhvcNAQELBQAwETEPMA0GA1UEAwwGR2VyYXJkMB4XDTIzMDMzMTE1
MDA1OVoXDTQ4MDMyNDE1MDA1OVowETEPMA0GA1UEAwwGR2VyYXJkMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAoHRDpRAJgIIYWi8EBxmKJroINPDpYzcUPkPI8RipUaMi9esWb4hqT2QA
ezF8X2wiH4Osv2d1/vgplnA5sgLPod52XCQXzNnIJux2d7H6raUXk5EUb95sWBlYfhRsr73J4FZd
v0YXG8Ug/V2bZ9um7kX/U7dXCg5WPAdhzbIW+lekukro5v4T0QYfne+d21DvImAEbw87MJ6sAZPp
aB2+WABy2zlQ7UVGe/+0+VkE/jtnInfyplwPkKtz3QGDyCpzEAc3rR5eeCbSp//EOdpoZleqttMa
YavyNcWYyFvVw7+i140AfFbRN8UV4f8eUaSMtuPmEUMR+Db6ITd8gk6h3wIDAQABMA0GCSqGSIb3
DQEBCwUAA4IBAQBtQSd5H2iz+mHjCv4icP6GTsVWs23W2mcuqHQyCN8SgVJ/1H4NUcnNYek7oG4+
ckxe4i36V+B4vHQpwyS0wumv+g6Io6VT5leoL3NyKTcCkLcCjC2gzgBml/UaFfyBmNGnlvDunq0N
8qXCeoFjvUGqq0Q6L//q0yq8B8mQNZOryxB+b+37h45rkhfJONxzsQ649Hen7x6u2IziioyJ8kHV
eXea+VDVxgsWXz608ND0FAi9FL2ofW5B3/R+gR/KikAAARfJMOjdGiEvD7AX+JoRudG2oREdHHL7
4adsmD8jsYsRkB2rU23Ymp8bXEJvFJF6N7hYGKiFbWr2XL8ihF4o
"""

CERTIFICATE = re.sub(r"\s+", "", CERTIFICATE)


class MyException(Exception):
    pass


alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits


def shift_string_left(text, shift):
    return text[shift:] + text[:shift]


def _is_valid_cert(certificate: str) -> bool:
    user_cert = re.sub(r"\s+", "", certificate)
    return user_cert == CERTIFICATE


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
    parsed_str = shift_string_left(validity_string, score)
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
    app.run(debug=True, threaded=True)
