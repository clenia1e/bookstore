from database import db_session


class BooksModel(db_session.Model):
    __tablename__ = 'books'

    id = db_session.Column(db_session.Integer, primary_key=True)
    name = db_session.Column(db_session.String())
    price = db_session.Column(db_session.Integer())
    category_id = db_session.Column(db_session.Integer())

    def __init__(self, name, price, category_id):
        self.name = name
        self.price = price
        self.category_id = category_id


    def __repr__(self):
        return f"<Book {self.name}>"
