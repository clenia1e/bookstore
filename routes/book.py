from models.books import BooksModel
from database import db_session
from flask import make_response, request
import json
from models.category import CategoryModel
from sqlalchemy.orm.exc import NoResultFound as NotFound


def _response(data, code):
    return make_response(json.dumps(data, ensure_ascii=False), code)


def init_app(app):
    @app.route('/books', methods=['GET'])
    def get_books():
        books = BooksModel.query.all()
        results = dict(count=len(books), books=[{"name": book.name,
                                                 "price": book.price,
                                                 "category_id": book.category_id}
                                                for book in books])
        return _response(results, 200)

    @app.route('/books', methods=['POST'])
    def create_book():
        data = request.get_json()
        new_book = BooksModel(
            name=data['name'], price=data['price'], category_id=data['category_id'])
        db_session.session.add(new_book)
        db_session.session.commit()

        return _response({"messege": f"Book {new_book} has been added."}, 200)

    @app.route('/books/<book_id>', methods=['GET'])
    def get_book(book_id):
        try:
            book = BooksModel.query.get_or_404(book_id)
            return _response(book.to_dict(), 200)
        except NotFound:
            return _response({"message": "This book wasn't founded"}, 404)

    @app.route('/books/<book_id>', methods=['PUT'])
    def update_book(book_id):
        try:
            book = BooksModel.query.filter_by(id=book_id)
            data = request.get_json()
            book.update(dict(data))
            db_session.session.commit()
            return _response({"message": f"Book {book.first().name} successfully updated"}, 200)
        except NotFound:
            return _response({"message": "Book wasn't founded"}, 404)

    @app.route('/books/<book_id>', methods=['DELETE'])
    def delete_book(book_id):
        try:
            book = BooksModel.query.get_or_404(book_id)
            db_session.session.delete(book)
            return _response({"message": f"Book {book.name} successfully deleted."}, 200)
        except NotFound:
            return _response({"message": "Book wasn't founded"}, 404)