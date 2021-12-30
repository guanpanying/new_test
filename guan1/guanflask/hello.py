import sys

sys.path.append('/Users/guanpy/Desktop/guan1/venv/lib/python3.8/site-packages')
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库的地址,指到my_data数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@123.57.221.39/my_data'

# 跟踪数据库的修改--不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

'''
配置数据库
添加书和作者模型
添加数据
使用模板显示数据库的数据
使用WTF显示表单
实现逻辑
'''


# 数据库模型，需要继承db.Model
class Author(db.Model):
    # 定义表名
    __tablename__ = 'authors'

    # 定义字段,db.Column表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 外键，db.ForeignKey('roles.id') 表名.字段名

    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Book: %s %s' % (self.name, self.author_id)


@app.route('/')
def index():
    # 查询所有的作者信息，将信息传递给模板
    authors1 = Author.query.all()

    return render_template('shizhan.html', authors=authors1)


if __name__ == '__main__':
    # 删除表
    db.drop_all()

    # 创建表
    db.create_all()
    use1 = Author(name='guan')
    user2 = Author(name='pan')
    db.session.add_all([use1, user2])
    db.session.commit()

    book1 = Book(name='python入门', author_id=use1.id)
    book2 = Book(name='flask入门', author_id=use1.id)
    db.session.add_all([book1, book2])
    db.session.commit()

    app.run(debug=True)
