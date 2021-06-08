from database import db_session

class CategoryModel(db_session.Model):
    __tablename__ = 'category'
    
    id = db_session.Column(db_session.Integer, primary_key=True)
    name = db_session.Column(db_session.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Category name {self.name}>"