from app import db

class Goods(db.Model):
    __tablename__="goods"
    id = db.Column(db.Integer, primary_key=True)
    good_name= db.Column(db.String(20), unique=True)
    retail_price=db.Column(db.Float)
    wholesale_price=db.Column(db.Float)
    cost_price=db.Column(db.Float)
    good_image=db.Column(db.String(200))
    good_quantity=db.Column(db.Integer)
    is_hot=db.Column(db.Boolean)
    verder=db.Column(db.String(20))
    
    prrchase_good=db.relationship("Purchase_list",backref="goods" , lazy="dynamic")

    def __repr__(self):
        return '<Goods %r>' % self.good_name

class Purchase_order(db.Model):
    __tablename__="purchase_order"
    id = db.Column(db.Integer, primary_key=True)
    order_num=db.Column(db.String(15),unique=True)
    order_date=db.Column(db.Date)
    order_sum=db.Column(db.Float)
    order_quantity=db.Column(db.Integer)
    order_memo=db.Column(db.String(200), default="")
    
    prrchase_order_good=db.relationship("Purchase_list",backref="purchase_order" , lazy="dynamic")

    def __repr__(self):
        return '<purchase_order %r>' % self.order_num

class Purchase_list(db.Model):
    __tablename__="purchase_list"
    id = db.Column(db.Integer, primary_key=True)
    order_num=db.Column(db.String(15),db.ForeignKey('purchase_order.order_num'))
    good_name=db.Column(db.String(20),db.ForeignKey('goods.good_name'))
    good_quantity=db.Column(db.Integer)
    good_sum=db.Column(db.Float,default=0)

    def __repr__(self):
        return '<purchase_list %r>' % self.good_name