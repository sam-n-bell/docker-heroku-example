# How to venv
# python -m virtualenv virtual
# cd into virtual
# .\virtual\Scripts\activate
# pip install X
# pip freeze > requirements.txt

# run app with python app.py

# windows (first time)
# run powershell as admin, paste in: Set-ExecutionPolicy Unrestricted -Force
# press enter


# Heroku things
1. heroku login
2. git init
2. heroku create <app-name>
3. git add .
4. git commit things
5. heroku stach:set container <--- tells heroku your app is ran within a container
6. git push (to heroku!)

# urls 
1. https://dev.to/erenaspire7/deploying-a-dockerized-flask-app-to-heroku-5h7j