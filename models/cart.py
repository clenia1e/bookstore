from database import db_session

class CartModel(db_session.Model):
    __tablename__ = 'cart'

    id = db_session.Column(db_session.Integer, primary_key=True)
    book_id = db_session.Column(db_session.Integer())

    def __init__(self, book_id):
        self.book_id = book_id

    def __repr__(self):
        return f"<ID {self.book_id}>"
