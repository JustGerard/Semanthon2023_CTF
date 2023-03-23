import pickle
from io import BytesIO

from flask import Flask, render_template, send_file, request

app = Flask(__name__)


class Character:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self) -> BytesIO:
        buffer = BytesIO()
        pickle.dump(self, buffer)
        buffer.seek(0)
        return buffer


def load_character(file) -> dict:
    pass


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/save-character")
def save_character():
    character = Character(**request.form)
    saved_character = character.save()
    return send_file(
        saved_character,
        as_attachment=True,
        download_name="character.backup",
        mimetype="application/octet-stream",
    )


@app.post("/load-character")
def load_character():
    file = request.files["file"]
    if not file:
        return "Invalid file", 400
    try:
        character = pickle.loads(file.read())
        print(character)
        return character.__dict__, 200
    except Exception as e:
        print(e)
        return "Invalid file", 400


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
