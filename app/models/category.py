from app.extensions import db

class Category(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __init__(self, username, avatar_url, github_id):
        self.username = username
        self.avatar_url = avatar_url

    def json(self):
        
        return {
            'id': self.id,
            'name': self.name,
        }
