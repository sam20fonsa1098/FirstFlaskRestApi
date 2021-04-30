from flask_restful import Resource, reqparse
from models.user import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field can not be left blank!")
    parser.add_argument('password', type=str, required=True, help="This field can not be left blank!")

    def post(self):
        data = self.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'error': True, 'message': 'User already exists'}, 400
        user = User(**data)
        user.save()
        return {'success': True, 'message': 'User created'}, 201
