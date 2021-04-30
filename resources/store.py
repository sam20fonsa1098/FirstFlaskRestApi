from models.store import Store
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This field can not be left blank!")

    @jwt_required()
    def get(self, name):
        store = Store.find_by_name(name)
        return store.json(), 200 if store else {'error': True, 'message': f'Not found Store with name {name}'}, 404

    @jwt_required()
    def post(self):
        data = self.parser.parse_args()
        store = Store.find_by_name(**data)
        if store:
            return {'error': True, 'message': f'Store already exists'}, 400
        store = Store(**data)
        store.save()
        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = Store.find_by_name(name)
        if store:
            store.delete()
        return {'success': True, 'message': 'Item deleted'}, 200
