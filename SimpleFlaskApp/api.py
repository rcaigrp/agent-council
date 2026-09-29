import flask

app = flask.Flask(__name__)

@app.route('/hello', methods=['GET']) 
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)