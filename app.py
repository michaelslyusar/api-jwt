from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from db import db

from security import authenticate, identity
from resources.user import UserRegister,User,UserList
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = "mike"
api = Api(app)


jwt = JWT(app,authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User,'/user/<int:user_id>')
api.add_resource(UserList,'/users')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port = 5000, debug=True)