from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

emails_to_display = []
emails = []

@app.route('/')
def index():
    return render_template("index.html", emails=emails)

@app.route('/greeting', methods = ["POST"])
def greeting():
    email = request.form.get("email")
    today = date.today()

    if not email:
        error_statement = "Поле вітання пусте!"
        return render_template("index.html", error_statement=error_statement, email=email)
        

    for em in emails:
        if (email == em):
           #error_statement = "Привіт", email, "вже бачилися!"
            error_statement = "Привіт {} вже бачилися!".format(email)
            return render_template("index.html", error_statement=error_statement, email=email)
            
    emails.append(email)
    emails_to_display.append(f" {email}   ||  {today}")
    return render_template("greeting.html", email=email)

@app.route('/list')
def list():
    return render_template("list.html", emails=emails_to_display)