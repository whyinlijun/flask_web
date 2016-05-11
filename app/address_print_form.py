#_*_ coding=utf-8 _*_
from flask.ext.wtf  import Form
from wtforms import StringField, BooleanField,TextAreaField,RadioField
from wtforms.validators import DataRequired

class Address_Print_form(Form):
    express=RadioField(u'快递公司',choices=[
        ('2', u'圆通快递（左右格式）'),
        ('1', u'邮政小包（上下格式)')],
        default='2')
    receive_message = StringField(u'发件人信息：', validators=[DataRequired()])
    post_message = StringField(u'收件人信息：', validators=[DataRequired()])
    order_message = TextAreaField(u'订单信息：')
    #remember_me = BooleanField('remember_me', default=False)