from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt



website = Flask(__name__)

website.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/database.db'
website.config['SECRET_KEY'] = 'pythonproject'
db = SQLAlchemy(website)
bcrypt = Bcrypt(website)

class User(db.Model, UserMixin):
    # db has 3 Columns, id is key(remember 11th grade), username max string 20 chars and can't be empty, same with password but will be converted to hash, username is unique
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True) 
    password = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
    #make a Registerform with LoginField, PasswordField and Submit Button, Passwordfield is hidden, min and max length for both, can't be empty
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "password"})
    submit = SubmitField("Register")
#check if username already exists, if throw Error and deny Registration
    def validation_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError("That Username already exists. Please choose a different one.")

class LoginForm(FlaskForm):
    #make a Loginform with LoginField, PasswordField and Submit Button, Passwordfield is hidden, fields can't be empty
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "username"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "password"})
    submit = SubmitField("Login")


@website.route("/") #Homepage
def home():
    return render_template("home.html")

@website.route("/login", methods=['GET', 'POST']) #Loginpage
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@website.route("/register", methods=['GET', 'POST']) #Registerpage
def register():
    form = RegisterForm()
    #set up Registration Database and hash password to make it secure, if valid send to Loginpage
    if form.validate_on_submit(): #for now doesn't get past validation, what the fucku why no worku
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("register.html", form=form)

@website.route("/admin") #Adminpage WIP
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    website.run(debug=True)