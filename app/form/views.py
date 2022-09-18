from flask import render_template, request

from app.form import form_bp
from app.form.forms import UserForm


@form_bp.route('/field-list', methods=['GET', 'POST'])
def demo_field_list():
    action = request.args.get('action')
    form = UserForm()
    if form.validate_on_submit():
        if action == 'add-email':
            form.emails.append_entry()
            return render_template('form/field_list.html', form=form)
        else:
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
