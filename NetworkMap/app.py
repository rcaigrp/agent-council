from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/todos', methods=['GET', 'POST'])
def get_todos():
    if request.method == 'GET':
        # TODO: Implement fetching todos from a database or file
        todos = []
        return jsonify(todos),
    elif request.method == 'POST':
        # TODO: Implement creating a new todo
        pass

if __name__ == '__main__':
    app.run(debug=True)