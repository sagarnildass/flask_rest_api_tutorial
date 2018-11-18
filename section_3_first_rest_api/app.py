#jsonify converts dictionary to string(json) which is easy to send across web
from flask import Flask, jsonify, request, render_template

#creating object of Flask
app = Flask(__name__)

#set the root path
#@app.route('/') #https://www.google.com/ <--- This slash is the homepage
#This has to return a response to our browser
'''
def home():
    return "Hello, World!"

app.run(port=5000)
'''

#When we write http://www.google.com/ - some computer in google is receiving this - GET / HTTP/1.1, Host:www.google.com
#a) GET is the verb - What we want. b) / is the path. c) HTTP/1.1 is the protocol
#Going to a page will always do a GET request. This normally returns a HTML. But we can do others like PUT, POST, DELETE, OPTIONS, HEAD and more

#From the browser's perspective: (From server's perspective, it's just opposite)
#GET - Retrieve something -->  GET /item/1
#POST - Send data and use it --> POST /item,  {'name':'chair', 'price':9.99}
#PUT - Make sure something is there --> PUT /item
#DELETE - delete someting --> DELETE /item/1

#REST API - It is a way of thinking about how a web server responds to our requests.
#It does not respond with just data. It responds with something called resources
#Resources - Similar to OOP. Think of the server as having resources, and each is able to interact with the pertinent request.
#Another key feature of REST is it is supposed to be stateless.This means that one request cannot depend on any other requests.
#So the server only knows about the current request and not any other previous requests.

#From a server's perspective:
#POST - used to receive data
#GET - used to send data back only

@app.route('/')
def home():
    return render_template('index.html')

#starting the list with a single store
stores = [
    {
        "name" : "My wonderful store",
        "items": [
            {
            "name" : "My item",
            "price" : 15.99
            }
        ]
    }
]

#Creating the endpoints
#POST /store data: {name:}
@app.route('/store', methods=['POST']) #by default, it is GET
def create_store():
    #this is the request which was made at /store endpoint
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>') #this name has to match the name passed in the function
def get_store(name):
    #iterate over the get_stores
    #if the store name matches, return that one
    #if none matches, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found!'})

#GET /store
@app.route('/store')
def get_stores():
    #we convert our stores to a dictionary because it is a list as of now and json cannot read list. go to http://127.0.0.1:5000/store
    return jsonify({'stores':stores})

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found!'})

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'item not found!'})

app.run(port=5001)
