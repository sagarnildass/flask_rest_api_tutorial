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
        item.insert()
        #try:
        #    item.insert()
        #except:
        #    return {"message":"An error occurred while inserting the item!"}, 500 #internal server error

        return item.json(), 201


    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {'message':'Item deleted!'}

    #for updating or creating
    def put(self, name):

        #data = request.get_json()
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message":"An error occurred while inserting the item!"}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message":"An error occurred while updating the item!"}, 500
        return updated_item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []

        for row in result:
            items.append({'name':row[0], 'price':row[1]})

        connection.close()

        return {'items':items}
