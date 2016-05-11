#coding=utf8
from app import app,db
from flask import render_template,flash, redirect,request
#引入定义的表类
import address_print_form
#引入add表
from order_form import order_form
from models import Goods,Purchase_order,Purchase_list
import datetime
import address_split

@app.route('/')
@app.route('/index')
def index():
    user={'nickname':'Yin lijun'}
    return render_template("index.html",title='Yin',user=user)

@app.route('/print',methods=['GET','POST'])
def print_address():
    form = address_print_form.Address_Print_form()
    if form.validate_on_submit():
        #flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return render_template("address_print.html", title=u"圆通快递单打印",
                               post_message=address_split.addSpilt(form.post_message.data),
                               receive_message=address_split.addSpilt(form.receive_message.data),
                               print_date=datetime.datetime.now().strftime('%Y-%m-%d %X'),
                               order_message=form.order_message.data,
                               express_chose=form.express.data)
    return render_template('address_print_form.html',
        title = 'Order Print',
        form = form)
        
@app.route('/add',methods=['GET','POST'])
def addOrder():
    addform=order_form()
    if addform.validate_on_submit():
        goods_count=int(request.form.get("goods_count"))
        goods_name=request.form.getlist("goods_name")
        dahao=request.form.get("danhao")
        riqi=request.form.get("chose_date")
        goods_quantity=request.form.getlist("goods_quantity")
        sum_order=0
        for i in range(len(goods_name)):
            good_model=Goods.query.filter_by(good_name=goods_name[i]).first()
            list=Purchase_list(
                order_num=dahao,
                good_name=goods_name[i],
                good_quantity=int(goods_quantity[i]),
                good_sum=int(goods_quantity[i])*good_model.cost_price
            )
            good_model.good_quantity+=list.good_quantity
            db.session.add(list)
            
            sum_order+=list.good_sum
        db.session.add(good_model)
        print sum_order
        if sum([int(i) for i in goods_quantity])==goods_count:
            print "IT's same!!!"
        else:
            print "it not same!!"
            goods_count=sum([int(i) for i in goods_quantity])
        ord=Purchase_order(
            order_num=dahao,
            order_date=datetime.datetime.strptime(riqi, "%Y-%m-%d").date(),
            order_sum=sum_order,
            order_quantity=goods_count,
            order_memo='',
        )
        db.session.add(ord)
        db.session.commit()
        redirect("/add")
    return render_template("add.html",form=addform,title="addorder",order_date=datetime.datetime.now().strftime('%Y-%m-%d'))

@app.route('/show/<dbname>')
def order_show(dbname):
    if dbname=="good":
        return render_template("show_good.html",goods=Goods.query.all())
    elif dbname=="order":
        orders=Purchase_order.query.order_by(Purchase_order.order_date).all()
        acount_count=0
        quantity_count=0
        for item in orders:
            acount_count+=item.order_sum
            quantity_count+=item.order_quantity
        return render_template("show_order.html",orders=orders,acount_count=acount_count,quantity_count=quantity_count)
    elif dbname=="search":
        good=Goods.query.first()
        print good
        num=good.prrchase_good
        for i in num:
            print i.good_quantity
        return redirect('/show')

@app.route('/show/order/<order_num_get>')
def show_order_detail(order_num_get):
    order=Purchase_order.query.filter_by(order_num=order_num_get).first()
    good=Purchase_list.query.filter_by(order_num=order_num_get).all()
    return render_template("show_order_details.html",good=good,order=order)        