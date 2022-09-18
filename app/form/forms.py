from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, FormField, FieldList


class EmailForm(FlaskForm):
    email = EmailField('Email', render_kw={'class': 'input'})


class UserForm(FlaskForm):
    name = StringField('Name')
    emails = FieldList(FormField(EmailForm), min_entries=1)