from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Divide(Resource):
    def get(self, x, y):
    	if(y == '0'):
    		return "Division by zero not possible"
    	else:
    		return float(x) / float(y)

api.add_resource(Divide, '/divide/<x>/<y>')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5054)