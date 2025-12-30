from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asupersecretivekey'

from app.form import form_bp

app.register_blueprint(form_bp)

from app.calendar import cal_bp

app.register_blueprint(cal_bp)

from app.datatable import table_bp

app.register_blueprint(table_bp)


@app.route('/')
def home():
    return render_template('index.html')