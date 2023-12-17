# app/app.py
from flask import Flask
from .controllers import prayer_bp

app = Flask(__name__)
app.register_blueprint(prayer_bp)


@app.route("/")
def hello():
    return "simple-prayer-service in ECS!"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
