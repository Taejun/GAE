from google.appengine.ext import db


class Board(db.Model):
    subject = db.StringProperty()
    content = db.StringProperty(indexed=False)
    date = db.DateTimeProperty(auto_now_add=True)
    
    