from flask import Flask, render_template
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('myapp_req.html')


@app.route('/login', methods=['post'])
def login():
    id = request.form.get('id')

    return render_template('myapp_res.html', myid=id)


if __name__ == '__main__':
    app.run()
