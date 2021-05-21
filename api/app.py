from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
  return {"secret": "not very secret"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug = True, host = port)