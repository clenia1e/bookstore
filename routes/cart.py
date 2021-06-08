from models.cart import CartModel
from flask import make_response
import json
from database import db_session
from models.books import BooksModel
from sqlalchemy.orm.exc import NoResultFound as NotFound



def _response(data, code):
    return make_response(json.dumps(data, ensure_ascii=False), code)


def init_app(app):
    @app.route('/cart/<book_id>', methods=['POST'])
    def post_cart(book_id):
        print(book_id)
        book = BooksModel.query.get_or_404(book_id)
        new_item = CartModel(book_id=book.id)
        db_session.session.add(new_item)
        db_session.session.commit()

        return _response(f"{book.name} added to the cart", 200)

    @app.route('/cart', methods=['GET'])
    def get_carts():
        cart = CartModel.query.all()
        results = dict(count=len(cart), categories=[{"name": cart.name}
                                                for category in cart])
        return _response(results, 200)

    @app.route('/cart/<cart_id>', methods=['DELETE'])
    def delete_cart(cart_id):
        try:
            cart = CartModel.query.get_or_404(cart_id)
            db_session.session.delete(cart)
            return _response({"message": f"Item successfully deleted."}, 200)
        except NotFound:
            return _response({"message": "Item wasn't founded"}, 404)
