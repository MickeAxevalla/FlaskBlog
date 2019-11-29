from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Epost",
                        validators=[
                            DataRequired(message="Du måste ange epost"),
                            Email(message="Du måste ange en giltig epost-adress")
                        ])
    password = PasswordField("Lösenord",
                             validators=[
                                 DataRequired(message="Måste vara ifyllt")])