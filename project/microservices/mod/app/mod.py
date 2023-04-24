from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class mod(Resource):
    def get(self, x, y):
    	return int(x) % int(y)

api.add_resource(mod, '/mod/<x>/<y>')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5055)