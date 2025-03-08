#find a way to handle configuration files


from flask_bcrypt import Bcrypt
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, url_for, redirect, render_template, request, flash, session
from flask_session import Session
from flask_wtf import CSRFProtect
from forms import ObesityPredictionForm, RegistrationForm, LoginForm
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import redis
import requests
from flask_mail import Mail,Message



app = Flask(__name__)




app.config['SECRET_KEY']='86cf016117fc3c20024cbece2419d4ce'

#mail automation configs
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = 'wibx kvun yjpe gdgp'
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

# FastAPI Endpoint
FASTAPI_URL = "http://127.0.0.1:8000/predict/"

# Session Configuration
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'flask_session:'
app.config['SESSION_REDIS'] = redis.Redis(host='localhost', port=6379, db=0)

Session(app)
load_dotenv()

#DB configurations
import os
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)



class User(db.Model):
    __tablename__='Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

with app.app_context():
    db.create_all()


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/about us')
def about():
    pass

@app.route('/contact')
def contact():
    pass

@app.route('/service')
def services():
    return render_template('services.html')

@app.route('/predictions')
def predictions():
    return render_template('predictions.html')

@app.route('/obesity', methods=['GET', 'POST'])
def obesity_predict():
    form = ObesityPredictionForm()
    prediction = None

    if request.method == "POST" and form.validate_on_submit():
        age = request.form.get("age")
        height = request.form.get("height")
        weight = request.form.get("weight")
        bmi = request.form.get("bmi")

        input_data = {
            "Age": int(age),
            "Height": float(height),
            "Weight": float(weight),
            "BMI": float(bmi),
        }

        try:
            response = requests.post(FASTAPI_URL, json=input_data)
            if response.status_code == 200:
                prediction = response.json().get("ObesityCategory", "Unknown")
                flash(f"Prediction: {prediction}", "success") 

                
                user_email = session.get("email")
                if user_email:
                    try:
                        msg = Message("Your Obesity Prediction Result", recipients=[user_email])
                        msg.body = f"Hello,\n\nYour obesity prediction result is: {prediction}\n\nThank you for using our service!"
                        mail.send(msg)
                        flash("Prediction result emailed successfully!", "info")
                    except Exception as e:
                        flash(f"Failed to send email: {str(e)}", "danger")
                else:
                    flash("Error: No email found for the logged-in user.", "danger")
            else:
                flash("Error: Could not get prediction.", "danger")
        except Exception as e:
            flash(f"Request failed: {str(e)}", "danger")
            return redirect(url_for('obesity_predict'))
    return render_template("obesity_predict.html", form=form, prediction=prediction)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please log in.', 'danger')
            return redirect(url_for('login'))
        if form.password.data != form.confirm_password.data:
            flash('Passwords do not match. Please try again.', 'danger')
            return redirect(url_for('register'))
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')


        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login')) 

    return render_template('register.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):  
            session['email'] = user.email  
            flash('You were successfully logged in', 'success')
            return redirect(url_for('predictions'))  
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    return redirect(url_for('main_page'))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
