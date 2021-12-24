from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, PasswordField
from wtforms.fields import DateField
class Registration(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    password = PasswordField('Password', [validators.length(min=7, max=150),validators.DataRequired()])

class CreateOrderForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])