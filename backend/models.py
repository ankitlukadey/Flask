from backend.__init import db
import datetime
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)
    time=db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
       return f"<User {self.title},{self.id}{self.complete},{self.time}>"
   