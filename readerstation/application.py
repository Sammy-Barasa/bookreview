import os
import requests
import csv
import flask_login


#import .import*

from flask import Flask, session, redirect,render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# from flask_login import LoginManager,login_required,user_loader,request_loader

app = Flask(__name__)

# Check for environment variable

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
app.config['DATABASE_URL'] = "path_to_db"
engine = create_engine(os.getenv("DATABASE_URL"))
db= scoped_session(sessionmaker(bind=engine))
# login = LoginManager(app)

#main function to insert books


@app.route("/")
# @login_required
def index():
    return redirect("/api")


@app.route("/bookpage")
def bookpage():
    data=[]
    with open('books.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        counter = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
        
            else:
                data.insert(counter,row)
                counter = counter+1
                line_count += 1
    return render_template("user2.html",data=data)
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")

        #enable flask login parameters
        #login_manager=LoginManager()
        #initialize every flask ogin requirement
        #get infomation from loginform
        #authenticate form information
        #form=LoginForm()  
        #redirect to user template page
    log="logged as:"
        
    return render_template("user2.html",message=log)
@app.route("/register", methods=["GET","POST"])
def reister():
    
    if request.method=="GET":
        return render_template("register.html")
    else:
        name=request.form.get("name")
        gender=request.form.get("gender")
        password=request.form.get("password")

        #geting form info
       # if not name or gender or password:
       #         message="please fill fields"
       #         return render_template("register.html",message=message)
        
                #making sure no empty field
        return render_template("login.html")
        #else:
         #   def user():
         #       name=request.form.get("name")
          #      gender=request.form.get("value")
         #       password=hash(request.form.get("password")
        #add User to database with SQLAformat

        #after user is added:
        # send back to enter 
        #        return redirect("login.html")

@app.route("/api")
def api():
        
    #KEY="NxHR0wNCivzIEefBextQ"(you cannot represent keys)
    #res = requests.get("https://www.goodreads.com/book/review_counts.json?isbns=1594489505&key=NxHR0wNCivzIEefBextQ")
    res = requests.get("https://www.goodreads.com/book/review_counts.json",params={"isbns":1594489505,"key":"NxHR0wNCivzIEefBextQ"})
    a=print(res.json())


    return render_template("user2.html", message=a)  
