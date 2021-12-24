from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, PasswordField ,IntegerField,DateTimeField
import datetime
class Registration(Form):
    name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    total = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    status = SelectField('status', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=7, max=150),validators.DataRequired()])

class CreateOrderForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    total = IntegerField('Total', [validators.DataRequired()])
    status = SelectField('Status', [validators.DataRequired()], choices=[('', 'N/A'), ('Delivered', 'Delivered'), ('Not Delivered', 'Not Delivered')], default='')
    date = DateTimeField("Time of creation",[validators.DataRequired()],format="%Y-%m-%dT%H:%M:%S", default=datetime.datetime.now())
        