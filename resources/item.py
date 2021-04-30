from models.item import Item
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field can not be left blank!")
    parser.add_argument('name', type=str, required=True, help="This field can not be left blank!")
    parser.add_argument('store_id', type=str, required=True, help="This field can not be left blank!")

    @jwt_required()
    def get(self, name):
        item = Item.find_by_name(name)
        return item.json(), 200 if item else {'error': True, 'message': 'Not found'}, 404

    @jwt_required()
    def post(self):
        data = self.parser.parse_args()
        item = Item.find_by_name(data['name'])
        if item:
            return {'error': True, 'message': f'Already exists an item with name {data["name"]}'}, 400
        item = Item(**data)
        item.save()
        return item.json(), 201

    @jwt_required()
    def delete(self, name):
        item = Item.find_by_name(name)
        if item:
            item.delete()
        return {'success': True, 'message': "Item deleted"}, 200

    @jwt_required()
    def put(self):
        data = self.parser.parse_args()
        item = Item.find_by_name(data['name'])
        if item is None:
            return {'error': True, 'message': f'Not found item with name {data["name"]}'}, 404
        item.price = data['price']
        item.save()
        return item.json(), 200
