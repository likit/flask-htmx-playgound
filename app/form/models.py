from app import db


class Province(db.Model):
    __tablename__ = 'provinces'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __str__(self):
        return self.name


class District(db.Model):
    __tablename__ = 'districts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    province_id = db.Column(db.Integer, db.ForeignKey('provinces.id'))
    province = db.relationship(Province, backref=db.backref('districts'))

    def __str__(self):
        return self.name

class Tambon(db.Model):
    __tablename__ = 'tambons'
    id = db.Column(db.Integer, primary_key=True)
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id'))
    name = db.Column(db.String)
    zipcode = db.Column(db.String)
    district = db.relationship(District, backref=db.backref('tambons'))

    def __str__(self):
        return self.name
