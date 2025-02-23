from flask import Flask, url_for, redirect, render_template, request, flash, session
from flask_session import Session
from flask_wtf import CSRFProtect
from forms import ObesityPredictionForm, RegistrationForm, LoginForm
import redis
import requests
from flask_mysqldb import MySQL



app = Flask(__name__)

# FastAPI Endpoint
FASTAPI_URL = "http://127.0.0.1:8000/predict/"

# Session Configuration
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'flask_session:'
app.config['SESSION_REDIS'] = redis.Redis(host='localhost', port=6379, db=0)

Session(app)
app.config['SECRET_KEY'] = '86cf016117fc3c20024cbece2419d4ce'


#DB configurations
app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='K3v!n254'
app.config['MYSQL_DB']='Health'



mysql=MySQL(app)


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
                    flash(f"Prediction: {prediction}", "success")  # Flash message for pop-up
            else:
                flash("Error: Could not get prediction.", "danger")
        except Exception as e:
            flash(f"Request failed: {str(e)}", "danger")
            
    return render_template("obesity_predict.html",form=form, prediction=prediction)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if form.validate_on_submit():
        if form.Email.data != 'konyomba@gmail.com' or form.password.data != '1234':
            error = 'Invalid credentials'
            flash('Invalid credentials', 'danger')
        else:
            flash('You were successfully logged in', 'success')
            return redirect(url_for('predictions'))
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True, port=5000,host='192.168.100.4')
