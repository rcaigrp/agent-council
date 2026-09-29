# Build a simple API for a to-do list

**Goal:** Create a RESTful API for managing a to-do list using Flask.

**Status:** Complete

## Endpoints
- `POST /tasks` – Create a new task (JSON `{ "title": "..." }`). Returns 201 with task data.
- `GET /tasks` – Retrieve all tasks.
- `GET /tasks/<id>` – Retrieve a single task.
- `PUT /tasks/<id>` – Update title/completed status.
- `DELETE /tasks/<id>` – Delete a task.

## Running locally
```bash
pip install -r requirements.txt
python -c "from api import create_app; app=create_app(); app.run(debug=True)"
```

## Tests
Run `./run_tests.sh` to execute the pytest suite.

*All tests have passed in the final verification.*