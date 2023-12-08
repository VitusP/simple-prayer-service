# app/app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, This is Flask in ECS!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)
