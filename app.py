from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class Helloworld(Resource):
    def get(self):
        return{"Hello": "성규"}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8989)
