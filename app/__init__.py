# -*- coding: utf-8 -*-
# 防止文件中有中文出现乱码现象
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from flask import Flask

app = Flask(__name__)
#全局秘钥
CSRF_ENABLED = True
app.config['SECRET_KEY'] = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:nettuts@localhost/bbs'

# 载入数据库
from models import db
db.init_app(app)

import views

#主程序控制 与 数据库迁移与更新工具
from flask.ext.script import Manager
from flask.ext.migrate import Migrate
migrate = Migrate(app, db)
manager = Manager(app)
from flask.ext.migrate import MigrateCommand
manager.add_command('db', MigrateCommand)
