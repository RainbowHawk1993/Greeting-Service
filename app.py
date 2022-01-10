from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Model of Database
class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    #Function to return a string, part of the model
    def __repr__(self):
        return '<Name %r>' % self.id

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
            error_statement = "Привіт {} вже бачилися!".format(email)
            return render_template("index.html", error_statement=error_statement, email=email)
            
    emails.append(email)
    emails_to_display.append(f" {email}   ||  {today}")
    return render_template("greeting.html", email=email)

@app.route('/list')
def list():
    return render_template("list.html", emails=emails_to_display)

@app.route('/list2', methods=['POST', 'GET'])
def list2():
    if request.method == "POST":
        person_name = request.form['name']
        new_person = List(name = person_name)

        #Adding info to database
        try:
            db.session.add(new_person)
            db.session.commit()
            return render_template("greeting.html", email=person_name)
        except:
            error_statement = "Привіт {} вже бачилися!".format(person_name)
            return render_template("greeting.html", error_statement=error_statement)
    else:
        people = List.query.order_by(List.date_created)
        return render_template("list2.html", people = people)