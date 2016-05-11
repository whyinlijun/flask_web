#coding=utf-8
import os
#CSRF_ENABLED 配置是为了激活 跨站点请求伪造 保护
CSRF_ENABLED=True
#SECRET_KEY 配置仅仅当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单
SECRET_KEY="Yin-sir-email-whyinlijun@163.com"
#定义数据库路径
basedir=os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(basedir,'data.sqlite')
#定义自动提交为真
SQLALCHEMY_COMMIT_ON_TEARDOWN=True
