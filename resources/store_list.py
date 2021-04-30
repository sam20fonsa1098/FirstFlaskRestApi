from models.store import Store
from flask_restful import Resource
from flask_jwt import jwt_required


class StoreList(Resource):
    @jwt_required()
    def get(self):
        stores = list(map(lambda x: x.json(), Store.query.all()))
        return stores, 200
