#_*_ coding=utf-8 _*_
from app import app

class Goods(db.Model):
    __tablename__="goods"
    id=db.Column(db.Integer,priary_key=True)
    name=db.Column(db.String(64),unique=True)
    
    def __repr__(self):
        return '<Good %r>' % self.name
