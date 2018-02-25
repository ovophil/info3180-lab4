from flask_wtf.file import FileAllowed, FileRequired, FileField 
from flask_wtf import FlaskForm

class UploadForm(FlaskForm):
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg','png'], 'Images only!')
    ])
    
    