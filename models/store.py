from data.db import db


class Store(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    items = db.relationship('Item', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'name': self.name, 'items': list(map(lambda x: x.json()), self.items.all())}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
