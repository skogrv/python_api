from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Hey(Resource):
    def get(self):
        return {"data": "hey"}
    
api.add_resource(Hey, "/hey")

if __name__ == "__main__":
    app.run(debug=True)
    