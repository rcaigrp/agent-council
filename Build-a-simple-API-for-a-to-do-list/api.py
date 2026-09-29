from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(120), nullable=False)
        completed = db.Column(db.Boolean, default=False)

        def to_dict(self):
            return {"id": self.id, "title": self.title, "completed": self.completed}

    @app.before_first_request
    def create_tables():
        db.create_all()

    @app.route('/tasks', methods=['POST'])
    def create_task():
        if not request.json or 'title' not in request.json:
            abort(400)
        title = request.json['title']
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([t.to_dict() for t in tasks])

    @app.route('/tasks/<int:task_id>', methods=['GET'])
    def get_task(task_id):
        task = Task.query.get_or_404(task_id)
        return jsonify(task.to_dict())

    @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(task_id):
        task = Task.query.get_or_404(task_id)
        data = request.json or {}
        if 'title' in data:
            task.title = data['title']
        if 'completed' in data:
            task.completed = bool(data['completed'])
        db.session.commit()
        return jsonify(task.to_dict())

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

    # expose db for tests
    app.db = db
    return app
