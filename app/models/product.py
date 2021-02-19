from app.extensions import db
from .auction import Auction

class Product(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)
    imagename = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float(), nullable=True)
    auction_id = db.Column(db.Integer, db.ForeignKey('auction.id'))
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchase.id'))
    sold = db.Column(db.Boolean(), default=False, nullable=False)

    def __init__(self, name, description, price, image=None, imagename=None):
        self.name = name
        self.image = image
        self.imagename = imagename
        self.description = description
        self.price = price

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
            'name': self.name,
            'imagename': self.imagename,
            'description': self.description,
            'price': self.price,
        }