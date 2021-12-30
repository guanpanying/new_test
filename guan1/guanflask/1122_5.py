from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    url_str = 'www.baidu.com'
    my_list = [1, 2, 3, 4]
    my_dict = {'a': 1, 'b': 'abc'}
    return render_template('11224.html', url_str=url_str, my_list=my_list, my_dict=my_dict)


if __name__ == '__main__':
    app.run(debug=True)
