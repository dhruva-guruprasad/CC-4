from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Multiply(Resource):
    def get(self, x, y):
        return float(x) * float(y)

api.add_resource(Multiply, '/multiply/<x>/<y>')

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5053)