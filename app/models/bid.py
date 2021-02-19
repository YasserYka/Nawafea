from app.extensions import db

class Bid(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(255), nullable=False)
    auction_id = db.Column(db.Integer, db.ForeignKey('auction.id'))

    def __init__(self, date, message):
        self.date = date
        self.message = message

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
            'date': self.date,
            'message': self.message,
            'auction_id': self.auction_id,
        }
