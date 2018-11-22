from flask import Flask
from flask_restful import Api #reqparse allows us to limit parsing to only certain elements of the payload. See the put method
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
#This turns off flask's SQLAlchemy tracker but not SqlAlchemy's tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  False
#telling where the db file resides
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#This should be private
app.secret_key = 'sagar'
api = Api(app)

#jwt object with functions we defined in security.py. JWT creates a new endpoint /auth
jwt = JWT(app, authenticate, identity)


#make this Student resource accessible via the Api. Also we don't route like before, we set the endpoint here.
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

#we write this so that when we import stuffs from app.py to other files,
#we don't run the app. So whatever, we don't wanna run on import goes
#under this __name__ = '__main__' block
if __name__ == '__main__':
    from db import db
    db.init_app(app)
#run the app, debug=True gives nice error messages
    app.run(port=5000, debug=True)
