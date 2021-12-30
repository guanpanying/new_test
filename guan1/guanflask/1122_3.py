from flask import Flask

app = Flask(__name__)


@app.route('/orders/<int:order_id>')
def hello_guan(order_id):
    return f'hello itcast {order_id}'


if __name__ == '__main__':
    app.run(debug=True)
