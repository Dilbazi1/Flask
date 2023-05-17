from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField,validators,SubmitField,TextAreaField


class CreateArticleForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    text = TextAreaField('Text', [validators.DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    submit = SubmitField('Create')