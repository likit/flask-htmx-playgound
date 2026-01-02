from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asupersecretivekey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


from app.form import form_bp
app.register_blueprint(form_bp)

from app.calendar import cal_bp

app.register_blueprint(cal_bp)

from app.datatable import table_bp

app.register_blueprint(table_bp)


from app.form.models import *
from app.form.views import dropdown_items

with app.app_context():
    db.create_all()
    for province_name in dropdown_items['provinces'].keys():
        province = Province(name=province_name)
        db.session.add(province)
        for district_name in dropdown_items['provinces'][province_name]:
            district = District(name=district_name, province=province)
            db.session.add(district)
            for tambon_name in dropdown_items['districts'][district_name]:
                db.session.add(Tambon(name=tambon_name, district=district))
        db.session.commit()


@app.route('/')
def home():
    return render_template('index.html')