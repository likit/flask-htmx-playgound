import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, FormField, FieldList, DateField, SubmitField, Field, SelectField
from wtforms.widgets import TextInput


class EmailForm(FlaskForm):
    email = EmailField('Email', render_kw={'class': 'input'})


class AddressForm(FlaskForm):
    province = SelectField('Province', choices=[(c, c) for c in ['กทม.', 'นนทบุรี', 'นครปฐม']])


class UserForm(FlaskForm):
    name = StringField('Name')
    emails = FieldList(FormField(EmailForm), min_entries=1)
    addresses = FieldList(FormField(AddressForm), min_entries=1)


class DatePickerField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return self.data.strftime('%d/%m/%Y')
        else:
            return ''

    def process_formdata(self, value):
        if value[0]:
            self.data = datetime.datetime.strptime(value[0], '%d/%m/%Y')
        else:
            self.data = None


class AppointmentForm(FlaskForm):
    purchase_date = DatePickerField('Purchase Date')
    start_date = DatePickerField('Start Guarantee Date')
    end_date = DatePickerField('End Guarantee Date')
    submit = SubmitField('Send')