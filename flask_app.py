from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_cors import CORS

from config import config

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Test(Resource):
    def get(self):
        return 'Welcome to, Test App API!'

    def post(self):
        try:
            value = request.get_json()
            if(value):
                return {'Post Values': value}, 201

            return {"error":"Invalid format."}

        except Exception as error:
            return {'error': error}

api.add_resource(Test,'/')

if __name__ == "__main__":
    
    app.run(host=config["HOST"], port=int(config["PORT"]))