from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
  return {"secret": "not very secret"}

if __name__ == '__main__':
  # Heroku runs your app depending on the ports available. 
  # In several instances, It might not assign the port 5000 which means our app crashes. 
  # In order to fix this error, we’d add this to our “app.py”
  # This tells our app to use the port assigned by heroku, if not, use 5000.
  port = int(os.environ.get('PORT', 5000))
  print(f'Running on port {port} {type(port)}')
  app.run(host = '0.0.0.0', port = port)

