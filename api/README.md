# How to venv
1. python -m virtualenv virtual
2. cd into virtual
3. .\virtual\Scripts\activate
4. pip install X
5. pip freeze > requirements.txt

6. run app with python app.py

# windows (first time)
1. run powershell as admin, paste in: Set-ExecutionPolicy Unrestricted -Force
2. press enter
3. profit

# Heroku things
1. heroku login
2. git init
2. heroku create <app-name>
3. git add .
4. git commit things
5. heroku stach:set container <--- tells heroku your app is ran within a container
6. git push (to heroku!)

# notes 
1. https://dev.to/erenaspire7/deploying-a-dockerized-flask-app-to-heroku-5h7j