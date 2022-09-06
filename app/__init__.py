from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asupersecretivekey'
app.config['DEBUG'] = True

from app.form import form_bp

app.register_blueprint(form_bp)
