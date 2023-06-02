from flask import Flask,render_template

root=Flask(__name__,template_folder='templates',static_folder='static')


@root.route('/')


def index():
    return render_template('index.html')


if __name__ =='__main__':
    root.run(host="127.0.0.1", port=52100,  threaded=True)