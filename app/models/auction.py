from app.extensions import db
from datetime import datetime

class Auction(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    initial_bid = db.Column(db.Float())
    bids = db.relationship("Bid", backref=db.backref('auction', lazy=True))
    end_date = db.Column(db.DateTime(), nullable=False)
    opened = db.Column(db.Boolean, default=True, nullable=False)
    products = db.relationship("Product", backref=db.backref('auction', lazy=True))
    description = db.Column(db.String(255), nullable=True)
    title = db.Column(db.String(255), nullable=True)

    def __init__(self, initial_bid, end_date, description, title):
        self.initial_bid = initial_bid
        self.end_date = end_date
        self.description = description
        self.title = title

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
            'initial_bid': self.initial_bid,
            'bids': [bid.json() for bid in self.bids],
            'end_date': self.end_date,
            'opened': self.opened,
            'products': [product.json() for product in self.products],
            'title': self.title,
            'description': self.description
        }
