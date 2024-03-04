from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class WikiModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)
    views = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Article(name = {name}, views = {views})"

article_put_args = reqparse.RequestParser()
article_put_args.add_argument(
    "subject", type=str, help="Subject of article is required", required=True)
article_put_args.add_argument("views", type=int, help="Views of article")

resource_fields = {
    'id': fields.Integer,
    'subject': fields.String,
    'views': fields.Integer 
}

article_patch_args = reqparse.RequestParser()
article_patch_args.add_argument(
    "subject", type=str, help="Subject of article is required")
article_patch_args.add_argument("views", type=int, help="Views of article")

class Wiki(Resource):
    @marshal_with(resource_fields)
    def get(self, article_id):
        result = WikiModel.query.filter_by(id=article_id).first()
        if not result: 
            abort(404, message="Article with that ID does not exist")
        return result

    @marshal_with(resource_fields)
    def put(self, article_id):
        args = article_put_args.parse_args()
        result = WikiModel.query.filter_by(id=article_id).first()
        if result:
            abort(409, message="Article id exists")
        article = WikiModel(id=article_id, subject=args['subject'], views=args['views'])
        db.session.add(article)
        db.session.commit()
        return article, 201

    @marshal_with(resource_fields)
    def patch(self, article_id): 
        args = article_patch_args.parse_args()
        result = WikiModel.query.filter_by(id=article_id).first()
        if not result:
            abort(404, message="Artcle id does not exist")
        for key in args.keys():
            if args[key]:
                setattr(result, key, args[key])
        db.session.commit()
    
    def delete(self, article_id):
        return '', 204


api.add_resource(Wiki, "/wiki/<int:article_id>")


if __name__ == "__main__":
    app.run(debug=True)
