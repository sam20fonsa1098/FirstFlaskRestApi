from data.db import db


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('Store')

    def __init__(self, name: str, price: str, store_id: str) -> None:
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self) -> dict:
        return {'name': self.name, 'price': self.price}

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name: str) -> 'Item':
        return cls.query.filter_by(name=name).first()

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()
