import time

from flask import render_template, request, make_response, url_for

from app.form import form_bp
from app.form.forms import UserForm, AppointmentForm, ReservationForm

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


@form_bp.route('/field-list2')
def demo_field_list2():
    form = UserForm()
    if form.validate_on_submit():
        return 'Done'
    return render_template('form/field_list2.html', form=form)


@form_bp.route('/field-list/add-address', methods=['POST'])
def demo_field_list_add_address():
    form = UserForm()
    form.addresses.append_entry()
    address_form = form.addresses[-1]
    partial = '''
    <div class="field">
        <label>{}</label>
        <div>
        {}
        </div>
    </div>
    '''.format(address_form.province.label, address_form.province(class_='province'))

    resp = make_response(partial)
    resp.headers['HX-Trigger-After-Swap'] = 'initializeSelector'
    return resp


@form_bp.route('/modal1')
def demo_form_modal():
    form = UserForm()
    return render_template('form/form_modal1.html', form=form)


@form_bp.route('/modal1_template')
def get_modal1_template():
    return render_template('form/modal1.html')


@form_bp.route('/loading')
def loading():
    time.sleep(5)
    resp = make_response()
    resp.headers['HX-Trigger-After-Swap'] = 'closeModal'
    return resp


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


@form_bp.route('/datepicker2', methods=['GET', 'POST'])
def datepicker_form2():
    form = ReservationForm()
    if form.validate_on_submit():
        print(form.data)
    else:
        print(form.errors)
    return render_template('form/datepicker2.html', form=form)


@form_bp.route('/datepicker2/add-date-field', methods=['GET', 'POST'])
def add_reservation_date_form_field():
    form = ReservationForm()
    form.dates.append_entry()
    print(form.dates)
    entry_ = form.dates[-1]
    template = f'''
    <div class="field has-addons" id="{entry_.date.id}-container">
        <label class="label">{entry_.date.label}</label>
        <div class="control is-expanded">
            {entry_.date(class_="input")}
            <p class="help">{entry_.date.id}</p>
        </div>
        <div class="control">
            <button class="button is-danger"
                    hx-confirm="Are you sure?"
                    hx-swap="outerHTML"
                    hx-target="#{entry_.date.id}-container"
                    hx-delete="{url_for('form.remove_reservation_date_form_field', name=entry_.date.name)}">
                Remove
            </button>
        </div>
    </div>
    '''
    print(template)
    resp = make_response(template)
    resp.headers['HX-Trigger-After-Swap'] = 'initDatePicker'
    return resp


@form_bp.route('/datepicker2/remove-date-field/<name>', methods=['DELETE'])
def remove_reservation_date_form_field(name):
    form = ReservationForm(request.form)
    entries = []
    for i in range(len(form.dates)):
        e = form.dates.pop_entry()
        entries.append(e)
    entries.reverse()
    for e in entries:
        if e.name != name:
            form.dates.append_entry(e)
    return ''


@form_bp.route('/selectjs-new-item')
def selectjs_new_item():
    return render_template('form/selectjs-new-item.html')