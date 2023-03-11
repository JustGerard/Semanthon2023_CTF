from flask import Flask, render_template, request

app = Flask(__name__)

with open("passwords.txt") as f:
    passwords = [x.strip() for x in f.readlines()]

pre_final_password = passwords[-2]
final_password = passwords[-1]


@app.route("/")
def index():
    return render_template("index.html", password=passwords[0], count=1)


@app.route("/", methods=["POST"])
def check_password():
    text = request.form['text'].strip()
    if text not in passwords:
        return render_template("index.html", password=passwords[0], count=1, error="Incorrect! Try again!")
    if text in [pre_final_password, final_password]:
        flag = "flag{" + passwords[-1] + "}"
        return render_template("success.html", password=flag)
    password_index = passwords.index(text)
    return render_template("index.html", password=passwords[password_index + 1], count=password_index + 2)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
