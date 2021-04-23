# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):

        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):

        data = request.get_json()     # status code
        return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class Square(Resource):
    #parthKurani, nathanRego, admin*
    def get(self, str):
        if (str == "76cea6bba3bbbf77c82519ed1b1c804a00137e30592f37b36085e0deeb0eb752" or str == "a4e092cff81f5dba7babfbc05a7495c367df6ee88f1e202fa6459e3aa591174e" or str == "e340d13874054b103f74f42bfefda69de32cf22789d8897f17647d85bd20d809"):
            return True
        else:
            return False

# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<string:str>')


# driver function
if __name__ == '__main__':

    app.run(debug = True)
