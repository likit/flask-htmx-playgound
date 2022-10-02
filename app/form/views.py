from flask import render_template, request, make_response

from app.form import form_bp
from app.form.forms import UserForm, AppointmentForm

users = []

@form_bp.route('/field-list')
def demo_field_list():
    form = UserForm()
    if form.validate_on_submit():
        return 'Done'
    return render_template('form/field_list.html', form=form)


@form_bp.route('/field-list/add-email', methods=['POST'])
def demo_field_list_add_email():
    form = UserForm()
    form.emails.append_entry()
    email_form = form.emails[-1]
    return '''
    <div class="field">
        <label>{}</label>
        <div class="control">
        {}
        </div>
    </div>
    '''.format(email_form.label, email_form.email())


@form_bp.route('/modal1')
def demo_form_modal():
    form = UserForm()
    return render_template('form/form_modal1.html', form=form)


@form_bp.route('/modal1_template')
def get_modal1_template():
    return render_template('form/modal1.html')


@form_bp.route('/modal2_template')
def get_modal2_template():
    form = UserForm()
    return render_template('form/modal2.html', form=form)


@form_bp.route('/modal2/process', methods=['GET', 'POST'])
def modal2_form():
    form = UserForm()
    if request.method == 'GET':
        return render_template('form/form_modal2.html')
    if form.validate_on_submit():
        resp = make_response('''
        <tr>
            <td>{}</td><td>{}</td>
        </tr>
        '''.format(form.name.data, form.emails[0].email.data)
        )
        resp.headers['HX-Trigger-After-Swap'] = 'closeModal'
        return resp


@form_bp.route('/datepicker1', methods=['GET', 'POST'])
def datepicker_form1():
    form = AppointmentForm()
    if form.validate_on_submit():
        print(form.data)
    else:
        print(form.errors)
    return render_template('form/datepicker1.html', form=form)
