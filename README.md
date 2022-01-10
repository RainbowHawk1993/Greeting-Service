# Greeting-Service

To launch application locally, open Bash terminal (using Git Bash for example) in directory where `app.py` is.

Then you want to turn on the virtual environment using the following commands: 

```
python -m venv virtual
source virtual/bin/activate
```

Make sure that you have flask installed, if you don't, run `pip install flask`
Also you'll need SQLAlchemy, to get it run `pip install flask-sqlalchemy`

After this, you should be able to execute `flask run` and HTTP server will start.

The server runs on port 5000, so typing in 127.0.0.1:5000 in your web-browser should take you to the web-app.

Or alternatively you can just view this app online on https://greetingservice5.herokuapp.com/
