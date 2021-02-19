from app.extensions import db

class Purchase(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    total = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.String(80), nullable=True)
    paid = db.Column(db.Boolean(), default=False ,nullable=True)
    rating = db.Column(db.Float(), nullable=True)
    comment = db.Column(db.String(255), nullable=True)
    products = db.relationship("Product", backref=db.backref('purchase', lazy=True))

    def __init__(self, date):
        self.date = date
        self.total = 0

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def json(self):
        
        return {
            'id': self.id,
            'total': self.total,
            'date': self.date,
            'paid': self.paid,
            'rating': self.rating,
            'comment': self.comment,
            'products': [product.json() for product in self.products]
        }
