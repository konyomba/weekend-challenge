from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,IntegerField,FloatField
from wtforms.validators import DataRequired,Length,Email,EqualTo,NumberRange

class RegistrationForm(FlaskForm):
    username= StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password',message='password must match')])
    submit=SubmitField('Sign Up')


class LoginForm(FlaskForm):
    
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login Up')

class ObesityPredictionForm(FlaskForm):
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1, max=120)])
    height = FloatField('Height (m)', validators=[DataRequired(), NumberRange(min=1)])
    weight = FloatField('Weight (kg)', validators=[DataRequired(), NumberRange(min=1)])
    bmi = FloatField('BMI', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Predict')