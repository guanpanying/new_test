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


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    age = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    # 设置relations
    books = db.relationship("Book", backref="students")


# 一对多  书是多   (一个学生有多本书)
class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(200))
    author = db.Column(db.String(200))
    publish = db.Column(db.String(200))
    price = db.Column(db.String(200))
    types = db.Column(db.String(200))
    pages = db.Column(db.String(200))
    s_id = db.Column(db.Integer, db.ForeignKey(Student.id))


@app.route("/home")
def home():
    # 所有的学生
    s_all = Student.query.all()
    return render_template("hh.html", s_all=s_all)
