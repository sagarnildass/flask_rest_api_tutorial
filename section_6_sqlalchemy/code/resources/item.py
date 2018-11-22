import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

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
        item = ItemModel.find_by_name(name)
        if item:
            #because now it returns an item object
            return item.json()
        return {'message':'Item not found!'}, 404



    def post(self, name):
        #adding exception handling if someone wants to add an item which already exists
        if ItemModel.find_by_name(name):
            return {'message':'An item with name {} already exists!'.format(name)}, 400
        #otherwise put the item
        #data = request.get_json()

        data = Item.parser.parse_args()
        #this price comes from postmaster setting - 15.99
        item = ItemModel(name, data['price'])
        #item.insert()
        try:
            item.save_to_db()
        except:
            return {"message":"An error occurred while inserting the item!"}, 500 #internal server error

        return item.json(), 201


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message':'Item deleted!'}

    #for updating or creating
    def put(self, name):

        #data = request.get_json()
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
