from flask_restful import Resource
from flask_jwt import jwt_required
from models.item import Item


class ItemList(Resource):
    @jwt_required()
    def get(self):
        items = list(map(lambda x: x.json(), Item.query.all()))
        return items, 200
