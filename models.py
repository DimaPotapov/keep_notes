from sqlalchemy import Column, Integer, String
from __init__ import db
class User(db.Model):
    id = Column(Integer, primary_key=True)
    login = Column(String(50), unique=True)
    password = Column(String(120))

    def __init__(self, login=None, password=None):
        self.login = login
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.login)