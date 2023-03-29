#!/usr/bin/env python
import re

from flask import Flask, request

app = Flask(__name__)

FLAG = "flag{7h1nK1n9_a80U7_P1nK_3l3PhaN72}"
MIN_SCORE = 2137
CERTIFICATE = """MIIC5DCCAcwCAQEwDQYJKoZIhvcNAQELBQAwNzEWMBQGA1UEAwwNQW5kcm9pZCBEZWJ1ZzEQMA4G
    A1UECgwHQW5kcm9pZDELMAkGA1UEBhMCVVMwIBcNMjMwMzI5MTg0MTI0WhgPMjA1MzAzMjExODQx
    MjRaMDcxFjAUBgNVBAMMDUFuZHJvaWQgRGVidWcxEDAOBgNVBAoMB0FuZHJvaWQxCzAJBgNVBAYT
    AlVTMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAi+ko05eKJroFJsSBOeMy0dafkWQc
    Ila6GTiqFH4q+3ZyKgk1T3PsN+MiA2syQgMLVCGB9KNNIJ9nqpj6V+y202FNtPBoeHuK5z3IYx0a
    r3u6UeiSTA7qN4O6xYIdmx7fJCzLvyO0v4c+Vebh/RockoLsrO2Ei/hcZ9HYcxIYkC8jbwbbLvT0
    9ux1D4iVgVw8uUiYdEkUu/+INBzVcZI67zbBtkXH2NW/UDwOuYmOMiqnw0pVhtjyKC1P0qMThR1S
    hPKUX3H4QAj1AQn6VxoNxGhqKI7uoyhkM2h2Pq/thRFFth21B+QKkIRuemxFWAh1kErwF7Wv9i8G
    a/WHPp0D/wIDAQABMA0GCSqGSIb3DQEBCwUAA4IBAQAAPayvwruA/ZhG9dEU8rMhUc153dx6HjCs
    mUnDfUCQaZ6/nEE+CCmxd9d63mfJiySJGeRHFNRUYeonjJFFx9GyHPXB7VrsLqka07kaBsgMu/Qk
    SAfY7/qwwVtHvzWUWY7Qo62AHo0bzm016pjtSTyy1R6tB9O7gA6Q/QPTEsHKRqs08WOlFgnQ6gCT
    Cg30X6trjHwX11UIP5H/vUg/ogAJ5fT53uuYxJcUZR7Aw5isg5nLiTMnl7+yuFc8sh4DYG1fU3zG
    MZwDu6GN72CiQWcKRxZzYrxYAdKiQ+7qa+k9g3wWjlFte+v3jyXON+C9eMDMaxfuIgMstg8+fkg/
    01xr"""

CERTIFICATE = re.sub(r"\s+", "", CERTIFICATE)


def _is_valid_cert(certificate: str) -> bool:
    user_cert = re.sub(r"\s+", "", certificate)
    return user_cert == CERTIFICATE


@app.post("/validate-cert")
def validate_cert():
    try:
        certificate = request.json["cert"]
        if _is_valid_cert(certificate):
            return {}, 200
    except Exception as _:
        pass
    return {"status": "No hacking!!!"}, 400


@app.post("/validate-score")
def validate_score():
    try:
        data = request.json
        if not _is_valid_cert(data["cert"]):
            raise Exception("No hacking!!!")
        score = data['score']
        if score < MIN_SCORE:
            raise Exception("You lost!!!")
        return {"status": f"You won!!!\n{FLAG}"}, 200
    except Exception as e:
        return {"status": str(e)}, 400


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
