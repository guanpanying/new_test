# 1。导入flask扩展

from flask import Flask

# 2。创建flask应用程序实例
# 需要传入__name__，作用是为了确定资源所在的路径
app = Flask(__name__)


# 3。定义路由及视图函数
# Flask中定义路由是通过装饰器实现的
@app.route('/')
def index():
    return 'hello guan!!!!!'


# 4.启动程序
if __name__ == '__main__':
    app.run(debug=True)
