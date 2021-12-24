from flask_uploads import UploadSet, IMAGES
from wtforms import Form, TextAreaField, StringField
from wtforms.fields.core import DateField, IntegerField,FloatField,DateField
#StringField, RadioField, SelectField, validators
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

photos = UploadSet('photos', IMAGES)

class UpdateProductForm(Form):
    product_image = FileField('Product Image',validators=[FileRequired()])
    produt_name = StringField('Product Name', validators=[DataRequired()])
    product_category = StringField('Product Category', validators=[DataRequired()])
    product_price= FloatField('Product Price', validators=[DataRequired()])
    product_description= TextAreaField('Product Description', validators=[DataRequired()])
    product_stock= IntegerField('Product Stock', validators=[DataRequired()])
    create_time = DateField('Date Joined', format='%Y-%m-%d')

#Form object – Used to create a WTForms Form.
#StringField object – Used to create an HTML textfield.
#RadioField object – Used to create an HTML radio button group.
#SelectField object – Used to create an HTML dropdown list.
#TextAreaField object – Used to create an HTML textarea.
#validators object – validators allow you to specify the constraints for each of the fields such as minimum and maximum length, DataRequried or Optional.

