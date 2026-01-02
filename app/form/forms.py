import datetime

from flask_wtf import FlaskForm
from wtforms_alchemy import model_form_factory
from wtforms import StringField, EmailField, FormField, FieldList, DateField, SubmitField, Field, SelectField
from wtforms.widgets import TextInput
from wtforms_alchemy import QuerySelectField

from app import db
from app.form.models import Province, District, Tambon

BaseModelForm = model_form_factory(FlaskForm)

class ModelForm(BaseModelForm):
    @classmethod
    def get_session(self):
        return db.session


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


class DateForm(FlaskForm):
    date = DatePickerField('Date')


class ReservationForm(FlaskForm):
    dates = FieldList(FormField(DateForm), min_entries=1)
    submit = SubmitField('Submit')


class DynamicDropdownForm(FlaskForm):
    province = SelectField('Province')
    district = SelectField('District')
    tambon = SelectField('Tambon')


class DynamicDropdownQuerySelectForm(ModelForm):
    province = QuerySelectField('Province', query_factory=lambda: Province.query.all())
    district = QuerySelectField('District', query_factory=lambda: District.query.all())
    tambon = QuerySelectField('Tambon', query_factory=lambda: Tambon.query.all())