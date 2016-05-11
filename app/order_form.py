#_*_ coding=utf-8 _*_
from flask.ext.wtf  import Form
from wtforms import StringField, BooleanField,TextAreaField,RadioField,IntegerField,SelectField
from wtforms.validators import DataRequired
from app.models import Goods

class order_form(Form):
    try:
        choices_list=[(good.good_name,good.good_name) for good in Goods.query.order_by(Goods.is_hot.desc()).all()]
    except:
        choices_list=[("error","error")]
    goods = SelectField(u'商品名称：',
                        choices=choices_list)
    quantity = IntegerField(u'商品数量：')
    #remember_me = BooleanField('remember_me', default=False)