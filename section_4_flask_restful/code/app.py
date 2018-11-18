from flask import Flask, request
from flask_restful import Resource, Api, reqparse #reqparse allows us to limit parsing to only certain elements of the payload. See the put method
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
#This should be private
app.secret_key = 'sagar'
api = Api(app)

#jwt object with functions we defined in security.py. JWT creates a new endpoint /auth
jwt = JWT(app, authenticate, identity)

items = []

#Every resource has to be a class. We no longer need to do jsonify when working with flask restful
class Item(Resource):
    parser = reqparse.RequestParser()
    #This will make the parser only see 'price' and ignore others.
    parser.add_argument('price',
            type=float,
            required=True,
            help='This field cannot be left blank.'
            )

    @jwt_required()
    def get(self, name):
        #applying the filter function. next gives the first item found by the filter function. That's ok as we only will have one match
        #If the next does not find anything, it will return None as we exception handled it
        item = next(filter(lambda x: x['name'] == name, items), None)
        #adding http status 404 - not found
        return {'item':item}, 200 if item else 404

    def post(self, name):
        #adding exception handling if someone wants to add an item which already exists
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message':'An item with name {} already exists!'.format(name)}, 400
        #otherwise put the item
        #data = request.get_json()

        data = Item.parser.parse_args()
        #this price comes from postmaster setting - 15.99
        item = {'name':name, 'price':data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        #we are defining this because otherwise python will think, that it's some local variable we are defining
        global items
        #if we wouldn't have defined the global var, python would have thrown an error 'local' referenced before assignment
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message':'Item deleted!'}

    #for updating or creating
    def put(self, name):

        #data = request.get_json()
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price':data['price']}
            items.append(item)
        else:
            #dict objects has an update method. But here, if the payload consists of name too, that will
            #also get updated. That's why we will use reqparse
            item.update(data)
        return item

class ItemList(Resource):
    def get(self):
        return {'items':items}


#make this Student resource accessible via the Api. Also we don't route like before, we set the endpoint here.
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

#run the app, debug=True gives nice error messages
app.run(port=5000, debug=True)
