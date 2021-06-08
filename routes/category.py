from models.category import CategoryModel
from database import db_session
from flask import make_response, request
import json
from sqlalchemy.orm.exc import NoResultFound as NotFound



def _response(data, code):
    return make_response(json.dumps(data, ensure_ascii=False), code)


def init_app(app):
    @app.route('/category', methods=['POST'])
    def create_category():
        data = request.get_json()
        new_category = CategoryModel(name=data['name'])
        db_session.session.add(new_category)
        db_session.session.commit()
        return _response({"message": f"Category {new_category.name} has been created successfully."}, 200)

    @app.route('/category', methods=['GET'])
    def get_categories():
        categories = CategoryModel.query.all()
        results = dict(count=len(categories), categories=[{"name": category.name}
                                                for category in categories])
        return _response(results, 200)


    @app.route('/category/<category_id>', methods=['GET'])
    def get_category(category_id):
        try:
            category = CategoryModel.query.get_or_404(category_id)
            return _response(category.to_dict(), 200)
        except NotFound:
            return _response({"message": "This category wasn't founded"}, 404)

    @app.route('/category/<category_id>', methods=['PUT'])
    def update_category(category_id):
        try:
            category = CategoryModel.query.filter_by(id=category_id)
            data = request.get_json()
            category.update(dict(data))
            db_session.session.commit()
            return _response({"message": f"Book {category.first().name} successfully updated"}, 200)
        except NotFound:
            return _response({"message": "Book wasn't founded"}, 404)

    @app.route('/category/<category_id>', methods=['DELETE'])
    def delete_category(category_id):
        try:
            category = CategoryModel.query.get_or_404(category_id)
            db_session.session.delete(category)
            return _response({"message": f"category {category.name} successfully deleted."}, 200)
        except NotFound:
            return _response({"message": "category wasn't founded"}, 404)