from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)


article_put_args = reqparse.RequestParser()
article_put_args.add_argument(
    "subject", type=str, help="Subject of article is required", required=True)
article_put_args.add_argument("views", type=int, help="Views of article")

articles = {

}


class Wiki(Resource):
    def get(self, article_id):
        id_not_exists(article_id)
        return articles[article_id]

    def put(self, article_id):
        id_exists(article_id)
        args = article_put_args.parse_args()
        articles[article_id] = args
        return articles[article_id], 201

    def delete(self, article_id):
        id_not_exists(article_id)
        del articles[article_id]
        return '', 204


api.add_resource(Wiki, "/wiki/<int:article_id>")


def id_not_exists(article_id):
    if article_id not in articles:
        abort(404, message="Article id does not exists")


def id_exists(article_id):
    if article_id in articles:
        abort(409, message="Article already exists with that id")


if __name__ == "__main__":
    app.run(debug=True)
